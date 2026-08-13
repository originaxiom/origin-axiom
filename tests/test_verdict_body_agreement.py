"""The verdict-convention gate (the owner's desk decision 1, 2026-08-13).

The cloud window's finding 2: thirty-one arcs carried verdict PROVED while
bodies carried STALLED/NEEDS_VALIDATION/retraction language — a routing
failure between two metadata fields. The forward rule: the five-word verdict
vocabulary stays; NEW arcs (B1060+) whose FINDINGS carry an explicit
divergent status word must not silently disagree with their arc_verdict.json.
History is never flipped (the lane-0 era rule); this gate is forward-only.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIVERGENT = re.compile(r'^#+\s*Verdict\b.*?(STALLED|NEEDS[_ ]VALIDATION)', re.I | re.M)


def test_new_arcs_bodies_agree_with_their_verdict_field():
    bad = []
    for d in sorted(ROOT.glob("frontier/B1*")):
        m = re.match(r"B(\d+)", d.name)
        if not m or int(m.group(1)) < 1060:
            continue
        f, v = d / "FINDINGS.md", d / "arc_verdict.json"
        if not (f.exists() and v.exists()):
            continue
        body = f.read_text(encoding="utf-8", errors="ignore")
        verdict = json.loads(v.read_text(encoding="utf-8")).get("verdict")
        hit = DIVERGENT.search(body)
        if hit and verdict == "PROVED":
            bad.append((d.name, hit.group(1), verdict))
    assert not bad, f"body/verdict routing failure (the cloud finding-2 species): {bad}"


def test_the_gate_is_not_vacuous():
    """MB12: at least one B1060+ arc with both files must exist to scan."""
    n = sum(1 for d in ROOT.glob("frontier/B106*")
            if (d / "FINDINGS.md").exists() and (d / "arc_verdict.json").exists())
    assert n >= 3, "the gate scanned almost nothing"
