"""B269 locks -- T[4_1] Rungs 2 (cusp Weyl Z/2 exact A-poly symmetry; flavor=O(2) not SU(2)) + 3 (state-integral
saddle z=e^{i pi/3} -> Vol=2.0299, B250). FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B269_t41_rungs_2_3" / "t41_rungs_2_3.py"
_spec = importlib.util.spec_from_file_location("b269", _PATH)
b269 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b269)


def test_rung2_cusp_weyl_symmetry():
    # the meridian Weyl Z/2 (M,L)->(1/M,1/L) is an exact symmetry of the figure-eight A-polynomial
    assert b269.cusp_weyl_invariant()
    L = sp.Symbol("L")
    assert b269.complete_structure_longitude() == (L + 1)**2   # complete/amphichiral, double root L=-1


def test_rung3_saddle_reproduces_complex_volume():
    # state-integral saddle = regular ideal tetrahedron e^{i pi/3} -> Vol(4_1)=2.0299 (B250)
    assert abs(b269.complex_volume_from_saddle() - mp.mpf("2.0298832128")) < 1e-9


def test_saddle_shape_is_ramified_prime_center():
    # the saddle shape is e^{i pi/3} = Riley t (B264) = the center reduced mod (sqrt-3) to make 2T (B266)
    assert abs(b269.GEOMETRIC_SHAPE - mp.e ** (1j * mp.pi / 3)) < 1e-25
