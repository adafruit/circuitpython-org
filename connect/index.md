---
layout: common
---

# Overview

Starting with CircuitPython 7, there are a couple of ways of connecting to a CircuitPython board and editing files. We call these "workflows". The classic workflow is over USB where the CircuitPython board appears as a `CIRCUITPY` drive with all of the code files on it. The second way to connect is wirelessly over Bluetooth Low Energy (BLE). Unlike USB, BLE works better with phones and tablets.

## USB

To connect to CircuitPython over USB, connect the USB cable from the CircuitPython board to your computer. The two most common mistakes are:

1. Expecting CIRCUITPY before loading CircuitPython onto the device.
1. Using a USB cable that only connects the power wires. Double check any new cable with a working device. With your first device, try multiple cables.

See the [Welcome to CircuitPython guide](https://learn.adafruit.com/welcome-to-circuitpython) for more details and troubleshooting.

## BLE

Bluetooth Low Energy (BLE) doesn't have standard for transferring files. As a result, operating systems don't have built in support for the protocol CircuitPython uses. Instead, you'll need to use an app or webpage designed for the file transfer protocol.

### PyLeap

PyLeap is an iOS app by Adafruit designed to quickly get you started by loading existing projects onto your device. These projects are from [learn.adafruit.com](https://learn.adafruit.com).

Get PyLeap through Apple's beta testing app TestFlight [here](https://adafru.it/pyleap).

PyLeap is openly developed [on GitHub](https://github.com/adafruit/PyLeap-iOS).

### File Glider

File Glider is an iOS app by Adafruit designed to interoperate with iOS's files API. Files can be edited directly in File Glider or indirectly in other Files API compatible apps. The app is not CircuitPython specific so it can be used with any file transfer capable device.

Get File Glider through Apple's beta testing app TestFlight [here](https://adafru.it/file-glider).

File Glider is openly developed [on GitHub](https://github.com/adafruit/Glider-for-iOS).

### code.circuitpython.org

[code.circuitpython.org](https://code.circuitpython.org) is a webapp designed by Adafruit to edit files over WebBluetooth in Chrome. This works on the latest Chrome on desktop and on Android.

Go to [code.circuitpython.org](https://code.circuitpython.org) to get started.

The web editor is openly developed [on GitHub](https://github.com/circuitpython/web-editor).
