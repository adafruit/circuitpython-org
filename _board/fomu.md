---
layout: download
board_id: "fomu"
title: "Fomu Download"
name: "Fomu"
manufacturer: Sean Cross (xobs)
board_url:
 - "https://tomu.im/fomu.html"
 - "https://www.adafruit.com/product/4332"
board_image: "fomu.jpg"
date_added: 2020-04-16
family: litex
---

Only 13mm long, **Fomu** really puts the _micro_ in microprocessor. Fomu is a fully open-source, programmable FPGA device that sits inside a USB Type-A port. It has four buttons, an RGB LED, and an FPGA that is compatible with a fully open source chain and capable of running a RISC-V core. Fomu comes in a custom plastic enclosure that slots perfectly into a USB port.

Fomu:

 * **has Python**
   * With 128 kilobytes of RAM and a large amount of storage, Fomu is powerful enough to run Python natively. And since it lives in your USB port, installation is super simple. FPGAs are complicated, but the latest Python tools make it easy to use Fomu without any specialized training.
 * **runs RISC-V**
   * Underneath the Python interpreter lies a RISC-V softcore running on the FPGA fabric. RISC-V is an up-and-coming processor architecture that is poised to take over everything from deeply-embedded chips to high-performance computing. Fomu’s RISC-V softcore is a great introduction to the processor architecture of the future.
 * **is an FPGA**
   * An FPGA is a piece of reconfigurable silicon. The default Fomu firmware exposes a USB bootloader running a RISC-V softcore, but you can load whatever you want. Softcores are also available for LM32 and OpenRISC. You can practice adding instructions to the CPU, or add new blocks such as LED blink patterns or better captouch hardware blocks.
 * **is entirely open**
   * Developing with Fomu is incredibly easy: just load code via USB and go. Whether you’re writing RISC-V code, Python code, or HDL, it’s all uploaded to Fomu in the same way. The ICE40UP5K FPGA is supported with a fully open toolchain, meaning you can start development without creating an account, signing an NDA, or downloading a multi-gigabyte installer.
An FPGA is an Array of Gates that is Field-Programmable. When you buy a chip such as a CPU, the logic cells are all fixed in place. A CPU can run any amount of code, but if you want to do anything exotic you need to create software and, depending on what you want to do, that software can be very slow.

For example, many embedded projects use WS2812 LEDs such as [NeoPixels](https://www.adafruit.com/?q=WS2812) that require a specialized timing signal. A CPU can generate this signal in software, but it can’t do anything in the background while talking to the light. If the string of LEDs is very long, then the CPU wastes a lot of time and power generating the signal.

With an FPGA, it becomes possible to create an “LED driver” that allows the CPU to keep running while a hardware component handles the timing. The CPU could do other work, or could put itself in a low power state.

In fact, the “CPU” in the FPGA is created from a hardware description language, meaning it can be modified or swapped out. If you wanted, you could create a brand-new CPU instruction. Do you want to have fast 64-bit multiplies? Or maybe you want a way to get random numbers easily? With Fomu and its FPGA, you have the source code to the CPU itself.

## Purchase
* [Adafruit](https://www.adafruit.com/product/4332)
