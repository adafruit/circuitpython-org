---
layout: download
board_id: "muselab_nanoesp32_s2_wroom"
title: "NanoESP32 S2 w/WROOM Download"
name: "NanoESP32 S2 w/WROOM"
manufacturer: "Muselab"
board_url:
 - "https://www.muselab-tech.com/nanoesp32-s2kai-fa-ban/"
board_image: "muselab_nanoesp32_s2.jpg"
date_added: 2020-09-16
family: esp32s2
bootloader_id: muselab_nanoesp32-s2_wroom
features:
  - USB-C
  - Wi-Fi
  - Breadboard-Friendly
---

This is the nanoESP32-S2 board with a WROOM ESP32-S2 module.

## Technical details

* Microcontroller: Xtensa single-core 32-bit LX7
* Clock Frequency: 160/240 MHz
* Co-processor: ULP (RISC-V)
* SRAM: 320 KB
* ROM: 128 KB
* RTC Memory: 16 KB
* External SPIRAM: Up to 128 MB
* External Flash: Up to 1 GB
* Wi-Fi (802.11 b/g/n): HT20
* ESP-MESH: Yes
* GPIO (total): 43
* Touch sensors: 14
* SPI: 4 (OSPI)
* I2C: 2
* I2S: 1
* UART: 2
* ADC/DAC: 20 (12-bit)/2 (8-bit)
* USB OTG: Yes
* LCD/Camera interface: Yes/Yes
* Temperature/hall sensor: Yes/No
* Low Power Consumption: Automatic RF power management 5 uA in idle mode, 24 uA at 1% duty cycle

## Setup

This image can be flashed with the [TinyUF2 bootloader](https://github.com/adafruit/tinyuf2/releases) or with `esptool` using this command:

```sh
esptool.py -p (COMPORT) -b 460800 write_flash --flash_mode dio \
  --flash_size detect --flash_freq 40m 0x00000 \
  adafruit-circuitpython-muselab_nanoesp32_s2_wroom-ll_LL-X.Y.Z.bin
```

**NOTE:** This board has 2 USB-C connector, one for Serial (ch340) and one for Native USB (esp32).

## Learn More

* [User Guide](https://github.com/wuxx/nanoESP32-S2)
