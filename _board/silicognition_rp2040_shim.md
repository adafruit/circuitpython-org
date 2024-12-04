---
layout: download
board_id: "silicognition_rp2040_shim"
title: "RP2040-Shim Download"
name: "RP2040-Shim"
manufacturer: "Silicognition LLC"
board_url:
 - "https://github.com/xorbit/RP2040-Shim"
board_image: "silicognition-rp2040-shim.jpg"
date_added: 2022-07-01
family: rp2040
features:
  - Feather-Compatible
  - Breadboard-Friendly
---

This board is an alternative to the [Silicognition M4-Shim](https://www.amazon.com/M4-Shim-Feather-PoE-FeatherWing-Ultra-Compact-Vertical/dp/B0971PKDV7/), and just like that board it is specifically made to fit on top of the [PoE-FeatherWing](https://www.amazon.com/Silicognition-PoE-FeatherWing-Ethernet-802-3at-Feather/dp/B08KTVD7BR/), filling the empty space around the RJ45 and flyback transformer and allowing the creation of extremely compact Power over Ethernet systems.

Since the ATSAMD51J19 used on the M4-Shim is pretty much unobtainium right now, I needed to provide an alternative, and with good availability and popularity of the [RP2040](https://www.raspberrypi.com/products/rp2040/) this chip seemed like a natural choice.  You get dual ARM Cortex-M0+ @ 133 MHz, 264 kB on-chip SRAM, PIO and 4 MB of QSPI flash!

The RP2040 comes with built-in UF2 bootloader, and the board has CircuitPython with Wiznet W5500 drivers pre-installed, plus a `poe_featherwing.py` module that sets the Ethernet connection up for you.

A special feature of this board is a custom chip to enable the familiar single-press to reset, double-press for bootloader button!  So from a user experience point of view, it behaves the same as the M4-Shim.

## Learn More
* [Hardware Github repo](https://github.com/xorbit/RP2040-Shim)
