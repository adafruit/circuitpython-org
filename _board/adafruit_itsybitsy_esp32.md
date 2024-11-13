---
layout: download
board_id: "adafruit_itsybitsy_esp32"
title: "Adafruit ItsyBitsy ESP32 Download"
name: "Adafruit ItsyBitsy ESP32"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5889"
board_image: "adafruit_itsybitsy_esp32.jpg"
date_added: 2024-02-20
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-itsybitsy-esp32/circuitpython-setup
features:
  - Bluetooth/BTLE
  - Wi-Fi
  - Breadboard-Friendly
  - STEMMA QT/QWIIC
---

What's smaller than a Feather but larger than a Trinket? It's an Adafruit ItsyBitsy ESP32, a powerful processor PCB with a plethora of pins! It features the ESP32 Pico module, an FCC-certified module that contains an ESP32 chip with dual-core 240MHz Tensilica processor, WiFi, and Bluetooth classic + BLE, configured with 8 MB of Flash memory, and 2 MB of PSRAM.

We've added some handy accessories like a USB to serial converter chip, power regulator, USB Micro B, buttons, NeoPixel, and Stemma QT I2C connector to outfit this super-hero chip for any task you want to throw it at. This is also an ultra low power ESP32 board with a deep sleep current consumption of 10uA!

At the core of the Itsy is the ESP32 (PICO ECO V3) chip, which is a single 2.4 GHz Wi-Fi and Bluetooth combo chip designed with TSMC’s 40 nm low-power technology. The ESP32 PICO in particular integrates all peripheral components seamlessly, including a crystal oscillator, flash, PSRAM, filter capacitors, and RF matching links in one single package. This makes it perfect for stuffing into a small space as the ItsyBitsy.

Please note, like other ESP32 modules, the ItsyBitsy ESP32 does not have native USB support - instead, there's a USB to serial converter chip. This means it cannot act like a USB keyboard or mouse, but it does have BLE and BT classic, so you could use it wirelessly.

## Technical details

* Same size, form-factor as the remaining ItsyBitsy mainboards - with a similar but not identical pinout (there are no pins at the end of the board like most other Itsy's due to the radio antenna being there)
* USB Micro B - To maintain compatibility with the rest of the ItsyBitsy's
* ESP32 V2 03 Dual Core 240MHz Xtensa processor - the ESP32 you know and love, with the latest engineering fixes. Massive user base and thousands of existing projects and libraries to use.
* WiFi, Bluetooth LE, and BT Classic for any IoT project usage
* 8 MB Flash & 2 MB PSRAM
* USB to Serial converter built-in with high-speed UART for debugging and uploading, auto-reset circuit works perfectly with any ESP32 uploading tool.
* Can be used with Arduino IDE, CircuitPython or MicroPython
* Built-in RGB NeoPixel LED with power control to reduce quiescent power in deep sleep
* Built-in Red LED on pin D13
* 5V level-shifted output on D5, perfect for driving NeoPixels or other devices that want 5V logic signal
* Battery input pads on the underside with diode protection for external battery packs up to 6V input
* 20 General Purpose "IO" pins:
* 20 Pads expose pins from the ESP32:
* 3 are analog input only (A3, A4, A5)
* 1 is digital output only (5) with 5V level shifted up
* 13 x 12-bit analog inputs (A0, A1, A2, A3, A4, A5, D12, D13, D14, SDA, SCL, D32, D33)
* Dual 8-bit analog output DACs on A0/A1
* PWM outputs on any pin
* I2C port with STEMMA QT plug-n-play connector - a second I2C port can be defined on any other pins.
* Hardware UART in addition to the USB-serial UART
* Hardware SPI on the high speed SPI peripheral pins - a second SPI port can be defined on any other pins.
* Hardware I2S on any pins
* 8 x Capacitive Touch with no additional components required
* 3.3V regulator with 600mA peak output
* Light sleep at 4mA, deep sleep at ~10uA
* Reset switch for starting your project code over, for entering bootloader mode or for user reading
* User switch on pin 35
* Really small

## Tutorials

* [Adafruit ItsyBitsy ESP32](https://learn.adafruit.com/adafruit-itsybitsy-esp32)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5889)
