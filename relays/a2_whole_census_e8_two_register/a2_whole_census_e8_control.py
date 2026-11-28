#!/usr/bin/env python3
"""Standalone self-contained failing control for Card A2-WHOLE-CENSUS-E8-TWO-REGISTER.
Demonstrates under python3 -I that replacing the order-4 C_4 sheet lift j (j^2 = -1)
with an order-5 C_5 sheet rotation r (r^5 = 1, eigenvalues zeta_5, zeta_5^{-1}) fails to
collapse the 128-spinor peripheral adjoint kernel in E_8 to 0 (yielding 4 or 6 > 0).
Exits 1 with 0 stderr bytes. Standard library only; zero AST floats.
"""
import itertools
import sys


def f25_mul(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5, (x[0] * y[1] + x[1] * y[0]) % 5)


def f25_tr(x):
    return (2 * x[0]) % 5


def main():
    # Build 12 pairs {+-x} in F_25^*
    pairs = []
    seen = set()
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            neg = ((-a) % 5, (-b) % 5)
            p = min((a, b), neg)
            if p not in seen:
                seen.add(p)
                pairs.append(p)
    v1, v2, two = (1, 0), (0, 3), (2, 0)
    w12 = [(f25_tr(f25_mul(v1, f25_mul(two, f25_mul(x, x)))),
            f25_tr(f25_mul(v2, f25_mul(two, f25_mul(x, x))))) for x in pairs]
    rem = list(w12)
    p6 = []
    while rem:
        w = rem.pop(0)
        rem.remove(((-w[0]) % 5, (-w[1]) % 5))
        p6.append(w)
    hp = [((4 * ((3 * wm) % 5)) % 20, (4 * ((3 * wl) % 5)) % 20) for wm, wl in p6]
    w64 = [
        (sum(e * h[0] for e, h in zip(eps, hp)) % 20,
         sum(e * h[1] for e, h in zip(eps, hp)) % 20)
        for eps in itertools.product((1, -1), repeat=6)
    ]
    # Faulted control: replace C_4 j (phases 5, 15 mod 20) with C_5 r (phases 4, 16 mod 20) on meridian!
    w2_faulted = [(4, 10), (16, 10)]
    w128 = [((a[0] + b[0]) % 20, (a[1] + b[1]) % 20) for a in w64 for b in w2_faulted]
    spins = [(0, 0), (0, 10), (10, 0), (10, 10)]
    k128_total = sum(1 for x in w128 if x in spins)
    print(f"FAIL_CONTROL: C5_sheet_rotation_k128_total={k128_total} expected=0")
    return 0 if k128_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
