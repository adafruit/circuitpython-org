---
layout: download
board_id: "upico"
title: "uPico Download"
name: "uPico"
manufacturer: "Quadbit"
board_url:
 - "https://github.com/dotcypress/upico"
board_image: "upico.jpg"
date_added: 2023-11-29
family: rp2040
features:
---

uPico is a RP2040 powered expansion card designed to enhance the capabilities of [Clockwork's uConsole](https://www.clockworkpi.com/uconsole).
uPico is fully compatible with RaspberryPi Pico, including LED pin(GPIO25).

All sources are open, including:
- PCB design
- Control application code
- Cover bracket 3D model

For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs that are multiplexed across the GPIO - check the pinout for what pins can be set to which. There are 16 PWM channels, each pin has a channel it can be set to (ditto on the pinout).

You'll note there's no I2S peripheral, or SDIO, or camera, what's up with that? Well instead of having specific hardware support for serial-data-like peripherals like these, the RP2040 comes with the PIO state machine system which is a unique and powerful way to create custom hardware logic and data processing blocks that run on their own without taking up a CPU. For example, NeoPixels - often we bitbang the timing-specific protocol for these LEDs. For the RP2040, we instead use a PIO object that reads in the data buffer and clocks out the right bitstream with perfect accuracy. Same with I2S audio in or out, LED matrix displays, 8-bit or SPI based TFTs, even VGA! In MicroPython and CircuitPython you can create PIO control commands to script the peripheral and load it in at runtime. There are 2 PIO peripherals with 4 state machines each.

**There is [great C/C++ support](https://github.com/raspberrypi/pico-sdk), unofficial (but really good) [Arduino support](https://learn.adafruit.com/rp2040-arduino-with-the-earlephilhower-core) an official [MicroPython port](https://micropython.org/download/?mcu=rp2040), and a CircuitPython port!** We of course [recommend CircuitPython because we think its the easiest way to get started](https://learn.adafruit.com/welcome-to-circuitpython) and it has support with most our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials.

While the RP2040 has lots of onboard RAM (264KB), it does not have built in FLASH memory. Instead that is provided by the external QSPI flash chip. On this board there is 2MB, which is shared between the program its running and any file storage used by MicroPython or CircuitPython. When using C/C++ you get the whole flash memory, if using Python you will have about 1 MB remaining for code, files, images, fonts, etc.

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

[Click here for the Raspberry Pi documentation.](https://raspberrypi.org/documentation/pico/getting-started/)
[Click here for Getting Started with Raspberry Pi Pico and CircuitPython.](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)

## Purchase
* [Quadbit](https://www.tindie.com/products/quadbit/upico/)
