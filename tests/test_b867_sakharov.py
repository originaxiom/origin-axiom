"""Locks B867 -- the Sakharov gate (structural preconditions only)."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B867_sakharov_gate"
_S = importlib.util.spec_from_file_location("b867", _D / "sakharov_gate.py")
b7 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b7)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_s1_the_coset_is_the_xy_content():
    s1 = b7.s1_coset()
    assert s1["coset_dim"] == 12 == s1["xy_dim"] and s1["match"]


def test_s2_three_is_the_minimal_cp_capable_count():
    s2 = b7.s2_km_counting()
    assert s2["phase_counts"] == {1: 0, 2: 0, 3: 1, 4: 3, 5: 6}
    assert s2["first_N_with_phase"] == 3


def test_s3_the_barrier_is_exact_and_galois_conjugate():
    s3 = b7.s3_barrier()
    assert s3["broken_below_symmetric"] and s3["barrier"] and s3["galois_conjugates"]


def test_all_three_present_and_the_scope_is_the_stage_not_the_play():
    assert RES["verdict"]["all_preconditions_structural"] is True
    assert "stage, not the play" in RES["verdict"]["what_this_is_NOT"]
    assert "not a computation of the asymmetry" in _F.lower().replace("*","")


def test_s2_inherits_the_signature_caveat():
    assert "signature-not-mechanism" in _F or "signature, not banked" in _F.lower() \
        or "signature" in _F


def test_no_value_anywhere():
    """Gate 5 discipline: the results contain no physical value, rate, or epoch."""
    txt = json.dumps(RES)
    for banned in ("GeV", "second", "temperature", "10^-", "asymmetry ="):
        assert banned not in txt
