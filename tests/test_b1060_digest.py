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


def test_open_state_is_declared():
    txt = LED.read_text()
    assert "DIGEST STATUS: OPEN" in txt
    # while OPEN, EMPTY rows are legal; the completion lock ships with the closing
    # arc and will assert zero EMPTY. This lock only pins the declared state.
    n_empty = txt.count("| EMPTY |")
    assert n_empty > 0 or "DIGEST STATUS: CLOSED" in txt
