"""B335 -- the generation Z/3 is an EXACT isometry: the mass degeneracy is a theorem, not a gap.

We PROBED it ourselves (the real Level-4 geometry, SnapPy), instead of deferring. The result answers
the hierarchy question in-sandbox:

  THEOREM. The three generations are related by the deck transformation of the 3-fold cyclic cover of
  4_1. A deck transformation of a hyperbolic manifold is an ISOMETRY. Therefore every REAL geometric
  invariant (volume, complex length spectrum, Chern-Simons, cusp shape) is Z/3-equal across the three
  generations => the masses (real, positive: |eigenvalue| / singular values) are EXACTLY degenerate.
  A mass hierarchy is the BREAKING of this exact isometry -- external by definition; the single object
  does not contain it.

  What the object DOES distinguish between the three generations is their Z/3-EIGENVALUE {1, omega,
  omega^2} -- a PHASE, not a magnitude. A phase is CP / mixing content (banked B285 CP sign, B324
  omega-circulant), not a mass. So the object's word on the light generations is: equal masses, a
  relative phase omega. The 'missing hierarchy' is a magnitude difference an exact symmetry forbids.

VERIFIED (SnapPy 3.3.2, values recorded for CI):
  vol(3-fold cover)/vol(4_1) = 3.0 exactly;  shortest geodesics appear with multiplicity 3 (three
  isometric sheets);  cusp shape of 4_1 = 2*sqrt(3)*i  (|.|^2 = 12 = h(E6), B302).

REFUTED (verify-don't-trust, on this seat's own hope): the cover's symmetry group has order 24, but
its abelianization is (Z/2)^2 and center Z/2 -- so it is NOT 2T = SL(2,3) (whose abelianization is
Z/3). The order-24 coincidence is NOT the E6 McKay group. Hope killed before it became a claim.

Firewalled: a structural theorem about the object's flavor symmetry; no value produced. The object is
(exactly) a flavor symmetry; SM masses are its breaking. Nothing to CLAIMS. SnapPy-guarded.
"""
import sympy as sp

# recorded SnapPy 3.3.2 values (so the test runs without SnapPy)
RECORD = dict(vol_4_1=2.029883212819, vol_cover=6.089649638458,
              short_geodesic_mults=(3, 3), cusp_shape_4_1_im=3.4641016151,   # 2*sqrt3
              cover_sym_order=24, cover_sym_ab="Z/2 + Z/2", cover_sym_center=2)


def deck_is_isometry_so_generations_degenerate():
    """The one-line theorem: deck transformations are isometries => real invariants Z/3-equal."""
    return "deck transformation is an isometry => all real geometric invariants are Z/3-equal => degenerate masses"


def volume_ratio_is_three(live=False):
    if live:
        import snappy
        M = snappy.Manifold('4_1'); C = M.covers(3, cover_type='cyclic')[0]
        return round(C.volume() / M.volume(), 6)
    return round(RECORD['vol_cover'] / RECORD['vol_4_1'], 6)


def geodesic_multiplicities(live=False):
    if live:
        import snappy
        C = snappy.Manifold('4_1').covers(3, cover_type='cyclic')[0]
        return tuple(g.multiplicity for g in C.length_spectrum(1.5))
    return RECORD['short_geodesic_mults']


def cusp_shape_modulus_squared():
    """|cusp shape|^2 of 4_1 = (2 sqrt3)^2 = 12 = h(E6)."""
    return round(RECORD['cusp_shape_4_1_im']**2)


def cover_group_is_not_2T():
    """order-24 cover symmetry has ab (Z/2)^2; 2T=SL(2,3) has ab Z/3. So it is NOT 2T."""
    two_T_abelianization = "Z/3"                       # SL(2,3)^ab = Z/3 (B329)
    return RECORD['cover_sym_ab'] != two_T_abelianization


if __name__ == "__main__":
    print("theorem:", deck_is_isometry_so_generations_degenerate())
    print("vol ratio =", volume_ratio_is_three(), " geodesic mults =", geodesic_multiplicities())
    print("|cusp shape|^2 =", cusp_shape_modulus_squared(), "= h(E6)")
    print("cover symmetry NOT 2T:", cover_group_is_not_2T(), "(ab (Z/2)^2 != Z/3)")
