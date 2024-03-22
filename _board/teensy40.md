---
layout: download
board_id: "teensy40"
title: "Teensy 4.0 Download"
name: "Teensy 4.0"
manufacturer: "PJRC"
board_url:
 - "https://www.pjrc.com/store/teensy40.html"
 - "https://www.adafruit.com/product/4323"
board_image: "teensy40.jpg"
date_added: 2020-01-31
family: mimxrt10xx
features:
  - Breadboard-Friendly
---
Who else could pack a 600 MHz microcontroller into such a Teensy little board? The Teensy 4.0 features an ARM Cortex-M7 processor at 600 MHz, with a NXP iMXRT1062 chip, the fastest microcontroller available today - [ten times faster than the Teensy 3.2](https://github.com/PaulStoffregen/CoreMark)! The NXP iMXRT1062 is a 'cross-over' processor, which has the functionality of a microcontroller, at the speeds of a microcomputer. It's perfect for when you need tons of flash, RAM and, to crunch lots of data, or when you need two full speed USB ports. It even has a graphics processor! All this for two sawbucks.

Teensy 4.0 can be programmed using the Arduino IDE with [Teensyduino add-on](https://www.pjrc.com/teensy/td_download.html).

**Power Consumption & Management**
When running at 600 MHz, Teensy 4.0 consumes approximately 100 mA current, considerably more than most microcontrollers. To help reduce power, Teensy 4.0 provides support for dynamic clock scaling. Unlike traditional microcontrollers, where changing the clock speed causes wrong baud rates and other issues, Teensy 4.0 hardware and Teensyduino's software support for Arduino timing functions are designed to allow dynamically speed changes. Serial baud rates, audio streaming sample rates, and Arduino functions like delay() and millis(), and Teensyduino's extensions like IntervalTimer and elapsedMillis, continue to work properly while the CPU changes speed.

Teensy 4.0 also provides a power shut off feature. By connecting a pushbutton to the On/Off pin, the 3.3V power supply can be completely disabled by holding the button for 5 seconds, and turned back on by a brief button press. If a coin cell is connected to VBAT, Teensy 4.0's RTC also continues to keep track of date & time while the power is off.

Teensy 4.0 also can also be overclocked, well beyond 600 MHz!

**Technical Specifications**
 - ARM Cortex-M7 at 600 MHz
 - 1024K RAM (512K is tightly coupled)
 - 2048K Flash (64K reserved for recovery & EEPROM emulation)
 - 2 USB ports, both 480 MBit/sec
 - 3 CAN Bus (1 with CAN FD)
 - 2 I2S Digital Audio
 - 1 S/PDIF Digital Audio
 - 1 SDIO (4 bit) native SD
 - 3 SPI, all with 16 word FIFO
 - 3 I2C, all with 4 byte FIFO
 - 7 Serial, all with 4 byte FIFO
 - 32 general purpose DMA channels
 - 31 PWM pins
 - 40 digital pins, all interrrupt capable
 - 14 analog pins, 2 ADCs on chip
 - Cryptographic Acceleration
 - Random Number Generator
 - RTC for date/time
 - Programmable FlexIO
 - Pixel Processing Pipeline
 - Peripheral cross triggering
 - Power On/Off management

## Purchase
* [Adafruit](https://www.adafruit.com/product/4323)
