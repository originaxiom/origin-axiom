#!/usr/bin/env python3
"""CELL 10 -- propagation onto main (addendum-only), verified against the banked cells.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL10_PREREG.md

The owner authorised ADDENDUM-ONLY edits to main: append dated addenda beside
the affected rows, strike nothing, rewrite nothing.

Three corrections Phase 1 and Phase 2 found in main-tree files:
  1. frontier/B749_genesis_forks/FINDINGS.md -- the F9 addendum states "The
     price of a third record is the atom" with NO depth qualifier; false at
     depth 4 (cell 5).
  2. docs/TOE_REQUIREMENTS_LEDGER.md -- section C row 2's "counts 2 at every
     fixed locus" carries no frame, so its 2 and B1321's 3 read as comparable
     and are not (cell 3).
  3. docs/WHAT_WOULD_COUNT.md -- section 4A lacks B1116's scope caveat, which
     GRAND_COMPUTATION_LEDGER says "must ride with the headline" (cell 9).

THE INSTRUMENT: an addendum that misquotes its own certificate is worse than
no addendum.  So every load-bearing number and quotation in the three addenda
is checked BACK against the banked cell outputs, and the edits are checked to
be APPEND-ONLY (zero deletions in the diff).

Stdlib only.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "outside_bench", "outputs")

TOUCHED = [
    "frontier/B749_genesis_forks/FINDINGS.md",
    "docs/TOE_REQUIREMENTS_LEDGER.md",
    "docs/WHAT_WOULD_COUNT.md",
]


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def read(rel, base=ROOT):
    with open(os.path.join(base, rel), encoding="utf-8") as fh:
        return norm(fh.read())


# (addendum file, the string it asserts, the banked cell output that must also carry it)
FAITHFUL = [
    ("frontier/B749_genesis_forks/FINDINGS.md", "m412",
     "require_and_test_cell5_out.txt"),
    ("frontier/B749_genesis_forks/FINDINGS.md", "5.074708",
     "require_and_test_cell5_out.txt"),
    ("frontier/B749_genesis_forks/FINDINGS.md", "12.179299",
     "require_and_test_cell5_out.txt"),
    ("frontier/B749_genesis_forks/FINDINGS.md", "10 684",
     None),   # arithmetic, checked below
    ("docs/TOE_REQUIREMENTS_LEDGER.md", "89.88",
     "require_and_test_cell3_out.txt"),
    ("docs/TOE_REQUIREMENTS_LEDGER.md", "0.050",
     "require_and_test_cell3_out.txt"),
    ("docs/TOE_REQUIREMENTS_LEDGER.md", "m202",
     "require_and_test_cell3_out.txt"),
    ("docs/WHAT_WOULD_COUNT.md",
     "Every banked value/scale no-go quantifies over SINGLE-LEVEL invariants",
     "require_and_test_cell9_out.txt"),
    ("docs/WHAT_WOULD_COUNT.md", "consumes rather than reproves",
     "require_and_test_cell9_out.txt"),
    ("docs/WHAT_WOULD_COUNT.md", "no SM number is produced",
     "require_and_test_cell9_out.txt"),
]

# quotations the addenda attribute to OTHER files -- must be present there
ATTRIBUTED = [
    ("docs/MAIN_GOAL.md", "|det(A−I)| ∈ {0: 882, 4: 494}"),
    ("docs/MAIN_GOAL.md", "χ(Fix g) = 1 − s_μ(g) ∈ {0, 2}"),
    ("docs/GRAND_COMPUTATION_LEDGER.md", "must ride with the headline"),
    ("docs/THE_SM_VERDICT.md", "no SM number is produced"),
    ("frontier/B1323_the_genesis_upgrades/FINDINGS.md",
     "a computed fork over the enumerated set, not a theorem about all carriers"),
    ("frontier/B666_leads_campaign/cellS/PROOF_NOTE.md",
     "the one assembly ingredient this note consumes rather than reproves"),
    ("frontier/B1116_asymptotic_channel/FINDINGS.md",
     "Every banked value/scale no-go quantifies over SINGLE-LEVEL invariants"),
]


def main() -> int:
    print("=" * 78)
    print(" CELL 10 -- PROPAGATION ONTO MAIN, VERIFIED")
    print("=" * 78)
    failures = []

    # ------------------------------------------------------------------ S1
    rule("CONTROL S1 -- the edits must be APPEND-ONLY (zero deletions)")
    diff = subprocess.run(["git", "-C", ROOT, "diff", "--numstat", "--"] + TOUCHED,
                          capture_output=True, text=True)
    if diff.returncode != 0:
        print("    git diff failed:", diff.stderr.strip())
        failures.append("S1-git")
    total_del = 0
    for line in diff.stdout.strip().splitlines():
        add, dele, path = line.split("\t")
        print(f"    +{add:>4}  -{dele:>4}   {path}")
        total_del += int(dele) if dele.isdigit() else 0
    print(f"    total deletions: {total_del}")
    ok_s1 = (total_del == 0) and bool(diff.stdout.strip())
    print(f"    -> {'PASS' if ok_s1 else 'FAIL'} (strike nothing, rewrite nothing)")
    if not ok_s1:
        failures.append("S1")

    # ------------------------------------------------------------------ S2
    rule("CONTROL S2 -- every number in an addendum is in the cell that produced it")
    cache = {}
    bad = []
    for rel, needle, outfile in FAITHFUL:
        if rel not in cache:
            cache[rel] = read(rel)
        in_doc = norm(needle) in cache[rel]
        if outfile:
            key = "OUT:" + outfile
            if key not in cache:
                cache[key] = read(outfile, base=OUT)
            in_cell = norm(needle) in cache[key]
        else:
            in_cell = None
        mark = "ok " if (in_doc and in_cell is not False) else "FAIL"
        print(f"    [{mark}] {needle[:46]:46s} doc={in_doc} cell={in_cell}"
              + (f"  ({outfile})" if outfile else "  (arithmetic)"))
        if not in_doc or in_cell is False:
            bad.append(needle)
    print(f"\n    checked {len(FAITHFUL)}   unfaithful {len(bad)}")
    assert len(FAITHFUL) > 0, "nothing checked -- the B1197 vacuity trap"
    if bad:
        failures.append("S2")
    print(f"    -> {'PASS' if not bad else 'FAIL'}")

    # ------------------------------------------------------------------ S3
    rule("CONTROL S3 -- every quotation an addendum ATTRIBUTES is in the file named")
    bad2 = []
    for rel, q in ATTRIBUTED:
        if rel not in cache:
            cache[rel] = read(rel)
        ok = norm(q) in cache[rel]
        print(f"    [{'ok ' if ok else 'MISS'}] {rel:52s} {q[:38]}")
        if not ok:
            bad2.append((rel, q))
    print(f"\n    checked {len(ATTRIBUTED)}   missing {len(bad2)}")
    if bad2:
        failures.append("S3")
    print(f"    -> {'PASS' if not bad2 else 'FAIL'}")

    # ------------------------------------------------------------------ S4
    rule("CONTROL S4 -- the word-count arithmetic in the B749 addendum")
    s12 = sum(6 ** n for n in range(2, 6))
    s04 = sum(4 ** n for n in range(2, 6))
    base12, base04 = sum(6 ** n for n in range(2, 4)), sum(4 ** n for n in range(2, 4))
    print(f"    S_1,2  depth<=3 {base12}   depth<=5 {s12}")
    print(f"    S_0,4  depth<=3 {base04}   depth<=5 {s04}")
    print(f"    totals  {base12 + base04} -> {s12 + s04}")
    ok_s4 = (base12 + base04 == 332) and (s12 + s04 == 10684)
    print(f"    addendum says 332 -> 10 684   -> {'PASS' if ok_s4 else 'FAIL'}")
    if not ok_s4:
        failures.append("S4")

    # ------------------------------------------------------------------ row 5
    rule("ROW 5 -- dynamics and gravity: NOT-COMPUTABLE, and it stays that way")
    print("""
    A row this bench cannot move is reported as such, not converted into
    activity.  Both rows stay NOT-COMPUTABLE, and the record names its own
    minimal sub-question for each:

      DYNAMICS  TOE_REQUIREMENTS_LEDGER section E row 1 lists SIX declared
                inputs for the one conditional 4d action in the record (the
                Lorentzian 4d spin spacetime, the COMPACT real form, the field
                content, the family number N_f, the potential's coefficients,
                the scales).  The row becomes computable when an action is
                DERIVED rather than declared.  Nothing in this programme
                derives one, and no cell here attempts it.

      GRAVITY   the grade is "containment, not a theory": a spin-2 slot in the
                E6(-26) branch's 64, with NO propagator and NO coupling.  The
                minimal sub-question the record names is section E row 4's
                I-26 -- "the dimension gap not exhibited".  Exhibiting it is
                specialist work on Pantev-Wijnholt's frame for a 3-manifold
                with boundary; FRESH_EYES Q9 has carried it as OPEN since
                2026-09-08 and this bench has no instrument for it.

    STATED PLAINLY: this bench cannot move either row today, and says so
    rather than producing activity around them.""")

    rule("VERDICT")
    print(f"    addenda written to {len(TOUCHED)} main-tree files, append-only")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: nothing new.  This cell PROPAGATES results already banked
    in cells 3, 5 and 9 and verifies the propagation is faithful to them.  No
    verdict on main is edited or struck.  Gate 5 untouched.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
