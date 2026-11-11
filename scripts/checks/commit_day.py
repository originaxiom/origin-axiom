#!/usr/bin/env python3
"""The day a gate judges by: the commit's own.

A gate is a function of the commit (the closure programme's WP-0.7; the advisor seat's planted case PV15).  The four debt
checkers aged their rows against the wall clock, so one commit passed on its own day and failed sixty days later with
nothing in it changed; and the variable that moves the date for a test moved it for the gate as well.

This is the one place the day is decided, in this order:

  1. `--today YYYY-MM-DD` on the command line.  Each gate passes the date of HEAD's commit this way, so nothing in the
     environment can move a gate's day.
  2. the seam `OA_<NAME>_TODAY`, for a test and for a look ahead by hand ("what goes stale next week").  It is read only
     when the checker is run without `--today`, which a gate never does.
  3. the date of HEAD's commit, read from git.

Never the wall clock.  Where no day is given and there is no commit to read, the checker refuses; and a day that is not a
day (`--today tomorrow`) is refused in plain words, not answered with a traceback.
"""
import datetime
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def of_head(root=ROOT):
    """the committer date of HEAD, as the commit states it; None where there is no commit to read"""
    try:
        r = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs", "HEAD"], capture_output=True, text=True, timeout=30)
    except Exception:
        return None
    try:
        return datetime.date.fromisoformat(r.stdout.strip()) if r.returncode == 0 else None
    except ValueError:
        return None


def _day(text, where):
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        raise SystemExit("refused: %s is %r, which is not a day. Write it YYYY-MM-DD" % (where, text))


def today(env_name, argv=None, root=ROOT):
    """the day a debt is aged against (see the module's note for the order)"""
    argv = sys.argv[1:] if argv is None else list(argv)
    for i, a in enumerate(argv):
        if a == "--today" and i + 1 < len(argv):
            return _day(argv[i + 1], "--today")
        if a.startswith("--today="):
            return _day(a.split("=", 1)[1], "--today")
    env = os.environ.get(env_name)
    if env:
        return _day(env, env_name)
    day = of_head(root)
    if day is None:
        raise SystemExit("refused: no day was given and there is no commit to take one from (this is not a git repository). "
                         "Pass --today YYYY-MM-DD")
    return day


if __name__ == "__main__":
    print(today("OA_TODAY"))
