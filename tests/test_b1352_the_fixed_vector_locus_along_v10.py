"""B1352 -- the fixed-vector locus along V_10.  Fast: the two banked locus points are Sp(8) points (three unit eigenvalues, the
other 24 of the form y_i^{+-1} y_j^{+-1}; 100-digit eigenvalues) and their 27 is cyclic; the four banked V_10 points of B1350
have no unit eigenvalue.  Slow: the exact first-order table (stage C, Q(omega)) and the formal loss orders (stage D, two primes,
branches to order 6)."""
import sys, subprocess
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1352_the_fixed_vector_locus_along_v10" / "verification"
pytest.importorskip("flint")
pytest.importorskip("mpmath")


def test_the_locus_points_are_sp8_points_and_the_v10_points_are_not():
    out = subprocess.run([sys.executable, str(VER / "locus_point_is_sp8.py")], capture_output=True, text=True, timeout=1800).stdout
    locus = [l for l in out.splitlines() if "eigenvalues equal to 1: 3" in l]
    v10 = [l for l in out.splitlines() if "eigenvalues equal to 1: 0" in l]
    assert len(locus) == 4 and all("Sp(8) pattern {+-u_i +- u_j} on the other 24: YES" in l for l in locus)
    assert len(v10) == 8 and all(": NO" in l for l in v10)


def test_the_27_is_cyclic_at_the_locus_points_with_three_cusp_fixed_vectors():
    out = subprocess.run([sys.executable, str(VER / "locus_point_structure.py"), str(VER / "fixed_locus_points.json")], capture_output=True, text=True, timeout=1800).stdout
    assert out.count("cusp-fixed vectors: 3") == 2
    assert out.count("generates a submodule of dimension 27") == 6
    assert out.count("all cusp-fixed vectors together generate dimension 27") == 2


@pytest.mark.slow
def test_the_v10_direction_keeps_all_three_cusp_fixed_vectors_to_first_order():
    out = subprocess.run([sys.executable, str(VER / "fixed_vector_tangent.py")], capture_output=True, text=True, timeout=3600).stdout
    assert "V10  : keeps fixed vector 0/1/2 to first order: [True, True, True]" in out
    assert "V10#2: keeps fixed vector 0/1/2 to first order: [True, True, True]" in out
    assert "V16  : keeps fixed vector 0/1/2 to first order: [False, False, False]" in out
    assert "V8   : keeps fixed vector 0/1/2 to first order: [False, True, True]" in out
    assert out.count("dimension of the tangent combinations = 2") == 3


@pytest.mark.slow
def test_the_formal_v10_branches_lose_the_cusp_fixed_vectors_at_order_four():
    out = subprocess.run([sys.executable, str(VER / "fixed_vector_order.py"), "6"], capture_output=True, text=True, timeout=7200).stdout
    assert out.count("[greedy]: (4, 4, 4)   agreement between primes: True") == 4
    assert out.count("[random-keep]: (4, 4, 4)   agreement between primes: True") == 4
    assert out.count("[random]: (2, 2, 2)   agreement between primes: True") == 4
    assert "V8           [greedy]: (1, 3, 3)   agreement between primes: True" in out
