"""B1034 locks — L154 adjudicated (sealed 6361f222)."""
import importlib.util
import json
import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1034_l154_sigma"


def _cells():
    spec = importlib.util.spec_from_file_location("b1034_cells", ARC / "b1034_cells.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_both_sides_exact():
    m = _cells()
    assert all(m.v1_both_sides().values())
    # re-derive the Sugawara arithmetic independently:
    assert sp.Rational(78, 13) == 6
    assert sp.Rational(16, 5) + sp.Rational(14, 5) == 6


def test_v2_no_exhibit_adjudicated():
    m = _cells()
    r = m.v2_map_hunt()
    own = "frontier/B1034_l154_sigma/PREREGISTRATION.md"
    # the only hits outside the arc's own prereg are the three registration surfaces
    allowed = {"CHANGELOG.md", "docs/CROSSING_REQUIREMENTS.md",
               "docs/views/VERDICT_LEDGER.md", "docs/views/REVIEWER.md",
               "docs/views/COVERAGE.md", own,
               # post-bank surfaces that quote this arc's own verdict are self-echoes:
               "PROGRESS_LOG.md", "docs/CAMPAIGN_STATUS.md", "docs/TERMINOLOGY.md",
               "TERMINOLOGY.md", "frontier/B1034_l154_sigma/FINDINGS.md",
               "docs/OPEN_LEADS.md",  # the lead's own disposition note (B1034 self-echo)
               # The structure paper's TERMINOLOGY POLICY is the document that FORBIDS
               # the bare symbol `c`; its TIER-3 row necessarily lists all four
               # referents, including c((E6)_1) and c_BH. Naming a collision in order
               # to ban it is the opposite of a drive-by mention -- the same
               # self-reference the terminology checker itself has to exempt.
               "papers/structure_paper/TERMINOLOGY_POLICY.md",
               # the SEALED SUCCESSOR CELL (2026-08-13): B1064 is the L154
               # re-pose itself — the one arc entitled to discuss the pairing;
               # the lock still bars drive-by mentions everywhere else:
               "frontier/B1064_cusp_torus_repose/PREREGISTRATION.md",
               "frontier/B1064_cusp_torus_repose/FINDINGS.md",
               "docs/SEAL_LEDGER.md"}
    for key, files in r.items():
        assert set(files) <= allowed, (key, files)


def test_v3_no_clash():
    m = _cells()
    assert all(m.v3_clash().values())


def test_findings_and_terminology():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "NO-EXHIBIT" in flat and "NO-CLASH" in flat and "UNDECIDED" in flat
    assert "c = 6 is NOT derived" in flat or "NOT derived" in flat
    assert "unobstructed" in flat.lower()
    assert "one banked bridge statement" in flat
    assert "pins" in flat  # the quantization adjudication
    t = " ".join((ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
                 .replace("**", "").split())
    assert '"σ" names THREE quantities' in t or "names THREE quantities" in t


def test_verdict_and_seal():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1034" and v["verdict"] == "PROVED"
    assert "UNDECIDED" in v["claim_one_line"]
    assert "B1012" in v["depends_on"] and "B945" in v["depends_on"]
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1034_l154_sigma/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("6361f222")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1)
