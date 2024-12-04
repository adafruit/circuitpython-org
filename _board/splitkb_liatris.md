---
layout: download
board_id: "splitkb_liatris"
title: "Liatris Download"
name: "Liatris"
manufacturer: "SplitKB"
board_url:
 - "https://splitkb.com/products/liatris"
board_image: "splitkb_liatris.jpg"
date_added: 2023-07-28
family: rp2040
features:
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
  - Castellated Pads
---

The Liatris is a new controller designed by splitkb.com that's a designed specifically for (split) keyboards. It's a drop-in replacement for the Pro Micro, and a perfect alternative for other RP2040-based controllers.

### Core features

- Designed for **maximum compatibility** with kits that work with Pro Micro controllers, including the Kyria and our Aurora Series.
- **Supports [QMK](https://docs.qmk.fm/#/platformdev_rp2040) (all capabilities) and ZMK firmware (wired, single controller)** out of the box. Also compatible with [KMK](https://github.com/KMKfw/kmk_firmware) and [CircuitPython](https://circuitpython.org/).
- **Has 128Mbit (16MB) of flash memory**, ensuring you'll never run out of space even when making heavy use of OLED animations or text expansion macros. We added as much flash as the RP2040 can handle!
- **Access to 23 GPIO pins** to use on your keyboard, meaning that on any Aurora Series keyboard, you'll have 5 pins left over for any modifications you may want to do.
- **Rear-facing bootloader button** allowing you to easily recover from a bricked firmware, even when mounted in the usual upside-down position.
- An **ultra-low profile** with a mid-mounted USB-C port and a mere 1mm thick PCB. The rear-mounted reset button checks in at only 0.35mm, too, like it's almost not there.
- **Supports at least 1A of power output**, so you can maximize the output of your LEDs when your computer outputs enough power.

### Advanced features

The default settings are right for most people out of the gate. For those who demand more of their controller, we have some advanced features:

- **5V tolerant I2C pins** so you won't have to worry when hooking up an I2C device like an OLED or trackball board;
- **Runs at 3.6V for better 5V signal compatibility** so your LEDs will listen better to those smooth colour change commands (according to data sheets, 3.5V is the minimum to reliably talk with LEDs);
- **Selectable voltage on the VCC** (defaults to 5V to support RGB LEDs) **and RAW pins** (which we named VA, and isn't connected by default to be compatible with common Corne-style kits that bridge VCC with RAW on the keyboard by default) for when you need to get specific with your kit;
- **USB data pads** for hand wired builds where you want to have a separate USB port somewhere else on the board;
- **Debug pads** to be able to better look into microcontroller behaviour when you really need to.

## Purchase

* [SplitKB](https://splitkb.com/products/liatris)
