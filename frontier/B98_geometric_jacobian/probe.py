"""B98 (Probe 1) -- the trace-map Jacobian at the GEOMETRIC representation (not the trivial fixed line).

Neutral low-dim-topology / Lie-theory mathematics. The physics framework (the 3d-3d correspondence) is
cited from the published literature, NOT claimed; our contribution is the specific computation below.

The metallic tower char(J(m)) = the Dickson catalog (B89-T) is computed at the TRIVIAL fixed line of the
trace map (all traces = n). Task T (B89-T) showed that route degenerates there. The GEOMETRIC
representation -- the holonomy of the complete hyperbolic structure -- is a DIFFERENT fixed point, and is
where the literature's bridges live:
  * the 3d-3d correspondence (Dimofte-Gaiotto-Gukov, arXiv:1108.4389, 1112.5179; Terashima-Yamazaki,
    arXiv:1103.5748; Gang-Koh-Lee-Park, arXiv:1305.0937) -- the SL(n) character variety of a 3-manifold;
  * Daly (arXiv:2411.04431, 2024) -- for once-punctured-torus bundles, the monodromy action on the tangent
    space of the character variety AT THE GEOMETRIC REP is the group-theoretic cohomological action (the
    twisted-Alexander object).
We had never computed the Jacobian spectrum at the geometric rep. This does it at SL(2).

RESULT (figure-eight, SL(2); exact). The figure-eight trace map is T_1^2 with
T_1(x,y,z)=(z, x, xz-y) on the Fricke coordinates (x,y,z)=(tr A, tr B, tr AB). On the geometric component
V0 = {y=z=x/(x-1)} the Jacobian char poly is
        char(D T_1^2)|_{V0} = (t - 1) * ( t^2 - c(x) t + 1 ),     c(x) = (2x^2 - x + 1)/(x - 1).
The GEOMETRIC fixed point has parabolic puncture (tr[A,B] = -2), i.e. on V0: x^2 - 3x + 3 = 0, so
        x_geom = (3 +- sqrt(-3))/2   in  Q(sqrt(-3))   -- exactly the figure-eight trace field.
There c(x_geom) = 5 and
        char(D T_1^2)|_geom = (t - 1)( t^2 - 5 t + 1 ).
The transverse pair {mu, 1/mu} (mu + 1/mu = 5) gives the ADJOINT REIDEMEISTER TORSION
        tau = (1 - mu)(1 - 1/mu) = 2 - c = -3,
which equals the figure-eight adjoint torsion tau_1 = -3 (cs_invariant_family; Porti), and is the object
Daly identifies with the geometric tangent-space monodromy action.

VERDICT. The Dickson TOWER does NOT appear at the geometric rep -- it is a TRIVIAL-REP phenomenon. At the
geometric rep the same monodromy's Jacobian gives the t^2 - 5 t + 1 = adjoint-torsion / twisted-Alexander
object (consistent with Daly, arXiv:2411.04431; reproduces tau_1 = -3). The two fixed points of the trace
map carry DIFFERENT invariants: trivial -> the Dickson tower; geometric -> the torsion. (This also explains
why Task T degenerated at the trivial rep: the cohomological/torsion content lives at the geometric rep.)

PROBE 5b (a deflation check). Is the tower = the Kostant principal-sl(2) branching of sl(n)? NO. Kostant's
sl(n) = (+)_{k=1}^{n-1} V_{2k} is EVEN-power Sym^{2k} only; the tower's two-sequence
[Sym^2..Sym^n] x [Sym^0..Sym^{n-3}] uses consecutive intervals of BOTH parities -- a different object (so
the tower is not "just a known decomposition"; consistent with the V27 even-only kill).

Standalone low-dim topology / Lie theory; no physics claim; no Origin-core claim; P1-P16 untouched.
"""
from __future__ import annotations

import sympy as sp

x, y, z, t = sp.symbols("x y z t")


def _T1sq_jacobian_on_V0():
    """char(D T_1^2) restricted to the geometric component V0={y=z=x/(x-1)}, as (factored) poly in t,x."""
    T1 = lambda v: (v[2], v[0], v[0] * v[2] - v[1])
    F = [sp.expand(c) for c in T1(T1((x, y, z)))]
    J = sp.Matrix([[sp.diff(F[i], v) for v in (x, y, z)] for i in range(3)])
    yc = x / (x - 1)
    return sp.factor(J.subs({y: yc, z: yc}).charpoly(t).as_expr())


def geometric_fixed_point():
    """The geometric (parabolic-puncture, tr[A,B]=-2) fiber trace on V0: x^2-3x+3=0 => (3+-sqrt(-3))/2."""
    return sp.Rational(3, 2) + sp.sqrt(-3) / 2


def char_at_geometric():
    """char(D T_1^2) at the geometric rep = (t-1)(t^2 - 5t + 1)."""
    xg = geometric_fixed_point()
    return sp.expand(sp.simplify(_T1sq_jacobian_on_V0().subs(x, xg)))


def torsion_from_geometric_jacobian():
    """tau = 2 - c(x_geom) = -3, the adjoint Reidemeister torsion (== cs_invariant_family tau_1)."""
    xg = geometric_fixed_point()
    c = (2 * x**2 - x + 1) / (x - 1)
    return sp.simplify(2 - c.subs(x, xg))


def tower_vs_kostant(n):
    """(Kostant Sym-powers [even-only], tower two-sequence Sym-powers) -- they differ => tower != branching."""
    kostant = sorted(2 * k for k in range(1, n))
    tower = sorted(list(range(2, n + 1)) + list(range(0, n - 2)))
    return kostant, tower, kostant == tower


def main():
    print("B98 (Probe 1) -- the trace-map Jacobian at the GEOMETRIC rep (figure-eight, SL(2))\n")
    print(f"  char(D T_1^2)|_V0  = {_T1sq_jacobian_on_V0()}")
    xg = geometric_fixed_point()
    print(f"  geometric fixed point x_geom = {xg}  (x^2-3x+3=0, in Q(sqrt-3) = the fig-8 trace field)")
    print(f"  char at geometric            = {sp.factor(char_at_geometric())}")
    print(f"  adjoint torsion tau = 2 - c  = {torsion_from_geometric_jacobian()}  (== cs_invariant tau_1 = -3)")
    print("  => the Dickson tower is a TRIVIAL-rep phenomenon; the geometric rep gives the torsion /")
    print("     twisted-Alexander object (consistent with Daly arXiv:2411.04431). DIFFERENT fixed points.\n")
    print("Probe 5b -- tower vs Kostant principal-sl(2) branching (even-only Sym^{2k}):")
    for n in (3, 4):
        k, tw, same = tower_vs_kostant(n)
        print(f"  n={n}: Kostant {k} vs tower {tw} -> same? {same}  (tower is NOT the Kostant branching)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
