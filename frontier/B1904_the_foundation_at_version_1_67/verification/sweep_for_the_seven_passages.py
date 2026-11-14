#!/usr/bin/env python3
"""B1904 -- where the seven passages still stand as they were, in every tracked text file.

Main's pairs are read from main's own file in the arc B1898.  For each passage, the tracked files that hold it in its old
form are counted by kind.  Nothing of a passage is printed: its number, and the counts.

    python3 sweep_for_the_seven_passages.py        # prints the table kept in sweep_for_the_seven_passages_out.txt
"""
import collections
import importlib.util
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
KEPT_COPY = re.compile(r"^frontier/[^/]+/received/GENESIS_v1_\d+[^/]*\.md$")          # a version of the foundation as it was received, kept in its arc


def kind(rel):
    if KEPT_COPY.match(rel):
        return "a kept copy of an older version of the foundation"
    if rel.endswith("checks/genesis_v1_67.py"):
        return "main's script, which holds the pairs"
    return "ANOTHER FILE: " + rel


def sweep():
    spec = importlib.util.spec_from_file_location("write_version_1_67_for_the_sweep", HERE / "write_version_1_67.py")
    w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
    edits = w.mains().EDITS
    names = [f for f in subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True).stdout.split("\n") if f]
    found = [collections.Counter() for _ in edits]
    read = 0
    for rel in names:
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        read += 1
        flat = " ".join(text.split())
        for n, (old, _new) in enumerate(edits):
            if old in text or " ".join(old.split()) in flat:
                found[n][kind(rel)] += 1
    return read, found


if __name__ == "__main__":
    read, found = sweep()
    print("tracked files read as text: %d" % read)
    for n, c in enumerate(found, 1):
        print("passage %d, as it was: %s" % (n, "; ".join("%d x %s" % (k, what) for what, k in sorted(c.items())) or "nowhere"))
    others = sorted({what for c in found for what in c if what.startswith("ANOTHER FILE")})
    print("files of another kind that hold a passage as it was: %d" % len(others))
