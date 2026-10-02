#!/usr/bin/env python3
"""B1456 -- GENESIS v1.2 (the SM seat's sm:B1519, as received) -> GENESIS v1.3 (main's), as a list of explicit changes.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.3 and differs from what this produces

Same form as B1454's: every change is an exact string of the received text and its replacement, asserted to occur
exactly once.  Lines that add content are marked [v1.3] in the page.
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_2.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_2 = "9cf581654dfdac6b52db4f3a7235e1dff6d7a864ee2474388ec7e680afb581a8"
BAR = "THE_BAR.md (under docs/ on the SM seat's branch; not yet on main)"

CHANGES = [
 ("**Version 1.2 · 2026-10-02 · canonical.**",
  "**Version 1.3 · 2026-10-02 · canonical.**"),
 ("its own, each marked **[v1.2]**. The version log (§10) lists every change; the v1.0 text as received is kept on main in\nB1454's arc (`received/GENESIS_v1_0.md`).",
  "its own, each marked **[v1.2]**. v1.3 (main's B1456) is main's verification of v1.2 with its own code and its adoption,\n"
  "with the three seats' results of the same day folded in, each marked **[v1.3]**. The version log (§10) lists every\n"
  "change; the texts as received are kept on main in the arcs that adopted them\n"
  "(`frontier/B1454_genesis_v1_verified_and_adopted/received/GENESIS_v1_0.md`,\n"
  "`frontier/B1456_genesis_v1_2_verified_and_the_seats_reconciled/received/GENESIS_v1_2.md`)."),
 # ---- section 5: the harmonic frame on the root, now with the vacuum test
 ("at q = 1 both halves on one background, with opposite signs (sm:B1515) |",
  "at q = 1 both halves on one background, with opposite signs (sm:B1515). **[v1.3]** These counts sit on non-split "
  "configurations. On the reductive ones, the vacua of the harmonic family, the count is zero for every q > 0 and every "
  "central twist, by proof (main B1455; independently sm:B1520) |"),
 # ---- section 7: the source
 ("- **GAP3, the source.** Chirality sits on non-split bundles, which carry no harmonic metric without a source (sm:B1378, by\n  Corlette–Donaldson; the audit lane's F01 and R41).",
  "- **GAP3, the source.** Chirality sits on non-split bundles, which carry no harmonic metric without a source (sm:B1378, by\n"
  "  Corlette–Donaldson; the audit lane's F01 and R41). **[v1.3]** What the source must be is on the audit lane's record,\n"
  "  read on main and not re-derived there except where said: one balance for each step of the ordered flag of the\n"
  "  non-split module, each with a definite sign — a scalar source pairs to zero with all of them, a non-central\n"
  "  direction pairs (12, 8, 4) and its negative (−12, −8, −4) (R41; the table re-derived, main B1457); the source may\n"
  "  be supported in the compact core (R76), or the balance may be paid by flux through an end (R41, R80); an added\n"
  "  source model does hold the counted configuration, at the price of infinitely many undetermined flat directions\n"
  "  (R77). **So a count needs three things together: an order of the pieces, an open end, and a source or a flux of\n"
  "  the right sign. A one-ended state can get the third only from a relation** (FK8). No report derives the source.\n"
  "  The counts on record that wait for one: +1 and +1 on m010 (R40), a conditional three on a two-ended exterior with\n"
  "  sources between its ends (R19, R24), −3 on levels three and six for a rank-six coefficient induced from a cover\n"
  "  (R69) — each fenced by its author as not a physical count."),
 # ---- section 7: the observer line, with the corrections its sources carry
 ("choice\" (B717, with B716 and B723).",
  "choice\" (B717, with B716 and B723). **[v1.3]** B723's identification of that choice with a thermodynamic breaking is\n"
  "withdrawn in its own banner: complex conjugation is not in Gal(K^ab/K) (B942), the value torsor failed the same\n"
  "identification (B957), and the breaking has no order parameter at the manifold level (B849). That the apparatus was\n"
  "built does not repair those maps."),
 # ---- section 8: FK9 and FK12
 ("a vacuum fixed by none comes with a mirror partner of equal action |",
  "a vacuum fixed by none comes with a mirror partner of equal action. **[v1.3]** Run (main B1455, NEGATIVE, scoped to "
  "F-HE on m004's harmonic family at level one; independently sm:B1520, the same outcome with the same witnesses): every "
  "vacuum is fixed by a count-odd symmetry, the knot's inversion followed by dualising, so no vacuum of the family "
  "carries a count. The geometric mirror does not change a count at all; dualising does (main B1297, B868, B871). The "
  "family's vacua do break half the symmetries, a mirror among them, with no count attached. Silent on a sourced "
  "vacuum, on other states and on selection by a relation |"),
 ("whether the genesis generates the partner with the act |",
  "whether the genesis generates the partner with the act. **[v1.3]** Three things the record adds, and one "
  "qualification. (i) There are two signs, not one: \"which way\" — the mirror bit c of the observer line — and \"which "
  "of a pair is the particle\" — the linear exchange of a module with its dual, under which a count is odd and c is "
  "absent (B868, B871; B1455). (ii) In the class-index frame a count is the *order* of the two pieces of a non-split "
  "module: the slope law gives it as one term for each order and says when the order counts (main B1438), the fibre's "
  "period-2 involution followed by dualising reverses the order (B1297), and a vacuum in the harmonic sense is a direct "
  "sum, which has no order. (iii) The audit lane's act-and-register audit gives a test for where a register is lost: a "
  "reduction keeps it exactly when both the updates and the declared outputs descend, and all future outputs define "
  "the coarsest record that suffices (its ACT_REGISTER; read on main, not re-derived). The qualification, the audit "
  "lane's: B37's \"never reads\" rests on a detector of a symbol's presence, which an inserted factor r − I at r = I "
  "flips without changing the dynamics; its reads-and-branches criterion is not tested by that detector. Main carries "
  "the question as the standing lead L241 |"),
 # ---- section 10
 ("  - No status changes. FK1 and FK12 are the owner's to frame.",
  "  - No status changes. FK1 and FK12 are the owner's to frame.\n"
  "- **v1.3 · 2026-10-02 · main B1456.** v1.2 verified on main and adopted.\n"
  "  - Verification with main's own code (B1456): the reversal identity on all 8 190 words to length twelve; 758 states\n"
  "    are 536 classes under rotation, swap and reversal, and SnapPy's isometry signatures give that partition; main's\n"
  "    own census read by manifold is 87 of 536 with no pair split; −(LR)² is m207 with H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3, and a signed\n"
  "    even power is the level of no state; the eight isometries of m004 act on the cusp by the four sign pairs, twice\n"
  "    each.\n"
  "  - Added (marked [v1.3]): the deciding test's result at FK9 and in §5 (main B1455, sm:B1520); what a source must be\n"
  "    and what a count needs, at GAP3 (the audit lane's R41, R76, R77, R80, R40, R69; main B1457); the corrections that\n"
  "    B723 carries, in the observer line; at FK12 the two signs, the count as an order (B1438, B1297), the audit\n"
  "    lane's criterion for a lost register and its qualification of B37.\n"
  "  - Named, not changed: THE_BAR is a page of the SM seat's branch and is not yet on main.\n"
  "  - Unchanged and still the owner's: FK1 and FK12."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_2, "the received v1.2 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    n = t.count("`docs/THE_BAR.md`"); assert n == 3, n
    t = t.replace("`docs/THE_BAR.md`", BAR)
    return t, n


def main(argv):
    t, n = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.3 ·" in cur and cur != t:
            print("GENESIS.md is at v1.3 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.3: PASS (%d changes, %d path relabels)" % (len(CHANGES), n)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.3: %d changes, %d path relabels" % (len(CHANGES), n)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
