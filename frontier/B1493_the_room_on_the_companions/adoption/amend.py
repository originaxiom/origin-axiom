#!/usr/bin/env python3
"""B1493 -- GENESIS v1.18 (main's, B1492) -> v1.19 (main's): FK14 and GAP2 gain the room -- Theorem C's cap read on both
companions: the line has no room there, so no character of order <= 8 carries three or two, and what moves the count on the
record is the room of the line, which a cover chosen by a character (N45) has and the companions do not.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.19 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_18_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_18 = "6c223302f5786aeff06b922deea7fd46bcef6d4a59070ef437823d3443e660d3"

CHANGES = [
 ("**Version 1.18 · 2026-10-07 · canonical.**", "**Version 1.19 · 2026-10-07 · canonical.**"),
 ("not ruled: characters of order four and eight on the companions, where b0 = 0 and the bounds change shape, and non-unitary ones |",
  "not ruled: characters of order four and eight on the companions, where b0 = 0 and the bounds change shape, and non-unitary ones. "
  "**[v1.19] The room (B1493, sealed; a scoped NEGATIVE):** the SM seat's Theorem C (sm:B1535) caps the count at a finite-order character by b0 + n(ν⁴), the room of the line L = ν⁻⁴, and by n(ν³ ⊗ four). On both companions the line has no room — n(ν⁴) = 0 at every sign character of L8a15 and of o10_150729 — so at order eight the cap is 0 and at order four or two it is 1: **no character of order ≤ 8 on either companion carries three generations, or two**; read directly on L8a15 at every order, every member counts exactly −b0 (sign (−1, −1); order four (−1, 0); order eight (0, 0)) — the generation is the trivial line and nothing else. What moves the count on the record is the room of the line: N₄₅ (the seat's golden cover: degree 45 over m003, the 5-fold cyclic cover of a degree-9 cover along a character; H₁ = ℤ⁹ ⊕ (ℤ/2)²) has room 3 and reaches two (sm:B1547); the companions the state determines have none. Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines |"),
 ("  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value.**",
  "  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value. [v1.19] And at every character of order ≤ 8 the count at a member is exactly b0 + n(ν⁴) with n(ν⁴) = 0 (B1493): the generation is the trivial line; what reaches two on the record is a line with room on a cover chosen by a character.**"),
 ("  - FK14 and GAP2: the harmonic frame read under seal on L8a15 (three ends) and o10_150729 (five ends) at every sign character — every interior class counts one, as on the one-cusped members; on L8a15 no character trivial on an end has a member; in F-CI no three (order-3 isometries fix no cusp; cusps not hexagonal). The ends raise the floor's room, not the value. Not ruled: characters of order four and eight, and non-unitary ones, on the companions.",
  "  - FK14 and GAP2: the harmonic frame read under seal on L8a15 (three ends) and o10_150729 (five ends) at every sign character — every interior class counts one, as on the one-cusped members; on L8a15 no character trivial on an end has a member; in F-CI no three (order-3 isometries fix no cusp; cusps not hexagonal). The ends raise the floor's room, not the value. Not ruled: characters of order four and eight, and non-unitary ones, on the companions.\n"
  "- **v1.19 · 2026-10-07 · main B1493.** The room on the companions.\n"
  "  - FK14 and GAP2: Theorem C's cap b0 + n(ν⁴) read on both companions — the line has no room at any sign character, so no character of order ≤ 8 carries three or two on either; every member read on L8a15 counts exactly −b0. What moves the count is the room of the line, which N₄₅ has and the companions do not. Not ruled: other orders, non-unitary characters, a line with room on an object the genesis determines."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_18, "the received v1.18 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.19 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.19, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
