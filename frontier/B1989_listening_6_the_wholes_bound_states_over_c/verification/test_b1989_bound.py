"""B1989's lock: the committed run holds the bound states' kappa levels per group (the run takes 30 s; it is not rerun here)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_levels():
    t = (HERE / "bound_run.txt").read_text()
    assert "Q8: order 8; 11 distinct readings of pairs; 4 orbits" in t and "kappa values carrying a bound state: [-2, 2]" in t
    assert "kappa values carrying a bound state: [-2, -1, 0, 1, 2]" in t
    assert "kappa values carrying a bound state: [-2, -sqrt(5)/2 - 1/2, -1, 1/2 - sqrt(5)/2, 0, -1/2 + sqrt(5)/2, 1, 1/2 + sqrt(5)/2, 2]" in t
    assert t.count("the common point (0, 0, 0) among the readings: True") == 4
