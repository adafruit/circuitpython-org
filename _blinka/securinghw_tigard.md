---
layout: download
board_id: "securinghw_tigard"
title: "Tigard Download"
name: "Tigard"
manufacturer: "SecuringHardware.com"
board_url:
 - "https://tigard-tools.org/tigard"
board_image: "securinghw_tigard.jpg"
download_instructions: "https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h"
downloads_display: true
date_added: 2026-09-17
blinka: true
features:
board_usage:
 - Attached
---

Tigard is an FTDI FT2232H-based multi-protocol tool for hardware hacking. It's designed to be easy to use, with individually labelled wire harnesses and built-in level shifting.

Highlights:
* Dual-port, with one dedicated to UART and the second shared with other interfaces
* High-performance directional level shifters for 1.8 to 5.5v operation
* Switch to choose between on-board 1.8, 3.3, and 5.0v supplies and vTarget
* Switch to choose between SPI/JTAG and I2C/SWD modes
* Logic analyser port to observe device-level signals 
* Indicator lights to aid debugging

## Learn More
Adafruit's [Blinka-on-FT232H](https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h) guide covers most of what you'll need to use it with Tigard, but keep in mind:
* Tigard uses the FT2232H with two separate interfaces, so you'll need to:```export BLINKA_FT2232H=1```
* Tigard has unidirectional level shifters - only certain pins can be in or out
* UART header is connected to the first interface on the AC# and AD# pins
* I2C, SPI, and JTAG headers use the second interface on the BC#, BD#, and SDA1, SCL1, SCLK1, etc pins.
* [Documentation](https://tigard-tools.org/tigard)

## Purchase
* [1BitSquared](https://1bitsquared.com/products/tigard)
* [Crowd Supply](https://www.crowdsupply.com/securinghw/tigard#products)
