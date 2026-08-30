#!/usr/bin/env python3
"""REVERSE SWEEP (campaign Cell 0) -- arcs -> surfaces, the direction open_claim_sweep cannot see.

`open_claim_sweep.py` runs surfaces -> arcs: it takes a CLAIM OF OPENNESS and asks whether a
settled arc already decided it. That direction structurally CANNOT find a banked result that no
surface mentions at all -- there is no claim to match against. B1188 measured that population;
B985 measured the bias producing it (object-faces recover 79-100%, relation-faces 6-19%).

This asks the other question, of every settled arc: DOES ANY LIVE SURFACE CARRY THIS RESULT?

Two signals, because either alone is wrong:
  (1) citation -- is the arc id written on a live surface? (exact, but prose can carry a result
                  without naming the arc)
  (2) content  -- do the claim's distinctive (high-IDF) terms co-occur on some surface?
An arc counts as OFF-SURFACE only if BOTH fail.

    python3 scripts/checks/reverse_sweep.py            # the sweep
    python3 scripts/checks/reverse_sweep.py --selftest # planted bite controls
"""
import json
import math
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
SETTLED = {"PROVED", "NEGATIVE", "RESOLVED", "RESOLVED-A", "THEOREM"}

SURFACES = ["docs/THE_ROAD.md", "docs/OPEN_LEADS.md", "docs/THE_CLAIM.md",
    "docs/THE_SM_VERDICT.md", "docs/THE_FRAMEWORK.md", "docs/MASTERPLAN.md",
    "docs/PRICED_DOORS.md", "docs/LEAD_REGISTER.md", "docs/OPEN_PROBLEMS.md",
    "docs/FALSIFIER_REGISTER.md", "docs/CROSSING_REQUIREMENTS.md", "docs/LAW_MAP.md",
    "docs/GRAND_COMPUTATION_LEDGER.md", "docs/THEOREM_REGISTRY.md", "docs/THEOREM_LEDGER.md",
    "docs/CAMPAIGN_STATUS.md", "docs/THE_REMAINING_MATH.md",
    "README.md", "ROADMAP.md", "papers/P3_THE_PAPER/main.tex"]

# THE TAUTOLOGY RULE (B1218, re-earned here). VERDICT_LEDGER (1180 arcs), THE_SPINE (979) and
# CLOSED_DOORS (528) are GENERATED per-arc enumerations: every arc appears in them BY
# CONSTRUCTION. Counting that as "the result reached a surface" makes this measurement return
# ZERO -- which is exactly what the first run did, against B1188's known 132. Being in a database
# dump is not being on a surface; B1188's own phrase is "absent from all LIVE surfaces".
_GENERATED = ("VERDICT_LEDGER", "THE_SPINE", "CLOSED_DOORS")
SURFACES += [str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("docs/views/*.md"))
             if not any(g in p.name for g in _GENERATED)]

STOP = set("""the a an and or of to in on at by for with from is are was were be been being this
that these those it its as not no but if then than so such which who whom whose what when where
how why all any both each few more most other some only own same too very can will just should
now here there we our us you your they them their one two three four five six seven eight nine
ten first second third new old open closed free bit bits row rows claim claims case cases thing
things part parts side sides fact facts point points line lines name named names level levels
form forms type types kind kinds set sets map maps run runs does did done make made take taken
give given object observer paper program record corpus repo arc arcs seat seats bench doc docs
section sections page pages note notes item items list lists table tables see per via above below
within without between across over under also still yet even ever never exactly exact""".split())
TOKEN = re.compile(r"[a-z0-9_^+\-/]{3,}")
COVER_BAR = 0.55   # a judgement, not a derived constant -- see the arc's honest-scope note

# This instrument's own arc names every arc it reports, so without excluding it those arcs
# reclassify as SUPERSEDED ("a later arc owns the result") -- which is false: being named in the
# sweep's own findings is not being surfaced. Observed live: banking B1219 moved SURFACE-IT
# 29 -> 26. Same rule as already_banked.py's `exclude` and B1218's SELF: honesty, not evasion.
SELF = "B1219"


def toks(text):
    out = set()
    for w in TOKEN.findall(text.lower()):
        w = w.strip("-/^+_")
        if len(w) > 2 and w not in STOP and not w.isdigit():
            out.add(w)
    return out


def _surfaces():
    return {s: (ROOT / s).read_text(encoding="utf-8", errors="ignore")
            for s in SURFACES if (ROOT / s).exists()}


def main():
    arcs = {}
    for vp in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(vp.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        m = re.match(r"(B\d+[a-z]?)", vp.parent.name)
        if not m or m.group(1) == SELF:
            continue
        arcs[m.group(1)] = {"verdict": d.get("verdict", "?"),
                            "instrument": bool(d.get("instrument")),
                            "claim": d.get("claim_one_line") or ""}

    surf = _surfaces()
    blob = " ".join(surf.values())
    surfaced_ids = set(re.findall(r"\bB\d{2,4}[a-z]?\b", blob))   # one pass, not N regex scans
    st = {s: toks(t) for s, t in surf.items()}

    df = Counter()
    for a in arcs.values():
        df.update(toks(a["claim"]))
    n = max(len(arcs), 1)
    idf = {t: math.log(n / (1 + c)) for t, c in df.items()}

    cited_by_arc = set()
    for aid, a in arcs.items():
        for other in re.findall(r"B\d{3,4}", a["claim"]):
            if other != aid:
                cited_by_arc.add(other)

    rows = []
    for aid, a in arcs.items():
        if a["verdict"] not in SETTLED or aid in surfaced_ids:
            continue
        at = toks(a["claim"])
        if len(at) < 6:
            continue
        # tie-break on the term itself: without it the top-12 TRUNCATION depends on
        # set iteration order, which PYTHONHASHSEED randomizes per process -- two runs
        # of this file gave 45 and 46. A verifier that does not reproduce is worthless.
        top = sorted(at, key=lambda t: (-idf.get(t, 0), t))[:12]
        den = max(sum(idf.get(t, 0) for t in top), 1e-9)
        best = max(sum(idf.get(t, 0) for t in top if t in s) / den for s in st.values())
        if best >= COVER_BAR:
            continue
        cls = ("INTERNAL" if a["instrument"]
               else "SUPERSEDED" if aid in cited_by_arc else "SURFACE-IT")
        rows.append((den, aid, a["verdict"], cls, " ".join(a["claim"].split())[:130]))
    rows.sort(reverse=True)
    return rows, arcs


def selftest():
    """Bite control with PLANTED targets, so it cannot go stale.

    A control keyed to named arcs decays as those arcs get surfaced -- which is exactly what
    happened here: B1188's five sharpest off-surface arcs did NOT flag, because B1188's own
    remedy had since surfaced them into GRAND_COMPUTATION_LEDGER.md. The control was testing a
    condition the corpus had already repaired. Planted targets do not decay.
    """
    surf = _surfaces()
    st = {s: toks(t) for s, t in surf.items()}
    claims = {}
    for vp in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(vp.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        claims[vp.parent.name] = d.get("claim_one_line") or ""
    # PLANT A: object-facing vocabulary occurring on no surface -> MUST flag
    claims["_PLANT_A"] = ("The quadratic dispersal of the pentachoral wobble index is conserved "
        "under thistle rotation; the marmoset bracket vanishes identically on every kestrel "
        "stratum and the dispersal constant equals the reciprocal of the wobble genus.")
    # PLANT B: copied verbatim from a heavily-surfaced document -> must NOT flag
    claims["_PLANT_B"] = " ".join(
        (ROOT / "docs/THE_CLAIM.md").read_text(encoding="utf-8", errors="ignore").split()[:120])

    df = Counter()
    for c in claims.values():
        df.update(toks(c))
    n = len(claims)
    idf = {t: math.log(n / (1 + c)) for t, c in df.items()}

    def cover(key):
        top = sorted(toks(claims[key]), key=lambda t: (-idf.get(t, 0), t))[:12]
        den = max(sum(idf.get(t, 0) for t in top), 1e-9)
        return max(sum(idf.get(t, 0) for t in top if t in s) / den for s in st.values())

    a, b = cover("_PLANT_A"), cover("_PLANT_B")
    ok = a < COVER_BAR <= b
    print(f"PLANT A (off-surface, MUST flag) : cover={a:.2f}  flagged={a < COVER_BAR}")
    print(f"PLANT B (surfaced, must NOT flag): cover={b:.2f}  flagged={b < COVER_BAR}")
    print("CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    rows, arcs = main()
    tally = Counter(r[3] for r in rows)
    scanned = sum(1 for a in arcs.values() if a["verdict"] in SETTLED)
    print(f"settled arcs scanned : {scanned}")
    print(f"OFF-SURFACE total    : {len(rows)}   {dict(tally)}\n")
    for w, aid, v, cls, claim in rows:
        if cls == "SURFACE-IT":
            print(f"[{w:6.1f}] {v:8s} {aid:6s} {claim}")
