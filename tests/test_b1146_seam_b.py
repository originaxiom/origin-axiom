"""B1146 lock -- SEAM-B: the 2T-vs-A4 distinction is the object's own -I, visible on BOTH the 27
and the 78 for the fermion-capable minimal-A1 stratum; codex's 'the adjoint can't distinguish them'
is a principal-sl2 artifact. NUANCED-MATCH on the sealed prereg (own-bench, exact). Fast tests pin
b1146_results.json + FINDINGS; OA_SLOW re-runs the own-code computation."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1146_seam_b"


def _d():
    return json.loads((ARC / "b1146_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1146" and d["verdict"] == "PROVED"


def test_minimal_A1_minusI_visible_on_both():
    o = _d()["object_minimal_A1_stratum"]
    # the standard minimal-nilpotent 5-grading, 40 odd dims -> -I nontrivial on the adjoint
    assert o["adjoint78_ad_h_spectrum"] == {"-2": 1, "-1": 20, "0": 36, "1": 20, "2": 1}
    assert o["adjoint78_odd_dims"] == 40 and o["rho78_minusI_nontrivial"] is True
    assert o["weight27_spectrum"] == {"-1": 6, "0": 15, "1": 6}
    assert o["weight27_odd_dims"] == 12 and o["rho27_minusI_nontrivial"] is True


def test_principal_is_the_even_extreme():
    p = _d()["principal_sl2_reference"]
    assert p["rho78_minusI_nontrivial"] is False   # codex's claim, principal-specific


def test_verdict_nuanced_match_and_seal_corrected():
    d = _d()
    assert "NUANCED-MATCH" in d["verdict"]
    assert "verify-don't-trust catch" in d["seal_correction"]
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "principal-sl₂ artifact" in t or "principal-sl2 artifact" in t.lower()
    assert "DEFUSED" in t
    assert "memo 34" in t                          # the convergence


@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="own-code SEAM-B e6 computation; set OA_SLOW=1")
def test_seam_b_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "seam_b.py")],
                       capture_output=True, text=True, cwd=str(ROOT), timeout=600)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "rho78(-I) != I : True" in r.stdout        # minimal A1 adjoint sees -I
    assert "spectrum all even? True" in r.stdout       # principal does not
