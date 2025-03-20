---
layout: download
board_id: "adafruit_metro_rp2350"
title: "Metro RP2350 Download"
name: "Metro RP2350"
manufacturer: "Adafruit"
board_url:
    - "https://www.adafruit.com/product/6003"
    - "https://www.adafruit.com/product/6267"
board_image: "adafruit_metro_rp2350.jpg"
date_added: 2024-08-08
family: rp2350
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Arduino Shield Compatible
  - External Display
  - USB Host

---

Choo! Choo! This is the RP2350 Metro Line, making all station stops at "Dual Cortex M33 mountain", "520K RAM round-about" and "16 Megabytes of Flash town" and available with a bonus stop at "8 Megabytes of PSRAM village". This train is piled high with hardware that complements the Raspberry Pi RP2350 chip to make it an excellent development board for projects that want Arduino-shape-compatibility or just need the extra space and debugging ports.

* RP2350 main chip, 150MHz clock, 3.3V logic
* 16 MB of QSPI flash for program storage
* Available with 8 MB of QSPI PSRAM for extra dynamic memory
* 24 GPIO, 8 of which are also analog inputs
* Micro SD card socket wired up for SPI interfacing, also has extra pins connected for advanced-user SDIO interfacing (note that there's no released usage code for SDIO in Arduino/Python, so this is a super-cutting-edge setup)
* Onboard RGB NeoPixel
* Onboard #13 LED
* Stemma QT port for I2C peripherals and sensors
* 22-pin 3-lane differential HSTX FPC port with 'Pi 5' compatible pinout
* Reset and Boot buttons on PCB edge
* Pico Probe debug port - 3 pin JST SH compatible
* USB Type C power and data
* 5.5mm / 2.1mm DC jack for 6-12VDC power
* On/off switch for DC jack
* GPIO pin numbers match classic Arduino pins
* RX / TX switch for swapping D0 and D1 locations

You may be wondering about the RX-TX switch: we added this because traditional Arduino board start counting the GPIO for the digital pins with 0-7 and then 8-13. However, the D0/D1 pins are also traditionally the hardware UART Serial1, where D0 is Rx and D1 is Tx. On the RP2350, however, the UART pins are the other around: D0 is Tx and D1 is Rx. Thus a DPDT switch: flip one way to have the GPIO go in order of 0-7, flip the other way to have the logical locations of the hardware UART correct but now the pin order is 1, 0, 2, 3..7. Of course, it's also handy if, like us, you often swap the pins - now you don't need to require or cut/solder traces!

**Inside the RP2350 is a 'permanent ROM' USB UF2 bootloader**. What that means is when you want to program new firmware, you can hold down the BOOTSEL button while plugging it into USB (or pulling down the RUN/Reset pin to ground) and it will appear as a USB disk drive you can drag the firmware onto. Folks who have been using Adafruit products will find this very familiar - we use the technique on all our native-USB boards. Just note you don't double-click reset instead hold down BOOTSEL during boot to enter the bootloader!

**There is great [C/C++ support](https://github.com/raspberrypi/pico-sdk), [unofficial (but really good) Arduino support,](https://learn.adafruit.com/rp2040-arduino-with-the-earlephilhower-core) an official [MicroPython port](https://github.com/micropython/micropython), and a [CircuitPython port](https://circuitpython.org/downloads)!** We of course [recommend CircuitPython because we think it's the easiest way to get started](https://learn.adafruit.com/welcome-to-circuitpython) and it has support with most of our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials.

While the RP2350 has lots of onboard RAM, it does not have built-in FLASH memory. Instead, that is provided by the external QSPI flash chip. **On this board there is 16 MB**, which is shared between the program it's running and any file storage used by MicroPython or CircuitPython. When using C/C++ you get the whole flash memory, if using Python you will have about 14 MB remaining for code, files, images, fonts, etc.

**RP2350 Chip features:**

- Dual ARM Cortex-M33 with floating point unit *or* Dual RISC-V @ 150MHz
- 520 kB on-chip SRAM
- 8 kB of one-time-programmable (OTP) memory.
- Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus
- Support for external QSPI PSRAM
- DMA controller, 16 channel, 4 IRQ
- Fully-connected AHB crossbar
- On-chip switched-mode power supply and programmable low-dropout regulator (LDO) to generate core voltage
- Two on-chip PLLs to generate 48 MHz USB and 150MHz core clocks
- Optional boot signing with protected OTP storage
- Hardware SHA-256 accelerator
- Hardware random number generator (TRNG)
- 48 GPIO pins, 8 of which can be used as analog inputs
- Peripherals
  - 2 UARTs
  - 2 SPI controllers
  - 2 I2C controllers
  - 24 PWM channels (compared to 16 on RP2040)
  - USB 1.1 controller and PHY, with host and device support
  - 12 PIO state machines

## Purchase

* [Adafruit (No PSRAM)](https://www.adafruit.com/product/6003)
* [Adafruit (8MB PSRAM)](https://www.adafruit.com/product/6267)