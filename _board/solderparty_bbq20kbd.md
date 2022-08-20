---
layout: download
board_id: "solderparty_bbq20kbd"
title: "BBQ20KBD Download"
name: "BBQ20KBD"
manufacturer: "Solder Party"
board_url: "https://www.solder.party/docs/bbq20kbd/"
board_image: "solderparty_bbq20kbd.jpg"
date_added: 2022-08-20
family: raspberrypi
bootloader_id: solderparty__bbq20kbd
downloads_display: true
blinka: false
download_instructions: ""

features:
  - USB-C
  - STEMMA QT/QWIIC
---

## Official description of the BBQ20KBD running official firmware

A BB Q20 Keyboard in USB/PMOD/Qwiic format with a injection molded clear plastic case.

This is the evolution of our previous BBQ10 PMOD board. We took all the feedback from that board and improved on the design in every way.

We added a Qwiic/Stemma QT connector, we added USB HID support, we changed to a Q20 keyboard, which gave us four extra buttons, and the optical trackpad that works as a USB HID Mouse. And we decided to put the whole thing into a custom-designed injection molded clear plastic case for better usability and durability, as well as that retro 90s look.

The board uses the Raspberry Pi RP2040 MCU to poll the keyboard and trackpad and put the key press information into a FIFO.

You can use the I2C interface to read the FIFO, reconfigure the chip, and change the keyboar backlight.

In addition to that, the board also has a USB Type-C socket, and when connected to a desktop computer (Windows/Linux/MacOS), a smartphone (iOS/Android), or a SBC (Raspberry Pi, etc), it enumerates as a USB HID Keyboard and Mouse combo!

The firmware can be configured over USB using the Vendor Class interface.

The I2C interface is compatible with the old BBQ10 module, you can use the same libraries to interface this board.

Note: This board is not 5V-tolerant!

## Installing CircuitPython Firmware on BBQ20KBD

Installation is like for any RP2040 board, you need to get into the UF2 mode, in our case power the BBQ20KBD while pressing the top left button (boot button).

Download CircuitPython UF2 file of your choice and copy that file RPI-RP2 drive.

If ever you regret your choice, the official UF2 firmware is [available](https://github.com/solderparty/i2c_puppet/releases).

## BBQ20KBD running CircuitPython firmware

You now have a very small keyboard running CircuitPython and many possibilities.

You can scan those keys using the keypad library, the top right button will need to have a special treatment.

You can also try controling the backlight and plug an I2C sensor, an I2C screen or both via the Stemma QT connector.

Of course you can make your BBQ20KBD act as a keyboard by using adafruit usb-hid library.

If you feel advanturous you could even try using KMK library, or implement a library to handle the mouse button.

## Links

* [Documentation](https://bbq20kbd.solder.party/)