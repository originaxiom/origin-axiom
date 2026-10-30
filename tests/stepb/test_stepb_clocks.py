"""T1 under hyperbolic area on the band: the CDF's ends and median, and the two-sided tail."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import clocks as T


def test_area_cdf():
    assert T.area_cdf(1.0) == 0.0 and abs(T.area_cdf(4.0) - 1.0) < 1e-15
    assert abs(T.area_cdf(1.6) - 0.5) < 1e-12          # (1 - 1/y)/(3/4) = 1/2 at y = 8/5


def test_tail_and_grade():
    r = T.T1(T.area_cdf, 3.03)
    assert abs(r["t"] - 2 * (1 - T.area_cdf(3.03))) < 1e-15 and r["grade"] == "CONSISTENT"
    assert T.T1(T.area_cdf, 3.999)["grade"] == "NEGATIVE"


def test_nan_raises():
    import pytest
    with pytest.raises(ValueError):
        T.T1(T.area_cdf, float("nan"))
    with pytest.raises(ValueError):
        T.T1(lambda y: float("nan"), 2.0)
