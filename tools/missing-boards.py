#!/usr/bin/python3

# Print a list of hidden and missing boards

import os
import json
from pathlib import Path
import frontmatter

def get_files(folder):
    return sorted(Path(folder).glob("*.md"), key=os.path.basename)

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
    print(f"{len(hidden_boards)} Hidden boards")
    if hidden_boards:
        print("-" * (15 + len(str(len(hidden_boards)))))
        print("\n".join(hidden_boards))

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
    print("")
    print(f"{len(missing_boards)} Missing boards")
    if missing_boards:
        print("-" * (16 + len(str(len(missing_boards)))))
        print("\n".join(missing_boards))

find_hidden_boards("_board")
find_missing_boards("_board")