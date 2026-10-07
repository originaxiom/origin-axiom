#!/usr/bin/env python3
"""B1496 -- GENESIS v1.21 (main's, B1495) -> v1.22 (main's): FK14 gains the specification of three from the researched physics
(an index of closed-cycle cohomology, obtained by selection -- a free quotient and characters -- with the 5bar and 10 counts
equal by an identity the class index lacks; nobody derives three), the record's two frames named as the two mechanisms,
and the family's blindness by construction; the version log records it.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.22 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_21_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_21 = "37d28a9badc8576a00725cea9e59aa8687d8ae33a3e920667987d662616494f2"

CHANGES = [
 ("**Version 1.21 · 2026-10-07 · canonical.**", "**Version 1.22 · 2026-10-07 · canonical.**"),
 ("a glued module and the two deck-fixed spin structures are not ruled |",
  "a glued module and the two deck-fixed spin structures are not ruled. **[v1.22] The specification (B1496, the physics researched and verified claim by claim; `docs/THREE_GENERATIONS_RESEARCHED.md`):** in every established construction the number of generations is an INDEX of closed-cycle cohomology (ind(V) = ∫ch₃(V) = −h¹ + h²; ∣χ∣/2 for the standard embedding; ∫G₄ in F-theory), vector-like pairs cancelling; three is obtained by SELECTION — a free quotient divides a cover's count by ∣G∣ and the characters of G (Wilson lines) select the isotypic piece, the index refining per character; the 5̄ and 10 counts are equal by ch₃(Λ²V) = (n − 4)ch₃(V) at rank five, an identity the class index on a 3-manifold does not have (B1495's (3, 9)); no-exotics is a separate condition; nobody derives three. The record's F-CI is the orbifold mechanism (fixed points of a global order-3 symmetry on a hexagonal end; unverified in the run) and F-HE the smooth one (the room = closed cycles, the companion = the cover, the members = its characters, Shapiro = the index per character). **The family is blind to both by construction** — no global order-3 isometry, no closed cycle — so the frames were right to read one. Three generations in the smooth mechanism is ONE rank-5 bundle of index three, never three rank-5 bundles: the object to build is a glued module of the three members. THE_BAR's baseline: selection is the state of the art; a derivation — a reason internal to the genesis for an object of index three — would be new; the record's candidate is the Lefschetz number of the act |"),
 ("  - FK14: L8a15's three members as one rank-15 module read (10′, 5̄′) = (3, 9); the cross terms −2 each (each generation's class through another's four); the orbit reading survives on the 10′ side only, a selection; a glued module and the deck-fixed spin structures not ruled.",
  "  - FK14: L8a15's three members as one rank-15 module read (10′, 5̄′) = (3, 9); the cross terms −2 each (each generation's class through another's four); the orbit reading survives on the 10′ side only, a selection; a glued module and the deck-fixed spin structures not ruled.\n"
  "- **v1.22 · 2026-10-07 · main B1496.** Three generations, researched first.\n"
  "  - FK14: the specification of three from the verified physics — an index of closed-cycle cohomology, obtained by selection (a free quotient and the characters of its deck group), the 5̄ and 10 counts equal by an identity the class index lacks, nobody deriving three; F-CI = the orbifold mechanism, F-HE = the smooth one; the family blind to both by construction; three generations = ONE rank-5 bundle of index three. THE_BAR's baseline recorded."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_21, "the received v1.21 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.22 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.22, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
