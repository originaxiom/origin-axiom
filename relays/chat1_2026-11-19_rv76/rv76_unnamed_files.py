#!/usr/bin/env python3
"""Status section 34 (main's M76): this seat's markdown files on its branch that are outside B1957's register and outside
the lane's exclusions, and whether any row of main's harvest or relay ledger names them. Data-free. Post hoc and not
sealed: computed once.

    python3 -I -u rv76_unnamed_files.py <a checkout of main at 48055978c> <the mask script> <this seat's repository> <head>

- The files: every relays/**/*.md at <head> of this seat's branch, less those in B1957's UNITS.json for the web lane,
  less those matching the web lane's EXCLUDE_PATTERNS (read from main's extract.py as text, not run).
- The ledgers: docs/HARVEST_LEDGER.md and docs/RELAY_LEDGER.md, each read only through the mask.
- A file is "named" if its basename without .md appears in a ledger, and "in a named folder" if its folder (the path
  part under relays/) does. Both sides are normalised as the mask does on hot lines (every number to '#'), case ignored.
- For each file not named it prints its path, whether its folder is named, the date of its first commit on the branch,
  and whether it changed after the window's base b1727da04. It prints no text of main's.
"""
import fnmatch
import json
import os
import re
import subprocess
import sys

MAIN, MASK, SEAT, HEAD = sys.argv[1:5]
NUM = re.compile(r"[+\-−±%≈~<>]*\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")


def norm(s):
    return re.sub(r"#+", "#", NUM.sub("#", s)).lower()


def git(*a, cwd=SEAT):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True).stdout


units = json.load(open(os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification/UNITS.json")))
registered = {f["file"] for f in units["files"] if f["lane"] == "web"}
src = open(os.path.join(MAIN, "frontier/B1957_the_seats_claims_register/verification/extract.py")).read()
m = re.search(r'"web": \(("relays/[^)]*)\)', src[src.index("EXCLUDE_PATTERNS"):])
patterns = re.findall(r'"([^"]+)"', m.group(1))
ledgers = ""
for led in ("docs/HARVEST_LEDGER.md", "docs/RELAY_LEDGER.md"):
    out = subprocess.run([sys.executable, "-I", MASK, led], cwd=MAIN, capture_output=True, text=True).stdout
    ledgers += norm(" ".join(line[7:] for line in out.splitlines())) + " "
files = [p for p in git("ls-tree", "-r", "--name-only", HEAD, "relays").split("\n") if p.endswith(".md")]
changed = set(git("diff", "--name-only", "b1727da04", HEAD, "--", "relays").split())
rest = [p for p in files if p not in registered and not any(fnmatch.fnmatch(p, q) for q in patterns)]
n_named = n_folder = 0
print("files on the branch: %d; registered: %d; excluded: %d; the rest: %d"
      % (len(files), sum(p in registered for p in files),
         sum(any(fnmatch.fnmatch(p, q) for q in patterns) for p in files), len(rest)))
for p in sorted(rest):
    base = norm(os.path.basename(p)[:-3])
    folder = os.path.dirname(p)[len("relays/"):]
    if base in ledgers:
        n_named += 1
        continue
    in_folder = bool(folder) and norm(folder) in ledgers
    n_folder += in_folder
    first = git("log", "--diff-filter=A", "--format=%ad", "--date=short", HEAD, "--", p).split()
    print("%s | folder named: %s | first commit: %s | changed in the window: %s"
          % (p, "yes" if in_folder else ("no" if folder else "-"), first[-1] if first else "?",
             "yes" if p in changed else "no"))
print("named by a ledger row: %d; not named: %d, of them in a named folder: %d"
      % (n_named, len(rest) - n_named, n_folder))
