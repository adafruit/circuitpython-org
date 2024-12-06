---
layout: download
board_id: "adafruit_feather_rp2040_usb_host"
title: "Feather RP2040 with USB Type A Host Download"
name: "Feather RP2040 with USB Type A Host"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5723"
board_image: "adafruit_feather_rp2040_usb_host.jpg"
date_added: 2023-05-02
family: rp2040
download_instructions: https://learn.adafruit.com/adafruit-feather-rp2040-with-usb-type-a-host/circuitpython
tags:
  - USB Host Feather
  - Feather USB Host
features:
  - Feather-Compatible
  - Battery Charging
  - STEMMA QT/QWIIC
  - USB-C
  - Breadboard-Friendly
---

You're probably really used to microcontroller boards with USB, but what about a dev board with two? Two is more than one, so that makes it twice as good! And the Adafruit Feather RP2040 with USB Host is definitely double-the-fun of our other Feather RP2040 boards, with a USB Type A port on the end for connecting USB devices to.

Now you might be thinking "hey waitaminute, the RP2040 doesn't have two USB port peripherals???" and you'd be correct! But what it does have is a nifty PIO peripheral that can be (ab)used to emulate a USB host peripheral. You get to keep the main USB port for uploading, debugging, and data communication, while at the same time sending and receiving data to just-about-any USB device. This work is originally by sekigon on GitHub, and if you're using Pico SDK that's still the recommended library to use.

Currently, support for the USB Host peripheral is only in Arduino. So check out the TinyUSB 'dual role' examples for some things you can do! For example, datalogging to a USB Key. Or reading from another device/microcontroller that has USB CDC serial interface. Or creating an HID re-mapper. Or connecting to weird devices that require firmware-updates like the Cypress EZ-USB based Intellikeys communications board.

## Tutorials

* [Primary Guide: Adafruit Feather RP2040 with USB Type A Host](https://learn.adafruit.com/adafruit-feather-rp2040-with-usb-type-a-host)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5723)
