---
layout: download
board_id: "adafruit_qtpy_esp32s2"
title: "Adafruit QT Py ESP32-S2 (including uFL version) Download"
name: "Adafruit QT Py ESP32-S2 (including uFL version)"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5325"
 - "https://www.adafruit.com/product/5348"
board_image: "adafruit_qtpy_esp32s2.jpg"
date_added: 2021-11-30
family: esp32s2
bootloader_id: adafruit_qtpy_esp32s2
download_instructions: https://learn.adafruit.com/adafruit-qt-py-esp32-s2/circuitpython
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
  - Wi-Fi
  - Xiao / QTPy Form Factor
  - Castellated Pads
---

What has your favorite Espressif WiFi microcontroller, comes with [our favorite connector - the STEMMA QT](http://adafruit.com/stemma), a chainable I2C port, and has lots of Flash and RAM memory for your next IoT project? What will make your next IoT project flyyyyy? What a cutie pie! Or is it... a **QT Py**? This diminutive dev board comes with one of our new favorite lil chips, the **ESP32-S2**!

The ESP32-S2 is a highly-integrated, low-power, 2.4 GHz Wi-Fi System-on-Chip (SoC) solution that now has **built-in native USB** as well as some other interesting new technologies like Time of Flight distance measurements. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

**Please note** the QT Py ESP32-S2 has a single-core 240 MHz chip, so it won't be as fast as ESP32's with dual-core. Also, there is no Bluetooth support. However, we are super excited about the ESP32-S2's native USB which unlocks a lot of capabilities for advanced interfacing! This ESP32-S2 mini-module we are using on the QT Py comes with 4 MB flash and 2 MB PSRAM so you can buffer massive JSON files for parsing!

[OLEDs](https://www.adafruit.com/?q=qt+oled&main_page=category&cPath=1005&sort=BestMatch)! [Inertial Measurement Units](https://www.adafruit.com/?q=qt+imu&main_page=category&cPath=1005&sort=BestMatch)! [Sensors a-plenty](https://www.adafruit.com/?q=qt+sensor&main_page=category&cPath=1005&sort=BestMatch). All plug-and-play thanks to the innovative chainable design: [SparkFun Qwiic](https://www.sparkfun.com/qwiic)-compatible [STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt) connectors for the I2C bus so you don't even need to solder! Just plug in a compatible cable and attach it to your MCU of choice, and you’re ready to load up some software and measure some light. [Seeed Grove I2C boards](https://www.adafruit.com/product/4528) will also work with this adapter cable.

Pinout and shape are [Seeed Xiao](https://wiki.seeedstudio.com/Seeeduino-XIAO/) compatible, with castellated pads so you can solder it flat to a PCB. In addition to the QT connector, we also added an **RGB NeoPixel** (with controllable power pin to allow for ultra-low-power usage), **a reset button** (great for restarting your program or entering the bootloader) and a button on GPIO 0 for entering the ROM bootloader or for user input.

Runs Arduino like a dream, and CircuitPython projects are fantastically fun.

## Technical details

- Same size, form-factor, and pin-out as Seeed Xiao
- **USB-C connector** - [If you have only Micro B cables, this adapter will come in handy](https://www.adafruit.com/product/4299)!
- **ESP32-S2 240MHz Tensilica processor** - the next generation of ESP32, now with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
- **4 MB Flash & 2 MB PSRAM**
- Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, MIDI, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
- Can be used with **Arduino IDE** or **CircuitPython**
- **Built-in RGB NeoPixel LED** with power control to reduce quiescent power in deep sleep
- Battery input pads on underside with diode protection for external battery packs up to 6V input
- 13 GPIO pins:
  - 11 on breakout pads, 2 more on QT connector
  - 10 12-bit analog inputs (SPI high speed pads do not have analog inputs)
  - 8-bit analog output DAC
  - PWM outputs on any pin
  - 2 I2C ports, one on the breakout pads, and another with STEMMA QT plug-n-play connector
  - Hardware UART
  - Hardware SPI on the high speed SPI peripheral pins
  - Hardware I2S on any pins
  - 5 Capacitive Touch with no additional components required
- 3.3 V regulator with [**600 mA peak output**](https://www.diodes.com/assets/Datasheets/AP2112.pdf)
- Deep sleep at 100 uA
- **Reset switch** for starting your project code over, boot 0 button for entering bootloader mode
- **Really really small**

## Purchase

* [Adafruit](https://www.adafruit.com/product/5325) built-in Wifi antenna
* [Adafruit](https://www.adafruit.com/product/5348) uFL connector for external antenna
