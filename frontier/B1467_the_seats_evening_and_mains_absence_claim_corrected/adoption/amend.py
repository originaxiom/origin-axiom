#!/usr/bin/env python3
"""B1467 -- GENESIS v1.9 (main's, B1466) -> GENESIS v1.10 (main's): the SM seat's exact sentence on the meridian twist
(sm:B1528, its "v1.8", a number main had already used), and lead L17 named where L244 claimed an absence.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.10 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_9_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_9 = "7eb2df0fee9e32c638b6c872bb4ec07a1f8b93d96c3038153d75508752b5eca2"

CHANGES = [
 ("**Version 1.9 · 2026-10-03 · canonical.**", "**Version 1.10 · 2026-10-03 · canonical.**"),
 ("to an axis — a quantity on no report.",
  "to an axis — a quantity on no report. **[v1.10]** Exact, from the SM seat's sm:B1528 (its own code at m004's complete point): "
  "for modules with no meridian twist the sign is the SL(2) factors' own, as in B1459; a meridian twist t ↦ λ enters squared, "
  "P*V ≅ V* ⊗ (t ↦ λ²), so P carries V to its dual up to a sign exactly when λ² = ±1 — main's B1465 computed the twisted indices "
  "zero on four states regardless. On Ballas' family P fixes ρ_q, which is not self-dual for q ≠ 1."),
 ("    B128, B849, B1327 and FK12 already state it).",
  "    B128, B849, B1327 and FK12 already state it).\n"
  "- **v1.10 · 2026-10-03 · main B1467.** Two corrections, no status change.\n"
  "  - FK12 (ii) made exact on the meridian twist (sm:B1528, read and consistent with main's B1465). **A version-number\n"
  "    collision is recorded:** the SM seat's arc of this content calls itself GENESIS v1.8, made on main's v1.7 in parallel\n"
  "    with main's v1.8 (B1463); main's line is v1.8 (B1463), v1.9 (B1466), v1.10 (this); the seat's v1.8 is received in B1467.\n"
  "  - L244's sweep corrected: 'symmetric phase' is on main — lead **L17** (\"Symmetric-phase exclusion / quantized breaking\",\n"
  "    is the commuting locus empty rather than unstable), B849's seal, B853's script — found by the SM seat's sm:B1531 and\n"
  "    confirmed by grep; main's tool reads verdict lines and titles and had been cited beyond its domain. The reading's\n"
  "    three kinds cover 14 of the chirality chain's 26 negatives (sm:B1531, read): the taxonomy is incomplete."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_9, "the received v1.9 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.10 ·" in cur and cur != t:
            print("GENESIS.md is at v1.10 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.10: PASS (%d changes)" % len(CHANGES)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.10: %d changes" % len(CHANGES)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
