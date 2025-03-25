---
layout: download
board_id: "adafruit_fruit_jam"
title: "Fruit Jam - Mini RP2350 Computer Download"
name: "Fruit Jam - Mini RP2350 Computer"
manufacturer: "Adafruit"
board_url:
    - "https://www.adafruit.com/product/6200"
board_image: "adafruit_fruit_jam.jpg"
date_added: 2025-03-19
family: rp2350
features:
  - STEMMA QT/QWIIC
  - USB-C
  - External Display
  - USB Host
  - Speaker

---

We were catching up on a recent [hackaday hackchat with eben upton](https://hackaday.io/event/202122-raspberry-pi-hack-chat-with-eben-upton) and learned some fun facts: such as the DVI hack for the RP2040 was inspired by [a device called the IchigoJam](https://www.hackster.io/news/ichigojam-combines-strawberry-and-raspberry-to-deliver-a-raspberry-pi-pico-powered-educational-micro-66aa5d2f6eec). we remember reading about this back when it was an LPC1114, now it uses an RP2040. well, we're wrapping up the [Metro RP2350](https://www.adafruit.com/product/6003) and lately we've been joking around that with DVI output and USB Host support via bit-banged PIO, you could sorta build a little stand-alone computer.

Well, one pear-green-tea-fueled-afternoon later we tried our hand at designing a 'credit card sized' computer - that's 3.375" x 2.125", [about the same size as a business card](https://hackaday.com/2024/05/07/the-2024-business-card-challenge-starts-now/) and turns out there's even a standard named for it: [ISO/IEC 7810 ID-1](https://www.iso.org/standard/70483.html).

Anyhow, with the extra pins of the QFN-80 RP2350B, we're able to jam a ridonkulous amount of hardware into this shape:

- RP2350B dual 150MHz Cortex M33
- PicoProbe debug port
- 16 MB Flash + 8 MB PSRAM - the PSRAM will help when we want do do things like run emulations that we need to store in fast RAM access, and also let us use the main SRAM as the DVI video buffer.
- USB type C for bootloading/USB client
- Micro SD card with SPI or SDIO
- DVI output on the HSTX port
- I2S stereo headphone + mono speaker via the [TLV320DAC3100](https://www.digikey.com/en/products/detail/texas-instruments/tlv320dac3100irhbt/2353656)
- 2-port USB type A hub for both keyboard and mouse or game controllers
- Chunky on-off switch
- Stemma QT I2C
- Stemma classic JST 3-pin
- EYESPI for TFT displays
- 5x NeoPixels
- 3x tactile switches
- 16-pin socket header with 10 A/D GPIO + 5V/3V/GND power pins.

## Purchase

* [Adafruit](https://www.adafruit.com/product/6200)