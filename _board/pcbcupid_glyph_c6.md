---
layout: download
board_id: "pcbcupid_glyph_c6"
title: "Pcbcupid GLYPH C6 Download"
name: "Pcbcupid GLYPH C6"
manufacturer: "Pcbcupid"
board_url:
 - "https://shop.pcbcupid.com/product/gd002"
board_image: "pcbcupid_glyph_c6.jpg"
date_added: 2026-07-10
family: esp32c6
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - USB-C
  - Battery Charging
  - Breadboard-Friendly
---
The Pcbcupid GLYPH C6 is a compact development board based on the ESP32-C6-MINI-1-N4 module, designed for next-gen IoT applications requiring Wi-Fi 6, Bluetooth LE, and Zigbee/Thread (802.15.4) connectivity in one footprint. Onboard LiPo charging makes it ready for portable and battery-backed deployments.

The board features an onboard GLINK connector — QWIIC/STEMMA QT compatible — for solder-free sensor and module integration. It includes auto power switching between USB and battery, battery voltage sensing, and a slide switch to cut battery power entirely.

The GLYPH C6 uses a built-in USB bootloader. Hold BOOT while plugging in USB to enter bootloader mode — it appears as a COM port for flashing.

For peripherals, the ESP32-C6 exposes I2C, SPI (including SDIO-capable pins), and UART via the GPIO matrix. The chip also includes a dedicated low-power (LP) core with its own UART and I2C for ultra-low-power peripheral handling independent of the main processor.

**Board specifications**
  - ESP32-C6-MINI-1-N4 module
  - Single-core 32-bit RISC-V processor up to 160 MHz, 3.3V logic
  - Dedicated low-power RISC-V core for LP peripherals
  - 512KB SRAM, 4MB SPI flash
  - Wi-Fi 6 802.11 ax/b/g/n (2.4 GHz)
  - Bluetooth 5 (LE)
  - 802.15.4 radio for Zigbee/Thread
  - USB-C for power, programming, and serial debugging
  - Built-in LiPo/Li-ion charger with charging status LED
  - Auto power switching between USB and battery
  - Onboard slide switch to cut battery power
  - Battery voltage sensing
  - LiPo solder pads on rear of board
  - 3.3V regulator
  - I2C: SCL=GPIO5, SDA=GPIO4
  - LP I2C: SDA=GPIO6, SCL=GPIO7
  - UART0: TX=GPIO16, RX=GPIO17
  - LP UART: TX=GPIO3, RX=GPIO2
  - SDIO-capable pins: GPIO18-23
  - GLINK connector (QWIIC/STEMMA QT compatible)
  - BOOT and RESET buttons onboard

## Learn More
* [Documentation](https://learn.pcbcupid.com)

## Purchase
* [Pcbcupid](https://shop.pcbcupid.com/product/gd002)
