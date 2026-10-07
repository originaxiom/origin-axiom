#!/usr/bin/env python3
"""B1494 -- GENESIS v1.19 (main's, B1493) -> v1.20 (main's): FK14 and GAP2 gain the mechanism -- the two supplies of a count,
the ends (the floor) and the room of the line (the cap), are separated on every companion and meet on N45; and the theorem
T-COMPANION-NO-ROOM (b1 = ends on every fixed-point companion: no closed surface, no room at the trivial line).

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.20 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_19_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_19 = "d7bf725aa7a30e8df2d254d0217242dda03c2dfb5408cd9da1b923c2582a4a05"

CHANGES = [
 ("**Version 1.19 · 2026-10-07 · canonical.**", "**Version 1.20 · 2026-10-07 · canonical.**"),
 ("Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines |",
  "Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines. "
  "**[v1.20] The mechanism (B1494, sealed):** a count needs two supplies at one character — ends on which the character is trivial and a class dies (the seat's floor) and a line with room (its cap, b0 + n(ν⁴)). **T-COMPANION-NO-ROOM:** every fixed-point companion has b₁ = |T| = ends (no closed surface), so its trivial line has no room — a theorem, its hypothesis h¹(M; χ) = 1 at every torsion character verified on all 758 own-level states to length twelve. But the room is not absent from the family: **m135's eight-ended companion has room 2 at eight sign characters** (verified by its 255 double covers) — every one trivial on no end, where the floor gives zero generations whatever the room, and where the four has no class to extend. On every companion read the two supplies exist and never meet; on N₄₅ (rebuilt on main: degree 45 over m003, b₁ = 9 over 5 ends, n(1) = 4) they meet at cusp-trivial room-3 characters and the count reaches two. **The search for three is the search for an object the genesis determines on which the ends and the room coincide at one character.** Which word states have three ends: |2 − tr φ| = 3 ⇔ tr φ = 5 ⇔ L³R, the only one; its companion L8a15 is chiral with S₃ on its ends |"),
 ("  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value. [v1.19] And at every character of order ≤ 8 the count at a member is exactly b0 + n(ν⁴) with n(ν⁴) = 0 (B1493): the generation is the trivial line; what reaches two on the record is a line with room on a cover chosen by a character.**",
  "  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value. [v1.19] And at every character of order ≤ 8 the count at a member is exactly b0 + n(ν⁴) with n(ν⁴) = 0 (B1493): the generation is the trivial line; what reaches two on the record is a line with room on a cover chosen by a character. [v1.20] The room is closed-surface homology (n(1) = b₁ − ends); no companion has any at the trivial line (T-COMPANION-NO-ROOM), one companion has it at eight sign characters trivial on no end (B1494) — the ends and the room are separated on the family and meet on N₄₅.**"),
 ("  - FK14 and GAP2: Theorem C's cap b0 + n(ν⁴) read on both companions — the line has no room at any sign character, so no character of order ≤ 8 carries three or two on either; every member read on L8a15 counts exactly −b0. What moves the count is the room of the line, which N₄₅ has and the companions do not. Not ruled: other orders, non-unitary characters, a line with room on an object the genesis determines.",
  "  - FK14 and GAP2: Theorem C's cap b0 + n(ν⁴) read on both companions — the line has no room at any sign character, so no character of order ≤ 8 carries three or two on either; every member read on L8a15 counts exactly −b0. What moves the count is the room of the line, which N₄₅ has and the companions do not. Not ruled: other orders, non-unitary characters, a line with room on an object the genesis determines.\n"
  "- **v1.20 · 2026-10-07 · main B1494.** No room on any companion, and one companion with room.\n"
  "  - FK14 and GAP2: T-COMPANION-NO-ROOM (b₁ = ends on every fixed-point companion; hypothesis verified on 758 states); m135's companion has room 2 at eight sign characters trivial on no end, where the floor gives zero; N₄₅ rebuilt on main (n(1) = 4). The two supplies of a count — ends and room — are separated on the family and meet on N₄₅; three needs an object the genesis determines on which they coincide. The only word state with three ends is L³R."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_19, "the received v1.19 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.20 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.20, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
