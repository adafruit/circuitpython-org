---
layout: download
board_id: "adafruit_qtpy_esp32c3"
title: "Adafruit QT Py ESP32-C3 Download"
name: "Adafruit QT Py ESP32-C3"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5405"
board_image: "adafruit_qtpy_esp32c3.jpg"
date_added: 2022-04-01
family: esp32c3
downloads_display: true
features:
  - STEMMA QT/QWIIC
  - Xiao / QTPy Form Factor
  - USB-C
  - Breadboard-Friendly
  - Wi-Fi
  - Castellated Pads
---

What's life without a little RISC? This miniature dev board is perfect for small projects: it comes with [our favorite connector - the STEMMA QT](http://adafruit.com/stemma), a chainable I2C port, WiFi, Bluetooth LE, and plenty of FLASH and RAM memory for many IoT projects. What a cutie pie! Or is it... a **QT Py**? This diminutive dev board comes with a RISC-V IoT microcontroller, the **ESP32-C3**!

ESP32-C3 is a low-cost microcontroller from Espressif that supports 2.4 GHz Wi-Fi and Bluetooth® Low Energy (Bluetooth LE). It has built-in USB-to-Serial, but *not* native USB - it cannot act as a keyboard or disk drive. The chip used here has 4MB of Flash memory, 400 KB of SRAM and can easily handle TLS connections.

The ESP32-C3 integrates a rich set of peripherals, ranging from UART, I2C, I2S, remote control peripheral, LED PWM controller, general DMA controller, TWAI controller, USB Serial/JTAG controller, temperature sensor, and ADC. It also includes SPI, Dual SPI, and Quad SPI interfaces. There is no DAC or native capacitive touch.

There's a minimum number of pins on this chip, it's specifically designed to be low cost and for simpler projects than ESP32-Sx or ESP32 classics with their large number of GPIO. Think of it more as an intended replacement to the ESP8266 than to the ESP32!

With its state-of-the-art power and RF performance, this SoC is an ideal choice for a wide variety of application scenarios relating to the [Internet of Things (IoT)](https://www.adafruit.com/category/342), [wearable electronics](https://www.adafruit.com/category/65), and smart homes.

**Please note:** The C3 uses **RISC V** as a core, not Tensilica, and has Bluetooth LE (not classic!). The BLE core supports BT version 5 including Mesh

[OLEDs](https://www.adafruit.com/?q=qt+oled&main_page=category&cPath=1005&sort=BestMatch)! [Inertial Measurement Units](https://www.adafruit.com/?q=qt+imu&main_page=category&cPath=1005&sort=BestMatch)! [Sensors a-plenty](https://www.adafruit.com/?q=qt+sensor&main_page=category&cPath=1005&sort=BestMatch). All plug-and-play thanks to the innovative chainable design: [SparkFun Qwiic](https://www.sparkfun.com/qwiic)-compatible [STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt) connectors for the I2C bus so you don't even need to solder! Just plug in a compatible cable and attach it to your MCU of choice, and you’re ready to load up some software and measure some light. [Seeed Grove I2C boards](https://www.adafruit.com/product/4528) will also work with this adapter cable.

Pinout and shape are [Seeed Xiao](https://wiki.seeedstudio.com/Seeeduino-XIAO/) compatible, with castellated pads. In addition to the QT connector, we also added an **RGB NeoPixel**, **a reset button** (great for restarting your program or entering the ROM bootloader), and a button on GPIO 9 for entering the ROM bootloader or for user input

Runs [Arduino with Espressif's ESP32 core](https://github.com/espressif/arduino-esp32) and [you can also run MicroPython on this chipset](https://micropython.org/download/esp32c3-usb/).

- Same size, form-factor, and pin-out as Seeed Xiao
- **USB Type C connector** - [If you have only Micro B cables, this adapter will come in handy](https://www.adafruit.com/product/4299)!
- **ESP32-C3 32­-bit RISC­-V single­ core processor with 4MB of Flash memory, 400 KB of SRAM**
- Built in USB-to-Serial inside the chip, which can also be used for JTAG programming. This peripheral is not native serial, so not for USB HID, MIDI or MSC: it does reduce cost since a separate converter isnt needed
- Can be used with **Arduino IDE** or **MicroPython**
- **Built-in RGB NeoPixel LED** note that due the small number of GPIO, we could not add a NeoPixel power pin
- Battery input pads on underside with diode protection for external battery packs up to 6V input
- 13 GPIO pins:
  - 11 on breakout pads
  - 5 x 12-bit analog inputs on A0 thru A3 and SDA pin
  - PWM outputs on any pin
  - I2C port, on the breakout pads shared with the STEMMA QT plug-n-play connector
  - Hardware UART which is also the hardware serial debug port
  - Hardware SPI
  - Hardware I2S on any pins
- 3.3V regulator with [**600mA peak output**](https://www.diodes.com/assets/Datasheets/AP2112.pdf)
- Light sleep at 500uA***,\*** deep sleep at ~300uA. Lower power deep-sleep is not possible because we don't have an extra GPIO for disabling the NeoPixel power and we didn't want to share that with any of the IO pads. An engineering trade-off!
- **Reset switch** for starting your project code over, boot 9 button for entering bootloader mode
- **Really really small**

## Purchase

* [Adafruit](https://www.adafruit.com/product/5405)

## Getting Started
Since the ESP32C3 chip does not have support for native USB, you won't see a CIRCUITPY drive appear when you plug it into your computer. [Here is a complete guide](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/overview) for getting Circuitpython installed onto an ESP32C3 device, and for enabling [Web Workflow](https://docs.circuitpython.org/en/latest/docs/workflows.html#web) so you can load your Python code onto it.




