#!/usr/bin/env python3
"""
Appendix B -- verification of "the plane is a fixed algebra" (paper Prop. "twoO"
and its corollary on the Z/2 grading).

Self-contained: needs only sympy.  Imports NOTHING project-internal, so it travels
with the paper.  Exact arithmetic throughout -- characters are computed by an
integer/quadratic-irrational recurrence, never by evaluating a trigonometric
function numerically.

The claim: the plane the cascade is measured on is not a choice.

    N_{SU(2)}(2T) = 2O   and   2O/2T = Z/2,

so 2T admits exactly ONE outer involution, Ad(w) for w in 2O minus 2T.  Its
eigenvalues on the four charge lines are (+1,-1,+1,-1) on degrees (8,14,16,22), so
e6^{2O} = <x_8, x_16> is precisely the measurement plane.

Method.  For g in SU(2) with trace tau, the character of Sym^n C^2 is the Chebyshev
value chi_n(tau) obeying chi_n = tau*chi_{n-1} - chi_{n-2}, chi_0 = 1, chi_1 = tau.
So dim (Sym^n)^G = (1/|G|) sum_g chi_n(tau_g), an exact computation from the trace
multiset alone.  For 2T the traces are {2,-2,0,1,-1}; 2O adds {sqrt2, -sqrt2}.

The self-normalizing claim needs no construction of 2I:
    N_{2I}(2T) = 2I intersect N_{SU(2)}(2T) = 2I intersect 2O,
which is a subgroup of 2O containing 2T (index 2).  It is 2T or 2O; it cannot be 2O
because 48 does not divide 120.  Hence it is 2T.

Run:  python3 check_measurement_plane.py        (exit 0 = all PASS)
"""

import itertools
import sys

import sympy as sp

FAILURES = []

# The principal-sl2 exponent degrees of e6: 2m for m in {1,4,5,7,8,11}.
EXPONENT_DEGREES = (2, 8, 10, 14, 16, 22)


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def quaternion_traces_2T():
    """Traces of the 24 Hurwitz units, as exact numbers (trace = 2*real part)."""
    reals = []
    for s in (1, -1):
        reals += [s, 0, 0, 0]                       # +-1, +-i, +-j, +-k
    for sg in itertools.product((1, -1), repeat=4):
        reals.append(sp.Rational(sg[0], 2))         # (+-1 +-i +-j +-k)/2
    return [2 * r for r in reals]


def quaternion_traces_2O_extra():
    """Traces of the 24 units (e_a +- e_b)/sqrt2, a < b."""
    out = []
    r2 = 1 / sp.sqrt(2)
    for a in range(4):
        for b in range(a + 1, 4):
            for sa in (1, -1):
                for sb in (1, -1):
                    real = (sa * r2) if a == 0 else 0   # only e_0 contributes a real part
                    out.append(2 * real)
    return out


def sym_character(n, tau):
    """chi_n(tau) = character of Sym^n C^2 at an element of trace tau, exactly."""
    prev, cur = sp.Integer(1), sp.sympify(tau)
    if n == 0:
        return prev
    for _ in range(n - 1):
        prev, cur = cur, sp.expand(sp.sympify(tau) * cur - prev)
    return sp.simplify(cur)


def invariant_dim(traces, n):
    total = sum(sym_character(n, t) for t in traces)
    val = sp.simplify(sp.Rational(1, len(traces)) * total)
    val = sp.nsimplify(sp.radsimp(val))
    assert val.is_Integer, f"non-integer invariant dimension {val} at n={n}"
    return int(val)


def main():
    print("=" * 70)
    print("Appendix B -- the measurement plane is the 2O fixed algebra")
    print("=" * 70)

    T_2T = quaternion_traces_2T()
    T_2O = T_2T + quaternion_traces_2O_extra()

    print("\n1. the groups and their trace multisets")
    check("|2T| = 24", len(T_2T), 24)
    check("|2O| = 48", len(T_2O), 48)
    check("2T traces lie in {2,-2,0,1,-1}",
          sorted({sp.nsimplify(t) for t in T_2T}, key=lambda z: float(z)),
          [sp.Integer(-2), sp.Integer(-1), sp.Integer(0),
           sp.Integer(1), sp.Integer(2)])
    extra = {sp.simplify(t) for t in quaternion_traces_2O_extra()}
    check("2O adds traces {sqrt2, 0, -sqrt2}",
          sorted(extra, key=lambda z: float(z)),
          sorted({-sp.sqrt(2), sp.Integer(0), sp.sqrt(2)}, key=lambda z: float(z)))

    print("\n2. the charge algebra C = e6^{2T} is four-dimensional")
    dims_2T = {n: invariant_dim(T_2T, n) for n in EXPONENT_DEGREES}
    check("dim (Sym^n)^{2T} over the exponent degrees",
          dims_2T, {2: 0, 8: 1, 10: 0, 14: 1, 16: 1, 22: 1})
    check("dim C = 4", sum(dims_2T.values()), 4)
    check("the charge degrees are 8, 14, 16, 22",
          [n for n, d in dims_2T.items() if d == 1], [8, 14, 16, 22])

    print("\n3. the 2O fixed algebra IS the measurement plane")
    dims_2O = {n: invariant_dim(T_2O, n) for n in EXPONENT_DEGREES}
    check("dim (Sym^n)^{2O} over the exponent degrees",
          dims_2O, {2: 0, 8: 1, 10: 0, 14: 0, 16: 1, 22: 0})
    check("dim e6^{2O} = 2", sum(dims_2O.values()), 2)
    check("e6^{2O} = <x_8, x_16>",
          [n for n, d in dims_2O.items() if d == 1], [8, 16])

    print("\n4. the outer involution and its eigenvalues")
    eig = {n: (1 if dims_2O[n] == 1 else -1) for n in (8, 14, 16, 22)}
    check("Ad(w) eigenvalues on degrees (8,14,16,22)",
          [eig[n] for n in (8, 14, 16, 22)], [1, -1, 1, -1])
    check("C_0 = <x_8, x_16>", sorted(n for n in eig if eig[n] == 1), [8, 16])
    check("C_1 = <x_14, x_22>", sorted(n for n in eig if eig[n] == -1), [14, 22])
    print("          (each invariant space is a LINE, so Ad(w) acts on it by a")
    print("           scalar; w^2 in 2T forces that scalar to be +-1, and it is")
    print("           +1 exactly when the line survives to 2O.)")

    print("\n5. uniqueness of the involution, without constructing 2I")
    check("2T has index 2 in 2O", len(T_2O) // len(T_2T), 2)
    check("48 does not divide 120, so 2O is not inside 2I", 120 % 48, 24)
    print("          N_{2I}(2T) = 2I ^ N_{SU(2)}(2T) = 2I ^ 2O is a subgroup of 2O")
    print("          containing 2T with index 2; it cannot be 2O, so it is 2T.")
    print("          Hence 2T is SELF-NORMALIZING in 2I: no competing involution.")

    print("-" * 70)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: the measurement plane reproduces as e6^{2O} exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
