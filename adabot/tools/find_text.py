# SPDX-FileCopyrightText: 2022 Eva Herrada
#
# SPDX-License-Identifier: MIT

"""
Tool for searching for text across all circuitpython libraries.
Intended to be used to verify patches.

IMPORTANT: Must be run from the top-level adabot directory (one directory up
           from this one)

Type `python3 find_text.py -h` to figure out how to use.
"""

import datetime
import getopt
import json
import sys

import requests

from adabot import REQUESTS_TIMEOUT
from adabot.lib.common_funcs import list_repos

argumentList = sys.argv[1:]

OPTIONS = "ht:f:o:j"

long_options = ["help", "text=", "file=", "outfile=", "json"]

HELPMSG = """Usage:
    python3 find_text.py [-h | -t text | -f file | -o outfile | -j]
Arguments:
    -h --help    - Displays this message
    -t --text    - (required) Text to check, can be used multiple times
    -f --file    - (required) File to check for text for on github
    -o --outfile - (optional) Output file, prints output to stdout if variable
                   is not set
    -j --json    - Outputs in json instead of plain text"""

text = []
FILE = None
OUTFILE = None
j = False

URL_TEMPLATE = "https://raw.githubusercontent.com/adafruit/{}/main/{}"
RELEASE_TEMPLATE = "https://api.github.com/repos/adafruit/{}/releases/latest"

try:
    arguments, values = getopt.getopt(argumentList, OPTIONS, long_options)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print(HELPMSG)
            sys.exit()

        if currentArgument in ("-t", "--text"):
            print(f"Text: {currentValue}")
            text.append(currentValue)
            print(text)

        if currentArgument in ("-f", "--file"):
            print(f"File: {currentValue}")
            FILE = currentValue

        if currentArgument in ("-o", "--outfile"):
            OUTFILE = currentValue

        if currentArgument in ("-j", "--json"):
            j = True

except getopt.error as err:
    print(str(err))


if len(text) == 0 or FILE is None:
    if len(text) == 0:
        print("Please enter text to check for")
    if FILE is None:
        print("Please enter a file to search for the text in")
    print(HELPMSG)
    sys.exit()

RESULTS = {
    "file_not_found": [],
    "file_has_none": [],
    "file_has_all": [],
}
for i in range(len(text)):
    RESULTS[f"file_has_text_{i}"] = []


def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line


def prettyprint(info, results):
    """Prints info about current repo and result of search"""
    print("┌" + "─" * (len(info) + 4) + "┐")
    print("│ ", info, " │")
    for res in results:
        print("│ ", res, " " * (len(info) - (len(res) - 9)), "│")
    print("└" + "─" * (len(info) + 4) + "┘")
    delete_multiple_lines(3 + len(results))


try:
    with open("repos.json", "r") as f:
        LAST_RUN = f.readline().rstrip()
except FileNotFoundError:
    LAST_RUN = ""

print(f"Last run: {LAST_RUN}")
if LAST_RUN != str(datetime.date.today()):
    with open("repos.json", "w") as f:
        print("Fetching Repos List")
        all_repos = list_repos()
        print("Got Repos List")
        f.write(str(datetime.date.today()) + "\n")
        f.write(json.dumps(all_repos))

with open("repos.json", "r") as f:
    all_repos = json.loads(f.read().split("\n")[1])

print(f"Repos found: {len(all_repos)}")


for repo in all_repos:
    INFO = "getting {} for: {}".format(FILE, repo["name"])
    response = requests.get(
        URL_TEMPLATE.format(repo["name"], FILE), timeout=REQUESTS_TIMEOUT
    )
    result = []
    if response.status_code == 404:
        RESULTS["file_not_found"].append(repo["html_url"])
        result.append("\033[91mFile not found\033[0m")
    else:
        tracker = [False for i in range(len(text))]
        for index, item in enumerate(text):
            if item in response.text:
                tracker[index] = True

        if all(tracker):
            result = ["\033[92mFound all text\033[0m"]
            RESULTS["file_has_all"].append(repo["html_url"])
        elif not any(tracker):
            result = ["\033[91mDid not find any text\033[0m"]
            RESULTS["file_has_none"].append(repo["html_url"])
        for index, item in enumerate(tracker):
            if item:
                result.append(f"\033[93mFound text {index}\033[0m")
                RESULTS[f"file_has_text_{index}"].append(repo["html_url"])
            else:
                result.append(f"\033[93mDid not find text {index}\033[0m")

    prettyprint(INFO, result)

if j:
    if OUTFILE is not None:
        with open(OUTFILE, "w") as F:
            F.write(json.dumps(RESULTS))
    else:
        print(json.dumps(RESULTS))
else:
    if OUTFILE is not None:
        with open(OUTFILE, "w") as F:
            for k, v in RESULTS.items():
                F.write(k + "\n")
                for i in v:
                    F.write(i + "\n")
                F.write("\n")
    else:
        for k, v in RESULTS.items():
            print(k)
            for i in v:
                print(i)


print("┌" + "─" * 30 + "┐")
for k, v in RESULTS.items():
    print("│ ", k, len(v), " " * (24 - (len(k) + len(str(len(v))))), " │")
print("└" + "─" * 30 + "┘")
