---
layout: download
board_id: "lolin_c3_mini"
title: "LOLIN C3 Mini Download"
name: "LOLIN C3 Mini"
manufacturer: "Wemos"
board_url:
 - "https://www.wemos.cc/en/latest/c3/c3_mini.html"
board_image: "lolin_c3_mini.png"
date_added: 2021-11-02
family: esp32c3
bootloader_id: lolin_c3_mini
download_instructions: https://www.wemos.cc/en/latest/tutorials/c3/get_started_with_circuitpython_c3.html
features:
  - Wi-Fi
  - USB-C
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

A mini Wi-Fi & Bluetooth LE board based on ESP32-C3FH4.

## Features

- based ESP32-C3 WIFI & Bluetooth LE RISC-V Single-Core CPU
- Type-C USB
- 4MB Flash
- Clock speed: 160 Mhz
- 12x Digital IO
- ADC, I2C, SPI, UART
- Size: 34.3 mm x 25.4 mm
- Weight: 2.6g
- Compatible with LOLIN D1 mini shields
- Compatible with MicroPython, Arduino and ESP-IDF
- Default firmware: MicroPython


## About Board Versions

Circuitpython builds after 8.0.0-beta6 target the v2.1 revision of this board. V1.0 had a design flaw
in the antenna circuitry which cannot be compensated for in software. V2.1 replaces the PCB trace antenna
with a small ceramic antenna and the status LED on GPIO7 is replaced by a WS2812B RGB addressable LED.

Using 8.0.0-beta6 or earlier builds on a v2.1 board or post-8.0.0-beta6 builds on a 1.0 board will not result in proper
status LED operation.

V1.0 boards need set WIFI Tx Power to 8.5dBm in order to use WIFI.

`wifi.radio.tx_power = 8.5`

## Purchase

* [AliExpress](https://www.aliexpress.com/item/1005004740051202.html)

## Learn More

* [Manufacturer Specifications](https://www.wemos.cc/en/latest/c3/c3_mini.html)
* [ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
* [Schematic](https://www.wemos.cc/en/latest/_static/files/sch_c3_mini_v2.1.0.pdf)
* [Dimension](https://www.wemos.cc/en/latest/_static/files/dim_c3_mini_v1.0.0.pdf)
