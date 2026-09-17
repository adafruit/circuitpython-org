---
layout: download
board_id: "circuitart_zero_s3"
title: "CircuitArt ESP32S3 Zero Download"
name: "CircuitArt ESP32S3 Zero"
manufacturer: "CircuitArt"
board_url:
 - "https://github.com/CircuitART/ESP32S3zero"
board_image: "CircuitArt_ESP32S3_Zero.jpg"
date_added: 2024-09-09
family: esp32s3
bootloader_id: circuitart_zero_s3
downloads_display: true
features:
  - Wi-Fi
  - Battery Charging
  - USB-C
  - Display
  - Camera
---

A new ESP32S3 Dev board in a RaspberryPI zero footprint, The board has an additional tiny SPI/I2C connector for a 1.3" IPS display + AHT20 sensor.

That's not all, This board comes with native USB, Debug USB, and **16 MB Flash + 8 MB of PSRAM**, so it is perfect for use with CircuitPython or Arduino with low-cost WiFi. Native USB means it can act like a keyboard or a disk drive. WiFi and Camera means it's awesome for IoT projects. And the PI ZERO footprint makes the expandability super easy.

**Features:**

- **ESP32-S3 Dual Core 240MHz Tensilica processor** - the next generation of ESP32-Sx, with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **huge data buffers** the board comes with 16 MByte of Flash and 8 MByte of PSRAM
- **Color 1.3" IPS TFT** - bright and colorful display with ST7789 chipset that can be viewed at any angle angle.
- **Power options** - USB type C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - LC709203 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **USB-c debug port** the board has CP2102 serial chip (optional, for checking the hardware serial debug console)
- **Micro I2C** connector for I2C devices, with switchable power, so you can go into low power mode.
- **Charge & User** LEDs + status
- **NeoPixel** 4 tiny neopixel led next to the camera so they  can act as cam light or flash.
- **Low Power friendly**! In deep sleep mode, we can get down to 80~100uA of current draw from the battery
- **Works with Arduino or CircuitPython**

## Learn More

* [GitHub](https://github.com/CircuitART/ESP32S3zero)
