#!/usr/bin/env python3
"""B1625 -- GENESIS v1.35 (main's, B1620) -> v1.36 (main's): the SM seat's corrections to B1620 taken (TM1 under T-bar(x)T only,
TM2 under T(x)T; the frame named; the 13 unreduced in every frame on record, W44), and the seat's W45 recorded against
FK11's earning condition (the triplet's index on the weave's own surface is 0 in the canonical reading); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.36 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_35_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_35 = "6b2112ffa8fcbdb0316e5a0d10f18ad90e298772e2a6a6bc57c8286b4d730072"

FIX = (" **[v1.36] Corrected (B1625, the SM seat's W43 and W44):** the sentence above names the type and the frame wrongly. In "
       "B1620's frame (all of the weave's group is flavour) the PMNS reduces to two parameters as TM1 or TM2 under T̄ ⊗ T, as "
       "TM2 only under T ⊗ T (sin²θ₁₂ = 1/(3 cos²θ₁₃)), and not at all under Sym² T; P10 (TM1) applies under T̄ ⊗ T. Where c is "
       "gauge (W44), TM1 and TM2 are allowed under T̄ ⊗ T and T ⊗ T, and Sym² T allows one relation (a fixed entry 1/√2 or ½). "
       "In W24's frame only c is flavour and nothing is constrained. The CKM needs a four-dimensional family in every frame on "
       "record, so the weave's symmetry reduces none of the 13 without a frame.")
FK11 = (" **[v1.36] The weave's own surface, read (the SM seat's W45, given Λ, registered):** the four-dimensional Dirac operator "
        "on M₁,₂ twisted by the weave's bundle, with the odd spin structure, at the weight 3/2 the geometry forces and the "
        "canonical condition at the cusp, has index 0 for both hands; on that object a chiral three is exactly one unit of end "
        "data at the cusp, which is FK10's question. So FK11's earning condition is not met there in the canonical reading.")
CHANGES = [
 ("**Version 1.35 · 2026-10-08 · canonical.**", "**Version 1.35 · 2026-10-08 · canonical.**".replace("1.35 · 2026-10-08", "1.36 · 2026-10-09")),
 ("not at all under Sym² T. With couplings in τ alone every residual", "not at all under Sym² T." + FIX + " With couplings in τ alone every residual"),
 ("or an even-dimensional object of the weave with a non-flat bundle |", "or an even-dimensional object of the weave with a non-flat bundle." + FK11 + " |"),
 ("- **v1.35 · 2026-10-08 · main B1620.**",
  "- **v1.36 · 2026-10-09 · main B1625.** B1620's lepton sentence corrected; the weave's own surface read against FK11.\n"
  "  - The SM seat's W43 and W44 taken: TM1 under T̄ ⊗ T only, TM2 under T ⊗ T, the frame named, the 13 unreduced in every frame on record. W45 registered under FK11: the index on M₁,₂ is 0 in the canonical reading; a chiral three there is one unit of end data at the cusp (FK10).\n"
  "- **v1.35 · 2026-10-08 · main B1620.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_35, "the received v1.35 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.36 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.36, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
