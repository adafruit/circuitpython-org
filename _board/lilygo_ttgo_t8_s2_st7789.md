---
layout: download
board_id: "lilygo_ttgo_t8_s2_st7789"
title: "TTGO T8 ESP32-S2 ST7789 Download"
name: "TTGO T8 ESP32-S2 ST7789"
manufacturer: "LILYGO"
board_url:
 - "http://www.lilygo.cn/prod_view.aspx?TypeId=50033&Id=1321"
board_image: "lilygo_ttgo_t8_s2_st7789.jpg"
date_added: 2021-02-14
family: esp32s2
bootloader_id: lilygo_ttgo_t8_s2_st7789
features:
  - Wi-Fi
  - Display
  - Battery Charging
  - USB-C
  - Breadboard-Friendly
---

The TTGO T8 ESP32-S2 development board has a ST7789 display and other useful features which allows one to create a variety of projects.

The display has native CircuitPython support.

## Features & Specifications

* ESP32-S2 240 MHz Tensilica processor
* Wi-Fi 802.11 b/g/n 2.4 GHz
* 4 MB FLASH
* 8 MB PSRAM
* 1.14" ST7789 Display (Resolution: 240 x 135)
* microSD card slot
* built in battery charging, 2-pin 1.25 mm JST connector
* on/off power switch
* reset and boot button
* onboard 32.768 kHz crystal oscillator
* USB-C connector

## Schematic

* [LILYGO Github repository](https://github.com/Xinyuan-LilyGO/LilyGo-T-Display-S2)

## Setup

To flash this image, use this command:

```sh
esptool.py  --chip esp32s2 --port (COMPORT) --baud 115200 write_flash 0x000 \
  adafruit-circuitpython-lilygo_ttgo_t8_s2_st7789-xx_XX-X.Y.Z.bin
```

After flashing change the DIP switches (the ones closer to the USB-C connector) to OTG mode, when reconnected you should see the CIRCUITPY drive.

```text
USB        OTG

On         On
o   o        o   o
  o   o    o   o
1 2 3 4    1 2 3 4
```

## Purchase

* [AliExpress - LILYGO store](https://www.aliexpress.com/item/4001211703708.html)
