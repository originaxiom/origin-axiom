#!/usr/bin/env python3
"""B1829 -- GENESIS v1.60 (main's) -> v1.61 (main's): THE TWO-LEVEL BAR. The owner's ruling of 2026-11-03 on P-577: the owner
proposed a tiered bar ("first level is looser, and what passes first level goes through more strictness to be counted as the
result"), main assessed it (sound under three conditions; it is the record's option D with a fixed screen) and the owner
answered "agreed". FK9's v1.56 sentence (the looks counted jointly) stands; what changes is how THE_BAR's correction uses
the joint count: a fixed screen, then a confirmation by held-out prediction (GAP1's v1.60 rule).

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.61 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_60_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_60 = "4b514caee7c0be4693aa76d43edd4472e49c6d4129814a8432bfd318b9fc3501"
RULE = (
    "and THE_BAR's correction counts them all. **[v1.61] THE TWO-LEVEL BAR (the owner's ruling, 2026-11-03, P-577; B1829).** "
    "Where the joint look count applies, it is applied in two levels. *Level 1, the screen:* THE_BAR's procedure with every "
    "within-arc choice priced (the matched null re-makes every choice read from the data, B1798, P-389), at p < 0.01 with "
    "no factor for the joint count; a look that holds its support cell and passes is a **CANDIDATE** — frozen, never cited "
    "as support, owed a confirmation, and not a result. *Level 2, the confirmation:* the frozen candidate predicts held-out "
    "quantities under GAP1's v1.60 rule (each at p_V < 0.01/m_V, two at least); only then do its values count, as "
    "PREDICTED. The joint ledger stays, as the count of screens, and reports beside the candidates the number expected by "
    "chance (0.01 per screen). Level 0, exploration (unsealed; no claim), costs no look. Elsewhere THE_BAR is unchanged. |"
)
CHANGES = [
 ("**Version 1.60 · 2026-11-03 · canonical.**", "**Version 1.61 · 2026-11-03 · canonical.**"),
 ("and THE_BAR's correction counts them all. |", RULE),
 ("- **v1.60 · 2026-11-03 · main B1828.**",
  "- **v1.61 · 2026-11-03 · main B1829.** The owner's ruling on P-577 (\"agreed\", to the owner's own proposal of a tiered "
  "bar, as main assessed it): where the joint look count applies, a fixed screen (p < 0.01 with every within-arc choice "
  "priced, no joint factor) makes a CANDIDATE, and only a confirmation by held-out prediction (GAP1's v1.60 rule) makes a "
  "result; the joint ledger stays as the count of screens. FK9's v1.56 sentence stands; no status cell changes; the v1.60 "
  "entry below is not rewritten.\n"
  "- **v1.60 · 2026-11-03 · main B1828.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_60, "the received v1.60 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.61 · 2026-11-03 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out)
    print("GENESIS.md written at v1.61")
