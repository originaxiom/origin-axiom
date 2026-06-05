"""B94 §1b -- the n=2 actual-Jacobian cross-check for a genuine NON-square monodromy.

The B94 squaring device only reaches det=+1 monodromies of the form N=M^2 (metallic squares). This probe
checks the ACTUAL SL(2) trace-map Jacobian (not the Sym-product proxy) for a genuine NON-square,
non-metallic monodromy [[3,2],[1,1]] (det=+1, period-2 CF, NOT a metallic power), at the n=2 level.

Build the trace map of a free-group automorphism with the target abelianization by composing Nielsen
generators on the Fricke coordinates (x,y,z)=(tr A, tr B, tr AB):
    alpha  (a->ab, b->b) : (x,y,z) -> (z, y, y z - x)
    beta   (a->a, b->ba) : (x,y,z) -> (x, z, x z - y)
Take the Jacobian at the trivial point (2,2,2) and factor. Compare to
    char(Sym^2 N) = (s^2 - (tr^2 - 2 det) s + det^2)(s - det)   [eigenvalues lam^2, mu^2, lam*mu].

Result (computer-assisted, n=2):
    metallic  [[1,1],[1,0]] (det -1) -> (s+1)(s^2 - 3 s + 1)    [HAS the (s+1) sign marker]
    square    [[2,1],[1,1]] (det +1) -> (s-1)(s^2 - 7 s + 1)    [no (s+1)]
    NONsquare [[3,2],[1,1]] (det +1) -> (s-1)(s^2 - 14 s + 1)   [no (s+1)] = char(Sym^2 N)
So the catalog factor char(Sym^2 N) appears at the actual-Jacobian level for a genuine non-square, with
the parity marker (s - det N): (s+1) iff det = -1. This upgrades B94's "covered structurally by MyCalc-1"
to "confirmed at the actual-Jacobian level at n=2 for a genuine non-square." Still open: char(-N^k) sign
sectors for non-metallic N at n>=3.  Standalone; no physics; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sympy as sp

x, y, z, s = sp.symbols("x y z s")

# Nielsen-generator trace maps on (x,y,z) = (tr A, tr B, tr AB)
Ta = lambda v: (v[2], v[1], v[1] * v[2] - v[0])        # alpha: a->ab, b->b
Tb = lambda v: (v[0], v[2], v[0] * v[2] - v[1])        # beta:  a->a,  b->ba


def compose(gens):
    """phi = g1 o g2 o ... ; apply the trace maps T_g1, T_g2, ... in order."""
    v = (x, y, z)
    for g in gens:
        v = g(v)
    return [sp.expand(c) for c in v]


def charpoly_at_triv(f):
    """char poly (in s) of the trace-map Jacobian at the trivial point (2,2,2)."""
    J = sp.Matrix([[sp.diff(fi, u) for u in (x, y, z)] for fi in f]).subs({x: 2, y: 2, z: 2})
    return sp.factor(J.charpoly(s).as_expr())


def sym2(N):
    """char(Sym^2 N) = (s^2 - (tr^2 - 2 det) s + det^2)(s - det)."""
    N = sp.Matrix(N)
    tr, dt = N.trace(), N.det()
    return sp.factor((s**2 - (tr**2 - 2 * dt) * s + dt**2) * (s - dt))


CASES = {
    "metallic [[1,1],[1,0]] det -1": ([z, x, x * z - y], [[1, 1], [1, 0]]),   # a->ab, b->a direct
    "square   [[2,1],[1,1]] det +1": (compose([Tb, Ta]), [[2, 1], [1, 1]]),   # beta o alpha
    "NONsquare[[3,2],[1,1]] det +1": (compose([Tb, Tb, Ta]), [[3, 2], [1, 1]]),  # beta o beta o alpha
}


def main():
    print("B94 §1b -- the n=2 actual-Jacobian check for a genuine NON-square monodromy\n")
    for name, (T, N) in CASES.items():
        got, want = charpoly_at_triv(T), sym2(N)
        print(f"  {name}:  J = {got}   Sym^2 = {want}   match = {sp.simplify(got - want) == 0}")
    print("\n=> the catalog factor char(Sym^2 N) appears at the actual-Jacobian level even for a genuine")
    print("   non-square; parity marker (s - det N) = (s+1) iff det = -1. computer-assisted (n=2).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
