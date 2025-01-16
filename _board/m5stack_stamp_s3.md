---
layout: download
board_id: "m5stack_stamp_s3"
title: "M5Stamp S3 Download"
name: "M5Stamp S3"
manufacturer: "M5Stack"
board_url:
 - "https://shop.m5stack.com/products/m5stamp-esp32s3-module"
 - "https://docs.m5stack.com/en/core/StampS3"
board_image: "m5stack_stamp_s3.jpg"
date_added: 2025-01-11
downloads_display: true
blinka: false
family: esp32s3
bootloader_id: adafruit_feather_esp32s3_nopsram
features:
  - Bluetooth/BTLE
  - USB-C
  - Wi-Fi
---

STAMPS3 is a highly integrated embedded controller designed for IoT applications. It utilizes the Espressif ESP32-S3FN8 main control chip and features 8MB of SPI flash memory. Powered by a high-performance Xtensa 32-bit LX7 dual-core processor, STAMPS3 delivers impressive processing power with a main frequency of up to 240MHz. This module is specifically designed to meet the demands of IoT projects that require embedded main control modules.

STAMPS3 comes equipped with a built-in highly integrated 5V to 3.3V circuit, ensuring stable power supply for reliable operation. It features an RGB status indicator and a programmable button for enhanced user control and visual feedback. The module conveniently leads out 23 GPIOs on the ESP32-S3, allowing for extensive expansion capabilities. The GPIOs are accessible through 1.27mm/2.54mm spacing leads, supporting various usage methods such as SMT, DIP row, and jump wire connections. STAMPS3 offers a compact form factor, delivering strong performance, rich expansion IO, and low power consumption.

USB-C connector and RGB Status LED are independent from all broken-out GPIO. GPIO46 is drop-down by default.

### Mounting Considerations
* 2.54mm DIP mounting breaks out 10 GPIO plus EN, 5V, 3V3, GND, GND
* 1.27mm DIP mounting breaks out 23 GPIO plus EN, 5V, 3V3, GND, GND
* Optional 8 pin 0.5mm pitch FPC header breaks out 6 additional GPIO plus 3V3, GND
* Optional 12 pin 0.5mm pitch FPC header breaks out 9 additional GPIO plus 5V, 3v3, GND

### Optional LCD
The M5Stamp S3 is available as a "Cardputer Accessory Kit", which includes a pre-soldered 8 pin FPC header and a 1.14" 240x135px LCD screen. If you wish to make use of this functionality, please use the adafruit_st7789 library.

## Documentation

* [M5Stamp S3](https://docs.m5stack.com/en/core/StampS3)

## Purchase

* [M5Stack - StampS3 Module](https://shop.m5stack.com/products/m5stamp-esp32s3-module)
* [M5Stack - StampS3 with 1.27 Header Pin](https://shop.m5stack.com/products/m5stamps3-with-1-27-header-pin)
* [M5Stack - StampS3 with 2.54 Header Pin](https://shop.m5stack.com/products/m5stamps3-with-2-54-header-pin)
* [M5Stack - StampS3 with Display](https://shop.m5stack.com/products/cardputer-accessory-kit)
