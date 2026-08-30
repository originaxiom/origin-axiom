"""B1143 lock -- SP-1 CLOSES: the physical B-L is a genuine FOURTH Cartan direction (independent
of {Y,T3R,T3L}), family c=[0,c1,0,-1/3,1,0] -- CONFIRMED TWO-BENCH with cloud memo 25 on B1139's
banked 27. (Reframed 2026-08-25 / B1144: an earlier 'the cloud's vector was wrong (Y-T3L)' claim
is WITHDRAWN as a cross-frame artifact; memo 25's own-frame construction is correct.)

Fast tests pin b1143_results.json (the solve, the fourth-direction span-membership, the naive
cross-frame vector, SP-3 invariance + the honest 36/36 flag, SP-4 flag). The full re-derivation
(~72s, incl. the 72-assignment search + a repo-wide SP-4 grep) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1143_bl_fourth_cartan"
RESULTS = ARC / "b1143_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the solve (corrected family)
def test_the_physical_bl_family():
    d = _load()
    assert d["item1_structural_verdict"] == "CONFIRMED"
    assert d["rank_12eq_system"] == 5 and d["nullity_12eq_system"] == 1
    assert d["my_family_c_vector"] == ["0", "c1", "0", "-1/3", "1", "0"]
    assert d["beta_L_redundant"] is True
    assert d["Tr_BL_identically_zero_whole_family"] is True
    assert d["Tr_BL3_identically_zero_whole_family"] is True
    assert d["all_27_physical_at_t0"] is True


# ---------------------------------------------------------------- the load-bearing claim
def test_bl_is_a_genuine_fourth_direction():
    d = _load()
    assert d["item3_fourth_direction_confirmed_whole_family"] is True
    # span{Y,T3R} and span{Y,T3R,T3L} both UNSOLVABLE (nonzero witness residuals)
    assert d["span_a_solvable_generic_t"] is False
    assert d["span_b_solvable_generic_t"] is False
    assert "3/2" in d["span_a_witness_residuals"]        # w.(B-L) = 3/2
    assert "3" in d["span_b_witness_residuals"]          # w.(B-L) = 3


# ----------------------------------- THE NAIVE VECTOR IS A CROSS-FRAME ARTIFACT (not a cloud error)
def test_naive_vector_is_cross_frame_artifact():
    # These fields record a TRUE computation: the naive/relayed vector, evaluated in B1139's frame,
    # does not solve there and reads as Y - T3L. That is a FRAME MISMATCH, not a defect in memo 25
    # (whose own-frame sp1_bl.py builds B-L physical on all 27, independent). Reframed in B1144.
    d = _load()
    assert d["cloud_family_matches_this_construction"] is False   # doesn't solve *in B1139's frame*
    assert d["cloud_family_same_line_as_mine"] is False
    # in B1139's frame the naive vector is exactly Y - T3L -> IN span{Y,T3R,T3L}: a cross-frame artifact
    assert d["cloud_pinned_vector_in_span_YT3R"] is False
    assert d["cloud_pinned_vector_in_span_YT3RT3L"] is True
    assert d["cloud_pinned_vector_explicit_combo"] == {"x": "1", "y": "0", "z": "-1"}  # Y - T3L in B1139's frame
    assert d["cloud_pinned_doublet_uniform"] is False    # not SU(2)_L-uniform (in this frame)


# ---------------------------------------------------------------- SP-3 (invariance + the honest flag)
def test_sp3_invariance_and_36_flag():
    d = _load()
    assert d["sp3_n_assignments_checked"] == 72
    assert d["sp3_table_invariant_across_all_assignments"] is True
    assert d["own_battery_5charge_zero"] == d["own_battery_5charge_total"] == 30   # all vanish
    assert d["own_battery_YQonly_zero"] == d["own_battery_YQonly_total"] == 6
    assert "FLAGGED" in d["sp3_36_figure_verdict"]       # 36 not reproduced without fitting


# ---------------------------------------------------------------- SP-4 flag
def test_sp4_flagged():
    d = _load()
    assert "FLAGGED" in d["sp4_verdict"]


# ---------------------------------------------------------------- the FINDINGS
def test_findings_states_close_and_reconciliation():
    t = FINDINGS.read_text(encoding="utf-8")
    assert "SP-1 closes" in t or "SP-1 CLOSES" in t
    assert "fourth Cartan direction" in t or "FOURTH Cartan" in t
    assert "two-bench" in t.lower()                       # confirmed with memo 25
    assert "Y − T₃L" in t or "Y - T3L" in t              # named as the cross-frame artifact
    assert "cross-frame" in t.lower() or "frame difference" in t.lower()
    assert "withdrawn" in t.lower()                       # the earlier catch is withdrawn


# ---------------------------------------------------------------- reproduction present
def test_verification_present():
    assert (VERIF / "verify_b25_physical_bl_final.py").exists()


# ---------------------------------------------------------------- full re-derivation (OA_SLOW, ~72s)
@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="B-L solve + 72-assignment search + repo-wide SP-4 grep ~72s; set OA_SLOW=1")
def test_bl_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF / "verify_b25_physical_bl_final.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=600)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "===RESULTS_JSON===" in r.stdout and "CONFIRMED" in r.stdout
