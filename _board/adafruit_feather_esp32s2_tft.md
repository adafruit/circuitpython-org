---
layout: download
board_id: "adafruit_feather_esp32s2_tft"
title: "Feather ESP32-S2 with TFT Download"
name: "Feather ESP32-S2 with TFT"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5300"
board_image: "adafruit_feather_esp32s2_tft.jpg"
date_added: 2021-04-06
family: esp32s2
bootloader_id: adafruit_feather_esp32s2_tft
download_instructions: https://learn.adafruit.com/adafruit-esp32-s2-tft-feather/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - Wi-Fi
  - USB-C
  - Display
  - Breadboard-Friendly
---

We've got a new machine here at Adafruit, it can uncover your deepest desires. Don't believe me? I'll turn it on right now to prove it to you! What, you want unlimited mozzarella sticks? OK well, that's not something we can provide. But we can provide your *second*-deepest desire: an **ESP32-S2 Feather board with a built in IPS TFT color display**. It's got all the ~~gooeyness of a mozzarella stick~~ features of a Feather main board, the comforting warmth of an ESP32-S2 WiFi microcontroller, and the crispness of a 240x135 pixel color TFT display. All that and it will even plug in nicely into a breadboard, [terminal block wing](https://www.adafruit.com/product/2926), or [Feather Doubler](https://www.adafruit.com/product/2890) or even just stack on top of another wing.

This feather comes with native USB and **4 MB flash + 2 MB of PSRAM**, so it is perfect for use with CircuitPython or Arduino with low-cost WiFi. Native USB means it can act like a keyboard or a disk drive. WiFi means its awesome for IoT projects. And Feather means it works with the large community of Feather Wings for expandability.

The ESP32-S2 is a highly-integrated, low-power, 2.4 GHz Wi-Fi System-on-Chip (SoC) solution that now has **built-in native USB** as well as some other interesting new technologies like Time of Flight distance measurements. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

**Please note** the Feather ESP32-S2 has a single-core 240 MHz chip, so it won't be as fast as ESP32's with dual-core. Also, there is no Bluetooth support. However, we are super excited about the ESP32-S2's native USB which unlocks a lot of capabilities for advanced interfacing! This ESP32-S2 mini-module we are using on the Feather comes with 4 MB flash and 2 MB PSRAM so you can buffer massive JSON files for parsing!

The color TFT is connected to the SPI pins, and uses additional pins for control that are not exposed to the breakout pads. [It's the same display as you see here, with 240x135 pixels and is IPS](https://www.adafruit.com/product/4383) so you get bright color at any angle. The backlight is also connected to a separate pin so you can PWM the backlight up and down as desired.

For low power usages, the Feather has a *second* AP2112 regulator. The regulator is controlled with a GPIO pin on the enable line and can shut off power to the Stemma QT port and TFT. There is also a separate power pin for the NeoPixel that can be used to disable it for even lower quiescent power. With everything off and in deep sleep mode, the TFT feather uses about 100uA of current.

## Technical details

- **ESP32-S2 240 MHz Tensilica processor** - the next generation of ESP32, now with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **Mini module** has FCC/CE certification and comes with 4 MB of Flash and 2 MB of PSRAM - you can have huge data buffers
- **[Color 1.14" IPS TFT with 240x135 pixels](https://www.adafruit.com/product/4383)** - bright and colorful display with ST7789 chipset that can be viewed at any angle angle.
- **Power options** - USB-C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** - LC709203 chip actively monitors your battery for voltage and state of charge / percentage reporting over I2C
- **Reset and DFU** (BOOT0) buttons to get into the ROM bootloader (which is a USB serial port so you don't need a separate cable!)
- **Serial debug output pin** (optional, for checking the hardware serial debug console)
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode
- **On/Charge/User** LEDs + status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode we can get down to 80~100 uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32-S2 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C/TFT power for the lowest quiescent current draw.
- Works with Arduino or CircuitPython

## Purchase

* [Adafruit](https://www.adafruit.com/product/5300)
