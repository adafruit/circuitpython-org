---
layout: download
board_id: "uchip"
title: "uChip Download"
name: "uChip M0"
manufacturer: "Itaca Innovation"
board_url:
 - "https://shop.itaca-innovation.com"
board_image: "uchip.jpg"
date_added: 2019-03-25
family: atmel-samd
bootloader_id: uchip
features:
  - Breadboard-Friendly
---

**Small. Yet powerful!**

Despite a size smaller than the ATMEGA328 which powers Arduino Uno, **uChip** mounts the same ATSAMD21 series of Arduino Zero! Everything that runs on Arduino Zero runs also on uChip, at the same speed! However, unlike Arduino Zero, it **fits a 16-pin DIP socket** and it leaves a lot of space on your breadboard. No more bulky shields or flying wires all around your breadboard!

And now uChip runs CircuitPython too!

Unlike many Arduino Zero compatible board, uChip also mounts a high efficiency buck converter, which converts the USB voltage down to 3.3V at up to 1A, which is provided on pin 16, for the external circuitry. A software-selected pass-through mode also allows to output 5V instead of 3.3V.
uChip can operate also as an USB host. For this purpose, a built-in boost converter can provide up to 500mA to the external USB device, even when the input voltage is as low as 3.3V. The built-in automatic power-path management prevents external power from being fed into an USB port, when uChip is connected to a PC/Mac, and a voltage is provided also externally on pin 16.

You can program uChip using virtually any IDE, in many languages (CircuitPython too!) and you can choose of using either the USB port or an external SWD programmer.

**uChip Features:**

* CPU: 32-bit Cortex M0+ ATSAMD21-series running at 48 MHz (Arduino Zero Compatible)
* FLASH: 256 kB (248 kB due to integrated bootloader).
* RAM: 32 kB, zero wait states.
* Powered via USB or externally (3.3V to 5V).
* Integrated 500-mA boost and 1-A buck converters and automatic power switching circuitry.
* Each converter can also be individually turned off, e.g. if you want to force power draw exclusively from external pins (self-powered device), or if you want to turn off an external USB device connected with a micro A cable.
* When powered through the USB port, the output voltage on the power pins can be selected via software to be either 3.3V or the USB voltage (typically 5V +/- 10%).
* Pin 15 can be configured (via SMD jumper) as an additional 3.3V auxiliary output @100mA when pin 16 is 5V (either as input or output). By default pin 15 is a regular I/O. If this feature is not used, 5/3.3V (at up to 1A) are still available on pin 16.
* 14 I/O pins (2 of them can be used to connect an external SWD programmer/debugger) and 2 power pins (VCC and GND).
* Status LED (it can be turned on/off via software using a single instruction).
* Multi function push button for reset/program.
* 8 12-bit ADC inputs.
* 10-bit DAC output.
* 14 external interrupt input pins.
* Up to 5 serials between SPI, I2C and UART.
* I2S port for audio decoders such as  UDA1334A.
* 13 PWM pins.
* Size: 28.5 mm x 10.16 mm (1.1 “ x 0.40 “), including USB port protrusions (27.23 mm x 10.16 mm excluding USB)
* 4-layer board for improved noise performance.
* Standards narrow-DIP footprint: 0.3” (7.62 mm) row spacing, 0.1” (2.54) pin spacing.
* Pinout standard logic CMOS compatible: power and GND are on pin 16 and 8, so you can also emulate some 16 pin CMOS ICs (4000 and 74HC series)!

**Additional Notes:**

* The uChip does not have an RGB LED.
* The on-board LED is amber, rather than green.
* The board's bootloader is BOSSA-compatible, but does not support UF2, so use a CircuitPython .bin file with BOSSA.  See [this page](https://learn.adafruit.com/welcome-to-circuitpython/non-uf2-installation) for the general process of using BOSSA.  A Windows .bat script that demonstrates exactly how to use the BOSSAC commandline tool with uChip to flash CircuitPython is available [here](https://github.com/mew-cx/circuitpython_stuff/tree/main/uChip); you may use it as a template and customize as needed.

## Purchase

* [Itaca Innovation Store](https://shop.itaca-innovation.com)
