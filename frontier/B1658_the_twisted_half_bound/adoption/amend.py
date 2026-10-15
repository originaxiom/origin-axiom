#!/usr/bin/env python3
"""B1658's landing (S133) -- GENESIS v1.46 (main's, B1655) -> v1.47 (main's): the price restated. The count of irreducible
identifications in GENESIS's line on the root's inputs was B1266's eleven; the live price, rerun on the ledger after the
field stage's four rows (I-31 to I-34), is 4 axioms + 9 irreducible sources = 13; the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.47 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_46_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_46 = "67c11212e51410257c9226a8c264ecf0adf0977ca9b37a7fb542750d884e5148"
CHANGES = [
 ("**Version 1.46 · 2026-10-15 · canonical.**", "**Version 1.47 · 2026-10-15 · canonical.**"),
 ("eleven irreducible identifications\n(B1266),", "eleven irreducible identifications\n(B1266; **[v1.47] the live price, rerun on the identification ledger, is 4 axioms + 9 irreducible sources = 13** —\nthe field stage's rows I-31 to I-34, S133; `outside_bench/certificates/the_price_is_twelve.py`),"),
 ("- **v1.46 · 2026-10-15 · main B1655.**",
  "- **v1.47 · 2026-10-15 · main, at B1658's landing (S133).** The price restated: the identification ledger gains the "
  "field stage's four rows — I-31 (\"given Λ\", the owner's tagged postulate, its own source), I-32 (the hypercharge "
  "dictionary), I-33 (the read-out), I-34 (the index given the cusp's unit) — and the live price is 4 + 9 = 13.\n"
  "- **v1.46 · 2026-10-15 · main B1655.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_46, "the received v1.46 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.47 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.47, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
