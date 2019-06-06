---
layout: download
board_id: "feather_nrf52832"
title: "Feather nRF52832 Download"
name: "Feather nRF52832"
manufacturer: "Adafruit"
board_url: ""
board_image: "feather_nrf52832.jpg"
features:
  - Feather-compatible
  - Battery Charging
  - Bluetooth/BTLE
---

The **Adafruit Feather nRF52 Bluefruit** is an easy-to-use all-in-one Bluetooth Low Energy board, with a native-Bluetooth chip, the nRF52832!  It's an 'all-in-one' Bluetooth Low Energy board with built in USB and battery charging.

This chip has twice the flash, SRAM and performance of the earlier nRF51-based Bluefruit modules. It's got tons of awesome peripherals: plenty of GPIO, analog inputs, PWM, timers, etc. Leaving out the extra microcontroller means the price, complexity and power-usage are all lower/better. It allows you to run code directly on the nRF52832 as you would with any other MCU. A single MCU means better performance, lower overall power consumption, and lower production costs if you ever want to design your own hardware based on your Bluefruit nRF52 Feather project. **NOTE: CIRCUITPYTHON 3.0 IS ONLY SUPPORTED.**

**Features:**

*   ARM Cortex M4F (with HW floating point acceleration) running at 64MHz
*   512KB flash and 64KB SRAM
*   **Built in USB Serial converter for fast and efficient programming and debugging**
*   Bluetooth Low Energy compatible 2.4GHz radio (Details available in the [nRF52832](https://www.nordicsemi.com/eng/Products/Bluetooth-low-energy/nRF52832) product specification)
*   **FCC / IC / TELEC certified module**
*   Up to +4dBm output power
*   1.7v to 3.3v operation with internal linear and DC/DC voltage regulators
*   19 GPIO, 8 x 12-bit ADC pins, up to 12 PWM outputs (3 PWM modules with 4 outputs each)
*   Pin #17 red LED for general purpose blinking
*   Power/enable pin
*   Measures 2.0" x 0.9" x 0.28" (51mm x 23mm x 8mm) without headers soldered in
*   Light as a (large?) feather - 5.7 grams
*   4 mounting holes
*   Reset button
*   Optional SWD connector for debugging

Bluetooth Low Energy is the hottest new low-power, 2.4GHz spectrum wireless protocol. In particular, it's the only wireless protocol that you can use with iOS without needing special certification, and it's supported by all modern smart phones. This makes it excellent for use in portable projects that will make use of an iOS or Android phone or tablet. It also is supported in Mac OS X and Windows 8+.

To make it easy to use for portable projects, a connector is added for 3.7V Lithium polymer batteries and built in battery charging. You don't need a battery because it will run just fine straight from the micro USB connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when it's available. Adafruit also tied the battery thru a divider to an analog pin, so you can measure and monitor the battery voltage to detect when you need a recharge.

## Purchase
* [Adafruit](https://www.adafruit.com/product/3406)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
