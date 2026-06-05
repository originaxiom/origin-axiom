"""B93 (Paper 0, Phase C) -- the bridge: det=-1 is exactly what gives the tower its parity.

Neutral mathematics; the motivation is quarantined elsewhere and unused here.

The Layer-1 classification (B92) singles out the metallic family by det = -1. This stage shows det = -1
is not merely "the simplest slice" but is STRUCTURALLY DISTINGUISHED: it is exactly the condition that
gives the trace-map tower its sign/parity sectors. Two results.

MyCalc-1 (det=-1 <=> the parity sectors). For a hyperbolic unimodular 2x2 N:
  * det N = -1  <=>  eigenvalues are lambda > 1 and -1/lambda in (-1,0) (the small one NEGATIVE);
  * det N = +1  <=>  both eigenvalues positive (lambda > 1 and 1/lambda in (0,1)).
The Dickson catalog factor is char(sign*N^k) = t^2 - sign*tr(N^k) t + det(N)^k. The sign/parity sector
char(-N^k) is the m -> -m image of char(N^k) under the contragredient, governed by the Dickson parity
tr(N^k)|_{m->-m} = (-1)^k tr(N^k), which holds for the det=-1 companion M_m=[[m,1],[1,0]]. For det N=+1
both eigenvalues are positive, det(N)^k = +1 for all k, and there is NO negative-rooted char(-N^k) sector
(verified at the Jacobian level in B94: squaring the det=-1 tower to det=+1 removes every char(-N^k) and
the (t+1) factor). So the tower's two-sheeted (CPT) structure is a det = -1 phenomenon.

MyCalc-4 (Galois vs parity -- a clarification refining the handoff's "Galois = C"). The metallic
eigenvalues lie in the real quadratic field Q(sqrt(m^2+4)). There are TWO distinct Z/2 involutions, and
they are NOT the same:
  * the PARITY / contragredient P:  m -> -m  (the diagram automorphism -w0; B62/B64). It sends
    char(M^k) -> char((-1)^k M^k), i.e. permutes char(M^k) <-> char(-M^k) for odd k (Dickson parity
    L_k(-m) = (-1)^k L_k). This is the tower's parity split.
  * the GALOIS involution g of Q(sqrt(m^2+4))/Q:  sqrt(m^2+4) -> -sqrt(m^2+4), i.e. lambda <-> -1/lambda.
    It FIXES every L_k = lambda^k + (-1/lambda)^k (symmetric in the two roots), so it does NOT permute the
    char(M^k) factors -- it swaps the two ROOTS WITHIN each char(M^k) (the meridian eigenvalue pair).
So the parity/CPT is the contragredient m->-m, NOT the field Galois action; the Galois action is the
within-factor (charge-conjugation-of-the-eigenvalue) swap. Both are Z/2; they are distinct. (Handoff
Idea-4 conflated them; this is the honest correction.)

Standalone number theory / Lie theory; no physics, no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sympy as sp

t, m = sp.symbols("t m")


def char_Nk(N, k, sign=1):
    """char(sign*N^k) = t^2 - sign*tr(N^k) t + det(N)^k -- the Dickson catalog for ANY 2x2 N."""
    N = sp.Matrix(N)
    Nk = N**k if k >= 0 else N.inv() ** (-k)
    return sp.expand(t**2 - sign * sp.trace(Nk) * t + sp.det(N) ** k)


def eigenvalue_signs(N):
    """(det, [eigenvalues]) -- det=-1 gives one negative eigenvalue, det=+1 both positive."""
    N = sp.Matrix(N)
    evs = sorted([sp.nsimplify(sp.re(sp.N(e))) for e in N.eigenvals()])
    return int(N.det()), [float(e) for e in evs]


def mycalc1_det_iff_parity(Ns):
    """For each N: (det, eigenvalue signs, has-negative-eigenvalue == (det==-1))."""
    out = {}
    for name, N in Ns.items():
        det, evs = eigenvalue_signs(N)
        has_neg = any(e < 0 for e in evs)
        out[name] = (det, evs, has_neg, has_neg == (det == -1))
    return out


def parity_action_on_Lk(kmax=4):
    """Parity P (m->-m): L_k(-m) = (-1)^k L_k  -- so P swaps char(M^k)<->char(-M^k) for odd k."""
    M = sp.Matrix([[m, 1], [1, 0]])
    res = {}
    for k in range(1, kmax + 1):
        Lk = sp.expand(sp.trace(M**k))
        res[k] = sp.expand(Lk.subs(m, -m) - (-1) ** k * Lk) == 0
    return res


def galois_fixes_Lk(kmax=4):
    """Galois g (sqrt->-sqrt, lambda<->-1/lambda): FIXES every L_k -> g != parity (within-factor swap)."""
    lam = (m + sp.sqrt(m**2 + 4)) / 2
    sig = (m - sp.sqrt(m**2 + 4)) / 2
    res = {}
    for k in range(1, kmax + 1):
        Lk = sp.expand(lam**k + sig**k)
        g = Lk.subs(sp.sqrt(m**2 + 4), -sp.sqrt(m**2 + 4))
        res[k] = sp.simplify(g - Lk) == 0
    return res


def main():
    print("B93 (Paper 0, Phase C) -- det=-1 is exactly the tower's parity condition\n")
    print("MyCalc-1: det sign <-> eigenvalue sign <-> parity sectors")
    Ns = {"M_1 (det=-1)": [[1, 1], [1, 0]], "M_2 (det=-1)": [[2, 1], [1, 0]],
          "M_1^2=[[2,1],[1,1]] (det=+1)": [[2, 1], [1, 1]], "[[3,2],[1,1]] (det=+1)": [[3, 2], [1, 1]]}
    for name, (det, evs, has_neg, ok) in mycalc1_det_iff_parity(Ns).items():
        tag = "one NEGATIVE -> char(-N^k) sectors" if has_neg else "both POSITIVE -> NO sign sectors"
        print(f"  {name}: eig={evs} -> {tag}   [det=-1 <=> neg: {ok}]")
    print("\nMyCalc-4: parity (m->-m) vs Galois (sqrt->-sqrt) -- distinct Z/2 involutions")
    par = parity_action_on_Lk()
    gal = galois_fixes_Lk()
    print(f"  parity P: L_k(-m)=(-1)^k L_k for k=1..4 ? {all(par.values())}  (permutes char(M^k)<->char(-M^k), odd k)")
    print(f"  Galois g: fixes every L_k for k=1..4 ? {all(gal.values())}  (swaps the 2 roots WITHIN char(M^k))")
    print("  => parity != Galois: the CPT/parity is the contragredient m->-m, NOT the field Galois action.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
