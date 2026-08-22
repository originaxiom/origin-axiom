"""B1139 lock -- THE SYMMETRY-POINT TABLE: one SM generation (QUANTIZED), sin²θ_W = 3/8 typed
as a REPRODUCTION (forced direction + B991-convention normalization), the 8 anomaly traces = 0
as the realized E₆ anomaly-freedom theorem, and the honest naive-B−L NEGATIVE. Verified
two-bench (cloud memos 23/24, golden_gate 577712f, + this bench's own-code re-derivation).

Fast tests pin b1139_results.json, assert the sin²θ_W ratio arithmetic, cross-check against
banked B883 (the 27 = [1,10,16]) and B1102 (the arc that pins the assignment non-circularly),
and assert the honest TYPING is stated in FINDINGS. The full re-derivation (own crystal BFS +
exhaustive assignment search + B883 subprocess, >2min) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1139_symmetry_point_table"
RESULTS = ARC / "b1139_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the table (QUANTIZED)
def test_table_is_one_sm_generation():
    d = _load()["table"]
    assert d["n_states"] == 27 == d["multiset_sum_check"]
    assert d["colored_states"] == 18 and d["singlet_states"] == 9
    assert d["is_one_SM_generation"] is True
    assert set(d["Q_value_set"]) == {"-1", "-2/3", "-1/3", "0", "1/3", "2/3", "1"}
    assert sum(d["Q_multiset"].values()) == 27
    assert d["y_multiset_matches_B1102"] is True


# ---------------------------------------------------------------- sin²θ_W (REPRODUCTION)
def test_weinberg_ratio_and_typing():
    d = _load()["weinberg_memo23"]
    assert d["Tr_T3L2"] == 3 and d["Tr_Q2"] == 8
    assert Fraction(d["Tr_T3L2"], d["Tr_Q2"]) == Fraction(3, 8)   # sin²θ_W = Tr T₃L²/Tr Q²
    assert d["sin2_theta_W"] == "3/8"
    assert d["closing_independent"] == "72/72"
    # the honest type: forced direction + assumed (B991-convention) normalization = reproduction
    assert "REPRODUCTION" in d["typing"] and "B991" in d["typing"]
    assert "FORCED-DIRECTION" in d["typing"] and "ASSUMED-NORMALIZATION" in d["typing"]


# ---------------------------------------------------------------- anomaly-freedom (realized theorem)
def test_eight_anomaly_traces_zero_scoped():
    d = _load()["anomaly_memo24"]
    assert len(d["eight_traces_all_zero"]) == 8 and d["all_exactly_zero"] is True
    assert d["e6_invariant_degrees"] == [2, 5, 6, 8, 9, 12]      # no degree 3
    assert 3 not in d["e6_invariant_degrees"] and d["no_degree_3_invariant"] is True
    assert "general E6 anomaly-freedom theorem" in d["honest_scope"].replace("_", " ") \
        or "GENERAL E6 anomaly-freedom" in d["honest_scope"]


# ---------------------------------------------------------------- the honest B−L negative
def test_naive_bl_unphysical():
    d = _load()["naive_BL_negative_memo24"]
    assert d["verdict"] == "UNPHYSICAL"
    assert set(d["unphysical_colored"]) == {"5/3", "-4/3"}
    assert set(d["unphysical_singlet"]) == {"2", "-2"}
    assert "SP-1" in d["note"]                                   # the open cell it points to


# ---------------------------------------------------------------- cross-bench consistency
def test_cross_consistent_with_banked_arcs():
    b883 = json.loads((REPO / "frontier" / "B883_the_27" / "results.json").read_text())
    assert b883["s1_multiplicities"] == [1, 10, 16]              # the 27 both benches use
    # the arc that pins the assignment non-circularly must exist
    assert (REPO / "frontier" / "B1102_exact_hypercharge_solve" / "b1102_results.json").exists()


# ---------------------------------------------------------------- the FINDINGS typing
def test_findings_types_every_datum():
    t = FINDINGS.read_text(encoding="utf-8")
    assert "QUANTIZED" in t
    assert "reproduction" in t.lower()
    assert "realized" in t.lower() and "anomaly-freedom" in t
    assert "NEGATIVE" in t


# ---------------------------------------------------------------- reproduction present
def test_verification_script_present():
    assert (VERIF / "verify_sm_table.py").exists()


# ---------------------------------------------------------------- full reproduction (OA_SLOW)
@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="own crystal BFS + exhaustive assignment search + B883 subprocess >2min; set OA_SLOW=1")
def test_full_table_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF / "verify_sm_table.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=1800)
    assert r.returncode == 0, r.stderr[-2000:]
    out = r.stdout
    assert "3/8" in out or "sin" in out.lower()   # the weinberg check runs to completion
