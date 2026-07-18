"""B570 Lane C, cell C1 -- cusp-sign propagation to the theta-odd H^1 deformation direction.

Reuses the banked B347 machinery (frontier/B347_e6_tangent_gradings/e6_tangent_gradings.py):
rho0 = geometric holonomy of 4_1 over Q(sqrt3, i), with sqrt(-3) = +i*sqrt(3) (the B486
cusp-sign convention tau = +2*sqrt(-3)); H^1(4_1, Sym^{2m}) at the six E6 exponents
m in {1,4,5,7,8,11}; the amphichiral (orientation-reversing) involution J, realized by the
pi_1-automorphism a->ababAB, b->baBA composed with entrywise complex conjugation
(= the geometric action of flipping the sign of sqrt(-3)).

Result locked here: J^2 = +1 EXACTLY on every one of the six 1-dim lines, including both
theta-odd exponents {4,8} -- but this is a TAUTOLOGY of linear algebra (any antilinear
self-map J of a 1-dim C-vector space satisfies J^2 = |c|^2 * id, always real >=0; see
test_j_squared_is_forced_nonneg_for_any_antilinear_map_on_a_line), so it carries ZERO
exponent-discriminating information. The finer quantity -- the antilinear coefficient
lambda with J(z0) = lambda * z0 in the code's natural Fox-cochain basis -- IS basis-phase
dependent (z0 -> e^{i phi} z0 sends lambda -> e^{-2i phi} lambda) and hence not a gauge
invariant "sign"; computed in the natural convention it is a GENERIC (non-real) phase on
theta-odd (m=4,8) exponents, uniformly with the theta-even ones. No preferred sign
propagates to the theta-odd direction. NULL banked.

Place at tests/test_b570_c1_cusp_sign.py (sibling of tests/test_b347_e6_tangent_gradings.py,
same sys.path convention) to run against the live repo.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B347_e6_tangent_gradings'))
import mpmath as mp
import pytest

# E12 (module-level-dps sweep): e6_tangent_gradings sets mp.mp.dps=70 at module
# level. In a full-suite run test_b347 imports it first and this import is a
# sys.modules cache hit (no re-execution), but in a single-file run THIS import
# executes the module and would leak the assignment; save/restore covers both.
_saved_dps = mp.mp.dps
from e6_tangent_gradings import (
    EXPONENTS, _BASE, _AMPHI, _HYPER, _line_eigenvalue, _guard,
)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_70():
    # E12 repair (the b204 pattern): most tests _guard() to 70 themselves; pin
    # the same dps=70 per test as well so the ungarded paths (e.g. the pure
    # linear-algebra tautology test) never depend on the collection-time global.
    saved = mp.mp.dps
    mp.mp.dps = 70
    yield
    mp.mp.dps = saved

THETA_ODD = [4, 8]
THETA_EVEN = [1, 5, 7, 11]


def test_cusp_sign_convention_matches_b486():
    # tau = +2*sqrt(-3) (B486 rectangular-cusp convention): sqrt(-3) = +i*sqrt(3) here.
    _guard()
    a00 = _BASE["a"][0, 0]
    assert abs(a00 - mp.mpc(-2, -mp.sqrt(3))) < mp.mpf(10) ** -60


def test_amphichiral_D_solves_its_defining_relation():
    # rho(a->ababAB) = D * conj(rho(a)) * D^-1 ,  rho(b->baBA) = D * conj(rho(b)) * D^-1
    _guard()
    D = _AMPHI["D"]
    assert abs(mp.det(D) - 1) < mp.mpf(10) ** -60
    from e6_tangent_gradings import _ev
    target = {"a": ("ababAB", True), "b": ("baBA", True)}
    for g in "ab":
        word, conj = target[g]
        L = _ev(word)
        Rc = mp.matrix([[mp.conj(_BASE[g][i, j]) for j in range(2)] for i in range(2)]) if conj else _BASE[g]
        assert mp.norm(L - D * Rc * D ** -1) < mp.mpf(10) ** -55


def test_amphichiral_and_hyperelliptic_automorphisms_are_different_maps():
    # c (orientation-reversing, amphichiral) and theta (orientation-preserving, hyperelliptic)
    # are literally different automorphisms of pi_1(4_1) -- distinct word substitutions.
    assert _AMPHI["sinv"] != _HYPER["sinv"]
    assert _AMPHI["conjugate"] is True and _HYPER["conjugate"] is False


def test_j_squared_forced_plus_one_on_every_exponent_including_theta_odd():
    _guard()
    for m in EXPONENTS:
        mu = _line_eigenvalue(m, _AMPHI, square=True)
        assert abs(mu.imag) < mp.mpf(10) ** -25
        assert abs(mu.real - 1) < mp.mpf(10) ** -25
    for m in THETA_ODD:
        mu = _line_eigenvalue(m, _AMPHI, square=True)
        assert abs(mu.real - 1) < mp.mpf(10) ** -25          # no theta-odd-specific deviation


def test_j_squared_is_forced_nonneg_for_any_antilinear_map_on_a_line():
    # Pure-algebra sanity: J(v) = c*conj(v) on a 1-dim C-line => J^2(v) = |c|^2 * v, ALWAYS
    # real and >=0 -- so "J^2 = +1" can structurally never discriminate exponents.
    import random
    random.seed(0)
    for _ in range(20):
        c = complex(random.uniform(-3, 3), random.uniform(-3, 3))
        v = complex(random.uniform(-2, 2), random.uniform(-2, 2))
        Jv = c * v.conjugate()
        JJv = c * Jv.conjugate()
        ratio = JJv / v
        assert abs(ratio.imag) < 1e-12
        assert ratio.real >= -1e-12


def test_amphichiral_phase_is_generic_not_real_on_theta_odd_lines():
    # The basis-dependent coefficient lambda (J(z0) = lambda*z0 in the natural Fox-cochain
    # basis) is NOT close to +-1 (real) on either theta-odd exponent -- no natural sign.
    _guard()
    for m in THETA_ODD:
        lam = _line_eigenvalue(m, _AMPHI, square=False)
        assert abs(abs(lam) - 1) < mp.mpf(10) ** -25          # |lambda| = 1 (unitary, forced)
        assert abs(lam.imag) > mp.mpf("0.1")                  # far from real: no preferred sign


def test_amphichiral_phase_is_generic_uniformly_theta_even_too():
    # The same genericity holds on ALL six exponents -- theta-odd is not special/singled out.
    _guard()
    for m in EXPONENTS:
        lam = _line_eigenvalue(m, _AMPHI, square=False)
        assert abs(lam.imag) > mp.mpf("0.1")


def test_no_theta_parity_pattern_in_the_phases():
    # The phases of theta-odd {4,8} do not cluster differently from theta-even {1,5,7,11}
    # under any obvious statistic (both sets span a similar |Im(lambda)| range).
    _guard()
    odd_im = sorted(abs(_line_eigenvalue(m, _AMPHI, square=False).imag) for m in THETA_ODD)
    even_im = sorted(abs(_line_eigenvalue(m, _AMPHI, square=False).imag) for m in THETA_EVEN)
    # odd range [0.38, 0.45] sits strictly inside the even range [0.13, 0.997] -- no separation
    assert min(even_im) < min(odd_im) and max(odd_im) < max(even_im)
