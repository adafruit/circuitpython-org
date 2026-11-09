---
layout: download
board_id: "generic_esp32s3_supermini"
title: "Generic ESP32S3 SuperMini Download"
name: "Generic ESP32S3 SuperMini"
manufacturer: "Generic"
board_url: "https://www.espboards.dev/esp32/esp32-s3-super-mini/"
board_image: "generic_esp32s3_supermini.jpg"
date_added: 2026-10-13
family: esp32s3
bootloader_id: generic_esp32s3_super_mini
downloads_display: true
features:
  - USB-C
  - Breadboard-Friendly
  - Wi-Fi
  - Battery Charging
  - Castellated Pads
---

This is a tiny ESP32S3 board exposing a wealth of GPIO connections -- 35 in total.  It has 4MB Flash and 2MB PSRAM.  It is available at a number of sites without a listed manufacturer which is why it is listed as a Generic ESP32S3 Supermini.

**Variant Note:** Please note that there are multiple variants of this Generic board.  The variants marked with a version number commonly `HW747 V0.0.2` have a different Neopixel order of `RGB` instead of the more common `GRB`.  See a more detailed note below.  There is even an early variant with 8M Flash and no PSRAM.

 * ESP32-S3FH4R2 dual-core Xtensa® 32-bit LX7 processor - up to 240MHz
 * USB Type-C Port
 * WS2812 RGB LED
 * BOOT button
   Press it and then press the RESET button to enter download mode
 * RESET button
 * 35 GPIO contacts (15 available on breadboard friendly castelated edges, 20 on the bottom of the board through exposed pads)
 * 2.4G ceramic antenna
   * Supports 2.4GHz Wi-Fi (802.11 b/g/n) and Bluetooth® 5 (LE)
 * Built in 512KB of SRAM and 384KB ROM, onboard 4MB Flash memory and 2MB PSRAM
 * Castellated module and onboard ceramic antenna, allows soldering direct to carrier boards
 * Supports flexible clock, module power supply independent setting, and other controls to realize low power consumption in different scenarios

## Learn more
For more information please see the [ESPboards blog page](https://www.espboards.dev/esp32/esp32-s3-super-mini/)

## Purchase

* [Aliexpress](https://www.aliexpress.us/item/3256810386456708.html)
* [Amazon](https://www.amazon.com/DWEII-Development-Ultra-Small-ESP32-S3FH4R2-Micropython/dp/B0GRNC5MFC)
* [esp32s.com](https://esp32s.com/product/esp32-s3-supermini-development-board/)

Amazon search in case previous link doesn't work (may pick up XIAO and others which is are different boards so read carefully):

[Amazon search ESP32S3 Supermini](https://www.amazon.com/s?k=esp32s3+supermini)

## Alternate RGB order V0.0.2 variant note

A variant of this board more commonly available from various sellers on Amazon commonly marked `HW747 V0.0.2` uses the less common Neopixel order `RGB` instead of `GRB`.  The result of this is that the UF2 Bootloader will indicate bootloader mode with a red pixel rather than the normal green and when initializing the Neopixel library you will need to pass `pixel_order="RGB"` as a parameter.  Additionally some of CircuitPython's status indications may have the color switched.

The latest releases of CircuitPython in the 11.0.x series have a settings.toml variable to correct the operation of the CircuitPython's status displays for these boards.

```
CIRCUITPY_BOARD_VARIANT="rgb_led"
``` 

However the UF2 Bootloader will still indicate red rather than green and you must define `pixel_order="RGB"` when initializing Neopixel in your code.

