#!/usr/bin/python3

# Print a list of boards with no board url

# We want a list of boards that are carried in the Adafruit Store, but do not have a board_url with the product link in it.
# If a board has Adafruit in the text or an adafruit link, we will consider it a product carried in the store.


import os
import yaml
import re
from pathlib import Path
import frontmatter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_files(folder):
    return sorted(Path(folder).glob("*.md"), key=os.path.basename)

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

def has_product_link(board_urls):
    for board_url in board_urls:
        if "https://www.adafruit.com/product/" in board_url:
            return True
    return False

def find_adafruit_boards(folder):
    adafruit_boards = []
    keyword_regex = re.compile(r".*[Aa]dafruit.*", re.MULTILINE | re.DOTALL)
    for filename in get_files(folder):
        is_adafruit_board = False
        try:
            with open(filename, "rt") as f:
                metadata, content = frontmatter.parse(f.read())
        except yaml.parser.ParserError as e:
            print(f"Error parsing {filename}: {e}")

        board_id = metadata.get('board_id')
        if board_id == "unknown":
            continue
        board_urls = metadata.get('board_url')
        if board_urls is not None and isinstance(board_urls, str):
            board_urls = [board_urls]

        # Look for Adafruit in the text
        result = keyword_regex.match(content)
        if result is not None:
            is_adafruit_board = True

        if not is_adafruit_board or has_product_link(board_urls):
            continue

        result = re.findall(r".*\[Adafruit\]\((.*?)\)", content, re.MULTILINE | re.DOTALL)
        if result is not None:
            print(board_id, result)
            adafruit_boards.append(board_id)

def find_boards_missing_url(folder):
    missing_url_boards = []
    for filename in get_files(folder):
        try:
            with open(filename, "rt") as f:
                metadata, _ = frontmatter.parse(f.read())
        except yaml.parser.ParserError as e:
            print(f"Error parsing {filename}: {e}")

        downloads_display = metadata.get('downloads_display')
        if downloads_display is None or downloads_display:
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue

            board_urls = metadata.get('board_url')
            if board_urls is not None and isinstance(board_urls, str):
                print(f"{bcolors.WARNING}{folder}/{board_id} is still string{bcolors.ENDC}")
                if len(board_urls) == 0:
                    board_urls = []
                else:
                    board_urls = [board_urls]

            # Remove any empty strings
            if board_urls is not None:
                for index, board_url in enumerate(reversed(board_urls)):
                    if len(board_url) == 0:
                        del board_urls[index]

            if board_urls is not None and len(board_urls) > 0:
                continue

            print(f"{bcolors.FAIL}{folder}/{board_id} is missing a URL{bcolors.ENDC}")
            missing_url_boards.append(board_id)

find_boards_missing_url("_board")
find_boards_missing_url("_blinka")
