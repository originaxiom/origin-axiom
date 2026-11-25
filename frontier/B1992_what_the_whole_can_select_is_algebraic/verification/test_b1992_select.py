"""B1992's lock: the committed check holds the zero-dimensionality count and the typing of the listening line's numbers (the run takes minutes; it is not rerun here)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_check():
    t = (HERE / "select_check_run.txt").read_text()
    assert "SUMMARY T2a: words of length <= 4 whose fixed set on the cusp's leaf is zero-dimensional with algebraic points: 26 of 30; not zero-dimensional: ['LLL', 'RRR', 'LLLL', 'RRRR']" in t
    assert "SUMMARY T2b: every number the listening line found is algebraic: True" in t
