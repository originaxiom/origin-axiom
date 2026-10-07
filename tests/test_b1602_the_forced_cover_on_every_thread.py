"""B1602 -- THE FORCED COVER ON EVERY THREAD: the census as recorded (74 threads), the four cells, the carrier and the controls."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1602_the_forced_cover_on_every_thread" / "verification"


def test_the_census_and_the_cells_as_recorded():
    s = json.load(open(HERE / "summary.json"))
    assert s["threads"] == 74 and s["read"] == 74 and not s["missing"] and s["odd"] == 32 and s["even"] == 42
    assert s["T1_len6_odd_no_member"]["holds"]
    assert not s["T2_len8_odd_no_member"]["holds"] and s["T2_len8_odd_no_member"]["carriers"] == ["b+-LLRLRLRR"]
    assert not s["T3_every_even_carries"]["holds"] and s["T3_every_even_carries"]["carriers"] == 17 and len(s["T3_every_even_carries"]["non_carriers"]) == 25
    assert s["T4_trivial_character"]["first_half_holds"] and not s["T4_trivial_character"]["second_half_holds"]
    assert s["T4_trivial_character"]["odd_with_trivial_class"] == [] and len(s["T4_trivial_character"]["even_with_trivial_class"]) == 8
    assert s["odd_carriers"] == ["b++LR", "b+-LR", "b+-LLRLRLRR"]
    assert s["kernels_per_class"] == {"A4": [1], "D4": [2], "V4": [4]} and s["cusps_per_class"]["A4"] == [4]


def test_the_carrier_and_the_controls():
    d = json.load(open(HERE / "read_b+-LLRLRLRR.json"))
    assert d["cusps"] == 4 and len(d["members"]) == 1
    m = d["members"][0]; r = m["readings"][0]
    assert (m["h1"], m["r1"], m["n"]) == (4, 3, 1) and m["t0"] == [0, 0, 0, 0]
    assert (r["I_W1"], r["I_L2W1"]) == (3, 1) and r["dead_on_cusps"] == [False, False, False, False]
    plus = json.load(open(HERE / "read_b++LR.json")); minus = json.load(open(HERE / "read_b+-LR.json"))
    assert all((r["I_W1"], r["I_L2W1"]) == (-1, -1) and all(r["dead_on_cusps"]) for m in plus["members"] for r in m["readings"])
    assert all((r["I_W1"], r["I_L2W1"]) == (0, -3) and all(r["dead_on_cusps"]) for m in minus["members"] for r in m["readings"])


def test_every_thread_file_is_consistent_with_the_census():
    rows = [json.loads(l) for l in open(HERE / "census_8.jsonl") if l.strip()]
    assert len(rows) == 74
    for r in rows:
        d = json.load(open(HERE / f"forced_{r['thread']}.json"))
        assert d["any_member"] == r["any_member"] and [c["members"] for c in d["covers"]] == [c["members"] for c in r["covers"]]
        assert d["orientable"] and all(abs(c["volume_ratio"] - {"A4": 12, "D4": 8, "V4": 4}[d["deck"]]) < 1e-6 for c in d["covers"])
