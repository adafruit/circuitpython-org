---
layout: download
board_id: "adafruit_feather_esp32s2_reverse_tft"
title: "ESP32-S2 Reverse TFT Feather Download"
name: "ESP32-S2 Reverse TFT Feather"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5345"
board_image: "adafruit_feather_esp32s2_reverse_tft.jpg"
date_added: 2023-01-31
family: esp32s2
bootloader_id: adafruit_feather_esp32s2_reverse_tft
download_instructions: https://learn.adafruit.com/esp32-s2-reverse-tft-feather/circuitpython
tags:
  - Feather ESP32-S2 Reverse TFT
  - Reverse Feather TFT
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Display
---

Like Missy Elliot, we like to ["put our [Feather\] down, flip it and reverse it"](https://www.youtube.com/watch?v=cjIvu7e6Wq8) and that's exactly what we've done with this new development board. It's basically our **[ESP32-S2 TFT Feather](https://www.adafruit.com/product/5300)** but with the 240x135 color TFT display on the back-side not the front-side. That makes it great for panel-mounted projects, particularly since we've also got some space for 3 buttons to go along. It's like an all-in-one display interface dev board, powered by the fantastic ESP32-S2 WIFI module.

This feather comes with native USB and **4 MB flash + 2 MB of PSRAM**, so it is perfect for use with CircuitPython or Arduino with low-cost WiFi. Native USB means it can act like a keyboard or a disk drive. WiFi means it's awesome for IoT projects. And Feather means it works with the large community of Feather Wings for expandability.

The ESP32-S2 is a highly-integrated, low-power, 2.4 GHz Wi-Fi System-on-Chip (SoC) solution that now has **built-in native USB** as well as some other interesting new technologies like Time of Flight distance measurements. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

**Please note** the Feather ESP32-S2 has a single-core 240 MHz chip, so it won't be as fast as ESP32's with dual-core. Also, there is no Bluetooth support. However, we are super excited about the ESP32-S2's native USB which unlocks a lot of capabilities for advanced interfacing! This ESP32-S2 mini-module we are using on the Feather comes with 4 MB flash and 2 MB PSRAM so you can buffer massive JSON files for parsing!

The color TFT is connected to the SPI pins, and uses additional pins for control that are not exposed to the breakout pads. [It's the same display as you see here, with 240x135 pixels and is IPS](https://www.adafruit.com/product/4383) so you get bright color at any angle. The backlight is also connected to a separate pin so you can PWM the backlight up and down as desired.

For low power usage, the Feather has a *second* RT9080 regulator. The regulator is controlled with a GPIO pin on the enable line and can shut off power to the Stemma QT port and TFT. There is also a separate power pin for the NeoPixel that can be used to disable it for even lower quiescent power. With everything off and in deep sleep mode, the TFT feather uses about 40uA of current.

**Features:**

- **ESP32-S2 240MHz Tensilica processor** - the next generation of ESP32, now with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **Mini module** has FCC/CE certification and comes with 4 MByte of Flash and 2 MByte of PSRAM - you can have huge data buffers
- **[Color 1.14" IPS TFT with 240x135 pixels](https://www.adafruit.com/product/4383)** - bright and colorful display with ST7789 chipset that can be viewed at any angle.
- **Three User Tactile buttons** - D0, D1, and D2. D0/BOOT0 is also used for entering ROM bootloader mode if necessary.
- **Power options** - USB type C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - MAX17048 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **Serial debug output pin** (optional, for checking the hardware serial debug console)
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode.
- **On/Charge/User** LEDs + status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode, we can get down to 40~50uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32-S2 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C/TFT power for the lowest quiescent current draw.
- **Works with Arduino or CircuitPython**

## Purchase

* [Adafruit](https://www.adafruit.com/product/5345)
