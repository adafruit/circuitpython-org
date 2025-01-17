---
layout: download
board_id: "adafruit_sparkle_motion"
title: "Adafruit Sparkle Motion Download"
name: "Adafruit Sparkle Motion"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/6100"
board_image: "adafruit_sparkle_motion.jpg"
date_added: 2025-01-16
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-sparkle-motion/install-circuitpython
features:
  - Bluetooth/BTLE
  - Wi-Fi
  - USB-C
  - STEMMA QT/QWIIC
---

[Adafruit Sparkle Motion - All-In-One WLED and xLights Board](https://www.adafruit.com/product/6100)

We're designing a board for using WLED - and we want to make like the bestest board in the whole world. Our resident mermaid, firepixie makes a lot of projects with WLED and she loves it! So how can we make something that will be powerful but not too bulky? Here's some things we're thinking about as
the design starts to congeal like cranberry sauce:

* Power via USB Type C PD with a slide switch that selects between 5, 12 and 20V (24V pixels can usually run fine at 20V) OR via 2.1mm DC jack
* Low forward-voltage diodes so its good for up to 5A from either
* 5 Amp fuse to protect from over-current drive
* ESP32 mini module with built in or optionally wFL antenna port (the classic '32 has broad support even if we'd prefer the 'S2 or 'S3)
* Three output signal terminal block sets with power and ground for each - they'll be level shifted to 5V.
* 6 GPIO breakout pads with a fourth level-shifted ouput, and 3 more GPIO plus power and ground.
* Built-in I2S microphone
* Built-in IR receiver
* Stemma QT I2C port to connect external sensors/OLED/etc
* Separate analog/digital input JST port for analog input, potentiometer, microphone or external IR receiver
* Compact enough you can use it for wearable projects - 1.3"x1.75" / 33mm x 45mm size with mounting holes

## Purchase

* [Adafruit](https://www.adafruit.com/product/6100)
