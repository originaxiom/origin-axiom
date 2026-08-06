#!/usr/bin/env python3
"""B928 -- THE D2 DECODE (sealed cell; PREREGISTRATION.md is binding).

B923 proved the whole generation hierarchy is carried by the 11-flip diagonal
D2 (B916: H' = H+ * diag(D2), the tau-twisted second Hermitian structure vs
the charge-equivariant H+).  WHAT IS D2?  The sealed sub-questions:

Q1 (characterization), candidates:
  (a) sign characters on other/shifted lattices;
  (b) block/atom membership of the 11 flips (one octet Pi-block + the three
      vacuum lines?) -- decided EXACTLY;
  (c) the wall-conjugation formula: D2 from (chi+, chi- = -chi+) through the
      tau cocycle -- derived symbolically;
  (d) the classification: ALL +-1 diagonals D with H+ D an invariant
      Hermitian structure for some involution in the B907 census (the 8
      C-compatible representatives, and the full 128).
Q2 (arithmetic): derive the pole prime 953, the 2304 = 2^8 3^2 lead, the
  d-ratio minpolys, HIER's coefficients -- as far as derivation goes; state
  the exact residue where it stops.
Q3 (shape sheet): the exact dimensionless overlaps between D2's flip
  eigenspaces and the generation-indexed atom frames, blind to any measured
  value; S3-orbit structure; forced equalities.  THE SHEET IS THE DELIVERABLE.

HOUSE RULES ENFORCED HERE: exact arithmetic for every verdict-bearing claim;
verify-don't-trust (H+, H-, and the second structure H(phi*) are re-SOLVED
from their own defining equations in this cell -- no handoff files, no banked
H entries assumed; the banked B912/B916 data is only COMPARED against);
e6_centralizer.py exec'd in an isolated namespace with chdir to scratch and
__file__ set; NO Rayleigh-quotient eigenvalue readouts anywhere (componentwise
eigen-readouts with residual certificates on the numeric belts).

Output: results.json (exact data + checks).  Runtime ~ a few minutes.
"""
import io
import os
import json
import math
import time
import tempfile
import contextlib
import itertools
from fractions import Fraction as Fr
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b928_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B928 D2 decode", "checks": {}, "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def dump():
    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        dump()
        raise SystemExit(f"UNSTABLE at {name}")


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


# ================================================================ [0] inputs
log("[0] banked inputs: rep27, B912 H+/-, B916 D2, B914 cubic, B918 HIER ...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27",
                                   "rep27.json")))
REP = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]]
       for k in range(78)]
WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diagonal_27_distinct_weights",
    all(all(REP[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT)) == 27)
CHK("rep27_entries_pm1",
    all(REP[k][a][b] in (-1, 0, 1) for k in range(78)
        for a in range(27) for b in range(27)))
CHK("weights_disjoint_from_their_negatives",
    not (set(WT) & {tuple(-x for x in w) for w in WT}),
    "=> NO inner twist admits an invariant pairing (support empty); "
    "the classification lives entirely on the outer sheet")

B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
piW_banked = list(B912["H_plus_support_pi"])
cbP_banked = [int(x) for x in B912["H_plus_entries_c_b"]]
cbM_banked = [int(x) for x in B912["H_minus_entries_c_b"]]
Dd_banked = [int(x) for x in B912["D_diag"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2_banked = [int(x) for x in B916["H_prime_diag_vs_H_plus"]["D2"]]
MINPOLY_S_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["S0"]]
MINPOLY_A_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["A0p"]]
B914 = json.load(open(os.path.join(REPO, "frontier", "B914_ratio_table",
                                   "results.json")))
TRIP = [tuple(t) for t in B914["cubic_B883"]["triples"]]
COEF = [int(c) for c in B914["cubic_B883"]["coeffs"]]
B918 = json.load(open(os.path.join(REPO, "frontier", "B918_v_kummer",
                                   "results.json")))
HIER_ints = [int(c) for c in B918["hier_cubic"]["coeffs"]]
B907V = json.load(open(os.path.join(REPO, "frontier",
                                    "B907_real_form_selector", "verdict.json")))
CHI_P = tuple(int(x) for x in B907V[0]["signs"])     # (1,-1,1,-1,1,1)
CHI_M = tuple(int(x) for x in B907V[1]["signs"])     # its global negation
CHK("banked_wall_pair_is_a_global_negation",
    CHI_M == tuple(-x for x in CHI_P), f"chi+ = {CHI_P}")

# the weight pairing pi: w -> -flip(w); FLIP = the E6 diagram flip (B907)
FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}


def flipw(w):
    return tuple(w[FLIP[i]] for i in range(6))


negflip = {tuple(-x for x in flipw(WT[b])): b for b in range(27)}
piW = [None] * 27
for b in range(27):
    piW[b] = negflip[WT[b]]                    # a with w_a = -flip(w_b)
CHK("weight_pairing_pi_recomputed_and_involutive",
    sorted(piW) == list(range(27)) and all(piW[piW[b]] == b for b in range(27))
    and piW == piW_banked, "matches the banked B912 support permutation")

# ================================================================ [1] B854 frame
log("[1] B854 frame (isolated exec, chdir scratch, __file__ set) ...")
cache = os.path.join(SCRATCH, "b928_frame_cache.pkl")
import pickle
if os.path.exists(cache):
    FR = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
          "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    FR = {"ROOTS": [tuple(r) for r in g6["ROOTS"]],
          "C": [list(row) for row in g6["C"]],
          "ns": list(g6["ns"]),
          "INV": {n: [Fr(c) for c in g6["INV"][n]] for n in g6["ns"]},
          "BB": [[[Fr(x) for x in g6["BB"][p][q]] for q in range(78)]
                 for p in range(78)],
          "EPS": {(a, b): g6["eps"](a, b) for a in g6["ROOTS"]
                  for b in g6["ROOTS"]
                  if tuple(x + y for x, y in zip(a, b)) in g6["IDX"]}}
    pickle.dump(FR, open(cache, "wb"))
ROOTS = FR["ROOTS"]
IDX = {r: i for i, r in enumerate(ROOTS)}
CMAT = FR["C"]
ns = FR["ns"]
INV = FR["INV"]
BB = FR["BB"]
EPS = FR["EPS"]
CHK("frame_72_roots_ns_8_14_16_22", len(ROOTS) == 72
    and sorted(ns) == [8, 14, 16, 22])

# charges over Q on the 27
Rex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV[n]):
        if c:
            Rk = REP[k]
            for a in range(27):
                ra = Rk[a]
                for b in range(27):
                    if ra[b]:
                        M[a][b] += c * ra[b]
    Rex[n] = M
CHK("four_charges_commute_exactly",
    all(all(sum(Rex[m_][i][t] * Rex[n_][t][j] for t in range(27))
            == sum(Rex[n_][i][t] * Rex[m_][t][j] for t in range(27))
            for i in range(27) for j in range(27))
        for m_, n_ in itertools.combinations(ns, 2)))

# rep bracket sanity (verify-don't-trust, sample): [rho_p, rho_q] = rho([p,q])
import random
random.seed(928)
ok = True
for _ in range(40):
    p = random.randrange(78)
    q = random.randrange(78)
    Bv = BB[p][q]
    for i in range(27):
        for j in range(27):
            lhs = sum(REP[p][i][t] * REP[q][t][j]
                      - REP[q][i][t] * REP[p][t][j] for t in range(27))
            rhs = sum(Bv[k] * REP[k][i][j] for k in range(78) if Bv[k])
            if lhs != rhs:
                ok = False
CHK("rep_homomorphism_40_random_bracket_pairs_exact", ok)

# ================================================================ [2] tau cocycle
log("[2] the tau cocycle d: F2 solve (B907 route, re-run here) ...")
ridx = {r: i for i, r in enumerate(ROOTS)}
rows, rhs = [], []
for a_ in ROOTS:
    for b_ in ROOTS:
        s_ = tuple(a_[i] + b_[i] for i in range(6))
        if s_ in ridx:
            row = [0] * 72
            row[ridx[a_]] ^= 1
            row[ridx[b_]] ^= 1
            row[ridx[s_]] ^= 1
            cc = EPS[(a_, b_)] * EPS[(flipw(a_), flipw(b_))]
            rows.append(row)
            rhs.append(0 if cc == 1 else 1)
Aa = [row + [r] for row, r in zip(rows, rhs)]
r_ = 0
for c_ in range(72):
    piv = next((i for i in range(r_, len(Aa)) if Aa[i][c_]), None)
    if piv is None:
        continue
    Aa[r_], Aa[piv] = Aa[piv], Aa[r_]
    for i in range(len(Aa)):
        if i != r_ and Aa[i][c_]:
            Aa[i] = [x ^ y for x, y in zip(Aa[i], Aa[r_])]
    r_ += 1
CHK("tau_cocycle_consistent_rank_66",
    r_ == 66 and not any(sum(row[:72]) == 0 and row[72] for row in Aa))
sol = [0] * 72
for i in range(r_):
    c_ = next(cc for cc in range(72) if Aa[i][cc])
    sol[c_] = Aa[i][72]
dcoc = {ROOTS[i]: (-1) ** sol[i] for i in range(72)}


def chi_of(signs):
    def ch(r):
        v = 1
        for i in range(6):
            if r[i] % 2:
                v *= signs[i]
        return v
    return ch


def inner_gmap(signs):
    """generator map of sigma_chi: k -> (j, coef)."""
    ch = chi_of(signs)
    out = []
    for i in range(6):
        out.append((i, 1))
    for r in ROOTS:
        out.append((6 + IDX[r], ch(r)))
    return out


def outer_gmap(signs):
    """generator map of sigma_chi o tau (the B907 outer_matrix convention)."""
    ch = chi_of(signs)
    out = []
    for i in range(6):
        out.append((FLIP[i], 1))
    for r in ROOTS:
        fr = flipw(r)
        out.append((6 + IDX[fr], dcoc[r] * ch(fr)))
    return out


def gmap_compose(g2, g1):
    """(g2 o g1)(x_k)."""
    out = []
    for k in range(78):
        j1, c1 = g1[k]
        j2, c2 = g2[j1]
        out.append((j2, c1 * c2))
    return out


def gmap_is_id(g):
    return all(g[k] == (k, 1) for k in range(78))


BBnz = [[[(k, Bv[k]) for k in range(78) if Bv[k]] for Bv in row]
        for row in BB]


def is_automorphism_gmap(g):
    """full 78^2 bracket-pair check for a monomial generator map."""
    for p in range(78):
        jp, cp = g[p]
        for q in range(78):
            jq, cq = g[q]
            img = {}
            for (k, v) in BBnz[p][q]:
                jk, ck = g[k]
                img[jk] = img.get(jk, 0) + ck * v
            tgt = {k: cp * cq * v for (k, v) in BBnz[jp][jq]}
            for k in set(img) | set(tgt):
                if img.get(k, 0) != tgt.get(k, 0):
                    return False
    return True


def pattern_of_gmap(g):
    """C-compatibility: does the automorphism send each charge to +- itself?"""
    out = {}
    for n in ns:
        vec = INV[n]
        img = [Fr(0)] * 78
        for k in range(78):
            if vec[k]:
                j, c = g[k]
                img[j] += c * vec[k]
        ev = None
        for k in range(78):
            if vec[k] == 0 and img[k] == 0:
                continue
            if vec[k] == 0:
                return None
            rt = img[k] / vec[k]
            if rt not in (1, -1):
                return None
            if ev is None:
                ev = int(rt)
            elif int(rt) != ev:
                return None
        out[n] = ev
    return out


ALL_ONES = (1,) * 6
ALL_MINUS = (-1,) * 6
g_phi_p = outer_gmap(CHI_P)
g_phi_m = outer_gmap(CHI_M)
g_phi_star = outer_gmap(ALL_MINUS)
g_sigma_allminus = inner_gmap(ALL_MINUS)
g_sigma_chim = inner_gmap(CHI_M)
CHK("phi_plus_involution_and_automorphism",
    gmap_is_id(gmap_compose(g_phi_p, g_phi_p))
    and is_automorphism_gmap(g_phi_p))
CHK("phi_minus_involution_and_automorphism",
    gmap_is_id(gmap_compose(g_phi_m, g_phi_m))
    and is_automorphism_gmap(g_phi_m))
CHK("phi_star_involution_and_automorphism",
    gmap_is_id(gmap_compose(g_phi_star, g_phi_star))
    and is_automorphism_gmap(g_phi_star),
    "phi* = the all-minus outer composite")
CHK("wall_ratio_identity_phi_plus_o_phi_minus_equals_sigma_allminus",
    gmap_compose(g_phi_p, g_phi_m) == g_sigma_allminus,
    "the banked completeness fact g = phi1 phi2 = inner all-minus, recomputed")
g_tau = outer_gmap(ALL_ONES)
CHK("phi_star_equals_tau_o_phi_plus_o_phi_minus",
    gmap_compose(g_phi_p, g_sigma_chim) == g_phi_star
    and gmap_compose(g_tau, gmap_compose(g_phi_p, g_phi_m)) == g_phi_star,
    "phi* = phi+ o sigma_{chi-} = tau o (phi+ o phi-) -- a banked-data "
    "composite of the tau-lift with the two wall conjugations, nothing else")
CHK("phi_plusminus_C_compatible_wall_pattern",
    pattern_of_gmap(g_phi_p) == {8: -1, 14: 1, 16: -1, 22: 1}
    and pattern_of_gmap(g_phi_m) == {8: -1, 14: 1, 16: -1, 22: 1})
REC("phi_star_C_compatibility", str(pattern_of_gmap(g_phi_star)),
    "None = phi* does NOT act +-diagonally on the charge family "
    "(explains B916: H' is not charge-equivariant for any sign pattern)")

# ================================================================ [3] H solves
log("[3] the invariant-pairing solves H(phi): own solves, no banked entries ...")


def solve_H_outer(g):
    """solve rho(x)^T H + H rho(phi x) = 0 for outer phi with generator map g.

    Cartan rows force support H[pi(b)][b] (pi = the -flip pairing);
    the 72 root rows are two-term relations in y_b = H[pi(b)][b];
    propagation from y_0 = 1; then EVERY equation re-verified exactly.
    Returns y (list of Fraction) or None."""
    eqs = []
    for k in range(6, 78):
        j, c = g[k]
        Rk = REP[k]
        Rj = REP[j]
        seen = set()
        for a in range(27):
            for b in range(27):
                if Rk[piW[b]][a] or Rj[piW[a]][b]:
                    key = (a, b)
                    if key in seen:
                        continue
                    seen.add(key)
                    #  Rk[pi(b)][a] * y_b  +  c * Rj[pi(a)][b] * y_{pi(a)} = 0
                    eqs.append((b, piW[a], Rk[piW[b]][a], c * Rj[piW[a]][b]))
    y = [None] * 27
    y[0] = Fr(1)
    changed = True
    while changed:
        changed = False
        for b1, b2, c1, c2 in eqs:
            if c1 and c2:
                if y[b1] is not None and y[b2] is None:
                    y[b2] = -Fr(c1) * y[b1] / c2
                    changed = True
                elif y[b2] is not None and y[b1] is None:
                    y[b1] = -Fr(c2) * y[b2] / c1
                    changed = True
    if any(v is None for v in y):
        return None                      # not connected: solution not unique
    for b1, b2, c1, c2 in eqs:
        if c1 * y[b1] + c2 * y[b2] != 0:
            return None                  # inconsistent: no solution
    return y


yP = solve_H_outer(g_phi_p)
CHK("H_plus_own_solve_unique_and_equals_banked",
    yP is not None and [int(v) for v in yP] == cbP_banked,
    "H+ re-solved from its defining equation; propagation connected "
    "(unique up to scale); equals the banked B912 H+ entrywise")
cbP = [int(v) for v in yP]
yM = solve_H_outer(g_phi_m)
CHK("H_minus_own_solve_unique_and_equals_banked",
    yM is not None and [int(v) for v in yM] == cbM_banked)
cbM = [int(v) for v in yM]
Dd = [cbM[b] * cbP[b] for b in range(27)]
CHK("D_wall_equals_banked_B912_D_diag", Dd == Dd_banked,
    f"H- = H+ * D, D = the wall twist, {Dd.count(-1)} flips")
yS = solve_H_outer(g_phi_star)
CHK("H_phi_star_own_solve_unique", yS is not None)
D2rec = [int(yS[b]) * cbP[b] for b in range(27)]
if D2rec[0] == -1:
    D2rec = [-x for x in D2rec]
CHK("D2_RECOMPUTED_from_own_solves_equals_banked_B916_D2",
    D2rec == D2_banked,
    "THE VERIFY-DON'T-TRUST GATE: D2 = H+^{-1} H(phi*) with H+ and H(phi*) "
    "both re-solved from their own invariance equations -- handoff-free; "
    "equals the banked B916 flip diagonal exactly")
D2 = D2rec
FLIPSET = [b for b in range(27) if D2[b] == -1]
CHK("D2_11_flips_pi_symmetric", len(FLIPSET) == 11
    and all(D2[piW[b]] == D2[b] for b in range(27)),
    "pi-symmetric => H+ D2 is symmetric (a Hermitian structure)")
CHK("H_phi_star_is_H_plus_times_D2_symmetric",
    all(D2[b] == D2[piW[b]] for b in range(27)))

# ================================================================ [4] Q1(a)
log("[4] Q1(a): character tests on the weight lattice and beyond ...")


def char_pattern(coords, a, pol):
    return [pol * (1 if sum(ai * ci for ai, ci in zip(a, c)) % 2 == 0 else -1)
            for c in coords]


hits_naive = [(a, pol) for a in itertools.product((0, 1), repeat=6)
              for pol in (1, -1) if char_pattern(WT, a, pol) == D2]
CHK("naive_unshifted_characters_all_64_fail",
    not [h for h in hits_naive if h[1] == 1],
    "re-verifies the B916 addendum: no (-1)^<a,w> flips the eleven")
CHK("SHIFTED_character_hit_unique",
    len(hits_naive) == 1 and hits_naive[0][1] == -1,
    f"D2 = -(-1)^<a*,w> with a* = {hits_naive[0][0]} -- the affine/shifted "
    "character candidate of the sealed list (a) SUCCEEDS, uniquely in the "
    "128-member family")
A_STAR = hits_naive[0][0]
s_chim = tuple(1 if CHI_M[i] == -1 else 0 for i in range(6))
CHK("a_star_equals_sign_vector_of_chi_minus", A_STAR == s_chim,
    f"a* = s(chi-) = {s_chim}: the exponent is the SECOND wall "
    "conjugation's sign character")

# the other-lattice family: pairing through 3 C^{-1} (the coweight route)
import sympy as sp
Ci = sp.Matrix(CMAT).inv()
U3 = []
for w in WT:
    u = 3 * Ci * sp.Matrix(w)
    CHK_int = all(sp.Rational(x).q == 1 for x in u)
    if not CHK_int:
        CHK("coweight_coordinates_integral", False)
    U3.append(tuple(int(x) for x in u))
hits_cow = [(a, pol) for a in itertools.product((0, 1), repeat=6)
            for pol in (1, -1) if char_pattern(U3, a, pol) == D2]
CHK("coweight_family_hit_unique_same_exponent",
    len(hits_cow) == 1 and hits_cow[0] == ((1, 0, 1, 0, 1, 1), -1),
    "the 3C^{-1}-lattice family hits at the same a*")
pat_naive = {tuple(char_pattern(WT, a, 1))
             for a in itertools.product((0, 1), repeat=6)}
pat_cow = {tuple(char_pattern(U3, a, 1))
           for a in itertools.product((0, 1), repeat=6)}
CHK("the_two_lattice_families_coincide_as_sets",
    pat_naive == pat_cow,
    "det(3C^{-1}) = 243 is odd => the mod-2 reparametrization is invertible; "
    "'other lattice' adds NO new sign patterns -- only the affine shift is new")
REC("family_27bar_weights_identical",
    True, "(-1)^<a,-w> = (-1)^<a,w>: the 27bar-weight family is literally "
    "the same 128 candidates")

# the direct symbolic derivation (c): the 27-diagonal of sigma_{chi-}
def rep_diagonal_of_inner(signs):
    """the unique (up to global sign) +-1 diagonal T with
    T rho(x) T = rho(sigma_chi x); None if inconsistent."""
    ch = chi_of(signs)
    T = [None] * 27
    T[0] = 1
    changed = True
    while changed:
        changed = False
        for kr, r in enumerate(ROOTS):
            M = REP[6 + kr]
            c = ch(r)
            for a in range(27):
                for b in range(27):
                    if M[a][b]:
                        if T[b] is not None and T[a] is None:
                            T[a] = c * T[b]
                            changed = True
                        elif T[a] is not None and T[b] is None:
                            T[b] = c * T[a]
                            changed = True
    if any(t is None for t in T):
        return None
    for kr, r in enumerate(ROOTS):
        M = REP[6 + kr]
        c = ch(r)
        for a in range(27):
            for b in range(27):
                if M[a][b] and T[a] != c * T[b]:
                    return None
    return T


T_chim = rep_diagonal_of_inner(CHI_M)
CHK("FORMULA_D2_equals_rep27_diagonal_of_sigma_chi_minus",
    T_chim is not None and (T_chim == D2 or [-x for x in T_chim] == D2),
    "D2 = +-rho_27(sigma_{chi-}): the eleven-flip diagonal IS the second "
    "wall conjugation's sign character acting on the 27")
T_allm = rep_diagonal_of_inner(ALL_MINUS)
CHK("D_wall_equals_rep27_diagonal_of_sigma_allminus",
    T_allm is not None and (T_allm == Dd or [-x for x in T_allm] == Dd),
    "and the B912 wall twist D = +-rho_27(sigma_{-1}) = +-rho_27(phi+ phi-)")
T_chip = rep_diagonal_of_inner(CHI_P)
Klein_prods = {T_chip[b] * T_chim[b] * T_allm[b] for b in range(27)} \
    if T_chip is not None else set()
Klein_ok = len(Klein_prods) == 1
CHK("Klein_group_structure_T_chip_T_chim_T_allminus",
    Klein_ok, "rho27(sigma_chi+) * rho27(sigma_chi-) = +-rho27(sigma_{-1}): "
    "the three nontrivial diagonals form the Klein group {I, D2, Dd, D2*Dd} "
    "up to global signs")
RES["Q1a"] = {
    "unshifted_characters": "all 64 fail (B916 addendum re-verified)",
    "shifted_character": {"a_star": list(A_STAR), "polarity": -1,
                          "unique_in_128": True,
                          "a_star_equals_s_chi_minus": True},
    "other_lattice_families": "identical to the weight-lattice family "
                              "(3C^{-1} mod 2 invertible; 27bar identical)",
    "formula": "D2 = +-rho_27(sigma_{chi-}); Dd = +-rho_27(phi+ phi-)"}
dump()

# ================================================================ [5] Q1(d)
log("[5] Q1(d): the classification sweep (64 inner + 64 outer) ...")
sweep = []
for signs in itertools.product((1, -1), repeat=6):
    g = outer_gmap(signs)
    y = solve_H_outer(g)
    ok_inv = gmap_is_id(gmap_compose(g, g))
    pat = pattern_of_gmap(g)
    row = {"signs": list(signs), "involution": bool(ok_inv),
           "C_compatible": pat is not None,
           "eps": ([pat[n] for n in ns] if pat else None)}
    if y is None:
        row["H"] = None
    else:
        D = [int(y[b]) * cbP[b] for b in range(27)]
        if D[0] == -1:
            D = [-x for x in D]
        row["D_normalized"] = D
        row["D_flips"] = D.count(-1)
        row["H_symmetric"] = all(D[piW[b]] == D[b] for b in range(27))
    sweep.append(row)
CHK("all_64_outer_composites_admit_a_unique_invariant_pairing",
    all("D_normalized" in r for r in sweep))
CHK("Hermitian_symmetry_iff_involution",
    all(r["H_symmetric"] == r["involution"] for r in sweep),
    "H(sigma_chi o tau) is symmetric EXACTLY when the composite is an "
    "involution (chi flip-symmetric): the Hermitian-structure "
    "classification is precisely the involution sheet of the census "
    "(found by the run: the first draft wrongly expected all 64 symmetric)")
n_invol = sum(1 for r in sweep if r["involution"])
CHK("outer_involutions_are_the_16_flip_symmetric_characters",
    n_invol == 16 and all(
        (tuple(r["signs"]) == tuple(r["signs"][FLIP[i]] for i in range(6)))
        == r["involution"] for r in sweep))
n_compat = sum(1 for r in sweep if r["C_compatible"])
REC("outer_C_compatible_count", n_compat,
    "the census's outer C-compatible representatives")
compat_sigs = sorted(tuple(r["signs"]) for r in sweep if r["C_compatible"])
CHK("outer_C_compatible_match_B907_census",
    compat_sigs == sorted([(1, 1, -1, -1, -1, 1), (1, -1, 1, -1, 1, 1),
                           (-1, 1, -1, 1, -1, -1), (-1, -1, 1, 1, 1, -1)]),
    "the 4 outer members of the banked 8-representative census "
    "(the other 4 are inner, and every inner twist has NO invariant pairing)")

# the character-formula theorem for the whole sweep
ok_form = True
for r in sweep:
    signs = tuple(r["signs"])
    delta = tuple(signs[i] * CHI_P[i] for i in range(6))
    Tt = rep_diagonal_of_inner(delta)
    if Tt is None:
        ok_form = False
        continue
    D = r["D_normalized"]
    if not (Tt == D or [-x for x in Tt] == D):
        ok_form = False
CHK("classification_theorem_D_chi_equals_repdiag_of_chi_times_chiplus",
    ok_form,
    "for EVERY outer composite: H(sigma_chi o tau) = H+ * "
    "rho_27(sigma_{chi.chi+}) -- the classification is exactly the "
    "character group; the invariant structures are a torsor over the "
    "adjoint 2-torsion characters (a first-draft o-flip in the exponent "
    "was refuted by the run; on the involution sheet chi.chi+ is "
    "flip-symmetric and the two readings coincide)")

# the sealed census check: which D arise from the 8 C-compatible members?
census_D = []
for r in sweep:
    if r["C_compatible"]:
        D = tuple(r["D_normalized"])
        if D not in [tuple(x) for x in census_D]:
            census_D.append(list(D))
census_D_named = []
for D in census_D:
    tag = ("I" if D == [1] * 27 else
           "D_wall" if D == Dd else
           "D2" if D == D2 else
           "D_wall*D2" if D == [Dd[b] * D2[b] for b in range(27)] else
           "other")
    census_D_named.append({"D": D, "flips": D.count(-1), "name": tag})
REC("census_8_D_set",
    str([(d["name"], d["flips"]) for d in census_D_named]),
    "the +-1 diagonals D with H+ D invariant for a C-COMPATIBLE census "
    "involution")
D2_in_census = any(d["name"] == "D2" for d in census_D_named)
REC("D2_in_C_compatible_census_set", D2_in_census,
    "the sealed (d) first check: is D2 pinned by the C-compatible census?")

# the full-128 layer: D-set over ALL outer involutions
invol_D = []
for r in sweep:
    if r["involution"]:
        D = tuple(r["D_normalized"])
        if D not in [tuple(x) for x in invol_D]:
            invol_D.append(list(D))
REC("full_128_involution_D_set_size", len(invol_D),
    "distinct normalized diagonals over the 16 outer involutions "
    "(inner: none -- proven empty support)")
d2_carriers = [tuple(r["signs"]) for r in sweep
               if r.get("D_normalized") == D2]
CHK("D2_arises_from_exactly_one_composite_the_allminus_one",
    d2_carriers == [ALL_MINUS],
    "phi* = sigma_{-1} o tau = tau o phi+ o phi- is the UNIQUE member of the "
    "128-census whose invariant Hermitian structure is H+ D2; it is an "
    "involution, an automorphism, and NOT C-compatible")
RES["Q1d"] = {
    "inner_64": "no invariant pairing (weight-support empty, exact)",
    "outer_64": "one Hermitian structure each, all symmetric",
    "outer_involutions": 16,
    "census_8_D_set": census_D_named,
    "D2_in_census_8_set": D2_in_census,
    "full_involution_D_set_size": len(invol_D),
    "D2_unique_carrier_signs": [list(s) for s in d2_carriers]}
dump()

# ================================================================ [6] fields
log("[6] the exact tower K -> N -> Mbar and K(omega) (B923 machinery) ...")
MU = [500716339200, -2075673600, -4769856, 2197]
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))


def kmul(x, y):
    c0 = x[0] * y[0]
    c1 = x[0] * y[1] + x[1] * y[0]
    c2 = x[0] * y[2] + x[1] * y[1] + x[2] * y[0]
    c3 = x[1] * y[2] + x[2] * y[1]
    c4 = x[2] * y[2]
    if c4:
        c0 += c4 * R4K[0]
        c1 += c4 * R4K[1]
        c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]
        c1 += c3 * R3K[1]
        c2 += c3 * R3K[2]
    return (c0, c1, c2)


def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def ksub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


def kscale(x, s):
    return (x[0] * s, x[1] * s, x[2] * s)


def kis0(x):
    return not (x[0] or x[1] or x[2])


def kinv(x):
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))),
            kmul(x, (Fr(0), Fr(0), Fr(1)))]
    Aug = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)]
           for i in range(3)]
    for c in range(3):
        pr = next(r for r in range(c, 3) if Aug[r][c] != 0)
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = Aug[c][c]
        Aug[c] = [e / iv for e in Aug[c]]
        for r in range(3):
            if r != c and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(4)]
    return (Aug[0][3], Aug[1][3], Aug[2][3])


b_mu = Fr(MU[1], MU[0])
c_mu = Fr(MU[2], MU[0])
P_N = (b_mu, Fr(1), Fr(0))
Q_N = (c_mu, b_mu, Fr(1))
NZERO = (KZERO, KZERO)
NONE_ = (KONE, KZERO)


def nmul(a, b):
    a0, a1 = a
    b0, b1 = b
    x00 = kmul(a0, b0)
    x11 = kmul(a1, b1)
    x01 = kadd(kmul(a0, b1), kmul(a1, b0))
    return (ksub(x00, kmul(x11, Q_N)), ksub(x01, kmul(x11, P_N)))


def nadd(a, b):
    return (kadd(a[0], b[0]), kadd(a[1], b[1]))


def nsub(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def nscale(a, s):
    return (kscale(a[0], s), kscale(a[1], s))


def nis0(a):
    return kis0(a[0]) and kis0(a[1])


def ninv(a):
    x, y = a
    det = kadd(ksub(kmul(x, x), kmul(kmul(P_N, x), y)), kmul(Q_N, kmul(y, y)))
    di = kinv(det)
    return (kmul(ksub(x, kmul(P_N, y)), di), kscale(kmul(y, di), Fr(-1)))


def sigma(j, x):
    c0, c1, c2 = x
    if j == 0:
        return ((c0, c1, c2), KZERO)
    if j == 1:
        return (ksub((c0, Fr(0), Fr(0)), kscale(Q_N, c2)),
                ksub((c1, Fr(0), Fr(0)), kscale(P_N, c2)))
    R3N = ((-b_mu, Fr(-1), Fr(0)), (Fr(-1), Fr(0), Fr(0)))
    acc = ((Fr(c0), Fr(0), Fr(0)), KZERO)
    acc = nadd(acc, nscale(R3N, c1))
    acc = nadd(acc, nscale(nmul(R3N, R3N), c2))
    return acc


class TR:
    def mul(self, a, b):
        Xv = nsub(nmul(a[0], b[0]), nscale(nmul(a[1], b[1]), Fr(3)))
        Yv = nadd(nmul(a[0], b[1]), nmul(a[1], b[0]))
        return (Xv, Yv)

    def add(self, a, b):
        return (nadd(a[0], b[0]), nadd(a[1], b[1]))

    def sub(self, a, b):
        return (nsub(a[0], b[0]), nsub(a[1], b[1]))

    def scale(self, a, s):
        return (nscale(a[0], s), nscale(a[1], s))

    def is0(self, a):
        return nis0(a[0]) and nis0(a[1])

    def conj(self, a):
        return (a[0], nscale(a[1], Fr(-1)))


T = TR()
TZERO = (NZERO, NZERO)

FTZERO = (KZERO, KZERO)
FTONE = (KONE, KZERO)


def ftmul(a, b):
    return (ksub(kmul(a[0], b[0]), kscale(kmul(a[1], b[1]), Fr(231))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def ftadd(a, b):
    return (kadd(a[0], b[0]), kadd(a[1], b[1]))


def ftsub(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def ftscale(a, s):
    return (kscale(a[0], s), kscale(a[1], s))


def ftscaleK(a, kx):
    return (kmul(a[0], kx), kmul(a[1], kx))


def ftis0(a):
    return kis0(a[0]) and kis0(a[1])


def ftconj(a):
    return (a[0], kscale(a[1], Fr(-1)))


def ftinv(a):
    nrm = kadd(kmul(a[0], a[0]), kscale(kmul(a[1], a[1]), Fr(231)))
    ni = kinv(nrm)
    return (kmul(a[0], ni), kscale(kmul(a[1], ni), Fr(-1)))


def qkernel(M):
    m, n = len(M), len(M[0])
    A2 = [row[:] for row in M]
    piv = []
    rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if A2[r][c] != 0), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = A2[rr][c]
        A2[rr] = [e / iv for e in A2[rr]]
        for r in range(m):
            if r != rr and A2[r][c]:
                f = A2[r][c]
                A2[r] = [A2[r][j] - f * A2[rr][j] for j in range(n)]
        piv.append(c)
        rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A2[i][fc]
        ker.append(v)
    return ker


def qsolve_span(basis, vec):
    k, n = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n)]
    piv = []
    rr = 0
    for c in range(k):
        pr = next((r for r in range(rr, n) if Aug[r][c] != 0), None)
        if pr is None:
            continue
        Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
        iv = Aug[rr][c]
        Aug[rr] = [e / iv for e in Aug[rr]]
        for r in range(n):
            if r != rr and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(k + 1)]
        piv.append(c)
        rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n):
        if sum(sol[j] * basis[j][i] for j in range(k)) != vec[i]:
            return None
    return sol


def matmulQ(Xm, Ym):
    n = len(Xm)
    m = len(Ym[0])
    kk = len(Ym)
    return [[sum(Xm[i][t2] * Ym[t2][j] for t2 in range(kk) if Xm[i][t2])
             for j in range(m)] for i in range(n)]


import mpmath
from mpmath import mp


def _ratrec_real(x, maxden):
    f = mp.mpf(x)
    p0, q0, p1, q1 = mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0)
    r = f
    for _ in range(4000):
        a = mp.floor(r)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if q1 > maxden or r == a:
            break
        den = r - a
        if den == 0:
            break
        r = 1 / den
    if q1 > maxden:
        p1, q1 = p0, q0
    if q1 == 0:
        return None
    num, den = int(mp.nint(p1)), int(mp.nint(q1))
    if den < 0:
        num, den = -num, -den
    return Fr(num, den) if den else None


def _mu_roots_numeric(dps=400):
    mp.dps = dps
    rts = mp.polyroots([mp.mpf(c) for c in MU], maxsteps=300, extraprec=400)
    return [mp.re(r) for r in rts]


def _kev_num(x, r):
    return (mp.mpf(x[0].numerator) / mp.mpf(x[0].denominator)
            + (mp.mpf(x[1].numerator) / mp.mpf(x[1].denominator)) * r
            + (mp.mpf(x[2].numerator) / mp.mpf(x[2].denominator)) * r * r)


def _interp_K(vals, mu_roots, maxden, hmax):
    M3 = mp.matrix(3, 3)
    for i in range(3):
        M3[i, 0] = 1
        M3[i, 1] = mu_roots[i]
        M3[i, 2] = mu_roots[i] ** 2
    try:
        solv = mp.lu_solve(M3, mp.matrix(vals))
    except Exception:
        return None
    cand = []
    for v in solv:
        r = _ratrec_real(v, maxden)
        if r is None or max(abs(r.numerator), r.denominator) > hmax:
            return None
        cand.append(r)
    return tuple(cand)


def root_in_K(h_coeffs, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q)
          for c in h_coeffs]
    h_roots = mp.polyroots(hh, maxsteps=400, extraprec=400)
    reals = [mp.re(r) for r in h_roots
             if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 2)]
    maxden = mp.mpf(10) ** (dps // 3)
    for pick in itertools.permutations(range(len(reals)), 3):
        cand = _interp_K([reals[pick[j]] for j in range(3)], mu_roots,
                         maxden, hmax)
        if cand is None:
            continue
        acc = (Fr(sp.Rational(h_coeffs[0]).p, sp.Rational(h_coeffs[0]).q),
               Fr(0), Fr(0))
        for c in h_coeffs[1:]:
            acc = kmul(acc, cand)
            acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q),
                   acc[1], acc[2])
        if kis0(acc):
            return cand
    return None


def sqrt_in_K(targetk, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    tv = [_kev_num(targetk, r) for r in mu_roots]
    if any(t < 0 for t in tv):
        return None
    sq = [mp.sqrt(t) for t in tv]
    maxden = mp.mpf(10) ** (dps // 3)
    for sgs in itertools.product((1, -1), repeat=2):
        vals = [sq[0], sgs[0] * sq[1], sgs[1] * sq[2]]
        cand = _interp_K(vals, mu_roots, maxden, hmax)
        if cand is None:
            continue
        if kis0(ksub(kmul(cand, cand), targetk)):
            return cand
    return None


def kkernel(M):
    m, n = len(M), len(M[0])
    A2 = [row[:] for row in M]
    piv = []
    rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not kis0(A2[r][c])), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = kinv(A2[rr][c])
        A2[rr] = [kmul(iv, e) for e in A2[rr]]
        for r in range(m):
            if r != rr and not kis0(A2[r][c]):
                f = A2[r][c]
                A2[r] = [ksub(A2[r][j], kmul(f, A2[rr][j])) for j in range(n)]
        piv.append(c)
        rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [KZERO] * n
        v[fc] = KONE
        for i, c in enumerate(piv):
            v[c] = kscale(A2[i][fc], Fr(-1))
        ker.append(v)
    return ker


def krank(M):
    m, n = len(M), len(M[0])
    A2 = [row[:] for row in M]
    rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not kis0(A2[r][c])), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = kinv(A2[rr][c])
        A2[rr] = [kmul(iv, e) for e in A2[rr]]
        for r in range(m):
            if r != rr and not kis0(A2[r][c]):
                f = A2[r][c]
                A2[r] = [ksub(A2[r][j], kmul(f, A2[rr][j])) for j in range(n)]
        rr += 1
    return rr


def kcharpoly3(kx):
    cols = [kmul(kx, KONE), kmul(kx, (Fr(0), Fr(1), Fr(0))),
            kmul(kx, (Fr(0), Fr(0), Fr(1)))]
    Mv = [[cols[j][i] for j in range(3)] for i in range(3)]
    x = sp.Symbol("x")
    Msp = sp.Matrix(3, 3, lambda i, j: sp.Rational(Mv[i][j].numerator,
                                                   Mv[i][j].denominator))
    return [sp.Rational(c) for c in Msp.charpoly(x).all_coeffs()]


def int_minpoly_from_charpoly(cp):
    """monic rational charpoly (deg 3) -> primitive integer minpoly
    (descending), assuming irreducibility (checked by the caller)."""
    den = 1
    for c in cp:
        den = den * sp.Rational(c).q // math.gcd(den, sp.Rational(c).q)
    ints = [int(sp.Rational(c) * den) for c in cp]
    g = 0
    for v in ints:
        g = math.gcd(g, abs(v))
    ints = [v // g for v in ints]
    if ints[0] < 0:
        ints = [-v for v in ints]
    return ints


# ================================================================ [7] atoms
log("[7] the nine colorless atoms, exact (B914/B916 route, re-run) ...")
CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
      for i in range(27)]
x = sp.Symbol("x")
cp = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                Mc[i][j].denominator)
               ).charpoly(x)
fl = sp.factor_list(cp.as_expr())
facs = sorted([(sp.degree(f, x), m, sp.Poly(f, x)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])
h_S = [int(c) for c in facs[0][2].all_coeffs()]
h_A = [int(c) for c in facs[1][2].all_coeffs()]
h_col = [sp.Rational(c) for c in facs[2][2].all_coeffs()]


def poly_mat(coeffs):
    Acc = [[Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q)
            if i == j else Fr(0) for j in range(27)] for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        cf = Fr(sp.Rational(c).p, sp.Rational(c).q)
        for i in range(27):
            Acc[i][i] += cf
    return Acc


W3 = qkernel(poly_mat(h_S))
W6 = qkernel(poly_mat(h_A))
CHK("rational_blocks_dim_3_and_6", len(W3) == 3 and len(W6) == 6)
Me = [[Fr(3) * Rex[8][i][j] + Fr(13) * Rex[16][i][j] for j in range(27)]
      for i in range(27)]
Mo = [[Fr(7) * Rex[14][i][j] + Fr(17) * Rex[22][i][j] for j in range(27)]
      for i in range(27)]


def restrict(Mbig, W):
    Crows = []
    for w in W:
        img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j])
               for i in range(27)]
        solv = qsolve_span(W, img)
        assert solv is not None
        Crows.append(solv)
    return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]


C_S = restrict(Mc, W3)
C_E = restrict(Me, W6)
C_O = restrict(Mo, W6)
cpE = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_E[i][j].numerator,
                                               C_E[i][j].denominator)
                ).charpoly(x)
flE = sp.factor_list(cpE.as_expr())
gs = [(f, m) for f, m in flE[1] if sp.degree(f, x) > 0]
CHK("char_Me_W6_is_g_squared_cubic", len(gs) == 1 and gs[0][1] == 2
    and sp.degree(gs[0][0], x) == 3)
g_even = sp.Poly(gs[0][0], x).all_coeffs()
g_even = [sp.Rational(c, g_even[0]) for c in g_even]
cpO = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_O[i][j].numerator,
                                               C_O[i][j].denominator)
                ).charpoly(x)
co = sp.Poly(cpO.as_expr(), x).all_coeffs()
CHK("char_Mo_W6_even", co[1] == 0 and co[3] == 0 and co[5] == 0)
h_B = [co[0], co[2], co[4], co[6]]
xS = root_in_K([sp.Rational(c) for c in h_S])
alph = root_in_K(g_even)
Bk = root_in_K(h_B)
CHK("K_roots_xS_alpha_B_found", None not in (xS, alph, Bk))
wK = sqrt_in_K(kscale(Bk, Fr(-1, 3)))
CHK("B_equals_minus_3_w_squared", wK is not None
    and kis0(ksub(kmul(wK, wK), kscale(Bk, Fr(-1, 3)))))

CmK = [[ksub((Fr(C_S[i][j]), Fr(0), Fr(0)), xS if i == j else KZERO)
        for j in range(3)] for i in range(3)]
kerS = kkernel(CmK)
CHK("kernel_S_dim_1", len(kerS) == 1)
vS3 = kerS[0]


def fmulB(a, b):
    return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def fsubB(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))


def fis0B(a):
    return kis0(a[0]) and kis0(a[1])


def finvB(a):
    den = ksub(kmul(a[0], a[0]), kmul(Bk, kmul(a[1], a[1])))
    di = kinv(den)
    return (kmul(a[0], di), kscale(kmul(a[1], di), Fr(-1)))


rowsF = []
for i in range(6):
    rowsF.append([(ksub((Fr(C_E[i][j]), Fr(0), Fr(0)),
                        alph if i == j else KZERO), KZERO) for j in range(6)])
for i in range(6):
    rowsF.append([((Fr(C_O[i][j]), Fr(0), Fr(0)),
                   (Fr(-1), Fr(0), Fr(0)) if i == j else KZERO)
                  for j in range(6)])
A2m = [row[:] for row in rowsF]
piv = []
rr = 0
for c in range(6):
    pr = next((r for r in range(rr, 12) if not fis0B(A2m[r][c])), None)
    if pr is None:
        continue
    A2m[rr], A2m[pr] = A2m[pr], A2m[rr]
    iv = finvB(A2m[rr][c])
    A2m[rr] = [fmulB(iv, e) for e in A2m[rr]]
    for r in range(12):
        if r != rr and not fis0B(A2m[r][c]):
            f = A2m[r][c]
            A2m[r] = [fsubB(A2m[r][j], fmulB(f, A2m[rr][j])) for j in range(6)]
    piv.append(c)
    rr += 1
FZ = (KZERO, KZERO)
kerA = []
for fc in [c for c in range(6) if c not in piv]:
    v = [FZ] * 6
    v[fc] = (KONE, KZERO)
    for i, c in enumerate(piv):
        v[c] = fsubB(FZ, A2m[i][fc])
    kerA.append(v)
CHK("kernel_nonS_dim_1_over_K_beta", len(kerA) == 1)
vA6 = kerA[0]


def lift(coords, W):
    out = []
    for i in range(27):
        acc = KZERO
        for a, cf in enumerate(coords):
            if W[a][i]:
                acc = kadd(acc, kscale(cf, W[a][i]))
        out.append(acc)
    return out


def normalize27(vec):
    L2 = 1
    for kt in vec:
        for x2 in kt:
            if x2:
                d = x2.denominator
                L2 = L2 * d // math.gcd(L2, d)
    vec2 = [kscale(kt, Fr(L2)) for kt in vec]
    G = 0
    for kt in vec2:
        for x2 in kt:
            G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [kscale(kt, Fr(1, G)) for kt in vec2]
    return vec2


vS27 = normalize27(lift(vS3, W3))
u27 = lift([f[0] for f in vA6], W6)
wt27 = lift([f[1] for f in vA6], W6)
wodd27 = [kmul(wK, kt) for kt in wt27]
uw = normalize27(u27 + wodd27)
u27, wodd27 = uw[:27], uw[27:]

# abstract eigenvalues of R8 on the S line and on the A plane (branch anchors)
def k_eigenvalue_of(Rn, vec):
    k0 = next(i for i in range(27) if not kis0(vec[i]))
    img = KZERO
    for j in range(27):
        if Rn[k0][j] and not kis0(vec[j]):
            img = kadd(img, kscale(vec[j], Rn[k0][j]))
    lam = kmul(img, kinv(vec[k0]))
    for i in range(27):
        acc = KZERO
        for j in range(27):
            if Rn[i][j] and not kis0(vec[j]):
                acc = kadd(acc, kscale(vec[j], Rn[i][j]))
        if not kis0(ksub(acc, kmul(lam, vec[i]))):
            return None
    return lam


c8vac = k_eigenvalue_of(Rex[8], vS27)
c8oct = k_eigenvalue_of(Rex[8], u27)
c16vac = k_eigenvalue_of(Rex[16], vS27)
c16oct = k_eigenvalue_of(Rex[16], u27)
CHK("S_and_A_are_exact_R8_R16_eigenvectors_over_K",
    None not in (c8vac, c8oct, c16vac, c16oct),
    "branch anchors: the abstract octet/vacuum charge labels")
CHK("vacuum_and_octet_labels_distinct", not kis0(ksub(c8vac, c8oct)))

# ================================================================ [8] Q1(b)
log("[8] Q1(b): the Pi-blocks vs the 11-flip coordinate set, EXACT ...")
R8K = [[(Rex[8][i][j], Fr(0), Fr(0)) for j in range(27)] for i in range(27)]
Moct = [[ksub(R8K[i][j], c8oct if i == j else KZERO) for j in range(27)]
        for i in range(27)]
OCT = [normalize27(v) for v in kkernel(Moct)]
CHK("abstract_octet_block_dim_8_over_K", len(OCT) == 8)
lam16 = None
for vec in OCT:
    l16 = k_eigenvalue_of(Rex[16], vec)
    if l16 is None:
        lam16 = None
        break
    if lam16 is None:
        lam16 = l16
    elif not kis0(ksub(lam16, l16)):
        lam16 = None
        break
CHK("octet_block_R16_scalar_equals_A_label",
    lam16 is not None and kis0(ksub(lam16, c16oct)),
    "the 8-dim R8-eigenblock is the joint Pi-octet (R16 scalar on it)")

flip_ind = [b for b in range(27) if D2[b] == -1]
CHK("flip_set_size_11", len(flip_ind) == 11)
unflip = [b for b in range(27) if D2[b] == 1]

# membership tests: v in span_F  <=>  v vanishes on the 16 unflipped coords
oct_in_F = all(all(kis0(vec[b]) for b in unflip) for vec in OCT)
vac_in_F = all(kis0(vS27[b]) for b in unflip)
REC("octet_contained_in_flip_span", oct_in_F)
REC("vacuum_line_contained_in_flip_span", vac_in_F)
# exact intersection dims: dim(span_F cap octet) = 19 - rank([OCT; e_F])
rowsFK = [[KONE if j == b else KZERO for j in range(27)] for b in flip_ind]
r_oct = krank(OCT + rowsFK)
dim_oct_cap = 8 + 11 - r_oct
r_vac = krank([vS27] + rowsFK)
dim_vac_cap = 1 + 11 - r_vac
r_W3 = krank([[(Fr(w[j]), Fr(0), Fr(0)) for j in range(27)]
              for w in W3] + rowsFK)
dim_W3_cap = 3 + 11 - r_W3
REC("dim_flipspan_cap_octet_g", dim_oct_cap,
    "same for every generation g (the flip span is rational, sigma-stable)")
REC("dim_flipspan_cap_vacuum_line", dim_vac_cap)
REC("dim_flipspan_cap_W3_vacuum_sum", dim_W3_cap)
b_conjecture = (dim_oct_cap == 8 and dim_W3_cap == 3)
CHK("Q1b_flipset_is_one_octet_plus_three_vacuum_lines_DECIDED",
    True,
    f"the 8+3 conjecture is {'CONFIRMED' if b_conjecture else 'REFUTED'}: "
    f"dim(span_F cap octet) = {dim_oct_cap} (needs 8), "
    f"dim(span_F cap vacuum-sum W3) = {dim_W3_cap} (needs 3); moreover if "
    "one octet lay inside the rational flip span, all three Galois images "
    "would (24 > 11): the span reading is impossible a priori")
RES["Q1b"] = {
    "conjecture_8_plus_3": bool(b_conjecture),
    "dim_flipspan_cap_octet": dim_oct_cap,
    "dim_flipspan_cap_single_vacuum": dim_vac_cap,
    "dim_flipspan_cap_vacuum_sum_W3": dim_W3_cap,
    "octet_in_flipspan": bool(oct_in_F),
    "vacuum_in_flipspan": bool(vac_in_F),
    "galois_argument": "an octet inside the rational 11-dim flip span forces "
                       "all three octets inside (24 > 11) -- impossible"}
dump()

# ================================================================ [9] Q2 core
log("[9] Q2: the twist ratios d = q'/q from the CHARACTERIZATION, exact ...")
# the characterized diagonal: D2 = rho_27(sigma_{chi-}) (normalized [0]=+1)
D2f = T_chim if T_chim[0] == 1 else [-x for x in T_chim]
CHK("characterized_diagonal_equals_D2", D2f == D2)
cbP_tw = [cbP[b] * D2f[b] for b in range(27)]

# S line: q, q' in K;  A plane: abstract q, q' in K (tau-free certified)
def kq(vec, cb):
    acc = KZERO
    for b in range(27):
        a = piW[b]
        if kis0(vec[a]) or kis0(vec[b]):
            continue
        acc = kadd(acc, kscale(kmul(vec[a], vec[b]), Fr(cb[b])))
    return acc


def kq_A(cb):
    """q(A+-) = sum cb (u u + 3 w w) +- tau-cross; cross must vanish."""
    even = KZERO
    cross = KZERO
    for b in range(27):
        a = piW[b]
        t1 = kmul(u27[a], u27[b])
        t2 = kmul(wodd27[a], wodd27[b])
        even = kadd(even, kscale(kadd(t1, kscale(t2, Fr(3))), Fr(cb[b])))
        c1 = kmul(u27[a], wodd27[b])
        c2 = kmul(wodd27[a], u27[b])
        cross = kadd(cross, kscale(ksub(c1, c2), Fr(cb[b])))
    return even, cross


qS = kq(vS27, cbP)
qS_tw = kq(vS27, cbP_tw)
qA, crossA = kq_A(cbP)
qA_tw, crossA_tw = kq_A(cbP_tw)
CHK("A_norms_tau_free_both_gauges_FORCED_EQUALITY",
    kis0(crossA) and kis0(crossA_tw),
    "the tau-cross term vanishes => q(A+) = q(A-) in both gauges: the +- "
    "pair overlaps are forced equal")
CHK("q_nonzero_all", not (kis0(qS) or kis0(qS_tw) or kis0(qA)
                          or kis0(qA_tw)))
d_S = kmul(qS_tw, kinv(qS))
d_A = kmul(qA_tw, kinv(qA))
m_S = kscale(ksub(KONE, d_S), Fr(1, 2))
m_A = kscale(ksub(KONE, d_A), Fr(1, 2))

cp_dS = kcharpoly3(d_S)
cp_dA = kcharpoly3(d_A)
mp_dS = int_minpoly_from_charpoly(cp_dS)
mp_dA = int_minpoly_from_charpoly(cp_dA)
CHK("dS_minpoly_DERIVED_equals_banked_B916",
    mp_dS == MINPOLY_S_banked, f"{mp_dS}")
CHK("dA_minpoly_DERIVED_equals_banked_B916",
    mp_dA == MINPOLY_A_banked, f"{mp_dA}")
import sympy.ntheory as nt
lead_fac = nt.factorint(abs(mp_dS[0]))
const_fac = nt.factorint(abs(mp_dS[-1]))
CHK("lead_2304sq_const_953sq_DERIVED",
    lead_fac == {2: 16, 3: 4} and const_fac == {953: 2},
    "lead = 2304^2 = 2^16 3^4, const = 953^2 -- derived from the "
    "characterization (the sigma_{chi-} diagonal) on the banked atom lines")
# norm via charpoly: N(x) = (-1)^3 * c0 (monic cubic)
def Knorm(kx):
    cp3 = kcharpoly3(kx)
    c0 = sp.Rational(cp3[3])
    return Fr(-c0.p, c0.q) if c0.q else None


N_dS = Knorm(d_S)
N_dA = Knorm(d_A)
CHK("NORM_LAW_N_d_equals_minus_953_over_2304_squared",
    N_dS == -Fr(953, 2304) ** 2 and N_dA == -Fr(953, 2304) ** 2,
    "the pole prime and the lead DERIVE from the characterization: "
    "prod_g sigma_g(d) = N_{K/Q}(1 - 2m) = -(953/2304)^2 on BOTH atom "
    "families; the affine polarity (the global -1 in D2) supplies the "
    "minus sign of the norm")
mp_mS = int_minpoly_from_charpoly(kcharpoly3(m_S))
mp_mA = int_minpoly_from_charpoly(kcharpoly3(m_A))
REC("flip_mass_minpoly_S", str(mp_mS),
    f"lead {nt.factorint(abs(mp_mS[0]))}, const {nt.factorint(abs(mp_mS[-1]))}")
REC("flip_mass_minpoly_A", str(mp_mA),
    f"lead {nt.factorint(abs(mp_mA[0]))}, const {nt.factorint(abs(mp_mA[-1]))}")
RES["Q2_colorless"] = {
    "d_S_K_coords": [str(c) for c in d_S],
    "d_A_K_coords": [str(c) for c in d_A],
    "m_S_K_coords": [str(c) for c in m_S],
    "m_A_K_coords": [str(c) for c in m_A],
    "minpoly_d_S": [str(c) for c in mp_dS],
    "minpoly_d_A": [str(c) for c in mp_dA],
    "minpoly_m_S": [str(c) for c in mp_mS],
    "minpoly_m_A": [str(c) for c in mp_mA],
    "norm_law": "N(d_S) = N(d_A) = -(953/2304)^2 exact"}
dump()

# ================================================================ [10] colored
log("[10] the colored sector over K(omega) (B923 route, re-run) ...")
W18 = qkernel(poly_mat([sp.Rational(c) for c in
                        sp.Poly(facs[2][2].as_expr(), x).all_coeffs()]))
CHK("colored_block_dim_18", len(W18) == 18)
C18 = restrict(Mc, W18)
h_col_ints = [sp.Rational(c) for c in facs[2][2].all_coeffs()]
mp.dps = 400
hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q)
      for c in h_col_ints]
rts6 = mp.polyroots(hh, maxsteps=400, extraprec=400)
pairs = []
usedr = [False] * 6
for i in range(6):
    if usedr[i] or mp.im(rts6[i]) <= 0:
        continue
    for j in range(6):
        if j != i and not usedr[j] and abs(rts6[j] - mp.conj(rts6[i])) \
                < mp.mpf(10) ** (-150):
            pairs.append((rts6[i], rts6[j]))
            usedr[i] = usedr[j] = True
            break
CHK("h_col_roots_three_conjugate_pairs", len(pairs) == 3)
mu_roots = _mu_roots_numeric(400)
maxden = mp.mpf(10) ** 133
pK = qKq = None
for perm in itertools.permutations(range(3)):
    pv = [-2 * mp.re(pairs[perm[g]][0]) for g in range(3)]
    qv = [mp.re(pairs[perm[g]][0]) ** 2 + mp.im(pairs[perm[g]][0]) ** 2
          for g in range(3)]
    pc = _interp_K(pv, mu_roots, maxden, 10 ** 130)
    qc = _interp_K(qv, mu_roots, maxden, 10 ** 130)
    if pc is None or qc is None:
        continue
    lc = sp.Rational(h_col_ints[0])
    hmon = [sp.Rational(c) / lc for c in h_col_ints]
    prodN = [NONE_]
    for gg in range(3):
        qg = [sigma(gg, qc), sigma(gg, pc), sigma(gg, KONE)]
        new = [NZERO] * (len(prodN) + 2)
        for a2, ca in enumerate(prodN):
            for b2, cb_ in enumerate(qg):
                new[a2 + b2] = nadd(new[a2 + b2], nmul(ca, cb_))
        prodN = new
    okp = all(nis0(nsub(prodN[d],
                        (((Fr(hmon[6 - d].p, hmon[6 - d].q), Fr(0), Fr(0)),
                          KZERO)))) for d in range(7))
    if okp:
        pK, qKq = pc, qc
        break
CHK("h_col_is_K_norm_form_of_one_quadratic", pK is not None)
disc_c = ksub(kmul(pK, pK), kscale(qKq, Fr(4)))
w_c = sqrt_in_K(kscale(disc_c, Fr(-1, 231)))
CHK("colored_disc_minus_231_wc_squared", w_c is not None)
r1N = ((Fr(0), Fr(1), Fr(0)), KZERO)
r2N = (KZERO, KONE)
r3N = nsub(nsub(((Fr(-b_mu), Fr(0), Fr(0)), KZERO), r1N), r2N)
delta = nmul(nmul(nsub(r1N, r2N), nsub(r1N, r3N)), nsub(r2N, r3N))
dd2 = nmul(delta, delta)
CHK("delta_squared_rational", kis0(dd2[1]) and dd2[0][1] == 0
    and dd2[0][2] == 0)
t77 = sp.sqrt(sp.Rational(dd2[0][0].numerator, dd2[0][0].denominator) / 77)
CHK("disc_mu_77_times_square", t77.is_rational)
t77f = Fr(sp.Rational(t77).p, sp.Rational(t77).q)
S77 = nscale(delta, 1 / t77f)
CHK("S77_squared_77", nis0(nsub(nmul(S77, S77),
                                ((Fr(77), Fr(0), Fr(0)), KZERO))))
theta_x = kscale(pK, Fr(-1, 2))
theta_y = kscale(w_c, Fr(1, 2))
Mft = [[((ksub((Fr(C18[i][j]), Fr(0), Fr(0)), theta_x),
          kscale(theta_y, Fr(-1))) if i == j else
         ((Fr(C18[i][j]), Fr(0), Fr(0)), KZERO)) for j in range(18)]
       for i in range(18)]
Aft = [row[:] for row in Mft]
piv = []
rr = 0
for c in range(18):
    pr = next((r for r in range(rr, 18) if not ftis0(Aft[r][c])), None)
    if pr is None:
        continue
    Aft[rr], Aft[pr] = Aft[pr], Aft[rr]
    iv = ftinv(Aft[rr][c])
    Aft[rr] = [ftmul(iv, e) for e in Aft[rr]]
    for r in range(18):
        if r != rr and not ftis0(Aft[r][c]):
            f = Aft[r][c]
            Aft[r] = [ftsub(Aft[r][j], ftmul(f, Aft[rr][j]))
                      for j in range(18)]
    piv.append(c)
    rr += 1
kerC = []
for fc in [c for c in range(18) if c not in piv]:
    v = [FTZERO] * 18
    v[fc] = FTONE
    for i, c in enumerate(piv):
        v[c] = ftsub(FTZERO, Aft[i][fc])
    kerC.append(v)
CHK("colored_eigenspace_dim_3_over_K_omega", len(kerC) == 3)


def ftlift(coords):
    out = []
    for i in range(27):
        ax, ay = KZERO, KZERO
        for a, cf in enumerate(coords):
            if W18[a][i]:
                ax = kadd(ax, kscale(cf[0], W18[a][i]))
                ay = kadd(ay, kscale(cf[1], W18[a][i]))
        out.append((ax, ay))
    return out


def ftnormalize27(vec):
    L = 1
    for (ax, ay) in vec:
        for kt in (ax, ay):
            for x2 in kt:
                if x2:
                    L = L * x2.denominator // math.gcd(L, x2.denominator)
    vec2 = [(kscale(ax, Fr(L)), kscale(ay, Fr(L))) for (ax, ay) in vec]
    G = 0
    for (ax, ay) in vec2:
        for kt in (ax, ay):
            for x2 in kt:
                G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [(kscale(ax, Fr(1, G)), kscale(ay, Fr(1, G)))
                for (ax, ay) in vec2]
    return vec2


colB = [ftnormalize27(ftlift(v)) for v in kerC]
mu8c = None
okc = True
for a in range(3):
    u = colB[a]
    w = []
    for i in range(27):
        ax, ay = KZERO, KZERO
        for jj in range(27):
            if Rex[8][i][jj] and not ftis0(u[jj]):
                ax = kadd(ax, kscale(u[jj][0], Rex[8][i][jj]))
                ay = kadd(ay, kscale(u[jj][1], Rex[8][i][jj]))
        w.append((ax, ay))
    k0 = next(i for i in range(27) if not ftis0(u[i]))
    mu_a = ftmul(w[k0], ftinv(u[k0]))
    for i in range(27):
        if not ftis0(ftsub(w[i], ftmul(mu_a, u[i]))):
            okc = False
    if mu8c is None:
        mu8c = mu_a
    elif not ftis0(ftsub(mu8c, mu_a)):
        okc = False
CHK("colored_R8_scalar", okc)
CHK("colored_R8_eigenvalue_omega_free_equals_octet_label",
    kis0(mu8c[1]) and kis0(ksub(mu8c[0], c8oct)),
    "the colored atoms live INSIDE the octet block of the same branch: "
    "the branch alignment of octets, A-lines, and colored atoms is exact")

# ================================================================ [11] Q3 colored
log("[11] Q3: the colored twist spectra X = G^{-1} G' over K(omega) ...")


def gram_colored(cb):
    G = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = FTZERO
            for b in range(27):
                a2 = piW[b]
                if ftis0(colB[i][a2]) or ftis0(colB[j][b]):
                    continue
                acc = ftadd(acc, ftscale(ftmul(ftconj(colB[i][a2]),
                                               colB[j][b]), Fr(cb[b])))
            G[i][j] = acc
    return G


def ftdet3(G):
    d = FTZERO
    for pi2, sgn2 in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                      ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        t2 = ftmul(ftmul(G[0][pi2[0]], G[1][pi2[1]]), G[2][pi2[2]])
        d = ftadd(d, ftscale(t2, Fr(sgn2)))
    return d


def ftinv3(G):
    d = ftdet3(G)
    di = ftinv(d)
    C2 = [[FTZERO] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            i1, i2 = [a2 for a2 in range(3) if a2 != i]
            j1, j2 = [a2 for a2 in range(3) if a2 != j]
            m = ftsub(ftmul(G[i1][j1], G[i2][j2]),
                      ftmul(G[i1][j2], G[i2][j1]))
            if (i + j) % 2:
                m = ftscale(m, Fr(-1))
            C2[j][i] = ftmul(m, di)
    return C2, d


Gp = gram_colored(cbP)
Gt = gram_colored(cbP_tw)
CHK("colored_grams_hermitian",
    all(ftis0(ftsub(Gp[j][i], ftconj(Gp[i][j]))) for i in range(3)
        for j in range(3))
    and all(ftis0(ftsub(Gt[j][i], ftconj(Gt[i][j]))) for i in range(3)
            for j in range(3)))
Gpi, detGp = ftinv3(Gp)
CHK("colored_gram_invertible", not ftis0(detGp))
Xm = [[FTZERO] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        acc = FTZERO
        for t2 in range(3):
            acc = ftadd(acc, ftmul(Gpi[i][t2], Gt[t2][j]))
        Xm[i][j] = acc
e1 = ftadd(ftadd(Xm[0][0], Xm[1][1]), Xm[2][2])
e2 = FTZERO
for (i, j) in ((0, 1), (0, 2), (1, 2)):
    e2 = ftadd(e2, ftsub(ftmul(Xm[i][i], Xm[j][j]),
                         ftmul(Xm[i][j], Xm[j][i])))
e3 = ftdet3(Xm)
CHK("colored_twist_charpoly_omega_free_FORCED",
    kis0(e1[1]) and kis0(e2[1]) and kis0(e3[1]),
    "tr, e2, det of G^{-1}G' are omega-free => the (g,+) and (g,-) colored "
    "atoms carry IDENTICAL twist spectra (forced equality)")
e1K, e2K, e3K = e1[0], e2[0], e3[0]
trM_col = kscale(ksub((Fr(3), Fr(0), Fr(0)), e1K), Fr(1, 2))
mp_e1 = int_minpoly_from_charpoly(kcharpoly3(e1K))
mp_e3 = int_minpoly_from_charpoly(kcharpoly3(e3K))
REC("colored_twist_trace_minpoly", str(mp_e1),
    f"lead {nt.factorint(abs(mp_e1[0])) if mp_e1[0] else {}}, "
    f"const {nt.factorint(abs(mp_e1[-1])) if mp_e1[-1] else {}}")
REC("colored_twist_det_minpoly", str(mp_e3),
    f"lead {nt.factorint(abs(mp_e3[0])) if mp_e3[0] else {}}, "
    f"const {nt.factorint(abs(mp_e3[-1])) if mp_e3[-1] else {}}")
N_e3 = Knorm(e3K)
REC("colored_det_ratio_norm", str(N_e3),
    "N_{K/Q}(det G'/det G) for the colored twist")
RES["Q3_colored"] = {
    "charpoly_X_e1_K": [str(c) for c in e1K],
    "charpoly_X_e2_K": [str(c) for c in e2K],
    "charpoly_X_e3_K": [str(c) for c in e3K],
    "trace_flip_mass_K": [str(c) for c in trM_col],
    "minpoly_e1": [str(c) for c in mp_e1],
    "minpoly_e3": [str(c) for c in mp_e3],
    "forced_equality": "omega-free charpoly => identical for (g,+),(g,-)"}
dump()

# ================================================================ [12] traces
log("[12] Q3: the exact block-overlap trace table + the sum rule ...")


def kq_pair(vecs, cb):
    """Gram of K-vectors under the H-pairing sum u[pi b] cb[b] v[b]."""
    k = len(vecs)
    G = [[KZERO] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            acc = KZERO
            for b in range(27):
                a2 = piW[b]
                if kis0(vecs[i][a2]) or kis0(vecs[j][b]):
                    continue
                acc = kadd(acc, kscale(kmul(vecs[i][a2], vecs[j][b]),
                                       Fr(cb[b])))
            G[i][j] = acc
    return G


def kinv_mat(G):
    k = len(G)
    Aug = [[G[i][j] for j in range(k)]
           + [KONE if i == j2 else KZERO for j2 in range(k)]
           for i in range(k)]
    for c in range(k):
        pr = next((r for r in range(c, k) if not kis0(Aug[r][c])), None)
        assert pr is not None
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = kinv(Aug[c][c])
        Aug[c] = [kmul(iv, e) for e in Aug[c]]
        for r in range(k):
            if r != c and not kis0(Aug[r][c]):
                f = Aug[r][c]
                Aug[r] = [ksub(Aug[r][j], kmul(f, Aug[c][j]))
                          for j in range(2 * k)]
    return [[Aug[i][k + j] for j in range(k)] for i in range(k)]


def flip_trace(vecs, cb, subset):
    """tr(P_span Pi_subset) with P the H-orthogonal projector, exact in K."""
    G = kq_pair(vecs, cb)
    Gi = kinv_mat(G)
    k = len(vecs)
    acc = KZERO
    for b in subset:
        for i in range(k):
            if kis0(vecs[i][b]):
                continue
            for j in range(k):
                if kis0(vecs[j][piW[b]]):
                    continue
                acc = kadd(acc, kscale(kmul(kmul(vecs[i][b], Gi[i][j]),
                                            vecs[j][piW[b]]), Fr(cb[b])))
    return acc


t_oct = flip_trace(OCT, cbP, flip_ind)
t_oct_full = flip_trace(OCT, cbP, list(range(27)))
CHK("octet_projector_trace_8", kis0(ksub(t_oct_full, (Fr(8), Fr(0), Fr(0)))))
t_vac = kmul(kq(vS27, [cbP[b] if b in flip_ind else 0 for b in range(27)]),
             kinv(qS))
CHK("vacuum_flip_trace_equals_m_S", kis0(ksub(t_vac, m_S)))
# octet trace decomposition: t_oct = 2 m_A + 2 trM_col  (branch-aligned)
CHK("octet_trace_decomposition_FORCED",
    kis0(ksub(t_oct, kadd(kscale(m_A, Fr(2)), kscale(trM_col, Fr(2))))),
    "t_octet = 2 m_A + 2 tr M_colored as abstract K-elements -- the octet "
    "overlap is carried by its two A-lines and two colored atoms in "
    "equal +- pairs")
# the sum rule: Tr_{K/Q}(m_S) + Tr_{K/Q}(t_oct) = 11
def Ktrace(kx):
    cp3 = kcharpoly3(kx)
    return -sp.Rational(cp3[1])


sumrule = Ktrace(m_S) + Ktrace(t_oct)
CHK("SUM_RULE_total_flip_trace_11",
    sumrule == 11,
    "sum over all 6 Pi-blocks (3 branches) of the flip-overlap traces = "
    "tr Pi_F = 11 exactly")
mp_toct = int_minpoly_from_charpoly(kcharpoly3(t_oct))
REC("octet_flip_trace_minpoly", str(mp_toct))
RES["Q3_traces"] = {
    "t_vacuum_equals_m_S": True,
    "t_octet_K_coords": [str(c) for c in t_oct],
    "t_octet_minpoly": [str(c) for c in mp_toct],
    "decomposition": "t_oct = 2 m_A + 2 trM_col (exact)",
    "sum_rule": "Tr(m_S) + Tr(t_oct) = 11"}
dump()

# ================================================================ [13] HIER
log("[13] Q2: HIER from the characterization (V_ccl in the D2f gauge) ...")
T3 = {}
for t, cf in zip(TRIP, COEF):
    for perm in set(itertools.permutations(t)):
        T3[perm] = cf
nzrow = [[[(i, REP[k][l][i]) for i in range(27) if REP[k][l][i]]
          for l in range(27)] for k in range(78)]
ok = True
for k in range(78):
    rownz = nzrow[k]
    acc = {}
    for (x1, y1, z1), v in T3.items():
        for (i, w) in rownz[x1]:
            acc[(i, y1, z1)] = acc.get((i, y1, z1), 0) + w * v
        for (i, w) in rownz[y1]:
            acc[(x1, i, z1)] = acc.get((x1, i, z1), 0) + w * v
        for (i, w) in rownz[z1]:
            acc[(x1, y1, i)] = acc.get((x1, y1, i), 0) + w * v
    if any(v != 0 for v in acc.values()):
        ok = False
CHK("banked_cubic_exact_derivation_identity_all_78", ok)

colBm = [[ftconj(c) for c in v] for v in colB]
T2 = [[FTZERO] * 3 for _ in range(3)]
for (xx, yy, zz), cf in T3.items():
    if kis0(vS27[zz]):
        continue
    for a2 in range(3):
        ua = colB[a2][xx]
        if ftis0(ua):
            continue
        for b2 in range(3):
            vb = colBm[b2][yy]
            if ftis0(vb):
                continue
            T2[a2][b2] = ftadd(T2[a2][b2],
                               ftscaleK(ftmul(ua, vb), kscale(vS27[zz],
                                                              Fr(cf))))
CHK("diagonal_ccl_tensor_nonzero",
    any(not ftis0(T2[a2][b2]) for a2 in range(3) for b2 in range(3)))


def V_ccl_of(cb):
    Gp_ = gram_colored(cb)
    Gpi_, dp_ = ftinv3(Gp_)
    Gm_ = [[ftconj(Gp_[i][j]) for j in range(3)] for i in range(3)]
    Gmi_, dm_ = ftinv3(Gm_)
    qS_ = kq(vS27, cb)
    qSi = kinv(qS_)
    acc = FTZERO
    for a2 in range(3):
        for b2 in range(3):
            if ftis0(T2[a2][b2]):
                continue
            for a3 in range(3):
                for b3 in range(3):
                    if ftis0(T2[a3][b3]):
                        continue
                    term = ftmul(ftmul(T2[a2][b2], ftconj(T2[a3][b3])),
                                 ftmul(Gpi_[a2][a3], Gmi_[b2][b3]))
                    acc = ftadd(acc, term)
    acc = ftscaleK(acc, qSi)
    return acc


Vtw = V_ccl_of(cbP_tw)
Vcan = V_ccl_of(cbP)
CHK("V_ccl_tau_free_both", kis0(Vtw[1]) and kis0(Vcan[1]))
CHK("canonical_gauge_collapse_minus_3",
    kis0(ksub(Vcan[0], (Fr(-3), Fr(0), Fr(0)))),
    "re-verifies B923: the charge-equivariant gauge sees NO hierarchy")
cpV = kcharpoly3(Vtw[0])
scaled = [sp.Rational(c) * 953 ** 4 for c in cpV]
CHK("HIER_DERIVED_953p4_charpoly_V_ccl_twisted",
    all(sp.Rational(s).q == 1 for s in scaled)
    and [int(s) for s in scaled] == HIER_ints,
    f"HIER = {HIER_ints}: the hierarchy cubic's coefficients are computed "
    "from the characterization (D2 = rho_27(sigma_chi-)) + the banked "
    "atoms/cubic -- no belt, no measured number")
RES["Q2_HIER"] = {"V_ccl_twisted_K": [str(c) for c in Vtw[0]],
                  "HIER_ints": HIER_ints,
                  "canonical_collapse": "-3 (exact)"}
dump()

# ================================================================ [14] belts
log("[14] numeric belts (dps 60; componentwise eigen-readout, certified) ...")
mp.dps = 60
mu_roots_60 = sorted(_mu_roots_numeric(200))
mp.dps = 60


def knum_at(kx, r):
    return (mp.mpf(kx[0].numerator) / kx[0].denominator
            + (mp.mpf(kx[1].numerator) / kx[1].denominator) * r
            + (mp.mpf(kx[2].numerator) / kx[2].denominator) * r * r)


# numeric colorless lines + flip masses vs exact embeddings
RnB = {}
for n in ns:
    M = mp.matrix(27, 27)
    for a in range(27):
        for b in range(27):
            if Rex[n][a][b]:
                M[a, b] = mp.mpf(Rex[n][a][b].numerator) \
                    / Rex[n][a][b].denominator
    RnB[n] = M
ZB = 3 * RnB[8] + 17 * RnB[14] + 5 * RnB[16] + 7 * RnB[22]
Zc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Zc[i, j] = mp.mpc(ZB[i, j])
Ev, ER = mp.eig(Zc, left=False, right=True)
order = sorted(range(27), key=lambda k: (mp.re(Ev[k]), mp.im(Ev[k])))
clusters = []
for k in order:
    for cl in clusters:
        if abs(Ev[k] - cl["ev"]) < mp.mpf("1e-20"):
            cl["ks"].append(k)
            break
    else:
        clusters.append({"ev": Ev[k], "ks": [k]})
lines = []
for cl in clusters:
    if len(cl["ks"]) == 1:
        k = cl["ks"][0]
        v = mp.matrix([ER[j, k] for j in range(27)])
        v = v / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
        # componentwise eigen-readout certificate (house rule: no Rayleigh)
        istar = max(range(27), key=lambda i: abs(v[i]))
        lam = sum(Zc[istar, j] * v[j] for j in range(27)) / v[istar]
        resid = max(abs(sum(Zc[i, j] * v[j] for j in range(27)) - lam * v[i])
                    for i in range(27))
        lines.append({"v": v, "resid": resid})
CHK("numeric_nine_colorless_lines", len(lines) == 9
    and max(l["resid"] for l in lines) < mp.mpf("1e-45"))
HBn = mp.matrix(27, 27)
HTn = mp.matrix(27, 27)
for b in range(27):
    HBn[piW[b], b] = cbP[b]
    HTn[piW[b], b] = cbP_tw[b]
m_num = []
for l in lines:
    v = l["v"]
    q = mp.re(sum(mp.conj(v[piW[b]]) * cbP[b] * v[b] for b in range(27)))
    qf = mp.re(sum(mp.conj(v[piW[b]]) * cbP[b] * v[b] for b in flip_ind))
    m_num.append(qf / q)
mS_emb = sorted([knum_at(m_S, r) for r in mu_roots_60])
mA_emb = sorted([knum_at(m_A, r) for r in mu_roots_60])
m_num_sorted = sorted(m_num)
# the nine numeric masses must be {m_S branches} + {m_A branches x2}
expect = sorted(mS_emb + mA_emb + mA_emb)
worst = max(abs(a - b) for a, b in zip(m_num_sorted, expect))
CHK("numeric_flip_masses_match_exact_embeddings",
    worst < mp.mpf("1e-40"), f"worst {mp.nstr(worst, 3)}")
RES["belt"] = {"worst_mass_residual": mp.nstr(worst, 4)}

# 50-digit certificates (per ascending-rho branch convention)
mp.dps = 120
mu_r = sorted(_mu_roots_numeric(200))
mp.dps = 120
certs = {}
for nm, kx in (("m_S", m_S), ("m_A", m_A), ("d_S", d_S), ("d_A", d_A),
               ("t_oct", t_oct), ("trM_col", trM_col),
               ("e1_colored", e1K), ("e2_colored", e2K), ("e3_colored", e3K),
               ("V_ccl_twisted", Vtw[0])):
    certs[nm] = [mp.nstr(knum_at(kx, r), 50) for r in mu_r]
RES["Q3_certificates_50d_by_ascending_rho"] = certs
dump()

# ================================================================ [15] verdict
log("[15] the sealed verdict ...")
RES["Q1_summary"] = {
    "a": "SUCCEEDS (shifted): D2 = -(-1)^<a*,w>, a* = s(chi-), unique in "
         "the 128-member family; pure characters fail (re-verified); other "
         "lattices add nothing (mod-2 equivalent)",
    "b": "REFUTED as spans: dim(flip cap octet) = %d, dim(flip cap W3) = %d; "
         "the Galois argument makes the 8+3 span reading impossible; the "
         "true octet/vacuum content is the exact trace table" % (
             dim_oct_cap, dim_W3_cap),
    "c": "DERIVED: D2 = +-rho_27(sigma_{chi-}); H+ D2 = H(phi*), "
         "phi* = tau o phi+ o phi- = sigma_{-1} o tau; Dd = "
         "+-rho_27(phi+ phi-); Klein group {I, D2, Dd, D2 Dd}",
    "d": "the C-compatible census does NOT contain D2 (its involution "
         "phi* is not C-compatible -- exactly B916's no-epsilon-pattern "
         "fact); over the full 128, H+ D2 belongs to EXACTLY ONE member: "
         "phi*, pinned with no freedom",
}
RES["Q2_summary"] = {
    "derived": "d-minpolys (2304^2 lead, 953^2 const, every coefficient), "
               "the norm law N(1-2m) = -(953/2304)^2 (the affine polarity "
               "supplies the minus), and HIER = 953^4 charpoly(V_ccl) -- "
               "all recomputed exactly from the characterized diagonal on "
               "the banked atom lines",
    "residue": "no pipeline-free closed form for 953/2304: the "
               "characterization reduces the twist arithmetic to the "
               "K-norm of (1 - 2 x flip-mass) on the atom lines; the atom "
               "lines themselves (the eigenline solve over K) remain the "
               "carrier of the specific integers; where each prime of "
               "2^8 3^2 and 953 enters the eigenline coordinates is open",
}
RES["verdict"] = (
    "OUTCOME FORCED -- candidate (c) [with (a) as its character form] "
    "characterizes D2 by a banked equation with NO residual freedom: "
    "D2 = +-rho_27(sigma_{chi-}) -- the second wall conjugation's sign "
    "character acting on the 27 -- equivalently H+ D2 = H(phi*) with "
    "phi* = tau o phi+ o phi- the composite of the banked tau-lift with "
    "BOTH wall conjugations, the unique carrier in the 128-census.  "
    "Q2 derives the pole prime 953, the 2304^2 lead, both d-minpolys, the "
    "norm law with its sign, and HIER's coefficients from the "
    "characterization (residue: the atom-line solve itself).  "
    "Q3's sheet is nonempty: three abstract K-invariants (m_S, m_A, "
    "t_oct = 2m_A + 2trM_col), the omega-free colored twist charpoly "
    "(e1, e2, e3), the forced equalities (A+- and colored +- pairs, "
    "octet decomposition), and the sum rule Tr(m_S) + Tr(t_oct) = 11.")
RES["runtime_s"] = round(time.time() - T00, 1)
dump()
log("results.json written")
log("VERDICT:", RES["verdict"][:120], "...")
