"""R47-2 — the arc_verdict schema-validator lock (landed WITH the creates_law
field per the audit seat's sharpening: a declaration a gate reads beats a
standing rule nobody reads).

Every frontier/*/arc_verdict.json must:
  - parse as JSON with the five required fields;
  - carry a verdict from the closed enum;
  - carry instrument as a BOOLEAN (E45's species, locked);
  - carry creates_law as a BOOLEAN when present — and ALWAYS from B1103 on
    (legacy arcs may omit it; omission means false to the registry gate);
  - have an id matching its directory prefix.
"""
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
# The corpus's actual universal core (schema survey 2026-08-21: 906 of 995
# verdicts carry {authored_by, claim_one_line, depends_on, id, instrument,
# superseded_by, supersedes, verdict}; `title` exists only in a recent subset
# and is NOT required). E45's lesson, applied by survey not by one neighbor.
REQUIRED = {"id", "verdict", "claim_one_line", "instrument"}
VERDICTS = {"NEGATIVE", "OPEN", "PROVED", "RETRACTED"}
CREATES_LAW_REQUIRED_FROM = 1103
# B1231: identifications declared, same self-declaration pattern as creates_law. The programme's
# dominant error mode is gluing two structures whose labels match, in different places, without a
# map (B813; B1223's "direct is not semidirect"; and two of this bench's own in one session).
IDENTIFICATIONS_REQUIRED_FROM = 1231

FILES = sorted((ROOT / "frontier").glob("*/arc_verdict.json"))


def test_verdict_files_exist():
    assert len(FILES) > 900, "the corpus's verdict census went missing"


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.parent.name)
def test_schema(path):
    d = json.load(open(path, encoding="utf-8"))
    missing = REQUIRED - set(d)
    assert not missing, f"{path.parent.name}: missing {missing}"
    assert d["verdict"] in VERDICTS, f"{path.parent.name}: verdict {d['verdict']!r}"
    assert isinstance(d["instrument"], bool), (
        f"{path.parent.name}: instrument must be boolean (E45)")
    m = re.match(r"(B\d+)", path.parent.name)
    assert m and d["id"] == m.group(1), (
        f"{path.parent.name}: id {d['id']!r} does not match directory")
    num = int(d["id"][1:])
    if "creates_law" in d:
        assert isinstance(d["creates_law"], bool), (
            f"{path.parent.name}: creates_law must be boolean")
    if "identifications" in d:
        assert isinstance(d["identifications"], list), (
            f"{path.parent.name}: identifications must be a list")
        for it in d["identifications"]:
            assert isinstance(it, dict) and "row" in it, (
                f"{path.parent.name}: each identification needs a 'row' naming its "
                f"docs/IDENTIFICATION_LEDGER.md entry (I-n)")
    if num >= IDENTIFICATIONS_REQUIRED_FROM:
        assert "identifications" in d, (
            f"{path.parent.name}: arcs from B{IDENTIFICATIONS_REQUIRED_FROM} on must declare "
            f"identifications (use [] if the arc makes none)")
    if num >= CREATES_LAW_REQUIRED_FROM:
        assert "creates_law" in d, (
            f"{path.parent.name}: creates_law is REQUIRED from "
            f"B{CREATES_LAW_REQUIRED_FROM} on (declare it, the gate reads it)")
