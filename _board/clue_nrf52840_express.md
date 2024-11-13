---
layout: download
board_id: "clue_nrf52840_express"
title: "CLUE NRF52840 Express Download"
name: "CLUE NRF52840 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4500"
 - "https://www.adafruit.com/product/4491"
 - "https://www.adafruit.com/product/5627"
board_image: "clue_nrf52840_express.jpg"
date_added: 2019-12-30
family: nrf52840
bootloader_id: clue_nrf52840
download_instructions: https://learn.adafruit.com/adafruit-clue/circuitpython
features:
  - Display
  - Bluetooth/BTLE
  - Solder-Free Alligator Clip
  - STEMMA QT/QWIIC
---
We wanted to build some projects that have a small screen and a lot of sensors. This board has a 1.3″ 240×240 IPS TFT display, two buttons, and sensors.

Available sensors:

* LSM series 9-DoF motion - LSM6DS33 Accel/Gyro + LIS3MDL magnetometer
* APDS9960 Proximity, Light, RGB, and Gesture Sensor
* PDM Microphone sound sensor
* Humidity, temperature and barometric environmental sensing

There’s a Qwiic/STEMMA QT connector for adding more sensors, like PM2.5 air quality and others that were too big to fit on the board.

We’ll be primarily using CircuitPython for programming it, but it will also work in Arduino.

After designing it, the board was close enough to micro:bit-shape-size that we moved a few parts to make it fit in micro:bit robots and some projects – the nrf52840 is a big upgrade chip and can do stuff like Tensorflow Lite for Microcontrollers, BLE central and peripheral, and more.

## Technical details

* Nordic nRF52840 Bluetooth LE processor - 1 MB of Flash, 256 KB RAM, 64 MHz Cortex M4 processor
* 1.3″ 240x240 Color IPS TFT display for high resolution text and graphics
* Power it from any 3-6V battery source (internal regulator and protection diodes)
* Two A/B user buttons and one reset button
* RGB NeoPixel indicator LED
* 2 MB internal flash storage for datalogging, images, fonts or CircuitPython code
* Buzzer/speaker for playing tones and beeps
* Two bright white LEDs in front for illumination/color sensing.

## Tutorials

* [CLUE Overview](https://learn.adafruit.com/adafruit-clue)
* [Projects and Guides](https://learn.adafruit.com/products/4500/guides)

## Purchase

* [Adafruit CLUE](https://www.adafruit.com/product/4500)
