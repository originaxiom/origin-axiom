#!/usr/bin/env python3
"""B1828 -- GENESIS v1.59 (main's) -> v1.60 (main's): THE EARNED DICTIONARY. The owner's ruling of 2026-11-03 on P-580
("first decision is YES"): a frame may earn its dictionary by held-out prediction (THE_FINAL_ACTS_BAR's V cell), amending
GAP1's stance. The criteria are main's drafting, the owner's to revise. GAP1's sentence and FK11's unearnability by
derivation stand; a new status, EARNED BY PREDICTION, scoped to one frame and revocable.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.60 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_59_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_59 = "a56f4b09b175cc5d6210b2be339d7b3c9a774116c1ec264fa82b7d1f1338bae2"
RULE = (
    "  **[v1.60] A DICTIONARY MAY BE EARNED BY PREDICTION (the owner's ruling, 2026-11-03, P-580; B1828).** The sentence above\n"
    "  stands: no frame is derived from §1–§4. What changes is how a frame's dictionary may be earned. An identification\n"
    "  (I-26, a row of docs/IDENTIFICATION_LEDGER.md) is **EARNED BY PREDICTION within a frame F** when all six hold:\n"
    "  1. *Fixed before.* F, every discrete choice, every fitted continuous input and the identification itself are on a\n"
    "     sealed frame card (WORKING_RULES, the rule of 2026-10-29) before any predicted value is compared.\n"
    "  2. *Held out.* Each predicted quantity is on THE_FINAL_ACTS_BAR's held-out list (V), or is added to it before any\n"
    "     look, and no function of it was used in building, choosing or tuning F (V's rule); its prior looks count in m_V.\n"
    "  3. *Passed.* Each is graded PASSED by V: the measured value inside the prediction's stated 68% band, and\n"
    "     p_V < 0.01/m_V against the matched null (F's pipeline re-run over its whole CHOSEN menu, B1798).\n"
    "  4. *Two at least.* At least two held-out quantities, not functions of one another, pass on the same card.\n"
    "  5. *Verified.* Main recomputes the passes from the sealed card with its own code; a hostile referee and a third\n"
    "     opinion (the standing directive for positive value matches) find no fault.\n"
    "  6. *Scoped and revocable.* The status reads \"EARNED BY PREDICTION within F, by arc X\". It reverts to UNEARNED, the\n"
    "     record kept, if a later sealed held-out prediction of F through the same identification is graded NEGATIVE.\n"
    "  **What it changes.** A value matched through an identification so earned is graded **PREDICTED**, not a READING, and\n"
    "  counts on the board as predicted. The values used to build F stay FITTED or CHOSEN and count as inputs (P-418's\n"
    "  vector). DERIVED, from §1–§4 with no frame choice, stays a separate and higher grade. FK11's unearnability **by\n"
    "  derivation** within F-HE and F-CI stands: this route earns a frame's use of a dictionary by what it predicts; it does\n"
    "  not derive the dictionary. The criteria are main's drafting; the owner may revise them.\n"
)
CHANGES = [
 ("**Version 1.59 · 2026-10-28 · canonical.**", "**Version 1.60 · 2026-11-03 · canonical.**"),
 ("- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.\n",
  "- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.\n" + RULE),
 ("| FK11 | The dictionary (I-26) | UNEARNED — **[v1.27] UNEARNABLE within F-HE and F-CI",
  "| FK11 | The dictionary (I-26) | UNEARNED — **[v1.60] earnable BY PREDICTION within a frame (GAP1's v1.60 rule; the "
  "owner's ruling of 2026-11-03, B1828); by derivation:** **[v1.27] UNEARNABLE within F-HE and F-CI"),
 ("- **v1.59 · 2026-10-28 · main B1797.**",
  "- **v1.60 · 2026-11-03 · main B1828.** The owner's ruling on P-580: a dictionary may be EARNED BY PREDICTION within a "
  "frame — six conditions (fixed before; held out; PASSED by V; two at least; verified on main; scoped and revocable) "
  "under GAP1, with a pointer in FK11's status cell. A value matched through it is PREDICTED, not a READING. GAP1's "
  "sentence and FK11's unearnability by derivation stand; no other status cell changes; the v1.59 entry below is not "
  "rewritten.\n"
  "- **v1.59 · 2026-10-28 · main B1797.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_59, "the received v1.59 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.60 · 2026-11-03 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out)
    print("GENESIS.md written at v1.60")
