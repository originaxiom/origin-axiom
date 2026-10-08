#!/usr/bin/env python3
"""B1617 -- GENESIS v1.33 (main's, B1616) -> v1.34 (main's): the owner's ruling of 2026-10-08 that the fibre's modulus
tau = omega is a tagged working postulate (made with main), and the weave at tau = omega (B1617); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.34 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_33_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_33 = "c47ffdffde19b9c6e1ab8e2155fdd5d2b6cac195900339b5c614c9e9ed404dce"

OMEGA = (" **[v1.34] THE MODULUS: τ = ω, A TAGGED WORKING POSTULATE (the owner's ruling of 2026-10-08, made with main).** The "
         "weave forces no fibre modulus (no point of the upper half-plane is fixed by every move; only the orbifold points i and "
         "ω are distinguished, ω pointed to by LR ≡ ST mod 2 and by the common point's √−3); results computed at the modulus carry "
         "\"given τ = ω\" and the choice stays formally open. **The weave at τ = ω (B1617, NEGATIVE as sealed):** the residual "
         "symmetry — the order-3 elliptic class, the sign, and every inner automorphism (which acts on the matter as the parity "
         "signs, a symmetry at every τ) — is a group of order 48 under which the triplet T stays irreducible (an A₄-type action), "
         "so at ω an ordinary Higgs vacuum gives one Dirac coupling and three equal masses and no Majorana mass; near ω the "
         "degeneracy splits by powers of ε = τ − ω (U's charges on T: ¼, 7/12, 11/12 of a turn), a quasi-degenerate pattern, "
         "not the observed hierarchy. Owed: Yukawa couplings as modular forms of weight k, which at ω sit in U-eigenspaces with "
         "weight-dependent phases rather than in the invariant line.")

CHANGES = [
 ("**Version 1.33 · 2026-10-08 · canonical.**", "**Version 1.34 · 2026-10-08 · canonical.**"),
 ("values need a forced modulus, dynamics or end data.", "values need a forced modulus, dynamics or end data." + OMEGA),
 ("- **v1.33 · 2026-10-08 · main B1616.**",
  "- **v1.34 · 2026-10-08 · main B1617.** The modulus τ = ω, tagged; the weave at ω.\n"
  "  - The owner's ruling (τ = ω a tagged working postulate). B1617: at ω the residual group (order 48) keeps T irreducible — degenerate masses at the point, quasi-degenerate near it; weighted modular-form Yukawas owed.\n"
  "- **v1.33 · 2026-10-08 · main B1616.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_33, "the received v1.33 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.34 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.34, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
