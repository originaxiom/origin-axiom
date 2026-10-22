#!/usr/bin/env python3
"""B1721 -- GENESIS v1.53 (main's) -> v1.54 (main's): v1.53's three overreaches corrected, found by main's math referee in
the integrity sweep of 2026-10-22 (P-291): FK10's string count and its condition; FK9's W57 sentence tagged as the seat's,
unverified on main; FK12's CP sentence held to what its sources say.  The version log's own lines are not rewritten.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.54 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_53_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_53 = "bbc17bdd570d4122ac507c72f132bcd3b0c7ae48ca3f734298d28221cd71e4cb"
CHANGES = [
 ("**Version 1.53 · 2026-10-22 · canonical.**", "**Version 1.54 · 2026-10-22 · canonical.**"),
 ("The closed torus-fibred 4d vacua over the weave's "
  "τ-line close at 12 or 24 strings, and the moves' ℤ/12 makes their units of end data a multiple of twelve. The triplet "
  "lives only where χ(O_S) is even (K3 the least), and its count there is −15χ(O_S) or −18χ(O_S) (−30 and −36 on K3), never three.",
  "The closed torus-fibred 4d vacua over the weave's "
  "τ-line close at 12χ(O_S) strings [v1.54: 12, 24, 36, …; v1.53 said 12 or 24], so their units of end data come in "
  "multiples of twelve. The triplet lives only where χ(O_S) is even (K3 the least), and its count there is −15χ(O_S) or "
  "−18χ(O_S) (−30 and −36 on K3), never three [v1.54: given the SM seat's reduction of the 4d Dirac index to Riemann–Roch "
  "on the base, which main did not re-derive (B1710)]."),
 ("The seat's own test of "
  "the seed's invariant measure (W57) found no draw within 32σ of the ten numbers,",
  "The seat's own test of "
  "the seed's invariant measure (W57) found no draw within 32σ of the ten numbers [the seat's, unverified on main: row "
  "1099, P-091; v1.54],"),
 ("so the word's order is "
  "where a CP sign is chosen: a convention between CP-conjugate vacua, CP broken vacuum by vacuum.",
  "so the word's order is "
  "where a CP sign would have to be chosen (P-149). That the choice is a convention between CP-conjugate vacua, CP broken "
  "vacuum by vacuum, is the web seat's reading [post hoc in B1652's addendum; v1.54]. Whether any potential on record has "
  "a minimum with J ≠ 0 is open (P-277)."),
 ("- **v1.53 · 2026-10-22 · main B1715.**",
  "- **v1.54 · 2026-10-22 · main B1721.** v1.53's three overreaches corrected, found by main's math referee (P-291):\n"
  "  - FK10: the closed 4d vacua close at 12χ(O_S) strings, not \"12 or 24\", and the triplet's count is given the SM seat's "
  "Leray reduction (B1710).\n"
  "  - FK9: W57's sentence tagged as the seat's, unverified on main.\n"
  "  - FK12: the CP sign \"would have to be chosen\"; the conjugate-vacua reading is the web seat's; P-277 is open.\n"
  "  - The v1.53 entry below is not rewritten.\n"
  "- **v1.53 · 2026-10-22 · main B1715.**"),
]
def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_53, "the received v1.53 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out
if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("Version 1.54" in cur[:400] and cur != text) else 0)
    open(OUT, "w", encoding="utf-8").write(text); print("GENESIS.md written at v1.54")
