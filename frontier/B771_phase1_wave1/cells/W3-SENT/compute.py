#!/usr/bin/env python3
"""W3-SENT -- re-fire the armed B403/B405/B406 sentinels on e1,e2,e3 with the
CORRECTED e2 (Wave-2 carry fix).

CONTEXT (read in full before writing this cell):
  frontier/B771_phase1_wave1/cells/W2-SENT/{compute.py,output.txt}  -- the cell
    this one repairs. W2-SENT's SET_A dict used e2_num=-3, e2_den=48. That pair
    is WRONG: -3/48 = -1/16, not e2. W2-SENT's own in-cell derivation (and the
    banked OI-031 result) both correctly established e2 = -1/48 = -3/144
    (S2 = -3 exactly; e2 = S2/144). The bug was purely in how the fraction was
    RE-SPLIT into (numerator, denominator) for the SET_A prime-factoring table:
    -3 was kept from the /144 derivation but paired with the *reduced* 48
    instead of either (a) the reduced pair (-1, 48) or (b) the unreduced pair
    (-3, 144). Mixing an unreduced numerator with a reduced denominator silently
    changes the value being fed to factorint.
  frontier/B403_lead_package/{PREREGISTRATION,FINDINGS,scrutiny.json}
  frontier/B405_supersingular_check/{FINDINGS,sentinels.json,counts_15a1.json}
  frontier/B406_two_conductor/{FINDINGS,bridge.json,mod4_extension.json}
  frontier/B771_phase1_wave1/cells/OI-031/{compute.py,output.txt}  (Wave-1: e3
    identified; banked e1=0, e2=-1/48, e3=(1*c9)/1728, c9=2cos(2*pi/9))

FIX APPLIED: SET_A now uses the UNREDUCED pair (e2_num=-3, e2_den=144), which is
the pair the in-cell symbolic derivation actually produces (S2=-3, e2=S2/144).
A SELF-TEST below asserts num/den == -1/48 exactly (Fraction), and separately
asserts the OLD buggy pair (-3,48) does NOT equal -1/48 -- so the fix is not a
tautology (substituting the buggy pair changes the asserted value, proving the
check has teeth).

THE THREE REGISTERED SENTINEL PREDICATES (verbatim from the banked files,
restated -- identical wording to W2-SENT, since the predicates themselves did
not change; only the e2 pair does):

  B403 (V3 salvage, scrutiny.json): if either 17 (non-principal, form (3,-1) for
    disc -15) or 19 (principal, form (1,2)) EVER appears as a prime factor of a
    seam-channel NUMERATOR at a higher level, that is a registered test with real
    content (a live discrepancy against the "class-filters-primes" picture that was
    killed for denominators but left open for numerators).

  B405 (sentinels.json): supersingular_below_200 for 15a1 = {7,23,31,79,167}.
    Registered hook: if a future EXCEPTIONAL prime in higher-level Gram/singles-
    support spectra (FINDINGS.md names "the 1215 identifications" explicitly as the
    anticipated site) lands on this list, that is an immediate registered test.

  B406 (FINDINGS.md, "THE 31-COLLISION"): Chat-1's E2 row claims split-principal
    primes {19,31,61,79,...} are "absent from the program"; 31 and 79 are also B405
    supersingular sentinels. If "the 1215-triple identification" (= e1,e2,e3 of the
    depth-5 level-1215 triple -- exactly OI-031's object) surfaces 31, both the
    "principal absent" row and the B405 sentinel fire simultaneously. Registered
    consequence: BOTH claims collide/die together.

METHOD: recompute the discriminating facts IN-CELL (not cited from OI-031's printed
summary or from W2-SENT's) -- rebuild the exact cyclotomic identity for e1,e2,e3
from Phi_27 symbolically, extract every integer that appears anywhere in that exact
arithmetic (numerator, denominator, minimal-polynomial coefficients/discriminant of
the field element, root-index labels, banked residue-class labels), factor every
one of them, and check membership against the three registered prime sets above.
A sentinel FIRES iff its literal registered predicate is satisfied; near-miss
coincidences that fail the predicate's own terms (e.g. an index label vs a
numerator prime) are recorded, not counted as fires -- MB12 vacuity discipline:
the predicate must be able to fail.
"""
import json, math, os, time
from fractions import Fraction
from sympy import (symbols, Poly, QQ, ZZ, expand, Rational, factorint, cos, pi,
                    nsimplify, discriminant, minimal_polynomial, Symbol, sqrt)

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
def log(*a):
    print(f"[{time.time()-T0:7.2f}s]", *a, flush=True)

# ============================================================ 1. in-cell recompute
# Independent re-derivation of e1, e2, e3 exactly in Q[z]/Phi_27(z), z = zeta_27,
# following the same algebraic identity OI-031 verified (product over the Galois
# orbit {1,10,19} of (z^k+z^-k)), built fresh here (no numbers copied from
# OI-031's or W2-SENT's output.txt -- only the *root-index set* {1,10,19} and the
# level 1215 / 27 identification are cited as the object under test).
log("=== in-cell re-derivation of e1,e2,e3 (Q[z]/Phi_27) ===")
z = symbols('z')
PHI27 = Poly(z**18 + z**9 + 1, z, domain=QQ)   # 27th cyclotomic polynomial

def red(expr):
    return Poly(expand(expr), z, domain=QQ).rem(PHI27)

K = (1, 10, 19)                    # the Galois-orbit root-index set (banked, B399/OI-031)
rz = {k: z**k + z**(27 - k) for k in K}     # = 2*cos(2*pi*k/27) as a poly in z, degree<18
S1 = red(sum(rz.values()))
S2 = red(rz[1]*rz[10] + rz[1]*rz[19] + rz[10]*rz[19])
S3 = red(rz[1]*rz[10]*rz[19])
log(f"sum(2cos) == 0 exactly:      {S1.is_zero}")
e2_num_check = red(S2.as_expr() + 3)          # S2 should be the constant -3
log(f"S2 == -3 exactly (=> e2 = S2/144 = -1/48): {e2_num_check.is_zero}")
c9_poly = z**3 + z**24                        # = 2*cos(2*pi/9) reduced mod Phi_27
S3_minus_c9 = red(S3.as_expr() - c9_poly)
log(f"S3 == z^3+z^-3 (=2cos(2pi/9)) exactly: {S3_minus_c9.is_zero}")
assert S1.is_zero and e2_num_check.is_zero and S3_minus_c9.is_zero, "re-derivation failed"

E1 = Rational(0, 1)
E2 = Rational(-3, 144)   # e2 = S2/144 with S2 = -3 (verified above, unreduced pair)
assert E2 == Rational(-1, 48), f"e2 recompute mismatch: got {E2}"
DEN3 = 1728
NUM3_COEFF = 1                  # coefficient of c9 in e3 = (1*c9)/1728, constant term 0
c9 = 2*cos(2*pi/9)
e3_float = float(c9) / DEN3
log(f"e3 = (1*c9)/1728,  c9 = 2cos(2pi/9),  numeric e3 = {e3_float:.15f}")
assert math.gcd(NUM3_COEFF, DEN3) == 1
log(f"e3 numerator coefficient (lowest terms): {NUM3_COEFF}   denominator: {DEN3}")
log(f"e1 = {E1}   e2 = {E2}   (= S2/144, S2=-3, UNREDUCED pair (-3,144))")

# minimal polynomial and discriminant of c9 = 2cos(2*pi/9), computed in-cell
mp = minimal_polynomial(c9, Symbol('x'))
log(f"minimal polynomial of c9 = 2cos(2pi/9):  {mp} = 0")
disc_c9 = discriminant(Poly(mp, Symbol('x')))
log(f"discriminant of that minimal polynomial: {disc_c9}")

# ============================================================ 1b. SELF-TEST:
# the W2-SENT defect and its fix are not vacuous. Substituting the OLD buggy
# pair (-3, 48) for the FIXED pair (-3, 144) must change the asserted value --
# if it didn't, the "fix" would be a no-op / tautological theater.
log("=== self-test: W2-SENT's e2 pair was a genuine defect (not vacuous) ===")
OLD_BUGGY_PAIR = Fraction(-3, 48)     # what W2-SENT's SET_A literally encoded
FIXED_PAIR = Fraction(-3, 144)        # the true unreduced pair, this cell
TRUE_E2 = Fraction(-1, 48)
log(f"  old buggy pair value  -3/48  = {OLD_BUGGY_PAIR}  (== true e2 {TRUE_E2}? {OLD_BUGGY_PAIR == TRUE_E2})")
log(f"  fixed pair value     -3/144  = {FIXED_PAIR}  (== true e2 {TRUE_E2}? {FIXED_PAIR == TRUE_E2})")
assert OLD_BUGGY_PAIR != TRUE_E2, "self-test failed: old pair should NOT equal true e2 (else no real bug existed)"
assert FIXED_PAIR == TRUE_E2, "self-test failed: fixed pair must equal true e2"
log("  self-test PASS: old pair genuinely wrong (-1/16 != -1/48); fixed pair genuinely correct.")

# ============================================================ 2. gather integers,
# split cleanly into two categories (conflating them is exactly the error the
# predicates must not be judged by -- MB12 vacuity discipline):
#
#   SET A -- ARITHMETIC content: numerators/denominators of the rational quantities
#            e1,e2,e3 actually equal (UNREDUCED as produced by the derivation, so
#            no re-splitting artifact can sneak in), plus the discriminant of the
#            minimal polynomial of e3's algebraic numerator element c9.
#   SET B -- LABEL/INDEX content: the level N, order O1, the root-index set K, the
#            mod-405 triple-class labels, the mod-45 residue selector. Pre-existing
#            bookkeeping constants (banked in B399, before e3 was ever identified)
#            that select/name cells; not numerators or denominators of any Gram
#            quantity. Scanned and reported for full transparency (so a real hit
#            is never silently missed) but explicitly EXCLUDED from the fire
#            decision, since none of the three predicates are stated in terms of
#            index labels.
SET_A = dict(e1_num=0, e1_den=1,
             e2_num=-3, e2_den=144,          # <-- FIXED: unreduced pair, S2/144
             e3_num=NUM3_COEFF, e3_den=DEN3,
             minpoly_c9_discriminant=int(disc_c9))
SET_B = dict(level_N=1215, order_O1=1620, mod45_residue=31, k_root_indices=list(K),
             triple_classes=[121, 256, 391], cyclotomic_index=27,
             subfield_degree_index=9)

def prime_union(d):
    s = set()
    for name, val in d.items():
        vals = val if isinstance(val, list) else [val]
        for v in vals:
            if v not in (0, 1, -1):
                s |= set(factorint(abs(v)).keys())
    return s

log("=== SET A: arithmetic content of e1,e2,e3 (numerators/denominators/discriminant) ===")
for name, val in SET_A.items():
    log(f"  {name} = {val}: factors {factorint(abs(val)) if val not in (0,1,-1) else '(unit/zero)'}")
PRIMES_A = prime_union(SET_A)
log(f"  Set A prime union: {sorted(PRIMES_A)}")
# cross-check: Set A prime union must be independent of reduced-vs-unreduced
# representation of e2 (2,3 either way) -- verify explicitly in-cell.
PRIMES_A_reduced_e2 = prime_union(dict(SET_A, e2_num=-1, e2_den=48))
log(f"  cross-check (reduced e2 pair -1/48 instead): prime union = {sorted(PRIMES_A_reduced_e2)}  "
    f"(matches unreduced pair: {PRIMES_A_reduced_e2 == PRIMES_A})")
assert PRIMES_A_reduced_e2 == PRIMES_A, "reduced vs unreduced e2 pair must give the same prime union"

log("=== SET B: label/index content (pre-existing bookkeeping, NOT Gram arithmetic) ===")
for name, val in SET_B.items():
    if isinstance(val, list):
        for v in val:
            log(f"  {name} entry {v}: factors {factorint(v) if v not in (0,1) else '(unit)'}")
    else:
        log(f"  {name} = {val}: factors {factorint(val) if val not in (0,1) else '(unit)'}")
PRIMES_B = prime_union(SET_B)
log(f"  Set B prime union: {sorted(PRIMES_B)}  "
    f"(NOT eligible for the sentinel predicates -- index labels, not Gram quantities)")

ALL_PRIMES_PRESENT = PRIMES_A   # the sentinel-eligible pool is Set A only
log(f"sentinel-eligible prime pool (Set A only): {sorted(ALL_PRIMES_PRESENT)}")
log(f"for the record, Set B \\ Set A (labels that would be false positives if "
    f"wrongly conflated with Gram arithmetic): {sorted(PRIMES_B - PRIMES_A)}")

# ============================================================ 3. the three sentinels
log("=== sentinel checks ===")
RESULTS = {}

# --- B403: 17 or 19 as a NUMERATOR prime of a rational Gram/seam-channel quantity ---
e3_den_factors = factorint(DEN3)
e2_den_factors = factorint(144)
b403_numerator_primes = set()  # NUM3_COEFF=1 (unit) contributes nothing; e2 numerator -3 -> {3}
b403_numerator_primes |= set(factorint(3).keys())
b403_fire = bool({17, 19} & b403_numerator_primes)
log(f"B403: e3 denominator 1728 factors = {e3_den_factors} ({'2,3-smooth' if set(e3_den_factors)<= {2,3} else 'NOT smooth'})")
log(f"B403: e2 denominator 144 (unreduced) factors = {e2_den_factors}")
log(f"B403: numerator primes found across e1,e2,e3 = {sorted(b403_numerator_primes)} "
    f"(e3 numerator coeff = 1, a unit, contributes none)")
log(f"B403: registered set {{17,19}} intersect numerator primes = "
    f"{sorted({17,19} & b403_numerator_primes)}  => "
    f"{'FIRES' if b403_fire else 'no fire (PASS)'}")
log("B403 near-miss (recorded, does not satisfy the predicate): k=19 is one of the "
    "root-index labels {1,10,19} identifying class 256 -- an index, not a numerator "
    "prime factor; the registered predicate is specifically about numerator prime "
    "factors, so this does NOT count as a fire.")
RESULTS['B403'] = dict(
    predicate="17 or 19 divides a seam-channel numerator",
    fired=b403_fire,
    evidence=dict(e3_numerator=NUM3_COEFF, e3_denominator_factors=e3_den_factors,
                  e2_numerator=-3, e2_denominator_factors=e2_den_factors,
                  numerator_primes_found=sorted(b403_numerator_primes),
                  near_miss_k19_is_index_not_numerator=True),
)

# --- B405: an exceptional (non-{2,3,5}) prime in the level-1215 identification
# lands on {7,23,31,79,167} ---
SUPERSINGULAR_15A1 = json.load(open(
    os.path.join(HERE, "..", "..", "..", "B405_supersingular_check",
                 "sentinels.json")))["supersingular_below_200"]
log(f"B405: banked supersingular_below_200 (15a1) = {SUPERSINGULAR_15A1}")
exceptional_candidates = ALL_PRIMES_PRESENT - {2, 3, 5}
log(f"B405: primes in the e1/e2/e3 identification outside the predicted-smooth "
    f"{{2,3,5}} set = {sorted(exceptional_candidates)}  "
    f"(this is the candidate pool of 'exceptional primes' to test)")
b405_fire_primes = exceptional_candidates & set(SUPERSINGULAR_15A1)
b405_fire = bool(b405_fire_primes)
log(f"B405: {{2,3,5}}-exceptional primes intersect supersingular sentinel list = "
    f"{sorted(b405_fire_primes)}  => "
    f"{'FIRES' if b405_fire else 'no fire (PASS -- no exceptional prime exists to test)'}")
RESULTS['B405'] = dict(
    predicate="an exceptional (non-{2,3,5}) prime in the level-1215 identification "
              "lands on the 15a1 supersingular list",
    fired=b405_fire,
    evidence=dict(exceptional_candidates=sorted(exceptional_candidates),
                  supersingular_list=SUPERSINGULAR_15A1,
                  intersection=sorted(b405_fire_primes)),
)

# --- B406: does "the 1215-triple identification" (e1,e2,e3, exactly this object)
# surface 31 anywhere in its NEW arithmetic content? ---
b406_fire = 31 in ALL_PRIMES_PRESENT
log(f"B406: is 31 among the primes appearing in the e1/e2/e3 exact identification? "
    f"{31 in ALL_PRIMES_PRESENT}")
log(f"B406: full prime set again for reference = {sorted(ALL_PRIMES_PRESENT)}")
log(f"B406: registered consequence if fired = simultaneous death of Chat-1's E2 "
    f"'split-principal primes absent from the program' row AND a live B405 sentinel "
    f"firing (31 is on both the E2 list and the supersingular list) => "
    f"{'FIRES -- both collide' if b406_fire else 'no fire (PASS)'}")
log(f"B406 note: Set B's mod45_residue=31 is PRE-EXISTING banked structure (the "
    f"level-1215 support's residue-class gate, banked in B399 before OI-031/this "
    f"cell ever ran) -- not new content surfaced BY the triple identification, and "
    f"not a Gram-quantity numerator/denominator either. It is scanned and logged "
    f"above (Set B) for completeness/honesty but is explicitly excluded from "
    f"ALL_PRIMES_PRESENT (Set A only). 31 in Set B \\ Set A: {31 in (PRIMES_B - PRIMES_A)} "
    f"(recorded near-miss, does not satisfy the predicate). The predicate concerns "
    f"what the IDENTIFICATION of e1,e2,e3 itself arithmetically equals; "
    f"e1=0, e2=-1/48, e3=(1*c9)/1728, discriminant 81 introduce no 31.")
RESULTS['B406'] = dict(
    predicate="31 surfaces in the 1215-triple (e1,e2,e3) identification",
    fired=b406_fire,
    evidence=dict(prime_union=sorted(ALL_PRIMES_PRESENT),
                  mod45_residue_is_preexisting_not_new=True),
)

# ============================================================ 4. verdict
log("=== verdict ===")
any_fired = any(r['fired'] for r in RESULTS.values())
for name, r in RESULTS.items():
    log(f"  {name}: {'FIRED' if r['fired'] else 'PASS'}  ({r['predicate']})")
verdict = "RESOLVED-B" if any_fired else "RESOLVED-A"
log(f"VERDICT: {verdict}")
log(f"CARRY-FIX CONSEQUENCE: correcting W2-SENT's e2 pair from the buggy (-3,48) "
    f"[=-1/16] to the true (-3,144)=(-1,48) [=-1/48] leaves the sentinel-eligible "
    f"prime pool unchanged ({{2,3}} either way, since 48=2^4*3 and 144=2^4*3^2 share "
    f"the same prime support) -- so all three sentinel verdicts are UNCHANGED from "
    f"W2-SENT's (all PASS), but they are now sound: computed from the correct value "
    f"of e2 rather than by accident matching despite a wrong intermediate fraction.")

summary = dict(
    cell="W3-SENT",
    target="e1=0, e2=-1/48 (CORRECTED pair -3/144), e3=cos(2*pi/9)/864=(1*c9)/1728 "
           "in Q(zeta9)+ (OI-031, RESOLVED-A)",
    carry_fix="W2-SENT SET_A e2 pair (-3,48)=[-1/16, WRONG] -> (-3,144)=[-1/48, CORRECT]",
    e1=str(E1), e2=str(E2), e3_form="(1*c9)/1728", e3_numeric=e3_float,
    minpoly_c9=str(mp), minpoly_c9_discriminant=int(disc_c9),
    set_A_arithmetic_primes=sorted(PRIMES_A),
    set_B_label_primes_excluded=sorted(PRIMES_B),
    sentinel_eligible_pool=sorted(ALL_PRIMES_PRESENT),
    sentinels=RESULTS,
    any_fired=any_fired,
    verdict=verdict,
)
print(json.dumps(summary, indent=1, default=str))
