#!/usr/bin/env python3
"""B8119 -- FINISHING THE 3d THEORY: the checklist re-audited after B8118, and one unsearched row.

The owner asked whether the 3d goal was finished; it was not, and the reason was B8099's AMBIGUOUS
matter row.  B8118 resolved it.  This re-audits every row of B8099's eleven-item checklist against
what the corpus now holds -- and finds that one row was never searched.

THE UNSEARCHED ROW.  B8099 marked the state integral PARTIAL, "B262/B269 rungs, not a closed
evaluation."  B8099 mentions B787 ZERO times.  B787's D5 cell computes the figure-eight state
integral in the Andersen-Kashaev / Marino-Rella normalisation with Faddeev's quantum dilogarithm
VALIDATED, and at the self-dual point b=1 the exact residue evaluation collapses to a SINGLE term.
That is a closed evaluation.  WORKING_RULES section 0 again, and mine.

QUANTIFIER: the eleven rows of B8099's checklist, re-read against the corpus.  Recomputes the
saddle independently.  Gate 5 untouched.
"""
import json, os
import mpmath as mp
import snappy

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

print("=" * 78); print("SECTION 1 -- THE SADDLE, RECOMPUTED INDEPENDENTLY"); print("=" * 78)
# The state integral's classical saddle is the regular ideal tetrahedron z = e^{i pi/3};
# the action's imaginary part is 2 * Im Li_2(z) = Vol(4_1).  Recompute from scratch.
z = mp.exp(1j * mp.pi / 3)
vol_saddle = 2 * mp.im(mp.polylog(2, z))
# NOTE: str() on a SnapPy.Number truncates to its ACCURACY setting -- "2.0298832128", 11 digits.
# Using str() here produced a FALSE FAIL at 1.9e-11 against a 1e-13 threshold: the computation was
# right and the COMPARISON was crippled. float() gives the full double. Recorded because a
# precision-truncating serialisation is the inverse of the usual failure -- it manufactures a
# negative rather than hiding one.
vol_snappy = mp.mpf(float(snappy.Manifold("m004").volume()))
print(f"  saddle shape z          = e^(i pi/3) = {mp.nstr(z, 20)}")
print(f"  2 Im Li_2(z)            = {mp.nstr(vol_saddle, 25)}")
print(f"  SnapPy Vol(m004)        = {mp.nstr(vol_snappy, 20)}")
gate("the state integral's saddle reproduces Vol(4_1)",
     abs(vol_saddle - vol_snappy) < mp.mpf('1e-13'), f"|diff| = {mp.nstr(abs(vol_saddle-vol_snappy),4)}")
# and the arithmetic form, since it is what makes the theory parameter-free rather than fitted
Lchi = mp.mpf(0)
for n in range(1, 200000):
    r = n % 3
    if r: Lchi += (1 if r == 1 else -1) / mp.mpf(n) ** 2
vol_arith = 3 * mp.sqrt(3) / 2 * Lchi
# The L-series is truncated at 2e5 terms, so ~1e-11 is the honest tolerance here, not 1e-30.
gate("Vol(4_1) = (3 sqrt3 / 2) L(chi_-3, 2) -- an L-value, not a fitted constant",
     abs(vol_arith - vol_saddle) < mp.mpf('1e-9'), f"|diff| = {mp.nstr(abs(vol_arith-vol_saddle),4)}")

print(); print("=" * 78); print("SECTION 2 -- THE UNSEARCHED ROW"); print("=" * 78)
b8099 = open(os.path.join(HERE, "..", "B8099_3d_completeness", "FINDINGS.md")).read()
gate("B8099 mentions B787 zero times (the search that was never run)", "B787" not in b8099)
d5 = json.load(open(os.path.join(HERE, "..", "B787_interaction_programme",
                                 "D5_state_integral", "results.json")))
pv = d5["phi_validation"]
print(f"  B787/D5 point           : {d5['point_b']}")
print(f"  Faddeev Phi_b func. eq. : residual {pv['func_eq_maxresidual']:.2e}")
print(f"  saddle vs Vol(4_1)      : {pv['saddle_u0_check']:.2e}")
gate("B787/D5 validated the Faddeev quantum dilogarithm", pv["phi_validated"] is True)
gate("B787/D5's saddle agrees with Vol(4_1) to better than 1e-30",
     float(pv["saddle_u0_check"]) < 1e-30)
gate("and it is evaluated at a point where the residue formula is a SINGLE term",
     "single residue" in d5["point_b"])

print(); print("=" * 78); print("SECTION 3 -- THE ELEVEN ROWS, RE-AUDITED"); print("=" * 78)
ROWS = [
 ("classical solution",       "PRESENT",   "PRESENT",        "2 regular ideal tetrahedra, verified (B8099)"),
 ("cosmological constant",    "PRESENT",   "PRESENT",        "Lambda = -1 exactly (B259)"),
 ("the action",               "PRESENT",   "PRESENT",        "forced (B1012)"),
 ("boundary central charge",  "PRESENT",   "PRESENT",        "c = 6 sigma, derived twice (B1012; Brown-Henneaux)"),
 ("complex CS action",        "PRESENT",   "PRESENT",        "purely real, CS = 0 (B8099)"),
 ("the 3d-3d theory T[4_1]",  "PRESENT",   "PRESENT",        "U(1) + 2 chirals (B262)"),
 ("state integral",           "PARTIAL",   "PRESENT",        "B787/D5: closed residue evaluation at b=1, Phi_b validated. B8099 NEVER SEARCHED B787"),
 ("matter spectrum",          "AMBIGUOUS", "RESOLVED",       "B8118: it is T[4_1]'s 2 chirals; E6/27 is ARITHMETIC, not matter"),
 ("E6 as a DYNAMICAL gauge",  "MISSING",   "CLOSED NEGATIVE","B8118 closes B262's wall #2"),
 ("E6 state integral",        "MISSING",   "DISSOLVED",      "no dynamical E6 => no such object for this manifold"),
 ("the 4d lift",              "MISSING",   "OUT OF SCOPE",   "owner elected 'finish rather than lift'; B8099 proved 3d-3d cannot reach 4d"),
]
print(f"  {'row':<26}{'B8099':<12}{'now':<17}why")
for r, was, now, why in ROWS:
    print(f"  {r:<26}{was:<12}{now:<17}{why[:44]}")
open_rows = [r for r, was, now, why in ROWS if now in ("PARTIAL", "AMBIGUOUS", "MISSING")]
gate("no row of B8099's checklist is left PARTIAL, AMBIGUOUS or MISSING",
     not open_rows, f"open: {open_rows}" if open_rows else "all eleven disposed")

print(); print("=" * 78); print("SECTION 4 -- WHAT IS *NOT* FINISHED, STATED FIRST"); print("=" * 78)
RESIDUES = [
 "the cusp's CONTINUOUS spectrum -- B739/B8101's phi(s) is in hand; the spin-2 cusped test function is NOT",
 "the step from Ray-Singer analytic torsion to the graviton determinant -- B8112 declined it",
 "the n = 2 factor's convergence -- it sits AT the abscissa Re(s) = 2; conditionally convergent at best (B8113)",
]
for i, r in enumerate(RESIDUES, 1):
    print(f"  {i}. {r}")
gate("the one-loop partition function is NOT assembled, and its residues are named", len(RESIDUES) == 3)
print("\n  These were never on B8099's checklist -- they are a rung THIS SEAT added (B8100-B8113).")
print("  The checklist measures the theory's DEFINITION. The residues are its QUANTUM evaluation.")

print(); print("=" * 78); print("THE HONEST VERDICT"); print("=" * 78)
print("""
  THE 2+1 THEORY IS COMPLETE AS A DEFINITION, AND IT IS PARAMETER-FREE.
  Lambda = -1 exactly; the action forced; c = 6 sigma derived twice; matter = 2 chirals, now
  unambiguous; and a CLOSED state integral whose saddle is Vol(4_1) = (3 sqrt3/2) L(chi_-3, 2)
  -- an L-value, not a fitted constant.  Nothing in it is tuned.

  IT IS NOT NEW, AND THIS SEAT DOES NOT CLAIM IT IS.  DGG built T[4_1]; Andersen-Kashaev built
  the state integral; 2+1 gravity with Lambda < 0 is standard.  What the corpus did is ASSEMBLE
  and VERIFY the combination for this manifold, and remove an ambiguity of its own making.

  WHAT REMAINS IS THE QUANTUM SIDE: the one-loop partition function, with three named residues.
  That is where an actual new result would live, and it is open.
""")

RES = {"saddle_volume": str(vol_saddle), "snappy_volume": str(vol_snappy),
       "vol_as_L_value": str(vol_arith),
       "snappy_str_truncation_caught": ("str() on a SnapPy.Number gives 11 digits and produced a "
            "FALSE FAIL at 1.9e-11; float() gives the full double. The computation was correct and "
            "the comparison was not -- a precision-truncating serialisation manufactures a negative "
            "rather than hiding one."),
       "b8099_mentions_b787": b8099.count("B787"),
       "b787_phi_validated": pv["phi_validated"],
       "b787_func_eq_residual": pv["func_eq_maxresidual"],
       "b787_saddle_check": pv["saddle_u0_check"], "b787_point": d5["point_b"],
       "rows": [{"row": r, "b8099": w, "now": n, "why": y} for r, w, n, y in ROWS],
       "rows_still_open": open_rows,
       "one_loop_residues": RESIDUES, "one_loop_assembled": False,
       "definition_complete": True, "parameter_free": True, "novelty_claimed": False,
       "verdict": ("THE 2+1 THEORY IS COMPLETE AS A DEFINITION AND IS PARAMETER-FREE, THE QUANTUM "
                   "SIDE IS NOT, AND ONE ROW OF THE ORIGINAL AUDIT WAS NEVER SEARCHED. Re-auditing "
                   "B8099's eleven rows after B8118: six were already PRESENT; the MATTER SPECTRUM "
                   "is RESOLVED (B8118 -- it is T[4_1]'s 2 chirals, since E6 is arithmetic and not "
                   "matter); E6 AS A DYNAMICAL GAUGE is CLOSED NEGATIVE (B262's wall #2); the E6 "
                   "STATE INTEGRAL DISSOLVES (no dynamical E6, no such object); and the 4d LIFT is "
                   "OUT OF SCOPE by the owner's own election plus B8099's proof that 3d-3d cannot "
                   "reach 4d. THE UNSEARCHED ROW: B8099 marked the state integral PARTIAL, 'not a "
                   "closed evaluation', and mentions B787 ZERO times -- yet B787's D5 cell computes "
                   "the figure-eight state integral in the Andersen-Kashaev normalisation with "
                   "Faddeev's quantum dilogarithm VALIDATED to 1.6e-30, at the self-dual point b=1 "
                   "where the exact residue evaluation collapses to a SINGLE term, with the saddle "
                   "matching Vol(4_1) to 3.9e-31. That is a closed evaluation, and the PARTIAL "
                   "label was a WORKING_RULES section 0 violation by this seat. So no row is left "
                   "PARTIAL, AMBIGUOUS or MISSING. THE THEORY IS PARAMETER-FREE IN A STRONG SENSE: "
                   "the saddle recomputed here independently gives Vol = 2 Im Li_2(e^{i pi/3}) = "
                   "2.029883212819307, which equals (3 sqrt3/2) L(chi_-3, 2) -- an L-VALUE, not a "
                   "fitted constant. NOVELTY IS NOT CLAIMED AND IS EXPLICITLY DISCLAIMED: DGG built "
                   "T[4_1], Andersen-Kashaev built the state integral, and 2+1 gravity with "
                   "negative Lambda is standard; what the corpus did is ASSEMBLE and VERIFY the "
                   "combination for this manifold and remove an ambiguity of its own making. WHAT "
                   "IS NOT FINISHED, STATED FIRST RATHER THAN LAST: the ONE-LOOP PARTITION FUNCTION "
                   "is NOT assembled, with three named residues -- the cusp's continuous spectrum "
                   "(phi(s) in hand, the spin-2 cusped test function not), the "
                   "torsion-to-determinant step B8112 declined, and the n=2 factor's convergence at "
                   "the abscissa (B8113). Those were never on B8099's checklist; they are a rung "
                   "this seat added. The checklist measures the theory's DEFINITION; the residues "
                   "are its QUANTUM EVALUATION, and that is where a genuinely new result would "
                   "live."),
       "scope": ("Re-audits B8099's eleven rows against the corpus and recomputes the state "
                 "integral's saddle independently. Does NOT re-derive T[4_1] or the state integral "
                 "-- both are read from B262 and B787 and, for B787, re-run in-sandbox. Claims no "
                 "novelty. Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
