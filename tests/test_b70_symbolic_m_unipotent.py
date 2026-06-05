"""B70 (P5, V51) -- the symbolic-m unipotent expansion tools are correct.

Locks that A0^m = sum_{j<n} C(m,j) N^j and d/deps((I+eps g)A0)^m = sum C(...) N^j g N^k (symbolic in m)
match direct matrix powers at integer m -- the V45-enabled tool for symbolic-m matrix work."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b70_symu", _ROOT / "frontier" / "B70_trace_ring" / "symbolic_m_unipotent.py")
su = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(su)


def test_symbolic_m_unipotent_powers_match():
    assert su.validate(3)
    assert su.validate(4)
