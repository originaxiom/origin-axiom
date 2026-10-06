#!/usr/bin/env python3
"""B1476 -- GENESIS v1.10 (main's, B1467) -> GENESIS v1.11 (main's): GAP6 narrowed to its hypotheses, and the register
question's bit located on the family (the spin swap, B1474/B1475), under the owner's rule of 2026-10-04.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.11 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_10_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_10 = "b3ac6129e6e63ed409c38a7f6fa603767da2194916ffb89463bb15ed3a45b6a8"

CHANGES = [
 ("**Version 1.10 · 2026-10-03 · canonical.**", "**Version 1.11 · 2026-10-04 · canonical.**"),
 ("- **[v1.9] GAP6, the flatness.** Every frame on this page is a frame of flat bundles, and a flat bundle has ch = rk: no\n"
  "  index built on it can tell 27 from 27̄ (Chern–Weil; the record's Chern–Weil row). The chirality of the Standard Model is a\n"
  "  statement about curvature — instantons, a bulk — that no flat frame carries.",
  "- **[v1.9, narrowed v1.11] GAP6, the flatness.** Every frame on this page is a frame of flat bundles, and a flat bundle has\n"
  "  ch = rk: no characteristic-class index on a CLOSED bulk can tell 27 from 27̄ over it (Chern–Weil; the record's Chern–Weil\n"
  "  row). **[v1.11]** That is the whole of what flatness forbids. With the object as boundary — this page's setting — the\n"
  "  index carries the boundary's spectral term (Atiyah–Patodi–Singer's η), a flat-structure quantity; the record's class\n"
  "  index I = n(V) − n(V*) (B1297) is a flat-bundle quantity that fires at ±1, ±2 on the family (B1418); and the mirror's\n"
  "  action on the spin structure — a flat datum — is genuine on seven amphichiral members and absent on the knot (B1474,\n"
  "  B1475). So the flat frame reaches DISCRETE data (counts, bits, signs) through the boundary and cannot reach CONTINUOUS\n"
  "  values (a mass, a coupling): the record's value-negatives are theorems about flat moduli and bound the frame, not\n"
  "  physics (lead L247; the census of 173 value-kills, 107 on flat premises). Narrowed on two readings of the same day from\n"
  "  opposite sides — the audit lane's R89 (\"narrow GAP6 to its smooth closed bulk spin-Dirac hypotheses\") and the web seat's\n"
  "  handoff (\"the wall is a flat-sector theorem\") — against main's own v1.9 sentence, which had dropped the hypotheses.\n"
  "  What remains of the gap: the continuous values; and the step from the boundary's η to a physical count (B279's\n"
  "  unbanked link, L246 Phase 2)."),
 ("    three kinds cover 14 of the chirality chain's 26 negatives (sm:B1531, read): the taxonomy is incomplete.",
  "    three kinds cover 14 of the chirality chain's 26 negatives (sm:B1531, read): the taxonomy is incomplete.\n"
  "- **v1.11 · 2026-10-04 · main B1476.** One narrowing, one location, one rule.\n"
  "  - GAP6 narrowed to its hypotheses (closed bulk, characteristic classes); the flat frame reaches discrete data through the\n"
  "    boundary (B1297/B1418's index; B1474/B1475's spin swap) and not continuous values (L247's census). Credit R89 and the web seat.\n"
  "  - FK12's bit located on the family: the SL(2,ℂ) lift (the spin structure) is the bit; on seven amphichiral members of the\n"
  "    112-family no spin structure is mirror-invariant and on the knot both are (B1474, B1475); B1476 asks whether the class is\n"
  "    read off CS = ¼ and whether it is the parent's Pin type (sm:B1382) seen from the other side.\n"
  "  - **The owner's rule (2026-10-04): \"existence emerges from the family as object; we shouldn't tie ourselves to m004.\"**\n"
  "    A5 (SE2's torsion-free tie-break) selects a member; the page's object is the family (B1418), and this page's statements\n"
  "    about m004 are statements about one member unless they say otherwise."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_10, "the received v1.10 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


if __name__ == "__main__":
    t = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        if "**Version 1.11 ·" in cur and cur != t: print("GENESIS.md differs from B1476's amendment"); sys.exit(1)
        print("ok"); sys.exit(0)
    open(OUT, "w", encoding="utf-8").write(t); print("GENESIS.md written at v1.11; sha256", hashlib.sha256(t.encode()).hexdigest()[:16])
