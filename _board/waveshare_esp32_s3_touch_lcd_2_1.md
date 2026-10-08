---
layout: download
board_id: "waveshare_esp32_s3_touch_lcd_2_1"
title: "ESP32-S3-Touch-LCD-2.1 Download"
name: "ESP32-S3-Touch-LCD-2.1"
manufacturer: "Waveshare"
board_url:
 - "https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm"
board_image: "waveshare_esp32_s3_touch_lcd_2_1.jpg"
date_added: 2026-10-07
family: esp32s3
features:
  - USB-C
  - Battery Charging
  - Display
  - Wi-Fi
  - Bluetooth/BTLE
---

The ESP32-S3-Touch-LCD-2.1 is a round 2.1 inch 480×480 touch display development board built on the ESP32-S3R8 (dual-core Xtensa LX7 at 240 MHz, 8 MB octal PSRAM) with 16 MB flash, 2.4 GHz Wi-Fi and Bluetooth 5 LE. The IPS panel is driven over a 16-bit RGB bus by an ST7701S and has a CST820 capacitive touch controller.

**Technical details**

 - ESP32-S3R8 with 8 MB PSRAM and 16 MB flash, onboard antenna with an IPEX option
 - 2.1 inch round IPS display, 480×480, ST7701S controller on a 16-bit RGB565 bus, PWM backlight
 - CST820 capacitive touch with gesture support (I2C)
 - QMI8658 6-axis IMU and PCF85063 RTC (I2C)
 - TCA9554 I/O expander for the display and touch resets, SD card select and the onboard buzzer
 - microSD card slot, 3.7 V lithium battery header with charging, battery voltage sense
 - Two USB-C ports: native USB (CircuitPython REPL and CIRCUITPY drive) and a CH343 USB-UART
 - 12-pin header with GPIO0, UART, I2C and USB signals

In CircuitPython, `board.DISPLAY` is ready at boot and the touch controller, IMU, RTC and I/O expander share `board.I2C()`. The expander bit numbers are exported as `board.EXIO_*` constants.

## Purchase

* [Waveshare](https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm)
