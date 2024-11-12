---
layout: download
board_id: "pyportal_pynt"
title: "PyPortal Pynt Download"
name: "PyPortal Pynt"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4465"
board_image: "pyportal_pynt.jpg"
date_added: 2019-12-11
family: atmel-samd
bootloader_id: pyportal_m4
download_instructions: https://learn.adafruit.com/adafruit-pyportal/install-circuitpython
features:
  - Display
  - Speaker
  - Wi-Fi
---

The **PyPortal Pynt** is the little sister to our [popular PyPortal](https://www.adafruit.com/product/4116) - zapped with a shink ray to take the design from a 3.2" diagonal down to 2.4" diagonal screen - but otherwise the same! The PyPortal is our easy-to-use IoT device that allows you to create all the things for the “Internet of Things” in minutes. Make custom touch screen interface GUIs, all open-source, and Python-powered using tinyJSON / APIs to get news, stock, weather, cat photos, and more – all over Wi-Fi with the latest technologies. Create little pocket universes of joy that connect to something good. Rotate it 90 degrees, it’s a web-connected conference badge #badgelife.

The PyPortal uses an ATMEL (Microchip) ATSAMD51J20, and an Espressif ESP32 Wi-Fi coprocessor with TLS/SSL support built-in. PyPortal has a **2.4″ diagonal 320 x 240 color TFT** with resistive touch screen. PyPortal includes: speaker, light sensor, temperature sensor, NeoPixel, microSD card slot, 8MB flash, plug-in ports for I2C and 2 analog/digital pins, 3D files for custom enclosures / lanyard fastening. Open-source hardware, and Open-Source software, CircuitPython and Arduino. The device shows up as a USB drive and the code (Python) can be edited in any IDE, text editor, etc.

**Compared to the original PyPortal, the Pynt does not include a ADT7410 temperature sensor. Other than the ADT7410, the Pynt's display, processor, STEMMA conectors and WiFi have the exact same wiring as the original 3.2" PyPortal so all Arduino/CircuitPython code will run exactly the same - just smaller!**

The M4 and ESP32 are a great couple - and each bring their own strengths to this board. The SAMD51 M4 has native USB so it can show up like a disk drive, act as a MIDI or HID keyboard/mouse, and of course bootload and debug over a serial port. It also has DACs, ADC, PWM, and tons of GPIO. Meanwhile, the ESP32 has secure WiFi capabilities, and plenty of Flash and RAM to buffer sockets. By letting the ESP32 focus on the complex TLS/SSL computation and socket buffering, it frees up the SAMD51 to act as the user interface. You get a great programming experience thanks to the native USB with files available for drag-n-drop, and you don't have to spend a ton of processor time and memory to do SSL encryption/decryption and certificate management. It's the best of both worlds!

## Tutorial

- [PyPortal Pynt Overview](https://learn.adafruit.com/adafruit-pyportal)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4465)
