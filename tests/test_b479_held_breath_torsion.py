"""B479 — held breath = torsion: full sympy recompute of the exact certificates.

Locks: the held-breath eliminant Fix(sigma_m) on the cusp kappa = -2 for small m
(m=3 -> z^2-z+2 of disc -7; m=4 -> breathless; m=6 -> the SAME point as m=3;
m=5 -> the degree-4 minpoly z^4-3z^3+7z^2-4z+4), the divisor-law field certificates
Delta_d = tau^2(tau^2-8) (d=3,8,12 -> -7,-12,-15; d=1,2,4 degenerate), and the
capstone (prime m=7 held breath = the order-7 cyclotomic trace).

FIELD CORRECTION (B491 FINDINGS R1, round-2 re-panel, 2026-07-09): the d=5 held
breath is NOT Q(sqrt(41)) as B479's FINDINGS table still says. The corrected
statement, recomputed live here: the minpoly z^4-3z^3+7z^2-4z+4 is irreducible of
degree 4 over Q, it is quadratic over Q(sqrt(5)) (sqrt(5) lies in the field), the
field discriminant is 5^2*41 = 1025 (poly disc 2^4*5^2*41), and 41 is only a
discriminant/norm factor — the product of the two per-tau discriminants is 41.
This test intentionally does NOT lock the stale sqrt(41) field label.
"""
import pathlib

import pytest
import sympy as sp

X, Z = sp.symbols("x z")
QUARTIC = Z**4 - 3 * Z**3 + 7 * Z**2 - 4 * Z + 4

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _held_components(m):
    """Nontrivial z-eliminant factors of Fix(T_m) on the cusp (y = x, kappa = -2),
    exactly as in held_breath_tower.py / held_breath_ext.py."""
    t = {0: X, 1: Z}
    for k in range(2, m + 2):
        t[k] = sp.expand(X * t[k - 1] - t[k - 2])
    eqs = [sp.expand(t[m] - X), sp.expand(t[m + 1] - Z),
           sp.expand(2 * X**2 + Z**2 - X * X * Z)]
    G = sp.groebner(eqs, X, Z, order="lex")
    elim = [g for g in G.exprs if g.free_symbols <= {Z}]
    poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
    return [sp.expand(f) for f, _ in sp.factor_list(poly)[1] if sp.Poly(f, Z).degree() > 1 or sp.solve(f, Z)[0] != 0]


def test_held_breath_tower_small_m():
    """m=3: the disc -7 point z^2-z+2; m=4: breathless; m=6: SAME point as m=3
    (3|m law); m=5: the degree-4 component (5|m law)."""
    c3 = _held_components(3)
    assert c3 == [Z**2 - Z + 2]
    assert sp.discriminant(c3[0], Z) == -7
    assert _held_components(4) == []                      # m=4 holds no breath
    assert (Z**2 - Z + 2) in _held_components(6)          # same point for 3|m
    assert QUARTIC in _held_components(5)                 # the d=5 component


def test_d5_field_corrected_degree4_over_Qsqrt5_not_sqrt41():
    """B491 R1 correction, recomputed live: irreducible degree-4 minpoly; poly disc
    2^4 * 5^2 * 41; splits into two quadratics over Q(sqrt5); sqrt5 IS in the field
    (so it is quadratic over Q(sqrt5)); it stays irreducible over Q(sqrt41), so the
    field is NOT Q(sqrt41) — 41 enters only through the discriminant."""
    assert sp.Poly(QUARTIC, Z).degree() == 4
    assert sp.factor_list(QUARTIC)[1] == [(QUARTIC, 1)]   # irreducible over Q
    disc = sp.discriminant(QUARTIC, Z)
    assert disc == 16400
    assert sp.factorint(16400) == {2: 4, 5: 2, 41: 1}     # = 2^4 * 5^2 * 41
    # squarefree part 41 (16400 = 20^2 * 41) — the source of the stale "sqrt41" misread
    assert 16400 == 20**2 * 41
    assert sp.factorint(16400 // 20**2) == {41: 1}
    # two conjugate quadratics over Q(sqrt5)
    facs5 = sp.factor_list(QUARTIC, extension=sp.sqrt(5))[1]
    assert len(facs5) == 2 and all(sp.Poly(f, Z).degree() == 2 for f, _ in facs5)
    # sqrt5 in K = Q[z]/(QUARTIC): w = 3 - 2 z^2 (z-2)^{-1} satisfies w^2 = 5 mod q
    inv = sp.invert(Z - 2, QUARTIC, Z)
    w = sp.expand(3 - 2 * Z**2 * inv)
    assert sp.rem(sp.expand(w**2 - 5), QUARTIC, Z) == 0
    # NOT Q(sqrt41): the quartic does not even split over Q(sqrt41)
    facs41 = sp.factor_list(QUARTIC, extension=sp.sqrt(41))[1]
    assert facs41 == [(QUARTIC, 1)]


def test_d5_field_discriminant_is_5sq_times_41():
    """The corrected 'disc 5^2*41' of B491 R1 is the FIELD discriminant: nfdisc of
    the quartic = 1025 = 5^2 * 41 (pari, shipped with snappy)."""
    cypari = pytest.importorskip("cypari")
    assert int(cypari.pari("nfdisc(x^4-3*x^3+7*x^2-4*x+4)")) == 1025 == 5**2 * 41


def test_41_is_the_norm_of_the_per_tau_discriminants():
    """The quartic = product of the two golden-tau cusp quadratics z^2 - tau^2 z
    + 2 tau^2 (tau = 2cos(2pi/5), 2cos(4pi/5)); the per-tau discriminants
    tau^2(tau^2-8) have norm exactly 41 — '41' is a norm factor, not a field."""
    taus = [sp.nsimplify(2 * sp.cos(2 * sp.pi / 5)), sp.nsimplify(2 * sp.cos(4 * sp.pi / 5))]
    prod = sp.expand((Z**2 - taus[0]**2 * Z + 2 * taus[0]**2)
                     * (Z**2 - taus[1]**2 * Z + 2 * taus[1]**2))
    assert sp.simplify(prod - QUARTIC) == 0
    discs = [sp.simplify(t**2 * (t**2 - 8)) for t in taus]
    assert sp.simplify(discs[0] * discs[1]) == 41


def test_divisor_law_field_certificates():
    """Addendum certificates: Delta_d = tau_d^2(tau_d^2 - 8) gives -7 (d=3),
    -12 ~ Q(sqrt-3) (d=8), -15 (d=12); d = 1, 2, 4 are degenerate (|tau| = 2 or 0),
    which is exactly why m = 1, 2, 4 are breathless."""
    delta = {}
    for d in (1, 2, 3, 4, 8, 12):
        tau = sp.nsimplify(2 * sp.cos(2 * sp.pi / d))
        delta[d] = sp.simplify(tau**2 * (tau**2 - 8))
    assert (delta[3], delta[8], delta[12]) == (-7, -12, -15)
    assert delta[1] == delta[2] == -16 and delta[4] == 0  # parabolic / collapsed


def test_capstone_prime_m7_is_order7_torsion():
    """Capstone at prime m=7: the nontrivial factor of the x-eliminant is EXACTLY
    the minimal polynomial of 2cos(2pi/7) — the held breath is order-7 torsion."""
    m = 7
    t = {0: X, 1: Z}
    for k in range(2, m + 2):
        t[k] = sp.expand(X * t[k - 1] - t[k - 2])
    eqs = [sp.expand(t[m] - X), sp.expand(t[m + 1] - Z),
           sp.expand(2 * X**2 + Z**2 - X * X * Z)]
    G = sp.groebner(eqs, Z, X, order="lex")
    ex = [g for g in G.exprs if g.free_symbols <= {X}][0]
    cyc = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 7), X)
    assert cyc == X**3 + X**2 - 2 * X - 1
    assert any(sp.expand(f - cyc) == 0 for f, _ in sp.factor_list(ex)[1])


def test_correction_and_surviving_verdicts_documented():
    """Documentation-integrity lock (not a recompute): B491 R1 records the corrected
    d=5 field statement, and B479's still-valid verdict lines (the 3|m law and the
    held-breath-=-torsion theorem) are present. The stale sqrt(41) FIELD label in
    B479 is deliberately NOT locked."""
    b491 = (_ROOT / "frontier" / "B491_novelty_assessment" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "d=5 gives a DEGREE-4 field over ℚ(√5)" in b491
    assert "z⁴−3z³+7z²−4z+4, disc 5²·41" in b491
    assert "NOT ℚ(√41)" in b491
    b479 = (_ROOT / "frontier" / "B479_held_breath_torsion" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "3 | m ⟺ the ℚ(√−7) held breath is present" in b479
    assert "THEOREM (held breath = torsion)" in b479
