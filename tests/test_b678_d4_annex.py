"""B678 locks — the D4 annex decisive values (from the MERGED json)."""
import json
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B678_d4_annex")


def _merged():
    return json.load(open(os.path.join(_B, "d4_results_MERGED.json")))


def test_no_growth_anywhere():
    m = _merged()
    assert m["any_growth_any_level"] is False
    assert all(v == [] for v in m["failed_gates_by_level"].values())


def test_own_channel_and_cross_campaign_values():
    m = _merged()
    phi = (1 + 5**0.5) / 2
    got = {(r["n"], r["kappa"]): abs(complex(float(r["Z_re"]),
                                             float(r["Z_im"])))
           for r in m["table_rows"]}
    for k in (5, 10, 15):
        assert abs(got[(3, k)] - 1/phi) < 1e-12
    assert abs(got[(4, 12)] - (3**0.5 - 1)) < 1e-12


def test_ceiling_map_consistent():
    m = _merged()
    cm = {}
    for r in m["table_rows"]:
        z = abs(complex(float(r["Z_re"]), float(r["Z_im"])))
        cm[r["n"]] = max(cm.get(r["n"], 0.0), z)
    for n, v in m["ceiling_map_recomputed"].items():
        assert abs(cm[int(n)] - v["max_abs"]) < 1e-9
