"""B92 (Paper 0, Layer 1) -- locking tests: the metallic family = det=-1 = purely-periodic-period-1 CF,
up to conjugacy (m free); the four naive premises admit det=+1; the systole picks m=1 only with a metric."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b92", _ROOT / "frontier" / "B92_metallic_classification" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_three_equivalent_forms():
    """self-reference x=m+1/x, CF [m;m,..], and Moebius z->m+1/z all give lambda_m, for m=1,2,3."""
    for m in (1, 2, 3):
        assert B.three_equivalent_forms(m) == (True, True, True)


def test_det_minus1_iff_period1():
    """The operative condition: det=-1 <=> purely-periodic-period-1 CF, over all entries<=5 matrices."""
    n, equiv, invariant, dm1 = B.census(5)
    assert n > 0 and equiv is True
    assert invariant is True                     # CF-period constant within each (trace,det) class
    # every det=-1 trace-m class is period-1 with repeat-block (m,) -> conjugate to the companion M_m
    for m, (perlen, block) in dm1.items():
        assert perlen == 1 and block == (m,)


def test_refinement_a_naive_premises_admit_det_plus1():
    """M_1^2 = [[2,1],[1,1]] satisfies the four premises (positive, expanding, automorphism) but det=+1,
    so det=-1 is the operative extra condition."""
    M, det, tr = B.refinement_a()
    assert M == [[2, 1], [1, 1]] and det == 1 and tr == 3


def test_systole_picks_m1():
    """MyCalc-5: m=1 (golden) is the systole -- minimal geodesic length 2 log lambda_m -- so the member is
    distinguished only by importing a metric; the family itself leaves m free."""
    L = B.systole_lengths(range(1, 6))
    assert min(L, key=L.get) == 1
    assert all(L[m] < L[m + 1] for m in range(1, 5))   # strictly increasing in m
