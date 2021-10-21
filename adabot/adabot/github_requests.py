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

"""Wrapper for GitHub requests."""

from base64 import b64encode
import datetime
import functools
import logging
import os
import time
import traceback

import requests
import requests_cache

TIMEOUT = 60


def setup_cache(expire_after=7200):
    """Sets up a cache for requests."""
    requests_cache.install_cache(
        cache_name="github_cache",
        backend="sqlite",
        expire_after=expire_after,
        allowable_codes=(200, 404),
    )


def _fix_url(url):
    if url.startswith("/"):
        url = "https://api.github.com" + url
    return url


def _fix_kwargs(kwargs):
    api_version = (
        "application/vnd.github.scarlet-witch-preview+json;"
        "application/vnd.github.hellcat-preview+json"
    )
    if "headers" in kwargs:
        if "Accept" in kwargs["headers"]:
            kwargs["headers"]["Accept"] += ";" + api_version
        else:
            kwargs["headers"]["Accept"] = api_version
    else:
        kwargs["headers"] = {"Accept": "application/vnd.github.hellcat-preview+json"}
    if "ADABOT_GITHUB_ACCESS_TOKEN" in os.environ and "auth" not in kwargs:
        user = os.environ.get("ADABOT_GITHUB_USER", "")
        access_token = os.environ["ADABOT_GITHUB_ACCESS_TOKEN"]
        basic_encoded = b64encode(str(user + ":" + access_token).encode()).decode()
        auth_header = "Basic {}".format(basic_encoded)

        kwargs["headers"]["Authorization"] = auth_header

    return kwargs


def request(method, url, **kwargs):
    """Processes request for `url`."""
    try:
        response = getattr(requests, method)(
            _fix_url(url), timeout=TIMEOUT, **_fix_kwargs(kwargs)
        )
        from_cache = getattr(response, "from_cache", False)
        remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
        logging.debug(
            "GET %s %s status=%s",
            url,
            f"{'(cache)' if from_cache else '(%d remaining)' % remaining}",
            response.status_code,
        )
    except requests.RequestException:
        exception_text = traceback.format_exc()
        if "ADABOT_GITHUB_ACCESS_TOKEN" in os.environ:
            exception_text = exception_text.replace(
                os.environ["ADABOT_GITHUB_ACCESS_TOKEN"], "[secure]"
            )
        logging.critical("%s", exception_text)
        raise RuntimeError(
            "See log for error text that has been sanitized for secrets"
        ) from None

    if not from_cache and remaining <= 1:
        rate_limit_reset = datetime.datetime.fromtimestamp(
            int(response.headers["X-RateLimit-Reset"])
        )
        logging.warning(
            "GitHub API Rate Limit reached. Pausing until Rate Limit reset."
        )
        while datetime.datetime.now() < rate_limit_reset:
            logging.warning("Rate Limit will reset at: %s", rate_limit_reset)
            reset_diff = rate_limit_reset - datetime.datetime.now()

            logging.info("Sleeping %s seconds", reset_diff.seconds)
            time.sleep(reset_diff.seconds + 1)

        if remaining % 100 == 0:
            logging.info(remaining, "requests remaining this hour")

    return response


get = functools.partial(request, "get")
post = functools.partial(request, "post")
put = functools.partial(request, "put")
delete = functools.partial(request, "delete")
patch = functools.partial(request, "patch")
