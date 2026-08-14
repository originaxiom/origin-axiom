"""B935 + B938 locks: the rank-2 degeneracy, composition rigidity, the coset verdict."""
import json
import os

FR = os.path.join(os.path.dirname(__file__), "..", "frontier")


def _r(arc):
    with open(os.path.join(FR, arc, "results.json")) as f:
        return json.load(f)


def test_b935_rank_two_and_no_band_flags():
    r = _r("B935_composition_hunt")
    assert r["band_flags_1p2_1p6"] == []
    t = json.dumps(r)
    assert "X2_rank" in t and "X4_rank" in t
    # both ranks recorded as 2 (DATA rows store {"value":..., "detail":...})
    assert r["checks"]["X2_rank"]["value"] == 2
    assert r["checks"]["X4_rank"]["value"] == 2


def test_b935_composition_rigidity_forced():
    r = _r("B935_composition_hunt")
    ch = r["checks"]
    for k in ("FORCED_eig_Ci_equals_eig_Ghat", "FORCED_eig_C4_equals_eig_Ghat",
              "FORCED_eig_GhatR_equals_eig_RGhat"):
        assert ch[k]["pass"] is True


def test_b938_no_swap_coset_verdict():
    r = _r("B938_unity_and_sign")
    v = r["verdict_7_11"]
    assert v["swap_11_to_minus1_7sq_to_plus1"] is False
    # D is level-degenerate on the colorless register: all-zero prime tables
    assert all(all(x == [0, 0] for x in fam.values())
               for fam in v["D"].values())
    assert "COSET INVARIANT" in r["verdict"]
