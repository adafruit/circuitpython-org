---
layout: download
board_id: "ai-thinker-esp32-cam"
title: "Ai Thinker ESP32-CAM Download"
name: "Ai Thinker ESP32-CAM"
manufacturer: "Ai-Thinker"
board_url:
  - "https://docs.ai-thinker.com/en/esp32-cam"
board_image: "ai-thinker-esp32-cam.jpg"
date_added: 2024-05-17
family: esp32
download_instructions: https://learn.adafruit.com/circuitpython-with-esp32-quick-start/
features:
  - Camera
  - Wi-Fi
  - Bluetooth/BTLE
  - Breadboard-Friendly
---

### More features
* Flashlight
* MicroSD Card Reader
* Optional ESP32-MB expansion board includes buttons and Serial port
* 8Mb PSRAM


ESP32-CAM is a small sized ESP32 camera module released by Ai-Thinker. The module can work independently with a size of only 27 x 40.5 x 4.5mm, and a deep sleep current as low as 6mA.

ESP32-CAM can be widely used in various IoT applications, suitable for home smart devices, industrial wireless control, wireless monitoring, QR wireless identification, wireless positioning system signals and other IoT applications. It is an ideal solution for IoT applications.

ESP32-CAM adopts DIP package and can be used directly by plugging in the bottom plate, realizing the rapid production of products, providing customers with high-reliability connection methods, which is convenient for application in various IoT hardware terminal occasions.

Ultra-small 802.11b/g/n Wi-Fi + BT/BLE SoC module


### Product Features
* Using low-power dual-core 32-bit CPU, can be used as an application processor
* Main frequency up to 240MHz, computing power up to 600 DMIPS
* Built-in 520 KB SRAM, external 8MB PSRAM included
* Support UART/SPI/I2C/PWM/ADC/DAC and other interfaces
* Support OV2640 and OV7670 cameras, built-in flashlight
* Support picture WiFI upload
* Support TF card
* Support multiple sleep modes
* Embedded Lwip, FreeRTOS, and CircuitPython
* Support STA/AP/STA+AP working mode
* Support Smart Config/AirKiss one-click network configuration
* Support secondary development


### Application scenarios
* Home smart device image transmission
* Wireless monitoring
* Smart agriculture
* QR wireless recognition


### Usage Notes

The serial port on the ESP32-MB adapter which usually ships with these boards has the Serial Request-To-Send (RTS) hardware flow-control line physically connected to the ESP32 Reset (RST) pin, and it also has the Serial Data-Terminal-Ready (DTR) hardware flow-control line physically connected to the ESP32 GPIO pin.

This allows software which knows this (e.g. Arduino) to automatically perform hardware resets over the serial port by pulsing the RTS-line, and to automatically perform firmware updates by holding the DTR line low while pulsing the RTS line.

Unfortunately, many serial emulators and even some python libraries which communicate via Serial ports will typically set the state of one of both of these hardware flow control lines - this means that your ESP32-CAM might not be able to boot or be used by some software.  Notable examples include Thonny, ampy, pyboard, and Windows version of Python itself\*

\* The work-around for Windows python is to first create the serial port object, without specifying which port to use - this bypasses the Python windows bug which always sets the RTS/DTR pins.  You can then tell the serial object which port, and set the RTS/DTR pins as you like.


## CircuitPython on ESP32

Want to learn how to load circuitpython onto this board? check out [this](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/) on the Adafruit learning system


## Purchase

* [Aliexpress](https://www.aliexpress.com/w/wholesale-esp32%2525252dcam.html)
* [Amazon](https://www.amazon.com/s?k=esp32-cam)
* [eBay](https://www.ebay.com/sch/i.html?_nkw=esp32-cam)
