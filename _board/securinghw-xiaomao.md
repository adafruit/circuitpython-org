---
layout: download
board_id: "securinghw-xiaomao"
title: "Xiaomao Download"
name: "Xiaomao"
manufacturer: "SecuringHardware.com"
board_url: "https://tigard-tools.org/xiaomao"
board_image: "securinghardware_xiaomao.jpg"
date_added: 2026-09-15
family: "rp2040"
features:
  - USB-C
---
Xiǎomāo is a development board geared toward hardware hacking and hardware implant design that can safely interfacing with a wide range of logic levels

Xiǎomāo (小猫) means 'small cat' and gets its name from the original revision which used the small Seeed Studio XIAO module with the catlike tigard-tools wiring harnesses. The current version, Xiǎomāo v2 is a redesign based on an RP2040 but the Xiǎomāo name (and shape) stuck.

All the GPIO pins have 200 ohm current limiting resistors that should protect both the target and the device. If you have a Tigard, you can re-use the wiring harnesses. You should be able to tap power and ground from your target system to get your device running in standalone implant mode.

<<<<<<<< HEAD:_board/xiaomao.md
Alongside a logic analyzer and an I/O interface board, a simple microcontroller board rounds out a basic hardware hacking toolkit, allowing you to bitbang proprietary protocols, search for disabled interfaces, log data, drop payloads, and act as an implant-in-the-middle. For example, [Hecate](https://github.com/tigard-tools/hecate) is a CircuitPython framework for UART logging, payloads, and interdiction. It will work on any board but was built with Xiǎomāo in mind.
========
Alongside a logic analyzer and an I/O interface board, a simple microcontroller board rounds out a basic hardware hacking toolkit, allowing you to bitbang proprietary protocols, search for disabled interfaces, log data, drop payloads, and act as an implant-in-the-middle. For example, [Hecate](https://tigard-tools.org/hecate) is a CircuitPython framework for UART logging, payloads, and interdiction. It will work on any board but was built with Xiǎomāo in mind.
>>>>>>>> 7257695b735dfe9bca3c8b05386acdc31b402e0d:_board/securinghw-xiaomao.md

## Purchase
* Not planned for sale, but as a freebie with some workshops

## Learn More
* [Documentation](https://tigard-tools.org/xiaomao) includes all the board files, as well as some recommended use cases and code samples.
