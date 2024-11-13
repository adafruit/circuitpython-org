---
layout: download
board_id: "adafruit_feather_esp32_v2"
title: "Adafruit Feather ESP32 V2 Download"
name: "Adafruit Feather ESP32 V2"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5400"
board_image: "adafruit_feather_esp32_v2.jpg"
date_added: 2022-08-19
family: esp32
downloads_display: true
download_instructions: https://learn.adafruit.com/adafruit-esp32-feather-v2/circuitpython
features:
  - Feather-Compatible
  - Battery Charging
  - Bluetooth/BTLE
  - Wi-Fi
  - USB-C
  - Breadboard-Friendly
  - STEMMA QT/QWIIC
---

One of our star Feathers is the [Adafruit HUZZAH32 ESP32 Feather](https://www.adafruit.com/product/3405) - with the fabulous ESP32 WROOM module on there, it makes quick work of WiFi and Bluetooth projects that take advantage of Espressifs most popular chipset. Recently we had to redesign this feather to move from the obsolete CP2104 to the available CH9102F and one thing led to another and before you know it we made a completely refreshed design: the **Adafruit ESP32 Feather V2**.

The V2 is a significant redesign, enough so we consider it a completely new product. It *still* features the ESP32 chip but has many upgrades and improvements:

- Compared to the original Feather with 4 MB Flash and no PSRAM, the V2 has **8 MB Flash and 2 MB PSRAM**
- Additional **user button tactile switch** on input pin 38
- Additional **NeoPixel mini RGB LED** with controllable power pin
- Additional **STEMMA QT** port for plug and play I2C connections
- **USB Type C** port instead of Micro B
- **Separate controllable 3.3V power supply for STEMMA QT** to allow for ultra low power consumption even with sensors are attached
- Designed for low power usage: [verified with a PPK](https://www.adafruit.com/product/5048) to **draw 70uA from the Lipoly battery in deep sleep** and 1.2mA in light sleep.
- ESP32 Pico module is much smaller, allowing for clear marking of all breakout pads and additional mounting holes!
- Upgrade the USB to serial converter from CP2102 to CH9102F which is available for purchase! The CH9102F has no issues with uploading at 921600 bps for speedy firmware loading.

However, in order to add the PSRAM, and use the new Pico module which was small enough to allow all the fun extras, some of the breakout pads have changed, so here's what you need to know:

- The pin *numbers* for the I2C port (SDA, SCL), hardware UART (RX, TX), and SPI (SCK, MOSI, MISO) have changed. If your code has hardcoded use for those pins, you'll want to replace them either by the new numbers or change the code to use the 'pretty' names like SDA or SCK.
  When selecting the new Feather ESP32 V2 board in the Espressif board support package, the correct numbers will be substituted.
  Note the names are in the same spots, we haven't changed where the I2C/UART/SPI pins are located on the board, just which ESP32 pin numbers they are connected to in the module.
- The 'corner' pin next to TX has changed from pin 21 to 37. This pin is not used in any FeatherWings because its considered an 'extra pin'. It's also changed from a GPIO to input-only
- The remaining numbered pins and A0-A5 pins have not changed pin numbers.

That module nestled in at the end of this Feather contains a dual-core ESP32 chip, 8 MB of SPI Flash, 2 MB of PSRAM, tuned PCB antenna, and all the passives you need to take advantage of this powerful new processor. The ESP32 has both WiFi *and* Bluetooth Classic/LE support. That means it's perfect for just about any wireless or Internet-connected project.

Because it's part of our [Feather eco-system, you can take advantage of the 50+ Wings](https://www.adafruit.com/category/814) that we've designed to add all sorts of cool accessories. Plus that built in battery charging and monitoring you know and love with the ESP32 Feather is still there in this upgrade.



**Features:**

- **ESP32 Dual core 240MHz Xtensa®** **processor** - the classic dual-core ESP32 you know and love!
- **Mini module** has FCC/CE certification and comes with 8 MByte of Flash and 2 MByte of PSRAM - you can have huge data buffers
- **Power options** - USB type C **or** Lipoly battery
- **Built-in battery charging** when powered over USB-C
- **LiPoly battery monitor** with two 200K resistor divider
- **Reset and User** (I38) buttons to reset board and as a separate input
- **High speed upload with auto-reset and serial debug** with ultra-reliable CP2102N chipset.
- **STEMMA QT** connector for I2C devices, with switchable power, so you can go into low power mode.
- **Charge/User** LEDs + status **NeoPixel** with pin-controlled power for low power usage
- **Low Power friendly**! In deep sleep mode we can get down to 80~100uA of current draw from the Lipoly connection. Quiescent current is from the power regulator, ESP32 chip, and Lipoly monitor. Turn off the NeoPixel and external I2C power for the lowest quiescent current draw.
- **Works with Arduino or MicroPython**

Comes fully assembled and tested, with a USB interface that lets you quickly use it with the Arduino IDE or the low-level ESP32 IDF. We also toss in some header so you can solder it in and plug into a solderless breadboard. **Lipoly battery and USB cable not included** (but we do have lots of options in the shop if you'd like!)

## Purchase

* [Adafruit](https://www.adafruit.com/product/5400)
