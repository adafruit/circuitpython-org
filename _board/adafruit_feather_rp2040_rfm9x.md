---
layout: download
board_id: "adafruit_feather_rp2040_rfm9x"
board_alias: "adafruit_feather_rp2040_rfm"
title: "Feather RP2040 RFM9x Board Download"
name: "Feather RP2040 RFM9x"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5714"
board_image: "adafruit_feather_rp2040_rfm9x.jpg"
date_added: 2023-04-04
family: rp2040
download_instructions: https://learn.adafruit.com/feather-rp2040-rfm95/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - LoRa/Radio
  - USB-C
  - Breadboard-Friendly
  - STEMMA QT/QWIIC
---
This is the Adafruit Feather RP2040 RFM9x. We call these RadioFruits, our take on a microcontroller with packet radio transceiver with built-in USB and battery charging. It's an Adafruit Feather RP2040 with a radio module cooked in! Great for making wireless networks that are more flexible than Bluetooth LE and without the high power requirements of WiFi.

Feather is the development board specification from Adafruit, and like its namesake, it is thin, light, and lets you fly! We designed Feather to be a new standard for portable microcontroller cores. We have other boards in the Feather family, check'em out here.

It's kinda like we took our RP2040 Feather and an RFM9x breakout board and glued them together. You get all the pins for use on the Feather, the LiPoly battery support, USB C power / data, onboard NeoPixel, 8MB of FLASH for storing code and files, and then with the 8 unused pins, we wired up all the DIO pins on the RFM module. There's even room left over for a STEMMA QT connector and a uFL connector for connecting larger antennas.

At the Feather's heart is an RP2040 chip, clocked at 133 MHz and at 3.3V logic, the same one used in the Raspberry Pi Pico. This chip has a whopping 8MB of onboard QSPI FLASH and 264K of RAM! This makes it great for making wireless sensor nodes that can send to each other without a lot of software configuration.

To make it easy to use for portable projects, we added a connector for any of our 3.7V Lithium polymer batteries and built-in battery charging. You don't need a battery, it will run just fine straight from the USB Type C connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when it's available.

## Technical Details

* Measures approximately 2.0" x 0.9" x 0.28" (50.8mm x 22.8mm x 7mm) without headers soldered in
* Light as a (large?) feather - approximately 6 grams
* RP2040 32-bit Cortex M0+ dual core running at ~133 MHz @ 3.3V logic and power
* 264 KB RAM
* 8 MB SPI FLASH chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
* Tons of GPIO! 21 x GPIO pins with following capabilities:
* Four 12-bit ADCs (one more than Pico)
* Two I2C, Two SPI, and two UART peripherals, we label one for the 'main' interface in standard Feather locations
* 16 x PWM outputs - for servos, LEDs, etc
* Built-in 200mA+ lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* RGB NeoPixel for full-color indication.
* On-board STEMMA QT connector that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
* Both Reset button and Bootloader select button for quick restarts (no unplugging-replugging to relaunch code)
* USB Type C connector lets you access built-in ROM USB bootloader and serial port debugging
* 3.3V Power/enable pin
* 4 mounting holes
* 12 MHz crystal for perfect timing.
* 3.3V regulator with 500mA peak current output
* SX127x LoRa® based module with SPI interface
* Packet radio with ready-to-go Arduino libraries
* Uses the license-free ISM bands (ITU "Europe" @ 433MHz and ITU "Americas" @ 900MHz)
* +5 to +20 dBm up to 100 mW Power Output Capability (power output selectable in software)
* ~300uA during full sleep, ~120mA peak during +20dBm transmit, ~40mA during active radio listening.
* Simple wire antenna can be soldered into a solder pad, there's also a uFL connector that can be used with uFL-to-SMA adapters for attaching bigger antennas.

## Tutorials

* Guide is coming soon!

## Purchase

* [Adafruit](https://www.adafruit.com/product/5714)