---
layout: download
board_id: "fluff_m0"
title: "Fluff M0 Download"
name: "Fluff M0"
manufacturer: "Radomir Dopieralski"
board_url:
 - "https://hackaday.io/project/171381-fluff-m0"
board_image: "fluff_m0.jpg"
date_added: 2020-05-22
family: atmel-samd
bootloader_id: fluff_m0
features:
  - USB-C
  - Breadboard-Friendly
---
A minimal CircuitPython board compatible with the Feather M0 Basic. Everything
that is non-essential has been removed, and the smallest possible chip is used.


[Project page on hackaday.io](https://hackaday.io/project/171381-fluff-m0)


**Here are some handy specs!**
*   Measures 2.0" x 0.9" x 0.28" (51mm x 23mm x 8mm) without headers soldered in
*   ATSAMD21E18 @ 48MHz with 3.3V logic/power
*   256KB of FLASH + 32KB of RAM
*   No EEPROM
*   3.3V regulator with 500mA peak current output
*   USB native support, comes with USB bootloader and serial port debugging
*   You also get tons of pins - 23 GPIO pins
*   Hardware Serial, hardware I2C, hardware SPI support
*   8 x 12-bit analog inputs
*   1 x 10-bit analog ouput (DAC)
*   Yellow LED for general purpose blinking
*   4 mounting holes

**Differences from Feather M0**
*   No battery charger
*   No crystal
*   No external flash
*   No reset button
*   No enable pin, instead you get another GPIO pin
*   Two additional analog pins (AREF and A6)
*   LED is on a separate, dedicated pin, not on D13
*   USB-C PCB socket
