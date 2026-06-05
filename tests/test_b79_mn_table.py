"""B79 (Phase 1c, V64) -- locking test: the (m,n) degree table. Every COMPUTED cell has d=rank; a live
re-confirmation that the m=3 odd-metallic bundle gives M^3=L at n=3 (the m-axis cell)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b79_mn", _ROOT / "frontier" / "B79_mn_table" / "probe.py")
B79 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B79)


def test_every_computed_cell_equals_rank():
    """All computed (m,n) cells satisfy d = n (= rank)."""
    for (m, n), (d, _prov) in B79.COMPUTED.items():
        assert d == n, (m, n, d)


def test_m3_cell_reconfirms_M3():
    """Live: the m=3 metallic bundle at n=3 on {1,i,-i} gives M^3=L (the odd-m-axis cell, d(3,3)=3)."""
    found, bestk, dev = B79.reconfirm_cell(3, 3, [1, 1j, -1j], n_reps=2)
    assert found >= 1, "need an m=3 Dehn-filling rep"
    assert bestk == 3 and dev < 1e-9, (bestk, dev)
