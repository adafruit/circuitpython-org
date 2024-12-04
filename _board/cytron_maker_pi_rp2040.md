---
layout: download
board_id: "cytron_maker_pi_rp2040"
title: "Maker Pi RP2040 Download"
name: "Maker Pi RP2040"
manufacturer: "Cytron Technologies"
board_url:
 - "https://www.cytron.io/p-maker-pi-rp2040"
 - "https://www.adafruit.com/product/5129"
board_image: "cytron_maker_pi_rp2040.jpg"
date_added: 2021-05-31
family: rp2040
download_instructions: https://github.com/CytronTechnologies/MAKER-PI-RP2040#circuitpython
features:
  - Battery Charging
  - Speaker
  - Robotics
---

Cytron Maker Pi RP2040 features the RP2040 chip, embedded on a robot controller board. The board also comes with 2-channel DC motor driver, 4 servo motor ports and 7 Grove I/O connectors, ready for your next DIY robot/motion control projects.

The DC motor driver onboard is able to control two brushed DC motors or single bipolar/unipolar stepper motor from 3.6 V to 6 V, providing up to 1 A current per channel continuously. The built-in Quick Test buttons and motor output LEDs allow functional test of the motor driver in a quick and convenient way without the need of writing any test code. Vmotor for both DC and servo motors depends on the input voltage supplied to the board.

Maker Pi RP2040 has lots of LEDs for troubleshooting and visual effects, is able to make quite some noise with the onboard piezo buzzer and comes with push buttons ready to detect your touch.

There are three ways to supply power to the Maker Pi RP2040 - via USB (5 V) socket, with a single cell LiPo/Li-Ion battery or through the VIN (3.6-6 V) terminals. However only one power source is needed to power up both controller board and motors at a time. Power supply from all these power sources can all be controlled with the power on/off switch onboard.

CircuitPython is preloaded on the Maker Pi RP2040 and it runs a simple demo program right out-of-the-box. It can also be programmed with C/C++ (natively or with Arduino IDE support) or MicroPython.

## Technical details

- Dual-core Arm Cortex-M0+ processor
- 264 KB internal RAM
- 2 MB of Flash memory
- Robot controller board
  - 4x Servo motors (`GPIO12`. `GPIO13`, `GPIO14`, `GPIO15`)
  - 2x DC motors with quick test buttons (Dual-channel H-bridge)
- Versatile power circuit
  - 7 Automatic power selection: USB 5 V, LiPo (1-cell) or Vin (3.6-6 V)
  - Built-in 1-cell LiPo/Li-Ion charger (over-charged & over-discharged protection)
  - Power on/off switch
- 13x Status indicator LEDs for GPIO pins
- 1x Piezo buzzer with mute switch
- 2x Push button
- 22x RGB LED (Neopixel)
- 7x Grove ports (flexible I/O options: digital, analog, I2C, SPI, UART)
- Mouting holes
  - 4x 4.8 mm mounting hole (LEGO® pin compatible)
  - 6x M3 screw hole

## Resources

- [Getting Started with Maker Pi RP2040 & Example Code](https://github.com/CytronTechnologies/MAKER-PI-RP2040)
- [Maker Pi RP2040 Datasheet](https://docs.google.com/document/d/1DJASwxgbattM37V4AIlJVR4pxukq0up25LppA8-z_AY/edit)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5129)
* [Cytron](https://www.cytron.io/p-maker-pi-rp2040)
