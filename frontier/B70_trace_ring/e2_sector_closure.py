"""B70 -- SL(4) e_2-sector: two-index content of tr(A^a B A^b B), GENERIC tangent (see CORRECTION).

CORRECTION (2026-06-04): this script uses the GENERIC traceless tangent A=(I+eps X)^a (X generic).
That object's two-index (a,b)-content GROWS UNBOUNDED with eps-order -- the max single-index degree
equals the eps-order (1,2,3,...,7 by eps^8), as the table below already hints and a longer run
confirms. So this script does NOT demonstrate a (3,3) bound; the lone "(3,3)" printed at eps^6 is one
monomial among a growing set, not a cap. The fixed-line / e_2-sector object is the UNIPOTENT one
(c=n => A unipotent, (A-I)^n=0), on which A^a = sum_{j<n} C(a,j) N^j has a-degree <= n-1=3, so
tr(A^a B A^b B) has bidegree <= (3,3) (one line from the c=n nilpotency). The CORRECT computation is
in e2_unipotent_bound.py (bidegree exactly (3,3), tight for a full-index nilpotent). This file is kept
as the generic-tangent contrast (it shows the eps-series growth, which is real but is NOT the closure
object). The leading-order (eps^2) rank-1 result of two_block_rank1.py is on the proper traceless
sl(n) tangent and is unaffected.

Method: keep (a,b,eps) symbolic, use NUMERICAL traceless rational X,Y (fast matrix powers; the full
symbolic 4x4 expansion to high eps-order is intractable).

VERDICT (generic tangent): the two-index content GROWS with eps-order -- (1,1) at eps^2, (2,1) at
eps^3, (3,1)/(2,2) at eps^4, ... unbounded. This is the WRONG object for the bound; see
e2_unipotent_bound.py for the correct (3,3) cap on the unipotent fixed-line object.
"""
import random
import sympy as sp

a, b, eps = sp.symbols("a b epsilon")
n, L = 4, 6
random.seed(1)


def rmat():
    M = sp.Matrix(n, n, lambda i, j: sp.Rational(random.randint(-3, 3)))
    return M - sp.eye(n) * sp.trace(M) / n


X, Y, I = rmat(), rmat(), sp.eye(n)


def Apow(p, Mx):                                  # (I + eps Mx)^p to O(eps^L)
    M = I; Xk = I
    for k in range(1, L + 1):
        Xk = Xk * Mx
        c = sp.prod([p - i for i in range(k)]) / sp.factorial(k)
        M = M + c * eps**k * Xk
    return M


S = sp.expand(sp.trace(sp.expand(Apow(a, X) * (I + eps * Y) * Apow(b, X) * (I + eps * Y))))
print("tr(A^a B A^b B), traceless X,Y: non-separable two-index bidegree per eps-order")
for p in range(2, L + 1):
    c = sp.expand(S.coeff(eps, p))
    ns = sp.expand(c - c.subs(a, 0) - c.subs(b, 0) + c.subs({a: 0, b: 0}))
    if ns == 0:
        print(f"  eps^{p}: separable"); continue
    two = sorted(m for m, _ in sp.Poly(ns, a, b).terms() if m[0] >= 1 and m[1] >= 1)
    print(f"  eps^{p}: two-index monomials {two}, max bidegree {max(two)}")
print("\nVERDICT (generic tangent): rank-1 only at eps^2; the two-index content GROWS UNBOUNDED with")
print("eps-order (max single-index degree = eps-order). This is the WRONG object for the closure bound.")
print("The (3,3) cap is a property of the UNIPOTENT fixed-line object (A^a = sum_{j<n} C(a,j) N^j,")
print("a-degree <= n-1=3) -- see e2_unipotent_bound.py (bidegree exactly (3,3)).")
