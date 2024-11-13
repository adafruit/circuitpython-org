---
layout: download
board_id: "metro_m0_express"
title: "Metro M0 Express Download"
name: "Metro M0 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3505"
board_image: "metro_m0_express.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: metro_m0
download_instructions: https://learn.adafruit.com/adafruit-metro-m0-express/circuitpython
features:
  - Arduino Shield Compatible
---

This **Metro M0 Express** board looks a whole lot like the [original Metro 328](https://www.adafruit.com/product/2488), but with a huge upgrade. Instead of the ATmega328, this Metro features a ATSAMD21G18 chip, an ARM Cortex M0+. It's the first Adafruit Metro that is designed for use with CircuitPython!

At the Metro M0's heart is an ATSAMD21G18 ARM Cortex M0 processor, clocked at 48 MHz and at 3.3 V logic, the same one used in the new [Arduino Zero](https://www.adafruit.com/products/2843). This chip has a whopping 256 KB of FLASH (8x more than the Atmega328) and 32 KB of RAM (16x as much)! This chip comes with built in USB so it has USB-to-Serial program & debug capability built in with no need for an FTDI-like chip.

## Technical details

* **Power the METRO** with 7-9 V polarity protected DC or the micro USB connector to any 5 V USB source. The 2.1 mm DC jack has an on/off switch next to it so you can turn off your setup easily. The METRO will automagically switch between USB and DC.
* **METRO has 25 GPIO pins**, 12 of which are analog in, and one of which is a true analog out. There's a hardware SPI port, hardware I2C port and hardware UART. Logic level is 3.3 V.
* **Native USB**, there's no need for a hardware USB to Serial converter as the Metro M0 has built in USB support. When used to act like a serial device, the USB interface can be used by any computer to listen/send data to the METRO, and can also be used to launch and update code via the bootloader. It can also act like a keyboard, mouse or MIDI device as well.
* **Four indicator LEDs and one NeoPixel**, on the front edge of the PCB, for easy debugging. One green power LED, two RX/TX LEDs for data being sent over USB, and a red LED connected. Next to the reset button there is an RGB NeoPixel that can be used for any purpose.
* **2 MB SPI Flash** storage chip is included on board. You can use the SPI Flash storage like a very tiny hard drive. When used in Circuit Python, the 2 MB flash acts as storage for all your scripts, libraries and files.
* **Easy reprogramming**, comes pre-loaded with the [UF2 bootloader](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader), which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython, PXT/MakeCode or Arduino IDE (it is bossa-compatible).

Comes fully assembled with headers, tested, and with the UF2 bootloader loaded on. Includes 4 rubber bumpers to keep it from slipping off your desk. No soldering required to use, plug and play!

## Tutorial

* [Metro M0 Express Overview](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/overview)

## Purchase

* [Adafruit](https://www.adafruit.com/product/3505)
