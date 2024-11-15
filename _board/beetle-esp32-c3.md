---
layout: download
board_id: "beetle-esp32-c3"
title: "DFRobot Beetle ESP32-C3 Download"
name: "DFRobot Beetle ESP32-C3"
manufacturer: "DFRobot"
board_url:
 - "https://wiki.dfrobot.com/SKU_DFR0868_Beetle_ESP32_C3"
board_image: "beetle-esp32-c3.png"
date_added: 2022-07-17
downloads_display: true
blinka: false
family: esp32c3
bootloader_id: lolin_c3_mini
download_instructions: https://github.com/adafruit/circuitpython/tree/main/ports/espressif#building-and-flashing
features:
  - Battery Charging
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - External Display
  - USB-C
  - Wi-Fi
---

Beetle ESP32-C3, mainly intended for IoT applications, is a controller based on
ESP32-C3 RISC-V 32bit single-core processor.

On a coin-size board of 25*20.5 mm, there are up to 13 IO ports broken out, so
you don't have to worry about running out of IO ports when making projects.
Meanwhile, li-ion battery charging management function is integrated on the
board which allows to directly connect li-ion battery without extra modules,
while ensuring the application size and safety.

The equipped expansion board for Beetle ESP32-C3 brings out more power sources
without increasing product volume, more convenient to solder. Besides, the
onboard easy-to-connect GDI saves the trouble of wiring when using a screen.

## Interface pins

- Digital I/O x13
- LED PWM controller with 6 channels
- SPI x1
- UART x2
- I2C x1
- I2S x1
- Infrared receiver and transmitter: transmit channel x2, receive channel x2,
(any pin)
- 2 × 12-bit SAR A/D converters, 6 channels
- DMA controller, 3 receive channels and 3 transmit channels
- USB Type-C: 5V
- PIN10/LED: Onboard LED pin
- ESP32-C3 module: the latest ESP32-C3 module launched by Espressif
- RST: reset pin, short contact point trigger reset
- TP4057: TP4057 lithium battery charge management chip
- Charge: charging indicator
  - Off: not plugged in power supply or fully charged
  - On: charging
  - Blinking: battery not connected
- 18Pin-FPC:GDI display interface

## To Boot into Firmware Download Mode

![Beetle ESP32 C3 Firmware Download](/assets/images/boards/original/beetle-esp32-c3-downloadmode.png)

1. Pull PIN 9 Down
1. Place a jumper across RST and hold for 3 seconds
1. Release RST and PIN 9
1. Flash as normal per [Espressif port instructions](https://github.com/adafruit/circuitpython/tree/main/ports/espressif#building-and-flashing)

## Purchase
Add any links to purchase the board
* [DFRobot](https://www.dfrobot.com/product-2566.html)
