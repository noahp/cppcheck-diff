import collections
import re


def diff_lines_to_file_lines(diff_lines):
    """
    Pass an iterator of the diff lines, eg:

    diff --git "a/file" "b/file"
    new file mode 100644
    index 0000000..bd88e01
    --- /dev/null
    +++ "b/file"
    @@ -0,0 +1 @@
    +yolo

    Returns a dictionary of {"file name": [line numbers]}.
    """
    out = collections.defaultdict(list)
    for line in diff_lines:
        # TODO parser :( FSM I guess lol
        print(line.decode(), end="")
    return out
    if args.to:
        diff_range = "{start}{range_spec}{end}".format(
            start=args.from_commit, range_spec=diff_range_specifier, end=args.to
        )
    else:
        diff_range = args.from_commit
        "git --no-pager diff {extra_args} --unified=0 " "{diff_range} -- {files}"
        diff_range=diff_range,
    cmd_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    diff_lines = diff_lines_to_file_lines(cmd_process.stdout)