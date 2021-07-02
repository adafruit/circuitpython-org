---
layout: download
board_id: "aloriumtech_evo_m51"
title: "AloriumTech Evo M51 Download"
name: "AloriumTech Evo M51"
manufacturer: "Alorium Technology, LLC"
board_url: "https://www.aloriumtech.com/evom51"
board_image: "aloriumtech_evo_m51.jpg"
date_added: 2020-5-21
downloads_display: true
blinka: false
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC

---

The Evo M51 is an FPGA-enhanced Feather compatible compute module from Alorium Technology that features a 32-bit SAMD51 microcontroller along with an Intel MAX 10 FPGA.  

Designed for use as an embeddable system-on-module, all of the standard Feather I/O are also routed to castellated vias along the edge of the board. There are 34 additional castellated digital I/O connected to the FPGA and accessible via the SAMD51.

Most digital I/O connections are routed through the FPGA to and from the primary and castellated I/O.  This provides the opportunity for developers to immediately capture inputs or drive outputs from the FPGA without requiring direct interaction with the SAMD controller.  

Evo M51 will support Alorium Technology-supplied pre-built FPGA images that target specific application use cases.  In addition, designers will have the option to develop their own custom logic blocks and integrate them into the top-level MAX 10 FPGA design.

Evo was specifically designed to support running CircuitPython.  It is also programmable with Arduino just like many other boards based upon the SAMD51.  So, writing and uploading firmware to the microcontroller is easy and familiar.

__Features__
- Atmel SAMD51 32-bit ARM Cortex-M4 Microcontroller
- Intel MAX 10 FPGA
- 512KB FLASH / 192KB RAM
- 2MB External QSPI FLASH
- 6 Analog Inputs
- 2 Analog Outputs
- 55 Digital I/O
  - 21 Through-Hole/Castellated
  - 34 Additional Castellated-Only
- STEMMA QT (QWIIC Compatible)
- Feather Footprint
- 0.9 in. x 2.2 in.

__Evo M51 CircuitPython Library Bundle__  
In order to take full advantage of the additional I/O on Evo M51 using CircuitPython, we have created a custom library bundle that can be found on the Alorium Technology GitHub page:

- [AloriumTech_CircuitPython_EvoM51](https://github.com/AloriumTechnology/AloriumTech_CircuitPython_EvoM51)
- Download the .ZIP file here: [Download .ZIP](https://github.com/AloriumTechnology/AloriumTech_CircuitPython_EvoM51/archive/master.zip)

## Purchase
Add any links to purchase the board
* [Alorium Technology](https://www.aloriumtech.com/evom51-buy/)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/main/_board/{{ page.board_id }}.md).
