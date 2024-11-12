---
layout: download
board_id: "adafruit_esp32s3_camera"
title: "MEMENTO - Python Programmable DIY Camera Download"
name: "MEMENTO - Python Programmable DIY Camera"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5420"
board_image: "adafruit_esp32s3_camera.jpg"
date_added: 2023-10-27
family: esp32s3
bootloader_id: adafruit_camera_esp32s3
download_instructions: https://learn.adafruit.com/adafruit-memento-camera-board/install-circuitpython
features:
  - Wi-Fi
  - Bluetooth/BTLE
  - Camera
  - Display
  - USB-C
  - Battery Charging
---

Make memories, or just a cool camera-based project, with **Adafruit's MEMENTO Camera Board**. It's a development board with everything you need to create programmable camera and vision projects: with a camera module, TFT preview screen, buttons, SD card slot and driven by a powerful ESP32-S3 with 2 MB of PSRAM for buffering 5 MegaPixel camera images.

**This product is just the mainboard, and does not come with an enclosure, LED ring, hardware, SD card, or battery.**

The ESP32-S3 is a WiFi and Bluetooth LE capable, 240 MHz dual core Tensilica processor - much like the famous ESP32. The S3 adds native USB support so it's great for use with Arduino or CircuitPython. The S3 also has the ability to interface with raw camera modules. The cameras require 12 GPIO pins and fast data transfer in order to get images off the sensor, and then a lot of memory for storing 2560 x 1920 images - which is why we picked an S3 module with 2MB of PSRAM so that we can read JPEGs into memory for saving onto an SD card.

To make the board easy to use we added a ton of supporting hardware, here's a full list of the hardware included:

- **ESP32-S3 module with 8 MB Flash, 2 MB PSRAM** - dual core 240MHz Tensilica with WiFi and BTLE.
- [**OV5640 camera module with 72 degree view and auto-focus motor**](https://www.adafruit.com/product/5840) - 5MP camera sensor with JPEG encoder built in.
- [**1.54" 240x240 Color TFT**](https://www.adafruit.com/product/4421) - For previewing the camera images, or user interface design.
- **MicroSD card slot** - Store images or animations to any SPI-capable micro SD card.
- **Two Digital/Analog Stemma Ports** - JST PH-3 connectors for A0, A1 and power+ground for adding external buttons, LEDs, or sensors. Can provide 3V or 5V power.
- **I2C Stemma QT Port** - Connect just about any I2C sensor you please with a Stemma QT JST SH port, provides 3.3V power and logic.
- **LIS3DH Accelerometer** - Triple-access accelerometer can detect orientation, shaking or movement.
- **LiPoly battery charging support** - [Use a 3.7/4.2V 350mA](https://www.adafruit.com/product/4237) or [420mA battery](https://www.adafruit.com/product/4236) for on-the-go snaps.
- **6 User Buttons** - change modes, preview saved images, play DOOM (?). Connected through a GPIO expander
- **Buzzer** - play tones or alerts, or indicate when a photo was successfully taken
- **Analog Microphone** - Can be used as a sensor to detect loud sounds, not for recording video with audio.
- **Shutter button** - Connected to GPIO 0 for entering the ROM bootloader
- **Reset button** - For entering the bootloader or starting over
- **On/Off switch** - Cut all power when using a battery
- **USB Type C** for programming the ESP32-S3, as well as REPL access in CircuitPython and charging the optional LiPoly battery
- **Breakout pads for hardware UART** - for more intense debugging needs, solder wires to the through-hole pads to connect to a console cable.
- **Four M3 standoffs** for mounting or enclosure attachment.

We've got both Arduino and CircuitPython example code that lets you preview the camera, adjust settings, and take photos that are saved to disk. However, we recommend CircuitPython because the compilation time in Arduino is pretty intense due to the huge amount of code required to run the camera. [CircuitPython is fast to develop for and our library will make it easy to start making custom camera projects](https://github.com/adafruit/Adafruit_CircuitPython_PyCamera).

## Purchase

* [Adafruit](https://www.adafruit.com/product/5420)
