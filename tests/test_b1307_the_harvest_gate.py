"""B1307 -- THE HARVEST GATE: the DESIGN is sealed; the first live report and the live pin-override control are pinned from their
receipts; the pins table names every branch seat; the v0 receipt (before the parser fixes) is kept beside the first run."""
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1307_the_harvest_gate"; V = ARC / "verification"


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_first_run_is_pinned():
    r = json.loads((V / "harvest_debt_first_run.json").read_text(encoding="utf-8"))
    s = r["summary"]
    assert (s["index"], s["new_unrowed"], s["backlog"], s["stale_rows"], s["relays_unrowed"], s["aged"], s["mirror_lag"]) == (494, 6, 428, 0, 348, 0, 2)
    assert r["integrity"] == []
    assert r["seats"]["cloud"]["new_unrowed"] == ["memo 183", "memo 184"]
    assert set(r["seats"]["sm"]["new_rowed"]) == {"sm:B1281", "sm:B1303", "sm:B1304", "sm:B1350"}
    assert "FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT.md" in r["seats"]["fc"]["relays_unrowed"]
    assert r["seats"]["braver"]["relays_unrowed_named_on_main"] and len(r["seats"]["braver"]["relays_unrowed_named_on_main"]) == 131
    v0 = json.loads((V / "harvest_debt_first_run_v0_before_parser_fixes.json").read_text(encoding="utf-8"))["summary"]
    assert (v0["index"], v0["stale_rows"]) == (489, 2)          # the two STALE flags were real (hostile memos 11, 27 in a cloud row)


def test_live_control_receipt():
    t = (V / "pin_override_control.txt").read_text(encoding="utf-8")
    assert "LIVE CONTROL: PASS" in t
    assert "NEW unrowed grew by ['THE_TOWER_2026-09-08']; NEW rowed grew by ['sm:B1280', 'sm:B1282', 'sm:B1302']" in t
    assert "NEW unrowed grew by []; NEW rowed grew by []; lost []; other seats unchanged: True" in t


def test_pins_table_and_receipts_present():
    t = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert "## Pins" in t
    for key in ("sm", "fc", "codex", "cc3", "hostile", "cloud", "braver", "qor5up", "audit"):
        assert f"| {key} |" in t, key
    for f in ("harvest_debt_first_run.txt", "sense_census_routeA.txt", "sense_census_routeB.txt", "already_banked_at_seal.txt"):
        assert (V / f).is_file(), f
