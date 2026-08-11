"""B1026/B1027 — locks: the nomination's determinism, the verdict's arithmetic, the discipline."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1027_fourth_crossing"))


def test_the_verdict_arithmetic_is_locked():
    from verdict import circ_dist, QUARK, LEPTON, PRED
    assert PRED == [120.0, 240.0]
    # quark: both predictions miss by >= 11 sigma
    for p in PRED:
        d = circ_dist(QUARK["central"], p)
        assert d / QUARK["sigma_up"] > 11
    # leptonic 240: the one-degree miss, exactly
    d240 = circ_dist(LEPTON["central"], 240.0)
    assert d240 == 43.0 and LEPTON["sigma_up"] == 42.0, (
        "the precision-frontier margin (43.0 vs 42.0) must stay recorded exactly")
    # powered in both sectors under the sealed clause
    assert 4 * (QUARK["sigma_up"] + QUARK["sigma_dn"]) / 2 <= 180
    assert 4 * (LEPTON["sigma_up"] + LEPTON["sigma_dn"]) / 2 <= 180


def test_the_miss_is_not_promoted():
    v = json.loads((ROOT / "frontier" / "B1027_fourth_crossing" / "arc_verdict.json").read_text())
    assert v["verdict"] == "NEGATIVE"
    c = v["claim_one_line"]
    assert "NOT PROMOTED" in c and "PRECISION FRONTIER" in c
    assert "REFRESH VERDICT IS PRE-COMMITTED" in c
    assert "zero anchors" in c.lower()


def test_the_nomination_near_miss_stays_recorded():
    src = (ROOT / "frontier" / "B1026_nomination" / "nominate.py").read_text()
    assert "T5 excluded" in src and "1.585" in src, (
        "the N1 near-miss must stay in the source -- the gate against its own author")
    v = json.loads((ROOT / "frontier" / "B1026_nomination" / "arc_verdict.json").read_text())
    assert "2.0 priced bits" in v["claim_one_line"]
