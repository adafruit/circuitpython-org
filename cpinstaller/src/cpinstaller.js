'use strict';
import { html } from 'https://unpkg.com/lit-html?module';
import * as zip from "https://deno.land/x/zipjs/index.js";
import * as esptoolPackage from "https://unpkg.com/esp-web-flasher@5.1.2/dist/web/index.js?module"
import { InstallButton } from "./installer.js";

// TODO: Figure out how to make the Web Serial from ESPTool and Web Serial to communicate with CircuitPython not conflict
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
// To run REPL code, I may need to modularize the work I did for code.circuitpython.org
// That allows you to run code in the REPL and get the output back. I may end up creating a
// library that uses Web Serial and allows you to run code in the REPL and get the output back
// because it's very integrated into the serial recieve and send code.
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
        this.init();
    }

    connectedCallback() {
        this.boardName = this.getAttribute("boardname") || "ESP32-based device";

        // If this is empty, it's a problem
        this.boardId = this.getAttribute("boardid");
        this.releaseVersion = this.getAttribute("version");

        // We need either the bootloader and uf2 or bin file to continue
        this.bootloaderUrl = this.getAttribute("bootloader");
        if (this.bootloaderUrl) {
            this.bootloaderUrl = `/bin/${this.bootloaderUrl.split("/").pop()}`;
        }
        this.uf2FileUrl = this.getAttribute("uf2file");
        this.binFileUrl = this.getAttribute("binfile");

        // Nice to have for now
        this.chipFamily = this.getAttribute("chipfamily");
        this.bootloadId = this.getAttribute("bootloadid"); // This could be used to check serial output from board matches the UF2 file

        super.connectedCallback();
    }

    // This may end up moving to a superclass that extends the installer
    // These are a series of the valid steps that should be part of a program flow
    flows = {
        binProgram: {
            label: `Install CircuitPython [version] Bin`,
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepFlashBin, this.stepSuccess],
            isEnabled: () => { return !!this.binFileUrl },
        },
        uf2Program: {
            label: `Install CircuitPython [version] UF2 and Bootloader`,
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepCopyUf2, this.stepSettings, this.stepSuccess],
            isEnabled: () => { return !!this.bootloaderUrl && !!this.uf2FileUrl },
        },
        bootloaderOnly: {
            label: "Install Bootloader Only",
            steps: [this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSuccess],
            isEnabled: () => { return !!this.bootloaderUrl },
        },
        settingsOnly: {
            label: "Update WiFi credentials",
            steps: [this.stepSerialConnect, this.stepCredentials, this.stepSettings, this.stepSuccess],
            isEnabled: () => { return this.cpDetected() },
        }
    }

    // This is the data for the dialogs
    cpDialogs = {
        serialConnect: {
            closeable: true,
            template: (data) => html`
                <p>
                    Welcome to the CircuitPython Installer. This tool will install CircuitPython on your ${data.boardName}.
                </p>
                <p>Make sure your board is plugged into this computer via a Serial connection using a USB Cable.
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
                    If you aren't sure which to choose, look for words like "USB", "UART", and "Bridge Controller". There may be more than one right option depending on your system configuration. Experiment if needed.
                </p>
            `,
            buttons: [this.previousButton, {
                label: "Next",
                onClick: this.nextStep,
                isEnabled: () => { return (this.currentStep < this.currentFlow.steps.length - 1) && this.connected == this.connectionStates.CONNECTED },
                onUpdate: async (e) => { console.log("updating"); this.currentDialogElement.querySelector("#butConnect").innerText = this.connected; },
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
        erase: {
            template: (data) => html`
                <p class="centered">Erasing Flash...</p>
                <div class="loader"><div></div><div></div><div></div><div></div></div>
            `,
            buttons: [],
        },
        flash: {
            template: (data) => html`
                <p class="centered">${data.action} ${data.file}...</p>
                <progress id="flashProgress" max="100" value="0"></progress>
            `,
            buttons: [],
        },
        // We may have a waiting for Bootloader to start dialog
        copyUf2: {
            template: (data) => html`
                <p class="centered">Copying ${data.file}...</p>
                <progress id="copyProgress" max="100" value="0"></progress>
            `,
            buttons: [this.nextButton],
        },
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
                    <input id="circuitpy_drive" class="setting" type="checkbox" value="disabled" checked />
                    <label for="circuitpy_drive">Disable CIRCUITPY Drive (Required for write access)</label>
                </div>
            `,
        },
        circuitPythonCheck: {
            template: (data) => html`
                <p>Looking for CircuitPython...</p>
                <progress id="copyProgress" max="100" value="${data.percentage}"> ${data.percentage}% </progress>
            `,
        },
        setUpWebWorkflow: {
            template: (data) => html`
                <p>Setting up Web Workflow...</p>
                <progress id="copyProgress" max="100" value="${data.percentage}"> ${data.percentage}% </progress>
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
            closeable: false,
            buttons: [this.closeButton],
        },
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
            this.logMsg("Connected to " + esploader.chipName);
            this.logMsg("MAC Address: " + this.formatMacAddr(esploader.macAddr()));

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

    async stepConfirm() {
        // Display Confirm Dialog
        this.showDialog(this.dialogs.confirm, {boardName: this.boardName});
    }

    async stepEraseAll() {
        // Display Erase Dialog
        this.showDialog(this.dialogs.erase);
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
        await this.downloadAndInstall(this.bootloaderUrl, 'combined.bin');
        // TODO: Reboot into bootloader
        await this.nextStep();
    }

    async stepCopyUf2() {
        // Display CopyUf2 Dialog
        this.showDialog(this.dialogs.copyUf2, {file: this.uf2FileUrl});
    }

    async stepSettings() {
        // Display Settings Dialog
        this.showDialog(this.dialogs.settings);
    }

    async stepCredentials() {
        // Display Credentials Request Dialog
        this.showDialog(this.dialogs.credentials);
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
            response = await fetch(url, {mode: "cors"});
        } catch (err) {
            this.errorMsg("Unable to download file: " + url);
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

    async downloadAndInstall(url, fileToExtract = null) {
        // Display Flash Dialog
        let filename = url.split("/").pop();

        this.showDialog(this.dialogs.flash, {
            action: "Downloading",
            file: filename,
        });

        const progressElement = this.currentDialogElement.querySelector("#flashProgress");

        // Download the file at the url updating the progress in the process
        let fileContents = await this.downloadFile(url, progressElement);

        // If the file is a zip file, unzip and find the file to extract
        if (filename.endsWith(".zip") && fileToExtract) {
            let foundFile;
            console.log("Extracting step");
            // Update the flash dialog
            this.showDialog(this.dialogs.flash, {
                action: "Extracting",
                file: fileToExtract,
            });

            // Set that to the current file to flash
            [foundFile, fileContents] = await this.findAndExtractFromZip(fileContents, fileToExtract);
            if (!fileContents) {
                this.errorMsg("Unable to find " + fileToExtract + " in " + filename);
                return;
            }
            filename = foundFile;
        }

        // Update the flash dialog
        if (fileContents) {
            console.log("Flash step");
            let lastPercent = 0;
            this.showDialog(this.dialogs.flash, {
                action: "Flashing",
                file: filename,
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
                this.errorMsg("Unable to flash file: " + filename);
                console.log(err);
            }
        }
    }

    async findAndExtractFromZip(zipBlob, filename) {
        const reader = new zip.ZipReader(new zip.BlobReader(zipBlob));

        // unzip into local file cache
        let zipContents = await reader.getEntries();

        for(const zipEntry of zipContents) {
            console.log(filename, zipEntry.filename, zipEntry.filename.localeCompare(filename));
            if (zipEntry.filename.localeCompare(filename) === 0) {
                const extractedFile = await zipEntry.getData(new zip.Uint8ArrayWriter());
                return [zipEntry.filename, extractedFile.buffer]; // ESPTool wants an ArrayBuffer
            }
        }

        return [null, null];
    }
}

customElements.define('cp-install-button', CPInstallButton, {extends: "button"});

// Changes to make:
// Hide the log and make it accessible via the menu (future feature, console.log for now)
// Generate dialogs on the fly
// Make a drop-in component
// Keep in mind it will be used for LEARN too
// May need to deal with CORS issues
// May need to deal with the fact that the ESPTool uses Web Serial and CircuitPython REPL uses Web Serial

/*
const maxLogLength = 100;
const disableWhileBusy = [partitionData, butProgram, butProgramBootloader, baudRate];

document.addEventListener("DOMContentLoaded", () => {


    // register dom event listeners
    butConnect.addEventListener("click", () => {
        clickConnect().catch(async (e) => {
            // Default Help Message:
            // if we've failed to catch the message before now, we need to give
            // the generic advice: reconnect, refresh, go to support
            this.errorMsg(
                `Connection Error, your board may be incompatible. Things to try:\n` +
                `1. Reset your board and try again.\n` +
                `  - Look for a little black button near the power port.\n` +
                `2. Refresh your browser and try again.\n` +
                `3. Make sure you are not connected in another browser tab.\n` +
                `4. Double-check your board type and serial port selection.\n` +
                `5. Post on the Support Forum (link above) with this info:\n\n` +
                `"Firmware Tool: ${e}"\n`
            );
            await disconnect();
            updateUIConnected(this.connectionStates.DISCONNECTED);
        });
    });
    //butClear.addEventListener("click", clickClear);
    butProgram.addEventListener("click", clickProgram);
    butProgramBootloader.addEventListener("click", clickProgramNvm);
    for (let i = 0; i < partitionData.length; i++) {
        partitionData[i].addEventListener("change", checkProgrammable);
        partitionData[i].addEventListener("keydown", checkProgrammable);
        partitionData[i].addEventListener("input", checkProgrammable);
    }
    //autoscroll.addEventListener("click", clickAutoscroll);
    //baudRate.addEventListener("change", changeBaudRate);

    // handle runaway errors
    window.addEventListener("error", event => {
        console.warn(`Uncaught error: ${event.error}`);
    });

    // handle runaway rejections
    window.addEventListener("unhandledrejection", event => {
        console.warn(`Unhandled rejection: ${event.reason}`);
    });

    // WebSerial feature detection
    if ("serial" in navigator) {
        const notSupported = document.getElementById("notSupported");
        notSupported.classList.add("hidden");
    }

    //initBinSelector();
    //initBaudRate();
    loadAllSettings();
    this.logMsg("CircuitPython ESP32 Installer loaded.");
    checkProgrammable();
});

let latestFirmwares = []


function doThingOnClass(method, thing, classSelector) {
    const classItems = document.getElementsByClassName(classSelector)
    for (let idx = 0; idx < classItems.length; idx++) {
        classItems.item(idx).classList[method](thing)
    }
}

function setDefaultBoard() {
    const board = getFromQuerystring(QUERYSTRING_BOARD_KEY)
    if (board && hasBoard(board)) {
        binSelector.value = board
        return true
    }
}

function hasBoard(board) {
    for (let opt of binSelector.options) {
        if (opt.value == board) { return opt }
    }
}

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

let semver
function initSemver(newSemver) {
    if (!newSemver) { return }

    semver = newSemver
    semverLabel.innerHTML = semver

    return true
}

function lookupFirmwareByBinSelector() {
    // get the currently selected board id
    const selectedId = binSelector.value
    if (!selectedId || selectedId === 'null') { throw new Error("No board selected.") }

    // grab the stored firmware settings for this id
    let selectedFirmware
    for (let firmware of latestFirmwares) {
        if (firmware.id === selectedId) {
            selectedFirmware = firmware
            break
        }
    }

    if (!selectedFirmware) {
        const { text, value } = binSelector.selectedOptions[0]
        throw new Error(`No firmware entry for: ${text} (${value})`)
    }

    return selectedFirmware
}

let lastPercent = 0;

async function clickAutoscroll() {
    saveSetting("autoscroll", autoscroll.checked);
}

async function clickProgram() {
    await programScript(full_bin_program);
}

async function clickProgramNvm() {
    await programScript(factory_reset_program);
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




async function mergeSettings() {
    const { settings } = lookupFirmwareByBinSelector()

    const transformedSettings = {
        ...settings,
        // convert the offset value from hex string to number
        offset: parseInt(settings.offset, 16),
        // replace the structure object with one where the keys have been converted
        // from hex strings to numbers
        structure: Object.keys(settings.structure).reduce((newObj, hexString) => {
            // new object, converted key (hex string -> numeric), same value
            newObj[parseInt(hexString, 16)] = settings.structure[hexString]

            return newObj
        }, {})
    }

    // merge with the defaults and send back
    return {
        ...BASE_SETTINGS,
        ...transformedSettings
    }
}

async function programScript(stages) {
    butProgram.disabled = true
    butProgramNvm.disabled = true
    try {
        await fetchFirmwareForSelectedBoard()
    } catch(error) {
        this.errorMsg(error.message)
        return
    }

    // pretty print the settings object with VERSION placeholders filled
    const settings = await mergeSettings()
    const settingsString = JSON.stringify(settings, null, 2)
    const strippedSettings = settingsString.replaceAll('VERSION', semver)
    this.logMsg(`Flashing with settings: <pre>${strippedSettings}</pre>`)

    let steps = [];
    for (let i = 0; i < stages.length; i++) {
        if (stages[i] == stage_erase_all) {
            steps.push({
                name: "Erasing Flash",
                func: async function () {
                    await this.espStub.eraseFlash();
                },
                params: {},
            });
        } else if (stages[i] == stage_flash_cpbin) {
            for (const [offset, filename] of Object.entries(settings.structure)) {
                steps.push({
                    name: "Flashing " + filename.replace('VERSION', semver),
                    func: async function (params) {
                        const firmware = await getFirmware(params.filename);
                        const progressBar = progress.querySelector("div");
                        lastPercent = 0;
                        await this.espStub.flashData(
                            firmware,
                            (bytesWritten, totalBytes
                            ) => {
                                let percentage = Math.floor((bytesWritten / totalBytes) * 100)
                                if (percentage != lastPercent) {
                                    this.logMsg(`${percentage}% (${bytesWritten}/${totalBytes})...`);
                                    lastPercent = percentage;
                                }
                                progressBar.style.width = percentage + "%";
                            },
                            params.offset,
                            0
                        );
                    },
                    params: {
                        filename: filename,
                        offset: offset,
                    },
                });
            }
        } else if (stages[i] == stage_flash_bootloader) {
            for (const [offset, filename] of Object.entries(settings.structure)) {
                steps.push({
                    name: "Flashing " + filename.replace('VERSION', semver),
                    func: async function (params) {
                        const firmware = await getFirmware(params.filename);
                        const progressBar = progress.querySelector("div");
                        lastPercent = 0;
                        await this.espStub.flashData(
                            firmware,
                            (bytesWritten, totalBytes
                            ) => {
                                let percentage = Math.floor((bytesWritten / totalBytes) * 100)
                                if (percentage != lastPercent) {
                                    this.logMsg(`${percentage}% (${bytesWritten}/${totalBytes})...`);
                                    lastPercent = percentage;
                                }
                                progressBar.style.width = percentage + "%";
                            },
                            params.offset,
                            0
                        );
                    },
                    params: {
                        filename: filename,
                        offset: offset,
                    },
                });
            }
        } else if (stages[i] == stage_program_settings) {
            // TODO: This needs to be rewritten to talk with circuitpython
            // and run python code via the repl to write a settings.toml file
            // See https://learn.adafruit.com/circuitpython-with-esp32-quick-start/setting-up-web-workflow
            // and https://github.com/circuitpython/web-editor/pull/46
            steps.push({
                name: "Generating and Writing the WiFi Settings",
                func: async function (params) {
                    let fileSystemImage = await generate(params.flashParams);

                    if (DO_DOWNLOAD) {
                        // Download the Partition
                        var blob = new Blob([new Uint8Array(fileSystemImage)], {
                            type: "application/octet-stream",
                        });
                        var link = document.createElement("a");
                        link.href = window.URL.createObjectURL(blob);
                        link.download = "littleFS.bin";
                        link.click();
                        link.remove();
                    } else {
                        const progressBar = progress.querySelector("div");
                        lastPercent = 0;
                        await this.espStub.flashData(
                            new Uint8Array(fileSystemImage).buffer,
                            (bytesWritten, totalBytes) => {
                                let percentage = Math.floor((bytesWritten / totalBytes) * 100)
                                if (percentage != lastPercent) {
                                    this.logMsg(`${percentage}% (${bytesWritten}/${totalBytes})...`);
                                    lastPercent = percentage;
                                }
                                progressBar.style.width = percentage + "%";
                            },
                            params.flashParams.offset,
                            0
                        );
                    }
                },
                params: {
                    flashParams: settings,
                },
            });
        }
    }

    for (let i = 0; i < disableWhileBusy.length; i++) {
        if (Array.isArray(disableWhileBusy[i])) {
            for (let j = 0; j < disableWhileBusy[i].length; i++) {
                disableWhileBusy[i][j].disable = true;
            }
        } else {
            disableWhileBusy[i].disable = true;
        }
    }

    progress.classList.remove("hidden");
    stepname.classList.remove("hidden");
    showStep(5)

    for (let i = 0; i < steps.length; i++) {
        stepname.innerText = steps[i].name + " (" + (i + 1) + "/" + steps.length + ")...";
        await steps[i].func(steps[i].params);
    }

    stepname.classList.add("hidden");
    stepname.innerText = "";
    progress.classList.add("hidden");
    progress.querySelector("div").style.width = "0";

    for (let i = 0; i < disableWhileBusy.length; i++) {
        if (Array.isArray(disableWhileBusy[i])) {
            for (let j = 0; j < disableWhileBusy[i].length; i++) {
                disableWhileBusy[i][j].disable = false;
            }
        } else {
            disableWhileBusy[i].disable = false;
        }
    }

    checkProgrammable();
    await disconnect();
    this.logMsg("To run the new firmware, please reset your device.");
    showStep(6);
}
*/