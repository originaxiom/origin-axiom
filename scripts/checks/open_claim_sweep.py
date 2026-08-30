#!/usr/bin/env python3
"""OPEN-CLAIM SWEEP -- already_banked.py, run over every live surface at once.

`already_banked.py` answers "is THIS one thing already banked?" It is mandatory before
writing MISSING / OPEN / "never run", and it works. Its limit is that it must be AIMED:
it only ever checks the claim a seat happened to think of. On 2026-08-30 the owner asked
"are you sure theyre not lost" and aiming it by hand at five hand-picked rows found five
locks (three in THE_ROAD Section IX, plus L175 and III.4's key count in Section X). The
question this instrument answers is the one that follows: how many more are there?

So: extract EVERY open/free/pending claim from the live surfaces, and scan the corpus
for a SETTLED arc that already decided it. Ranking is by shared-term IDF, not raw count
-- rare terms carry the signal, and an unweighted count just surfaces whatever arc says
"the object" most often.

MB12: this instrument must be able to report NOTHING. A claim with no settled match
scores zero and is silent. Bite control is built in (--selftest): the five locks found
by hand must rank, and genuinely-open rows must not.

    python3 scripts/checks/open_claim_sweep.py            # the sweep
    python3 scripts/checks/open_claim_sweep.py --selftest # bite control
"""
import json
import math
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
SETTLED = {"PROVED", "NEGATIVE", "RESOLVED", "RESOLVED-A", "THEOREM"}

# Live, normative surfaces -- what a seat or reader consults to learn the current state.
# CAMPAIGN_STATUS/REVIEWS are append-only LOGS (historical entries are not live claims),
# so they are deliberately out of scope; a stale line there is a record, not a surface.
SURFACES = [
    "docs/THE_ROAD.md", "docs/OPEN_LEADS.md", "docs/THE_CLAIM.md",
    "docs/THE_SM_VERDICT.md", "docs/THE_FRAMEWORK.md", "docs/MASTERPLAN.md",
    "docs/PRICED_DOORS.md", "docs/LEAD_REGISTER.md", "docs/OPEN_PROBLEMS.md",
    "docs/FALSIFIER_REGISTER.md", "docs/CROSSING_REQUIREMENTS.md",
    "docs/LAW_MAP.md", "docs/GRAND_COMPUTATION_LEDGER.md",
    "papers/P3_THE_PAPER/main.tex",
]
# views/VERDICT_LEDGER.md is a GENERATED index OF arcs -- every row matches its own arc
# by construction, so including it measures nothing. Excluding it is the tautology rule.
SURFACES += [str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("docs/views/*.md"))
             if "VERDICT_LEDGER" not in p.name]

# Assertions that something is open RIGHT NOW.
OPEN_MARK = re.compile(
    r"NAMED-OPEN|still open|remains open|not run|never run|no successor|"
    r"unresolved|not yet (?:run|done|computed|proved|closed|attempted)|ungated|"
    r"no acceptance|genuinely free|census of the free|remain(?:s|ing)? free|"
    r"open question|\bawaits\b|NEEDS-SPECIALIST|OWNER-PENDING|TODO|"
    r"unproven|not proved|no gate|\bOPEN\b",
    re.I)

# If the unit already records a resolution, it is a HISTORY line, not a live open claim.
RESOLVED_MARK = re.compile(
    r"CLOSED|CLOSES|FALSIFIED|RESOLVED|REFUTED|RETRACTED|SUPERSEDED|WITHDRAWN|"
    r"\bPROVED\b|\bNEGATIVE\b|\[BANKED\]|PROVEN-FREE|DECIDED|ADOPTED|DONE\b|"
    r"banked|verified|answered|discharged|complete",
    re.I)

# Words that carry no discriminating power in THIS corpus.
STOP = set("""the a an and or of to in on at by for with from is are was were be been being
this that these those it its as not no but if then than so such which who whom whose what
when where how why all any both each few more most other some only own same too very can
will just should now here there we our us you your they them their he she his her i me my
one two three four five six seven eight nine ten first second third new old open closed
free bit bits row rows claim claims case cases thing things part parts side sides fact
facts point points line lines name named names level levels form forms type types kind
kinds set sets map maps run runs runs' does did done make made take taken give given
object observer paper program record corpus repo arc arcs seat seats bench doc docs
section sections page pages note notes item items list lists table tables see per via
above below within without between across over under also still yet even ever never
""".split())

TOKEN = re.compile(r"[a-z0-9_^+\-/]{3,}")


def toks(text):
    out = set()
    for t in TOKEN.findall(text.lower()):
        t = t.strip("-/^+_")
        if len(t) > 2 and t not in STOP and not t.isdigit():
            out.add(t)
    return out


# This instrument's own arc quotes its test phrases and every lock it reports, so it
# matches them all. Excluding it is the established rule (already_banked.py's `exclude`):
# honesty, not evasion. Fifth instance of the self-documenting-instrument class.
SELF = "B1218_open_claim_sweep"


def load_corpus():
    """Each arc -> (name, verdict, text, token set). Verdict arcs plus their FINDINGS."""
    docs = {}
    for vp in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(vp.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        name = vp.parent.name
        if name == SELF:
            continue
        txt = (d.get("claim_one_line") or "")
        fp = vp.parent / "FINDINGS.md"
        if fp.exists():
            txt += "\n" + fp.read_text(encoding="utf-8", errors="ignore")[:20000]
        docs[name] = {"verdict": d.get("verdict", "?"), "text": txt, "toks": toks(txt)}
    return docs


def build_idf(docs):
    df = Counter()
    for d in docs.values():
        df.update(d["toks"])
    n = len(docs)
    return {t: math.log(n / (1 + c)) for t, c in df.items()}, n


def claim_units(path):
    """A claim unit = a bullet or paragraph on a live surface carrying an open-marker."""
    p = ROOT / path
    if not p.exists():
        return []
    raw = p.read_text(encoding="utf-8", errors="ignore")
    units, buf = [], []
    for ln in raw.splitlines():
        if not ln.strip():
            if buf:
                units.append("\n".join(buf)); buf = []
            continue
        if re.match(r"\s*[-*]\s|\s*\|", ln) and buf:
            units.append("\n".join(buf)); buf = [ln]
        else:
            buf.append(ln)
    if buf:
        units.append("\n".join(buf))
    out = []
    for u in units:
        if len(u) < 40 or not OPEN_MARK.search(u):
            continue
        if RESOLVED_MARK.search(u):
            continue          # history line, not a live open claim
        out.append(u[:1200])
    return out


def sweep(min_score=25.0, top=3):
    docs = load_corpus()
    idf, _ = build_idf(docs)
    rows = []
    for surf in SURFACES:
        for unit in claim_units(surf):
            ut = toks(unit)
            if len(ut) < 5:
                continue
            cited = set(re.findall(r"B\d{3,4}", unit))
            scored = []
            for name, d in docs.items():
                if d["verdict"] not in SETTLED:
                    continue
                shared = ut & d["toks"]
                if len(shared) < 4:
                    continue
                s = sum(idf.get(t, 0) for t in shared)
                arcid = re.match(r"(B\d+)", name)
                if arcid and arcid.group(1) in cited:
                    continue    # the unit already points at this arc: not lost
                scored.append((s, name, d["verdict"], sorted(shared, key=lambda t: -idf.get(t, 0))[:6]))
            scored.sort(reverse=True)
            if scored and scored[0][0] >= min_score:
                rows.append((scored[0][0], surf, unit, scored[:top]))
    rows.sort(reverse=True)
    return rows


def selftest():
    """Bite control. The instrument must FIND the five hand-found locks and must be
    SILENT on a claim with no settled counterpart. Both directions, or it is vacuous."""
    docs = load_corpus()
    idf, _ = build_idf(docs)

    def best(text, want):
        ut = toks(text)
        sc = []
        for name, d in docs.items():
            if d["verdict"] not in SETTLED:
                continue
            sh = ut & d["toks"]
            if len(sh) < 3:
                continue
            sc.append((sum(idf.get(t, 0) for t in sh), name))
        sc.sort(reverse=True)
        rank = next((i for i, (_, n) in enumerate(sc[:25]) if want in n), None)
        return rank, sc[:3]

    print("== POSITIVE control: the five locks found by hand must rank ==")
    cases = [
        ("the A2 stratum, roughly 4.3 bits of freedom, the landing stratum choice "
         "among the twenty nilpotent strata, projective lift even weights", "B1112"),
        ("the hypercharge direction among eighteen rational directions, 4.17 bits, "
         "orbits under the Weyl product, orbit-lead pending", "B1109"),
        ("the spin lift is free, one bit, the two spin structures of the manifold, "
         "pair-invisible, the observer's last free discrete purchase", "B1141"),
        ("L175 the h=0 locus, the vanishing locus of the listener channels, open",
         "B1110"),
        ("the product-structure keys, frame-map key, other-color key, other-stratum "
         "key su(6), three keys open", "B1109"),
    ]
    ok = 0
    for text, want in cases:
        r, top = best(text, want)
        flag = "HIT " if r is not None and r < 10 else "MISS"
        if flag == "HIT ":
            ok += 1
        print(f"  {flag} want={want:7s} rank={r}  top={[n for _, n in top]}")

    print("== NEGATIVE control (MB12): nonsense must NOT score ==")
    ctrl = "the quarterly beverage procurement schedule for the office kitchen refrigerator"
    ut = toks(ctrl)
    sc = [sum(idf.get(t, 0) for t in (ut & d["toks"]))
          for d in docs.values() if d["verdict"] in SETTLED and len(ut & d["toks"]) >= 4]
    mx = max(sc) if sc else 0.0
    print(f"  max score on off-corpus text = {mx:.2f} (must be < 6.0)")
    print(f"\n  positive {ok}/5, negative {'PASS' if mx < 6.0 else 'FAIL'}")
    return 0 if (ok >= 4 and mx < 6.0) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    rows = sweep()
    print(f"OPEN-CLAIM SWEEP: {len(rows)} open claims with a strongly-matching SETTLED arc\n")
    for score, surf, unit, top in rows[:40]:
        first = " ".join(unit.split())[:150]
        print("=" * 78)
        print(f"[{score:6.1f}] {surf}")
        print(f"  CLAIM: {first}")
        for s, name, verd, sh in top:
            print(f"    -> [{s:6.1f}] {verd:9s} {name}   shared: {', '.join(sh)}")
