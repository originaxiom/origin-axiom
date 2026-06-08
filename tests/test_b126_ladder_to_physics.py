"""Locks for B126 -- the ladder to physics (how far the metallic rigidity propagates).

Pure-math facts always run: H_1(M_m) = Z (+) (Z/m)^2 (SNF), and the kappa-degree pattern m=1..4. The SnapPy
homology cross-check is guarded (skips when SnapPy is absent).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b126_probe", _ROOT / "frontier/B126_ladder_to_physics/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B126 = _load()


def test_homology_torsion_is_metallic_parameter():
    h = B126.homology_torsion(mmax=7)
    assert h["torsion_is_Zm_squared"]   # H_1(M_m) = Z (+) (Z/m)^2 for all m=1..7


def test_kappa_degree_arithmetic_simplicity():
    # m=1,2 (arithmetic) -> kappa rational in z (degree 1); m=3,4 acquire a degree-3 geometric component.
    assert max(B126.kappa_degree(1)) == 1
    assert max(B126.kappa_degree(2)) == 1
    assert max(B126.kappa_degree(3)) == 3
    assert max(B126.kappa_degree(4)) == 3
    assert B126.ARITHMETIC == (1, 2)


def test_snappy_homology_crosscheck_if_available():
    pytest.importorskip("snappy")
    snap = B126.homology_torsion_snappy(mmax=4)
    assert snap is not None
    assert snap[1] == "Z"
    assert "Z/2 + Z/2" in snap[2]
    assert "Z/3 + Z/3" in snap[3]
    assert "Z/4 + Z/4" in snap[4]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
