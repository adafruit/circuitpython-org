---
layout: download
board_id: "adafruit_feather_esp32s3_tft"
title: "Feather ESP32-S3 TFT Download"
name: "Feather ESP32-S3 TFT PSRAM"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5483"
board_image: "adafruit_feather_esp32s3_tft.jpg"
date_added: 2022-06-09
family: esp32s3
bootloader_id: adafruit_feather_esp32s3_tft
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-esp32-s3-tft-feather/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Display
  - Breadboard-Friendly
---

We've got a new machine here at Adafruit, it can uncover your deepest desires. Don't believe me? I'll turn it on right now to prove it to you! What, you want your very own soft serve ice cream machine? OK well, that's not something we can provide. But we can provide your *second*-deepest desire: an **ESP32-S*3* Feather board with a built in IPS TFT color display**. It's got all the delicious creamy goodness features of a Feather main board, the comforting warmth of an ESP32-S3 WiFi+BLE microcontroller, and the crispness of a 240x135 pixel color TFT display. All that and it will even plug in nicely into a breadboard, [terminal block wing](https://www.adafruit.com/product/2926), or [Feather Doubler](https://www.adafruit.com/product/2890) or even just stack on top of another wing.

This Feather comes with native USB and **4 MB Flash + 2 MB of PSRAM**, so it is perfect for use with CircuitPython or Arduino with low-cost WiFi. Native USB means it can act like a keyboard or a disk drive. WiFi means it's awesome for IoT projects. And Feather means it works with the large community of Feather Wings for expandability.

The ESP32-S3 is a highly-integrated, low-power, 2.4 GHz Wi-Fi/BLE System-on-Chip (SoC) solution that has built-in native USB as well as some other interesting new technologies like Time of Flight distance measurements and AI acceleration. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

The Feather ESP32-S3 has a dual-core 240 MHz chip, so it is comparable to ESP32's dual-core. However, there is no Bluetooth **Classic** support, only Bluetooth LE. This chip is a great step up from the earlier ESP32-S2! This ESP32-S3 mini-module we are using on the Feather comes with 4 MB flash and 2 MB PSRAM, as well as lots of 512KB of SRAM so it's perfect for use with CircuitPython support or any time massive buffers are needed: for fast memory access use SRAM, for slower-but-roomier access use PSRAM. It's also great for use in ESP-IDF or with Arduino support.

The color TFT is connected to the SPI pins and uses additional pins for control that are not exposed to the breakout pads. [It's the same display as you see here, with 240x135 pixels and is IPS](https://www.adafruit.com/product/4383) so you get bright color at any angle. The backlight is also connected to a separate pin so you can PWM the backlight up and down as desired.

For low power usages, the Feather has a *second* low-dropout 3.3V regulator. The regulator is controlled with a GPIO pin on the enable line and can shut off power to the Stemma QT port and TFT. There is also a separate power pin for the NeoPixel that can be used to disable it for even lower quiescent power. With everything off and in deep sleep mode, the TFT feather uses about 100uA of current.

**Features:**

- **ESP32-S3 Dual Core 240MHz Tensilica processor** - the next generation of ESP32-Sx, with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **Mini module** has FCC/CE certification and comes with 4 MByte of Flash and 2 MByte of PSRAM - you can have huge data buffers
- **[Color 1.14" IPS TFT with 240x135 pixels](https://www.adafruit.com/product/4383)** - bright and colorful display with ST7789 chipset that can be viewed at any angle angle.
- **Power options** - USB type C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - LC709203 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **Serial debug output pin** (optional, for checking the hardware serial debug console)
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode.
- **On/Charge/User** LEDs + status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode, we can get down to 80~100uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32-S2 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C/TFT power for the lowest quiescent current draw.
- **Works with Arduino or CircuitPython**

## Purchase

* [Adafruit](https://www.adafruit.com/product/5483)
