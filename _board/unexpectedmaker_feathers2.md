---
layout: download
board_id: "unexpectedmaker_feathers2"
title: "Unexpected Maker Feather S2 Download"
name: "Unexpected Maker Feather S2"
manufacturer: "Unexpected Maker"
board_url: ""
board_image: "unexpectedmaker_feathers2.jpg"
date_added: 2020-6-14
features:
  - Feather-Compatible
  - Battery Charging
  - Wi-Fi
  - STEMMA QT/QWIIC
---

Introducing the FeatherS2 - The PRO ESP32-S2 based development board in a Feather format!

**Features & Specifications**
 - 32-bit 240 MHz single-core processor 
 - 16 MB SPI Flash
 - 8 MB extra PSRAM
 - 2.4 GHz Wi-Fi - 802.11b/g/n
 - 3D Antenna
 - 2x 700 mA 3.3 V LDO regulator
 - Optimised power path for low-power battery usage
 - LiPo battery management
 - Power (red), Charge (orange) & IO13 (blue) LEDs
 - 21x GPIO
 - USB-C
 - USB backfeed protection
 - APA102 RGB LED (CLK IO45, DATA IO40)
 - ALS-PT19 Ambient Light Sensor (IO14)
 - QWIIC/STEMMA connector
 - Feather format

**2x LDO Voltage Regulators?**
Yup! The first one is for the general operation of the board and the ESP32-S2, RAM and Flash. 

The second LDO is for you to use to connect external 3V3 modules, sensors and peripherals, and it has programmable EN control tied to GPIO21 + it’s connected to the deep sleep capabilities of the S2, so if the S2 goes into deep sleep, the 2nd LDO is automatically shut down for you!

## Purchase
* [Unexpected Maker](https://unexpectedmaker.com/shop/feathers2-esp32-s2)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
