"""B1137 lock -- THE REGULATOR PROBE (R48-3): no SM value is algebraic over the object's
higher regulators -> DISJOINT, the value question's last route. Results pinned; the aggregate
re-derives from the committed grids (fast); the full PSLQ grid re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1137_regulator_probe"


def _res():
    return json.loads((ARC / "b1137_results.json").read_text(encoding="utf-8"))


def _fr():
    return json.loads((ARC / "results" / "final_report.json").read_text(encoding="utf-8"))


def test_overall_disjoint():
    assert _res()["overall_verdict"] == "DISJOINT"
    assert _fr()["overall_verdict"] == "DISJOINT"


def test_no_regulator_involved_in_any_target():
    d = _res()
    assert d["n_targets"] == 18
    assert d["n_targets_with_regulator_relation"] == 0   # the whole point: regulators absent


def test_matched_null_base_rate_zero():
    d = _res()
    assert d["null_base_rates_by_H"]
    assert all(float(v) == 0.0 for v in d["null_base_rates_by_H"].values())


def test_near_misses_are_bare_integers():
    nm = _res()["near_misses"]
    assert "V=4" in nm["delta_CP"] and "V=20" in nm["m_s/m_d"]
    assert all("zero regulator" in v for v in nm.values())


def test_arc_verdict_negative():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1137" and v["verdict"] == "NEGATIVE"


def test_findings_states_close_and_precisions():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "DISJOINT" in f and "rung 1" in f.lower()
    assert "27-reality" in f and "B991" in f
    assert "NEEDS-SPECIALIST" in f
    assert "Gate 5 untouched" in f


def test_aggregate_re_derives_from_pinned_grids():
    # re-run the aggregate logic on the COMMITTED grids -> DISJOINT (no grid recompute)
    r = subprocess.run([sys.executable, str(ARC / "aggregate.py")], cwd=str(ARC),
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "overall verdict = DISJOINT" in r.stdout


@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="full PSLQ grid ~30min; set OA_SLOW=1 to re-run from scratch")
def test_full_grid_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(ARC / "pslq_probe.py"), "real"], cwd=str(ARC),
                       capture_output=True, text=True, timeout=7200)
    assert r.returncode == 0, r.stderr[-2000:]
