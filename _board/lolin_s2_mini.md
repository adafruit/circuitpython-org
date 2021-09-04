---
layout: download
board_id: "lolin_s2_mini"
title: "LOLIN S2 Mini Download"
name: "LOLIN S2 Mini "
manufacturer: "LOLIN"
board_url: "https://www.wemos.cc/en/latest/s2/s2_mini.html"
board_image: "lolin_s2_mini.jpg"
date_added: 2021-9-3
features:
  - Wi-Fi
---

### Features

- ESP32-S2FN4R2 WiFi SoC
- USB Type-C connector, for built-in ROM USB bootloader & serial port debugging
- 4MB Flash
- 2MB PSRAM
- 27x IO
- ADC, DAC, I2C, SPI, UART, USB OTG
- Compatible with LOLIN D1 mini shields
- Compatible with CircuitPython, MicroPython, Arduino and ESP-IDF
- Default firmware: MicroPython

### Flashing UF2 Bootloader

***Important***: *this will erase previously flashed firmware & sketches from the board.*

- Download the latest `tinyuf2-lolin_s2_mini-......zip` from [TinyUF2 releases](https://github.com/adafruit/tinyuf2/releases),
    - Unzip to find `combined.bin`.
- Place board in bootloader mode:
    - Plug board into a USB port on your computer using a data/sync cable. Make sure it is the only board plugged in, and that a charge-only cable is not being used.
    - Press and hold the `0` button down. Don't let go of it yet!
    - Press and release the `RST` button. You should have the `0` button pressed while you do this.
    - Release the `0` button.
- Use the Adafruit WebSerial ESPTool to upload `combined.bin` (Google Chrome 89 or newer):
    - Open a new web browser window or tab to the [Adafruit WebSerial ESPTool](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/)
    - Select *460800 Baud* from the pull-down menu at the top-right of the page.
    - Click the *Connect* button at the top-right of the page.
    - Select the COM or Serial port from the pop-up window.
    - After successful connection, click the `Erase` button.
    - After successful erase, click the first `Choose a file...` button, locate the `combined.bin` file unzipped earlier, click `Ok`.
    - After successfully choosing the `combined.bin` file, click the `Program` button.
    - After the TinyUF2 firmware update is complete, press the `RST` button. A new drive `S2MINIBOOT` should be visible in your file browser.

### Flashing CircuitPython

- Flash the UF2 bootloader using the instruction above.
- Download the `.UF2` file from this page.
- Drag & Drop the `.UF2` file to the `S2MINIBOOT` drive.

## Purchase

* [AliExpress](https://www.aliexpress.com/item/1005003145192016.html)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
