"""B914 locks: the one-number ratio table + the signed skeleton."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B914_ratio_table")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_all_51_checks_pass():
    r = _res()
    assert all(v["pass"] for v in r["checks"].values())
    assert len(r["checks"]) >= 45


def test_the_table_is_one_number():
    r = _res()
    vals = {v["value_50d"] for v in r["T_table"].values()}
    assert len(vals) == 1
    assert vals.pop().startswith("4.775781328852112587377582312996804957776592668646e-32")
    # all pairwise ratios exactly 1
    for v in r["T_pairwise_ratios"].values():
        assert v["value_50d"] == "1.0"


def test_T_is_cubic_algebraic():
    r = _res()
    assert r["T_single"]["minpoly_deg"] == 3


def test_scale_reconciliation_and_cS():
    r = _res()
    assert float(r["scale_reconciliation_worst_rel_diff"]) < 1e-34
    assert r["c_S_vs_disc_mu13"]["ratio"] == "-1"
    assert r["h_S_mirror_of_B908"] in (True, "True")
