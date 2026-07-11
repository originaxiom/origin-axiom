"""B479 erratum locks (2026-07-11) — the d=5, d=7 held-breath field labels.

The original table labelled these ℚ(√41) and ℚ(√−239) by a degree-2-only heuristic;
both integers are the NORM of the discriminant Δ_d = τ_d²(τ_d²−8), not the field.
These locks pin the corrected fields so the mislabel cannot re-enter.
Cross-checked by the parallel closure audit's B494 (Cantat-corollary duel).
"""
import sympy as sp

z, t = sp.symbols('z t')


def test_d5_field_is_degree4_subfield_sqrt5_not_sqrt41():
    q5 = z**4 - 3*z**3 + 7*z**2 - 4*z + 4
    assert sp.Poly(q5, z).is_irreducible                         # degree-4 field
    # splits into two quadratics over Q(sqrt5) -> quadratic subfield is Q(sqrt5)
    fac5 = sp.factor_list(q5, extension=sp.sqrt(5))[1]
    assert len(fac5) == 2 and all(sp.Poly(f, z).degree() == 2 for f, _ in fac5)
    # stays irreducible over Q(sqrt41) -> 41 is NOT the field
    fac41 = sp.factor_list(q5, extension=sp.sqrt(41))[1]
    assert len(fac41) == 1 and fac41[0][1] == 1
    # 41 is the squarefree part of the discriminant (a norm), not a generator
    disc = sp.discriminant(sp.Poly(q5, z))
    sf = sp.sign(disc) * sp.prod([p for p, e in sp.factorint(abs(disc)).items() if e % 2])
    assert sf == 41


def test_d7_field_is_degree6_norm_minus239_not_sqrt_minus239():
    # order-7 symmetric cusp: eliminate tau_7 (minpoly t^3+t^2-2t-1) from z^2 - tau^2 z + 2 tau^2
    Psi7 = t**3 + t**2 - 2*t - 1
    E7 = sp.expand(sp.resultant(Psi7, z**2 - t**2*z + 2*t**2, t))
    assert E7 == z**6 - 5*z**5 + 16*z**4 - 25*z**3 + 30*z**2 - 12*z + 8
    assert sp.Poly(E7, z).is_irreducible                        # degree-6 field
    # stays irreducible over Q(sqrt-239) -> no quadratic subfield; -239 is not the field
    fac = sp.factor_list(E7, extension=sp.sqrt(-239))[1]
    assert len(fac) == 1 and fac[0][1] == 1
    # -239 is the norm of Delta_7 = tau^2(tau^2-8) over Q(tau_7)
    assert sp.resultant(Psi7, t**2*(t**2 - 8), t) == -239
    # ... equivalently the squarefree part of disc(E7)
    disc = sp.discriminant(sp.Poly(E7, z))
    sf = sp.sign(disc) * sp.prod([p for p, e in sp.factorint(abs(disc)).items() if e % 2])
    assert sf == -239
