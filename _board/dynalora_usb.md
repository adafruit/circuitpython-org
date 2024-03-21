---
board_id: dynalora_usb
board_image: dynalora_usb.jpg
board_url:
- https://github.com/BHDynamics/rfm_radio_dongle
date_added: 2021-02-11 12:00:00
downloads_display: true
family: atmel-samd
features:
- LoRa/Radio
layout: download
manufacturer: BH Dynamics
name: DynaLoRa-USB
title: DynaLoRa-USB Download
---

## Overview

DynaLoRa-USB is a low cost and open source, CircuitPython and Arduino compatible, LoRa tinkering dongle designed by and for makers.

Our aim is to facilitate access to the hottest radio technology (LoRa) through the use of maker-friendly languages such as Python and the Arduino framework. With that intent, DynaLoRa-USB is a simple device that you just plug and play with! It includes a powerful SAMD21 microcontroller and a HopeRF LoRa radio module (RFM96W for 868/915 MHz), an user button, an RGB LED and an external interface to plug your favorite peripherals.


- ATSAMD21E18 48 MHz Cortex-M0+ processor with 256 KB flash + 32 KB RAM, compatible with CircuitPython and Arduino
- 32 Mbit SPI flash for storing CircuitPython code and libraries
- High performance HopeRF radio module. We offer the device with the RFM96W, which is capable of LoRa modulation at 868/915 MHz, but you can easily replace it by the 433 MHz version (RFM95W) or a generic Sub-GHz radio (RFM69HCW) since they are pin compatible.
- User-controllable WS2812B addressable RGB LED
- Regular user LED
- 3V3 @ 1A power through a DC/DC buck regulator from USB
- MicroSD Card slot
- GPIO header exposing SWD interface, a full SERCOM (enabling external SPI/I2C/UART peripherals) and a DAC for prototyping
- This version comes with an USB-A plug. It should be easy enough to modify the design to offer other options (such as USB-C).
- Comes preprogrammed with the UF2 Bootloader and latest stable release of CircuitPython.

Hardware is licensed under **CERN OHL v1.2**.

## Documentation

This board is open source hardware. You can check the docs and contribute [here](https://github.com/BHDynamics/rfm_radio_dongle).

## Purchase

* [Tindie](https://www.tindie.com/products/bhdynamics/dynalora-usb/)
