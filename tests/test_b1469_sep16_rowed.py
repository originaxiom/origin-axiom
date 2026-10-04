"""B1469 -- the sep16 lane and the cloud's memos rowed; the lane's claims about main listed to verify."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1469_the_sep16_lane_and_the_clouds_memos_rowed")


def test_rows_pins_and_the_lead():
    h = open(os.path.join(ROOT, "docs", "HARVEST_LEDGER.md")).read()
    assert all(("| xB%03d |" % k) in h for k in range(3, 35)) and "| memo 236 |" in h
    assert "| sep16 | `<remote>/sep16-branch` | `3205984b` |" in h and "| cloud | `<remote>/outside-bench` | `13d2c5b6` |" in h
    o = open(os.path.join(ROOT, "docs", "OPEN_LEADS.md")).read(); assert "## L245 — THE SEP16 LANE'S CLAIMS ABOUT MAIN, TO VERIFY" in o and "- **xB003:**" in o
    d = json.load(open(os.path.join(A, "verification", "readers_sep16.json"))); assert len(d) == 31 and sum(len(r.get("claims_about_main") or []) for r in d) >= 90
