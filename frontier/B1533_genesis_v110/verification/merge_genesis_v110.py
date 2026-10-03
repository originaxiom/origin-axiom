#!/usr/bin/env python3
"""B1533 -- GENESIS v1.9 (main's B1466, as received) -> GENESIS v1.10 (sm:B1533): main's head taken as the head, as main
asked; the SM seat's v1.8 lines (sm:B1528), which main's v1.9 does not carry, re-applied as they were; and three marked
additions: GAP6's scope, Part H verified on main (FK9), and main's form of the twisted identity (FK12 (ii)).
Same form as main's amend.py and sm:B1528's merge: every change is an exact string of the text it applies to and its
replacement, asserted to occur exactly once. The v1.8 lines are sm:B1528's own CHANGES, imported from its merge (the
content changes only; v1.8's version line, intro sentence and log entry are restated below for v1.10). Lines that add
content are marked [v1.10]. Run only after genesis_v110_checks.py passes (its pre-write log is kept).

    python3 merge_genesis_v110.py            # writes GENESIS.md at the repository root
    python3 merge_genesis_v110.py --check    # exit 1 unless the root file is exactly what this produces
"""
import hashlib
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = HERE.parents[2]
SRC = ARC / "received" / "GENESIS_v1_9_main.md"
OUT = ROOT / "GENESIS.md"
SHA_V1_9 = "7eb2df0fee9e32c638b6c872bb4ec07a1f8b93d96c3038153d75508752b5eca2"


def b1528():
    spec = importlib.util.spec_from_file_location("b1528_merge_genesis_v18",
                                                  ROOT / "frontier" / "B1528_genesis_v18" / "verification" / "merge_genesis_v18.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V18 = b1528().CHANGES
V18_CONTENT = V18[2:5]          # FK12 (ii), FK9, section 8's frontier: sm:B1528's three content changes, as they were
V18_LOG = V18[5][1].split("\n", 1)[1]
assert V18_LOG.startswith("- **v1.8 · 2026-10-03 · sm:B1528.**")
_HEAD18 = ("- **v1.8 · 2026-10-03 · sm:B1528.** Main's head, v1.7, taken as the head, as main asked (its relay of 2026-10-03:\n"
           "  \"Please take v1.7 as head\").")
assert V18_LOG.count(_HEAD18) == 1
V18_LOG = V18_LOG.replace(_HEAD18, "- **v1.8 on the SM seat's branch · 2026-10-03 · sm:B1528.** Main's head, v1.7, taken as the head, as main\n"
                                   "  asked (its relay of 2026-10-03: \"Please take v1.7 as head\").", 1)

V110 = [
 ("**Version 1.9 · 2026-10-03 · canonical.**",
  "**Version 1.10 · 2026-10-03 · canonical.**"),
 ("of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. The version log (§10) lists every",
  "of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. v1.8 (sm:B1528) takes main's\n"
  "head, v1.7, as main asked, makes that sentence's scope exact and records sm:B1527, marked **[v1.8]**. Main's own v1.8\n"
  "(B1463), made on v1.7 in parallel and numbered the same, adds a line to the version log, and v1.9 (main's B1466) is made on\n"
  "it, marked **[v1.9]**. v1.10 (sm:B1533) takes main's head, v1.9, as main asked, carries the SM seat's v1.8 lines as they\n"
  "were, and adds what is marked **[v1.10]**; the two v1.8s and v1.9 are kept as received in sm:B1533's `received/`. The\n"
  "version log (§10) lists every"),
 # FK12 (ii): main's B1465 states the twisted identity in the same form (inside main's parenthesis, after the [v1.8] text)
 ("(sm:B1528 C2–C3, own code))",
  "(sm:B1528 C2–C3, own code); **[v1.10]** main's B1465 states it in the same form, ι̃*V ≅ V* ⊗ ε ⊗ λ², and computes that "
  "half at the complete points of the first mirror-broken states, where it finds no count (FK9))"),
 # FK9: Part H verified on main
 ("Open: the eigenvalue-one locus of the infinite-volume part (sL-10 item 9).",
  "Open: the eigenvalue-one locus of the infinite-volume part (sL-10 item 9). **[v1.10]** Part H, the hyperbolic point "
  "itself, verified on main by a route sharing nothing with the seat's (B1465): on ±LLRLRR and ±L³RLR², at the parabolic "
  "points of their periodic curves, for every fibre character and seven twists of the meridian, 7 364 indices, all zero."),
 # section 7: v1.9 added GAP6 under the heading's old count
 ("**Five gaps**, none of which work on one state can close:",
  "**Six gaps**, none of which work on one state can close:"),
 # GAP6: its scope, from the record
 ("  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.\n",
  "  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.\n"
  "  **[v1.10]** Its scope, from the record (sm:B1531 §3 and §7; re-derived in sm:B1533 C3–C6). The Chern–Weil row is B1420's\n"
  "  A4: on a closed spin 4-manifold a flat bundle's Dirac index is rk(V)·(−σ/8), rank-blind; and B1420 states the second\n"
  "  edge, that the non-zero values on non-split modules are flat data too, counts of twisted classes and not Dirac indices.\n"
  "  So the sentence holds for Dirac indices and for every count on a closed or sealed problem (sm:B1351, sm:B1392) or with no\n"
  "  flux (sm:B1502), and not for B1297's class index, which reads the open end: on M₄, at sm:B1515's member ν = (1/3, 0), the\n"
  "  non-split W₁, its dual and the split V ⊕ L are flat of rank five, so of one Chern character, each with h¹ = 2, and they\n"
  "  count +1, −1 and 0 (two routes, sm:B1533 C4); main's B1466 counts −1 and +1 on its two orders and 0 on their sum, the\n"
  "  same way. A flat frame's count can tell a module from its dual; whether such a count is a physical chirality is GAP1.\n"
  "  Frames with curvature or a singular point are on the record, each with its outcome: sm:B1397's flux caps give chirality\n"
  "  linear in the charges and even in every E₆ frame; sm:B1502's cone points carry no rational flux, and sm:B1503's apex\n"
  "  index is zero, the links having positive scalar curvature; and an end flux may pay GAP3's balance (R41, R80). Curvature\n"
  "  alone is not what the record found missing; a frame with curvature whose arithmetic allows three is (sm:B1531, lead\n"
  "  (c)). Nor do the three kinds exhaust the record's negatives: of the chirality chain's 26 (the reading of 2026-09-30),\n"
  "  read record by record as data (sm:B1531 C2), 8 are symmetry, 3 flatness, 3 non-uniqueness and 12 none of the three,\n"
  "  nine of these frame arithmetic, where the frame's representation theory and charge lattices forbid the target: a fourth\n"
  "  kind (lead L244 (a)).\n"),
 # section 10: the SM seat's v1.8, after main's v1.8
 ("  Lead L243 (a) paid.\n",
  "  Lead L243 (a) paid.\n" + V18_LOG + "\n"),
 # section 10: the v1.10 entry, last
 ("    B128, B849, B1327 and FK12 already state it).\n",
  "    B128, B849, B1327 and FK12 already state it).\n"
  "- **v1.10 · 2026-10-03 · sm:B1533.** Main's head, v1.9, taken as the head, as main asked (its relay of 2026-10-03: \"Please\n"
  "  take v1.9 as head\"). Main's v1.9 is main's v1.8 with exactly the changes main's B1466 lists, and main's v1.8 is v1.7 with\n"
  "  its version line and one log entry (sm:B1533 C1). Main's v1.8 and the SM seat's (sm:B1528) were made on v1.7 in parallel\n"
  "  and numbered the same; the seat's lines were not in main's v1.9.\n"
  "  - Carried as they were (marked [v1.8]): FK12 (ii)'s sentence made exact, and FK9's and §8's record of sL-10 item 8\n"
  "    (sm:B1533 C2: sm:B1528's changes on main's v1.7 give the seat's v1.8 byte for byte, and each lands once in v1.9).\n"
  "  - Added (marked [v1.10]) at GAP6: its scope (the Chern–Weil row is the Dirac index's, as B1420 says; the class index\n"
  "    counts +1, −1 and 0 on three flat modules of one rank, sm:B1533 C4, own code, two routes), the frames with curvature\n"
  "    or a singular point on the record, and lead L244 (a) on the chirality chain (sm:B1531).\n"
  "  - Added (marked [v1.10]) at FK9: Part H verified on main (B1465: 7 364 indices, all zero); at FK12 (ii): main's B1465\n"
  "    states the twisted identity in the same form.\n"
  "  - Corrected: §7's heading counts six gaps (v1.9 added GAP6 under \"Five gaps\").\n"
  "  - No status changes. FK1 and FK12 as the owner decided (v1.5).\n"),
]

CHANGES = V18_CONTENT + V110


def build():
    raw = SRC.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_9, "the received v1.9 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        ok = OUT.read_text(encoding="utf-8") == t
        print("VERDICT genesis-merge-v1.10: " + ("PASS" if ok else "FAIL") + f" ({len(CHANGES)} changes)")
        return 0 if ok else 1
    OUT.write_text(t, encoding="utf-8")
    print(f"wrote GENESIS.md v1.10: {len(CHANGES)} changes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
