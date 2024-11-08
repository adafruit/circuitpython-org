---
layout: download
board_id: "adafruit_feather_esp32s2"
title: "Feather ESP32-S2 Download"
name: "Feather ESP32-S2"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5000"
board_image: "adafruit_feather_esp32s2.jpg"
date_added: 2021-04-06
family: esp32s2
bootloader_id: adafruit_feather_esp32s2
download_instructions: https://learn.adafruit.com/adafruit-esp32-s2-feather/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
---

What's Feather-shaped and has an ESP32-S2 WiFi module? What has a STEMMA QT connector for I2C devices? What has your favorite Espressif WiFi microcontroller and lots of Flash and RAM memory for your next IoT project? What will make your next IoT project flyyyyy?

That's right - it's the new **Adafruit Feather ESP32-S2**! With native USB and 4 MB flash + 2 MB of PSRAM, this board is perfect for use with CircuitPython or Arduino with low-cost WiFi. Native USB means it can act like a keyboard or a disk drive. WiFi means its awesome for IoT projects. And Feather means it works with the large community of Feather Wings for expandability.

The ESP32-S2 is a highly-integrated, low-power, 2.4 GHz Wi-Fi System-on-Chip (SoC) solution that now has **built-in native USB** as well as some other interesting new technologies like Time of Flight distance measurements. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

**Please note** the Feather ESP32-S2 has a single-core 240 MHz chip, so it won't be as fast as ESP32's with dual-core. Also, there is no Bluetooth support. However, we are super excited about the ESP32-S2's native USB which unlocks a lot of capabilities for advanced interfacing! This ESP32-S2 mini-module we are using on the Feather comes with 4 MB flash and 2 MB PSRAM so you can buffer massive JSON files for parsing!

## Technical details

- **ESP32-S2 240 MHz Tensilica processor** - the next generation of ESP32, now with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **Mini module** has FCC/CE certification and comes with 4 MB of Flash and 2 M of PSRAM - you can have huge data buffers
- **Power options** - USB-C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - LC709203 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **Serial debug output pin** (optional, for checking the hardware serial debug console)
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode
- **On/Charge/User** LEDs and status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode we can get down to 30 uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32-S2 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C power for the lowest quiescent current draw.
- Works with Arduino or CircuitPython

## Purchase

* [Adafruit](https://www.adafruit.com/product/5000)
