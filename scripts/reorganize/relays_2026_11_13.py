"""The second physical move under GOVERNANCE section 12 (docs/REORGANIZATIONS.md): the notes and hand-overs between
sessions under docs/handoffs/ leave the tree, 2026-11-13, at the owner's word that how sessions talked to each other need
not stay in the tree and that git's history keeps it. The last commit to hold them is LAST.

Kept: main's four hand-over folders of 2026-11-12, which the building session is still turning into arcs (each leaves the
tree when its arcs have landed); and one data file, run_main_bench.json, which B1487's floor check reads at its path and
which B1487's seal covers (the script cannot be edited, so the file stays where it reads it).
The relay ledger and the move log say where every removed file stands in history; the path check accepts a citation of a
removed path only when git has the file at LAST.

    python3 scripts/reorganize/relays_2026_11_13.py          # make the move, once
    python3 scripts/reorganize/relays_2026_11_13.py --check  # say whether the tree is as the move leaves it"""
import subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LAST = "9c8a50887de1288e2c6667a80c0f480f358f88bb"
KEEP = ("docs/handoffs/MAIN_TO_BUILDER_2026-11-12/", "docs/handoffs/MAIN_TO_BUILDER_2026-11-12_B/",
        "docs/handoffs/MAIN_TO_BUILDER_2026-11-12_C/", "docs/handoffs/MAIN_TO_BUILDER_2026-11-12_D/",
        "docs/handoffs/cc_2026-10-06_sm_b1541_reproduction/run_main_bench.json")
MOVES = []

def git(*a, out=False):
    r = subprocess.run(["git", "-C", str(ROOT), *a], check=True, capture_output=True, text=True)
    return r.stdout

def tracked_under(prefix, rev=None):
    args = ["ls-tree", "-r", "--name-only", rev, "--", prefix] if rev else ["ls-files", "--", prefix]
    return [p for p in git(*args).split("\n") if p]

def to_remove():
    return [p for p in tracked_under("docs/handoffs/", LAST) if not p.startswith(KEEP) and p not in dict(MOVES)]

def check():
    now = tracked_under("docs/handoffs/")
    bad = [p for p in now if not p.startswith(KEEP)]
    bad += [old for old, new in MOVES if (ROOT / old).exists() or not (ROOT / new).exists()]
    return bad

if __name__ == "__main__":
    if "--check" in sys.argv:
        bad = check(); print("as moved" if not bad else "not as moved: %d paths, e.g. %s" % (len(bad), bad[:3])); sys.exit(1 if bad else 0)
    for old, new in MOVES:
        if (ROOT / old).exists(): git("mv", old, new)
    rm = [p for p in to_remove() if (ROOT / p).exists()]
    for i in range(0, len(rm), 200):
        git("rm", "-q", "--", *rm[i:i + 200])
    bad = check(); print("removed %d files; moved %d; %s" % (len(rm), len(MOVES), "as moved" if not bad else "INCOMPLETE: %s" % bad[:3]))
    sys.exit(1 if bad else 0)
