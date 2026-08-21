"""B1116 lock -- the asymptotic value channel (scope audit facts + the stored
numeric fits; the mpmath re-run is the slow gate)."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1116_asymptotic_channel"


def test_scope_audit_verdict():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "not excluded by any banked no-go" in f
    assert "the reason IS the adelic split" in f or "REASON is the adelic split" in f
    # all four no-goes named
    for ng in ("scale-torsor", "type law", "frame-relativity", "k-blindness"):
        assert ng in f


def test_numeric_headline():
    r = json.loads((ARC / "b1116_results.json").read_text(encoding="utf-8"))
    h = r["headline_vs_memo"]
    from mpmath import mpf
    assert abs(mpf(h["power_this_bench_best"]) - mpf("1.5")) < mpf("1e-10")
    assert abs(mpf(h["constant_this_bench_best"]) - mpf(h["constant_target_3^-1/4"])) < mpf("1e-10")
    assert abs(mpf(h["exponent_this_bench_best"]) - mpf(h["exponent_vol_banked"])) < mpf("1e-11")


def test_fence_first_class():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "not-excluded" in f.lower() or "not excluded" in f.lower()
    assert "L180" in f and "not an arrival" in f
    assert "seven sealed misses stand" in f or "seven misses stand" in f


def test_verdict_creates_law():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED" and d["creates_law"] is True


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 mpmath re-run")
def test_numeric_reruns():
    p = subprocess.run([sys.executable, str(ARC / "b1116_verify.py")],
                       capture_output=True, text=True, cwd=str(ROOT), timeout=1800)
    assert p.returncode == 0, p.stderr[-500:]
