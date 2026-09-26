"""B1381 lock -- THE RANK-ONE BOUND ON EVERY LEVEL.  On every cyclic cover M_n of m004, h^1 = 2 needs the whole Fox Jacobian
to vanish; its t-column is (1 - x, 1 - y), so the character must be trivial on the fibre, and there the block is s*I - (M^n)^T,
never zero because M^n is never scalar.  The control (the hyperelliptic involution, abelianization -I) shows the criterion can
fire.  Small ranges here; the full run is `verification/rank_one_bound.py`."""
import importlib.util
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1381_the_rank_one_bound_on_every_level" / "verification"
_spec = importlib.util.spec_from_file_location("b1381_bound", VER / "rank_one_bound.py")
R = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(R)


def test_the_t_column_and_the_fibre_block():
    rows = R.s1_jacobian(4)                      # asserts the t-column and s*I - (M^n)^T for n = 1..4
    assert [n for n, _, _ in rows] == [1, 2, 3, 4]
    assert rows[-1][2] == [[34, 21], [21, 13]]


def test_m_to_the_n_is_never_scalar():
    nmax, ev = R.s2_never_scalar(40)
    assert nmax == 40 and abs(ev[0] * ev[1] - 1) < 1e-12 and ev[0] != ev[1]


def test_the_control_fires():
    J, rank_involution, rank_m004 = R.s3_control()
    assert rank_involution == 0 and rank_m004 == 2    # h^1 = 2 at (1,1,-1) for the involution, not for m004


def test_the_golden_loci_have_h1_one():
    rows = R.s4_samples(3)
    assert all(max(sm) <= 1 and sm[0] == 1 and sm[-2:] == [1, 1] for _, sm in rows)
