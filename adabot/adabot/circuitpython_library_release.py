# SPDX-FileCopyrightText: 2023 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Check if a new release needs to be made, and if so, make it.
"""
import argparse
import subprocess
import logging
from datetime import datetime
import toml

# Empty RELEASE_TITLE will prompt to ask for a title for each release.
# Set a value here if you want to use the same string for the title of all releases
config = {"RELEASE_TITLE": ""}

release_date_format = "%Y-%m-%dT%H:%M:%SZ"
commit_date_format = "%a %b %d %H:%M:%S %Y"

VALID_MENU_CHOICES = ("1", "2", "3", "4", "")


def make_release(new_tag, logger, test_run=False):
    """
    Make the release
    """
    # pylint: disable=line-too-long

    while config["RELEASE_TITLE"] == "":
        config["RELEASE_TITLE"] = input("Enter a Release Title: ")

    if not test_run:
        make_release_result = subprocess.getoutput(
            f"gh release create {new_tag} --generate-notes -t '{new_tag} - {config['RELEASE_TITLE']}'"
        )

        if logger is not None:
            logger.info(make_release_result)
        else:
            print(make_release_result)
    else:
        print("would run: ")
        print(
            "gh release create {new_tag} -F release_notes.md -t '{new_tag} - {config['RELEASE_TITLE']}'"
        )


def get_pypi_name():
    """
    return the shorthand pypi project name
    """
    data = toml.load("pyproject.toml")

    return data["project"]["name"].replace("adafruit-circuitpython-", "")


def needs_new_release(logger):
    """
    return true if there are commits newer than the latest release
    """
    last_commit_time = subprocess.getoutput(
        " TZ=UTC0 git log -1 --date=local --format='%cd'"
    )
    logger.info(f"last commit: {last_commit_time}")

    last_commit_date_obj = datetime.strptime(last_commit_time, commit_date_format)

    release_info = get_release_info()

    logger.info(f"Latest release is: {release_info['current_tag']}")
    logger.info(f"createdAt: {release_info['created_at']}")

    release_date_obj = datetime.strptime(
        release_info["created_at"], release_date_format
    )
    return release_date_obj < last_commit_date_obj


def bump_major(tag_symver):
    """
    Returns a string with a new tag created by incrementing
    the major version of the given semantic version tag.
    """
    tag_parts = tag_symver.split(".")
    tag_parts[0] = str(int(tag_parts[0]) + 1)
    tag_parts[1] = "0"
    tag_parts[2] = "0"
    return ".".join(tag_parts)


def bump_minor(tag_symver):
    """
    Returns a string with a new tag created by incrementing
    the minor version of the given semantic version tag.
    """
    tag_parts = tag_symver.split(".")
    tag_parts[1] = str(int(tag_parts[1]) + 1)
    tag_parts[2] = "0"
    return ".".join(tag_parts)


def bump_patch(tag_symver):
    """
    Returns a string with a new tag created by incrementing
    the patch version of the given semantic version tag.
    """
    tag_parts = tag_symver.split(".")
    tag_parts[-1] = str(int(tag_parts[-1]) + 1)
    return ".".join(tag_parts)


def get_release_info():
    """
    return a dictionary of info about the latest release
    """
    result = subprocess.getoutput("gh release list -L 1 | awk 2")
    createdAt = result.split("\t")[-1]
    tag = result.split("\t")[-2]
    return {
        "current_tag": tag,
        "new_tag_patch": bump_patch(tag),
        "new_tag_minor": bump_minor(tag),
        "new_tag_major": bump_major(tag),
        "created_at": createdAt,
    }


def get_compare_url(tag_name):
    """
    Get the URL to the GitHub compare page for the latest release compared
    to current main.
    """
    remote_url = subprocess.getoutput("git ls-remote --get-url origin")
    if not remote_url.startswith("https"):
        remote_url = subprocess.getoutput("git ls-remote --get-url adafruit")

    if not remote_url.startswith("https"):
        return "Sorry, Unknown Remotes"

    compare_url = remote_url.replace(".git", f"/compare/{tag_name}...main")
    return compare_url


def main_cli():
    """
    Main CLI entry point
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("../../../automated_releaser.log"),
            logging.StreamHandler(),
        ],
    )

    parser = argparse.ArgumentParser(
        prog="adabot.circuitpython_library_release",
        description="Create GitHub releases for CircuitPython Library projects if they "
        "contain commits newer than the most recent release.",
    )
    parser.add_argument("-t", "--title")
    args = parser.parse_args()
    if args.title is not None:
        config["RELEASE_TITLE"] = args.title

    def menu_prompt(release_info):
        """
        Prompt the user to ask which part of the symantic version should be
        incremented, or if the library release should be skipped.
        Returns the choice inputted by the user.
        """
        print("This library needs a new release. Please select a choice:")
        print(f"Changes: {get_compare_url(release_info['current_tag'])}")
        print(
            f"1. *default* Bump Patch, new tag would be: {release_info['new_tag_patch']}"
        )
        print(f"2. Bump Minor, new tag would be: {release_info['new_tag_minor']}")
        print(f"3. Bump Major, new tag would be: {release_info['new_tag_major']}")
        print("4. Skip releasing this library and go to next in the list")
        return input("Choice, enter blank for default: ")

    result = subprocess.getoutput("git checkout main")

    result = subprocess.getoutput("pwd")
    logging.info("Checking: %s", "/".join(result.split("/")[-3:]))

    if needs_new_release(logging):
        release_info = get_release_info()
        choice = menu_prompt(release_info)
        while choice not in VALID_MENU_CHOICES:
            logging.info("Error: Invalid Selection '%s'", choice)
            choice = menu_prompt(release_info)

        if choice in ("1", ""):
            logging.info(
                "Making a new release with tag: %s", release_info["new_tag_patch"]
            )
            make_release(release_info["new_tag_patch"], logging)
        elif choice == "2":
            logging.info(
                "Making a new release with tag: %s", release_info["new_tag_minor"]
            )
            make_release(release_info["new_tag_minor"], logging)
        elif choice == "3":
            logging.info(
                "Making a new release with tag: %s", release_info["new_tag_major"]
            )
            make_release(release_info["new_tag_major"], logging)
        elif choice == "4":
            logging.info("Skipping release.")

    else:
        logging.info("No new commits since last release, skipping")


if __name__ == "__main__":
    main_cli()
