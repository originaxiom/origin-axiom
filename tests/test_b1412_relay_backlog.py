"""B1412 lock: every relay file on the four retiring lanes' branches has a RELAY_LEDGER row (checked from the arc's own
triage table, so it needs no branch fetch), and the residue is exactly the fifteen named OPEN rows."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1412_the_relay_backlog", "verification")
LEDGER = open(os.path.join(ROOT, "docs", "RELAY_LEDGER.md"), encoding="utf-8").read()

def _rowed(name):
    return re.search(r"^\|\s*`" + re.escape(name) + r"`", LEDGER, re.M) is not None

def test_every_triaged_relay_has_a_row():
    tri = json.load(open(os.path.join(V, "relay_triage.json"), encoding="utf-8"))
    assert len(tri) == 342, len(tri)
    missing = [r["name"] for r in tri if not _rowed(r["name"])]
    assert not missing, missing[:10]

def test_the_residue_is_fifteen_open_rows_escalated_by_name():
    tri = json.load(open(os.path.join(V, "relay_triage.json"), encoding="utf-8"))
    names = [r["name"] for r in tri]
    opens = [n for n in names if re.search(r"^\|\s*`" + re.escape(n) + r"`\s*\|\s*OPEN\s*\|", LEDGER, re.M)]
    assert len(opens) == 15, (len(opens), opens[:5])
    for n in opens:
        row = re.search(r"^\|\s*`" + re.escape(n) + r"`[^\n]*$", LEDGER, re.M).group(0)
        assert "ESCALATED(2026-09-15)" in row, n
