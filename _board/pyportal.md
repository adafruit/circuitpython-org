---
layout: download
board_id: "pyportal"
title: "PyPortal Download"
name: "PyPortal"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4116"
 - "https://www.adafruit.com/product/4061"
board_image: "pyportal.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: pyportal_m4
download_instructions: https://learn.adafruit.com/adafruit-pyportal/install-circuitpython
features:
  - Display
  - Speaker
  - Wi-Fi
---

**PyPortal**, is Adafruit's easy-to-use IoT device that allows you to create all the things for the “Internet of Things” in minutes. Make custom touch screen interface GUIs, all open-source, and Python-powered using tinyJSON / APIs to get news, stock, weather, cat photos, and more – all over Wi-Fi with the latest technologies. Create little pocket universes of joy that connect to something good. Rotate it 90 degrees, it’s a web-connected conference badge #badgelife.

[![PyPortal](http://img.youtube.com/vi/9meeVehRS6A/0.jpg)](http://www.youtube.com/watch?v=9meeVehRS6A "PyPortal")

The PyPortal uses an ATMEL (Microchip) ATSAMD51J20, and an Espressif ESP32 Wi-Fi coprocessor with TLS/SSL support built-in. PyPortal has a **3.2″ 320 x 240 color TFT** with resistive touch screen. PyPortal includes: speaker, light sensor, temperature sensor, NeoPixel, microSD card slot, 8MB flash, plug-in ports for I2C and 2 analog/digital pins, 3D files for custom enclosures / lanyard fastening. Open-source hardware, and Open-Source software, and CircuitPython. The device shows up as a USB drive and the code (Python) can be edited in any IDE, text editor, etc.

The M4 and ESP32 are a great couple - and each bring their own strengths to this board. The SAMD51 M4 has native USB so it can show up like a disk drive, act as a MIDI or HID keyboard/mouse, and of course bootload and debug over a serial port. It also has DACs, ADC, PWM, and tons of GPIO. Meanwhile, the ESP32 has secure WiFi capabilities, and plenty of Flash and RAM to buffer sockets. By letting the ESP32 focus on the complex TLS/SSL computation and socket buffering, it frees up the SAMD51 to act as the user interface. You get a great programming experience thanks to the native USB with files available for drag-n-drop, and you don't have to spend a ton of processor time and memory to do SSL encryption/decryption and certificate management. It's the best of both worlds!

## Tutorials
* [PyPortal Overview](https://learn.adafruit.com/adafruit-pyportal)
* [Projects and Guides](https://learn.adafruit.com/products/4116/guides)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4116)
