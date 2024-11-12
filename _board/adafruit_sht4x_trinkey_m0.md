---
layout: download
board_id: "adafruit_sht4x_trinkey_m0"
title: "Temp and Humidity Trinkey Download"
name: "Temp and Humidity Trinkey"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5896"
 - "https://www.adafruit.com/product/5912"
board_image: "adafruit_sht4x_trinkey_m0.jpg"
date_added: 2024-03-13
family: atmel-samd
download_instructions: https://learn.adafruit.com/adafruit-sht4x-trinkey/install-circuitpython
features:

---

It's half USB Key, half temperature-humidity sensor*...* it's the **Adafruit SHT41 and SHT45 Trinkey** boards. We wanted to make it super-easy to add one of our most popular combination environmental sensors to any computer with a USB A port.

The PCB is designed to slip into any USB A port on a computer or laptop. There's an ATSAMD21 microcontroller on board with just enough circuitry to keep it happy. One pin of the microcontroller connects to a NeoPixel LED. Another pin is used as a capacitive touch input on the end. A reset button lets you enter bootloader mode if necessary. That's it!

The SAMD21 can run CircuitPython or Arduino nicely - both have existing SHT4x, NeoPixel, and our FreeTouch (capacitive touch) libraries. Over the USB connection, you can have serial, MIDI, or HID connectivity.

The SHT41 sensor is the fourth generation of I2C temperature and humidity sensor from Sensirion. (They started at the SHT10 and reached the top!). The **SHT41 has an excellent ±1.8% typical relative humidity accuracy from 25 to 75% and ±0.2 °C typical accuracy from 0 to 75 °C.** The reported temperature may be a few degrees higher than ambient due to self-heating.

The **SHT45** sensor is the fourth generation (started at the SHT10 and worked its way up to the top!). **The SHT45 has an excellent ±1.0% typical relative humidity accuracy from 25 to 75% and ±0.1°C typical accuracy from 0 to 75 °C**. The reported temperature may be a few degrees higher than ambient due to self-heating.

The SHT41 or SHT45 Trinkey is perfect for simple projects that want to read the ambient temperature and humidity without extra wiring, soldering, drivers, or complex software. We even ship the board pre-programmed with code that will print a unique serial number, the temperature, humidity, and touch sensor over a serial/COM port in CSV (comma-separated value) format so you can use it immediately. [If you need to measure farther than the computer port, simply use any USB A extension cable](https://www.adafruit.com/product/993).

[If you don't need high precision, save a few $ with the SHT41 Trinkey](https://www.adafruit.com/product/5912), which has ±1.8% typical relative humidity accuracy from 25 to 75% and ±0.2°C typical accuracy from 0 to 75 °C.

We think it's just an adorable little board. It's small, durable, and inexpensive enough to be a first microcontroller board or an inspiration for advanced developers to make something simple and fun.

- ATSAMD21E18 32-bit Cortex M0+ - 48 MHz 32-bit processor with 256KB Flash and 32 KB RAM
- Native USB supported by every OS - can be used in Arduino or CircuitPython as a USB serial console, MIDI, Keyboard/Mouse HID, and even a little disk drive for storing Python scripts.
- Can be used with Arduino IDE or CircuitPython
- One RGB NeoPixel LED
- One Capacitive Touchpad
- SHT41 or SHT45 Temperature + Humidity sensor with thermal-isolation cutout
- Reset switch **to start** your project code over or enter bootloader mode
- Slim and cute, keychain-friendly!

## Purchase

* [Adafruit SHT41 Trinkey](https://www.adafruit.com/product/5912)
* [Adafruit SHT45 Trinkey](https://www.adafruit.com/product/5896)