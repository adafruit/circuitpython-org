---
layout: download
board_id: "challenger_nb_rp2040_wifi"
title: "Challenger NB RP2040 WiFi Download"
name: "Challenger NB RP2040 WiFi"
manufacturer: "Invector Labs"
board_url:
 - "https://www.tindie.com/products/invector/challenger-nb-rp2040-wifi/"
board_image: "challenger_nb_rp2040_wifi.jpg"
date_added: 2021-11-15
family: rp2040
download_instructions: https://ilabs.se/product/challenger-nb-rp2040-wifi-with-u-fl-connector/#tab-getting-started
features:
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
  - Feather-Compatible
---

The Challenger NB RP2040 WiFi is an Arduino/Micropython compatible **Challenger NB** (NB for No Battery) format micro controller board based on the Raspberry Pico chip. The **Challenger NB** form factor is based on Adafruits Feather format but we have removed the battery connector, LiPo charger and instead added a bunch of IO pins. It has retained most of the original Feather pinout so most (all) existing feather wings should work nicely with this board as well.

Just like the Challenger RP2040 WiFi it has a ESP8285 WiFi chip. For those of you that is unfamiliar with this device, it is basically an ESP8266 device with an integrated 1MByte of flash memory. This allows us to have an AT command interpreter inside this chip that the main controller can talk to and connect to you local WiFi network. The communications channel between the two devices is an unused UART on the main controller and the standard UART on the ESP8285. As simple as it can be.

The ESP8285 chip comes pre-flashed with Espressif’s AT command interpreter stored in the internal 1MByte of the ESP8285. This interpreter support most of the operating and sleep modes of the standard ESP8266 framework which makes it easy to work with. Talking to the device is as easy as opening the second serial port (Serial2), resetting the ESP8285 and start listening for events and sending commands.

### Technical details

- Raspberry Pi Pico Dual Core Cortex-M0 @ 133 MHz
- 8 MByte FLASH Memory
- 264 KByte SRAM Memory
- 1 Hardware I2C channel
- 1 Hardware SPI channel
- 1 Hardware UART for the user (Serial1)
- 1 Hardware UART connected to the network processor (Serial2 @ 1 Mbit/s)
- 12 Bit ADC.
- ESP8285 with internal 1MByte FLASH Memory
- WiFi (2.4 GHz)
- Espressif AT interpreter
- Communicates at 921600 bits/s
- Neopixel LED
- New fancy schmancy I2C connector =)
- USB-C connector

## Purchase

* [Tindie](https://www.tindie.com/products/invector/challenger-nb-rp2040-wifi/)

