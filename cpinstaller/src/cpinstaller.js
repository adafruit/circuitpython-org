'use strict';
import { html } from 'https://unpkg.com/lit-html?module';
import * as zip from "https://deno.land/x/zipjs/index.js";
import * as esptoolPackage from "https://unpkg.com/esp-web-flasher@5.1.2/dist/web/index.js?module"
import {REPL} from 'https://cdn.jsdelivr.net/gh/adafruit/circuitpython-repl-js@1.0.0/repl.js';
import { InstallButton } from "./base_installer.js";

// TODO: Figure out how to make the Web Serial from ESPTool and Web Serial to communicate with CircuitPython not conflict.
// It may just be easier to reconnect because for chips like the S3 and S2, it's a JTAG connection and there is
// inconsistency among the different chips. We may also be able to attempt to just connect.
// I think at the very least we'll have to reuse the same port so the user doesn't need to reselct, though it's possible it
// may change after reset. Since it's not
//
// For now, we'll use the following procedure for ESP32-S2 and ESP32-S3:
// 1. Install the bin file
// 2. Reset the board
// (if version 8.0.0-beta.6 or later)
// 3. Generate the settings.toml file
// 4. Write the settings.toml to the board via the REPL
// 5. Reset the board again
//
// For the esp32 and esp32c3, the procedure may be slightly different and going through the
// REPL may be required for the settings.toml file.
// 1. Install the bin file
// 2. Reset the board
// (if version 8.0.0-beta.6 or later)
// 3. Generate the settings.toml file
// 4. Write the settings.toml to the board via the REPL
// 5. Reset the board again
//

const PREFERRED_BAUDRATE = 921600;

const CSS_DIALOG_CLASS = "cp-installer-dialog";
const FAMILY_TO_CHIP_MAP = {
    'esp32s2': esptoolPackage.CHIP_FAMILY_ESP32S2,
    'esp32s3': esptoolPackage.CHIP_FAMILY_ESP32S3,
    'esp32c3': esptoolPackage.CHIP_FAMILY_ESP32C3,
    'esp32': esptoolPackage.CHIP_FAMILY_ESP32
}

export class CPInstallButton extends InstallButton {
    constructor() {
        super();
        this.releaseVersion = "[version]";
        this.boardName = "ESP32-based device";
        this.boardId = null;
        this.bootloaderUrl = "";
        this.uf2FileUrl = "";
        this.binFileUrl = "";
        this.releaseVersion = 0;
        this.chipFamily = null;
        this.bootloadId = null;
        this.dialogCssClass = CSS_DIALOG_CLASS;
        this.dialogs = { ...this.dialogs,  ...this.cpDialogs };
        this.bootDriveHandle = null;
        this._bootDriveName = null;
        this.fileCache = [];
        this.init();
    }

    connectedCallback() {
        this.boardName = this.getAttribute("boardname") || "ESP32-based device";

        // If this is empty, it's a problem
        this.boardId = this.getAttribute("boardid");
        this.releaseVersion = this.getAttribute("version");

        // We need either the bootloader and uf2 or bin file to continue
        this.bootloaderUrl = this.getAttribute("bootloader");
        this.bootloaderUrl = this.bootloaderUrl.replace("https://downloads.circuitpython.org/bootloaders/esp32/", "/bin/");
        this.uf2FileUrl = this.getAttribute("uf2file");
        this.uf2FileUrl = this.uf2FileUrl.replace("https://downloads.circuitpython.org/bin/adafruit_feather_esp32s3_tft/en_US/", "/bin/");
        this.binFileUrl = this.getAttribute("binfile");

        // Nice to have for now
        this.chipFamily = this.getAttribute("chipfamily");
        this.bootloaderId = this.getAttribute("bootloaderid"); // This could be used to check serial output from board matches the UF2 file

        super.connectedCallback();
    }

    // This may end up moving to a superclass that extends the installer
    // These are a series of the valid steps that should be part of a program flow
    flows = {
        uf2Program: {
            label: `Install CircuitPython [version] UF2 and Bootloader`,
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSelectBootDrive, this.stepCopyUf2, this.stepCredentials, this.stepSettingsToml, this.stepSuccess],
            isEnabled: () => { return !!this.bootloaderUrl && !!this.uf2FileUrl },
        },
        uf2Only: {
            label: `Install CircuitPython [version] UF2 Only`,
            steps: [this.stepSelectBootDrive, this.stepCopyUf2, this.stepCredentials, this.stepSuccess],
            isEnabled: () => { return !!this.uf2FileUrl },
        },
        binProgram: {
            label: `Install CircuitPython [version] Bin`,
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepFlashBin, this.stepSuccess],
            isEnabled: () => { return !!this.binFileUrl },
        },
        bootloaderOnly: {
            label: "Install Bootloader Only",
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSuccess],
            isEnabled: () => { return !!this.bootloaderUrl },
        },
        credentialsOnly: {
            label: "Update WiFi credentials",
            steps: [this.stepSerialConnect, this.stepCredentials, this.stepSettingsToml, this.stepSuccess],
            isEnabled: () => { return this.cpDetected() },
        },
        test: {
            label: "Test (To be Removed)",
            steps: [this.stepTest],
            isEnabled: () => { return true; },
        }
    }

    // This is the data for the CircuitPython specific dialogs
    cpDialogs = {
        serialConnect: {
            closeable: true,
            template: (data) => html`
                <p>
                    Welcome to the CircuitPython Installer. This tool will install CircuitPython on your ${data.boardName}.
                </p>
                <p>
                    Make sure your board is plugged into this computer via a Serial connection using a USB Cable.
                </p>
                <ul>
                    <li><em><strong>NOTE:</strong> A lot of people end up using charge-only USB cables and it is very frustrating! Make sure you have a USB cable you know is good for data sync.</em></li>
                </ul>
                <p>
                    <button id="butConnect" type="button" @click=${this.connectHandler.bind(this)}>Connect</button>
                    Click this button to open the Web Serial connection menu.
                </p>

                <p>There may be many devices listed, such as your remembered Bluetooth peripherals, anything else plugged into USB, etc.</p>

                <p>
                    If you aren't sure which to choose, look for words like "USB", "UART", "JTAG", and "Bridge Controller". There may be more than one right option depending on your system configuration. Experiment if needed.
                </p>
            `,
            buttons: [this.previousButton, {
                label: "Next",
                onClick: this.nextStep,
                isEnabled: () => { return (this.currentStep < this.currentFlow.steps.length - 1) && this.connected == this.connectionStates.CONNECTED },
                onUpdate: async (e) => { this.currentDialogElement.querySelector("#butConnect").innerText = this.connected; },
            }],
        },
        confirm: {
            template: (data) => html`
                <p>This will overwrite everything on the ${data.boardName}.</p>
            `,
            buttons: [
                this.previousButton,
                {
                    label: "Continue",
                    onClick: this.nextStep,
                }
            ],
        },
        uf2FolderSelect: {
            closeable: true,
            template: (data) => html`
                <p>
                    Please select the ${data.drivename} Drive where the UF2 file will be copied.
                </p>
                <p>
                If you just installed the bootloader, you may need to reset your board. If you already had the bootloader installed,
                you may need to double press the reset button.
                </p>
                <p>
                    <button id="butSelectBootDrive" type="button" @click=${this.bootDriveSelectHandler.bind(this)}>Select ${data.drivename} Drive</button>
                </p>
            `,
            buttons: [{
                label: "Next",
                onClick: this.nextStep,
                isEnabled: () => { return (this.currentStep < this.currentFlow.steps.length - 1) && !!this.bootDriveHandle },
            }],
        },
        actionWaiting: {
            template: (data) => html`
                <p class="centered">${data.action}...</p>
                <div class="loader"><div></div><div></div><div></div><div></div></div>
            `,
            buttons: [],
        },
        actionProgress: {
            template: (data) => html`
                <p>${data.action}...</p>
                <progress id="stepProgress" max="100" value="${data.percentage}"> ${data.percentage}% </progress>
            `,
            buttons: [],
        },
        // We may have a waiting for Bootloader to start dialog (may reuse the erase dialog)
        credentials: {
            template: (data) => html`
                <div class="field">
                    <label for="circuitpy_wifi_ssid">WiFi Network Name (SSID):</label>
                    <input id="circuitpy_wifi_ssid" class="setting-data" type="text" placeholder="WiFi SSID" value="" />
                </div>
                <div class="field">
                    <label for="circuitpy_wifi_password">WiFi Password:</label>
                    <input id="circuitpy_wifi_password" class="setting-data" type="text" placeholder="WiFi Password" value=""  />
                </div>
                <div class="field">
                    <label for="circuitpy_web_api_password">Web Workflow API Password:</label>
                    <input id="circuitpy_web_api_password" class="setting-data" type="text" placeholder="Web Workflow API Password" value=""  />
                </div>
                <div class="field">
                    <!-- Alternatively "Disable USB Mass Storage" -->
                    <input id="circuitpy_drive" class="setting" type="checkbox" value="disabled" checked />
                    <label for="circuitpy_drive">Disable CIRCUITPY Drive (Required for write access)</label>
                </div>
            `,
        },
        success: {
            closeable: true,
            template: (data) => html`
                <p>Successfully Completed Installation</p>
            `,
            buttons: [this.closeButton],
        },
        error: {
            closeable: true,
            template: (data) => html`
                <p>Installation Error: ${data.message}</p>
            `,
            buttons: [this.closeButton],
        },
    }

    async bootDriveSelectHandler(e) {
        const bootloaderVolume = await this.getBootDriveName();
        let dirHandle;

        // This will need to show a dialog selector
        try {
            dirHandle = await window.showDirectoryPicker({mode: 'readwrite'});
        } catch (e) {
            // Likely the user cancelled the dialog
            console.log(e);
            return;
        }
        if (bootloaderVolume && bootloaderVolume != dirHandle.name) {
            alert(`The selected drive named ${dirHandle.name} does not match the expected name of ${bootloaderVolume}. Please select the correct drive.`);
            return;
        }
        if (!await this._verifyPermission(dirHandle)) {
            alert("Unable to write to the selected folder");
            return;
        }
        // The returned value should match the boot drive name and have write access
        // If so, we set a class variable, which and trigger an update of the buttons
        // The dialog update could actually just go to the next step automatically
        // Or we could just do that here

        this.bootDriveHandle = dirHandle;
        this.updateButtons();
    }

    async _verifyPermission(folderHandle) {
        const options = {mode: 'readwrite'};

        if (await folderHandle.queryPermission(options) === 'granted') {
            return true;
        }

        if (await folderHandle.requestPermission(options) === 'granted') {
            return true;
        }

        return false;
    }

    async connectHandler(e) {
        await this.disconnect();
        let esploader;
        try {
            esploader = await esptoolPackage.connect({
                log: (...args) => this.logMsg(...args),
                debug: (...args) => {},
                error: (...args) => this.errorMsg(...args),
            });
        } catch (err) {
            this.errorMsg("Unable to open Serial connection to board. Make sure the port is not already in use by another application or in another browser tab.");
            return;
        }

        try {
            this.updateUIConnected(this.connectionStates.CONNECTING);
            await esploader.initialize();
            this.updateUIConnected(this.connectionStates.CONNECTED);
        } catch (err) {
            await esploader.disconnect();
            // Disconnection before complete
            this.updateUIConnected(this.connectionStates.DISCONNECTED);
            this.errorMsg("Unable to connect to the board. Make sure it is in bootloader mode by holding the boot0 button when powering on and try again.")
            return;
        }

        try {
            this.logMsg(`Connected to ${esploader.chipName}`);
            this.logMsg(`MAC Address: ${this.formatMacAddr(esploader.macAddr())}`);

            // check chip compatibility
            if (FAMILY_TO_CHIP_MAP[this.chipFamily] == esploader.chipFamily) {
                console.log("This chip checks out");
                this.espStub = await esploader.runStub();
                this.espStub.addEventListener("disconnect", () => {
                    this.updateUIConnected(this.connectionStates.DISCONNECTED);
                    this.espStub = null;
                });

                await this.setBaudRateIfChipSupports(esploader.chipFamily, PREFERRED_BAUDRATE);
                return
            }

            // Can't use it so disconnect now
            this.errorMsg("Oops, this is the wrong firmware for your board.")
            await this.disconnect()

        } catch (err) {
            await esploader.disconnect();
            // Disconnection before complete
            this.updateUIConnected(this.connectionStates.DISCONNECTED);
            this.errorMsg("Oops, we lost connection to your board before completing the install. Please check your USB connection and click Connect again. Refresh the browser if it becomes unresponsive.")
        }
    }

    async stepSerialConnect() {
        // Display Serial Connect Dialog
        this.showDialog(this.dialogs.serialConnect, {boardName: this.boardName});
    }

    async getBootDriveName() {
        if (this._bootDriveName) {
            return this._bootDriveName;
        }

        if (!this.bootloaderId || !this.bootloaderUrl) {
            return null;
        }

        // Download the bootloader zip file
        let [filename, fileBlob] = await this.downloadAndExtract(this.bootloaderUrl, 'tinyuf2.bin');
        const fileContents = await fileBlob.text();

        const regex = /B\x00B\x00([A-Z0-9\x00]{11})FAT16/;
        const matches = fileContents.match(regex);
        if (!matches || matches.length < 2) {
            return null;
        }

        // Strip any null characters from the name
        this.removeCachedFile(this.bootloaderUrl.split("/").pop());
        this._bootDriveName = matches[1].replace(/\0/g, '');
        return this._bootDriveName;
    }

    async stepConfirm() {
        // Display Confirm Dialog
        this.showDialog(this.dialogs.confirm, {boardName: this.boardName});
    }

    async stepEraseAll() {
        // Display Erase Dialog
        this.showDialog(this.dialogs.actionWaiting, {
            action: "Erasing Flash",
        });
        try {
            await this.espStub.eraseFlash();
        } catch (err) {
            this.errorMsg("Unable to finish erasing Flash memory. Please try again.");
        }
        await this.nextStep();
    }

    async stepFlashBin() {
        if (!this.binFileUrl) {
            // We shouldn't be able to get here, but just in case
            this.errorMsg("Missing bin file URL. Please make sure the installer button has this specified.");
            return;
        }

        await this.downloadAndInstall(this.binFileUrl);
        await this.nextStep();
    }

    async stepBootloader() {
        if (!this.bootloaderUrl) {
            // We shouldn't be able to get here, but just in case
            this.errorMsg("Missing bootloader file URL. Please make sure the installer button has this specified.");
            return;
        }
        // Display Bootloader Dialog
        await this.downloadAndInstall(this.bootloaderUrl, 'combined.bin', true);
        // TODO: Reboot into bootloader (or prompt user to reset the board)
        await this.nextStep();
    }

    async stepSelectBootDrive() {
        const bootloaderVolume = await this.getBootDriveName();

        if (bootloaderVolume) {
            console.log(`Waiting for user to select a bootloader volume named ${bootloaderVolume}`);
        }

        // Display Select Bootloader Drive Dialog
        this.showDialog(this.dialogs.uf2FolderSelect, {
            drivename: bootloaderVolume ? bootloaderVolume : "Bootloader",
        });
    }

    async stepCopyUf2() {
        // To actually copy the file, we can use the File System Access API and look at the name of the folder
        // that the user chose. Changing it is just for the session, so we could restrict the user to only using
        // the expected name. If this cause problems, we can remove the check in the future.

        if (!this.bootDriveHandle) {
            this.errorMsg("No boot drive selected. stepSelectBootDrive should preceed this step.");
            return;
        }
        // Display Progress Dialog
        this.showDialog(this.dialogs.actionProgress, {
            action: `Copying ${this.uf2FileUrl}`,
        });

        // Do a copy and update progress along the way
        await this.downloadAndCopy(this.uf2FileUrl);

        // Once done, call nextstep
        await this.nextStep();
    }

    async stepTest() {
        console.log(await this.getBootDriveName());
    }

    async stepCredentials() {
        // Display Credentials Request Dialog
        this.showDialog(this.dialogs.credentials);
    }

    async stepSettingsToml() {
        // Connect to the Serial Port and interact with the REPL
    }

    async stepWebWorkflow() {
        // Display Dialog to set up Web Workflow
        // Wait for CircuitPython to be detected
        // Write the Settings.toml file
        // If Disable CIRCUITPY Drive was checked, write the boot.py file
        // Reboot

        this.showDialog(this.dialogs.setUpWebWorkflow);
    }

    async stepSuccess() {
        // Display Success Dialog
        this.showDialog(this.dialogs.success);
        // If we were setting up Web Workflow, we may want to provide a link to code.circuitpython.org
        // Alternatively, we may want a separate dialog with a link
    }

    async stepClose() {
        // Close the currently loaded dialog
        this.closeDialog();
    }

    cpDetected() {
        // TODO: Actually detect CircuitPython
        // We may also want to have it return the version number and return null if not detected
        return false;
    }

    async downloadFile(url, progressElement) {
        let response;
        try {
            response = await fetch(url);
        } catch (err) {
            this.errorMsg(`Unable to download file: ${url}`);
            return null;
        }

        const body = response.body;
        const reader = body.getReader();
        const contentLength = +response.headers.get('Content-Length');
        let receivedLength = 0;
        let chunks = [];
        while(true) {
            const {done, value} = await reader.read();
            if (done) {
                break;
            }
            chunks.push(value);
            receivedLength += value.length;
            progressElement.value = Math.round(receivedLength / contentLength) * 100;
            console.log(`Received ${receivedLength} of ${contentLength}`)
        }
        let chunksAll = new Uint8Array(receivedLength);
        let position = 0;
        for(let chunk of chunks) {
            chunksAll.set(chunk, position);
            position += chunk.length;
        }

        let result = new Blob([chunksAll]);

        return result;
    }

    addCachedFile(filename, blob) {
        this.fileCache.push({
            filename: filename,
            blob: blob
        });
    }

    getCachedFile(filename) {
        for (let file of this.fileCache) {
            if (file.filename === filename) {
                return file.contents;
            }
        }
        return null;
    }

    removeCachedFile(filename) {
        for (let file of this.fileCache) {
            if (file.filename === filename) {
                this.fileCache.splice(this.fileCache.indexOf(file), 1);
            }
        }
    }

    async downloadAndExtract(url, fileToExtract = null, cacheFile = false) {
        // Display Progress Dialog
        let filename = url.split("/").pop();
        let fileBlob = this.getCachedFile(filename);

        if (!fileBlob) {
            this.showDialog(this.dialogs.actionProgress, {
                action: `Downloading ${filename}`
            });

            const progressElement = this.currentDialogElement.querySelector("#stepProgress");

            // Download the file at the url updating the progress in the process
            fileBlob = await this.downloadFile(url, progressElement);

            if (cacheFile) {
                this.addCachedFile(filename, fileBlob);
            }
        }

        // If the file is a zip file, unzip and find the file to extract
        if (filename.endsWith(".zip") && fileToExtract) {
            let foundFile;
            // Update the Progress dialog
            this.showDialog(this.dialogs.actionProgress, {
                action: `Extracting ${fileToExtract}`
            });

            // Set that to the current file to flash
            [foundFile, fileBlob] = await this.findAndExtractFromZip(fileBlob, fileToExtract);
            if (!fileBlob) {
                this.errorMsg(`Unable to find ${fileToExtract} in ${filename}`);
                return;
            }
            filename = foundFile;
        }

        return [filename, fileBlob];
    }

    async downloadAndInstall(url, fileToExtract = null, cacheFile = false) {
        let [filename, fileBlob] = await this.downloadAndExtract(url, fileToExtract, cacheFile);

        // Update the Progress dialog
        if (fileBlob) {
            const fileContents = new Uint8Array(await fileBlob.arrayBuffer());

            let lastPercent = 0;
            this.showDialog(this.dialogs.actionProgress, {
                action: `Flashing ${filename}`
            });
            try {
                await this.espStub.flashData(fileContents, (bytesWritten, totalBytes) => {
                    let percentage = Math.floor((bytesWritten / totalBytes) * 100);
                    if (percentage != lastPercent) {
                        progressElement.value = percentage;
                        this.logMsg(`${percentage}% (${bytesWritten}/${totalBytes})...`);
                        lastPercent = percentage;
                    }
                }, 0, 0);
            } catch (err) {
                this.errorMsg(`Unable to flash file: ${filename}`);
                console.log(err);
            }
        }
    }

    /*
    while(true) {
        const {done, value} = await reader.read();
        if (done) {
            break;
        }
        chunks.push(value);
        receivedLength += value.length;
        progressElement.value = Math.round(receivedLength / contentLength) * 100;
        console.log(`Received ${receivedLength} of ${contentLength}`)
    }

    */

    async downloadAndCopy(url, dirHandle = null) {
        const CHUNK_SIZE = 64 * 1024;
        if (!dirHandle) {
            dirHandle = this.bootDriveHandle;
        }
        if (!dirHandle) {
            this.errorMsg("No drive handle available");
            return;
        }

        const progressElement = this.currentDialogElement.querySelector("#stepProgress");
        progressElement.value = 0;

        let [filename, fileBlob] = await this.downloadAndExtract(url);
        const fileHandle = await dirHandle.getFileHandle(filename, {create: true});
        const writableStream = await fileHandle.createWritable();
        const totalSize = fileBlob.size;
        let bytesWritten = 0;
        let chunk;
        while(bytesWritten < totalSize) {
            chunk = fileBlob.slice(bytesWritten, bytesWritten + CHUNK_SIZE);
            await writableStream.write(chunk, {position: bytesWritten, size: chunk.size});

            bytesWritten += chunk.size;
            progressElement.value = Math.round(bytesWritten / totalSize * 100);
            console.log(`${Math.round(bytesWritten / totalSize * 100)}% (${bytesWritten} / ${totalSize}) written...`);
        }
        console.log("File successfully written");
        try {
            // Attempt to close the file, but since the device reboots, it may error
            await writableStream.close();
            console.log("File successfully closed");
        } catch (err) {
            console.log("Error closing file. Continuing...");
        }
    }

    async findAndExtractFromZip(zipBlob, filename) {
        const reader = new zip.ZipReader(new zip.BlobReader(zipBlob));

        // unzip into local file cache
        let zipContents = await reader.getEntries();

        for(const zipEntry of zipContents) {
            if (zipEntry.filename.localeCompare(filename) === 0) {
                //const writer = extractAsString ? new zip.TextWriter() : new zip.Uint8ArrayWriter();
                const extractedFile = await zipEntry.getData(new zip.BlobWriter());
                return [zipEntry.filename, extractedFile];
            }
        }

        return [null, null];
    }
}

customElements.define('cp-install-button', CPInstallButton, {extends: "button"});

// Changes to make:
// Hide the log and make it accessible via the menu (future feature, console.log for now)
// May need to deal with the fact that the ESPTool uses Web Serial and CircuitPython REPL uses Web Serial

// Ideas for CP Installer:
// Put the Select Serial Port ahead of the menu
// If already connected, skip past
// Add a menu item to select a different port

// Possible Issues to resolve:
// Serial Port is not closing when it fails to connect
/*

function toggleConsole(show) {
    // hide/show the console log and its widgets
    const consoleItemsMethod = show ? "remove" : "add"
    for (let idx = 0; idx < consoleItems.length; idx++) {
        consoleItems.item(idx).classList[consoleItemsMethod]("hidden")
    }
    // toggle the button
    //butShowConsole.checked = show
    // tell the app if it's sharing space with the console
    const appDivMethod = show ? "add" : "remove"
    appDiv.classList[appDivMethod]("with-console")

    // scroll both to the bottom a moment after adding
    setTimeout(() => {
        log.scrollTop = log.scrollHeight
        appDiv.scrollTop = appDiv.scrollHeight
    }, 200)
}

async function populateSecretsFile(path) {
    let response = await fetch(path);
    let contents = await response.json();

    // Get the secrets data
    for (let field of getValidFields()) {
        const { id, value } = partitionData[field]
        if(id === "status_pixel_brightness") {
            const floatValue = parseFloat(value)
            updateObject(contents, id, isNaN(floatValue) ? 0.2 : floatValue);
        } else {
            updateObject(contents, id, value);
        }
    }

    // Convert the data to text and return
    return JSON.stringify(contents, null, 4);
}

function doThingOnClass(method, thing, classSelector) {
    const classItems = document.getElementsByClassName(classSelector)
    for (let idx = 0; idx < classItems.length; idx++) {
        classItems.item(idx).classList[method](thing)
    }
}

function updateObject(obj, path, value) {
    if (typeof obj === "undefined") {
        return false;
    }

    var _index = path.indexOf(".");
    if (_index > -1) {
        return updateObject(obj[path.substring(0, _index)], path.substr(_index + 1), value);
    }

    obj[path] = value;
}
*/