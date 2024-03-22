---
layout: download
board_id: "lilygo_ttgo_t8_esp32_s2_wroom"
title: "TTGO T8 ESP32-S2-WROOM Download"
name: "TTGO T8 ESP32-S2-WROOM"
manufacturer: "LILYGO"
board_url:
 - "http://www.lilygo.cn/prod_view.aspx?TypeId=50063&Id=1320&FId=t3:50063:3"
board_image: "lilygo_ttgo_t8_esp32_s2_wroom.jpg"
bootloader_id: "lilygo_ttgo_t8_s2_wroom"
date_added: 2022-03-01
downloads_display: true
family: esp32s2
features:
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
---

The LILYGO TTGO T8 ESP32-S2 ESP32-S2-WROOM is a basic development board.

## Features & Specifications

 - ESP32-S2 240 MHz Tensilica processor
 - Wi-Fi 802.11 b/g/n 2.4 GHz
 - 4 MB FLASH
 - 320 kB RAM (no PSRAM)
 - reset and boot button
 - onboard 32.768 kHz crystal oscillator
 - USB-C connector

## Schematic

- [LILYGO Github repository](https://github.com/Xinyuan-LilyGO/ESP32_S2)

## Setup instructions

You need to install an UF2 Bootloader.

After flashing the Bootloader change the DIP switches (the ones closer to the
USB-C connector) to OTG mode, when reconnected you should see the drive and can
copy over the CircuitPython UF2 file.

```text
USB        OTG

On         On
o   o        o   o
  o   o    o   o
1 2 3 4    1 2 3 4
```

## Purchase

* [AlixExpress](https://www.aliexpress.com/item/4001080875553.html?spm=a2g0o.store_pc_groupList.8148356.17.4c0236fcsFJuWs)
