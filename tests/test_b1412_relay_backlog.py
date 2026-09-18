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
    """B1412 left 15 of its 342 relays OPEN and escalated each by name on 2026-09-15.

    REWRITTEN 2026-09-18 (B1425). The original form asserted those 15 are *still* OPEN, which pinned a
    TRANSIENT state: the backlog was then paid, and by today all 342 rows read BANKED or DECLINED, so the
    lock went red for the arc having succeeded. The durable facts are the two below -- the escalation
    happened and is still recorded, and no relay from that window is left open -- and a lock should hold
    those, not a snapshot of the queue on one day.
    """
    tri = json.load(open(os.path.join(V, "relay_triage.json"), encoding="utf-8"))
    rows = {}
    for r in tri:
        m = re.search(r"^\|\s*`" + re.escape(r["name"]) + r"`\s*\|\s*(\w+)\s*\|[^\n]*$", LEDGER, re.M)
        assert m, "triaged relay has no ledger row: %s" % r["name"]
        rows[r["name"]] = m.group(0)
    escalated = [n for n, row in rows.items() if "ESCALATED(2026-09-15)" in row]
    assert len(escalated) == 15, (len(escalated), escalated[:5])
    still_open = [n for n, row in rows.items() if re.match(r"^\|[^|]*\|\s*OPEN\s*\|", row)]
    assert not still_open, "relays from B1412's window left open: %s" % still_open[:5]
