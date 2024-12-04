---
layout: download
board_id: "adafruit_feather_rp2040_dvi"
title: "Feather RP2040 with DVI Output Port Download"
name: "Feather RP2040 with DVI Output Port"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5710"
board_image: "adafruit_feather_rp2040_dvi.jpg"
date_added: 2023-03-27
family: rp2040
download_instructions: https://learn.adafruit.com/adafruit-feather-rp2040-dvi/circuitpython
tags:
  - DVI Feather
  - Feather DVI
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

Wouldn't it be cool if you could display images and graphics from a microcontroller directly to an HDMI monitor or television? We think so! So we designed this RP2040 Feather that has a digital video output (a.k.a DVI) that will work with any HDMI monitor or display. Note it doesn't do audio, just graphics!

It's kinda like we took our [RP2040 Feather](https://www.adafruit.com/product/4884) and [DVI Breakout board](https://www.adafruit.com/product/4984) and glued them together. You get all the pins for use on the Feather, the Lipoly battery support, USB C power / data, onboard NeoPixel, 8MB of FLASH for storing code and files, and then with the 8 unused pins, a DVI output that can be used with the [PicoDVI library in Arduino](https://github.com/adafruit/PicoDVI) or [Pico SDK](https://github.com/Wren6991/PicoDVI) (note we don't have Circuitpython support for DVI output at this time)

In Arduino, which is what we recommend, [we use our fork of PicoDVI](https://github.com/adafruit/PicoDVI) to create an internal framebuffer of 320x240 or 400x240 16-bit pixels that is then continuously blitted out as pixel-doubled 640x480 or 800x480 digital video. Whatever you 'draw' to the internal memory framebuffer appears instantly on the digital display in crisp color. Since the library is a subclass of AdafruitGFX, it'll be familiar to folks who have used our TFT or OLED displays before.

Note that the DVI video generation uses one full core, both PIOs, and 150K (320x240) or 190K (400x240) of SRAM. It's kinda maxed out so be aware of the remaining resource limitations.

We also connected the HDMI-connectors I2C pins to the SDA/SCL of the Feather (through a safe level shifter) so you can read the EDID EEPROM of displays, and have broken out the CEC and Utility pads. The Hot Plug Detect pin is also available on the very end of the 16-pin header. Read this pin to know when a display has been connected!

## Purchase

* [Adafruit](https://www.adafruit.com/product/5710)
