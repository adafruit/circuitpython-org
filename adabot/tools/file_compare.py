# SPDX-FileCopyrightText: 2022 Eva Herrada
#
# SPDX-License-Identifier: MIT

"""

file-compare.py
===============

Functionality to compare a file across all Adafruit CircuitPython repos
and output the text of the files along with which and how many repos use that
exact file text.

* Author(s): Eva Herrada

"""
import argparse
from typing import Optional

import requests
from requests.structures import CaseInsensitiveDict

from adabot import REQUESTS_TIMEOUT
from adabot.lib.common_funcs import list_repos


def compare(git_file: str, token: Optional[str] = None) -> list:
    """Uses requests to compare files across the adafruit org

    .. note::

        The GitHub API token is not necessary as long as all repos
        being accessed are public. However: it does make things easier
        as you won't get rate-limited quite as often

    :param str git_file: The file to compare
    :param str|None token: The (optional but recommended) github API token
    :return: A list containing all the unique file texts, sorted from most to
        least common along with the repos that have that exact file text.
    :rtype: list
    """

    files = {}

    all_repos = list_repos()
    print("Got Repos List")
    print(f"Repos found: {len(all_repos)}")

    for repo in all_repos:
        name = repo["name"]
        url = f"https://raw.githubusercontent.com/adafruit/{name}/main/{git_file}"

        if token:
            # If repo is private - we need to add a token in header:
            headers = CaseInsensitiveDict()
            headers["Authorization"] = f"token {token}"

            resp = requests.get(url, headers=headers, timeout=REQUESTS_TIMEOUT)
        else:
            resp = requests.get(url, timeout=REQUESTS_TIMEOUT)

        if resp.status_code != 200:
            print(name)
            print(resp.status_code)
        if resp.text not in files:
            files[resp.text] = [1, [repo["html_url"]]]
        else:
            files[resp.text][0] = files[resp.text][0] + 1
            files[resp.text][1].append(repo["html_url"])

    top = 0
    sort = []
    for text, repos in files.items():
        if repos[0] >= top:
            sort.insert(0, [repos[0], text, repos[1]])
            top = repos[0]
        else:
            for i, val in enumerate(sort):
                if val[0] <= repos[0]:
                    sort.insert(i, [repos[0], text, repos[1]])
                    break

    return sort


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare files across the adafruit CircuitPython repos",
    )
    parser.add_argument(
        "gh_token",
        metavar="GH_TOKEN",
        type=str,
        help="GitHub token with proper scopes",
    )

    parser.add_argument(
        "--file",
        metavar="<FILE>",
        type=str,
        dest="file",
        required=True,
        help="File to compare",
    )

    parser.add_argument(
        "-o",
        metavar="<OUTFILE>",
        type=str,
        dest="outfile",
        default=None,
        help="File to send output to",
    )

    args = parser.parse_args()

    results = compare(args.file, args.gh_token)

    for index, value in enumerate(results):
        print(f"##### {index+1}/{len(results)} #####")
        print(value[0])
        print("START OF FILE")
        print(value[1])
        print("END OF FILE")
        print(value[2])
        print()
    if args.outfile:
        with open(args.outfile, "w") as F:
            for index, value in enumerate(results):
                F.write(f"##### {index+1}/{len(results)} #####\n")
                F.write(f"{value[0]}\n")
                F.write("START OF FILE\n")
                F.write(f"{value[1]}\n")
                F.write("END OF FILE\n")
                for r in value[2]:
                    F.write(r + "\n")
                F.write("\n")
