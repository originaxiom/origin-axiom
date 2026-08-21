"""B1107 + B1108 harvest locks."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _flat(rel):
    return " ".join((ROOT / rel).read_text(encoding="utf-8").split())


# ---- B1107: the one-loop harvest ----

def test_b1107_results_core():
    r = json.loads((ROOT / "frontier/B1107_oneloop_harvest/b1107_results.json")
                   .read_text(encoding="utf-8"))
    assert not r["failures"]
    c1 = r["claim1_algebraic_identity"]
    assert c1["max_err_real_m004_data"] < 1e-14
    assert c1["max_err_synthetic_500_trials"] < 1e-13
    c2a = r["claim2a_logZ_geod"]
    assert c2a["agreement_with_banked"] < 1e-13
    assert abs(c2a["logZ_by_cutoff"]["5.5"] - (-0.2729771708384004)) < 1e-13
    counts = r["class_geodesic_counts_by_cutoff"]["5.5"]
    assert counts["classes"] == 214 and counts["geodesics_with_multiplicity"] == 2819, (
        "the corrected 5.5 spectrum counts are part of the banked record")


def test_b1107_findings_carry_the_flags():
    f = _flat("frontier/B1107_oneloop_harvest/FINDINGS.md")
    assert "15 significant figures" in f or "fifteen significant figures" in f
    assert "pure roundoff" in f
    assert "214 classes, 2819" in f, "the found defect's correction must stay banked"
    assert "three residues" in f, "B8113's scope must ride the harvest"


# ---- B1108: the C5 negative ----

def test_b1108_two_source_and_two_doors():
    f = _flat("frontier/B1108_c5_archimedean/FINDINGS.md")
    assert "finite-group-valued" in f
    assert "independent" in f and "1905.13610" in f, "two-source verification"
    assert "TWO candidate doors" in f, "the B8116 correction must stay carried"
    assert "closed surgeries vs the cusped complement" in f, "the scope fence"
    d = json.loads((ROOT / "frontier/B1108_c5_archimedean/arc_verdict.json")
                   .read_text(encoding="utf-8"))
    assert d["verdict"] == "NEGATIVE" and d["creates_law"] is False


def test_framework_item6_closed_and_road_vi4():
    fw = _flat("docs/THE_FRAMEWORK.md")
    assert "CLOSED NEGATIVE 2026-08-21" in fw
    assert "TWO candidate doors" in fw
    road = _flat("docs/THE_ROAD.md")
    assert "VI.4 The arithmetic-CS analogue" in road


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 full re-run")
def test_b1107_live_rerun():
    p = subprocess.run(
        [sys.executable, str(ROOT / "frontier/B1107_oneloop_harvest/b1107_verify.py")],
        capture_output=True, text=True, cwd=str(ROOT), timeout=900)
    assert p.returncode == 0, p.stderr[-500:]
