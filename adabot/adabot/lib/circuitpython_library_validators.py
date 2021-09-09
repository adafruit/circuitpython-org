# pylint: disable=no-self-use
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

"""Collection of validator methods to maintain a standard, as well as detect
errors, across the entire CirtuitPython library ecosystem."""

import datetime
from io import StringIO
import json
import logging
import pathlib
import re
from tempfile import TemporaryDirectory

from packaging.version import parse as pkg_version_parse
from packaging.requirements import Requirement, InvalidRequirement

from pylint import lint
from pylint.reporters import JSONReporter

import requests

import sh
from sh.contrib import git

import yaml

from adabot import github_requests as github
from adabot.lib import common_funcs
from adabot.lib import assign_hacktober_label as hacktober


class CapturedJsonReporter(JSONReporter):
    """Helper class to stringify PyLint JSON reports."""

    def __init__(self):
        self._stringio = StringIO()
        super().__init__(self._stringio)

    def get_result(self):
        """The current value."""
        return self._stringio.getvalue()


# Define constants for error strings to make checking against them more robust:
ERROR_README_DOWNLOAD_FAILED = "Failed to download README"
ERROR_README_IMAGE_MISSING_ALT = "README image missing alt text"
ERROR_README_DUPLICATE_ALT_TEXT = "README has duplicate alt text"
ERROR_README_MISSING_DISCORD_BADGE = "README missing Discord badge"
ERROR_README_MISSING_RTD_BADGE = "README missing ReadTheDocs badge"
ERROR_README_MISSING_CI_BADGE = "README missing CI badge"
ERROR_README_MISSING_CI_ACTIONS_BADGE = (
    "README CI badge needs to be changed to GitHub Actions"
)
ERROR_PYFILE_DOWNLOAD_FAILED = "Failed to download .py code file"
ERROR_PYFILE_MISSING_STRUCT = (
    ".py file contains reference to import ustruct"
    " without reference to import struct.  See issue "
    "https://github.com/adafruit/circuitpython/issues/782"
)
ERROR_PYFILE_MISSING_RE = (
    ".py file contains reference to import ure"
    " without reference to import re.  See issue "
    "https://github.com/adafruit/circuitpython/issues/1582"
)
ERROR_PYFILE_MISSING_JSON = (
    ".py file contains reference to import ujson"
    " without reference to import json.  See issue "
    "https://github.com/adafruit/circuitpython/issues/1582"
)
ERROR_PYFILE_MISSING_ERRNO = (
    ".py file contains reference to import uerrno"
    " without reference to import errno.  See issue "
    "https://github.com/adafruit/circuitpython/issues/1582"
)
ERROR_MISMATCHED_READTHEDOCS = "Mismatched readthedocs.yml"
ERROR_MISSING_DESCRIPTION = "Missing repository description"
ERROR_MISSING_EXAMPLE_FILES = "Missing .py files in examples folder"
ERROR_MISSING_EXAMPLE_FOLDER = "Missing examples folder"
ERROR_EXAMPLE_MISSING_SENSORNAME = "Example file(s) missing sensor/library name"
ERROR_MISSING_EXAMPLE_SIMPLETEST = "Missing simpletest example."
ERROR_MISSING_STANDARD_LABELS = (
    "Missing one or more standard issue labels"
    " (bug, documentation, enhancement, good first issue)."
)
ERROR_MISSING_LIBRARIANS = (
    "CircuitPythonLibrarians team missing or does not have write access"
)
ERROR_MISSING_LICENSE = "Missing license."
ERROR_MISSING_LINT = "Missing lint config"
ERROR_MISSING_CODE_OF_CONDUCT = "Missing CODE_OF_CONDUCT.md"
ERROR_MISSING_README_RST = "Missing README.rst"
ERROR_MISSING_READTHEDOCS = "Missing readthedocs.yml"
ERROR_MISSING_SETUP_PY = "For pypi compatibility, missing setup.py"
ERROR_MISSING_REQUIREMENTS_TXT = "For pypi compatibility, missing requirements.txt"
ERROR_MISSING_BLINKA = (
    "For pypi compatibility, missing Adafruit-Blinka in requirements.txt"
)
ERROR_NOT_IN_BUNDLE = "Not in bundle."
ERROR_INCORRECT_DEFAULT_BRANCH = "Default branch is not main"
ERROR_UNABLE_PULL_REPO_CONTENTS = "Unable to pull repo contents"
ERROR_UNABLE_PULL_REPO_DETAILS = "Unable to pull repo details"
ERRRO_UNABLE_PULL_REPO_EXAMPLES = "Unable to retrieve examples folder contents"
ERROR_WIKI_DISABLED = "Wiki should be disabled"
ERROR_ONLY_ALLOW_MERGES = "Only allow merges, disallow rebase and squash"
ERROR_RTD_SUBPROJECT_FAILED = "Failed to list CircuitPython subprojects on ReadTheDocs"
ERROR_RTD_SUBPROJECT_MISSING = "ReadTheDocs missing as a subproject on CircuitPython"
ERROR_RTD_ADABOT_MISSING = "ReadTheDocs project missing adabot as owner"
ERROR_RTD_VALID_VERSIONS_FAILED = "Failed to fetch ReadTheDocs valid versions"
ERROR_RTD_FAILED_TO_LOAD_BUILDS = "Unable to load builds webpage"
ERROR_RTD_FAILED_TO_LOAD_BUILD_INFO = "Failed to load build info"
ERROR_RTD_OUTPUT_HAS_WARNINGS = "ReadTheDocs latest build has warnings and/or errors"
ERROR_RTD_AUTODOC_FAILED = (
    "Autodoc failed on ReadTheDocs. (Likely need to automock an import.)"
)
ERROR_RTD_SPHINX_FAILED = "Sphinx missing files"
ERROR_GITHUB_RELEASE_FAILED = "Failed to fetch latest release from GitHub"
ERROR_GITHUB_NO_RELEASE = "Library repository has no releases"
ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_GTM = (
    "Library has new commits since last release over a month ago"
)
ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_1M = (
    "Library has new commits since last release within the last month"
)
ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_1W = (
    "Library has new commits since last release within the last week"
)
ERROR_GITHUB_FAILING_ACTIONS = "The most recent GitHub Actions run has failed"
ERROR_RTD_MISSING_LATEST_RELEASE = (
    "ReadTheDocs missing the latest release. (Ignore me! RTD doesn't update when a new version is"
    " released. Only on pushes.)"
)
ERROR_DRIVERS_PAGE_DOWNLOAD_FAILED = (
    "Failed to download drivers page from CircuitPython docs"
)
ERROR_DRIVERS_PAGE_DOWNLOAD_MISSING_DRIVER = "CircuitPython drivers page missing driver"
ERROR_UNABLE_PULL_REPO_DIR = "Unable to pull repository directory"
ERROR_UNABLE_PULL_REPO_EXAMPLES = "Unable to pull repository examples files"
ERROR_NOT_ON_PYPI = "Not listed on PyPi for CPython use"
ERROR_PYLINT_VERSION_NOT_FIXED = "PyLint version not fixed"
ERROR_PYLINT_VERSION_NOT_LATEST = "PyLint version not latest"
ERROR_PYLINT_FAILED_LINTING = "Failed PyLint checks"
ERROR_NEW_REPO_IN_WORK = "New repo(s) currently in work, and unreleased"

# Temp category for GitHub Actions migration.
ERROR_NEEDS_ACTION_MIGRATION = (
    "Repo(s) need to be migrated from TravisCI to GitHub Actions"
)

# Since this has been refactored into a separate module, the connection to 'output_handler()'
# and associated 'file_data' list is broken. To keep from possibly having conflicted
# file operations, and writing to the `output_filename` concurrently, establish an
# output_handler error flag, so that the calling function can handle it. Information related
# to the flag will be stored in a instance variable.
ERROR_OUTPUT_HANDLER = "A programmatic error occurred"

# These are warnings or errors that sphinx generate that we're ok ignoring.
RTD_IGNORE_NOTICES = (
    "WARNING: html_static_path entry",
    "WARNING: nonlocal image URI found:",
)

# Constant for bundle repo name.
BUNDLE_REPO_NAME = "Adafruit_CircuitPython_Bundle"

# Repos to ignore for validation they exist in the bundle.  Add repos by their
# full name on Github (like Adafruit_CircuitPython_Bundle).
BUNDLE_IGNORE_LIST = [BUNDLE_REPO_NAME]

LIBRARIES_DONT_NEED_BLINKA = [
    "Adafruit_CircuitPython_BusDevice",
    "Adafruit_CircuitPython_CircuitPlayground",
    "Adafruit_CircuitPython_FancyLED",
    "Adafruit_CircuitPython_IRRemote",
    "Adafruit_CircuitPython_ImageLoad",
    "Adafruit_CircuitPython_MCP9808",
    "Adafruit_CircuitPython_PCA9685",
    "Adafruit_CircuitPython_PCF8523",
    "Adafruit_CircuitPython_TLC59711",
    "Adafruit_CircuitPython_Waveform",
    "Adafruit_CircuitPython_miniQR",
]

STD_REPO_LABELS = {
    "bug": {"color": "ee0701"},
    "documentation": {"color": "d4c5f9"},
    "enhancement": {"color": "84b6eb"},
    "good first issue": {"color": "7057ff"},
}


class LibraryValidator:
    """Class to hold instance variables needed to traverse the calling
    code, and the validator functions.
    """

    def __init__(
        self, validators, bundle_submodules, latest_pylint, keep_repos=False, **kw_args
    ):
        self.validators = validators
        self.bundle_submodules = bundle_submodules
        self.latest_pylint = pkg_version_parse(latest_pylint)
        self._rtd_yaml_base = None
        self.output_file_data = []
        self.validate_contents_quiet = kw_args.get("validate_contents_quiet", False)
        self.has_setup_py_disabled = set()
        self.keep_repos = keep_repos
        self.rtd_subprojects = None
        self.core_driver_page = None

    @property
    def rtd_yml_base(self):
        """The parsed YAML from `.readthedocs.yml` in the cookiecutter-adafruit-circuitpython repo.
        Used to verify that a library's `.readthedocs.yml` matches this version.
        """
        if self._rtd_yaml_base is None:
            rtd_yml_dl_url = (
                "https://raw.githubusercontent.com/adafruit/cookiecutter-adafruit-"
                "circuitpython/main/%7B%25%20if%20cookiecutter.library_prefix"
                "%20%25%7D%7B%7B%20cookiecutter.library_prefix%20%7C%20capitalize"
                "%20%7D%7D_CircuitPython%7B%25%20else%20%25%7DCircuitPython_Org%7B"
                "%25%20endif%20%25%7D_%7B%7B%20cookiecutter.library_name%7Creplace"
                "(%22%20%22%2C%20%22_%22)%7D%7D/%7B%25%20if%20cookiecutter.sphinx"
                "_docs%20in%20%5B'y'%2C%20'yes'%5D%20%25%7D.readthedocs.yml%7B%25"
                "%20endif%20%25%7D"
            )
            rtd_yml = requests.get(rtd_yml_dl_url)
            if rtd_yml.ok:
                try:
                    self._rtd_yaml_base = yaml.safe_load(rtd_yml.text)
                except yaml.YAMLError:
                    print("Error parsing cookiecutter .readthedocs.yml.")
                    self._rtd_yaml_base = ""
            else:
                print("Error retrieving cookiecutter .readthedocs.yml")
                self._rtd_yaml_base = ""

        return self._rtd_yaml_base

    def run_repo_validation(self, repo):
        """Run all the current validation functions on the provided repository and
        return their results as a list of string errors.
        """
        errors = []
        for validator in self.validators:
            errors.extend(validator(self, repo))
        return errors

    def validate_repo_state(self, repo):
        """Validate a repository meets current CircuitPython criteria.  Expects
        a dictionary with a GitHub API repository state (like from the list_repos
        function).  Returns a list of string error messages for the repository.
        """
        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []

        search_keys = {
            "has_wiki",
            "license",
            "permissions",
            "allow_squash_merge",
            "allow_rebase_merge",
        }

        repo_fields = repo.copy()

        repo_fields_keys = set(repo_fields.keys())
        repo_missing_some_keys = search_keys.difference(repo_fields_keys)

        if repo_missing_some_keys:
            # only call the API if the passed in `repo` doesn't have what
            # we need.
            response = github.get("/repos/" + repo["full_name"])
            if not response.ok:
                return [ERROR_UNABLE_PULL_REPO_DETAILS]
            repo_fields = response.json()

        errors = []

        if not repo_fields.get("description"):
            errors.append(ERROR_MISSING_DESCRIPTION)

        if repo_fields.get("has_wiki"):
            errors.append(ERROR_WIKI_DISABLED)

        if not repo_fields.get("license") and not repo["name"] in BUNDLE_IGNORE_LIST:
            errors.append(ERROR_MISSING_LICENSE)

        if not repo_fields.get("permissions", {}).get("push"):
            errors.append(ERROR_MISSING_LIBRARIANS)

        repo_in_bundle = common_funcs.is_repo_in_bundle(
            repo_fields["clone_url"], self.bundle_submodules
        )
        if not repo_in_bundle and not repo["name"] in BUNDLE_IGNORE_LIST:
            # Don't assume the bundle will bundle itself and possibly
            # other repos.
            errors.append(ERROR_NOT_IN_BUNDLE)

        if repo_fields.get("allow_squash_merge") or repo_fields.get(
            "allow_rebase_merge"
        ):
            errors.append(ERROR_ONLY_ALLOW_MERGES)
        return errors

    def validate_actions_state(self, repo):
        """Validate if the most recent GitHub Actions run on the default branch
        has passed.
        Just returns a message stating that the most recent run failed.
        """
        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []

        actions_params = {"branch": repo["default_branch"]}
        response = github.get(
            "/repos/" + repo["full_name"] + "/actions/runs", params=actions_params
        )

        if not response.ok:
            return [ERROR_UNABLE_PULL_REPO_DETAILS]

        workflow_runs = response.json()["workflow_runs"]
        if workflow_runs and workflow_runs[0]["conclusion"] == "failure":
            return [ERROR_GITHUB_FAILING_ACTIONS]
        return []

    # pylint: disable=too-many-locals,too-many-return-statements,too-many-branches
    def validate_release_state(self, repo):
        """Validate if a repo 1) has a release, and 2) if there have been commits
        since the last release. Only files that drive user-facing changes
        will be considered when flagging a repo as needing a release.

        If 2), categorize by length of time passed since oldest commit after the release,
        and return the number of days that have passed since the oldest commit.
        """

        def _filter_file_diffs(filenames):
            _ignored_files = {
                "CODE_OF_CONDUCT.md",
                "LICENSE",
                "LICENSES/*",
                "*.license",
                "setup.py.disabled",
                ".github/workflows/build.yml",
                ".github/workflows/release.yml",
                ".pre-commit-config.yaml",
                ".pylintrc",
                ".gitignore",
                "CODE_OF_CONDUCT.md",
                "README.rst",
                "pyproject.toml",
            }
            compare_files = [name for name in filenames if not name.startswith(".")]

            return list(set(compare_files).difference(_ignored_files))

        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []

        if repo["name"] in BUNDLE_IGNORE_LIST:
            return []

        repo_last_release = github.get(
            "/repos/" + repo["full_name"] + "/releases/latest"
        )
        if not repo_last_release.ok:
            return [ERROR_GITHUB_NO_RELEASE]
        repo_release_json = repo_last_release.json()
        if "message" in repo_release_json:
            if repo_release_json["message"] == "Not Found":
                return [ERROR_GITHUB_NO_RELEASE]

            err_msg = [
                f"Error: retrieving latest release information failed on '{repo['name']}'.",
                f"Information Received: {repo_release_json['message']}",
            ]
            self.output_file_data.append("".join(err_msg))
            return [ERROR_OUTPUT_HANDLER]

        tag_name = repo_release_json.get("tag_name", "")
        main_branch = repo["default_branch"]
        compare_tags = github.get(
            f"/repos/{repo['full_name']}/compare/{tag_name}...{main_branch}"
        )
        if not compare_tags.ok:
            self.output_file_data.append(
                f"Error: failed to compare {repo['name']} '{main_branch}' to tag '{tag_name}'"
            )
            return [ERROR_OUTPUT_HANDLER]
        compare_tags_json = compare_tags.json()
        if "status" in compare_tags_json:
            if compare_tags_json["status"] != "identical":

                filtered_files = _filter_file_diffs(
                    [file["filename"] for file in compare_tags_json.get("files")]
                )
                if filtered_files:
                    oldest_commit_date = datetime.datetime.today()
                    for commit in compare_tags_json["commits"]:
                        commit_date_val = commit["commit"]["committer"]["date"]
                        commit_date = datetime.datetime.strptime(
                            commit_date_val, "%Y-%m-%dT%H:%M:%SZ"
                        )
                        if commit_date < oldest_commit_date:
                            oldest_commit_date = commit_date

                    date_diff = datetime.datetime.today() - oldest_commit_date
                    if date_diff.days > datetime.date.today().max.day:
                        return [
                            (
                                ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_GTM,
                                date_diff.days,
                            )
                        ]
                    if date_diff.days <= datetime.date.today().max.day:
                        if date_diff.days > 7:
                            return [
                                (
                                    ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_1M,
                                    date_diff.days,
                                )
                            ]

                        return [
                            (
                                ERROR_GITHUB_COMMITS_SINCE_LAST_RELEASE_1W,
                                date_diff.days,
                            )
                        ]
        elif "errors" in compare_tags_json:
            err_msg = [
                f"Error: comparing latest release to '{main_branch}' failed on '{repo['name']}'. ",
                f"Error Message: {compare_tags_json['message']}",
            ]
            self.output_file_data.append("".join(err_msg))
            return [ERROR_OUTPUT_HANDLER]

        return []

    # pylint: disable=too-many-branches
    def _validate_readme(self, download_url):
        # We use requests because file contents are hosted by
        # githubusercontent.com, not the API domain.
        contents = requests.get(download_url, timeout=30)
        if not contents.ok:
            return [ERROR_README_DOWNLOAD_FAILED]

        errors = []
        badges = {}
        current_image = None
        for line in contents.text.split("\n"):
            if line.startswith(".. image"):
                current_image = {}

            if line.strip() == "" and current_image is not None:
                if "alt" not in current_image:
                    errors.append(ERROR_README_IMAGE_MISSING_ALT)
                elif current_image["alt"] in badges:
                    errors.append(ERROR_README_DUPLICATE_ALT_TEXT)
                else:
                    badges[current_image["alt"]] = current_image
                current_image = None
            elif current_image is not None:
                first, second, value = line.split(":", 2)
                key = first.strip(" .") + second.strip()
                current_image[key] = value.strip()

        if "Discord" not in badges:
            errors.append(ERROR_README_MISSING_DISCORD_BADGE)

        if "Documentation Status" not in badges:
            errors.append(ERROR_README_MISSING_RTD_BADGE)

        if "Build Status" not in badges:
            errors.append(ERROR_README_MISSING_CI_BADGE)
        else:
            status_img = badges["Build Status"]["image"]
            if "travis-ci.com" in status_img:
                errors.append(ERROR_README_MISSING_CI_ACTIONS_BADGE)

        return errors

    def _validate_py_for_u_modules(self, download_url):
        """For a .py file, look for usage of "import u___" and
        look for "import ___".  If the "import u___" is
        used with NO "import ____" generate an error.
        """
        # We use requests because file contents are hosted by
        # githubusercontent.com, not the API domain.
        contents = requests.get(download_url, timeout=30)
        if not contents.ok:
            return [ERROR_PYFILE_DOWNLOAD_FAILED]

        errors = []

        lines = contents.text.split("\n")
        ustruct_lines = [
            l for l in lines if re.match(r"[\s]*import[\s][\s]*ustruct", l)
        ]
        struct_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*struct", l)]
        if ustruct_lines and not struct_lines:
            errors.append(ERROR_PYFILE_MISSING_STRUCT)

        ure_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*ure", l)]
        re_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*re", l)]
        if ure_lines and not re_lines:
            errors.append(ERROR_PYFILE_MISSING_RE)

        ujson_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*ujson", l)]
        json_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*json", l)]
        if ujson_lines and not json_lines:
            errors.append(ERROR_PYFILE_MISSING_JSON)

        uerrno_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*uerrno", l)]
        errno_lines = [l for l in lines if re.match(r"[\s]*import[\s][\s]*errno", l)]
        if uerrno_lines and not errno_lines:
            errors.append(ERROR_PYFILE_MISSING_ERRNO)

        return errors

    def _validate_actions_build_yml(self, actions_build_info):
        """Check the following configurations in the GitHub Actions
        build.yml file:
            - Pylint version is the latest release
        """

        download_url = actions_build_info["download_url"]
        contents = requests.get(download_url, timeout=30)
        if not contents.ok:
            return [ERROR_PYFILE_DOWNLOAD_FAILED]

        errors = []

        pylint_version = None
        re_pip_pattern = r"pip\sinstall.*"
        re_pylint_pattern = r"(?P<pylint>pylint(?:[<>~=]){0,2}\d*(?:\.\d){0,2})"

        pip_line = re.search(re_pip_pattern, contents.text)
        if not pip_line:
            return [ERROR_PYLINT_VERSION_NOT_FIXED]

        pip_line = pip_line[0]

        pylint_info = re.search(re_pylint_pattern, pip_line)
        if not pylint_info or not pylint_info.group("pylint"):
            return [ERROR_PYLINT_VERSION_NOT_FIXED]

        try:
            pylint_version = Requirement(pylint_info.group("pylint"))
        except InvalidRequirement:
            pass

        if not pylint_version:
            errors.append(ERROR_PYLINT_VERSION_NOT_FIXED)
        elif self.latest_pylint not in pylint_version.specifier:
            errors.append(ERROR_PYLINT_VERSION_NOT_LATEST)

        return errors

    def _validate_setup_py(self, file_info):
        """Check setup.py for pypi compatibility"""
        download_url = file_info["download_url"]
        contents = requests.get(download_url, timeout=30)
        if not contents.ok:
            return [ERROR_PYFILE_DOWNLOAD_FAILED]

        errors = []

        return errors

    def _validate_requirements_txt(self, repo, file_info):
        """Check requirements.txt for pypi compatibility"""
        download_url = file_info["download_url"]
        contents = requests.get(download_url, timeout=30)
        if not contents.ok:
            return [ERROR_PYFILE_DOWNLOAD_FAILED]

        errors = []
        lines = contents.text.split("\n")
        blinka_lines = [l for l in lines if re.match(r"[\s]*Adafruit-Blinka[\s]*", l)]

        if not blinka_lines and repo["name"] not in LIBRARIES_DONT_NEED_BLINKA:
            errors.append(ERROR_MISSING_BLINKA)
        return errors

    # pylint: disable=too-many-locals,too-many-branches,too-many-statements,too-many-return-statements
    def validate_contents(self, repo):
        """Validate the contents of a repository meets current CircuitPython
        criteria (within reason, functionality checks are not possible).  Expects
        a dictionary with a GitHub API repository state (like from the list_repos
        function).  Returns a list of string error messages for the repository.
        """

        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []
        if repo["name"] == BUNDLE_REPO_NAME:
            return []

        content_list = github.get("/repos/" + repo["full_name"] + "/contents/")
        empty_repo = False
        if not content_list.ok:
            # Empty repos return:
            #  - a 404 status code
            #  - a "message" that the repo is empty.
            if "message" in content_list.json():
                if "empty" in content_list.json()["message"]:
                    empty_repo = True
            if not empty_repo:
                if not self.validate_contents_quiet:
                    return [ERROR_UNABLE_PULL_REPO_CONTENTS]
                return []

        content_list = content_list.json()
        files = []
        # an empty repo will return a 'message'
        if not empty_repo:
            files = [x["name"] for x in content_list]

        # ignore new/in-work repos, which should have less than 8 files:
        # ___.py or folder, CoC, .github/, .readthedocs.yml, docs/,
        # examples/, README, LICENSE
        if len(files) < 8:
            BUNDLE_IGNORE_LIST.append(repo["name"])
            if not self.validate_contents_quiet:
                return [ERROR_NEW_REPO_IN_WORK]

        if "setup.py.disabled" in files:
            self.has_setup_py_disabled.add(repo["name"])

        # if we're only running due to -v, ignore the rest. we only care about
        # adding in-work repos to the BUNDLE_IGNORE_LIST and if setup.py is
        # disabled
        if self.validate_contents_quiet:
            return []

        errors = []
        if ".pylintrc" not in files:
            errors.append(ERROR_MISSING_LINT)

        if "CODE_OF_CONDUCT.md" not in files:
            errors.append(ERROR_MISSING_CODE_OF_CONDUCT)

        if "README.rst" not in files:
            errors.append(ERROR_MISSING_README_RST)
        else:
            readme_info = None
            for file in content_list:
                if file["name"] == "README.rst":
                    readme_info = file
                    break
            errors.extend(self._validate_readme(readme_info["download_url"]))

        if ".travis.yml" in files:
            errors.append(ERROR_NEEDS_ACTION_MIGRATION)
        elif ".github" in files:
            # grab '.github' entry, extract URL, build new URL to build.yml, retrieve and pass
            build_yml_url = ""
            actions_build_info = None

            for item in content_list:
                if item.get("name") == ".github" and item.get("type") == "dir":
                    build_yml_url = item["url"].split("?")[0]
                    break

            if build_yml_url:
                build_yml_url = build_yml_url + "/workflows/build.yml"
                response = github.get(build_yml_url)
                if response.ok:
                    actions_build_info = response.json()

            if actions_build_info:
                errors.extend(self._validate_actions_build_yml(actions_build_info))
            else:
                errors.append(ERROR_UNABLE_PULL_REPO_CONTENTS)

        if "readthedocs.yml" in files or ".readthedocs.yml" in files:
            if self.rtd_yml_base != "":
                filename = "readthedocs.yml"
                if ".readthedocs.yml" in files:
                    filename = ".readthedocs.yml"
                file_info = content_list[files.index(filename)]
                rtd_contents = requests.get(file_info["download_url"])
                if rtd_contents.ok:
                    try:
                        rtd_yml = yaml.safe_load(rtd_contents.text)
                        if rtd_yml != self.rtd_yml_base:
                            errors.append(ERROR_MISMATCHED_READTHEDOCS)
                    except yaml.YAMLError:
                        self.output_file_data.append(
                            "Error parsing {} .readthedocs.yml.".format(repo["name"])
                        )
                        errors.append(ERROR_OUTPUT_HANDLER)
        else:
            errors.append(ERROR_MISSING_READTHEDOCS)

        if "setup.py" in files:
            file_info = content_list[files.index("setup.py")]
            errors.extend(self._validate_setup_py(file_info))
        elif "setup.py.disabled" not in files:
            errors.append(ERROR_MISSING_SETUP_PY)

        if repo["name"] not in self.has_setup_py_disabled:
            if "requirements.txt" in files:
                file_info = content_list[files.index("requirements.txt")]
                errors.extend(self._validate_requirements_txt(repo, file_info))
            else:
                errors.append(ERROR_MISSING_REQUIREMENTS_TXT)

        # Check for an examples folder.
        dirs = [
            x["url"]
            for x in content_list
            if (x["type"] == "dir" and x["name"] == "examples")
        ]
        examples_list = []
        if dirs:
            while dirs:
                # loop through the results to ensure we capture files
                # in subfolders, and add any files in the current directory
                result = github.get(dirs.pop(0))
                if not result.ok:
                    errors.append(ERROR_UNABLE_PULL_REPO_EXAMPLES)
                    break
                result_json = result.json()
                dirs.extend([x["url"] for x in result_json if x["type"] == "dir"])
                examples_list.extend([x for x in result_json if x["type"] == "file"])

            if len(examples_list) < 1:
                errors.append(ERROR_MISSING_EXAMPLE_FILES)
            else:

                def __check_lib_name(
                    repo_name, file_name
                ):  # pylint: disable=unused-private-member
                    """Nested function to test example file names.
                    Allows examples to either match the repo name,
                    or have additional underscores separating the repo name.
                    """
                    file_names = set()
                    file_names.add(file_name)

                    name_split = file_name.split("_")
                    name_rebuilt = "".join(
                        (part for part in name_split if ".py" not in part)
                    )

                    if name_rebuilt:  # avoid adding things like 'simpletest.py' -> ''
                        file_names.add(name_rebuilt)

                    return any(name.startswith(repo_name) for name in file_names)

                lib_name_start = repo["name"].rfind("CircuitPython_") + 14
                lib_name = repo["name"][lib_name_start:].lower()

                all_have_name = True
                simpletest_exists = False
                for example in examples_list:
                    if example["name"].endswith(".py"):
                        check_lib_name = __check_lib_name(
                            lib_name, example["name"].lower()
                        )
                        if not check_lib_name:
                            all_have_name = False
                    if "simpletest" in example["name"].lower():
                        simpletest_exists = True
                if not all_have_name:
                    errors.append(ERROR_EXAMPLE_MISSING_SENSORNAME)
                if not simpletest_exists:
                    errors.append(ERROR_MISSING_EXAMPLE_SIMPLETEST)
        else:
            errors.append(ERROR_MISSING_EXAMPLE_FOLDER)

        # first location .py files whose names begin with "adafruit_"
        re_str = re.compile(r"adafruit\_[\w]*\.py")
        pyfiles = [
            x["download_url"] for x in content_list if re_str.fullmatch(x["name"])
        ]
        for pyfile in pyfiles:
            # adafruit_xxx.py file; check if for proper usage of u___ versions of modules
            errors.extend(self._validate_py_for_u_modules(pyfile))

        # now location any directories whose names begin with "adafruit_"
        re_str = re.compile(r"adafruit\_[\w]*")
        for adir in dirs:
            if re_str.fullmatch(adir):
                # retrieve the files in that directory
                dir_file_list = github.get(
                    "/repos/" + repo["full_name"] + "/contents/" + adir
                )
                if not dir_file_list.ok:
                    errors.append(ERROR_UNABLE_PULL_REPO_DIR)
                dir_file_list = dir_file_list.json()
                # search for .py files in that directory
                dir_files = [
                    x["download_url"]
                    for x in dir_file_list
                    if x["type"] == "file" and x["name"].endswith(".py")
                ]
                for dir_file in dir_files:
                    # .py files in subdirectory adafruit_xxx
                    # check if for proper usage of u___ versions of modules
                    errors.extend(self._validate_py_for_u_modules(dir_file))

        return errors

    def validate_readthedocs(self, repo):
        """Method to check the health of `repo`'s ReadTheDocs."""
        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []
        if repo["name"] in BUNDLE_IGNORE_LIST:
            return []
        if not self.rtd_subprojects:
            rtd_response = requests.get(
                "https://readthedocs.org/api/v2/project/74557/subprojects/", timeout=15
            )
            if not rtd_response.ok:
                return [ERROR_RTD_SUBPROJECT_FAILED]
            self.rtd_subprojects = {}
            for subproject in rtd_response.json()["subprojects"]:
                self.rtd_subprojects[
                    common_funcs.sanitize_url(subproject["repo"])
                ] = subproject

        repo_url = common_funcs.sanitize_url(repo["clone_url"])
        if repo_url not in self.rtd_subprojects:
            return [ERROR_RTD_SUBPROJECT_MISSING]

        errors = []
        subproject = self.rtd_subprojects[repo_url]

        if 105398 not in subproject["users"]:
            errors.append(ERROR_RTD_ADABOT_MISSING)

        valid_versions = requests.get(
            "https://readthedocs.org/api/v2/project/{}/active_versions/".format(
                subproject["id"]
            ),
            timeout=15,
        )
        if not valid_versions.ok:
            errors.append(ERROR_RTD_VALID_VERSIONS_FAILED)
        else:
            valid_versions = valid_versions.json()
            latest_release = github.get(
                "/repos/{}/releases/latest".format(repo["full_name"])
            )
            if not latest_release.ok:
                errors.append(ERROR_GITHUB_RELEASE_FAILED)
            # disabling this for now, since it is ignored and always fails
            # else:
            #    if (
            #       latest_release.json()["tag_name"] not in
            #       [tag["verbose_name"] for tag in valid_versions["versions"]]
            #   ):
            #        errors.append(ERROR_RTD_MISSING_LATEST_RELEASE)

        # There is no API which gives access to a list of builds for a project so we parse the html
        # webpage.
        builds_webpage = requests.get(
            "https://readthedocs.org/projects/{}/builds/".format(subproject["slug"]),
            timeout=15,
        )
        # pylint: disable=too-many-nested-blocks
        # TODO: look into reducing the number of nested blocks.
        if not builds_webpage.ok:
            errors.append(ERROR_RTD_FAILED_TO_LOAD_BUILDS)
        else:
            for line in builds_webpage.text.split("\n"):
                if '<div id="build-' in line:
                    build_id = line.split('"')[1][len("build-") :]
                # We only validate the most recent, latest build. So, break when the first "version
                # latest" found. Its in the page after the build id.
                if "version latest" in line:
                    break
            build_info = requests.get(
                "https://readthedocs.org/api/v2/build/{}/".format(build_id), timeout=15
            )
            if not build_info.ok:
                errors.append(ERROR_RTD_FAILED_TO_LOAD_BUILD_INFO)
            else:
                build_info = build_info.json()
                output_ok = True
                autodoc_ok = True
                sphinx_ok = True
                for command in build_info["commands"]:
                    if command["command"].endswith("_build/html"):
                        for line in command["output"].split("\n"):
                            if "... " in line:
                                _, line = line.split("... ")
                            if "WARNING" in line or "ERROR" in line:
                                if not line.startswith(("WARNING", "ERROR")):
                                    line = line.split(" ", 1)[1]
                                if not line.startswith(RTD_IGNORE_NOTICES):
                                    output_ok = False
                            elif line.startswith("ImportError"):
                                autodoc_ok = False
                            elif line.startswith("sphinx.errors") or line.startswith(
                                "SphinxError"
                            ):
                                sphinx_ok = False
                        break
                if not output_ok:
                    errors.append(ERROR_RTD_OUTPUT_HAS_WARNINGS)
                if not autodoc_ok:
                    errors.append(ERROR_RTD_AUTODOC_FAILED)
                if not sphinx_ok:
                    errors.append(ERROR_RTD_SPHINX_FAILED)

        return errors

    def validate_core_driver_page(self, repo):
        """Method to ensure that `repo` is listed on the main driver page in the bundle."""
        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []
        if repo["name"] in BUNDLE_IGNORE_LIST:
            return []
        if not self.core_driver_page:
            driver_page = requests.get(
                (
                    "https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/"
                    "main/docs/drivers.rst"
                ),
                timeout=15,
            )
            if not driver_page.ok:
                return [ERROR_DRIVERS_PAGE_DOWNLOAD_FAILED]
            self.core_driver_page = driver_page.text

        repo_short_name = repo["name"][len("Adafruit_CircuitPython_") :].lower()
        full_url = (
            "https://circuitpython.readthedocs.io/projects/"
            + repo_short_name
            + "/en/latest/"
        )
        full_url_dashes = full_url.replace("_", "-")
        if (
            full_url not in self.core_driver_page
            and full_url_dashes not in self.core_driver_page
        ):
            return [ERROR_DRIVERS_PAGE_DOWNLOAD_MISSING_DRIVER]
        return []

    # TODO: this could probably be moved to `common_funcs` and used through Adabot
    def github_get_all_pages(self, url, params):
        """Retrieves all paginated results from the GitHub `url`."""
        results = []
        response = github.get(url, params=params)

        if not response.ok:
            self.output_file_data.append(f"Github request failed: {url}")
            return ERROR_OUTPUT_HANDLER

        while response.ok:
            results.extend(response.json())

            if response.links.get("next"):
                response = github.get(response.links["next"]["url"])
            else:
                break

        return results

    # pylint: disable=too-many-nested-blocks
    def gather_insights(self, repo, insights, since, show_closed_metric=False):
        """Gather analytics about a repository like open and merged pull requests.
        This expects a dictionary with GitHub API repository state (like from the
        list_repos function) and will fill in the provided insights dictionary
        with analytics it computes for the repository.
        """

        if repo["owner"]["login"] != "adafruit":
            return []
        params = {
            "sort": "updated",
            "state": "all",
            "per_page": 100,
            "since": since.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        issues = self.github_get_all_pages(
            "/repos/" + repo["full_name"] + "/issues", params=params
        )
        if issues == ERROR_OUTPUT_HANDLER:
            return [ERROR_OUTPUT_HANDLER]

        for issue in issues:
            created = datetime.datetime.strptime(
                issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"
            )
            if "pull_request" in issue:
                pr_info = github.get(issue["pull_request"]["url"])
                pr_info = pr_info.json()
                if issue["state"] == "open":
                    if created > since:
                        insights["new_prs"] += 1
                        insights["pr_authors"].add(pr_info["user"]["login"])
                    insights["active_prs"] += 1
                else:
                    merged = datetime.datetime.strptime(
                        issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                    if pr_info["merged"] and merged > since:
                        merged_info = ""
                        if show_closed_metric:
                            created = datetime.datetime.strptime(
                                issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"
                            )
                            merged = datetime.datetime.strptime(
                                issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ"
                            )

                            days_open = merged - created
                            if days_open.days < 0:  # opened earlier today
                                days_open += datetime.timedelta(
                                    days=(days_open.days * -1)
                                )
                            elif days_open.days == 0:
                                days_open += datetime.timedelta(days=(1))
                            merged_info = " (Days open: {})".format(days_open.days)

                        pr_link = "{0}{1}".format(
                            issue["pull_request"]["html_url"], merged_info
                        )
                        insights["merged_prs"].append(pr_link)

                        pr_author = pr_info["user"]["login"]
                        if pr_author == "weblate":
                            pr_commits = github.get(str(pr_info["url"]) + "/commits")
                            if pr_commits.ok:
                                for commit in pr_commits.json():
                                    author = commit.get("author")
                                    if author:
                                        insights["pr_merged_authors"].add(
                                            author["login"]
                                        )
                        else:
                            insights["pr_merged_authors"].add(pr_info["user"]["login"])

                        insights["pr_reviewers"].add(pr_info["merged_by"]["login"])
                        pr_reviews = github.get(str(pr_info["url"]) + "/reviews")
                        if pr_reviews.ok:
                            for review in pr_reviews.json():
                                if review["state"].lower() == "approved":
                                    insights["pr_reviewers"].add(
                                        review["user"]["login"]
                                    )
                    else:
                        insights["closed_prs"] += 1
            else:
                issue_info = github.get(issue["url"])
                issue_info = issue_info.json()
                if issue["state"] == "open":
                    if created > since:
                        insights["new_issues"] += 1
                        insights["issue_authors"].add(issue_info["user"]["login"])
                    insights["active_issues"] += 1

                else:
                    insights["closed_issues"] += 1
                    insights["issue_closers"].add(issue_info["closed_by"]["login"])

        params = {"state": "open", "per_page": 100}
        issues = self.github_get_all_pages(
            "/repos/" + repo["full_name"] + "/issues", params=params
        )
        if issues == ERROR_OUTPUT_HANDLER:
            return [ERROR_OUTPUT_HANDLER]

        for issue in issues:
            created = datetime.datetime.strptime(
                issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"
            )
            days_open = datetime.datetime.today() - created
            if days_open.days < 0:  # opened earlier today
                days_open += datetime.timedelta(days=(days_open.days * -1))
            if "pull_request" in issue:
                pr_link = "{0} (Open {1} days)".format(
                    issue["pull_request"]["html_url"], days_open.days
                )
                insights["open_prs"].append(pr_link)
            else:
                issue_link = "{0} (Open {1} days)".format(
                    issue["html_url"], days_open.days
                )
                insights["open_issues"].append(issue_link)
                if "labels" in issue:
                    for i in issue["labels"]:
                        if i["name"] == "good first issue":
                            insights["good_first_issues"] += 1

        # process Hacktoberfest labels if it is Hacktoberfest season
        in_season, season_action = hacktober.is_hacktober_season()
        if in_season:
            hacktober_issues = [
                issue for issue in issues if "pull_request" not in issue
            ]
            if season_action == "add":
                insights["hacktober_assigned"] += hacktober.assign_hacktoberfest(
                    repo, issues=hacktober_issues
                )
            elif season_action == "remove":
                insights["hacktober_removed"] += hacktober.assign_hacktoberfest(
                    repo, issues=hacktober_issues, remove_labels=True
                )

        # get milestones for core repo
        if repo["name"] == "circuitpython":
            params = {"state": "open"}
            response = github.get(
                "/repos/adafruit/circuitpython/milestones", params=params
            )
            if not response.ok:
                self.output_file_data.append("Failed to get core milestone insights.")
                return [ERROR_OUTPUT_HANDLER]

            milestones = response.json()
            for milestone in milestones:
                insights["milestones"][milestone["title"]] = milestone["open_issues"]
        return []

    def validate_in_pypi(self, repo):
        """prints a list of Adafruit_CircuitPython libraries that are in pypi"""
        if (
            repo["name"] in BUNDLE_IGNORE_LIST
            or repo["name"] in self.has_setup_py_disabled
        ):
            return []
        if not (
            repo["owner"]["login"] == "adafruit"
            and repo["name"].startswith("Adafruit_CircuitPython")
        ):
            return []
        if not common_funcs.repo_is_on_pypi(repo):
            return [ERROR_NOT_ON_PYPI]
        return []

    def validate_labels(self, repo):
        """ensures the repo has the standard labels available"""
        response = github.get("/repos/" + repo["full_name"] + "/labels")
        if not response.ok:
            # replace 'output_handler' with ERROR_OUTPUT_HANDLER
            self.output_file_data.append(
                "Labels request failed: {}".format(repo["full_name"])
            )
            return [ERROR_OUTPUT_HANDLER]

        errors = []

        repo_labels = [label["name"] for label in response.json()]

        has_all_labels = True
        for label, info in STD_REPO_LABELS.items():
            if not label in repo_labels:
                response = github.post(
                    "/repos/" + repo["full_name"] + "/labels",
                    json={"name": label, "color": info["color"]},
                )
                if not response.ok:
                    has_all_labels = False
                    self.output_file_data.append(
                        "Request to add '{}' label failed: {}".format(
                            label, repo["full_name"]
                        )
                    )
                    if ERROR_OUTPUT_HANDLER not in errors:
                        errors.append(ERROR_OUTPUT_HANDLER)

        if not has_all_labels:
            errors.append(ERROR_MISSING_STANDARD_LABELS)

        return errors

    def validate_passes_linting(self, repo):
        """Clones the repo and runs pylint on the Python files"""
        if not repo["name"].startswith("Adafruit_CircuitPython"):
            return []

        ignored_py_files = ["setup.py", "conf.py"]

        desination_type = TemporaryDirectory
        if self.keep_repos:
            desination_type = pathlib.Path("repos").absolute

        with desination_type() as tempdir:
            repo_dir = pathlib.Path(tempdir) / repo["name"]
            try:
                if not repo_dir.exists():
                    git.clone("--depth=1", repo["git_url"], repo_dir)
            except sh.ErrorReturnCode as err:
                self.output_file_data.append(
                    f"Failed to clone repo for linting: {repo['full_name']}\n {err.stderr}"
                )
                return [ERROR_OUTPUT_HANDLER]

            if self.keep_repos and (repo_dir / ".pylint-ok").exists():
                return []

            for file in repo_dir.rglob("*.py"):
                if file.name in ignored_py_files or str(file.parent).endswith(
                    "examples"
                ):
                    continue

                pylint_args = [str(file)]
                if (repo_dir / ".pylintrc").exists():
                    pylint_args += [f"--rcfile={str(repo_dir / '.pylintrc')}"]

                reporter = CapturedJsonReporter()

                logging.debug("Running pylint on %s", file)

                lint.Run(pylint_args, reporter=reporter, exit=False)
                pylint_stderr = ""
                pylint_stdout = reporter.get_result()

                if pylint_stderr:
                    self.output_file_data.append(
                        f"PyLint error ({repo['name']}): '{pylint_stderr}'"
                    )
                    return [ERROR_OUTPUT_HANDLER]

                try:
                    pylint_result = json.loads(pylint_stdout)
                except json.JSONDecodeError as json_err:
                    self.output_file_data.append(
                        f"PyLint output JSONDecodeError: {json_err.msg}"
                    )
                    return [ERROR_OUTPUT_HANDLER]

                if pylint_result:
                    return [ERROR_PYLINT_FAILED_LINTING]

            if self.keep_repos:
                with open(repo_dir / ".pylint-ok", "w") as pylint_ok:
                    pylint_ok.write("".join(pylint_result))

        return []

    def validate_default_branch(self, repo):
        """Makes sure that the default branch is main"""
        if not repo["name"].startswith("Adafruit_CircuitPython"):
            return []

        if repo["default_branch"] != "main":
            return [ERROR_INCORRECT_DEFAULT_BRANCH]

        return []
