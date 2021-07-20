import json
import requests
import os
import sys
import argparse
import shutil
import sh
from sh.contrib import git
from adabot.lib import common_funcs


working_directory = os.path.abspath(os.getcwd())
lib_directory = working_directory + "/.libraries/"
patch_directory = working_directory + "/patches/"
repos = []
check_errors = []
apply_errors = []
stats = []

"""
Setup the command line argument parsing object.
"""
cli_parser = argparse.ArgumentParser(description="Apply patches to any common file(s) in"
                                     " all Adafruit CircuitPython Libraries.")
cli_parser.add_argument("-l", "--list", help="Lists the available patches to run.",
                        action='store_true')
cli_parser.add_argument("-p", help="Runs only the single patch referenced.",
                        metavar="<PATCH FILENAME>", dest="patch")
cli_parser.add_argument("-f", help="Adds the referenced FLAGS to the git.am call."
                        " Only available when using '-p'. Enclose flags in brackets '[]'."
                        " Multiple flags can be passed. NOTE: '--signoff' is already used "
                        " used by default, and will be ignored. EXAMPLE: -f [-C0] -f [-s]",
                        metavar="FLAGS", action="append", dest="flags", type=str)
cli_parser.add_argument("--use-apply", help="Forces use of 'git apply' instead of 'git am'."
                        " This is necessary when needing to use 'apply' flags not available"
                        " to 'am' (e.g. '--unidiff-zero'). Only available when using '-p'.",
                        action="store_true", dest="use_apply")
cli_parser.add_argument("--dry-run", help="Accomplishes a dry run of patches, without applying"
                        " them.", action="store_true", dest="dry_run")
cli_parser.add_argument("--local", help="Force use of local patches. This skips verification"
                        " of patch files in the adabot GitHub repository. MUST use '--dry-run'"
                        " with this argument; this guards against applying unapproved patches.",
                        action="store_true", dest="run_local")

def get_repo_list():
    """ Uses adabot.circuitpython_libraries module to get a list of
        CircuitPython repositories. Filters the list down to adafruit
        owned/sponsored CircuitPython libraries.
    """
    repo_list = []
    get_repos = common_funcs.list_repos()
    for repo in get_repos:
        if not (repo["owner"]["login"] == "adafruit" and
                repo["name"].startswith("Adafruit_CircuitPython")):
            continue
        repo_list.append(dict(name=repo["name"], url=repo["clone_url"]))

    return repo_list

def get_patches(run_local):
    """ Returns the list of patch files located in the adabot/patches
        directory.
    """
    return_list = []
    if not run_local:
        contents = requests.get("https://api.github.com/repos/adafruit/adabot/contents/patches")
        if contents.ok:
            for patch in contents.json():
                patch_name = patch["name"]
                return_list.append(patch_name)
    else:
        contents = os.listdir(patch_directory)
        for file in contents:
            if file.endswith(".patch"):
                return_list.append(file)

    return return_list

def apply_patch(repo_directory, patch_filepath, repo, patch, flags, use_apply):
    """ Apply the `patch` in `patch_filepath` to the `repo` in
        `repo_directory` using git am or git apply. The commit
        with the user running the script (adabot if credentials are set
        for that).

        When `use_apply` is true, the `--apply` flag is automatically added
        to ensure that any passed flags that turn off apply (e.g. `--check`)
        are overridden.
    """
    if not os.getcwd() == repo_directory:
        os.chdir(repo_directory)

    if not use_apply:
        try:
            git.am(flags, patch_filepath)
        except sh.ErrorReturnCode as Err:
            apply_errors.append(dict(repo_name=repo,
                                     patch_name=patch, error=Err.stderr))
            return False
    else:
        apply_flags = ["--apply"]
        for flag in flags:
            if not flag == "--signoff":
                apply_flags.append(flag)
        try:
            git.apply(apply_flags, patch_filepath)
        except sh.ErrorReturnCode as Err:
            apply_errors.append(dict(repo_name=repo,
                                     patch_name=patch, error=Err.stderr))
            return False

        with open(patch_filepath) as f:
            for line in f:
                if "[PATCH]" in line:
                    message = '"' +  line[(line.find("]") + 2):] + '"'
                    break
        try:
            git.commit("-a", "-m", message)
        except sh.ErrorReturnCode as Err:
            apply_errors.append(dict(repo_name=repo,
                                     patch_name=patch, error=Err.stderr))
            return False

    try:
        git.push()
    except sh.ErrorReturnCode as Err:
        apply_errors.append(dict(repo_name=repo,
                                 patch_name=patch, error=Err.stderr))
        return False
    return True

def check_patches(repo, patches, flags, use_apply, dry_run):
    """ Gather a list of patches from the `adabot/patches` directory
        on the adabot repo. Clone the `repo` and run git apply --check
        to test wether it requires any of the gathered patches.

        When `use_apply` is true, any flags except `--apply` are passed
        through to the check call. This ensures that the check call is
        representative of the actual apply call.
    """
    applied = 0
    skipped = 0
    failed = 0

    repo_directory = lib_directory + repo["name"]

    for patch in patches:
        try:
            os.chdir(lib_directory)
        except FileNotFoundError:
            os.mkdir(lib_directory)
            os.chdir(lib_directory)

        try:
            git.clone(repo["url"])
        except sh.ErrorReturnCode_128 as Err:
            if b"already exists" in Err.stderr:
                pass
            else:
                raise RuntimeError(Err.stderr)
        os.chdir(repo_directory)

        patch_filepath = patch_directory + patch

        try:
            check_flags = ["--check"]
            if use_apply:
                for flag in flags:
                    if not flag in ("--apply", "--signoff"):
                        check_flags.append(flag)
            git.apply(check_flags, patch_filepath)
            run_apply = True
        except sh.ErrorReturnCode_1 as Err:
            run_apply = False
            if (b"error" not in Err.stderr or
                b"patch does not apply" in Err.stderr):
                    parse_err = Err.stderr.decode()
                    parse_err = parse_err[parse_err.rfind(":")+1:-1]
                    print(
                        "   . Skipping {}:{}".format(repo["name"], parse_err)
                    )
                    skipped += 1
            else:
                failed += 1
                error_str = str(Err.stderr, encoding="utf-8").replace("\n", " ")
                error_start = error_str.rfind("error:") + 7
                check_errors.append(dict(repo_name=repo["name"],
                                         patch_name=patch, error=error_str[error_start:]))

        except sh.ErrorReturnCode as Err:
            run_apply = False
            failed += 1
            error_str = str(Err.stderr, encoding="utf-8").replace("\n", " ")
            error_start = error_str.rfind("error:") + 7
            check_errors.append(dict(repo_name=repo["name"],
                                     patch_name=patch, error=error_str[error_start:]))

        if run_apply and not dry_run:
            result = apply_patch(repo_directory, patch_filepath, repo["name"],
                                 patch, flags, use_apply)
            if result:
                applied += 1
            else:
                failed += 1
        elif run_apply and dry_run:
            applied += 1

    return [applied, skipped, failed]

if __name__ == "__main__":
    cli_args = cli_parser.parse_args()
    use_apply = cli_args.use_apply
    dry_run = cli_args.dry_run
    run_local = cli_args.run_local
    if run_local:
        if dry_run or cli_args.list:
            pass
        else:
            raise RuntimeError("'--local' can only be used in conjunction with"
                               " '--dry-run' or '--list'.")

    run_patches = get_patches(run_local)
    flags = ["--signoff"]

    if cli_args.list:
        print("Available Patches:", run_patches)
        sys.exit()
    if cli_args.patch:
        if not cli_args.patch in run_patches:
            raise ValueError("'{}' is not an available patchfile.".format(cli_args.patch))
        run_patches = [cli_args.patch]
    if not cli_args.flags == None:
        if not cli_args.patch:
            raise RuntimeError("Must be used with a single patch. See help (-h) for usage.")
        if "[-i]" in cli_args.flags:
            raise ValueError("Interactive Mode flag not allowed.")
        for flag in cli_args.flags:
            if not flag == "[--signoff]":
                flags.append(flag.strip("[]"))
    if cli_args.use_apply:
        if not cli_args.patch:
            raise RuntimeError("Must be used with a single patch. See help (-h) for usage.")

    print(".... Beginning Patch Updates ....")
    print(".... Working directory:", working_directory)
    print(".... Library directory:", lib_directory)
    print(".... Patches directory:", patch_directory)

    check_errors = []
    apply_errors = []
    stats = [0, 0, 0]

    print(".... Deleting any previously cloned libraries")
    try:
        libs = os.listdir(path=lib_directory)
        for lib in libs:
            shutil.rmtree(lib_directory + lib)
    except FileNotFoundError:
        pass

    repos = get_repo_list()
    print(".... Running Patch Checks On", len(repos), "Repos ....")

    for repo in repos:
        results = check_patches(repo, run_patches, flags, use_apply, dry_run)
        for k in range(3):
           stats[k] += results[k]

    print(".... Patch Updates Completed ....")
    print(".... Patches Applied:", stats[0])
    print(".... Patches Skipped:", stats[1])
    print(".... Patches Failed:", stats[2], "\n")
    print(".... Patch Check Failure Report ....")
    if len(check_errors) > 0:
        for error in check_errors:
            print(">> Repo: {0}\tPatch: {1}\n   Error: {2}".format(error["repo_name"],
                  error["patch_name"], error["error"]))
    else:
        print("No Failures")
    print("\n")
    print(".... Patch Apply Failure Report ....")
    if len(apply_errors) > 0:
        for error in apply_errors:
            print(">> Repo: {0}\tPatch: {1}\n   Error: {2}".format(error["repo_name"],
                  error["patch_name"], error["error"]))
    else:
        print("No Failures")
