#!/usr/bin/env python3
"""B1480 -- GENESIS v1.12 (main's, B1478) -> v1.13 (main's): fork FK13 ruled by the principle, FK4 restated with its
stake (B1479), at the owner's word of 2026-10-07 that such forks are settled by the mathematics and the evidence.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.13 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_12_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_12 = "b60767ce8a542ed54c2ff6904942ec6c98de90f03c3db397b1918905f1374d31"

CHANGES = [
 ("**Version 1.12 · 2026-10-06 · canonical.**", "**Version 1.13 · 2026-10-07 · canonical.**"),
 ("Which set the owner's rule of 2026-10-04 means is fork FK13 (§8); main does not rule on it.",
  "Which set the owner's rule of 2026-10-04 means was fork FK13 (§8); **[v1.13]** it is ruled by the principle: the word states."),
 ("| FK4 | Inverse moves (GM5b) | OPEN | operational legality; until then the signed states are an extension of the grammar |",
  "| FK4 | Inverse moves (GM5b) | OPEN | operational legality; until then the signed states are an extension of the grammar. **[v1.13] Its stake (B1479):** the sign − of a word state is the monodromy with the fibre's elliptic involution, −I = (L·R⁻¹·L)², which needs an inverse letter; and on every amphichiral word to length 12 the − state is the one on which no spin structure survives the mirror (rhombic cusp, Chern–Simons class ¼), the + state the one on which nothing at the cusp forbids it. So FK4 now reads: **does the principle generate the sign?** If it does, the place where a hand can be registered on a fermion emerges; if not, it is an added choice |"),
 ("| FK13 **[v1.12]** | Which set \"the family as object\" names (the owner's rule of 2026-10-04) | OPEN — the owner's | the owner's word: X_gen (§3's word states, the web seat's reading), m004's commensurability class, or B1186's 112 (the set main's B1474–B1477 computed on). Until then every statement names its set (§6) |",
  "| FK13 **[v1.12]** | Which set \"the family as object\" names (the owner's rule of 2026-10-04) | **[v1.13] RULED BY THE PRINCIPLE** (main B1480; the owner, 2026-10-07: \"it's not up to me, it should be up to math, to the principle of emergence\") | the family that emerges is the one the principle generates: the word states X_gen (§1 → §2 → §3). m004's commensurability class and B1186's 112 are named lists drawn by an outside relation; statements about them stay true as statements about those lists (§6). Revisable by a better argument, not by preference |"),
 ("  - The web seat has its own branch from this date (`chat1/web-seat`); its relays are rowed and its pin set in B1478.",
  "  - The web seat has its own branch from this date (`chat1/web-seat`); its relays are rowed and its pin set in B1478.\n"
  "- **v1.13 · 2026-10-07 · main B1480.** One fork ruled, one restated.\n"
  "  - FK13 ruled by the principle: the family is the generated state space, the word states. The owner declined to decide\n"
  "    it by preference and asked that such forks be settled by the mathematics and the evidence.\n"
  "  - FK4 carries a stake: the sign of a word state needs an inverse letter and is the fermionic bit (B1479, with B1477's\n"
  "    Theorem A). Whether the principle generates the sign is the question.\n"
  "  - Recorded from B1480: at own level the class index does not follow the sign — it fires on both; the count and the\n"
  "    bit are independent there, and the next cell is the index under the mirror's swap of spin structures."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_12, "the received v1.12 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.13 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.13, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
