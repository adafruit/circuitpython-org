---
layout: download
board_id: "pcbcupid_glyph_c3"
title: "Pcbcupid GLYPH C3 Download"
name: "Pcbcupid GLYPH C3"
manufacturer: "Pcbcupid"
board_url:
 - "https://shop.pcbcupid.com/product/gd001"
board_image: "pcbcupid_glyph_c3.jpg"
date_added: 2026-07-10
family: esp32c3
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - USB-C
  - Battery Charging
  - Breadboard-Friendly
---
The Pcbcupid GLYPH C3 is a compact development board based on the ESP32-C3-MINI-1-N4 module, built for low-power IoT, sensor nodes, and Wi-Fi/BLE connected embedded projects. With a RISC-V core, integrated wireless, and onboard LiPo charging, the GLYPH C3 packs full connectivity into a breadboard-friendly footprint.

The board features an onboard GLINK connector — QWIIC/STEMMA QT compatible — for solder-free sensor and module integration. It includes auto power switching between USB and battery, battery voltage sensing, and a slide switch to cut battery power entirely.

The GLYPH C3 uses a built-in USB bootloader. Hold BOOT while plugging in USB to enter bootloader mode — it appears as a COM port for flashing. Note: CIRCUITPY_USB_DEVICE is disabled at the port level for all C3 boards, so there's no mass storage drive when running CircuitPython — use `ampy` or the serial REPL for file transfer instead.

For peripherals, the ESP32-C3 exposes I2C, SPI, and UART via the GPIO matrix — default pin assignments are silkscreened. All GPIO pins support PWM.

**Board specifications**
  - ESP32-C3-MINI-1-N4 module
  - Single-core 32-bit RISC-V processor up to 160 MHz, 3.3V logic
  - 400KB SRAM, 4MB SPI flash
  - Wi-Fi 802.11 b/g/n (2.4 GHz)
  - Bluetooth 5 (LE)
  - USB-C for power, programming, and serial debugging
  - Built-in LiPo/Li-ion charger with charging status LED
  - Auto power switching between USB and battery
  - Onboard slide switch to cut battery power
  - Battery voltage sensing
  - LiPo solder pads on rear of board
  - 3.3V regulator
  - I2C: SCL=GPIO5, SDA=GPIO4
  - SPI: SCK=GPIO10, MOSI=GPIO6, MISO=GPIO7
  - UART0: TX=GPIO21, RX=GPIO20
  - GLINK connector (QWIIC/STEMMA QT compatible)
  - BOOT and RESET buttons onboard

## Learn More
* [Documentation](https://learn.pcbcupid.com)

## Purchase
* [Pcbcupid](https://shop.pcbcupid.com/product/gd001)
