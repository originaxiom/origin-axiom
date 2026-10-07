"""B1489 -- the SM seat's nine proposals ruled: GENESIS at v1.16, the amendment reproduces it, the bookkeeping holds."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1489_the_sm_seats_nine_proposals_ruled"


def test_genesis_is_at_v1_16_with_nine_rulings_and_the_amendment_reproduces_it():
    g = (HERE.parents[1] / "GENESIS.md").read_text()
    assert "**Version 1.16 " in g and g.count("[v1.16") >= 9 and "the SM seat's P9, recorded under FK14" in g
    r = subprocess.run([sys.executable, str(HERE / "adoption" / "amend.py"), "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_the_bookkeeping_check_holds():
    d = json.load(open(HERE / "verification" / "proposals_check.json"))
    assert d["ok"] and d["v1_16_marks"] == 9 and d["all_cited_arcs_rowed"] and d["anchors_unique_in_v1_15"]
    assert all(v >= 1 for v in d["marks_in_the_seats_file"].values()) and d["marks_in_the_seats_file"]["P3"] == 2
