"""B1052 locks — the handoff's countable claims, held against the tree.

A handoff that drifts is worse than none, because a seat trusts it. These locks make the manual
FAIL rather than go quietly stale.
"""
import glob
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
HANDOFF = "docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md"


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _prose(s):
    """Blockquote markers stripped, then whitespace collapsed — see the arc for why."""
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1052_the_handoff/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 45


def test_the_handoff_exists_in_the_conventions_directory():
    assert (ROOT / HANDOFF).is_file()
    assert len(glob.glob(str(ROOT / "docs" / "handoffs" / "*.md"))) >= 3
    h = _read(HANDOFF)
    assert h.startswith("# HANDOFF —") and "*From:" in h and "To:" in h
    assert "B1024–B1051" in h


def test_the_arc_and_instrument_counts_match_the_tree():
    arcs = {}
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B10[2-5]*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        vp = os.path.join(d, "arc_verdict.json")
        if m and os.path.isfile(vp) and 1024 <= int(m.group(1)) <= 1051:
            arcs[int(m.group(1))] = json.loads(pathlib.Path(vp).read_text())
    assert len(arcs) == 28
    assert sorted(n for n, v in arcs.items() if v.get("instrument")) == [1025, 1044, 1046, 1049]
    h = _read(HANDOFF)
    assert "**28** — B1024 … B1051" in h and "**4 are instruments**" in h


def test_the_gate_count_matches():
    # REPAIRED BY REVIEW 1 (B1054). `== 28` is E38 -- an absolute count in a programme whose
    # consolidation work ADDS gates; R1-15's `atlas-generated` made it 29 and this inverted.
    # And it is the FOURTH time in this review that a repair fixed an instrument and left its
    # sibling lock: the standing rule "sweep the FILE" needed to be "sweep the ARC AND its lock",
    # which is now what `scripts/checks/instrument_freshness.py` plus the suite do together.
    # The handoff's claim is HISTORICAL -- this window took the gates 26 -> 28 -- and that does
    # not move; what must not happen is a REGRESSION.
    n = len(re.findall(r'^\s{4}"[a-z0-9-]+": gate_', _read("scripts/gates/gates.py"), re.M))
    assert n >= 28, n
    assert "**26 → 28**" in _read(HANDOFF)


def test_the_debt_figure_matches_the_tree():
    cur = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]
    blob = "\n".join(_read(p) for p in cur)
    debt, seen = 0, set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        vp = os.path.join(d, "arc_verdict.json")
        if not m or not os.path.isfile(vp):
            continue
        n = int(m.group(1))
        if n in seen:
            continue
        seen.add(n)
        v = json.loads(pathlib.Path(vp).read_text())
        if v.get("verdict") == "PROVED" and not v.get("instrument") \
           and not (re.search(rf"\bB{n}\b", blob) or re.search(rf"B{n}_", blob)):
            debt += 1
    assert debt == 175, debt
    assert "**245 → 175**" in _read(HANDOFF)


def test_the_L166_count_is_fourteen_not_twenty_four():
    def token(d):
        b = pathlib.Path(d, "FINDINGS.md").read_text(encoding="utf-8", errors="ignore")
        mm = re.search(r"^##\s*Verdict\s*$", b, re.M)
        if not mm:
            return None
        w = b[mm.end():mm.end() + 400]
        m2 = (re.search(r"```(?:text)?\s*\n([A-Z][A-Z0-9_\-]+)", w)
              or re.search(r"\*\*`([A-Z][A-Z0-9_\-]+)`\*\*", w))
        return m2.group(1) if m2 else None

    neg, pos, seen = [], [], set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        if not m or not pathlib.Path(d, "arc_verdict.json").is_file() \
           or not pathlib.Path(d, "FINDINGS.md").is_file():
            continue
        n = int(m.group(1))
        if n in seen:
            continue
        seen.add(n)
        if json.loads(pathlib.Path(d, "arc_verdict.json").read_text()).get("verdict") != "PROVED":
            continue
        t = token(d)
        if t is None or t == "PROVED":
            continue
        (neg if t in ("STALLED", "NEEDS_VALIDATION") else pos).append(n)
    assert len(neg) == 14 and len(pos) == 9
    assert all(n < 100 for n in neg)


def test_the_honesty_clauses_are_present():
    """The part a later seat cannot reconstruct from the arcs."""
    h = _read(HANDOFF)
    p = _prose(h)
    assert "## 2. EVERY CORRECTION THIS WINDOW MADE" in h
    assert len(re.findall(r"^\| \d+ \|", h, re.M)) >= 20
    assert "Read this section before you trust anything else" in p
    # the ONE published overstatement must be separated from the near-misses
    assert "The one that was published wrong" in h
    assert "B564 had CLOSED it" in p
    assert "only overstatement in this window that reached a curated surface" in p
    # limits of the author
    assert "What I would not claim" in h and "perhaps a third of the corpus" in p
    for tool in ("snappy", "sage", "cypari", "flint"):
        assert tool in h, tool
    assert "What is structurally fragile" in h


def test_the_manual_is_registered_as_campaign_step_seven():
    c = _read("docs/THE_CAMPAIGN.md")
    assert "## THE MANUAL — the refresh's seventh step" in c
    assert "A manual written once is a snapshot" in _prose(c)
    assert HANDOFF.split("/")[-1] in c
    assert "a window is not closed until its handoff exists" in _prose(c)
    # registered, NOT gated — and the reason is named
    assert "`E34` apparatus-inflation" in c
    assert not (ROOT / "scripts" / "checks" / "handoff_exists.py").exists()


def test_nothing_moved():
    h = _read(HANDOFF)
    assert "Nothing was promoted to `CLAIMS.md`" in h
    assert "Gate 5 was never touched" in h
    assert "nothing should be read as endorsing or contesting them" in _prose(h)
