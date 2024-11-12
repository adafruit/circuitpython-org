---
layout: download
board_id: "trellis_m4_express"
title: "NeoTrellis M4 Download"
name: "NeoTrellis M4"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/4020"
 - "https://www.adafruit.com/product/3938"
 - "https://www.adafruit.com/product/4018"
board_image: "trellis_m4_express.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: trellis_m4
download_instructions: https://learn.adafruit.com/adafruit-neotrellis-m4/circuitpython
features:
---

The **NeoTrellis M4** is an all-in-one **USB + NeoPixel + Elastomer + Audio** board. It's powered by the SAMD51, a Cortex M4 core running at 120 MHz. This chip has a speedy core with CircuitPython support, hardware DSP/floating point, dual DACs and all the goodies you expect from normal chips like I2C, ADC, DMA, etc. It has a roomy 512KB of flash and 192KB of SRAM so it's great for CircuitPython, includes a full 8MB flash chip so tons of space for files and audio clips.

The native USB port can turn it into a MIDI USB device if you like - currently that's only supported in Arduino. Tether it to a computer or tablet, if you like. Or use it in standalone mode, as long as its powered from a USB power plug, it'll run whatever firmware is burned into it.

OK so you've got this big brain, but now you need inputs and outputs! There's a 4x8 grid of elastomer button pads with a NeoPixel nestled in the center of each one. You can read any/all button presses simultaneously thanks to the fully diode'd matrix, and also set each button color to any of 24-bit colors. The elastomer buttons are translucent so they glow beautifully when lit.

Time to make some noise! Adafruit picked the SAMD51 mostly because it has dual DACs - that's two 12-bit, 500KSPS 'true analog' outputs connected them to left and right on a standard headphone jack. Since the DAC pins are also ADC pins you could also use the left/right for audio line level _input_ if you so choose. You're not going to get audiophile-quality outputs from two 12-bit DACs but you can certainly play audio clips and make beeps and bloops.

To add more interactivity, a precision triple-axis accelerometer from Analog Devices, the ADXL343, is included as well, and provides sensor information on tilt, motion, or tapping. Great for adding another dimension of data input in addition to the button pads.

Finally, a 4 pin JST hacking port is available for extra add-ons. It's STEMMA and Grove compatible, and provides GND, 3.3V power, and two pins that can be used for I2C, ADC, or a UART. So connect some other sensor, or read stereo audio in, or maybe hack together a MIDI port. Whatever you like!

Features:

*   **ATSAMD51 32-bit Cortex M4** core running at **120 MHz** (32-bit, 3.3V logic and power)
*   Hardware DSP and floating point support
*   **512 KB** flash, **192 KB** RAM
*   Native USB that can act as a true USB MIDI device if you like.
*   **8 MB SPI FLASH chip** for storing files and CircuitPython code storage.
*   4x8 elastomer pads with fully diode'd matrix - no ghosting!
*   4x8 NeoPixels for each pad, glows through the elastomer buttons
*   TRRS Headphone jack with stereo DAC outputs on Left/Right, can also be stereo ADC inputs.
*   Built in [MAX4466 electret mic amplifier](https://www.adafruit.com/product/1063) for mobile phone headsets. 'Raw' DC level reading also available on a separate ADC
*   4-JST hacking port with 3.3V power, ground, and two GPIO that can be I2C/ADC/UART
*   [Analog Devices ADXL343 triple-axis accelerometer](https://www.analog.com/en/products/adxl343.html)
*   Really fun to press buttons and have sounds come out!

## Tutorials
* [NeoTrellis M4 Overview](https://learn.adafruit.com/adafruit-neotrellis-m4)
* [Projects and Guides](https://learn.adafruit.com/products/4020/guides)

## Purchase
* [Full Kit - Adafruit](https://www.adafruit.com/product/4020)
* [Mainboard - Adafruit](https://www.adafruit.com/product/3938)
