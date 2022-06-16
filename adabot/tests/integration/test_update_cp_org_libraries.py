# SPDX-FileCopyrightText: 2021 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Integration tests for 'adabot/update_cp_org_libraries.py'"""

import json

import pytest  # pylint: disable=unused-import

from adabot.lib import common_funcs
from adabot import github_requests
from adabot import update_cp_org_libraries

# pylint: disable=unused-argument
def mock_list_repos(*args, **kwargs):
    """Function to monkeypatch `common_funcs.list_repos()` for a shorter set of repos."""
    repos = []
    result = github_requests.get(
        "/search/repositories",
        params={
            "q": "Adafruit_CircuitPython user:adafruit archived:false fork:true",
            "per_page": 100,
            "sort": "updated",
            "order": "asc",
        },
    )

    if result.ok:
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

    repo_names = [repo["name"] for repo in repos]

    if kwargs.get("include_repos", False):
        for repo in kwargs["include_repos"]:
            if repo not in repo_names:
                add_repo = github_requests.get("/repos/adafruit/" + repo)
                if add_repo.ok:
                    repos.append(add_repo.json())
                else:
                    print("list_repos(): Failed to retrieve '{}'".format(repo))

    if len(repos) > 5:
        repos = repos[:5]

    return repos


# pylint: disable=unused-argument
def mock_get_contribs(*args):
    """Function to monkeypatch `update_cp_org_libraries.get_contributors()` to ensure
    proper testing of usage. Monkeypatched `list_repos` will likely not produce results.
    """
    contribs = ["test_user1", "test_user2"]
    reviewers = ["test_reviewer1", "test_reviewer2"]
    merged_pr_count = 4

    return contribs, reviewers, merged_pr_count


def test_update_cp_org_libraries(monkeypatch):
    """Test main function of 'circuitpyton_libraries.py', without writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)
    monkeypatch.setattr(update_cp_org_libraries, "get_contributors", mock_get_contribs)

    update_cp_org_libraries.main(loglevel="INFO")


# pylint: disable=invalid-name
def test_update_cp_org_libraries_output_file(monkeypatch, tmp_path, capsys):
    """Test main funciton of 'update_cp_org_libraries.py', with writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)
    monkeypatch.setattr(update_cp_org_libraries, "get_contributors", mock_get_contribs)

    tmp_output_file = tmp_path / "output_test.txt"

    update_cp_org_libraries.main(loglevel="INFO", output_file=tmp_output_file)

    output = tmp_output_file.read_text()

    assert json.loads(output)
