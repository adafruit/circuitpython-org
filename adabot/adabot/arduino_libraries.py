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

"""Adabot utility for Arduino Libraries."""

import argparse
import logging
import sys
import traceback

import requests

from adabot import github_requests as github

logger = logging.getLogger(__name__)
ch = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[ch])

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Adabot utility for Arduino Libraries.",
    prog="Adabot Arduino Libraries Utility",
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

all_libraries = []
adafruit_library_index = []


def list_repos():
    """Return a list of all Adafruit repositories with 'Arduino' in either the
    name, description, or readme. Each list item is a dictionary of GitHub API
    repository state.
    """
    repos = []
    result = github.get(
        "/search/repositories",
        params={
            "q": (
                "Arduino in:name in:description in:readme fork:true user:adafruit archived:false"
                " OR Library in:name in:description in:readme fork:true user:adafruit"
                " archived:false OR Adafruit_ in:name fork:true user:adafruit archived:false AND"
                " NOT PCB in:name AND NOT Python in:name"
            ),
            "per_page": 100,
            "sort": "updated",
            "order": "asc",
        },
    )
    while result.ok:
        repos.extend(
            result.json()["items"]
        )  # uncomment and comment below, to include all forks

        if result.links.get("next"):
            result = github.get(result.links["next"]["url"])
        else:
            break

    return repos


def is_arduino_library(repo):
    """Returns if the repo is an Arduino library, as determined by the existence of
    the 'library.properties' file.
    """
    lib_prop_file = requests.get(
        "https://raw.githubusercontent.com/adafruit/"
        + repo["name"]
        + "/master/library.properties"
    )
    return lib_prop_file.ok


def print_list_output(title, coll):
    """Helper function to format output."""
    logger.info("")
    logger.info(title.format(len(coll) - 2))
    long_col = [
        (max([len(str(row[i])) for row in coll]) + 3) for i in range(len(coll[0]))
    ]
    row_format = "".join(["{:<" + str(this_col) + "}" for this_col in long_col])
    for lib in coll:
        logger.info("%s", row_format.format(*lib))


def validate_library_properties(repo):
    """Checks if the latest GitHub Release Tag and version in the library_properties
    file match. Will also check if the library_properties is there, but no release
    has been made.
    """
    lib_prop_file = None
    lib_version = None
    release_tag = None
    lib_prop_file = requests.get(
        "https://raw.githubusercontent.com/adafruit/"
        + repo["name"]
        + "/master/library.properties"
    )
    if not lib_prop_file.ok:
        # print("{} skipped".format(repo["name"]))
        return None  # no library properties file!

    lines = lib_prop_file.text.split("\n")
    for line in lines:
        if "version" in line:
            lib_version = line[len("version=") :]
            break

    get_latest_release = github.get(
        "/repos/adafruit/" + repo["name"] + "/releases/latest"
    )
    if get_latest_release.ok:
        response = get_latest_release.json()
        if "tag_name" in response:
            release_tag = response["tag_name"]
        if "message" in response:
            if response["message"] == "Not Found":
                release_tag = "None"
            else:
                release_tag = "Unknown"

    if lib_version and release_tag:
        return [release_tag, lib_version]

    return None


def validate_release_state(repo):
    """Validate if a repo 1) has a release, and 2) if there have been commits
    since the last release. Returns a list of string error messages for the
    repository.
    """
    if not is_arduino_library(repo):
        return None

    compare_tags = github.get(
        "/repos/" + repo["full_name"] + "/compare/master..." + repo["tag_name"]
    )
    if not compare_tags.ok:
        logger.error(
            "Error: failed to compare %s 'master' to tag '%s'",
            repo["name"],
            repo["tag_name"],
        )
        return None
    compare_tags_json = compare_tags.json()
    if "status" in compare_tags_json:
        if compare_tags.json()["status"] != "identical":
            return [repo["tag_name"], compare_tags_json["behind_by"]]
    elif "errors" in compare_tags_json:
        logger.error(
            "Error: comparing latest release to 'master' failed on '%s'. Error Message: %s",
            repo["name"],
            compare_tags_json["message"],
        )

    return None


def validate_actions(repo):
    """Validate if a repo has workflows/githubci.yml"""
    repo_has_actions = requests.get(
        "https://raw.githubusercontent.com/adafruit/"
        + repo["name"]
        + "/master/.github/workflows/githubci.yml"
    )
    return repo_has_actions.ok


def validate_example(repo):
    """Validate if a repo has any files in examples directory"""
    repo_has_ino = github.get("/repos/adafruit/" + repo["name"] + "/contents/examples")
    return repo_has_ino.ok and len(repo_has_ino.json())


# pylint: disable=too-many-branches
def run_arduino_lib_checks():
    """Run necessary functions and outout the results."""
    logger.info("Running Arduino Library Checks")
    logger.info("Getting list of libraries to check...")

    repo_list = list_repos()
    logger.info("Found %s Arduino libraries to check\n", len(repo_list))
    failed_lib_prop = [
        ["  Repo", "Release Tag", "library.properties Version"],
        ["  ----", "-----------", "--------------------------"],
    ]
    needs_release_list = [
        ["  Repo", "Latest Release", "Commits Behind"],
        ["  ----", "--------------", "--------------"],
    ]
    needs_registration_list = [["  Repo"], ["  ----"]]
    missing_actions_list = [["  Repo"], ["  ----"]]
    missing_library_properties_list = [["  Repo"], ["  ----"]]

    for repo in repo_list:
        have_examples = validate_example(repo)
        if not have_examples:
            # not a library
            continue

        entry = {"name": repo["name"]}

        lib_check = validate_library_properties(repo)
        if not lib_check:
            missing_library_properties_list.append(["  " + str(repo["name"])])
            continue

        # print(repo['clone_url'])
        needs_registration = False
        for lib in adafruit_library_index:
            if (repo["clone_url"] == lib["repository"]) or (
                repo["html_url"] == lib["website"]
            ):
                entry["arduino_version"] = lib["version"]  # found it!
                break
        else:
            needs_registration = True
        if needs_registration:
            needs_registration_list.append(["  " + str(repo["name"])])

        entry["release"] = lib_check[0]
        entry["version"] = lib_check[1]
        repo["tag_name"] = lib_check[0]

        needs_release = validate_release_state(repo)
        entry["needs_release"] = needs_release
        if needs_release:
            needs_release_list.append(
                ["  " + str(repo["name"]), needs_release[0], needs_release[1]]
            )

        missing_actions = not validate_actions(repo)
        entry["needs_actions"] = missing_actions
        if missing_actions:
            missing_actions_list.append(["  " + str(repo["name"])])

        all_libraries.append(entry)

    for entry in all_libraries:
        logging.info(entry)

    if len(failed_lib_prop) > 2:
        print_list_output(
            "Libraries Have Mismatched Release Tag and library.properties Version: ({})",
            failed_lib_prop,
        )

    if len(needs_registration_list) > 2:
        print_list_output(
            "Libraries that are not registered with Arduino: ({})",
            needs_registration_list,
        )

    if len(needs_release_list) > 2:
        print_list_output(
            "Libraries have commits since last release: ({})", needs_release_list
        )

    if len(missing_actions_list) > 2:
        print_list_output(
            "Libraries that is not configured with Actions: ({})", missing_actions_list
        )

    if len(missing_library_properties_list) > 2:
        print_list_output(
            "Libraries that is missing library.properties file: ({})",
            missing_library_properties_list,
        )


def main(verbosity=1, output_file=None):  # pylint: disable=missing-function-docstring
    if output_file:
        file_handler = logging.FileHandler(output_file)
        logger.addHandler(file_handler)

    if verbosity == 0:
        logger.setLevel("CRITICAL")

    try:
        reply = requests.get("http://downloads.arduino.cc/libraries/library_index.json")
        if not reply.ok:
            logging.error(
                "Could not fetch http://downloads.arduino.cc/libraries/library_index.json"
            )
            sys.exit()
        arduino_library_index = reply.json()
        for lib in arduino_library_index["libraries"]:
            if "adafruit" in lib["url"]:
                adafruit_library_index.append(lib)
        run_arduino_lib_checks()
    except:
        _, exc_val, exc_tb = sys.exc_info()
        logger.error("Exception Occurred!", quiet=True)
        logger.error(("-" * 60), quiet=True)
        logger.error("Traceback (most recent call last):")
        trace = traceback.format_tb(exc_tb)
        for line in trace:
            logger.error(line)
        logger.error(exc_val)

        raise


if __name__ == "__main__":
    cmd_line_args = cmd_line_parser.parse_args()
    main(verbosity=cmd_line_args.verbose, output_file=cmd_line_args.output_file)
