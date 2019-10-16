#!/usr/bin/env python
"""
Wrapper for cppcheck that only passes through errors in lines that were added in
the passed diff FROM..TO .
"""
from __future__ import print_function

import argparse
import subprocess


def main():
    """Main cli entrance point"""

    parser = argparse.ArgumentParser(
        description="cppcheck a git diff",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--from-commit", default="HEAD", help="Diff base commit")
    parser.add_argument("--to-commit", default="", help="Diff destination commit")
    parser.add_argument(
        "--no-common-ancestor",
        action="store_true",
        help=(
            "Don't use the ... form when invoking git diff "
            "(i.e. don't search for common ancestor when diffing)"
        ),
    )
    parser.add_argument(
        "--file-types",
        default=",".join(("c", "cpp", "h", "hpp")),
        help="Comma-delimited list of file extensions to filter when diffing",
    )
    parser.add_argument(
        "--extra-args",
        default="--diff-filter=d --no-ext-diff",
        help="Extra args to pass to git diff. Default set keeps things somewhat sane",
    )
    parser.add_argument(
        "--print-cmd", action="store_true", help="Print the command before running it"
    )

    args = parser.parse_args()

    # pass into git diff + diff-added-lines.
    diff_range_specifier = ".." if args.no_common_ancestor else "..."
    file_types = args.file_types.split(",")
    cmd = (
        "git diff {extra_args} --unified=0 "
        "{diff_range} -- {files} | bash diff-added-lines.sh"
    ).format(
        extra_args=args.extra_args,
        diff_range="{start}{range_spec}{end}".format(
            start=args.from_commit, range_spec=diff_range_specifier, end=args.to_commit
        )
        if args.to_commit
        else args.from_commit,
        files=" ".join(["'*.{}'".format(c) for c in file_types]),
    )
    if args.print_cmd:
        print(cmd)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    main()
