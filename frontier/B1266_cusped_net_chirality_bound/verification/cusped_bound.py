#!/usr/bin/env python3
"""B1266, the exact stage: the net-chirality lemma and its bound, instantiated on the cusped object.

THE LEMMA.  For M = m004 (torus boundary, chi(M) = 0) and a representation V of pi_1(M) with
h0(M;V) = h0(M;V*) = 0 -- or, more generally, whenever the H^0 terms are accounted for below --
Poincare-Lefschetz duality on the pair (M, dM) gives
        N(V) := h1(M;V) - h1(M;V*) = rank(res_V) - h0(dM;V),
where res_V: H1(M;V) -> H1(dM;V) is the restriction (the proof is in
docs/EXTERNAL_VERIFICATION_2026-09-06.md section 3; here it is CHECKED, not cited, on every row).
The images of res_V and res_V* are mutual annihilators under the cup pairing, so
        rank(res_V) + rank(res_V*) = h1(dM;V) = h0(dM;V) + h0(dM;V*),
and therefore
        -h0(dM;V)  <=  N(V)  <=  h0(dM;V*).                                      (THE BOUND)
Near the geometric point, h1(M;27_s) <= h1(M;27_0) = 3 by upper semicontinuity, so for every small
deformation rho_s of the geometric E6 holonomy (theta-odd or not)
        N(27_s) <= min(3 - h0(dM;27_s), h0(dM;27bar_s))  <=  1.

THIS SCRIPT (exact over Q(omega), no floats): the lemma's ingredients on the geometric point for the
27 AND the 27bar (h1, h0(dM), h1(dM), rank(res), N), on the abelian sector at the Alexander root
phi^2 and at a non-root (B1260's wall, seen through the lemma), and the existence of the theta-odd
deformation class (h1(M; V8) = 1) that the high-precision stage (cusped_theta_odd_hp.py) follows.
"""
from __future__ import annotations
import os, sys
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1265_spectrum_law_rebuilt', 'verification'))
import e6_instrument as E
import spectrum_law as S

Qw, ONE, ZERO, OMEGA = E.Qw, E.ONE, E.ZERO, E.OMEGA
REL, LONG = S.REL, S.LONG


def nullspace_qw(M):
    """Exact right nullspace basis of a Qw matrix (list of column vectors, as python lists)."""
    A = [[M[i, j] for j in range(M.shape[1])] for i in range(M.shape[0])]
    n, m = len(A), (len(A[0]) if A else 0)
    r, pivcols = 0, []
    for c in range(m):
        piv = next((i for i in range(r, n) if not A[i][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                fct = A[i][c]
                A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        pivcols.append(c)
        r += 1
        if r == n:
            break
    free = [c for c in range(m) if c not in pivcols]
    out = []
    for fc in free:
        v = [ZERO] * m
        v[fc] = ONE
        for i, pc in enumerate(pivcols):
            v[pc] = -A[i][fc]
        out.append(v)
    return out


def cocycle_value(rep, word, fa, fb):
    n = rep.n
    val = np.array([[ZERO] for _ in range(n)], dtype=object)
    cur = E.qw_eye(n)
    fd = {1: fa, 2: fb}
    for L in word:
        if L > 0:
            val = val + cur.dot(fd[L])
            cur = cur.dot(rep.M[L])
        else:
            cur = cur.dot(rep.I[-L])
            val = val - cur.dot(fd[-L])
    return val


def lemma_row(rep, label, quiet=False):
    """All the lemma's ingredients for a representation of pi_1(m004) (exact)."""
    n = rep.n
    I = E.qw_eye(n)
    h0, h1, r0, r1 = S.h0_h1(rep, [1, 2], [REL])
    mu, lam = rep.M[1], rep.ev(LONG)
    assert E.qw_is_zero(mu.dot(lam) - lam.dot(mu))
    h0t = n - E.rank_qw(np.vstack([mu - I, lam - I]))
    rZ = E.rank_qw(np.hstack([lam - I, -(mu - I)]))
    Bt = np.vstack([mu - I, lam - I])
    rB = E.rank_qw(Bt)
    h1t = (2 * n - rZ) - rB
    d1 = np.hstack([rep.fox(REL, 1), rep.fox(REL, 2)])
    kern = nullspace_qw(d1)
    cols = []
    for v in kern:
        fa = np.array([[x] for x in v[:n]], dtype=object)
        fb = np.array([[x] for x in v[n:]], dtype=object)
        val = np.vstack([cocycle_value(rep, [1], fa, fb), cocycle_value(rep, LONG, fa, fb)])
        cols.append([val[i, 0] for i in range(2 * n)])
    R = np.array(cols, dtype=object).T if cols else np.empty((2 * n, 0), dtype=object)
    rank_res = E.rank_qw(np.hstack([R, Bt])) - rB
    N = rank_res - h0t
    if not quiet:
        print(f"  {label}: h0(M) = {h0}, h1(M) = {h1}, h0(dM) = {h0t}, h1(dM) = {h1t}, rank(res) = {rank_res}  =>  "
              f"lemma value rank(res) - h0(dM) = {N}")
    return dict(h0=h0, h1=h1, h0t=h0t, h1t=h1t, rank_res=rank_res, N=N)


def character_rep(val):
    mats = {1: np.array([[val]], dtype=object), 2: np.array([[val]], dtype=object)}
    invs = {1: np.array([[val.inv()]], dtype=object), 2: np.array([[val.inv()]], dtype=object)}
    return S.Rep(mats, invs)


def main():
    ok = True
    print("=== the geometric point: the principal 27 and its dual ===")
    e, h, f = E.principal_sl2()
    rep = S.build_rep(e, f)
    S.check_rep(rep, [1, 2], [REL])
    a = lemma_row(rep, "27   ")
    b = lemma_row(rep.dualrep(), "27bar")
    Nab = a['h1'] - b['h1']
    print(f"  N = h1(27) - h1(27bar) = {Nab};  lemma predicts {a['N']} (27) and {b['N']} (27bar); "
          f"complementarity rank(res_27) + rank(res_27bar) = {a['rank_res'] + b['rank_res']} vs h1(dM;27) = {a['h1t']}")
    ok &= (Nab == a['N'] == -b['N'] == 0) and (a['rank_res'] + b['rank_res'] == a['h1t'])
    ok &= (a['h1'], a['h0t'], a['rank_res']) == (3, 3, 3)
    print(f"  the bound: -{a['h0t']} <= N <= {b['h0t']}  and the semicontinuity bound near this point: "
          f"N(27_s) <= min(3 - h0(dM;27_s), h0(dM;27bar_s)) <= 1 for every small deformation")

    print("\n=== the subregular 27 (B1257's embedding) ===")
    es, hs, fs, _ = E.subregular_sl2()
    reps = S.build_rep(es, fs)
    S.check_rep(reps, [1, 2], [REL])
    c = lemma_row(reps, "27   ")
    d = lemma_row(reps.dualrep(), "27bar")
    ok &= (c['h1'] - d['h1'] == c['N'] == 0) and (c['rank_res'] + d['rank_res'] == c['h1t'])

    print("\n=== the abelian sector through the lemma (B1260 (2), seen from the boundary) ===")
    # the Alexander root t = phi^2 is not in Q(omega); use the lemma on t = -1 (non-root) and on the
    # character t = omega (non-root) -- and, for a root, the field Q(omega, sqrt5) is not in this
    # instrument; B1260's own arc covers the root exactly.  Here: the wall at two non-roots, both duals.
    for name, val in (("t = -1", Qw(-1)), ("t = omega", OMEGA)):
        r1 = lemma_row(character_rep(val), f"C_{name}      ")
        r2 = lemma_row(character_rep(val.inv()), f"C_{name} dual")
        ok &= (r1['h1'] == r2['h1'] == 0) and (r1['N'] == 0)

    print("\n=== the theta-odd deformation class exists: h1(M; V8) ===")
    HV = E.hw_vectors(e)
    import sympy as sp
    basis = [HV[8]]
    v = HV[8]
    for k in range(8):
        v = E.br(f, v)
        basis.append(v)
    Bm = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in b_] for b_ in basis]).T

    def restrict(y):
        img = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in E.br(y, b_)] for b_ in basis]).T
        return Bm.gauss_jordan_solve(img)[0]
    ade, adf = restrict(e), restrict(f)

    def qwm(M, cst):
        out = E.qw_zeros(9)
        for i in range(9):
            for j in range(9):
                x = sp.Rational(M[i, j])
                out[i, j] = Qw(F(int(x.p), int(x.q))) * cst
        return out
    Aa, Aai = E.qw_expm_nilpotent(qwm(ade, ONE)), E.qw_expm_nilpotent(qwm(ade, Qw(-1)))
    Bb, Bbi = E.qw_expm_nilpotent(qwm(adf, E.U_RILEY)), E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))
    R8 = S.Rep({1: Aa, 2: Bb}, {1: Aai, 2: Bbi})
    S.check_rep(R8, [1, 2], [REL])
    h0_8, h1_8, _, _ = S.h0_h1(R8, [1, 2], [REL])
    print(f"  block V8 (the hv8 slot): h0 = {h0_8}, h1 = {h1_8}   (the theta-odd direction of the E6 character variety at the geometric point)")
    ok &= (h0_8, h1_8) == (0, 1)
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
