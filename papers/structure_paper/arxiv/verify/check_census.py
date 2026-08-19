#!/usr/bin/env python3
"""
Appendix B -- Census 5.1, recomputed from the submitted source.

## WHY THIS SCRIPT EXISTS

The census counts the chain ledger, and the ledger lived only in the repository. A paper
whose subject is verifiability should not ask a referee to take a count on trust, so the
links now travel with the source: chain_links.md carries one row per link, label included,
extracted from the ledger. This script recomputes the census from that file.

WHAT IT ASSERTS
  1. the ledger deposit has exactly 43 links, with labels parsed rather than assumed;
  2. the six figures the paper prints -- 26 theorems, 6 identities, 5 no-go results,
     1 corollary, 1 census, 4 axioms -- and that they sum to 43;
  3. the axioms are exactly C3, C4, C5, C18.

WHAT IT DOES NOT ASSERT, and the distinction is the census's own.  A count of LINKS is not
a count of STIPULATIONS.  The principal placement is a stipulation and not a link at all,
so no census over links can see it; the paper's scope on that placement governs, and a
green run here certifies the arithmetic of the ledger, nothing about what was assumed.

No third-party dependencies.
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEPOSIT = os.path.join(HERE, "chain_links.md")
EXPECTED = {"THEOREM": 26, "IDENTITY": 6, "NO-GO": 5, "COROLLARY": 1,
            "CENSUS": 1, "AXIOM": 4}
EXPECTED_AXIOMS = [3, 4, 5, 18]
FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)


def main():
    print("=" * 70)
    print("Census 5.1 -- recomputed from the deposited chain ledger")
    print("=" * 70)
    if not os.path.exists(DEPOSIT):
        print(f"FAIL: deposit not found: {DEPOSIT}")
        return 1
    rows = []
    for line in open(DEPOSIT, encoding="utf-8"):
        m = re.match(r"^\|\s*C(\d+)\s*\|\s*\*\*([A-Z][A-Z-]*)\*\*\s*\|", line)
        if m:
            rows.append((int(m.group(1)), m.group(2)))
    # An unparseable deposit is a failure, never a pass.
    if not rows:
        print("FAIL: no links parsed from the deposit (format changed?)")
        return 1

    print(f"\n  links parsed: {len(rows)}")
    counts = collections.Counter(lab for _, lab in rows)
    for k in sorted(EXPECTED):
        print(f"      {k:<10} {counts[k]}")
    print()
    check("the deposit carries 43 links", len(rows), 43)
    check("link numbers are distinct", len({n for n, _ in rows}), len(rows))
    check("the label census matches the printed figures",
          {k: counts[k] for k in EXPECTED}, EXPECTED)
    check("the six figures sum to 43", sum(EXPECTED.values()), 43)
    check("the axioms are exactly C3, C4, C5, C18",
          sorted(n for n, lab in rows if lab == "AXIOM"), EXPECTED_AXIOMS)
    check("no label outside the six occurs",
          sorted(set(counts) - set(EXPECTED)), [])
    forced = sum(v for k, v in counts.items() if k != "AXIOM")
    check("39 of the 43 links carry no declared choice", forced, 39)

    print("\n  NOTE, and it is the census's own caveat: a count of LINKS is not a count of")
    print("  STIPULATIONS. The principal placement is a stipulation and not a link, so no")
    print("  census over links can see it. This run certifies the ledger's arithmetic only.")
    print()
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce: {FAILURES}")
        return 1
    print("PASS: every check reproduced exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
