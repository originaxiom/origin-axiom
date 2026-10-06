"""B1486 -- the two orders at the silver members: the stored cells and controls."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1486_the_two_orders_at_the_silver_members" / "verification"


def _members(name): return json.load(open(HERE / f"fused_{name}.json"))


def test_the_controls_reproduced_b1466_and_the_three_generator_path():
    c = json.load(open(HERE / "control_c3b.json"))
    assert c["control_pass"] and c["obstruction"]["rank_L"] == 20 and c["commutant_dim"] == 1 and c["I_mixed"]["I"] == 0
    c2 = json.load(open(HERE / "control_three_generators.json")); assert c2["control_pass"]


def test_each_order_alone_is_a_cocycle_and_unobstructed_on_both_states():
    for name in ("m135", "m136"):
        for m in _members(name):
            for k in ("obstruction c1 alone", "obstruction c2 alone"):
                assert float(m[k]["first_order_residual"]) < 1e-40 and m[k]["unobstructed"], (name, k, m[k])
            assert float(m["obstruction c1 + c2"]["first_order_residual"]) < 1e-40
            assert float(m["J_c1_vs_c2_proportional"]) < 1e-30          # the two interior classes are dual through the Lorentz form


def test_the_mixed_direction_is_unobstructed_on_m135_and_the_fusion_counts_zero():
    for m in _members("m135"):
        ob = m["obstruction c1 + c2"]; assert ob["unobstructed"] and float(ob["residual"]) < 1e-40 * max(1.0, float(ob["norm_Q"]))
        conv = [f for f in m["fusions"] if f["converged"]]
        assert conv, "no fusion converged"
        for f in conv:
            assert f["commutant_dim"] == 1 and (f["invariant_line"], f["dual_invariant_line"]) == (0, 0)
            assert (f["I_X"], f["I_L2X"]) == (0, 0) and f["X"]["a1"] == f["Xdual"]["a1"] == 0
        # the two orders, in the same code path, still read opposite and non-zero
        assert (m["reference W1"]["I"], m["reference W1"]["I_L2"]) == (-1, -1) and (m["reference W2"]["I"], m["reference W2"]["I_L2"]) == (1, 1)
        assert m["reference split"]["I"] == 0 and m["reference split"]["commutant_dim"] == 2


def test_the_mixed_direction_is_unobstructed_on_m136():
    for m in _members("m136"):
        ob = m["obstruction c1 + c2"]; assert ob["unobstructed"] and float(ob["residual"]) < 1e-40 * max(1.0, float(ob["norm_Q"]))
        for f in m["fusions"]:
            if f["converged"]:
                assert f["commutant_dim"] == 1 and (f["I_X"], f["I_L2X"]) == (0, 0)
