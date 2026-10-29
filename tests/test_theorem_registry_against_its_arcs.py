"""P-484 (2026-10-29): the theorem registry against its arcs.  Two rows (B1672, B1673) once stated refuted claims as PROVED
while their arcs were NEGATIVE.  This lock reads every registry row, takes the first arc its arc cell names (the row's own
arc), and fails if the status cell reads PROVED while that arc's verdict is NEGATIVE, OPEN or RETRACTED -- unless the
status cell itself carries the scope (a NEGATIVE, REFUTED, OPEN, RETRACTED or 'as sealed' word, or 'Scoped').  A planted
control row shows the check can fail."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
REG = ROOT / "docs" / "THEOREM_REGISTRY.md"
SCOPE = re.compile(r"NEGATIVE|REFUTED|OPEN|RETRACTED|as sealed|[Ss]coped|UNPROVED|CONDITIONAL")


def _verdicts():
    out = {}
    for f in (ROOT / "frontier").glob("B*/arc_verdict.json"):
        try: d = json.loads(f.read_text(encoding="utf-8"))
        except Exception: continue
        if isinstance(d, dict) and "id" in d: out[d["id"]] = d.get("verdict")
    return out


def offenders(lines, verdicts):
    bad = []
    for l in lines:
        if not l.startswith("| T-"): continue
        cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
        if len(cells) < 4: continue
        status = cells[-1]
        m = re.search(r"\bB(\d{1,4})\b", cells[2])
        if not m: continue
        arc = "B" + m.group(1); v = verdicts.get(arc)
        if re.match(r"\**PROVED", status) and v in ("NEGATIVE", "OPEN", "RETRACTED") and not SCOPE.search(status):
            bad.append((cells[0], arc, v))
    return bad


def test_no_registry_row_reads_proved_against_its_own_arcs_negative_verdict():
    v = _verdicts()
    assert offenders(REG.read_text(encoding="utf-8").splitlines(), v) == []


def test_the_check_can_fail():
    v = {"B9999": "NEGATIVE", "B9998": "PROVED"}
    rows = ["| T-PLANTED | a refuted claim | B9999 | `tests/x.py` | PROVED |",
            "| T-SCOPED | an identity in a negative arc | B9999 | `tests/x.py` | NEGATIVE as sealed; the identity PROVED |",
            "| T-FINE | a proved claim | B9998 | `tests/x.py` | PROVED |"]
    assert offenders(rows, v) == [("T-PLANTED", "B9999", "NEGATIVE")]
