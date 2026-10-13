#!/usr/bin/env python3
"""B1641 -- GENESIS v1.42 (main's, B1640) -> v1.43 (main's): W46 verified on main; the fibre loops of M_{1,2} and the ruled
moves are one action under the record's lifts (the geometric lift differs by the central sign at Delta^4), with a parity
selection rule on couplings; the hand is not the puncture condition's orientation at the representation level; the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.43 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_42_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_42 = "6991b5f7334d4c51e7269df9cc50b747e6669f12b5b23afc1d8ab8ca3297b00f"

ADD = (" **[v1.43] W46 on main, and the two objects (B1641).** W46 is verified on main's own lifts: the six local solutions "
       "have exponents (⅛, ⅛, ⅜, ⅝, ⅞, ⅞) and split as irreducibles of dimension 2 and 4, every χ₁ = 0, χ_{3/2}(ρ_T) = 0, and the "
       "four-dimensional index is n(|Λ₊| − 3) — so \"±3 given Λ and the unit\" now rests on main. M₁,₂'s fibre loops are the "
       "inner automorphisms. The lift of them that agrees with the ruled moves at Δ⁴ = conj(a b⁻¹ a⁻¹ b) acts on T by the parity "
       "signs (and Δ⁴ by −1); the geometric lift, trivial on the fibre's cohomology, differs from the moves by the central sign "
       "there. So the surface of the index and the branch of the couplings are one object, and couplings obey a parity "
       "selection rule: a parity-blind Higgs allows only diagonal couplings, a Higgs carrying parity exactly the golden "
       "pattern (c(u, u, u) = 24η⁶). Neither ρ_T nor its conjugate is a sub or quotient of the six, so the hand is not the "
       "puncture condition's orientation at the representation level.")
CHANGES = [
 ("**Version 1.42 · 2026-10-13 · canonical.**", "**Version 1.43 · 2026-10-13 · canonical.**"),
 ("a derivation from the zero modes' period map is owed.", "a derivation from the zero modes' period map is owed." + ADD),
 ("- **v1.42 · 2026-10-13 · main B1640.**",
  "- **v1.43 · 2026-10-13 · main B1641.** W46 verified on main; the two objects are one, with a parity selection rule.\n"
  "  - The fibre loops act on T by the parity signs under the lifts that agree with the moves (the geometric lift differs by −1 at Δ⁴): a parity-blind Higgs gives diagonal couplings only, a Higgs in T the golden pattern; the hand is not the puncture orientation at the representation level.\n"
  "- **v1.42 · 2026-10-13 · main B1640.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_42, "the received v1.42 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.43 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.43, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
