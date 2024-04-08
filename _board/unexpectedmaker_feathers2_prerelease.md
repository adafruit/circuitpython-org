---
layout: download
board_id: "unexpectedmaker_feathers2_prerelease"
title: "Unexpected Maker FeatherS2 Prerelease Download"
name: "Unexpected Maker FeatherS2 Prerelease"
manufacturer: "Unexpected Maker"
board_url:
 - "https://unexpectedmaker.com/shop/feathers2-esp32-s2"
 - "https://www.adafruit.com/product/4769"
board_image: "unexpectedmaker_feathers2_prerelease.jpg"
date_added: 2020-06-14
family: esp32s2
bootloader_id: unexpectedmaker_feathers2
features:
  - Feather-Compatible
  - Battery Charging
  - Wi-Fi
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

Pre-Release version of the FeatherS2
For those that purchased the pre-release version and would like to run CircuitPython on it without having to compile from source.

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

You can find out more about the FeatherS2 at [feathers2.io](https://feathers2.io), including how to [install the UF2 Bootloader](https://feathers2.io/install_uf2.html).

## Purchase
The FeatherS2 pre-release boards are no longer available for purchase now that the final release version is out, which you can grab from these locations:

* [Unexpected Maker](https://unexpectedmaker.com/shop/feathers2)
* [Adafruit](https://www.adafruit.com/product/4769)
