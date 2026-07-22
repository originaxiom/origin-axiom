"""P3 depth-exposure stratum -- locks for the E22 re-adjudication."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load():
    with open(ROOT / "frontier/B765_p3_depth/results.json") as f:
        return json.load(f)


def _kg():
    with open(ROOT / "frontier/B742_negatives_hunt_p1/stageA/kill_graph.json") as f:
        return json.load(f)


def _bp():
    with open(ROOT / "frontier/B742_negatives_hunt_p1/stageA/bprime_annotations.json") as f:
        return json.load(f)


def test_target_count():
    r = _load()
    assert r["targets"] == 21


def test_no_halt():
    r = _load()
    assert r["halt"] is False


def test_verdicts_partition():
    r = _load()
    assert r["depth_closed"] + r["depth_held"] + r["depth_exposed"] == r["targets"]


def test_depth_closed_count():
    r = _load()
    assert r["depth_closed"] == 8


def test_depth_held_count():
    r = _load()
    assert r["depth_held"] == 6


def test_depth_exposed_count():
    r = _load()
    assert r["depth_exposed"] == 7


def test_all_depth_exposed_are_p1():
    r = _load()
    kg = _kg()
    p1_ids = {rec["id"] for rec in kg["records"] if rec.get("p1")}
    for cid, cell in r["cells"].items():
        if cell["final_verdict"] == "DEPTH-EXPOSED":
            assert cid in p1_ids, f"{cid} not in P1"


def test_all_targets_have_depth_exposure_flag():
    r = _load()
    bp = _bp()
    for cid in r["cells"]:
        assert bp[cid].get("depth_exposure") is True, f"{cid} missing depth_exposure"


def test_structural_forms_mostly_closed():
    r = _load()
    structural = [c for c in r["cells"].values() if c["structural_form"]]
    closed = [c for c in structural if c["final_verdict"] == "DEPTH-CLOSED"]
    assert len(closed) >= 5, "most structural forms should be depth-closed"


def test_p2_kill_extends_implies_held_or_closed():
    r = _load()
    for cid, cell in r["cells"].items():
        if cell["p2_verdict"] == "KILL-EXTENDS":
            assert cell["final_verdict"] in ("DEPTH-CLOSED", "DEPTH-HELD"), \
                f"{cid}: P2 KILL-EXTENDS but final={cell['final_verdict']}"


def test_depth_exposed_wall7_is_face_irrelevant():
    r = _load()
    w7 = r["cells"]["WALL-7"]
    assert w7["final_verdict"] == "DEPTH-EXPOSED"
    assert w7["p2_verdict"] == "FACE-IRRELEVANT"


def test_exposed_cells_are_expected():
    r = _load()
    exposed = {cid for cid, c in r["cells"].items() if c["final_verdict"] == "DEPTH-EXPOSED"}
    expected = {"B489", "B500", "B685", "TOMB-L255", "TOMB-L310", "TOMB-L34", "WALL-7"}
    assert exposed == expected


def test_method_a_b_consistency():
    r = _load()
    for cid, cell in r["cells"].items():
        a, b = cell["method_a"], cell["method_b"]
        fv = cell["final_verdict"]
        if a == "DEPTH-CLOSED" and b == "DEPTH-CLOSED":
            assert fv == "DEPTH-CLOSED"
        elif a == "DEPTH-EXPOSED" and b == "DEPTH-HELD":
            assert fv == "DEPTH-HELD"
        elif a == "DEPTH-EXPOSED" and b == "DEPTH-EXPOSED":
            assert fv == "DEPTH-EXPOSED"
