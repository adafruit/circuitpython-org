---
layout: download
board_id: "bpi_picow_s3"
title: "BPI-PicoW-S3 Download"
name: "BPI-PicoW-S3"
manufacturer: "Banana Pi"
board_url:
 - "https://wiki.banana-pi.org/BPI-PicoW-S3"
board_image: "bpi_picow_s3.jpg"
date_added: 2022-10-11
family: esp32s3
bootloader_id: bpi_picow_s3
download_instructions: https://wiki.banana-pi.org/BPI-PicoW-S3#CircuitPython
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - Castellated Pads
---

BPI-Pico-S3 is the same size as Raspberry Pi Pico board, equipped with ESP32S3 chip, 8M flash, 4-layer PCB, electroplated half-hole process, ceramic antenna, supports 2.4 GHz Wi-Fi and Bluetooth® LE dual-mode wireless communication, is a development board designed for IoT development and Maker DIY.

**Features:**

- **ESP32-S3R2**: Xtensa® dual-core 32-bit LX7 microprocessor,
up to 240 MHz; 2.4G Wi-Fi + Bluetooth LE; RISC-V Ultra Low Power Co-processor; **2 MB Quad SPI PSRAM** is integrated in the package, so don't worry too much about using massive buffers, it's basically sufficient.
- **8MB Quad SPI Flash**
- **Pins and Pads**: It's the same size as Raspberry Pi Pico board, can also have headers soldered in for use in a breadboard or perfboard, or can be soldered directly onto a PCB with the castellated pads. There's 20 pads on each side, with groups of general purpose input-and-output (GPIO) pins interleaved with plenty of ground pins.
- **Order of Pins**: Keep the same order as Raspberry Pi Pico board in circuitpython. You get a total of 27 GPIO pins, 4 of those can be analog inputs.The ADC_VREF on Raspberry Pi Pico was change to GP29_A3 on BPI-PicoW-S3. In fact, the pin function assignments of ESP32S3 and RP2040 chip are not exactly the same, so redefine the pin order in circuitpython to adapt.
- **Native USB Port**: ESP32-S3 full-speed USB OTG interface, using microUSB Connector with back-feed protection. The interface is used for power supply to the board, for flashing applications to the chip, for communication with the chip using USB protocols, as well as for JTAG debugging.
- **5V to 3.3V DC/DC**: Maximum theoretical output 2A 3.3V.
- **Reset Button**: Support double-clicking the reset button to enter the UF2 bootloader.
- **BOOT0**: If the UF2 Bootloader is removed, you can use any conductor bar such as metal pins or tweezers to short it to put the EPS32S3 chip into bootloader mode, then the UF2 Bootloader can be re-installed.
  - Plug board into a USB port on your computer using a data/sync cable. Make sure it is the only board plugged in, and that a charge-only cable is not being used.
  - Short circuit BOOT0 contact.
  - Press and release the Reset button.
  - Release the BOOT0 contact.
- **RGB LED**: Addressable WS2812 RGB LED, control it with board.NEOPIXEL in circuitpython.
- **Monochrome LED**: Control it with board.GP25 or board.LED in circuitpython.

## Purchase

[Aliexpress shop](https://www.aliexpress.com/item/1005004775634442.html)