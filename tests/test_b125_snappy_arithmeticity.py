"""Locks for B125 -- SnapPy arithmeticity of the metallic R^m L^m bundles (overturns K009).

The spine (M_m^2 = R^m L^m, trace m^2+2) is pure numpy and always runs. The arithmeticity verdict is recorded from
the in-sandbox SnapPy run; a SnapPy-guarded test recomputes it live when SnapPy/cypari are importable (otherwise it
skips, so the suite stays green on machines without SnapPy).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b125_probe", _ROOT / "frontier/B125_snappy_arithmeticity/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B125 = _load()


def test_structural_identity_Mm2_is_RmLm():
    si = B125.structural_identity(mmax=6)
    assert si["all_equal_RmLm"]
    assert si["trace_is_m2_plus_2"]
    assert [tr for _, tr, _ in si["rows"]] == [3, 6, 11, 18, 27, 38]


def test_record_two_element_selector_not_unique_m1():
    # The correction of K009: arithmeticity selects {m=1, m=2}, not uniquely m=1.
    assert B125.ARITHMETIC_SELECTED == (1, 2)
    assert B125.RECORD[1]["arithmetic"] and B125.RECORD[1]["field"] == "Q(sqrt-3)"
    assert B125.RECORD[2]["arithmetic"] and B125.RECORD[2]["field"] == "Q(i)"
    assert all(not B125.RECORD[m]["arithmetic"] for m in (3, 4, 5, 6))
    # the two arithmetic fields are distinct -> not commensurable -> two genuinely distinct manifolds
    assert B125.RECORD[1]["field"] != B125.RECORD[2]["field"]


def test_live_arithmeticity_if_snappy_available():
    pytest.importorskip("snappy")
    pytest.importorskip("cypari")
    live = B125.live_arithmeticity(mmax=4)
    assert live is not None
    # m=1, m=2 arithmetic (imaginary quadratic, degree 2); m=3, m=4 not (degree > 2)
    assert live[1]["arithmetic"] and live[1]["kM_degree"] == 2
    assert live[2]["arithmetic"] and live[2]["kM_degree"] == 2
    assert not live[3]["arithmetic"] and live[3]["kM_degree"] > 2
    assert not live[4]["arithmetic"] and live[4]["kM_degree"] > 2
    # the two arithmetic fields differ (Q(sqrt-3) vs Q(sqrt-1)) -> not commensurable
    assert live[1]["field"] != live[2]["field"]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
