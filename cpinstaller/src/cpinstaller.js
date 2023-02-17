'use strict';
import { html } from 'https://unpkg.com/lit-html?module';
import * as toml from "https://unpkg.com/iarna-toml-esm@3.0.5/toml-esm.mjs"
import * as zip from "https://cdn.jsdelivr.net/npm/@zip.js/zip.js@2.6.65/+esm";
import * as esptoolPackage from "https://unpkg.com/esp-web-flasher@5.1.2/dist/web/index.js?module"
//import * as esptoolPackage from "https://adafruit.github.io/Adafruit_WebSerial_ESPTool/js/modules/esptool.js"
import { REPL } from 'https://cdn.jsdelivr.net/gh/adafruit/circuitpython-repl-js@1.1.0/repl.js';
import { InstallButton } from "./base_installer.js";

// We'll use the following procedure for ESP32-S2, ESP32-S3 and esp32c3:
// 1. Install the bootloader file
// 2. Have User Reset the board
// 3. Have the User select the Bootloader Drive
// 4. Install the UF2 file, at which point it automatically resets
// 5. Have the User select the CIRCUITPY drive
// 6. Generate the settings.toml file and write it to the drive
// 7. Have the user reset the board again
//
// For the esp32 (possibly c3 too if no CIRCUITPY drive), the procedure will be slightly different:
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
//
// TODO: Hide the log and make it accessible via the menu (future feature, console.log for now)
// May need to deal with the fact that the ESPTool uses Web Serial and CircuitPython REPL uses Web Serial


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
        this.circuitpyDriveHandle = null;
        this._bootDriveName = null;
        this._serialPortName = null;
        this.serialDevice = null;
        this.repl = null;
        this.fileCache = [];
        this.reader = null;
        this.writer = null;
        this.tomlSettings = null;
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
            this.bootloaderUrl = this.bootloaderUrl.replace("https://downloads.circuitpython.org/bootloaders/esp32/", "/bin/bootloaders/");
        }
        this.uf2FileUrl = this.getAttribute("uf2file");
        if (this.uf2FileUrl) {
            this.uf2FileUrl = this.uf2FileUrl.replace("https://downloads.circuitpython.org/bin/", "/bin/");
        }
        this.binFileUrl = this.getAttribute("binfile");
        if (this.binFileUrl) {
            this.binFileUrl = this.binFileUrl.replace("https://downloads.circuitpython.org/bin/", "/bin/");
        }
        // Nice to have for now
        this.chipFamily = this.getAttribute("chipfamily");
        this.bootloaderId = this.getAttribute("bootloaderid"); // This could be used to check serial output from board matches the UF2 file

        super.connectedCallback();
    }

    // These are a series of the valid steps that should be part of a program flow
    // Some steps currently need to be grouped together
    flows = {
        uf2FullProgram: {  // Native USB Install
            label: `Full CircuitPython [version] Install`,
            steps: [this.stepWelcome, this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSelectBootDrive, this.stepCopyUf2, this.stepSelectCpyDrive, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return this.hasNativeUsb() && !!this.bootloaderUrl && !!this.uf2FileUrl },
        },
        binFullProgram: {  // Non-native USB Install
            label: `Full CircuitPython [version] Install`,
            steps: [this.stepWelcome, this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepFlashBin, this.stepSetupRepl, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return !this.hasNativeUsb() && !!this.binFileUrl },
        },
        uf2Only: { // Upgrade when Bootloader is already installer
            label: `Upgrade/Install CircuitPython [version] UF2 Only`,
            steps: [this.stepWelcome, this.stepSelectBootDrive, this.stepCopyUf2, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return this.hasNativeUsb() && !!this.uf2FileUrl },
        },
        binOnly: {
            label: `Upgrade CircuitPython [version] Bin Only`,
            steps: [this.stepWelcome, this.stepSerialConnect, /*this.stepConfirm, this.stepEraseAll,*/ this.stepFlashBin, this.stepSuccess],
            isEnabled: async () => { return !!this.binFileUrl },
        },
        bootloaderOnly: { // Used to allow UF2 Upgrade/Install
            label: "Install Bootloader Only",
            steps: [this.stepWelcome, this.stepSerialConnect, this.stepConfirm, this.stepEraseAll, this.stepBootloader, this.stepSuccess],
            isEnabled: async () => { return this.hasNativeUsb() && !!this.bootloaderUrl },
        },
        credentialsOnlyRepl: { // Update via REPL
            label: "Update WiFi credentials",
            steps: [this.stepWelcome, this.stepSetupRepl, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return !this.hasNativeUsb() },
        },
        credentialsOnlyDrive: { // Update via CIRCUITPY Drive
            label: "Update WiFi credentials",
            steps: [this.stepWelcome, this.stepSelectCpyDrive, this.stepCredentials, this.stepSuccess],
            isEnabled: async () => { return this.hasNativeUsb() },
        }
    }

    // This is the data for the CircuitPython specific dialogs. Some are reused.
    cpDialogs = {
        welcome: {
            closeable: true,
            template: (data) => html`
                <p>
                    Welcome to the CircuitPython Installer. This tool will install CircuitPython on your ${data.boardName}.
                </p>
                <p>
                    This tool is <strong>new</strong> and <strong>experimental</strong>. If you experience any issues, feel free to check out
                    <a href="https://github.com/adafruit/circuitpython-org/issues">https://github.com/adafruit/circuitpython-org/issues</a>
                    to see if somebody has already submitted the same issue you are experiencing. If not, feel free to open a new issue. If
                    you do see the same issue and are able to contribute additional information, that would be appreciated.
                </p>
                <p>
                    If you are unable to use this tool, then the manual installation methods should still work.
                </p>
            `
        },
        espSerialConnect: {
            closeable: true,
            template: (data) => html`
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
        bootDriveSelect: {
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
        circuitpyDriveSelect: {
            closeable: true,
            template: (data) => html`
                <p>
                    Please select the CIRCUITPY Drive. If you don't see your CIRCUITPY drive, it may be disabled in boot.py or you may have renamed it at some point.
                </p>
                <p>
                    <button id="butSelectCpyDrive" type="button" @click=${this.circuitpyDriveSelectHandler.bind(this)}>Select CIRCUITPY Drive</button>
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

        credentials: {
            closeable: true,
            template: (data) => html`
                <fieldset>
                    <div class="field">
                        <label for="circuitpy_wifi_ssid">WiFi Network Name (SSID):</label>
                        <input id="circuitpy_wifi_ssid" class="setting-data" type="text" placeholder="WiFi SSID" value="${data.wifi_ssid}" />
                    </div>
                    <div class="field">
                        <label for="circuitpy_wifi_password">WiFi Password:</label>
                        <input id="circuitpy_wifi_password" class="setting-data" type="text" placeholder="WiFi Password" value="${data.wifi_password}" />
                    </div>
                    <div class="field">
                        <label for="circuitpy_web_api_password">Web Workflow API Password:</label>
                        <input id="circuitpy_web_api_password" class="setting-data" type="text" placeholder="Web Workflow API Password" value="${data.api_password}"  />
                    </div>
                    <div class="field">
                        <label for="circuitpy_web_api_port">Web Workflow API Port:</label>
                        <input id="circuitpy_web_api_port" class="setting-data" type="number" min="0" max="65535" placeholder="Web Workflow API Port" value="${data.api_port}"  />
                    </div>
                    ${data.mass_storage_disabled === true || data.mass_storage_disabled === false
                    ? html`<div class="field">
                        <label for="circuitpy_drive"><input id="circuitpy_drive" class="setting" type="checkbox" value="disabled" ${data.mass_storage_disabled ? "checked" : ""} />Disable CIRCUITPY Drive (Required for write access)</label>
                    </div>` : ''}
                </fieldset>
            `,
            buttons: [this.previousButton, {
                label: "Next",
                onClick: this.saveCredentials,
            }]
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

    async stepWelcome() {
        // Display Welcome Dialog
        this.showDialog(this.dialogs.welcome, {boardName: this.boardName});
    }

    async stepSerialConnect() {
        // Display Serial Connect Dialog
        this.showDialog(this.dialogs.espSerialConnect);
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
        await this.nextStep();
    }

    async stepSelectBootDrive() {
        const bootloaderVolume = await this.getBootDriveName();

        if (bootloaderVolume) {
            this.logMsg(`Waiting for user to select a bootloader volume named ${bootloaderVolume}`);
        }

        // Display Select Bootloader Drive Dialog
        this.showDialog(this.dialogs.bootDriveSelect, {
            drivename: bootloaderVolume ? bootloaderVolume : "Bootloader",
        });
    }

    async stepSelectCpyDrive() {
        this.logMsg(`Waiting for user to select CIRCUITPY drive`);

        // Display Select CIRCUITPY Drive Dialog
        this.showDialog(this.dialogs.circuitpyDriveSelect);
    }

    async stepCopyUf2() {
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
        this.tomlSettings = await this.getCurrentSettings();

        const parameters = {
            wifi_ssid: this.getSetting('CIRCUITPY_WIFI_SSID'),
            wifi_password: this.getSetting('CIRCUITPY_WIFI_PASSWORD'),
            api_password: this.getSetting('CIRCUITPY_WEB_API_PASSWORD'),
            api_port: this.getSetting('CIRCUITPY_WEB_API_PORT', 80),
        }
        if (this.hasNativeUsb()) {
            // TODO: Currently it is just disabled and not used because we don't have anything to modify boot.py in place.
            //parameters.mass_storage_disabled = true;
        }

        // Display Credentials Request Dialog
        this.showDialog(this.dialogs.credentials, parameters);
    }

    async stepSuccess() {

        // Determine if the credentials step was in steps of the current workflow and include instructions if so

        // Display Success Dialog
        this.showDialog(this.dialogs.success);
        // If we were setting up Web Workflow, we may want to provide a link to code.circuitpython.org
        // Alternatively, we may want a separate dialog with a link
    }

    async stepClose() {
        // Close the currently loaded dialog
        this.closeDialog();
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

    async circuitpyDriveSelectHandler(e) {
        let dirHandle;

        // This will need to show a dialog selector
        try {
            dirHandle = await window.showDirectoryPicker({mode: 'readwrite'});
        } catch (e) {
            // Likely the user cancelled the dialog
            return;
        }
        // Check if boot_out.txt exists
        if (!(await this.getBootOut(dirHandle))) {
            alert(`Expecting a folder with boot_out.txt. Please select the root folder of your CIRCUITPY drive.`);
            return;
        }
        if (!await this._verifyPermission(dirHandle)) {
            alert("Unable to write to the selected folder");
            return;
        }

        this.circuitpyDriveHandle = dirHandle;
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
                this.logMsg("This chip checks out");
                this.espStub = await esploader.runStub();
                this.espStub.addEventListener("disconnect", () => {
                    this.updateEspConnected(this.connectionStates.DISCONNECTED);
                    this.espStub = null;
                });

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

    //////////////// FILE HELPERS ////////////////

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

    async getBootOut(dirHandle) {
        return await this.readFile("boot_out.txt", dirHandle);
    }

    async readFile(filename, dirHandle = null) {
        // Read a file from the given directory handle

        if (!dirHandle) {
            dirHandle = this.circuitpyDriveHandle;
        }
        if (!dirHandle) {
            console.warn("CIRCUITPY Drive not selected and no Directory Handle provided");
            return null;
        }
        try {
            const fileHandle = await dirHandle.getFileHandle(filename);
            const fileData = await fileHandle.getFile();

            return await fileData.text();
        } catch (e) {
            return null;
        }
    }

    async writeFile(filename, contents, dirHandle = null) {
        // Write a file to the given directory handle
        if (!dirHandle) {
            dirHandle = this.circuitpyDriveHandle;
        }
        if (!dirHandle) {
            console.warn("CIRCUITPY Drive not selected and no Directory Handle provided");
            return null;
        }

        const fileHandle = await dirHandle.getFileHandle(filename, {create: true});
        const writable = await fileHandle.createWritable();
        await writable.write(contents);
        await writable.close();
    }


    //////////////// DOWNLOAD HELPERS ////////////////

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
            this.logMsg(`Received ${receivedLength} of ${contentLength}`)
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

            const progressElement = this.currentDialogElement.querySelector("#stepProgress");
            progressElement.value = 0;

            try {
                await this.espStub.flashData(fileContents, (bytesWritten, totalBytes) => {
                    let percentage = Math.round((bytesWritten / totalBytes) * 100);
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


    //////////////// OTHER HELPERS ////////////////

    async saveCredentials() {
        this.saveSetting('CIRCUITPY_WIFI_SSID');
        this.saveSetting('CIRCUITPY_WIFI_PASSWORD');
        this.saveSetting('CIRCUITPY_WEB_API_PASSWORD');
        this.saveSetting('CIRCUITPY_WEB_API_PORT');

        this.writeSettings(this.tomlSettings);
        if (this.hasNativeUsb()) {
            // TODO: Update boot.py to include 'import storage' and 'storage.disable_usb_drive()' if checked
        }
        await this.nextStep();
    }

    getSetting(setting, defaultValue = '') {
        if (this.tomlSettings.hasOwnProperty(setting)) {
            return this.tomlSettings[setting];
        }

        return defaultValue;
    }

    saveSetting(settingName) {
        const formElement = this.currentDialogElement.querySelector(`#${settingName.toLowerCase()}`)
        if (formElement) {
            if (formElement.type == "number") {
                this.tomlSettings[settingName] = parseInt(formElement.value);
            } else if (formElement.type == "text") {
                this.tomlSettings[settingName] = formElement.value;
            } else {
                this.errorMsg(`A setting was found, but a form element of type ${formElement.type} was not expected.`);
            }
        } else {
            this.errorMsg(`A setting named '${settingName}' was not found.`);
        }
    }

    async writeSettings(settings) {
        if (this.repl) {
            let replCode = [];

            replCode.push(`import storage`);
            replCode.push(`storage.remount("/", False)`);
            replCode.push(`f = open('settings.toml', 'w')`);

            for (const [setting, value] of Object.entries(settings)) {
                if (typeof value === "string") {
                    replCode.push(`f.write('${setting} = "${value}"\\n')`);
                } else {
                    replCode.push(`f.write('${setting} = ${value}\\n')`);
                }
            }
            replCode.push(`f.close()`);

            console.log(replCode.join("\n"));
            console.log(await this.repl.runCode(replCode.join("\n")));

            // Reset the microcontroller. This will probably cause us to lose the connection.
            //console.log(await this.repl.runCode(`microcontroller.reset()`));
        } else if (this.circuitpyDriveHandle) {
            const contents = toml.stringify(settings);
            await this.writeFile("settings.toml", contents);
        } else {
            this.errorMsg("Connect to the CIRCUITPY drive or the REPL first");
            return null;
        }
    }

    async getCurrentSettings() {
        let fileContents;
        if (this.repl) {
            fileContents = await this.repl.runCode("f = open('settings.toml', 'r')\nprint(f.read())\nf.close()\n")
        } else if (this.circuitpyDriveHandle) {
            fileContents = await this.readFile("settings.toml");
        } else {
            this.errorMsg("Connect to the CIRCUITPY drive or the REPL first");
            return null;
        }

        if (fileContents) {
            return toml.parse(fileContents);
        }
        console.warn("Unable to read settings.toml from CircuitPython. It may not exist.");
        return null;
    }

    async espDisconnect() {
        // Disconnect the ESPTool
        /*if (this.espStub) {
            this.espStub.removeEventListener("disconnect", this.espDisconnect.bind(this));
            await this.espStub.disconnect();
            this.updateEspConnected(this.connectionStates.DISCONNECTED);
            this.espStub = null;
        }*/
    }

    async serialTransmit(msg) {
        const encoder = new TextEncoder();
        if (this.writer) {
            const encMessage = encoder.encode(msg);
            await this.writer.ready.catch((err) => {
                this.errorMsg(`Ready error: ${err}`);
            });
            await this.writer.write(encMessage).catch((err) => {
                this.errorMsg(`Chunk error: ${err}`);
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
                    await this.onReplDisconnected();
                    break;
                }
            }
        }

        this.logMsg("Read Loop Stopped. Closing Serial Port.");
    }

    async cpVersion() {
        // TODO: Actually detect CircuitPython. We may not use this or use if for version only.
        // Or add it to the REPL lib. We should have it return the version number and return null
        // if not detected

        // Some of the ideas for this was for making a comparison between the old CircuitPython Version and new one
        // possibly for checking that we are at a minimum version. Likely it won't be that useful now until we have
        // some issues to investigate in the future.
        return false;
    }

    hasNativeUsb() {
        if (!this.chipFamily || ("esp32").includes(this.chipFamily)) {
            return false;
        }

        // Since most new chips have it, we return true by default.
        return true;
    }
}


customElements.define('cp-install-button', CPInstallButton, {extends: "button"});