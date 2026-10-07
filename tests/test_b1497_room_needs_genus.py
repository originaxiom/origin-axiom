"""B1497 -- ROOM NEEDS GENUS: the theorem's inequality on every cover built (genus 1 => room 0), the censuses of m003, m004 and
+LLLR, the room-carrying cover o10_150691, and its readings at sign and order-four characters."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1497_room_needs_genus" / "verification"


def test_genus_one_means_room_zero_on_every_cover_built():
    s = json.load(open(HERE / "census_summary.json"))
    assert s["m003"]["covers"] == 35 and s["m004"]["covers"] == 39 and s["+LLLR"]["covers"] == 22
    assert all(s[k]["genus1_room0"] for k in s)
    for name, f in (("m003", "fibre_census_m003_D8.json"), ("m004", "fibre_census_m004_D8.json"), ("+LLLR", "fibre_census_b++LLLR_D6.json")):
        rows = json.load(open(HERE / f))
        assert all(r["room"] == 0 for r in rows if r["fibre_genus"] == 1) and all(r["fibre_genus"] >= 2 for r in rows if r["room"] > 0)
        assert all(r["room"] >= 0 and r["degree"] == r["base_degree"] * r["fibre_degree"] for r in rows)


def test_the_familys_room_is_on_m003s_degree_five_cover_only():
    s = json.load(open(HERE / "census_summary.json"))
    assert s["m004"]["room_rows"] == [] and s["+LLLR"]["room_rows"] == [] and s["m004"]["genus_ge2"] == 24
    assert [tuple(r) for r in s["m003"]["room_rows"]] == [(5, 1, 5, 3, 2, 2, "Z + Z + Z", 1)] * 2
    rows = json.load(open(HERE / "fibre_census_m003_D8.json")); lvl9 = [r for r in rows if r["degree"] == 8 and r["base_degree"] == 8]; assert len(lvl9) == 1 and lvl9[0]["fibre_genus"] == 1


def test_o10_150691_at_sign_characters_the_first_member_at_the_trivial_character():
    d = json.load(open(HERE / "room_o10_150691.json")); assert len(d["rows"][0]["t0"]) == 2 and d["n_trivial"] == 1 and d["max_room"] == 1
    assert all(r["h1"] == r["m_A"] for r in d["rows"] if any(c != 1 for c in r["chi"]))
    s = json.load(open(HERE / "survey_o10_150691.json")); rows = s["rows"]; triv = [r for r in rows if all(v == 1 for v in r["nu"].values())][0]
    assert triv["V"]["a1"] == 3 and triv["interior"] == 1 and triv["other"] == 2 and triv["readings"][0]["I_W1"] == -1 and triv["readings"][0]["I_L2W1"] == -1
    every = [x for r in rows for x in r["readings"]]; assert max(-x["I_W1"] for x in every) == 1 and sum(1 for r in rows if r["interior"]) == 5


def test_o10_150691_at_order_four_characters_the_cap_is_two_and_the_count():
    o = json.load(open(HERE / "order4_o10_150691.json")); assert len(o) == 56
    every = [x for r in o for x in r["readings"]]; assert all(r["b0"] == 1 and r["room"]["n"] == 1 for r in o)
    assert max(-x["I_W1"] for x in every) == 1 and all(x["relator_ok"] for x in every)
    assert max(r["interior"] for r in o) == 2
