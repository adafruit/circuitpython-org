---
layout: download
board_id: "adafruit_feather_esp32c6_4mbflash_nopsram"
title: "Feather ESP32-C6 4MB Flash No PSRAM Download"
name: "Feather ESP32-C6 4MB Flash No PSRAM"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5933"
board_image: "adafruit_feather_esp32c6_4mbflash_nopsram.jpg"
date_added: 2024-03-18
family: esp32c6
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-esp32-c6-feather/install-circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly

---

The ESP32-C6 is Espressif’s first Wi-Fi 6 SoC integrating 2.4 GHz Wi-Fi 6, Bluetooth 5 (LE) and the 802.15.4 protocol. It brings the goodness you know from the [low-cost C3 series](https://www.adafruit.com/product/5337) and improves it with Zigbee/802.15.4 at 2.4Ghz. [That means it could make for great Matter development hardware](https://csa-iot.org/all-solutions/matter/)!

We took our Feather ESP32-S2 and swapped out the 'S2 for a C6. Plus some re-routing and here's what we've got: a C6 Feather with lots of GPIO, lipoly charging and monitoring with the MAX17048, NeoPixel, I2C Stemma QT port, and a second low-quiescent LDO for disabling the I2C and NeoPixel when we want ultra-low power usage - as low as 17uA in deep sleep.

One thing to watch for is that, like the C3, the C6 does not have native USB. It does have a 'built in' USB Serial core that can be used for debugging, but it cannot act like a mouse, keyboard, or disk drive. That means if you are running CircuitPython you will need to use WiFi, Bluetooth or WebSerial for transferring files back and forth rather than drag-and-dropping to a drive. Ditto for the bootloader side, this chip cannot run UF2.

## Purchase

* [Adafruit](https://www.adafruit.com/product/5933)
