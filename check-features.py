#!/usr/bin/python3
from pathlib import Path
import frontmatter

# Check CircuitPython Download Features
with open('template.md', "rt") as f:
    metadata, content = frontmatter.parse(f.read())
    acceptable_features = set(metadata['features'])

def verify_features(folder, valid_features):
    success = True
    for filename in Path(folder).glob("*.md"):
        with open(filename, "rt") as f:
            metadata, content = frontmatter.parse(f.read())
        features = metadata.get('features') or ()
        for feature in sorted(set(features) - valid_features):
            print(f"{filename}:0: Non-standard feature: {feature}")
            success = False
    return success

if not verify_features("_board", acceptable_features):
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-downloads for acceptable features")
    raise SystemExit(True)

# Check Blinka Download Features
blinka_features = {
    "Ethernet",
    "HDMI",
    "Wi-Fi",
    "40-pin GPIO",
    "GPS",
    "Feather-Compatible",
    "Bluetooth/BLE",
    "STEMMA QT/QWIIC",
    "USB 3.0",
    "Infrared Receiver",
}

failed = not verify_features("_blinka", blinka_features)
if failed:
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-blinka for acceptable features")

raise SystemExit(failed)
