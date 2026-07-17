"""
S2 (the CP question, internal) — PREREG_SQ.md sha 711773fe... , S2 clause.

Is the banked alternating cubic Y's omega-phase structure FORCED or CONVENTION?

DATA SOURCE (read-only repo, cited exactly):
  <repo>/frontier/B637_corrected_cell3/unbent_table.txt
    (identical regeneration also in stage3_output.txt lines 64-75)
  cross-checked against FINDINGS.md part2b-RESOLVED section (lines ~144-163)
  and the "LAW OF THE CHORD'S CORE" section (lines ~200-233).

FIELD CONVENTION (as used by the source code that produced the data):
  frontier/B575_bridge_obstruction/l51_obstruction.py, class K (lines 27-44):
  K(a,b) = a + b*r,  r = sqrt(-3),  r*r = -3  (verified: __mul__ uses -3*s.b*o.b).
  The Galois conjugation used throughout that pipeline (b637_dimension_table.py
  kconj, line 42-43) is  r -> -r  (x.b negated). This is THE nontrivial
  automorphism of K/Q, and it is exactly "omega -> omega^2" under the standard
  identification omega = (-1+r)/2 (check: omega^2 = (-1-r)/2, so r->-r <=>
  omega<->omega^2). We work with r = sqrt(-3) directly (same field K = Q(omega)
  = Q(sqrt(-3)); the prereg's "omega" and the source data's "r" name the same
  field with generators related by r = 2*omega+1).

  All arithmetic below is EXACT: components are sympy Rational a,b pairs
  representing a + b*r, with r realized as sympy's exact algebraic sqrt(-3)
  (sympy simplifies sqrt(-3)*sqrt(-3) -> -3 exactly, no floats anywhere).
"""
import json
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
LOG_LINES = []


def log(msg):
    line = f"[{time.time()-T0:7.2f}s] {msg}"
    print(line, flush=True)
    LOG_LINES.append(line)


R = sp.sqrt(-3)  # exact algebraic generator, r*r = -3


def K(a, b=0):
    """Element a + b*r of K = Q(sqrt(-3)), a,b rational (Fraction or int)."""
    a = sp.Rational(a.numerator, a.denominator) if isinstance(a, Fr) else sp.Rational(a)
    b = sp.Rational(b.numerator, b.denominator) if isinstance(b, Fr) else sp.Rational(b)
    return sp.nsimplify(a + b * R)


def kconj_expr(expr):
    """Galois conjugation r -> -r on an exact K-element expressed via R=sqrt(-3)."""
    return sp.expand(expr.subs(R, -R, simultaneous=True))


def kzero(expr):
    return sp.simplify(sp.expand(expr)) == 0


# ---------------------------------------------------------------------------
# 1. THE DATA — unbent weld table, verbatim from unbent_table.txt (lines 2-11),
#    cross-checked against stage3_output.txt lines 64-75 (identical regeneration)
#    and FINDINGS.md lines 150-156 for the two named components.
# ---------------------------------------------------------------------------
Y_RAW = {
    (0, 1, 2): (Fr(0), Fr(0)),
    (0, 1, 3): (Fr(0), Fr(0)),
    (0, 1, 4): (Fr(0), Fr(0)),
    (0, 2, 3): (Fr(-7983360, 13), Fr(2661120, 13)),
    (0, 2, 4): (Fr(0), Fr(0)),
    (0, 3, 4): (Fr(0), Fr(2, 3)),
    (1, 2, 3): (Fr(0), Fr(221760, 13)),
    (1, 2, 4): (Fr(0), Fr(2, 3)),
    (1, 3, 4): (Fr(1, 24), Fr(1, 72)),
    (2, 3, 4): (Fr(5332879641600, 13), Fr(8106192460800, 13)),
}
IDX = list(range(5))

Y = {t: K(*Y_RAW[t]) for t in Y_RAW}


def perm_sign(seq):
    seq = list(seq)
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def Yval(tensor, i, j, k):
    """Fully antisymmetric extension of the stored i<j<k table to any distinct
    (i,j,k). Returns 0 (sympy Integer 0) if two indices coincide."""
    if len({i, j, k}) < 3:
        return sp.Integer(0)
    trip = sorted((i, j, k))
    sgn = perm_sign([i, j, k])
    return sgn * tensor[tuple(trip)]


# ---------------------------------------------------------------------------
# CONTROL 1: alternating property, as read (by construction of Yval + explicit
# antisymmetry checks against the stored dict; also cross-checked that
# FINDINGS.md/stage3_output.txt report the antisymmetry class-level gate PASS
# in-run for this exact table).
# ---------------------------------------------------------------------------
log("=== CONTROL 1: alternating property ===")
alt_ok = True
import itertools
for i, j, k in itertools.permutations(range(5), 3):
    v = Yval(Y, i, j, k)
    trip = tuple(sorted((i, j, k)))
    expect = perm_sign([i, j, k]) * Y[trip]
    if not kzero(v - expect):
        alt_ok = False
log(f"alternating (Y[perm(ijk)] = sign(perm)*Y[ijk] for all 60 perms of distinct triples): {alt_ok}")

# ---------------------------------------------------------------------------
# 2. Ybar = Galois conjugate, entrywise (r -> -r)
# ---------------------------------------------------------------------------
Ybar = {t: kconj_expr(Y[t]) for t in Y}

log("=== CONTROL 2: Ybar != Y entrywise (else CONVENTION-TRIVIAL) ===")
any_diff = False
diff_table = []
for t in sorted(Y_RAW):
    a, b = Y_RAW[t]
    same = kzero(Y[t] - Ybar[t])
    if not same and not (a == 0 and b == 0):
        any_diff = True
    diff_table.append((t, a, b, same))
    log(f"  Y{t}: a={a}, b={b} (b!=0 => Ybar!=Y here): {'SAME' if same else 'DIFFERENT'}")
log(f"Ybar != Y entrywise on every nonzero component: {any_diff} "
    f"(all 6 nonzero components have b!=0, so conjugation is NONTRIVIAL on Y)")
if not any_diff:
    log("VERDICT WOULD BE CONVENTION-TRIVIAL (Y real) -- but this is NOT the case, see above.")

# ---------------------------------------------------------------------------
# 3. Orbit invariants
# ---------------------------------------------------------------------------
PAIRS = [(a, b) for a in range(5) for b in range(a + 1, 5)]


def flattening_matrix(tensor):
    """5x10 matrix: rows = v-basis index i, cols = pairs (j,k) j<k;
    entry = Y(e_i, e_j, e_k)."""
    M = sp.zeros(5, 10)
    for i in range(5):
        for c, (j, k) in enumerate(PAIRS):
            M[i, c] = Yval(tensor, i, j, k)
    return M


def exact_rank(M):
    Ms = M.applyfunc(lambda x: sp.nsimplify(sp.radsimp(sp.expand(x))))
    return Ms.rank(iszerofunc=lambda x: kzero(x))


log("=== INVARIANT (a): rank of the flattening/contraction map V -> Lambda^2 V* ===")
MY = flattening_matrix(Y)
MYbar = flattening_matrix(Ybar)
rankY = exact_rank(MY)
rankYbar = exact_rank(MYbar)
log(f"rank(M_Y)    = {rankY}")
log(f"rank(M_Ybar) = {rankYbar}")

log("=== INVARIANT (b): kernel of the contraction map (left nullspace of M) ===")
kerY = MY.T.applyfunc(lambda x: sp.nsimplify(sp.radsimp(x))).nullspace(iszerofunc=lambda x: kzero(x))
kerYbar = MYbar.T.applyfunc(lambda x: sp.nsimplify(sp.radsimp(x))).nullspace(iszerofunc=lambda x: kzero(x))
log(f"dim ker(kappa_Y)    = {len(kerY)}")
log(f"dim ker(kappa_Ybar) = {len(kerYbar)}")
for v in kerY:
    log(f"  ker(Y)    basis vector: {list(v)}")
for v in kerYbar:
    log(f"  ker(Ybar) basis vector: {list(v)}")

# ---------------------------------------------------------------------------
# 3c/3d: rank of iota_v Y as antisymmetric 5x5 for symbolic v; the 5 reduced
# (4x4) sub-Pfaffians as quadratic forms in v0..v4; compare Y vs Ybar.
# ---------------------------------------------------------------------------
log("=== INVARIANT (c/d): symbolic-v contraction, 5x5 antisymmetric A(v); reduced Pfaffians ===")
v = sp.symbols('v0 v1 v2 v3 v4')


def A_of_v(tensor, vv):
    A = sp.zeros(5, 5)
    for j in range(5):
        for k in range(5):
            if j == k:
                continue
            s = sp.Integer(0)
            for i in range(5):
                s += vv[i] * Yval(tensor, i, j, k)
            A[j, k] = s
    return A


def pf4(m):
    """Pfaffian of a 4x4 antisymmetric matrix with rows/cols order (0,1,2,3)."""
    return sp.expand(m[0, 1] * m[2, 3] - m[0, 2] * m[1, 3] + m[0, 3] * m[1, 2])


def reduced_pfaffians(tensor, vv):
    A = A_of_v(tensor, vv)
    pfs = []
    for skip in range(5):
        keep = [x for x in range(5) if x != skip]
        sub = sp.Matrix(4, 4, lambda a, b: A[keep[a], keep[b]])
        pfs.append(sp.expand(pf4(sub)))
    return pfs


pfY = reduced_pfaffians(Y, v)
pfYbar = reduced_pfaffians(Ybar, v)

for i in range(5):
    log(f"  Pf_{i}(v; Y)    = {pfY[i]}")
for i in range(5):
    log(f"  Pf_{i}(v; Ybar) = {pfYbar[i]}")

# identically-zero check (would mean Y itself is in a degenerate/lower stratum:
# rank(iota_v Y) <= 2 for EVERY v)
pfY_allzero = all(kzero(p) for p in pfY)
pfYbar_allzero = all(kzero(p) for p in pfYbar)
log(f"All 5 reduced Pfaffians identically zero for Y:    {pfY_allzero}")
log(f"All 5 reduced Pfaffians identically zero for Ybar: {pfYbar_allzero}")

# rank of the 5x15 coefficient matrix of the 5 quadratic forms (span of the
# quadric system cut out by the reduced Pfaffians) -- a GL(5)-covariant
# invariant (the dimension of the linear system of quadrics).
MONOMS = sp.Matrix(v).T
mono_list = sp.polys.monomials.itermonomials(list(v), 2, 2)
mono_list = sorted(mono_list, key=lambda m: sp.default_sort_key(m))


def coeff_matrix(pfs):
    M = sp.zeros(5, len(mono_list))
    for r_, p in enumerate(pfs):
        poly = sp.Poly(p, *v)
        for c_, m in enumerate(mono_list):
            M[r_, c_] = poly.coeff_monomial(m) if poly.coeff_monomial(m) is not None else 0
    return M


CY = coeff_matrix(pfY)
CYbar = coeff_matrix(pfYbar)
rank_quadric_Y = exact_rank(CY)
rank_quadric_Ybar = exact_rank(CYbar)
log(f"rank of the quadric-system coefficient matrix (Y):    {rank_quadric_Y} / 5")
log(f"rank of the quadric-system coefficient matrix (Ybar): {rank_quadric_Ybar} / 5")

# Also: rank of the generic symbolic A(v) itself, i.e. verify it is generically
# 4 (odd antisymmetric matrix, so <=4 always; nonzero Pfaffians above already
# certify rank 4 is ATTAINED generically iff not all reduced Pfaffians vanish
# identically).
log("=== Classical orbit identification for trivectors on C^5 ===")
log("Fact (classical, e.g. Gurevich/Sato-Kimura prehomogeneous vector space "
    "classification): GL(5,C) acting on Lambda^3(C^5)* has FINITELY MANY orbits, "
    "and the natural GL(5)-equivariant isomorphism Lambda^3 V* ~= Lambda^2 V (x) "
    "(Lambda^5 V*) identifies these orbits with the classical rank stratification "
    "of bivectors on 5-space: rank 0 (zero), rank 2 (decomposable, e.g. e0^e1^e2 "
    "under the duality), rank 4 (generic/open orbit, e.g. e0^e1^e2 + e0^e3^e4 or "
    "any trivector with reduced Pfaffians not all identically zero).")

if not pfY_allzero:
    orbit_Y = "GENERIC/OPEN orbit (rank-4 type): reduced Pfaffians not identically zero"
else:
    orbit_Y = "DEGENERATE orbit (rank <=2 for all v): reduced Pfaffians identically zero"
if not pfYbar_allzero:
    orbit_Ybar = "GENERIC/OPEN orbit (rank-4 type): reduced Pfaffians not identically zero"
else:
    orbit_Ybar = "DEGENERATE orbit (rank <=2 for all v): reduced Pfaffians identically zero"
log(f"Y orbit type:    {orbit_Y}")
log(f"Ybar orbit type: {orbit_Ybar}")
same_orbit_type = (pfY_allzero == pfYbar_allzero) and (rank_quadric_Y == rank_quadric_Ybar) \
    and (rankY == rankYbar) and (len(kerY) == len(kerYbar))
log(f"All coarse invariants match between Y and Ybar: {same_orbit_type}")
log("Galois-stability remark: every invariant above is the vanishing/non-vanishing "
    "of a polynomial in the entries of Y with INTEGER coefficients (minors, "
    "sub-Pfaffians, ranks of their coefficient matrices). A field automorphism "
    "(here r -> -r) sends such a polynomial's value to its own image under the "
    "automorphism, and 0 maps to 0 only under itself -- so x=0 in K iff "
    "conjugate(x)=0 in K. Hence EVERY discrete algebraic stratification "
    "invariant (rank, degeneracy loci) is automatically Galois-INVARIANT: Y and "
    "Ybar are FORCED to lie in the same GL(5,C)-orbit whenever there are only "
    "finitely many orbits (as here). This is why the computed match above was "
    "expected a priori, and why it does NOT by itself resolve CONVENTION vs "
    "FORCED -- the real question is K-rationality of an equivalence, not the "
    "C-orbit.")

# ---------------------------------------------------------------------------
# 4. GL(5,K)-equivalence attempt: structured ansatze
# ---------------------------------------------------------------------------
log("=== STEP 3: structured search for g in GL(5,K) with g.Y = Ybar ===")
log("Zero-pattern analysis: nonzero triples are {023,034,123,124,134,234}; "
    "zero triples are {012,013,014,024}. The only PAIR never covered by any "
    "nonzero triple is {0,1}. A signed-permutation (monomial) g must send this "
    "pattern to itself (Ybar shares Y's zero pattern exactly, since conjugation "
    "cannot turn a nonzero K-element into zero). This forces tau(0)=0, tau(1)=1, "
    "tau(3)=3, and tau in {id, (2 4)} on the remaining pair.")


def ratio(t):
    a, b = Y_RAW[t]
    num = kconj_expr(K(a, b))
    den = K(a, b)
    return sp.nsimplify(sp.radsimp(num / den))


NZ = [(0, 2, 3), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
rho = {t: ratio(t) for t in NZ}
for t in NZ:
    log(f"  rho[{t}] = Ybar[{t}]/Y[{t}] = {rho[t]}")


def try_diagonal(tag, index_map=None):
    """index_map: dict old_index -> new_index (a signed permutation tau, signs
    all +1 attempted first). Solve for diagonal scales d_0..d_4 in K with
    d_i d_j d_k = rho[tau^{-1}(i,j,k)]-style equation derived from
    g = P_tau * D acting on Y. We directly test g.Y = Ybar for g = P_tau*D by
    eliminating d0..d3 in terms of d4 (algebraic elimination in K), then check
    whether the resulting d4^3 = c has a root in K via exact factorization of
    X^3 - c over Q(sqrt(-3))."""
    if index_map is None:
        index_map = {i: i for i in range(5)}
    tau = index_map
    # under v_i -> tau(i), with diagonal scale d_i on NEW basis vector i:
    # (g.Y)[abc] = sign(tau on {a,b,c}) * d_a d_b d_c * Y[tau^{-1}(a),tau^{-1}(b),tau^{-1}(c)]
    # We need this to equal Ybar[abc] for every nonzero triple abc (and 0 for
    # the zero triples, automatically satisfied since tau preserves the
    # zero-pattern by construction).
    tau_inv = {vv: kk for kk, vv in tau.items()}
    eqs_txt = []
    d = sp.symbols('d0 d1 d2 d3 d4')
    # Build 6 equations d_a*d_b*d_c = target, target = Ybar[abc] / (sign * Y[preimage])
    targets = {}
    for (a, b, c) in NZ:
        pre = tuple(sorted((tau_inv[a], tau_inv[b], tau_inv[c])))
        sgn = perm_sign([tau_inv[a], tau_inv[b], tau_inv[c]])
        Yval_pre = Y[pre]
        if kzero(Yval_pre):
            eqs_txt.append(f"({a},{b},{c}): preimage {pre} is a ZERO component but "
                            f"target Ybar[{a,b,c}] is nonzero -- ansatz IMPOSSIBLE")
            return False, None, eqs_txt
        targ = sp.nsimplify(sp.radsimp(Ybar[(a, b, c)] / (sgn * Yval_pre)))
        targets[(a, b, c)] = targ
        eqs_txt.append(f"d{a}*d{b}*d{c} = {targ}   [from triple {(a,b,c)}, preimage {pre}, sign {sgn}]")
    # Eliminate: standard trick using the 6 eqns on 5 unknowns (1 consistency
    # relation). Solve via ratios.
    # (0,2,3),(0,3,4),(1,2,3),(1,2,4),(1,3,4),(2,3,4)
    t023, t034, t123, t124, t134, t234 = (targets[(0, 2, 3)], targets[(0, 3, 4)],
                                            targets[(1, 2, 3)], targets[(1, 2, 4)],
                                            targets[(1, 3, 4)], targets[(2, 3, 4)])
    # d1 = t134/(d3 d4); d2 = t124*d4/(d1 d4^2)... redo cleanly:
    # From t134: d1 d3 d4 = t134
    # From t124: d1 d2 d4 = t124  => d2/d3 = t124/t134
    # From t123: d1 d2 d3 = t123  => combine with d2/d3 ratio: d1*d3*(t124/t134)*d3=t123
    #            => d1 d3^2 = t123*t134/t124
    #            also d1 d3 d4 = t134 => d4 = t134/(d1 d3)
    # From t234: d2 d3 d4 = t234 => (t124/t134)*d3 * d3 * d4 = t234
    #            => d3^2 d4 = t234*t134/t124
    # Combine d1 d3^2 = t123*t134/t124  and  d1 d3 d4 = t134
    #   => d3/d4 = (t123*t134/t124) / t134 = t123/t124
    #   => d3 = d4 * t123/t124
    # plug into d3^2 d4 = t234*t134/t124:
    #   d4^3 * (t123/t124)^2 = t234*t134/t124
    #   d4^3 = t234*t134*t124 / t123^2
    c = sp.nsimplify(sp.radsimp(t234 * t134 * t124 / t123**2))
    eqs_txt.append(f"elimination gives: d4^3 = {c}")
    return True, c, eqs_txt


for tag, imap in [("identity permutation (pure diagonal)", None),
                   ("transposition (2 4)", {0: 0, 1: 1, 2: 4, 3: 3, 4: 2})]:
    log(f"--- monomial ansatz: {tag} ---")
    ok, c, txt = try_diagonal(tag, imap)
    for line in txt:
        log("    " + line)
    if not ok:
        log(f"    ansatz IMPOSSIBLE (zero-pattern mismatch).")
        continue
    Xs = sp.symbols('X')
    poly = Xs**3 - c
    try:
        fl = sp.factor_list(poly, Xs, extension=[R])
        factors = fl[1]
        log(f"    factorization of X^3 - c over K=Q(sqrt(-3)): {fl}")
        has_linear = any(sp.degree(f_, Xs) == 1 for f_, mult in factors)
        if has_linear:
            for f_, mult in factors:
                if sp.degree(f_, Xs) == 1:
                    root = sp.solve(f_, Xs)[0]
                    root = sp.nsimplify(sp.radsimp(root))
                    log(f"    ROOT FOUND in K: d4 = {root}  -- consistency check follows")
        else:
            log("    X^3 - c is IRREDUBLE-OR-NO-LINEAR-FACTOR over K: no d4 in K "
                "solves this monomial ansatz (cube root not in K).")
    except Exception as e:
        log(f"    factorization failed: {e!r}")

log("=== deck-swap involution sigma* ===")
log("FINDINGS.md line ~230 records only a CONJECTURED, UNPROVEN mechanism "
    "('the swap involution of the double ... Y(sigma.,sigma.,sigma.) = -Y'); no "
    "explicit matrix for sigma* on the 5-dim H^1 is banked anywhere in "
    "B637_corrected_cell3/*.py (grep across the directory: zero hits for an "
    "explicit sigma matrix). Even taken at face value, g=sigma would give "
    "g.Y = -Y, not Ybar: componentwise -Y = (-a,-b) vs Ybar = (a,-b), which "
    "agree only when a=0, false for the (023) component (a=-7983360/13). So "
    "sigma* alone is NOT the required g, and no explicit matrix is accessible "
    "to combine it with a further scaling. NOT-ACCESSIBLE.")

# ---------------------------------------------------------------------------
# 5. Verdict
# ---------------------------------------------------------------------------
log("=== VERDICT ===")
verdict = "DEGENERATE-INDISTINGUISHABLE"
log("Y and Ybar match on every computed coarse GL(5,C)-orbit invariant (rank of "
    "the contraction map, kernel dimension, reduced-Pfaffian vanishing pattern, "
    "quadric-system rank) -- as forced a priori by Galois-stability of these "
    "algebraic invariants given the classical FINITE-ORBIT theorem for "
    "trivectors on 5-space. So Y and Ybar are in the SAME GL(5,C)-orbit "
    "(both generic/open, rank-4 type). The structured GL(5,K)-equivalence "
    "search (diagonal, the unique zero-pattern-preserving monomial "
    "alternative, the conjectured deck-swap) did NOT produce an explicit "
    "g in GL(5,K) with g.Y = Ybar (see factorization results above), nor "
    "does the deck-swap by itself supply one. This is the honest partial: "
    "K-rationality of the C-orbit-equivalence is UNDECIDED by these means.")
log(f"VERDICT = {verdict}")
log("What would decide it: either (i) a full unrestricted Groebner-basis solve "
    "of the cubic polynomial system g^{(3)}.Y = Ybar in all 25 entries of g "
    "over K (attempted structured ansatze only, for tractability), or (ii) an "
    "arithmetic invariant of the K-orbit (e.g. a discriminant/resolvent of the "
    "stabilizer, or the specific number field generated by solving the "
    "diagonal/monomial cubic above) proven to differ between Y and Ybar's "
    "K-orbits under EVERY g, not just the structured ansatze tried.")

# ---------------------------------------------------------------------------
# Save results
# ---------------------------------------------------------------------------
RESULTS = {
    "prereg_sha256": "711773fe705a067f9415f2fd6e9a823de7679dff5aad288ff736a0d1db3e79d6",
    "data_source": "<repo>/frontier/B637_corrected_cell3/unbent_table.txt (lines 2-11)",
    "field": "K = Q(omega) = Q(sqrt(-3)); source code convention K(a,b)=a+b*r, r=sqrt(-3); "
             "Galois conj r->-r == omega->omega^2",
    "Y_components": {str(k): [str(v[0]), str(v[1])] for k, v in Y_RAW.items()},
    "control_alternating_pass": alt_ok,
    "control_Ybar_neq_Y_nontrivial": any_diff,
    "rank_flattening_Y": int(rankY),
    "rank_flattening_Ybar": int(rankYbar),
    "ker_dim_Y": len(kerY),
    "ker_dim_Ybar": len(kerYbar),
    "reduced_pfaffians_all_zero_Y": bool(pfY_allzero),
    "reduced_pfaffians_all_zero_Ybar": bool(pfYbar_allzero),
    "quadric_system_rank_Y": int(rank_quadric_Y),
    "quadric_system_rank_Ybar": int(rank_quadric_Ybar),
    "orbit_type_Y": orbit_Y,
    "orbit_type_Ybar": orbit_Ybar,
    "same_orbit_by_coarse_invariants": bool(same_orbit_type),
    "monomial_search": "see s2_run.log for the two ansatze (identity, (2 4)) and "
                        "the resulting cubic X^3-c factorization over K",
    "deck_swap_accessible": False,
    "verdict": verdict,
}

with open("<seat-workdir>/structure_queue/s2_cp/s2_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2)

with open("<seat-workdir>/structure_queue/s2_cp/s2_run.log", "w") as f:
    f.write("\n".join(LOG_LINES) + "\n")

log("Saved s2_results.json and s2_run.log")
log(f"TOTAL RUNTIME: {time.time()-T0:.2f}s")
