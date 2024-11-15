---
layout: download
board_id: "targett_module_clip_wrover"
title: "Targett ESP32-S2 Module Clip (WROVER) Download"
name: "Targett ESP32-S2 Module Clip (WROVER)"
manufacturer: "Targett"
board_url:
 - "https://www.targettpcb.co.uk/s2-mcb-1"
board_image: "targett_module_clip_wrover.jpg"
date_added: 2020-12-06
family: esp32s2
bootloader_id: targett_mcb_wrover
features:
  - Wi-Fi
---

This board will allow you to clip in an ESP32-S2 WROOM or WROVER module for programming, prototyping and testing. Slot the module into the pins where it will be held securely while you upload your code.

The Board has two USB micro sockets: The first is connected to a CP2104 USB to UART to upload of your firmware and receive serial messages. The second is directly connected to GPIO19 & 20 that are the onboard USB - & + pins.

The board can be powered from either of the USB sockets, the UART USB has a power switch and the S2 USB will directly power the board. These sockets are separated by diodes so neither can reverse power the other. The S2 USB has bridgeable solder pads so that it can be used to supply USB power if acting as OTG Host.

The CP2104 handles the USB to UART conversion as well as putting the module into "programming mode".

Where Espressif have enabled programming via the S2 USB and the module can be put in "programming mode" using the IO_0 and Reset buttons.

All GPIO pins are broken out to 2.54mm header pins. Caution should be taken as some pins are used by the WROVER module for PSRAM.

## Purchase

You can purchase the S2-MCB from [Tindie](https://www.tindie.com/products/targett/esp32-s2-module-protoprogrammer/)
