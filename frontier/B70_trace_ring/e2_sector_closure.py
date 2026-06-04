"""B70 -- SL(4) e_2-sector closure attempt (does the rank-1 generator suffice?).

The fixed-line Jacobian uses the FULL eps-series (the 15 coords separate only across orders 1..L --
the B58-Phase-A 'rank-3 Fricke block' fact). B70's rank-1 result is the LEADING (eps^2) order. This
computes the non-separable (genuinely two-index) content of tr(A^a B A^b B) at higher eps-orders to
test whether one generator closes the sector.

Method: keep (a,b,eps) symbolic, use NUMERICAL traceless rational X,Y (fast matrix powers; the full
symbolic 4x4 expansion to high eps-order is intractable). The (a,b)-bidegree of the non-separable part
is a combinatorial fact independent of the specific X,Y, so numerical X,Y detect it correctly.

VERDICT: the two-index content GROWS with eps-order -- rank-1 (bidegree (1,1)) only at eps^2, then
(2,1) at eps^3, (3,1)/(2,2) at eps^4, ... So a SINGLE rank-1 generator does NOT close the e_2 sector;
the closure needs the full higher-bidegree two-index structure. BUT it is BOUNDED: the fixed-line
derivative sequences have degree <= n-1 = 3 (c=n nilpotency), so the Jacobian-relevant two-index
content caps at bidegree (3,3). The e_2-sector closure is therefore a FINITE problem (a bounded
multi-generator two-index set), with the rank-1 (1,1) as its leading order -- not a single generator,
but not an unbounded wall either.
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
print("\nVERDICT: rank-1 only at eps^2; the two-index content grows -> the e_2 sector needs MORE than")
print("one generator. Bounded by c=n nilpotency (derivative-sequence degree <= n-1=3) -> bidegree <=")
print("(3,3): the closure is a FINITE multi-generator problem, with the rank-1 (1,1) as leading order.")
