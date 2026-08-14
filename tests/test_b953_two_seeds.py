"""B953 locks — E6 vs E4, and the complementary defects of the two seeds."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B953_two_seeds_rank"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def _n(p):
    return " ".join(p.read_text(encoding="utf-8").split())


def test_E4_is_SU5_and_carries_the_SM_rank():
    r = _res()
    assert r["E_n_series"]["E4=SU(5)"] == 4
    assert r["rank_SM"] == 4
    assert r["E4_is_the_rank_of_the_SM"] is True


def test_the_rank_drops_are_the_two_extra_U1s_and_the_last_step_is_free():
    r = _res()
    d = r["descent_rank_drops"]
    assert d["E6->SO(10)"]["sheds"] == "U(1)_psi" and d["E6->SO(10)"]["drop"] == 1
    assert d["SO(10)->SU(5)"]["sheds"] == "U(1)_chi" and d["SO(10)->SU(5)"]["drop"] == 1
    assert d["SU(5)->SM"]["drop"] == 0, "SU(5)->SM is rank-preserving"
    assert r["skipping_SU5_is_skipping_the_rank_reduction"] is True


def test_the_theta_split_is_exact_and_F4_has_the_SM_rank():
    r = _res()
    t = r["theta_split"]
    assert t["dim_E6"] == 78
    assert t["theta_even_F4"]["dim"] == 52 and t["theta_even_F4"]["rank"] == 4
    assert t["theta_odd_26"]["dim"] == 26
    assert t["sum_checks"] is True
    assert r["rank_F4_equals_rank_SM"] is True


def test_the_seeds_have_COMPLEMENTARY_defects_so_switching_is_no_fix():
    """The load-bearing lock: neither branch is the answer."""
    r = _res()
    even, odd = r["the_tradeoff"]["theta_even"], r["the_tradeoff"]["theta_odd"]
    assert even["rank_ok"] is True and even["chiral"] is False
    assert odd["rank_ok"] is False and odd["chiral"] is True
    assert r["switching_seed_is_not_a_fix"] is True
    assert "NOT the theta-projection" in r["what_is_actually_needed"]


def test_the_geometric_point_is_on_the_achiral_stratum_per_B576():
    r = _res()
    assert r["geometric_point_is_on_the_F4_achiral_stratum"] is True
    b576 = " ".join((ROOT / "frontier" / "B576_deformed_closure" / "FINDINGS.md")
                    .read_text(encoding="utf-8").split())
    assert "F₄-stable (achiral) stratum" in b576


def test_the_inference_is_flagged_as_inferred_not_computed():
    t = _n(CELL / "FINDINGS.md")
    assert "INFERRED from the rank" in t and "not established here" in t
    assert "does not refute anything" in t.lower()
