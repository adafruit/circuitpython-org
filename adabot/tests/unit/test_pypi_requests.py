import pytest

from adabot import pypi_requests

def test_fix_url():
    url = pypi_requests._fix_url("/test")
    assert url == "https://pypi.org/test"