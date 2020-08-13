import json
from pathlib import Path
import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def contrib_data_json():
    contrib_data = None

    conf_yaml_dir = Path(__file__).resolve().parents[1]
    conf_yaml_file = conf_yaml_dir / "_config.yml"

    yaml_data = {}
    with open(conf_yaml_file) as file:
        yaml_data = yaml.safe_load(file.read())

    if yaml_data:
        json_url = yaml_data.get("jekyll_get_json", [{}])[0].get("json")
        result = requests.get(json_url)
        if result.ok:
            contrib_data = json.loads(result.text)

    return contrib_data
