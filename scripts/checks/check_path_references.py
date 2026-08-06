#!/usr/bin/env python3
"""Check that every backticked repo-path cited in a tracked .md file actually resolves.

Instituted 2026-07-29 (Review 32 sweep). The repo cites its own artifacts overwhelmingly as
backticked paths (~1331 of them) rather than markdown links (~32), so a markdown link-checker
audits 2% of the real reference graph. This audits the other 98%.

The first run found 13 non-resolving paths, of which exactly TWO were defects:
  papers/sl4_dehn_filling/README.md      cited frontier/B149/... for B149_sl4_ideal_completeness/
                                         -- in a paper headed for external Zenodo deposit
  frontier/B350_.../FINDINGS.md          cited tests/test_b347_... for test_b350_...
The other eleven were legitimate and are handled by rule, not by whitelist, wherever possible:

  RESOLUTION RULE (not an exemption): a path is tried repo-root-relative AND relative to the
  citing file's own directory. The B600 packet README cites `scripts/engine.py` meaning its own
  packet/scripts/engine.py -- correct in context. Six citations resolved this way.

  EXEMPTIONS (judgment, so they are explicit and few):
  - PROGRESS_LOG.md is append-only by GOVERNANCE §9 and gate `append-only`. Historical entries
    naming since-renamed files CANNOT be corrected without violating that. History is allowed
    to be stale; that is what makes it history.
  - frontier/B742_negatives_hunt_p1/reviews/ are hash-pinned forensic seals (also exempt in
    gates.gate_attribution). They cite B739/B737 paths from before a renumber. Editing them
    would break the seals they exist to preserve.
  - Cross-clone provenance pins: docs/CLOSURE_2026-07-10.md is the terminal doc of the AUDIT
    SEAT's clone (branch closure/phase1-duels @ e42c336), not a main-repo file. Citing it is
    correct; creating it here would be a forgery.
  - Paths containing '...' are prose elisions, not paths.

Run:  python3 scripts/checks/check_path_references.py        (exit 1 if any unexplained)

Lives under scripts/checks/, NOT scripts/audit/: .gitignore line 11 is a bare `audit/`,
unanchored, so it swallows any directory named audit at any depth. A scripts/audit/ copy
would be silently untracked -- the gate would soft-skip on a fresh clone and pass while
checking nothing. Discovered when the first commit attempt refused to add the file.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Directories that look like repo paths when they appear inside backticks.
_DIRS = ("tests", "frontier", "docs", "scripts", "knowledge", "papers",
         "speculations", "philosophy", "story", "src")
PATH_RE = re.compile(
    r"`((?:" + "|".join(_DIRS) + r")/[A-Za-z0-9_./\-]+\.(?:py|md|json|txt))`")

# Files whose stale citations are structurally uncorrectable -- see module docstring.
EXEMPT_CITERS = ("PROGRESS_LOG.md",
                 "frontier/B921_branch_harvest/harvested/",  # forensic ARCHIVE copies: their internal citations reference the SOURCE BRANCH's layout by design (the harvest preserves them verbatim; the manifest maps them) -- added at the B921 harvest, same class as the B742 forensic seals
                 "frontier/B742_negatives_hunt_p1/reviews/")

# Paths that correctly name something outside this repo.
EXEMPT_TARGETS = frozenset({
    "docs/CLOSURE_2026-07-10.md",          # audit-seat clone, closure/phase1-duels @ e42c336
})


def scan():
    out = subprocess.run(["git", "-C", ROOT, "ls-files", "*.md"],
                         capture_output=True, text=True, timeout=60).stdout
    unexplained, total = [], 0
    for rel in out.split():
        if rel.startswith(EXEMPT_CITERS):
            continue
        try:
            text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        except OSError:
            continue
        citing_dir = os.path.dirname(os.path.join(ROOT, rel))
        for m in PATH_RE.finditer(text):
            target = m.group(1)
            total += 1
            if "..." in target or target in EXEMPT_TARGETS:
                continue
            # repo-root-relative, else relative to the citing file's own directory
            if os.path.exists(os.path.join(ROOT, target)) or \
               os.path.exists(os.path.join(citing_dir, target)):
                continue
            unexplained.append((rel, target))
    return total, unexplained


def main():
    total, bad = scan()
    print(f"backticked repo-path citations checked: {total}")
    if not bad:
        print("all resolve (repo-root or citing-file-relative)")
        return 0
    print(f"UNRESOLVED: {len(bad)}")
    for rel, target in sorted(set(bad)):
        print(f"  {rel}\n      -> {target}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
