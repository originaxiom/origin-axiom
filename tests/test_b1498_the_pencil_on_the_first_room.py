"""B1498 -- THE PENCIL ON THE FIRST ROOM: every rank-five extension at the eight two-class characters of o10_150691 reads (0, -1)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1498_the_pencil_on_the_first_room" / "verification"


def test_the_pencil_is_constant_and_reads_zero_at_all_eight_characters():
    d = json.load(open(HERE / "pencil_o10_150691.json")); assert len(d) == 8
    for r in d:
        assert all((b["I_W1"], b["I_L2W1"], b["relator_ok"]) == (0, -1, True) for b in r["basis"])
        assert len(r["pencil"]) == 6 and all((v["I_W1"], v["I_L2W1"], v["relator_ok"]) == (0, -1, True) for v in r["pencil"].values())
        assert r["generic_I_W1"] == 0 and r["special_values"] == [0] and r["rank6_both"]["I"] == -1 and r["rank6_both"]["relator_ok"]
