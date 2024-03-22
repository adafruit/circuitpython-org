---
layout: download
board_id: "feather_m0_express_crickit"
title: "Feather M0 Express + Crickit Download"
name: "Feather M0 Express + Crickit"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/3343"
board_image: "feather_m0_express_crickit.jpg"
date_added: 2019-03-09
family: atmel-samd
bootloader_id: feather_m0_express
features:
  - Speaker
  - Feather-Compatible
  - Battery Charging
  - Robotics
---

**Crickit** is Adafruit's **C**reative **R**obotics & **I**nteractive **C**onstruction **Kit**. It's an add-on to popular Feather ecosystem boards that lets you **#MakeRobotFriend **using CircuitPython.

Plug in _any_ Feather mainboard you want into the center, and you're good to go! The Crickit is powered by seesaw, an I2C-to-whatever bridge firmware. So you only need to use two I2C data pins to control the huge number of inputs and outputs on the Crickit. All those timers, PWMs, sensors are offloaded to the co-processor.

The only thing that is _not_ managed by seesaw is the audio output. Provided is a small jumper you can solder to connect the audio amplifier to the first analog pin. On Feather M0's this is a true analog output (DAC) and you can play audio clips with CircuitPython. Other Feathers _may not have a DAC!_ In that case, you can solder a wire to jumper the audio amp to a PWM pin.

You get to use all the non-I2C signal pins on your feather and get a boat-load of extra in/out pins, motor controllers, capacitive touch sensors, a NeoPixel driver and amplified speaker output. It complements & extends your Feather so you can still use all the goodies, including stacking FeatherWings on top. But now you have a robotics playground as well.

## Technical details

* 4 x Analog or Digital Servo control, with precision 16-bit timers
* 2 x Bi-directional brushed DC motor control, 1 A current limited each, with 8-bit PWM speed control (or one stepper)
* 4 x High current "Darlington" 500 mA drive outputs with kick-back diode protection. For solenoids, relays, large LEDs, or one uni-polar stepper
* 4 x Capacitive touch sensors with alligator-pads
* 8 x Signal pins, digital in/out or analog inputs
* 1 x NeoPixel driver with 5V level shifter - The NeoPixels are buffered and controlled by the seesaw chip
* 1 x Class D, 4-8 ohm speaker, 3 W-max audio amplifier - the audio input pin is available as a solder-able pad for your configuration, you can connect it to your Feather's DAC or PWM output as you desire.

All are powered via 5V DC, so you can use any 5V-powered servos, DC motors, steppers, solenoids, relays etc. To keep things simple and safe, we don't support mixing voltages, so only 5V, not for use with 9V or 12V robotic components.

## Tutorial

- [Feather M0 Express + Crickit Overview](https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit)

## Purchase

* [Feather M0 Express - Adafruit](https://www.adafruit.com/product/3403)
* [CRICKIT for Feather - Adafruit](https://www.adafruit.com/product/3343)
