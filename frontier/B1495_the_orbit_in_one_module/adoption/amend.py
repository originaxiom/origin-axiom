#!/usr/bin/env python3
"""B1495 -- GENESIS v1.20 (main's, B1494) -> v1.21 (main's): FK14 gains the orbit read as one module -- (10', 5bar') = (3, 9),
the cross terms between generations at -2 each -- so the orbit reading survives on the 10' side only and stays a selection.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.21 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_20_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_20 = "06c47e8eaadfe783fb07efb6afb81033b1986b1ca48b8b6cd7bc4bf67d6a159b"

CHANGES = [
 ("**Version 1.20 · 2026-10-07 · canonical.**", "**Version 1.21 · 2026-10-07 · canonical.**"),
 ("Which word states have three ends: |2 − tr φ| = 3 ⇔ tr φ = 5 ⇔ L³R, the only one; its companion L8a15 is chiral with S₃ on its ends |",
  "Which word states have three ends: |2 − tr φ| = 3 ⇔ tr φ = 5 ⇔ L³R, the only one; its companion L8a15 is chiral with S₃ on its ends. **[v1.21] The orbit as one module (B1495, sealed; the SM seat's three-orbit: L8a15's three members are one orbit of the deck ℤ/3, verified):** the direct sum of the three members' extensions reads (10′, 5̄′) = (3, 9) in the seat's dictionary — the three cross terms between generations are −2 each, carried around the ends by the deck, one from each generation's class seen through another's four — so the reading \"three generations = the deck orbit of a member\" survives on the 10′ side only and stays a selection; a glued module and the two deck-fixed spin structures are not ruled |"),
 ("  - FK14 and GAP2: T-COMPANION-NO-ROOM (b₁ = ends on every fixed-point companion; hypothesis verified on 758 states); m135's companion has room 2 at eight sign characters trivial on no end, where the floor gives zero; N₄₅ rebuilt on main (n(1) = 4). The two supplies of a count — ends and room — are separated on the family and meet on N₄₅; three needs an object the genesis determines on which they coincide. The only word state with three ends is L³R.",
  "  - FK14 and GAP2: T-COMPANION-NO-ROOM (b₁ = ends on every fixed-point companion; hypothesis verified on 758 states); m135's companion has room 2 at eight sign characters trivial on no end, where the floor gives zero; N₄₅ rebuilt on main (n(1) = 4). The two supplies of a count — ends and room — are separated on the family and meet on N₄₅; three needs an object the genesis determines on which they coincide. The only word state with three ends is L³R.\n"
  "- **v1.21 · 2026-10-07 · main B1495.** The orbit in one module.\n"
  "  - FK14: L8a15's three members as one rank-15 module read (10′, 5̄′) = (3, 9); the cross terms −2 each (each generation's class through another's four); the orbit reading survives on the 10′ side only, a selection; a glued module and the deck-fixed spin structures not ruled."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_20, "the received v1.20 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.21 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.21, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
