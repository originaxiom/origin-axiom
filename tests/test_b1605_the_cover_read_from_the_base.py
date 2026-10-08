"""B1605 -- THE COVER READ FROM THE BASE: the certified re-read of the 29 threads B1604's audit found unreliable, and
the +-LR validation against B1602."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1605_the_cover_read_from_the_base" / "verification"


def test_the_cells_as_recorded():
    s = json.load(open(HERE / "summary.json"))
    assert s["population"] == 29 and s["odd"] == 19 and s["even"] == 10 and s["kernels"] == 39
    assert s["V1_pm_LR_reproduced"] and s["R1_all_accepted"] and s["R2_no_odd_carrier"]
    assert s["max_residual"] < 1e-30
    assert set(s["R3_even_status_changes"]) == {"b+-LLRLRLRR", "b++LLLRLLR"}
    assert s["R4_kinds"] == [[-1, -2], [-1, -1]] and s["even_carriers"] == ["b++LLLLLLR"]
    assert s["generation_shaped_on_population"] == 4


def test_every_kernel_certified_and_the_odd_threads_empty():
    pop = [l.strip() for l in open(HERE / "unreliable_threads.txt") if l.strip()]
    for t in pop:
        d = json.load(open(HERE / f"schreier_{t}.json"))
        for c in d["covers"]:
            assert float(c["four_residual"]) < 1e-30 and c["chi_fails"] == 0, (t, c["four_residual"], c["chi_fails"])
    third = json.load(open(HERE / "schreier_b+-LLRLRLRR.json"))
    assert all(c["member_count"] == 0 for c in third["covers"])
    plus = json.load(open(HERE / "schreier_b++LR.json"))["covers"][0]; minus = json.load(open(HERE / "schreier_b+-LR.json"))["covers"][0]
    assert plus["member_count"] == 24 and plus["structures"] == [[1, 0, 1]] and plus["kinds"] == [[-1, -1]]
    assert minus["member_count"] == 6 and minus["structures"] == [[4, 0, 4]] and minus["kinds"] == [[0, -3]]
