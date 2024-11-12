---
layout: download
board_id: "adafruit_qualia_s3_rgb666"
title: "Qualia ESP32-S3 for TTL RGB-666 Displays Download"
name: "Qualia ESP32-S3 for TTL RGB-666 Displays"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5800"
board_image: "adafruit_qualia_s3_rgb666.jpg"
date_added: 2023-10-03
family: esp32s3
bootloader_id: adafruit_qualia_s3_rgb666
tags:
  - Qualia S3
download_instructions: https://learn.adafruit.com/adafruit-qualia-esp32-s3-for-rgb666-displays/circuitpython-5
features:
  - External Display
  - Wi-Fi
  - Bluetooth/BTLE
  - STEMMA QT/QWIIC
  - USB-C
---

There's a few things everyone loves: ice cream, kittens, and honkin' large TFT screens. We're no strangers to small TFT's - [from our itsy 1.14" color display](https://www.adafruit.com/search?q=1.14+tft) that graces many-a-TFT-Feather to [our fancy 3.5" 320x480](https://www.adafruit.com/product/2050) breakout screen. But most people who dabble or engineer with microcontrollers know that you sort of 'top out' at 320x480 - that's the largest resolution you can use with every day SPI or 8-bit 8080 interfaces. After that, you're in TTL-interface TFT land, where displays no longer have an internal memory buffer and instead the controller has to continuously write scanline data over a 16 or 18 or 24 pin interface.

RGB TTL interface TFT displays can get big: they start out at around 4.3" diagonal 480x272, and can get to 800x480, 800x600 or even 720x720. For displays that big, you need a lot of video RAM (800x480 at 24 bit color is just over 1MB), plenty of spare GPIO to dedicate, and a peripheral that will DMA the video RAM out to the display continuously. This is a setup familiar to people working with hefty microcontrollers or microcomputers, the sort of device that run cell phones, or your car's GPS navigation screen. But until now, nearly impossible to use on low cost microcontrollers.

The ESP32-S3 is the first low-cost microcontroller that has a built in peripheral that can drive TTL displays, and can come with enough PSRAM to buffer those large images. For example, on the **Adafruit Qualia ESP32-S3 for TTL RGB-666 Displays**, we use a S3 module with 16 MB of Flash and 8 MB of octal PSRAM. Using the built in RGB display peripheral you can display graphics, images, animations or even video (cinepak, natch!) with near-instantaneous updates since the whole screen gets updated every ~30FPS.

This dev board is designed to make it easy for you to explore displays that use the "secondary standard' 40-pin RGB-666 connector. This pin order is most commonly seen on square, round and bar displays. [You'll want to compare the display you're using to this datasheet](https://cdn-shop.adafruit.com/product-files/5792/Specification_TL021WVC02CT-B1323B.pdf), if it matches you'll probably be good! One nice thing about this connector ordering is that it also includes pins for capacitive touch overlay, and we wire those up to the ESP32-S3's I2C port so you can also have touch control with your display.

**Don't forget! This is just the development board, a display is not included.** Use any RGB-666 pinout display with or without a touch overlay. Note that you will need to program in the driver initialization code, dimensions, and pulse widths in your programming language. Here are some known-working displays that you can use in Arduino or CircuitPython:

- [2.1" 480x480 Round with Capacitive Touch](https://www.adafruit.com/product/5792)
- [2.1" 480x480 Round without touch](https://www.adafruit.com/product/5806)
- [4" 720x720 Square with Capacitive Touch](https://www.adafruit.com/product/5794)
- [4" 720x720 Round without touch](https://www.adafruit.com/product/5793)
- [4.6" 960x320 Rectangular Bar](https://www.adafruit.com/product/5805)

On the Qualia board we have the S3 modules, with 16 pins connected to the TFT for 5-6-5 RGB color, plus HSync, VSync, Data Enable and Pixel Clock. There's a constant current backlight control circuit using the [TPS61169](https://www.ti.com/product/TPS61169/part-details/TPS61169DCKR) which can get up to 30V forward voltage and can be configured for 25mA-200mA in 25mA increments (default is 25mA). Power and programming is provided over a USB C connector, wired to the S3's native USB port. For debugging, the hardware UART TX pin is available as well.

Since almost every GPIO is used, and almost all RGB-666 displays need to be initialized over SPI, we put a [PCA9554](https://www.ti.com/product/PCA9554) I/O expander on the shared I2C bus. Arduino or CircuitPython can be instructed on how to use the expander to reset and init the display you have if necessary. The remaining expander pins are connected to two right-angle buttons, and the display backlight.

The expander is what lets us have a full 4-pin SPI port and two more analog GPIO pins - [enough to wire up an MMC in 1-wire SDIO mode along with an I2S amplifier to make an A/V playback demo](https://www.youtube.com/watch?v=pEjw-bCQ-lQ). Maybe we can even eat ice cream while watching kitten vids! There is also the shared I2C port, we provide a Stemma QT / Qwiic port for easy addition of any sensor or device you like.

## Purchase:

* [Adafruit](https://www.adafruit.com/product/5800)