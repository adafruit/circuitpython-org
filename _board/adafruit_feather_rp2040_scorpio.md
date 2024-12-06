---
layout: download
board_id: "adafruit_feather_rp2040_scorpio"
title: "Feather RP2040 SCORPIO Download"
name: "Feather RP2040 SCORPIO"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5650"
board_image: "adafruit_feather_rp2040_scorpio.jpg"
date_added: 2022-12-23
family: rp2040
download_instructions: https://learn.adafruit.com/introducing-feather-rp2040-scorpio/install-circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

If there is one thing Adafruit is known for, its mega-blinky-fun-rainbow-LEDs. [We just love sticking NeoPixels anywhere and everywhere](https://www.adafruit.com/category/168). When we saw the new 'PIO' peripheral on[ the RP2040 from Raspberry Pi](https://www.adafruit.com/category/875), we just knew it would be perfect for driving large quantities of NeoPixels. So we created this board, the **Adafruit Feather RP2040 SCORPIO**, designed specifically for NeoPixel (WS2812) driving but also good for various other PIO-based projects that want to take advantage of the Feather pinout with 8 separate consecutive outputs (or inputs).

[The RP2040 PIO state machine](https://learn.adafruit.com/intro-to-rp2040-pio-with-circuitpython) is perfect for LED driving: it can generate perfect waveforms, with up to 8 outputs concurrently, all through DMA. That means that you don't need to use any processor time to bit-bang-out the LED data. Just set up the buffer and tell the PIO peripheral to 'make it so' and it will shove that data to the 8 outputs without delay while your code can continue to read buttons, play music, run CircuitPython - whatever you like!

The SCORPIO has a clever pinout, where all the standard Feather pins are the same as the GPIO pins, plus the standard I2C, SPI and UART lines - and theres *still* enough pins left over to have 8 consecutive pins for PIO usage on GPIO16 through GPIO23 inclusive.

To make NeoPixel usage glitch-free there is a 3V->5V level shifter so that the output logic is 5V. If you happen to want 3V signals, you can adjust the shifter voltage with a jumper on the bottom. It's also possible to flip the direction of the level shifter to make the 8 I/O pins inputs - say for making a logic analyzer - with a directional jumper selection also on the bottom of the PCB.

The RP2040 SCORPIO also has a *ton* of RAM, 264KB, making it trivial to buffer huge numbers of NeoPixels…*several thousand* if needed. In fact there's so much RAM you can even *dither* the pixels to for finer brightness control, for better-looking LEDs at low brightness or for gamma correction.

We have [NeoPXL8 driver code available in Arduino](https://github.com/adafruit/Adafruit_NeoPXL8) and [CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_NeoPxl8), so you can jump immediately to making beautiful artworks driven by the Adafruit SCORPIO.

- Measures 2.0" x 0.9" x 0.28" (50.8mm x 22.8mm x 7mm) without headers soldered in
- Light as a (large?) feather - 5 grams
- RP2040 32-bit Cortex M0+ dual core running at ~125 MHz @ 3.3V logic and power
- 264 KB RAM
- **8 MB SPI FLASH** chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
- Tons of GPIO! 21 x GPIO pins with following capabilities:
  - **Four** 12-bit ADCs (one more than Pico)
  - Two I2C, Two SPI, and two UART peripherals, we label one for the 'main' interface in standard Feather locations
  - 16 x PWM outputs - for servos, LEDs, etc
  - 8 x consecutive GPIO outputs with 5V level shifting for PIO NeoPixel driving
- **Built-in 200mA+ lipoly charger** with charging status indicator LED
- **Pin #13 red LED** for general purpose blinking
- **RGB NeoPixel** for full-color indication on **D4**
- On-board **STEMMA QT connector** that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
- **Both Reset button and Bootloader select button for quick restarts** (no unplugging-replugging to relaunch code). Bootloader button is also available as user-input button on GPIO #7
- 3.3V Power/enable pin
- 4 mounting holes
- 12 MHz crystal for perfect timing.
- 3.3V regulator with 500mA peak current output
- **USB Type C connector** lets you access built-in ROM USB bootloader and serial port debugging

## Purchase

* [Adafruit](https://www.adafruit.com/product/5650)
