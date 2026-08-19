#!/usr/bin/env python3
"""
Appendix B -- the rung spectrum is ATTAINED, and the eleven-element bound is TIGHT.

## WHY THIS SCRIPT EXISTS

Its companion check_rung_spectrum.py establishes the CONTAINMENT and reports what a
SAMPLE of the subspace lattice of C sees: {12, 30, 78} over all 16 coordinate subsets,
with a sweep of 440 further rational directions adding nothing.  An earlier draft
concluded from that sample that the realized spectrum is "far smaller" than the eleven
values.  It is not.  The sample was the wrong instrument, and this script says why and
replaces it.

The subspace lattice of C is INFINITE, so no sample can decide the question.  What
decides it is that the lattice's IMAGE under dim z is finite:

  (1) e6 = z(C) (+) V', with C acting as identically ZERO on z(C) -- not merely
      nilpotently -- and the characteristic polynomial of a generic element of ad(C)
      factoring as t^12 * q6^3 * q12 * q12'^3 with q6, q12, q12' irreducible over Q.
      So C acts semisimply on V' with thirty non-zero weights in three Galois orbits:
      six of multiplicity 3, twelve of multiplicity 1, twelve of multiplicity 3, and
      12 + 18 + 12 + 36 = 78 accounts for e6.

  (2) Hence for EVERY subspace S of C,   dim z(S) = 12 + sum{ m_L : L|_S = 0 },
      so dim z is the flat-function of an arrangement of thirty hyperplanes in a
      four-dimensional space.

  (3) Enumerating the 109 flats returns exactly the eleven values.

Step (1) is exact over Q.  Step (3) is exhaustive at a prime at which the thirty weights
stay distinct with the multiplicities computed in step (1); reduction modulo p can only
ADD linear dependencies among weights, so this is not a certificate over Kbar, and the
paper says so in Remark (spectrum scope) rather than suppressing it.

Why the sample could not have worked: the eight values it missed are attained only on
proper subvarieties of C, which a random rational direction misses with probability 1.
The sharpest case is checked here exactly -- on the (8,16)-plane the enhancement locus is
cut by an IRREDUCIBLE cubic, so every RATIONAL direction there gives 30 and the value 46
appears only after base change.

Exact over Q except where stated; sympy is used for the principal sl2, the invariant
binary forms, and the characteristic polynomial factorisation.
"""
import itertools
from fractions import Fraction

import sympy as sp

from check_rung_spectrum import (A, DIM, IDX, N, ROOTS, add, br, eps, evec,  # noqa: F401
                                 smul)

FAILURES = []
ELEVEN = [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def build_charges():
    A6 = sp.Matrix(A)
    cv = A6.T.solve(sp.Matrix([2] * N))
    h = [Fraction(0)] * DIM
    for j in range(N):
        q = sp.Rational(cv[j])
        h[j] = Fraction(q.p, q.q)
    e = [Fraction(0)] * DIM
    for j in range(N):
        e = add(e, evec(tuple(1 if i == j else 0 for i in range(N))))
    f = [Fraction(0)] * DIM
    for j in range(N):
        pos = tuple(1 if i == j else 0 for i in range(N))
        neg = tuple(-t for t in pos)
        q = sp.Rational(cv[j])
        f = add(f, smul(Fraction(q.p, q.q) / eps(pos, neg), evec(neg)))

    def hw(n):
        cands = [r for r in ROOTS if br(h, evec(r))[N + IDX[r]] == n]
        M = sp.zeros(DIM, len(cands))
        for j, r in enumerate(cands):
            for i2, val in enumerate(br(e, evec(r))):
                M[i2, j] = sp.Rational(val.numerator, val.denominator)
        ns = M.nullspace()
        out = [Fraction(0)] * DIM
        for j, r in enumerate(cands):
            co = sp.Rational(ns[0][j])
            if co:
                out = add(out, smul(Fraction(co.p, co.q), evec(r)))
        return out

    x, y = sp.symbols("x y")
    tp = x**5 * y - x * y**5
    Wp = x**8 + 14 * x**4 * y**4 + y**8
    FORMS = {8: Wp, 14: sp.expand(tp * Wp), 16: sp.expand(Wp**2),
             22: sp.expand(tp * Wp**2)}
    C = {}
    for n in (8, 14, 16, 22):
        top = hw(n)
        P = sp.Poly(FORMS[n], x, y)
        acc, cur = [Fraction(0)] * DIM, top
        for k in range(n + 1):
            co = P.coeff_monomial(x**(n - k) * y**k)
            if co:
                q = sp.Rational(sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n))
                acc = add(acc, smul(Fraction(q.p, q.q), cur))
            cur = br(f, cur)
        C[n] = acc
    return C


def ad_matrix(x):
    cols = [br(x, [Fraction(1) if i == j else Fraction(0) for i in range(DIM)])
            for j in range(DIM)]
    return sp.Matrix(DIM, DIM, lambda i, j: sp.Rational(cols[j][i].numerator,
                                                        cols[j][i].denominator))


def nullspace_mod(M, p):
    Mx = [row[:] for row in M]
    piv, r = [], 0
    for c in range(DIM):
        pr = next((i for i in range(r, DIM) if Mx[i][c] % p), None)
        if pr is None:
            continue
        Mx[r], Mx[pr] = Mx[pr], Mx[r]
        iv = pow(Mx[r][c], p - 2, p)
        Mx[r] = [v * iv % p for v in Mx[r]]
        for i in range(DIM):
            if i != r and Mx[i][c] % p:
                fq = Mx[i][c]
                Mx[i] = [(Mx[i][j] - fq * Mx[r][j]) % p for j in range(DIM)]
        piv.append(c)
        r += 1
    free = [c for c in range(DIM) if c not in piv]
    out = []
    for fc in free:
        v = [0] * DIM
        v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mx[i][fc]) % p
        out.append(v)
    return out


def rank4(vs, p):
    Mx = [list(v) for v in vs]
    r = 0
    for c in range(4):
        pr = next((i for i in range(r, len(Mx)) if Mx[i][c] % p), None)
        if pr is None:
            continue
        Mx[r], Mx[pr] = Mx[pr], Mx[r]
        iv = pow(Mx[r][c], p - 2, p)
        Mx[r] = [v * iv % p for v in Mx[r]]
        for i in range(len(Mx)):
            if i != r and Mx[i][c] % p:
                fq = Mx[i][c]
                Mx[i] = [(Mx[i][j] - fq * Mx[r][j]) % p for j in range(4)]
        r += 1
    return r


def main():
    print("=" * 74)
    print("Appendix B -- the rung spectrum is ATTAINED; the eleven-element bound is TIGHT")
    print("=" * 74)

    print("\n1. the four 2T-invariant charges, and dim z(C)")
    C = build_charges()
    check("the four charges are built, degrees 8/14/16/22", sorted(C), [8, 14, 16, 22])
    DEG = [8, 14, 16, 22]
    AD = {n: ad_matrix(C[n]) for n in DEG}
    zC = sp.Matrix.vstack(*[AD[n] for n in DEG]).nullspace()
    check("dim z(C) = 12, exactly over Q", len(zC), 12)

    print("\n2. the decomposition e6 = z(C) (+) V'  -- exact over Q")
    R = AD[8] + 2 * AD[14] + 3 * AD[16] + 5 * AD[22]
    t = sp.symbols("t")
    cp = R.charpoly(t)
    fac = sp.factor_list(cp.as_expr())[1]
    zero_mult = next(m for f_, m in fac if sp.Poly(f_, t).as_expr() == t)
    check("the zero weight has multiplicity 12 = dim z(C)", zero_mult, 12)
    orbits = sorted((sp.Poly(f_, t).degree(), m) for f_, m in fac
                    if sp.Poly(f_, t).as_expr() != t)
    check("three Galois orbits of weights: 6x3, 12x1, 12x3", orbits,
          [(6, 3), (12, 1), (12, 3)])
    check("dimensions account exactly: 12 + 18 + 12 + 36 = 78",
          12 + sum(d * m for d, m in orbits), 78)
    # The generalised zero-space of R.  An earlier version formed R^128 by repeated
    # squaring and took its nullspace: correct, but the entries of an exact 78x78
    # rational 128th power are enormous and it dominated the runtime of the whole
    # suite.  The same space is ker(R^12): the zero eigenvalue has algebraic
    # multiplicity 12 in charpoly(R) (checked above), so the Jordan blocks at 0 have
    # total size 12 and stabilise by step 12 at the latest.
    Rp = R ** 12
    V0 = Rp.nullspace()
    check("the generalised zero-space is z(C), of dimension 12", len(V0), 12)
    B0 = sp.Matrix.hstack(*V0)
    check("C acts as identically ZERO on z(C), not merely nilpotently",
          all((AD[n] * B0).is_zero_matrix for n in DEG), True)
    # and it really is the *generalised* zero-space: one more power adds nothing
    check("ker(R^13) = ker(R^12), so the generalised zero-space has stabilised",
          len((R ** 13).nullspace()), 12)
    print("      => for EVERY subspace S of C,  dim z(S) = 12 + sum{ m_L : L|_S = 0 }")
    print("         The lattice is infinite; its image is not.")

    print("\n3. the (8,16)-plane: why no RATIONAL direction ever reaches 46")
    W = AD[16].columnspace()
    BW = sp.Matrix.hstack(*W)
    check("W = im(ad x16) has dimension 48", len(W), 48)
    cols8, cols16 = [], []
    for j in range(BW.cols):
        cols16.append(BW.gauss_jordan_solve(AD[16] * BW[:, j])[0])
        cols8.append(BW.gauss_jordan_solve(AD[8] * BW[:, j])[0])
    Q = sp.Matrix.hstack(*cols16).inv() * sp.Matrix.hstack(*cols8)
    fq = sp.factor_list(Q.charpoly(t).as_expr())[1]
    check("charpoly(Q) is one cubic to the 16th power (16 = the jump 46-30, derived)",
          sorted((sp.Poly(f_, t).degree(), m) for f_, m in fq), [(3, 16)])
    g = sp.Poly(next(f_ for f_, _ in fq), t)
    check("that cubic is IRREDUCIBLE over Q, so no rational direction gives 46",
          g.is_irreducible, True)

    def sqfree(v):
        s = 1
        for pp, e_ in sp.factorint(abs(int(v))).items():
            if e_ % 2:
                s *= pp
        return s
    u = sp.symbols("u")
    check("its discriminant shares the squarefree part 77 with x^3-12x-5",
          (sqfree(sp.discriminant(g)),
           sqfree(sp.discriminant(sp.Poly(u**3 - 12 * u - 5, u)))), (77, 77))
    Kf = sp.QQ.algebraic_field(sp.rootof(u**3 - 12 * u - 5, 0))
    check("it acquires a root in K, hence generates K itself",
          sorted(sp.Poly(f_, t).degree()
                 for f_, _ in sp.factor_list(sp.Poly(g.as_expr(), t, domain=Kf))[1]),
          [1, 2])

    print("\n4. the flat enumeration -- exhaustive, at a faithful prime")
    p = 409
    Mp = {n: [[int(AD[n][i, j].p) * pow(int(AD[n][i, j].q), p - 2, p) % p
               for j in range(DIM)] for i in range(DIM)] for n in DEG}
    Rm = [[(Mp[8][i][j] + 2 * Mp[14][i][j] + 3 * Mp[16][i][j] + 5 * Mp[22][i][j]) % p
           for j in range(DIM)] for i in range(DIM)]
    # the ad-matrices carry denominators, so the charpoly coefficients are rationals:
    # reduce each as p/q mod the prime rather than assuming it is an integer.
    cpz = []
    for c in sp.Poly(cp.as_expr(), t).all_coeffs():
        rc = sp.Rational(c)
        cpz.append(int(rc.p) % p * pow(int(rc.q) % p, p - 2, p) % p)

    def ev(a):
        acc = 0
        for c in cpz:
            acc = (acc * a + c) % p
        return acc
    eigs = [a for a in range(p) if ev(a) == 0]          # only the actual eigenvalues
    weights = []
    for a in eigs:
        E = nullspace_mod([[(Rm[i][j] - (a if i == j else 0)) % p for j in range(DIM)]
                           for i in range(DIM)], p)
        if not E:
            continue
        v = E[0]
        nzi = next(i for i in range(DIM) if v[i])
        lam = []
        for n in DEG:
            w = [sum(Mp[n][i][j] * v[j] for j in range(DIM)) % p for i in range(DIM)]
            s = w[nzi] * pow(v[nzi], p - 2, p) % p
            if any((w[i] - s * v[i]) % p for i in range(DIM)):
                lam = None
                break
            lam.append(s)
        if lam is None:
            continue
        weights.append((tuple(lam), len(E)))
    nz = [(l, m) for l, m in weights if any(l)]
    check(f"p={p} is faithful: thirty distinct weights with the exact Q-multiplicities",
          (len(nz), sorted((m, sum(1 for _, mm in nz if mm == m))
                           for m in {mm for _, mm in nz})), (30, [(1, 12), (3, 18)]))
    check("control: exactly six weights, of total multiplicity 18, vanish on the "
          "(8,16)-plane, giving 12+18 = 30",
          (len([1 for l, m in nz if l[0] == 0 and l[2] == 0]),
           sum(m for l, m in nz if l[0] == 0 and l[2] == 0)), (6, 18))
    flats = {}
    for k in range(5):
        for sub in itertools.combinations(range(30), k):
            vs = [nz[i][0] for i in sub]
            if (rank4(vs, p) if vs else 0) != k:
                continue
            flats[frozenset(i for i in range(30)
                            if rank4(vs + [nz[i][0]], p) == k)] = k
    spectrum = sorted({12 + sum(nz[i][1] for i in F) for F in flats})
    check("the arrangement has 109 flats", len(flats), 109)
    check("the realized spectrum is EXACTLY the theorem's eleven values",
          spectrum, ELEVEN)
    fourteen = sorted({4 - r for F, r in flats.items()
                       if 12 + sum(nz[i][1] for i in F) == 14})
    check("dim z(S) = 14 is attained, at 3-dimensional S "
          "(so Thm (second measurement)'s occurrence is not an assumption)",
          fourteen, [3])

    print("\n5. what this replaces")
    print("      the sample saw {12, 30, 78}; the enumeration returns all eleven.")
    print("      the eight it missed lie on proper subvarieties, which a random")
    print("      rational direction misses with probability 1.  The sample was not")
    print("      unlucky -- it was the wrong instrument for the question.")
    print("      SCOPE: steps 1-3 are exact over Q; step 4 is exhaustive at a faithful")
    print("      prime and is NOT a certificate over Kbar, since reduction mod p can")
    print("      only ADD dependencies among weights.  Remark (spectrum scope) says so.")

    print()
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce: {FAILURES}")
        return 1
    print("PASS: every check reproduced exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
