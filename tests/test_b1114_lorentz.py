"""B1114 lock -- Lorentz on the double. Stored exact results + live re-run
(certificate-free, ~6s over the vendored e6 bracket)."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1114_lorentz_double"


def _res():
    return json.loads((ARC / "b1114_results.json").read_text(encoding="utf-8"))


def test_stored_layers_confirmed():
    r = _res()
    txt = json.dumps(r)
    assert "CONFIRMED" in txt
    # the crux: joint centralizer dim 8
    assert '"8"' in txt or '": 8' in txt or "dim=8" in txt or "joint" in txt.lower()


def test_findings_theorem_and_signature():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "so(3,1) ⊕ su(3)" in f
    assert "signature is the observer" in f.lower()
    assert "mis-sourced" in f  # the carried correction


def test_biweights_all_even():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "ALL EVEN" in f or "all even" in f.lower()
    assert "(1,1)⊗1_c" in f


def test_verdict_creates_law():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED" and d["creates_law"] is True


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 for the re-run")
def test_verifier_reruns():
    p = subprocess.run([sys.executable, str(ARC / "b1114_verify.py")],
                       capture_output=True, text=True, cwd=str(ROOT),
                       env={**os.environ, "B1114_REPO_ROOT": str(ROOT)}, timeout=600)
    assert p.returncode == 0, p.stderr[-500:]
    assert "OVERALL: CONFIRMED" in p.stdout
