---
layout: download
board_id: "pcbcupid_glyph_s3"
title: "PCBCupid GLYPH S3 Download"
name: "PCBCupid GLYPH S3"
manufacturer: "PCBCupid"
board_url:
 - "https://shop.pcbcupid.com/product/gd004"
board_image: "pcbcupid_glyph_s3.jpg"
date_added: 2026-06-04
family: esp32s3
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - USB-C
  - Battery Charging
  - Breadboard-Friendly
---
The PCBCupid GLYPH S3 is a compact development board based on the ESP32-S3-MINI-1-N8 module, designed for AIoT, edge computing, and computer vision applications. With dual-core performance, wireless connectivity, and onboard LiPo charging, the GLYPH S3 delivers robust capabilities in a breadboard-friendly footprint.

The board features an onboard GLINK connector — QWIIC/STEMMA QT compatible — making it easy to connect hundreds of sensors and modules from Adafruit and SparkFun without soldering. It also includes auto power switching between USB and battery, battery capacity measurement via IO0, and a slide switch to cut battery power entirely.

The GLYPH S3 uses a built-in USB bootloader. To flash firmware, hold BOOT while plugging in USB — it appears as a COM port. Flash CircuitPython as a .bin using esptool.

For peripherals, the ESP32-S3 exposes two I2C controllers, three SPI controllers, and three UART controllers via the GPIO matrix — check the pinout for default assignments. All 20 GPIO pins support PWM with configurable frequency and duty cycle. The chip also includes vector extension instructions for lightweight on-device ML inference.

**Board specifications**
  - ESP32-S3-MINI-1-N8 module 
  - Dual-core Xtensa LX7 processor up to 240 MHz, 3.3V logic
  - 512KB SRAM, 8MB SPI flash (shared between code, files, and OTA)
  - Wi-Fi 802.11 b/g/n (2.4 GHz) with BluFi, ESP-WIFI-MESH
  - Bluetooth 5 LE with ESP-BLE-MESH support
  - USB-C for power, programming, and serial debugging
  - Built-in LiPo/Li-ion charger with charging status LED
  - Auto power switching between USB and battery
  - Reverse voltage protection
  - Onboard slide switch to cut battery power
  - Battery capacity measurement via IO0 (MSR pad)
  - LiPo solder pads on rear of board
  - 3.3V regulator, 900mA peak output
  - 20 GPIO pins
  - 9 × 12-bit ADC1 pins: IO1, IO2, IO4, IO5, IO6, IO7, IO8, IO9, IO10
  - I2C: SDA=IO4, SCL=IO5 (second bus assignable to any GPIO pair)
  - SPI: SCK=IO35, MOSI=IO36, MISO=IO37
  - UART0: TX=IO43, RX=IO44 | UART1: TX=IO17, RX=IO18
  - Onboard LED on GPIO21
  - GLINK connector (QWIIC/STEMMA QT compatible)
  - Dimensions: 50.8mm × 22.8mm × 1.6mm (without headers)

## Learn More
* [Documentation](https://learn.pcbcupid.com/documentation/modules/glyph/glyph-esp32s3/glyph-s3-overview)

## Purchase
* [PCBCupid](https://shop.pcbcupid.com/product/gd004)
