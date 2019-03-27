---
layout: download
board_id: "feather_m0_rfm69"
title: "Feather M0 RFM69 Download"
name: "Feather M0 RFM69"
manufacturer: "Adafruit"
board_url: ""
board_image: "/assets/images/boards/feather_m0_rfm69.jpg"
---

This is the** Adafruit Feather M0 RFM69 Packet Radio (868 or 915 MHz)****.** Also called _RadioFruits**,**_ Adafruit's take on an microcontroller with a RFM69HCW packet radio transceiver plus built in USB and battery charging. Its an Adafruit Feather M0 with a 900MHz radio module cooked in!

Feather is the development platform from Adafruit, and like its namesake it is thin, light, and lets you fly! Adafruit designed Feather to be an open standard for portable microcontroller cores. [Adafruit has other boards in the Feather family here.](https://www.adafruit.com/feather)

**This is the 900 MHz radio version, which can be used for either 868MHz or 915MHz transmission/reception** - the exact radio frequency is determined when you load the software since it can be tuned around dynamically.

At the Feather M0's heart is an ATSAMD21G18 ARM Cortex M0 processor, clocked at 48 MHz and at 3.3V logic, the same one used in the new [Arduino Zero](https://www.adafruit.com/products/2843). This chip has a whopping 256K of FLASH (8x more than the Atmega328 or 32u4) and 32K of RAM (16x as much)! This chip comes with built in USB so it has USB-to-Serial program & debug capability built in with no need for an FTDI-like chip.

To make it easy to use for portable projects, Adafruit added a connector for 3.7V Lithium polymer batteries and built in battery charging. You don't need a battery, it will run just fine straight from the micro USB connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when its available. The battery is tied thru a divider to an analog pin, so you can measure and monitor the battery voltage to detect when you need a recharge.

**Here's some handy specs! Like all Feather M0's you get:**

*   Measures 2.0" x 0.9" x 0.3" (51mm x 23mm x 8mm) without headers soldered in
*   Light as a (large?) feather - 5.8 grams
*   ATSAMD21G18 @ 48MHz with 3.3V logic/power
*   No EEPROM
*   3.3V regulator with 500mA peak current outpu0t
*   USB native support, comes with USB bootloader and serial port debugging
*   You also get tons of pins - 20 GPIO pins
*   Hardware Serial, hardware I2C, hardware SPI support
*   8 x PWM pins
*   10 x analog inputs
*   1 x analog output
*   Built in 100mA lipoly charger with charging status indicator LED
*   Pin #13 red LED for general purpose blinking
*   Power/enable pin
*   4 mounting holes
*   Reset button

The **Feather M0 Radio** uses the extra space left over to add an RFM69HCW 433 or 900MHz radio module. These radios are not good for transmitting audio or video, but they do work quite well for small data packet transmission when you need more range than 2.4 GHz (BT, BLE, WiFi, ZigBee)

*   SX1231 based module with SPI interface
*   Uses the license-free ISM band ("European ISM" @ 868MHz or "American ISM" @ 915MHz)
*   +13 to +20 dBm up to 100 mW Power Output Capability (power output selectable in software)
*   50mA (+13 dBm) to 150mA (+20dBm) current draw for transmissions
*   Range of approx. 350 meters, depending on obstructions, frequency, antenna and power output
*   Create multipoint networks with individual node addresses
*   Encrypted packet engine with AES-128
*   Simple wire antenna or spot for uFL connector

Comes fully assembled and tested, with a USB bootloader. Includes some headers so you can solder it in and plug into a solderless breadboard. You will need to cut and solder on a small piece of wire (any solid or stranded core is fine) in order to create your antenna.

## Purchase
* [Adafruit](https://www.adafruit.com/product/3176)

## Contribute

Have some info to add for this board? Edit the source for this page [here](https://github.com/adafruit/circuitpython-org/edit/master/_board/{{ page.board_id }}.md).
