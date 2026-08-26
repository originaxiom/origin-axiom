#!/usr/bin/env python3
"""affected_tests.py -- the fast lane's test selector (B1152, harvesting cc3's B8139 "cost class").

WHY: collection is the suite's cost bottleneck -- pytest imports EVERY test module before running
any test (see tests/conftest.py), so the full collect alone is minutes and whole runs get killed by
timeout. cc3's B8139 named this the "cost" failure class: a lock that works but is never REACHED.
Given the working-tree (or a diff-range) changes, this prints only the test files whose inputs
changed, so `pytest <those>` collects a handful of files in seconds.

CONSERVATIVE BY DESIGN -- it never risks a false green. Any change it cannot map to a BOUNDED
superset of affected tests makes it fall back to the FULL suite. Safe mappings:
  - a test file             -> itself
  - conftest / plugin       -> FULL (affects every test)
  - frontier/B<id>/...      -> tests/test_b<id>_*.py  +  EVERY corpus-scanning test
  - kill_graph/atlas/views  -> EVERY corpus-scanning test
  - anything else           -> FULL (scripts, gates, core docs, data, root)

The full suite stays the certificate of record (scripts/run_suite.sh). This is the inner-loop lane.

Usage:  python3 scripts/affected_tests.py [ref] [--run]
        ref default HEAD (uncommitted changes). --run executes pytest on the selection (else lists).
        Exit code is pytest's when --run, else 0.
"""
import os
import re
import sys
import glob
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ALL = sorted(glob.glob("tests/test_*.py"))
_ARC = re.compile(r"frontier/(B\d+[a-zA-Z]?)[_/]")
# A test is "corpus-scanning" (must run on any arc / shared-doc change) if it references any of
# these repo-wide inputs. Kept liberal -- over-inclusion only runs more tests, never fewer.
_SCAN = re.compile(
    r"frontier/\*|glob\([^)]*frontier|kill_graph|atlas_data|RECURRENCE_ATLAS|docs/|knowledge/|"
    r"scripts/gates|test_repo_gates|CHANGELOG|PROGRESS_LOG|GOVERNANCE|WORKING_RULES|TERMINOLOGY|"
    r"PROVENANCE|METHOD|README"
)
# Shared corpus / doc inputs -> route to the corpus-scanning set (not FULL): a bank touches these.
_DOC_CORPUS = {"CHANGELOG.md", "PROGRESS_LOG.md", "README.md", "GOVERNANCE.md",
               "WORKING_RULES.md", "TERMINOLOGY.md", "METHOD.md", "PROVENANCE.md"}
# Cross-seat relay correspondence -- verified test-inert (no test reads them; the tracked-forbidden
# gate keeps them out of the substrate), so a loose relay file affects no test.
_RELAY = re.compile(r"^(CC_TO_CC3|CC3_TO_CC|CC_TO_CC2|CC2_TO_CC|CC_TO_CLOUD|CLOUD_TO_CC)[^/]*\.md$")


def _changed(ref):
    out = set()
    for cmd in (["git", "diff", "--name-only", ref],
                ["git", "diff", "--cached", "--name-only"],
                ["git", "ls-files", "--others", "--exclude-standard"]):
        r = subprocess.run(cmd, capture_output=True, text=True)
        out |= {ln for ln in r.stdout.splitlines() if ln.strip()}
    return out


def _corpus_scanners():
    """Every test that reads ACROSS arcs -- must run whenever any arc / generated corpus file
    changes. Detected liberally (over-inclusion is safe; it only runs more)."""
    s = set()
    for f in ALL:
        try:
            if _SCAN.search(open(f, encoding="utf-8", errors="ignore").read()):
                s.add(f)
        except OSError:
            pass
    s.add("tests/test_repo_gates.py")  # the gate runner: always, on any repo/arc change
    return {f for f in s if f in ALL}


def select(files):
    agg = _corpus_scanners()
    sel, full = set(), []
    for f in files:
        base = os.path.basename(f)
        if f.startswith("tests/") and f.endswith(".py"):
            if base in ("conftest.py", "__init__.py"):
                full.append(f)                      # affects every test
            elif f in ALL:
                sel.add(f)                          # (a renamed/deleted test: nothing to run)
        elif f.startswith("frontier/"):
            m = _ARC.match(f)
            if m:
                bid = m.group(1).lower()
                sel |= set(glob.glob(f"tests/test_{bid}_*.py")) | set(glob.glob(f"tests/test_{bid}.py"))
                sel |= agg                          # an arc edit can flip a corpus-aggregate test
            else:
                full.append(f)
        elif (f in _DOC_CORPUS or f.startswith("docs/") or f.startswith("knowledge/")
              or f == "scripts/atlas/atlas_data.json"):
            sel |= agg                              # shared corpus/docs feed the aggregate + gate tests
        elif _RELAY.match(base):
            continue                                # cross-seat relay correspondence: test-inert
        else:
            full.append(f)                          # scripts code, conftest, core, unknown -> full suite
    return sorted(sel), sorted(set(full))


def main():
    argv = [a for a in sys.argv[1:] if a != "--run"]
    ref = argv[0] if argv else "HEAD"
    run = "--run" in sys.argv
    files = _changed(ref)
    sel, full = select(files)
    if full or not sel:
        why = f"unmappable: {full[:6]}" if full else "no test-mapped changes"
        print(f"FULL SUITE REQUIRED ({why}) -- run scripts/run_suite.sh")
        sys.exit(subprocess.run(["scripts/run_suite.sh"]).returncode if run else 0)
    print(f"AFFECTED: {len(sel)} test file(s) for {len(files)} changed path(s)")
    for f in sel:
        print("  " + f)
    if run:
        sys.exit(subprocess.run(["python", "-m", "pytest", "-q", "-p", "no:randomly", *sel]).returncode)


if __name__ == "__main__":
    main()
