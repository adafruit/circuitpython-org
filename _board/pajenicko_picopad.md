---
layout: download
board_id: "pajenicko_picopad"
title: "Pajenicko Picopad Download"
name: "Pajenicko Picopad"
manufacturer: "Pajenicko s.r.o."
board_url:
 - "https://github.com/Pajenicko/Picopad"
board_image: "pajenicko_picopad.jpg"
date_added: 2023-07-25
family: rp2040
download_instructions: https://github.com/Pajenicko/Picopad/tree/main/circuitpython
features:
  - Display
  - Speaker
  - Battery Charging
  - Bluetooth/BTLE
  - Wi-Fi

---

Picopad is an **open-source DIY gaming console kit** for young tech enthusiasts. It utilizes a Raspberry Pi Pico module and features a 2" 240x320 IPS display, speaker, LED, buttons, and a microSD slot. Picopad supports programming in C, MicroPython and CircuitPython, enabling users to learn coding skills. The kit contains all necessary components to assemble the console. Picopad promotes STEM education through electronics and programming. It has an external connector for expansions. The Picopad Wifi variant adds wireless connectivity with Wifi 802.11n 2.4GHz (WPA3 security) and Bluetooth 5.2. Games and software are open source to enable customization. Picopad enables hands-on learning of electronics and programming in an engaging gaming platform. There are 16 classic games including Pacman, Tetris, Snake, and more available in the [Picopad GitHub repository](https://github.com/Pajenicko/Picopad) that are programmed using the Picopad C SDK and their source codes are included.


## How to upload CircuitPython:
* Download UF2 file for Picopad
* Press and hold BOOTSEL button (bottom) while connecting USB cable to power on Picopad
* Picopad enters bootloader mode, release BOOTSEL button
* Copy UF2 file to RPI-RP2 drive
* Picopad reboots and runs the new firmware
* If everything went smoothly, you should see the CircuitPython console appear on screen
* Have fun!


## Features
* Powered by Raspberry Pico/Pico-W (RP2040)
* ARM Cortex M0+ running at up to 133Mhz
* 264kB of SRAM
* IPS LCD 240x320 screen (ST7789)
* LED
* Buttons
* Lipo battery with charging circuit (TP4056)
* Speaker
* External connector
* [More info & guides](https://picopad.eu/en/)

## Community
* [Picopad 3D printed case](https://www.printables.com/model/504447-picopad-case)
* [Picopad GameBoy Emulator](https://github.com/tvecera/picopad-playground/tree/main/picopad-sdk/picopad-gb)
* [Picopad SDK Pico SDK Fork](https://github.com/tvecera/picopad-playground/tree/main/picopad-sdk)
* [Picopad Program Template](https://github.com/tvecera/picopad-template)


## Purchase
* [Pajenicko](https://pajenicko.cz/picopad-wifi-open-source-herni-konzole)


