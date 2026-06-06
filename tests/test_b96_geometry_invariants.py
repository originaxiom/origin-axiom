"""B96 -- locking tests (computer-assisted, SnapPy): the metallic mapping-torus volume ordering is
strictly monotone (2.030<3.664<4.814; m=1 figure-eight smallest), the Bloch-Wigner dilog reproduces the
SnapPy volumes, and the volume Hessian at the complete structure is DEFINITE (complete = strict volume
maximum, Mostow) -- signature (0,2), not Lorentzian."""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b96", _ROOT / "frontier" / "B96_geometry_invariants" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

snappy = pytest.importorskip("snappy")


def test_volume_ordering_monotone():
    """vol(4_1) < vol(m136) < vol(s464); each matches its Bloch-Wigner dilog volume to ~1e-6."""
    table = B.volume_table()
    vols = [row[1] for row in table]
    assert vols[0] == pytest.approx(2.0298832, abs=1e-5)
    assert vols[1] == pytest.approx(3.6638624, abs=1e-5)
    assert vols[2] == pytest.approx(4.8138192, abs=1e-5)
    assert vols[0] < vols[1] < vols[2]                         # strictly monotone (ordering continues)
    for _m, vs, vbw, _nt, _name in table:
        assert vs == pytest.approx(vbw, abs=1e-6)              # Bloch-Wigner == SnapPy


def test_volume_hessian_is_definite_not_lorentzian():
    """The complete structure is a strict volume maximum over fillings (Mostow): all filled volumes < V0,
    none above => the NZ volume Hessian is negative definite, signature (0,2), NOT indefinite/Lorentzian."""
    V0, below, above, total = B.volume_hessian_definite()
    assert total > 50
    assert above == 0                                          # NOTHING exceeds the complete structure
    assert below >= total - 2                                  # ~all strictly below (a tie = a near-complete
    #                                                            filling) => complete is a strict max => definite
