#!/usr/bin/env python3
"""B1609 -- GENESIS v1.29 (main's, B1607) -> v1.30 (main's): THE EVEN SUBWEAVE -- on the subweave where both hands are
global choices the weave's three is not a sector's count: the three is the S3-invariant part of a level-2 count, and every
McKay sector counts nine; the three's hand is the records' orientation, the bit that also carries the qutrit flux class
(the SM seat's W30); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.30 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_29_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_29 = "f0e88ea19cacc41268236e0fe65a133655c96eed6ad8382c6dcafc79521fd858"

EVEN = (" **[v1.30] THE EVEN SUBWEAVE (main, B1609; sealed f8b9a8fea).** On the index-2 subweave Γ of even-length words "
        "(ℤ/6 ∗_{ℤ/2} ℤ/6, the preimage of A₃), where both hands are global choices, the E₆ 27 counts −χ(Γ; 27) = 9 = 3 + 6 "
        "(Shapiro: the weave's three plus a sign-twisted six) through the principal sl₂, E₆(a₁) and E₆(a₃) alike; at level 2 "
        "the 27 is 3·1 + 6·ε + 9·std; and each of the three McKay sectors ω⁰, ω, ω² on Γ counts nine (the 78: 30, 24, 24). "
        "So **the weave's three is the S₃-invariant part of a level-2 count and is the count of no McKay sector**: a global "
        "choice of ω and the count three are exclusive on the weave's surface, and the McKay orientation (ω against ω²; "
        "27 against 27̄) cannot be the hand of the three. On Γ the puncture keeps its odd index (three inequivalent doublets "
        "under 2T, the deck exchanging the two McKay-labelled ones; ±3 with the grading), and W21's form is kept by every "
        "move, so the hand that survives is the records' orientation — the same bit that carries the qutrit flux class "
        "(commutator ω against ω̄; kept by L, R and −I, reversed by P: the SM seat's W30). Every route to the gauge side's "
        "complex structure on the record now meets this fork.")

CHANGES = [
 ("**Version 1.29 · 2026-10-08 · canonical.**", "**Version 1.30 · 2026-10-08 · canonical.**"),
 ("GM5c stays OPEN as a fork; what it decides is now computed on both branches.",
  "GM5c stays OPEN as a fork; what it decides is now computed on both branches." + EVEN),
 ("- **v1.29 · 2026-10-08 · main B1607.** The principle's tick at the common point.\n",
  "- **v1.30 · 2026-10-08 · main B1609.** The even subweave.\n"
  "  - GM5c/FK14: on the even subweave (both hands global) the 27 counts 9 = 3 + 6, every McKay sector counts nine, and the weave's three is the S₃-invariant part of the level-2 count 3·1 + 6·ε + 9·std — a global ω and the three are exclusive, so the McKay orientation is not the three's hand; the hand is the records' orientation, which also carries the qutrit flux class (W30). The fork GM5c is where every gauge-side route now meets.\n"
  "- **v1.29 · 2026-10-08 · main B1607.** The principle's tick at the common point.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_29, "the received v1.29 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.30 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.30, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
