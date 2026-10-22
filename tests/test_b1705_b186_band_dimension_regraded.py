"""B1705 -- B186's band dimension re-graded (Review 67). Stored: the line count BLAS-independent, the ordering by > 0.1 at
both settings, the two-dimensional count's drift. Live: the band's operator is Hermitian (imaginary parts below 1e-12)."""
import importlib.util, json, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1705_b186_band_dimension_regraded" / "verification"


def test_stored():
    d = json.loads((A / "regrade.json").read_text(encoding="utf-8"))
    assert d["the line count is BLAS-independent"] and d["the ordering holds by at least 0.1 at both settings"]
    s, m = d["single-threaded BLAS"], d["default BLAS"]
    assert abs(s["2"]["d_band_lock_2d"] - m["2"]["d_band_lock_2d"]) > 0.03          # the old count drifted
    assert abs(s["1"]["d_band_line"] - 0.9385) < 1e-3 and abs(s["2"]["d_band_line"] - 0.8830) < 1e-3


def test_live_hermitian():
    spec = importlib.util.spec_from_file_location("t186", str(A.parents[2] / "tests" / "test_b186_hyperbolicity_certification.py"))
    t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
    ev = t._spectrum(t._word(6, 2), 0.0)
    assert np.abs(ev.imag).max() < 1e-12
