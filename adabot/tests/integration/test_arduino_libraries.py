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

"""Integration tests for 'adabot/arduino_libraries.py'"""

import pytest  # pylint: disable=unused-import

from adabot import arduino_libraries
from adabot import github_requests


def mock_list_repos():
    """Function to monkeypatch `arduino_libraries.list_repos()` for a shorter set of repos."""

    return [github_requests.get("/repos/adafruit/Adafruit_NeoPixel").json()]


def test_adafruit_libraries(monkeypatch):
    """Test main arduino_libraries function, without writing an output file."""

    monkeypatch.setattr(arduino_libraries, "list_repos", mock_list_repos)

    arduino_libraries.main()


# pylint: disable=invalid-name
def test_adafruit_libraries_output_file(monkeypatch, tmp_path, capsys):
    """Test main arduino_libraries funciton, with writing an output file."""

    monkeypatch.setattr(arduino_libraries, "list_repos", mock_list_repos)

    tmp_output_file = tmp_path / "output_test.txt"

    arduino_libraries.main(output_file=tmp_output_file)

    captured = capsys.readouterr()

    assert tmp_output_file.read_text() == captured.out
