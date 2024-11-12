---
layout: download
board_id: "itsybitsy_m4_express"
title: "ItsyBitsy M4 Express Download"
name: "ItsyBitsy M4 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3800"
 - "https://www.adafruit.com/product/4028"
board_image: "itsybitsy_m4_express.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: itsybitsy_m4
download_instructions: https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/circuitpython
features:
  - Breadboard-Friendly
---

What's smaller than a Feather but larger than a Trinket? It's an **Adafruit ItsyBitsy M4 Express** featuring the **Microchip ATSAMD51**! Small, powerful, with a ultra fast ATSAMD51 Cortex M4 processor running at 120 MHz - this microcontroller board is perfect when you want something very compact, with a ton of horsepower and a bunch of pins. This Itsy is like a bullet train, with it's **120MHz Cortex M4** with floating point support and **512KB Flash and 192KB RAM**. Your code will zig and zag and zoom, and with a bunch of extra peripherals for support, this will for sure be your favorite new chipset.

ItsyBitsy M4 Express is only is only 1.4" long by 0.7" wide, but has 6 power pins, 23 digital GPIO pins (7 of which can be analog in, 2 x 1 MSPS analog out DACs, and 18 x PWM out). It's the same chip as the [Adafruit Metro M4](https://www.adafruit.com/product/3382) but _really really small_. So it's great once you've finished up a prototype on a Metro M4 or (the upcoming) Feather M4, and want to make the project much smaller. It even comes with 2MB of SPI Flash built in, for data logging, file storage, or CircuitPython code.

The most exciting part of the ItsyBitsy M4 is that it ships with CircuitPython on board. When you plug it in, it will show up as a very small disk drive with code.py on it. Edit code.py with your favorite text editor to build your project using Python, the most popular programming language. No installs, IDE or compiler needed, so you can use it on any computer, even ChromeBooks or computers you can't install software on. When you're done, unplug the Itsy' and your code will go with you.

Here are some of the updates you can look forward to when using ItsyBitsy M4:

*   Same size, form-factor as the [ItsyBitsy 32u4](https://www.adafruit.com/product/3675) and [ItsyBitsy M0](https://www.adafruit.com/product/3727), and nearly-identical pinout as both
*   **ATSAMD51 32-bit Cortex M4** core running at **120 MHz**
*   [Floating point support with Cortex M4 DSP instructions](https://developer.arm.com/technologies/dsp/dsp-for-cortex-m)
*   **512 KB** flash, **192 KB** RAM
*   **2 MB SPI FLASH chip** for storing files and CircuitPython code storage.
*   32-bit, 3.3V logic and power
*   Tons of GPIO! 23 x GPIO pins with following capabilities:
    *   Dual 1 MSPS 12 bit true analog DAC (A0 and A1) - can be used to play 12-bit stereo audio clips
    *   Dual 1 MSPS 12 bit ADC (7 analog pins some on ADC1 and some on ADC2)
    *   6 x hardware SERCOM - Native hardware SPI, I2C and Serial all available
    *   18 x PWM outputs - for servos, LEDs, etc
    *   No I2S. I2S is only supported on the 64 pin version of this chip. But there's a stereo DAC you could use.
    *   1 x Special **Vhigh** output pin gives you the higher voltage from VBAT or VUSB, for driving NeoPixels, servos, and other 5V-logic devices. **Digital 5** level-shifted output for high-voltage logic level output.
    *   Can drive NeoPixels or DotStars on any pins, with enough memory to drive 60,000+ pixels. [DMA-NeoPixel support on the VHigh pin ](https://learn.adafruit.com/dma-driven-neopixels)so you can drive pixels without having to spend any processor time on it.
*   Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
*   Can be used with Arduino IDE or CircuitPython
*   Built in red pin #13 LED
*   Built in RGB DotStar LED
*   Reset button and pin
*   Power with either USB or external output (such as a battery) - it'll automatically switch over
*   Comes pre-loaded with the [UF2 bootloader](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader), which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython or Arduino IDE (it is bossa v1.8 compatible)

Comes assembled and tested, with headers that can be soldered in for use with a breadboard. ItsyBitsy M4 comes with CircuitPython programmed in.

## Tutorials

* [Overview](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4)

## Purchase

* [Adafruit](https://www.adafruit.com/product/3800)
