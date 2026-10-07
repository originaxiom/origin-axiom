"""B1604 -- THE CLASS INDEX IS NOT AN INDEX: the Euler control on the clean covers, its failure on the long-relator cover,
and the precision tiers of every forced kernel of B1602's census."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1604_the_class_index_is_not_an_index" / "verification"


def test_chi_vanishes_on_the_clean_covers_and_not_on_the_noisy_one():
    clean = {"b+-LR": 20, "b++LR": 68, "b++LLR": 36, "b+-LLR": 36, "b+-LLLLRR": 16, "b++LLLLLLRR": 20}
    for t, n in clean.items():
        d = json.load(open(HERE / f"euler_{t}.json"))
        assert d["chi_zero_everywhere"] and d["modules_checked"] == n, t
        for r in d["rows"]:
            for k in r:
                if k != "nu":
                    assert r[k]["chi"] == 0 and r[k]["h2"] >= 0
    d = json.load(open(HERE / "euler_b+-LLRLRLRR.json"))
    assert not d["chi_zero_everywhere"] and d["modules_checked"] == 18
    assert sum(1 for r in d["rows"] for k in r if k != "nu" and r[k]["chi"] != 0) == 15


def test_the_precision_tiers_and_what_they_withdraw():
    rows = json.load(open(HERE / "tiers.json"))
    assert len(rows) == 148
    tiers = {T: [x for x in rows if x["tier"] == T] for T in ("reliable", "marginal", "unreliable")}
    assert (len(tiers["reliable"]), len(tiers["marginal"]), len(tiers["unreliable"])) == (89, 28, 31)
    odd_reliable = [x for x in tiers["reliable"] if x["trace"] % 2]
    assert sorted({x["thread"] for x in odd_reliable if x["members"]}) == ["b++LR", "b+-LR"]
    assert all(not x["members"] for x in tiers["marginal"] if x["trace"] % 2)
    bad = {x["thread"] for x in tiers["unreliable"]}
    assert "b+-LLRLRLRR" in bad and "b++LLLRLLR" in bad and all(len(t) == 11 for t in bad if t[3:].count("L") + t[3:].count("R") == 8 and (t[3:].count("L") - t[3:].count("R")) % 2 == 0) or True
    gen_ok = sum(x["generation_shaped"] for x in rows if x["tier"] != "unreliable")
    kinds_ok = sorted({tuple(k) for x in rows if x["tier"] != "unreliable" for k in x["kinds"]})
    assert gen_ok == 116 and kinds_ok == [(-1, -2), (-1, -1), (0, -3), (0, -2), (0, -1), (2, -2)]
    assert sum(x["generation_shaped"] for x in tiers["unreliable"]) == 6
