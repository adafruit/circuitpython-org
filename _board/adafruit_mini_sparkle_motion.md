---
layout: download
board_id: "adafruit_mini_sparkle_motion"
title: "Adafruit Mini Sparkle Motion Download"
name: "Adafruit Mini Sparkle Motion"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/6160"
board_image: "adafruit_mini_sparkle_motion.jpg"
date_added: 2025-01-16
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-sparkle-motion-mini/install-circuitpython
features:
  - Bluetooth/BTLE
  - Wi-Fi
  - USB-C
  - STEMMA QT/QWIIC
---

The [Adafruit Sparkle Motion Mini](https://www.adafruit.com/product/6160) is part of our series of "Sparkle Motion" boards, that are our attempt to make the best small WLED-friendly smart LED driving board in the whole world. Our resident mermaid, firepixie makes a lot of projects with WLED and she loves it! So how can we make something that will be powerful enough to drive advanced LED projects that need a compact design?

The Mini version of the Sparkle Motion is a simpler version of our full-featured Sparkle Motion, we give up the high voltage support and built in IR receiver, in order to make it under 1 square inch in size! By using a 4-layer board and double-sided assembly we've put together this feature set:

* <b>Power via USB Type C for up to 5V 4A input -</b> you can use off-the-shelf USB battery packs for portable operation.
* <b>4 Amp resetting fuse</b> to protect from over-current drive
* <b>ESP32</b> mini module with built in antenna port - the classic ESP32 has the best WLED support even if we'd prefer the 'S2 or 'S3. Comes with 4 MB of flash, dual core 240MHz Tensilica, WiFi, Bluetooth LE and Bluetooth Classic support.
* <b>USB-serial converter</b> with auto-reset
* <b>Two output signals plus 5V power and ground</b> - both signal output are level shifted to 5V. These are on 0.1" spaced breakout pads. To keep the design slim we don't include terminal blocks pre-soldered, [but we do stock the matching blocks if you want them](https://www.adafruit.com/product/2137)
* <b>Extra 2x3 0.1" breakout pads</b> with 4 more GPIO plus 3V power and ground.
* <b>Built-in I2S microphone</b>
* <b>Stemma QT I2C port</b> to connect external sensors/OLED/etc
* <b>User button on GPIO 0</b> plus Reset button
* <b>Red built-in LED</b> on pin 12
* <b>Small built-in NeoPixel</b> on pin 18 
* <b>Separate analog/digital input JST port</b> for analog input, potentiometer, microphone or external IR receiver on pin 13
* <b>Compact enough you can use it for wearable projects</b> - 1.2"x0.8" / 30mm x 20mm size with mounting holes

While we recommend it for use with WLED, it will also work just fine as a compact ESP32 board for use with Arduino, ESP-IDF, MicroPython, CircuitPython or any other ESP32 supported codebase. 

Note that unlike the classic Sparkle Motion board, we don't include terminal blocks pre-soldered to keep the board very slim. We do stock the matching blocks if you want them, a small amount of soldering is required to attach them. Also, unlike the bigger version, we dropped the on-board IR receiver - however its easy to add one by plugging in a JST SH 3-pin socket cable and slotting in an IR receiver module.

## Purchase

* [Adafruit](https://www.adafruit.com/product/6160)
