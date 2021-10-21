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

"""Integration tests for 'adabot/update_cp_org_libraries.py'"""

import pytest  # pylint: disable=unused-import

from adabot.lib import common_funcs
from adabot import github_requests
from adabot import update_cp_org_libraries

# pylint: disable=unused-argument
def mock_list_repos(*args, **kwargs):
    """Function to monkeypatch `common_funcs.list_repos()` for a shorter set of repos."""
    return [
        github_requests.get("/repos/adafruit/Adafruit_CircuitPython_TestRepo").json()
    ]


# pylint: disable=unused-argument
def mock_get_contribs(*args):
    """Function to monkeypatch `update_cp_org_libraries.get_contributors()` to ensure
    proper testing of usage. Monkeypatched `list_repos` will likely not produce results.
    """
    contribs = ["test_user1", "test_user2"]
    reviewers = ["test_reviewer1", "test_reviewer2"]
    merged_pr_count = 4

    return contribs, reviewers, merged_pr_count


def test_update_cp_org_libraries(monkeypatch):
    """Test main function of 'circuitpyton_libraries.py', without writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)
    monkeypatch.setattr(update_cp_org_libraries, "get_contributors", mock_get_contribs)

    update_cp_org_libraries.main()


# pylint: disable=invalid-name
def test_update_cp_org_libraries_output_file(monkeypatch, tmp_path, capsys):
    """Test main funciton of 'update_cp_org_libraries.py', with writing an output file."""

    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)
    monkeypatch.setattr(update_cp_org_libraries, "get_contributors", mock_get_contribs)

    tmp_output_file = tmp_path / "output_test.txt"

    update_cp_org_libraries.main(output_file=tmp_output_file)

    captured = capsys.readouterr()

    assert tmp_output_file.read_text() == captured.out
