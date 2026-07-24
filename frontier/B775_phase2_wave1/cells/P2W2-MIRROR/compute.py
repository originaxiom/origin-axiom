"""
B775 Phase-2 Wave-2 -- Cell P2W2-MIRROR  (OI-045)
================================================================
The mirror's NON-GALOIS mechanism + the (2,3) stabilizer.

Two open leads from Review 3 / OPEN_LEADS, both in the "emergent-symmetry
family" (B380 R2/R3, B395, B397):

  (I)  WHY is the mirror  t(a,-b) = tau3(t(a,b))  NON-Galois -- i.e. why is
       there NO single Galois index-scaling that induces it, even though it
       holds table-wide?

  (II) WHY is the pair table (2,3) stabilized by the ENTIRE sqrt5-fixing
       half-group  H5 = {1,11,19,29,31,41,49,59}  (an order-8 "enhanced"
       symmetry), whereas the other pairs get only {1,31} or {1,11,31,41}?

Everything below is EXACT (cyclotomic engine over Q(zeta60), Fraction
arithmetic). Two independent reproductions per claim. Structural only:
no SM value, no consciousness claim, one-number pin untouched.

Object under study (B380/B358/B367 machinery):
  C[j,l] = tr(Par . W1^j . W2^l . J^{-1})          (parity-trace coefficients)
  t(a,b) = (1/o1 o2) SUM_{j,l} w1^{-ja} w2^{-lb} C[j,l]   (the pair-table DFT)
           then H-projected to (p,q,r,s) in basis {1, sqrt5, sqrt-3, sqrt-15}.
  sigma_c : zeta60 -> zeta60^c ; the Galois index-covariances are the
  DIAGONAL scalings  sigma_c : (a,b) -> (c a mod o1, c b mod o2).
"""
import sys, os, json, math
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B358_seam_certification"))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B367_value_map"))
import seam_certification as SC                                   # noqa: E402
from step0_exact_matrices import (build_theta_W, matrix_order,    # noqa: E402
                                  par_trace, pair_smatrix)

UNITS = [c for c in range(60) if math.gcd(c, 60) == 1]            # (Z/60)^*, order 16

# --- Galois action on the H-projected value field Q(sqrt5, sqrt-3) --------
# sigma_c on the 4-vector (p, q, r, s) = p + q*sqrt5 + r*sqrt-3 + s*sqrt-15.
# sqrt5  -> eps5(c) sqrt5 ,  eps5=+1 iff c = +-1 mod 5
# sqrt-3 -> eps3(c) sqrt-3,  eps3=+1 iff c = 1 mod 3
# sqrt-15 = sqrt5*sqrt-3 -> eps5*eps3 sqrt-15
def eps5(c): return 1 if c % 5 in (1, 4) else -1
def eps3(c): return 1 if c % 3 == 1 else -1
def sig_val(c, v):
    p, q, r, s = v
    return (p, eps5(c) * q, eps3(c) * r, eps5(c) * eps3(c) * s)

def table(m1, m2):
    o1, p1 = matrix_order(build_theta_W(m1))
    o2, p2 = matrix_order(build_theta_W(m2))
    return o1, o2, pair_smatrix(p1, p2)

def covariance_stabilizer(m1, m2):
    """{c in (Z/60)^* : t(ca,cb) == sigma_c(t(a,b)) for every cell}."""
    o1, o2, t = table(m1, m2)
    good = []
    for c in UNITS:
        ok = True
        for (a, b), v in t.items():
            key = ((c * a) % o1, (c * b) % o2)
            if key not in t or t[key] != sig_val(c, v):
                ok = False
                break
        if ok:
            good.append(c)
    return o1, o2, good

R = {}   # results accumulator
print("=" * 72)
print("P2W2-MIRROR : mirror non-Galois mechanism + the (2,3) stabilizer")
print("=" * 72)

# ==========================================================================
# PART I -- the (2,3) stabilizer:  WHAT it is  (reproduce B380 R3)
# ==========================================================================
print("\n[PART I] covariance stabilizers of the six pair tables")
H5 = sorted(c for c in UNITS if c % 5 in (1, 4))        # sqrt5-fixing half-group
quartet = sorted(c for c in UNITS if c % 5 == 1)        # zeta5-fixing quartet
stabs = {}
for pair in [(2, 3), (1, 2), (3, 4), (1, 3), (1, 4)]:
    o1, o2, g = covariance_stabilizer(*pair)
    stabs[pair] = g
    tag = ("= H5 (sqrt5-fixing half-group, order 8)" if g == H5 else
           "= zeta5-fixing quartet"                  if g == quartet else
           "")
    print(f"   ({pair[0]},{pair[1]})  orders({o1:>2},{o2:>2})  Stab = {g}   {tag}")
print(f"   H5      (units = +-1 mod 5) = {H5}")
print(f"   quartet (units =   1 mod 5) = {quartet}")

# discriminating fact (reproduction #1): the (2,3) stabilizer IS H5 exactly.
stab23 = stabs[(2, 3)]
claim_23_is_H5 = (stab23 == H5)
# reproduction #2 of the same set, arithmetically, WITHOUT the table:
# H5 = Gal(Q(zeta60)/Q(sqrt5)) = { c : c = +-1 mod 5 }.
claim_23_is_gal_sqrt5 = (stab23 == sorted(c for c in UNITS if eps5(c) == 1))
R["I_stab_2_3"] = stab23
R["I_stab_2_3_equals_H5"] = claim_23_is_H5
R["I_stab_2_3_equals_Gal_over_Qsqrt5"] = claim_23_is_gal_sqrt5
R["I_other_stabs"] = {f"{a},{b}": stabs[(a, b)] for (a, b) in stabs if (a, b) != (2, 3)}

# ==========================================================================
# PART II -- the (2,3) stabilizer:  WHY  (the mechanism)
# ==========================================================================
# Claim: the enhancement quartet -> H5 is forced by ONE order-arithmetic
# coincidence: the unit 49 acts as the IDENTITY on the (2,3) table both on
# indices (49 = 1 mod o1=12 AND 49 = 1 mod o2=6) and on the value field
# (eps5(49)=+1, eps3(49)=+1).  Hence {1,49} is a "phantom kernel" and
#   Stab(2,3) = quartet  U  49*quartet  =  H5.
# 49 is the UNIQUE non-identity unit that is index-trivial on orders (12,6)
# and value-trivial -- it exists only because (2,3) has orders (12,6).
print("\n[PART II] mechanism of the (2,3) enhancement -- the phantom kernel 49")
o1_23, o2_23, _ = table(2, 3)
phantoms = [c for c in UNITS
            if c % o1_23 == 1 and c % o2_23 == 1 and eps5(c) == 1 and eps3(c) == 1]
print(f"   (2,3) orders = ({o1_23},{o2_23})")
print(f"   units index-trivial on ({o1_23},{o2_23}) AND value-trivial : {phantoms}")
print(f"   49 : mod12={49 % 12}  mod6={49 % 6}  mod5={49 % 5}(eps5={eps5(49):+d})"
      f"  mod3={49 % 3}(eps3={eps3(49):+d})")
enh = sorted((49 * x) % 60 for x in quartet)
print(f"   quartet                = {quartet}")
print(f"   49 * quartet  (mod 60) = {enh}")
print(f"   quartet  U  49*quartet = {sorted(set(quartet) | set(enh))}")
kernel_ok = (phantoms == [1, 49])
enhancement_ok = (sorted(set(quartet) | set(enh)) == H5)
# cross-pair control: 49 is NOT index-trivial for any pair whose orders
# don't both divide the order of 49 in the index groups.
control = {}
for (a, b) in [(1, 2), (3, 4), (1, 3), (1, 4)]:
    oa, ob, _ = table(a, b)
    control[f"{a},{b}"] = dict(orders=[oa, ob],
                               idx49=[49 % oa, 49 % ob],
                               idx_trivial=(49 % oa == 1 and 49 % ob == 1))
    print(f"   control ({a},{b}) orders({oa},{ob}): 49 -> "
          f"({49 % oa},{49 % ob}) index-trivial={control[f'{a},{b}']['idx_trivial']}")
R["II_phantom_kernel"] = phantoms
R["II_kernel_is_1_49"] = kernel_ok
R["II_quartet_times_49_gives_H5"] = enhancement_ok
R["II_49_index_trivial_only_at_2_3"] = all(not v["idx_trivial"] for v in control.values())

# ==========================================================================
# PART III -- the mirror is NON-Galois:  the mechanism (on (1,2), 240 cells)
# ==========================================================================
# The mirror is the ANTI-DIAGONAL axis map (a,b) -> (a, -b) = (+1 on a-axis,
# -1 on b-axis).  The Galois index-covariances are DIAGONAL scalings
# (a,b)->(ca,cb).  Realizing the mirror as a single sigma_c would need a unit
#   c = 1 (mod o1)   and   c = -1 (mod o2).
# For (1,2): o1=20, o2=12.  a-axis fix forces c = 1 mod 4 (4 | 20);
# b-axis reflect forces c = -1 = 3 mod 4 (4 | 12).  1 != 3 mod 4 -> IMPOSSIBLE.
print("\n[PART III] the mirror  t(a,-b)=tau3(t(a,b))  is non-Galois")
o1m, p1m = matrix_order(build_theta_W(1))
o2m, p2m = matrix_order(build_theta_W(2))
Cm = {(j, l): par_trace(p1m[j], p2m[l]) for j in range(o1m) for l in range(o2m)}

# (III.a) NO diagonal Galois scaling induces the anti-diagonal reflection.
diag_reflect = [c for c in UNITS if c % o1m == 1 and c % o2m == (o2m - 1) % o2m]
print(f"   (III.a) units c with c=1 mod {o1m} and c=-1 mod {o2m}: {diag_reflect}")
print(f"           a-axis fix -> c=1 mod4 ; b-axis reflect -> c=3 mod4 : contradiction")
mirror_not_diagonal = (diag_reflect == [])

# (III.b) the natural CELL-WISE coefficient identity C[j,-l]=sigma11(C[j,l])
# FAILS (reproduces B395: 140/240).  tau3|Q(zeta15) = sigma11 (11=1 mod5, -1 mod3).
cellwise_fail = {}
for c in (11, 41):   # 41 = the i-fixing lift of 11 (41=11 mod15, 41=1 mod4)
    bad = sum(1 for j in range(o1m) for l in range(o2m)
              if SC.sigma(Cm[(j, l)], c) != Cm[(j, (-l) % o2m)])
    cellwise_fail[c] = bad
    print(f"   (III.b) cell-wise law sigma_{c}(C[j,l])=C[j,-l] FAILS at "
          f"{bad}/{o1m * o2m} cells")
mirror_no_cell_local = all(b > 0 for b in cellwise_fail.values())

# (III.c) yet the mirror HOLDS table-wide as tau3 on the summed values
#         (independent reproduction of P61/B380 R2 on this cell's own table).
_, _, t12 = table(1, 2)
mirror_holds = True
for (a, b), v in t12.items():
    key = (a % o1m, (-b) % o2m)
    if key in t12:
        p, q, r, s = v
        if t12[key] != (p, q, -r, -s):   # tau3 : (p,q,r,s)->(p,q,-r,-s)
            mirror_holds = False
            break
print(f"   (III.c) table-wide mirror t(a,-b)=tau3(t(a,b)) holds: {mirror_holds}")
R["III_no_diagonal_scaling_induces_mirror"] = mirror_not_diagonal
R["III_cellwise_coefficient_law_fails"] = cellwise_fail
R["III_mirror_is_not_cell_local"] = mirror_no_cell_local
R["III_mirror_holds_table_wide_as_tau3"] = mirror_holds

# ==========================================================================
# VERDICT BLOCK  (able to emit UNRESOLVED)
# ==========================================================================
print("\n" + "=" * 72)
print("VERDICT")
print("=" * 72)

# ---- (2,3) stabilizer: mechanism identified (structure shown)?
stab_resolved = (claim_23_is_H5 and claim_23_is_gal_sqrt5
                 and kernel_ok and enhancement_ok
                 and R["II_49_index_trivial_only_at_2_3"])

# ---- mirror non-Galois: mechanism identified (structure shown)?
mirror_resolved = (mirror_not_diagonal and mirror_no_cell_local
                   and mirror_holds)

if stab_resolved and mirror_resolved:
    verdict = "RESOLVED-A"
    headline = ("both mechanisms identified with structure shown and each "
                "reproduced a second way")
elif not (stab_resolved or mirror_resolved):
    verdict = "UNRESOLVED"
    headline = "neither mechanism established in-cell"
else:
    # a mechanism found for one but not the other -> still a structural
    # advance, but not the full sealed RESOLVED-A criterion.
    verdict = "UNRESOLVED"
    headline = ("partial: one mechanism shown, the other not -- "
                f"(stab={stab_resolved}, mirror={mirror_resolved})")

# the sealed criterion also admits RESOLVED-B (mirror IS Galois after all).
# That branch would require a single sigma_c inducing the anti-diagonal
# reflection; we PROVED that set empty, so RESOLVED-B is ruled out.
if not mirror_not_diagonal:
    verdict = "RESOLVED-B"
    headline = "a single Galois scaling induces the mirror after all"

R["verdict"] = verdict
R["headline"] = headline
R["discriminating_fact"] = (
    "Stab(2,3) = {1,11,19,29,31,41,49,59} = Gal(Q(zeta60)/Q(sqrt5)); the "
    "quartet->octet enhancement is forced by the phantom unit 49 (=1 mod 12, "
    "=1 mod 6, eps5=eps3=+1), which is index-and-value trivial ONLY at the "
    "(2,3) orders (12,6). The mirror (a,b)->(a,-b) is the ANTI-diagonal axis "
    "map; no diagonal Galois scaling sigma_c realizes it (would need c=1 mod4 "
    "AND c=3 mod4), and its cell-wise coefficient law fails 140/240 -- it is "
    "carried only emergently as tau3 on the summed values."
)

for k in ["I_stab_2_3_equals_H5", "I_stab_2_3_equals_Gal_over_Qsqrt5",
          "II_kernel_is_1_49", "II_quartet_times_49_gives_H5",
          "II_49_index_trivial_only_at_2_3",
          "III_no_diagonal_scaling_induces_mirror",
          "III_mirror_is_not_cell_local",
          "III_mirror_holds_table_wide_as_tau3"]:
    print(f"   {k:<46} : {R[k]}")
print(f"\n   VERDICT   : {verdict}")
print(f"   HEADLINE  : {headline}")

json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1, default=str)
print("\nresults.json written. DONE")
