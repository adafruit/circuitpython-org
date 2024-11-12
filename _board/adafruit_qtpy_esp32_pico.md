---
layout: download
board_id: "adafruit_qtpy_esp32_pico"
title: "Adafruit QT Py ESP32 Pico Download"
name: "Adafruit QT Py ESP32 Pico"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5395"
board_image: "adafruit_qtpy_esp32_pico.jpg"
date_added: 2022-08-19
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/circuitpython-with-esp32-quick-start/installing-circuitpython
features:
  - Xiao / QTPy Form Factor
  - Bluetooth/BTLE
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
  - STEMMA QT/QWIIC
  - Castellated Pads
---

This dev board is like when you're watching a super-hero movie and the protagonist shows up in a totally amazing costume in the third act and you're like 'OMG! That's the hero and they're here to kick some serious butt!" but in this case its a microcontroller.

This QT Py board is a thumbnail-sized PCB that features the **ESP32 Pico V3 02**, an all-in-one chip that has an **ESP32 chip with dual-core 240MHz Tensilica processor**, **WiFi** and **Bluetooth classic + BLE**, adds a bunch of required passives and oscillator, **8 MB of Flash memory** and **2 MB of PSRAM**. We add a USB to serial converter chip, some more passives, an antenna, USB C, buttons, NeoPixel and QT connector to outfit this super-hero chip for any task you want to throw it at.

At the core of ESP32-PICO-V3-02 is the ESP32 (ECO V3) chip, which is a single 2.4 GHz Wi-Fi and Bluetooth combo chip designed with TSMC’s 40 nm low-power technology. ESP32-PICO-V3-02 integrates all peripheral components seamlessly, including a crystal oscillator, flash, PSRAM, filter capacitors, and RF matching links in one single package. This makes it perfect for stuffing into such a small space as the QT Py.

**Please note** the QT Py ESP32 Pico does not have native USB support - instead there's a USB to serial converter chip. This means it *cannot* act like a USB keyboard or mouse - but it does have BLE and BT classic so you could wireless.

[OLEDs](https://www.adafruit.com/?q=qt+oled&main_page=category&cPath=1005&sort=BestMatch)! [Inertial Measurement Units](https://www.adafruit.com/?q=qt+imu&main_page=category&cPath=1005&sort=BestMatch)! [Sensors a-plenty](https://www.adafruit.com/?q=qt+sensor&main_page=category&cPath=1005&sort=BestMatch). All plug-and-play thanks to the innovative chainable design: [SparkFun Qwiic](https://www.sparkfun.com/qwiic)-compatible [STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt) connectors for the I2C bus so you don't even need to solder! Just plug in a compatible cable and attach it to your MCU of choice, and you’re ready to load up some software and measure some light. [Seeed Grove I2C boards](https://www.adafruit.com/product/4528) will also work with this adapter cable.

Pinout and shape are [Seeed Xiao](https://wiki.seeedstudio.com/Seeeduino-XIAO/) compatible, with castellated pads. In addition to the QT connector, we also added an **RGB NeoPixel** (with controllable power pin to allow for ultra-low-power usage), **a reset button** (great for restarting your program or entering the bootloader), and a button on GPIO 0 for entering the ROM bootloader or for user input

Runs Arduino like a dream, or use the ESP IDF for more control over your projects.

- Same size, form-factor, and pin-out as Seeed Xiao
- **USB Type C connector** - [If you have only Micro B cables, this adapter will come in handy](https://www.adafruit.com/product/4299)!
- **ESP32 V2 03 Dual Core 240MHz Xtensa processor** - the ESP32 you know and love, with the latest engineering fixes. Massive user base and thousands of existing projects and libraries to use.
- WiFi, Bluetooth LE and Classic for any IoT project usage
- **8 MB Flash & 2 MB PSRAM**
- USB to Serial converter built in with high speed UART for debugging and uploading.
- Can be used with **Arduino IDE** or **MicroPython**
- **Built-in RGB NeoPixel LED** with power control to reduce quiescent power in deep sleep
- Battery input pads on underside with diode protection for external battery packs up to 6V input
- 13 GPIO pins:
  - 11 on breakout pads, 2 more on QT connector
  - 10 x 12-bit analog inputs
  - Dual 8-bit analog output DACs on A0/A1
  - PWM outputs on any pin
  - Two I2C ports, one on the breakout pads, and another with STEMMA QT plug-n-play connector
  - Hardware UART in addition to the USB-serial UART
  - Hardware SPI on the high speed SPI peripheral pins
  - Hardware I2S on any pins
  - 8 x Capacitive Touch with no additional components required
- 3.3V regulator with [**600mA peak output**](https://www.diodes.com/assets/Datasheets/AP2112.pdf)
- Light sleep at 4mA, deep sleep at ~70uA
- **Reset switch** for starting your project code over, boot 0 button for entering bootloader mode or for user reading
- **Really really small**
## Purchase

* [Adafruit](https://www.adafruit.com/product/5395)
