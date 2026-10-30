"""B1823 -- Step A v2, the tied heavy sector's one-loop vacuum: NEGATIVE as a compression.  The committed results carry the
sealed reading per n (n = 1-3 fail, n = 4-8 pass in the CHOSEN sup/N convention, on the draft's run and main's stable-F
rerun alike), the convention-free ranks recomputed by main (Z n = 2: 1; Z n = 5: 6), the referee's FAIL, and the
anomaly that requires H_u.  A rank rule that cannot tell 1 from 6 must fail the control."""
import json, pathlib
from fractions import Fraction as Fr
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1823_step_a_the_tied_heavy_vacuum" / "verification"


def test_the_sealed_reading():
    c = json.loads((V / "main" / "compare_D.json").read_text(encoding="utf-8"))["per_n"]
    for who in ("draft", "rerun"):
        assert [c[str(n)][who]["passes"] for n in range(1, 9)] == [False, False, False, True, True, True, True, True], who


def test_the_convention_free_ranks():
    j = json.loads((V / "main" / "conv_jacobian_main.json").read_text(encoding="utf-8"))
    assert j["Z n=2"]["rank_mu"] == 1 and j["Z n=2"]["rank_all"] == 1
    assert j["Z n=5"]["rank_mu"] == 1 and j["Z n=5"]["rank_all"] == 6
    assert abs(j["Z n=2"]["one_minus_overlap_S_with_W1xW2"]) < 1e-30
    assert abs(j["Z n=5"]["V0_mp"] - j["Z n=5"]["V0_numpy"]) < 1e-10


def test_the_referee_and_the_anomaly():
    r = json.loads((V / "referee" / "REPORT.json").read_text(encoding="utf-8"))
    assert r["verdict"] == "FAIL" and len(r["blocking"]) == 3
    # three Higgsino doublets of Y = -1/2: Tr Y^3 = -3/4, Tr Y = -3; the doublet count 12 + 2n + 3 is odd (Witten)
    ys = [Fr(-1, 2)] * 6
    assert sum(y ** 3 for y in ys) == Fr(-3, 4) and sum(ys) == -3
    assert all((12 + 2 * n + 3) % 2 == 1 for n in range(1, 9))


def test_the_rank_rule_can_fail():
    rank = lambda s: int((s > 1e-6 * s[0]).sum())
    assert rank(np.array([0.66, 8.7e-17, 2.2e-17])) == 1 and rank(np.array([2.9, 2.1, 0.63, 0.23, 0.095, 0.023])) == 6
