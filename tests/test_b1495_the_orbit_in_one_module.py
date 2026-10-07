"""B1495 -- THE ORBIT IN ONE MODULE: L8a15's three members as one rank-15 module read (10', 5bar') = (3, 9); the cross terms
-2 each, carried around the ends by the deck; the piece responsible; the control on m136."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1495_the_orbit_in_one_module" / "verification"


def test_the_orbit_module_counts_three_and_nine():
    d = json.load(open(HERE / "cross_L8a15.json")); assert len(d["members"]) == 3 and len(d["cross"]) == 3
    assert all((x["I_W1"], x["I_L2W1"]) == (-1, -1) for x in d["single"])
    assert all(x["I"] == -2 and x["relator_ok"] for x in d["cross"]) and d["I_W"] == -3 and d["I_L2W"] == -9
    t0s = sorted(tuple(x["E"]["t0"]) for x in d["cross"]); assert t0s == [(1, 1, 5), (1, 5, 1), (5, 1, 1)]      # the deck carries the special end around


def test_the_piece_responsible_and_the_control():
    p = json.load(open(HERE / "cross_pieces.json"))
    assert p["V_i x V_j (16)"]["I"] == 0 and p["W_i x V_j (20; sub)"]["I"] == -1 and p["V_i x W_j (20; sub)"]["I"] == -1 and p["W_i x W_j (25)"]["I"] == -2
    assert p["W_i x W_j (25)"]["n"] == 0 and p["W_i x W_j (25)"]["n_dual"] == 2 and p["line nu_i nu_j"]["n"] == 0 and p["four x nu_i nu_j"]["n"] == 0
    c = json.load(open(HERE / "cross_m136.json")); assert c["I_W"] == -2 and c["I_L2W"] == -3 and [x["I"] for x in c["cross"]] == [-1]
