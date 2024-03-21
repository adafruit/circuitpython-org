---
layout: download
board_id: "bdmicro_vina_d51_pcb7"
title: "Vina-D51 (PCB 7) Download"
name: "VINA-D51 (PCB 7)"
manufacturer: "BDMICRO, LLC"
board_url:
 - "https://bdmicro.com/products/vina-d51"
board_image: "bdmicro_vina_d51.jpg"
date_added: 2021-05-26
family: atmel-samd
features:
  - Wi-Fi
---

The VINA-D51 is a powerful, robust, pluggable control module designed for modular control applications, even in harsh environments. Built with all-industrial grade components, latching connectors and features, it is well-suited for a wide variety of automation and control applications.

* **Performance**: Powerful 32-bit ARM Cortex M4 microcontroller @ 120 MHz, based on the Microchip ATSAMD51N20 with 1 MB of program flash and 256 KB of RAM.
* **Industrial grade**: All industrial spec parts and Latch-Lock connectors for reliable operation in demanding applications.
* **Connectivitiy**:
  * USB interface for connecting to your development PC or Laptop computer for programming.
  * provides virtual COM port for CircuitPython console and UART, and mass storage filesystem interface to the 64 MB on-board QSPI flash for programs and data storage.
* **Control & interfacing**:
  * RS485, I2C, WIFI & Expansion: Latching RS485 interface connector on-board which is a UART-style differential bus with high noise immunity common in manufacturing and control automation.
  * Latching I2C interface connector on-board for sensors, controllers, displays, keypads, etc, on this commonly used bus; 12-pin AUX Expansion Socket on-board for expansion versatility and WIFI-enabled using the ubiquitous and inexpensive ESP-01S module.
  * additionally, VINA-D51 brings out 48 I/O capable of Digital I/O, UARTs, I2C, SPI, A/D, DAC, USB, and many other useful control and interfacing capabilities to the edge + 10 additional I/O on the AUX Socket.
* **Development & debug**:
  * CircuitPython and UF2 Bootloader pre-installed to get started developing right away with just a laptop or PC and a text editor.
  * With a standard ARM Cortex SWD debug header on-board, low level programming in C/C++ with source-level, single-step debugging utilizing a hardware programmer like the Segger J-Link is easy.
* **Data storage**:
  * 64 MB of on-board flash filesystem storage space for your programs and data presented as an external drive on your development workstation.
  * Soldered directly to the board, this flash storage will not suffer from corrosion or vibration in harsh environments like SD-Card type storage are prone.
* **Flexible voltage**:
  * Robust power section with wide voltage input range for flexible and reliable operation, and enough headroom to supply power to other devices up to about 3 A.
  * incorporates industrial grade Molex Latch-Lock connector that will not vibrate loose even in the most demanding applications.

## Technical details

* 32-bit ARM Cortex M4F MCU @ 120 MHz using the ATSAMD51N20A
* 1 MB Firmware Flash and 256 KB Static RAM
* Hardware Peripheral Control - A/D, DAC, Digital I/O, UARTs, I2C, SPI, I2S, PWM, Timers, Capacitive Touch, and more
* USB Port for programming and interfacing
* Virtual COM Port for connecting to the console using standard terminal emulator from a PC or Laptop - no additional hardware required for programming
* 16 MB Flash Filesystem for data and programs
* Mass Storage Device Interface to PC or Mac for downloading programs
* WIFI using the ESP-01S module socket
* WIFI using the BDMICRO ATW-01 WINC1500-based WiFi module
* Wide voltage input from 3.7 to 24 V with robust Latch-Lock connector that won't vibrate loose
* USB Port Power
* RS485 Port - with optional termination on-board, for interfacing with this common, differential, high noise immunity industrial control bus — mating part is the Molex —0430250408 3mm MicroFit 3.0 Series; optional power can be supplied to or from the RS485 bus through jumper selection
* I2C connector - 4-pins supplying SCL, SDA, GND, and optional 3.3 V to power external I2C devices like sensors and displays
* On-board I2C pull-ups - can be optionally disabled
* ARM Cortex SWD Debug Port - for low-level firmware flashing and source level single-step debugging with hardware programmer support such as the Segger J-Link
* Robust, Latch-Lock Power Connector - will not vibrate loose, suitable for harsh environments; mating part is the Molex 0430250208 MicroFit 3.0 series
* Jumper Selectable Power - either USB or external
* Jumper Enabled RS485 Bus termination
* Jumper Enabled I2C Bus pull-ups
* Jumper Enabled 3.3 V Power to or from the RS485 Bus
* Jumper Enabled 3.3 V Power to or from the I2C Bus
* Fused Power Inputs - both USB and External Power fused appropriately for their voltage input and current draw
* Power Indicator LED
* 3 Programmable Status LEDs - Red, Green, and Blue
* RX & TX LEDs - for use by CircuitPython to indicate transmission and reception of data over USB, or fully programmable under application control
* Small Size - 1.6" x 2.8" (41 mm x 71 mm)

## Misc

* [VINA-D51 Manual](https://cdn.shopify.com/s/files/1/0087/5718/2544/files/vina-d51.pdf?v=1641358819)
* [Eagle Part Library for VINA-D51](https://cdn.shopify.com/s/files/1/0087/5718/2544/files/vina-d51.lbr?v=1620249715)

## Purchase

* [BDMICRO](https://bdmicro.com/products/vina-d51)
