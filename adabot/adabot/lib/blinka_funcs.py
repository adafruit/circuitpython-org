# SPDX-FileCopyrightText: 2019 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Common functions used with Adabot & Blinka interactions."""

from adabot import github_requests as github


def board_count():
    """Retrieve the number of boards currently supported by Adafruit_Blinka,
    via the count of files in circuitpython-org/_blinka.
    """
    count = 0
    cirpy_org_url = "/repos/adafruit/circuitpython-org/contents/_blinka"
    response = github.get(cirpy_org_url)
    if response.ok:
        response_json = response.json()
        count = len(response_json)

    return count
