"""C28's corrected ramification clause (B894 addendum 2026-08-18; E41).

The golden 5 is model-borne, not ramified in the charge field K: disc K = 6237
and 5 does not divide it. Locks the reduced model, the isomorphism, maximality,
and the splitting shapes so the corrected clause cannot silently regress.
"""
from sympy import Poly, discriminant, factorint, gcd, factor_list, rootof, symbols

t, x = symbols("t x")

# mu — the charge cubic, banked coefficients (B866/B889), leading coeff first
L, B, C, D = 500716339200, -159667200, -28224, 1
MU = L * t**3 + B * t**2 + C * t + D
F = x**3 - 12 * x - 5  # the reduced (monogenic) model


def test_disc_mu_factorization_and_resolvent():
    d = discriminant(Poly(MU, t))
    assert factorint(d) == {2: 32, 3: 10, 5: 2, 7: 3, 11: 1, 13: 6}
    sf = 1
    for p, e in factorint(d).items():
        if e % 2:
            sf *= p
    assert sf == 77  # the resolvent Q(sqrt 77)


def test_reduced_model_is_the_field():
    # disc of the reduced cubic
    assert discriminant(Poly(F, x)) == 6237
    assert factorint(6237) == {3: 4, 7: 1, 11: 1}
    # genuine isomorphism: mu factors with a linear piece over Q(beta)
    beta = rootof(F, 0)
    degs = sorted(p.degree() for p, _ in factor_list(Poly(MU, t), extension=beta)[1])
    assert 1 in degs


def test_index_one_by_dedekind_at_3():
    # f mod 3 = (x+1)^3; Dedekind criterion gcd must be 1 (then index = 1,
    # since only 3^4 is a square factor of 6237, so disc K = 6237 exactly)
    f3 = Poly(F, x, modulus=3).factor_list()
    assert f3[1] == [(Poly(x + 1, x, modulus=3), 3)]
    gstar = Poly(x + 1, x)
    hstar = Poly((x + 1) ** 2, x)
    Fcap = Poly((gstar.as_expr() * hstar.as_expr() - F) / 3, x)
    gg = gcd(
        gcd(Poly(Fcap, x, modulus=3), Poly(gstar, x, modulus=3)),
        Poly(hstar, x, modulus=3),
    )
    assert gg.degree() == 0


def test_five_is_unramified_with_value_prime_shape():
    # THE CORRECTED CLAUSE: 5 does not divide disc K
    assert 6237 % 5 != 0
    # splitting shape [1,2] in K (index 1, so factorization mod 5 is faithful)
    fl = Poly(F, x, modulus=5).factor_list()[1]
    assert sorted(p.degree() for p, _ in fl) == [1, 2]
    assert all(m == 1 for _, m in fl)  # squarefree: unramified
    # unramified in Q(sqrt 77) too (disc 77): the whole S3 closure
    assert 77 % 5 != 0
    # and the model-borne twins: 2 and 13 likewise unramified in K
    assert 6237 % 2 != 0 and 6237 % 13 != 0
    # K's genuinely ramified primes are exactly {3, 7, 11}
    assert sorted(factorint(6237)) == [3, 7, 11]
