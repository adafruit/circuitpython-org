---
layout: download
board_id: "clue_nrf52840_express"
title: "CLUE NRF52840 Express Download"
name: "CLUE NRF52840 Express"
manufacturer: "Adafruit"
board_url: "https://www.adafruit.com/product/4500"
board_image: "clue_nrf52840_express.jpg"
features:
  - Display
  - Wi-Fi
  - Bluetooth/BTLE
  - Solder-free Alligator clip

---
We wanted to build some projects that have a small screen and a lot of sensors. This board has a 1.3″ 240×240 IPS TFT display, two buttons, and a ton of sensors:

LSM series 9-DoF motion - LSM6DS33 Accel/Gyro + LIS3MDL magnetometer
APDS9960 Proximity, Light, RGB, and Gesture Sensor
PDM Microphone sound sensor
Humidity, temperature and barometric environmental sensing
There’s a Qwiic / STEMMA QT connector for adding more sensors, like PM2.5 air quality and others that were too big to fit on the board.

We’ll be primarily using CircuitPython for programming it, but it will also work in Arduino. And of course, we’d love to see MakeCode on it!

After designing it, the board was close enough to micro:bit-shape-size that we moved a few parts to make it fit in micro:bit robots and some projects – the nrf52840 is a big upgrade chip and can do stuff like Tensorflow Lite for Microcontrollers, BLE central and peripheral, and more.

## Tutorials

[CLUE Overview](https://learn.adafruit.com/adafruit-clue)
[Projects and Guides](https://learn.adafruit.com/search?q=CLUE)

## Purchase
* [Adafruit CLUE](https://www.adafruit.com/product/4500)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
