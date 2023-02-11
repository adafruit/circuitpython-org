'use strict';
import { html } from 'https://unpkg.com/lit-html?module';
import * as zip from "https://deno.land/x/zipjs/index.js";
import * as esptoolPackage from "https://unpkg.com/esp-web-flasher@5.1.2/dist/web/index.js?module"
import {REPL} from 'https://cdn.jsdelivr.net/gh/adafruit/circuitpython-repl-js@1.0.0/repl.js';
import { InstallButton } from "./base_installer.js";
import * as settingsTemplate from "./templates/settings.js";

// TODO: Figure out how to make the Web Serial from ESPTool and Web Serial to communicate with CircuitPython not conflict.
// It may just be easier to reconnect because for chips like the S3 and S2, it's a JTAG connection and there is
// inconsistency among the different chips. We may also be able to attempt to just connect.
// I think at the very least we'll have to reuse the same port so the user doesn't need to reselct, though it's possible it
// may change after reset. Since it's not
//
// For now, we'll use the following procedure for ESP32-S2 and ESP32-S3:
// 1. Install the bootloader file
// 2. Have User Reset the board
// 3. Install the UF2 file
// 4. Connect to REPL Serial
// 5. Generate the settings.toml file
// 6. Write the settings.toml to the board via the REPL
// 7. Have the user reset the board again
//
// For the esp32 and esp32c3, the procedure may be slightly different:
// 1. Install the bin file
// 2. Have User Reset the board
// 3. Connect to REPL Serial
// 4. Generate the settings.toml file
// 5. Write the settings.toml to the board via the REPL
// 6. Have the user reset the board again
//
// TODO: Combine multiple steps together. For now it was easier to make them separate,
// but for ease of configuration, it would be work better to combine them together.
// For instance stepSelectBootDrive and stepCopyUf2 should always be together and in
// that order, but due to having handlers in the first of those steps, it was easier to
// just call nextStep() from the handler.

const PREFERRED_BAUDRATE = 921600;
const COPY_CHUNK_SIZE = 64 * 1024; // 64 KB Chunks

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
        this._serialPortName = null;
        this.serialDevice = null;
        this.repl = null;
        this.fileCache = [];
        this.reader = null;
        this.writer = null;
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
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSelectBootDrive, this.stepCopyUf2, this.stepSetupRepl, this.stepCredentials, this.stepSettingsToml, this.stepSuccess],
            isEnabled: async () => { return !!this.bootloaderUrl && !!this.uf2FileUrl },
        },
        uf2Only: {
            label: `Install CircuitPython [version] UF2 Only`,
            steps: [this.stepSelectBootDrive, this.stepCopyUf2, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return !!this.uf2FileUrl },
        },
        binProgram: {
            label: `Install CircuitPython [version] Bin`,
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepFlashBin, this.stepSuccess],
            isEnabled: async () => { return !!this.binFileUrl },
        },
        bootloaderOnly: {
            label: "Install Bootloader Only",
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSuccess],
            isEnabled: async () => { return !!this.bootloaderUrl },
        },
        credentialsOnly: {
            label: "Update WiFi credentials",
            steps: [this.stepSetupRepl, this.stepCredentials, this.stepSettingsToml, this.stepSuccess],
            isEnabled: async () => { return true; },
        },
        test: {
            label: "Test (To be Removed)",
            steps: [this.stepTest],
            isEnabled: async () => { return true; },
        }
    }

    // This is the data for the CircuitPython specific dialogs
    cpDialogs = {
        espSerialConnect: {
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
                    <button id="butConnect" type="button" @click=${this.espToolConnectHandler.bind(this)}>Connect</button>
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
                isEnabled: async () => { return (this.currentStep < this.currentFlow.steps.length - 1) && this.connected == this.connectionStates.CONNECTED },
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
            buttons: [],
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
        cpSerial: {
            closeable: true,
            template: (data) => html`
                <p>
                    The next step is to write your credentials to settings.toml. Make sure your board is running CircuitPython. You may need to reset it first.
                </p>
                <p>
                    <button id="butConnect" type="button" @click=${this.cpSerialConnectHandler.bind(this)}>Connect</button>
                    Click this button to open the Web Serial connection menu. If it is already connected, pressing again will allow you to select a different port.
                </p>

                <p>${data.serialPortInstructions}</p>
            `,
            buttons: [this.previousButton, {
                label: "Next",
                onClick: this.nextStep,
                isEnabled: async () => { return (this.currentStep < this.currentFlow.steps.length - 1) && !!this.serialDevice; },
                onUpdate: async (e) => { this.currentDialogElement.querySelector("#butConnect").innerText = !!this.serialDevice ? "Connected" : "Connect"; },
            }],
        },

        // We may have a waiting for Bootloader to start dialog (may reuse the erase dialog)
        credentials: {
            closeable: true,
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


    ////////// STEP FUNCTIONS //////////

    async stepSerialConnect() {
        // Display Serial Connect Dialog
        this.showDialog(this.dialogs.espSerialConnect, {boardName: this.boardName});
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

    async stepSetupRepl() {
        const serialPortName = await this.getSerialPortName();
        let serialPortInstructions ="There may be several devices listed. If you aren't sure which to choose, look for one that includes the name of your microcontroller.";
        if (serialPortName) {
            serialPortInstructions =`There may be several devices listed, but look for one called something like ${serialPortName}.`
        }
        this.showDialog(this.dialogs.cpSerial, {
            serialPortInstructions: serialPortInstructions
        });
    }

    async stepCredentials() {
        // We may want to see if the board has previously been set up and fill in any values from settings.toml and boot.py

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

    async stepTest() {
        console.log(await this.getBootDriveName());
        console.log(await this.getSerialPortName());
    }


    ////////// HANDLERS //////////

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

        this.bootDriveHandle = dirHandle;
        await this.nextStep();
    }

    async espToolConnectHandler(e) {
        await this.onReplDisconnected(e);
        await this.espDisconnect();
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
            this.updateEspConnected(this.connectionStates.CONNECTING);
            await esploader.initialize();
            this.updateEspConnected(this.connectionStates.CONNECTED);
        } catch (err) {
            await esploader.disconnect();
            // Disconnection before complete
            this.updateEspConnected(this.connectionStates.DISCONNECTED);
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
                this.espStub.addEventListener("disconnect", this.espDisconnect.bind(this));

                await this.setBaudRateIfChipSupports(esploader.chipFamily, PREFERRED_BAUDRATE);
                return
            }

            // Can't use it so disconnect now
            this.errorMsg("Oops, this is the wrong firmware for your board.")
            await this.espDisconnect();

        } catch (err) {
            await esploader.disconnect();
            // Disconnection before complete
            this.updateEspConnected(this.connectionStates.DISCONNECTED);
            this.errorMsg("Oops, we lost connection to your board before completing the install. Please check your USB connection and click Connect again. Refresh the browser if it becomes unresponsive.")
        }
    }

    async onSerialReceive(e) {
        await this.repl.onSerialReceive(e);
    }

    async cpSerialConnectHandler(e) {
        // Disconnect from the ESP Tool if Connected
        await this.espDisconnect();

        await this.onReplDisconnected(e);

        // Connect to the Serial Port and interact with the REPL
        try {
            this.serialDevice = await navigator.serial.requestPort();
        } catch (e) {
            // Likely the user cancelled the dialog
            console.log(e);
            return;
        }
        await this.serialDevice.open({baudRate: 115200});

        this.repl = new REPL();
        this.repl.serialTransmit = this.serialTransmit.bind(this);

        this.serialDevice.addEventListener("message", this.onSerialReceive.bind(this));

        // Start the read loop
        this._readLoopPromise = this._readSerialLoop().catch(
            async function(error) {
                await this.onReplDisconnected();
            }.bind(this)
        );

        if (this.serialDevice.writable) {
            this.writer = this.serialDevice.writable.getWriter();
            await this.writer.ready;
        }

        this.nextStep();
    }

    async onReplDisconnected(e) {
        if (this.reader) {
            await this.reader.cancel();
            this.reader = null;
        }
        if (this.writer) {
            await this.writer.releaseLock();
            this.writer = null;
        }

        if (this.serialDevice) {
            await this.serialDevice.close();
            this.serialDevice = null;
        }
    }

    //////////////// HELPERS ////////////////

    async espDisconnect() {
        // Disconnect the ESPTool
        if (this.espStub) {
            this.espStub.removeEventListener("disconnect", this.espDisconnect.bind(this));
            await this.espStub.disconnect();
            this.updateEspConnected(this.connectionStates.DISCONNECTED);
            this.espStub = null;
        }
    }

    async serialTransmit(msg) {
        const encoder = new TextEncoder();
        if (this.writer) {
            const encMessage = encoder.encode(msg);
            await this.writer.ready.catch((err) => {
                console.error(`Ready error: ${err}`);
            });
            await this.writer.write(encMessage).catch((err) => {
                console.error(`Chunk error: ${err}`);
            });
            await this.writer.ready;
        }
    }

    async _readSerialLoop() {
        if (!this.serialDevice) {
            return;
        }

        const messageEvent = new Event("message");
        const decoder = new TextDecoder();

        if (this.serialDevice.readable) {
            this.reader = this.serialDevice.readable.getReader();
            while (true) {
                const {value, done} = await this.reader.read();
                if (value) {
                    messageEvent.data = decoder.decode(value);
                    this.serialDevice.dispatchEvent(messageEvent);
                }
                if (done) {
                    this.reader.releaseLock();
                    break;
                }
            }
        }

        console.log("Read Loop Stopped. Closing Serial Port.");
    }

    async getBootDriveName() {
        if (this._bootDriveName) {
            return this._bootDriveName;
        }
        await this.extractBootloaderInfo();

        return this._bootDriveName;
    }

    async getSerialPortName() {
        if (this._serialPortName) {
            return this._serialPortName;
        }
        await this.extractBootloaderInfo();

        return this._serialPortName;
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

    async extractBootloaderInfo() {
        if (!this.bootloaderUrl) {
            return false;
        }

        // Download the bootloader zip file
        let [filename, fileBlob] = await this.downloadAndExtract(this.bootloaderUrl, 'tinyuf2.bin');
        const fileContents = await fileBlob.text();

        const bootDriveRegex = /B\x00B\x00([A-Z0-9\x00]{11})FAT16/;
        const serialNameRegex = /0123456789ABCDEF(.+)\x00UF2/;
        // Not sure if manufacturer is displayed. If not, we should use this instead
        // const serialNameRegex = /0123456789ABCDEF(?:.*\x00)?(.+)\x00UF2/;

        let matches = fileContents.match(bootDriveRegex);
        if (matches && matches.length >= 2) {
            // Strip any null characters from the name
            this._bootDriveName = matches[1].replace(/\0/g, '');
        }

        matches = fileContents.match(serialNameRegex);
        if (matches && matches.length >= 2) {
            // Replace any null characters with spaces
            this._serialPortName = matches[1].replace(/\0/g, ' ');
        }

        this.removeCachedFile(this.bootloaderUrl.split("/").pop());
    }

    async cpDetected() {
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
            progressElement.value = Math.round((receivedLength / contentLength) * 100);
            //console.log(`Received ${receivedLength} of ${contentLength}`)
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

    async writeSettings(settings) {
        settings = {
            CIRCUITPY_WIFI_SSID: "yourwifissid",
            CIRCUITPY_WIFI_PASSWORD: "yourpassword",
            CIRCUITPY_WEB_API_PASSWORD: "passw0rd",
            CIRCUITPY_WEB_API_PORT: 80,
        }

        template = settingsTemplate(settings);
        /* Python Code
        f = open('settings.toml', 'w')
        f.write('CIRCUITPY_WIFI_SSID = "wifissid"\n')
        f.write('CIRCUITPY_WIFI_PASSWORD = "wifipassword"\n')
        f.write('CIRCUITPY_WEB_API_PASSWORD = "webpassword"\n')
        f.close()
        */
    }

    async getCurrentSettings() {
        // Not sure if this is possible via the REPL
        // Maybe this?

        /* Python Code
        f = open('settings.toml', 'r')
        print(f.read())
        f.close()
        */

        // Then we parse it
    }

    // TODO: Write a toml reader/writer
    // For getting values, it should maybe use https://github.com/newproplus/iarna-toml/tree/ESM to parse
    // Then perhaps something simple that iterates through and rewrites new values in a new file.

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

    async downloadAndCopy(url, dirHandle = null) {
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
            chunk = fileBlob.slice(bytesWritten, bytesWritten + COPY_CHUNK_SIZE);
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