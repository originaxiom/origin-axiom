#!/usr/bin/env python3
"""B1491 -- GENESIS v1.16 (main's, B1489) -> v1.17 (main's): FK14 gains the SM seat's fixed-point companions as the first
candidate answer to "what adds an end" (registered, not adopted; two of its facts verified on main), and GAP2 gains the
seat's ceiling beside its floor (the correction to B1487's T3, credited).

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.17 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_16_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_16 = "22c3e6b637600d2b2e3e0ffeaa600bf6aa3dcbe0bc2ecefd7fe7c820e69b14da"

CHANGES = [
 ("**Version 1.16 · 2026-10-07 · canonical.**", "**Version 1.17 · 2026-10-07 · canonical.**"),
 ("Until it is ruled, a count of three on a cover is a selection, graded by `docs/THE_BAR.md`, not a derivation |",
  "Until it is ruled, a count of three on a cover is a selection, graded by `docs/THE_BAR.md`, not a derivation. **[v1.17] The first candidate answer, the SM seat's fixed-point companions (its note of 2026-10-07; registered, not adopted):** every word state has a canonical several-ended cover — the maximal abelian cover to which the cusp lifts, the mapping torus of the monodromy with every fixed point punctured — with ∣2 − tr φ∣ ends, one per fixed point, determined by the state alone (Proposition 1, the seat's proof); m004's is itself, m003's is o10_150729 = S³ − L10n113 (five ends, A₅ on them), m136's has four ends, m135's eight; and on m003's and m136's companions no member carries three (the seat's Proposition 3). **Verified on main (B1491):** o10_150729 is isometric to L10n113; +LLLR, whose monodromy has trace 5, has a three-ended companion — the link complement L8a15, chiral, symmetry group of order 12. So \"an end\" has a candidate meaning in the grammar: a fixed point of the act. What is not derived: that the companion is a state the genesis generates (it is a cover chosen by a character), and any count on one |"),
 ("  trivial and the class dies, so g generations need at least g − b0 such cusps; in main's frame F-CI three sits on two-cusped",
  "  trivial and the class dies, so g generations need at least g − b0 such cusps **[v1.17: and the count is bounded on the other side too, I(W₁) ≤ 2m_A + m_B − b0, the seat's ceiling — every value of it, not only the generation side, is a count of ends; the two-sided form B1487 first wrote was withdrawn on the seat's correction]**; in main's frame F-CI three sits on two-cusped"),
 ("  - P9 (where the supplies can grow): recorded, not adopted as a programme — under FK14 each item is a search for ends, and a count found there is a selection until the rule is named first.",
  "  - P9 (where the supplies can grow): recorded, not adopted as a programme — under FK14 each item is a search for ends, and a count found there is a selection until the rule is named first.\n"
  "- **v1.17 · 2026-10-07 · main B1491.** The correction and the companions.\n"
  "  - GAP2: B1487's T3 corrected on the SM seat's relay — the floor is one-sided; the ceiling I(W₁) ≤ 2m_A + m_B − b0 is the seat's; the generation-side conclusions stand.\n"
  "  - FK14: the seat's fixed-point companions registered as the first candidate answer to what adds an end (∣2 − tr φ∣ ends, one per fixed point of the act); two facts verified on main (o10_150729 = L10n113; +LLLR's three-ended companion L8a15). Not adopted: whether a companion is a generated state is the fork itself."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_16, "the received v1.16 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.17 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.17, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
