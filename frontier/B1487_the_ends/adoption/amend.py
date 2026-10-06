#!/usr/bin/env python3
"""B1487 -- GENESIS v1.14 (main's, B1482) -> v1.15 (main's): THE ENDS. GAP2 sharpened (a count in the frames on record is a
count of ends; a generated state has one), GAP1 sharpened (the class index is mirror-even for every module; the F-HE frame's
internal group contains the geometry's structure group), the heading corrected to six gaps (the SM seat's P1, credited),
FK14 registered, B1483 and B1484 recorded.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.15 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_14_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_14 = "9c1c44d58222f3bd186f7e744ba7a783f5618495329d0d0ffef8a994a7cf2069"

CHANGES = [
 ("**Version 1.14 · 2026-10-07 · canonical.**", "**Version 1.15 · 2026-10-07 · canonical.**"),
 ("**Five gaps**, none of which work on one state can close:",
  "**Six gaps** (the heading corrected from \"five\" at v1.15 — the SM seat's proposal P1, sm:B1537), none of which work on one state can close:"),
 ("- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.",
  "- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.\n"
  "  **[v1.15] Two facts about every count on the record (B1487).** (i) The class index I(E) = n(E) − n(E*) is mirror-even for\n"
  "  every module: cohomology dimensions do not change under pullback by a diffeomorphism or under complex conjugation, so a\n"
  "  mirror carries a module at a spin structure s to one at its partner s′ with the same index. No choice of module makes a\n"
  "  count see the hand; the hand lives where cohomology vanishes (the odd modules of the lift are acyclic on every word state,\n"
  "  their torsion's phase is the hand, B1481) and can enter a count only as the choice of order (B1466, B1486). (ii) In the\n"
  "  harmonic E₈ frame the internal SU(5)′ contains the geometry's own structure group, SL(4) ⊃ SO(3,1): its 10′ and 5̄′ are\n"
  "  extension classes of the Lorentz vector bundle, and the four is ρ ⊗ ρ̄, blind to the spin structure. A frame is a\n"
  "  hypothesis; this one is a hypothesis of that kind."),
 ("  ends). sL-8's rule forbids choosing an end to rescue a count.",
  "  ends). sL-8's rule forbids choosing an end to rescue a count.\n"
  "  **[v1.15] Sharpened (B1487):** in the harmonic E₈ frame a count IS a count of ends — the SM seat's floor\n"
  "  I(W₁) ≥ k − m_A − b0 (sm:B1544, sm:B1545; checked on main on 390 readings) bounds it by the cusps on which the character is\n"
  "  trivial and the class dies, so g generations need at least g − b0 such cusps; in main's frame F-CI three sits on two-cusped\n"
  "  members and is excluded on one-cusped manifolds (B1291, B1418). **A generated state (§3) has one end; no state of X_gen\n"
  "  carries three generations in either frame, by counting ends, not by search.** The question is FK14."),
 ("| FK13 **[v1.12]** | Which set \"the family as object\" names (the owner's rule of 2026-10-04) |",
  "| FK14 **[v1.15]** | The ends (B1487): does the genesis generate states with several ends, or are generations not ends? | OPEN | a move of the grammar that adds punctures — none is named in §2, and a level (§3) adds none — or a frame whose count is not a count of ends. Bears on it: the LP seat's LP01 (is a manifold covering both m004 and the two-cusped members where three appears reached from the root by a cover?), the SM seat's P6 (the commensurability class as the object; ruled against by FK13), and GAP2. Until it is ruled, a count of three on a cover is a selection, graded by `docs/THE_BAR.md`, not a derivation |\n"
  "| FK13 **[v1.12]** | Which set \"the family as object\" names (the owner's rule of 2026-10-04) |"),
 ("  - B1481 recorded: on the − states every spin structure carries a phase its mirror partner negates.",
  "  - B1481 recorded: on the − states every spin structure carries a phase its mirror partner negates.\n"
  "- **v1.15 · 2026-10-07 · main B1487.** The ends.\n"
  "  - GAP2 sharpened: in the harmonic E₈ frame a count is a count of ends (the SM seat's floor, checked on main); a generated state has one, so no state of X_gen carries three in either frame on record.\n"
  "  - GAP1 sharpened: the class index is mirror-even for every module, so the hand can enter a count only as the order; the harmonic frame's internal group contains the geometry's structure group.\n"
  "  - FK14 registered: does the genesis generate states with several ends, or are generations not ends?\n"
  "  - The heading of §7 corrected to six gaps (the SM seat's P1, sm:B1537, credited).\n"
  "  - B1483 recorded at GAP6/GAP2: at a cusp the frame space of a spin structure is a bundle of elliptic curves ℂ/ker σ_s; on a − state the two classes of spin structures put complex-conjugate curves there, isomorphic only where the cusp lattice is hexagonal or square.\n"
  "  - B1484 recorded: the weak-mixing-angle crossing needs the colour triplet split from the Higgs doublet, which no flat abelian line does on any state (w_D = −2·w_Q in the 27); it waits, with the chirality count, on a frame in which matter is counted by an index (L250).\n"
  "  - B1485, B1486 recorded: the one generation of the harmonic frame on the silver squares read by main's instrument (every count agrees); at every member the two orders fuse into an irreducible module that counts zero."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_14, "the received v1.14 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.15 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.15, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
