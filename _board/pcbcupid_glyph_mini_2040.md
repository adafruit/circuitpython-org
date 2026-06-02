---
layout: download
board_id: "pcbcupid_glyph_mini_2040"
title: "PCBCupid Glyph Mini 2040 Download"
name: "Glyph Mini 2040"
manufacturer: "PCBCupid"
board_url:
 - "https://shop.pcbcupid.com/product/gdm001"
board_image: "pcbcupid_glyph_mini_2040.jpg"
date_added: 2026-05-29
family: rp2040
features:
  - USB-C
  - Breadboard-Friendly
---
The PCBCupid Glyph Mini 2040 is a compact, high-performance microcontroller board designed for space-constrained embedded and educational projects. Powered by the Raspberry Pi Rp2040 dual-core Arm Cortex-M0+ processor running at up to 133 MHz, it offers 264KB of SRAM and 8MB of external QSPI flash for program storage.

 It features 20 GPIO pins, 12-bit ADC inputs, I²C, SPI, USB Serial, and UART peripherals for seamless interfacing with sensors, displays, and external modules. Castellated pads allow direct soldering onto carrier boards, and the USB-C connector keeps it modern and easy to use.

Inside the Glyph Mini 2040 is a 'permanent ROM' USB UF2 bootloader. When you want to program new firmware, hold down the BOOT button while plugging it into USB (or pulling down the RUN/Reset pin to ground) and it will appear as a USB disk drive you can drag the firmware onto. Just note you don't double-click reset  instead hold down BOOT during startup to enter the bootloader.

For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs multiplexed across the GPIO check the pinout for which pins map to which. There are 16 PWM channels, each pin has a channel it can be set to.

There's no I2S peripheral, SDIO, or camera but instead of specific hardware support for these, the Glyph Mini 2040 comes with the PIO state machine system. This is a unique and powerful way to create custom hardware logic and data processing blocks that run independently without consuming CPU. 

While the Glyph Mini 2040 has 264KB of onboard RAM, flash memory is provided by an external QSPI chip. The Glyph Mini 2040 has 8MB of flash, shared between the running program and file storage for MicroPython or CircuitPython. With C/C++ you get the full 8MB with Python you'll have about 7MB remaining for code, files, images, fonts, etc.

**Board specifications**
  - Rp2040 microcontroller chip designed by Raspberry Pi
  - Dual-core Arm Cortex M0+ processor, flexible clock running up to 133 MHz
  - 264KB of SRAM, and 8MB of on-board Flash memory
  - USB-C connector for programming and power
  - Castellated pads for direct carrier board soldering
  - Onboard LED on GP16
  - USB 1.1 with device and host support
  - Low-power sleep and dormant modes
  - Drag-and-drop programming using mass storage over USB
  - 2 × SPI, 2 × I2C, 2 × UART peripherals
  - 4 × 12-bit ADC inputs (GP26–GP29)
  - 16 × controllable PWM channels
  - 8 × Programmable I/O (PIO) state machines for custom peripheral support
  - Accurate clock and timer on-chip
  - Temperature sensor
  - Accelerated floating-point libraries on-chip
  - Dimensions: 18mm × 23.5mm × 1.8mm

## Learn More
* [Documentation](https://learn.pcbcupid.com/boards/glyph_mini/overview-rp_2040)

## Purchase
* [PCBCupid](https://shop.pcbcupid.com/product/gdm001)