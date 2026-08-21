"""B1113 lock -- the t-meter. Fast: stored exact traces (dial-blind constant +
four-way separation). Slow (OA_SLOW): the certificate-free verifier re-run."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1113_tmeter"


def _res():
    return json.loads((ARC / "b1113_results.json").read_text(encoding="utf-8"))


def test_stored_dial_blind_and_separating():
    r = _res()
    assert r["outcome"] == "CONFIRMED"
    tr = r["traces"]["hv8"]
    # dial-blind: tr(A.B_R) identical across all four dial values
    blind = {tr[t]["tr_A_BR"]["display"] for t in ("0", "1", "2", "omega")}
    assert blind == {"141750+1011915q"}, f"dial-blind broken: {blind}"
    # separating: tr(B_L.B_R) distinct across the four
    sep = {tr[t]["tr_BL_BR"]["display"] for t in ("0", "1", "2", "omega")}
    assert len(sep) == 4, f"separator not 4-way distinct: {sep}"
    # memo cross-check: all matches True
    xc = r["memo_number_cross_check"]["hv8"]
    assert all(v["match"] for t in xc.values() for v in t.values())


def test_findings_and_law():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "Free data of one object = forced" in f
    assert "measurement-by-coupling" in f
    assert "12/12" in f


def test_verdict_creates_law():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED" and d["creates_law"] is True


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 for the full re-run")
def test_verifier_reruns_certificate_free():
    p = subprocess.run([sys.executable, str(ARC / "b1113_tmeter_verify.py")],
                       capture_output=True, text=True, cwd=str(ROOT), timeout=1200)
    assert p.returncode == 0, p.stderr[-500:]
    assert "141750+1011915q" in p.stdout
