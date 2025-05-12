---
layout: download
board_id: "challenger_rp2040_sdrtc"
title: "Challenger RP2040 SD/RTC Download"
name: "Challenger RP2040 SD/RTC"
manufacturer: "Invector Labs"
board_url:
 - "https://ilabs.se/product/challenger-rp2040-sd-rtc/"
board_image: "challenger_rp2040_sdrtc.jpg"
date_added: 2022-12-23
family: rp2040
download_instructions: https://ilabs.se/product/challenger-rp2040-sd-rtc/#tab-getting-started
features:
  - USB-C
  - Breadboard-Friendly
  - Feather-Compatible
  - Battery Charging
---

The Challenger RP2040 SD/RTC is an Arduino/Circuitpython compatible Adafruit Feather format micro controller board based on the Raspberry Pico chip. This board is equipped with an micro SD card reader and a Real Time Clock making it super useful for data logging applications.

RP2040 is the debut micro controller from Raspberry Pi. It brings their signature values of high performance, low cost, and ease of use to the micro controller space. With a large on-chip memory, symmetric dual-core processor complex, deterministic bus fabric, and rich peripheral set augmented with our unique Programmable I/O (PIO) subsystem, RP2040 provides professional users with unrivaled power and flexibility. With detailed documentation, a polished Circuitpython port, and a UF2 boot loader in ROM, it has the lowest possible barrier to entry for beginner and hobbyist users

This board is equipped with a micro SD card connector that will house standard micro SD cards allowing your application to have many gigabytes of storage room for sensor data or what ever you want to place on it. Together with a fancy display you could also store cool images.

It is normally very useful to tag sensor data with a time stamp so we included a Real Time Clock chip to make this easy for you.

The chip we use is the MCP79410 general purpose I2C™Compatible real-time clock/calendar. It is a highly integrated real time clock with nonvolatile memory and many other advanced features. These features include a battery switchover circuit for backup power, a timestamp to log power failures and digital trimming for accuracy. Using a low-cost 32.768 kHz crystal or other clock source, time is tracked in either a 12-hour or 24-hour format with an AM/PM indicator and timing to the second, minute, hour, day of the week, day, month and year. As an interrupt or wakeup signal, a multifunction open drain output can be programmed as an Alarm Out or as a Clock Out that supports 4 selectable frequencies.

The intperrupt output from the RTC is connected to pin GPIO25 on the RP2040 and can be used to wake up the device repeatedly to collect data.

In the recent years we have noticed that we are seeing more and more USB Type C cable laying around the lab due to the fact that all new phones and accessories use them. As of yet we haven’t seen any shortage of micro USB cables but we are not getting any new ones any more and old ones do break occasionally. So we decided to go for a USB Type C connector for this board. A bonus of this is that they are quite bit more durable and you don’t have to fiddle with the cable when plugging it in.

The board is equipped with a standard 2.0mm JST connector for connecting a rechargeable LiPo battery. There is also an internal battery charger circuit that charges your battery as long as a USB cable is inserted or the VUSB connection is connected to 5V.

## Purchase

* [Invector Labs)](https://ilabs.se/product/challenger-rp2040-sd-rtc/)
