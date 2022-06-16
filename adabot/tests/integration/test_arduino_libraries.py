# SPDX-FileCopyrightText: 2021 Michael Schroeder
#
# SPDX-License-Identifier: MIT

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
