#!/usr/bin/env python3
"""B1492 -- GENESIS v1.17 (main's, B1491) -> v1.18 (main's): FK14 gains the first read of a companion -- on L8a15 (three
ends) and o10_150729 (five ends) every interior class at a sign character counts one, as on the one-cusped members; the
ends raise the floor's room and the value does not follow -- and GAP2's sharpened line gains the same fact.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.18 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_17_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_17 = "d483a41763a994a9d5d1c3f15e58a11d59f29666b4f0a28c15a8ab4a8467d45a"

CHANGES = [
 ("**Version 1.17 · 2026-10-07 · canonical.**", "**Version 1.18 · 2026-10-07 · canonical.**"),
 ("What is not derived: that the companion is a state the genesis generates (it is a cover chosen by a character), and any count on one |",
  "What is not derived: that the companion is a state the genesis generates (it is a cover chosen by a character), and any count on one. "
  "**[v1.18] The first read of a companion (B1492, sealed):** on L8a15 and on o10_150729, at every sign character of the four, every interior class "
  "reads (I(W₁), I(Λ²W₁)) = (−1, −1) with the class dead on every end — the count is one wherever it is not zero, on three ends and on five as on "
  "the one-cusped m135 and m136 (B1485), whatever the number of ends on which the character is trivial (the floor's room reaches three on the "
  "five-ended companion and the value stays one). On L8a15 no character trivial on any end has an interior class at all; its members sit where "
  "no end carries the character, as m136's do. In F-CI L8a15's order-3 isometries cycle the ends and fix no cusp, and its cusps are not hexagonal: "
  "no three (B1490's two conditions both fail). Evidence for the fork's second half — the ends raise the bound, not the value, at sign characters; "
  "not ruled: characters of order four and eight on the companions, where b0 = 0 and the bounds change shape, and non-unitary ones |"),
 ("  carries three generations in either frame, by counting ends, not by search.** The question is FK14.",
  "  carries three generations in either frame, by counting ends, not by search.** The question is FK14. **[v1.18] On the first several-ended\n"
  "  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value.**"),
 ("  - FK14: the seat's fixed-point companions registered as the first candidate answer to what adds an end (∣2 − tr φ∣ ends, one per fixed point of the act); two facts verified on main (o10_150729 = L10n113; +LLLR's three-ended companion L8a15). Not adopted: whether a companion is a generated state is the fork itself.",
  "  - FK14: the seat's fixed-point companions registered as the first candidate answer to what adds an end (∣2 − tr φ∣ ends, one per fixed point of the act); two facts verified on main (o10_150729 = L10n113; +LLLR's three-ended companion L8a15). Not adopted: whether a companion is a generated state is the fork itself.\n"
  "- **v1.18 · 2026-10-07 · main B1492.** The three-ended companion read.\n"
  "  - FK14 and GAP2: the harmonic frame read under seal on L8a15 (three ends) and o10_150729 (five ends) at every sign character — every interior class counts one, as on the one-cusped members; on L8a15 no character trivial on an end has a member; in F-CI no three (order-3 isometries fix no cusp; cusps not hexagonal). The ends raise the floor's room, not the value. Not ruled: characters of order four and eight, and non-unitary ones, on the companions."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_17, "the received v1.17 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.18 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.18, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
