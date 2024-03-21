---
layout: download
board_id: "espressif_esp32s3_devkitc_1_n8r8"
title: "ESP32-S3-DevKitC-1-N8R8 Download"
name: "ESP32-S3-DevKitC-1-N8R8"
manufacturer: "Espressif"
board_url:
 - "https://www.adafruit.com/product/5336"
board_image: "espressif_esp32s3_devkitc_1.jpg"
date_added: 2022-01-15
family: esp32s3
bootloader_id: espressif_esp32s3_devkitc_1
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

The ESP32-S3-DevKitC-1 is an entry-level development board equipped with ESP32-S3-WROOM-1, a general-purpose Wi-Fi + Bluetooth LE MCU module that integrates complete Wi-Fi and Bluetooth LE functions. **This version is equipped with the ESP32-S3-WROOM-1 (PCB antenna) with 8MB Flash and 8MB PSRAM.**

Most of the I/O pins on the module are broken out to the pin headers on both sides of this board for easy interfacing. Developers can either connect peripherals with jumper wires or mount ESP32-S3-DevKitC-1 on a breadboard. We particularly like that there's a debug UART/USB port and a separate native USB port, so you can upload/debug/USB all at once.

At the core of the module is an ESP32-S3FN8, an Xtensa® 32-bit LX7 CPU that operates at up to 240 MHz. You can power off the CPU and make use of the low-power co-processor to constantly monitor the peripherals for changes or crossing of thresholds.

ESP32-S3FN8 integrates a rich set of peripherals including SPI, LCD, Camera interface, UART, I2C, I2S, remote control, pulse counter, LED PWM, USB Serial/Jtag, MCPWM, SDIO host, GDMA, TWAI® controller (compatible with ISO 11898-1, i.e. CAN Specification 2.0), ADC, touch sensor, temperature sensor, timers, and watchdogs, as well as up to 45 GPIOs. It also includes a full-speed USB 1.1 On-The-Go (OTG) interface to enable USB communication

There are three mutually exclusive ways to provide power to the board:

- USB-to-UART Port and ESP32-S3 USB Port (either one or both), default power supply (recommended)
- 5V and G (GND) pins
- 3v3 and G (GND) pins

**Components:**

- **ESP32-S3-WROOM-1**: ESP32-S3-WROOM-1 is a powerful, generic Wi-Fi + Bluetooth LE MCU module that has a rich set of peripherals. It provides acceleration for neural network computing and signal processing workloads. ESP32-S3-WROOM-1 comes with a PCB antenna.
- **5V to 3.3V LDO**: Power regulator that converts a 5V supply into a 3.3V output.
- **Pin Headers**: All available GPIO pins (except for the SPI bus for flash) are broken out to the pin headers on the board for easy interfacing and programming. For details, please see [Header Block](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html#user-guide-s3-devkitc-1-v1-header-blocks).
- **USB-to-UART Port**: A Micro-USB port used for power supply to the board, for flashing applications to the chip, as well as for communication with the chip via the on-board USB-to-UART bridge.
- **Native ESP32-S3 USB Port**: ESP32-S3 full-speed USB OTG interface, compliant with the USB 1.1 specification. The interface is used for power supply to the board, for flashing applications to the chip, for communication with the chip using USB 1.1 protocols, as well as for JTAG debugging.
- **Boot Button**: Download button. Holding down **Boot** and then pressing **Reset** initiates Firmware Download mode for downloading firmware through the serial port.
- **Reset Button**
- **USB-to-UART Bridge:** Single USB-to-UART bridge chip provides transfer rates up to 3 Mbps.
- **RGB LED**: Addressable RGB LED, driven by GPIO48.
- **3.3V Power On LED**: Turns on when the USB power is connected to the board.

## Purchase

* [Adafruit](https://www.adafruit.com/product/5336)
