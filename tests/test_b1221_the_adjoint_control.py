"""B1221 lock -- the control row "adjoint-only content | 72" was a grid's size, not a kernel's order (corrected 2026-11-11).

Found by a second derivation on another family of model (agy-002's card A2-C1) and checked here on the arc's own instrument,
which samples the circle U(1) at N points.  What could fail: the adjoint count not growing with the grid (then 72 would have
been a kernel's order after all); a count that matters moving with the grid; or the correction missing from the page."""
import importlib.util
import pathlib
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1221_global_form_path_independence"
spec = importlib.util.spec_from_file_location("b1221_kernel_27", ARC / "kernel_27.py")
k27 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k27)
ADJ = [(0, 0, 0)] * 3
INTS = [(0, 0, 6), (0, 0, 0), (0, 1, -3), (0, 1, 3)]


def test_the_adjoint_count_is_the_size_of_the_grid():
    for n in (12, 24, 60):
        assert len(k27.kernel(ADJ, n)) == 6 * n                      # 72, 144, 360: every sampled element, at every grid
    # and off every grid: an element with an angle the instrument never samples acts trivially on adjoint content too
    for c in (F(1, 7), F(5, 13), F(123, 1009)):
        assert all(((F(a * t, 3) + F(b * s, 2) + y * c) % 1) == 0 for a in range(3) for b in range(2) for t, s, y in ADJ)


def test_the_counts_that_matter_do_not_move_with_the_grid():
    for n in (12, 24, 60):
        assert len(k27.kernel(k27.C27, n)) == 6 and len(k27.kernel(k27.G16, n)) == 6 and len(k27.kernel(k27.G10, n)) == 6
        assert len(k27.kernel(INTS, n)) == 18
        assert max(k27.order(g) for g in k27.kernel(k27.C27, n)) == 6     # cyclic of order 6
    # the control of this test: on a grid that misses the sixths the instrument does lose the kernel on the 27
    assert len(k27.kernel(k27.C27, 5)) < 6


def test_the_correction_stands_under_the_table_and_the_row_is_kept():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "| adjoint-only content | 72 |" in f
    for s in ("CORRECTED 2026-11-11", "is not the order of a kernel", "which is infinite", "with 24 points it prints 144 and with 60 it prints 360"):
        assert s in f, s
