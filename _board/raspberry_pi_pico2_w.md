---
layout: download
board_id: "raspberry_pi_pico2_w"
title: "Pico 2 W Download"
name: "Pico 2 W"
manufacturer: "Raspberry Pi"
board_url:
  - "https://www.adafruit.com/product/6087"
board_image: "raspberry_pi_pico2_w.jpg"
date_added: 2024-11-25
family: rp2350
tags:
  - pico 2
  - picow
  - 🥧🐮
features:
  - Breadboard-Friendly
  - Wi-Fi
  - Castellated Pads
---


Raspberry Pi Pico 2W is Raspberry Pi Foundation's update to their popular RP2040-based wireless ico board, now built on RP2350: their new high-performance, secure microcontroller. With a higher core clock speed, double the on-chip SRAM (512KB), double the on-board flash memory (4MB!), more powerful Arm M33 cores, new security and low-power features, and upgraded interfacing capabilities, the Raspberry Pi Pico 2 delivers a significant performance and feature boost while retaining hardware and software compatibility with earlier members of the Raspberry Pi Pico series.

The unique dual-core, dual-architecture capability of RP2350 allows users to choose between a pair of industry-standard Arm Cortex-M33 cores and a pair of open-hardware Hazard3 RISC-V cores. You can use either Arm or RISC-V cores, so this is a great way to dabble in RISC-V development with an affordable board that has lots of peripherals. The M33 has an FPU, and is 'basically' 2x as fast as the M0+ of the RP2040 when we speed-tested it.

Not only is the Pico 2 twice as fast, it has twice as much RAM, 520KB compared to 264KB. The Pico also has twice as much FLASH memory, 4MB instead of 2MB, which will make it a much better board for CircuitPython usage where the internal memory is used to store files. There's also one more PIO blocks (3 blocks with 4 state machines apiece, rather than 2) so you can do even more pin twiddling at once. For folks who want to use the RP2350 to generate high frequency output signals like DVI display output, you can use the HSTX (high speed transmission) peripheral rather than PIO. 

For customers who wanted a more secure microcontroller for product design, the RP2350 provides a comprehensive security architecture, built around Arm TrustZone for Cortex-M, and incorporating signed boot, 8KB of antifuse OTP for key storage, SHA-256 acceleration, a hardware TRNG, and fast glitch detectors. These features, including the secure boot ROM, are extensively documented and available to all users without restriction: this transparent approach, which contrasts with the “security through
obscurity” offered by legacy vendors, allows professional users to integrate RP2350, and Raspberry Pi Pico 2, into products with confidence.

Programmable in C / C++ and CircuitPython/MicroPython, and with detailed documentation, Raspberry Pi Pico 2 is the ideal microcontroller board for enthusiasts and professional developers alike. It makes an excellent upgrade to the RP2040, with lots of back-compatibility and some excellent upgrades.

Please note: The Pico 2Wcomes with the A2 version of the RP2350, [which is affected by the E9 erratum](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf#page=1342). This erratum affects some uses of GPIO and PIO such as high-impedance inputs and the internal pulldowns. You may need to use 8.2K or smaller resistors if pull-downs are required. At this time, Sept 9 2024, there is no other version of the RP2350 available - only the A2 version.

