---
layout: download
board_id: "feather_m0_express"
title: "Feather M0 Express Download"
name: "Feather M0 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3403"
board_image: "feather_m0_express.jpg"
date_added: 2019-03-08
family: atmel-samd
bootloader_id: feather_m0_express
download_instructions: https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/kattni-circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - Breadboard-Friendly
---

The Adafruit Feather M0 Express was one of the first development boards designed for CircuitPython by Adafruit. Unlike the original Feather M0 Basic, it added a NeoPixel status LED and external 2 MB SPI Flash for storing CircuitPython code.

It is a great entry into the Feather ecosystem with CircuitPython. However, it is now out performed by the [Feather M4 Express]({{ "/board/feather_m4_express/" | relative_url }}) which has a faster microcontroller with more RAM. The additional RAM allows CircuitPython to load more code all at once than this Feather M0 Express can. Check out the other boards in the [Feather family](https://www.adafruit.com/feather).

## Technical details

* Measures 2.0" x 0.9" x 0.28" (51 mm x 23 mm x 8 mm) without headers soldered in
* Light as a (large?) feather - 5 grams
* TSAMD21G18 @ 48 MHz with 3.3V logic/power
* 256 KB of FLASH + 32 KB of RAM
* No EEPROM
* 32.768 kHz crystal for clock generation & RTC
* 3.3 V regulator with 500 mA peak current output
* USB native support, comes with USB bootloader and serial port debugging
* 20x GPIO pins (PWM outputs on all pins)
  * Hardware Serial, hardware I2C, hardware SPI support
  * 6 x 12-bit analog inputs
  * 1 x 10-bit analog ouput (DAC)
* Built in 100 mA lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* Power/enable pin
* 4 mounting holes
* Reset button

## Tutorials

* [Feather M0 Express Overview](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython)

## Purchase

* [Adafruit](https://www.adafruit.com/product/3403)
* [Digi-Key](https://www.digikey.com/short/p87w83)
