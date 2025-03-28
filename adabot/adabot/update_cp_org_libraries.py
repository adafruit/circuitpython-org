# SPDX-FileCopyrightText: 2019 Michael Schroeder
#
# SPDX-License-Identifier: MIT

"""Adabot utility for updating circuitpython.org libraries info."""

# pylint: disable=redefined-outer-name

import argparse
import datetime
import inspect
import json
import logging
import re
import sys

from adabot.lib import common_funcs
from adabot.lib import circuitpython_library_validators as cpy_vals
from adabot import github_requests as gh_reqs
from adabot import pypi_requests as pypi

logger = logging.getLogger(__name__)
ch = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(format="%(message)s", handlers=[ch])


DO_NOT_VALIDATE = [
    "CircuitPython_Community_Bundle",
    "cookiecutter-adafruit-circuitpython",
]

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Adabot utility for updating circuitpython.org libraries info.",
    prog="Adabot circuitpython.org/libraries Updater",
)
cmd_line_parser.add_argument(
    "-o",
    "--output_file",
    help="Output JSON file to the filename provided.",
    metavar="<OUTPUT FILENAME>",
    dest="output_file",
)
cmd_line_parser.add_argument(
    "--cache-http",
    help="Cache HTTP requests using requests_cache",
    action="store_true",
    default=False,
)
cmd_line_parser.add_argument(
    "--cache-ttl", help="HTTP cache TTL", type=int, default=7200
)
cmd_line_parser.add_argument(
    "--keep-repos", help="Keep repos between runs", action="store_true", default=False
)
cmd_line_parser.add_argument(
    "--loglevel", help="Adjust the log level (default INFO)", type=str, default="INFO"
)

sort_re = re.compile(r"(?<=\(Open\s)(.+)(?=\sdays)")


def get_open_issues_and_prs(repo):
    """Retreive all of the open issues (minus pull requests) for the repo."""
    open_issues = []
    open_pull_requests = []
    params = {"state": "open"}
    result = gh_reqs.get("/repos/adafruit/" + repo["name"] + "/issues", params=params)
    if not result.ok:
        return [], []

    issues = result.json()
    for issue in issues:
        created = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        days_open = datetime.datetime.today() - created
        if days_open.days < 0:  # opened earlier today
            days_open += datetime.timedelta(days=(days_open.days * -1))

        issue_title = "{0} (Open {1} days)".format(issue["title"], days_open.days)
        if "pull_request" not in issue:  # ignore pull requests
            issue_labels = ["None"]
            if len(issue["labels"]) != 0:
                issue_labels = [label["name"] for label in issue["labels"]]

            issue_dict = {
                "title": issue_title,
                "url": issue["html_url"],
                "labels": issue_labels,
            }

            open_issues.append(issue_dict)
        else:
            open_pull_requests.append({issue["html_url"]: issue_title})

    return open_issues, open_pull_requests


def get_contributors(repo):
    """Gather contributor information."""
    contributors = []
    reviewers = []
    merged_pr_count = 0
    params = {"state": "closed", "sort": "updated", "direction": "desc"}
    result = gh_reqs.get("/repos/adafruit/" + repo["name"] + "/pulls", params=params)
    if result.ok:
        today_minus_seven = datetime.datetime.today() - datetime.timedelta(days=7)
        pull_requests = result.json()
        for pull_request in pull_requests:
            merged_at = datetime.datetime.min
            if "merged_at" in pull_request:
                if pull_request["merged_at"] is None:
                    continue
                merged_at = datetime.datetime.strptime(
                    pull_request["merged_at"], "%Y-%m-%dT%H:%M:%SZ"
                )
            else:
                continue
            if merged_at < today_minus_seven:
                continue
            contributors.append(pull_request["user"]["login"])
            merged_pr_count += 1

            # get reviewers (merged_by, and any others)
            single_pr = gh_reqs.get(pull_request["url"])
            if not single_pr.ok:
                continue
            pr_info = single_pr.json()
            reviewers.append(pr_info["merged_by"]["login"])
            pr_reviews = gh_reqs.get(str(pr_info["url"]) + "/reviews")
            if not pr_reviews.ok:
                continue
            for review in pr_reviews.json():
                if review["state"].lower() == "approved":
                    reviewers.append(review["user"]["login"])

    return contributors, reviewers, merged_pr_count


# pylint: disable=too-many-locals,too-many-branches,too-many-statements
def main(
    loglevel="ERROR",
    keep_repos=False,
    cache_http=False,
    cache_ttl=7200,
    output_file=None,
):
    """Main"""
    logger.setLevel(loglevel)
    logger.info("Running circuitpython.org/libraries updater...")

    run_time = datetime.datetime.now()

    logger.info("Run Date: %s", run_time.strftime("%d %B %Y, %I:%M%p"))

    if output_file:
        logger.info(" - Report output will be saved to: %s", output_file)
        file_handler = logging.FileHandler(output_file)
        logger.addHandler(file_handler)

    if cache_http:
        cpy_vals.gh_reqs.setup_cache(cache_ttl)

    repos = common_funcs.list_repos(
        include_repos=(
            "CircuitPython_Community_Bundle",
            "cookiecutter-adafruit-circuitpython",
        )
    )

    new_libs = {}
    updated_libs = {}
    open_issues_by_repo = {}
    open_prs_by_repo = {}
    contributors = set()
    reviewers = set()
    merged_pr_count_total = 0
    repos_by_error = {}

    default_validators = [
        vals[1]
        for vals in inspect.getmembers(cpy_vals.LibraryValidator)
        if vals[0].startswith("validate")
    ]
    bundle_submodules = common_funcs.get_bundle_submodules()

    latest_pylint = ""
    pylint_info = pypi.get("/pypi/pylint/json")
    if pylint_info and pylint_info.ok:
        latest_pylint = pylint_info.json()["info"]["version"]

    validator = cpy_vals.LibraryValidator(
        default_validators,
        bundle_submodules,
        latest_pylint,
        keep_repos=keep_repos,
    )

    for repo in repos:
        if (
            repo["name"] in cpy_vals.BUNDLE_IGNORE_LIST
            or repo["name"] == "circuitpython"
        ):
            continue
        repo_name = repo["name"]

        # get a list of new & updated libraries for the last week
        check_releases = common_funcs.is_new_or_updated(repo)
        if check_releases == "new":
            new_libs[repo_name] = repo["html_url"]
        elif check_releases == "updated":
            updated_libs[repo_name] = repo["html_url"]

        # get a list of open issues and pull requests
        check_issues, check_prs = get_open_issues_and_prs(repo)
        if check_issues:
            open_issues_by_repo[repo_name] = check_issues
        if check_prs:
            open_prs_by_repo[repo_name] = check_prs

        # get the contributors and reviewers for the last week
        get_contribs, get_revs, get_merge_count = get_contributors(repo)
        if get_contribs:
            contributors.update(get_contribs)
        if get_revs:
            reviewers.update(get_revs)
        merged_pr_count_total += get_merge_count

        if repo_name in DO_NOT_VALIDATE:
            continue

        # run repo validators to check for infrastructure errors
        errors = []
        try:
            errors = validator.run_repo_validation(repo)
        except Exception as err:  # pylint: disable=broad-except
            logging.exception("Unhandled exception %s", str(err))
            errors.extend([cpy_vals.ERROR_OUTPUT_HANDLER])
        for error in errors:
            if not isinstance(error, tuple):
                # check for an error occurring in the validator module
                if error == cpy_vals.ERROR_OUTPUT_HANDLER:
                    # print(errors, "repo output handler error:", validator.output_file_data)
                    logging.error(", ".join(validator.output_file_data))
                    validator.output_file_data.clear()
                if error not in repos_by_error:
                    repos_by_error[error] = []
                repos_by_error[error].append(repo["html_url"])
            else:
                if error[0] not in repos_by_error:
                    repos_by_error[error[0]] = []
                repos_by_error[error[0]].append(f"{repo['html_url']} ({error[1]} days)")

    # assemble the JSON data
    build_json = {
        "updated_at": run_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "contributors": sorted(contributors, key=str.lower),
        "reviewers": sorted(reviewers, key=str.lower),
        "merged_pr_count": str(merged_pr_count_total),
        "library_updates": {
            "new": {key: new_libs[key] for key in sorted(new_libs, key=str.lower)},
            "updated": {
                key: updated_libs[key] for key in sorted(updated_libs, key=str.lower)
            },
        },
        "open_issues": {
            key: open_issues_by_repo[key]
            for key in sorted(open_issues_by_repo, key=str.lower)
        },
        "pull_requests": {
            key: open_prs_by_repo[key]
            for key in sorted(open_prs_by_repo, key=str.lower)
        },
        "repo_infrastructure_errors": {
            key: repos_by_error[key] for key in sorted(repos_by_error, key=str.lower)
        },
    }

    logger.info("%s", json.dumps(build_json, indent=2))


if __name__ == "__main__":
    cmd_line_args = cmd_line_parser.parse_args()
    main(
        loglevel=cmd_line_args.loglevel,
        keep_repos=cmd_line_args.keep_repos,
        cache_http=cmd_line_args.cache_http,
        cache_ttl=cmd_line_args.cache_ttl,
        output_file=cmd_line_args.output_file,
    )
