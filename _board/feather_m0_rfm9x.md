---
layout: download
board_id: "feather_m0_rfm9x"
title: "Feather M0 RFM9x Download"
name: "Feather M0 RFM9x"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3178"
 - "https://www.adafruit.com/product/3179"
board_image: "feather_m0_rfm9x.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: radiofruit_m0
download_instructions: https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/circuitpython-for-rfm9x-lora
features:
  - Feather-Compatible
  - Battery Charging
  - LoRa/Radio
  - Breadboard-Friendly
---

This is the **Adafruit Feather M0 RFM96 LoRa Radio (433 MHz).** Also called _RadioFruits**,**_ Adafruit's take on an microcontroller with a "[Long Range (LoRa)](https://www.lora-alliance.org/)" packet radio transceiver with built in USB and battery charging. It is an Adafruit Feather M0 with a 433MHz radio module cooked in! Great for making wireless networks that are more flexible than Bluetooth LE and without the high power requirements of WiFi.

Feather is the development board platform from Adafruit, and like its namesake it is thin, light, and lets you fly! Adafruit designed Feather to be an open standard for portable microcontroller cores. Check out the other boards in the [Feather family](https://www.adafruit.com/feather).

**There are 433 MHz and 898/915 MHz radio versions.**

At the Feather M0's heart is an ATSAMD21G18 ARM Cortex M0 processor, clocked at 48 MHz and at 3.3 V logic, the same one used in the new [Arduino Zero](https://www.adafruit.com/products/2843). This chip has a whopping 256 K of FLASH (8x more than the Atmega328 or 32u4) and 32 K of RAM (16x as much)! This chip comes with built in USB so it has USB-to-Serial program & debug capability built in with no need for an FTDI-like chip.

To make it easy to use for portable projects, Adafruit added a connector for 3.7 V Lithium polymer batteries and built in battery charging. You don't need a battery, it will run just fine straight from the micro USB connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when its available. The battery is tied thru a divider to an analog pin, so you can measure and monitor the battery voltage to detect when you need a recharge.

## Technical details

* Measures 2.0" x 0.9" x 0.3" (51 mm x 23 mm x 8 mm) without headers soldered in
* Light as a (large?) feather - 5.8 grams
* ATSAMD21G18 @ 48MHz with 3.3 V logic/power
* No EEPROM
* 3.3 V regulator with 500mA peak current output
* USB native support, comes with USB bootloader and serial port debugging
* You also get tons of pins - 20 GPIO pins
* Hardware Serial, hardware I2C, hardware SPI support
* 8 x PWM pins
* 10 x analog inputs
* 1 x analog output
* Built in 100 mA lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* Power/enable pin
* 4 mounting holes
* Reset button

This **Feather M0 LoRa Radio** uses the extra space left over to add an RFM9x LoRa 868/915 MHz radio module. These radios are not good for transmitting audio or video, but they do work quite well for small data packet transmission when you need more range than 2.4 GHz (BT, BLE, WiFi, ZigBee).

* SX127x LoRa® based module with SPI interface
* Packet radio with ready-to-go Arduino libraries
* Uses the license-free ISM bands (ITU "Europe" @ 433 MHz and ITU "Americas" @ 900 MHz)
* +5 to +20 dBm up to 100 mW Power Output Capability (power output selectable in software)
* ~300 uA during full sleep, ~120 mA peak during +20 dBm transmit, ~40 mA during active radio listening.
* Simple wire antenna or spot for uFL connector

The initial tests with default library settings: over 1.2mi/2Km line-of-sight with wire quarter-wave antennas. ([With setting tweaking and directional antennas, 20 km is possible](http://forum.anarduino.com/posts/list/46.page#2854)).

Comes fully assembled and tested, with a USB bootloader. Also includes some headers so you can solder it in and plug into a solderless breadboard. You will need to cut and solder on a small piece of wire (any solid or stranded core is fine) in order to create your antenna.

## Tutorial

- [Feather M0 RFM9x](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module)

## Purchase

* [Feather M0 RFM95 - Adafruit](https://www.adafruit.com/product/3178)
* [Feather M0 RFM96 - Adafruit](https://www.adafruit.com/product/3179)
