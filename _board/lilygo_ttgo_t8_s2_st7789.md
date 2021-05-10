---
layout: download
board_id: "lilygo_ttgo_t8_s2_st7789"
title: "TTGO T8 ESP32-S2 ST7789 Download"
name: "TTGO T8 ESP32-S2 ST7789"
manufacturer: "LILYGO"
board_url: "http://www.lilygo.cn/prod_view.aspx?TypeId=50033&Id=1321"
board_image: "lilygo_ttgo_t8_s2_st7789.jpg"
features:
  - Wi-Fi
  - Display 
  - Battery Charging
---

**Features & Specifications:**
 - ESP32-S2 240MHz Tensilica processor
 - Wi-Fi 802.11 b/g/n 2.4GHz
 - 4MB FLASH
 - 8MB PSRAM
 - 1.14" ST7789 Display
 - microSD card slot
 - built in battery charging, 2-pin 1.25mm JST connector
 - on/off power switch
 - reset and boot button
 - onboard 32.768kHz crystal oscillator
 - USB type-C connector

**Schematic:**
- [LILYGO Github repository](https://github.com/Xinyuan-LilyGO/LilyGo-T-Display-S2)

**Board compatibility:**

This image is working on the TTGO T8 ESP32-S2 V1.1 as well.
It's basically the same board as the st7789 just without the display.

To flash this image use this command:

esptool.py  --chip esp32s2 --port (COMPORT) --baud 115200 write_flash 0x000 "adafruit-circuitpython-lilygo_ttgo_t8_s2_st7789-xx_XX-6.2.0.bin"

After flashing change the dip switches to OTG mode, when reconnected you should see the CIRCUITPY drive.

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
