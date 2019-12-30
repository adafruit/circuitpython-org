---
layout: download
board_id: "clue_nrf52840_express"
title: "CLUE NRF52840 Express Download"
name: "CLUE NRF52840 Express"
manufacturer: "Adafruit"
board_url: ""
board_image: "clue_nrf52840_express.jpg"
features:
  - Display
  - Wi-Fi
  - Bluetooth/BTLE
  - Solder-free Alligator clip

---
We wanted to build some projects that have a small screen and a lot of sensors. this board has a 1.3″ 240×240 ips tft display, two buttons, and a ton of sensors:

lsm series 9 dof motion, apds9960 light/color/proximity, pdm microphone, humidity, temperature and barometric environmental sensing.

There’s a qwiic/stemmaqt connector for adding more sensors like pm2.5 air quality and others that were too big to fit on the board.

We’ll be primarily using circuitpython for programming it, but it will also work in arduino. and of course, we’d love to see makecode on it!

After designing it, the board was close enough to micro:bit-shape-size that we moved a few parts to make it fit in micro:bit robots and some projects – the nrf52840 is a big upgrade chip and can do stuff like tensorflow lite for microcontrollers, ble central and peripheral, and more.

## Learn More
* [YouTube](https://youtu.be/uNDqkglM8_Y)
* [Adafruit Blog](https://blog.adafruit.com/2019/12/24/adafruit-top-secret-december-24-2019-get-a-clue-adafruit-clue/)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
