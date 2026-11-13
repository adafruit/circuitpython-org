---
layout: download
board_id: "elecrow_crowpanel_2_13_epaper"
title: "Elecrow CrowPanel ESP32S3 2.13 Epaper"
name: "Elecrow CrowPanel 2.13"
manufacturer: "Elecrow"
board_url:
 - "https://www.elecrow.com/crowpanel-esp32-2-13-e-paper-hmi-display-with-122-250-resolution-black-white-color-driven-by-spi-interface.html"
board_image: "elecrow_crowpanel_2_13_epaper.jpg"
date_added: 2026-11-12
family: esp32s3
features:
  - Bluetooth/BTLE
  - Battery Charging
  - Display
  - USB-C
  - Wi-Fi
---

The CrowPanel 2.13" is an ESP32-S3 board with a 250 x 122 black-and-white e-paper screen, 8 MB of flash and 8 MB of
PSRAM. It has a three-way rotary switch, MENU and EXIT buttons, a two-pin GPIO header (IO40, IO41), a UART0 header and
a battery socket.

It has no native USB: CircuitPython's console is on the CH340K USB-serial port, and files go over web workflow or the
serial REPL. `board.DISPLAY` is not set up at boot; the panel's pins and SPI bus are in `board` (`EPD_SPI`, `EPD_CS`,
`EPD_DC`, `EPD_RES`, `EPD_BUSY`).

## Specifications

- MCU: ESP32-S3, up to 240 MHz
- 8 MB flash, 8 MB PSRAM
- 2.13-inch e-paper display, 122 x 250 pixels, black and white, SPI
- Buttons: rotary switch, MENU, EXIT, RESET, BOOT
- Interfaces: UART0, battery (SH1.0 2-pin), GPIO header
- Power: USB Type-C or a lithium battery

## Documentation

* [Elecrow wiki](https://www.elecrow.com/wiki/CrowPanel_ESP32_E-Paper_HMI_2.13-inch_Display.html)

## Purchase

* [Elecrow](https://www.elecrow.com/crowpanel-esp32-2-13-e-paper-hmi-display-with-122-250-resolution-black-white-color-driven-by-spi-interface.html)
