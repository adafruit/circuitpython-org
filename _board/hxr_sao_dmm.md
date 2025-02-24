---
layout: download
board_id: "hxr_sao_dmm"
title: "SAO Digital Multimeter Download"
name: "SAO Digital Multimeter"
manufacturer: "HXR.DK"
board_url:
 - "https://github.com/flummer/dmm-sao"
board_image: "hxr_sao_dmm.jpg"
date_added: 2025-02-24
family: rp2040
downloads_display: true
blinka: false
download_instructions: ""

features:
  - Display
  - USB-C
---

This is a Digital Multimeter in the shape of an SAO (Shitty Add-On/Simple Add-on), designed specifically to assist in electronic badge and SAO development.

This follows the 1.69bis version of the SAO standard ([Shitty Add-on standard](https://hackaday.io/project/52950-shitty-add-ons), [Simple Add-on standard](https://hackaday.io/project/175182-simple-add-ons-sao))

It is based on the RP2040 chip, includes a small OLED display, a rotary encoder for the main knob, a function button for sub functionality selection and two 2mm banana terminals for connecting probes for resistance, LED and continuity testing.

A USB-C connector on the side allows easy modification of the firmware, and boot and reset buttons are also included for convenience, when updating or replacing CircuitPython.

**CAUTION! THIS IS NOT A NORMAL MULTIMETER, AND DOES NOT INCLUDE THE PROTECTION FEATURES NORMALLY FOUND IN A DMM**

If you would like to probe a live circuit, please check [the schematic](https://github.com/flummer/dmm-sao/blob/main/DMM%20SAO%20Schematics.pdf) first, and proceed only if you understand the implications, as improper use might result in a short circuit and harm either the multimeter, the device under test, a connected computer or a combination of those.

**VOLTAGE OR CURRENT SHOULD NEVER BE MEASURED WITH THE PROBES OR TERMINALS ON THE FRONT**

## Features

- Resistance measurement (not the most precise, but should be OK in the range of 50-10K ohm)
- LED Tester (this will lit up the LED if the polarity is correct and show the voltage across it on the screen, 100 ohm resistor in series to 3.3v)
- Continuity tester with buzzer to indicate very low resistance
- Measurement of input voltage on the SAO port
- SAO Port GPIO monitoring (shown as either digital high/low or an analog voltage reading)
- I2C monitor (monitor or scan the I2C bus on the SAO port)

## Technical Details

- Raspberry Pi RP2040 controller
- 16MB SPI flash (W25Q128JVxQ)
- SSD1306 128x64 pixel 0.96" OLED display (white on black)
- Automatic power switching from SAO port to USB-C (both can be connected at the same time)
- Voltage boost circuit for operation on lower than 3.3v on the SAO port
- Maximum input voltage on the SAO port is 3.3v
- UART RX + TX connected to SBU pins on USB-C connector

## Links

- [hackaday.io page](https://hackaday.io/project/198892-sao-digital-multimeter)
- [Github repository](https://github.com/flummer/dmm-sao)
