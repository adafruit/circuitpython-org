---
layout: download
board_id: "pimoroni_explorer2350"
title: "Pimoroni Explorer (RP2350) Download"
name: "Pimoroni Explorer (RP2350)"
id: "PIM720"
manufacturer: "Pimoroni"
board_url: "https://shop.pimoroni.com/products/explorer"
board_image: "pimoroni_explorer2350.jpg"
date_added: 2024-08-22
family: rp2350
downloads_display: true
blinka: false
features:
  - Breadboard-Friendly
  - Display
  - Robotics
  - Solder-Free Alligator Clip
  - Speaker
  - STEMMA QT/QWIIC
  - USB-C
---

An electronic adventure playground for physical computing, built around the high-performance RP2350B chip.

Pimoroni Explorer is designed for playing with circuits, building science experiments, and prototyping tiny robots. It features a large **2.8" IPS LCD screen** surrounded by **six tactile buttons**, making it easy to monitor and control your projects. With an integrated speaker, **mini breadboard**, **servo headers**, and **analog-friendly crocodile clip terminals**, it’s a self-contained workstation for tinkering without the mess of loose wires.

## Features

- Powered by RP2350B (Dual Arm Cortex M33 running at up to 150MHz with 520KB of SRAM)
- 16MB of QSPI flash supporting XiP
- 2.8” IPS LCD screen (320 x 240 pixels, ST7789V driver)
- USB-C connector for power and programming
- Mini breadboard for circuit prototyping
- Piezo speaker for audio feedback
- 6x user-controllable tactile switches, plus reset and boot buttons
- 2x Qw/ST (Qwiic/STEMMA QT) connectors for I2C breakouts
- 4x 3-pin servo outputs
- 6x crocodile clip terminals (3x ADCs, plus 3.3V and Ground)
- 2-pin JST-PH connector for adding a battery (input voltage 3V to 5.5V)
- Fully-assembled (no soldering required)
- Programmable with C/C++ or MicroPython

## Getting Started

See [this Adafruit Playground note](https://adafruit-playground.com/u/tyeth/pages/circuitpython-on-the-pimoroni-explorer) to help you begin your journey!

## About RP2350

The RP2350 chip is the "Double Quarter Pounder & Fries" to the RP2040's "Double Cheeseburger." It features upgraded dual-core Arm Cortex-M33 processors and introduces optional RISC-V cores for specialized development.

In addition to the modern M33 ARM cores, you get a significant boost in PIO capability, lower power states for battery-efficient projects, and a robust security architecture. 

Performance-wise, you can expect "real world" MicroPython tests to run up to 2x faster than on the RP2040, while floating-point math in C/C++ is up to 20x faster. The extra on-chip RAM and external PSRAM support make a massive difference when working with memory-intensive operations like driving the Explorer's high-resolution display.

The Pimoroni Explorer uses the **RP2350B** variant, which features 48 usable GPIO pins, enabling the dense integration of the screen, servos, and expansion headers all on one board.

## Purchase

* [Pimoroni](https://shop.pimoroni.com/products/explorer)