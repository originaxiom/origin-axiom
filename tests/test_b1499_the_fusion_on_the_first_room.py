"""B1499 -- THE FUSION ON THE FIRST ROOM: the mixed direction unobstructed, two irreducible fusions at the arithmetic floor, each counting (0, 0)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1499_the_fusion_on_the_first_room" / "verification"


def test_the_fusions_are_irreducible_and_count_zero():
    f = json.load(open(HERE / "fusion_o10_150691_2_0_0.json")); assert f["classes"] == [2, 2] or tuple(f["classes"]) == (2, 2)
    assert f["obstruction c + d"]["unobstructed"] and f["obstruction c alone"]["unobstructed"] and f["obstruction d alone"]["unobstructed"]
    assert f["split S"]["I"] == 0 and f["W1 (c alone)"] == {"I": 0, "I_L2": -1, "n": 2, "n_dual": 2} and f["W2 (d alone)"] == {"I": 0, "I_L2": 1, "n": 2, "n_dual": 2}
    assert len(f["fusions"]) == 2
    for r in f["fusions"]:
        assert r["at_floor"] and not r["converged"] and r["commutant_dim"] == 1 and not r["invariant_line"] and not r["dual_invariant_line"]
        assert r["count"] == {"I": 0, "I_L2": 0, "n": 0, "n_dual": 0}
