'use strict';
import {html, render} from 'https://unpkg.com/lit-html?module';
import {asyncAppend} from 'https://unpkg.com/lit-html/directives/async-append?module';
import * as esptoolPackage from "https://unpkg.com/esp-web-flasher@5.1.2/dist/web/index.js?module"

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

export const ESP_ROM_BAUD = 115200;

export class InstallButton extends HTMLButtonElement {
    static isSupported = 'serial' in navigator;
    static isAllowed = window.isSecureContext;

    constructor() {
        super();
        this.dialogElements = {};
        this.currentFlow = null;
        this.currentStep = 0;
        this.currentDialogElement = null;
        this.port = null;
        this.espStub = null;
        this.dialogCssClass = "install-dialog";
        this.connected = this.connectionStates.DISCONNECTED;
    }

    init() {
        this.preloadDialogs();
    }

    // Define some common buttons
    /* Buttons should have a label, and a callback and optionally a condition function on whether they should be enabled */
    previousButton = {
        label: "Previous",
        onClick: this.prevStep,
        isEnabled: async () => { return this.currentStep > 0 },
    }

    nextButton = {
        label: "Next",
        onClick: this.nextStep,
        isEnabled: async () => { return this.currentStep < this.currentFlow.steps.length - 1; },
    }

    closeButton = {
        label: "Close",
        onClick: async (e) => {
            this.closeDialog();
        },
    }

    // Default Buttons
    defaultButtons = [this.previousButton, this.nextButton];

    // States and Button Labels
    connectionStates = {
        DISCONNECTED: "Connect",
        CONNECTING: "Connecting...",
        CONNECTED: "Disconnect",
    }

    dialogs = {
        notSupported: {
            preload: false,
            closeable: true,
            template: (data) => html`
                Sorry, <b>Web Serial</b> is not supported on your browser at this time. Browsers we expect to work:
                <ul>
                <li>Google Chrome 89 (and higher)</li>
                <li>Microsoft Edge 89 (and higher)</li>
                <li>Opera 75 (and higher)</li>
                </ul>
            `,
            buttons: [this.closeButton],
        },
        menu: {
            closeable: true,
            template: (data) => html`
                <p>CircuitPython Installer for ${data.boardName}</p>
                <ul class="flow-menu">
                ${asyncAppend(this.generateMenu(
                    (flowId, flow) => html`<li><a href="#" @click=${this.runFlow.bind(this)} id="${flowId}">${flow.label.replace('[version]', this.releaseVersion)}</a></li>`
                ))}
                </ul>`,
            buttons: [this.closeButton],
        },
    };

    flows = {};

    baudRates = [
        115200,
        128000,
        153600,
        230400,
        460800,
        921600,
        1500000,
        2000000,
    ];

    connectedCallback() {
        if (InstallButton.isSupported && InstallButton.isAllowed) {
            this.toggleAttribute("install-supported", true);
        } else {
            this.toggleAttribute("install-unsupported", true);
        }

        this.addEventListener("click", async (e) => {
            e.preventDefault();
            // WebSerial feature detection
            if (!InstallButton.isSupported) {
                await this.showNotSupported();
            } else {
                await this.showMenu();
            }
        });
    }

    // Parse out the url parameters from the current url
    getUrlParams() {
        // This should look for and validate very specific values
        var hashParams = {};
        if (location.hash) {
            location.hash.substr(1).split("&").forEach(function(item) {hashParams[item.split("=")[0]] = item.split("=")[1];});
        }
        return hashParams;
    }

    // Get a url parameter by name and optionally remove it from the current url in the process
    getUrlParam(name) {
        let urlParams = this.getUrlParams();
        let paramValue = null;
        if (name in urlParams) {
            paramValue = urlParams[name];
        }

        return paramValue;
    }

    async enabledFlowCount() {
        let enabledFlowCount = 0;
        for (const [flowId, flow] of Object.entries(this.flows)) {
            if (await flow.isEnabled()) {
                enabledFlowCount++;
            }
        }
        return enabledFlowCount;
    }

    async * generateMenu(templateFunc) {
        if (await this.enabledFlowCount() == 0) {
            yield html`<li>Coming soon. Check back later.</li>`;
            //yield html`<li>No installable options available for this board.</li>`;
        }
        for (const [flowId, flow] of Object.entries(this.flows)) {
            if (await flow.isEnabled()) {
                yield templateFunc(flowId, flow);
            }
        }
    }

    preloadDialogs() {
        for (const [id, dialog] of Object.entries(this.dialogs)) {
            if ('preload' in dialog && !dialog.preload) {
                continue;
            }
            this.dialogElements[id] = this.getDialogElement(dialog);
        }
    }

    createIdFromLabel(text) {
        return text.replace(/^[^a-z]+|[^\w:.-]+/gi, "");
    }

    createDialogElement(id, dialogData) {
        // Check if an existing dialog with the same id exists and remove it if so
        let existingDialog = this.querySelector(`#cp-installer-${id}`);
        if (existingDialog) {
            this.remove(existingDialog);
        }

        // Create a dialog element
        let dialogElement = document.createElement("dialog");
        dialogElement.id = id;
        dialogElement.classList.add(this.dialogCssClass);

        // Add a close button
        let closeButton = document.createElement("button");
        closeButton.href = "#";
        closeButton.classList.add("close-button");
        closeButton.addEventListener("click", (e) => {
            e.preventDefault();
            dialogElement.close();
        });
        dialogElement.appendChild(closeButton);

        // Add a body element
        let body = document.createElement("div");
        body.classList.add("dialog-body");
        dialogElement.appendChild(body);

        let buttons = this.defaultButtons;
        if (dialogData && dialogData.buttons) {
            buttons = dialogData.buttons;
        }

        dialogElement.appendChild(
            this.createNavigation(buttons)
        );

        // Return the dialog element
        document.body.appendChild(dialogElement);
        return dialogElement;
    }

    createNavigation(buttonData) {
        // Add buttons according to config data
        const navigation = document.createElement("div");
        navigation.classList.add("dialog-navigation");

        for (const button of buttonData) {
            let buttonElement = document.createElement("button");
            buttonElement.innerText = button.label;
            buttonElement.id = this.createIdFromLabel(button.label);
            buttonElement.addEventListener("click", async (e) => {
                e.preventDefault();
                await button.onClick.bind(this)();
            });
            buttonElement.addEventListener("update", async (e) => {
                if ("onUpdate" in button) {
                    await button.onUpdate.bind(this)(e);
                }
                if ("isEnabled" in button) {
                    e.target.disabled = !(await button.isEnabled.bind(this)());
                }
            });

            navigation.appendChild(buttonElement);
        }

        return navigation;
    }

    getDialogElement(dialog, forceReload = false) {
        function getKeyByValue(object, value) {
            return Object.keys(object).find(key => object[key] === value);
        }

        const dialogId = getKeyByValue(this.dialogs, dialog);

        if (dialogId) {
            if (dialogId in this.dialogElements && !forceReload) {
                return this.dialogElements[dialogId];
            } else {
                return this.createDialogElement(dialogId, dialog);
            }
        }
        return null;
    }

    updateButtons() {
        // Call each button's custom update event for the current dialog
        if (this.currentDialogElement) {
            const navButtons = this.currentDialogElement.querySelectorAll(".dialog-navigation button");
            for (const button of navButtons) {
                button.dispatchEvent(new Event("update"));
            }
        }
    }

    showDialog(dialog, templateData = {}) {
        if (this.currentDialogElement) {
            this.closeDialog();
        }

        this.currentDialogElement = this.getDialogElement(dialog);
        if (!this.currentDialogElement) {
            console.error(`Dialog not found`);
        }

        if (this.currentDialogElement) {
            const dialogBody = this.currentDialogElement.querySelector(".dialog-body");
            if ('template' in dialog) {
                render(dialog.template(templateData), dialogBody);
            }

            // Close button should probably hide during certain steps such as flashing and erasing
            if ("closeable" in dialog && dialog.closeable) {
                this.currentDialogElement.querySelector(".close-button").style.display = "block";
            } else {
                this.currentDialogElement.querySelector(".close-button").style.display = "none";
            }

            let dialogButtons = this.defaultButtons;
            if ('buttons' in dialog) {
                dialogButtons = dialog.buttons;
            }

            this.updateButtons();
            this.currentDialogElement.showModal();
        }
    }

    closeDialog() {
        this.currentDialogElement.close();
        this.currentDialogElement = null;
    }

    errorMsg(text) {
        text = this.stripHtml(text);
        console.error(text);
        this.showError(text);
    }

    logMsg(text, showTrace = false) {
        // TODO: Eventually add to an internal log that the user can bring up
        console.info(this.stripHtml(text));
        if (showTrace) {
            console.trace();
        }
    }

    updateEspConnected(connected) {
        if (Object.values(this.connectionStates).includes(connected)) {
            this.connected = connected;
            this.updateButtons();
        }
    }

    stripHtml(html) {
        let tmp = document.createElement("div");
        tmp.innerHTML = html;
        return tmp.textContent || tmp.innerText || "";
    }

    formatMacAddr(macAddr) {
        return macAddr.map((value) => value.toString(16).toUpperCase().padStart(2, "0")).join(":");
    }

    async disconnect() {
        if (this.espStub) {
            await espStub.disconnect();
            await espStub.port.close();
            this.updateUIConnected(this.connectionStates.DISCONNECTED);
            this.espStub = null;
        }
    }

    async runFlow(flow) {
        if (flow instanceof Event) {
            flow.preventDefault();
            flow.stopImmediatePropagation();
            if (flow.target.id in this.flows) {
                flow = this.flows[flow.target.id];
            } else {
                return;
            }
        }

        this.currentFlow = flow;
        this.currentStep = 0;
        await this.currentFlow.steps[this.currentStep].bind(this)();
    }

    async nextStep() {
        if (!this.currentFlow) {
            return;
        }

        if (this.currentStep < this.currentFlow.steps.length) {
            this.currentStep++;
            await this.currentFlow.steps[this.currentStep].bind(this)();
        }
    }

    async prevStep() {
        if (!this.currentFlow) {
            return;
        }

        if (this.currentStep > 0) {
            this.currentStep--;
            await this.currentFlow.steps[this.currentStep].bind(this)();
        }
    }

    async showMenu() {
        // Display Menu
        this.showDialog(this.dialogs.menu, {boardName: this.boardName});
    }

    async showNotSupported() {
        // Display Not Supported Message
        this.showDialog(this.dialogs.notSupported);
    }

    async showError(message) {
        // Display Menu
        this.showDialog(this.dialogs.error, {message: message});
    }

    async setBaudRateIfChipSupports(chipType, baud) {
        if (baud == ESP_ROM_BAUD) { return } // already the default

        if (chipType == esptoolPackage.CHIP_FAMILY_ESP32) { // only supports the default
            this.logMsg(`ESP32 Chip only works at 115200 instead of the preferred ${baud}. Staying at 115200...`);
            return
        }

        await this.changeBaudRate(baud);
    }

    async changeBaudRate(baud) {
        if (this.espStub && this.baudRates.includes(baud)) {
            await this.espStub.setBaudrate(baud);
        }
    }

    async espHardReset(bootloader = false) {
        if (this.espStub) {
            await this.espStub.hardReset(bootloader);
        }
    }

    async espConnect(logger) {
        // - Request a port and open a connection.
        this.port = await navigator.serial.requestPort();

        logger.log("Connecting...");
        await this.port.open({ baudRate: ESP_ROM_BAUD });

        logger.log("Connected successfully.");

        return new esptoolPackage.ESPLoader(this.port, logger);
    };
}