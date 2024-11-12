---
layout: download
board_id: "adafruit_proxlight_trinkey_m0"
title: "Proximity Trinkey - SAMD21 Download"
name: "Proximity Trinkey - SAMD21"
manufacturer: "Adafruit"
board_url:
 - "https://www.adafruit.com/product/5022"
board_image: "adafruit_proxlight_trinkey_m0.jpg"
date_added: 2021-04-14
family: atmel-samd
bootloader_id: proxsense_trinkey_m0
download_instructions: https://learn.adafruit.com/adafruit-proximity-trinkey/circuitpython
features:

---

It's half USB Key, half [Adafruit Trinket M0](https://www.adafruit.com/product/3500), half [APDS9960 breakout](https://www.adafruit.com/product/3595)*...*it's **Proximity Trinkey**, the circuit board with a Trinket M0 heart, APDS9960 Proximity, Light, RGB, and Gesture Sensor, and two RGB NeoPixels for a customizable glow. We wanted to make it super-easy to add one of our most popular combination-sensors to any computer with a USB port and this one is ready to go in an instant.

The PCB is designed to slip into any USB A port on a computer or laptop. There's an ATSAMD21 microcontroller on board with just enough circuitry to keep it happy. One pin of the microcontroller connects to the two NeoPixel LEDs. Two other pins are used as capacitive touch inputs on the end - if you look carefully you can see the slotted end has left and right touch pads. A reset button lets you enter bootloader mode if necessary. That's it!

The SAMD21 can run CircuitPython or Arduino very nicely - both have existing APDS9960, NeoPixel and our FreeTouch (capacitive touch) libraries. Over the USB connection, you can have serial, MIDI, or HID connectivity. The Proximity Trinkey is perfect for simple projects that want to use motion, light or color sensing as an input to make fun and intuitive user experiences.

The star of this Trinkey is the APDS9960 from Avago Technologies, which has a few different capabilities thanks to integrated IR LED, photodiodes, and RGB sensing:

- **Proximity sensing** up to about 6" away by bouncing IR light off an object
- **RGB color sensing** can detect color when light refects off of an object - good for bright colorful items like LEGO bricks
- **Ambient light sensing** - how dark or bright is it in the room?
- **Basic gesture sensing** using 4 cardinal locations of photodiodes - this sensor is a little tough to use but it does work with practice
- Configurable interrupt pin that can fire when a certain proximity threshold is broken, or when a color sensor breaks a certain threshold.

We think it's just an adorable little board, small and durable and inexpensive enough that it could be a first microcontroller board or inspiration for advanced developers to make something simple and fun.

## Technical details

- ATSAMD21E18 32-bit Cortex M0+ - 48 MHz 32 bit processor with 256 KB Flash and 32 KB RAM
- Native USB supported by every OS - can be used in Arduino or CircuitPython as USB serial console, MIDI, Keyboard/Mouse HID, even a little disk drive for storing Python scripts.
- Can be used with Arduino IDE or CircuitPython
- 2 RGB NeoPixel LEDs
- 2 Capacitive Touchpads
- APDS9960 Light/Color/Proximity/Gesture sensor
- Reset switch for starting your project code over or entering bootloader mode
- Slim and cute, keychain-friendly!

## Purchase

* [Adafruit](https://www.adafruit.com/product/5022)
