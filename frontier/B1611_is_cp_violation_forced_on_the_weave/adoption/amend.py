#!/usr/bin/env python3
"""B1611 -- GENESIS v1.31 (main's, B1610) -> v1.32 (main's): IS CP VIOLATION FORCED ON THE WEAVE? -- the weave's
generalized CP is the record swap; CP violation is allowed, not forced; P and CP have one origin on the weave (the
double-tick restriction); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.32 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_31_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_31 = "45875b5bbde3e70ddca6211caa141d8a647846d75380821a87081ec55ea8eab8"

CP = (" **[v1.32] CP ON THE WEAVE (main, B1611; sealed 43ec84e8b).** The weave's group G (the lifts of L and R on V = T ⊕ T̄, "
      "order 96) has 96 automorphisms (24 inner); 24 send the matter triplet T to T̄; 24 invert every conjugacy class, so G is "
      "not of type I; every irreducible of T ⊗ T and T ⊗ T̄ admits a consistent CP, and (post-seal) ten automorphisms are one "
      "consistent CP on every sector at once — among them conjugation by the swap's lift, with twisted Frobenius–Schur "
      "indicator +1 on T and on every sector. **So the weave's generalized CP is the record swap:** CP is a symmetry exactly "
      "when the swap is a move, and on the double-tick weave, where the three is chiral, it is not imposed — CP violation is "
      "allowed, not forced, and P and CP have one origin, the double-tick restriction. The weave's group fixes no CP phase: "
      "a phase can come only from couplings, which the weave does not yet force.")

CHANGES = [
 ("**Version 1.31 · 2026-10-08 · canonical.**", "**Version 1.32 · 2026-10-08 · canonical.**"),
 ("the same kind of choice as SE2.", "the same kind of choice as SE2." + CP),
 ("- **v1.31 · 2026-10-08 · main B1610.** The hands on the founding torsor.\n",
  "- **v1.32 · 2026-10-08 · main B1611.** CP on the weave.\n"
  "  - GM5c: the weave's group is not of type I; its generalized CP is the record swap (consistent on the matter triplet and every mass-term sector); CP is a symmetry exactly when the swap is a move — on the chiral double-tick weave CP violation is allowed, not forced; P and CP share one origin; no CP phase is fixed by the group.\n"
  "- **v1.31 · 2026-10-08 · main B1610.** The hands on the founding torsor.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_31, "the received v1.31 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.32 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.32, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
