---
layout: download
board_id: "waveshare_esp32_s3_touch_lcd_1_69"
title: "ESP32-S3-Touch-LCD-1.69 Download"
name: "ESP32-S3-Touch-LCD-1.69"
manufacturer: "Waveshare"
board_url:
 - "https://www.waveshare.com/esp32-s3-touch-lcd-1.69.htm"
board_image: "waveshare_esp32_s3_touch_lcd_1_69.jpg"
date_added: 2026-10-08
family: esp32s3
features:
  - USB-C
  - Battery Charging
  - Display
  - Wi-Fi
  - Bluetooth/BTLE
---

The ESP32-S3-Touch-LCD-1.69 is a watch-sized development board built on the ESP32-S3 (dual-core Xtensa LX7 at 240 MHz, 8 MB PSRAM, 16 MB flash) with a 1.69 inch 240×280 IPS touch display, 2.4 GHz Wi-Fi and Bluetooth 5 LE.

**Technical details**

 - ESP32-S3 with 8 MB octal PSRAM and 16 MB flash, onboard antenna
 - 1.69 inch IPS display, 240×280, ST7789V2 controller over SPI, PWM backlight
 - CST816T capacitive touch with gesture support (I2C)
 - QMI8658C 6-axis IMU and PCF85063A RTC with an RTC battery header (I2C)
 - ETA6098 lithium battery charger, MX1.25 battery connector, battery voltage sense
 - Passive buzzer, BOOT and RST buttons, and a PWR key with a power-hold circuit for battery operation
 - USB-C (native USB: CircuitPython REPL and CIRCUITPY drive)

In CircuitPython, `board.DISPLAY` is ready at boot, the touch controller, IMU and RTC share `board.I2C()`, and the power-hold line is asserted automatically so the board runs from its battery; `board.PWR_BUTTON` reads the key.

## Purchase

* [Waveshare](https://www.waveshare.com/esp32-s3-touch-lcd-1.69.htm)
