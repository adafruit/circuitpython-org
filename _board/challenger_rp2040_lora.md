---
layout: download
board_id: "challenger_rp2040_lora"
title: "Challenger RP2040 LoRa Download"
name: "Challenger RP2040 LoRa"
manufacturer: "Invector Labs"
board_url:
 - "https://www.tindie.com/products/invector/challenger-rp2040-lora-915mhz/"
 - "https://thepihut.com/products/challenger-rp2040-lora-868mhz"
board_image: "challenger_rp2040_lora.jpg"
date_added: 2022-06-09
family: rp2040
download_instructions: https://ilabs.se/product/challenger-rp2040-lora/#tab-getting-started
features:
  - LoRa/Radio
  - Battery Charging
  - Feather-Compatible
  - USB-C
  - Breadboard-Friendly
---

The iLabs Challenger RP2040 LoRa is a small embedded computer equipped with a LoRa modem module on board, in the popular [Adafruit Feather form factor](https://www.adafruit.com/?q=feather). It is based on an RP2040 microcontroller from Raspberry Pi which is a dual-core Cortex M0 that can run on a clock up to 133MHz.

This is a spin-off from our [Challenger RP2040 WiFi ](/board/challenger_rp2040_wifi/) board but we have replaced the WiFi module with a low power RFM95W LoRa radio module from Hope RF. The transceiver features a LoRa long range modem that provides ultra-long range spread spectrum communication and high interference immunity whilst minimizing current consumption.

The RFM95W is connected to the microcontroller using an SPI channel and a few GPIO signals to handle signalling from the modem circuit. Besides the modem module, there is only one additional U.FL connector that forms the modem functionality. Simply hook your external antenna to this connector and you are ready to go.

We paired the RP2040 with 8MByte high-speed flash capable of supplying data up to the max speed. The flash memory can be used both to store instructions for the microcontroller as well as data in a file system and having a file system available makes it easy to store data in a structured and easy to program approach.

The device can be powered by a Lithium Polymer battery connected through a standard 2.0mm connector on the side of the board. An internal battery charging circuit allows you to charge your battery safely and quickly. The device is shipped with a programming resistor that sets the charging current to ~450mA. this resistor can be exchanged by the user to either increase or decrease the charging current, depending on the battery that is being used.

## Purchase
* 915MHz Version: [Tindie](https://www.tindie.com/products/invector/challenger-rp2040-lora-915mhz/)
* 868 MHz Version: [PiHut](https://thepihut.com/products/challenger-rp2040-lora-868mhz)
