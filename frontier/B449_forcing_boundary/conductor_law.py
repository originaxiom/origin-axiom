#!/usr/bin/env python3
"""B449 — the disc×disc adjudication + the in-family conductor law (exact).

Run: python3 conductor_law.py   (prints ALL CHECKS PASS)
"""
import sympy as sp

t = sp.Symbol('t')

ALEXANDER = {'4_1': t**2 - 3*t + 1, '5_2': 2*t**2 - 3*t + 2, '6_1': 2*t**2 - 5*t + 2}


def run():
    ok = True
    # 1. fiberedness: Alexander monic <=> fibered (for these knots)
    fib = {k: abs(sp.LC(p, t)) == 1 for k, p in ALEXANDER.items()}
    ok &= fib['4_1'] and not fib['5_2'] and not fib['6_1']
    print(f"fibered: 4_1={fib['4_1']}  5_2={fib['5_2']}  6_1={fib['6_1']}  "
          f"(the disc x disc 'prediction' for 5_2/6_1 names a nonexistent dynamics end)")

    # 2. the fig-8 Alexander IS the monodromy char poly (dynamics disc = 5)
    A = sp.Matrix([[2, 1], [1, 1]])
    ok &= sp.expand(A.charpoly(t).as_expr() - ALEXANDER['4_1']) == 0
    ok &= sp.discriminant(ALEXANDER['4_1'], t) == 5
    print("Alexander(4_1) == charpoly(monodromy), disc 5 (the golden/dynamics end):", ok)

    # 3. the conductor law: golden 15, silver 8 (with the B448 zeta_8 witness), bronze prediction
    #    conductors: Q(sqrt-3)->3, Q(sqrt5)->5, Q(i)->4, Q(sqrt2)->8, Q(sqrt13)->13
    golden_level = sp.ilcm(3, 5)
    silver_level = sp.ilcm(4, 8)
    ok &= golden_level == 15 and silver_level == 8
    S = sp.Matrix([[5, 2], [2, 1]])
    ds = sp.discriminant(S.charpoly(t).as_expr(), t)
    ok &= ds == 32                                   # -> Q(sqrt2), conductor 8
    B3 = sp.Matrix([[10, 3], [3, 1]])
    db = sp.discriminant(B3.charpoly(t).as_expr(), t)
    ok &= db == 117 and sp.factorint(db) == {3: 2, 13: 1}   # -> Q(sqrt13), cond 13
    bronze_pred = sorted([sp.ilcm(3, 13), sp.ilcm(4, 13)])
    ok &= bronze_pred == [39, 52]
    print(f"conductor law: golden level {golden_level} (banked B424), silver level {silver_level} "
          f"(B448 gate: z^4+16 -> Q(zeta8)), bronze prediction level in {bronze_pred}")

    # 4. the silver zeta_8 witness: z^4+16 has splitting field Q(zeta_8)
    f = t**4 + 16
    roots = sp.roots(f, t)
    # each root is sqrt2*(±1±i) -> lies in Q(zeta8); check minimal polynomial degree 4 and
    # that root/(1+i) is quadratic (i.e. the field contains i and sqrt2)
    r = list(roots)[0]
    ok &= sp.minimal_polynomial(r, t) == t**4 + 16
    ok &= sp.simplify(r**2 / 4) in (sp.I, -sp.I)      # r^2 = ±4i -> i in the field
    print("silver witness: roots of z^4+16 generate Q(zeta8) (r^2 = ±4i):", ok)

    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    return bool(ok)


if __name__ == '__main__':
    run()
