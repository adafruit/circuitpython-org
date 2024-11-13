---
layout: download
board_id: "grandcentral_m4_express"
title: "Grand Central M4 Express Download"
name: "Grand Central M4 Express"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4064"
 - "https://www.adafruit.com/product/4084"
board_image: "grandcentral_m4_express.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: grandcentral_m4
download_instructions: https://learn.adafruit.com/adafruit-grand-central/circuitpython
features:
  - Arduino Shield Compatible
---

The **Adafruit Grand Central** features the **Microchip ATSAMD51**. This dev board is so big, it's not named after a Metro train, it's a whole freakin' _station_!

This board is like a freight train, with its 120MHz Cortex M4 with floating point support. Your code will zig and zag and zoom, and with a bunch of extra peripherals for support, this will for sure be your favorite new chipset.

The Grand Central is the first SAMD board that has enough pins to make it in the form of the Arduino Mega - with a massive number of pins, tons of analog inputs, dual DAC output, 8 MBytes of QSPI flash, SD card socket, and a NeoPixel.

To start off our ATSAMD51 journey, it goes large with the Mega shape and pinout you know and love. The front half has the same shape and pinout as an Adafruit Metro, so it is compatible with many shields. It's got analog pins where you expect, and SPI/UART/I2C hardware support in the same spot as the Metro 328 and M0. But! It's powered with an ATSAMD51P20:

*   Cortex M4 core running at **120 MHz**
*   [Floating point support with Cortex M4 DSP instructions](https://developer.arm.com/technologies/dsp/dsp-for-cortex-m)
*   **1MB** flash, **256 KB** RAM
*   32-bit, 3.3V logic and power
*   **70 GPIO pins in total**
*   Dual 1 MSPS DAC (A0 and A1)
*   Dual 1 MSPS ADC (15 analog pins)
*   8 x hardware SERCOM (can be I2C, SPI or UART)
*   22 x PWM outputs
*   Stereo I2S input/output with MCK pin
*   12-bit Parallel capture controller (for camera/video in)
*   Built in crypto engines with AES (256 bit), true RNG, Pubkey controller

Extras:

*   **Power the Grand Central** with 6-12V polarity protected DC or the micro USB connector to any 5V USB source. The 2.1mm DC jack has an on/off switch next to it so you can turn off your setup easily. The board will automagically switch between USB and DC.
*   **Grand Central has 62 GPIO pins**, 16 of which are analog in, and two of which is a true analog out. There's a hardware SPI port, hardware I2C port and hardware UART. 5 more SERCOMs are available for extra I2C/SPI/UARTs.
*   **Logic level is 3.3V**
*   **Native USB**, there's no need for a hardware USB to Serial converter as the Metro M4 has built in USB support. When used to act like a serial device, the USB interface can be used by any computer to listen/send data to the METRO, and can also be used to launch and update code via the bootloader. It can also act like an HID keyboard or mouse.
*   **Four indicator LEDs and one NeoPixel**, on the front edge of the PCB, for easy debugging. One green power LED, two RX/TX LEDs for data being sent over USB, and a red LED connected. Next to the reset button there is an RGB NeoPixel that can be used for any purpose.
*   **8 MB QSPI Flash **storage chip is included on board. You can use the SPI Flash storage like a very tiny hard drive. When used in Circuit Python, the 8 MB flash acts as storage for all your scripts, libraries and files.
*   **Micro SD Card slot** - removable storage of any size, connected to an SPI SERCOM (SDIO is not supported)
*   **Easy reprogramming**, comes pre-loaded with the [UF2 bootloader](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader), which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython (it is bossa v1.8 compatible)

The primary target for this board is CircuitPython - with 120 MHz, and 256KB of RAM CircuitPython runs _really_ well on this chip!

## Tutorial

- [Grand Central M4 Express Overview](https://learn.adafruit.com/adafruit-grand-central)

## Purchase

* [Adafruit](https://www.adafruit.com/product/4064)
