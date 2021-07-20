import pytest
from adabot.lib import common_funcs

def test_list_repos():
    repos = common_funcs.list_repos()

    assert isinstance(repos, list)

def test_repo_is_on_pypi_true():
    assert common_funcs.repo_is_on_pypi({"name": "pytest"})
