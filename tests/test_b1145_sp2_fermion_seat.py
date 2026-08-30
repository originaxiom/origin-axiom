"""B1145 lock -- SP-2 GREEN: the beat's spin payment reaches the fermions; the generation's
kinematic seat closes ON-OBJECT. The odd A1/su(6) stratum's 27 (minuscule => 6 fundamental-2
doublets + 15 singlets) inherits B1141's beat-selected lift; the beat closes on it, every identity
EXACT over Q(sqrt-3). Verified three independent ways (this bench blind + the cloud's cert + own
adversarial own-code). Fast tests pin b1145_results.json + FINDINGS; OA_SLOW re-runs the own-code cert."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1145_sp2_fermion_seat"
RESULTS = ARC / "b1145_results.json"
VERIF = ARC / "verification" / "sp2_independent.py"


def _d():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1145" and d["verdict"] == "PROVED"


def test_verdict_algebraic_closure_and_prereg_blind():
    d = _d()
    assert "GREEN" in d["verdict"] and "algebraic" in d["verdict"].lower()
    assert d["sealed_prereg_sha256"] == "c384dd3e069e6963"
    assert d["prereg_sealed_before_answer_and_before_memo29_contact"] is True
    # the physical-generation reading is explicitly NOT a theorem (codex-sharpened fence)
    assert "not a theorem" in d["physical_generation_reading"].lower()
    assert len(d["does_NOT_establish"]) >= 5


def test_all_hinge_identities_exact():
    idn = _d()["identities_exact"]
    assert idn["relator_abABaBAbaB_is_identity"] is True
    assert idn["C_neq_I"] is True and idn["C_sq_eq_I"] is True
    assert idn["C_commutes_A27"] is True and idn["C_commutes_B27"] is True
    assert idn["hinge_a_Omega2_eq_A27"] is True
    assert idn["hinge_b_Omega_A27_conj_eq_A27"] is True
    assert idn["hinge_c_Omega_B27_conj_eq_rho_wB"] is True


def test_verified_three_independent_ways():
    assert len(_d()["verified_three_independent_ways"]) == 3


def test_findings_sharpened_fence():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "minuscule" in t.lower()
    assert "kinematics" in t.lower()          # the held fence
    # the codex-sharpened non-claims: the exact algebra is the theorem, the physical reading is not
    assert "not a theorem" in t.lower() or "thesis" in t.lower()
    assert "Weyl spinor" in t                 # internal parity is NOT a 4d Weyl spinor
    assert "Dirac" in t                       # no Dirac operator/index
    assert "generations are NOT proved" in t or "generations are not proved" in t.lower()


@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="own-code SP-2 re-derivation (exact e6/27 build); set OA_SLOW=1")
def test_sp2_independent_reproduces_green_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF)], capture_output=True, text=True,
                       cwd=str(ROOT), timeout=600)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "SP-2 GREEN" in r.stdout
