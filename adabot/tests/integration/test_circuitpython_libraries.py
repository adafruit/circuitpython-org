import pytest

from adabot.lib import common_funcs
from adabot import github_requests
from adabot import circuitpython_libraries

def test_circuitpython_libraires(monkeypatch):
    
    def mock_list_repos(*args, **kwargs):
        repos = []
        repos.append(github_requests.get("/repos/adafruit/Adafruit_CircuitPython_TestRepo").json())
        return repos
    
    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)

    circuitpython_libraries.main(validator="all")

def test_circuitpython_libraires_output_file(monkeypatch, tmp_path, capsys):
    
    def mock_list_repos(*args, **kwargs):
        repos = []
        repos.append(github_requests.get("/repos/adafruit/Adafruit_CircuitPython_TestRepo").json())
        return repos
    
    monkeypatch.setattr(common_funcs, "list_repos", mock_list_repos)

    tmp_output_file = tmp_path / "output_test.txt"

    circuitpython_libraries.main(validator="all", output_file=tmp_output_file)

    captured = capsys.readouterr()

    assert tmp_output_file.read_text() == captured.out