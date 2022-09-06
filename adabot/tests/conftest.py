# SPDX-FileCopyrightText: 2022 Alec Delaney, for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Configuration file for pytest (along with `pytest.ini`)"""


def pytest_addoption(parser):
    """Add options to the `pytest` command"""
    parser.addoption(
        "--use-tokens",
        action="store_true",
        default=False,
        help="Test commands that use environment tokens",
    )
