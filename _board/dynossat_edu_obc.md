---
layout: download
board_id: "dynossat_edu_obc"
title: "DynOSSAT-EDU OBC Download"
name: "DynOSSAT-EDU OBC"
manufacturer: "BH Dynamics"
board_url:
 - "https://bhdyn.com/newspace"
board_image: "dynossat_edu_obc.jpg"
date_added: 2020-10-16
family: atmel-samd
downloads_display: true

features:
  - USB-C
---

DynOSSAT-EDU is the first open source PocketQube educational kit compatible with CircuitPython and Arduino.

This plaform is equipped with all the necessary modules for the operation of a nanosatellite (PocketQube)
in Low Earth Orbit (LEO) that would serve as a device for teaching, training, and driving curiosity about the philosophy and technology related to NewSpace.

This is the On-Board Computer (OBC), the module responsible for managing the satellite and process sensor data. It
integrates a 9-axis IMU, a gas sensor, a temperature sensor and carries a powerful ATSAMD51.

Hardware is licensed under **CERN OHL v1.2**.

## Technical details

- Powerful ATSAMD51J20A-AU 120 MHz Cortex-M4F processor with 1 MB flash + 256 KB RAM for all your CircuitPython needs
- 32 Mbit SPI flash for storing CircuitPython code and libraries
- High-precision ICM-20948 Inertial Measurement Unit including Accelerometer, Gyroscope and Magnetometer for Attitude management
- MCP9808 Digital Temperature Sensor
- SGP30 TVOC and eqCO2 air quality sensor
- User-controllable WS2812B addressable RGB LED
- Separate 5V and 3.3V rails, providing up to 1A/500mA respectively
- MicroSD Card slot
- Female USB-C 2.0 connector for power and data logging
- PQBH40 bus exposing 10 digital pins, 6 analog pins (+ true DAC), an I2C bus, an SPI bus and an UART
- Comes preprogrammed with the UF2 bootloader and CircuitPython 6.0.0

## Documentation

This board is open source hardware. You can check the docs and contribute [here](https://github.com/BHDynamics/dynossat-edu-obc).

## Purchase

* [Tindie](https://www.tindie.com/products/21832/)
