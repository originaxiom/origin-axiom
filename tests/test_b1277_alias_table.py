"""B1277 — the reserved arc-number ranges are respected on main.

Two collisions of the same shape have now happened: B1025+ (cloud, docs/CLOUD_ALIAS_TABLE.md)
and B1267+ (SM-derivation seat, docs/SM_SEAT_ALIAS_TABLE.md). Both arose because a seat
renumbered to dodge main and main then banked into the vacated range. Renumbering is
reactive; a RESERVED RANGE checked by a gate is the fix that holds.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESERVED = [(1045, 1059), (1278, 1289)]      # cloud's, then the SM seat's


def _main_arc_ids():
    out = []
    for d in (ROOT / "frontier").iterdir():
        if d.is_dir():
            m = re.match(r"B(\d{1,4})", d.name)
            if m:
                out.append((int(m.group(1)), d.name))
    return out


def test_no_main_arc_sits_in_a_reserved_range():
    bad = [(n, name) for n, name in _main_arc_ids()
           for lo, hi in RESERVED if lo <= n <= hi]
    assert not bad, f"main arcs inside a RESERVED range (gate-worthy defect): {bad}"


def test_both_alias_tables_exist_and_are_cross_linked():
    cloud = (ROOT / "docs" / "CLOUD_ALIAS_TABLE.md").read_text(encoding="utf-8")
    sm = (ROOT / "docs" / "SM_SEAT_ALIAS_TABLE.md").read_text(encoding="utf-8")
    assert "SM_SEAT_ALIAS_TABLE" in cloud, "the older table must point at the newer one"
    assert "CLOUD_ALIAS_TABLE" in sm, "the newer table must cite the precedent"
    assert "B1278" in sm and "B1290" in sm


def test_the_six_collisions_are_all_recorded():
    sm = (ROOT / "docs" / "SM_SEAT_ALIAS_TABLE.md").read_text(encoding="utf-8")
    for n in (1267, 1272, 1273, 1274, 1275, 1276):
        assert f"B{n}" in sm, f"collision B{n} missing from the alias table"
