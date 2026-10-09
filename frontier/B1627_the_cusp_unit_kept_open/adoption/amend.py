#!/usr/bin/env python3
"""B1627 -- GENESIS v1.36 (main's, B1625) -> v1.37 (main's): the SM seat's W45 and W46 registered together under FK11 with the
seat's scope sentence, and the owner's ruling of 2026-10-09 on FK10 (keep it open; relayed by the SM seat); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.37 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_36_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_36 = "b175ee644f31f25942f81eb9e479f312dec20c4f1c528d82a2d47ccfeb10e73c"

W46 = (" **[v1.37] W45 and W46 together (the SM seat, registered, not re-run on main):** given Λ, on M₁,₂, for every end "
       "condition the moves keep, the triplet's four-dimensional index is n times the fibre's index, where n is the cusp's "
       "units; the natural cusp condition gives n = 0. So on the weave's own surface FK11's earning condition is FK10's question "
       "at the cusp.")
FK10 = (" **[v1.37] The owner's ruling of 2026-10-09 (relayed by the SM seat, its relay §49): keep FK10 open.** No postulate is "
        "added for the unit of end data at the weave's cusp; results stay \"given Λ\"; revisit when a forcing is found or a "
        "physical end mechanism at the cusp is derived. The question carried: does the principle force one unit of end data at "
        "the weave's cusp (the SM seat's W45, W46)?")
CHANGES = [
 ("**Version 1.36 · 2026-10-09 · canonical.**", "**Version 1.37 · 2026-10-09 · canonical.**"),
 ("which is FK10's question. So FK11's earning condition is not met there in the canonical reading.",
  "which is FK10's question. So FK11's earning condition is not met there in the canonical reading." + W46),
 ("| FK10 | The end law | OPEN | an end condition derived from physics (sL-8) |",
  "| FK10 | The end law | OPEN" + FK10 + " | an end condition derived from physics (sL-8) |"),
 ("- **v1.36 · 2026-10-09 · main B1625.**",
  "- **v1.37 · 2026-10-09 · main B1627.** W45 and W46 under FK11; the owner's FK10 ruling recorded.\n"
  "  - The SM seat's W46: the four-dimensional index on M₁,₂ is n times the fibre's index (n the cusp's units; natural condition n = 0). The owner's ruling of 2026-10-09, relayed: keep FK10 open, no postulate for the cusp's unit.\n"
  "- **v1.36 · 2026-10-09 · main B1625.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_36, "the received v1.36 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.37 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.37, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
