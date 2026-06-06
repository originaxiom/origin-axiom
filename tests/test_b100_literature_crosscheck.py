"""B100 (Probes 2 + 6) -- locking tests: SnapPy's Ptolemy variety reproduces the boundary-unipotent SL(3)
slice of B71 (2 obstruction classes; 6 reps in the trivial class), and the Baker-Petersen twisted-Alexander
anchor equals the B98 geometric-rep Jacobian quadratic t^2-5t+1. Methods cited, not claimed."""
import importlib.util
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b100", _ROOT / "frontier" / "B100_literature_crosscheck" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

_snappy = pytest.importorskip("snappy", reason="SnapPy required for the Ptolemy cross-check")


def test_ptolemy_two_obstruction_classes():
    """The N=3 Ptolemy variety of 4_1 has 2 obstruction classes (H^2(M,dM; Z/3))."""
    assert B.ptolemy_obstruction_classes() == 2


def test_ptolemy_class0_boundary_unipotent_count():
    """The trivial obstruction class has 6 boundary-unipotent SL(3,C) reps -- the 0-dim slice of B71."""
    assert B.ptolemy_class0_solution_count() == 6


def test_twisted_alexander_equals_b98_geometric_jacobian():
    """The Baker-Petersen twisted-Alexander anchor is the B98 geometric-rep Jacobian quadratic t^2-5t+1."""
    t = sp.symbols("t")
    assert sp.expand(B.twisted_alexander_transverse_quadratic() - (t**2 - 5 * t + 1)) == 0


def test_genus_table_distinguishes_the_two_curves():
    """The trace-coord canonical component (genus 0) and the A-poly spectral curve (genus 3) are different
    curves -- the figures must not be conflated."""
    g = B.genus_table()
    assert g["canonical_component_trace_coords"] == 0
    assert g["A_polynomial_spectral_curve"] == 3
