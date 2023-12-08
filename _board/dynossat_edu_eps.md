---
layout: download
board_id: "dynossat_edu_eps"
title: "DynOSSAT-EDU EPS Download"
name: "DynOSSAT-EDU EPS"
manufacturer: "BH Dynamics"
board_url:
 - "https://bhdyn.com/newspace"
board_image: "dynossat_edu_eps.jpg"
date_added: 2020-10-16
family: atmel-samd
downloads_display: true

features:
  - USB-C
---

DynOSSAT-EDU is the first open source PocketQube educational kit compatible with CircuitPython and Arduino.

This plaform is equipped with all the necessary modules for the operation of a nanosatellite (PocketQube)
in Low Earth Orbit (LEO) that would serve as a device for teaching, training, and driving curiosity about the philosophy and technology related to NewSpace.

This is the EPS (Electric Power System), the module responsible for battery management and power distribution subsystems,
including charging through solar panels using flight-proven MPPT electronics.

Hardware is licensed under **CERN OHL v1.2**.

## Technical details

- Well-known 48 MHz Cortex-M0 ATSAMD21E18 MCU with 256 KB flash + 32 KB RAM
- 32 Mbit SPI flash for storing CircuitPython code and libraries
- Flight-proven SPV1040 Maximum Power Point Tracking (MPPT) IC for solar cells power management
- Ultra low input voltage L6924D Lithium battery charger management IC optimized for pairing with the SPV1040
- Separate 5V and 3.3V power rails generated through high-performance DC/DC converters
- Battery Current/Voltage/Power measurement through the flight-proven INA226 digital meter
- Back-powering protection and load switching through the TPS22918, member of a flight-proven family of switches
- User-controllable WS2812B addressable RGB LED
- Female USB-C 2.0 connector for power and data logging
- Standard Molex Picoblade 1.5 mm connectors for battery and solar cells
- Connected to the OBC through SPI/I2C/UART for data communication and/or redundancy
- Comes preprogrammed with the UF2 Bootloader and CircuitPython 6.0.0

## Documentation

This board is open source hardware. You can check the docs and contribute [here](https://github.com/BHDynamics/dynossat-edu-eps).

## Purchase

* [Tindie](https://www.tindie.com/products/21832/)
