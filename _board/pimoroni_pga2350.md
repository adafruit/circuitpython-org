---
layout: download
board_id: "pimoroni_pga2350"
title: "PGA2350 Download"
name: "PGA2350"
manufacturer: "Pimoroni"
board_url:
 - "https://shop.pimoroni.com/products/pga2350"
board_image: "pimoroni_pga2350.jpg"
date_added: 2024-08-22
family: rp2350
---

A minimal but powerful RP2350 breakout board modelled on a Pin Grid Array, with the maximum exposed pins crammed into the smallest possible space.

PGA2350 is a **compact RP2350 breakout** designed to be embedded in projects where space is limited. It contains the components necessary to run the mighty RP2350B chip (that's the crystal, regulator and essential support circuits), a beefy **8MB of PSRAM** and a prodigious **16MB of flash storage**. Note that it has no LEDs, buttons or USB connectors - you'll need to attach your own USB connector to be able to program it.

All this drastic pruning means you get a small 25.4mm square footprint and **a lot of exposed RP2350 pins** to play with. 48 of them can be used as general purpose I/O (that's eighteen more I/O than on a Raspberry Pi Pico!) and 8 are ADC-equipped. We've even managed to squeeze in some tiny pin labels to help identify them.

**Header pins are sold separately** - you can use [standard Pico pin headers](https://shop.pimoroni.com/products/pico-header-pack) (though bear in mind you'll need 64 pins if you want to populate it fully).

## Features
- Powered by RP2350B (Dual Arm Cortex M33 running at up to 150MHz with 520KB of SRAM)
- 16MB of QSPI flash supporting XiP
- 8MB PSRAM (CS wired to GP47 via cuttable trace)
- Crystal oscillator
- On-board 3V3 regulator (max regulator current output 300mA)
- 64 pins, arranged with 2.54mm (0.1") spacing in a Pin Grid Array
- 48 multi-function General Purpose IO (8 can be used for ADC)
- 6 GND pins
- Input voltage range 3V - 5.5V (on VB pin only)
- Measurements: approx 25.4mm x 25.4mm x 3.6mm (L x W x H)
- Programmable with C/C++ or MicroPython

## About RP2350
The RP2350 chip is the Double Quarter Pounder & Fries to the RP2040's Double Cheeseburger and can have one or more RISC-V burgers instead of either of the M33 ARMs, to stretch the metaphor.

In addition to the modern M33 ARM cores, there are sides of: more PIO capability, a variety of low power states for sipping electrons, a whole security system and some sprinklings of specialist digital video circuits to offload DVI/HDMI output.

You can expect a tasty boost in performance - our "real world" MicroPython tests are running up to 2x faster compared to RP2040, and floating point number crunching in C/C++ is up to 20x faster. The extra on-chip RAM will make a big difference when performing memory intensive operations (such as working with higher resolution displays) and even more can be added thanks to external PSRAM support.

RP2350 comes in two flavours - A (standard) and B (all the pins). The B chip has a stonking 48 usable GPIO pins, including 8 ADCs and 24 PWMs, and features on some of our new products.

## Purchase
* [Pimoroni](https://shop.pimoroni.com/products/pga2350)
