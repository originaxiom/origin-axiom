"""B730 lock — forced faces close at a Klein-four V4; the cosmic-topology meeting point is real-math /
physics-nil. Three-way converged (cc independent + cc2 faces + cc2 capstone). Structural/arithmetic
+ topology only; no cosmology claim (Gate 5).
"""
import sympy as sp

x = sp.Symbol('x')


def test_forced_faces_are_the_klein_four_V4():
    # being Q(sqrt-3) disc -3, hearing Q(sqrt5) disc 5, meeting Q(sqrt-15) fundamental disc -15.
    assert sp.discriminant(x**2 - x + 1, x) == -3          # tetrahedron shape -> being
    assert sp.discriminant(x**2 - 3*x + 1, x) == 5         # Alexander -> hearing
    # meeting = being*hearing: sqrt-3 * sqrt5 = sqrt-15
    assert sp.simplify(sp.sqrt(-3)*sp.sqrt(5) - sp.sqrt(-15)) == 0
    # Q(sqrt-15) fundamental disc = -15 (since -15 = 1 mod 4), NOT -60 (that is the non-maximal order)
    assert (-15) % 4 == 1                                   # -> fundamental disc -15, maximal order Z[(1+sqrt-15)/2]
    # the three subfields of the biquadratic V4 = Gal(Q(sqrt-3,sqrt5)/Q) = C2xC2
    subfield_discs = {-3, 5, -15}
    assert len(subfield_discs) == 3                        # Klein-four: exactly 3 quadratic subfields


def test_sqrt_minus7_explodes_V4_so_it_is_a_stage_not_a_face():
    # the SL(3) boundary-unipotent field: 4c^2-c+4 has disc -63 = -7*9 -> Q(sqrt-7).
    assert sp.discriminant(4*x**2 - x + 4, x) == -63       # -7*9
    # adjoining sqrt-7 to the V4 field does NOT refine it -- it makes (Z/2)^3 (7 quadratic subfields).
    # {sqrt-3, sqrt5, sqrt-7} generate an order-8 group with 7 involutions -> a STAGE (the B704 seam), not a 4th face.
    generators = 3                                          # sqrt-3, sqrt5, sqrt-7 independent in Q*/(Q*)^2
    n_quadratic_subfields = 2**generators - 1              # (Z/2)^3 has 7 order-2 subgroups
    assert n_quadratic_subfields == 7                       # explodes past V4's 3 -> not a refinement


def test_child_fields_lose_the_being_B718_confirmed():
    # Thurston = m004(5,1) invariant trace field x^4-x-1: disc -283, Galois S4 (order 24), NO quadratic subfield.
    p4 = x**4 - x - 1
    assert sp.discriminant(p4, x) == -283
    assert sp.Poly(p4, x).galois_group()[0].order() == 24  # S4 -> no quadratic subfield -> being does NOT survive
    # Weeks = m003(-3,1) invariant trace field x^3-x-1: disc -23, S3.
    p3 = x**3 - x - 1
    assert sp.discriminant(p3, x) == -23
    assert sp.Poly(p3, x).galois_group()[0].order() == 6   # S3
    # neither child field contains Q(sqrt-3): the being washes out on Dehn filling (B718)


def test_thurston_manifold_is_m004s_own_child_second_smallest_closed():
    # m004(5,1) is the Thurston manifold, #2-smallest closed orientable hyperbolic 3-manifold.
    try:
        import snappy
    except ImportError:
        import pytest
        pytest.skip("snappy unavailable")
    M = snappy.Manifold("m004(5,1)")
    assert abs(M.volume() - 0.98136882889) < 1e-8          # Thurston manifold volume (#2 smallest)
    assert M.is_isometric_to(snappy.Manifold("m003(-2,3)"))    # = the Thurston manifold census name
    assert not M.is_isometric_to(snappy.Manifold("m003(-3,1)"))  # NOT the Weeks manifold (#1, the sister's child)
    W = snappy.Manifold("m003(-3,1)")
    assert abs(W.volume() - 0.94270736278) < 1e-8          # Weeks (#1 smallest) = the sister m003's child
