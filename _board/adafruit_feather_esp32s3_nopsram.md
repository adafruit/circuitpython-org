---
layout: download
board_id: "adafruit_feather_esp32s3_nopsram"
title: "Feather ESP32-S3 No PSRAM Download"
name: "Feather ESP32-S3 No PSRAM"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5323"
board_image: "adafruit_feather_esp32s3_nopsram.jpg"
date_added: 2022-04-01
family: esp32s3
bootloader_id: adafruit_feather_esp32s3_nopsram
download_instructions: https://learn.adafruit.com/adafruit-esp32-s3-feather/circuitpython
downloads_display: true
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly

---

The ESP32-S3 has arrived in Feather format - and what a great way to get started with this powerful new chip from Espressif! With dual 240 MHz cores, WiFi and BLE support, and native USB, this Feather is great for powering your IoT projects.

That's right - it's the new **Adafruit ESP32-\*S3\* Feather**! With native USB and 8 MB flash, this board will let you upgrade your existing ESP32 projects. Native USB means it can act like a keyboard or a disk drive, and no external USB-to-Serial converter required. WiFi and BLE mean it's awesome for IoT projects. And Feather means it works with the large community of Feather Wings for expandability.

The ESP32-S3 is a highly-integrated, low-power, 2.4 GHz Wi-Fi/BLE System-on-Chip (SoC) solution that has built-in native USB as well as some other interesting new technologies like Time of Flight distance measurements and AI acceleration. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

The Feather ESP32-S3 has a dual-core 240 MHz chip, so it is comparable to ESP32's dual-core. However, there is no Bluetooth **Classic** support, only Bluetooth LE. This chip is a great step up from the earlier ESP32-S2! This ESP32-S3 mini-module we are using on the Feather comes with 8 MB flash and no PSRAM, but it does have 512KB of SRAM so its fine for use with CircuitPython support as long as massive buffers are not needed. It's also great for use in ESP-IDF or with Arduino support.

**Features:**

- **ESP32-S3 Dual Core 240MHz Tensilica processor** - the next generation of ESP32-Sx, with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **Mini module** has FCC/CE certification and comes with 8 MByte of Flash, no PSRAM
- **Power options** - USB type C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - LC709203 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **Serial debug output pin** (optional, for checking the hardware serial debug console)
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode.
- **On/Charge/User** LEDs + status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode we can get down to ~100uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32-S3 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C power for the lowest quiescent current draw.
- **Works with ESP-IDF, Arduino** (coming soon) **or CircuitPython** (not recommended since there is no PSRAM, but for some simple IoT projects without large buffers it will work)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5323)
