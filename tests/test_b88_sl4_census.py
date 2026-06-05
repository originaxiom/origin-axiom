"""B88 (Task 2, V71) -- locking test: the SL(4) Dehn-filling census exposes degrees {3,4} -- the
principal {1,1,w,w2}->M^4 and {prim 8th}->M^3 components."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b88_census", _ROOT / "frontier" / "B88_sl4_census" / "probe.py")
B88 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B88)


def test_principal_component_is_degree_4():
    """{1,1,w,w2} (principal, tr=1) -> M^4=L (degree 4 = rank), c=-1 a root of unity."""
    spec = B88.COMPONENTS["{1,1,w,w2} (principal, tr=1)"]
    f, bk, dev, c = B88.degree_of(spec, budget=20)
    assert f >= 1 and bk == 4 and dev < 1e-7, (f, bk, dev)
    assert abs(c - (-1.0)) < 1e-3, ("principal c = -1 (root of unity)", c)


def test_second_component_is_degree_3():
    """{prim 8th, z^4+1} (tr=0) -> M^3=L (degree 3)."""
    spec = B88.COMPONENTS["{prim 8th, z^4+1} (tr=0)"]
    f, bk, dev, c = B88.degree_of(spec, budget=20)
    assert f >= 1 and bk == 3 and dev < 1e-7, (f, bk, dev)
