"""B264 locks -- the E6 character variety of the figure-eight: tangent dim at the principal rep = rank(E6) = 6,
deformation directions beyond F4. dim H^1(pi1(4_1), Sym^{2k}) = 1 for all k (matches Menal-Ferrer-Porti / Thurston).
FIREWALLED (flat-connection geometry, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B264_e6_character_variety" / "e6_charvar_tangent.py"
_spec = importlib.util.spec_from_file_location("b264", _PATH)
b264 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): e6_charvar_tangent sets mp.mp.dps=80 at module
# level and computes its import-time matrices under that dps itself; restore the
# entry dps after the collection-time import so the assignment cannot leak into
# later-collected modules.
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b264)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_80():
    # E12 repair (the b204 pattern): H1_sym self-guards to 80 internally, but pin
    # the module's declared dps=80 per test anyway so every entry point (incl.
    # adjoint_tangent_dim) runs at the precision its 1e-50 rank tolerances need.
    saved = mp.mp.dps
    mp.mp.dps = 80
    yield
    mp.mp.dps = saved


def test_sym2_matches_thurston():
    # the figure-eight deforms: dim H^1(adjoint = Sym^2) = 1 (Thurston). The non-negotiable anchor.
    assert b264.H1_sym(1) == 1


def test_h1_is_one_for_all_exponents():
    # Menal-Ferrer-Porti: dim H^1(Sym^{2k}) = #cusps = 1 for all k>=1
    for k in range(1, 12):
        assert b264.H1_sym(k) == 1


def test_adjoint_tangent_equals_rank_e6():
    # sum over E6 exponents {1,4,5,7,8,11} = 6 = rank(E6): the E6 char variety is rank-dimensional at rho_prin
    assert b264.adjoint_tangent_dim() == 6
    assert sorted(set(b264.E6_EXPONENTS) - set(b264.F4_EXPONENTS)) == [4, 8]   # directions escaping F4
