# SPDX-FileCopyrightText: 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""

docs_status.py
==============

Functionality for checking the ReadTheDocs build status for libraries
in the Adafruit CircuitPython Bundle

* Author(s): Alec Delaney

"""

from typing import Any, Optional
import argparse
import time
import parse
import requests
from github.Repository import Repository
from github.ContentFile import ContentFile
from iterate_libraries import (
    iter_remote_bundle_with_func,
    RemoteLibFunc_IterResult,
)


def check_docs_status(
    lib_repo: Repository, rtd_token: str, *, debug: bool = True
) -> Optional[bool]:
    """Checks a library for  the latest documentation build status with the
    requested information

    .. note::

        The ReadTheDocs token must have sufficient privileges for accessing
        the API; therefore, only a maintainer can use this functionality.

    :param str gh_token: The Github token to be used for with the Github
        API
    :param str rtd_token: A ReadTheDocs API token with sufficient privileges
    :param bool debug: Whether to use debug print statements
    :return: Whether the documentation built successfully; returns None if it
        could not be determined
    :rtype: bool|None
    """

    if debug:
        print("Checking", lib_repo.name)

    # Get the README file contents
    content_file: ContentFile = lib_repo.get_contents("README.rst")
    readme_text = content_file.decoded_content.decode("utf-8")

    # Parse for the ReadTheDocs slug
    search_results: parse.Result = parse.search(
        "https://readthedocs.org/projects/{slug:S}/badge", readme_text
    )
    rtd_slug: str = search_results.named["slug"]
    rtd_slug = rtd_slug.replace("_", "-", -1)

    # GET the latest documentation build runs
    url = f"https://readthedocs.org/api/v3/projects/{rtd_slug}/builds/"
    headers = {"Authorization": f"token {rtd_token}"}
    response = requests.get(url, headers=headers)
    json_response: dict[str, Any] = response.json()

    # Return the results of the latest run
    doc_build_results: Optional[list[dict[str, Any]]] = json_response.get(
        "results", None
    )
    if doc_build_results is None:
        return None
    result = doc_build_results[0].get("success")
    if debug and not result:
        print(f"RTD build failed or unavailable for {lib_repo.name}")
    time.sleep(3)
    return result


def check_docs_statuses(
    gh_token: str, rtd_token: str
) -> list[RemoteLibFunc_IterResult[Optional[bool]]]:
    """Checks all the libraries in a cloned Adafruit CircuitPython Bundle
    to get the latest documentation build status with the requested
    information

    .. note::

        The ReadTheDocs token must have sufficient privileges for accessing
        the API; therefore, only a maintainer can use this functionality.

    :param str gh_token: The Github token to be used for with the Github
        API
    :param str rtd_token: A ReadTheDocs API token with sufficient privileges
    :return: A list of tuples containing paired Repository objects and
        documentation build statuses
    :rtype: list
    """

    return iter_remote_bundle_with_func(
        gh_token, [(check_docs_status, (rtd_token,), {"debug": True})]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check the RTD docs build status of the Bundle libraries"
    )
    parser.add_argument(
        "gh_token", metavar="GH_TOKEN", type=str, help="GitHub token with proper scopes"
    )
    parser.add_argument(
        "rtd_token", metavar="RTD_TOKEN", type=str, help="ReadTheDocs token"
    )

    args = parser.parse_args()

    results = check_docs_statuses(args.gh_token, args.rtd_token)
    fail_list = [
        repo_name.name
        for repo_name, repo_results in results
        if not repo_results[0]  # pylint: disable=singleton-comparison
    ]

    if fail_list:
        print("Failures for RTD builds:")
        for failure in fail_list:
            print(failure)
        RETURN_CODE = 1
    else:
        print("No failures for RTD builds!")
        RETURN_CODE = 0

    raise SystemExit(RETURN_CODE)
