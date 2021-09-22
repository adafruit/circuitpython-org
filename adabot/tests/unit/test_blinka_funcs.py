import pytest

from adabot.lib import blinka_funcs

def test_board_count():
    assert blinka_funcs.board_count() >= 0