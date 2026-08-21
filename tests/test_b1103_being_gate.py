"""B1103 locks — the being gate (harvest arc; outside-session theorem,
two-engine verified at the bank).

Fast: the vendored exact certificate at length 3 (84 words, ~seconds) —
exit-code disciplined, conditional pass lines (inspected at receipt), exact
in Z[zeta_30]. Slow (OA_SLOW=1): the full shipped scope, length 5 (1364
words), plus the banking seat's own zeta60 engine end-to-end.
"""
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1103_being_gate"


def _run(script, *args, timeout=600):
    return subprocess.run(
        [sys.executable, str(ARC / script), *args],
        capture_output=True, text=True, cwd=str(ROOT), timeout=timeout)


def test_certificate_length3_fast():
    r = _run("check_being_gate_vendored.py", "3")
    assert r.returncode == 0, r.stdout[-800:] + r.stderr[-400:]
    assert "ALL CHECKS PASSED" in r.stdout


def test_findings_carry_the_flags():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "OBSERVED-UNREPRODUCED" in t, "the census flag must stay banked"
    assert "integrate-don't-merge" in t, "harvest provenance must stay declared"
    assert "28 of the 1364" in t, "the h=0 clause's reality must stay stated"


def test_verdict_declares_creates_law():
    import json
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["creates_law"] is True and d["verdict"] == "PROVED"


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 for the full sweep")
def test_certificate_full_scope_slow():
    r = _run("check_being_gate_vendored.py", "5", timeout=1800)
    assert r.returncode == 0
    assert "1364" in r.stdout and "ALL CHECKS PASSED" in r.stdout


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 for the full sweep")
def test_own_engine_full_slow():
    r = _run("b1103_exact_engine.py", timeout=1800)
    assert "E5 PASS" in r.stdout and "E6 PASS" in r.stdout
    assert "all in Q(zeta5): True" in r.stdout
