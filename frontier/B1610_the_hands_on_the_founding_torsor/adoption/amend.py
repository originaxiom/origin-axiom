#!/usr/bin/env python3
"""B1610 -- GENESIS v1.30 (main's, B1609) -> v1.31 (main's): THE HANDS ON THE FOUNDING TORSOR -- the McKay hand of the tick
is the founding torsor's swap bit given the forced arrow; the records' hand is on no rule, so the three's hand is the
orientation sheet (SE2), not a naming; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.31 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_30_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_30 = "ee3496e3f8d4d98a075c9ed49bbd6edfa28809729a5620b090534f9e169675f8"

HANDS = (" **[v1.31] THE HANDS ON THE FOUNDING TORSOR (main, B1610; sealed f916539c6; NEGATIVE as sealed).** On B1083's four "
         "founding rules and the inverse rule: the McKay hand of the tick (its parity 3-cycle's sense; the 2T-class of its lift) "
         "is flipped by swap-conjugation and by the arrow and kept by the reversal, so, the arrow being forced (B1083), it is the "
         "torsor's swap bit — which record is called a — a naming. The records' hand is on no rule: all five reverse W21's form "
         "and exchange T and T̄, every double tick keeps them, so the records' orientation is carried by the parity of the tick "
         "count and **the three's hand is the sheet of the orientation double cover — SE2's choice — not a naming** (the sealed "
         "headline \"both hands are one bit\" is refuted; its spectral detector was vacuous and is withdrawn). The two sheets are "
         "exchanged by the rule and isometric, so which is \"left\" is a convention as in physics; that the distinction exists is "
         "the double-tick restriction (this fork answered no), the same kind of choice as SE2.")

CHANGES = [
 ("**Version 1.30 · 2026-10-08 · canonical.**", "**Version 1.31 · 2026-10-08 · canonical.**"),
 ("Every route to the gauge side's complex structure on the record now meets this fork.",
  "Every route to the gauge side's complex structure on the record now meets this fork." + HANDS),
 ("- **v1.30 · 2026-10-08 · main B1609.** The even subweave.\n",
  "- **v1.31 · 2026-10-08 · main B1610.** The hands on the founding torsor.\n"
  "  - GM5c/SE2: the McKay hand of the tick is the founding torsor's swap bit given the forced arrow (a naming); the records' hand is on no rule (every founding rule and the inverse reverse it), so the three's hand is the orientation sheet chosen at SE2, not a naming; its existence is the double-tick restriction. NEGATIVE as sealed (\"both hands are one bit\" refuted; the spectral detector vacuous, E82).\n"
  "- **v1.30 · 2026-10-08 · main B1609.** The even subweave.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_30, "the received v1.30 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.31 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.31, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
