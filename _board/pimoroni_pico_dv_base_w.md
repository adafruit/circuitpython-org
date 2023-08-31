---
layout: download
board_id: "pimoroni_pico_dv_base_w"
title: "Pimoroni Pico DV Demo Base for Pico W Download"
name: "Pimoroni Pico DV Demo Base for Pico W"
manufacturer: "Pimoroni"
board_url: "https://shop.pimoroni.com/en-us/products/pimoroni-pico-dv-demo-base"
board_image: "pimoroni_pico_dv_base_w.jpg"
date_added: 2023-8-29
family: raspberrypi
---

A demo board for exploring the digital video and audio capabilities of Raspberry Pi Pico or Pico W, with 
HDMI connector, SD card slot, line level I2S audio and buttons.  

**Note** The Pico W version of the Pico dv Demo Base does not bring up the DVI output by default. In order to activate the DVI output you must run CircuitPython user code. If you are running version 8.2.4 of CircuitPython the following example code will activate and display the REPL on the DVI interface.
```py
import displayio
displayio.release_displays()

import board
import picodvi
import framebufferio

fb = picodvi.Framebuffer(
    width=320, height=240, color_depth=8,
    clk_dp=board.CKP, clk_dn=board.CKN,
    red_dp=board.D0P, red_dn=board.D0N,
    green_dp=board.D1P, green_dn=board.D1N,
    blue_dp=board.D2P, blue_dn=board.D2N)

display = framebufferio.FramebufferDisplay(fb)
```

## Features
- HDMI connector
- PCM5100A DAC for line out audio over I2S [datasheet](https://cdn.shopify.com/s/files/1/0174/1800/files/pcm5100a_617130f1-79f1-45ac-96bc-a3752b4afa59.pdf?v=1611151321)
- SD card slot
- Reset button
- Socket headers to install your Raspberry Pi Pico
- Three user-controllable switches
- Rubber feet
- Compatible with Raspberry Pi Pico
- No soldering required (as long as your Pico has header pins attached)
- Programmable with C/C++
- [Schematic](https://cdn.shopify.com/s/files/1/0174/1800/files/pico_dv_schematic.pdf?v=1636985340)

## Purchase
* [Adafruit](https://www.adafruit.com/product/5674)
* [Pimoroni](https://shop.pimoroni.com/en-us/products/pimoroni-pico-dv-demo-base)
