---
layout: download
board_id: "aloriumtech_evo_m51"
title: "AloriumTech Evo M51 Download"
name: "AloriumTech Evo M51"
manufacturer: "Alorium Technology, LLC"
board_url:
 - "https://www.aloriumtech.com/evom51"
board_image: "aloriumtech_evo_m51.jpg"
date_added: 2020-05-21
family: atmel-samd
downloads_display: true
blinka: false
download_instructions: https://aloriumtech.com/evom51-quickstart/
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Breadboard-Friendly
---

The Evo M51 is an FPGA-enhanced Feather compatible compute module from Alorium Technology that features a 32-bit SAMD51 microcontroller along with an Intel MAX 10 FPGA.

Designed for use as an embeddable system-on-module, all of the standard Feather I/O are also routed to castellated vias along the edge of the board. There are 34 additional castellated digital I/O connected to the FPGA and accessible via the SAMD51.

Most digital I/O connections are routed through the FPGA to and from the primary and castellated I/O. This provides the opportunity for developers to immediately capture inputs or drive outputs from the FPGA without requiring direct interaction with the SAMD controller.

Evo M51 will support Alorium Technology-supplied pre-built FPGA images that target specific application use cases. In addition, designers will have the option to develop their own custom logic blocks and integrate them into the top-level MAX 10 FPGA design.

Evo was specifically designed to support running CircuitPython. It is also programmable with Arduino just like many other boards based upon the SAMD51.

## Technical details

- Atmel SAMD51 32-bit ARM Cortex-M4 Microcontroller
- Intel MAX 10 FPGA
- 512 KB FLASH and 192 KB RAM
- 2 MB External QSPI FLASH
- 6 Analog Inputs
- 2 Analog Outputs
- 55 Digital I/O
  - 21 Through-Hole/Castellated
  - 34 Additional Castellated-Only (3.3 V inputs/ouput)
- 1 NeoPixel (`D13`)
- STEMMA QT (QWIIC Compatible)
- Feather Footprint
- 0.9" x 2.2" (23 mm x 56 mm)

## Misc

* [Quickstart guide](https://aloriumtech.com/evom51-quickstart/)
* [Pinout](https://aloriumtech.com/documents/Evo_M51_PinMap.pdf)
* [Schematics](https://aloriumtech.com/documents/Evo_M51_Schematic.pdf)

In order to take full advantage of the additional I/O on Evo M51 using CircuitPython, we have created a custom library bundle that can be found on the Alorium Technology GitHub page:

- [Evo M51 CircuitPython Library Bundle](https://github.com/AloriumTechnology/AloriumTech_CircuitPython_EvoM51)
- Download the [.ZIP file](https://github.com/AloriumTechnology/AloriumTech_CircuitPython_EvoM51/archive/master.zip)

## Purchase

* [Alorium Technology](https://www.aloriumtech.com/evom51-buy/)
