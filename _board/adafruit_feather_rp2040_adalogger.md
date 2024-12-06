---
layout: download
board_id: "adafruit_feather_rp2040_adalogger"
title: "Feather RP2040 Adalogger Download"
name: "Feather RP2040 Adalogger"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5980"
board_image: "adafruit_feather_rp2040_adalogger.jpg"
date_added: 2024-06-28
family: rp2040
download_instructions: https://learn.adafruit.com/adafruit-feather-rp2040-adalogger/install-circuitpython
tags:
  - Adalogger Feather
  - Adalogger
  - Feather Adalogger
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

This is the <b>Adafruit Feather RP2040 Adalogger</b> - our take on an 'all-in-one' RP2040 data-logger (or data-reader) with built-in USB, battery charging, and a microSD holder ready to rock! [We have other boards in the Feather family, check'em out here.](https://www.adafruit.com/feather)

The RP2040 Adalogger is the same size and shape as a Feather and is intended to make your next data logging or data reading project super easy. Micro SD card socket wired for SPI or SDIO? Yes! STEMMA QT / Qwiic connector for fast I2C? Of course! Neopixel? It's a-glowin' This board will work excellently with Arduino or CircuitPython/MicroPython for any data recording/retreiving projects.

At the Feather's heart is an RP2040 chip, clocked at 133 MHz and at 3.3V logic, the same one used in the [Raspberry Pi Pico](https://www.adafruit.com/product/4864). This chip has a whopping 8MB of onboard QSPI FLASH and 264K of RAM! This makes it great for buffering and processing data before writing it to the SD card.

To make it easy to use for portable projects, we added a connector for any of our 3.7V Lithium polymer batteries and built-in battery charging. You don't need a battery, it will run just fine straight from the USB Type C connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when it's available.

<b>Here're some handy specs! You get:</b>

* Measures 2.0" x 0.9" x 0.28" (50.8mm x 22.8mm x 7mm) without headers soldered in
* Light as a (large?) feather - 6.3 grams
* RP2040 32-bit Cortex M0+ dual core running at ~133 MHz @ 3.3V logic and power
* 264 KB RAM
* <b>8 MB SPI FLASH</b> chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
* <b>Tons of GPIO! 21 x GPIO pins with following capabilities:</b>
	* <b>Four</b> 12-bit ADCs (one more than Pico)
	* Two I2C, Two SPI, and two UART peripherals, we label one for the 'main' interface in standard Feather locations
	* 16 x PWM outputs - for servos, LEDs, etc
* <b>Built-in 200mA+ lipoly charger</b> with charging status indicator LED
* <b>Pin #13 red LED</b> for general purpose blinking
* <b>RGB NeoPixel</b> for full-color indication.
* <b>MicroSD card holder</b> for adding as much storage as you could possibly want for reading or writing. Connected to the 'second' SPI port on pins 18, 19, 20 and card select on 23. Optional card detect line can be connected to pin 15. For advanced hackers who want to use 4-bit SDIO, we connect DAT1 and DAT2 to 21 and 22 - note we do not have Arduino or CircuitPython code for this mode.
* On-board <b>STEMMA QT connector</b> that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
* <b>Both Reset button and Bootloader select button for quick restarts</b> (no unplugging-replugging to relaunch code)
* <b>USB Type C connector</b> lets you access built-in ROM USB bootloader and serial port debugging
* 3.3V Power/enable pin
* 4 mounting holes
* 12 MHz crystal for perfect timing.
* 3.3V regulator with 500mA peak current output

Comes assembled and tested, with some header. You'll need a soldering iron to attach the header for installing onto your Feather. Stacking headers will let you put another FeatherWing on top. <b>Lipoly battery, MicroSD card, and USB cable not included</b> (but we do have lots of options in the shop if you'd like!)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5768)