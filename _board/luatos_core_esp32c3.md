---
layout: download
board_id: "luatos_core_esp32c3"
title: "Luatos Core ESP32C3 Download"
name: "Luatos Core ESP32C3"
manufacturer: "Luatos"
board_url:
 - "https://wiki.luatos.com/chips/esp32c3/index.html"
board_image: "luatos_core_esp32c3.jpg"
date_added: 2022-12-20
family: esp32c3
bootloader_id: luatos_core_esp32c3
features:
  - Wi-Fi
  - USB-C
  - Bluetooth/BTLE
  - Breadboard-Friendly
  - Castellated Pads

---

A low-cost WiFi/BLE board based on ESP32-C3.

## Features

- Based on the ESP32-C3 WIFI & Bluetooth LE RISC-V Single-Core CPU
- Type-C USB
- Castellated pads
- 4MB Flash
- Clock speed: 160 Mhz
- 15x Digital IO
- ADC(5 channel, 12-bit), I2C, SPI, UARTx2
- Size: 21mm x 51mm
- Default firmware: LuatOS
- 2 red status LEDs

## Note

There are 2 versions of this board, differing in the inclusion of a CH343 UART to USB component. This board definition targets the
version without the CH343 which connects the built-in USB-CDC/JTAG to the USB-C connector.

Onboard LDO can be disabled by grounding the PWB pin (15).

GPIO11 can only be used by setting the EFUSE_VDD_SPI_AS_GPIO efuse and building a custom Circuitpython image.

## Learn More

* [Manufacturer Specifications](https://wiki.luatos.com/chips/esp32c3/board.html)
* [ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
* [Schematic](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220609213416069_CORE-ESP32-A12.pdf)
* [Dimension](https://cdn.openluat-luatcommunity.openluat.com/attachment/CORE-ESP32-C3%E5%8F%82%E8%80%83%E5%B0%BA%E5%AF%B8_V1.2.pdf)
