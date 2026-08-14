#!/usr/bin/env python3
"""B872 support -- the normalization certificate (and a THIRD derivation of the cubic).

Establishes mod p = 2^61 - 1: the fresh deterministic B854 build's enhancement cubic
(radical of the interpolated det48 along the pencil ad(x8 + t x16)) equals
banked_B866_mine(t/13) up to a unit -- i.e. today's build carries the SOLO seat's
rho-normalization, and the enhancement points sit at t = 13 x (banked roots).
Consequence recorded in [[b854-pencil-normalization-13x]]: using the banked roots
unscaled on a fresh build lands on the generic 30-stratum, not the enhancement.
Run: python3 cubic_modp_check.py   (prints mu = 1/13 and consistency at all degrees)
"""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
P = (1 << 61) - 1
BANKED = [1, -28224, -159667200, 500716339200]      # ascending, B866 "mine"


def main():
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]

    def admat_exact(v):
        cols = [br(v, b) for b in basis]
        return [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
    A8 = admat_exact(g["INV"][8])
    A16 = admat_exact(g["INV"][16])

    def amodp(t):
        return [[(int(A8[i][j].numerator) * pow(int(A8[i][j].denominator), -1, P)
                  + t * int(A16[i][j].numerator)
                  * pow(int(A16[i][j].denominator), -1, P)) % P
                 for j in range(DIM)] for i in range(DIM)]

    def rank_pivots(M):
        M = [row[:] for row in M]
        piv, r = [], 0
        for c in range(DIM):
            pr = next((i for i in range(r, DIM) if M[i][c] % P), None)
            if pr is None:
                continue
            M[r], M[pr] = M[pr], M[r]
            inv = pow(M[r][c], -1, P)
            for i in range(DIM):
                if i != r and M[i][c]:
                    f = (M[i][c] * inv) % P
                    for j in range(c, DIM):
                        M[i][j] = (M[i][j] - f * M[r][j]) % P
            piv.append(c)
            r += 1
        return r, piv

    random.seed(1)
    t0 = random.randrange(P)
    M0 = amodp(t0)
    r0, cols = rank_pivots(M0)
    MT = [[M0[j][i] for j in range(DIM)] for i in range(DIM)]
    r1, rows = rank_pivots(MT)
    assert r0 == 48, r0
    rows48, cols48 = rows[:48], cols[:48]

    def det48(t):
        A = amodp(t)
        M = [[A[i][j] for j in cols48] for i in rows48]
        d = 1
        for c in range(48):
            pr = next((i for i in range(c, 48) if M[i][c] % P), None)
            if pr is None:
                return 0
            if pr != c:
                M[c], M[pr] = M[pr], M[c]
                d = (-d) % P
            d = (d * M[c][c]) % P
            inv = pow(M[c][c], -1, P)
            for i in range(c + 1, 48):
                if M[i][c]:
                    f = (M[i][c] * inv) % P
                    for j in range(c, 48):
                        M[i][j] = (M[i][j] - f * M[c][j]) % P
        return d

    xs = list(range(51))
    ys = [det48(x) for x in xs]
    n = len(xs)
    coef = ys[:]
    for k in range(1, n):
        for i in range(n - 1, k - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) * pow(xs[i] - xs[i - k], -1, P) % P
    poly = [0] * n
    for i in range(n - 1, -1, -1):
        newp = [0] * n
        for k in range(n - 1):
            newp[k + 1] = poly[k]
        for k in range(n):
            newp[k] = (newp[k] - xs[i] * poly[k]) % P
        newp[0] = (newp[0] + coef[i]) % P
        poly = newp
    deg = max(i for i, c in enumerate(poly) if c)
    assert deg == 48, deg

    def polmod(a, b):
        a = a[:]
        db = max(i for i, c in enumerate(b) if c)
        inv = pow(b[db], -1, P)
        while True:
            da = max((i for i, c in enumerate(a) if c), default=-1)
            if da < db:
                return a
            f = (a[da] * inv) % P
            for i in range(db + 1):
                a[da - db + i] = (a[da - db + i] - f * b[i]) % P

    def polgcd(a, b):
        while any(c for c in b):
            a, b = b, polmod(a, b)
        da = max((i for i, c in enumerate(a) if c), default=0)
        inv = pow(a[da], -1, P)
        return [(c * inv) % P for c in a[:da + 1]]

    def poldiv(a, b):
        q = [0] * len(a)
        a = a[:]
        db = max(i for i, c in enumerate(b) if c)
        inv = pow(b[db], -1, P)
        while True:
            da = max((i for i, c in enumerate(a) if c), default=-1)
            if da < db:
                break
            f = (a[da] * inv) % P
            q[da - db] = f
            for i in range(db + 1):
                a[da - db + i] = (a[da - db + i] - f * b[i]) % P
        return q

    dpoly = [(i * c) % P for i, c in enumerate(poly)][1:]
    radical = poldiv(poly[:deg + 1], polgcd(poly[:deg + 1], dpoly))
    dr = max(i for i, c in enumerate(radical) if c)
    assert dr == 3, dr
    r = [(c * pow(radical[0], -1, P)) % P for c in radical[:4]]
    b = [(c * pow(BANKED[0] % P, -1, P)) % P for c in [x % P for x in BANKED]]
    mu = (r[1] * pow(b[1], -1, P)) % P
    ok2 = (r[2] == (b[2] * mu * mu) % P)
    ok3 = (r[3] == (b[3] * pow(mu, 3, P)) % P)
    inv13 = pow(13, -1, P)
    print(f"det48 degree {deg}; radical degree {dr}")
    print(f"mu mod p = {mu}; equals 1/13: {mu == inv13}; "
          f"consistent at deg 2/3: {ok2}/{ok3}")
    assert mu == inv13 and ok2 and ok3
    print("CERTIFIED: fresh-build cubic = banked(t/13); enhancement at t = 13 x banked roots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
