---
layout: download
board_id: "lilygo_ttgo_t8_s2_st7789"
title: "TTGO T8 ESP32-S2 ST7789 Download"
name: "TTGO T8 ESP32-S2 ST7789"
manufacturer: "LILYGO"
board_url: "http://www.lilygo.cn/prod_view.aspx?TypeId=50033&Id=1321"
board_image: "lilygo_ttgo_t8_s2_st7789.jpg"
date_added:
family: esp32s2
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

 - ESP32-S2 240 MHz Tensilica processor
 - Wi-Fi 802.11 b/g/n 2.4 GHz
 - 4 MB FLASH
 - 8 MB PSRAM
 - 1.14" ST7789 Display
 - microSD card slot
 - built in battery charging, 2-pin 1.25 mm JST connector
 - on/off power switch
 - reset and boot button
 - onboard 32.768 kHz crystal oscillator
 - USB-C connector

## Schematic
- [LILYGO Github repository](https://github.com/Xinyuan-LilyGO/LilyGo-T-Display-S2)

## Board compatibility

This image is working on the TTGO T8 ESP32-S2 V1.1 as well.
It's basically the same board as the ST7789 just without the display.

To flash this image use this command:

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
