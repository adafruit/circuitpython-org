#!/usr/bin/python3
from pathlib import Path
import frontmatter

# Check CircuitPython Download Features
with open('template.md', "rt") as f:
    metadata, content = frontmatter.parse(f.read())
    acceptable_features = set(metadata['features'])

failed = False
for filename in Path('_board').glob("*.md"):
    with open(filename, "rt") as f:
        metadata, content = frontmatter.parse(f.read())
    features = metadata.get('features') or ()
    for feature in sorted(set(features) - acceptable_features):
        print(f"{filename}:0: Non-standard feature: {feature}")
        failed = True

if failed:
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-downloads for acceptable features")
    raise SystemExit(failed)

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

failed = False
for filename in Path('_blinka').glob("*.md"):
    with open(filename, "rt") as f:
        metadata, content = frontmatter.parse(f.read())
    features = metadata.get('features') or ()
    for feature in sorted(set(features) - blinka_features):
        print(f"{filename}:0: Non-standard feature: {feature}")
        failed = True

if failed:
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-blinka for acceptable features")

raise SystemExit(failed)
