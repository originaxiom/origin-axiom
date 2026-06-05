"""B94 (Paper 0, G1) -- locking tests: squaring the proved metallic Jacobian to a det=+1 monodromy keeps
the Dickson catalog (universal) but removes every parity sign sector char(-N^k) and the (t+1) factor
(parity det=-1-specific), at SL(3) and SL(4); and degree=rank is det-agnostic (figure-eight is det=+1)."""
import importlib.util
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b94", _ROOT / "frontier" / "B94_tower_universality" / "probe.py")
B = importlib.util.module_from_spec(_spec)
sys.modules["b94"] = B
_spec.loader.exec_module(B)


def test_catalog_universal_parity_det_minus1_specific_sl3():
    r = B.universality(B._sl3_jacobian_m1(), ks=(1, 2, 3, 4))
    assert r["catalog_k"] == [1, 2, 3]            # char(N^k) all divide char(J^2): catalog universal
    assert r["sign_sectors_k"] == []             # no char(-N^k): parity removed by squaring to det=+1
    assert r["tplus1_present"] is False          # the (t+1) Cartan-parity factor also gone


def test_catalog_universal_parity_det_minus1_specific_sl4():
    r = B.universality(B._sl4_jacobian_m1(), ks=(1, 2, 3, 4))
    assert r["catalog_k"] == [1, 2, 3, 4]        # catalog universal at SL(4) too
    assert r["sign_sectors_k"] == []             # parity sectors gone
    assert r["tplus1_present"] is False


def test_degree_rank_is_det_agnostic():
    """The figure-eight bundle monodromy is [[2,1],[1,1]] (det=+1) and M^n=L holds there (B89) --
    so degree=rank is det-agnostic, unlike the tower's det=-1-specific parity."""
    fe, det = B.degree_rank_is_det_agnostic()
    assert fe == [[2, 1], [1, 1]] and det == 1
