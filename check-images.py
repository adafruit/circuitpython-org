#!/usr/bin/python3
import os
from pathlib import Path
import frontmatter
from PIL import Image

MIN_ACCEPTABLE_RATIO = 0.75   # HEIGHT / WIDTH
MAX_ACCEPTABLE_RATIO = 0.8
SMALL_IMAGE_MIN_WIDTH = 292
SMALL_IMAGE_MAX_WIDTH = 800
LARGE_IMAGE_MIN_WIDTH = 590
REQUIRE_ORIGINAL_IMAGE = True

BOARD_IMAGE_PATH = "./assets/images/boards/"
SMALL_IMAGE_PATH = BOARD_IMAGE_PATH + "small/"
LARGE_IMAGE_PATH = BOARD_IMAGE_PATH + "large/"
ORIGINAL_IMAGE_PATH = BOARD_IMAGE_PATH + "original/"

def verify_images(folder):
    valid = True
    for filename in sorted(Path(folder).glob("*.md")):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_image = metadata.get('board_image') or ()
            board_id = metadata.get('board_id') or ()
            if board_id == "unknown":
                continue
            # Small Image
            small_image_found = os.path.exists(SMALL_IMAGE_PATH + board_image)
            if small_image_found:
                img = Image.open(SMALL_IMAGE_PATH + board_image)
                if not verify_image_size(SMALL_IMAGE_PATH + board_image, SMALL_IMAGE_MIN_WIDTH, SMALL_IMAGE_MAX_WIDTH):
                    valid = False
            else:
                print(f"{SMALL_IMAGE_PATH + board_image} not found for {board_id}")
                valid = False
            large_image_found = os.path.exists(LARGE_IMAGE_PATH + board_image)
            if large_image_found:
                if not verify_image_size(LARGE_IMAGE_PATH + board_image, LARGE_IMAGE_MIN_WIDTH):
                    valid = False
                img.close()
            else:
                print(f"{LARGE_IMAGE_PATH + board_image} not found for {board_id}")
                valid = False
            sized_images_missing = not small_image_found and not large_image_found
            if REQUIRE_ORIGINAL_IMAGE or sized_images_missing:
                if os.path.exists(ORIGINAL_IMAGE_PATH + board_image):
                    img = Image.open(ORIGINAL_IMAGE_PATH + board_image)
                    if not verify_image_size(ORIGINAL_IMAGE_PATH + board_image, LARGE_IMAGE_MIN_WIDTH, check_ratio=sized_images_missing):
                        valid = False
                    img.close()
                else:
                    if sized_images_missing:
                        print(f"No images found for {board_id}")
                    else:
                        print(f"Original image {ORIGINAL_IMAGE_PATH + board_image} not found for {board_id}.")
                    valid = False
    return valid

def verify_image_size(image_path, min_width, max_width=None, check_ratio=True):
    valid = True
    img = Image.open(image_path)
    width, height = img.size
    min_height = int(min_width * MIN_ACCEPTABLE_RATIO)
    if width < min_width:
        print(f"Image file {image_path} is too narrow ({width} x {height}). It should be at least {min_width} x {min_height} pixels.")
        valid = False
    elif (max_width and width > max_width):
        max_height = int(max_width * MAX_ACCEPTABLE_RATIO)
        print(f"Image file {image_path} is too wide ({width} x {height}). It should be no larger than {max_width} x {max_height} pixels.")
        valid = False
    elif check_ratio and height / width < MIN_ACCEPTABLE_RATIO:
        print(f"Ratio for image file {image_path} is too wide ({width} x {height}). Try reducing width or increasing height.")
        valid = False
    elif check_ratio and height / width > MAX_ACCEPTABLE_RATIO:
        print(f"Ratio for image file {image_path} is too tall ({width} x {height}). Try reducing height or increasing width.")
        valid = False
    img.close()
    return valid

success = verify_images("_board") and verify_images("_blinka")
if not success:
    print("Missing images or images that do not meet requirements found. See https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/preparing-the-images for images acceptable sizes.")

raise SystemExit(not success)
