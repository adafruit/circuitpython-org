# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

""" Helper for requests to pypi.org

* Author(s): Michael McWethy
"""

import requests

from adabot import REQUESTS_TIMEOUT


def _fix_url(url):
    if url.startswith("/"):
        url = "https://pypi.org" + url
    return url


def get(url, **kwargs):
    """Process a GET request from pypi.org"""
    return requests.get(_fix_url(url), timeout=REQUESTS_TIMEOUT, **kwargs)
