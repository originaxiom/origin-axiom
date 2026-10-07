#!/usr/bin/env python3
"""B1602 -- GENESIS v1.25 (main's, B1601) -> v1.26 (main's): main's weave items renamed WM1, WM2 (the SM seat's W5-W10
preceded them on its lane); WM3 recorded at FK14 -- the forced cover on every thread to length eight: content on the
odd-trace covers on +-LR only (the 3-cycle's three-or-nothing), on the even-trace covers on most threads but not all;
the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.26 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_25_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_25 = "b9a392c166dfa92b87fb8a6b7c4eb28b30b692df25e86b10b1067e68ed79f6f1"

RESULT = 'on all 74 signed threads to length eight (32 of odd trace, 42 of even; none chosen) the cover the common point forces (A₄ on odd trace, D₄ or V₄ on even) carries members of the four at sign characters on +LR (24, reading (−1, −1)), on −LR (6, reading (0, −3)) and on ONE more odd-trace thread, −LLRLRLRR (trace −39): one member whose class is alive on all four cusps and reads (+3, +1) — the seat\'s floor k − m_A − b0 attained exactly, the ends\' value, not generation-shaped; its sign twin and the other 28 odd-trace threads carry nothing. On even trace 17 of 42 carry (the two-syllable words with small exponents and the V₄ words L^{2k}R²), 25 do not. Interior classes of the four at the trivial character only on the eight shortest even threads, on no odd one. NEGATIVE as sealed: neither the ±LR exclusivity (the seat\'s W6 census to length six) nor an even-trace genericity holds; "content ⟺ arithmetic" was killed before the seal (+LLR, not arithmetic, carries). Content on the weave\'s forced cover is rare on odd trace because Theorem G makes it three-or-nothing; what admits ±LR and −LLRLRLRR is the open question for W6 (3 ramifies in all three trace fields — and in four non-carriers\').'

CHANGES = [
 ("**Version 1.25 · 2026-10-07 · canonical.**", "**Version 1.26 · 2026-10-07 · canonical.**"),
 ("**[v1.25] W5 (main, B1601):**", "**[v1.25] WM1 (main, B1601; named W5 at v1.25, renamed at v1.26 — the SM seat's W5–W10 preceded it on its lane):**"),
 ("**[v1.25] W7, THE COMMON POINT IS THE GEOMETRY MOD 3 (main, B1601, sealed; a weave result):**", "**[v1.25] WM2 (named W7 at v1.25, renamed likewise), THE COMMON POINT IS THE GEOMETRY MOD 3 (main, B1601, sealed; a weave result):**"),
 ("the ±LR pattern stays arithmeticity's, unexplained. ",
  "the ±LR pattern stays arithmeticity's, unexplained. **[v1.26] WM3, THE FORCED COVER ON EVERY THREAD (main, B1602, sealed; a weave result):** " + RESULT + " "),
 ("  - FK14: W5 — the four at the common point is the trivial line plus the triplet; W7 — ",
  "  - FK14: W5 (WM1 from v1.26) — the four at the common point is the trivial line plus the triplet; W7 (WM2 from v1.26) — "),
 ("- **v1.25 · 2026-10-07 · main B1601.** The common point is the geometry mod 3.\n",
  "- **v1.26 · 2026-10-07 · main B1602.** The forced cover on every thread; main's weave items renamed WM1, WM2.\n"
  "  - FK14: WM3 — " + "the forced cover on all 74 signed threads to length eight at sign characters: content on +LR, −LR and −LLRLRLRR (its member the floor's value (+3, +1) with four live ends), on 17 of 42 even threads; the ±LR exclusivity and the even-trace genericity both fail; 'content ⟺ arithmetic' killed before the seal." + "\n"
  "- **v1.25 · 2026-10-07 · main B1601.** The common point is the geometry mod 3.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_25, "the received v1.25 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.26 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.26, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
