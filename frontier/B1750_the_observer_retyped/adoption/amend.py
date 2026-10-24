#!/usr/bin/env python3
"""B1750 -- GENESIS v1.54 (main's) -> v1.55 (main's), at the owner's ruling of 2026-10-24 (P-372): the observer re-typed.
Of the three senses the record gives the word, the closer is retired as an explanatory move, the signer kept (a unit and an
orientation; the frame's mirror maps J to -J), the identifier made the identification ledger (FK11).  The version log's
own lines are not rewritten; every status cell is unchanged.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.55 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_54_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_54 = "6073241a0d0ebd7d45cd81ee786ff9b8308c1a965cd766d2d5b9db0e15d61e05"
CHANGES = [
 ("**Version 1.54 · 2026-10-22 · canonical.**", "**Version 1.55 · 2026-10-24 · canonical.**"),
 ("choice\" (B717, with B716 and B723). **[v1.9]**",
  "choice\" (B717, with B716 and B723). **[v1.55] The observer re-typed** (the owner's ruling, 2026-10-24, P-372; B1750). "
  "The record gives the word three senses, sorted by one test (the SM seat's): a choice is a convention when the joint "
  "action's symmetry carries every option to every other; otherwise it is forced or a free number counted against the "
  "19. **The closer** — every closing above — is retired as an explanatory move: the arrow is forced (the walk's escape, "
  "B1083, B1662); that the index is chiral is forced, which sheet is left a convention; the basepoint is a convention "
  "with free ratios of scales; the filling slope is open information (FK10); in B1656's frame the end L, τ and the flat "
  "line, the readings S/S̃ and the Higgs's direction are each forced, a dynamical selection (THE WEAVE's rule on "
  "spontaneous breaking, adopted 2026-10-24), a relation (B1327) or a counted free number. FK12 keeps the question of "
  "experience only. **The signer** stands (B1183, B1184; B1168): the observer supplies one unit (the "
  "frame emits only dimensionless ratios) and one orientation (the frame's mirror τ ↦ −τ̄, b ↦ −b maps every mass ratio "
  "and CKM modulus to itself and J to −J, B1750 §3) — conventions, not values. **The identifier** is the identification "
  "ledger (FK11): every identification of a frame object with a Standard Model one (S̃ ↔ H̃, the channels ↔ the sectors, "
  "the hypercharge twists, the comparison scale) is an input, earned or priced (B1750's table). **[v1.9]**"),
 ("- **v1.54 · 2026-10-22 · main B1721.**",
  "- **v1.55 · 2026-10-24 · main B1750.** The observer re-typed at the owner's ruling (P-372): the closer retired as an "
  "explanatory move, the signer kept (a unit and an orientation; the frame's mirror maps J to −J, checked on main), the "
  "identifier made the identification ledger (FK11); B1750's table types every ingredient of B1656's frame. No status "
  "cell changes; the v1.54 entry below is not rewritten.\n"
  "- **v1.54 · 2026-10-22 · main B1721.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_54, "the received v1.54 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.55 · 2026-10-24 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written (v1.55)")
