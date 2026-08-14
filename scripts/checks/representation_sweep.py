#!/usr/bin/env python3
"""L143 — the representation sweep.

B976 found eleven banked cascade arcs (B860-B873) cited ZERO times on any synthesis
surface — including B864, which DERIVES hypercharge, while a ledger row written five
days later called hypercharge "OPEN, the sharpest available target". The repo lost
nothing; the SUMMARIES forgot. Two gates already police the CONTENT of rows that exist
(`lawmap-scope`, `retraction-sweep`). Neither notices a row that was never written.

This does. For every SUBSTANTIAL banked arc, is its ID cited on any synthesis surface?

SUBSTANTIALITY = length of `claim_one_line`, not file size. Calibrated on the block that
was actually lost: file size would have caught 1 of 11 (B864's FINDINGS is only 3.7 KB —
short and dense); claim length >= 500 catches 11 of 11 while flagging ~99 arcs corpus-wide.
A seat writes a long claim line when there is a lot to say.

Unrepresented arcs are not automatically defects. They are triaged in
docs/REPRESENTATION_TRIAGE.md as PROCESS (correctly absent from an object atlas),
SURFACE (the arc IS a synthesis surface), or PENDING (owed a row — a real debt).
The gate requires every unrepresented substantial arc to carry a disposition.
"""
import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TRIAGE = os.path.join(ROOT, "docs", "REPRESENTATION_TRIAGE.md")
CLAIM_FLOOR = 500

SURFACES = [
    "docs/LAW_MAP.md", "docs/THE_SM_VERDICT.md", "docs/SM_SPECIFICATION_LEDGER.md",
    "docs/GUT_REQUIREMENTS_LEDGER.md", "docs/CAMPAIGN_STATUS.md", "docs/OPEN_LEADS.md",
    "docs/OPEN_PROBLEMS.md", "docs/HINT_LEDGER.md", "knowledge/INDEX.md",
]


def _surfaces_text():
    out = ""
    for rel in SURFACES:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="ignore") as fh:
                out += fh.read()
    return out


def _triaged():
    ids = set()
    if not os.path.exists(TRIAGE):
        return ids
    import re
    with open(TRIAGE, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\|\s*`?(B\d{1,4})`?\s*\|", line)
            if m:
                ids.add(m.group(1))
    return ids


def substantial_arcs():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json"))):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if d.get("instrument"):
            continue
        if d.get("verdict") not in ("PROVED", "NEGATIVE"):
            continue
        claim = d.get("claim_one_line", "") or ""
        if len(claim) >= CLAIM_FLOOR:
            out.append((d["id"], d["verdict"], len(claim)))
    return out


def sweep():
    """Substantial arcs cited on no surface AND not triaged."""
    surf = _surfaces_text()
    triaged = _triaged()
    return [(i, v, n) for i, v, n in substantial_arcs()
            if i not in surf and i not in triaged]


if __name__ == "__main__":
    subs = substantial_arcs()
    surf = _surfaces_text()
    uncited = [x for x in subs if x[0] not in surf]
    missing = sweep()
    print(f"substantial arcs (claim >= {CLAIM_FLOOR} chars): {len(subs)}")
    print(f"of those, cited on no synthesis surface:        {len(uncited)}")
    print(f"of those, NOT triaged (= the defect):           {len(missing)}")
    for i, v, n in missing:
        print(f"  {i:6s} [{v[:4]}] claim {n} chars")
