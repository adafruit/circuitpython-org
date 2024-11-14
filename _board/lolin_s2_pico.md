---
layout: download
board_id: "lolin_s2_pico"
title: "LOLIN S2 Pico Download"
name: "LOLIN S2 Pico"
manufacturer: "Wemos"
board_url:
 - "https://www.wemos.cc/en/latest/s2/s2_pico.html"
board_image: "lolin_s2_pico.jpg"
date_added: 2021-11-02
family: esp32s2
bootloader_id: lolin_s2_pico
download_instructions: https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_circuitpython_s2.html
features:
  - Wi-Fi
  - USB-C
  - Display
  - Breadboard-Friendly
---

A development boards with an OLED and a small form factor.

## Features

- ESP32-S2FN4R2 WiFi SoC
  - Xtensa® single-core 32-bit LX7 microprocessor, up to 240 MHz
  - Integrated 802.11 b/g/n WiFi 2.4 GHz Transceiver, up to 150 Mbps
  - Integrated RISC-V ULP Coprocessor
  - Integrated Temperature Sensor (-20 °C to 110 °C)
  - Operating Voltage: 3.0 to 3.6 V (WiFi: 310 mA (peak), Modem sleep: 12-19 mA, Light sleep: 450 µA, Deep sleep: 20-190 µA)
  - 320 KB SRAM, 4 MB Flash (embedded), 2 MB PSRAM (embedded), 16 KB SRAM in RTC (accessable by main CPU, 8 KB accessable by ULP coprocessor), 4 Kbit eFuse (1792 bits reserved for user data)
  - 2 x 13-bit SAR ADCs, up to 20 channels (2 channels not available on ADC2 due to USB D+/D-)
  - 2 x 8-bit DAC, 14 x touch sensing IOs
  - 4 x SPI (2 usable due to embedded flash & PSRAM), 1 x I2S, 2 x I2C, 2 x UART
  - 1 x DVP 8/16 camera interface, implemented using the hardware resources of I2S
  - 1 x LCD interface SPI2 (8-bit serial RGB/8080/6800), 1 x LCD interface I2S (8/16/24-bit parallel)
  - 1 x TWAI® controller compatible with ISO 11898-1 (CAN Specification 2.0)
  - LED PWM controller, up to 8 channels
  - USB OTG 1.1 controller and PHY, with host and device support
  - Cryptographic Hardware Accelerators: AES, ECB/CBC/OFB/CFB/CTR, GCM, SHA, RSA, ECC (Digital Signature)
- USB-C connector, for built-in ROM USB bootloader, serial port debugging, and USB device mode
- 27 x GPIO pins, plus `VBUS`, `3V3`, `GND`
  - 21 x pins broken out to breadboard-friendly headers
  - `EN` RESET button
  - `GPIO0` BOOT button
  - `GPIO10` LED (blue status LED)
  - Lolin I2C JST SH 4-pin port (**does not match QWIIC/Stemma-Qt pinout**) using `GPIO8` (SDA) and `GPIO9` (SCL)
  - 128 x 32 SSD1306 OLED display internally connected to the same I2C bus as the external port, reset pin connected to `GPIO18`, I2C address `0x3C` (**native support in CircuitPython started with firmware version 8.1.0-beta.0, otherwise user code initialization is required**)
- Compatible with CircuitPython, MicroPython (default firmware), Arduino and ESP-IDF

## Purchase

* [AliExpress](https://www.aliexpress.com/item/1005003215673294.html)

## Learn More

* [Manufacturer Specifications](https://www.wemos.cc/en/latest/s2/s2_pico.html)
* [Schematic](https://www.wemos.cc/en/latest/_static/files/sch_s2_pico_v1.0.0.pdf)
* [Dimension](https://www.wemos.cc/en/latest/_static/files/dim_s2_pico_v1.0.0.pdf)
* [Factory MicroPython firmware](https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_micropython_s2.html)
