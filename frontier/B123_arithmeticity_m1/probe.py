"""B123 -- m=1 arithmeticity: a THIRD independent selection criterion for the figure-eight (golden, m=1).

The figure-eight complement has a regular ideal triangulation with shape parameter z_0 = e^{i pi/3} (a 6th root of
unity; z^2 - z + 1 = Phi_6), invariant trace field Q(sqrt-3) -- so it is ARITHMETIC. By Reid (1991) the figure-eight
is the UNIQUE arithmetic knot complement (and there are exactly two arithmetic once-punctured-torus bundles), so the
m>=2 metallic manifolds are NOT arithmetic. This gives a third independent reason m=1 is special:

  the figure-eight is the unique metallic manifold that is both SIMPLEST (smallest volume / systole, B92) AND MOST
  REGULAR (arithmetic / root-of-unity shape) -- a selection criterion INDEPENDENT of the systole and the expansion
  threshold (P004).

STATUS / HONEST SCOPE (do NOT overstate):
  * COMPUTED in-house (this probe): the cyclotomic shape z^2-z+1=Phi_6 (root e^{i pi/3}); the ORDER-6 echo at the
    geometric cusp (the (0,0,0) non-void Jacobian spectrum, B122, char poly lambda^3+1 = 6th roots, at kappa=-2).
  * CITED (Reid 1991): the figure-eight is the unique arithmetic knot; m>=2 metallic manifolds are non-arithmetic.
  * SnapPy/Magma-GATED (the named CONFIRMATION step, NOT done here): the m>=2 invariant-trace-field non-arithmeticity
    computed via the standard arithmeticity criterion (the repo has no trace-field classifier). So this is banked
    SUPPORTED, NOT TESTED-POSITIVE.

THE ORDER-6 ECHO IS AN OBSERVATION, NOT A CONNECTION. Both the regular-tetrahedron shape e^{i pi/3} and the
geometric-cusp (kappa=-2) Jacobian spectrum are 6th-root-of-unity / Q(sqrt-3) phenomena -- consistent with the
figure-eight's invariant trace field Q(sqrt-3). Whether this is a deep structural link or two manifestations of the
same field is itself open; recorded as an observation, not a banked connection.

CROSS-REFERENCE (not a new finding): the det=-1 middle eigenvalue = -1 (vs +1 for det=+1) is the PROVED B121 parity
(the external det=-1 GL(2,Z)-rep / the odd-Sym^d obstruction), already re-derived via fig-8 = golden^2 (B122). An
asset, not a kill.

Standalone arithmetic geometry; NO physics; no CLAIMS.md promotion; the rho_n / Sym-mu_d proof stays the prize;
P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B122 = _load("b123_b122", "frontier/B122_W_symmetric_powers/probe.py")


# --------------------------------------------------------------------------- #
# the figure-eight cyclotomic shape (computed in-house)
# --------------------------------------------------------------------------- #
def figure_eight_shape_is_cyclotomic():
    """The fig-8 ideal-triangulation shape z_0 satisfies z^2 - z + 1 = Phi_6 (the 6th cyclotomic), so z_0 = e^{i
    pi/3} is a primitive 6th root of unity; the invariant trace field is Q(sqrt-3) (arithmetic)."""
    z = sp.symbols("z")
    shape_poly = z ** 2 - z + 1
    is_phi6 = sp.simplify(shape_poly - sp.cyclotomic_poly(6, z)) == 0
    roots = sp.roots(shape_poly, z)
    z0 = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2                      # = e^{i pi/3}
    # verify z0 is a primitive 6th root and satisfies the shape poly (use rectangular form, not raw exp)
    satisfies = sp.simplify(z0 ** 2 - z0 + 1) == 0
    primitive_6th = sp.simplify(z0 ** 6 - 1) == 0 and sp.simplify(z0 ** 3 - 1) != 0 and sp.simplify(z0 ** 2 - 1) != 0
    return {"shape_poly": "z^2 - z + 1", "is_cyclotomic_Phi6": bool(is_phi6),
            "roots": [str(r) for r in roots], "z0_rect": "1/2 + sqrt(3)/2 i = e^{i pi/3}",
            "z0_satisfies_shape": bool(satisfies), "z0_primitive_6th_root": bool(primitive_6th),
            "invariant_trace_field": "Q(sqrt-3) -> ARITHMETIC (Reid 1991: the unique arithmetic knot)"}


# --------------------------------------------------------------------------- #
# the order-6 echo at the geometric cusp (kappa = -2) -- OBSERVATION, not a connection
# --------------------------------------------------------------------------- #
def order6_echo_at_geometric_cusp():
    """The (0,0,0) non-void Jacobian (B122) has char poly lambda^3+1 = {-1, e^{+-i pi/3}} (6th roots, order 6), and
    (0,0,0) is the GEOMETRIC cusp kappa = x^2+y^2+z^2-xyz-2 = -2 (the complete hyperbolic structure, B69/B109).
    So the geometric cusp's Jacobian spectrum is the SAME e^{i pi/3}/Q(sqrt-3) as the tetrahedron shape -- an
    OBSERVATION (both Q(sqrt-3) phenomena), NOT a banked connection."""
    vs = _B122.sym_tower_is_void_specific()
    kappa = lambda x, y, z: x * x + y * y + z * z - x * y * z - 2
    return {"zero_jacobian_6th_roots": vs["zero_charpoly_is_lam3_plus_1"], "order_is_6": vs["order_is_6_not_3"],
            "zero_spectrum": vs["zero_spectrum"], "kappa_at_zero": kappa(0, 0, 0),
            "is_geometric_cusp": kappa(0, 0, 0) == -2,
            "status": "OBSERVATION (both the tetrahedron shape e^{i pi/3} and the geometric-cusp Jacobian spectrum "
                      "are 6th-root / Q(sqrt-3) phenomena; structural-vs-incidental is open) -- NOT a connection."}


# --------------------------------------------------------------------------- #
# the third selection criterion + the honest status split
# --------------------------------------------------------------------------- #
def third_selection_criterion():
    """m=1 is special for THREE independent reasons: (i) systole (B92), (ii) expansion threshold (P004/B120),
    (iii) arithmeticity (this). SUPPORTED (shape computed + Reid cited; SnapPy trace-field = named confirmation)."""
    sh = figure_eight_shape_is_cyclotomic()
    return {"criterion_i_systole": "B92/S001 -- m=1 = the systole (shortest closed geodesic on H/GL(2,Z))",
            "criterion_ii_expansion": "P004/B120 -- m=0 static |lambda|=1, m=1 first interaction ignites the tower",
            "criterion_iii_arithmeticity": "this -- m=1 = arithmetic (Q(sqrt-3), z0=e^{i pi/3}); m>=2 not (Reid 1991)",
            "shape_computed": sh["is_cyclotomic_Phi6"] and sh["z0_primitive_6th_root"],
            "m_ge_2_nonarith_status": "SUPPORTED (Reid 1991) -- SnapPy/Magma invariant-trace-field computation is "
                                      "the named CONFIRMATION step (tooling-gated; the repo has no trace-field classifier)",
            "banked_as": "SUPPORTED (not TESTED-POSITIVE)"}


def det_minus_one_is_b121():
    """Cross-reference (NOT a new finding): the det=-1 middle eigenvalue = -1 (vs +1 at det=+1) is the proved B121
    parity (the external det=-1 GL(2,Z)-rep / the odd-Sym^d obstruction), already re-derived via fig-8 = golden^2
    (B122). An asset, not a kill."""
    return {"is_b121_restated": True, "anchor": "B121/V109 (the det=-1 parity); re-derived in B122 (fig-8=golden^2)",
            "note": "cross-reference, not a new finding -- the det=-1 middle eigenvalue is the B121 parity asset."}


def main():
    print("=" * 78)
    print("B123 -- m=1 arithmeticity: a third independent selection criterion (SUPPORTED)")
    print("=" * 78)
    sh = figure_eight_shape_is_cyclotomic()
    print(f"\n[shape] fig-8 shape poly z^2-z+1 = Phi_6: {sh['is_cyclotomic_Phi6']}; z0={sh['z0_rect']}, "
          f"satisfies shape: {sh['z0_satisfies_shape']}, primitive 6th root: {sh['z0_primitive_6th_root']}")
    print(f"        {sh['invariant_trace_field']}")
    ec = order6_echo_at_geometric_cusp()
    print(f"\n[order-6 echo, OBSERVATION] (0,0,0) Jacobian = {ec['zero_spectrum']}; kappa(0,0,0)={ec['kappa_at_zero']} "
          f"(geometric cusp: {ec['is_geometric_cusp']})")
    print(f"        {ec['status']}")
    tc = third_selection_criterion()
    print(f"\n[3rd criterion] (i) {tc['criterion_i_systole']}")
    print(f"                (ii) {tc['criterion_ii_expansion']}")
    print(f"                (iii) {tc['criterion_iii_arithmeticity']}")
    print(f"     banked as: {tc['banked_as']}; m>=2: {tc['m_ge_2_nonarith_status']}")
    db = det_minus_one_is_b121()
    print(f"\n[cross-ref] det=-1 middle eigenvalue = B121 parity (asset, not a kill): {db['anchor']}")
    print("\nNONE of this lowers the wall: the functorial Sym(W)->trace-ring construction is still the missing piece.")


if __name__ == "__main__":
    main()
