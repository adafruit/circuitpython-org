#!/usr/bin/python3

# Print a list of hidden, missing, and extra boards

import os
import json
from pathlib import Path
import frontmatter

def get_files(folder):
    return sorted(Path(folder).glob("*.md"), key=os.path.basename)

def print_section(title, data, extra_lines=1):
    for _ in range(extra_lines):
        print("")
    print(f"{len(data)} {title}")
    if data:
        print("-" * (len(title) + len(str(len(data))) + 2))
        print("\n".join(data))

# List all boards in the _boards folder that have downloads_display set to false
def find_hidden_boards(folder):
    hidden_boards = []
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
        downloads_display = metadata.get('downloads_display')
        if downloads_display is not None and not downloads_display:
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue
            hidden_boards.append(board_id)
    print_section("Hidden Boards", hidden_boards, 0)

# List all board ids in the data file that are not in the _boards folder
def find_missing_boards(folder):
    missing_boards = []
    # Add all board ids to a list from data file
    with open('./_data/files.json') as board_file:
        boards = json.load(board_file)
        for board in boards:
            if not os.path.exists(f"./_boards/{board}.md"):
                missing_boards.append(board["id"])

    # Scan through files and remove board_ids from list
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue
            if board_id in missing_boards:
                missing_boards.remove(board_id)

    # Print out remaining board_ids
    print_section("Missing Boards", missing_boards)

# List all boards in the _boards folder that are not in the data file
def find_extra_boards(folder):
    extra_boards = []
    aliases = {}
    # Start with a list the board_id from all boards in the _boards folder
    for filename in get_files(folder):
        with open(filename, "rt") as f:
            metadata, _ = frontmatter.parse(f.read())
            board_id = metadata.get('board_id')
            if board_id == "unknown":
                continue
            board_alias = metadata.get('board_alias')
            if board_alias is not None and board_alias != "":
                aliases[board_id] = board_alias
            extra_boards.append(board_id)

    # Remove all board_ids that are in the data file
    with open('./_data/files.json') as board_file:
        boards = json.load(board_file)
        for board in boards:
            if board["id"] in extra_boards:
                extra_boards.remove(board["id"])

    # Update any remaining board IDs with an alias to show the alias
    for i in range(len(extra_boards)):
        board_id = extra_boards[i]
        if board_id in aliases:
            extra_boards[i] = f"{board_id} (alias) --> {aliases[board_id]})"

    # Print out remaining board_ids
    print_section("Extra Boards", extra_boards)

find_hidden_boards("_board")
find_missing_boards("_board")
find_extra_boards("_board")