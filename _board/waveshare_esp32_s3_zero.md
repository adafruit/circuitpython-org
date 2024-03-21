---
board_id: waveshare_esp32_s3_zero
board_image: waveshare_esp32_s3_zero.png
board_url:
- https://www.waveshare.com/esp32-s3-zero.htm
bootloader_id: adafruit_feather_esp32s3
date_added: 2023-10-21 12:00:00
downloads_display: true
family: esp32s3
features:
- Wi-Fi
- USB-C
- Breadboard-Friendly
layout: download
manufacturer: Waveshare
name: Waveshare ESP32-S3-Zero
title: Waveshare ESP32-S3-Zero Download
---

Tiny, but mighty! This board with a powerful ESP32-S3 MCU measures in at 24.8mmx18mm (23.5mm for just the PCB, the USB-C connector sticks out a little bit). Despite it's small size it still exposes a wealth of GPIO connections - a whopping 34 in total. It does however have 'only' 4MB of Flash storage rather than the more typical 8MB found on most ESP32-S3 boards (and even 16MB on some).

 * ESP32-S3FH4R2 dual-core Xtensa® 32-bit LX7 processor - up to 240MHz
 * USB Type-C Port
 * ME6217C33M5G low dropout LDO, 800mA (Max)
 * WS2812 GRB LED (R and G are swapped from their usual order)
 * BOOT button
   Press it and then press the RESET button to enter download mode
 * RESET button
 * 34 GPIO contacts (18 available on breadboard friendly castelated edges, 16 on the bottom of the board through exposed pads)
 * 2.4G ceramic antenna
   * Supports 2.4GHz Wi-Fi (802.11 b/g/n) and Bluetooth® 5 (LE)
   *although CircuitPython at the time of writing does not offer proper Bluetooth supports for ESP32-S3 chips, a NRF52840 based board will serve you better in that regard*
 * Built in 512KB of SRAM and 384KB ROM, onboard 4MB Flash memory and 2MB PSRAM
 * Castellated module and onboard ceramic antenna, allows soldering direct to carrier boards
 * Supports flexible clock, module power supply independent setting, and other controls to realize low power consumption in different scenarios
 * Integrated with USB serial port full-speed controller, 34 × GPIO pins allows flexibly configuring pin functions
   * 4 × SPI, 2 × I2C, 3 × UART, 2 × I2S, 2 × ADC, etc.

*Due to the limited flash memory available on this board it hasn't been 'build' with esp-camera support - if that's something you want to use you'll have to roll your own build and sacrifice some other feature to make space (like the at the moment non-functional bluetooth)*

## Learn more
For more information please see the [Waveshare product page](https://www.waveshare.com/esp32-s3-zero.htm)

*Warning: At the time of writing their product page does contain 2 small mistakes*
It states it has a WS2812 RGB LED on pin 10. It does not.
 1. It's a GRB LED, not RGB. Keep this in mind when trying to use it.
 2. It's on IO21, not 10.

 There's a link reserved for a wiki although currently there's nothing there yet:
https://www.waveshare.com/wiki/ESP32-S3-Zero

The Chinese version of this page does however contain some content:
https://www.waveshare.net/wiki/ESP32-S3-Zero

## Purchase
It's available for purchase from [Waveshare directly](https://www.waveshare.com/esp32-s3-zero.htm) although it can be found on certain online stores as well including amazon and aliexpress.
