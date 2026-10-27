"""Lock test for B1763: Matter Kähler Metric and Residual Flavour Pull Elimination."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1763_matter_kahler_metric_and_residual_flavour_pulls"
VER = ARC / "verification"


def test_b1763_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "matter_kahler_metric.py").is_file()
    assert (VER / "matter_kahler_metric.json").is_file()
    assert (VER / "matter_kahler_metric_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1763"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-390"}


def test_b1763_pull_reduction_at_geodesic_apex():
    data = json.loads((VER / "matter_kahler_metric.json").read_text())
    # Locate geodesic apex tau = 0.3333 + 3.0551i
    apex_key = [k for k in data.keys() if "0.3333" in k][0]
    apex_res = data[apex_key]

    flat = apex_res["flat"]
    one_sixth = apex_res["step_minus_one_sixth"]
    one_fourth = apex_res["step_minus_one_fourth"]

    # Flat baseline
    assert abs(flat["chi2_10_gut"] - 32.27) < 0.1
    assert abs(flat["chi2_9_gut"] - 24.95) < 0.1
    assert abs(flat["pull_J"] - (-2.71)) < 0.05

    # 1/6 step arithmetic progression Delta k_5bar = (-1/3, -1/6, 0)
    assert one_sixth["chi2_10_gut"] < 23.5
    assert one_sixth["chi2_9_gut"] < 19.5
    assert abs(one_sixth["pull_J"]) < 2.05
    # Max pull across all 10 observables is bounded by 2.2 sigma
    max_pull_9 = max(abs(p) for p in one_sixth["pulls_gut_9"])
    assert max_pull_9 <= 2.20
    assert abs(one_sixth["pull_J"]) <= 2.20

    # 1/4 step progression Delta k_5bar = (-1/2, -1/4, 0)
    assert one_fourth["chi2_10_gut"] < 22.5
    assert one_fourth["chi2_9_gut"] < 20.0
    assert abs(one_fourth["pull_J"]) < 1.55


def test_b1763_apex_remains_strictly_preferred():
    data = json.loads((VER / "matter_kahler_metric.json").read_text())
    apex_key = [k for k in data.keys() if "0.3333" in k][0]
    apex_chi2_10 = data[apex_key]["step_minus_one_sixth"]["chi2_10_gut"]

    for k, v in data.items():
        if k != apex_key and ("3.1000" in k or "2.9500" in k):
            other_chi2_10 = v["step_minus_one_sixth"]["chi2_10_gut"]
            # Out-of-geodesic strip points have chi2_10 > 40
            assert other_chi2_10 > 40.0
            assert other_chi2_10 > apex_chi2_10 + 15.0
