"""B1053 locks — the audit gap, and the invisibility finding it turned up."""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
WALL = ("B19", "B21", "B28", "B30", "B34", "B35")
HUNT_ARCS = ("B742", "B745", "B754", "B765", "B770")


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _prose(s):
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def _vd(bid):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))[0]).read_text())


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1053_the_unread_handoffs/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 30


def test_the_six_wall_arcs_were_invisible_to_the_negatives_hunt():
    """The load-bearing finding: metadata removed 14 arcs from an audit's population."""
    for b in WALL:
        assert _vd(b)["verdict"] == "PROVED", b
        body = pathlib.Path(glob.glob(
            str(ROOT / "frontier" / f"{b}_*" / "FINDINGS.md"))[0]).read_text()
        assert "**`STALLED`**" in body, b
    atlas = json.loads(_read("scripts/atlas/atlas_data.json"))["probes"]
    for b in WALL:
        assert atlas.get(b, {}).get("status") != "dead", b
    hunt = ""
    for b in HUNT_ARCS:
        for f in glob.glob(str(ROOT / "frontier" / f"{b}_*" / "*.md")):
            hunt += pathlib.Path(f).read_text(encoding="utf-8", errors="ignore")
    assert [b for b in WALL if re.search(rf"\b{b}\b", hunt)] == []


def test_the_hunt_actually_ran():
    """Stated because the opposite conclusion was available and would have been wrong."""
    for b in HUNT_ARCS:
        assert glob.glob(str(ROOT / "frontier" / f"{b}_*")), b
    assert "213 banked negatives" in _prose(
        _read("frontier/B742_negatives_hunt_p1/FINDINGS.md"))
    assert "P1–P3" in _read("frontier/B770_closure_census/CENSUS.md")


def test_the_finding_is_registered_where_it_belongs():
    assert "invisible to a repo-wide owner-directed audit" in _prose(_read("docs/OPEN_LEADS.md"))
    row = [ln for ln in _read("docs/LAW_MAP.md").splitlines()
           if ln.startswith("| **") and "THE PROJECTIVE QUOTIENT IS FULLY NATURAL" in ln[:200]]
    assert len(row) == 1
    assert "negatives hunt" in row[0].lower() and "P4" in row[0]
    hf = _prose(_read("docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md"))
    assert "I had not read either of the two handoffs" in hf
    assert "the owner asked" in hf.lower()


def test_the_P4_token_is_overloaded_which_is_why_the_claim_is_not_a_regex():
    """E1 vocabulary drift, inside the arc that reports it."""
    for f in ("docs/handoffs/NEGATIVES_HUNT_HANDOFF_2026-07-21.md",
              "frontier/B401_sixth_angle/FINDINGS.md",
              "frontier/B570_allowed_plays/RESULTS.md",
              "frontier/B737_candidate_zero/FINDINGS.md"):
        assert re.search(r"\bA?P4\b", _read(f)), f
    claims = ""
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*" / "arc_verdict.json"))):
        if "B1053" in d:
            continue
        claims += json.loads(pathlib.Path(d).read_text()).get("claim_one_line", "") + "\n"
    assert not re.search(r"early era|pre-?B300", claims, re.I)


def test_nothing_moved():
    fnd = _read("frontier/B1053_the_unread_handoffs/FINDINGS.md")
    assert "It does not claim the wall is wrong" in fnd
    assert "nothing to\n`CLAIMS.md`" in fnd or "nothing to `CLAIMS.md`" in _prose(fnd)
