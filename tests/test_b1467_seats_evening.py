"""B1467 -- the seats' evening rowed and main's absence claim corrected."""
import importlib.util, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1467_the_seats_evening_and_mains_absence_claim_corrected")


def test_the_amend_and_the_correction():
    spec = importlib.util.spec_from_file_location("amend_b1467", os.path.join(A, "adoption", "amend.py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    t = m.build(); cur = open(os.path.join(ROOT, "GENESIS.md")).read()
    if "**Version 1.10 ·" in cur: assert cur == t
    assert "A version-number" in cur and "lead **L17**" in cur and "enters squared" in cur
    o = open(os.path.join(ROOT, "docs", "OPEN_LEADS.md")).read()
    assert "which reads verdict lines and FINDINGS titles only" in o and "taxonomy is incomplete" in o
    assert "the seat's literal claim holds." not in o.split("## L244")[1][:1200]
    e = open(os.path.join(ROOT, "docs", "ERROR_LEDGER.md")).read(); assert "E54 instance (this bench, L244, 2026-10-03)" in e
    h = open(os.path.join(ROOT, "docs", "HARVEST_LEDGER.md")).read()
    assert all(("| sm:B15%d |" % k) in h for k in (27, 28, 29, 30, 31, 32)) and "| audit R80/R81 |" in h and "`2eb3841f`" in h and "@ ddd345a8" in h   # the rows' own reading of the audit lane, not its moving pin (E86, found S96)
