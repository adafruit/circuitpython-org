---
layout: download
board_id: "feather_stm32f405_express"
title: "Feather STM32F405 Express Download"
name: "Feather STM32F405 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4382"
board_image: "feather_stm32f405_express.jpg"
date_added: 2019-09-26
family: stm
download_instructions: https://learn.adafruit.com/adafruit-stm32f405-feather-express/circuitpython-setup
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

ST takes flight in this upcoming Feather board. The new STM32F405 Feather (video) that we designed runs CircuitPython at a blistering 168MHz – our fastest CircuitPython board ever! We put a STEMMA QT / Qwiic port on the end, so you can really easily plug and play I2C sensors.

This Feather has lots of goodies:

STM32F405 Cortex M4 with 1MB Flash, 168MHz speed
3.3V logic, but almost all pins are 5V compliant!
USB C power and data - our first USB C Feather!
LiPo connector and charger
SD socket on the bottom, connected to SDIO port
2 MB SPI Flash chip
Built in NeoPixel indicator
I2C, UART, GPIO, ADCs, DACs
Qwiic/STEMMA-QT connector for fast I2C connectivity
We use the built-in USB DFU bootloader to load firmware. It does not come with a UF2 bootloader.
With CircuitPython basics running on this board, it's fast to get all our drivers working, then use the built in plotter in Mu to instantly get sensor data displaying within 3 minutes of unboxing.

You can use MicroPython, CircuitPython or Arduino IDE with this board, with some caveats. This board and chipset is new so expect rapid developments and updates!

CircuitPython support is under development. We have digital IO, analog in/out, I2C, SPI, PWM working so far and more on the way. For example, the SDIO SD card is not yet supported natively. DisplayIO is also not yet supported.
Arduino is supported through STM32duino. There's no auto-reset bootloader support yet so you have to pull the BOOT0 pin high and manually reset before uploading. That said, STM32 support is really good, and we were able to run just about every sketch we tried.
MicroPython support is very solid but Adafruit does not provide MicroPython libraries for sensors!
We tested this in Arduino STM32duino with all our FeatherWings and only the RFM69/RFM9x libraries did not work (they are very platform specific). Its an extraordinarily fast Feather, and our first foray into STM32 - very exciting!

## Tutorial

- [Feather STM32F405 Express Overview](https://learn.adafruit.com/adafruit-stm32f405-feather-express)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4382)
