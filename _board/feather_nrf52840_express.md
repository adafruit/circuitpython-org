---
layout: download
board_id: "feather_nrf52840_express"
title: "Feather nRF52840 Express Download"
name: "Feather nRF52840 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4062"
board_image: "feather_nrf52840_express.jpg"
date_added: 2019-03-09
family: nrf52840
bootloader_id: feather_nrf52840_express
download_instructions: https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

The **Adafruit Feather nRF52840 Express** is the new Feather family member with Bluetooth Low Energy and _native USB support_ featuring the nRF52840!  It is Adafruit's take on an 'all-in-one' Bluetooth Low Energy device with built in USB plus battery charging. With native USB it's part of the CircuitPython party.

This chip has twice the flash, and four times the SRAM of its earlier sibling, the nRF52832 - 1 MB of FLASH and 256KB of SRAM. Compared to the nRF51, this board has 4-8 times more of everything.

**This is Adafruit's first BLE-friendly CircuitPython board**! CircuitPython works best with disk drive access, and this is the only BLE-plus-USB-native chip that has the memory to handle running the Python interpreter. The massive RAM and speedy Cortex M4F chip makes this a good match.

It's got tons of peripherals: plenty of GPIO, analog inputs, PWM, timers, etc. Best of all, it's got that native USB! Finally, no need for a separate USB serial chip like CP2104 or FT232.

Some other upgrades are an extra 'USER' switch that could be used to trigger OTA updates (or whatever you choose), a NeoPixel LED for status updates, 2 MB of QSPI Flash for storing CircuitPython files, and a SWD connector.

Comes pre-programed the chip with a UF2 bootloader, which can use either command line UART programming with nrfutil or drag-n-drop mass storage, for CircuitPython installation and also because mass-storage-drive bootloaders make updating firmware so easy. Want to program the chip directly? You can use command line tools with your favorite editor and toolchain. If you want to use an SWD programmer/debugger (for even more advanced usage), use a standard 2x5 0.05" connector.

**Features:**

*   ARM Cortex M4F (with HW floating point acceleration) running at 64MHz
*   1MB flash and 256KB SRAM
*   **Native Open Source USB stack** - pre-programmed with UF2 bootloader
*   Bluetooth Low Energy compatible 2.4GHz radio (Details available in the [nRF52840](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52840) product specification)
*   **FCC / IC / TELEC certified module**
*   Up to +8dBm output power
*   1.7v to 3.3v operation with internal linear and DC/DC voltage regulators
*   21 GPIO, 6 x 12-bit ADC pins, up to 12 PWM outputs (3 PWM modules with 4 outputs each)
*   Pin #3 red LED for general purpose blinking, NeoPixel for colorful feedback
*   Power/enable pin
*   Measures 2.0" x 0.9" x 0.28" (51mm x 23mm x 7.2mm) without headers soldered in
*   Light as a (large?) feather - 6 grams
*   4 mounting holes
*   Reset button
*   SWD connector for debugging

## Tutorial

- [Feather nRF52840 Express Overview](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4062)
