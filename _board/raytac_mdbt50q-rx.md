---
layout: download
board_id: "raytac_mdbt50q-rx"
title: "MDBT50Q-RX Download"
name: "MDBT50Q-RX"
manufacturer: "Raytac Corporation"
board_url:
 - "https://www.raytac.com/product/ins.php?index_id=89"
 - "https://www.adafruit.com/product/5199"
board_image: "raytac_mdbt50q-rx.jpg"
date_added: 2021-08-13
family: nrf52840
bootloader_id: raytac_mdbt50q_rx
features:
  - Bluetooth/BTLE

---

This USB dongle/key type thing is a little unusual - it *isn't* a BLE adapter that you plug into a computer to add wireless capability. (If you do want something like that, our [Bluetooth 4.0 USB Module](https://www.adafruit.com/products/1327) will do the job nicely.) Instead, this is basically a minimal nRF52840 wireless microcontroller dev board on a stick. You can program it in Arduino or CircuitPython and it's completely standalone. This could be useful for some situations where you want to have a standalone BLE device that communicates with a USB host *but without dealing with the operating system's BLE stack*.

Each MDBT50Q-RX dongle comes pre-programmed with the TinyUF2 bootloader, which makes loading code onto it very easy (note that only the ones from Adafruit do this, its a special-order item). To enter the bootloader, hold down the dongle's button while inserting into USB. The button can be used in Arduino/CircuitPython as an input. There's also a single blue LED indicator. It's all very simple but we could see situations where perhaps this acts as a beacon, a OS-less BLE interface or bridge, or a compact development board for experimenting with the nRF52840.

The blue LED is connected to P1.13, set that pin to be an output and pull low to turn on the LED

The button is connected to P0.15, set that pin to be an input with an internal pullup - when pressed the pin will go low.

Of course the best way to program these chips is with the Nordic SDK. This chip also has [some basic Arduino support](https://github.com/adafruit/Adafruit_nRF52_Arduino), [CircuitPython support](https://github.com/adafruit/circuitpython/tree/main/ports/nrf), and is [supported by MyNewt](https://mynewt.apache.org/latest/tutorials/blinky/nRF52.html).

## Purchase
* [Adafruit](https://www.adafruit.com/product/5199)
* [Raytac Corporation](https://www.raytac.com/product/ins.php?index_id=89)
