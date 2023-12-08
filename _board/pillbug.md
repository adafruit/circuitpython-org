---
layout: download
board_id: "pillbug"
title: "PillBug Download"
name: "PillBug"
manufacturer: "MechWild"
board_url:
 - "https://mechwild.com/product/pillbug/"
board_image: "pillbug.jpg"
date_added: 2022-11-10
downloads_display: true
family: nrf52840
bootloader_id: pillbug
# Features are tags; they should be limited to the items in this list and spelled exactly the same.
# Include only the features your board supports, and remove these comment lines before committing.
# Breadboard-Friendly is a parallel pin layout with minimal non-critical perpendicular pins
features:
  - Battery Charging
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - USB-C
---

The PillBug is a BLE enabled development board powered by the nRF52840 that is designed to be a drop in replacement for the stm32f401/stm32f411 blackpill development board. This board was designed for compatibility with blackpill driven keyboards and will work as a simple replacement in most cases. The PillBug features 3.7V Li-Ion battery charger, a software controlled hardware cutoff for powering peripherals, a controllable status LED, and compatibility with blackpill's pinouts for I2C/SPI/UART.

## Technical details

* BLE (Bluetooth Low Energy) capable
* nRF52840 powered with 1MB Flash memory and 256KB RAM
* Preloaded Adafruit nRF52 Bootloader utlizing UF2 and DFU flashing options
* Software controlled blue status LED that can be configured by application
* Hardware controlled charging red status LED
* 3.3V GPIO logic and power provided through VCC pins
* Software controlled MOSFET to disable providing power through the power pins to external peripherals
* 30 Total GPIO pins in an easy to use and breadboard friendly layout
* RTC (real-time clock) capabilities provided through use of 32.768kHz oscillator (necessary for BlE)

## Learn More

* [MechWild](https://mechwild.com/product/pillbug/)

## Purchase

* [MechWild](https://mechwild.com/product/pillbug/)
