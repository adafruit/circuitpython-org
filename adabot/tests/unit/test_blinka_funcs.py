# SPDX-FileCopyrightText: 2021 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Unit tests for 'adabot/lib/blinka_funcs.py'"""

import pytest  # pylint: disable=unused-import

from adabot.lib import blinka_funcs


def test_board_count():
    """Test that 'board_count' returns a number."""
    assert blinka_funcs.board_count() >= 0
