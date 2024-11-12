---
layout: download
board_id: "feather_m4_can"
title: "Feather M4 CAN Download"
name: "Feather M4 CAN"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4759"
board_image: "feather_m4_can.jpg"
date_added: 2020-09-28
family: atmel-samd
bootloader_id: feather_m4_can
download_instructions: https://learn.adafruit.com/adafruit-feather-m4-can-express/circuitpython-on-feather-m4-can
features:
  - Feather-Compatible
  - Battery Charging
  - USB-C
  - Breadboard-Friendly
---

One of our favorite Feathers, the Feather M4 Express, gets a glow-up here with an upgrade to the SAME51 chipset which has built-in CAN bus support! Like its SAMD51 cousin, the ATSAME51J19 comes with a 120 MHz Cortex M4 with floating point support and 512 KB Flash and 192 KB RAM. Your code will zig and zag and zoom, and with a bunch of extra peripherals for support, this will for sure be your favorite new chipset for CAN interfacing projects.

At the end of the board we have placed a CAN transceiver chip as well as a 5 V converter to generate 5 V power to the transceiver even when running on battery. The two CAN signal lines and ground reference signal are available on a 3-pin 3.5 mm terminal block. The chip and booster can be put to sleep for power saving. The built-in CAN can read or write packets and has support in both Arduino and CircuitPython.

Like the original Feather M4 Express, you'll find a Mini NeoPixel and 2 MB SPI Flash. When used in CircuitPython, the 2 MB flash acts as storage for all your scripts, libraries and files.

And best of all, it's a Feather - so you know it will work with all our FeatherWings! What a great way to quickly get up and running. It's even pin-compatible with the original Feather M4.

Easy reprogramming: the Feather M4 CAN comes pre-loaded with the UF2 bootloader, which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython or Arduino IDE (it is bossa-compatible).

Comes fully assembled and tested, with the UF2 USB bootloader. We also toss in some headers so you can solder it in and plug into a solderless breadboard.

## Technical details

* Measures 2.0" x 0.9" x 0.28" (50.8 mm x 22.8 mm x 7 mm) without headers soldered in
* Light as a (large?) feather - 5 grams
* ATSAME51 32-bit Cortex M4 core running at 120 MHz, 32-bit, 3.3 V logic and power
* Hardware CAN bus support with built-in transceiver, 5V booster and terminal connection.
* Floating point support with Cortex M4 DSP instructions
* 512 KB flash, 192 KB RAM
* 2 MB SPI FLASH chip for storing files and CircuitPython code storage.
* No EEPROM
* 32.768 kHz crystal for clock generation & RTC
* 3.3 V regulator with 500 mA peak current output
* USB-C connector for USB native support, comes with USB bootloader and serial port debugging
* Built in crypto engines with AES (256 bit), true RNG, Pubkey controller
* 21 GPIO pins with following capabilities:
  * Dual 1 MSPS 12 bit true analog DAC (A0 and A1) - can be used to play 12-bit stereo audio clips
  * Dual 1 MSPS 12 bit ADC (6 analog pins some on ADC1 and some on ADC2)
  * 6 hardware SERCOM - Native hardware SPI, I2C and Serial all available
  * 16 PWM outputs - for servos, LEDs, etc
  * I2S input and output
  * 8-bit Parallel capture controller (for camera/video in)
* Built in 100 mA lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* Power/enable pin
* 4 mounting holes
* Reset button

## Tutorials

* [CAN Bus with CircuitPython: Using the canio module](https://learn.adafruit.com/using-canio-circuitpython)

## Purchase

* [Adafruit](https://www.adafruit.com/product/4759)
* [Digikey](https://www.adafruit.com/product/4759)
