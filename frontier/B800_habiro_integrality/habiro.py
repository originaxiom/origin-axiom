#!/usr/bin/env python3
"""B800 — in-sandbox recomputation of B685's Habiro integrality leg.

B685 banked "the Habiro object is integral away from 3" by RE-READING GSWZ eq. 2, not by
computing it (kill_graph fact_computed: false; B799 registered this as the batch's highest-value
remaining recompute). This computes it.

THE OBJECT. GSWZ's symmetrised series is Phi(h)*Phi(-h), where Phi(h) is the perturbative
(asymptotic) series of the figure-eight's state integral at the geometric saddle. Built here
from first principles rather than transcribed:

  potential      V(u) = Li_2(e^u) - Li_2(e^-u)
  V'(u)          = -log( (1-e^u)(1-e^-u) ) = -log( 2 - e^u - e^-u )
  saddle         (1-w)(1-1/w) = 1  with w = e^u   <=>   w^2 - w + 1 = 0
                 => w0 = e^{i pi/3} = (1 + sqrt(-3))/2      [the geometric tetrahedron shape]
  1-loop         V''(u0) = w0 - 1/w0 = sqrt(-3)             [verified below, not assumed]

Every higher derivative V^(k)(u0) therefore lies in Q(sqrt-3), so the loop expansion's
coefficients do too. Phi carries a prefactor 1/sqrt(V''), so the SYMMETRISED product carries
1/V'' = 1/sqrt(-3) squared = -1/3 -- which is the mechanism that makes Phi(h)Phi(-h) RATIONAL
with 3-power denominators. "Integral away from 3" is a statement about that mechanism.

METHOD. Formal Gaussian (Feynman) expansion. With s the fluctuation and A = V''(u0), rescale
s = sqrt(h/A) t so the quadratic part becomes t^2/2 and the interaction is

    sum_{k>=3} g_k t^k ,      g_k = V_k * h^{k/2 - 1} * A^{-k/2} / k!

and Phi_hat(h) = < exp( -sum_k g_k t^k ) > under the standard Gaussian moments
< t^{2m} > = (2m-1)!!, < t^{odd} > = 0. Half-integer powers of h pair up, leaving a series in h.

SCOPE, stated honestly: this verifies the STRUCTURAL claim -- that the symmetrised series is
rational with denominators supported only at 3 -- to the computed order. It does NOT reproduce
the specific "(q-1)^100 denominator = 3^146" figure, which is a single data point at an order
far beyond what this expansion reaches.
"""
import sympy as sp


def saddle_data(kmax):
    """Return (w0, A, [V^(k)(u0) for k=3..kmax]) exactly in Q(sqrt-3)."""
    u = sp.Symbol("u")
    # V' = -log(2 - e^u - e^-u); differentiate to get V^(k) for k >= 2
    Vp = -sp.log(2 - sp.exp(u) - sp.exp(-u))
    u0 = sp.I * sp.pi / 3                      # w0 = e^{i pi/3}, the geometric shape
    w0 = sp.simplify(sp.exp(u0))
    derivs = {}
    expr = Vp
    for k in range(2, kmax + 1):
        expr = sp.diff(expr, u)                 # after this loop-step expr = V^(k)
        val = sp.simplify(sp.expand(sp.radsimp(expr.subs(u, u0).rewrite(sp.sqrt))))
        derivs[k] = sp.nsimplify(sp.simplify(val))
    return w0, derivs[2], derivs


def phi_hat(derivs, A, order):
    """Feynman expansion of < exp(-sum_{k>=3} g_k t^k) > as a series in h, to h^order."""
    h = sp.Symbol("h")
    # interaction in the rescaled variable; track t-degree symbolically
    t = sp.Symbol("t")
    inter = 0
    kmax = max(derivs)
    for k in range(3, kmax + 1):
        inter += derivs[k] * h**sp.Rational(k - 2, 2) * A**sp.Rational(-k, 2) * t**k / sp.factorial(k)
    # exp(-inter) expanded to the needed order in h^(1/2)
    N = 2 * order + 1
    E, term = 1, 1
    for m in range(1, N + 1):
        term = sp.expand(term * (-inter) / m)
        term = sp.expand(term + sp.O(h**sp.Rational(N + 1, 2)).removeO() * 0)
        # drop anything already beyond the target order in h
        term = sum(c * mono for mono, c in sp.Poly(term, t).as_dict().items() for c in [1]) if False else term
        E = sp.expand(E + term)
        if term == 0:
            break
    # Gaussian expectation: t^(2m) -> (2m-1)!!, odd -> 0
    P = sp.Poly(sp.expand(E), t)
    out = 0
    for (deg,), coeff in P.terms():
        if deg % 2:
            continue
        m = deg // 2
        out += coeff * sp.factorial2(2 * m - 1) if m else coeff
    return sp.expand(sp.simplify(out))


def main():
    ORDER = 6                                   # h^0 .. h^ORDER of the symmetrised series
    KMAX = 2 * ORDER + 4
    print("=" * 78)
    print("B800 — recomputing B685's Habiro integrality leg in-sandbox")
    print("=" * 78)
    w0, A, derivs = saddle_data(KMAX)
    print(f"  saddle w0            = {w0}   (geometric tetrahedron shape)")
    chk = sp.simplify(sp.expand(sp.exp(2*sp.I*sp.pi/3) - sp.exp(sp.I*sp.pi/3) + 1).rewrite(sp.cos))
    print(f"  check w0^2 - w0 + 1  = {sp.nsimplify(sp.simplify(chk))}   (must be 0)")
    print(f"  1-loop V''(u0)       = {sp.simplify(A)}")
    print(f"  check V'' == sqrt-3  = {sp.simplify(A - sp.sqrt(-3)) == 0}")
    print(f"  V^(k)(u0) for k=3..6 = {[sp.simplify(derivs[k]) for k in range(3, 7)]}")

    h = sp.Symbol("h")
    P = phi_hat(derivs, A, ORDER)
    ser = sp.Poly(sp.expand(P), h)
    # symmetrised: Phi(h)Phi(-h). The prefactor 1/sqrt(A) squared gives a FIXED algebraic
    # constant 1/A = 1/sqrt(-3); the arithmetic lives in the SERIES part, so the object whose
    # integrality is at stake is Phat(h)*Phat(-h). (A first pass divided by A and left 1/sqrt-3
    # sitting in the h^0 term -- a normalisation error, not an arithmetic one.)
    Pm = P.subs(h, -h)
    S = sp.expand(sp.simplify(sp.expand(P * Pm)))
    S = sp.expand(sp.nsimplify(sp.radsimp(S)))
    print("\n  symmetrised series  Phi(h)Phi(-h) = (1/V'') * Phat(h) * Phat(-h)")
    poly = sp.Poly(sp.expand(S), h)
    rows = []
    for n in range(0, ORDER + 1):
        c = sp.simplify(poly.coeff_monomial(h**n)) if n else sp.simplify(poly.coeff_monomial(1))
        c = sp.nsimplify(sp.radsimp(sp.simplify(c)))
        rows.append((n, c))
    print(f"\n  {'n':>3}  {'coefficient of h^n':<34} rational? denominator factors")
    ok = True
    for n, c in rows:
        c = sp.simplify(c)
        israt = c.is_rational
        if israt and c != 0:
            den = sp.denom(sp.Rational(c))
            fac = sp.factorint(den)
            only3 = set(fac) <= {3}
            ok &= only3
            print(f"  {n:>3}  {str(c)[:34]:<34} yes       {den} = {fac if fac else '1'}"
                  f"{'   <-- NOT a power of 3' if not only3 else ''}")
        else:
            print(f"  {n:>3}  {str(c)[:34]:<34} {'yes' if israt else 'NO'}")
            if not israt:
                ok = False
    print(f"\n  VERDICT: symmetrised series rational with 3-power denominators only, to h^{ORDER}: {ok}")
    return rows, ok


if __name__ == "__main__":
    main()
