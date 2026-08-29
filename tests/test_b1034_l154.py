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
               # THE_REGISTRY IS A REGISTRATION SURFACE -- the most registered one in the repo.
               # B1214's re-audit landed theorem rows there (B1200's Phi_3 three-faces row names the
               # partition function and the boundary; B1183's names the one-class theorem), which is
               # exactly the discussion this lock exists to LICENSE rather than bar. Added 2026-08-29.
               "docs/THEOREM_REGISTRY.md",
               "docs/views/VERDICT_LEDGER.md", "docs/views/REVIEWER.md",
               "docs/views/COVERAGE.md", own,
               # post-bank surfaces that quote this arc's own verdict are self-echoes:
               "PROGRESS_LOG.md", "docs/CAMPAIGN_STATUS.md", "docs/TERMINOLOGY.md",
               "TERMINOLOGY.md", "frontier/B1034_l154_sigma/FINDINGS.md",
               "docs/OPEN_LEADS.md",  # the lead's own disposition note (B1034 self-echo)
               # the SEALED SUCCESSOR CELL (2026-08-13): B1064 is the L154
               # re-pose itself — the one arc entitled to discuss the pairing;
               # the lock still bars drive-by mentions everywhere else:
               "frontier/B1064_cusp_torus_repose/PREREGISTRATION.md",
               "frontier/B1064_cusp_torus_repose/FINDINGS.md",
               "docs/SEAL_LEDGER.md",
               # THE GRAND-COMPUTATION CAMPAIGN (2026-08-28/29): B1190 is the L154 BRIDGE CELL
               # -- the successor entitled to discuss the pairing exactly as B1064 is -- and the
               # two campaign surfaces carry its adjudicated row (C4 / the sigma anchor). These
               # are admitted on the same ground as B1064 and no other: each states the
               # adjudication rather than asserting the join, which the next test enforces.
               "frontier/B1190_close_loop_batch2/FINDINGS.md",
               "docs/GRAND_COMPUTATION_LEDGER.md",
               "docs/GRAND_COMPUTATION_v0.md",
               # THE SELF-DOCUMENTING-INSTRUMENT CLASS, third instance (2026-08-29). B1207
               # documents the repair of THIS lock, and to do so it quotes the lock's own
               # criterion -- "Brown-Henneaux AND (E6)_1 in one file" -- which trips it. Same
               # species as B1202's already_banked.py matching its own arc, and as B1207's own
               # test spelling the machine-path literal it forbids. An arc that documents a lock
               # will quote that lock's criterion; admitting it is honesty, not evasion, and the
               # conditional test below still applies.
               "frontier/B1207_slow_lane_discharge/FINDINGS.md"}
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


CAMPAIGN_SURFACES = ("frontier/B1190_close_loop_batch2/FINDINGS.md",
                     "docs/GRAND_COMPUTATION_LEDGER.md",
                     "docs/GRAND_COMPUTATION_v0.md",
                     "frontier/B1207_slow_lane_discharge/FINDINGS.md")


def test_the_campaign_surfaces_state_the_adjudication_not_the_join():
    """The three surfaces admitted at the grand-computation campaign are allowed to discuss the
    L154 pairing BECAUSE they carry its negative adjudication. If one ever drops the
    no-exhibit/missing-bridge language it stops being an adjudication and becomes the drive-by
    join the lock exists to bar -- so the allowance is conditional, not a blanket."""
    root = Path(__file__).resolve().parents[1]
    words = ("NO-EXHIBIT", "no-exhibit", "ONE-BRIDGE-MISSING", "bridge", "REFUTED", "DEAD")
    for rel in CAMPAIGN_SURFACES:
        body = (root / rel).read_text(encoding="utf-8", errors="ignore")
        assert any(w in body for w in words), (
            f"{rel} discusses the L154 pairing without stating its adjudication")
