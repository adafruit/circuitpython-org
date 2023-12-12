---
layout: download
board_id: "olimex_a20_lime2"
title: "A20-OLinuXino-LIME2 Download"
name: "A20-OLinuXino-LIME2"
manufacturer: "Olimex"
board_url:
 - "https://www.olimex.com/wiki/A20-OLinuXino-LIME2"
board_image: "olimex_a20_lime2.jpg"
download_instructions: ""
downloads_display: true
blinka: true
date_added: 2023-12-11
features:
  - Ethernet
  - HDMI/DisplayPort
  - 40-pin GPIO
  - Infrared Receiver
---

A20-OLinuXino-LIME2 looks similar to both [A20-OLinuXino-LIME](https://www.olimex.com/wiki/A20-OLinuXino-LIME) and [A10-OLinuXino-LIME](https://www.olimex.com/wiki/A10-OLinuXino-LIME). The major differences between A20-OLinuXino-LIME2 and A20-OLinuXino-LIME are:

- LIME2 has gigabit Ethernet (GbE), compared to the standard 100Mb Ethernet of the LIME
- LIME2 design provides double the RAM memory, compared to the LIME design (1024 vs 512)
- Much better routing of DDR3 memory.
- Increased the number of layers from 6 in LIME to 8 in LIME2
- Corrected pinout of the LCD and GPIO connectors (shields designed for the LIME layout are not compatible with the LIME2 layout)


The A10 and the A20 processors are pin-to-pin compatible. Because of the processor, software-wise the board is closer to [A20-OLinuXino-LIME](https://www.olimex.com/wiki/A20-OLinuXino-LIME) than to the [A10-OLinuXino-LIME](https://www.olimex.com/wiki/A10-OLinuXino-LIME). This resemblance to other designs definitely might speed the development on the board - a lot of software written for A20-OLinuXino-LIME might work out-of-the-box with A20-OLinuXino-LIME2. Additionally, pinout tables, GPIO maps, etc released for A20-OLinuXino-LIME would apply to A20-OLinuXino-LIME2 **(except for the 0.05" step connectors - LCD display and all the GPIOs connectors, which have a different layout compared to both A20-OLinuXino-LIME and A10-OLinuXino-LIME)**.

A20-OLinuXino-LIME2 features:

- A20 Cortex-A7 dual-core ARM Cortex-A7 CPU and dual-core Mali 400 GPU
- **1GB DDR3 RAM memory**
- **1 gigabit native Ethernet**
- optional 4GB NAND FLASH memory
- SATA connector with 5V SATA power jack
- HDMI FullHD 1080p
- 2x USB Low-Full-High-Speed hosts with power control and current limiter
- USB-OTG with power control and current limiter
- LiPo Battery connector with battery-charging capabilities
- LCD connector compatible with with 4.3", 7.0", 10.1" LCD modules from Olimex
- 160 GPIOs on three GPIO connectors
- MicroSD card connector
- DEBUG-UART connector for console debug with USB-SERIAL-CABLE-F
- status LED
- Battery charge status LED
- Power LED
- 2KB EEPROM for MAC address storage and more
- 2 BUTTONS with ANDROID functionality + RESET button
- 2 mount holes
- 5V input power supply, noise immune design
- PCB dimensions: 84 x 60 mm

## Purchase
* [Olimex](https://www.olimex.com/Products/OLinuXino/A20/A20-OLinuXino-LIME2/open-source-hardware)
