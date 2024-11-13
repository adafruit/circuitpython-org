---
layout: download
board_id: "feather_m4_express"
title: "Feather M4 Express Download"
name: "Feather M4 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3857"
 - "https://www.adafruit.com/product/4352"
board_image: "feather_m4_express.jpg"
date_added: 2019-03-08
family: atmel-samd
bootloader_id: feather_m4
download_instructions: https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - Breadboard-Friendly
---

This feather is powered by the ATSAMD51J19 -  with its 120 MHz Cortex M4 with floating point support and 512 KB Flash and 192 KB RAM. Your code will zig and zag and zoom, and with a bunch of extra peripherals for support, this will for sure be your favorite new chipset.

And best of all, it's a Feather - so you know it will work with all our FeatherWings! What a great way to quickly get up and running.

The most exciting part of the Feather M4 is that while you can use it with the Arduino IDE - and it's bonkers fast when you do, we are shipping it with CircuitPython on board. When you plug it in, it will show up as a very small disk drive with main.py on it. Edit main.py with your favorite text editor to build your project using Python, the most popular programming language. No installs, IDE or compiler needed, so you can use it on any computer, even ChromeBooks or computers you can't install software on. When you're done, unplug the Feather and your code will go with you.

The Feather M4 Express uses the extra space left over to add a Mini NeoPixel, 2 MB SPI Flash storage and a little prototyping space. You can use the SPI Flash storage like a very tiny hard drive. When used in CircuitPython, the 2 MB flash acts as storage for all your scripts, libraries and files. When used in Arduino, you can read/write files to it, like a little datalogger or SD card, and then with our helper program, access the files over USB.

Easy reprogramming: the Feather M4 comes pre-loaded with the UF2 bootloader, which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython or Arduino IDE (it is bossa-compatible).

Comes fully assembled and tested, with the UF2 USB bootloader. We also toss in some headers so you can solder it in and plug into a solderless breadboard.

## Technical details

* Measures 2.0" x 0.9" x 0.28" (50.8 mm x 22.8 mm x 7 mm) without headers soldered in
* Light as a (large?) feather - 5 grams
* ATSAMD51 32-bit Cortex M4 core running at 120 MHz, 32-bit, 3.3 V logic and power
* Floating point support with Cortex M4 DSP instructions
* 512 KB flash, 192 KB RAM
* 2 MB SPI FLASH chip for storing files and CircuitPython code storage.
* No EEPROM
* 32.768 kHz crystal for clock generation & RTC
* 3.3 V regulator with 500 mA peak current output
* USB native support, comes with USB bootloader and serial port debugging
* Built in crypto engines with AES (256 bit), true RNG, Pubkey controller
* 21x GPIO pins with following capabilities:
  * Dual 1 MSPS 12 bit true analog DAC (A0 and A1) - can be used to play 12-bit stereo audio clips
  * Dual 1 MSPS 12 bit ADC (6 analog pins some on ADC1 and some on ADC2)
  * 6x hardware SERCOM - Native hardware SPI, I2C and Serial all available
  * 16x PWM outputs - for servos, LEDs, etc
  * I2S input and output
  * 8-bit Parallel capture controller (for camera/video in)
* Built in 100 mA lipoly charger with charging status indicator LED
* Pin #13 red LED for general purpose blinking
* Power/enable pin
* 4 mounting holes
* Reset button

## Tutorials

* [Feather M4 Express Overview](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)

## Purchase

* [Adafruit](https://www.adafruit.com/product/3857)
* [Digi-Key](https://www.digikey.com/short/p87f17)
