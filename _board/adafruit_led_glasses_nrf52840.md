---
layout: download
board_id: "adafruit_led_glasses_nrf52840"
title: "LED Glasses Download"
name: "LED Glasses "
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5217"
 - "https://www.adafruit.com/product/5255"
board_image: "adafruit_led_glasses_nrf52840.jpg"
date_added: 2021-09-03
family: nrf52840
bootloader_id: ledglasses_nrf52840
download_instructions: https://learn.adafruit.com/adafruit-eyelights-led-glasses-and-driver/circuitpython
features:
  - USB-C
  - Bluetooth/BTLE
  - Battery Charging
  - STEMMA QT/QWIIC
  - Breadboard-Friendly
---

This board is designed to be a thin, bluetooth-enabled driver board for our [Adafruit LED Glasses](https://www.adafruit.com/product/5210) RGB LED matrix. That said, it's a perfectly good stand-alone development board for the Nordic nRF52840 chipset, with a very slim design, optional LiPo battery support, a few sensors, and a Stemma QT port for adding other devices or sensors with I2C plug-and-play.

The driver *looks* a little like a Feather but it does not have any breakout pins to keep it very compact. If you need access to GPIO pins, we recommend an [nRF52840 ItsyBitsy](https://www.adafruit.com/product/4481), [nRF52840 Feather](https://www.adafruit.com/product/4062) or [Feather Sense](https://www.adafruit.com/product/4516).

In exchange for GPIO outputs, we added some sensors on instead: each board [comes with a LIS3DH triple-axis accelerometer](https://www.adafruit.com/product/2809) that can be used for motion and orientation sensing, [and a PDM digital microphone](https://www.adafruit.com/product/3492) for audio sensing. To add more sensors or connect to the LED Glasses front panel, there's a [STEMMA QT connector for plug-and-play I2C support](https://www.adafruit.com/category/1018).

Unlike our Itsy/Feather boards, this driver also comes with a proper on/off switch which will cut power to the microcontroller and external sensors. There's optional LiPo charge support because we think that many folks will want to power this board with AAA or coin cell batteries. If you'd like to enable LiPo charging, short the jumper on the back and then make sure to only use 4.2 V/3.7 V rechargeable batteries in the battery port.

The nRF52840 is a lovely Bluetooth LE microcontroller, with good support in both Arduino and CircuitPython. It feathers a Cortex M4 processor with 1 MB of FLASH and 256 KB of SRAM. Best of all, it's got that native USB! Finally, no need for a separate USB serial chip like CP2104 or FT232. Serial is handled as a USB CDC descriptor, and the chip can act like a keyboard, mouse, MIDI device or even disk drive. [This chip has TinyUSB support](https://github.com/adafruit/Adafruit_TinyUSB_Arduino) - that means you can use it with Arduino as a native USB device and act as UART (CDC), HID, Mass Storage, MIDI and more!

## Technical details

- ARM Cortex M4F (with HW floating point acceleration) running at 64 MHz
- 1 MB flash and 256 KB SRAM
- Bluetooth Low Energy compatible 2.4GHz radio (Details available in the [nRF52840](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52840) product specification)
- FCC/IC/TELEC certified module with up to +8 dBm output power
- 2 MB external QSPI flash for CircuitPython file storage
- Built in LIS3DH accelerometer and PDM microphone
- Red LED for general purpose blinking, plus a tiny NeoPixel for colorful feedback
- [STEMMA QT connector for plug-and-play I2C support](https://www.adafruit.com/category/1018).
- JST PH 2-pin battery port with optional LiPoly charger
- 4 mounting holes/slots
- Reset button and User button
- Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
- Can be used with Arduino IDE or CircuitPython
- Comes pre-loaded with the [UF2 bootloader](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader), which looks like a USB storage key. Simply drag firmware on to program, no special tools or drivers needed! It can be used to load up CircuitPython or Arduino IDE

For developers, we pre-programed the chip with our UF2 bootloader, which can use either command line UART programming with nrfutil (we use this for Arduino) or drag-n-drop mass storage, for CircuitPython installation and also because mass-storage-drive bootloaders make updating firmware so easy. Want to program the chip directly? You can use our command line tools with your favorite editor and toolchain. If you want to use an SWD programmer/debugger (for even more advanced usage), we have broken out the SWD pads for easy soldering.

## Purchase

* [Adafruit](https://www.adafruit.com/product/5217)
