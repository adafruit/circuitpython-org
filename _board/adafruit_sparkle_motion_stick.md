---
layout: download
board_id: "adafruit_sparkle_motion_stick"
title: "Adafruit Sparkle Motion Download"
name: "Adafruit Sparkle Motion"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/6332"
 - "https://www.adafruit.com/product/6333"
board_image: "adafruit_sparkle_motion_stick.jpg"
date_added: 2025-05-15
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-sparkle-motion/install-circuitpython
features:
  - Bluetooth/BTLE
  - Wi-Fi
---

The **Adafruit Sparkle Motion Stick** is part of our series of "Sparkle Motion" boards, which are our attempt to make the best small WLED-friendly smart LED driving board in the whole world. Our resident mermaid, [firepixie](https://learn.adafruit.com/u/firepixie) makes a lot of projects with WLED, and she loves it! So, how can we make something powerful enough to drive advanced LED projects that need a compact design?

**This version includes both the Sparkle Motion Stick and the enclosure**, which is great if you want to protect your USB dongle from everyday usage, but note that it is not waterproof or weatherproof. There are three pieces: two snap over the PCB to capture it in place, and one can be used as a USB A port cap. We also like there's a button lever - by default in WLED pin 0 is an on/off mode switcher, but you can program it to do other stuff.

The USB Stick version of the Sparkle Motion is a simpler version of our full-featured Sparkle Motion. [It even fits into a low cost off-the-shelf case for protection.](https://www.adafruit.com/product/6176)

- **Power via USB Type A for up to 5V 2A input -** you can use off-the-shelf USB battery packs for portable operation.
- **2 Amp resetting fuse** to protect from over-current drive
- **ESP32** mini module with built-in antenna port - the classic ESP32 has the best WLED support, even if we'd prefer the 'S2 or 'S3. Comes with 4 MB of flash, dual-core 240MHz Tensilica, WiFi, Bluetooth LE, and Bluetooth Classic support.
- **USB-serial converter** with auto-reset
- **Two output signals plus 5V power and ground** - both signal outputs are level shifted to 5V.
- **Built-in I2S microphone** for audio-reactive projects
- **Built-in Infrared receiver** on GPIO 10 for easy remote control integration
- **User button on GPIO 0** which you can press even when its in the snap-on case
- **Red built-in LED** on pin 4
- **Small built-in NeoPixel** on pin 18
- **Screw terminal blocks** for no-solder connectivity

Compared to our [larger Sparkle Motion board](https://www.adafruit.com/product/6100), this only supports 5V and doesn't have a reset button, there are fewer outputs, and no breakout pads of I2C/GPIO connections for external accessories.
Compared to our [Sparkle Motion Mini](https://www.adafruit.com/product/6160), this has a USB A port so it's 2A max power. It does have IR and built-in terminal blocks but does not have GPIO breakout pads.

While we recommend it for use with WLED, it will also work just fine as a compact ESP32 board for use with Arduino, ESP-IDF, MicroPython, CircuitPython, or any other ESP32-supported codebase.

## Purchase

* [Adafruit](https://www.adafruit.com/product/6332)
