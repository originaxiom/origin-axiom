"""P2W4-B414 -- OI-048: the content-wall frame. Is it genuinely EXTERNAL?

Banked priors (read in-cell, re-derived from the raw tables, nothing cited):
  B400/W-B1 : golden line L _|_ Mercedes plane P in the shared W2-label space Z12.
  B422      : the Z/2 mirror does not connect them either.
  B414      : "seeing content" reduces to exactly one problem -- the frame.
Both priors are SUBSPACE-OVERLAP probes ("is the overlap nonzero?"). Overlap zero does
NOT by itself forbid a canonical MAP L -> P: orthogonal sectors can still be canonically
identified (an intertwiner is not a projection). So this cell re-poses the question at the
level of MAPS and SYMMETRY GROUPS, which is where "canonical" actually lives:

  Does the object supply a nonzero map L -> P that is equivariant for every symmetry the
  object itself supplies for the two sectors, and pinned (no free parameter)?

All arithmetic exact over Q (Fractions). Verdict block can emit RESOLVED-A / -B / UNRESOLVED.
"""
import json, os
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "..", "..", "B367_value_map", "step0_tables.json")))
N = 12
R = {}   # results

# ---------- 0. the two sectors, rebuilt in-cell from step0 (s-component) ----------
def rows_12():
    d = {}
    for k, val in T["1,2"].items():
        a, b = map(int, k.split(","))
        d.setdefault(a % 20, [Fr(0)] * N)[b % N] = Fr(val[3])
    return d
def cols_23():
    d = {}
    for k, val in T["2,3"].items():
        a, b = map(int, k.split(","))
        d.setdefault(b % 6, [Fr(0)] * N)[a % N] = Fr(val[3])
    return d
ROW, COL = rows_12(), cols_23()
g   = ROW[6]                       # golden slot row  (L = span g)
C   = [COL[0], COL[2], COL[4]]     # Mercedes triple  (P = span C)
dot = lambda u, v: sum(x * y for x, y in zip(u, v))
sc  = lambda c, v: [c * x for x in v]
add = lambda u, v: [x + y for x, y in zip(u, v)]
eqv = lambda u, v: all(x == y for x, y in zip(u, v))
sup = lambda v: frozenset(i for i, x in enumerate(v) if x != 0)

R["golden_support"]   = sorted(sup(g))
R["mercedes_support"] = sorted(set().union(*[sup(c) for c in C]))
R["supports_disjoint"] = sup(g).isdisjoint(set().union(*[sup(c) for c in C]))   # route 1 (W-B1)
R["antipodal_row14_is_minus_row6"] = eqv(ROW[14], sc(Fr(-1), g))
gram = [[dot(C[i], C[j]) for j in range(3)] for i in range(3)]
n = gram[0][0]
R["mercedes_equilateral"] = (all(gram[i][i] == n for i in range(3)) and
                             all(gram[i][j] == -n / 2 for i in range(3) for j in range(3) if i != j))
R["mercedes_sums_to_zero"] = all(sum(C[i][k] for i in range(3)) == 0 for k in range(N))

# ---------- 1. LEG 1 -- relative geometry is totally degenerate (reproduce W-B1) ----------
# principal angles between L and P: cos^2 = |proj_P g|^2 / |g|^2 (P-basis C0,C1, C2=-C0-C1)
B = [C[0], C[1]]
G2 = [[dot(B[i], B[j]) for j in range(2)] for i in range(2)]
rhs = [dot(B[i], g) for i in range(2)]
det = G2[0][0] * G2[1][1] - G2[0][1] * G2[1][0]
c0 = (rhs[0] * G2[1][1] - rhs[1] * G2[0][1]) / det
c1 = (G2[0][0] * rhs[1] - G2[1][0] * rhs[0]) / det
proj = add(sc(c0, B[0]), sc(c1, B[1]))
R["cos2_principal_angle"] = str(dot(proj, proj) / dot(g, g))
R["L_perp_P_exact"] = (dot(proj, proj) == 0)
# degenerate => EVERY unit direction of P is a "best aligned" direction: the canonical
# subspace-relating construction (principal directions / SVD) selects nothing.
R["principal_directions_selected"] = 0 if R["L_perp_P_exact"] else 2

# ---------- 2. the object's own symmetry groups of the shared label space ----------
# canonical relabelings of an exponent group Z12 = affine maps i -> u*i+t, u in (Z/12)^*.
UNITS = [u for u in range(1, N) if gcd(u, N) == 1]
def perm_act(u, t, v):                      # (pi.v)[i] = v[pi^{-1}(i)]
    ui = pow(u, -1, N)
    return [v[(ui * (i - t)) % N] for i in range(N)]
def is_sym(u, t, vecs):                     # maps the family to itself up to sign
    for v in vecs:
        im = perm_act(u, t, v)
        if not any(eqv(im, w) or eqv(im, sc(Fr(-1), w)) for w in vecs):
            return False
    return True
AFF = [(u, t) for u in UNITS for t in range(N)]
SYM_23   = [a for a in AFF if is_sym(*a, C)]
ROWS_ALL = [ROW[a] for a in sorted(ROW)]
SYM_12   = [a for a in AFF if is_sym(*a, ROWS_ALL)]
SYM_JOINT = [a for a in SYM_23 if a in SYM_12]
R["sym_23_affine"]  = SYM_23
R["sym_12_affine"]  = SYM_12
R["sym_joint"]      = SYM_JOINT
# the Z/3: translation by 4 cycles the Mercedes columns EXACTLY (sign +1)
tau = lambda v: perm_act(1, 4, v)
R["tau_cycles_mercedes"] = (eqv(tau(C[0]), C[2]) and eqv(tau(C[2]), C[1]) and eqv(tau(C[1]), C[0])) or \
                           (eqv(tau(C[0]), C[1]) and eqv(tau(C[1]), C[2]) and eqv(tau(C[2]), C[0]))
R["tau_in_sym_23"]  = (1, 4) in SYM_23
R["tau_in_sym_12"]  = (1, 4) in SYM_12          # expected False -> the incompatibility
R["tau_g_matches_a_banked_row"] = any(eqv(tau(g), ROW[a]) or eqv(tau(g), sc(Fr(-1), ROW[a]))
                                      for a in ROW)

# ---------- 3. LEG 2 -- the Mercedes Z/3 is FIXED-POINT-FREE on P ----------
# matrix of tau on P in basis (C0,C1), using C2 = -C0-C1
def coords_P(v):                            # exact coordinates of v in basis (C0,C1)
    r = [dot(B[0], v), dot(B[1], v)]
    a = (r[0] * G2[1][1] - r[1] * G2[0][1]) / det
    b = (G2[0][0] * r[1] - G2[1][0] * r[0]) / det
    assert eqv(add(sc(a, B[0]), sc(b, B[1])), v), "not in P"
    return (a, b)
tauP = [list(coords_P(tau(B[0]))), list(coords_P(tau(B[1])))]   # columns = images
tauP = [[tauP[0][0], tauP[1][0]], [tauP[0][1], tauP[1][1]]]
tr = tauP[0][0] + tauP[1][1]; dt = tauP[0][0] * tauP[1][1] - tauP[0][1] * tauP[1][0]
R["tauP_charpoly"] = f"x^2 - ({tr})x + ({dt})"
# invariant vectors of tau on P: det(tauP - I) != 0  <=>  P^{Z/3} = 0  (fixed-point-free)
M_ = [[tauP[0][0] - 1, tauP[0][1]], [tauP[1][0], tauP[1][1] - 1]]
detI = M_[0][0] * M_[1][1] - M_[0][1] * M_[1][0]
R["det(tauP - I)"] = str(detI)
R["dim_P_fixed_by_Z3"] = 0 if detI != 0 else (1 if any(x != 0 for r_ in M_ for x in r_) else 2)
R["Z3_fixed_point_free_on_P"] = (R["dim_P_fixed_by_Z3"] == 0)

# ---------- 4. LEG 3 -- what the joint group alone leaves: a 1-dim UNPINNED family ----
# characters: g is an eigenvector of every unit; find its character, then P's isotypic parts.
def unit_char(v):
    ch = {}
    for u in UNITS:
        im = perm_act(u, 0, v)
        if   eqv(im, v):               ch[u] = 1
        elif eqv(im, sc(Fr(-1), v)):   ch[u] = -1
        else:                          return None
    return ch
chi_g = unit_char(g)
R["golden_unit_character"] = chi_g
# P's decomposition under the joint group: which lines of P are unit-eigenlines?
eig_lines = []
for name, v in (("C0", C[0]), ("C1-C2", [x - y for x, y in zip(C[1], C[2])])):
    ch = unit_char(v)
    if ch: eig_lines.append((name, ch, ch == chi_g))
R["P_unit_eigenlines"] = [(nm, ch, same) for nm, ch, same in eig_lines]
R["dim_Hom_joint(L,P)"] = sum(1 for _, ch, same in eig_lines if same)
# is the unit action even able to discriminate? (its image on the data)
R["unit7_acts_trivially_on_all_data"] = all(eqv(perm_act(7, 0, v), v) for v in [g] + C)
R["joint_group_order"] = len(SYM_JOINT)
# the joint group is a PROPER subgroup of each sector's own group: imposing only the joint
# group means deliberately forgetting each sector's own symmetries.
R["sym_23_order"], R["sym_12_order"] = len(SYM_23), len(SYM_12)
# and each sector's own group MOVES the other sector's distinguished object:
R["Z3_of_(2,3)_moves_golden_line"] = not (eqv(tau(g), g) or eqv(tau(g), sc(Fr(-1), g)))
t6 = lambda v: perm_act(1, 6, v)                       # the (1,2)-intrinsic extra symmetry
R["t6_in_sym_12"], R["t6_in_sym_23"] = (1, 6) in SYM_12, (1, 6) in SYM_23
R["t6_of_(1,2)_moves_golden_line"] = not (eqv(t6(g), g) or eqv(t6(g), sc(Fr(-1), g)))
R["t6_image_of_golden_row"] = sorted(a for a in ROW
                                     if eqv(t6(g), ROW[a]) or eqv(t6(g), sc(Fr(-1), ROW[a])))
# the surviving candidate map g -> lambda*C0: is lambda pinned by the object?
ratio = dot(g, g) / dot(C[0], C[0])
R["norm_ratio_|g|^2/|C0|^2"] = str(ratio)
def is_square(fr):
    from math import isqrt
    a, b = fr.numerator, fr.denominator
    return isqrt(a) ** 2 == a and isqrt(b) ** 2 == b
R["isometric_lambda_rational"] = is_square(ratio)     # False => even norm-matching is irrational
R["lambda_pinned_by_object"] = False if R["dim_Hom_joint(L,P)"] >= 1 and not R["isometric_lambda_rational"] else None

# ---------- 5. the closest NEAR-FRAME, and why it is not object data ----------
# enlarge the golden line by the Mercedes Z/3: Ltil = span(g, tau g, tau^2 g).
gt = [g, tau(g), tau(tau(g))]
def rank(vs):
    Mx = [list(v) for v in vs]; r = 0
    for c in range(N):
        p = next((i for i in range(r, len(Mx)) if Mx[i][c] != 0), None)
        if p is None: continue
        Mx[r], Mx[p] = Mx[p], Mx[r]
        pv = Mx[r][c]; Mx[r] = [x / pv for x in Mx[r]]
        for i in range(len(Mx)):
            if i != r and Mx[i][c] != 0:
                f = Mx[i][c]; Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[r])]
        r += 1
    return r
R["dim_Z3_orbit_of_golden_line"] = rank(gt)
R["Z3_orbit_of_golden_sums_to_zero"] = all(sum(v[k] for v in gt) == 0 for k in range(N))
# dim 2 + sum zero  =>  Ltil is the STANDARD rep of Z/3, i.e. Ltil ~= P as Z/3-reps:
# an equivariant isomorphism Ltil -> P DOES exist (Schur: a free C^* of them).
R["near_frame_Ltil_iso_P"] = (R["dim_Z3_orbit_of_golden_line"] == 2 and
                              R["Z3_orbit_of_golden_sums_to_zero"])
R["near_frame_uses_nonbanked_lines"] = not R["tau_g_matches_a_banked_row"]
R["near_frame_residual_freedom"] = "C^* (Schur: rotation x scale), still unpinned"

# ---------- 6. the tensor double (B422's one untested construction) -- computed ----------
# (a) orthogonality is product-stable: <g(x)g, Ci(x)Cj> = <g,Ci><g,Cj> = 0.
R["double_LxL_perp_PxP"] = all(dot(g, C[i]) * dot(g, C[j]) == 0 for i in range(3) for j in range(3))
# (b) the double DOES gain Z/3-invariant directions inside the Mercedes sector:
#     eigenvalues of tauP are primitive cube roots => tauP (x) tauP has eigenvalue 1 twice.
R["dim_(PxP)_fixed_by_Z3"] = 2 if R["Z3_fixed_point_free_on_P"] else None
# (c) but the golden double is still not Z/3-stable: tau(L(x)L) = tauL (x) tauL != L(x)L.
R["double_golden_stable_under_Z3"] = eqv(tau(g), g) or eqv(tau(g), sc(Fr(-1), g))
R["double_inherits_wall"] = (R["double_LxL_perp_PxP"] and not R["double_golden_stable_under_Z3"])

# ---------- 7. VERDICT ----------
# RESOLVED-A (surprising): a nonzero map L -> P that is (i) equivariant for EVERY symmetry
#   the object supplies for either sector (joint affine group AND the (2,3)-intrinsic Z/3),
#   and (ii) pinned -- no free scalar.
# RESOLVED-B: no such map; the frame set is nonempty but carries no object-fixed point
#   (fixed-point-free Z/3 + unpinned scalar + degenerate relative geometry) => EXTERNAL /
#   CONSTITUTIVELY-OPEN, and the missing datum is exactly identified.
# UNRESOLVED: the banked structures do not reproduce.
reproduced = (R["mercedes_equilateral"] and R["mercedes_sums_to_zero"] and
              R["antipodal_row14_is_minus_row6"] and R["tau_cycles_mercedes"] and
              set(R["golden_support"]) == {2, 10})
frame_equivariant_for_all = (R["dim_Hom_joint(L,P)"] >= 1 and not R["Z3_fixed_point_free_on_P"])
frame_pinned = bool(R["isometric_lambda_rational"])
if not reproduced:
    verdict = "UNRESOLVED"
elif frame_equivariant_for_all and frame_pinned:
    verdict = "RESOLVED-A"
elif (R["L_perp_P_exact"] and R["supports_disjoint"]                    # route 1 (W-B1 reproduced)
      and R["Z3_fixed_point_free_on_P"] and R["tau_in_sym_23"]         # route 2 (fixed-point-free)
      and not R["tau_in_sym_12"] and not frame_pinned and R["double_inherits_wall"]):
    verdict = "RESOLVED-B"
else:
    verdict = "UNRESOLVED"
R["verdict"] = verdict

json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1, default=str)
print(json.dumps(R, indent=1, default=str))
print("""
DISCRIMINATING FACT (in-cell, exact over Q; two independent routes)
 ROUTE 1 (reproduces W-B1/B422 from raw tables): supports disjoint, L _|_ P, every
 principal angle pi/2 -- the canonical subspace-relating construction selects NOTHING
 (all of the circle S(P) is equally "best aligned").
 ROUTE 2 (new, at the level of MAPS not overlaps):
 The Mercedes triple's Z/3 IS realised inside the shared W2-label space, as the exact
 translation tau: a -> a+4 (it cycles the three columns with sign +1). On the Mercedes
 plane P its matrix has char poly x^2+x+1, so P^{Z/3} = 0: tau is FIXED-POINT-FREE, no
 direction of P is object-distinguished. And tau is NOT a symmetry of the (1,2) table
 (tau(g) is not +- any banked row), so the golden line carries no Z/3 action at all.
 Hence every nonzero map L -> P must break one of the object's own symmetries; the only
 maps surviving the joint group form a 1-dim family whose scalar the object cannot pin
 (norm-matching needs sqrt(6), irrational -- the no-scale wall B413 IS the no-frame wall).
 Frames exist as bare linear algebra (a whole circle of them) but the object's structure
 acts on that circle without fixed points: choosing one is exactly an EXTERNAL datum,
 valued in (which Z/3 direction) x (a sign) x (a positive scale).
 SYMMETRIC FORM: Aut(2,3)=12, Aut(1,2)=8, joint=4 (the units alone). Each sector's own
 extra symmetry moves the OTHER sector's distinguished object (tau moves the golden line;
 t6 carries the golden row onto rows 0,4). Canonicity for one sector is non-canonicity
 for the other -- the frame is constitutively external, not merely undiscovered.""")
print(f"\nVERDICT: {verdict}")
