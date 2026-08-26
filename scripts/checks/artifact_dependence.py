#!/usr/bin/env python3
"""artifact_dependence.py -- find locks that depend on artifacts the repo can never carry.

THE CLASS (B8141, third in the series after B8139's "cost" and B8140's "two empties"):
a test that reads a file matched by .gitignore can only pass on a machine where that file
happens to exist. On a clean checkout it does not skip -- it FAILS. Permanent red trains a
reader to ignore failures, which costs more than the lock was ever worth.

This is distinct from the cost class. A cost-class lock works but is never reached. An
artifact-class lock is reached, and reports on the machine rather than on the code.

INSTRUMENT NOTE -- READ BEFORE TRUSTING THIS SCRIPT. Its first version matched only whole
repo-relative paths written as a single string literal, and therefore MISSED the very files
that motivated it: tests build those paths from fragments (ROOT / "frontier" / name). It
reported "0 gitignored" while two such tests were failing three metres away. The fix is to
match BASENAMES and index every file actually present. The POSITIVE CONTROL below encodes
that history: the scan must still detect two files independently confirmed absent, and this
script exits non-zero if it cannot. A scan that cannot see a known-missing file is not
evidence of absence.

Usage:  python3 scripts/checks/artifact_dependence.py
Exit 0 if no artifact-dependent test is found, 1 otherwise (or if the control fails).
"""
import collections
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
os.chdir(ROOT)

# Two files independently confirmed absent by direct pytest runs. If the scan cannot see
# these, its silence means nothing -- see the instrument note above.
CONTROL = ["b1062_v2_block1.log", "refresh_windows.log"]
# Manifests are a SECOND route into this class, and the first version of this script was
# blind to it: a test may read a manifest file that LISTS gitignored artifacts, so the
# paths never appear as string literals in any test source. Found by the suite sweep that
# this very script prompted -- test_b646_wave2 fails on exactly that.
MANIFEST_CONTROL = "ORIGINALS_MANIFEST.txt"

_LIT = re.compile(r'["\']([A-Za-z0-9_.\-]+\.(?:log|json|txt|md|csv|tsv|dat|out|npy|pkl))["\']')


def _present():
    idx = collections.defaultdict(list)
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git/" not in str(p):
            idx[p.name].append(str(p.relative_to(ROOT)))
    return idx


def _would_be_ignored(basenames):
    """Would a file of this name be gitignored if it were created inside an arc dir?"""
    if not basenames:
        return set()
    probes = [str(pathlib.Path("frontier") / "PROBE" / b) for b in basenames]
    r = subprocess.run(["git", "check-ignore"] + probes, capture_output=True, text=True)
    return {pathlib.Path(ln.strip()).name for ln in r.stdout.splitlines() if ln.strip()}


def main():
    present = _present()
    refs = collections.defaultdict(set)
    for t in sorted(ROOT.glob("tests/test_*.py")):
        for m in _LIT.finditer(t.read_text(errors="ignore")):
            refs[m.group(1)].add(t.name)

    missing = {b: v for b, v in refs.items() if b not in present}

    seen = [c for c in CONTROL if c in missing]
    if len(seen) != len(CONTROL):
        print("CONTROL FAILED: scan cannot see known-absent files %r -- found %r."
              % (CONTROL, seen))
        print("A scan that cannot detect a file known to be missing is not evidence of absence.")
        return 1
    print("CONTROL PASSED: both known-absent files detected (%s)" % ", ".join(seen))

    ignored = _would_be_ignored(list(missing))
    hits = {b: v for b, v in missing.items() if b in ignored}

    print("\nreferenced-but-absent basenames : %d" % len(missing))
    print("of those, GITIGNORED by pattern : %d   <-- the artifact class" % len(hits))
    if hits:
        print()
        by_test = collections.defaultdict(list)
        for b, ts in sorted(hits.items()):
            print("  %-34s <- %s" % (b, ", ".join(sorted(ts))))
            for t in ts:
                by_test[t].append(b)
        print("\naffected test files: %d" % len(by_test))
        for t, bs in sorted(by_test.items()):
            print("  %-32s depends on %d gitignored artifact(s)" % (t, len(bs)))
    # --- second route: manifests listing gitignored artifacts --------------------------
    print("\nManifest route (paths a test reads from a manifest, not from its own source):")
    # ONLY manifests some test actually reads. An earlier version reported every manifest
    # with gitignored-missing entries -- nine of them -- but eight are read by no test and
    # therefore break nothing. Reporting those would be noise, which is the same disease as
    # the permanent red this script exists to cure.
    test_src = {t.name: t.read_text(errors="ignore") for t in ROOT.glob("tests/test_*.py")}
    man_hits = 0
    seen_manifest = False
    for man in sorted(ROOT.rglob("*MANIFEST*.txt")):
        if ".git/" in str(man):
            continue
        # A test reads this manifest only if its source names the manifest AND names the
        # ARC DIRECTORY it lives under. Matching on the manifest's parent folder alone
        # mis-attributed B646/B651 to test_cc2_r5_adopted.py, which does not read them.
        arc_dir = next((p.name for p in man.parents if p.name.startswith("B")), "")
        readers = [n for n, src in test_src.items() if man.name in src and arc_dir and arc_dir in src]
        if not readers:
            continue
        seen_manifest = True
        base = man.parent
        names = []
        for line in man.read_text(errors="ignore").splitlines():
            tok = line.split()
            if tok:
                names.append(tok[-1].strip("()"))
        absent = [n for n in names if n and not (base / n).exists()]
        if not absent:
            continue
        r = subprocess.run(["git", "check-ignore"] + [str(base / n) for n in absent],
                           capture_output=True, text=True)
        ign = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
        if ign:
            man_hits += len(ign)
            print("  %-52s %d listed, %d absent, %d GITIGNORED  <- %s"
                  % (str(man.relative_to(ROOT)), len(names), len(absent), len(ign),
                     ", ".join(readers)))
    if not seen_manifest:
        print("  (no test-read manifest found)")
    elif man_hits == 0:
        print("  none found")

    # Absent-but-NOT-ignored names are reported separately: they may be legitimate
    # (this corpus keeps cross-seat relay files untracked on purpose, and locks assert
    # their NAMES appear in an index, not that the files exist).
    other = sorted(set(missing) - set(hits))
    if other:
        print("\nabsent but not gitignored (may be legitimate, e.g. untracked relay names): %d"
              % len(other))
        for b in other:
            print("  %-34s <- %s" % (b, ", ".join(sorted(missing[b]))))
    return 1 if (hits or man_hits) else 0


if __name__ == "__main__":
    sys.exit(main())
