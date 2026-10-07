"""B1492 -- THE THREE-ENDED COMPANION READ: the sealed surveys on L8a15 (+LLLR's three-ended companion) and on m003's
five-ended companion o10_150729, their summary, and the controls on m135/m136 (B1485's census and members row for row)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1492_the_three_ended_companion_read" / "verification"


def rows(name):
    d = json.load(open(HERE / f"survey_{name}.json")); return d, d["rows"]


def test_the_controls_reproduce_b1485_on_the_one_cusped_members():
    for name, m_A in (("m135", 1), ("m136", 0)):
        rs = json.load(open(HERE / f"control_{name}.json"))["rows"]; assert len(rs) == 8
        members = [r for r in rs if r["interior"]]
        assert [tuple(r["nu"][g] for g in "abc") for r in members] == [(1, -1, -1), (-1, -1, 1)] and all(r["m_A"] == m_A for r in members)
        for r in members:
            assert [(x["cls"], x["k"], x["I_W1"], x["I_L2W1"]) for x in r["readings"]][0] == ("interior 0", 0, -1, -1)
        if name == "m135": assert all([(x["I_W1"], x["I_L2W1"]) for x in r["readings"] if x["cls"].startswith("other")] == [(0, -1)] for r in members)


def test_d1_d2_d3_on_the_three_ended_companion():
    d, rs = rows("L8a15"); assert d["cusps"] == 3 and len(rs) == 8
    triv = [r for r in rs if all(v == 1 for v in r["nu"].values())][0]
    assert triv["V"]["a1"] == 3 and triv["interior"] == 0 and triv["other"] == 3 and triv["m_A"] == 3                    # D1: one boundary-type class per end
    assert all((x["k"], x["I_W1"], x["I_L2W1"]) == (3, 0, 0) for x in triv["readings"])
    every = [x for r in rs for x in r["readings"]]
    assert max(-x["I_W1"] for x in every) == 1 and min(x["I_W1"] for x in every) == -1 and max(x["I_W1"] for x in every) == 0   # D2: no two, no three
    members = [r for r in rs if r["interior"]]
    assert len(members) == 3 and all(r["m_A"] == 0 for r in members)                                                      # D3: members, all where no end is trivial
    assert all([(x["k"], x["I_W1"], x["I_L2W1"], x["dead_on_cusps"]) for x in r["readings"]] == [(0, -1, -1, [True] * 3)] for r in members)
    one_end = [r for r in rs if r["m_A"] == 1]
    assert len(one_end) == 3 and sorted(tuple(r["cusp_trivial"]) for r in one_end) == [(False, False, True), (False, True, False), (True, False, False)]
    assert all(r["interior"] == 0 and r["other"] == 1 and r["readings"][0]["I_W1"] == 0 for r in one_end)                 # one per end, counting zero
    assert all(r["interior"] == 0 for r in rs if r["m_A"] >= 1)                                                           # no interior class where an end is trivial
    assert sum(1 for r in rs if r["V"]["a1"] == 0) == 1


def test_the_floor_and_both_ceilings_hold_at_every_reading():
    for name in ("L8a15", "o10_150729"):
        d, rs = rows(name); m = d["cusps"]
        for r in rs:
            for x in r["readings"]:
                assert x["I_W1"] >= x["k"] - r["m_A"] - r["b0"], (name, r["nu"], x["cls"])
                assert x["I_W1"] <= 2 * r["m_A"] - r["b0"] <= 2 * r["m_A"] + (m - r["m_A"]) - r["b0"], (name, r["nu"], x["cls"])


def test_d4_on_the_five_ended_companion_and_the_summary():
    d, rs = rows("o10_150729"); assert d["cusps"] == 5 and len(rs) == 32
    triv = [r for r in rs if all(v == 1 for v in r["nu"].values())][0]
    assert triv["V"]["a1"] == 5 and triv["interior"] == 0 and triv["other"] == 5 and all((x["k"], x["I_W1"]) == (5, 0) for x in triv["readings"])
    every = [x for r in rs for x in r["readings"]]
    assert max(-x["I_W1"] for x in every) < 3
    s = json.load(open(HERE / "summary.json"))
    assert s["verdicts"] == {"D1": True, "D2": True, "D3": True, "D4": True, "D4_every_character_no_three": True}
    for name in ("L8a15", "o10_150729"):
        assert s[name]["interior_all_minus_one"] and s[name]["max_generations"] == 1 and not s[name]["floor_violations"] and not s[name]["ceiling_seat_violations"]
    assert s["L8a15"]["m_A_at_members"] == [0] and s["L8a15"]["n_members"] == 3 and s["L8a15"]["no_interior_where_an_end_is_trivial"]
