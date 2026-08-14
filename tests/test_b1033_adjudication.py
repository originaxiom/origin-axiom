"""B1033 locks — the generation adjudication (sealed 73eedc0b)."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1033_generation_adjudication"


def _cells():
    spec = importlib.util.spec_from_file_location("b1033_cells", ARC / "b1033_cells.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_chiral():
    m = _cells()
    table, verdicts, outcome, anomaly = m.v1_content_table()
    assert outcome == "CHIRAL"
    assert verdicts["A(lv2)"] == "distinct-copies"
    # the singlet anomaly resolved: arm02-charged, color(arm45)-neutral
    assert anomaly["arm45"] == (0, 0) and anomaly["arm02"] != (0, 0)


def test_v2_distinct_and_b299_reproduced():
    m = _cells()
    r = m.v2_orbit_identity()
    matches = [v for v in r.values() if isinstance(v, dict)]
    assert matches, "at least one valid transport required"
    # B299 reproduced: every valid transport is free with nine 3-orbits
    assert all(v["orbit_sizes"] == {3: 9} for v in matches)
    # and NONE matches the 9-channel (the declared prior was wrong; the record holds it)
    assert not any(v["matches_9channel"] for v in matches)


def test_findings_and_propagation():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "CHIRAL" in flat and "DISTINCT" in flat
    assert "prior WRONG" in flat or "prior wrong" in flat.lower()
    assert "B280" in flat and "B298" in flat and "STAND" in flat
    assert "dead" in flat.lower()
    # the constructive residue is stated (not a pure negative):
    assert "trinification structure" in flat and "chiral anatomy" in flat
    # THE_CLAIM re-scoped same batch:
    claim = " ".join((ROOT / "docs" / "THE_CLAIM.md").read_text(encoding="utf-8")
                     .replace("**", "").split())
    assert "chiral (trinification) anatomy" in claim and "B1033" in claim
    assert "not generation structure" in claim


def test_verdict_and_seal():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1033" and v["verdict"] == "PROVED"
    assert "ORTHOGONAL" in v["claim_one_line"]
    for dep in ("B298", "B280", "B299", "B897"):
        assert dep in v["depends_on"]
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1033_generation_adjudication/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("73eedc0b")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1)
