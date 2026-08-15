#!/usr/bin/env python3
"""FORCEDNESS CENSUS — the chain's label profile, regenerated and gate-checked.

WHY THIS EXISTS
---------------
The chain's forcedness is a real, banked property, but it lives DISTRIBUTED across
the per-link labels in docs/THEOREM_LEDGER.md. Nothing states it as one fact, so
readers meet Part 0's "THREE declared choices" and never learn that 39 of 43 links
are forced, or that the stretch doing the work contains no choice at all.

That is how it got lost before. Prose rots (docs/INDEX.md went five weeks stale
while looking authoritative); a checker does not. This script regenerates the census
from the ledger and FAILS if the counts drift, so the fact cannot quietly decay.

WHAT IT ASSERTS
---------------
1. the label census over all C-links
2. THE AXIOM-FREE STRETCH: no [AXIOM] link between C6 (the knot, Thurston/Riley)
   and C17 inclusive -- the stretch in which e6 and the 27 arrive.
3. the axioms are exactly {C3, C4, C5, C18} -- three BEFORE the knot, one at the
   observer's closings, none in the stretch above.

Run:  python3 scripts/checks/forcedness_census.py
Exit: 0 on match, 1 on drift (with the diff named).

Self-contained: stdlib only. Pass a path to check a different copy (used by the
drift test, which must never edit the real ledger).
"""
import re
import sys
from collections import Counter
from pathlib import Path

LEDGER = "docs/THEOREM_LEDGER.md"

# The banked profile. Update ONLY with a banked ledger change, never to silence a failure.
EXPECTED = {
    "THEOREM": 26,
    "IDENTITY": 6,
    "NO-GO": 5,
    "AXIOM": 4,
    "COROLLARY": 1,
    "CENSUS": 1,
}
# NOTE 2026-08-15 -- THE PAPER IS NOW STRICTER THAN THIS GATE.
# This census certifies "no declared choice in C6..C17". The structure paper has
# since rescoped that: the PRINCIPAL PLACEMENT of 2T inside a chosen sl2 conjugacy
# class of e6 is a declared choice (C4), made between the manifold and the algebra,
# and the paper prices it as an argument from economy rather than a theorem.
# The chain ledger does not carry that step as a link, so this gate cannot see it and
# still passes. DO NOT read a green census here as certifying the un-amended
# sentence; the paper's Scope on the principal placement governs.
EXPECTED_AXIOMS = [3, 4, 5, 18]
STRETCH = (6, 17)  # the knot .. the algebra's no-gos; e6 and the 27 arrive inside

LINK = re.compile(r"^\*\*C(\d+)\s*\[([A-Z][A-Z-]*)")


def parse(text):
    """-> {link_number: label}, first label wins (a link is declared once)."""
    out = {}
    for line in text.splitlines():
        m = LINK.match(line)
        if m:
            out.setdefault(int(m.group(1)), m.group(2))
    return out


def main(argv):
    path = Path(argv[1]) if len(argv) > 1 else Path(LEDGER)
    if not path.exists():
        print(f"FAIL: ledger not found: {path}")
        return 1

    links = parse(path.read_text(encoding="utf-8"))
    if not links:
        # Empty is never a result -- an unparseable ledger is a failure, not a pass.
        print(f"FAIL: no C-links parsed from {path} (format changed?)")
        return 1

    counts = Counter(links.values())
    axioms = sorted(n for n, lab in links.items() if lab == "AXIOM")
    lo, hi = STRETCH
    in_stretch = sorted(n for n in axioms if lo <= n <= hi)
    forced = sum(v for k, v in counts.items() if k != "AXIOM")

    print(f"THE FORCEDNESS CENSUS  ({path}, {len(links)} links)")
    print("-" * 52)
    for label, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {label:<10} {n:>3}")
    print("-" * 52)
    print(f"  FORCED (non-axiom): {forced} of {len(links)}")
    print(f"  axioms at: {axioms}")
    print(f"  axioms in C{lo}..C{hi} (the knot -> the algebra): {in_stretch or 'NONE'}")
    print()

    bad = []
    if dict(counts) != EXPECTED:
        bad.append(f"census drift: got {dict(counts)}, expected {EXPECTED}")
    if axioms != EXPECTED_AXIOMS:
        bad.append(f"axiom set drift: got {axioms}, expected {EXPECTED_AXIOMS}")
    if in_stretch:
        bad.append(f"AXIOM-FREE STRETCH BROKEN: {in_stretch} in C{lo}..C{hi}")

    if bad:
        for b in bad:
            print(f"FAIL: {b}")
        print("\nIf a link was legitimately relabelled, update EXPECTED with the")
        print("banking commit cited -- do not edit it to silence a failure.")
        return 1

    print("PASS: the census holds; the axiom-free stretch is intact.")
    print(f"      From the knot (C{lo}) to C{hi} -- where e6 and the 27 arrive --")
    print("      there is not one declared choice.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
