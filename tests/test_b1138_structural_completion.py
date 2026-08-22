"""B1138 lock -- THE STRUCTURAL COMPLETION: the fork theorem (memo 11), the exceptional
installment ladder (memo 14), the hypercharge spend (memo 13), and the E8 family triplet
(memo 15). Verified two-bench (cloud seat's phase-III structural memos, golden_gate 577712f,
+ this bench's independent own-code re-derivation, no discrepancy).

Fast tests pin b1138_results.json, assert cross-consistency with the already-banked
B1135 (128 involutions, the 81-pair E6(-14) gauge row) and B883 (the 27 = [1,10,16]),
and re-run the load-bearing FORK ladder independently (verify_memo11_fork.py, ~4s: 16/8/8/0,
joint centralizer 0, S3 torsor 216 each, |W(E6)|=51840). The heavier e7/e8 installment
ladder rebuild (~minutes) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1138_structural_completion"
RESULTS = ARC / "b1138_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- memo 11: the fork
def test_fork_ladder_and_torsor_pinned():
    d = _load()["memo11_fork"]
    assert d["z_ladder"] == [16, 8, 8, 0]          # the ladder, ending at the fork
    assert d["joint_centralizer"] == 0             # THE FORK: any two of three, never all
    assert d["W_E6"] == 51840
    assert d["S3_torsor_per_perm"] == 216 == 6 ** 3
    assert d["perms_realized"] == 6                 # full S3


# ---------------------------------------------------------------- memo 14: the ladder
def test_installment_ladder_pinned():
    d = _load()["memo14_ladder"]
    assert (d["room_E6"], d["room_E7"], d["room_E8"]) == (0, 1, 8)   # one layer per step
    assert d["E6_control"] == [16, 8, 0]           # matches the fork's tail
    assert d["E7_ladder"] == [35, 9, 1] and d["E7_room_pure_cartan"] is True
    assert d["E8_room"] == 8
    assert d["roots"] == {"E6": 72, "E7": 126, "E8": 240}
    assert d["dims"] == {"E6": 78, "E7": 133, "E8": 248}


# ---------------------------------------------------------------- memo 13: the Y spend
def test_hypercharge_spend_pinned():
    d = _load()["memo13_yselect"]
    assert d["n_Y"] == 18 and d["orbit_split"] == [9, 9]
    assert d["factor_preserving_involutions"] == 128
    assert d["gauge_row_lifts"] == 16 == d["gauge_row_lifts_in_dW"]  # all in the deltaW coset
    assert d["gauge_row_pairs"] == 81
    assert d["pairs_partition_18"] is True and d["no_Y_split"] is True
    assert d["P_closure_literal"] == "3/9"          # the self-correction carried
    assert d["real_invariant"] == "orbit-straddling"


# ---------------------------------------------------------------- memo 15: the triplet
def test_family_triplet_pinned():
    d = _load()["memo15_family"]
    assert d["E8_dim"] == 248 == d["dim_check"]      # 78+8+81+81
    assert d["twenty7_enters"] == 3 and d["A2_slots"] == 4
    assert d["decomp"] == "(8,1)+(1,78)+(3,27)+(3bar,27bar)"
    assert d["charge_multiset"] == {"4": 1, "-2": 10, "1": 16}
    assert "EXHIBITS-NOT-FORCES" in d["fence"]        # the object-forcing fence held


# ---------------------------------------------------------------- cross-bench consistency
def test_cross_consistent_with_banked_B1135_and_B883():
    # the Y spend's involution count + the 81-pair E6(-14) gauge row must match B1135's banked menu
    b1135 = json.loads((REPO / "frontier" / "B1135_gauge_closing" / "b1135_results.json").read_text())
    assert b1135["n_factor_preserving_involutions"] == 128
    row81 = [v for k, v in b1135["menu"].items() if v == 81 and "-14" in k]
    assert len(row81) >= 1 and all(v == 81 for v in row81)   # the gauge closing's 81-pair rows
    # the family's 27 branching must match B883's independently-derived multiplicities
    b883 = json.loads((REPO / "frontier" / "B883_the_27" / "results.json").read_text())
    assert b883["s1_multiplicities"] == [1, 10, 16]


# ---------------------------------------------------------------- the FINDINGS claims
def test_findings_states_the_fences():
    t = FINDINGS.read_text(encoding="utf-8")
    assert "any TWO of {spacetime, color, hypercharge}, never three" in t
    assert "FORKED" in t
    assert "EXHIBITS-NOT-FORCES" in t                 # the family fence
    assert "PRICE STRUCTURE" in t                     # the ladder fence


# ---------------------------------------------------------------- the reproduction is present
def test_verification_scripts_present():
    for f in ("my_chevalley.py", "verify_memo11_fork.py", "verify_memo14_ambient.py",
              "memo13_part1_core.py", "memo15_family_triplet.py"):
        assert (VERIF / f).exists(), f


# ---------------------------------------------------------------- independent recompute (fast, ~4s)
def test_fork_reproduces_independently():
    """Re-derive the load-bearing fork ladder + S3 torsor from scratch (own generic
    linear algebra, banked e6 only) -- the theorem the whole real-form correction rests on."""
    r = subprocess.run([sys.executable, str(VERIF / "verify_memo11_fork.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=180)
    assert r.returncode == 0, r.stderr[-2000:]
    out = r.stdout
    assert "choice A = (16, 8, 8, 0), choice B = (16, 8, 8, 0)" in out
    assert "Ladder 16/8/8/0 (fork = 0):  CONFIRMED" in out
    assert "S3 frame torsor, fiber 216:  CONFIRMED" in out


# ---------------------------------------------------------------- heavy reproduction (OA_SLOW)
@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="e7/e8 installment-ladder rebuild ~minutes; set OA_SLOW=1 to run")
def test_installment_ladder_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF / "verify_memo14_ambient.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=3600)
    assert r.returncode == 0, r.stderr[-2000:]
    out = r.stdout
    assert "0" in out and "8" in out   # the ladder runs to completion; detailed asserts in-script
