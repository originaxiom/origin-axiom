#!/usr/bin/env python3
"""
Appendix B -- the rung spectrum is an UPPER BOUND, not an attained set.

## WHY THIS SCRIPT EXISTS

An earlier version of Theorem (rung spectrum) enumerated the fourteen Levi dimensions
available in ambient E6 and asserted that each is ATTAINED by some subset S of the charge
algebra C.  That is an invalid converse: the enumeration bounds {dim z(S)} from above and
says nothing about which values a particular C realizes.  External review found the gap.

Centralizers are order-reversing, so S subset C implies z(C) subset z(S), and therefore
dim z(S) >= dim z(C) for every S.  This script computes dim z(C) = 12 exactly, which makes
the advertised values 6, 8 and 10 IMPOSSIBLE rather than merely unproved, and reports the
dimensions actually observed over all 16 coordinate subsets.

Exact over Q throughout; sympy is used only to solve for the principal sl2 and to expand
the invariant binary forms.
"""


import itertools
import sys
from fractions import Fraction

import sympy as sp

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


# ------------------------------------------------------------------ 1. E6 roots

# Bourbaki E6 Cartan matrix, chain 1-3-4-5-6 with node 2 attached to 4.
EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]
N = 6
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1


def build_roots():
    simples = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
    roots = set(simples)
    frontier = list(simples)
    while frontier:
        nxt = []
        for r in frontier:
            for j in range(N):
                # <r, alpha_j^vee> = sum_i r_i A[i][j]
                pair = sum(r[i] * A[i][j] for i in range(N))
                s = tuple(r[i] - pair * (1 if i == j else 0) for i in range(N))
                if any(s) and s not in roots:
                    roots.add(s)
                    nxt.append(s)
        frontier = nxt
    return sorted(roots)


ROOTS = build_roots()
IDX = {r: k for k, r in enumerate(ROOTS)}


def ip(a, b):
    """The Killing-normalised inner product (a,b), simply laced: = a^T A b."""
    return sum(a[i] * A[i][j] * b[j] for i in range(N) for j in range(N))


# ------------------------------------------------------------------ 2. cocycle


def eps_matrix():
    """Frenkel-Kac asymmetry function on the simple-root basis.

    eps(a,b) = prod (-1)^{B[i][j] a_i b_j} with B lower-unitriangular satisfying
    B[i][i] = 1 and B[i][j] + B[j][i] = (alpha_i, alpha_j) mod 2 for i != j.
    """
    B = [[0] * N for _ in range(N)]
    for i in range(N):
        B[i][i] = 1
        for j in range(i + 1, N):
            B[i][j] = A[i][j] % 2
    return B


B_COCYCLE = eps_matrix()


def eps(a, b):
    s = sum(B_COCYCLE[i][j] * a[i] * b[j] for i in range(N) for j in range(N))
    return -1 if s % 2 else 1


DIM = N + len(ROOTS)


def hvec(i):
    v = [Fraction(0)] * DIM
    v[i] = Fraction(1)
    return v


def evec(r):
    v = [Fraction(0)] * DIM
    v[N + IDX[r]] = Fraction(1)
    return v


def bracket_basis(p, q):
    """[b_p, b_q] in the Chevalley basis, as a coefficient vector."""
    out = [Fraction(0)] * DIM
    if p < N and q < N:
        return out                                  # Cartan is abelian
    if p < N:                                       # [h_i, e_r] = <r, alpha_i^vee> e_r
        r = ROOTS[q - N]
        c = sum(r[k] * A[k][p] for k in range(N))
        out[q] = Fraction(c)
        return out
    if q < N:
        r = ROOTS[p - N]
        c = sum(r[k] * A[k][q] for k in range(N))
        out[p] = Fraction(-c)
        return out
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if all(v == 0 for v in s):        # [e_a, e_-a] = eps(a,-a) h_a  (coroot, signed)
        sgn = eps(a, b)
        for i in range(N):
            out[i] = Fraction(sgn * a[i])
        return out
    if s in IDX:
        out[N + IDX[s]] = Fraction(eps(a, b))
    return out


BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    out = [Fraction(0)] * DIM
    for p, up in enumerate(u):
        if not up:
            continue
        for q, vq in enumerate(v):
            if not vq:
                continue
            row = BB[p][q]
            c = up * vq
            for k, rk in enumerate(row):
                if rk:
                    out[k] += c * rk
    return out


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def smul(c, u):
    return [Fraction(c) * a for a in u]


def is_zero(u):
    return all(a == 0 for a in u)




# ------------------------------------------------------------------ the audit

def dim_z(elts):
    """dim of the common centralizer in e6 of a list of elements, exactly over Q."""
    rows = []
    for x in elts:
        cols = [br(x, [Fraction(1) if i == j else Fraction(0) for i in range(DIM)])
                for j in range(DIM)]
        rows += [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
    if not rows:
        return DIM
    rows = [list(r) for r in rows]
    n = DIM
    piv = 0
    for c in range(n):
        pr = next((r for r in range(piv, len(rows)) if rows[r][c] != 0), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        piv += 1
        if piv == len(rows):
            break
    return DIM - piv


def main():
    print("=" * 70)
    print("Appendix B -- the rung spectrum is an UPPER BOUND, not an attained set")
    print("=" * 70)

    print("\n1. the E6 carrier")
    check("72 roots", len(ROOTS), 72)
    check("dim e6 = 6 + 72", DIM, 78)

    print("\n2. the principal sl2 and the four 2T-invariant charges")
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
            img = br(e, evec(r))
            for i2, val in enumerate(img):
                M[i2, j] = sp.Rational(val.numerator, val.denominator)
        ns = M.nullspace()
        if not ns:
            return None
        out = [Fraction(0)] * DIM
        for j, r in enumerate(cands):
            co = sp.Rational(ns[0][j])
            if co:
                out = add(out, smul(Fraction(co.p, co.q), evec(r)))
        return out

    x, y = sp.symbols("x y")
    tp = x**5 * y - x * y**5
    Wp = x**8 + 14 * x**4 * y**4 + y**8
    FORMS = {8: Wp, 14: sp.expand(tp * Wp), 16: sp.expand(Wp**2), 22: sp.expand(tp * Wp**2)}
    C = {}
    for n in (8, 14, 16, 22):
        top = hw(n)
        if top is None:
            continue
        P = sp.Poly(FORMS[n], x, y)
        acc, cur = [Fraction(0)] * DIM, top
        for k in range(n + 1):
            co = P.coeff_monomial(x**(n - k) * y**k)
            if co:
                q = sp.Rational(sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n))
                acc = add(acc, smul(Fraction(q.p, q.q), cur))
            cur = br(f, cur)
        C[n] = acc
    check("the four charges are built, degrees 8/14/16/22", sorted(C), [8, 14, 16, 22])

    print("\n3. dim z(S) over every subset of the four charges")
    keys = sorted(C)
    seen = {}
    for k in range(len(keys) + 1):
        for sub in itertools.combinations(keys, k):
            d = dim_z([C[i] for i in sub])
            seen.setdefault(d, []).append(sub)
    dzC = dim_z([C[i] for i in keys])
    for d in sorted(seen):
        print(f"      dim z(S) = {d:3d}   for {len(seen[d])} of the 16 subsets")
    check("dim z(C) = 12", dzC, 12)
    check("observed spectrum over all 16 subsets", sorted(seen), [12, 30, 78])

    print("\n4. the containment, and what it rules out")
    print("      centralizers are order-reversing: S subset C  =>  z(C) subset z(S)")
    check("every subset has dim z(S) >= dim z(C)", all(d >= dzC for d in seen), True)
    AMBIENT = [6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
    impossible = [v for v in AMBIENT if v < dzC]
    check("the ambient values below dim z(C), hence impossible", impossible, [6, 8, 10])
    check("the theorem's stated upper bound", [v for v in AMBIENT if v >= dzC],
          [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78])
    print("      NOTE: an earlier draft called the fourteen ambient values ATTAINED.")
    print("      They are an upper bound.  6, 8 and 10 are impossible; of the rest only")
    print("      12, 30 and 78 were observed here.  See Remark (spectrum scope).")

    print()
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce: {FAILURES}")
        return 1
    print("PASS: every check reproduced exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
