---
layout: download
board_id: "adafruit_qt2040_trinkey"
title: "Trinkey QT2040 Download"
name: "Trinkey QT2040"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5056"
board_image: "adafruit_qt2040_trinkey.jpg"
download_instructions: "https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico"
blinka: true
date_added: 2021-12-06
features:
  - STEMMA QT/QWIIC

---

It's half USB Key, half Adafruit QT Py, and a lotta RP2040*...*it's **Trinkey QT2040**, the circuit board with an RP2040 heart and Stemma QT legs. Folks are loving the [QT Py 2040](https://www.adafruit.com/product/4900) we made, but maybe you want something plug-and-play. So we thought, hey what if we made something like that plugs right into your computer's USB port? And this is what we came up with!

The PCB is designed to slip into any USB A port on a computer or laptop. There's an RP2040 microcontroller on board with just enough circuitry to keep it happy. There's an RGB NeoPixel, a reset and bootloader or user button and a STEMMA QT Port on the end. That's it!

With the body of the board being 1.0" x 0.7" and four mounting holes, you can attach just about any of our QT boards right on (some are a little larger so just check that has the holes in the same locations). [Use M2.5 sized standoffs and screws](https://www.adafruit.com/product/3658) to do so, you could use 2 diagonal at a minimum. Then use a [shorty QT cable](https://www.adafruit.com/product/4399) and you've got a custom sensor Trinkey for any sensor purpose.

The board comes with 8 MB of QSPI flash memory so you can put *all* of our CircuitPython drivers on the disk!

## Technical details

* Main body is same size/mounting holes as most of our Stemma QT boards (1.0" x 0.7" with M2.5 holes)
* USB Type A connector with extra-thick PCB to fit into a USB host port
* RP2040 32-bit Cortex M0+ dual-core running at ~125 MHz @ 3.3 V logic and power
* 264 KB RAM
* 8 MB SPI FLASH chip for storing files and CircuitPython/MicroPython code storage. No EEPROM
* Native USB supported by every OS - can be used as USB serial console, MIDI, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
* Built-in RGB NeoPixel LED
* STEMMA QT/Qwiic port for I2C connectivity
* 3.3 V regulator with 600 mA peak output
* 12 MHz crystal
* Both Reset button and Bootloader select buttons for quick restarts (no unplugging-replugging to relaunch code)
* Bootloader button can also be safely used in 'user' code

## Purchase

* [Adafruit](https://www.adafruit.com/product/5056)
