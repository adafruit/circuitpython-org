---
layout: download
board_id: "jpconstantineau_pykey60"
title: "PyKey 60% Keyboard Download"
name: "PyKey60 Keyboard"
manufacturer: "JPConstantineau"
board_url: "https://github.com/jpconstantineau/PyKey60"
board_image: "jpconstantineau_pykey60.jpg"
date_added: 2021-09-17

features:
  - USB-C
  - Speaker
---

The PyKey60 is a custom programmable mechanical keyboard with a standard ANSI 60% keyboard layout compatible with any cases made for the GH60. The PyKey60 uses mechanical switches (Cherry MX type). The keys are hot-swap socketed and have an individual underglow RGB LED which can be turned on.  The PCB was designed for use with PCB-mount stabilizers.

Since this is a Hot Swappable Switches keyboard, you can choose the MX switches as well as the keycaps you prefer.  You can even mix and match switches for the ultimate customization.

Just like CircuitPython, this keyboard is targeted for beginners.  The design keeps the matrix definition simple to 14 columns and 5 rows instead of using a GPIO-optimized matrix of 8 columns and 8 rows.  Neopixel order is also in line with key numbers.  This keeps the complexity of coding a keyboard firmware to a minimum.

## Features
* Powered by RP2040
* Per key RGB LEDs (NeoPixels)
* Kailh hot-swap switch sockets (for Cherry MX-compatible switches)
* Included buzzer for audio feedback
* Powered and programmable via USB-C

## About the RP2040
The RP2040 microcontroller is a dual core ARM Cortex M0+ running at up to 133Mhz. It bundles in 264kB of SRAM, 30 multifunction GPIO pins (including a four channel 12-bit ADC), a heap of standard peripherals (I2C, SPI, UART, PWM, clocks, etc), and USB support.

## Powered by CircuitPython
It's not just a keyboard but also a USB drive containing the firmware as CircuitPython files. Its Python code can be changed with any text editor and executed simultaneously, which makes it super easy to customize the keymap, add macros or add a new function.  This keyboard is fully programmable via CiruitPython so there's no software to install, just plug it in, change keymaps and start building macros. Since all of the programming happens on the keyboard Python files, you can plug it into any computer and take your custom layouts wherever you go.

## Learn More
* [Board Documentation](https://github.com/jpconstantineau/PyKey60)

## Purchase
The PyKey60 is available on the Tindie store if you are interested in getting one.
* [Tindie](https://www.tindie.com/products/jpconstantineau/pykey60-rgb-keyboard-pcb-with-a-rp2040/)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
