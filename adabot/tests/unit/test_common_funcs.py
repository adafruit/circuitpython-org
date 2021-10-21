# The MIT License (MIT)
#
# Copyright (c) 2021 Michael Schroeder
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

"""Unit tests for 'adabot/lib/common_funcs.py'"""

import datetime
import re

import pytest  # pylint: disable=unused-import
import requests

from adabot.lib import common_funcs
from adabot import github_requests


def test_list_repos():
    """Test that list_repos returns a list object."""
    repos = common_funcs.list_repos()

    assert isinstance(repos, list)


def test_repo_is_on_pypi_true():
    """Test 'repo_is_on_pypi'"""
    assert common_funcs.repo_is_on_pypi({"name": "pytest"})


sani_urls = [
    {"id": "sanitize http://", "url": "http://www.website.com/"},
    {"id": "sanitize https://", "url": "https://www.website.com"},
    {"id": "sanitize git://", "url": "git://www.website.com"},
    {"id": "sanitize ://*.git", "url": "http://www.website.com/page.git"},
]


@pytest.mark.parametrize("urls", sani_urls, ids=[url["id"] for url in sani_urls])
def test_sanitize_url(urls):
    """Test 'sanitize_urls'"""
    assert re.match(
        r"^(?!http|https|git)(?:\:\/\/){0,1}.+(?<!.git)$",
        common_funcs.sanitize_url(urls["url"]),
    )


doc_links = [
    {
        "id": "valid link",
        "content": (
            ".. image:: https://readthedocs.org/projects/adafruit-circuitpython-testrepo/badge/"
            "?version=latest\n    :target: https://circuitpython.readthedocs.io/projects/testrepo/"
            "en/latest/\n:alt: Documentation Status"
        ),
        "path": "repo",
        "expects": "https://circuitpython.readthedocs.io/projects/testrepo/en/latest/",
    },
    {
        "id": "no valid link",
        "content": "This is not valid.\n" * 15,
        "path": "repo",
        "expects": None,
    },
    {"id": "FileNotFoundError", "content": "", "path": "not_repo", "expects": None},
]


@pytest.mark.parametrize("links", doc_links, ids=[link["id"] for link in doc_links])
def test_get_docs_link(links, tmp_path):
    """Test 'get_docs_link'"""
    mock_submod_path = ["", {"path": links["path"]}]
    readme_path = tmp_path / "repo"
    readme_path.mkdir()
    readme = readme_path / "README.rst"
    readme.write_text(links["content"])

    assert links["expects"] == common_funcs.get_docs_link(tmp_path, mock_submod_path)


def published_date(subtract_days=0):
    """Utility to return a formatted date"""
    pub_date = datetime.datetime.today()
    pub_date = pub_date - datetime.timedelta(days=subtract_days)
    return datetime.datetime.strftime(pub_date, "%Y-%m-%dT%H:%M:%SZ")


mock_repo_results = [
    {
        "id": "new library",
        "name": "new_library",
        "latest": f'{{"published_at":"{published_date()}"}}',
        "releases": f'[{{"published_at":"{published_date()}"}}]',
        "expects": "new",
    },
    {
        "id": "updated library",
        "name": "updated_library",
        "latest": f'{{"published_at":"{published_date(subtract_days=6)}"}}',
        "releases": (
            "["
            f'{{"published_at":"{published_date(subtract_days=7)}"}},'
            f'{{"published_at":"{published_date(subtract_days=10)}"}}'
            "]"
        ),
        "expects": "updated",
    },
    {
        "id": "non-updated library",
        "name": "non_updated_library",
        "latest": f'{{"published_at":"{published_date(subtract_days=16)}"}}',
        "releases": f'[{{"published_at":"{published_date(subtract_days=16)}"}}]',
        "expects": None,
    },
]


@pytest.mark.parametrize(
    "repos", mock_repo_results, ids=[repo["id"] for repo in mock_repo_results]
)
# pylint: disable=protected-access
def test_is_new_or_updated(monkeypatch, repos):
    """Test 'is_new_or_updated'"""

    def mock_github_get(url):
        """Mock 'github_requests.get()' for testing"""
        mock_repo_key = url.split("/")[-1]

        result = requests.Response()
        result.status_code = 200
        result.encoding = "utf-8"
        result._content = repos[mock_repo_key].encode()

        return result

    monkeypatch.setattr(github_requests, "get", mock_github_get)

    assert repos["expects"] == common_funcs.is_new_or_updated(repos)
