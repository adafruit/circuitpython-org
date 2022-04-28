---
layout: download
board_id: "pimoroni_motor2040"
title: "Motor 2040 Download"
name: "Motor 2040"
manufacturer: "Pimoroni"
board_url: "https://shop.pimoroni.com/products/motor-2040"
board_image: "pimoroni_motor2040.jpg"
date_added: 2022-4-8
family: raspberrypi
features:
  - Robotics
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

A compact 4 channel motor+encoder controller, powered by RP2040. It has RGB and per-motor indicator LEDs plus built in voltage and current sensing.
​
Motor 2040 is a **standalone motor controller** for driving motors with encoders attached. **Encoder motors** can provide feedback to the controller, enabling more precise control over position and velocity - perfect for building a four wheel drive robot rover or buggy (add [mecanum omniwheels](https://pimoroni-2.myshopify.com/products/mecanum-wheels-pack-of-4) to go sideways!). We've built the RP2040 chip right into Motor 2040 so you don't need separate microcontroller and driver boards, keeping everything tidy and lightweight.
​
Why limit yourself to vehicular constructs though, you could use it as the brains of any project that involves motors: elaborate pulley systems, 1:12 replicas of It's A Small World or customisable dials with haptic feedback and programmable endpoints.
​
Motor 2040 comes with many useful built-in bells and whistles, such as:
​
- An **addressable RGB LED** (AKA Neopixel) for visual feedback and status reports.
- A pair of mono **indicator LEDs on each motor channel** to show you when and in what direction a motor is moving. This helps visualise what your code is doing and means you can prototype without having motors plugged in!
- A **QW/ST connector** to make it easy to attach [Qwiic](https://pimoroni-2.myshopify.com/collections/qwiic) or [STEMMA QT](https://pimoroni-2.myshopify.com/collections/stemma-qt) breakouts - great for adding some sensor smarts.
- Some neat **voltage/current/fault sensing features** to help prevent motor mishaps.
​
It's supported by a well documented C++/MicroPython motor and encoder library with lots of examples to show you how to use the individual features (and everything together).
​

## About RP2040
Raspberry Pi's RP2040 microcontroller is a dual core ARM Cortex M0+ running at up to 133Mhz. It bundles in 264kB of SRAM, 30 multifunction GPIO pins (including a four channel 12-bit ADC), a heap of standard peripherals (I2C, SPI, UART, PWM, clocks, etc), and USB support.

One very exciting feature of RP2040 is the programmable IOs which allow you to execute custom programs that can manipulate GPIO pins and transfer data between peripherals - they can offload tasks that require high data transfer rates or precise timing that traditionally would have required a lot of heavy lifting from the CPU.

## Purchase
* [Pimoroni](https://shop.pimoroni.com/products/motor-2040)
