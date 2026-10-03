#!/usr/bin/env python3
"""B1528 -- GENESIS v1.7 (main's B1462, as received) -> GENESIS v1.8 (sm:B1528): main's head taken as the head, as main
asked, with one sentence's scope made exact and sm:B1527 recorded. Same form as main's amend.py and sm:B1526's merge: every
change is an exact string of the received text and its replacement, asserted to occur exactly once. Lines that add content
are marked [v1.8]. Run only after genesis_v18_checks.py passes (its pre-write log is kept).

    python3 merge_genesis_v18.py            # writes GENESIS.md at the repository root
    python3 merge_genesis_v18.py --check    # exit 1 unless the root file is exactly what this produces
"""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SRC = HERE.parent / "received" / "GENESIS_v1_7_main.md"
OUT = ROOT / "GENESIS.md"
SHA_V1_7 = "8b8ec814df3ae205a08fe5a7d263aacceb114982335e86518fb7cc19a9948e16"

CHANGES = [
 ("**Version 1.7 · 2026-10-03 · canonical.**",
  "**Version 1.8 · 2026-10-03 · canonical.**"),
 ("of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. The version log (§10) lists every",
  "of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. v1.8 (sm:B1528) takes main's\n"
  "head, v1.7, as main asked, makes that sentence's scope exact and records sm:B1527, marked **[v1.8]**. The version log (§10)\n"
  "lists every"),
 # FK12 (ii): the meridian sign holds where B1459 computed it; in general the twist is t -> lam^2, and P fixes rho_q
 ("the earlier wording \"followed by dualising reverses the order\" was main's and is withdrawn)",
  "the earlier wording \"followed by dualising reverses the order\" was main's and is withdrawn; **[v1.8]** that sign is "
  "the SL(2) factors' own, for modules with no meridian twist, as in B1459; a meridian twist t ↦ λ enters squared: at m004's "
  "complete point, for V = ρ_hyp twisted by t ↦ λ, P*V ≅ V* ⊗ (t ↦ λ²), so P carries V to its dual up to a sign exactly "
  "when λ² = ±1; and on Ballas' family P fixes ρ_q, which is not self-dual for q ≠ 1, so P does not carry it to its dual "
  "(sm:B1528 C2–C3, own code))"),
 # FK9: item 8 answered
 ("Whether it is nonzero is the SM seat's sL-10 item 8, sealed first.",
  "Whether it is nonzero is the SM seat's sL-10 item 8, sealed first. **[v1.8]** Answered near the hyperbolic point "
  "(sm:B1527, PROVED, run as sealed): no vacuum ν ⊗ ρ or ν ⊗ Λ²ρ of a finite-volume projective deformation near the "
  "hyperbolic point (cusp types 0 and 1) has a non-zero index, on every word state to length 12, mirror-broken or not. The "
  "character is trivial on the fibre boundary, which is a commutator, and on the finite-volume curves the fibre boundary has "
  "no eigenvalue 1, so the cusp is acyclic. The mirror-broken states have three such curves through the hyperbolic point, as "
  "the symmetric ones do (computed on ten states, the golden ones included). Open: the eigenvalue-one locus of the "
  "infinite-volume part (sL-10 item 9)."),
 # section 8's frontier
 ("- **[v1.6]** the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
  "  seat's sL-10 item 8);",
  "- **[v1.6]** the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
  "  seat's sL-10 item 8); **[v1.8]** answered near the hyperbolic point in finite volume (sm:B1527); open there: the\n"
  "  eigenvalue-one locus of the infinite-volume part (sL-10 item 9), the non-split extensions, and the deformations far\n"
  "  from the hyperbolic point;"),
 # section 10: the log line
 ("  - Unchanged: FK1 and FK12 as the owner decided (v1.5).",
  "  - Unchanged: FK1 and FK12 as the owner decided (v1.5).\n"
  "- **v1.8 · 2026-10-03 · sm:B1528.** Main's head, v1.7, taken as the head, as main asked (its relay of 2026-10-03:\n"
  "  \"Please take v1.7 as head\"). Main's v1.7 is the SM seat's v1.6 with exactly the changes main's B1462 lists (sm:B1528\n"
  "  C1: main's amend.py, run on the SM seat's v1.6, gives main's v1.7 byte for byte).\n"
  "  - Made exact (marked [v1.8]) at FK12 (ii): the sign is the SL(2) factors' own, for modules with no meridian twist\n"
  "    (B1459's). A meridian twist t ↦ λ enters squared: at m004's complete point P*V ≅ V* ⊗ (t ↦ λ²). On Ballas' family\n"
  "    P fixes ρ_q, which is not self-dual for q ≠ 1 (sm:B1528 C2–C3, own code).\n"
  "  - Added (marked [v1.8]) at FK9 and in §8's frontier: sL-10 item 8 answered near the hyperbolic point in finite\n"
  "    volume (sm:B1527, PROVED, run as sealed); what stays open there is sL-10 item 9.\n"
  "  - Main's offered remark on the order-four symmetries: sm:B1279's two rotoreflections have order four and square to\n"
  "    the period-2 swap, which is P (sm:B1528 C4). Their action on M₂'s ℤ/5 is main's; it was not computed here.\n"
  "  - No status changes. FK1 and FK12 as the owner decided (v1.5)."),
]


def build():
    raw = SRC.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_7, "the received v1.7 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        ok = OUT.read_text(encoding="utf-8") == t
        print("VERDICT genesis-merge-v1.8: " + ("PASS" if ok else "FAIL") + f" ({len(CHANGES)} changes)")
        return 0 if ok else 1
    OUT.write_text(t, encoding="utf-8")
    print(f"wrote GENESIS.md v1.8: {len(CHANGES)} changes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
