#!/usr/bin/env python3
"""B1497 -- GENESIS v1.22 (main's, B1496) -> v1.23 (main's): FK14 gains the theorem ROOM NEEDS GENUS and the map of the family's
room -- the root's covers have none to degree eight, the sign-twin's one at degree five (o10_150691), where every count is one.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.23 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_22_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_22 = "9a0edfe2196a9256f7eb0c2930becb87cd1bc511f937461409f8c2d752e6fcfa"

CHANGES = [
 ("**Version 1.22 · 2026-10-07 · canonical.**", "**Version 1.23 · 2026-10-07 · canonical.**"),
 ("the record's candidate is the Lefschetz number of the act |",
  "the record's candidate is the Lefschetz number of the act. **[v1.23] Where the room comes from (B1497, T-ROOM-NEEDS-GENUS):** on any cover of a word state the room of the trivial line is the lifted act's invariant homology of the closed fibre, zero at genus one — so it needs a NON-ABELIAN cover of the register (degree ≥ 3), a move §2 does not name. Mapped: the root m004 has no room on any cover to degree eight (24 of its 39 reach genus 2–4); +LLLR none to degree six; the sign-twin m003 has one carrier by degree eight — o10_150691 at degree five (not a cover of m004; arithmetic, chiral; one cusp an index-three sublattice of the hexagonal lattice, one square), room 1. There the four has its first interior class at a trivial character, the second supply first reaches 2, Theorem C's cap is 2 at order four, and every count is one or zero. Both of the physics' mechanisms need what the sign-twin's side has (the hexagonal end; the room): FK4 and FK14 are one question |"),
 ("  - FK14: the specification of three from the verified physics — an index of closed-cycle cohomology, obtained by selection (a free quotient and the characters of its deck group), the 5̄ and 10 counts equal by an identity the class index lacks, nobody deriving three; F-CI = the orbifold mechanism, F-HE = the smooth one; the family blind to both by construction; three generations = ONE rank-5 bundle of index three. THE_BAR's baseline recorded.",
  "  - FK14: the specification of three from the verified physics — an index of closed-cycle cohomology, obtained by selection (a free quotient and the characters of its deck group), the 5̄ and 10 counts equal by an identity the class index lacks, nobody deriving three; F-CI = the orbifold mechanism, F-HE = the smooth one; the family blind to both by construction; three generations = ONE rank-5 bundle of index three. THE_BAR's baseline recorded.\n"
  "- **v1.23 · 2026-10-07 · main B1497.** Room needs genus.\n"
  "  - FK14: T-ROOM-NEEDS-GENUS — the room is the act's invariant closed homology of the fibre of a cover, zero at genus one, so it needs a non-abelian cover of the register; the root has none to degree eight, the sign-twin one at degree five (o10_150691), where the count is still one. FK4 and FK14 read as one question."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_22, "the received v1.22 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.23 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.23, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
