---
layout: download
board_id: "metro_m4_airlift_lite"
title: " Metro M4 AirLift Lite Download"
name: "Metro M4 AirLift Lite"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4000"
board_image: "metro_m4_airlift_lite.jpg"
date_added: 2019-04-13
family: atmel-samd
bootloader_id: metro_m4_airlift
download_instructions: https://learn.adafruit.com/adafruit-metro-m4-express-airlift-wifi/install-circuitpython
features:
  - Wi-Fi
  - Arduino Shield Compatible
---

Give your next project a lift with _AirLift_ - Adafruit's witty name for the ESP32 co-processor that graces this Metro M4.

You already know about the **Adafruit Metro M4** featuring the **Microchip ATSAMD51**, with it's 120 MHz Cortex M4 with floating point support. With a train-load of FLASH and RAM, your code will be fast and roomy. And what better way to improve it than to add wireless? Now cooked in directly on board, you get a certified WiFi module that can handle all your TLS and socket needs, it even has root certificates pre-loaded.

This Metro is the same size as the others, and is compatible with all our shields. It's got analog pins where you expect, and SPI/UART/I2C hardware support in the same spot as the Metro 328 and M0\. But! It's powered with an ATSAMD51J19.

## Technical details

* Cortex M4 core running at **120 MHz**
* [Floating point support with Cortex M4 DSP instructions](https://developer.arm.com/technologies/dsp/dsp-for-cortex-m)
* **512 KB** flash, **192 KB** RAM
* 32-bit, 3.3V logic and power
* Dual 1 MSPS DAC (A0 and A1)
* Dual 1 MSPS ADC (8 analog pins)
* 6x hardware SERCOM (I2C, SPI or UART)
* 22x PWM outputs
* Stereo I2S input/output with MCK pin
* 10-bit Parallel capture controller (for camera/video in)
* Built in crypto engines with AES (256 bit), true RNG, Pubkey controller
* 64 QFN

The PCB comes with all these extras:

* **Power the METRO M4** with 7-9 V polarity protected DC or the micro USB connector to any 5 V USB source. The 2.1 mm DC jack has an on/off switch next to it so you can turn off your setup easily. The METRO will automagically switch between USB and DC.
* **METRO has 25 GPIO pins**, 8 of which are analog in, and two of which is a true analog out. There's a hardware SPI port, hardware I2C port and hardware UART. Logic level is 3.3 V.
* **Native USB**, there's no need for a hardware USB to Serial converter as the Metro M4 has built in USB support. When used to act like a serial device, the USB interface can be used by any computer to listen/send data to the METRO, and can also be used to launch and update code via the bootloader. It can also act like an HID keyboard or mouse.
* **AirLift WiFi Co-processor**, with TLS/SSL support, plenty of RAM for sockets, communication is over SPI and has Arduino and CircuitPython libraries ready to go for fast wireless integration.
* **Four indicator LEDs and one NeoPixel**, on the back edge of the PCB, for easy debugging. One green power LED, two RX/TX LEDs for data being sent over USB, and a red LED connected. Next to the reset button there is an RGB NeoPixel that can be used for any purpose.
* **2 MB QSPI Flash** storage chip is included on board. You can use the SPI Flash storage like a very tiny hard drive. When used in Circuit Python, the 2 MB flash acts as storage for all your scripts, libraries and files. When used in Arduino, you can read/write files to it, like a little datalogger or SD card, and then with our helper program, access the files over USB.
* **Easy reprogramming**, comes pre-loaded with the [UF2 bootloader](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader), which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython (it is bossa v1.8 compatible).

The primary target for this board is CircuitPython - with 120 MHz, and 192 KB of RAM CircuitPython runs really well on this chip! CircuitPython's built in support for JSON parsing plus our _requests_ compatible library makes it incredibly easy to build secure IoT projects in just a few minutes.

Metro M4 AirLift, see how easy and fast it is to get started with IoT projects using CircuitPython!

## Tutorial

- [Metro M4 AirLift Lite Overview](https://learn.adafruit.com/adafruit-metro-m4-express-airlift-wifi)

## Purchase

* [Adafruit](https://www.adafruit.com/product/4000)
