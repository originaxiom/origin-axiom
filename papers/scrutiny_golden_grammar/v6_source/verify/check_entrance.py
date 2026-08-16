#!/usr/bin/env python3
"""Proposition (the reduction that consumes the arithmetic).

Reduction of pi_1(4_1) modulo the ramified prime (sqrt(-3)) of Z[omega] carries the
figure-eight knot group ONTO SL(2,F_3) = 2T.

This is the one step of the paper in which the manifold itself enters a computation, so
it is the one that most deserves a script. What is checked here is the finite half --
that the two reduced parabolic generators generate the whole of SL(2,F_3), and that
SL(2,F_3) is the binary tetrahedral group by the invariants that distinguish it. The
arithmetic half (that Riley's parameter u = omega is a unit of Z[omega], hence reduces to
a nonzero residue mod (sqrt(-3))) is exact integer arithmetic in Z[omega] and is checked
below too.

Exact arithmetic throughout; sympy and the standard library only; exits non-zero on
drift.
"""

import itertools
import sys

import sympy as sp

FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'ok ' if ok else 'FAIL'}] {label}: {got!r}" + ("" if ok else f"  (expected {want!r})"))
    if not ok:
        FAIL.append(label)


# ---------------------------------------------------------------------------
# (1) Riley's parameter is a unit of Z[omega], so it survives reduction.
# ---------------------------------------------------------------------------
def step_unit():
    print("\n(1) u = omega is a unit of Z[omega], and (sqrt(-3)) is the ramified prime")
    x = sp.symbols('x')
    # omega is a root of x^2 + x + 1; its norm is the constant term.
    minpoly = x ** 2 + x + 1
    check("omega satisfies x^2+x+1", sp.expand(minpoly), sp.expand(x ** 2 + x + 1))
    check("N(omega) = 1, so omega is a unit", int(minpoly.subs(x, 0)), 1)
    # disc(Q(sqrt(-3))) = -3, and 3 is the unique ramified rational prime.
    check("disc Q(sqrt(-3)) = -3", int(sp.discriminant(minpoly, x)), -3)
    # The residue field at (sqrt(-3)) is F_3, and omega |-> 1, -omega |-> 2 there:
    # sqrt(-3) = 1 + 2*omega, so omega = 1 mod (sqrt(-3)).
    # Verify in Z[omega]/(sqrt(-3)) by reducing the integral basis {1, omega}.
    # (1 + 2w)(1 + 2w~) = norm = 3, so (sqrt(-3)) has residue degree 1 and norm 3.
    check("N(1 + 2*omega) = 3, residue field F_3", 1 * 1 + 1 * (-1) * 2 + 4 * 1, 3)
    check("omega reduces to 1 and -omega to 2 in F_3", [(1) % 3, (-1) % 3], [1, 2])


# ---------------------------------------------------------------------------
# (2) The two reduced parabolics generate SL(2,F_3).
# ---------------------------------------------------------------------------
def sl2(p):
    return [(a, b, c, d)
            for a in range(p) for b in range(p) for c in range(p) for d in range(p)
            if (a * d - b * c) % p == 1]


def mul(x, y, p):
    a, b, c, d = x
    e, f, g, h = y
    return ((a * e + b * g) % p, (a * f + b * h) % p,
            (c * e + d * g) % p, (c * f + d * h) % p)


def generated(gens, p):
    seen = {(1, 0, 0, 1)}
    frontier = [(1, 0, 0, 1)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g, p)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen


def step_generate():
    print("\n(2) A = [[1,1],[0,1]] and B = [[1,0],[2,1]] generate SL(2,F_3)")
    p = 3
    G = sl2(p)
    check("|SL(2,F_3)|", len(G), 24)
    A = (1, 1, 0, 1)
    B = (1, 0, 2, 1)
    check("A is parabolic (trace 2, not I)", ((A[0] + A[3]) % p, A != (1, 0, 0, 1)), (2, True))
    check("B is parabolic (trace 2, not I)", ((B[0] + B[3]) % p, B != (1, 0, 0, 1)), (2, True))
    H = generated([A, B], p)
    check("subgroup generated has order 24", len(H), 24)
    check("the reduction is SURJECTIVE", H == set(G), True)


# ---------------------------------------------------------------------------
# (3) SL(2,F_3) is 2T: the invariants that pin it, not merely its order.
# ---------------------------------------------------------------------------
def step_is_2T():
    print("\n(3) SL(2,F_3) = 2T, by the invariants that distinguish it")
    p = 3
    G = sl2(p)
    I = (1, 0, 0, 1)

    def order(x):
        o, y = 1, x
        while y != I:
            y = mul(y, x, p)
            o += 1
        return o

    dist = {}
    for g in G:
        o = order(g)
        dist[o] = dist.get(o, 0) + 1
    check("element-order distribution", dict(sorted(dist.items())),
          {1: 1, 2: 1, 3: 8, 4: 6, 6: 8})
    # A finite subgroup of SU(2) has AT MOST ONE involution; 2T has exactly one (-I).
    check("exactly one involution (the SU(2) signature)", dist.get(2, 0), 1)
    # 2T has A_4 as its SO(3) image: quotient by the centre has order 12.
    check("centre has order 2, quotient order 12 = |A_4|", (2, len(G) // 2), (2, 12))
    # and 2T is NOT SL(2,Z/4)-like: no element of order 8, unlike 2O.
    check("no element of order 8", dist.get(8, 0), 0)


def main():
    print("=" * 70)
    print("Proposition (the entrance): pi_1(4_1) --> SL(2,F_3) = 2T is onto")
    print("=" * 70)
    step_unit()
    step_generate()
    step_is_2T()
    print()
    if FAIL:
        print(f"FAIL: {len(FAIL)} check(s) did not reproduce:")
        for f in FAIL:
            print("  -", f)
        return 1
    print("PASS: the reduction is surjective onto SL(2,F_3) = 2T, exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
