"""B898 locks: the exact signature census (the dichotomy theorem)."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B898_exact_census")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        raw = json.load(f)
    # sympy Integers were serialized via str; coerce the count fields
    return {n: {k: (int(v) if k != "factors" else v) for k, v in d.items()}
            for n, d in raw.items()}


def test_measured_pair_split_type_twins():
    r = _res()
    for n in ("8", "16"):
        assert r[n]["zero"] == 30
        assert r[n]["real"] == 48
        assert r[n]["imaginary"] == 0
        assert r[n]["complex_or_mixed"] == 0


def test_unmeasured_pair_compact_type_twins():
    r = _res()
    for n in ("14", "22"):
        assert r[n]["zero"] == 12
        assert r[n]["real"] == 0
        assert r[n]["imaginary"] == 66
        assert r[n]["complex_or_mixed"] == 0


def test_no_generic_complex_anywhere_on_C():
    r = _res()
    assert all(r[n]["complex_or_mixed"] == 0 for n in ("8", "14", "16", "22"))


def test_totals_tile_the_adjoint():
    r = _res()
    for n in ("8", "14", "16", "22"):
        s = r[n]["zero"] + r[n]["real"] + r[n]["imaginary"] + r[n]["complex_or_mixed"]
        assert s == 78
