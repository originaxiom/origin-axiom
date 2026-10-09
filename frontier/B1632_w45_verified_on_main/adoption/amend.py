#!/usr/bin/env python3
"""B1632 -- GENESIS v1.39 (main's, B1631) -> v1.40 (main's): the cusp's unit's payoff qualified -- the four-dimensional +-3
rests on the SM seat's W41 multiplier (main's own computation: the weave's lifts form only a projective representation, and
chi_{3/2} is 0 for that multiplier, 1 for another genuine one); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.40 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_39_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_39 = "5658f35e058bc746549a07a3904177c3391bee90fbdf9d65dc21448042cfd772"

ADD = (" **[v1.40] Qualified (B1632, main's own computation):** the weave's topological lifts on T form only a projective "
       "representation of Mp2(Z). Among its genuine rescalings χ_{3/2} is 0 for five and 1 for one, so W45's zero (and with it the "
       "±3 given the unit) holds for the multiplier the SM seat derived in W41 — the zero modes transforming by the topological "
       "action, T's exponents (⅛, ⅜, ⅞) — for which main reproduces χ_{3/2} = 0. W41's multiplier is registered, not yet "
       "verified on main; until it is, the payoff is \"given Λ, the unit and W41\".")
CHANGES = [
 ("**Version 1.39 · 2026-10-09 · canonical.**", "**Version 1.40 · 2026-10-09 · canonical.**"),
 ("audit lane derives an end mechanism at the cusp, or a forcing is found.",
  "audit lane derives an end mechanism at the cusp, or a forcing is found." + ADD),
 ("- **v1.39 · 2026-10-09 · main B1631.**",
  "- **v1.40 · 2026-10-09 · main B1632.** The unit's payoff qualified: it rests on W41's multiplier.\n"
  "  - Main's computation of W45: the lifts are projective; χ_{3/2} is 0 only for W41's multiplier among the genuine ones (one other gives 1). The ±3 is \"given Λ, the unit and W41\" until W41 is verified on main.\n"
  "- **v1.39 · 2026-10-09 · main B1631.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_39, "the received v1.39 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.40 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.40, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
