"""Locks for B370 leg A — the third-order verdicts (banked massey_legA.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B370_massey_depth2")
REPORT = json.load(open(os.path.join(HERE, "massey_legA.json")))
DIRS = {r["label"]: r for r in REPORT["directions"]}


def test_rep_checks_at_banked_thresholds():
    assert REPORT["rep_checks"]["relator"] < 1e-50
    assert REPORT["rep_checks"]["automorphism"] < 1e-60


def test_controls():
    cob = DIRS["coboundary"]
    assert cob["class_norm"] < 1e-80                      # exact-tier zero
    m1 = DIRS["m=1"]
    assert m1["gate_P1"] < 1e-50 and m1["gate_P2"] < 1e-50
    assert m1["class_norm"] < 1e-60                       # the integrable control


def test_all_six_directions_unobstructed_at_order_three():
    for m in (1, 4, 5, 7, 8, 11):
        r = DIRS[f"m={m}"]
        gates = max(r["gate_P1"], r["gate_P2"])
        assert gates < 1e-40                              # expansion floors hold
        # the class sits at least 4 orders below the direction's own gate floor
        assert r["class_norm"] < 1e-4 * gates


def test_mb12_nonvacuous_on_nontrivial_spans():
    for m in (4, 5, 7, 8, 11):
        r = DIRS[f"m={m}"]
        if r["indeterminacy_rank"] > 0:
            assert min(r["mb12_random_residuals"]) > 0.1
