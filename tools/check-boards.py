#!/usr/bin/python3
import datetime
import os
import json
import re
from pathlib import Path
import frontmatter

# Check CircuitPython Download Features
with open('template.md', "rt") as f:
    metadata, content = frontmatter.parse(f.read())
    acceptable_features = set(metadata['features'])

def get_files(folder):
    return sorted(Path(folder).glob("*.md"), key=os.path.basename)

def verify_board_id(folder):
    valid = True
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue
            if not board_id:
                print(f"board_id should be set for {filename}")
                valid = False

    return valid

def valid_date(date):
    return isinstance(date, datetime.date)

def verify_features(folder, valid_features):
    valid = True
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue
            features = metadata.get('features') or ()
            for feature in sorted(set(features) - valid_features):
                print(f"{filename}:0: Non-standard feature: {feature}")
                valid = False
    return valid

def verify_family(folder):
    valid = True
    with open('./_data/bootloaders.json') as bl_file:
        bootloaders = json.load(bl_file)
        valid_bootloaders = bootloaders["bootloaders"].keys()
        for filename in get_files(folder):
            with open(filename, "rt") as f:
                metadata, _ = frontmatter.parse(f.read())
            downloads_display = metadata.get('downloads_display')
            if downloads_display is None or downloads_display:
                board_id = metadata.get('board_id') or ()
                if board_id == "unknown":
                    continue
                family = metadata.get('family')
                if family is None:
                    print(f"Family field is missing for {board_id}")
                    valid = False
                elif family not in valid_bootloaders:
                    print(f"Family field value of {family} for {board_id} is invalid.")
                    valid = False
    return valid

def verify_date_added(folder):
    valid = True
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_id = metadata.get('board_id') or ()
            if board_id == "unknown":
                continue
            date_added = metadata.get('date_added')
            if date_added is None:
                print(f"date_added field is missing for {board_id}")
                valid = False
            elif not valid_date(date_added):
                print(f"{date_added} is an invalid date for {board_id}. The format must be YYYY-MM-DD, using leading zeros if necessary")
                valid = False
    return valid

def verify_contribute_not_present(folder):
    valid = True
    contribute = re.compile(r".*\n## Contribute", re.MULTILINE | re.DOTALL)
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, content = frontmatter.parse(f.read())
        board_id = metadata.get('board_id') or ()
        result = contribute.match(content)
        if result is not None:
            print(f"Contribute Section found for {board_id} in {folder}")
    return valid

def verify_blinka_board(folder):
    # Check that blinka flag is set for all boards in the folder
    valid = True
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_id = metadata.get('board_id') or ()
            if board_id == "unknown":
                continue
            blinka_flag = metadata.get('blinka')
            if blinka_flag is None or blinka_flag == False:
                print(f"blinka field is not set to True for {board_id}")
                valid = False
    return valid

if not verify_features("_board", acceptable_features):
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-downloads for acceptable features")
    raise SystemExit(True)

# Check Blinka Download Features
blinka_features = {
    "Ethernet",
    "HDMI/DisplayPort",
    "Wi-Fi",
    "40-pin GPIO",
    "GPS",
    "Feather-Compatible",
    "Bluetooth/BLE",
    "STEMMA QT/QWIIC",
    "USB 3.0",
    "Infrared Receiver",
    "NVME/M.2 Connector",
}

if not verify_board_id("_board"):
    print("board_id missing for some boards. This is a required field.")
    raise SystemExit(True)

if not verify_board_id("_blinka"):
    print("board_id missing for some boards. This is a required field.")
    raise SystemExit(True)

if not verify_features("_blinka", blinka_features):
    print("Non-standard features found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-blinka for acceptable features")
    raise SystemExit(True)

if not verify_family("_board"):
    print("Family or not found or invalid value. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-downloads for details")
    raise SystemExit(True)

if not verify_date_added("_board") or not verify_date_added("_blinka"):
    print("Date Added field not found or invalid value. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/adding-to-downloads for details")
    raise SystemExit(True)

if not verify_contribute_not_present("_board") or not verify_contribute_not_present("_blinka"):
    print("Contribute section found. This should not be there since it is automatically added.")
    raise SystemExit(True)

if not verify_blinka_board("_blinka"):
    print("blinka flag missing or false for some Blinka boards. Are you sure this board runs Blinka?")
    raise SystemExit(True)

raise SystemExit(False)
