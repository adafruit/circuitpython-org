# SPDX-FileCopyrightText: 2021 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Unit tests for 'adabot/pypi_requests.py'"""

import pytest  # pylint: disable=unused-import

from adabot import pypi_requests


def test_fix_url():
    """Test URL fixing function."""
    url = pypi_requests._fix_url("/test")  # pylint: disable=protected-access
    assert url == "https://pypi.org/test"
