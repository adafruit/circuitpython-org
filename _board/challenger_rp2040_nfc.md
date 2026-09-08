---
layout: download
board_id: "challenger_rp2040_nfc"
title: "Challenger RP2040 NFC Download"
name: "Challenger RP2040 NFC"
manufacturer: "Invector Labs"
board_url:
 - "https://ilabs.se/product/challenger-rp2040-nfc/"
board_image: "challenger_rp2040_nfc.jpg"
date_added: 2026-09-08
family: rp2040
features:
  - USB-C
  - Breadboard-Friendly
  - Feather-Compatible
  - Battery Charging
---

The Challenger RP2040 NFC is an Adafruit Feather format board based on the Raspberry Pi RP2040, with an NXP PN7150 NFC controller on board. Unlike a simple NFC tag, the PN7150 is a full reader/writer: it polls for NFC-A, NFC-B, NFC-F and NFC-V targets and speaks NCI over I2C, so CircuitPython can read and write NDEF messages on NTAG/Ultralight, MIFARE Classic, DESFire and ISO15693 tags.

It shares its layout with the rest of the Challenger RP2040 family (USB-C, 8 MByte of flash, a LiPo connector and charger, and a NeoPixel), so it drops into a Feather-shaped project like any other board in the series.

### Using the NFC controller

The PN7150 sits on its own I2C bus, exposed as `board.NFC_SDA` and `board.NFC_SCL`, with `board.NFC_IRQ` and `board.NFC_RESET` for the interrupt and VEN lines. That bus is internal to the board and does not appear on the headers; `board.I2C()` is the separate header bus on GPIO0/GPIO1.

[circuitpython-pn7150](https://github.com/TheFilipcom4607/circuitpython-pn7150) is a single-file driver for the controller that imports nothing outside the core modules. It reads NTAG/Ultralight, Mifare Classic, DESFire/ISO-DEP, ISO15693 and FeliCa, decodes and writes NDEF, and can emulate a Type 4 tag so that tapping a phone on the board opens a URL. It recognises this board's pin names, so `PN7150.from_board(board)` wires itself up:

```python
import board
from pn7150 import PN7150

nfc = PN7150.from_board(board)
with nfc:
    for tag in nfc.scan():
        print(tag.type, tag.uid_hex)
        if tag.ndef:
            print("  ->", tag.ndef.value)
```

Install it with `circup bundle-add TheFilipcom4607/circuitpython-pn7150` followed by `circup install pn7150`, or copy `pn7150.mpy` from the latest release into `CIRCUITPY/lib/`. [ElectronicCats_CircuitPython_PN7150](https://github.com/ElectronicCats/ElectronicCats_CircuitPython_PN7150) is the other driver for this chip; it covers tag detection, and its example needs `frequency` lowered from 400000 to 100000 to run here.

The on-board bus has no external pull-up resistors, so this board is built with `CIRCUITPY_I2C_ALLOW_INTERNAL_PULL_UP` and `busio.I2C` enables the RP2040's internal pull-ups on it. Those are weak, so **construct the NFC bus at 100 kHz**. 400 kHz will time out. Note also that `i2c.scan()` does not list the PN7150: it ignores the zero-length write that `scan()` uses and only answers real NCI frames.

### Technical details

- Raspberry Pi RP2040 dual core Cortex-M0+ @ 133 MHz
- 264 KByte SRAM, 8 MByte flash
- NXP PN7150 NFC controller with integrated firmware, on a dedicated I2C bus
- Reader/writer for NFC-A, NFC-B, NFC-F and NFC-V targets
- 1 hardware I2C, 1 hardware SPI and 1 hardware UART on the headers
- 4 x 12-bit ADC inputs
- NeoPixel and a red user LED
- LiPo charger and standard LiPo battery connector
- USB-C connector

The board ships without an NFC antenna. iLabs sells it as a kit with one, or you can attach your own to the antenna pads.

## Purchase

* [Invector Labs](https://ilabs.se/product/challenger-rp2040-nfc/)
