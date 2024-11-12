---
layout: download
board_id: "feather_bluefruit_sense"
title: "Feather Bluefruit Sense Download"
name: "Feather Bluefruit Sense"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4516"
board_image: "feather_bluefruit_sense.jpg"
date_added: 2020-02-01
family: nrf52840
bootloader_id: feather_nrf52840_sense
download_instructions: https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense
features:
  - Feather-Compatible
  - Battery Charging
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

The **Adafruit Feather Bluefruit Sense** takes our popular [Feather nRF52840 Express](https://www.adafruit.com/product/4062) and adds a smorgasbord of sensors to make a great wireless sensor platform. This Feather microcontroller comes with Bluetooth Low Energy and native USB support featuring the nRF52840!  This Feather is an 'all-in-one' Arduino-compatible + Bluetooth Low Energy with built in USB plus battery charging. With native USB it works great with CircuitPython, too.

Like the Feather nRF52840, **this chip comes with Arduino IDE support** - you can program the nRF52840 chip directly to take full advantage of the Cortex-M4 processor, and then calling into the Nordic SoftDevice radio stack when you need to communicate over BLE. Since the underlying API and peripherals are the same for the '832 and '840, you can supercharge your older nRF52832 projects with the same exact code, with a single recompile!

This Feather is also a **BLE-friendly CircuitPython board**! CircuitPython works best with disk drive access, and this is the only BLE-plus-USB-native chip that has the memory to handle running a little Python interpreter. The massive RAM and speedy Cortex M4F chip make this a good match. Make centrals or peripherals with the ease of CircuitPython.

A chorus of supporting sensors surround the module so you can do all sorts of **environmental and motion sensing**:

 * ST Micro series 9-DoF motion - [LSM6DS33 Accel/Gyro](https://www.adafruit.com/product/4480) + [LIS3MDL magnetometer](http://www.adafruit.com/product/4479)
 * [APDS9960 Proximity, Light, Color, and Gesture Sensor](https://www.adafruit.com/product/3595)
 * [PDM Microphone sound sensor](https://www.adafruit.com/product/3492)
 * [SHT Humidity](https://www.adafruit.com/product/4099)
 * [BMP280 temperature and barometric pressure/altitude](https://www.adafruit.com/product/2651)

## Technical details

 * ARM Cortex M4F (with HW floating point acceleration) running at 64MHz
 * 1MB flash and 256KB SRAM
 * **Native Open Source USB stack** - pre-programmed with UF2 bootloader
 * Bluetooth Low Energy compatible 2.4GHz radio (Details available in the [nRF52840](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52840) product specification)
 * **FCC / IC / TELEC certified module**
 * Up to +8 dBm output power
 * 21 GPIO, 6 x 12-bit ADC pins, up to 12 PWM outputs (3 PWM modules with 4 outputs each)
 * Pin #13 red LED for general purpose blinking, Blue LED for general purpose connection status, NeoPixel for colorful feedback
 * Power/enable pin
 * Measures 2.0" x 0.9" x 0.28" (51 mm x 23 mm x 7.2 mm) without headers soldered in
 * Light as a (large?) feather - 6 grams
 * 4 mounting holes
 * Reset button
 * SWD debug pads on bottom of PCB
 * [Works out of the box with all of our Adafruit FeatherWings!](https://www.adafruit.com/categories/814) (Even the UART-using ones like the GPS FeatherWing)

## Purchase

* [Adafruit](https://www.adafruit.com/product/4516)
