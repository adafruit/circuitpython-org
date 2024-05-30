---
layout: download
board_id: "autosportlabs_esp32_can_x2"
title: "Autosport Labs ESP32-CAN-X2 Download"
name: "Autosport Labs ESP32-CAN-X2"
manufacturer: "Autosport Labs"
board_url:
 - "https://www.autosportlabs.com/product/esp32-can-x2-dual-can-bus-automotive-grade-development-board/"
 - "https://wiki.autosportlabs.com/ESP32-CAN-X2"
board_image: "autosportlabs_esp32_can_x2.jpg"
date_added: 2024-05-29
family: esp32  # See _data/bootloaders.json
bootloader_id:
features:
  - Arduino Shield Compatible
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - USB-C
  - Wi-Fi
---

The Autosport Labs ESP32-CAN-X2 is a development board designed to make CAN bus communications easy for automotive and industrial applications.

It features the ESP32-S3-WROOM-1-N8R8 using an Xtensa® 32-bit LX7 CPU operating at up to 240 MHz (8MB flash, 8MB PSRAM), dual CAN bus support, two CAN bus transceivers, and an automotive-grade power supply to safely integrate it into your car project.

All IO pins are broken out to a breadboard-friendly layout so you can easily integrate it into bigger projects. A separate connector also provides power, ground, and dual CAN connections so you can quickly wire it into CAN networks.

The two CAN bus networks brings additional possibilities, such as:
  - Bridge two CAN bus networks with different baud rates
  - Collect data from two different CAN bus networks with different baud rates
  - Isolate traffic between CAN networks
  - Create a "man in the middle" agent, which will help identify the source of CAN messages, helpful for CAN bus reverse-engineering efforts

Sample Projects are available to get you started quickly [Example Projects in our Github](https://github.com/autosportlabs/ESP32-CAN-X2)

**Components:**

- **ESP32-S3-WROOM-1-N8R8** microcontroller powerful dual-core Xtensa LX6 CPU running at up to 240 MHz.
- **Automotive grade power supply**: Ruggedized power supply up to 40v input, provides safety for automotive applications where damaging voltage surges and load dumps are common.
- **Pin Headers**: All available GPIO pins are broken out to the pin headers on the board for easy interfacing and programming. For details, please see [our documentation](https://wiki.autosportlabs.com/ESP32-CAN-X2).
- **USB-C port**: A USB-C port supplies power for programming, flashing your code, communications using the USB 1.1 specification, and also provides JTAG debugging.
- **Boot Button**: Firmware download button. Holding down **Boot** and then pressing **Reset** initiates Firmware Download mode for installing firmware.
- **Reset Button**: Resets the device
- **LED**: User controllable LED; use it to indicate status or anything else you would like.
- **Power LED**: Turns on when power is connected to the board.
- **Power / CAN headers**: 6 pin JST-PH header provides 12v (nominal) power, ground, CAN1 and CAN2 connections.
- **CAN termination jumpers**: 2 CAN termination jumpers are provided, default enabled with 120 ohm termination
- **Built-in CAN transceivers**: Dual CAN transceivers are included on board. 
- **2nd CAN bus provided by MCP2515**: while CAN1 uses the built in TWAI CAN compatible controller; CAN2 uses the on-board MCP2515 CAN bus controller.

## Purchase

* [Autosport Labs](https://www.autosportlabs.com/product/esp32-can-x2-dual-can-bus-automotive-grade-development-board/)
* [Example Projects](https://github.com/autosportlabs/ESP32-CAN-X2)
* [Full documentation](https://wiki.autosportlabs.com/ESP32-CAN-X2)
