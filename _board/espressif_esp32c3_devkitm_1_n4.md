---
layout: download
board_id: "espressif_esp32c3_devkitm_1_n4"
title: "ESP32-C3-DevKitM-1-N4 Download"
name: "ESP32-C3-DevKitM-1-N4"
manufacturer: "Espressif"
board_url:
 - "https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitm-1.html"
board_image: "espressif_esp32c3_devkitm_1_n4.jpg"
date_added: 2022-02-14
family: esp32c3
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

The ESP32-C3-DevKitM-1 is an entry-level **RISC V** development board equipped with the ESP32-C3-MINI-1-N4, a powerful, generic Wi-Fi + Bluetooth LE MCU module that features a rich set of peripherals, yet an optimized size. It's an ideal choice for a wide variety of application scenarios related to the Internet of Things (IoT), such as embedded systems, smart homes, wearable electronics, etc. ESP32-C3-DevKitM-1 comes with a PCB antenna. **This version is equipped with the ESP32-C3-MINI-1-N4 with 4MB SPI Flash and no PSRAM.**

**Please note:** The C**3** is *similar* to the ESP32 - but uses **RISC V** as a core, not Tensilica, and has Bluetooth LE (not classic!) However, there is minimal support for this dev board. For example, as of the time of this writing, there is no CircuitPython support - only Arduino and ESP IDF! Please purchase if you're doing development with the C3, and recognize that it's a different core than the classic ESP32s most folks have used.

Most of the I/O pins on the module are broken out to the pin headers on both sides of this board for easy interfacing. Developers can either connect peripherals with jumper wires or mount ESP32-C3-DevKitM-1 on a breadboard.

At the core of the module is ESP32-C3, which has a 32-bit RISC-V single-core processor. The ESP32-C3 integrates a rich set of peripherals, ranging from UART, I2C, I2S, remote control peripheral, LED PWM controller, general DMA controller, TWAI controller, USB Serial/JTAG controller, temperature sensor, and ADC. It also includes SPI, Dual SPI, and Quad SPI interfaces.

There are three mutually exclusive ways to provide power to the board:

- Micro-USB Port, default power supply
- 5V and GND pin headers
- 3V3 and GND pin headers

It is recommended to use the first option: Micro-USB Port.

**Components:**

- **ESP32-C3-MINI-1-N4**: ESP32-C3-MINI-1-N4 from Espressif is a powerful and general-purpose RISC V module that offers Wi-Fi and Bluetooth LE coexistence. It has a PCB antenna and 4 MB SPI flash.
- **5V to 3.3V LDO**: Power regulator that converts a 5V supply into a 3.3V output.
- **5V Power On LED**: Turns on when the USB power is connected to the board.
- **Pin Headers**: All available GPIO pins (except for the SPI bus for flash) are broken out to the pin headers on the board for easy interfacing and programming. For details, please see [Header Block](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitm-1.html#user-guide-c3-devkitm-1-v1-header-blocks).
- **Micro-USB Port**: USB interface. Power supply for the board as well as the communication interface between a computer and the ESP32-C3 chip.
- **Boot Button**: Download button. Holding down **Boot** and then pressing **Reset** initiates Firmware Download mode for downloading firmware through the serial port.
- **Reset Button:** Press this button to restart the system.
- **USB-to-UART Bridge:** Single USB-to-UART bridge chip provides transfer rates up to 3 Mbps.
- **RGB LED**: Addressable RGB LED, driven by GPIO8.

## Purchase

* [DigiKey](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-C3-DEVKITM-1/13684315)
