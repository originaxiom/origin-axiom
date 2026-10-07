"""B1603 -- THE COUNT AT EVERY MEMBER: the five cells as recorded; the floor and ceiling on every reading."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1603_the_count_at_every_member" / "verification"


def test_the_cells_as_recorded():
    s = json.load(open(HERE / "summary.json"))
    assert s["threads"] == 20 and s["members"] == 242 and s["readings"] == 442
    assert s["C1_plus_LR_all_generation_shaped"]["holds"] and s["C1_plus_LR_all_generation_shaped"]["readings"] == 24
    assert s["C2_minus_LR_all_0_minus_3"]["holds"] and s["C2_minus_LR_all_0_minus_3"]["readings"] == 24
    assert not s["C3_no_even_generation_shaped"]["holds"] and sum(s["C3_no_even_generation_shaped"]["even_generation_shaped"].values()) == 98
    assert s["C4_floor_and_ceiling"]["holds"] and s["C4_floor_and_ceiling"]["floor_fails"] == 0 and s["C4_floor_and_ceiling"]["ceiling_fails"] == 0
    assert not s["C5_at_most_five_kinds"]["holds"] and s["C5_at_most_five_kinds"]["count"] == 8
    assert s["generation_shaped_total"] == 122 and s["odd_threads_generation_shaped"] == {"b++LR": 24}
    assert s["generation_shaped_by_thread"]["b++LLR"] == 12 and s["generation_shaped_by_thread"]["b+-LLRR"] == 12


def test_every_reading_obeys_the_floor_and_ceiling_and_the_files_agree():
    s = json.load(open(HERE / "summary.json")); n = 0
    for t in s["readings_by_thread"]:
        d = json.load(open(HERE / f"count_{t}.json"))
        for cv in d["covers"]:
            for m in cv["members"]:
                for r in m["readings"]:
                    n += 1; assert r["floor_holds"] and r["ceiling_holds"], (t, m["nu"], r)
                    assert r["generation_shaped"] == ((r["I_W1"], r["I_L2W1"]) == (-1, -1) and all(r["dead_on_cusps"]))
    assert n == 442
