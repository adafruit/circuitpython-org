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
"""
`adafruit_adabot`
====================================================

TODO(description)

* Author(s): Scott Shawcroft
"""
import os
import sys

import requests


def _fix_url(url):
    if url.startswith("/"):
        url = "https://api.travis-ci.com" + url
    return url

def _auth_token():
    if not "ADABOT_TRAVIS_ACCESS_TOKEN" in os.environ:
        print("Please configure the ADABOT_TRAVIS_ACCESS_TOKEN environment variable.")
        return "token "
    return "token {}".format(os.environ["ADABOT_TRAVIS_ACCESS_TOKEN"])

def _fix_kwargs(kwargs):
    user_agent = "AdafruitAdabot"
    if "headers" in kwargs:
        kwargs["headers"]["Authorization"] = _auth_token()
        kwargs["headers"]["User-Agent"] = user_agent
        kwargs["headers"]["Travis-API-Version"] = "3"
    else:
        kwargs["headers"] = {
            "Authorization": _auth_token(),
            "User-Agent": user_agent,
            "Travis-API-Version": "3"
        }
    return kwargs

def get(url, **kwargs):
    return requests.get(_fix_url(url), timeout=30, **_fix_kwargs(kwargs))

def post(url, **kwargs):
    return requests.post(_fix_url(url), timeout=30, **_fix_kwargs(kwargs))

def put(url, **kwargs):
    return requests.put(_fix_url(url), timeout=30, **_fix_kwargs(kwargs))
