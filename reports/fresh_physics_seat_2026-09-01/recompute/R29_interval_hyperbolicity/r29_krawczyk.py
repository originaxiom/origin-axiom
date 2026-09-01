#!/usr/bin/env python3
"""R29 — interval (Krawczyk) verification of the complete hyperbolic structure on the 112-member
Q(sqrt-3) family (R23 `sweep_candidates.json`) and the seven R24 members, WITHOUT Sage.

SnapPy's own `verify_hyperbolicity()` needs Sage (not installed here: SageNotAvailable).  This is an
independent implementation of the same certificate on mpmath interval arithmetic:

  * gluing equations from `Manifold.gluing_equations('rect')`: rows (a, b, c) meaning
    prod_i z_i^{a_i} (1-z_i)^{b_i} = c, c in {+1,-1}; rows = n edge equations, then per cusp a
    meridian and a longitude row (complete structure <=> all cusp rows hold).
  * log form  F_j(z) = sum_i a_ji log z_i + b_ji log(1-z_i) - log c_j - 2 pi i k_j, with the integer
    branch k_j read off the 212-bit numerical solution.  Any zero of the log form is a solution of the
    multiplicative equations, whatever k is.
  * a square full-rank subsystem (n rows, edge rows first, then meridians) is verified by the
    Krawczyk operator K(X) = z0 - Y F(z0) + (I - Y J(X))(X - z0) on a box X around z0:
    K(X) strictly inside X  =>  exactly one zero of the subsystem in X.
  * every remaining row is an integer/rational combination of the retained rows, so at the zero it
    holds up to a root of unity of order D (D = lcm of the denominators of that rational dependency);
    the interval evaluation of its log form on K(X) containing 0 with diameter < 2 pi / D pins it to
    exact equality.
  * Im z_i > 0 on the whole box  =>  positively oriented ideal triangulation  =>  the zero is the
    complete hyperbolic structure (Neumann–Zagier / Moser).

What this does NOT certify: Chern–Simons values, symmetry groups, isometry signatures (those need
verified canonical retriangulation, i.e. Sage).  Output: r29_results.json + r29_run.txt.
"""
import json, os, sys, time, warnings
warnings.filterwarnings('ignore')
import snappy
import mpmath as mp
from mpmath import iv
from fractions import Fraction
import sympy as sp

PREC = 300           # bits for mp and iv
RADIUS = mp.mpf('1e-40')
mp.mp.prec = PREC
iv.prec = PREC

def hi(q):
    """upper endpoint of an mpmath interval as a plain mpf (iv endpoints come back as point intervals)"""
    return mp.make_mpf(q._mpi_[1])

def civ(z):
    """point complex interval"""
    return iv.mpc(iv.mpf(mp.re(z)), iv.mpf(mp.im(z)))

def box(z0, r):
    return [iv.mpc(iv.mpf([mp.re(z) - r, mp.re(z) + r]), iv.mpf([mp.im(z) - r, mp.im(z) + r])) for z in z0]

def logform_rows(M):
    eq = M.gluing_equations('rect')
    rows = []
    for a, b, c in eq:
        rows.append(([int(x) for x in a], [int(x) for x in b], int(c)))
    return rows

def F_iv(row, Z, k):
    a, b, c = row
    s = iv.mpc(0, 0)
    for ai, bi, z in zip(a, b, Z):
        if ai: s += ai * iv.log(z)
        if bi: s += bi * iv.log(1 - z)
    s -= iv.log(iv.mpc(c, 0)) if c > 0 else iv.mpc(0, iv.pi)   # log(-1) = i pi
    s -= iv.mpc(0, 2 * iv.pi * k)
    return s

def F_num(row, z, k):
    a, b, c = row
    s = mp.mpc(0)
    for ai, bi, zi in zip(a, b, z):
        if ai: s += ai * mp.log(zi)
        if bi: s += bi * mp.log(1 - zi)
    s -= mp.log(mp.mpc(c))
    s -= mp.mpc(0, 2 * mp.pi * k)
    return s

def J_iv(row, Z):
    a, b, c = row
    return [ (ai / z if ai else iv.mpc(0, 0)) - (bi / (1 - z) if bi else iv.mpc(0, 0)) for ai, bi, z in zip(a, b, Z) ]

def J_num(row, z):
    a, b, c = row
    return [ (ai / zi if ai else 0) - (bi / (1 - zi) if bi else 0) for ai, bi, zi in zip(a, b, z) ]

def contained_strict(K, X):
    for k, x in zip(K, X):
        if not (k.real.a > x.real.a and k.real.b < x.real.b and k.imag.a > x.imag.a and k.imag.b < x.imag.b):
            return False
    return True

def verify(name):
    t0 = time.time()
    M = snappy.Manifold(name)
    n = M.num_tetrahedra(); nc = M.num_cusps()
    H = M.high_precision()
    # snappy's Number str() can carry a space before the exponent ('-1.8058... e-62'): strip it
    z0 = [mp.mpc(str(s.real()).replace(' ', ''), str(s.imag()).replace(' ', '')) for s in H.tetrahedra_shapes('rect')]
    rows = logform_rows(M)
    n_edge = len(rows) - 2 * nc
    # branch integers from the numeric solution (rows must be ~0 mod 2 pi i)
    ks = []
    for r in rows:
        v = F_num(r, z0, 0)
        k = int(mp.nint(mp.im(v) / (2 * mp.pi)))
        ks.append(k)
        res = abs(F_num(r, z0, k))
        if res > mp.mpf('1e-50'):
            return dict(name=name, verified=False, reason='numeric residual %.2e on row' % float(res), n_tet=n, n_cusps=nc)
    # choose n independent rows: edge rows first, then meridians (index n_edge + 2*i), then longitudes
    chosen, Jn = [], []
    for j in range(n_edge):
        Q = sp.Matrix([[sp.Rational(x) for x in rows[i][0] + rows[i][1]] for i in chosen + [j]])
        if Q.rank() == len(chosen) + 1:
            chosen.append(j); Jn.append(J_num(rows[j], z0))
        if len(chosen) == n - nc: break
    for i in range(nc):
        j = n_edge + 2 * i; chosen.append(j); Jn.append(J_num(rows[j], z0))
    Qall = sp.Matrix([[sp.Rational(x) for x in rows[i][0] + rows[i][1]] for i in chosen])
    if Qall.rank() != n:
        return dict(name=name, verified=False, reason='edge+meridian rows have rank %d != %d' % (Qall.rank(), n), n_tet=n, n_cusps=nc)
    if len(chosen) < n:
        return dict(name=name, verified=False, reason='could not find %d independent rows' % n, n_tet=n, n_cusps=nc)
    Jm = mp.matrix(Jn)
    Y = mp.inverse(Jm)
    X = box(z0, RADIUS)
    Z0 = [civ(z) for z in z0]
    # F(z0) in interval, J(X) in interval
    Fz0 = [F_iv(rows[j], Z0, ks[j]) for j in chosen]
    JX = [J_iv(rows[j], X) for j in chosen]
    Yiv = [[civ(Y[i, j]) for j in range(n)] for i in range(n)]
    K = []
    for i in range(n):
        s = Z0[i]
        for j in range(n): s -= Yiv[i][j] * Fz0[j]
        for j in range(n):
            coeff = (iv.mpc(1, 0) if i == j else iv.mpc(0, 0))
            for l in range(n): coeff -= Yiv[i][l] * JX[l][j]
            s += coeff * (X[j] - Z0[j])
        K.append(s)
    ok_k = contained_strict(K, X)
    if not ok_k:
        return dict(name=name, verified=False, reason='Krawczyk not contractive at radius %s' % str(RADIUS), n_tet=n, n_cusps=nc)
    # positivity of Im on the box
    ok_pos = all(x.imag.a > 0 for x in X)
    # remaining EDGE rows are Q-combinations (a|b)_d = sum_j q_j (a|b)_j of the retained rows
    # (Neumann-Zagier: edge rows have rank n - c over the 2n columns), so at the verified zero
    #   F_d = sum_j q_j (log c_j + 2 pi i k_j) - (log c_d + 2 pi i k_d)      -- an EXACT multiple of pi i.
    # The multiplicative edge equation d holds iff that number is in 2 pi i Z.  We compute it exactly and
    # also evaluate F_d on the Krawczyk box as a cross-check (must contain 0, diameter < 2 pi / D).
    # Longitude rows are not linear consequences but geometric ones: with the meridian holonomy a
    # translation of the cusp torus, any similarity commuting with it is a translation, so the
    # longitude equation follows; we still evaluate them on the box as a cross-check (contain 0).
    remaining = [j for j in range(len(rows)) if j not in chosen]
    Qc = sp.Matrix([[sp.Rational(x) for x in rows[i][0] + rows[i][1]] for i in chosen]).T   # (2n) x n
    def logc(j):  # (log c_j + 2 pi i k_j) / (pi i) as an exact rational
        return sp.Rational(2 * ks[j] + (1 if rows[j][2] < 0 else 0))
    rem_ok, rem_info = True, []
    for j in remaining:
        v = sp.Matrix([sp.Rational(x) for x in rows[j][0] + rows[j][1]])
        is_edge = j < n_edge
        val = F_iv(rows[j], K, ks[j])
        diam = max(hi(val.real.delta), hi(val.imag.delta))   # plain mpf upper bound on the diameter
        has0 = val.real.a <= 0 <= val.real.b and val.imag.a <= 0 <= val.imag.b
        if is_edge:
            sol, params = Qc.gauss_jordan_solve(v)
            if params.shape[0]:
                sol = sol.subs({pp: 0 for pp in params})
            exact = sum(q * logc(i) for q, i in zip(sol, chosen)) - logc(j)   # F_d / (pi i), exact rational
            D = 1
            for e in sol: D = sp.ilcm(D, sp.fraction(e)[1])
            good = (exact % 2 == 0) and has0 and diam < 2 * mp.pi / int(D)
            rem_info.append(dict(row=j, kind='edge', D=int(D), exact_F_over_pi_i=str(exact), contains_zero=bool(has0), diam=float(diam)))
        else:
            good = has0
            rem_info.append(dict(row=j, kind='longitude' if (j - n_edge) % 2 else 'meridian', contains_zero=bool(has0), diam=float(diam)))
        rem_ok &= bool(good)
    verified = bool(ok_k and ok_pos and rem_ok)
    return dict(name=name, verified=verified, n_tet=n, n_cusps=nc, rows=len(rows), chosen=chosen,
                branch_k=ks, krawczyk_contractive=bool(ok_k), im_positive=bool(ok_pos), remaining_rows_ok=bool(rem_ok),
                remaining=rem_info, radius=str(RADIUS), prec_bits=PREC, seconds=round(time.time() - t0, 2),
                shape0=str(mp.nstr(z0[0], 30)))

if __name__ == '__main__':
    names = sys.argv[1:]
    if not names:
        cands = json.load(open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/../R23_carriers_quine/sweep_candidates.json'))['candidates']
        extra = ['s118', 'o10_150700', 't12840', 's955', 'm015', 'm016']
        names = cands + [e for e in extra if e not in cands]
    out = []
    for nm in names:
        try:
            r = verify(nm)
        except Exception as e:
            r = dict(name=nm, verified=False, reason='EXC %s: %s' % (type(e).__name__, str(e)[:200]))
        out.append(r)
        print(('%-12s verified=%s  tets=%s cusps=%s  %s' % (nm, r.get('verified'), r.get('n_tet'), r.get('n_cusps'),
               r.get('reason', '') or ('K=%s Im>0=%s rest=%s t=%ss' % (r.get('krawczyk_contractive'), r.get('im_positive'), r.get('remaining_rows_ok'), r.get('seconds'))))), flush=True)
    json.dump(out, open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/r29_results.json', 'w'), indent=1)
    nv = sum(1 for r in out if r.get('verified'))
    print('== verified %d / %d ==' % (nv, len(out)))
