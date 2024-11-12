---
layout: download
board_id: "pyportal_titano"
title: "PyPortal Titano Download"
name: "PyPortal Titano"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4444"
board_image: "pyportal_titano.jpg"
date_added: 2019-08-30
family: atmel-samd
bootloader_id: pyportal_m4
download_instructions: https://learn.adafruit.com/adafruit-pyportal-titano/circuitpython
features:
  - Display
  - Speaker
  - Wi-Fi
  - USB-C
---

The **PyPortal Titano** is the big sister to our [popular PyPortal](https://www.adafruit.com/product/4116) now with _twice as many pixels!_ The PyPortal is our easy-to-use IoT device that allows you to create all the things for the “Internet of Things” in minutes. Make custom touch screen interface GUIs, all open-source, and Python-powered using tinyJSON / APIs to get news, stock, weather, cat photos, and more – all over Wi-Fi with the latest technologies. Create little pocket universes of joy that connect to something good. Rotate it 90 degrees, it’s a web-connected conference badge #badgelife.

The Titano uses an ATMEL (Microchip) ATSAMD51J20, and an Espressif ESP32 Wi-Fi coprocessor with TLS/SSL support built-in. PyPortal has a bigger **3.5″ diagonal 320 x 480 color TFT** with resistive touch screen. Compare that to the original PyPortal's 3.2" 240x320, we have twice as many pixels! Also, we've updated the connector to be a reverse-friendly **USB C** connector.

**Compared to the original PyPortal, the Titano does not include a ADT7410 temperature sensor. It also has a higher-resolution screen with a different controller chip. The Processor, STEMMA conectors and WiFi have the exact same wiring as the original 3.2" PyPortal so if you are running Arduino/CircuitPython code, you'll just have to adjust your graphics and fonts for the larger resolution screen!**

The PyPortal Titano includes: speaker, light sensor, temperature sensor, NeoPixel, microSD card slot, 8MB flash, plug-in ports for I2C and 2 analog/digital pins. Open-source hardware, and Open-Source software, CircuitPython and Arduino. The device shows up as a USB drive and the code (Python) can be edited in any IDE, text editor, etc.

The M4 and ESP32 are a great couple - and each bring their own strengths to this board. The SAMD51 M4 has native USB so it can show up like a disk drive, act as a MIDI or HID keyboard/mouse, and of course bootload and debug over a serial port. It also has DACs, ADC, PWM, and tons of GPIO. Meanwhile, the ESP32 has secure WiFi capabilities, and plenty of Flash and RAM to buffer sockets. By letting the ESP32 focus on the complex TLS/SSL computation and socket buffering, it frees up the SAMD51 to act as the user interface. You get a great programming experience thanks to the native USB with files available for drag-n-drop, and you don't have to spend a ton of processor time and memory to do SSL encryption/decryption and certificate management. It's the best of both worlds!

## Tutorial

- [PyPortal Titano Overview](https://learn.adafruit.com/adafruit-pyportal-titano)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4444)
