import pytest

from adabot import github_requests

def test_fix_url():
    url = github_requests._fix_url("/meta")
    assert  url == "https://api.github.com/meta"

def test_fix_kwargs():
    dummy_kwargs = github_requests._fix_kwargs({})

    assert "headers" in dummy_kwargs
    assert "Accept" in dummy_kwargs["headers"]