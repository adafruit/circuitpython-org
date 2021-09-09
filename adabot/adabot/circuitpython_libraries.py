# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#               2019 Michael Schroeder
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

"""Adabot utility for CircuitPython Libraries."""

import argparse
import datetime
import inspect
import logging
import re
import sys
import traceback

from adabot import github_requests as github
from adabot import pypi_requests as pypi
from adabot.lib import circuitpython_library_validators as cirpy_lib_vals
from adabot.lib import common_funcs
from adabot.lib import assign_hacktober_label as hacktober
from adabot.lib import blinka_funcs
from adabot import circuitpython_library_download_stats as dl_stats

logger = logging.getLogger(__name__)
ch = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[ch])

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Adabot utility for CircuitPython Libraries.",
    prog="Adabot CircuitPython Libraries Utility",
)
cmd_line_parser.add_argument(
    "-o",
    "--output_file",
    help="Output log to the filename provided.",
    metavar="<OUTPUT FILENAME>",
    dest="output_file",
)
cmd_line_parser.add_argument(
    "-p",
    "--print",
    help="Set the level of verbosity printed to the command prompt."
    " Zero is off; One is on (default).",
    type=int,
    default=1,
    dest="verbose",
    choices=[0, 1],
)
cmd_line_parser.add_argument(
    "-e",
    "--error_depth",
    help="Set the threshold for outputting an error list. Default is 5.",
    dest="error_depth",
    type=int,
    default=5,
    metavar="n",
)
cmd_line_parser.add_argument(
    "-v",
    "--validator",
    help="Run validators with 'all', or only the validator(s) supplied in a string.",
    dest="validator",
    metavar='all OR "validator1, validator2, ..."',
)

# Functions to run on repositories to validate their state.  By convention these
# return a list of string errors for the specified repository (a dictionary
# of Github API repository object state).
default_validators = [
    vals
    for vals in inspect.getmembers(cirpy_lib_vals.LibraryValidator)
    if vals[0].startswith("validate")
]

pr_sort_re = re.compile(r"(?<=\(Open\s)(.+)(?=\sdays)")
close_pr_sort_re = re.compile(r"(?<=\(Days\sopen:\s)(.+)(?=\))")

blinka_repos = [
    "Adafruit_Blinka",
    "Adafruit_Blinka_bleio",
    "Adafruit_Blinka_Displayio",
    "Adafruit_Python_PlatformDetect",
    "Adafruit_Python_PureIO",
    "Adafruit_Blinka_PyPortal",
    "Adafruit_Python_Extended_Bus",
]

# pylint: disable=too-many-locals, too-many-branches, too-many-statements
def run_library_checks(validators, kw_args, error_depth):
    """runs the various library checking functions"""

    # Load the latest pylint version
    latest_pylint = "2.0.1"
    pylint_info = pypi.get("/pypi/pylint/json")
    if pylint_info and pylint_info.ok:
        latest_pylint = pylint_info.json()["info"]["version"]
    logger.info("Latest pylint is: %s", latest_pylint)

    repos = common_funcs.list_repos(
        include_repos=tuple(blinka_repos)
        + ("CircuitPython_Community_Bundle", "cookiecutter-adafruit-circuitpython")
    )

    logger.info("Found %s repos to check.", len(repos))
    bundle_submodules = common_funcs.get_bundle_submodules()
    logger.info("Found %s submodules in the bundle.", len(bundle_submodules))
    github_user = common_funcs.whois_github_user()
    logger.info("Running GitHub checks as %s", github_user)
    need_work = 0

    lib_insights = common_funcs.InsightData()
    blinka_insights = common_funcs.InsightData()
    core_insights = common_funcs.InsightData()
    core_insights["milestones"] = dict()

    repo_needs_work = []
    since = datetime.datetime.now() - datetime.timedelta(days=7)
    repos_by_error = {}
    new_libs = {}
    updated_libs = {}

    validator = cirpy_lib_vals.LibraryValidator(
        validators, bundle_submodules, latest_pylint, **kw_args
    )
    for repo in repos:
        if len(validators) != 0:
            errors = validator.run_repo_validation(repo)
            if errors:
                need_work += 1
                repo_needs_work.append(repo)
                # print(repo["full_name"])
                # print("\n".join(errors))
                # print()
            for error in errors:
                if not isinstance(error, tuple):
                    # check for an error occurring in the valiator module
                    if error == cirpy_lib_vals.ERROR_OUTPUT_HANDLER:
                        # print(errors, "repo output handler error:", validator.output_file_data)
                        logger.info(", ".join(validator.output_file_data))
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
        insights = lib_insights
        if repo["owner"]["login"] == "adafruit":
            if repo["name"] in blinka_repos:
                insights = blinka_insights
            elif repo["name"] == "circuitpython":
                insights = core_insights
        closed_metric = bool(insights == lib_insights)
        errors = validator.gather_insights(
            repo, insights, since, show_closed_metric=closed_metric
        )
        if errors:
            print("insights error")
            for error in errors:
                if error == cirpy_lib_vals.ERROR_OUTPUT_HANDLER:
                    logger.info(", ".join(validator.output_file_data))
                    validator.output_file_data.clear()

        # get a list of new & updated libraries for the last week
        if repo["name"] != "Adafruit_CircuitPython_Bundle":
            check_releases = common_funcs.is_new_or_updated(repo)
            if check_releases == "new":
                new_libs[repo["name"]] = repo["html_url"]
            elif check_releases == "updated":
                updated_libs[repo["name"]] = repo["html_url"]

    logger.info("")
    logger.info("State of CircuitPython + Libraries + Blinka")

    logger.info("### Overall")
    print_pr_overview(lib_insights, core_insights, blinka_insights)
    print_issue_overview(lib_insights, core_insights, blinka_insights)

    logger.info("")
    logger.info("### Core")
    print_pr_overview(core_insights)
    logger.info("* %s open pull requests", len(core_insights["open_prs"]))
    sorted_prs = sorted(
        core_insights["open_prs"],
        key=lambda days: int(pr_sort_re.search(days).group(1)),
        reverse=True,
    )
    for pull_request in sorted_prs:
        logger.info("  * %s", pull_request)
    print_issue_overview(core_insights)
    logger.info("* %s open issues", len(core_insights["open_issues"]))
    logger.info("  * https://github.com/adafruit/circuitpython/issues")
    logger.info("* %s active milestones", len(core_insights["milestones"]))
    ms_count = 0
    for milestone in sorted(core_insights["milestones"].keys()):
        ms_count += core_insights["milestones"][milestone]
        logger.info(
            "  * %s: %s open issues", milestone, core_insights["milestones"][milestone]
        )
    logger.info(
        "  * %s issues not assigned a milestone",
        len(core_insights["open_issues"]) - ms_count,
    )
    logger.info("")

    ## temporarily disabling core download stats:
    #  - GitHub API has been broken, due to the number of release artifacts
    #  - Release asset delivery is being moved to AWS CloudFront/S3
    # print_circuitpython_dl_stats()
    logger.info("* Core download stats available at https://circuitpython.org/stats")

    logger.info("")
    logger.info("### Libraries")
    print_pr_overview(lib_insights)
    logger.info("  * Merged pull requests:")
    sorted_prs = sorted(
        lib_insights["merged_prs"],
        key=lambda days: int(close_pr_sort_re.search(days).group(1)),
        reverse=True,
    )
    for pull_request in sorted_prs:
        logger.info("    * %s", pull_request)
    print_issue_overview(lib_insights)
    logger.info("* https://circuitpython.org/contributing")
    logger.info("  * %s open issues", len(lib_insights["open_issues"]))
    logger.info("  * %s good first issues", lib_insights["good_first_issues"])
    open_pr_days = [
        int(pr_sort_re.search(pull_request).group(1))
        for pull_request in lib_insights["open_prs"]
        if pr_sort_re.search(pull_request) is not None
    ]
    if len(lib_insights["open_prs"]) != 0:
        logger.info(
            "  * %s open pull requests (Oldest: %s, Newest: %s)",
            len(lib_insights["open_prs"]),
            max(open_pr_days),
            max((min(open_pr_days), 1)),  # ensure the minumum is '1'
        )
    logger.info("Library updates in the last seven days:")
    if len(new_libs) != 0:
        logger.info("**New Libraries**")
        for title, link in new_libs.items():
            logger.info(" * [%s](%s)", title, link)
    if len(updated_libs) != 0:
        logger.info("**Updated Libraries**")
        for title, link in updated_libs.items():
            logger.info(" * [%s](%s)", title, link)

    if len(validators) != 0:
        lib_repos = []
        for repo in repos:
            if repo["owner"]["login"] == "adafruit" and repo["name"].startswith(
                "Adafruit_CircuitPython"
            ):
                lib_repos.append(repo)

        logger.info("%s out of %s repos need work.", need_work, len(lib_repos))

        list_repos_for_errors = [cirpy_lib_vals.ERROR_NOT_IN_BUNDLE]
        logger.info("")
        for error in sorted(repos_by_error):
            if not repos_by_error[error]:
                continue
            logger.info("")
            error_count = len(repos_by_error[error])
            logger.info("%s - %s", error, error_count)
            if error_count <= error_depth or error in list_repos_for_errors:
                logger.info(
                    "%s", "\n".join(["  * " + x for x in repos_by_error[error]])
                )

    logger.info("")
    logger.info("### Blinka")
    print_pr_overview(blinka_insights)
    logger.info("* %s open pull requests", len(blinka_insights["open_prs"]))
    sorted_prs = sorted(
        blinka_insights["open_prs"],
        key=lambda days: int(pr_sort_re.search(days).group(1)),
        reverse=True,
    )
    for pull_request in sorted_prs:
        logger.info("  * %s", pull_request)
    print_issue_overview(blinka_insights)
    logger.info("* %s open issues", len(blinka_insights["open_issues"]))
    logger.info("  * https://github.com/adafruit/Adafruit_Blinka/issues")
    blinka_dl = dl_stats.piwheels_stats().get("adafruit-blinka", {}).get("month", "N/A")
    logger.info("* Piwheels Downloads in the last month: %s", blinka_dl)
    logger.info("Number of supported boards: %s", blinka_funcs.board_count())


# pylint: disable=too-many-branches,too-many-statements
def print_circuitpython_dl_stats():
    """Gather and report analytics on the main CircuitPython repository."""

    # TODO: with the move of release assets to AWS CloudFront/S3, update
    #       this to use AWS CloudWatch metrics to gather download stats.
    #       AWS' Python SDK `boto3` has CloudWatch interfaces which should
    #       enable this.

    try:
        response = github.get("/repos/adafruit/circuitpython/releases")
    except (ValueError, RuntimeError):
        logger.info("Core CircuitPython GitHub download statistics request failed.")
        return

    if not response.ok:
        logger.info("Core CircuitPython GitHub download statistics request failed.")
        return
    releases = response.json()

    found_unstable = False
    found_stable = False
    stable_tag = None
    prerelease_tag = None

    by_board = {}
    by_language = {}
    by_both = {}
    total = {}

    asset_re = re.compile(
        r"""
            circuitpython\-   # end of the prefix
            (?P<board>.+)\-   # board name
            (?P<lang>.+)\-    # language
            (\d\.\d\.\d.*)    # version
            \.(?=uf2|bin|hex) # file extension
        """,
        re.I | re.X,
    )

    for release in releases:
        if not found_unstable and not release["draft"] and release["prerelease"]:
            found_unstable = True
            prerelease_tag = release["tag_name"]
        elif not found_stable and not release["draft"] and not release["prerelease"]:
            found_stable = True
            stable_tag = release["tag_name"]
        else:
            continue

        for asset in release["assets"]:
            if not asset["name"].startswith("adafruit-circuitpython"):
                continue
            count = asset["download_count"]
            info_re = asset_re.search(asset["name"])
            if not info_re:
                print("Skipping stats for '{}'".format(asset["name"]))
                continue
            board = info_re.group("board")
            language = info_re.group("lang")
            if language not in by_language:
                by_language[language] = {release["tag_name"]: 0}
            if release["tag_name"] not in by_language[language]:
                by_language[language][release["tag_name"]] = 0
            by_language[language][release["tag_name"]] += count
            if board not in by_board:
                by_board[board] = {release["tag_name"]: 0}
                by_both[board] = {}
            if release["tag_name"] not in by_board[board]:
                by_board[board][release["tag_name"]] = 0
            by_board[board][release["tag_name"]] += count
            by_both[board][language] = count

            if release["tag_name"] not in total:
                total[release["tag_name"]] = 0
            total[release["tag_name"]] += count

    logger.info("Number of supported boards: %s", len(by_board))
    logger.info("")
    logger.info("Download stats by board:")
    logger.info("")
    by_board_list = [
        [
            "Board",
            "{}".format(stable_tag.strip(" ")),
            "{}".format(prerelease_tag.strip(" ")),
        ],
    ]
    for board in sorted(by_board.items()):
        by_board_list.append(
            [
                str(board[0]),
                (str(board[1][stable_tag]) if stable_tag in board[1] else "-"),
                (str(board[1][prerelease_tag]) if prerelease_tag in board[1] else "-"),
            ]
        )

    long_col = [
        (max([len(str(row[i])) for row in by_board_list]) + 3)
        for i in range(len(by_board_list[0]))
    ]
    # row_format = "".join(["{:<" + str(this_col) + "}" for this_col in long_col])
    row_format = "".join(
        [
            "| {:<" + str(long_col[0]) + "}",
            "|{:^" + str(long_col[1]) + "}",
            "|{:^" + str(long_col[2]) + "}|",
        ]
    )

    by_board_list.insert(
        1,
        [
            "{}".format("-" * (long_col[0])),
            "{}".format("-" * (long_col[1])),
            "{}".format("-" * (long_col[2])),
        ],
    )

    by_board_list.extend(
        (
            [
                "{}".format("-" * (long_col[0])),
                "{}".format("-" * (long_col[1])),
                "{}".format("-" * (long_col[2])),
            ],
            [
                "{0}{1}".format(" " * (long_col[0] - 6), "Total"),
                "{}".format(total[stable_tag]),
                "{}".format(total[prerelease_tag]),
            ],
            [
                "{}".format("-" * (long_col[0])),
                "{}".format("-" * (long_col[1])),
                "{}".format("-" * (long_col[2])),
            ],
        )
    )

    for row in by_board_list:
        logger.info("%s", row_format.format(*row))
    logger.info("")

    logger.info("Download stats by language:")
    logger.info("")
    by_lang_list = [
        [
            "Board",
            "{}".format(stable_tag.strip(" ")),
            "{}".format(prerelease_tag.strip(" ")),
        ],
    ]
    for board in sorted(by_language.items()):
        by_lang_list.append(
            [
                str(board[0]),
                (str(board[1][stable_tag]) if stable_tag in board[1] else "-"),
                (str(board[1][prerelease_tag]) if prerelease_tag in board[1] else "-"),
            ]
        )

    long_col = [
        (max([len(str(row[i])) for row in by_lang_list]) + 3)
        for i in range(len(by_lang_list[0]))
    ]
    # row_format = "".join(["{:<" + str(this_col) + "}" for this_col in long_col])
    row_format = "".join(
        [
            "| {:<" + str(long_col[0]) + "}",
            "|{:^" + str(long_col[1]) + "}",
            "|{:^" + str(long_col[2]) + "}|",
        ]
    )

    by_lang_list.insert(
        1,
        [
            "{}".format("-" * (long_col[0])),
            "{}".format("-" * (long_col[1])),
            "{}".format("-" * (long_col[2])),
        ],
    )

    by_lang_list.extend(
        (
            [
                "{}".format("-" * (long_col[0])),
                "{}".format("-" * (long_col[1])),
                "{}".format("-" * (long_col[2])),
            ],
            [
                "{0}{1}".format(" " * (long_col[0] - 6), "Total"),
                "{}".format(total[stable_tag]),
                "{}".format(total[prerelease_tag]),
            ],
            [
                "{}".format("-" * (long_col[0])),
                "{}".format("-" * (long_col[1])),
                "{}".format("-" * (long_col[2])),
            ],
        )
    )

    for row in by_lang_list:
        logger.info("%s", row_format.format(*row))
    # for language in by_language:
    #    logger.info("* %s - %s", language, by_language[language])
    logger.info("")


def print_pr_overview(*insights):
    """Prints an overview of Pull Requests"""
    merged_prs = sum([len(x["merged_prs"]) for x in insights])
    authors = set().union(*[x["pr_merged_authors"] for x in insights])
    reviewers = set().union(*[x["pr_reviewers"] for x in insights])

    logger.info("* %s pull requests merged", merged_prs)
    logger.info("  * %s authors - %s", len(authors), ", ".join(authors))
    logger.info("  * %s reviewers - %s", len(reviewers), ", ".join(reviewers))


def print_issue_overview(*insights):
    """Prints an overview of Issues"""
    closed_issues = sum([x["closed_issues"] for x in insights])
    issue_closers = set().union(*[x["issue_closers"] for x in insights])
    new_issues = sum([x["new_issues"] for x in insights])
    issue_authors = set().union(*[x["issue_authors"] for x in insights])
    logger.info(
        "* %s closed issues by %s people, %s opened by %s people",
        closed_issues,
        len(issue_closers),
        new_issues,
        len(issue_authors),
    )

    # print Hacktoberfest labels changes if its Hacktober
    in_season, season_action = hacktober.is_hacktober_season()
    if in_season:
        hacktober_changes = ""
        if season_action == "add":
            hacktober_changes = "* Assigned Hacktoberfest label to {} issues.".format(
                sum([x["hacktober_assigned"] for x in insights])
            )
        elif season_action == "remove":
            hacktober_changes += "* Removed Hacktoberfest label from {} issues.".format(
                sum([x["hacktober_removed"] for x in insights])
            )
        logger.info(hacktober_changes)


# pylint: disable=too-many-branches
def main(verbose=1, output_file=None, validator=None, error_depth=5):
    """Main"""
    validator_kwarg_list = {}
    startup_message = [
        "Running CircuitPython Library checks...",
        "Report Date: {}".format(datetime.datetime.now().strftime("%d %B %Y, %I:%M%p")),
    ]

    if verbose == 0:
        logger.setLevel("CRITICAL")

    if output_file:
        file_handler = logging.FileHandler(output_file)
        logger.addHandler(file_handler)
        startup_message.append(
            " - Report output will be saved to: {}".format(output_file)
        )

    validators = []
    validator_names = []
    if validator:
        startup_message.append(
            " - Depth for listing libraries with errors: {}".format(error_depth)
        )

        if validator != "all":
            validators = []
            for func in validator.split(","):
                func_name = func.strip()
                try:
                    if not func_name.startswith("validate"):
                        raise KeyError
                        # print('{}'.format(func_name))
                    if "contents" not in func_name:
                        validators.append(
                            [
                                val[1]
                                for val in default_validators
                                if func_name in val[0]
                            ][0]
                        )
                    else:
                        validators.insert(
                            0,
                            [
                                val[1]
                                for val in default_validators
                                if func_name in val[0]
                            ][0],
                        )
                    validator_names.append(func_name)
                except KeyError:
                    # print(default_validators)
                    logger.info(
                        "Error: '%s' is not an available validator.\nAvailable validators are: %s",
                        func.strip(),
                        ", ".join([val[0] for val in default_validators]),
                    )
                    sys.exit()
        else:
            validators = [val_funcs[1] for val_funcs in default_validators]
            validator_names = [val_names[0] for val_names in default_validators]

        startup_message.append(
            " - These validators will run: {}".format(", ".join(validator_names))
        )

        if "validate_contents" not in validator_names:
            validator_kwarg_list["validate_contents_quiet"] = True
            validators.insert(
                0,
                [val[1] for val in default_validators if "validate_contents" in val[0]][
                    0
                ],
            )

    try:
        for message in startup_message:
            logger.info(message)
        logger.info("")
        # print(validators)
        run_library_checks(
            validators,
            validator_kwarg_list,
            error_depth,
        )
    except:
        _, exc_val, exc_tb = sys.exc_info()
        logger.error("Exception Occurred!")
        logger.error(("-" * 60))
        logger.error("Traceback (most recent call last):")
        trace = traceback.format_tb(exc_tb)
        for line in trace:
            logger.error(line)
        logger.error(exc_val)

        raise


if __name__ == "__main__":
    cli_args = cmd_line_parser.parse_args()
    main(
        verbose=cli_args.verbose,
        output_file=cli_args.output_file,
        validator=cli_args.validator,
        error_depth=cli_args.error_depth,
    )
