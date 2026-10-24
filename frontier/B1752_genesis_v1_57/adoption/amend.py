#!/usr/bin/env python3
"""B1752 -- GENESIS v1.56 (main's) -> v1.57 (main's): the ladder's rule's first clause corrected at the web seat's opinion
(P-379), under the owner's ruling that the seats still to answer could amend it: the end at 5 follows from the moves'
orders (W153); the adopted step is E₈ as the single container of the rungs.  Every status cell unchanged.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.57 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_56_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_56 = "28b0683cf03c82c3ff31a0acfd9f49324094b7466938498a1875b531d35cdd29"
CHANGES = [
 ("**Version 1.56 · 2026-10-24 · canonical.**", "**Version 1.57 · 2026-10-24 · canonical.**"),
 ("every finite rung of the moves' ladder at once, so E₈ and the prime 5 — adopted by the rule, not derived (the forced "
  "structures use 2 and 3, W153); the rule fixes the algebra, not its embedding or its fields (FK11)",
  "every finite rung of the moves' ladder at once — the end at 5 follows from the moves' orders 2 and 3 (W153), and E₈ "
  "as the single container of the rungs is adopted by the ruling, not derived ([v1.57] the web seat's correction of "
  "main's clause, P-379: the rungs' groups form no chain, so the container is a choice of rule); the rule fixes the "
  "algebra, not its embedding or its fields (FK11)"),
 ("- **v1.56 · 2026-10-24 · main B1751.**",
  "- **v1.57 · 2026-10-24 · main B1752.** The ladder's rule's first clause corrected at the web seat's opinion (P-379): "
  "the end at 5 follows from the moves' orders; E₈ as the container is the ruling's adoption. No status cell changes; the "
  "v1.56 entry below is not rewritten.\n"
  "- **v1.56 · 2026-10-24 · main B1751.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_56, "the received v1.56 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.57 · 2026-10-24 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written (v1.57)")
