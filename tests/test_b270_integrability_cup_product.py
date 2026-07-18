"""B270 locks -- integrability recomputed: the cup-product obstruction vanishes (SL(2)/Sym^2 smooth, computed),
and dim H^1(T^2,Sym^{2m})=2 (half-lives-half-dies => deformations are cusp deformations => integrate).
FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B270_integrability_cup_product" / "integrability_cup_product.py"
_spec = importlib.util.spec_from_file_location("b270", _PATH)
b270 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): integrability_cup_product sets no dps of its own
# but internally imports B264's e6_charvar_tangent, which sets mp.mp.dps=80 at
# module level (that import computes its own constants under its own dps);
# restore the entry dps after the collection-time import so the assignment
# cannot leak into later-collected modules.
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b270)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_80():
    # E12 repair (the b204 pattern): the runtime entry points call b264.symn and
    # SVD ranks with 1e-50-class tolerances; pin the dps=80 the embedded b264
    # dependency declares (the ambient precision of the module's own __main__
    # run), per test.
    saved = mp.mp.dps
    mp.mp.dps = 80
    yield
    mp.mp.dps = saved


def test_cup_product_obstruction_vanishes():
    r = b270.cup_product_obstruction_vanishes()
    assert r["dimZ1"] == 4 and r["dimB1"] == 3 and r["dimH1"] == 1
    assert r["cocycle"] is True
    assert r["obstruction_is_coboundary"] is True          # [Q(xi)]=0 in H^2 => smooth, computed


def test_cusp_mechanism_all_exponents():
    # dim H^1(T^2, Sym^{2m}) = 2 for every E6 exponent -> half = 1 = dim H^1(M) -> boundary-detected -> integrable
    for m in [1, 4, 5, 7, 8, 11]:
        assert b270.peripheral_h1_dim(m) == 2
