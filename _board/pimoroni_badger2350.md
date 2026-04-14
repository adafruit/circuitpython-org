---
layout: download
board_id: "pimoroni_badger2350"
title: "Badger 2350 Download"
name: "Badger 2350"
manufacturer: "Pimoroni"
board_url:
 - "https://shop.pimoroni.com/products/badger-2350"
board_image: "pimoroni_badger2350.jpg"
date_added: 2026-04-13
download_display: true
blinka: false
download_instructions: https://badgewa.re/
family: rp2350
bootloader_id:
features:
  - Battery Charging
  - Display
  - STEMMA QT/QWIIC
  - USB-C
  - Wi-Fi
---

Badger 2350 is an all-in-one badge wearable with a fast updating 2.7"
electronic paper screen, built-in rechargeable battery and sturdy
polycarbonate case. Hang it round your neck with the (included) Badger
lanyard or prop it up on your desk - either way it's ready to go
straight out of the box. It's way more than just a event badge too -
the four-level greyscale screen would also be great for displaying
charts, signage or QR codes.


## Features

* Display: 2.7" four-level greyscale electronic paper (264 x 176 pixels)
* Powered by RP2350A (Dual Arm Cortex M33 running at 250MHz with 520KB of SRAM)
* 16MB of QSPI flash supporting XiP
* 8MB of PSRAM
* Raspberry Pi RM2 module (CYW43439), supporting IEEE 802.11 b/g/n wireless LAN, and Bluetooth
* 1000mAh LiPo battery:
  * MCP73831 charger with 455mA charging current (datasheet)
  * XB6096I2S battery protector (datasheet)
* PCF85063A real-time clock for waking from sleep (datasheet)
* Polycarbonate case with teal back
* 4-zone mono LED case lighting
* Buttons:
  * Five front user buttons
  * Reset (and sleep) button
  * Home (and boot) button
* Connectors:
  * USB-C connector for charging and programming
  * I2C connector (Qwiic/STEMMA QT) for attaching breakouts
  * SWD debug connector
* Comes fully-assembled (no soldering required)
* Includes matching 2-clip lanyard
* Dimensions with case: 84mm (W) x 76mm (H) x 20mm (D)


## Note

There is no power switch. Since mainline CircuitPython does not
support low-power modes for the RP2350 (i.e. sleep/deep-sleep), the
LiPo will be drained fast when running with CircuitPython. So to make
full use of this board you either have to hack the hardware and add a
power-switch, or hack CircuitPython and implement the alarm-module for
the RP2350.


## Misc

* [Example code](https://github.com/bablokb/circuitpython-examples/tree/main/badger2350)


## Purchase

* [Pimoroni](https://shop.pimoroni.com/products/badger-2350)
