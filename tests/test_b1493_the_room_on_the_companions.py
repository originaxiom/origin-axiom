"""B1493 -- THE ROOM ON THE COMPANIONS: the line has no room on L8a15 or o10_150729; Theorem C's caps; the readings at order
four and eight on L8a15; the controls, and the corrected second supply's consistency with the theorem at m136's members."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1493_the_room_on_the_companions" / "verification"


def test_the_line_has_no_room_on_either_companion():
    for name, chars, m in (("L8a15", 8, 3), ("o10_150729", 32, 5)):
        d = json.load(open(HERE / f"room_{name}.json")); rows = d["rows"]
        assert len(rows) == chars and d["n_trivial"] == 0 and d["max_room"] == 0
        for r in rows:
            assert r["n"] == 0 and len(r["t0"]) == m
            if name == "o10_150729": assert r["h1"] == r["m_A"]                      # all of h^1 is boundary
        triv = [r for r in rows if all(v == 1 for v in r["chi"])][0]; assert triv["h1"] == m and triv["m_A"] == m
    L = json.load(open(HERE / "room_L8a15.json"))["rows"]
    assert sorted((r["m_A"], r["h1"]) for r in L) == [(0, 0)] * 4 + [(1, 1)] * 3 + [(3, 3)]


def test_the_controls_room_can_be_nonzero_and_m136_matches_theorem_c():
    c = json.load(open(HERE / "room_m140_4_1.json")); assert c["max_room"] == 1 and c["n_trivial"] == 0      # the criterion can fail
    m = json.load(open(HERE / "control_m136.json")); assert len(m) == 8
    for r in m:
        for x in r["readings"]:
            assert x["relator_ok"] and x["I_L2W1"] >= -r["second"]                   # Theorem C: I(Lambda^2 W1) >= -n(nu^3 x four)
            assert x["I_W1"] >= -r["b0"] - r["room"]["n"]
        if r["interior"]: assert r["second"] == 1 and r["readings"][0]["I_W1"] == -1 and r["readings"][0]["I_L2W1"] == -1
    s = json.load(open(HERE / "sealed_run" / "control_m136.json"))
    assert all(r["second"] == 0 for r in s)                                           # the sealed instrument's wrong module, kept


def test_the_orbits_and_the_second_supply_at_order_eight():
    o = json.load(open(HERE / "orbits_L8a15.json")); assert o["count"] == 42 and o["by_order"] == {"1": 1, "2": 3, "4": 9, "8": 29} and len(o["group_on_H1"]) == 12
    assert sum(x["size"] for x in o["orbits"]) == 512
    s = json.load(open(HERE / "second_L8a15.json")); assert len(s["orbits"]) == 29 and s["max_room"] == 0 and s["max_second"] == 1
    ones = [x for x in s["orbits"] if x["second"] == 1]; assert len(ones) == 1 and ones[0]["rep"] == [0, 0, 1] and ones[0]["size"] == 12
    assert all(x["cap_W"] == 0 for x in s["orbits"])                                  # b0 = 0 and no room: no generation at order eight
    by = {}
    for e in s["equivariance"]: by.setdefault(tuple(e["orbit"]), set()).add((e["second"], e["room"]))
    assert len(s["equivariance"]) == 24 and all(len(v) == 1 for v in by.values())


def test_the_readings_at_order_four_and_eight_count_exactly_minus_b0():
    r4 = json.load(open(HERE / "read_L8a15_order4.json")); assert len(r4) == 9 and all(r["b0"] == 1 and r["room"]["n"] == 0 for r in r4)
    members = [r for r in r4 if r["interior"]]; assert len(members) == 1 and members[0]["rep"] == [0, 0, 2]
    assert [(x["k"], x["I_W1"], x["I_L2W1"], x["relator_ok"]) for x in members[0]["readings"]] == [(0, -1, 0, True)]
    assert all(x["I_W1"] >= -1 and x["I_L2W1"] <= 0 for r in r4 for x in r["readings"])
    r8 = json.load(open(HERE / "read_L8a15_list.json")); assert [r["rep"] for r in r8] == [[0, 0, 1], [0, 0, 3]]
    for r in r8:
        assert r["b0"] == 0 and r["room"]["n"] == 0 and r["second"] == 1 and r["interior"] == 1
        assert [(x["I_W1"], x["I_L2W1"], x["relator_ok"]) for x in r["readings"]] == [(0, 0, True)]
