"""B1038 -- plan Arc 3: the retrieval-and-typing arc (verification mode; no outcome-prior
-- the content is the verification of the audit seat's at-risk census + the instruments).

V1: the census counts re-run on main (the corrected units: lines, not occurrences).
V2: the gauge-aware floor with the synonym set (their 19 = a floor; re-counted).
V3: the pi/6 TERMINOLOGY row + the point-of-use practice + the Jarlskog refresh note
    (installed as docs this batch; asserted here)."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def claim_lines():
    out = []
    for p in (ROOT / "frontier").glob("*/arc_verdict.json"):
        import json
        try:
            c = json.loads(p.read_text("utf-8")).get("claim_one_line", "")
        except Exception:
            continue
        out.append((p.parent.name, c))
    return out


def v1_census():
    cl = claim_lines()
    dec = re.compile(r"\d\.\d{3,}")
    inv_kw = re.compile(r"invarian|basis-invariant|gauge|convention|support", re.I)
    with_dec = [(a, c) for a, c in cl if dec.search(c)]
    with_inv = [(a, c) for a, c in with_dec if inv_kw.search(c)]
    without = [(a, c) for a, c in with_dec if not inv_kw.search(c)]
    return {
        "total claim lines": len(cl),
        "lines banking a 3+dp decimal": len(with_dec),
        "of those mentioning invariance-family keywords": len(with_inv),
        "without (the at-risk set)": len(without),
        "internally consistent": len(with_inv) + len(without) == len(with_dec),
        "at_risk_sample": sorted(a for a, _ in without)[:12],
    }


def v2_gauge_aware_floor():
    kw1 = re.compile(r"gauge|basis-invariant", re.I)
    kw2 = re.compile(r"frame-symmetric|frame-breaking|representative freedom|"
                     r"normalisation-dependent|sampling-dependent|pipeline gauge", re.I)
    s1, s2 = set(), set()
    for p in (ROOT / "frontier").glob("*/FINDINGS.md"):
        t = p.read_text("utf-8", errors="ignore")
        if kw1.search(t):
            s1.add(p.parent.name)
        if kw2.search(t):
            s2.add(p.parent.name)
    # NOTE (criterion difference, stated): this counts arcs MENTIONING the vocabulary
    # (a looser criterion than the audit seat's "arcs RUNNING a gauge check" = 12+7);
    # the check here verifies the PRINCIPLE (a single-vocabulary query undercounts).
    return {"gauge-vocab-mention arcs": len(s1), "frame-vocab-mention arcs": len(s2),
            "union (mentions)": len(s1 | s2),
            "single-vocabulary undercounts (the synonym-set principle)":
                len(s1 | s2) > min(len(s1), len(s2))}


def v3_docs_installed():
    term = " ".join((ROOT / "TERMINOLOGY.md").read_text("utf-8").replace("*", "").split())
    prac = " ".join((ROOT / "docs" / "PRACTICES.md").read_text("utf-8")
                    .replace("*", "").split())
    return {
        "pi/6 two-referent row installed": "π/6" in term and "two referents" in term.lower()
            or "names TWO objects" in term,
        "point-of-use practice registered": "point-of-use" in prac.lower(),
        "Jarlskog refresh note present":
            "Jarlskog" in (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text("utf-8"),
    }


if __name__ == "__main__":
    print("[V1] the census, re-run on main:")
    r1 = v1_census()
    for k, v in r1.items():
        print(f"   {k}: {v}")
    print("\n[V2] the gauge-aware floor (synonym set):")
    for k, v in v2_gauge_aware_floor().items():
        print(f"   {k}: {v}")
    print("\n[V3] the docs:")
    for k, v in v3_docs_installed().items():
        print(f"   {k}: {v}")
