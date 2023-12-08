---
layout: download
board_id: "espressif_esp32_eye"
title: "ESP-EYE Download"
name: "ESP-EYE"
manufacturer: "Espressif"
board_url:
 - "https://www.adafruit.com/product/4095"
board_image: "espressif_esp32_eye.jpg"
date_added: 2022-08-22
family: esp32
features:
  - Wi-Fi
  - Camera
  - Bluetooth/BTLE
---

Ever wanted to dabble in face and/or speech recognition? [Espressif's](https://www.espressif.com/) **ESP-EYE** is a miniature [ESP32-based](https://www.adafruit.com/?q=ESP32) development board that combines a digital microphone, ESP32 (of course) with 8 MB PSRAM and 4 MB flash, and a 2 megapixel camera. There's a few buttons and LEDs as well for basic control and configuration.

Unlike some boards, this codebase does not require internet connectivity - you don't have to send video or audio data to 'the cloud' - it's all processed on-chip! The built in demo shows off what it can do:

- Plug into a computer USB port and open up a serial port connection at 115,200 baud to the new serial port
- Once the red LED is lit, activate the board with the watchword "Hi Lehshin" (in documents they spell it lexin, the x is pronounced as a shh sound)
- The red LED will blink - then connect to the new Wi-Fi access point created
- Open up a web browser to http://192.168.4.1/face_stream
- Point the camera at faces to show off the recognition boxes! Video is about 2 frames per second, not super fast.

## Purchase

* [Adafruit](https://www.adafruit.com/product/4095)
