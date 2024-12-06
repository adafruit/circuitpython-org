---
layout: download
board_id: "pimoroni_motor2040"
title: "Motor 2040 Download"
name: "Motor 2040"
manufacturer: "Pimoroni"
board_url:
 - "https://shop.pimoroni.com/products/motor-2040"
board_image: "pimoroni_motor2040.jpg"
date_added: 2022-06-15
family: rp2040
features:
  - Robotics
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

A compact 4 channel motor+encoder controller, powered by RP2040. It has RGB and per-motor indicator LEDs plus built in voltage and current sensing. There's also a Qwiic/STEMMA QT connector for adding breakouts!

## Features
- Powered by RP2040 (Dual Arm Cortex M0+ running at up to 133Mhz with 264kB of SRAM)
- 2MB of QSPI flash supporting XiP
- 2 Dual H-Bridge motor drivers (DRV8833)
- 4 JST-SH connectors (6 pin) for attaching motors
- Wide voltage range for motors and logic (2.7V to 10V)
- On-board 3V3 regulator with input up to 13.2V (max regulator current output 150mA)
- Onboard voltage, current and fault sensing
- Per motor current limiting (0.5A) \*
- Per motor direction indicator LEDs **
- Addressable RGB LED/Neopixel
- Reset and BOOT button (the BOOT button can also be used as a user button)
- USB-C connector for programming and power (3A max)
- Qw/ST (Qwiic/STEMMA QT) connector for breakouts

## Powering Motor 2040
Motor 2040 can be powered either by plugging the board into a USB-C power source (like a PC or power adapter) or by connecting a battery pack to the EXT PWR or VSYS connections. On an unmodified board, **you should only have one power source connected at a time**, to avoid back-powering your computer or battery.

If you want to have two power sources connected at the same time, Motor 2040 has two traces on its underside that you can cut to do this safely.

- **Cut EXT PWR to VSYS** if you want to provide your motors with a separate power supply (up to 10V) from that used to power the rest of the board. Board power (up to 13.2V) will need to be provided either by USB 5V or VSYS.
- **Cut USB 5V to VSYS** if you want to run the board entirely off a separate power supply, without worry of back-powering your computer. Note that this also means the board will not turn on when only connected by USB.

## Notes
- \* The current limit of each motor can be disabled by soldering the "high current" pads on the rear (doing this will also disable the current monitoring). The maximum supported output current is 1.2 A continuous (2 A peak) per motor.
- ** The direction indicators for each motor can be disabled by cutting the "motor LED" traces on the rear.
- The pinout of the JST-SH motor connectors is M+, M-, 3v3, A, B, GND.

## About RP2040
Raspberry Pi's RP2040 microcontroller is a dual core ARM Cortex M0+ running at up to 133Mhz. It bundles in 264kB of SRAM, 30 multifunction GPIO pins (including a four channel 12-bit ADC), a heap of standard peripherals (I2C, SPI, UART, PWM, clocks, etc), and USB support.

One very exciting feature of RP2040 is the programmable IOs which allow you to execute custom programs that can manipulate GPIO pins and transfer data between peripherals - they can offload tasks that require high data transfer rates or precise timing that traditionally would have required a lot of heavy lifting from the CPU.

## Purchase
* [Pimoroni](https://shop.pimoroni.com/products/motor-2040)
