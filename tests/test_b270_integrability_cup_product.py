"""B270 locks -- integrability recomputed: the cup-product obstruction vanishes (SL(2)/Sym^2 smooth, computed),
and dim H^1(T^2,Sym^{2m})=2 (half-lives-half-dies => deformations are cusp deformations => integrate).
FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B270_integrability_cup_product" / "integrability_cup_product.py"
_spec = importlib.util.spec_from_file_location("b270", _PATH)
b270 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b270)


def test_cup_product_obstruction_vanishes():
    r = b270.cup_product_obstruction_vanishes()
    assert r["dimZ1"] == 4 and r["dimB1"] == 3 and r["dimH1"] == 1
    assert r["cocycle"] is True
    assert r["obstruction_is_coboundary"] is True          # [Q(xi)]=0 in H^2 => smooth, computed


def test_cusp_mechanism_all_exponents():
    # dim H^1(T^2, Sym^{2m}) = 2 for every E6 exponent -> half = 1 = dim H^1(M) -> boundary-detected -> integrable
    for m in [1, 4, 5, 7, 8, 11]:
        assert b270.peripheral_h1_dim(m) == 2
