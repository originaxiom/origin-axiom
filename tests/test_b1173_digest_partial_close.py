"""B1173 lock -- the digest partial-close (O4). The state pins live in test_b1060_digest (updated);
this lock pins the arc record + the discharge claims."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1173_digest_partial_close"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1173" and d["verdict"] == "OPEN"
    assert "CLOSED-PARTIAL" in d["claim_one_line"] and "L185+" in d["claim_one_line"]
    assert "R47-3 AND R48-5 DISCHARGE" in d["claim_one_line"]


def test_l185_and_release_on_record():
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "## L185" in leads and "QOR5UP UNPORTED RESIDUE" in leads
    reviews = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    assert "FROZEN-RECORD-CLOSED" in reviews and "R47-3" in reviews


def test_reproduce_runner_committed():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
