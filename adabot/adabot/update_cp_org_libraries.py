# The MIT License (MIT)
#
# Copyright (c) 2019 Michael Schroeder
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

import argparse
import datetime
import inspect
import json
import logging
import os
import re

from adabot.lib import common_funcs
from adabot.lib import circuitpython_library_validators as cpy_vals
from adabot import github_requests as github
from adabot import pypi_requests as pypi

DO_NOT_VALIDATE = ['CircuitPython_Community_Bundle', 'cookiecutter-adafruit-circuitpython']

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Adabot utility for updating circuitpython.org libraries info.",
    prog="Adabot circuitpython.org/libraries Updater"
)
cmd_line_parser.add_argument(
    "-o", "--output_file",
    help="Output JSON file to the filename provided.",
    metavar="<OUTPUT FILENAME>",
    dest="output_file"
)
cmd_line_parser.add_argument(
    "--cache-http",
    help="Cache HTTP requests using requests_cache",
    action='store_true',
    default=False
)
cmd_line_parser.add_argument(
    "--cache-ttl",
    help="HTTP cache TTL",
    type=int,
    default=7200
)
cmd_line_parser.add_argument(
    "--keep-repos",
    help="Keep repos between runs",
    action='store_true',
    default=False
)
cmd_line_parser.add_argument(
    "--loglevel",
    help="Adjust the log level (default ERROR)",
    type=str,
    default='ERROR'
)

sort_re = re.compile(r'(?<=\(Open\s)(.+)(?=\sdays)')


def get_open_issues_and_prs(repo):
    """ Retreive all of the open issues (minus pull requests) for the repo.
    """
    open_issues = []
    open_pull_requests = []
    params = {"state":"open"}
    result = github.get("/repos/adafruit/" + repo["name"] + "/issues",
                        params=params)
    if not result.ok:
        return [], []

    issues = result.json()
    for issue in issues:
        created = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        days_open = datetime.datetime.today() - created
        if days_open.days < 0: # opened earlier today
            days_open += datetime.timedelta(days=(days_open.days * -1))

        issue_title = "{0} (Open {1} days)".format(issue["title"],
                                                   days_open.days)
        if "pull_request" not in issue: # ignore pull requests
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
    contributors = []
    reviewers = []
    merged_pr_count = 0
    params = {"state":"closed", "sort":"updated", "direction":"desc"}
    result = github.get("/repos/adafruit/" + repo["name"] + "/pulls",
                        params=params)
    if result.ok:
        today_minus_seven = datetime.datetime.today() - datetime.timedelta(days=7)
        prs = result.json()
        for pr in prs:
            merged_at = datetime.datetime.min
            if "merged_at" in pr:
                if pr["merged_at"] is None:
                    continue
                merged_at = datetime.datetime.strptime(pr["merged_at"],
                                                       "%Y-%m-%dT%H:%M:%SZ")
            else:
                continue
            if merged_at < today_minus_seven:
                continue
            contributors.append(pr["user"]["login"])
            merged_pr_count += 1

            # get reviewers (merged_by, and any others)
            single_pr = github.get(pr["url"])
            if not single_pr.ok:
                continue
            pr_info = single_pr.json()
            reviewers.append(pr_info["merged_by"]["login"])
            pr_reviews = github.get(str(pr_info["url"]) + "/reviews")
            if not pr_reviews.ok:
                continue
            for review in pr_reviews.json():
                if review["state"].lower() == "approved":
                    reviewers.append(review["user"]["login"])

    return contributors, reviewers, merged_pr_count


if __name__ == "__main__":
    cmd_line_args = cmd_line_parser.parse_args()

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %T',
                        level=getattr(logging, cmd_line_args.loglevel))

    logging.info("Running circuitpython.org/libraries updater...")

    run_time = datetime.datetime.now()

    working_directory = os.path.abspath(os.getcwd())

    logging.info("Run Date: %s", run_time.strftime("%d %B %Y, %I:%M%p"))

    output_filename = ""
    local_file_output = False
    if cmd_line_args.output_file:
        output_filename = os.path.abspath(cmd_line_args.output_file)
        local_file_output = True
        logging.info(" - Output will be saved to: %s", output_filename)

    if cmd_line_args.cache_http:
        cpy_vals.github.setup_cache(cmd_line_args.cache_ttl)

    repos = common_funcs.list_repos(include_repos=("CircuitPython_Community_Bundle",
                                                   'cookiecutter-adafruit-circuitpython',))

    new_libs = {}
    updated_libs = {}
    open_issues_by_repo = {}
    open_prs_by_repo = {}
    contributors = []
    reviewers = []
    merged_pr_count_total = 0
    repos_by_error = {}

    default_validators = [
        vals[1] for vals in inspect.getmembers(cpy_vals.library_validator)
        if vals[0].startswith("validate")
    ]
    bundle_submodules = common_funcs.get_bundle_submodules()

    latest_pylint = ""
    pylint_info = pypi.get("/pypi/pylint/json")
    if pylint_info and pylint_info.ok:
        latest_pylint = pylint_info.json()["info"]["version"]

    validator = cpy_vals.library_validator(
        default_validators,
        bundle_submodules,
        latest_pylint,
        keep_repos=cmd_line_args.keep_repos
    )

    for repo in repos:
        if (repo["name"] in cpy_vals.BUNDLE_IGNORE_LIST
            or repo["name"] == "circuitpython"):
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
            contributors.extend(get_contribs)
        if get_revs:
            reviewers.extend(get_revs)
        merged_pr_count_total += get_merge_count

        if repo_name in DO_NOT_VALIDATE:
            continue

        # run repo validators to check for infrastructure errors
        errors = []
        try:
            errors = validator.run_repo_validation(repo)
        except Exception as e:
            logging.exception("Unhandled exception %s", str(e))
            errors.extend([cpy_vals.ERROR_OUTPUT_HANDLER])
        for error in errors:
            if not isinstance(error, tuple):
                # check for an error occurring in the validator module
                if error == cpy_vals.ERROR_OUTPUT_HANDLER:
                    #print(errors, "repo output handler error:", validator.output_file_data)
                    logging.error(", ".join(validator.output_file_data))
                    validator.output_file_data.clear()
                if error not in repos_by_error:
                    repos_by_error[error] = []
                repos_by_error[error].append(repo["html_url"])
            else:
                if error[0] not in repos_by_error:
                    repos_by_error[error[0]] = []
                repos_by_error[error[0]].append(
                    "{0} ({1} days)".format(repo["html_url"], error[1])
                )

    # sort all of the items alphabetically
    sorted_new_list = {}
    for new in sorted(new_libs, key=str.lower):
        sorted_new_list[new] = new_libs[new]

    sorted_updated_list = {}
    for updated in sorted(updated_libs, key=str.lower):
        sorted_updated_list[updated] = updated_libs[updated]

    sorted_issues_list = {}
    for issue in sorted(open_issues_by_repo, key=str.lower):
        sorted_issues_list[issue] = open_issues_by_repo[issue]

    sorted_prs_list = {}
    for pr in sorted(open_prs_by_repo, key=str.lower):
        sorted_prs_list[pr] = open_prs_by_repo[pr]

    sorted_repos_by_error = {}
    for error in sorted(repos_by_error, key=str.lower):
        sorted_repos_by_error[error] = repos_by_error[error]

    # assemble the JSON data
    build_json = {
        "updated_at": run_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "contributors": [contrib for contrib in set(contributors)],
        "reviewers": [rev for rev in set(reviewers)],
        "merged_pr_count": str(merged_pr_count_total),
        "library_updates": {"new": sorted_new_list, "updated": sorted_updated_list},
        "open_issues": sorted_issues_list,
        "pull_requests": sorted_prs_list,
        "repo_infrastructure_errors": sorted_repos_by_error,
    }
    json_obj = json.dumps(build_json, indent=2)

    if local_file_output:
        with open(output_filename, "w") as json_file:
            json.dump(build_json, json_file, indent=2)
    print(json_obj)
