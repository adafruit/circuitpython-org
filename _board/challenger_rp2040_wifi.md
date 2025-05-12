---
layout: download
board_id: "challenger_rp2040_wifi"
title: "Challenger RP2040 WiFi Download"
name: "Challenger RP2040 WiFi"
manufacturer: "Invector Labs"
board_url:
 - "https://www.tindie.com/products/invector/challenger-rp2040-wifi/"
board_image: "challenger_rp2040_wifi.jpg"
date_added: 2021-09-16
family: rp2040
download_instructions: https://ilabs.se/product/challenger-2040-wifi-chip/#tab-getting-started
features:
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
  - Feather-Compatible
  - Battery Charging
---

The Challenger RP2040 WiFi is an Arduino/Micropython compatible Adafruit Feather format micro controller board based on the Raspberry Pico chip.

When we designed this board we took our existing Challenger M0 WiFi board and replaced the SAMD21 micro controller with the much more powerful dual core RP2040 Cortex-M0 device. The RP2040 have two Cortex-M0 CPU cores clocked at 133 Mhz and 264 Kbyte SRAM integrated. On our board we decided to put a 8 MByte flash memory for your programs and file storage.

Just like the Challenger M0 WiFi it has a ESP8285 WiFi chip. For those of you that is unfamiliar with this device, it is basically an ESP8266 device with an integrated 1 MByte of flash memory. This allows us to have an AT command interpreter inside this chip that the main controller can talk to and connect to you local WiFi network. The communications channel between the two devices is an unused UART on the main controller and the standard UART on the ESP8285. As simple as it can be.

### Technical details

- Raspberry Pi Pico Dual Core Cortex-M0 @ 133 MHz
- 8 MByte FLASH Memory
- 264 KByte SRAM Memory
- 1 Hardware I2C channel
- 1 Hardware SPI channel
- 1 Hardware UART for the user (Serial1)
- 1 Hardware UART connected to the network processor (Serial2 @ 1Mbit/s)
- 12 Bit ADC.
- ESP8285 with internal 1MByte FLASH Memory
- WiFi (2.4 GHz)
- Espressif AT interpreter
- Communicates at 921600 bits/s
- Neopixel LED
- LiPo charger circuit with 250 mA charging current
- Standard LiPo battery connector
- USB-C connector

## Purchase

* [Tindie](https://www.tindie.com/products/invector/challenger-rp2040-wifi/)

