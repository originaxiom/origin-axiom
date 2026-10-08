#!/usr/bin/env python3
"""B1620 -- GENESIS v1.34 (main's, B1617) -> v1.35 (main's): τ = ω retired as a tested postulate (the owner-agreed plan of
2026-10-08: the goal restated, the breaking arc sealed, a write-up for outside review, τ = ω retired once computed out),
and the breaking the weave allows (B1620); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.35 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_34_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_34 = "71be2dfe0e55c2b8acf6ef452840eeb03120b70ec6b3097c64d1dd03129f1d57"

ADD = (" **[v1.35] τ = ω RETIRED AS TESTED (the owner-agreed plan of 2026-10-08).** Given τ = ω, no weight gives a hierarchy "
       "at ω or near it in either term: the Dirac masses are degenerate for every weight (B1618), the Majorana masses vanish at "
       "even weight and are degenerate at odd weight (B1618's addendum of 2026-10-08). Results stated \"given τ = ω\" stand as "
       "conditional; the modulus is no longer a working postulate, and the choice of τ is open as before. **[v1.35] THE "
       "BREAKING THE WEAVE ALLOWS (B1620, PROVED).** On all 68 subgroups of the weave's group, none chosen, three distinct "
       "masses need an abelian residual (57, exactly the abelian ones), every such residual leaves the masses free, and no "
       "mixing family short of the full four reaches the CKM, under T̄ ⊗ T, T ⊗ T and Sym² T alike (the last two the SM "
       "seat's W39, given Λ): **the weave's symmetry reduces none of the 13 flavour parameters**; the PMNS reduces to two "
       "(the TM type, P10) under the first two tensors and not at all under Sym² T. With couplings in τ alone every residual "
       "contains the inner automorphisms and every mixing matrix is a permutation, so the observed mixing needs a vacuum that "
       "breaks the parity grading. Outside the weave the rule's fixed-point word splits the three parity sectors 1 + 2 (the "
       "clock's parity bounded; the two letter-reading walks one orbit of φ): forced, elementary (A + B = n), its physical "
       "meaning open.")

CHANGES = [
 ("**Version 1.34 · 2026-10-08 · canonical.**", "**Version 1.35 · 2026-10-08 · canonical.**"),
 ("weight-dependent phases rather than in the invariant line.", "weight-dependent phases rather than in the invariant line." + ADD),
 ("- **v1.34 · 2026-10-08 · main B1617.**",
  "- **v1.35 · 2026-10-08 · main B1620.** τ = ω retired as tested; the breaking the weave allows.\n"
  "  - τ = ω: no hierarchy at ω for any weight in either term (B1617, B1618 and its odd-weight addendum); results \"given τ = ω\" stay conditional. B1620: on every subgroup and under all three mass tensors the weave reduces none of the 13; τ-only couplings give permutation mixing; the word's 1 + 2 split of the parity sectors.\n"
  "- **v1.34 · 2026-10-08 · main B1617.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_34, "the received v1.34 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.35 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.35, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
