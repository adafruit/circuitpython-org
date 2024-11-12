---
layout: download
board_id: "adafruit_magtag_2.9_grayscale"
title: "MagTag - 2.9\" Grayscale E-Ink WiFi Display Download"
name: "MagTag - 2.9\" Grayscale E-Ink WiFi Display"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4800"
 - "https://www.adafruit.com/product/4819"
board_image: "adafruit_magtag_2.9_grayscale.jpg"
date_added: 2020-11-10
family: esp32s2
download_instructions: https://learn.adafruit.com/adafruit-magtag/circuitpython
bootloader_id: adafruit_magtag_29gray
features:
  - Wi-Fi
  - Battery Charging
  - STEMMA QT/QWIIC
  - Speaker
  - Display
  - USB-C
---

The Adafruit MagTag combines the new ESP32-S2 wireless module and a 2.9" grayscale E-Ink display to make a low-power IoT display that can show data on its screen even when power is removed! The ESP32-S2 is great because it builds on the years of code and support for the ESP32 and also adds native USB support so you can use this board with Arduino _or_ CircuitPython!

We designed this board to be low-power friendly - with a spot for a 350 or 420 mAh battery and built in battery charging over USB C. During deep sleep, with the NeoPixels and speaker amplifier disabled, we measured 250uA power draw so you can run for a few weeks between charges.

And of course, the Mag in MagTag stands for _magnetic_. [We have four M3 standoffs that will work perfectly with these mini magnet feet](https://www.adafruit.com/product/4631). (Originally they're designed for RGB Matrices but they'll do an excellent job here as well). Screw on the feet and you can attach this display to a metallic shelf, fridge, or bench.

## Technical details

 * **ESP32-S2 240 MHz Tensilica processor** - the next generation of ESP32, now with native USB so it can act like a keyboard/mouse, MIDI device, disk drive, etc!
 * **WROVER module** has FCC/CE certification and comes with 4 MB of Flash and 2 MB of PSRAM - you can have huge data buffers
 * **2.9" grayscale display with 296x128 pixels**. Each pixel can be white, light gray, dark gray or black. Compared to 'tri-color' displays with a red pigment, this display takes a lot less time to update, only about a second instead of 15 seconds!
 * **USB C** power and data connector
 * 4 **RGB side-emitting NeoPixels** so you can light up the display with any color or pattern
 * 4 **buttons** can be used to wake up the ESP32 from deep-sleep, or select different modes
 * **Triple-axis accelerometer** (LIS3DH) can be used to detect orientation of the display
 * **Speaker/Buzzer** with mini class D amplifier on DAC output A0 can play tones or lo-fi audio clips.
 * Front facing **light sensor**
 * **STEMMA QT** port for [attaching all sorts of I2C devices](https://www.adafruit.com/stemma)
 * 2 **STEMMA 3 pin JST** connectors for attaching [NeoPixels](https://www.adafruit.com/product/3919), [speakers](https://www.adafruit.com/product/3885), [servos](https://www.adafruit.com/product/4326) or [relays](https://www.adafruit.com/product/4409).
 * **On/Off switch**
 * **Boot** and **Reset buttons** for re-programming

## Purchase:

* [Adafruit](https://www.adafruit.com/product/4800)
