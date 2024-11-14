---
layout: download
board_id: "bpi_bit_s2"
title: "BPI-Bit-S2 Download"
name: "BPI-Bit-S2"
manufacturer: "Banana Pi"
board_url:
 - "https://wiki.banana-pi.org/BPI-Bit-S2"
board_image: "bpi_bit_s2.jpg"
date_added: 2022-09-14
family: esp32s2
bootloader_id: bpi_bit_s2
download_instructions: https://wiki.banana-pi.org/BPI-Bit-S2#CircuitPython
features:
  - USB-C
  - Wi-Fi
  - Solder-Free Alligator Clip
  - Speaker
---

The BPI-Bit-S2 is a development board equipped ESP32-S2 chip, with 5x5 RGB LED matrix, 1 buzzer, 2 photosensitive sensors, 1 thermosensitive sensor, provides Wi-Fi functions via PCB antenna.

And, the board uses the same edge connector as the micro:bit or micro:bit v2, which makes it possible to connect the alligator clip, or the breakout boards in most micro:bit kits.

**Features:**

- **ESP32-S2N4R2**: Xtensa® single-core 32-bit LX7 microprocessor,
up to 240 MHz; 2.4G Wi-Fi; RISC-V Ultra Low Power Co-processor; **2 MB PSRAM** and **4MB FLASH** are integrated in the package, so don't worry too much about using massive buffers, it's basically sufficient.
- **Native USB Port**: ESP32-S2 full-speed USB OTG interface, using Type-C USB Connector with back-feed protection. The interface is used for power supply to the board, download firmware or programs to the chip.
- **5x5 RGB LED matrix**: 25 WS2812 Lamp beads, addressable, driven by GPIO18.
- **GPIO0 LED**: It lights up by default and acts as a power indicator, controlled by GPIO0.
- **Buzzer**: 8.5mm buzzer, controlled by GPIO17.
- **Photosensitive Sensors**: On the upper front of the board, there is one on each side, read their analog values through GPIO12 and GPIO13.
- **Thermosensitive Sensor**: Directly above pin 2, read its analog values through GPIO14.
- **A/B Button**: A controlled by GPIO38, B controlled by GPIO33.
- **Reset Button**
- **Boot Button**: It is a button that controls boot mode only at startup, and can be used as a normal button at other times. Holding down **Boot** and then pressing **Reset** initiates Firmware Download mode for downloading firmware through the USB port;If UF2 Bootloader already exists, press **Reset** once and press **Boot** once within a second to enter the bootloader.
- **5V to 3.3V DC/DC**: Maximum theoretical output 2A 3.3V.
- **Edge Connector**: Same as the micro:bit, support for alligator clips or the breakout boards in most most micro:bit kits.
