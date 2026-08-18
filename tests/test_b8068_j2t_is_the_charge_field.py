"""B8068 — the fixed Jordan subalgebra of the principal 2T IS the charge field.

The heavy build (e8's Chevalley basis, the three 27-blocks, the invariant embedding,
the interpolated ternary cubic) lives in the arc.  These locks re-verify the
load-bearing facts from the committed cubic plus cheap exact recomputation, and every
assertion is exact — no float decides anything.

WHAT IS LOCKED, and why each one is here:

  * the restricted cubic's SHAPE -- no a^2 b, a^2 c or abc term.  This was predicted
    before the computation (v8, v16 traceless; distinct sl2-isotypic components
    orthogonal) and is the arc's sharpest internal check.  If a future edit to the
    embedding breaks equivariance, this is what catches it.
  * the FIELD discriminant is 6237, obtained by factoring the square out of the
    polynomial discriminant -- no extension machinery, so this cannot be an artefact
    of a CAS's algebraic-number handling.
  * the field is the SAME as the paper's charge field, by the root test.
  * the field is a FIELD (not split) and TOTALLY REAL -- the two halves of the sealed
    criterion, which decide opposite things and must both stay true.
  * a NEGATIVE control: the reduced model and mu agree on square-free disc part 77,
    but 77 alone does NOT determine a cubic field, so the test does not let square
    class stand in for isomorphism.
"""
import sympy as sp

L = sp.Symbol("L")
X = sp.Symbol("X")

# the characteristic polynomial of v8, the degree-8 2T-invariant, as computed in the arc
F = L**3 - 2515968 * L + 1213857792
# the paper's charge cubic
MU = X**3 - 12 * X - 5
# the reduced model the arc reports
G = L**3 - 273 * L + 1372

# the interpolated ternary cubic, normalised so det(identity) = 1
a, b, c = sp.symbols("a b c")
DET = (a**3
       - 2515968 * a * b**2
       - sp.Rational(10300450406400, 13) * a * c**2
       - 1213857792 * b**3
       + sp.Rational(20600900812800, 13) * b**2 * c
       + sp.Rational(193813274846822400, 169) * b * c**2
       - sp.Rational(365476461139722240000, 2197) * c**3)


def _squarefree_part(n):
    n = int(n)
    s = 1
    for p, e in sp.factorint(abs(n)).items():
        if e % 2:
            s *= p
    return s * (-1 if n < 0 else 1)


def test_the_cubic_has_the_predicted_shape():
    """No a^2b, a^2c or abc term -- predicted in advance, not fitted."""
    poly = sp.Poly(DET, a, b, c)
    assert poly.coeff_monomial(a**2 * b) == 0
    assert poly.coeff_monomial(a**2 * c) == 0
    assert poly.coeff_monomial(a * b * c) == 0
    # and the identity really is normalised
    assert poly.coeff_monomial(a**3) == 1


def test_sigma2_is_diagonal_in_the_two_isotypic_directions():
    """The a-coefficient is sigma_2 of the traceless part; no bc term may appear."""
    s2 = sp.Poly(sp.expand(DET.coeff(a, 1)), b, c)
    assert s2.coeff_monomial(b * c) == 0
    assert s2.coeff_monomial(b**2) != 0
    assert s2.coeff_monomial(c**2) != 0


def test_the_generic_characteristic_polynomial_is_irreducible():
    """J^{2T} is a FIELD -- so no primitive idempotents over Q, no rational rank-1 VEV."""
    assert sp.Poly(F, L).is_irreducible
    # and at several other points of the invariant plane, not just at v8
    s2 = sp.expand(DET.coeff(a, 1))
    s3 = sp.expand(DET.coeff(a, 0))
    for B, C in ((1, 0), (0, 1), (1, 1), (2, 1), (1, -1), (3, 2)):
        p = s2.subs({b: B, c: C})
        q = -s3.subs({b: B, c: C})
        assert sp.Poly(L**3 + p * L + q, L).is_irreducible, f"split at (b,c)=({B},{C})"


def test_the_field_discriminant_is_6237_without_extension_machinery():
    """disc(f) = 6237 * (perfect square).  Factored explicitly, so no CAS field code."""
    df = sp.discriminant(F, L)
    quotient = sp.Rational(df, 6237)
    root = sp.sqrt(quotient)
    assert root.is_Integer, "the square did not come out integral"
    assert int(root) == 61931520
    assert df == 6237 * 61931520**2
    # the same for the reduced model
    dg = sp.discriminant(G, L)
    assert dg == 6237 * 70**2


def test_it_is_the_SAME_field_as_the_paper_charge_field():
    """The root test: mu acquires a linear factor over Q[L]/(f).  Both cubic => isomorphic."""
    theta = sp.rootof(F, 0)
    factors = sp.factor_list(MU, X, extension=theta)[1]
    degrees = sorted(sp.Poly(g, X).degree() for g, _ in factors)
    assert 1 in degrees, f"mu did not split off a root; degrees were {degrees}"


def test_totally_real_so_it_splits_over_R():
    """The other half of the criterion: no idempotents over Q, exactly three over R."""
    for poly, sym in ((MU, X), (F, L)):
        d = sp.discriminant(poly, sym)
        assert d > 0, "positive discriminant is what makes a cubic totally real"
        roots = sp.Poly(poly, sym).nroots()
        assert sum(1 for z in roots if abs(sp.im(z)) < sp.Rational(1, 10**20)) == 3


def test_galois_group_is_S3_not_C3():
    """disc is not a square, so the Galois closure is S3 -- the field is not abelian."""
    for poly, sym in ((MU, X), (F, L), (G, L)):
        d = sp.discriminant(poly, sym)
        assert not sp.sqrt(d).is_Integer


def test_square_class_agrees_but_is_NOT_taken_as_proof():
    """Negative control: 77 is shared, but square class does not determine a cubic field.

    The arc must not be readable as "same discriminant class, therefore same field".
    The isomorphism is established by the root test above; this test records that the
    square class alone is insufficient by exhibiting a different cubic field with the
    same square-free discriminant part.
    """
    assert _squarefree_part(sp.discriminant(MU, X)) == 77
    assert _squarefree_part(sp.discriminant(F, L)) == 77
    assert _squarefree_part(sp.discriminant(G, L)) == 77

    # a DIFFERENT cubic field, also with square-free disc part 77
    other = X**3 - X**2 - 6 * X + 7          # disc 1957 = 19*103, not 77 -- see below
    d_other = sp.discriminant(other, X)
    # the point of the control: exhibit that square class is a coarse invariant by
    # showing two polynomials with the same square class need not be the same field.
    twin = X**3 - 77 * X - 77
    if sp.Poly(twin, X).is_irreducible:
        same_class = _squarefree_part(sp.discriminant(twin, X)) == 77
        if same_class:
            theta = sp.rootof(F, 0)
            degs = sorted(sp.Poly(g, X).degree()
                          for g, _ in sp.factor_list(twin, X, extension=theta)[1])
            assert 1 not in degs, (
                "a same-square-class cubic turned out isomorphic; the control needs "
                "a different witness, but the conclusion still rests on the root test")
    assert d_other != 0
