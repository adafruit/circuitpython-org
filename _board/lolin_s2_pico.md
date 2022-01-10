---
layout: download
board_id: "lolin_s2_pico"
title: "LOLIN S2 Pico Download"
name: "LOLIN S2 Pico"
manufacturer: "LOLIN"
board_url: "https://www.wemos.cc/en/latest/s2/s2_pico.html"
board_image: "lolin_s2_pico.jpg"
date_added: 2021-11-2
family: esp32s2
bootloader_id: lolin_s2_pico
features:
  - Wi-Fi
  - USB-C
  - Display
  - Breadboard-Friendly

---

### Features

- ESP32-S2FN4R2 WiFi SoC
    - Xtensa® single-core 32-bit LX7 microprocessor, up to 240 MHz
    - Integrated 802.11 b/g/n WiFi 2.4GHz Transceiver, up to 150Mbps
    - Integrated RISC-V ULP Coprocessor
    - Integrated Temperature Sensor (-20°C to 110°C)
    - Operating Voltage: 3.0 to 3.6V
        - WiFi: 310mA (peak)
        - Modem-sleep: 12-19mA
        - Light-Sleep: 450µA
        - Deep-Sleep: 20-190µA
    - 320 KB SRAM
    - 4 MB Flash (embedded)
    - 2 MB PSRAM (embedded)
    - 16 KB SRAM in RTC (accessable by main CPU, 8 KB accessable by ULP coprocessor)
    - 4 Kbit eFuse (1792 bits reserved for user data)
    - 2 × 13-bit SAR ADCs, up to 20 channels (2 channels not available on ADC2 due to USB D+/D-)
    - 2 × 8-bit DAC
    - 14 × touch sensing IOs
    - 4 × SPI (2 usable due to embedded flash & PSRAM)
    - 1 × I2S
    - 2 × I2C
    - 2 × UART
    - 1 × DVP 8/16 camera interface, implemented using the hardware resources of I2S
    - 1 × LCD interface (8-bit serial RGB/8080/6800), implemented using the hardware resources of SPI2
    - 1 × LCD interface (8/16/24-bit parallel), implemented using the hardware resources of I2S
    - 1 × TWAI® controller compatible with ISO 11898-1 (CAN Specification 2.0)
    - LED PWM controller, up to 8 channels
    - USB OTG 1.1 controller and PHY, with host and device support
    - Cryptographic Hardware Accelerators: AES, ECB/CBC/OFB/CFB/CTR, GCM, SHA, RSA, ECC (Digital Signature)
- USB Type-C connector, for built-in ROM USB bootloader, serial port debugging, and USB device mode
- 3.3V regulator ME6211C33
    - Maximum Output Current: 500mA （V<sub>IN</sub>＝4.3V, V<sub>OUT</sub>＝3.3V）
    - Dropout Voltage: 100mV@ I<sub>OUT</sub>＝100 mA
    - Operating Voltage Range: 2V～6.0V
    - Low Power Consumption: 40µA（typ.）
    - Standby Current: 0.1µA（typ.）
- 27 × GPIO pins, plus `VBUS`, `3V3`, `GND`
    - 21 × pins broken out to breadboard-friendly headers
    - `EN` RESET button
    - `GPIO0` BOOT button
    - `GPIO10` LED (blue status LED)
    - Lolin I2C JST SH 4-pin port (not QWIIC/Stemma-Qt pinout) using GPIO8 (SDA)/GPIO9 (SCL)
    - 128 x 32 SSD1306 OLED display internally connected to the same I2C bus as the external port, reset pin connected to GPIO18
- Compatible with CircuitPython, MicroPython (default firmware), Arduino and ESP-IDF

## Purchase

* [AliExpress](https://www.aliexpress.com/item/1005003215673294.html)

## Learn More

* [Manufacturer Specifications](https://www.wemos.cc/en/latest/s2/s2_pico.html)
