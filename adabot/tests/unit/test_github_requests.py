# SPDX-FileCopyrightText: 2021 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Unit tests for 'adabot/github_requests.py'"""

# pylint: disable=protected-access

import pytest  # pylint: disable=unused-import

from adabot import github_requests


def test_fix_url():
    """Test URL fixing function."""
    url = github_requests._fix_url("/meta")
    assert url == "https://api.github.com/meta"


def test_fix_kwargs():
    """Test kwarg fixing function."""
    dummy_kwargs = github_requests._fix_kwargs({})

    assert "headers" in dummy_kwargs
    assert "Accept" in dummy_kwargs["headers"]
