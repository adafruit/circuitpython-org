# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
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

# GitHub API Serch has stopped returning the core repo for some reason. Tried several
# different search params, and came up emtpy. Hardcoding it as a failsafe.

"""Common functions used throughout Adabot."""

import collections
import datetime
import os
import re
import requests
from adabot import github_requests as github
from adabot import pypi_requests as pypi

CORE_REPO_URL = "/repos/adafruit/circuitpython"


def parse_gitmodules(input_text):
    # pylint: disable=anomalous-backslash-in-string
    """Parse a .gitmodules file and return a list of all the git submodules
    defined inside of it.  Each list item is 2-tuple with:
      - submodule name (string)
      - submodule variables (dictionary with variables as keys and their values)
    The input should be a string of text with the complete representation of
    the .gitmodules file.

    See this for the format of the .gitmodules file, it follows the git config
    file format:
      https://www.kernel.org/pub/software/scm/git/docs/git-config.html

    Note although the format appears to be like a ConfigParser-readable ini file
    it is NOT possible to parse with Python's built-in ConfigParser module.  The
    use of tabs in the git config format breaks ConfigParser, and the subsection
    values in double quotes are completely lost.  A very basic regular
    expression-based parsing logic is used here to parse the data.  This parsing
    is far from perfect and does not handle escaping quotes, line continuations
    (when a line ends in '\;'), etc.  Unfortunately the git config format is
    surprisingly complex and no mature parsing modules are available (outside
    the code in git itself).
    """
    # pylint: enable=anomalous-backslash-in-string

    # Assume no results if invalid input.
    if input_text is None:
        return []
    # Define a regular expression to match a basic submodule section line and
    # capture its subsection value.
    submodule_section_re = r'^\[submodule "(.+)"\]$'
    # Define a regular expression to match a variable setting line and capture
    # the variable name and value.  This does NOT handle multi-line or quote
    # escaping (far outside the abilities of a regular expression).
    variable_re = r"^\s*([a-zA-Z0-9\-]+) =\s+(.+?)\s*$"
    # Process all the lines to parsing submodule sections and the variables
    # within them as they're found.
    results = []
    submodule_name = None
    submodule_variables = {}
    for line in input_text.splitlines():
        submodule_section_match = re.match(
            submodule_section_re, line, flags=re.IGNORECASE
        )
        variable_match = re.match(variable_re, line)
        if submodule_section_match:
            # Found a new section.  End the current one if it had data and add
            # it to the results, then start parsing a new section.
            if submodule_name is not None:
                results.append((submodule_name, submodule_variables))
            submodule_name = submodule_section_match.group(1)
            submodule_variables = {}
        elif variable_match:
            # Found a variable, add it to the current section variables.
            # Force the variable name to lower case as variable names are
            # case-insensitive in git config sections and this makes later
            # processing easier (can assume lower-case names to find values).
            submodule_variables[variable_match.group(1).lower()] = variable_match.group(
                2
            )
    # Add the last parsed section if it exists.
    if submodule_name is not None:
        results.append((submodule_name, submodule_variables))
    return results


def get_bundle_submodules():
    """Query Adafruit_CircuitPython_Bundle repository for all the submodules
    (i.e. modules included inside) and return a list of the found submodules.
    Each list item is a 2-tuple of submodule name and a dict of submodule
    variables including 'path' (location of submodule in bundle) and
    'url' (URL to git repository with submodule contents).
    """
    # Assume the bundle repository is public and get the .gitmodules file
    # without any authentication or Github API usage.  Also assumes the
    # master branch of the bundle is the canonical source of the bundle release.
    result = requests.get(
        "https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/.gitmodules",
        timeout=15,
    )
    if result.status_code != 200:
        # output_handler("Failed to access bundle .gitmodules file from GitHub!", quiet=True)
        raise RuntimeError("Failed to access bundle .gitmodules file from GitHub!")
    return parse_gitmodules(result.text)


def sanitize_url(url):
    """Convert a Github repository URL into a format which can be compared for
    equality with simple string comparison.  Will strip out any leading URL
    scheme, set consistent casing, and remove any optional .git suffix.  The
    attempt is to turn a URL from Github (which can be one of many different
    schemes with and without suffxes) into canonical values for easy comparison.
    """
    # Make the url lower case to perform case-insensitive comparisons.
    # This might not actually be correct if Github cares about case (assumption
    # is no Github does not, but this is unverified).
    url = url.lower()
    # Strip out any preceding http://, https:// or git:// from the URL to
    # make URL comparisons safe (probably better to explicitly parse using
    # a URL module in the future).
    scheme_end = url.find("://")
    if scheme_end >= 0:
        url = url[scheme_end:]
    # Strip out any .git suffix if it exists.
    if url.endswith(".git"):
        url = url[:-4]
    return url


def is_repo_in_bundle(repo_clone_url, bundle_submodules):
    """Return a boolean indicating if the specified repository (the clone URL
    as a string) is in the bundle.  Specify bundle_submodules as a dictionary
    of bundle submodule state returned by get_bundle_submodules.
    """
    # Sanitize url for easy comparison.
    repo_clone_url = sanitize_url(repo_clone_url)
    # Search all the bundle submodules for any that have a URL which matches
    # this clone URL.  Not the most efficient search but it's a handful of
    # items in the bundle.
    for submodule in bundle_submodules:
        _, variables = submodule
        submodule_url = variables.get("url", "")
        # Compare URLs and skip to the next submodule if it's not a match.
        # Right now this is a case sensitive compare, but perhaps it should
        # be insensitive in the future (unsure if Github repos are sensitive).
        if repo_clone_url != sanitize_url(submodule_url):
            continue
        # URLs matched so now check if the submodule is placed in the libraries
        # subfolder of the bundle.  Just look at the path from the submodule
        # state.
        if variables.get("path", "").startswith("libraries/"):
            # Success! Found the repo as a submodule of the libraries folder
            # in the bundle.
            return True
    # Failed to find the repo as a submodule of the libraries folders.
    return False


def list_repos(*, include_repos=None):
    """Return a list of all Adafruit repositories that start with
    Adafruit_CircuitPython.  Each list item is a dictionary of GitHub API
    repository state.

    :param: tuple,list include_repos: A tuple or list of repositories to ensure
                                      are included.
    """
    repos = []
    result = github.get(
        "/search/repositories",
        params={
            "q": "Adafruit_CircuitPython user:adafruit archived:false fork:true",
            "per_page": 100,
            "sort": "updated",
            "order": "asc",
        },
    )

    while result.ok:
        # repos.extend(result.json()["items"]) # uncomment and comment below, to include all forks
        repos.extend(
            repo
            for repo in result.json()["items"]
            if (
                repo["owner"]["login"] == "adafruit"
                and (
                    repo["name"].startswith("Adafruit_CircuitPython")
                    or repo["name"] == "circuitpython"
                )
            )
        )

        if result.links.get("next"):
            result = github.get(result.links["next"]["url"])
        else:
            break

    repo_names = [repo["name"] for repo in repos]

    if "circuitpython" not in repo_names:
        core = github.get(CORE_REPO_URL)
        if core.ok:
            repos.append(core.json())

    if include_repos:
        for repo in include_repos:
            if repo not in repo_names:
                add_repo = github.get("/repos/adafruit/" + repo)
                if add_repo.ok:
                    repos.append(add_repo.json())
                else:
                    print("list_repos(): Failed to retrieve '{}'".format(repo))

    return repos


def get_docs_link(bundle_path, submodule):
    """The URL to the documentation from the README."""
    lines = None
    try:
        with open(f"{bundle_path}/{submodule[1]['path']}/README.rst", "r") as readme:
            lines = readme.read().split("\n")
        for i in range(10):
            if "target" in lines[i] and "readthedocs" in lines[i]:
                return lines[i].replace("    :target: ", "")
        return None
    except FileNotFoundError:
        # didn't find readme
        return None


def repo_is_on_pypi(repo):
    """returns True when the provided repository is in pypi"""
    is_on = False
    the_page = pypi.get("/pypi/" + repo["name"] + "/json")
    if the_page and the_page.status_code == 200:
        is_on = True

    return is_on


def is_new_or_updated(repo):
    """Check the repo for new release(s) within the last week. Then determine
    if all releases are within the last week to decide if this is a newly
    released library, or an updated library.
    """

    today_minus_seven = datetime.datetime.today() - datetime.timedelta(days=7)

    # first, check the latest release to see if within the last 7 days
    result = github.get("/repos/adafruit/" + repo["name"] + "/releases/latest")
    if not result.ok:
        return None
    release_info = result.json()
    if "published_at" not in release_info:
        return None

    release_date = datetime.datetime.strptime(
        release_info["published_at"], "%Y-%m-%dT%H:%M:%SZ"
    )
    if release_date < today_minus_seven:
        return None

    # we have a release within the last 7 days. now check if its a newly
    # released library within the last week, or if its just an update
    result = github.get("/repos/adafruit/" + repo["name"] + "/releases")
    if not result.ok:
        return None

    new_releases = 0
    releases = result.json()
    for release in releases:
        if not release["published_at"]:
            continue
        release_date = datetime.datetime.strptime(
            release["published_at"], "%Y-%m-%dT%H:%M:%SZ"
        )
        if not release_date < today_minus_seven:
            new_releases += 1

    if new_releases == len(releases):
        return "new"

    return "updated"


def whois_github_user():
    """Find who the user is that is running the current instance of adabot.
    'GITHUB_ACTOR' is an environment variable available on GitHub Actions.
    """
    user = None
    if "GITHUB_ACTOR" in os.environ:
        user = os.environ["GITHUB_ACTOR"]
    else:
        user = github.get("/user").json()["login"]

    return user


class InsightData(collections.UserDict):
    """Container class for holding insight data (issues, PRs, etc)."""

    # pylint: disable=super-init-not-called
    def __init__(self):
        self.data = {
            "merged_prs": [],
            "closed_prs": 0,
            "new_prs": 0,
            "active_prs": 0,
            "open_prs": [],
            "pr_authors": set(),
            "pr_merged_authors": set(),
            "pr_reviewers": set(),
            "closed_issues": 0,
            "new_issues": 0,
            "active_issues": 0,
            "open_issues": [],
            "good_first_issues": 0,
            "issue_authors": set(),
            "issue_closers": set(),
            "hacktober_assigned": 0,
            "hacktober_removed": 0,
        }

    def __contains__(self, key):
        return key in self.data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def keys(self):
        return self.data.keys()

    def copy(self):
        return self.data.copy()
