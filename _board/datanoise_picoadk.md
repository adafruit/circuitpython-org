---
layout: download
board_id: "datanoise_picoadk"
title: "PicoADK - Audio Development Kit Download"
name: "PicoADK - Audio Development Kit"
manufacturer: "DatanoiseTV"
board_url:
 - "https://www.tindie.com/products/datanoisetv/picoadk-audio-development-kit-raspberry-rp2040/"
board_image: "datanoise_picoadk.jpg"
date_added: 2023-07-28
family: rp2040
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

The PicoADK is a RP2040 based Audio Development Kit, which allows you to build your own digital oscillators, synthesizers, noise boxes and experiment around. It has all the base features of the Raspberry Pico / RP2040, plus a high quality Audio Output, 8 Analog Inputs for connecting potentiometers, control voltage from Eurorack systems or even additional input signals.

#### Why did you make it?

I made it initially for myself to build digital oscillators for a hybrid synth and to experiment with the RP2040 as a DSP.

#### What makes it special?

It has a 32-bit Audio Codec and an SPI 8x 12-bit ADC and is only longer by 4 pins on each side than the Raspberry Pico!

#### Specifications

- RP2040 Dual Core 133MHz Cortex M0+ (running at 2x 400MHz Overclocked in the RTOS Template)
- 2MB Flash (plenty for synthesizers and sound generators)
- Very low noise LDO regulators (separate LDO for digital circuits and separate for analog circuits)
- No switching regulators
- Pin-compatible with RP2040 (besides a few pins internally used or rearranged)
- PCM5100A 32-bit, up to 384KHz I2S Audio Codec
- Dedicated Boot and Reset Buttons
- 8 channel 12-bit ADC with up to 1MS/s, with selectable 3.3V range (on-board low-noise power supply) or range up to 5V via external VREF
- Low-Pass filter on each ADC input (fMax=48 KHz) at low-impedance (100 Ohm). With 5V VREF suitable for CV (no overvoltage protection, unipolar)
- Series resistors on ADC SPI to improve signal integrity and reduce crosstalk
- Symbols marking special pin functions on the pin headers
- 4 LEDs on shared GPIO2-5 for debugging
- GPIO15 is hard-wired to a LED
- ESD Protection on USB
- SWD Debug Port

## Purchase

* [Tindie](https://www.tindie.com/products/datanoisetv/picoadk-audio-development-kit-raspberry-rp2040/)
