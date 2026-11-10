#!/usr/bin/env python3
"""B1870 -- re-run the commands that decide each of the audit's findings, read-only, and say whether each prints what it printed
when main re-ran it on 2026-11-10.

The commands were written by eight read-only checkers (one per class of finding) and are stored, as main ran them, in
checkers_reports.json beside this file.  They read; none writes.  Before running, this script refuses any command that
matches its own list of writing verbs.  A changed output is not an error: main moves, counts drift, and a finding that
has been fixed stops reproducing -- which is the point of re-running.

    python3 -B frontier/B1870_the_audits_backlog_reproduced_on_main/verification/rerun.py [ID ...]      (all findings by default)
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WRITES = re.compile(r"(^|[;&|]\s*)(rm|mv|cp|tee|chmod|chown|pip|curl|wget|ssh|scp|kill|sudo|dd|ln|touch|mkdir|sed\s+-i|"
                    r"git\s+(checkout|switch|stash|reset|restore|clean|commit|push|pull|fetch|merge|rebase|tag|worktree|clone|add|rm|mv|apply|am|cherry-pick))\b"
                    r"|>\s*[^&|\s=]|\bopen\([^)]*['\"][wa]")


def screened(cmd):
    """True when the command passes the read-only screen (redirections to /dev/null and of stderr are allowed)"""
    c = re.sub(r"2>/dev/null|2>&1|>/dev/null", "", cmd)
    c = re.sub(r"\"[^\"]*\"|'[^']*'", lambda m: m.group(0).replace(">", " "), c)        # a '>' inside a quoted string compares, it does not write
    return not WRITES.search(c)


def main():
    reports = json.loads((HERE / "checkers_reports.json").read_text(encoding="utf-8"))
    want = set(sys.argv[1:])
    same = changed = 0
    for r in reports:
        if want and r["id"] not in want:
            continue
        print("%s  (the checker's verdict on 2026-11-10: %s)" % (r["id"], r["checker_verdict"]))
        for cmd, was in zip(r["commands"], r["main_rerun"]):
            if not screened(cmd):
                print("   REFUSED (not read-only): %s" % cmd[:100])
                continue
            try:
                p = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, timeout=150, cwd=str(ROOT))
                out = (p.stdout + (("\n[stderr] " + p.stderr) if p.stderr.strip() and not p.stdout.strip() else "")).strip()[:3000]
            except subprocess.TimeoutExpired:
                out = ""
            now = hashlib.sha256(out.encode("utf-8")).hexdigest()[:16]
            if now == was["sha256_of_output"]:
                same += 1
            else:
                changed += 1
            print("   %s  %s" % ("same   " if now == was["sha256_of_output"] else "CHANGED", re.sub(r"\s+", " ", cmd)[:110]))
    print("%d commands print what they printed on 2026-11-10; %d print something else" % (same, changed))


if __name__ == "__main__":
    main()
