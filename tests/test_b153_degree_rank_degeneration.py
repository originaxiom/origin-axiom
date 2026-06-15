"""B153 -- rank-stratified degeneration of degree=rank (V142).

Locks the deterministic facts: the toolkit self-test (B89 n=4: L=-M^4, irreducible, slice tangent 19),
and the n=5 semisimple involution argument (A^2=I => B=tAt^-1 => B^2=I => dihedral => reducible).
The n=3 rigid component and the n=5 non-semisimple absence are numerical/Sage results recorded in
FINDINGS.md (not in this fast test).
"""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
B153 = ROOT / "frontier" / "B153_degree_rank_degeneration"


def _toolkit():
    spec = importlib.util.spec_from_file_location("sln_toolkit", B153 / "sln_toolkit.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def test_toolkit_selftest_n4_slice():
    tk = _toolkit()
    tk._selftest()  # asserts B89 n=4: L=-M^4, irreducible, tangent 19, spectrum moves (slice)


def test_n5_semisimple_is_dihedral_reducible():
    """A^2=I => B=A^-2 t A t^-1 = t A t^-1 => B^2 = t A^2 t^-1 = I, for ANY t."""
    tk = _toolkit()
    A = np.diag([1, 1, 1, -1, -1]).astype(complex)
    assert np.allclose(A @ A, np.eye(5))
    rng = np.random.default_rng(1)
    for _ in range(5):
        t = rng.standard_normal((5, 5)) + 1j * rng.standard_normal((5, 5))
        B = tk.Bfrom(A, t)
        assert np.allclose(B @ B, np.eye(5), atol=1e-8)  # B is an involution => <A,B> dihedral => reducible


def test_probe_runs():
    spec = importlib.util.spec_from_file_location("b153_probe", B153 / "probe.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert m.check_n4_slice() and m.check_n5_semisimple_dihedral()
