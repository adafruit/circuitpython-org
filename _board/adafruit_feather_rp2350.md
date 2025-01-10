---
layout: download
board_id: "adafruit_feather_rp2350"
title: "Feather RP2350 Download"
name: "Feather RP2350"
manufacturer: "Adafruit"
board_url:
    - "https://www.adafruit.com/product/6000"
board_image: "adafruit_feather_rp2350.jpg"
date_added: 2024-08-08
family: rp2350
download_instructions: https://learn.adafruit.com/adafruit-feather-rp2350/install-circuitpython-2
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly

---

RP2350 flies high with the Feather format - now you can use any FeatherWings with this battery-powered dev board. It comes with 8MB of flash, 22pin HSTX output port, Stemma QT, debug SWD, and optional PSRAM spot. It's our first RP2350 board and we crammed a ton of goodies into our classic Feather format. It's an excellent starter board to go along with your Pico 2.

The RP2350 is Raspberry Pi's second microcontroller chip following their breakout-hit the RP2040. Building on their success, the RP2350 upgrades the dual M0 core to dual M33 cores with 150 MHz clock rate. The M33 is a much newer Arm chipset, we've found that firmware runs about twice as fast. Especially given that we now have hardware floating point support. Also, the RP2350 has twice as much SRAM: 520KB instead of 264KB which means that micropython/circuitpython runs great and also IoT projects that need a lot of memory buffer space will run better. Other improvements include, 3 PIO blocks instead of 2, TrustZone secure boot, and a special High Speed Transmit (HSTX) peripheral that drives 4 lanes of differential data transmission such as DVI output without needing to overclock or use PIO.

For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs that are multiplexed across the GPIO - check the pinout for what pins can be set to which. There are 24 PWM channels, each pin has a channel it can be set to (ditto on the pinout).

Feather RP2350 HSTX Specifications:

* Measures 2.0" x 0.9" x 0.28" (50.8mm x 22.8mm x 7mm) without headers soldered in
* Light as a (large?) feather - 5 grams
* RP2350 32-bit Cortex M33 dual core running at 150 MHz @ 3.3V logic and power
* 520 KB RAM + 8 KB OTP memory
* 8 MB SPI FLASH chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
* Optional spot for SOIC PSRAM chip with chip select line on GPIO 8
* Tons of GPIO! 29 x GPIO pins with following capabilities:
	* 21 GPIO available on the Feather header pins, 8 more 'consecutive' GPIO available on the HSTX connector (you don't have to use them with the HSTX peripheral) 
	* Four 12-bit ADCs (one more than Pico 2)
	* Two I2C, Two SPI, and two UART peripherals, we label one for the 'main' interface in standard Feather locations
	* 24 x PWM outputs - for servos, LEDs, etc
* Built-in 200mA+ lipoly charger with charging status indicator LED. For non-rechargeable battery usage the charger can be disabled by cutting a jumper trace on the back.
* Pin #7 red LED for general purpose blinking
* RGB NeoPixel for full-color indication.
* On-board STEMMA QT connector that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
* Both Reset button and Bootloader select button for quick restarts (no unplugging-replugging to relaunch code)
* 3.3V Power/enable pin
* Pico Probe 3-pin JST SH connector for SWD debugging
* 4 mounting holes
* 12 MHz crystal for perfect timing.
* 3.3V regulator with 500mA peak current output
* USB Type C connector lets you access built-in ROM USB bootloader and serial port debugging

Inside the RP2350 is a 'permanent ROM' USB UF2 bootloader. What that means is when you want to program new firmware, you can hold down the BOOTSEL button while plugging it into USB (or pulling down the RUN/Reset pin to ground) and it will appear as a USB disk drive you can drag the firmware onto. Folks who have been using Adafruit products will find this very familiar - we use the technique on all our native-USB boards. Just note you don't double-click reset instead hold down BOOTSEL during boot to enter the bootloader!

There is great C/C++ support, unofficial (but really good) Arduino support, an official MicroPython port, and a CircuitPython port! We of course recommend CircuitPython because we think it's the easiest way to get started and it has support with most of our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials.

While the RP2350 has lots of onboard RAM, it does not have built-in FLASH memory. Instead, that is provided by the external QSPI flash chip. On this board there is 8 MB, which is shared between the program it's running and any file storage used by MicroPython or CircuitPython. When using C/C++ you get the whole flash memory, if using Python you will have about 7 MB remaining for code, files, images, fonts, etc.

RP2350 Chip features:

* Dual ARM Cortex-M33 with floating point unit or Dual RISC-V @ 150MHz
* 520 kB on-chip SRAM
* 8 kB of one-time-programmable (OTP) memory.
* Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus
* Support for external QSPI PSRAM
* DMA controller, 16 channel, 4 IRQ
* Fully-connected AHB crossbar
* On-chip switched-mode power supply and programmable low-dropout regulator (LDO) to generate core voltage
* Two on-chip PLLs to generate 48 MHz USB and 150MHz core clocks
* Optional boot signing with protected OTP storage
* Hardware SHA-256 accelerator
* Hardware random number generator (TRNG)
* 30 GPIO pins, 4 of which can be used as analog inputs
* Peripherals
	* 2 UARTs
	* 2 SPI controllers
	* 2 I2C controllers
	* 24 PWM channels (compared to 16 on RP2040)
	* USB 1.1 controller and PHY, with host and device support
	* 12 PIO state machines

Please note: The Adafruit Feather RP2350 HSTX comes with the A2 version of the RP2350, which is affected by the E9 erratum. This errata affects some uses of GPIO and PIO such as high-impedance inputs and the internal pulldowns. You may need to use 8.2K or smaller resistors if pull-downs are required. At this time, Sept 9 2024, there is no other version of the RP2350 available - only the A2 version.
