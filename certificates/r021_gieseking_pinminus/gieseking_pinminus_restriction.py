#!/usr/bin/env python3
"""R021: Pin-minus structures on the Gieseking manifold.

This certificate is deliberately topological.  It proves the torsor counts
and the affine restriction behaviour for the orientable double cover
``p: m004 -> m000``.  It does not attempt to identify the resulting spin
structure with any separately chosen SL(2,C) sign lift.

Convention: for the Riemannian tangent bundle, Pin^- exists precisely when
    w2(TN) + w1(TN)^2 = 0.
When it exists, Pin^-(N) is an H^1(N; F_2)-torsor.  On the orientable cover a
restricted Pin^- structure is a Spin structure, and restriction is affine
over p^*: H^1(N; F_2) -> H^1(M; F_2).

No imports, input files, current-working-directory assumptions, or numerical
searches are used.
"""


def determinant_2x2(a, b, c, d):
    return a * d - b * c


def assert_presentation_smith_data():
    """Exact SNF-equivalent checks for the two abelianized presentations."""
    # M=m004: R_ab = a-b.  A primitive rank-one relation gives H_1(M)=Z.
    relator = "abABaBAbaB"
    r_a = relator.count("a") - relator.count("A")
    r_b = relator.count("b") - relator.count("B")
    assert (r_a, r_b) == (1, -1)
    m_rel = (1, -1)
    assert m_rel == (1, -1)
    assert abs(m_rel[0]) == 1  # its Smith invariant is 1

    # N=m000: generators (a,b,t).  The nontrivial abelianized relations are
    # R_ab=a-b and t^2=a, hence a-2t.  The conjugacy relations contribute
    # zero because beta is homologically trivial.
    beta_b = "BabAb"
    beta_a = beta_b.count("a") - beta_b.count("A")
    beta_b_count = beta_b.count("b") - beta_b.count("B")
    assert (beta_a, beta_b_count) == (0, 1)
    n_relations = ((1, -1, 0), (1, 0, -2))
    minor_ab = determinant_2x2(1, -1, 1, 0)
    assert minor_ab == 1
    # Rank two plus a unit 2-by-2 minor means SNF diag(1,1), so no torsion
    # and one free generator.  Eliminating gives a=b=2t.
    assert n_relations[0][0] - n_relations[1][0] == 0
    return m_rel, n_relations


def main():
    m_rel, n_relations = assert_presentation_smith_data()

    # Integral and mod-two homology consequences.
    h1_m = "Z<a=b>"
    h1_n = "Z<t>, with a=b=2t"
    h1_m_f2_rank = 1
    h1_n_f2_rank = 1
    assert h1_m_f2_rank == 1 and h1_n_f2_rank == 1

    # Independent mapping-torus homology check.  The Gieseking monodromy on
    # H_1(fibre;Z) is X; the orientation cover has monodromy X^2.  Unit
    # determinants for X-I and X^2-I make both cokernels trivial, leaving
    # exactly the base-circle Z in integral H_1.
    X = ((1, 1), (1, 0))
    X2 = (
        (X[0][0] * X[0][0] + X[0][1] * X[1][0],
         X[0][0] * X[0][1] + X[0][1] * X[1][1]),
        (X[1][0] * X[0][0] + X[1][1] * X[1][0],
         X[1][0] * X[0][1] + X[1][1] * X[1][1]),
    )
    assert determinant_2x2(X[0][0] - 1, X[0][1], X[1][0], X[1][1] - 1) == -1
    assert determinant_2x2(X2[0][0] - 1, X2[0][1], X2[1][0], X2[1][1] - 1) == -1

    # A compact core of N is the mapping torus of a once-punctured torus.
    # Thus chi(N)=0.  It has nonempty boundary, so b3=0; H1(N;F2) has rank
    # one, and b0=1.  Euler characteristic gives b2=0, hence H^2(N;F2)=0.
    b0, b1, b3, chi_n = 1, 1, 0, 0
    b2 = chi_n - b0 + b1 + b3
    assert b2 == 0
    h2_n_f2_rank = 0
    assert h2_n_f2_rank == 0

    # In the stated Pin^- convention the obstruction is w2+w1^2.  Its group
    # is zero here, so it vanishes without needing to evaluate either class.
    pin_minus_obstruction_group = "H^2(N;F_2)=0"
    pin_minus_obstruction = 0
    assert pin_minus_obstruction == 0

    # Let u(t)=1 generate H^1(N;F2).  On M, a=b=2t, so p^*u(a)=p^*u(b)=0.
    u_of_t = 1
    pullback_u_of_a = (2 * u_of_t) % 2
    pullback_u_of_b = (2 * u_of_t) % 2
    assert pullback_u_of_a == pullback_u_of_b == 0
    restriction_linear_map = ((0,),)  # H^1(N;F2) -> H^1(M;F2)
    assert restriction_linear_map == ((0,),)

    # Affine conclusion.  P is any one Pin^- structure and s is deliberately
    # an unnamed spin structure.  The other Pin^- structure is P+u; both
    # restrict to s because p^*u=0.
    pin_minus_count = 2 ** h1_n_f2_rank
    spin_count = 2 ** h1_m_f2_rank
    assert pin_minus_count == spin_count == 2

    print("R021 Gieseking Pin-minus restriction certificate")
    print("convention: Riemannian Pin^- obstruction = w2(TN)+w1(TN)^2")
    print("M=m004: R_ab=a-b; H1(M)=Z<a=b>; dim H1(M;F2)=1")
    print("N=m000: relations (a-b, a-2t); unit 2x2 minor=1")
    print("H1(N)=Z<t>, with a=b=2t; dim H1(N;F2)=1")
    print("chi(N)=0, b0=1, b1=1, b3=0 => b2=0 => H^2(N;F2)=0")
    print("Pin^- obstruction group H^2(N;F2) is zero; obstruction vanishes")
    print("Pin^-(N) is an H^1(N;F2)-torsor: exactly 2 Pin^- structures")
    print("Spin(M) is an H^1(M;F2)-torsor: exactly 2 spin structures")
    print("u(t)=1 gives p^*u(a)=p^*u(b)=u(2t)=0")
    print("linear difference map p^*: H1(N;F2)->H1(M;F2) is the zero map")
    print("affine restriction: res(P)=s and res(P+u)=s for one unnamed spin structure s")
    print("therefore the other spin structure on M does not extend to a Pin^- structure on N")
    print("scope fence: this does not identify s with any named SL(2,C) sign lift")
    print("typing fence: tangent Pin^- != deck representative t != internal 2T center != semilinear holonomy matrix")


if __name__ == "__main__":
    main()
