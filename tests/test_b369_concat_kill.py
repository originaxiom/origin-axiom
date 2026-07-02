"""Locks for B369 — the concatenation-kill test (banked concat_kill.json)."""

import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B369_concatenation_kill")
REPORT = json.load(open(os.path.join(HERE, "concat_kill.json")))


def test_prediction_seam_null_all_words():
    assert REPORT["prediction_seam_null"] is True
    for key in ("1+2", "2+1", "1+3", "2+3", "3+4", "1+4"):
        assert REPORT[key]["clean_sqrtm3_sqrtm15"] is True
        for vec in REPORT[key]["readout"].values():
            assert Fr(vec[2]) == 0 and Fr(vec[3]) == 0


def test_word_orders():
    assert {k: REPORT[k]["order"] for k in
            ("1+2", "2+1", "1+3", "2+3", "3+4", "1+4")} == {
        "1+2": 4, "2+1": 4, "1+3": 20, "2+3": 20, "3+4": 4, "1+4": 10}


def test_rotation_galois_identity():
    assert REPORT["rotation_gate_manifold"] is True
    assert REPORT["rotation_galois_identity"] is True
    r12, r21 = REPORT["1+2"]["readout"], REPORT["2+1"]["readout"]
    for a in r12:
        assert Fr(r21[a][0]) == Fr(r12[a][0])
        assert Fr(r21[a][1]) == -Fr(r12[a][1])


def test_total_par_trace_is_one():
    """Sum over a of tr(Par*P_a) = tr(Par) = 1, per word."""
    for key in ("1+2", "2+1", "1+3", "2+3", "3+4", "1+4"):
        tot = [Fr(0)] * 4
        for vec in REPORT[key]["readout"].values():
            tot = [t + Fr(v) for t, v in zip(tot, vec)]
        assert tot == [Fr(1), Fr(0), Fr(0), Fr(0)]
