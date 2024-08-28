#!/usr/bin/python3
import json
from pathlib import Path
import frontmatter
import argparse

INCLUDED_CHIP_FAMILIES = ("esp32s2", "esp32s3", "esp32c3", "esp32", "esp32c6")
BOOTLOADER_URL_PREFIX = (
    "https://adafruit-circuit-python.s3.amazonaws.com/bootloaders/esp32/"
)
DOWNLOAD_URL_PREFIX = "https://adafruit-circuit-python.s3.amazonaws.com/bin/"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output",
        help="Output filename. If not specified, output will just print to screen.",
        type=str,
    )

    args = parser.parse_args()

    # Get CircuitPython Bootloader Info
    with open("./_data/bootloaders.json", "rt") as f:
        bootloaders = json.load(f)['bootloaders']

    with open("./_data/files.json", "rt") as f:
        board_info = json.load(f)

    def get_releases(board_id):
        releases = []
        for board in board_info:
            if board_id in board["id"]:
                for board_releases in board["versions"]:
                    release = {}
                    release["version"] = board_releases["version"]
                    for extension in board_releases["extensions"]:
                        release[
                            f"{extension}file"
                        ] = f'{DOWNLOAD_URL_PREFIX}{board_id}/en_US/adafruit-circuitpython-{board_id}-en_US-{release["version"]}.{extension}'
                    releases.append(release)
                break
        return releases

    def get_bootloader(chipfamily, bootloader_id):
        if chipfamily in bootloaders and "version" in bootloaders[chipfamily]:
            bootloader_version = bootloaders[chipfamily]["version"]
            return f"{BOOTLOADER_URL_PREFIX}tinyuf2-{bootloader_id}-{bootloader_version}.zip"
        return None

    def generate_boards(folder):
        boards = {}
        for filename in Path(folder).glob("*.md"):
            board = {}
            with open(filename, "rt") as f:
                metadata, _ = frontmatter.parse(f.read())
            downloads_display = metadata.get("downloads_display")
            if downloads_display is None or downloads_display:
                board_id = metadata.get("board_id").strip() or ()
                if board_id == "unknown":
                    continue
                board_alias = metadata.get("board_alias")
                if not board_alias:
                    board_alias = board_id
                else:
                    board_alias = board_alias.strip()
                board["name"] = metadata.get("name").strip()
                board["chipfamily"] = metadata.get("family").strip()
                if board["chipfamily"] not in INCLUDED_CHIP_FAMILIES:
                    continue
                bootloader_id = metadata.get("bootloader_id")
                if board["chipfamily"] and bootloader_id:
                    board["bootloader"] = get_bootloader(
                        board["chipfamily"], bootloader_id
                    )
                board["releases"] = get_releases(board_alias)
                boards[board_id] = board
                print(f"Added {board_id}")
        return boards

    boards = generate_boards("_board")

    if args.output:
        with open(args.output, "wt") as f:
            json.dump(boards, f, indent=4)
        print(f"Wrote {args.output}")
    else:
        print(json.dumps(boards, indent=4))


if __name__ == "__main__":
    main()
