#!/usr/bin/env python3
"""B1751 -- GENESIS v1.55 (main's) -> v1.56 (main's), at the owner's rulings of 2026-10-24: FK9's looks counted jointly
across seats (P-367; docs/LOOK_LEDGER.md), and the ladder's rule R1 recorded at F-MC (P-375; docs/THE_WEAVE.md).  The
version log's own lines are not rewritten; every status cell is unchanged.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.56 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_55_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_55 = "eca8f6845f2d6af5ac4ce0e2009223854bfc83602ea52f8e5e1df8dd09df59db"
CHANGES = [
 ("**Version 1.55 · 2026-10-24 · canonical.**", "**Version 1.56 · 2026-10-24 · canonical.**"),
 ("and its uniqueness premise is scoped by the audit lane (P-107). |",
  "and its uniqueness premise is scoped by the audit lane (P-107). **[v1.56] (the owner's ruling, 2026-10-24, P-367; "
  "B1751)** The looks are counted jointly across seats: every seat's search of the same frame against the same data is one "
  "look in `docs/LOOK_LEDGER.md`, and THE_BAR's correction counts them all. |"),
 ("1)]/ℤ₆ and the hypercharge direction | main: B248, B266",
  "1)]/ℤ₆ and the hypercharge direction. **[v1.56]** The ladder's rule R1 (the owner's ruling, 2026-10-24, P-375; "
  "`docs/THE_WEAVE.md`): every finite rung of the moves' ladder at once, so E₈ and the prime 5 — adopted by the rule, not "
  "derived (the forced structures use 2 and 3, W153); the rule fixes the algebra, not its embedding or its fields (FK11) "
  "| main: B248, B266"),
 ("- **v1.55 · 2026-10-24 · main B1750.**",
  "- **v1.56 · 2026-10-24 · main B1751.** The owner's rulings of the evening: FK9's looks counted jointly across seats "
  "(the look ledger, P-367); the ladder's rule R1 recorded at F-MC with its two clauses (P-375). No status cell changes; the "
  "v1.55 entry below is not rewritten.\n"
  "- **v1.55 · 2026-10-24 · main B1750.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_55, "the received v1.55 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.56 · 2026-10-24 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written (v1.56)")
