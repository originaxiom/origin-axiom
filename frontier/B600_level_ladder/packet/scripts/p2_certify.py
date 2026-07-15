"""P2 certification pass — exact/50-digit certificates for the banked level-4 readouts.

1. Z4 = 0 EXACTLY: the unnormalized cyclotomic sum Tr(T^3 . U) reduced in Q(zeta_192)
   (sympy exact) — a zero of the sum certifies Z = 0 regardless of normalization.
   Same certificate recomputed for levels 1-3 (must give the banked +1 pattern).
2. ord(B_odd) = 12 at dps 50 (proper divisors 6, 4 bounded away).
3. The 18 magnitude values: minimal polynomials via mpmath.findpoly at dps 50
   (degree sweep 1..8), sympy-verified, discriminant/conductor prime content reported.
4. The Pisano candidate set {N <= 200 : ord(A1 mod N) = pi(N)/gcd(pi(N),2) = 12}.
5. The parity control: same order/magnitude readouts on the theta-EVEN block.
6. (tr_even, tr_odd) ladder row for level 4, exact.
"""
import sys
sys.path.insert(0, 'scripts')
import json

import mpmath as mp
import numpy as np
import sympy as sp

from engine import (Level, weyl_group, mp_odd_blocks, mp_magnitude_poly,
                    mp_certify_order, theta, HVEE)

mp.mp.dps = 50


def exact_Z(L):
    """Tr rho = sum_a zeta_{12K}^{3*T_expo[a]} * U_aa, U from exact counts.
    EXACT: accumulate an integer coefficient vector over powers of zeta_{12K},
    reduce mod the cyclotomic polynomial Phi_{12K}(x) over Z. Returns the
    reduced sympy Poly (zero poly <=> the value is exactly 0) + a 30-digit
    numeric evaluation."""
    M12 = 12 * L.K
    coef = [0] * M12
    for a in range(L.N):
        sh = 3 * int(L.T_expo[a])
        row = L.counts[a, a]
        for j in range(L.M6):
            c = int(row[j])
            if c:
                coef[(2 * j + sh) % M12] += c
    x = sp.Symbol('x')
    poly = sp.Poly(list(reversed(coef)), x, domain='ZZ')
    phi = sp.Poly(sp.cyclotomic_poly(M12, x), x, domain='ZZ')
    red = poly.rem(phi)
    zval = mp.e ** (2j * mp.pi / M12)
    num = mp.fsum(int(c) * zval ** e for e, c in enumerate(coef) if c)
    return red, num


def mp_even_block(L, dps=50):
    mp.mp.dps = dps
    S = L.S_mp(dps)
    T = L.T_mp(dps)
    rho = T * T * S * T
    fixed, pairs = L.fixed_idx, L.pairs
    n_even = len(fixed) + len(pairs)
    even = mp.matrix(L.N, n_even)
    for j, a in enumerate(fixed):
        even[a, j] = 1
    s2 = 1 / mp.sqrt(2)
    for j, (a, b) in enumerate(pairs):
        even[a, len(fixed) + j] = s2
        even[b, len(fixed) + j] = s2
    S_even = even.T * S * even
    B_even = even.T * rho * even
    return S_even, B_even


def eig_order(B, dps=50, qmax=100000):
    """Order of a unitary matrix via eigenvalue phases: each arg/2pi must be
    rational p/q (q <= qmax) to 1e-(dps-15); order = lcm(q). Certified by a
    matrix-power check at the found order and its maximal proper divisors."""
    from fractions import Fraction
    from math import lcm
    mp.mp.dps = dps
    ev = mp.eig(B, left=False, right=False)
    qs = []
    for lam in ev:
        t = mp.arg(lam) / (2 * mp.pi)
        fr = Fraction(float(t)).limit_denominator(qmax)
        if abs(t - mp.mpf(fr.numerator) / fr.denominator) > mp.mpf(10) ** (-(dps - 15)):
            return None, None, None   # not a root of unity at this precision
        qs.append(fr.denominator)
    order = 1
    for q in qs:
        order = lcm(order, q)
    d_ord, d_props = mp_certify_order(B, order, dps=dps)
    return order, d_ord, d_props


def minpolys(ws, dps=50):
    """Minimal polynomial per value via findpoly sweep, sympy-verified."""
    out = []
    for w in ws:
        got = None
        for deg in range(1, 9):
            p = mp.findpoly(w, deg, maxcoeff=10 ** 8, tol=mp.mpf(10) ** (-(dps - 10)))
            if p:
                poly = sp.Poly(list(p), sp.Symbol('w'))
                if poly.LC() < 0:
                    poly = sp.Poly([-c for c in list(p)], sp.Symbol('w'))
                fac = sp.factor_list(poly.as_expr())
                # take the irreducible factor vanishing at w
                best = None
                for f, _ in fac[1]:
                    pf = sp.Poly(f, sp.Symbol('w'))
                    val = abs(mp.mpf(1) * sum(mp.mpf(int(c)) * w ** i
                              for i, c in enumerate(reversed(pf.all_coeffs()))))
                    if val < mp.mpf(10) ** (-(dps - 15)):
                        best = pf
                        break
                if best is not None:
                    got = best
                    break
        if got is None:
            out.append((str(w), None, None, None))
            continue
        disc = sp.discriminant(got.as_expr(), sp.Symbol('w'))
        primes = sorted(sp.factorint(sp.Integer(abs(disc))).keys()) if disc != 0 else []
        out.append((mp.nstr(w, 30), got.all_coeffs(), int(disc), primes))
    return out


def fib_order(N):
    """ord(A1 mod N) for A1 = [[2,1],[1,1]] by direct matrix powers."""
    A = np.array([[2, 1], [1, 1]], dtype=object)
    M = A % N
    I = np.eye(2, dtype=object) % N
    P = M.copy()
    for m in range(1, 20000):
        if (P == I).all():
            return m
        P = (P @ M) % N
    return None


def main():
    W, eps = weyl_group()
    print("=== exact-Z certificates (integer reduction mod Phi_12K) ===")
    for k in (1, 2, 3, 4):
        L = Level(k, W, eps)
        red, num = exact_Z(L)
        iszero = red.is_zero
        print(f"level {k}: unnormalized Tr(T^3 U): zero-poly = {iszero}; "
              f"numeric ~ {mp.nstr(num, 12)}")
        if k == 4:
            assert iszero, "Z4 exact-zero certificate FAILED"
            print("  -> Z4 = 0 EXACTLY (the coefficient vector reduces to the zero "
                  "polynomial mod Phi_192 over Z)")

    print("\n=== level-4 blocks at dps 50 ===")
    L4 = Level(4, W, eps)
    S_odd, B_odd, _ = mp_odd_blocks(L4, dps=50)
    d_ord, d_props = mp_certify_order(B_odd, 12, dps=50)
    print(f"ord(B_odd) = 12 certificate: ||B^12 - I|| = {d_ord:.2e}; "
          f"proper divisor devs = { {d: f'{v:.2e}' for d, v in d_props.items()} }")
    o_eig = eig_order(B_odd, dps=50)
    print(f"eigenvalue-order cross-check: {o_eig[0]}")

    ints, D, ws50 = mp_magnitude_poly(L4, S_odd, dps=50, max_scale_pow3=12)
    ws = [mp.mpf(w) for w in ws50]
    print(f"\n18 magnitude values w = 32|S_odd|^2 (dps50): product-poly integer scale D = {D}")
    print("\n=== minimal polynomials of the 18 w-values ===")
    mps_ = minpolys(ws)
    for w, coeffs, disc, primes in mps_:
        print(f"  w = {w}\n     minpoly {coeffs}  disc {disc}  disc-primes {primes}")

    print("\n=== the parity control: theta-EVEN block ===")
    S_even, B_even = mp_even_block(L4, dps=50)
    oe, oe_dev, oe_props = eig_order(B_even, dps=50)
    print(f"ord(B_even) = {oe}  (certificate dev {oe_dev if oe_dev is None else f'{oe_dev:.2e}'}; "
          f"proper divisors { {d: f'{v:.2e}' for d, v in (oe_props or {}).items()} })")
    tr_o = mp.fsum(B_odd[i, i] for i in range(B_odd.rows))
    tr_e = mp.fsum(B_even[i, i] for i in range(B_even.rows))
    print(f"tr_odd = {mp.nstr(tr_o, 20)}   tr_even = {mp.nstr(tr_e, 20)}")
    # even-block magnitudes
    vals = []
    for i in range(S_even.rows):
        for j in range(S_even.cols):
            m = mp.sqrt((S_even[i, j] * mp.conj(S_even[i, j])).real)
            if m > mp.mpf('1e-30') and not any(abs(m - v) < mp.mpf('1e-30') for v in vals):
                vals.append(m)
    we = sorted(32 * v ** 2 for v in vals)
    print(f"even block: {len(we)} distinct magnitudes")
    mps_e = minpolys(we)
    ep = sorted({p for _, _, _, primes in mps_e if primes for p in primes})
    print(f"even-block disc primes union: {ep}")

    print("\n=== Pisano candidate set for the clock 12 ===")
    cands = [N for N in range(2, 201) if fib_order(N) == 12]
    print(f"{{N <= 200 : ord(A1 mod N) = 12}} = {cands}")
    for k, o in ((2, 4), (3, 60)):
        c = [N for N in range(2, 201) if fib_order(N) == o]
        print(f"  (ladder context) order {o} (level {k}): candidates {c}")

    print("\n=== odd-block T-content (mechanism readout) ===")
    todd = sorted({int(L4.T_expo[a]) % 192 for a, b in L4.pairs} |
                  {int(L4.T_expo[b]) % 192 for a, b in L4.pairs})
    import math
    g = math.gcd(*todd) if todd else 0
    print(f"T exponents on paired weights (mod 192): {todd}; gcd {g}; "
          f"orders {sorted({192 // math.gcd(192, e) for e in todd})}")


if __name__ == '__main__':
    main()
