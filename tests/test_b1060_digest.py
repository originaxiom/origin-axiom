"""B1060 locks -- the digest ledger: structure, vocabulary, the open-state counts."""
import pathlib, re

LED = (pathlib.Path(__file__).resolve().parents[1] / "frontier" /
       "B1060_digest_ledger" / "DIGEST_LEDGER.md")
VOCAB = {"EMPTY", "ACCEPTED", "ACCEPTED-WEAK", "CORRECTED", "REFUTED",
         "SUPERSEDED", "COLLIDES", "NOT-REACHED"}


def _rows():
    txt = LED.read_text()
    rows = []
    for line in txt.splitlines():
        if line.startswith("| ") and not line.startswith("| row") and "---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3 and cells[0] and cells[0][0].isdigit():
                rows.append(cells)
    return rows


def test_structure_and_vocabulary():
    rows = _rows()
    assert len(rows) >= 50, f"denominator eroded: {len(rows)} rows"
    for c in rows:
        disp = c[2].split()[0] if c[2] else ""
        assert any(disp.startswith(v) for v in VOCAB), f"bad disposition: {c[:3]}"


def test_arcs_lane_complete():
    txt = LED.read_text()
    for n in range(1024, 1054):
        assert f"qB{n}" in txt, f"missing arc row qB{n}"


def test_close_state_is_declared():
    # B1173: the digest PARTIAL-CLOSED (owner-directed O4). The lock now pins the closed state:
    # zero EMPTY rows (13 NOT-REACHED via the ledger's own honesty vocabulary), the L185 umbrella
    # pointer, and the qor5up release. The denominator stays 58 (test_structure_and_vocabulary).
    txt = LED.read_text()
    assert "DIGEST STATUS: CLOSED-PARTIAL" in txt
    assert txt.count("| EMPTY |") == 0, "EMPTY rows survived the partial-close"
    assert txt.count("NOT-REACHED at partial-close") == 13
    assert "L185" in txt and "FROZEN-RECORD-CLOSED" in txt
    assert "L185+" in txt  # the stale L165+ renumber instruction is corrected
