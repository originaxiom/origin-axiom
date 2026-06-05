"""B69 (P3) -- the m=2 metallic A-polynomial from the trace map, in the B67 framing (resolves the
"m!=1 framing does not transfer" open door).

REPO_STATE open door 2 flagged: for the m=2 bundle (mapping torus of phi_2^2, monodromy [[5,2],[2,1]]
= census m136) the B67 (figure-eight) trace-map framing "does not transfer (best framing residual
~6e-3)". That ~6e-3 was the BUGGY SnapPy gluing-equation SHAPE route (V37, discarded), NOT the
trace-map elimination. With the genuine meridian clarified (V46: for SL(2) eig(mu)=eig(t), so the bare
monodromy generator and the genuine peripheral meridian mu=w^-1 t share eigenvalues -- the trace
framing already uses the correct meridian spectrum), the B67 elimination transfers EXACTLY.

From B69's T_2^2 fixed locus:
   tr(t)^2 = x^4/(x^2-2)                          (meridian: P = tr(t) = M + 1/M)
   kappa   = tr[a,b] = (x^4-6x^2+12)/(x^2-2)      (longitude: S = kappa = L + 1/L)
Eliminating x:
   resultant = 16 (P^2 - S - 6)^4   =>   the meridian<->longitude TRACE IDENTITY  kappa = tr(t)^2 - 6
   (the m=2 analogue of B67's figure-eight identity kappa = tr(t)^4 - 5 tr(t)^2 + 2),
and in eigenvalue coordinates the squarefree eliminant is EXACTLY the established m136 A-polynomial
   A(M,L) = M^2 L^2 - (M^4 - 4 M^2 + 1) L + M^2     (V32/V38),
the same census-m136 invariant recovered independently in V38. So the trace-map framing DOES transfer
to m=2; the open door is resolved.

Standalone low-dim topology; no physics, no Origin claim. Proven core P1-P16 untouched.
"""
import sympy as sp

x, P, S, M, L = sp.symbols("x P S M L")

# B69 T_2^2 fixed-locus data
TR_T_SQ = x**4 / (x**2 - 2)                    # tr(t)^2
KAPPA = (x**4 - 6 * x**2 + 12) / (x**2 - 2)    # tr[a,b]
A_M136 = M**2 * L**2 - (M**4 - 4 * M**2 + 1) * L + M**2


def trace_identity():
    """The meridian<->longitude trace identity from eliminating x: returns (resultant, kappa - (P^2-6))."""
    e1 = P**2 * (x**2 - 2) - x**4
    e2 = S * (x**2 - 2) - (x**4 - 6 * x**2 + 12)
    res = sp.factor(sp.resultant(e1, e2, x))
    # the identity kappa = tr(t)^2 - 6  (i.e. S = P^2 - 6):
    check = sp.simplify(KAPPA - (TR_T_SQ - 6))
    return res, check


def derived_apolynomial():
    """The squarefree (M,L) eliminant of the m=2 trace-map framing."""
    e1 = P**2 * (x**2 - 2) - x**4
    e2 = S * (x**2 - 2) - (x**4 - 6 * x**2 + 12)
    F = sp.resultant(e1, e2, x)
    num, _ = sp.fraction(sp.together(F.subs({P: (M**2 + 1) / M, S: (L**2 + 1) / L})))
    _, factors = sp.factor_list(sp.expand(num))
    return sp.expand(sp.prod([f for f, _m in factors]))


def main():
    print("B69 (P3) -- m=2 metallic A-polynomial from the trace map (B67 framing)\n")
    res, check = trace_identity()
    print(f"  resultant(eliminate x) = {res}")
    print(f"  => trace identity  kappa = tr(t)^2 - 6   (residual {check})")
    derived = derived_apolynomial()
    print(f"\n  derived A(M,L) = {derived}")
    print(f"  m136 A-poly    = {sp.expand(A_M136)}")
    print(f"  derived / m136 = {sp.simplify(sp.cancel(derived / A_M136))}  (unit => EXACT match)")
    print("\n  => the B67 trace-map framing TRANSFERS to m=2: exact m136 A-polynomial. Open door resolved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
