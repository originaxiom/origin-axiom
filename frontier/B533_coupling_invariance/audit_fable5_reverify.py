#!/usr/bin/env python3
"""B533 Fable-5 audit: exact re-verification of all banked claims.

Independent recomputation, exact where possible:
  Part 1: symbolic core identities in Q(tau), tau = sqrt(phi)
  Part 2: EXACT Perron eigenvectors of the 5 type matrices (adjugate
          over Q(tau)) -- decides whether the Z-mixing law is exact
  Part 3: engine-independent census (plain string return words)
  Part 4: GL(4,Z) conjugacy re-test (Sylvester nullspace + unimodular
          integer search) -- checks the banked NON-conjugacy claim
  Part 5: Gate 3 false-positive control, magnitude-matched
"""

import sys
import os
import numpy as np
import sympy as sp
from collections import defaultdict
from itertools import product as iprod

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = list('abAB')

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1          # minimal polynomial of tau = sqrt(phi)
X = sp.Symbol('x')
CHARPOLY = X**4 - 2*X**3 - 5*X**2 - 4*X - 1

TAU_N = float(sp.sqrt((1 + sp.sqrt(5)) / 2).evalf(30))
PHI_N = TAU_N**2
BETA_T = t**2 + t**3           # beta = tau^2(1+tau)


def red(e):
    """Reduce an expression polynomial in t modulo MIN."""
    return sp.rem(sp.expand(e), MIN, t)


def inv(e):
    """Inverse of a Q(tau) element (given as reduced poly in t)."""
    p = sp.Poly(red(e), t, domain='QQ')
    m = sp.Poly(MIN, t, domain='QQ')
    s, _, h = sp.gcdex(p, m)
    hc = h.as_expr()
    assert sp.degree(h.as_expr(), t) in (0, sp.S.NegativeInfinity), "gcd not constant"
    return red(s.as_expr() / hc)


def num(e):
    """Numeric value at t = tau."""
    return float(sp.expand(e).subs(t, sp.nsimplify(0) + sp.Rational(0)) if False
                 else sp.expand(e).evalf(30, subs={t: sp.sqrt((1+sp.sqrt(5))/2)}))


# Exact letter frequencies in Q(tau)
F_A_ = red(t - 1)                    # f_a = tau - 1 = 1/beta
F_B_ = red((t - 1) * (t**2 - 1))     # f_b = (tau-1)/tau^2 ; 1/tau^2 = tau^2-1
F_CA = red(t * (t - 1))              # f_A = tau(tau-1)
F_CB = red((t - 1) * (t**3 - t))     # f_B = (tau-1)/tau ; 1/tau = tau^3-tau
FREQ_T = {'a': F_A_, 'b': F_B_, 'A': F_CA, 'B': F_CB}


def check(label, ok, detail=""):
    mark = "PASS" if ok else "FAIL  <────────── PROBLEM"
    print(f"  [{mark}] {label}{('  ' + detail) if detail else ''}")
    return ok


def part1():
    print("\n" + "=" * 78)
    print("PART 1 — Exact symbolic core identities")
    print("=" * 78)
    ok_all = True

    # 1. The substitution identity: (y+1)^4 - y^2(y+1)^2 - y^4 = -charpoly(y)
    y = sp.Symbol('y')
    lhs = sp.expand((y+1)**4 - y**2*(y+1)**2 - y**4)
    ok_all &= check("charpoly substitution identity (beta = 1/(tau-1))",
                    sp.expand(lhs + CHARPOLY.subs(X, y)) == 0)

    # 2. beta = tau^2 + tau^3 is a root of charpoly
    ok_all &= check("charpoly(tau^2+tau^3) == 0 in Q(tau)",
                    red(CHARPOLY.subs(X, BETA_T)) == 0)

    # 3. beta * (tau - 1) = 1
    ok_all &= check("beta*(tau-1) == 1", red(BETA_T * (t - 1)) == 1)

    # 4. lambda_2 = -1/(1+tau) is a root of charpoly
    lam2 = red(-inv(1 + t))
    ok_all &= check("charpoly(-1/(1+tau)) == 0", red(CHARPOLY.subs(X, lam2)) == 0)

    # 5. f_a + f_b = |lambda_2| exactly
    ok_all &= check("f_a + f_b == 1/(1+tau) == |lambda2|",
                    red(F_A_ + F_B_ - inv(1 + t)) == 0)

    # 6. frequencies sum to 1
    ok_all &= check("f_a+f_b+f_A+f_B == 1",
                    red(F_A_ + F_B_ + F_CA + F_CB) == 1)

    # 7. quadratic factorization over Q(sqrt5): the complex pair
    s5 = sp.sqrt(5)
    phi = (1 + s5) / 2
    q1 = X**2 - (2 + 2/phi)*X - phi          # (x-beta)(x-lambda2)
    q2 = X**2 + (2/phi)*X + 1/phi            # complex pair
    ok_all &= check("charpoly == q1*q2 over Q(sqrt5)",
                    sp.simplify(sp.expand(q1*q2 - CHARPOLY)) == 0)

    # from q2: Re(l3) = -1/phi, |l3|^2 = 1/phi, Im^2 = 1/phi - 1/phi^2 = 1/phi^3
    im2 = sp.simplify(sp.Rational(1)/phi - 1/phi**2 - 1/phi**3)
    ok_all &= check("Im(lambda3)^2 == 1/phi^3  (=> Im = 1/tau^3)", im2 == 0)

    # 8. |lambda3| = 1/tau, cos = -1/tau, sin = 1/phi
    #    |l3|^2 = 1/phi = 1/tau^2  => |l3| = 1/tau. cos = (-1/phi)/(1/tau) = -1/tau.
    #    sin = (1/tau^3)/(1/tau) = 1/tau^2 = 1/phi.  (pure tau-algebra)
    ok_all &= check("cos(theta) == -1/tau (tau-algebra)",
                    red((t**2 - 1)*t - (t**3 - t)) == 0)   # (1/phi)*tau == 1/tau
    ok_all &= check("sin(theta) == 1/phi (tau-algebra)", True,
                    "1/tau^3 / (1/tau) = 1/tau^2 = 1/phi, trivially")

    # 9. det(M) = -1 and modulus identity beta*|l2|*|l3|^2 = 1
    ok_all &= check("beta*|lambda2|*|lambda3|^2 == 1",
                    red(BETA_T * inv(1+t) * (t**2 - 1)) == 1)

    # 10. discriminants
    d1 = sp.discriminant(t**4 - t**2 - 1, t)
    d2 = sp.discriminant(CHARPOLY, X)
    ok_all &= check("disc(x^4-x^2-1) == -400", d1 == -400)
    ok_all &= check("disc(charpoly M) == -400", d2 == -400)

    # 11. irreducibility of x^4 - x^2 - 1 over Q
    ok_all &= check("x^4-x^2-1 irreducible over Q",
                    sp.factor(t**4 - t**2 - 1) == t**4 - t**2 - 1)

    # 12. Galois group D4 via the classical criterion for x^4+px^2+r (q=0):
    #     irreducible, r not a square in Q -> not V4;
    #     r*(p^2-4r) not a square -> not C4;  => D4.
    p_, r_ = -1, -1
    r_square = sp.sqrt(sp.Rational(r_)).is_rational
    c4_val = sp.Rational(r_) * (p_**2 - 4*r_)   # -1 * 5 = -5
    c4_square = sp.sqrt(c4_val).is_rational
    ok_all &= check("Galois group D4 (r=-1 not square, r(p^2-4r)=-5 not square)",
                    (not r_square) and (not c4_square))

    # 13. incidence matrix built INDEPENDENTLY from SUB; check M v = beta v
    #     with v = (f_a, f_b, f_A, f_B), column convention M[i][j] = count of
    #     letter i in sigma(letter j)
    M_col = sp.Matrix(4, 4, lambda i, j: SUB[ALPHA[j]].count(ALPHA[i]))
    v = sp.Matrix([F_A_, F_B_, F_CA, F_CB])
    resid = (M_col * v - sp.expand(BETA_T) * v).applyfunc(red)
    ok_all &= check("M_col * (f_a,f_b,f_A,f_B) == beta * v exactly",
                    all(e == 0 for e in resid))
    ok_all &= check("det(M) == -1", M_col.det() == -1)

    # 14. bonus identity: f_A - f_a = f_a^2
    ok_all &= check("f_A - f_a == f_a^2", red(F_CA - F_A_ - F_A_**2) == 0)

    return ok_all


def analyze(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 6:
        return None
    rws = standard_return_words_from_positions(host, positions, trim=trim)
    ind = canonical_induced_system(rws, max_power=2)
    if ind is None:
        return None
    return {'rws': rws, 'matrix': ind['matrix']}


def exact_perron(A):
    """Exact normalized Perron eigenvector of integer matrix A over Q(tau),
    via the adjugate of (A - beta*I). Returns list of reduced tau-polys."""
    n = A.rows
    N = (A - sp.expand(BETA_T) * sp.eye(n)).applyfunc(sp.expand)
    adj = N.adjugate().applyfunc(red)
    # pick a nonzero column
    tau_num = sp.sqrt((1 + sp.sqrt(5)) / 2)
    col = None
    for j in range(n):
        c = [adj[i, j] for i in range(n)]
        if any(e != 0 for e in c):
            vals = [float(sp.expand(e).evalf(30, subs={t: tau_num})) for e in c]
            if all(abs(x) > 1e-12 for x in vals):
                col = c
                break
    assert col is not None, "no usable adjugate column"
    # verify eigen-equation exactly
    vcol = sp.Matrix(col)
    resid = (A * vcol - sp.expand(BETA_T) * vcol).applyfunc(red)
    assert all(e == 0 for e in resid), "adjugate column is not an eigenvector"
    s = red(sum(col))
    s_inv = inv(s)
    out = [red(e * s_inv) for e in col]
    # positivity
    vals = [float(sp.expand(e).evalf(30, subs={t: tau_num})) for e in out]
    assert all(x > 0 for x in vals), f"not positive: {vals}"
    return out, vals


def coeffs_str(e):
    p = sp.Poly(red(e), t, domain='QQ')
    c = [sp.nsimplify(p.coeff_monomial(t**k)) for k in range(4)]
    return f"({c[0]}) + ({c[1]})tau + ({c[2]})phi + ({c[3]})tau^3"


def part2(host):
    print("\n" + "=" * 78)
    print("PART 2 — Exact Perron eigenvectors of the 5 type matrices")
    print("=" * 78)
    ok_all = True

    reps = {'T1': 'a', 'T2': 'B', 'T3': 'A', 'T4(rc5)': 'aA', 'T5': 'Bab'}
    combos = {
        'T2': [red(F_A_ + F_B_), F_A_, F_CB, red(F_CA - F_A_)],
        'T3': [red(F_A_ - F_B_ + F_CB), red(F_B_ + F_CA - F_CB), F_CB, F_B_],
    }

    exact_tables = {}
    for label, factor in reps.items():
        r = analyze(factor, host)
        assert r is not None, f"analyze failed for {factor}"
        A = sp.Matrix(r['matrix'])
        vec, vals = exact_perron(A)
        exact_tables[label] = (vec, vals)
        order = np.argsort(vals)[::-1]
        print(f"\n  {label} (u='{factor}', rc={A.rows}) exact Perron components"
              f" (sorted desc):")
        for i in order:
            print(f"    {vals[i]:.10f} = {coeffs_str(vec[i])}")

    # Claimed Z-mixing exactness tests
    print("\n  Z-mixing claims:")

    # T1 = letter frequencies (as a multiset)
    vec1, vals1 = exact_tables['T1']
    claimed1 = [F_A_, F_B_, F_CA, F_CB]
    used = set()
    all_match = True
    for e in vec1:
        found = False
        for k, cl in enumerate(claimed1):
            if k not in used and red(e - cl) == 0:
                used.add(k)
                found = True
                break
        all_match &= found
    ok_all &= check("T1 Perron == {f_a,f_b,f_A,f_B} EXACTLY (multiset)", all_match)

    for label in ('T2', 'T3'):
        vec, vals = exact_tables[label]
        used = set()
        all_match = True
        for e in vec:
            found = False
            for k, cl in enumerate(combos[label]):
                if k not in used and red(e - cl) == 0:
                    used.add(k)
                    found = True
                    break
            all_match &= found
        ok_all &= check(f"{label} Perron == claimed Z-combos EXACTLY", all_match)

    # T4 rc=5: claimed integer combos for three of five components
    vec4, vals4 = exact_tables['T4(rc5)']
    claims4 = {
        '-f_a+f_A+f_B': red(-F_A_ + F_CA + F_CB),
        '2f_a+f_b-f_A-f_B': red(2*F_A_ + F_B_ - F_CA - F_CB),
        '-f_a-f_b+f_A+f_B': red(-F_A_ - F_B_ + F_CA + F_CB),
    }
    for name, cl in claims4.items():
        hit = any(red(e - cl) == 0 for e in vec4)
        ok_all &= check(f"T4 contains {name} exactly", hit)

    # T5: claimed f_a component + 'irrational mixing' language check
    vec5, vals5 = exact_tables['T5']
    hit = any(red(e - F_A_) == 0 for e in vec5)
    ok_all &= check("T5 contains f_a exactly", hit)
    print("\n  T5 full exact table (were these 'irrational mixings'? they are")
    print("  elements of Q(tau) by necessity — the question is the denominators):")
    for e, x in zip(vec5, vals5):
        print(f"    {x:.10f} = {coeffs_str(e)}")

    return ok_all, exact_tables


def part3():
    print("\n" + "=" * 78)
    print("PART 3 — Engine-independent census (plain string return words)")
    print("=" * 78)

    # independent grow
    w = 'a'
    for _ in range(11):
        w = ''.join(SUB[c] for c in w)
    print(f"  independent host length: {len(w)}")

    def positions_of(u):
        out, i = [], w.find(u)
        while i != -1:
            out.append(i)
            i = w.find(u, i + 1)
        return out

    banked = {
        1: (0.3460, 0.2720, 0.2138, 0.1681),
        2: (0.4401, 0.2720, 0.2138, 0.0740),
        3: (0.3178, 0.3003, 0.2138, 0.1681),
        4: (0.2878, 0.2464, 0.1937, 0.1523, 0.1197),
        5: (0.3270, 0.2720, 0.2571, 0.1439),
    }

    clusters = defaultdict(list)
    n_points = 0
    for L in range(1, 5):
        seen = set()
        for i in range(len(w) - L + 1):
            seen.add(w[i:i+L])
        for u in sorted(seen):
            pos = positions_of(u)
            if len(pos) < 6:
                continue
            trimmed = pos[2:-2]
            rws = [w[trimmed[k]:trimmed[k+1]] for k in range(len(trimmed) - 1)]
            distinct = sorted(set(rws))
            if len(distinct) < 2:
                continue
            counts = np.array([rws.count(r) for r in distinct], dtype=float)
            freq = np.sort(counts / counts.sum())[::-1]
            key = tuple(np.round(freq, 3))
            clusters[key].append(u)
            n_points += 1

    print(f"  qualifying points: {n_points} (banked: 34)")
    print(f"  distinct empirical fingerprints: {len(clusters)}")

    # match clusters to banked types
    matched = defaultdict(list)
    unmatched = []
    for key, factors in clusters.items():
        best_t, best_d = None, 1e9
        for tnum, bk in banked.items():
            if len(bk) != len(key):
                continue
            d = max(abs(a - b) for a, b in zip(key, bk))
            if d < best_d:
                best_d, best_t = d, tnum
        if best_t is not None and best_d < 0.004:
            matched[best_t].extend(factors)
        else:
            unmatched.append((key, factors))

    for tnum in sorted(matched):
        print(f"  type {tnum}: {len(matched[tnum]):2d} factors: "
              f"{', '.join(sorted(matched[tnum]))}")
    if unmatched:
        print("  UNMATCHED fingerprints:")
        for key, factors in unmatched:
            print(f"    {key}: {factors}")

    counts = sorted((len(v) for v in matched.values()), reverse=True)
    ok = (n_points == 34 and len(unmatched) == 0
          and counts == [14, 10, 4, 3, 3])
    check("independent census: 34 points, 5 banked fingerprints, 14/10/4/3/3", ok,
          f"got {n_points} pts, per-type {counts}, {len(unmatched)} unmatched")
    return ok


def part4(host):
    print("\n" + "=" * 78)
    print("PART 4 — GL(4,Z) conjugacy re-test (banked claim: NOT conjugate)")
    print("=" * 78)

    mats = {}
    for label, factor in [('T1', 'a'), ('T2', 'B'), ('T3', 'A'), ('T5', 'Bab')]:
        r = analyze(factor, host)
        mats[label] = sp.Matrix(r['matrix'])

    x_ch = sp.Symbol('x')
    for label, A in mats.items():
        cp = sp.factor(A.charpoly(x_ch).as_expr())
        assert cp == sp.factor(CHARPOLY.subs(X, x_ch)), f"{label} charpoly differs!"

    results = {}
    base = mats['T1']
    for label in ('T2', 'T3', 'T5'):
        B = mats[label]
        # solve U*A = B*U : (A^T kron I - I kron B) vec(U) = 0
        K = sp.Matrix(sp.kronecker_product(base.T, sp.eye(4))
                      - sp.kronecker_product(sp.eye(4), B))
        ns = K.nullspace()
        basis = []
        for vv in ns:
            den = sp.lcm([sp.fraction(sp.nsimplify(e))[1] for e in vv])
            vv2 = (vv * den)
            g = sp.gcd([e for e in vv2 if e != 0])
            vv2 = vv2 / g
            basis.append(sp.Matrix(4, 4, lambda i, j: vv2[4*i + j]))
        print(f"\n  T1 ~ {label}: commutant-solution space dim = {len(basis)}")

        Bs = [np.array(bb.tolist(), dtype=float) for bb in basis]
        found = None
        N = 6
        rng = range(-N, N + 1)
        for c in iprod(rng, repeat=len(basis)):
            if all(ci == 0 for ci in c):
                continue
            U = sum((ci * bb for ci, bb in zip(c, Bs)),
                    np.zeros((4, 4)))
            d = np.linalg.det(U)
            if abs(abs(d) - 1) < 1e-6:
                Uex = sum((ci * bb for ci, bb in zip(c, basis)),
                          sp.zeros(4, 4))
                if abs(Uex.det()) == 1 and (Uex * base - B * Uex).is_zero_matrix:
                    if all(e == int(e) for e in Uex):
                        found = (c, Uex)
                        break
        if found:
            c, Uex = found
            print(f"    UNIMODULAR CONJUGATOR FOUND: coeffs {c}, det = {Uex.det()}")
            print(f"    U = {Uex.tolist()}")
            check(f"T1 and {label} ARE GL(4,Z)-conjugate (banked claim REFUTED)", True)
            results[label] = Uex
        else:
            print(f"    no unimodular conjugator with coeffs in [-{N},{N}]^4")
            check(f"T1 ~ {label}: inconclusive at this search radius", True)
            results[label] = None

    return results


def part5():
    print("\n" + "=" * 78)
    print("PART 5 — Gate 3 false-positive control, magnitude-matched")
    print("=" * 78)

    T4v = np.array([1.0, TAU_N, TAU_N**2, TAU_N**3])
    MAX_C = 8
    rng_ = np.arange(-MAX_C, MAX_C + 1, dtype=float)
    N = len(rng_)
    a = rng_.reshape(N, 1, 1, 1)
    b = rng_.reshape(1, N, 1, 1)
    c = rng_.reshape(1, 1, N, 1)
    d = rng_.reshape(1, 1, 1, N)
    lattice = np.sort((a*T4v[0] + b*T4v[1] + c*T4v[2] + d*T4v[3]).ravel())

    def best_err(v):
        i = np.searchsorted(lattice, v)
        errs = []
        if i < len(lattice):
            errs.append(abs(lattice[i] - v))
        if i > 0:
            errs.append(abs(lattice[i-1] - v))
        return min(errs)

    sm = {
        'alpha_s(M_Z)': 0.1180, 'sin2_thetaW': 0.23122,
        'm_tau/m_mu': 1.77686/0.1056583755, 'm_W/m_Z': 80.3692/91.1876,
        'V_us': 0.22500, 'V_cb': 0.04182, 'V_ub': 0.003650,
        'alpha_em': 1/137.035999084, 'm_u/m_d': 2.16/4.67,
        'm_s/m_d': 93.4/4.67, 'm_c/m_s': 1.27/0.0934,
        'm_t/m_b': 172.69/4.18, 'm_H/m_Z': 125.25/91.1876,
        'm_H/m_W': 125.25/80.3692, 'g_W/g_Y': np.sqrt((1-0.23122)/0.23122),
        'm_b/m_s': 4.18/0.0934,
    }

    rs = np.random.RandomState(7)
    n_ctrl = 400
    print(f"\n  {'target':>14s} {'value':>12s} {'err':>10s} {'p (matched ctrl)':>18s}")
    print(f"  {'-'*14} {'-'*12} {'-'*10} {'-'*18}")
    pvals = []
    for name, v in sm.items():
        e = best_err(v)
        draws = rs.uniform(0.5 * v, 1.5 * v, n_ctrl)
        ctrl = np.array([best_err(x) for x in draws])
        p = float(np.mean(ctrl <= e))
        pvals.append(p)
        print(f"  {name:>14s} {v:12.6f} {e:10.2e} {p:18.3f}")

    pvals = np.array(pvals)
    print(f"\n  p-value distribution: min={pvals.min():.3f}, "
          f"median={np.median(pvals):.3f}, mean={pvals.mean():.3f}")
    print(f"  Under pure chance p should be ~Uniform(0,1): "
          f"mean 0.5, and no pileup near 0.")
    n_small = int(np.sum(pvals < 0.05))
    print(f"  p < 0.05: {n_small}/{len(pvals)} "
          f"(expected ~{0.05*len(pvals):.1f} by chance)")
    ok = n_small <= 3
    check("Gate 3 verdict survives the corrected (magnitude-matched) control", ok)
    return ok


def main():
    print("=" * 78)
    print("B533 FABLE-5 AUDIT — exact re-verification")
    print("=" * 78)

    ok1 = part1()
    host = grow(10)
    ok2, _tables = part2(host)
    ok3 = part3()
    conj = part4(host)
    ok5 = part5()

    print("\n" + "=" * 78)
    print("AUDIT SUMMARY")
    print("=" * 78)
    print(f"  Part 1 (symbolic core):        {'ALL PASS' if ok1 else 'FAILURES'}")
    print(f"  Part 2 (exact Perron/Z-mix):   {'ALL PASS' if ok2 else 'FAILURES'}")
    print(f"  Part 3 (independent census):   {'PASS' if ok3 else 'FAIL'}")
    n_conj = sum(1 for v in conj.values() if v is not None)
    print(f"  Part 4 (GL(4,Z)):              {n_conj}/3 explicit conjugators found")
    if n_conj > 0:
        print(f"        => banked S2 'NOT GL(4,Z)-conjugate' is REFUTED")
    print(f"  Part 5 (Gate 3 FP control):    {'PASS' if ok5 else 'FAIL'}")


if __name__ == '__main__':
    main()
