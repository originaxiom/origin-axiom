#!/usr/bin/env python3
"""CLOSURE-CLAIM SWEEP -- the mirror of B1218's open-claim sweep.

Seal: outside_bench/seals/MIRROR_CLASS_PREREG.md.

B1218 (scripts/checks/open_claim_sweep.py) hunts E53: a SETTLED result asserted as OPEN.
This hunts the MIRROR, named in memo 163 and unhunted by any of the three existing instruments:

    an OPEN route asserted as SETTLED -- a permanence claim standing over live work.

METHOD: deliberately B1218's, with the poles reversed. Same claim units, same IDF ranking.
Where B1218 extracts openness assertions and looks for a SETTLED arc that decided them, this
extracts PERMANENCE assertions and looks for an OPEN arc that bears on them.

THE DISCRIMINATOR, v2 -- v1 WAS WRONG AND THE BINDING CONTROL CAUGHT IT. v1 filtered the arc pool
by the VERDICT FIELD (open = "not settled"). The control fired on neither side, and the diagnosis is
structural: the arcs bearing on the live instance are B990 (24.1) and B962 (29.6) and BOTH ARE
"PROVED". B990 is PROVED *and* titled "X10 SHARPENED, NOT CLOSED", names "exactly two routes", and
says "THE RUNG STAYS OPEN". A verdict field does not encode whether a ROUTE is live; the arc's TEXT
does. This is the same failure B1213 found in the paper's claim base -- reading a METADATA FIELD
where the CONTENT carries the signal.

v2: the pool is arcs whose CLAIM TEXT carries a live-route marker, whatever their verdict. A CORRECT
permanence claim matches arcs that close their subject; a DRIFTED one matches an arc that explicitly
leaves a route open.

FENCE: a flag is a prompt to READ, never a verdict. Gate 5 untouched: text only.
"""
import os, re, sys, json, glob, math, argparse, subprocess
from pathlib import Path

ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
SETTLED = {"PROVED", "NEGATIVE", "RESOLVED", "RESOLVED-A", "THEOREM", "RETRACTED"}

# B1218's surfaces, PLUS this lane -- memo 154/163: none of the three instruments reads it.
SURFACES = ["docs/THE_ROAD.md", "docs/OPEN_LEADS.md", "docs/THE_CLAIM.md",
            "docs/THE_SM_VERDICT.md", "docs/THE_FRAMEWORK.md", "docs/MASTERPLAN.md",
            "docs/PRICED_DOORS.md", "docs/LEAD_REGISTER.md", "docs/OPEN_PROBLEMS.md",
            "docs/FALSIFIER_REGISTER.md", "docs/LAW_MAP.md",
            "papers/P3_THE_PAPER/main.tex"]
SURFACES += [str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("outside_bench/*.md"))]

# PERMANENCE assertions -- the mirror of B1218's OPEN_MARK. Tight on purpose: "cannot" alone
# fires on every mathematical no-go in the corpus, which would be noise, not signal.
CLOSED_MARK = re.compile(
    r"will not reduce|will not close|cannot be reduced|no further reduction|"
    r"terminal state|is terminal|not a deficiency|irreducible|permanent(?:ly)?|"
    r"will not (?:move|change|shrink|improve)|stays supplied|remains supplied|"
    r"no route (?:exists|remains)|there is no route|nothing further|"
    r"cannot be derived|not derivable|never reduce|for good|final state|"
    r"the wall|closed for good|settled once",
    re.I)

# The mirror of B1218's RESOLVED_MARK: a unit that HEDGES is not an unqualified permanence claim.
HEDGE_MARK = re.compile(
    r"\bunless\b|\bunless and until\b|conditional|if and only if|one route|two routes|"
    r"\bopen\b|not yet|remains to|would (?:close|reduce|cross)|pending|awaits|"
    r"SUPERSEDED|~~|\bmay\b|\bmight\b|\bcould\b|hypothes",
    re.I)

# An arc leaves a ROUTE open when its own text says so -- regardless of its verdict field.
# B990 is PROVED and says all four of these.
LIVE_ROUTE = re.compile(
    r"SHARPENED, NOT CLOSED|not closed|stays open|remains open|rung stays open|"
    r"routes exist|two routes|next computation|what closes it|still open|"
    r"owed residual|remains the literature residual|NEEDS-SPECIALIST|"
    r"could be wrong|unfavourable prior|the one place|live opening|UNWORKED",
    re.I)

STOP = set("""the a an and or of to in on at by for with from is are was were be been being this
that these those it its as not no but if then than so such which who whom whose what when where how
why all any both each few more most other some only own same too very can will just should now here
there we our us you your they them their he she his her i me my one two three four five six seven
eight nine ten first second third new old open closed free bit bits row rows claim claims case cases
thing things part parts side sides fact facts point points line lines name named names level levels
form forms type types kind kinds set sets map maps run runs does did done make made take taken give
given object observer paper program record corpus repo arc arcs seat seats bench doc docs section
sections page pages note notes item items list lists table tables see per via above below within
without between across over under also still yet even ever never""".split())
TOKEN = re.compile(r"[a-z0-9_^+\-/]{3,}")
def toks(t): return {w for w in TOKEN.findall(t.lower()) if w not in STOP}

def is_live_near(d, shared, window=220):
    """CLAUSE-SCOPED, per B1210's own remedy. v3 asked whether a live-route phrase appears
    ANYWHERE in the arc's claim, and the control exposed that as structural noise: B991 -- the
    normalisation no-go, a CORRECT permanence claim -- contains "STAYS OPEN" about a different
    sub-question, and B1220 contains "Two routes". B1210 recorded this exact failure ("an arc
    claim is one long sentence about many things") and fixed it by scoping the verb to within
    90 characters of the reference. Same fix here: the live-route phrase must sit NEAR a term
    the claim and the arc actually share."""
    if d["verdict"] not in SETTLED:
        return True                       # an unsettled verdict is live regardless of prose
    txt = d["text"]; low = txt.lower()
    spans = [m.span() for t in shared for m in re.finditer(re.escape(t), low)]
    if not spans: return False
    for lm in LIVE_ROUTE.finditer(txt):
        a, b = lm.span()
        if any(a - window <= e and s0 <= b + window for s0, e in spans):
            return True
    return False


def load_corpus():
    docs = {}
    for p in ROOT.glob("frontier/*/arc_verdict.json"):
        try: v = json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if not isinstance(v.get("id"), str): continue
        docs[v["id"]] = {"verdict": v.get("verdict"), "dir": p.parent.name,
                         "text": v.get("claim_one_line") or "",
                         "toks": toks(v.get("claim_one_line") or "")}
    return docs

def build_idf(docs):
    N = len(docs); df = {}
    for d in docs.values():
        for t in d["toks"]: df[t] = df.get(t, 0) + 1
    return {t: math.log(N / c) for t, c in df.items() if c}

def claim_units(path):
    p = ROOT / path
    if not p.exists(): return []
    units, buf = [], []
    for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not ln.strip():
            if buf: units.append("\n".join(buf)); buf = []
            continue
        if re.match(r"\s*[-*]\s|\s*\|", ln) and buf:
            units.append("\n".join(buf)); buf = [ln]
        else: buf.append(ln)
    if buf: units.append("\n".join(buf))
    out = []
    for u in units:
        if len(u) < 40 or not CLOSED_MARK.search(u): continue
        if HEDGE_MARK.search(u): continue     # hedged = not an unqualified permanence claim
        out.append(u[:1200])
    return out

def sweep(min_score, top, surfaces):
    docs = load_corpus(); idf = build_idf(docs)
    openarcs = {k: d for k, d in docs.items()
                if d["verdict"] not in SETTLED or LIVE_ROUTE.search(d["text"])}
    print(f"corpus: {len(docs)} arcs, {len(openarcs)} carrying a LIVE-ROUTE signal "
          f"(verdict OR text) -- the pool this hunts")
    hits = []
    for surf in surfaces:
        for u in claim_units(surf):
            ut = toks(u)
            # B1218's OWN FILTERS, which v2 omitted and the first sweep's noise exposed.
            # B1219 recorded this exact slip -- "B1218's tautology rule, applied once and not
            # carried over" -- and I repeated it. Carried now, by rule not by whitelist.
            cited = set(re.findall(r"\bB\d{3,4}\b", u))
            if len(cited) >= 2:
                continue                      # TAUTOLOGY: an enumeration OF arcs, not a claim
            # THE DISCRIMINATOR, v3 -- v2 still flagged CORRECT permanence claims, because it
            # reported the top match without asking whether that match CLOSES the subject or
            # LEAVES IT OPEN. The paper's normalisation no-go tops out on B991, the arc that
            # PROVES it; its lambda note tops out on B1220, the arc that PLACED it. Those are
            # correct claims and must not flag. The mirror class is present only when the
            # strongest arc bearing on a permanence claim is a LIVE ROUTE, not a closure.
            live, closed = [], []
            for name, d in docs.items():
                if name in cited: continue    # SELF-CITATION: already pointing at it, not lost
                sh = ut & d["toks"]
                if not sh: continue
                sc = sum(idf.get(t, 0) for t in sh)
                tgt = live if is_live_near(d, sh) else closed
                tgt.append((sc, name, d["verdict"], sorted(sh, key=lambda t: -idf.get(t, 0))[:6]))
            live.sort(reverse=True); closed.sort(reverse=True)
            if not live or live[0][0] < min_score: continue
            best_closed = closed[0][0] if closed else 0.0
            if live[0][0] <= best_closed: continue    # a closure outranks the route: claim stands
            hits.append((live[0][0], surf, u, live[:top], best_closed))
    hits.sort(reverse=True)
    return hits

def show(hits, label):
    print(f"\n{'='*78}\n{label}: {len(hits)} permanence claims with a strongly-matching OPEN arc\n{'='*78}")
    for sc, surf, u, sc_list, bc in hits:
        print(f"\n[{sc:6.1f}] {surf}   (best CLOSING arc scores {bc:.1f} -- the route outranks it)")
        print(f"  CLAIM: {' '.join(u.split())[:190]}")
        for s, name, vd, sh in sc_list:
            print(f"    -> [{s:6.1f}] {vd:<6} {name}   shared: {', '.join(sh)}")
    return len(hits)

def control(min_score):
    print("="*78); print("M-1  TWO-SIDED CONTROL -- binding; the instrument is void without it")
    print("="*78)
    tmp = ROOT / "outside_bench" / "_ctrl_pos.md"
    tmp.write_text(
      "- The finite labels will not reduce further either: an invariant selector cannot pick a "
      "point of its own orbit, so a finite menu is the terminal state and not a deficiency. The "
      "rank-closing VEV direction and the integral orbit stay supplied.\n", encoding="utf-8")
    neg = ROOT / "outside_bench" / "_ctrl_neg.md"
    neg.write_text(
      "- The dimensionful unit is external by design and will not reduce: nobody derives the metre, "
      "and Mostow rigidity fixes the shape of a finite-volume hyperbolic 3-manifold and not its "
      "size, so the scale is permanently outside reach as a value.\n", encoding="utf-8")
    try:
        pos = sweep(min_score, 3, ["outside_bench/_ctrl_pos.md"])
        npos = show(pos, "POSITIVE CONTROL -- must FLAG (Route A is live)")
        ngv = sweep(min_score, 3, ["outside_bench/_ctrl_neg.md"])
        nneg = show(ngv, "NEGATIVE CONTROL -- must NOT flag (scale is permanent, correctly)")
    finally:
        tmp.unlink(missing_ok=True); neg.unlink(missing_ok=True)
    v = "M1-DISCRIMINATES" if (npos > 0 and nneg == 0) else "M1-USELESS"
    print(f"\n{'='*78}\nCONTROL: positive {npos}, negative {nneg}  =>  {v}")
    if v == "M1-USELESS": print("INSTRUMENT VOID -- not adopted.")
    print("="*78)
    return v

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--min-score", type=float, default=28.0)
    a = ap.parse_args()
    if a.control: control(a.min_score); sys.exit(0)
    v = control(a.min_score)
    if v == "M1-USELESS": sys.exit(1)
    h = sweep(a.min_score, 3, SURFACES)
    n = show(h, "M-2  SWEEP")
    print(f"\nOUTCOME: {'M2-FINDINGS' if n else 'M2-CLEAN'}")
    print("FENCE: a flag is a prompt to READ, never a verdict. It says only that an OPEN arc")
    print("bears on a permanence claim -- the judgement stays human-side.")
