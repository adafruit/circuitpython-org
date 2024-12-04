---
layout: download
board_id: "0xcb_helios"
title: "0xCB Helios Download"
name: "Helios"
manufacturer: "0xCB"
board_url:
 - "https://github.com/0xCB-dev/0xCB-Helios"
board_image: "0xcb_helios.jpg"
date_added: 2023-01-05
family: rp2040
features:
  - USB-C
  - Breadboard-Friendly
---

The 0xCB Helios is our Elite-C compatible MicroController, based on the high-performance and affordable RP2040.

It's a drop-in replacement for legacy ProMicro boards.

## Technical details

- **Powerful RP2040** 32-bit Cortex M0+ dual core running at 133 MHz and 264kB SRAM.
- **16MB/128Mb QSPI FLASH** chip for storing files and code
- **Only 3.16 mm thick** thanks to a mid-mounted USB-C port
- 3.3V 500mA LDO, PTC fuse and **ESD protection** chip
- Elite-C, Pro Micro, SparkFun Pro Micro RP2040, and nice!Nano compatible pinout (follows the **BastardKb standard**)
- **8 extra I/O pins**: (GP12-GP16) added along the bottom edge, (GP10-GP11) at the top and a 5V level shifted pin to drive RGB LEDs for example (GP25)
- **25 available digital pins** for a maximum of 13x12 = 156 switches (using a standard matrix)
- Default off **red power LED** (selectable via a jumper on the left side)
- **blue user LED** on pin GP17
- 4 pins configurable as **analog inputs**
- **USB D+/D- broken out** for use with an external USB socket/daughterboard
- **USB VBUS detection** on GPIO19 for split keyboard side detection
- **UF2 bootloader** for drag & drop programming via your file manager
- easy to use and backward compatible **Single button boot and reset circuit** push to reset and hold >500ms to enter bootloader (legacy boards with reset buttons will continue to work!)
- **RAW / VBUS** output, for powering RGB LEDs or other 5 V devices. The jumper on top lets you skip over the 500 mA fuse and Schottky diode, for up to 3A from USB ports.
- **USB-C connector** lets you access built-in ROM USB bootloader and serial port debugging

## Purchase

- [KeebSupply](https://keeb.supply/products/0xcb-helios)
