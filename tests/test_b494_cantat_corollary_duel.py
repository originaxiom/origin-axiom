"""Locks for B494 (CL-1b duel: the held-breath field law vs Cantat's fixed-curve method).

Recompute locks, all exact sympy (no pari dependency here; probe.py carries the pari
ground truth): (1) the mandatory CONTROL — Cantat's pseudo-Anosov [[2,1],[1,1]]: trace
action verified on honest SL2 words, fixed curve (x, x/(x-1), x), quartic
x^4-3x^3+x^2+4x-2 at kappa = 0, splitting over Q(sqrt(17)); (2) the degeneration-to-swap
mechanism with a negative control; (3) the d = 3 / 5 / 8 field computations including the
d = 5 erratum content (splits over Q(sqrt5), irreducible over Q(sqrt41), Norm = 41);
(4) the NEW m = 7 adjudication — Norm_{Q(tau_7)/Q}(Delta_7) = -239, true field degree
6 = phi(7), Q(sqrt(-239)) not even a subfield: the banked row is the same norm-vs-field
conflation, extending the 2026-07-09 erratum; (5) the completeness certificate (transfer-
matrix lemma ingredients, m <= 12) plus brute Groebner agreement at m = 6, 7, 12, 14;
(6) documentation-integrity lock on FINDINGS.md (verdict COROLLARY, firewall untouched).
"""
import pathlib

import sympy as sp

x, y, z, tau = sp.symbols('x y z tau')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B494_cantat_corollary_duel" / "FINDINGS.md").read_text(encoding="utf-8")

# generic det-1 matrices for honest trace verification
_a1, _a2, _a3, _b1, _b2, _b3 = sp.symbols('_a1 _a2 _a3 _b1 _b2 _b3')
_A = sp.Matrix([[_a1, _a2], [_a3, (1 + _a2*_a3)/_a1]])
_B = sp.Matrix([[_b1, _b2], [_b3, (1 + _b2*_b3)/_b1]])
_X, _Y, _Z = sp.cancel(_A.trace()), sp.cancel(_B.trace()), sp.cancel((_A*_B).trace())


def _trace_poly_ok(word, poly):
    M = sp.eye(2)
    for ch in word:
        M = M * (_A if ch == 'A' else _B)
    return sp.cancel(poly.subs({x: _X, y: _Y, z: _Z}, simultaneous=True) - M.trace()) == 0


def _t_seq(m, t0v, t1v, mult):
    t = {0: t0v, 1: t1v}
    for k in range(2, m + 2):
        t[k] = sp.expand(mult*t[k-1] - t[k-2])
    return t


def _minpoly(d, var):
    return sp.minimal_polynomial(2*sp.cos(2*sp.pi/d), var)


def _E(d):
    """z-eliminant of the order-d symmetric cusp point."""
    return sp.expand(sp.resultant(_minpoly(d, tau), z**2 - tau**2*z + 2*tau**2, tau))


def _norm_delta(d):
    return sp.resultant(_minpoly(d, tau), sp.expand(tau**2*(tau**2 - 8)), tau)


def _irreducible(poly, var, ext=None):
    fl = sp.factor_list(poly, extension=ext) if ext is not None else sp.factor_list(poly)
    nontriv = [f for f, _ in fl[1] if f.free_symbols]
    return len(nontriv) == 1 and nontriv[0].as_poly(var).degree() == sp.Poly(poly, var).degree()


# ---------------------------------------------------------------- (1) the mandatory control
def test_control_cantat_fixed_curve_quartic_and_sqrt17():
    Tc = (z, y*z - x, y*z**2 - x*z - y)          # psi_c: A -> BA, B -> BAB (class [[2,1],[1,1]])
    assert _trace_poly_ok("BA", Tc[0]) and _trace_poly_ok("BAB", Tc[1]) and _trace_poly_ok("BABAB", Tc[2])
    assert sp.expand(KAPPA.subs(dict(zip((x, y, z), Tc)), simultaneous=True) - KAPPA) == 0
    G = sp.groebner([sp.expand(Tc[0]-x), sp.expand(Tc[1]-y), sp.expand(Tc[2]-z)], z, y, x, order='lex')
    assert set(map(sp.expand, G.exprs)) == {sp.expand(z - x), sp.expand(x*y - x - y)}  # (x, x/(x-1), x)
    kc = sp.cancel(KAPPA.subs({y: x/(x-1), z: x}, simultaneous=True))
    quartic = sp.expand(sp.numer(kc))
    assert quartic == sp.expand(x**4 - 3*x**3 + x**2 + 4*x - 2)      # Cantat's quartic (kappa = 0)
    assert _irreducible(quartic, x)
    degs = sorted(sp.Poly(f, x).degree() for f, _ in sp.factor_list(quartic, extension=sp.sqrt(17))[1])
    assert degs == [2, 2]                                            # splits over Q(sqrt(17))


def test_control_is_the_m1_monodromy_and_fig8_anchor():
    T1 = (z, x, sp.expand(x*z - y))                                  # sigma_1: a -> ab, b -> a
    T1sq = tuple(sp.expand(c.subs({x: T1[0], y: T1[1], z: T1[2]}, simultaneous=True)) for c in T1)
    assert T1sq == (sp.expand(x*z - y), z, sp.expand(x*z**2 - y*z - x))   # = trace map of [[2,1],[1,1]]
    # the same pipeline at kappa = -2 recovers the figure-eight trace field Q(sqrt(-3))
    fig8 = sp.numer(sp.cancel((KAPPA + 2).subs({y: x/(x-1), z: x/(x-1)}, simultaneous=True)))
    assert sp.factor(fig8) == sp.factor(x**2*(x**2 - 3*x + 3))
    assert sp.discriminant(x**2 - 3*x + 3, x) == -3


# ---------------------------------------------------------------- (2) degeneration mechanism
def test_sigma_m_trace_action_and_degeneration_to_swap():
    for m in (1, 2, 3):
        t = _t_seq(m, y, z, x)
        assert _trace_poly_ok("A"*m + "B", t[m]) and _trace_poly_ok("A"*(m+1) + "B", t[m+1])
    for (d, m) in [(3, 6), (5, 10), (7, 14), (8, 16)]:               # T_m == swap on {x = tau_d}, d | m
        psi = _minpoly(d, x)
        t = _t_seq(m, y, z, x)
        assert sp.rem(sp.expand(t[m] - y), psi, x) == 0
        assert sp.rem(sp.expand(t[m+1] - z), psi, x) == 0
    psi = _minpoly(5, x)                                             # negative control: 5 does not divide 7
    t = _t_seq(7, y, z, x)
    assert sp.rem(sp.expand(t[7] - y), psi, x) != 0


def test_cusp_quadratic_and_total_negativity():
    t_ = sp.symbols('t')
    cusp = sp.expand((KAPPA + 2).subs({x: t_, y: t_}, simultaneous=True))
    assert cusp == sp.expand(z**2 - t_**2*z + 2*t_**2)
    assert sp.factor(sp.discriminant(cusp, z)) == sp.factor(t_**2*(t_**2 - 8))
    assert cusp.subs(t_, 0) == z**2                                  # d = 4 collapse (tau_4 = 0)
    for d in (3, 5, 7, 8):                                           # Delta_d totally negative => deg 2 exact
        assert all(sp.sign(sp.expand((tau**2*(tau**2 - 8)).subs(tau, r))) == -1
                   for r in sp.Poly(_minpoly(d, tau), tau).all_roots())


# ---------------------------------------------------------------- (3) d = 3 / 5 / 8 fields
def test_d3_field_is_sqrt_minus7():
    assert _E(3) == sp.expand(z**2 - z + 2)
    assert sp.discriminant(_E(3), z) == -7
    assert _E(6) == _E(3)                                            # coincident d=3/d=6 z-point


def test_d5_field_correction_content():
    E5 = _E(5)
    assert E5 == sp.expand(z**4 - 3*z**3 + 7*z**2 - 4*z + 4)         # the banked quartic, verbatim
    assert _irreducible(E5, z)                                       # degree 4, not 2
    assert sp.discriminant(E5, z) == 2**4 * 5**2 * 41
    degs = sorted(sp.Poly(f, z).degree() for f, _ in sp.factor_list(E5, extension=sp.sqrt(5))[1])
    assert degs == [2, 2]                                            # contains Q(sqrt5)
    assert _irreducible(E5, z, ext=sp.sqrt(41))                      # Q(sqrt41) was never the field
    assert _norm_delta(5) == 41                                      # the banked 41 is the NORM


def test_d8_collapse_explains_m8_m16_row():
    assert sp.factor(_E(8)) == sp.factor((z**2 - 2*z + 4)**2)        # tau_8^2 = 2 rational
    assert sp.discriminant(z**2 - 2*z + 4, z) == -12                 # => Q(sqrt(-3))


# ---------------------------------------------------------------- (4) the m = 7 adjudication
def test_m7_norm_is_minus239_and_field_is_degree6():
    E7 = _E(7)
    assert E7 == sp.expand(z**6 - 5*z**5 + 16*z**4 - 25*z**3 + 30*z**2 - 12*z + 8)
    assert sp.Poly(E7, z).degree() == 6 == sp.totient(7)
    assert _irreducible(E7, z)                                       # true field degree 6, not 2
    assert _norm_delta(7) == -239                                    # the banked -239 is the NORM
    D7 = sp.discriminant(E7, z)
    assert dict(sp.factorint(D7)) == {-1: 1, 2: 12, 7: 4, 239: 1}    # sf part -239: the label's origin
    assert _irreducible(E7, z, ext=sp.sqrt(-239))                    # Q(sqrt(-239)) not even a subfield


# ---------------------------------------------------------------- (5) completeness certificate
def test_completeness_transfer_matrix_certificate():
    MAXM = 12
    F = {0: sp.Integer(0), 1: sp.Integer(1)}
    for k in range(2, MAXM + 3):
        F[k] = sp.expand(x*F[k-1] - F[k-2])
    M = sp.Matrix([[x, -1], [1, 0]])
    Mk = sp.eye(2)
    for m in range(1, MAXM + 1):
        Mk = (Mk*M).applyfunc(sp.expand)
        assert Mk == sp.Matrix([[F[m+1], -F[m]], [F[m], -(F[m-1] if m >= 1 else sp.Integer(-1))]])
        assert sp.expand((Mk - sp.eye(2)).det() - (2 - Mk.trace())) == 0
        # eigenvalue locus: 2 - tr M^m = -(x-2)(x+2)^[2|m] prod_{d|m, d>=3} Psi_d^2
        got = {sp.expand(f): mult for f, mult in sp.factor_list(sp.expand(2 - Mk.trace()))[1]}
        expect = {sp.expand(x - 2): 1}
        if m % 2 == 0:
            expect[sp.expand(x + 2)] = 1
        for d in sp.divisors(m):
            if d >= 3:
                expect[sp.expand(_minpoly(d, x))] = 2
        assert got == expect
        for d in sp.divisors(m):                                     # whole line fixed at x = tau_d
            if d >= 3:
                assert Mk.applyfunc(lambda e: sp.rem(sp.expand(e), _minpoly(d, x), x)) == sp.eye(2)
        # fixed system IS (M^m - I)(z, x)^T = 0 (t_0 = x, t_1 = z)
        tt = _t_seq(m, x, z, x)
        v = (Mk - sp.eye(2)) * sp.Matrix([z, x])
        assert sp.expand(v[0] - (tt[m+1] - z)) == 0 and sp.expand(v[1] - (tt[m] - x)) == 0
    # isolated boundary points are off the cusp; trivial point is on it
    assert KAPPA.subs({x: 2, y: 2, z: 2}) == 2 and KAPPA.subs({x: -2, y: -2, z: 2}) == 2
    assert KAPPA.subs({x: 0, y: 0, z: 0}) == -2


def test_groebner_matches_divisor_union_prediction():
    def groebner_factors(m):
        tt = _t_seq(m, x, z, x)
        eqs = [sp.expand(tt[m] - x), sp.expand(tt[m+1] - z), sp.expand(2*x**2 + z**2 - x*x*z)]
        G = sp.groebner(eqs, x, z, order='lex')
        elim = [g for g in G.exprs if g.free_symbols <= {z}]
        poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
        return set(sp.expand(f) for f, _ in sp.factor_list(poly)[1] if f.free_symbols)

    def predicted(m):
        out = {z}
        for d in sp.divisors(m):
            if d >= 3:
                out |= set(sp.expand(f) for f, _ in sp.factor_list(_E(d))[1] if f.free_symbols)
        return out

    for m in (6, 7, 12, 14):                                         # prime, 2*prime, and 4 | m cases
        assert groebner_factors(m) == predicted(m)
    assert groebner_factors(7) - {z} == {sp.expand(_E(7))}           # the banked m=7 row IS E_7


# ---------------------------------------------------------------- (6) documentation integrity
def test_findings_verdict_and_corrections_documented():
    assert "verdict: **COROLLARY**" in _FIND
    assert "**splitting into two quadratics over ℚ(√17)**" in _FIND
    assert "z ∈ ℚ(τ_d, √(τ_d²(τ_d²−8)))" in _FIND
    assert "**Norm_{ℚ(τ₇)/ℚ}(τ₇²(τ₇²−8)) = −239 exactly.**" in _FIND
    assert "not even a subfield" in _FIND
    assert "extends the 2026-07-09 B479/B491 erratum" in _FIND
    assert "now unconditional for all m" in _FIND
    assert "Nothing to CLAIMS.md; firewall untouched." in _FIND
