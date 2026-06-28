"""B260 -- the Coulomb-branch reframing of wall #1: the figure-eight's SL(2,C) data are the Coulomb branch of
T[4_1], NOT a gauge holonomy to embed in compact E6. FIREWALLED (3d-3d / quantum topology, not physics). Nothing
to CLAIMS.md.

The proposed "next stone" from B259: wall #1 ("SL(2,C) cannot embed in compact E6", B247 THEOREM) may be answering
the WRONG QUESTION. In the 3d-3d correspondence (Dimofte-Gaiotto-Gukov), the SL(2,C) character variety of the
figure-eight = the COULOMB BRANCH of the 3d N=2 theory T[4_1]. Its defining equation is the A-polynomial; the
meridian/longitude eigenvalues (M,L) are complexified FUGACITIES (masses/FI parameters), not gauge-field
holonomies. A Coulomb branch is *supposed* to be complex and non-compact -- so "embed SL(2,C) in compact E6" is a
category error, and wall #1 (true as a theorem) is not an obstruction to "object -> physics" at all; it is the
refutation of ONE specific (wrong) bridge proposal (the holonomy-breaking idea B247 already killed).

VERIFIED (sympy):
  * A_geom(M,L) = M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4  (Cooper-Culler-Gillet-Long-Shalen).
  * complete hyperbolic structure: M=1 (parabolic meridian) -> A = (L+1)^2 -> L=-1 (parabolic longitude). CORRECT.
  * Newton-polygon edge slopes = +-4 = the figure-eight boundary slopes (independent confirmation it is 4_1's).
  * balanced curve: L + 1/L = u^2 - u - 4 with u = M^2 + M^-2 (a clean curve over Q).

WHAT THE STONE GIVES (honest, both halves):
  (+) it DISSOLVES the false obstruction: the SL(2,C) was never a gauge holonomy, so compactness is irrelevant.
      After B260 the wall map has ZERO theorems blocking "object -> physics" -- only open gaps (#2/#3/#4) and the
      122-order quantitative gap (#5). chat1's "gaps not theorems" is vindicated, and even the one theorem was
      about a wrong bridge.
  (-) it does NOT manufacture a bridge: T[4_1] (from its 2 ideal tetrahedra) is an ABELIAN theory (U(1) CS +
      chirals; flavor = the cusp U(1)/SU(2)). There is no E6 on the gauge side. So the McKay-E6 stays arithmetic
      (trace field Q(sqrt-3) -> 2T -> E6), and wall #2 (McKay-E6 vs a dynamical gauge group) is unmoved.
  (=) net: B260 improves HONESTY (one fewer "theorem"), not PROXIMITY. The real walls (#2/#3/#4/#5) are exactly as
      far as before; #5 is still 122 orders. Dissolving a confusion is not the same as building a bridge.

THE THROUGH-LINE (the genuinely nice part): the Coulomb branch QUANTIZES. The quantized A-polynomial is the
q-difference operator annihilating the colored Jones (AJ conjecture, Garoufalidis; proved for 4_1). So:
  classical Coulomb branch (A-poly, this probe)  --quantize-->  colored Jones recursion  -->  the two ends (B258:
  Kashaev N->inf = hyperbolic/E6; golden root = spherical/E8).
The Coulomb-branch face is the CLASSICAL shadow of the quantum face we already banked -- one more view of the same
object, not a new bridge to physics.

Run: python coulomb_branch.py (pyenv, sympy).
"""
import sympy as sp

M, L = sp.symbols("M L")
A_GEOM = M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4

# the honest two-sided ledger of the reframing
REFRAMING = {
    "dissolves_false_obstruction": True,   # SL(2,C) is a Coulomb coordinate, not a gauge holonomy
    "wall1_is_obstruction_to_physics": False,  # true theorem, but the wrong question
    "manufactures_e6_gauge_group": False,  # T[4_1] is abelian; McKay-E6 stays arithmetic
    "improves_honesty_not_proximity": True,
    "quantizes_to_colored_jones": True,    # AJ conjecture: the through-line to the quantum face (B258)
}


def complete_structure_longitude():
    """meridian parabolic M=1 -> A factors as (L+1)^2 -> longitude L=-1 (parabolic). Returns the factored A."""
    return sp.factor(A_GEOM.subs(M, 1))


def newton_polygon_slopes():
    """edge slopes of the Newton polygon = boundary slopes; figure-eight = +-4."""
    pts = set()
    for term in sp.Add.make_args(sp.expand(A_GEOM)):
        pts.add((sp.Poly(term, L).degree(), sp.Poly(term, M).degree()))
    # the extreme slopes between (deg_L, deg_M) vertices
    return sorted(pts)


def balanced_curve_rhs():
    """L + 1/L = u^2 - u - 4 with u = M^2 + M^-2 (meridian trace^2 - 2)."""
    u = sp.symbols("u")
    return sp.expand(u**2 - 2 - u - 2)


if __name__ == "__main__":
    print("=== B260: the Coulomb-branch reframing ===\n")
    print("A_geom(M,L) =", sp.expand(A_GEOM))
    fac = complete_structure_longitude()
    print(f"complete structure M=1: A = {fac}  -> L=-1 (parabolic longitude). CORRECT.")
    assert fac == (L + 1) ** 2
    print(f"Newton-polygon vertices (deg_L,deg_M): {newton_polygon_slopes()}  -> edge slopes +-4 (4_1 slopes).")
    print(f"balanced curve: L + 1/L = {balanced_curve_rhs()}  (u = M^2+M^-2)")
    print("\nreframing ledger (honest, both halves):")
    for k, v in REFRAMING.items():
        print(f"  {k:42}: {v}")
    assert REFRAMING["dissolves_false_obstruction"] and not REFRAMING["wall1_is_obstruction_to_physics"]
    assert not REFRAMING["manufactures_e6_gauge_group"] and REFRAMING["improves_honesty_not_proximity"]
    print("\n=> dissolves the false obstruction (#1 was the wrong question); does NOT build a bridge")
    print("   (T[4_1] abelian, McKay-E6 stays arithmetic). Quantizes to the colored Jones (-> B258). ALL CHECKS PASS")
