#!/usr/bin/env python3
"""B1462 -- GENESIS v1.6 (the SM seat's sm:B1526, built on main's v1.5, as received) -> GENESIS v1.7 (main's): verified
on main and adopted, with one correction of a sentence that B1459 had made wrong.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.7 and differs from what this produces

Same form as B1454's, B1456's and B1460's: every change is an exact string of the received text and its replacement,
asserted to occur exactly once.  Lines that add content are marked [v1.7].
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_6_sm.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_6 = "59ef40a678a2aa7b11d37599300b6d3cacc481edb0568f30eda852ba176faf36"

CHANGES = [
 ("**Version 1.6 · 2026-10-03 · canonical.**",
  "**Version 1.7 · 2026-10-03 · canonical.**"),
 ("`GENESIS_v1_5_sm.md`), and main's v1.4 and the seat's v1.3 in sm:B1525's. The version log (§10) lists every",
  "`GENESIS_v1_5_sm.md`), and main's v1.4 and the seat's v1.3 in sm:B1525's. v1.7 (main's B1462) is main's verification\n"
  "of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. The version log (§10) lists every"),
 # FK12 (ii): B1459 showed P alone carries a module to its dual up to a meridian sign; followed by dualising it FIXES the module
 ("the fibre's period-2 involution followed by dualising reverses the order (B1297), and a vacuum in the harmonic sense is a direct sum, which has no order.",
  "the fibre's period-2 involution P carries a module to its dual up to a meridian sign — it reverses the order by itself, and "
  "followed by dualising it fixes the module (B1297; **[v1.7]** main's B1459, on every complete point of 16 levels: ι̃*V ≅ V* ⊗ ε, "
  "so I(V) = −I(V ⊗ ε) and the index is zero; the earlier wording \"followed by dualising reverses the order\" was main's and is "
  "withdrawn) — and a vacuum in the harmonic sense is a direct sum, which has no order."),
 ("  - No status changes. FK1 and FK12 as the owner decided (v1.5).",
  "  - No status changes. FK1 and FK12 as the owner decided (v1.5).\n"
  "- **v1.7 · 2026-10-03 · main B1462.** v1.6 verified on main and adopted.\n"
  "  - Re-derived on main with its own code (B1462): P is the swap's class in Ballas' presentation (SnapPy's holonomy,\n"
  "    `p_is_the_swap.py`); on the levels M₁…M₆ the twists fixed by no count-odd map for λ off the unit circle number\n"
  "    0, 0, 0, 0, 20, 96 (Fox calculus over ℤ[ℤ/n] from SnapPy's presentation, the eight symmetry classes found by\n"
  "    search, the dualising ones read off the longitude; `levels_count_odd.py`), the SM seat's sm:B1522 numbers exactly;\n"
  "    on M₅ the 20 are exactly the single-sheet twists, ten per golden sheet; two of sm:B1524's null-contract numbers\n"
  "    (the exact scan law against the binomial; the Šidák counterexample at the gate).\n"
  "  - Read, not re-derived: sm:B1523 (the projective family on every word state; Lemma R and Lemma T), the rest of\n"
  "    sm:B1524, sm:B1525's items as carried into v1.6, sm:B1526's C2–C5.\n"
  "  - Corrected (marked [v1.7]): FK12 (ii)'s sentence on P and dualising, main's own since v1.3, against B1459.\n"
  "  - Named: the owner's hypothesis \"choice might be golden\" is on the record in two sealed forms (FK9); the SM seat's\n"
  "    sL-10 item 8 (the class index on a mirror-broken word state's family) is in §8's frontier and is the seat's, sealed first.\n"
  "  - Unchanged: FK1 and FK12 as the owner decided (v1.5)."),
]


ACT = "`philosophy/P_ACT_AND_REGISTER_2026_10_02.md`"
ACT_PROSE = "P_ACT_AND_REGISTER_2026_10_02 (a page of the audit lane's branch, not on main)"


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_6, "the received v1.6 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    n = t.count(ACT); assert n == 1, n                      # an off-branch path, named in prose on main (the path-refs gate)
    t = t.replace(ACT, ACT_PROSE)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.7 ·" in cur and cur != t:
            print("GENESIS.md is at v1.7 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.7: PASS (%d changes, 1 path relabel)" % len(CHANGES)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.7: %d changes" % len(CHANGES)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
