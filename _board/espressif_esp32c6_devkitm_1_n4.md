---
layout: download
board_id: "espressif_esp32c6_devkitm_1_n4"
title: "ESP32-C6-DevKitC-1-N4 Download"
name: "ESP32-C6-DevKitC-1-N4"
manufacturer: "Espressif"
board_url:
 - "https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitm-1/user_guide.html"
board_image: "espressif_esp32c6_devkitc_1.jpg"
date_added: 2023-10-27
family: esp32c6
bootloader_id: espressif_esp32c6_devkitc_1
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

The **ESP32-C6-DevKitC-1-N4** is an entry-level development board equipped with ESP32-C6-WROOM-1, a general-purpose Wi-Fi + Bluetooth LE RISC-V MCU module that integrates complete Wi-Fi and Bluetooth LE functions. This board integrates complete Wi-Fi, Bluetooth LE, Zigbee, and Thread functions.

**This version is equipped with the ESP32-C6-WROOM-1 with 4MB Flash.**

Most of the I/O pins on the module are broken out to the pin headers on both sides of this board for easy interfacing. Developers can either connect peripherals with jumper wires or mount ESP32-C6-DevKitC-1-N8 on a breadboard. We particularly like that there's a debug UART/USB port and a separate native USB port, so you can upload/debug/USB all at once.

At the core of the modules is an ESP32-C6, a RISC-V 32-bit single-core CPU that operates at up to 160 MHz. You can power off the CPU and make use of the low-power co-processor to constantly monitor the peripherals for changes or crossing of thresholds. ESP32-C6 integrates a rich set of peripherals including SPI, LCD, Camera interface, UART, I2C, I2S, remote control, pulse counter, LED PWM, USB Serial/JTAG controller, MCPWM, SDIO host, GDMA, TWAI® controller (compatible with ISO 11898-1), ADC, touch sensor, temperature sensor, timers, and watchdogs, as well as up to 45 GPIOs. It also includes a full-speed USB 1.1 On-The-Go (OTG) interface to enable USB communication

There are three mutually exclusive ways to provide power to the board:

- USB Type-C to UART Port, default power supply
- 5V and GND pin headers
- 3V3 and GND pin headers

It is recommended to use the first option: USB Type-C to UART Port.

**Components:**

- **ESP32-C6-WROOM-1**: ESP32-C6-WROOM-1 is a general-purpose module supporting Wi-Fi 6, Bluetooth 5, and IEEE 802.15.4 (Zigbee 3.0 and Thread). This module is built around the ESP32-C6 chip, and comes with a PCB antenna and 4 MB SPI flash.
- **5V to 3.3V LDO**: Power regulator that converts a 5V supply into a 3.3V output.
- **3.3V Power On LED**: Turns on when the USB power is connected to the board.
- **Pin Headers**: All available GPIO pins (except for the SPI bus for flash) are broken out to the pin headers on the board for easy interfacing and programming. For details, please see [Header Block](https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitm-1/user_guide.html#hardware-reference).
- **USB-to-UART Port**: Single USB-to-UART bridge chip provides transfer rates up to 3 Mbps.
- **ESP32-C6 USB Type-C Port**: The USB Type-C port on the ESP32-C6 chip is compliant with USB 2.0 full speed. It is capable of up to 12 Mbps transfer speed (Note that this port does not support the faster 480 Mbps high-speed transfer mode).
- **Boot Button**: Download button. Holding down **Boot** and then pressing **Reset** initiates Firmware Download mode for downloading firmware through the serial port.
- **Reset Button:** Press this button to restart the system.
- **USB-to-UART Bridge:** Used for power supply to the board, as well as the communication with the ESP32-C6 chip via the on-board USB-to-UART bridge.
- **RGB LED**: Addressable RGB LED, driven by GPIO8.
- **J5**: Used for current measurement. See details in Section [Current Measurement](https://espressif-docs.readthedocs-hosted.com/projects/espressif-esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide_v1.1.html#user-guide-c6-devkitc-1-v1-current).

## Purchase

* [DigiKey](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-C6-DEVKITM-1-N4/18667011)
