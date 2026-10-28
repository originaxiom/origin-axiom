#!/usr/bin/env python3
"""B1797 -- GENESIS v1.58 (main's) -> v1.59 (main's): the completion map's C8 recorded (P-288) -- FK10's tagged unit
reduced to the field's existence (FK15), a type identification, uniform end data and the least remainder, given Lambda
and the hand, none derived (B1796: the SM seat's W123, its exact route, and W130's non-unitarity and Hitchin's equation
verified on main).  FK10's tag and every status cell unchanged; FK15 gains a pointer.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.59 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_58_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_58 = "95e6d2f5ab1f7b2ec68de80bdc530187d33adc8a807dc48f554811413be6c3a1"
CHANGES = [
 ("**Version 1.58 · 2026-10-24 · canonical.**", "**Version 1.59 · 2026-10-28 · canonical.**"),
 ("FK10's single unit at the weave's cusp stays a tagged postulate. | an end condition derived from physics (sL-8) |",
  "FK10's single unit at the weave's cusp stays a tagged postulate. **[v1.59] The unit reduced to the field's existence "
  "and three further links, none derived on the record (B1796; P-288).** B1796 verified on main the SM seat's W123 (its "
  "exact route; row 1301) and, of W130 (row 1309), the point's non-unitarity and Hitchin's equation; W130's images, "
  "other points, 'exactly one field', H3 and H4 stay the seat's, unverified on main. With m = (m_P, m_M, m_N) units of "
  "end data on the eigenlines P, M = v₊, N of ρ_T's T-matrix, the weight-3/2 forms of ρ_T have dimension "
  "max(0, m_P + m_M + m_N) on every vector computed; proved: 0 whenever Σm ≤ 0, and 3n for n ≥ 0 uniform units "
  "(O(nδ), W46's uniform twist). The least datum on one eigenline gives one dimension (on v₊ alone, ∂R; B1700); the "
  "least uniform datum gives three, the space whose index is W46's three (as does any datum with Σm = 3); that the "
  "Higgs direction and the chiral three's zero modes share this space is B1700's reading, not a claim. At a Fuchsian "
  "point of the fibre, such as (3, 3, 3) (the modular torus), the flat datum is not unitary, so its Higgs field is "
  "nowhere zero. So the unit follows from four links, none derived on the record: the field's existence (FK15; W130's "
  "'forced' is PF1 read on the fibre's rest state, the seat's reading); the identification of the fibre's Higgs field "
  "(End E ⊗ K) with a weight-3/2 form of ρ_T; uniform end data; and the least remainder — given Λ and the hand (for "
  "the conjugate hand there is no weight-3/2 space at any end data). That the three are generations is FK11's (met "
  "conditionally, given Λ and the unit, v1.39). The tag stays: this is a reduction of the postulate, not a derivation. "
  "| an end condition derived from physics (sL-8) |"),
 ("or both (B1651). Settled by a derivation of the field",
  "or both (B1651). **[v1.59]** FK10's tagged unit follows from this fork's existence half — for the fibre's Higgs "
  "field as W130 types it (End E ⊗ K), not B1654's (0, 1) typing above — with three further links, none derived (B1796; "
  "see FK10). Settled by a derivation of the field"),
 ("- **v1.58 · 2026-10-24 · main B1754.**",
  "- **v1.59 · 2026-10-28 · main B1797.** P-288 (the completion map's C8): FK10's tagged unit reduced to the field's "
  "existence (FK15), a type identification, uniform end data and the least remainder, given Λ and the hand, none "
  "derived (B1796: W123's exact route and W130's non-unitarity verified on main); FK15 gains a pointer. No status cell "
  "changes; FK10 stays a tagged postulate; the v1.58 entry below is not rewritten.\n"
  "- **v1.58 · 2026-10-24 · main B1754.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_58, "the received v1.58 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.59 · 2026-10-28 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written (v1.59)")
