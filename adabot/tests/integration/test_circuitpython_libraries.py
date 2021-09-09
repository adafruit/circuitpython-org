# The MIT License (MIT)
#
# Copyright (c) 2021 Michael Schroeder
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

"""Integration tests for 'adabot/circuitpython_libraries.py'"""

import pytest  # pylint: disable=unused-import

from adabot.lib import common_funcs
from adabot import github_requests
from adabot import circuitpython_libraries

# pylint: disable=unused-argument
def mock_list_repos(*args, **kwargs):
    """Function to monkeypatch `common_funcs.list_repos()` for a shorter set of repos."""
    return [
        github_requests.get("/repos/adafruit/Adafruit_CircuitPython_TestRepo").json()
    ]


def test_circuitpython_libraires(monkeypatch):
    """Test main function of 'circuitpyton_libraries.py', without writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)

    circuitpython_libraries.main(validator="all")


# pylint: disable=invalid-name
def test_circuitpython_libraires_output_file(monkeypatch, tmp_path, capsys):
    """Test main funciton of 'circuitpython_libraries.py', with writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)

    tmp_output_file = tmp_path / "output_test.txt"

    circuitpython_libraries.main(validator="all", output_file=tmp_output_file)

    captured = capsys.readouterr()

    assert tmp_output_file.read_text() == captured.out
