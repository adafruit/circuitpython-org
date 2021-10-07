---
layout: download
board_id: "swan-r5"
title: "Swan Download"
name: "Swan"
manufacturer: "Blues Wireless"
board_url: "https://blues.io/products/swan"
board_image: "swan.jpg"
date_added: 2021-9-29
features:
  - Feather-Compatible
  - Battery Charging
  - Breadboard-Friendly
---

Swan is a low-cost embeddable STM32L4-based microcontroller designed to accelerate the development and deployment of battery-powered solutions. It is especially useful for applications requiring large memory or a high degree of I/O expandability at an affordable cost, such as edge inferencing and remote monitoring.

Uniquely for Feather-compatible boards, Swan is designed to satisfy developers’ needs that span from early prototyping through high-volume deployment. Developers may begin to use Swan in conjunction with Adafruit’s myriad sensors and FeatherWing-compatible carriers. Due to its novel design, for high-volume deployment the low-cost Swan can also be soldered directly to a parent PCB integrating those sensors, utilizing the full range of Swan’s I/O capabilities.

The board has three independent power options – USB, Battery, or Line power – and provides a software-switchable 2 Amp regulator for powering external sensors. When operating in its low-power operating mode, the entire Swan board commonly draws only about 8uA while retaining all of its memory, making it quite suitable for battery-powered devices.


### Swan Features
* Ultra low-power Arm Cortex-M4 core clocked at 120Mhz
* STM32L4R5-based microcontroller
* 2MB of flash and 640KB of RAM
* Castellated-edge access to 55 GPIO ports including:
  * 8 analog
  * 16 digital
  * 4x I2C, 3x SPI
  * USB OTG full speed
  * 1x 14-channel DMA
  * tRNG
  * 12-bit ADC, 2 x 12-bit DAC
  * low-power RTC, and CRC calculation peripherals

## Tutorial
* [Swan Quickstart on dev.blues.io](https://dev.blues.io/start/swan/swan-quickstart)

## Purchase
* [Blues Shop](https://shop.blues.io/products/swan)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).