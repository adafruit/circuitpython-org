---
layout: download
board_id: "thepihut_baguette_s3"
title: "Baguette S3 Download"
name: "Baguette S3"
manufacturer: "ThePiHut"
board_url:
 - "https://thepihut.com/products/baguette-s3-esp32-s3-prototyping-board"
board_image: "thepihut_baguette_s3.jpg"
date_added: 2026-10-28
downloads_display: true
blinka: false
download_instructions: "https://thepihut.com/blogs/raspberry-pi-tutorials/baguette-s3-user-guide"
family: esp32s3
bootloader_id:
features:
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - STEMMA QT/QWIIC
  - USB-C
  - Wi-Fi
---

The Baguette S3 is a compact ESP32-S3 prototyping board from The Pi Hut. All of its pins sit in a single row, so it fits a half-size breadboard while leaving the other side free for your circuit.

Features:

* ESP32-S3-MINI-1-N8 module with 8MB flash
* 2.4GHz Wi-Fi and Bluetooth 5 (LE)
* 27 GPIO on a single 30-pin header, including UART (TX/RX) and I2C (SDA/SCL)
* Qwiic / STEMMA QT connector (3.3V)
* MicroSD card slot
* WS2812C RGB LED
* RESET and BOOT buttons
* USB-C for power and programming

In CircuitPython, the header pins are named after the labels printed on the board, such as `board.IO5` and `board.RX`. The Qwiic port is available as `board.STEMMA_I2C()`, and the SD card has its own bus, `board.SD_SPI()`, with `board.SD_CS` as chip select.

## Purchase

* [The Pi Hut](https://thepihut.com/products/baguette-s3-esp32-s3-prototyping-board)
