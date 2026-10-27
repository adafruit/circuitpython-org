---
layout: download
board_id: "adafruit_metro_esp32p4"
title: "Metro ESP32-P4 Download"
name: "Metro ESP32-P4"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/6536"
board_image: "adafruit_metro_esp32p4.jpg"
# format is YYYY-MM-DD
date_added: 2026-10-27
family: esp32p4
bootloader_id: adafruit_metro_esp32p4
download_instructions: https://learn.adafruit.com/adafruit-metro-esp32-p4-hydra/install-circuitpython
features:
  - Wi-Fi
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Arduino Shield Compatible
  - OSHWA Certified
---

The METRO series just keeps getting faster and better, now powered with the ESP32-P4! This beast is a dual-core 360 MHz RISC-V CPU featuring AI instruction extensions, an advanced memory subsystem, and integrated new high-speed peripherals like MIPI DSI and CSI. According to Espressif, the P4 is tailored for high-performance applications demanding robust security and bumps the performance of their ESP32 line to 'single-board computing' levels. Given it's high speed, massive pin-count, and display/camera integration plus lots of SRAM/PSRAM/Flash memory, the ESP32-P4 is excellent for Human-Machine Interfaces, efficient edge computing, and increased IO-connectivity demands.

This board features a ESP32-P4 with the stock 768 KB L2 cache/SRAM, plus external <b>16 MB of QSPI NOR Flash</b> and <b>16 MB of PSRAM</b>.

<b>PLEASE NOTE:</b> This is <b>NOT</b> the ESP32-P4X chip, we are currently shipping with "v1" chips, if you need the "v3" P4X do not purchase this item!

The chip itself features ([Espressif specifications](https://documentation.espressif.com/esp32-p4_datasheet_en.html)):

* <b>Dual-core 32-bit RISC-V processor</b>, up to <b>360 MHz</b>.
* Separate <b>40 MHz low-power RISC-V core</b>.
* <b>768 KB high-performance SRAM</b>, plus <b>32 KB low-power SRAM</b>.
* <b>32 MB PSRAM</b> internally
* <b>Two-lane MIPI DSI</b> display and <b>two-lane MIPI CSI</b> camera interfaces.
* Hardware H.264 encoding, JPEG encoding/decoding, image processing, and pixel acceleration.
* Full-Speed USB OTG, and USB Serial/JTAG. (Main USB-C port)
* Separate 480 Mbps USB 2.0 High-Speed OTG (Secondary USB-A host port)
* UART, SPI, I²C, I3C, I²S, PWM, ADC, touch sensing, SD/MMC, CAN/TWAI, and Ethernet MAC peripherals.
* Hardware cryptography, secure boot, and flash encryption.

Our <b>Metro ESP32-P4 Hydra</b> brings that into a board with:

* <b>16 MB NOR flash</b>
* <b>ESP32-C6 wireless coprocessor</b> ([C6 specifications](https://www.espressif.com/sites/default/files/documentation/esp32-c6-mini-1_mini-1u_datasheet_en.pdf)), connected over SDIO for high speed WiFi access, the C6 radio also supports <b>Bluetooth LE 5.3, Thread, and Zigbee</b> but interfacing firmware may be required to expose that.  The C6 can also be reprogrammed over GPIO connected to the P4
* <b>USB-C</b> for power, programming, serial debugging, and <b>TinyUF2</b> drag-and-drop firmware update support
* <b>USB-A High-Speed host port</b>, with software-controlled power and a dedicated 5 V boost supply for battery operation, with on/off control
* Separate <b>22-pin, 0.5 mm-pitch MIPI display and camera connectors</b>, each carrying two data lanes. These follow the "Raspberry Pi" format with 2 lanes exposed for connecting off-the-shelf cameras and displays
* <b>microSD socket</b> using <b>four-bit SDIO</b>
* <b>Metro/Arduino Uno-style headers</b> with D0–D13, six analog inputs, I2C/I3C, and a separate six-pin SPI header - all GPIO uses <b>3.3 V logic</b>
* <b>STEMMA QT connector</b> for I2C/I3C sensors and accessories
* <b>Variety of Power options: 7–12 V DC</b> barrel-jack input, USB C power, or a <b>single-cell LiPo</b> battery connector with battery-voltage monitoring, onboard charging & charging/status indicators
* On/Off power switch
* <b>RGB NeoPixel</b>, separate D13 user LED, and <b>Reset</b> and <b>Boot</b> buttons (for entering the ROM bootloader)
* Dedicated hardware/ROM <b>UART</b> debugging connection

## Purchase
Add any links to purchase the board
* [Adafruit](https://www.adafruit.com/product/6536)
