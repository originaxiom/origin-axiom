"""B1494 -- NO ROOM ON ANY COMPANION: the theorem's hypothesis on the census, the companions by two routes, the room census on
m136's and m135's companions (room 2 on m135's, verified by double covers), N45 rebuilt and its room."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1494_no_room_on_any_companion" / "verification"


def test_r0_h1_is_one_at_every_torsion_character_of_every_state_to_length_twelve():
    d = json.load(open(HERE / "torsion_characters_len12.json")); assert len(d) == 758
    for r in d:
        assert r["all_one"] and r.get("b1_companion", 1) == r.get("ends", 1) == r["T"]
        if r["N"] > 1: assert len(r["primes"]) == 2 and all((p - 1) % r["N"] == 0 for p in r["primes"]) and len(r["h1"]) == r["T"]
    assert max(r["T"] for r in d) == 269 and sum(1 for r in d if r["T"] == 3) == 1          # +LLLR alone has three ends


def test_the_companions_by_two_routes_have_b1_equal_to_the_number_of_ends():
    e = json.load(open(HERE / "companions_len12.json")); assert len(e) == 24 and sorted(set(r["T"] for r in e)) == list(range(1, 11))
    assert all(r["n_candidates"] == 1 and r["companions"][0]["cusps"] == r["T"] and r["companions"][0]["b1_minus_ends"] == 0 for r in e)
    d = json.load(open(HERE / "companions_direct_len12_T60.json")); assert len(d) >= 24
    assert all(r["cusps"] == r["T"] and r["b1_minus_ends"] == 0 and abs(r["volume_ratio"] - r["T"]) < 1e-6 for r in d)
    by = {r["state"]: r for r in d}
    for r in e: assert by[r["state"]]["H1"] == r["companions"][0]["H1"]
    a = json.load(open(HERE / "routes_agree.json")); assert len(a) == 24 and all(x["isometric"] and x["H1_enum"] == x["H1_direct"] for x in a)   # the two routes: isometric on every state
    s = json.load(open(HERE / "seen_companions_named.json")); known = {r["state"]: r["companions"][0] for r in s}
    assert known["+LLLR"]["sym"] == 12 and known["+LLLR"]["chiral"] and known["+LLRR"]["sym"] == 32 and known["-LLRR"]["sym"] == 256 and known["-LR"]["sym"] == 240


def test_r1_room_zero_on_m136s_companion_and_r2_room_two_on_m135s():
    a = json.load(open(HERE / "room_m136_companion.json")); assert a["cusps"] == 4 and a["characters"] == 16 and a["max_room"] == 0 and a["n_trivial"] == 0
    assert all(r["h1"] == r["m_A"] for r in a["rows"]) and sorted(collections.Counter(r["m_A"] for r in a["rows"]).items()) == [(0, 9), (2, 6), (4, 1)]
    b = json.load(open(HERE / "room_m135_companion.json")); assert b["cusps"] == 8 and b["characters"] == 256 and b["max_room"] == 2 and b["n_trivial"] == 0
    c = collections.Counter((r["m_A"], r["h1"], r["n"]) for r in b["rows"]); assert c == {(2, 2, 0): 168, (4, 4, 0): 42, (0, 0, 0): 37, (0, 2, 2): 8, (8, 8, 0): 1}
    assert all(r["m_A"] == 0 for r in b["rows"] if r["n"])                                   # room only where no end is special
    dc = json.load(open(HERE / "room_m135_companion_double_covers.json")); assert len(dc["covers"]) == 255 and dc["b1"] == 8
    assert dc["by_mA_room"] == {"(4, 0)": 42, "(2, 0)": 168, "(0, 0)": 37, "(0, 2)": 8}
    x = json.load(open(HERE / "extra_m135_companion_order8.json")); r = x["row"]
    assert r["b0"] == 0 and r["room"]["n"] == 2 and r["cap_W"] == 2 and r["m_A"] == 0 and r["interior"] == 0 and r["other"] == 0 and r["second"] == 0


def test_r3_n45_rebuilt_and_r4_its_room():
    n = json.load(open(HERE / "n45.json")); assert len(n["candidates"]) == 1 and len(n["degree9"]) == 4
    c = n["candidates"][0]; assert c["cusps"] == 5 and c["b1"] == 9 and c["n1"] == 4 and abs(c["volume_over_m003"] - 45) < 1e-6 and c["sym"] == 240
    r = json.load(open(HERE / "room_n45.json")); assert r["cusps"] == 5 and r["characters"] == 2048 and r["n_trivial"] == 4
    rooms = collections.Counter(x["n"] for x in r["rows"]); assert dict(rooms) == {0: 766, 1: 435, 2: 560, 3: 30, 4: 247, 6: 10} and r["max_room"] == 6
    f = json.load(open(HERE / "room_n45_fourth_powers.json")); assert f["rank"] == 9 and f["fourth_powers"] == 512 and len(f["cusp_trivial_fourth_powers"]) == 16
    assert f["rooms_nontrivial"] == {"1": 10, "3": 5}                                         # the seat's fifteen: ten at room 1, five at room 3
    assert all(x["n"] in (1, 3, 4) for x in f["cusp_trivial_fourth_powers"])
