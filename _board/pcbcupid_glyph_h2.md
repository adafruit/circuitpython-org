---
layout: download
board_id: "pcbcupid_glyph_h2"
title: "Pcbcupid GLYPH H2 Download"
name: "Pcbcupid GLYPH H2"
manufacturer: "Pcbcupid"
board_url:
 - "https://shop.pcbcupid.com/product/gd003"
board_image: "pcbcupid_glyph_h2.jpg"
date_added: 2026-07-10
family: esp32h2
features:
  - Bluetooth/BTLE
  - USB-C
  - Battery Charging
  - Breadboard-Friendly
---
The Pcbcupid GLYPH H2 is a compact development board based on the ESP32-H2-MINI-1-N4 module, purpose-built for BLE, Zigbee, and Thread mesh networking applications. Unlike the C3/C6, the H2 has no Wi-Fi radio — it's optimized specifically for low-power 802.15.4 mesh and BLE connectivity, making it ideal for smart home nodes, sensor mesh networks, and Matter-compatible devices.

The board features an onboard GLINK connector — QWIIC/STEMMA QT compatible — for solder-free sensor and module integration. It includes auto power switching between USB and battery, battery voltage sensing, and a slide switch to cut battery power entirely.

The GLYPH H2 uses a built-in USB bootloader. Hold BOOT while plugging in USB to enter bootloader mode — it appears as a COM port for flashing.

For peripherals, the ESP32-H2 exposes I2C, SPI, and UART via the GPIO matrix. The chip includes a Zero-Cross Detection (ZCD) peripheral on GPIO10/GPIO11, useful for AC dimming and power control applications.

**Board specifications**
  - ESP32-H2-MINI-1-N4 module
  - Single-core 32-bit RISC-V processor, 3.3V logic
  - 4MB SPI flash
  - Bluetooth 5 (LE)
  - 802.15.4 radio for Zigbee and Thread
  - No Wi-Fi
  - USB-C for power, programming, and serial debugging
  - Built-in LiPo/Li-ion charger with charging status LED
  - Auto power switching between USB and battery
  - Onboard slide switch to cut battery power
  - Battery voltage sensing
  - LiPo solder pads on rear of board
  - 3.3V regulator
  - I2C: SCL=GPIO5, SDA=GPIO4
  - SPI: SCK=GPIO11, MOSI=GPIO2(FSPIWP)/GPIO1(FSPICS0), MISO=GPIO0(FSPIQ)
  - UART0: TX=GPIO24, RX=GPIO23
  - Zero-Cross Detection: ZCD0=GPIO10, ZCD1=GPIO11
  - GLINK connector (QWIIC/STEMMA QT compatible)
  - BOOT and RESET buttons onboard

## Learn More
* [Documentation](https://learn.pcbcupid.com)

## Purchase
* [Pcbcupid](https://shop.pcbcupid.com/product/gd003)
