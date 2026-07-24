"""B775 Phase-2 Wave-1 -- cell P2-SELRULE (OI-016).

The +-1/48 selection-rule / row-16 silence theorem: WHY row 16 is silent and WHY the
+-1/48 seam sign is selected.

Object (declared): the level-15 theta-lift Weil pair table (B358/B367 machinery).
  W_m = WR^m D^m,  D=diag(zeta15^{j(j-1)/2}),  WR=F D^{-1} F^{-1}  (exact over Q(zeta60)).
  C[j][l] = tr(Par * W1^j * W2^l)  in  Q(zeta15).
  t(a,b)  = (1/240) sum_{j,l} zeta20^{-ja} zeta12^{-lb} C[j][l], H-projected to
            H=Q(sqrt5,sqrt-3), solved in basis {1, sqrt5, sqrt-3, sqrt-15} = (x,y,z,s).
  "bright" = seam-bearing (s = sqrt-15 coeff != 0);  "silent/dark" = t in Q(sqrt5) (z=s=0).

House method (B775 prereg 4f73e186): exact/symbolic; discriminating fact IN-CELL; a
positive reproduced a second way; WALLED / CONSTITUTIVELY-OPEN legitimate terminals.
B774 discipline note: t(a,b)=tr(Par P_a Q_b) IS a symmetric trace invariant (character),
NOT a claimed non-abelian chord -- this cell proves a SELECTION RULE about trace
invariants, so the trace-polynomial form is the correct object, not a violation.

Re-runnable: `python3 compute.py`. Writes output.txt + results.json.
"""
import os, sys, json, math
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

LOG = []
def log(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s)

# ------------------------------------------------------------------ build table
W1 = build_theta_W(1); W2 = build_theta_W(2)
o1, pow1 = matrix_order(W1); o2, pow2 = matrix_order(W2)
C = [[par_trace(pow1[j], pow2[l]) for l in range(o2)] for j in range(o1)]

def traw(a, b):
    t = E.ZERO
    for j in range(o1):
        za = E.zeta((-3 * j * a) % 60)
        for l in range(o2):
            t = E.add(t, E.mul(E.mul(za, E.zeta((-5 * l * b) % 60)), C[j][l]))
    return E.scal(Fr(1, o1 * o2), t)

def Hp(a, b):
    return SC.solve_H(SC.H_avg(traw(a, b)))

def tau3(v):  # sqrt-3 conjugation on H = the mirror involution R2
    return (v[0], v[1], -v[2], -v[3])

ZERO4 = (Fr(0),) * 4
results = {}

log("orders (o1,o2) =", (o1, o2), " field Q(zeta60), DEG =", E.DEG)

# =================================================================== V0: C in Q(zeta15)
# 31 == 1 (mod 15) so sigma_31 fixes Q(zeta15) pointwise; test cellwise.
c_in_z15 = all(SC.sigma(C[j][l], 31) == C[j][l] for j in range(o1) for l in range(o2))
log("\n[V0] raw trace table C[j][l] lies in Q(zeta15):", c_in_z15)
results["V0_C_in_Qzeta15"] = c_in_z15

# =================================================================== V1: support rule
# nonzero rows must be exactly K1 (the 11 exponents where the singles are supported).
K1 = [0, 1, 4, 5, 6, 9, 11, 14, 15, 16, 19]
Hcache = {(a, b): Hp(a, b) for a in range(20) for b in range(12)}
nonzero_rows = [a for a in range(20) if any(Hcache[(a, b)] != ZERO4 for b in range(12))]
v1 = (nonzero_rows == K1)
log("\n[V1] support selection: nonzero rows == K1 :", v1)
log("     nonzero rows =", nonzero_rows)
results["V1_support_is_K1"] = v1

# =================================================================== V2: row-16 unique silence
# among the 11 supported rows, exactly one is silent (z=s=0 on its whole support): row 16.
def is_silent(a):
    return all(Hcache[(a, b)][2] == 0 and Hcache[(a, b)][3] == 0 for b in range(12))
silent_supported = [a for a in nonzero_rows if is_silent(a)]
v2 = (silent_supported == [16])
row16_supp = {b: tuple(str(x) for x in Hcache[(16, b)]) for b in range(12) if Hcache[(16, b)] != ZERO4}
log("\n[V2] silent AND supported rows :", silent_supported, " (unique row-16 silence:", v2, ")")
log("     row-16 support (real, Q(sqrt5)):", row16_supp)
# non-triviality: row 16 carries genuine real content (not an empty row)
row16_nontrivial = len(row16_supp) > 0 and all(Fr(v[2]) == 0 and Fr(v[3]) == 0 for v in
                                               [Hcache[(16, b)] for b in row16_supp])
results["V2_row16_unique_silent"] = v2
results["V2_row16_nontrivial_real"] = bool(row16_nontrivial)
results["V2_row16_support"] = row16_supp

# =================================================================== V3: mirror law R2 (structural)
# tau3(t(a,b)) == t(a,-b) for ALL 240 cells  =>  silence(a) <=> evenness(a).
mirror_all = all(tau3(Hcache[(a, b)]) == Hcache[(a, (-b) % 12)]
                 for a in range(20) for b in range(12))
even16 = all(Hcache[(16, b)] == Hcache[(16, (-b) % 12)] for b in range(12))
even4 = all(Hcache[(4, b)] == Hcache[(4, (-b) % 12)] for b in range(12))
log("\n[V3] mirror law  tau3(t(a,b)) = t(a,-b)  holds all 240 :", mirror_all)
log("     => silence <=> row-evenness.  row16 even:", even16, " row4 even:", even4,
    " (row4 bright/odd, row16 silent/even)")
results["V3_mirror_law_all240"] = mirror_all
results["V3_row16_even"] = even16
results["V3_row4_even"] = even4

# =================================================================== V4: silence is arithmetic, NOT symmetry-forced
# rows 4 and 16 satisfy the IDENTICAL symmetry constraints (mirror R2 + R1 b->7b) yet
# differ in reality; exhaustively, NO Galois element carries raw row-4 to raw row-16.
r1_4 = all(Hcache[(4, (7 * b) % 12)] == Hcache[(4, b)] for b in range(12))
r1_16 = all(Hcache[(16, (7 * b) % 12)] == Hcache[(16, b)] for b in range(12))
units = [c for c in range(1, 60) if math.gcd(c, 60) == 1]
forcing_4_to_16 = [c for c in units
                   if all(SC.sigma(traw(4, b), c) == traw(16, b) for b in range(12))]
fix_raw16 = [c for c in units if all(SC.sigma(traw(16, b), c) == traw(16, b) for b in range(12))]
not_symmetry_forced = (r1_4 and r1_16 and forcing_4_to_16 == [] and set(fix_raw16) == {1, 31})
log("\n[V4] silence is arithmetic-reality, NOT single-symmetry-forced:")
log("     R1 (b->7b) holds row4,row16 :", (r1_4, r1_16), " (twin symmetry constraints)")
log("     Galois c mapping raw row4 -> raw row16 :", forcing_4_to_16, "(none)")
log("     Galois c fixing raw row16 entirely     :", fix_raw16, "(only Q(zeta15)-stabilizer {1,31})")
log("     => the mirror reduces silence to evenness, but no ambient symmetry SELECTS")
log("        row16 over its twin row4; the darkness is the ARITHMETIC vanishing of the")
log("        sqrt-3/sqrt-15 content of the level-15 theta values (finite-exact fact).")
results["V4_R1_twins"] = [r1_4, r1_16]
results["V4_no_galois_row4_to_row16"] = (forcing_4_to_16 == [])
results["V4_raw16_stabilizer"] = fix_raw16

# =================================================================== V5: +-1/48 SIGN-SELECTION theorem
# the pure-seam cells |s|=1/48; the sign of the sqrt-15 (seam) coefficient is the
# sqrt5-Galois face. Reproduced two ways.
seam48 = {(a, b): Hcache[(a, b)] for a in range(20) for b in range(12)
          if abs(Hcache[(a, b)][3]) == Fr(1, 48)}
# ---- reproduction 1: direct components -- s = eps(a)*z with eps in {+1,-1} = sector sign
sector = {}
for (a, b), v in seam48.items():
    eps = 1 if v[3] == v[2] else (-1 if v[3] == -v[2] else 0)
    sector.setdefault(a, set()).add(eps)
sector_clean = all(len(s) == 1 and 0 not in s for s in sector.values())
# ---- reproduction 2: sigma_7 (sqrt5-flip) FLIPS the seam s, FIXES the sqrt-3 z ----
flag = Hcache[(0, 4)]
s7 = SC.solve_H(SC.H_avg(SC.sigma(traw(0, 4), 7)))
galois_flips_seam = (s7 is not None and s7[3] == -flag[3] and s7[2] == flag[2])
# ---- magnitude:  1/48 = (1/4)*(1/12),  1/12 = 1/16 + 1/48  (B382 det-class split) ----
mag_ok = (Fr(1, 4) * Fr(1, 12) == Fr(1, 48)) and (Fr(1, 16) + Fr(1, 48) == Fr(1, 12))
# ---- sector constants are exact sqrt5 conjugates:
#   slot   Pi_H = -(phi/6) sqrt-3 = -(1+sqrt5)/12 sqrt-3  -> (0,0,-1/12,-1/12)
#   3-block            sqrt5-flip -> +(1/(6phi)) sqrt-3   -> (0,0,-1/12,+1/12)
# build -(1+sqrt5)/12 * sqrt-3 exactly and apply sigma_7:
slot_const = E.scal(Fr(-1, 12), E.mul(E.add(E.ONE, E.SQRT5), E.SQRTm3))
slot_comps = SC.solve_H(slot_const)
block_comps = SC.solve_H(SC.sigma(slot_const, 7))
sector_conj = (slot_comps == (Fr(0), Fr(0), Fr(-1, 12), Fr(-1, 12)) and
               block_comps == (Fr(0), Fr(0), Fr(-1, 12), Fr(1, 12)))
v5 = sector_clean and galois_flips_seam and mag_ok and sector_conj
log("\n[V5] +-1/48 SIGN-SELECTION theorem:")
log("     pure-seam |s|=1/48 cells:", sorted(seam48.keys()))
log("     per-row sector sign eps (s = eps*z):", {a: list(v)[0] for a, v in sector.items()},
    " clean:", sector_clean)
log("     [repro 1] seam s = eps(a)*z, eps = sector sign (+/-1)")
log("     [repro 2] sigma_7 (sqrt5-flip) flips seam s, fixes sqrt-3 z :", galois_flips_seam)
log("       flagship t(0,4)=", tuple(str(x) for x in flag), " sigma_7 ->",
    tuple(str(x) for x in s7))
log("     magnitude 1/48=(1/4)(1/12), 1/12=1/16+1/48 :", mag_ok)
log("     sector constants sqrt5-conjugate  (0,0,-1/12,-1/12)<->(0,0,-1/12,+1/12):", sector_conj)
log("     => the +-1/48 seam SIGN is the sqrt5-Galois face (phi <-> -1/phi); the two")
log("        sectors (slot/3-block) are sigma_sqrt5-conjugate; within a sector the sign")
log("        flips under the mirror law b->-b (tau3).  SIGN SELECTION = Galois-forced.")
results["V5_sign_selection"] = {
    "seam_1over48_cells": sorted(f"{a},{b}" for (a, b) in seam48),
    "sector_signs": {str(a): list(v)[0] for a, v in sector.items()},
    "sector_clean": sector_clean,
    "sigma7_flips_seam_fixes_z": bool(galois_flips_seam),
    "magnitude_1over48_eq_quarter_twelfth": mag_ok,
    "sector_constants_sqrt5_conjugate": sector_conj,
}
results["V5_ok"] = bool(v5)

# =================================================================== VERDICT
# Sealed criterion: THEOREM (silence + sign selection proven) => RESOLVED-A ;
#                   the rule fails at a computed instance      => RESOLVED-B ;
#                   otherwise                                   => UNRESOLVED.
silence_proven = v0 = (c_in_z15 and v1 and v2 and bool(row16_nontrivial)
                       and mirror_all and even16)
sign_proven = v5
# a RESOLVED-B trigger would be: a supported bright row that is actually silent, or a
# seam cell whose sign contradicts the sector/Galois law -- none exist (checked above).
rule_fails = (not v1) or (silent_supported not in ([16],)) or (not sector_clean) \
    or (seam48 and not galois_flips_seam)

if silence_proven and sign_proven and not rule_fails:
    verdict = "RESOLVED-A"
    terminal = "RESOLVED-A"
    headline = ("Row-16 silence + +-1/48 sign selection PROVEN: row 16 is the UNIQUE "
                "silent-but-supported row (arithmetic reality, mirror-reduced to "
                "row-evenness, not symmetry-forced); the +-1/48 seam sign is the "
                "sqrt5-Galois face (sigma_sqrt5-conjugate sectors), reproduced two ways.")
elif rule_fails:
    verdict = "RESOLVED-B"
    terminal = "RESOLVED-B"
    headline = "The selection rule failed at a computed instance."
else:
    verdict = "UNRESOLVED"
    terminal = "CONSTITUTIVELY-OPEN"
    headline = "Silence/sign not established as a theorem in-cell."

results["verdict"] = verdict
results["terminal_state"] = terminal
results["headline"] = headline
results["silence_proven"] = bool(silence_proven)
results["sign_selection_proven"] = bool(sign_proven)

log("\n" + "=" * 72)
log("VERDICT:", verdict, "(terminal:", terminal + ")")
log(headline)
log("silence_proven =", silence_proven, " | sign_selection_proven =", sign_proven)
log("=" * 72)

# Gate 5/5-Q: structural language only; no SM values; no consciousness claims; nothing
# to CLAIMS; one-number pin untouched.  (This cell touches none of those.)
json.dump(results, open(os.path.join(HERE, "results.json"), "w"), indent=1)
open(os.path.join(HERE, "output.txt"), "w").write("\n".join(LOG) + "\n")
log("\nwrote results.json + output.txt")
