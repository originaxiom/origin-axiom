"""B70 -- the e_2-sector two-block (a,b)-bound, on the CORRECT (unipotent) fixed-line object.

Correction to e2_sector_closure.py.  That script measured the two-index (a,b)-content of the
two-block word tr(A^a B A^b B) using the GENERIC traceless tangent A=(I+eps X)^a (X generic). That
object's content GROWS UNBOUNDED with eps-order (max single-index degree = eps-order: 1,2,3,...,7 by
eps^8) -- so it does NOT demonstrate the (3,3) bound; the lone "(3,3)" it printed at eps^6 was one
monomial among a growing set, not a cap.

The CORRECT object is the c=n fixed line, where every trace equals n, i.e. A is UNIPOTENT with
(A - I)^n = 0.  Then
        A^a = (I + N)^a = sum_{j=0}^{n-1} C(a,j) N^j      (exact, since N^n = 0),
which is a polynomial of degree <= n-1 in a.  Hence tr(A^a B A^b B) has bidegree <= (n-1, n-1) in
(a,b) -- for n=4, <= (3,3) -- a one-line consequence of the c=n nilpotency (the proven B58_sl4 fact
that fixed-line derivative sequences are degree <= n-1 in word-length, here applied per index).

This script verifies it directly: with A = I + N_A (upper-nilpotent of index n) and B = I + N_B
(lower-nilpotent, so the word is NOT triangular and tr genuinely depends on a,b), the bidegree of
tr(A^a B A^b B) is exactly (n-1, n-1) = (3,3) for a generic full-index nilpotent (and less for a
lower-index N_A).  So the two-block / e_2-sector content is a BOUNDED, finite (bidegree <= (3,3))
object -- the V42 conclusion, now on the right object.  (A strictly-triangular A AND B would make the
whole word triangular with unit diagonal, tr == n, bidegree (0,0): the degenerate case to avoid.)

Standalone Lie/invariant theory; no physics claim.  Proven core P1-P16 untouched.
"""
import random

import sympy as sp

a, b = sp.symbols("a b")
n = 4


def binom(p, k):
    return sp.prod([p - i for i in range(k)]) / sp.factorial(k)


def nilpotent(seed, lower=False):
    """strictly-triangular n x n (upper, or lower if lower=True): nilpotent of index <= n."""
    random.seed(seed)
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if (j > i and not lower) or (j < i and lower):
                M[i, j] = sp.Integer(random.randint(-3, 3))
    return M


def unipotent_pow(p, N):
    """(I+N)^p = sum_{j=0}^{n-1} C(p,j) N^j, exact since N^n = 0."""
    out, Nj = sp.eye(n), sp.eye(n)
    for j in range(1, n):
        Nj = Nj * N
        out = out + binom(p, j) * Nj
    return out


def nil_index(N):
    return next(k for k in range(1, n + 1) if (N**k) == sp.zeros(n, n))


def bidegree(seedA, seedB):
    NA, NB = nilpotent(seedA, lower=False), nilpotent(seedB, lower=True)
    W = sp.expand(sp.trace(sp.expand(unipotent_pow(a, NA) * (sp.eye(n) + NB)
                                     * unipotent_pow(b, NA) * (sp.eye(n) + NB))))
    nonsep = sp.expand(W - W.subs(a, 0) - W.subs(b, 0) + W.subs({a: 0, b: 0}))
    monos = [m for m, _ in sp.Poly(nonsep, a, b).terms() if m[0] >= 1 and m[1] >= 1] if nonsep != 0 else []
    return (sp.degree(W, a), sp.degree(W, b)), (max(monos) if monos else None), nil_index(NA)


def main():
    print("B70 -- e_2-sector two-block bound on the UNIPOTENT fixed-line object (A unipotent, (A-I)^n=0)\n")
    print(f"n={n}: A^a = sum_(j=0)^({n-1}) C(a,j) N^j  =>  tr(A^a B A^b B) bidegree <= ({n-1},{n-1})")
    for seedA, seedB in [(1, 2), (5, 7), (11, 13), (4, 9)]:
        (da, db), nsmax, idx = bidegree(seedA, seedB)
        cap = "<= (3,3) OK" if da <= n - 1 and db <= n - 1 else "EXCEEDS (3,3)!"
        print(f"  N_A index {idx}: bidegree ({da},{db}); non-separable max monomial {nsmax}   [{cap}]")
    print("\n-> the two-block / e_2-sector content is BOUNDED at bidegree (3,3) (tight for full-index N_A),")
    print("   a one-line consequence of the c=n unipotency -- NOT the generic-X eps-series of")
    print("   e2_sector_closure.py (which grows unbounded; see its corrected note).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
