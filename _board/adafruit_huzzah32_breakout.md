---
layout: download
board_id: "adafruit_huzzah32_breakout"
title: "Adafruit HUZZAH32 Breakout Download"
name: "Adafruit HUZZAH32 Breakout"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4172"
board_image: "adafruit_huzzah32_breakout.jpg"
date_added: 2023-03-01
family: esp32
downloads_display: true
features:
  - Feather-Compatible
  - Battery Charging
  - Bluetooth/BTLE
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
---

Squeeeeze down your next ESP32 project to its bare-bones essential with the **Adafruit HUZZAH32 Breakout**. This breakout is basically the 'big sister' of our HUZZAH 8266, but instead of an ESP8266 it has the '32! We've pared down our popular [Feather ESP32](https://www.adafruit.com/product/3405), removing the battery charger and USB-serial converter. You just get a regulator, some protection diodes, two buttons and an LED. For some projects, where price and size are at a premium, you can program this board over the 'FTDI cable' breakout when needed, and leave it alone otherwise.

Note that this board *doesn't* come with a USB to serial converter chip and auto-reset circuit. Instead, you will need to plug in a [CP2104 Friend](https://www.adafruit.com/product/3309) or [FTDI cable](https://www.adafruit.com/product/70). Then, before uploading code, put it into bootloader mode by holding down the GPIO #0 button and clicking Reset button, then releasing the #0 button.

That module in the middle of the breakout contains a dual-core ESP32 chip, 4 MB of SPI Flash, tuned antenna, and all the passives you need to take advantage of this powerful new processor. The ESP32 has both WiFi *and* Bluetooth Classic/LE support. That means it's perfect for just about any wireless or Internet-connected project.

The ESP32 is a perfect upgrade from the ESP8266 that has been so popular. In comparison, the ESP32 has way more GPIO, plenty of analog inputs, two analog outputs, multiple extra peripherals (like a spare UART), two cores so you don't have to yield to the WiFi manager, much higher-speed processor, etc. etc!

Comes fully assembled and tested, pre-programmed with ESP32 SPI WiFi co-processor firmware that [you can use in CircuitPython to use this into a WiFi co-processsor over SPI + 2 pins](https://github.com/ladyada/Adafruit_CircuitPython_ESP32SPI). We also toss in some header so you can solder it in and plug into a solderless breadboard.

Here are [specifications from Espressif about the ESP32](https://espressif.com/en/products/hardware/esp32/overview):

- 240 MHz dual core Tensilica LX6 microcontroller with 600 DMIPS
- Integrated 520 KB SRAM
- Integrated 802.11b/g/n HT40 Wi-Fi transceiver, baseband, stack and LWIP
- Integrated dual mode Bluetooth (classic and BLE)
- 4 MByte flash include in the WROOM32 module
- On-board PCB antenna
- Ultra-low noise analog amplifier
- Hall sensor
- 10x capacitive touch interface
- 32 kHz crystal oscillator
- 3 x UARTs (only two are configured by default in the Feather Arduino IDE support, one UART is used for bootloading/debug)
- 3 x SPI (only one is configured by default in the Feather Arduino IDE support)
- 2 x I2C (only one is configured by default in the Feather Arduino IDE support)
- 12 x ADC input channels
- 2 x I2S Audio
- 2 x DAC
- PWM/timer input/output available on every GPIO pin
- OpenOCD debug interface with 32 kB TRAX buffer
- SDIO controller/peripheral 50 MHz
- SD-card interface support

**CircuitPython on ESP32**
Want to learn how to load circuitpython onto this board? check out [this](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/) on the Adafruit learning system
Want to use the supernew web workflow, [this](https://learn.adafruit.com/getting-started-with-web-workflow-using-the-code-editor) tutorial shows you how.

## Purchase

* [Adafruit](https://www.adafruit.com/product/4172)
