---
layout: download
board_id: "raspberry_pi_pico"
title: "Pico Download"
name: "Pico"
manufacturer: "Raspberry Pi"
board_url:
 - "https://www.adafruit.com/product/4883"
board_image: "raspberry_pi_pico.jpg"
download_instructions: "https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico"
downloads_display: true
blinka: true
date_added: 2021-05-20
---

The Raspberry Pi foundation changed single-board computing when they released the Raspberry Pi computer, now they're ready to do the same for microcontrollers with the release of the brand new **Raspberry Pi Pico**. This low-cost microcontroller board features a powerful new chip, the **RP2040**, and all the fixin's to get started with embedded electronics projects at a stress-free price.

The Pico is 0.825" x 2" and can have headers soldered in for use in a breadboard or perfboard, or can be soldered directly onto a PCB with the castellated pads. There's 20 pads on each side, with groups of general purpose input-and-output (GPIO) pins interleaved with plenty of ground pins. All of the GPIO pins are 3.3V logic, and are not 5V-safe so stick to 3V! You get a total of 25 GPIO pins (technically there are 26 but IO #15 has a special purpose and should not be used by projects), 3 of those can be analog inputs (the chip has 4 ADC but one is not broken out). There are no true analog output (DAC) pins.

On the slim green board is minimal circuitry to get you going: A 5V to 3.3V power supply converter, single green LED on GP25, boot select button, RP2040 chip with dual-core Cortex M0, 2 MegaBytes of QSPI flash storage, and crystal.

**Inside the RP2040 is a 'permanent ROM' USB UF2 bootloader.** What that means is when you want to program new firmware, you can hold down the BOOTSEL button while plugging it into USB (or pulling down the RUN/Reset pin to ground) and it will appear as a USB disk drive you can drag the firmware onto. Folks who have been using Adafruit products will find this very familiar - we use the technique all our native-USB boards. Just note you don't double-click reset, instead hold down BOOTSEL during boot to enter the bootloader!

The RP2040 is a powerful chip, which has the clock speed of our M4 (SAMD51), and two cores that are equivalent to our M0 (SAMD21). Since it is an M0 chip, it does not have a floating point unit, or DSP hardware support - so if you're doing something with heavy floating point math, it will be done in software and thus not as fast as an M4. For many other computational tasks, you'll get close-to-M4 speeds!

For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs that are multiplexed across the GPIO - check the pinout for what pins can be set to which. There are 16 PWM channels, each pin has a channel it can be set to (ditto on the pinout).

You'll note there's no I2S peripheral, or SDIO, or camera, what's up with that? Well instead of having specific hardware support for serial-data-like peripherals like these, the RP2040 comes with the PIO state machine system which is a unique and powerful way to create custom hardware logic and data processing blocks that run on their own without taking up a CPU. For example, NeoPixels - often we bitbang the timing-specific protocol for these LEDs. For the RP2040, we instead use a PIO object that reads in the data buffer and clocks out the right bitstream with perfect accuracy. Same with I2S audio in or out, LED matrix displays, 8-bit or SPI based TFTs, even VGA! In MicroPython and CircuitPython you can create PIO control commands to script the peripheral and load it in at runtime. There are 2 PIO peripherals with 4 state machines each.

**At the time of launch, there is no Arduino core support for this board. There is [great C/C++ support](https://github.com/raspberrypi/pico-sdk), an official [MicroPython port](https://github.com/raspberrypi/micropython), and a CircuitPython port!** We of course [recommend CircuitPython because we think its the easiest way to get started](https://learn.adafruit.com/welcome-to-circuitpython) and it has support with most our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials.

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
[Click here for CircuitPython Libraries on MicroPython using the Raspberry Pi Pico.](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico)
[Click here for CircuitPython Libraries on any Computer with Raspberry Pi Pico.](https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico)

## Purchase
* [Adafruit](https://www.adafruit.com/product/4883)
