---
layout: download
board_id: "adafruit_trrs_trinkey_m0"
title: "TRRS Trinkey Download"
name: "TRRS Trinkey"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5954"
board_image: "adafruit_trrs_trinkey_m0.jpg"
date_added: 2024-05-14
family: atmel-samd
download_instructions: https://learn.adafruit.com/adafruit-trrs-trinkey/install-circuitpython
features:
---

It's half USB Key, half TRRS breakout*...* it's the **Adafruit TRRS Trinkey** specifically designed for Assistive Technology hackers and creators as a simple and low cost, but also flexible and extendable AT device.

Many AT interface devices use 3.5mm audio jacks to create switches or variable inputs - often mono TS or stereo TRS plugs. On the TRRS Trinkey, we connect all 6 pins of a 'switched' TRRS jack - tip, ring 1, ring 2, sleeve and the tip switch plus ring 1 switch - to 6 GPIO pins on the microcontroller. That means we can not only detect when plugs are inserted but can change which pins are input, ground or even 3V power. With the use of a stereo/mic splitter, we can have up to 3 simple switches, or two analog potentiometers, or one of each! We particularly like this jack because it has two through-hole contacts near the opening for a good mechanical connection.

The PCB is designed to plug into any USB A port on a computer or laptop. There's an ATSAMD21 microcontroller on board with just enough circuitry to keep it happy. One pin of the microcontroller connects to a NeoPixel LED. A reset button lets you enter bootloader mode if necessary. The microcontroller can be programmed easily thanks to the UF2 bootloader and CircuitPython: simply drag-n-drop new code on.

The SAMD21 can run CircuitPython or Arduino nicely. Over the USB connection, you can have serial, MIDI, or HID keyboard/mouse connectivity. Because its a fully programmable chip, it's possible to customize the keyboard or mouse commands executed on each button, or even set up chording patterns.

**Features:**

- **ATSAMD21E18 32-bit Cortex M0+** - 48 MHz 32-bit processor with 256KB Flash and 32 KB RAM
- **Native USB supported by every OS** - can be used in Arduino or CircuitPython as a USB serial console, MIDI, Keyboard/Mouse HID, and even a little disk drive for storing Python scripts. Can act like a keyboard to phones or tablets with a USB adapter cable.
- Can be used with **Arduino IDE** or **CircuitPython**
- **TRRS Jack** with two switches on tip and ring 1. All 6 contacts connect to analog-input capable GPIO pins
- One **RGB NeoPixel LED**
- **STEMMA QT port with JST SH 4-pin compatible connector** - can be used to add I2C devices, or two more inputs. Note CircuitPython may not have enough memory for large chip drivers.
- **Reset switch** to start your project code over or enter bootloader mode
- **Open Source Hardware** so you have full control over your assistive tech!

## Purchase

* [Adafruit](https://www.adafruit.com/product/5954)