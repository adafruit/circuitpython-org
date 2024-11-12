---
layout: download
board_id: "adafruit_matrixportal_s3"
title: " MatrixPortal S3 Download"
name: "MatrixPortal S3"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5778"
board_image: "adafruit_matrixportal_s3.jpg"
date_added: 2023-06-26
family: esp32s3
bootloader_id: adafruit_matrixportal_s3
download_instructions: https://learn.adafruit.com/adafruit-matrixportal-s3/install-circuitpython
tags:
  - Matrix Portal
features:
  - External Display
  - Wi-Fi
  - Bluetooth/BTLE
  - STEMMA QT/QWIIC
  - USB-C
---

Folks love our [wide selection of RGB matrices](https://www.adafruit.com/category/327) and accessories for making custom colorful LED displays... and our RGB Matrix Shields and FeatherWings can be quickly soldered together to make the wiring much easier. But what if we made it *even easier* than that? **Like, no solder, no wiring, just instant plug-and-play?** Dream no more - with the **Adafruit Matrix Portal S3 add-on for RGB Matrices**, there's never been an easier way to create powerful Internet-connected LED displays.

You can plug directly into the back of [any HUB-75 compatible display (all the ones we stock will work) from 16x32 up to 64x64](https://www.adafruit.com/category/327) or use the stock 2x8 IDC cables to plug into the front. Use the included screws to attach the power cable to the power plugs with a common screwdriver, then power it with any USB C power supply. Chain dozens of displays for long stretches, or you can panelize them in a grid for bigger displays. For larger projects, power the matrices with a separate 5V power adapter.

Then code up your project in [CircuitPython](https://learn.adafruit.com/rgb-led-matrices-matrix-panels-with-circuitpython) or [Arduino](https://learn.adafruit.com/adafruit-protomatter-rgb-matrix-library), our Protomatter matrix library works great on the ESP32-S3 chipset, knowing that you've got the wiring and level shifting all handled. Here's what you get:

- **ESP32-S3 processor**, 8 MB flash, 2 MB of SRAM, with full Arduino or CircuitPython support
- **WiFi and Bluetooth LE** baked right in, full Arduino support. CircuitPython only supports WiFi at this time, not BLE on the S3 chip.
- **USB Type C** connector for data and power connectivity
- [**I2C STEMMA QT connector** for plug-n-play use of any of our STEMMA QT devices or sensors](https://www.adafruit.com/category/620) can also be used with [any Grove I2C devices using this adapter cable](https://www.adafruit.com/product/4528)
- **JST 3-pin connector** that also has analog input [for quick connection with any JST PH 2.0mm pitch cable](https://www.adafruit.com/search?q=jst+2mm).
- **LIS3DH accelerometer** for digital sand projects or detecting taps/orientation.
- **GPIO breakout strip -** has reset, boot selection, TX debug output, and 6 GPIO including 4 analog inputs with PWM, SPI, or I2S support for adding other hardware.
- **Address E line jumper** for use with 64x64 matrices (check your matrix to see which pin is used for address E, we default to pin 8
- **Two user interface buttons** + one reset button
- **Indicator NeoPixel** and red LED
- **Green power indicator LEDs** for both 3V and 5V power
- **2x10 socket connector** fits snugly into 2x8 HUB75 ports without worrying about 'off by one' errors
- **2x8 IDC plug connector** works with standard cables that come with matrices.

The Matrix Portal uses an Espressif ESP32-S3 Wi-Fi+BLE chipset, and has dropped the SAMD51 from the original Matrix Portal due to silicon shortages. But turns out the S3 is really great at doing all the work of the original all on its own:

- The S3 has a parallel output drive peripheral which means that controlling the matrix is done without bitbanging.
- The S3 has two cores so one can be dedicated to WiFi networking or matrix control while the other runs your code.
- With native USB, its easy to have it act like a keyboard, or mouse, or MIDI device and it also has plenty of I2C, SPI, I2S, UART and analog inputs.
- Lots of memory: 8MB of Flash means plenty of space for code, files, GIFs and more. 2MB of PSRAM means you can read and parse a lot of IoT data and still have plenty of RAM for the matrix display buffers.
- The only real thing missing from the original Matrix Portal is the S3 does not have an analog output DAC pin, we recommend an I2S amplifier for audio instead.

Comes with one fully programmed and assembled MatrixPortal, preprogrammed with a basic display demo for 32x64 LED matrices.

## Purchase:

* [Adafruit](https://www.adafruit.com/product/5778)