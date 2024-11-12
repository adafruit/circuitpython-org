---
layout: download
board_id: "adafruit_qtpy_esp32s3_4mbflash_2mbpsram"
title: "Adafruit QT Py ESP32-S3 4MB Flash/2MB PSRAM Download"
name: "Adafruit QT Py ESP32-S3 4MB Flash/2MB PSRAM"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5700"
board_image: "adafruit_qtpy_esp32s3_4mbflash_2mbpsram.jpg"
date_added: 2023-07-11
family: esp32s3
bootloader_id: adafruit_qtpy_esp32s3_n4r2
download_instructions: https://learn.adafruit.com/adafruit-qt-py-esp32-s3/circuitpython-2
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
  - Wi-Fi
  - Xiao / QTPy Form Factor
  - Castellated Pads
---

The ESP32-S3 has arrived in QT Py format - and what a great way to get started with this powerful new chip from Espressif! With dual 240 MHz cores, WiFi and BLE support, and native USB, this QT Py is great for powering your IoT projects. Now we even have this powerhouse of a board with built in 2 Megabytes of PSRAM for when you need to buffer large datasets in memory.

The ESP32-S3 is a highly-integrated, low-power, 2.4 GHz Wi-Fi System-on-Chip (SoC) solution that now has WiFi and BLE support, built-in native USB, as well as some other interesting new technologies like Time of Flight distance measurements. With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the Internet of Things (IoT), wearable electronics, and smart homes.

With native USB and 4 MB Flash + 2 MB PSRAM, this board will let you upgrade your existing ESP32 projects. Native USB means it can act like a keyboard or a disk drive, and no external USB-to-Serial converter required. WiFi and BLE mean it's awesome for IoT projects.

OLEDs! Inertial Measurement Units! Sensors a-plenty. All plug-and-play thanks to the innovative chainable design: SparkFun Qwiic-compatible STEMMA QT connectors for the I2C bus, so you don't even need to solder! Just plug in a compatible cable and attach it to your MCU of choice, and you’re ready to load up some software and measure some light. Seeed Grove I2C boards will also work with this adapter cable.

Pinout and shape are Seeed Xiao compatible, with castellated pads, so you can solder it flat to a PCB. In addition to the QT connector, we also added an RGB NeoPixel (with controllable power pin to allow for ultra-low-power usage), a reset button (great for restarting your program or entering the bootloader), and a button on GPIO 0 for entering the ROM bootloader or for user input

The ESP32-S3 has a dual-core 240 MHz chip, so it is comparable to ESP32's dual-core. However, there is no Bluetooth Classic support, only Bluetooth LE. This chip is a great step up from the earlier ESP32-S2! This ESP32-S3 chip we are using on the QT Py comes with 4 MB flash, 2 MB PSRAM, and 512KB of SRAM, so it's perfect for use with CircuitPython support even when massive buffers are needed. It's also great for use in ESP-IDF or with Arduino support.

## Technical details

* Same size, form factor, and pin-out as Seeed Xiao
* USB Type C connector - If you have only Micro B cables, this adapter will come in handy!
* ESP32-S3 Dual Core 240MHz Tensilica processor - the next generation of ESP32-Sx, with native USB, so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
* Comes with 4MB Flash, 512KB SRAM, 2MB PSRAM
* Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, MIDI, Keyboard/Mouse HID, and even a little disk drive for storing Python scripts.
* Can be used with Arduino IDE or CircuitPython
* Built-in RGB NeoPixel LED with power control to reduce quiescent power in deep sleep
* Battery input pads on underside with diode protection for external battery packs up to 6V input
* 13 GPIO pins:
	* 11 on breakout pads, 2 more on QT connector
	* 10 x 12-bit analog inputs (SPI high-speed pads do not have analog inputs)
	* PWM outputs on any pin
	* Two I2C ports, one on the breakout pads and another with STEMMA QT plug-n-play connector
	* Hardware UART
	* Hardware SPI on the high-speed SPI peripheral pins
	* Hardware I2S on any pins
	* 5 x Capacitive Touch with no additional components required
* 3.3V regulator with 600mA peak output
* Light sleep at 2~4mA, deep sleep at ~70uA
* Reset switch for starting your project code over, boot 0 button for entering bootloader mode
* Really really small

## Purchase

* [Adafruit](https://www.adafruit.com/product/5700)
