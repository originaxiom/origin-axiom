#!/usr/bin/env python3
"""B1631 -- GENESIS v1.38 (main's, B1629) -> v1.39 (main's): the owner's decision of 2026-10-09, made directly to main and
superseding the relayed 'keep FK10 open': the one unit of end data at the weave's cusp is a TAGGED WORKING POSTULATE; the
version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.39 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_38_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_38 = "961a80617efb6dff81b2174f382c41495c8acbb91574f10e9258f6fcc0f6bfe7"

ADD = (" **[v1.39] THE CUSP'S UNIT, A TAGGED WORKING POSTULATE (the owner's decision of 2026-10-09, made directly to main; it "
       "supersedes the relayed 'keep FK10 open').** One unit of end data at the weave's cusp is adopted as a working postulate, "
       "as Λ is: results that use it carry \"given the unit\". By the SM seat's W46, it gives the weave's own surface M₁,₂ a "
       "four-dimensional index of ±3 at the natural puncture conditions (±1 at the middle ones). So, given Λ and the unit, the "
       "chiral three is an index, and FK11's earning condition is met conditionally. The three is not chosen (it is dim T); only "
       "the unit's existence is postulated, and B1629 shows it cannot be supplied by the principle's dynamics. Revisit when the "
       "audit lane derives an end mechanism at the cusp, or a forcing is found.")
CHANGES = [
 ("**Version 1.38 · 2026-10-09 · canonical.**", "**Version 1.39 · 2026-10-09 · canonical.**"),
 ("if it is forced, it is forced as a boundary datum, by a physical end mechanism or a postulate.",
  "if it is forced, it is forced as a boundary datum, by a physical end mechanism or a postulate." + ADD),
 ("- **v1.38 · 2026-10-09 · main B1629.**",
  "- **v1.39 · 2026-10-09 · main B1631.** The cusp's unit, a tagged working postulate (the owner, directly).\n"
  "  - Results that use it carry \"given the unit\"; with W46 the weave's surface gives a four-dimensional index ±3, given Λ and the unit. It supersedes the relayed 'keep FK10 open'.\n"
  "- **v1.38 · 2026-10-09 · main B1629.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_38, "the received v1.38 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.39 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.39, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
