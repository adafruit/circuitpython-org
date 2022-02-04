---
layout: download
board_id: "muselab_nanoesp32_s2_wrover"
title: "NanoESP32 S2 w/WROVER Download"
name: "NanoESP32 S2 w/WROVER"
manufacturer: "Muselab"
board_url: "https://www.muselab-tech.com/nanoesp32-s2kai-fa-ban/"
board_image: "muselab_nanoesp32_s2.jpg"
date_added: 2020-09-16
family: esp32s2
bootloader_id: muselab_nanoesp32-s2_wrover

features:
  - USB-C
  - Wi-Fi
  - Breadboard-Friendly
---

This is the nanoESP32-S2 board with a WROVER ESP32-S2 module.

This image can be flashed with the [TinyUF2 bootloader](https://github.com/adafruit/tinyuf2/releases) or with esptool using this command:

esptool.py -p (COMPORT) -b 460800 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x00000 adafruit-circuitpython-muselab_nanoesp32_s2_wrover-ll_LL-X.Y.Z.bin

**NOTE:** This board has 2 USB-C connector, one for Serial (ch340) and one for Native USB (esp32).

## Learn More
* [User Guide](https://github.com/wuxx/nanoESP32-S2)
