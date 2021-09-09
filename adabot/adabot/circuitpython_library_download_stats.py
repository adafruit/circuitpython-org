# The MIT License (MIT)
#
# Copyright (c) 2018 Michael Schroeder
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

""" Collects download stats for the Adafruit CircuitPython Library Bundles
    and each library.
"""

import datetime
import sys
import argparse
import traceback
import operator
import requests

from adabot import github_requests as github
from adabot.lib import common_funcs

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Adabot utility for CircuitPython Library download stats."
    " Provides stats for the Adafruit CircuitPython Bundle, and PyPi if available.",
    prog="Adabot CircuitPython Libraries Download Stats",
)
cmd_line_parser.add_argument(
    "-o",
    "--output_file",
    help="Output log to the filename provided.",
    metavar="<OUTPUT FILENAME>",
    dest="output_file",
)
cmd_line_parser.add_argument(
    "-v",
    "--verbose",
    help="Set the level of verbosity printed to the command prompt."
    " Zero is off; One is on (default).",
    type=int,
    default=1,
    dest="verbose",
    choices=[0, 1],
)

# Global variables
OUTPUT_FILENAME = None
VERBOSITY = 1
file_data = []

# List containing libraries on PyPi that are not returned by the 'list_repos()' function,
# i.e. are not named 'Adafruit_CircuitPython_'.
PYPI_FORCE_NON_CIRCUITPYTHON = ["Adafruit-Blinka"]

# https://www.piwheels.org/json.html
PIWHEELS_PACKAGES_URL = "https://www.piwheels.org/packages.json"


def piwheels_stats():
    """Get data dump of piwheels download stats"""
    stats = {}
    response = requests.get(PIWHEELS_PACKAGES_URL)
    if response.ok:
        packages = response.json()
        stats = {
            pkg: {"total": dl_all, "month": dl_month}
            for pkg, dl_month, dl_all, *_ in packages
            if pkg.startswith("adafruit")
        }

    return stats


def get_pypi_stats():
    """Map piwheels download stats for each repo"""
    successful_stats = {}
    failed_stats = []
    repos = common_funcs.list_repos()
    dl_stats = piwheels_stats()
    for repo in repos:
        if repo["owner"]["login"] == "adafruit" and repo["name"].startswith(
            "Adafruit_CircuitPython"
        ):
            if common_funcs.repo_is_on_pypi(repo):
                pkg_name = repo["name"].replace("_", "-").lower()
                if pkg_name in dl_stats:
                    successful_stats[repo["name"]] = (
                        dl_stats[pkg_name]["month"],
                        dl_stats[pkg_name]["total"],
                    )
                else:
                    failed_stats.append(repo["name"])

    for lib in PYPI_FORCE_NON_CIRCUITPYTHON:
        pkg_name = lib.lower()
        if pkg_name in dl_stats:
            successful_stats[lib] = (
                dl_stats[pkg_name]["month"],
                dl_stats[pkg_name]["total"],
            )
        else:
            failed_stats.append(lib)

    return successful_stats, failed_stats


def get_bundle_stats(bundle):
    """Returns the download stats for 'bundle'. Uses release tag names to compile download
    stats for the last 7 days. This assumes an Adabot release within that time frame, and
    that tag name(s) will be the date (YYYYMMDD).
    """
    stats_dict = {}
    bundle_stats = github.get("/repos/adafruit/" + bundle + "/releases")
    if not bundle_stats.ok:
        return {"Failed to retrieve bundle stats": bundle_stats.text}
    start_date = datetime.date.today()

    for release in bundle_stats.json():
        try:
            release_date = datetime.date(
                int(release["tag_name"][:4]),
                int(release["tag_name"][4:6]),
                int(release["tag_name"][6:]),
            )
        except ValueError:
            output_handler(
                "Skipping release. Tag name invalid: {}".format(release["tag_name"])
            )
            continue
        if (start_date - release_date).days > 7:
            break

        for asset in release["assets"]:
            if asset["name"].startswith("adafruit"):
                asset_name = asset["name"][: asset["name"].rfind("-")]
                if asset_name in stats_dict:
                    stats_dict[asset_name] = (
                        stats_dict[asset_name] + asset["download_count"]
                    )
                else:
                    stats_dict[asset_name] = asset["download_count"]

    return stats_dict


def output_handler(message="", quiet=False):
    """Handles message output to prompt/file for functions."""
    if OUTPUT_FILENAME is not None:
        file_data.append(message)
    if VERBOSITY and not quiet:
        print(message)


def run_stat_check():
    """Run and report all download stats."""
    output_handler("Adafruit CircuitPython Library Download Stats")
    output_handler(
        "Report Date: {}".format(datetime.datetime.now().strftime("%d %B %Y, %I:%M%p"))
    )
    output_handler()
    output_handler("Adafruit_CircuitPython_Bundle downloads for the past week:")
    for stat in sorted(
        get_bundle_stats("Adafruit_CircuitPython_Bundle").items(),
        key=operator.itemgetter(1),
        reverse=True,
    ):
        output_handler(" {0}: {1}".format(stat[0], stat[1]))
    output_handler()

    pypi_downloads = {}
    pypi_failures = []
    downloads_list = [
        ["| Library", "| Last Month", "| Total |"],
        ["|:-------", "|:--------:", "|:-----:|"],
    ]
    output_handler("Adafruit CircuitPython Library Piwheels downloads:")
    output_handler()
    pypi_downloads, pypi_failures = get_pypi_stats()
    for stat in sorted(
        pypi_downloads.items(), key=operator.itemgetter(1, 1), reverse=True
    ):
        downloads_list.append(
            ["| " + str(stat[0]), "| " + str(stat[1][0]), "| " + str(stat[1][1]) + " |"]
        )

    long_col = [
        (max([len(str(row[i])) for row in downloads_list]) + 3)
        for i in range(len(downloads_list[0]))
    ]
    row_format = "".join(["{:<" + str(this_col) + "}" for this_col in long_col])
    for lib in downloads_list:
        output_handler(row_format.format(*lib))

    if len(pypi_failures) > 0:
        output_handler()
        output_handler(" * Failed to retrieve stats for the following libraries:")
        for fail in pypi_failures:
            output_handler("   * {}".format(fail))


if __name__ == "__main__":
    cmd_line_args = cmd_line_parser.parse_args()
    VERBOSITY = cmd_line_args.verbose
    if cmd_line_args.output_file:
        OUTPUT_FILENAME = cmd_line_args.output_file
    try:
        run_stat_check()
    except:
        if OUTPUT_FILENAME is not None:
            exc_type, exc_val, exc_tb = sys.exc_info()
            output_handler("Exception Occurred!", quiet=True)
            output_handler(("-" * 60), quiet=True)
            output_handler("Traceback (most recent call last):", quiet=True)
            tb = traceback.format_tb(exc_tb)
            for line in tb:
                output_handler(line, quiet=True)
            output_handler(exc_val, quiet=True)

        raise

    finally:
        if OUTPUT_FILENAME is not None:
            with open(OUTPUT_FILENAME, "w") as f:
                for line in file_data:
                    f.write(str(line) + "\n")
