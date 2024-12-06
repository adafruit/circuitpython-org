---
layout: download
board_id: "adafruit_metro_rp2040"
title: "Metro RP2040 Download"
name: "Metro RP2040"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5786"
board_image: "adafruit_metro_rp2040.jpg"
date_added: 2023-07-28
family: rp2040
download_instructions: https://learn.adafruit.com/adafruit-metro-rp2040/circuitpython
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Arduino Shield Compatible
---

Choo! Choo! This is the RP2040 Metro Line, making all station stops at "Dual Cortex M0+ mountain", "264K RAM round-about" and "16 Megabytes of Flash town". This train is piled high with hardware that complements the Raspberry Pi RP2040 chip to make it an excellent development board for projects that want Arduino-shape-compatibility or just need the extra space and debugging ports.

- **RP2040 main chip**, 133MHz clock, 3.3V logic
- **16 MB of QSPI flash** for program storage
- **24 GPIO**, 4 of which are also analog inputs
- **Micro SD card socket** wired up for SPI interfacing, also has extra pins connected for advanced-user SDIO interfacing (note that there's no released usage code for SDIO in Arduino/Python, so this is a super-cutting-edge setup)
- Onboard **RGB NeoPixel**
- Onboard **#13 LED**
- **Stemma QT** port for I2C peripherals and sensors
- **Reset and Boot buttons** on PCB edge
- **Pico Probe** debug port - 3 pin JST SH compatible
- **SWD debug** port - 2x5 0.05" standard connector
- **USB Type C** power and data
- 5.5mm / 2.1mm **DC jack** for 6-12VDC power
- **On/off switch** for DC jack
- GPIO pin numbers match classic Arduino pins, other than A4/A5 which are D24 and D25 (there's only 4 ADC pins on the RP2040)
- RX / TX switch for swapping D0 and D1 locations

You may be wondering about the RX-TX switch: we added this because traditional Arduino board start counting the GPIO for the digital pins with 0-7 and then 8-13. However, the D0/D1 pins are also traditionally the hardware UART Serial1, where D0 is Rx and D1 is Tx. On the RP2040, however, the UART pins are the other around: D0 is Tx and D1 is Rx. Thus a DPDT switch: flip one way to have the GPIO go in order of 0-7, flip the other way to have the logical locations of the hardware UART correct but now the pin order is 1, 0, 2, 3..7. Of course, it's also handy if, like us, you often swap the pins - now you don't need to require or cut/solder traces!

### **About the RP2040**

The RP2040 is a powerful chip, which has the clock speed of our M4 (SAMD51), and two cores that are equivalent to our M0 (SAMD21). Since it is an M0 chip, it does not have a floating point unit or DSP hardware support - so if you're doing something with heavy floating-point math, it will be done in software and thus not as fast as an M4. For many other computational tasks, you'll get close-to-M4 speeds!

For peripherals, there are two I2C controllers, two SPI controllers, and two UARTs that are multiplexed across the GPIO - check the pinout for what pins can be set to which. There are 16 PWM channels, each pin has a channel it can be set to (ditto on the pinout).

You'll note there's no I2S peripheral, or SDIO, or camera, what's up with that? Well, instead of having specific hardware support for serial-data-like peripherals like these, the RP2040 comes with the PIO state machine system, which is a unique and powerful way to create *custom hardware logic and data processing blocks* that run on their own without taking up a CPU. For example, NeoPixels - often we bitbang the timing-specific protocol for these LEDs. For the RP2040, we instead use PIO object that reads in the data buffer and clocks out the right bitstream with perfect accuracy. [Same with I2S audio in or out, LED matrix displays, 8-bit or SPI based TFTs, even VGA](https://github.com/raspberrypi/pico-examples/tree/master/pio)! In MicroPython and CircuitPython, you can create PIO control commands to script the peripheral and load it in at runtime. There are 2 PIO peripherals with 4 state machines each.

**There is great [C/C++ support](https://github.com/raspberrypi/pico-sdk), [unofficial (but really good) Arduino support,](https://learn.adafruit.com/rp2040-arduino-with-the-earlephilhower-core) an official [MicroPython port](https://github.com/micropython/micropython), and a [CircuitPython port](https://circuitpython.org/downloads)!** We, of course, [recommend CircuitPython because we think it's the easiest way to get started](https://learn.adafruit.com/welcome-to-circuitpython), and it has support with most of our drivers, displays, sensors, and more, supported out of the box so you can follow along with our CircuitPython projects and tutorials.

While the RP2040 has lots of onboard RAM (264KB), it does not have built-in FLASH memory. Instead, that is provided by the external QSPI flash chip. **On this board, there is 16 MB**, which is shared between the program it's running and any file storage used by MicroPython or CircuitPython. When using C/C++, you get the whole flash memory, if using Python, you will have about 15 MB remaining for code, files, images, fonts, etc.

### **RP2040 Chip features:**

- Dual ARM Cortex-M0+ @ 133MHz
- 264kB on-chip SRAM in six independent banks
- Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus
- DMA controller
- Fully-connected AHB crossbar
- Interpolator and integer divider peripherals
- On-chip programmable LDO to generate core voltage
- 2 on-chip PLLs to generate USB and core clocks
- 30 GPIO pins, 4 of which can be used as analog inputs
- Peripherals
  - 2 UARTs
  - 2 SPI controllers
  - 2 I2C controllers
  - 16 PWM channels
  - USB 1.1 controller and PHY, with host and device support
  - 8 PIO state machines

## Purchase

* [Adafruit](https://www.adafruit.com/product/5786)
