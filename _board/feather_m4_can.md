---
layout: download
board_id: "feather_m4_can"
title: "Feather M4 CAN Download"
name: "Feather M4 CAN"
manufacturer: "Adafruit"
board_url: "https://www.adafruit.com/product/4759"
board_image: "feather_m4_can.jpg"
date_added: 2020-9-28
family: atmel-samd
features:
  - Feather-Compatible
  - Battery Charging
  - USB-C
  - Breadboard-Friendly
---
 
One of our favorite Feathers, the Feather M4 Express, gets a glow-up here with an upgrade to the SAME51 chipset which has built-in CAN bus support! Like its SAMD51 cousin, the ATSAME51J19 comes with a 120MHz Cortex M4 with floating point support and 512KB Flash and 192KB RAM. Your code will zig and zag and zoom, and with a bunch of extra peripherals for support, this will for sure be your favorite new chipset for CAN interfacing projects.

At the end of the board we have placed a CAN transceiver chip as well as a 5V converter to generate 5V power to the transceiver even when running on battery. The two CAN signal lines and ground reference signal are available on a 3-pin 3.5mm terminal block. The chip and booster can be put to sleep for power saving. The built in CAN can read or write packets and has support in both Arduino and CircuitPython.

Like the original Feather M4 Express, you'll find a Mini NeoPixel and 2 MB SPI Flash. When used in CircuitPython, the 2 MB flash acts as storage for all your scripts, libraries and files.

And best of all, it's a Feather - so you know it will work with all our FeatherWings! What a great way to quickly get up and running. It's even pin-compatible with the original Feather M4.

Easy reprogramming: the Feather M4 CAN comes pre-loaded with the UF2 bootloader, which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython or Arduino IDE (it is bossa-compatible)

Comes fully assembled and tested, with the UF2 USB bootloader. We also toss in some headers so you can solder it in and plug into a solderless breadboard.

## Tutorials
* [CAN Bus with CircuitPython: Using the canio module](https://learn.adafruit.com/using-canio-circuitpython)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4759)
* [Digikey](https://www.adafruit.com/product/4759)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/main/_board/{{ page.board_id }}.md).
