"""Review 74 (S299), apply 1: the seeded sample's corrections (verified by main at source), the H = I scope the web seat's
T-NORM relay § 4 flagged (verified: no H = I / T-NORM / B1822 mention in the nine arcs, nor in B1734, B1735, B1741, B1829,
nor in the eleven LAW_MAP rows), and P-561's two scoreboard rows.  Each edit asserted; dated notes appended."""
import pathlib, re, glob
ROOT = pathlib.Path(__file__).resolve().parents[3]
D = "2026-11-04"
def arcdir(a): return pathlib.Path(glob.glob(str(ROOT / "frontier" / (a + "_*")))[0])
def append(a, text):
    p = arcdir(a) / "FINDINGS.md"; t = p.read_text(encoding="utf-8")
    assert "Review 74" not in t[-4000:] or a == "B1823", a
    p.write_text(t.rstrip("\n") + "\n\n" + text.strip("\n") + "\n", encoding="utf-8")

# --- the sample (Review 74's seeded read; main verified each at source) ---
append("B1821", "> *Dated note " + D + " (Review 74's seeded read, verified by main):* \"confirmed on every direction and line\" (the "
 "title, the claim line) is wider than what ran: the 200 random configurations of `re_symmetry_check_200.json` cover 146 of "
 "the census's 266 lines and the earlier file 20 (not 22) configurations on 20 lines — 154 lines together, all twelve orders "
 "represented; the relative-precision check (24 configurations) is the only one that sees outputs below 10⁻⁵. Two of the "
 "earlier 20, the order-4 lines (1/4, 1/2) and (1/2, 1/4), record 22 of 26 groups, undisclosed; the review's reader re-ran "
 "both with the committed check and got 26 of 26 (not re-run by main), and no committed script writes that file. The mirror "
 "map stands as confirmed on the lines tested. The radius is read from B1667's Re τ = 1/4 column, so its mirror-invariance is "
 "assumed, not tested (FL-11, UNSTATED). The strip guard the page calls 'a lock' is B1825's (rigid_census_refined.py). The "
 "\"2.6 × 10⁻⁶ against B1810's table\" has no committed output (control() asserts < 10⁻⁴). The arc reads J, mass ratios and "
 "∣V∣ with identifications [] (I-33; P-516's class).*")
append("B1822", "> *Dated note " + D + " (Review 74's seeded read, verified by main):* the headline's \"8 real parameters per field "
 "(2 under the diagonal SU(2))\" mixes two counts: the 8 is after the overall scale, the 2 is before it (the referee's "
 "independent.json, \"(iv) diagonal SU(2): real dim\": 2). After the scale it is 8 per field, and 1 under the diagonal SU(2). "
 "\"The referee reproduced every stored number\" means its rerun's six classes of 306 (referee/rerun_arc.py). G = H·‖F‖² has "
 "no LAW_MAP row.*")
append("B1823", "> *Dated note " + D + " (Review 74's seeded read, verified by main against `verification/summary.txt`):* \"every "
 "computed n = 3 and n = 4 vacuum lies on a line\" (§ 1) is false for the committed grid: four converged, isolated, "
 "non-runaway vacua sit off every mirror line at λv = 1.0 in menu Z (n = 3 at μ² = 0.5 and 0.8; n = 4 at μ² = 0.5 and 0.8), "
 "and their convention-free rank was never computed. The sentence holds for the decoupling point and the referee's vacua. "
 "The NEGATIVE stands either way: rank 3 on a mirror line already exceeds τ's 2. The robust paragraph's \"Y₃,₁ × Y₃,₂ … in "
 "every convention\" holds while both copies are heavy; in the source's cusp and the Petersson-type conventions n = 2 has a "
 "light copy at the decoupling point and that vacuum is lost (the paragraph before it). "
 "`main/rerun_stableF/step_a_v2.json` still carries the discarded first arbiter's *_mp fields, unmarked; the tallies do not "
 "use them. The text names H_u ≡ H_d UNEARNED, with identifications [] (P-516).*")
append("B1824", "> *Dated note " + D + " (Review 74's seeded read, verified by main):* \"confirmed by main componentwise at three "
 "values of τ\" matches no committed output: `verification/a0_identity_main.json` checks five τ values across its three "
 "parts, and B1823's `checks_extra.json` six. \"Twelve distinct\" (of B1810's thirteen) is not computed here; the review's "
 "reader found from B1810's table that only a₀/F₋₂ coincide among the 78 pairs (next closest 0.048; not re-run by main). "
 "The census confirmation is in B1825 (its a0/F₋₂ diagnostic: 2 184 pairs above the floor, differing by at most "
 "3.3 × 10⁻⁵ in log10, the double-precision limit; S280).*")
append("B1828", "> *Dated note " + D + " (Review 74's seeded read):* GENESIS carries the v1.60 text as adopted; the companions "
 "landed with FL-20 besides those listed. \"The rule uses V unchanged\" is not literal: v1.60 lets a target be added to V "
 "\"before any look\" where THE_FINAL_ACTS_BAR fixes its list, and its gloss of the null omits the bar's no-menu fallback. "
 "Unlike v1.49–v1.59 the arc has no lock test.*")

# --- the H = I scope (the web seat's T-NORM relay of 2026-10-30, § 4; P-594) ---
HI = ("computed with the generations' metric H = I, implicit in B1656's coupling: a CHOSEN input (B1822 — the flat "
      "structure leaves 8 real parameters per field after the scale, and the outputs move with H). Whether a conclusion "
      "holds at another H is not computed here")
for a in "B1725 B1726 B1732 B1734 B1735 B1741 B1742 B1743 B1745 B1746 B1747 B1829".split():
    append(a, "> *Dated note " + D + " (Review 74; the web seat's T-NORM relay of 2026-10-30, § 4, verified by main: this page "
           "carried no H = I scope):* every FR-FIB output here is " + HI + ".*")
append("B1744", "> *Dated note " + D + " (Review 74; the web seat's T-NORM relay of 2026-10-30, § 4):* every FR-FIB output here "
       "is " + HI + "; the web seat reads this arc's NEGATIVE for its question as holding for every H (not verified on main).*")
p = ROOT / "docs/LAW_MAP.md"; ls = p.read_text(encoding="utf-8").split("\n")
for n in (322, 327, 329, 330, 335, 337, 338, 339, 340, 341, 342):
    l = ls[n - 1]; assert l.startswith("| **") and l.endswith(" |") and "H = I" not in l, n
    extra = " (the web seat reads B1744's negative as holding for every H; not verified on main)" if n == 339 else ""
    ls[n - 1] = l[:-2] + " [scope, Review 74: FR-FIB at H = I, the generations' metric, a CHOSEN input (B1822); the outputs move with H" + extra + "] |"
p.write_text("\n".join(ls), encoding="utf-8")

# --- P-561: the scoreboard's first two rows ---
p = ROOT / "docs/HARVEST_LEDGER.md"; ls = p.read_text(encoding="utf-8").split("\n")
for n in (1478, 1479):
    k = [i for i, l in enumerate(ls) if l.startswith("| %d |" % n)]; assert len(k) == 1, n
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]; assert len(c) == 8, (n, len(c))
    c[5] += (" [Review 74 (P-561): the row counts I-33's T-NORM by hand and does not count the generations' metric; B1822 "
             "shows H = I is a CHOSEN input, 8 real parameters per field after the scale, uncounted among the row's inputs]")
    assert all("|" not in x for x in c)
    ls[k[0]] = "| " + " | ".join(c) + " |"
p.write_text("\n".join(ls), encoding="utf-8")
print("apply1 done")
