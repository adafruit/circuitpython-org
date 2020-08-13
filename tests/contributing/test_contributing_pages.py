import pytest
import requests
from bs4 import BeautifulSoup, SoupStrainer

contributing_pages = [
    {
        "test_id": "pull requests",
        "url_path": "/",
        "page_title": "Contributing - Pull Requests",
        "div_class_name": "libraries open-pull-requests",
        "list_item_class_name": "library-pr-li",
        "json_data_key": "pull_requests"
    },
    {
        "test_id": "open issues",
        "url_path": "/open-issues",
        "page_title": "Contributing - Open Issues",
        "div_class_name": "libraries open-issues",
        "list_item_class_name": "library-open-issue-li",
        "json_data_key": "open_issues"
    },
    {
        "test_id": "infrastructure issues",
        "url_path": "/library-infrastructure-issues",
        "page_title": "Contributing - Library Infrastructure Issues",
        "div_class_name": "libraries",
        "list_item_class_name": "library-libinfra-li",
        "json_data_key": "repo_infrastructure_errors"
    }
]

param_ids = [id["test_id"] for id in contributing_pages]

@pytest.mark.parametrize('page_data', contributing_pages, ids=param_ids)
def test_library_data(contrib_data_json, page_data):
    try:
        result = requests.get(
            "http://localhost:4000/contributing" + page_data["url_path"],
            allow_redirects=False,
        )
    except requests.exceptions.ConnectionError:
        pytest.skip("local server not running.")

    assert result.ok

    source = BeautifulSoup(result.content, "html.parser")
    assert source.title.string == page_data["page_title"]

    open_prs = BeautifulSoup(
        str(source),
        "html.parser",
        parse_only=SoupStrainer("div", class_=page_data["div_class_name"])
    )
    assert open_prs

    pr_list = open_prs.find_all("li", class_=page_data["list_item_class_name"])
    assert len(pr_list) == len(contrib_data_json[page_data["json_data_key"]])
