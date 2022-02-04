---
layout: download
board_id: "adafruit_feather_rp2040"
title: "Feather RP2040 Download"
name: "Feather RP2040"
manufacturer: "Adafruit"
board_url: "https://www.adafruit.com/product/4884"
board_image: "adafruit_feather_rp2040.jpg"
date_added: 2021-1-21
family: raspberrypi
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

A new chip means a new Feather, and the Raspberry Pi RP2040 is no exception. When we saw this chip we thought "this chip is going to be awesome when we give it the Feather Treatment" and so we did! This Feather features the **RP2040**, and all niceties you know and love about Feather
* Measures 2.0" x 0.9" x 0.28" (50.8mm x 22.8mm x 7mm) without headers soldered in
* Light as a (large?) feather - 5 grams
* RP2040 32-bit Cortex M0+ dual core running at ~125 MHz @ 3.3V logic and power
* 264 KB RAM
* **8 MB SPI FLASH** chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
* **Tons of GPIO! 21 x GPIO pins with following capabilities:**
  * **Four** 12 bit ADCs (one more than Pico)
  * Two I2C, Two SPI and two UART peripherals, we label one for the 'main' interface in standard Feather locations
  * 16 x PWM outputs - for servos, LEDs, etc
  * The 8 digital 'non-ADC/non-peripheral' GPIO are consecutive for maximum PIO compatibility
* **Built in 200mA lipoly charger** with charging status indicator LED
* **Pin #13 red LED** for general purpose blinking
* **RGB NeoPixel** with power pin on GPIO so you can depower it for low power usages.
* On-board **STEMMA QT connector** that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
* **Both Reset button and Bootloader select button for quick restarts (no unplugging-replugging to relaunch code)**
* 3.3V Power/enable pin
* [Optional SWD debug port can be soldered in for debug access](https://www.adafruit.com/product/752)
* 4 mounting holes
* 24 MHz crystal for perfect timing.
* 3.3V regulator with 500mA peak current output
* **USB Type C connector** lets you access built-in ROM USB bootloader and serial port debugging


**Inside the RP2040 is a 'permanent ROM' USB UF2 bootloader.** What that means is when you want to program new firmware, you can hold down the BOOTSEL button while plugging it into USB (or pulling down the RUN/Reset pin to ground) and it will appear as a USB disk drive you can drag the firmware onto. Folks who have been using Adafruit products will find this very familiar - we use the technique on all our native-USB boards. Just note you don't double-click reset, instead hold down BOOTSEL during boot to enter the bootloader!


The RP2040 is a powerful chip, which has the clock speed of our M4 (SAMD51), and two cores that are equivalent to our M0 (SAMD1). Since it is an M0 chip, it does not have a floating point unit, or DSP hardware support - so if you're doing something with heavy floating-point math, it will be done in software and thus not as fast as an M4. For many other computational tasks, you'll get close-to-M4 speeds!


For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs that are multiplexed across the GPIO - check the pinout for what pins can be set to which. There are 16 PWM channels, each pin has a channel it can be set to (ditto on the pinout).


You'll note there's no I2S peripheral, or SDIO, or camera, what's up with that? Well instead of having specific hardware support for serial-data-like peripherals like these, the RP2040 comes with the PIO state machine system which is a unique and powerful way to create custom hardware logic and data processing blocks that run on their own without taking up a CPU. For example, NeoPixels - often we bitbang the timing-specific protocol for these LEDs. For the RP2040, we instead use PIO object that reads in the data buffer and clocks out the right bitstream with perfect accuracy. Same with I2S audio in or out, LED matrix displays, 8-bit or SPI based TFTs, even VGA! In MicroPython and CircuitPython you can create PIO control commands to script the peripheral and load it in at runtime. There are 2 PIO peripherals with 4 state machines each.

 There is great [C/C++ support](https://github.com/raspberrypi/pico-sdk), an official [MicroPython port](https://github.com/raspberrypi/micropython), and a [CircuitPython port](/downloads)!** We of course [recommend CircuitPython because we think it's the easiest way to get started](https://learn.adafruit.com/welcome-to-circuitpython) and it has support with most of our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials. **At the time of launch, there is was no Arduino core support for this board. **At the time of launch, there is was no Arduino core support for this board. Earl Philhower has developed an Arduino supported [core](https://github.com/earlephilhower/arduino-pico).

While the RP2040 has lots of onboard RAM (264KB), it does not have built-in FLASH memory. Instead, that is provided by the external QSPI flash chip. **On this board there is 8 MB**, which is shared between the program it's running and any file storage used by MicroPython or CircuitPython. When using C/C++ you get the whole flash memory, if using Python you will have about 7 MB remaining for code, files, images, fonts, etc.

**RP2040 Chip features:**
* Dual ARM Cortex-M0+ @ 133MHz
* 264kB on-chip SRAM in six independent banks
* Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus
* DMA controller
* Fully-connected AHB crossbar
* Interpolator and integer divider peripherals
* On-chip programmable LDO to generate core voltage
* 2 on-chip PLLs to generate USB and core clocks
* 30 GPIO pins, 4 of which can be used as analog inputs
* Peripherals
  * 2 UARTs
  * 2 SPI controllers
  * 2 I2C controllers
  * 16 PWM channels
  * USB 1.1 controller and PHY, with host and device support
  * 8 PIO state machines

Comes fully assembled and tested, with the UF2 USB bootloader. We also toss in some header, so you can solder it in and plug it into a solderless breadboard.

## Purchase

* [Adafruit](https://www.adafruit.com/product/4884)
