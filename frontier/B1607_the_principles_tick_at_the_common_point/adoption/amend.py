#!/usr/bin/env python3
"""B1607 -- GENESIS v1.28 (main's, B1606) -> v1.29 (main's): THE PRINCIPLE'S TICK AT THE COMMON POINT -- the rule a -> ab,
b -> a as one automorphism of the records (L o P; the golden LP; the Gieseking at the root), its lift at the quaternion
point, its action on the parities, and the two hands under the rule, the moves and the double tick; GM5c's branches
computed; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.29 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_28_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_28 = "a2a416d3fc950e89596acea4e05d309b4fbd7b8cd72d3a02ac36c0d8f5ce0921"

TICK = (" **[v1.29] THE PRINCIPLE'S TICK AT THE COMMON POINT (main, B1607; sealed 805e2d488).** The rule a → ab, b → a is L∘P exactly "
        "(the swap, then L; a → ba, b → a is P∘R, its mirror), its matrix the golden LP, det −1, σ² = LR exactly; its mapping torus is m000 "
        "(SnapPy's single-letter bundles with the reversal flag), of which m004 is the orientable double cover — re-verified. So this fork asks "
        "whether the principle's own tick is a move of the weave, and both branches are now computed. At the quaternion point the rule lifts to "
        "±(1 − i − j − k)/2 ∈ 2T (orders 6 and 3; i → k → j); the mirror rule's lift is its k-conjugate, in the same 2T-class, so the common point "
        "does not see the rule from its mirror; the inverse rule's lift lies in the other class of order-6 elements, and the lifts of L and R "
        "(order 8, outside 2T) exchange the two classes. On the three parities L, R and P act by transpositions, the rule by a 3-cycle, the double "
        "tick by the inverse 3-cycle; on every odd-trace word to length eight the sense of the parity 3-cycle is kept by even rotations of the word "
        "and inverted by odd ones, kept by the mirror and inverted by reversal, and the oriented fibre orients no parity triangle — the McKay "
        "orientation (ω against ω²) is neither a thread invariant nor the mirror bit (the seat's W26, verified on main). **The two hands are "
        "complementary:** the records' orientation (T against T̄ on the weave's surface, v1.28) is reversed by the rule and by P and kept by every "
        "move; the McKay orientation is kept by the rule and inverted by every move; the double tick keeps both. If P is a move, the weave contains "
        "its mirror and its three is achiral (the form of W21 is reversed by P), its object the non-orientable quotient; the chiral three of v1.28 "
        "lives on the double tick's weave ⟨L, R⟩ = SL(2, ℤ), whose object is the orientation double cover (m004 over m000 at the root), and the hand "
        "is the choice of its sheet, which the rule — the deck involution (B466) — does not make. So **neither hand is derived on the weave**; each is "
        "derived on a subweave the weave does not select: a selection, located. GM5c stays OPEN as a fork; what it decides is now computed on both branches.")

CHANGES = [
 ("**Version 1.28 · 2026-10-08 · canonical.**", "**Version 1.29 · 2026-10-08 · canonical.**"),
 ("the identity is Skuratovskii's Prop. 1, arXiv:2307.13873). |",
  "the identity is Skuratovskii's Prop. 1, arXiv:2307.13873)." + TICK + " |"),
 ("- **v1.28 · 2026-10-08 · main B1606.** Three on the weave, graded.\n",
  "- **v1.29 · 2026-10-08 · main B1607.** The principle's tick at the common point.\n"
  "  - GM5c: the rule a → ab, b → a is L∘P (the golden LP, det −1; σ² = LR; the Gieseking m000 at the root, m004 its double cover); its lift at the quaternion point ±(1 − i − j − k)/2 ∈ 2T, the mirror rule's lift k-conjugate, the inverse rule's in the other class, exchanged by the moves' lifts; on the parities the moves are transpositions and the rule a 3-cycle, and the sense of a thread's parity 3-cycle is neither a thread invariant nor the mirror bit (W26 verified). The two hands complementary — the records' orientation reversed by the rule and P, kept by the moves; the McKay orientation kept by the rule, inverted by every move; the double tick keeps both — and neither derived on the weave: each a selection, located. GM5c's branches computed; the fork stays open.\n"
  "- **v1.28 · 2026-10-08 · main B1606.** Three on the weave, graded.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_28, "the received v1.28 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.29 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.29, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
