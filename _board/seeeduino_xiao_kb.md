---
layout: download
board_id: "seeeduino_xiao_kb"
title: "Seeeduino XIAO Download"
name: "Seeeduino XIAO - Keyboard Optimized"
manufacturer: "Seeed Studio"
board_url:
 - "https://wiki.seeedstudio.com/Seeeduino-XIAO/"
board_image: "seeeduino_xiao.jpg"
date_added: 2021-10-08
family: atmel-samd
download_instructions: https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/
bootloader_id: XIAO_m0

features:
  - USB-C
  - Breadboard-Friendly
  - Xiao / QTPy Form Factor
  - Castellated Pads
---

# Keyboard Optimized

Due to the limited memory and flash of the ATSAMD21G18, an optimized build of CircuitPython is needed for keyboard/keypad/macropad projects.  The following modules are made available:

* **keypad** for handing buttons and key matrices
* **rotaryio** for handling rotary encoders
* **usb_hid** for sending HID messages to the computer
* **adafruit_hid** (frozen module) for configuring your Xiao as a keyboard

Note that a number of modules are removed to make space for those listed above. It is assumed that a keyboard or macropad doesn't have sensors. As such, these modules are **not** included:

* **busio** needed for I2C, SPI and UART
* **pulseio** needed some sensors
* **onewireio** needed for 1-wire devices

If you need one of the modules removed or if you want to absolutely be sure that you don't run out of memory, consider using a better processor (RP2040 for example).

This build was tested with a 30 keys macropad which is the largest matrix the XIAO allows for (5x6 matrix = 11 GPIOs).

# Seeduino XIAO

SEEED Studio's Seeeduino XIAO is a minimal, low-cost board that uses the Atmel c, a powerful 32-bit ARM Cortex®-M0+ processor running at 48 MHz with 256 KB Flash and 32 KB SRAM. The board is 20 mm x 17.5 mm in size which is perfect for wearable devices and small projects. It has multiple interfaces including DAC output, SWD Bonding pad interface, I2C, UART and SPI interfaces. It's compatible with both Arduino IDE and CircuitPython and uses a USB-C connector.

## Technical details

* CPU: ARM Cortex-M0+ CPU (SAMD21G18) running at up to 48 MHz
* Flash Memory: 256 KB
* SRAM: 32 KB
* Digital I/O pins: 11
* Analog I/O pins: 11
* I2C interfaces: 1
* SPI interfaces: 1
* UART interfaces: 1
* USB-C connector for transferring code and power
* Power requirements: 3.3 V/5 V DC
* Dimensions: 20 mm x 17.5 mm x 3.5 mm

Note: This microcontroller runs at 3.3 V logic. Using a 5 V device may damage the chip or device.

For power supply pins: The built-in DC-DC converter circuit is able to change 5 V voltage into 3.3 V, which allows you to power the device with a 5 V supply via the VIN pin or 5V pin.

## Purchase

* [Seeed Studio](https://www.seeedstudio.com/Seeeduino-XIAO-Arduino-Microcontroller-SAMD21-Cortex-M0+-p-4426.html)
* [Digi-Key](https://www.digikey.com/en/product-highlight/s/seeed/seeeduino-xiao-arduino-microcontroller-samd21-cortex-m0)
* [Mouser](https://www.mouser.com/ProductDetail/Seeed-Studio/102010328?qs=GBLSl2AkirtQWO8CTzEK9g%3D%3D)
