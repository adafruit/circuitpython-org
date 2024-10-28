---
layout: download
board_id: "qtpy_m0_haxpress"
title: "QT Py Haxpress Download"
name: "QT Py Haxpress"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4600"
board_image: "qtpy_m0_haxpress.jpg"
date_added: 2020-09-28
family: atmel-samd
bootloader_id: QTPy_m0
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
  - Xiao / QTPy Form Factor
  - Castellated Pads
---

This is the [QT Py board](https://www.adafruit.com/product/4600) with [the SOIC-8 2MB Flash chip](https://www.adafruit.com/product/4763) soldered on. Both are in the [Adafruit shop](https://adafruit.com).

What a cutie pie! Or is it... a QT Py? This diminutive dev board comes with our favorite lil chip, the SAMD21 (as made famous in our GEMMA M0 and Trinket M0 boards).

This time it comes with [our favorite connector - the STEMMA QT](http://adafruit.com/stemma), a chainable I2C port that can be used with [any of our STEMMA QT sensors and accessories](https://www.adafruit.com/category/620).

[OLEDs](https://www.adafruit.com/?q=qt+oled&main_page=category&cPath=1005&sort=BestMatch)! [Inertial Measurment Units](https://www.adafruit.com/?q=qt+imu&main_page=category&cPath=1005&sort=BestMatch)! [Sensors a-plenty](https://www.adafruit.com/?q=qt+sensor&main_page=category&cPath=1005&sort=BestMatch). All plug-and-play thanks to the innovative chainable design: [SparkFun Qwiic](https://www.sparkfun.com/qwiic)-compatible STEMMA QT connectors for the I2C bus so you don't even need to solder! Just plug in a compatible cable and attach it to your MCU of choice, and you’re ready to load up some software and measure some light.

Use any [SparkFun Qwiic](http://www.sparkfun.com/qwiic) boards! [Seeed Grove I2C boards](https://www.adafruit.com/product/4528) will also work with this adapter cable.

Pinout and shape is [Seeed Xiao](https://wiki.seeedstudio.com/Seeeduino-XIAO/) compatible, with castellated pads so you can solder it flat to a PCB. In addition to the QT connector, we also added an **RGB NeoPixel** (with controllable power pin to allow for ultra-low-power usage), **and a reset button** (great for restarting your program, or entering the bootloader).

Runs Arduino like a dream, and can be used for basic CircuitPython projects. For more advanced usage like datalogging or file storage, solder an SOIC SPI flash chip onto the bottom pads,

 * Same size (20 mm x 17.5 mm), form-factor, and pin-out as Seeed Xiao
 * **ATSAMD21E18** 32-bit Cortex M0+ - 48 MHz 32 bit processor with 256 KB Flash and 32 KB RAM
 * Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, MIDI, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
 * Can be used with Arduino IDE or CircuitPython
 * Built in RGB NeoPixel LED
 * **11 GPIO pins**:
   * True analog output on one I/O pin - can be used to play 10-bit quality audio clips in Arduino (CircuitPython does not have storage for audio clips)
   * 9 x 12-bit analog inputs (SDA/SCL do not have analog inputs)
   * 1 x Optional AREF on `A1`
   * 9 x PWM outputs (`A0` is analog out, `A1` is not PWM capable)
   * Hardware I2C port with STEMMA QT plug-n-play connector
   * Hardware UART, Hardware SPI, Hardware I2S
   * 6 x Capacitive Touch with no additional components required
 * 3.3 V regulator with [600 mA peak output](https://www.diodes.com/assets/Datasheets/AP2112.pdf)
 * **Reset switch** for starting your project code over or entering bootloader mode
 * USB-C connector

## Purchase

* [Adafruit](https://www.adafruit.com/product/4600)
* [Adafruit - Flash Chip](https://www.adafruit.com/product/4763)
