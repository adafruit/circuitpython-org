---
layout: download
board_id: "feather_m0_adalogger"
title: "Feather M0 Adalogger Download"
name: "Feather M0 Adalogger"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/2796"
board_image: "feather_m0_adalogger.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: feather_m0
features:
  - Feather-Compatible
  - Battery Charging
  - Breadboard-Friendly
---

Feather is a development board from Adafruit, and like its namesake it is thin, light, and lets you fly! Adafruit designed Feather to be a new open standard for portable microcontroller cores.

This is the **Adafruit Feather M0 Adalogger** - Adafruit's take on an 'all-in-one' Cortex M0 datalogger (or data-reader) with built in USB and battery charging. It is an Adafruit Feather M0 with a microSD holder.  Check out the other boards in the [Feather family](https://www.adafruit.com/feather).

At the Feather M0's heart is an ATSAMD21G18 ARM Cortex M0 processor, clocked at 48 MHz and at 3.3 V logic, the same one used in the new [Arduino Zero](https://www.adafruit.com/products/2843). This chip has a whopping 256 KB of FLASH (8x more than the Atmega328 or 32u4) and 32 KB of RAM (16x as much)! This chip comes with built in USB so it has USB-to-Serial program & debug capability built in with no need for an FTDI-like chip.

To make it easy to use for portable projects, Adafruit added a connector for 3.7 V Lithium polymer batteries and built in battery charging. You don't need a battery, it will run just fine straight from the micro USB connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when its available. The battery is tied thru a divider to an analog pin, so you can measure and monitor the battery voltage to detect when you need a recharge.

## Technical details

* Measures 2.0" x 0.9" x 0.28" (51 mm x 23 mm x 8 mm) without headers soldered in
* Light as a (large?) feather - 5.3 grams
* ATSAMD21G18 @ 48MHz with 3.3V logic/power
* 256 KB of FLASH + 32 KB of RAM
* No EEPROM
* 3.3 V regulator with 500 mA peak current output
* USB native support, comes with USB bootloader and serial port debugging
* 20x GPIO pins
  * Hardware Serial, hardware I2C, hardware SPI support
  * 8x PWM pins
  * 10x analog inputs
* Built in 100 mA lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* Power/enable pin
* 4 mounting holes
* Reset button

The **Feather M0 Adalogger** uses the extra space left over to add MicroSD + a green LED:

* Pin #8 green LED for your blinking pleasure
* MicroSD card holder for adding as much storage as you could possibly want, for reading or writing.

Comes fully assembled and tested, with a USB bootloader. Includes some header so you can solder it in and plug into a solderless breadboard.

## Tutorial

- [Feather M0 Adalogger Overview](https://learn.adafruit.com/adafruit-feather-m0-adalogger)

## Purchase

* [Adafruit](https://www.adafruit.com/product/2796)
