#!/usr/bin/env python3
"""B1629 -- GENESIS v1.37 (main's, B1627) -> v1.38 (main's): FK10 sharpened -- nothing the principle forces visits the weave's
cusp, so a unit of end data there is not dynamical; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.38 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_37_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_37 = "5f58fda05ede5cc987d1e0553b65b748a67707164445590252ce14e266349cca"

ADD = (" **[v1.38] Sharpened (B1629): nothing the principle forces visits the weave's cusp.** The tick LR is the unique lowest "
       "closed geodesic of the weave (top √5/2; the next is √2, B482's Markov values); the clock's word, read as moves, stays "
       "below height 2.3; under the weave's uniform measure the fraction of letters in a run of length ≥ k, the time spent "
       "deep in the cusp, is (k+1)/2^k at every length, with no atom. So the unit of end data that W45 and W46 need for a chiral "
       "three is not dynamical: if it is forced, it is forced as a boundary datum, by a physical end mechanism or a postulate.")
CHANGES = [
 ("**Version 1.37 · 2026-10-09 · canonical.**", "**Version 1.37 · 2026-10-09 · canonical.**".replace("1.37", "1.38")),
 ("the weave's cusp (the SM seat's W45, W46)?", "the weave's cusp (the SM seat's W45, W46)?" + ADD),
 ("- **v1.37 · 2026-10-09 · main B1627.**",
  "- **v1.38 · 2026-10-09 · main B1629.** FK10 sharpened: nothing the principle forces visits the weave's cusp.\n"
  "  - The tick is the unique lowest closed geodesic (√5/2); the weave's measure has no atom at the cusp ((k+1)/2^k in runs ≥ k); the cusp's unit, if forced, is a boundary datum.\n"
  "- **v1.37 · 2026-10-09 · main B1627.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_37, "the received v1.37 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.38 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.38, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
