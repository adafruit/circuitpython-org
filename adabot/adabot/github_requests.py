# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

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
        # If rate limit remaining is missing, then assume we're fine. Use a million to signify this
        # case. GitHub will be in the single thousands.
        remaining = int(response.headers.get("X-RateLimit-Remaining", 1000000))
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

    if not from_cache:
        if remaining % 100 == 0 or remaining < 20:
            logging.info("%d requests remaining this hour", remaining)
    if not from_cache and remaining <= 1:
        rate_limit_reset = datetime.datetime.fromtimestamp(
            int(response.headers["X-RateLimit-Reset"])
        )
        logging.warning(
            "GitHub API Rate Limit reached. Pausing until Rate Limit reset."
        )
        # This datetime.now() is correct, *because* `fromtimestamp` above
        # converts the timestamp into local time, same as now(). This is
        # different than the sites that use GH_INTERFACE.get_rate_limit, in
        # which the rate limit is a UTC time, so it has to be compared to
        # utcnow.
        while datetime.datetime.now() < rate_limit_reset:
            logging.warning("Rate Limit will reset at: %s", rate_limit_reset)
            reset_diff = rate_limit_reset - datetime.datetime.now()

            logging.info("Sleeping %s seconds", reset_diff.seconds)
            time.sleep(reset_diff.seconds + 1)

    return response


get = functools.partial(request, "get")
post = functools.partial(request, "post")
put = functools.partial(request, "put")
delete = functools.partial(request, "delete")
patch = functools.partial(request, "patch")
