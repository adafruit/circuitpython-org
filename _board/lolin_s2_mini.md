---
layout: download
board_id: "lolin_s2_mini"
title: "LOLIN S2 Mini Download"
name: "LOLIN S2 Mini"
manufacturer: "LOLIN"
board_url: "https://www.wemos.cc/en/latest/s2/s2_mini.html"
board_image: "lolin_s2_mini.jpg"
date_added: 2021-9-3
features:
  - Wi-Fi
  - USB-C
---

### Features

- ESP32-S2FN4R2 WiFi SoC
    - Xtensa® single-core 32-bit LX7 microprocessor, up to 240 MHz
    - 320 KB SRAM
    - 4 MB Flash
    - 2 MB PSRAM
    - 2 × 13-bit SAR ADCs, up to 20 channels (2 channels not available on ADC2 due to USB)
    - 2 × 8-bit DAC
    - 14 × touch sensing IOs
    - 4 × SPI (2 useable due to embedded flash & psram)
    - 1 × I2S
    - 2 × I2C
    - 2 × UART
    - 1 × DVP 8/16 camera interface, implemented using the hardware resources of I2S
    - 1 × LCD interface (8-bit serial RGB/8080/6800), implemented using the hardware resources of SPI2
    - 1 × LCD interface (8/16/24-bit parallel), implemented using the hardware resources of I2S
    - 1 × TWAI® controller compatible with ISO 11898-1 (CAN Specification 2.0)
    - LED PWM controller, up to 8 channels
    - USB OTG 1.1 controller and PHY, with host and device support
- USB Type-C connector, for built-in ROM USB bootloader, serial port debugging, and USB device mode
- 27 × GPIO pins, outer 16 pins compatible with LOLIN D1 mini shields
- Compatible with CircuitPython, MicroPython, Arduino and ESP-IDF
- Default firmware: MicroPython

## Purchase

* [AliExpress](https://www.aliexpress.com/item/1005003145192016.html)

## Learn More

* [Manufacturer Specifications](https://www.wemos.cc/en/latest/s2/s2_mini.html)

### Flashing UF2 Bootloader

***Important***: *this will erase previously flashed firmware & sketches from the board, but needs to be perfomed only once.*

- Download the latest `tinyuf2-lolin_s2_mini-......zip` from [TinyUF2 releases](https://github.com/adafruit/tinyuf2/releases),
    - Unzip to find the file `combined.bin`.
- Place board in bootloader mode:
    - Plug board into a USB port on your computer using a data/sync cable. Make sure it is the only board plugged in, and that a charge-only cable is not being used.
    - Press and hold the `0` button down. Don't let go of it yet!
    - Press and release the `RST` button. You should have the `0` button pressed while you do this.
    - Release the `0` button.
- Use the Adafruit WebSerial ESPTool to upload `combined.bin` (Google Chrome 89 or newer):
    - Open a new web browser window or tab to the [Adafruit WebSerial ESPTool](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/).
    - Select `460800 Baud` from the pull-down menu at the top-right of the page.
    - Click the `Connect` button at the top-right of the page.
    - Select the COM or Serial port from the pop-up window.
    - After successful connection, click the `Erase` button.
    - After successful erase, click the first `Choose a file...` button, locate the `combined.bin` file unzipped earlier, click `Ok`.
    - After successfully choosing the `combined.bin` file, click the `Program` button.
    - After the TinyUF2 firmware update is complete, press the `RST` button on the board. A new drive `S2MINIBOOT` should be visible in your file browser.

### Flashing CircuitPython

- Flash the UF2 bootloader using the instructions above.
- Download the `.UF2` file from this page.
- In your file browser, Drag & Drop the `.UF2` file to the `S2MINIBOOT` drive.
- Your board should reboot automatically into CircuitPython. The `S2MINIBOOT` drive should disappear and be replaced with a new drive `CIRCUITPY`.

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
