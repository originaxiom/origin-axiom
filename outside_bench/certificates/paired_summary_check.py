#!/usr/bin/env python3
"""THE PAIRED-SUMMARY CHECK — does a summary claim more closure than its own cell?

Sealed design: outside_bench/seals/PAIRED_SUMMARY_PREREG.md (pushed before this file).

Successor to memo 164's NOT-ADOPTED detector.  Memo 164 asked an OPEN-ENDED question
("is there a live arc somewhere bearing on this permanence claim?") and failed because a
drifted permanence claim omits the vocabulary of the route it forecloses.  This asks a
CLOSED question about two texts that are about the same thing by construction.

TWO ARMS, and the difference between them is itself a finding filed in the memo:

  ARM A -- THE SEALED SUBSTRATE.  summary = arc_verdict.json:claim_one_line,
           cell = FINDINGS.md.  This is what the seal and memo 165 named.
  ARM B -- THE REPAIRED SUBSTRATE.  summary = claim_one_line + FINDINGS.md,
           cell = the arc's machine-readable CELL RECORDS (verification/*.json and
           *_results.json 'cells'), which is what B1220 actually compared by hand
           ("its own cell record GC-27").

Binding control, per the seal:  positive B1196 (the real instance, found by hand by
B1220, which this instrument had no part in choosing); negatives B990, B1202.

A flag is a prompt to read both texts, never a verdict.  Gate 5 untouched: text only.
"""

import json
import math
import os
import re
import sys
import glob
import collections

ROOT = os.environ.get("OA_ROOT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FRONTIER = os.path.normpath(os.path.join(ROOT, "frontier"))

# ---------------------------------------------------------------- lexicons
# Declared before running.  Kept deliberately plain: these are ordinary English
# closure / limitation verbs, not phrases lifted from any arc that will be judged.

CLOSURE = [
    r"\bwhich is why\b", r"\bexplains? why\b", r"\bexplained\b",
    r"\bclose[sd]?\b", r"\bclosing\b", r"\bsettle[sd]?\b", r"\bsettled\b",
    r"\bresolve[sd]?\b", r"\bproved?\b", r"\bproven\b", r"\bestablishe[sd]\b",
    r"\bderive[sd]\b", r"\baccounts? for\b", r"\brules? out\b", r"\bforbids?\b",
    r"\bno longer (open|a gap)\b", r"\bfully\b", r"\bcomplete(ly)?\b",
    r"\bterminal\b", r"\bpermanent\b", r"\bwill not\b", r"\bcannot be\b",
    r"\bconfirmed\b", r"\bidentified\b", r"\bexact(ly)?\b",
]

LIMIT = [
    r"\bdoes not (reach|exist|follow|hold|extend|cover|settle|close)\b",
    r"\bdo not (reach|exist|follow|hold|extend|cover)\b",
    r"\bfails?\b", r"\bfailing\b", r"\bnot (yet|been|independently|established|proved|proven|verified|checked|derived|shown)\b",
    r"\bpartial\b", r"\bopen\b", r"\bremains?\b", r"\bunproved\b", r"\bunverified\b",
    r"\bunresolved\b", r"\bcaveat\b", r"\bfence\b", r"\bscoped\b", r"\bnot general\b",
    r"\bnot claimed\b", r"\bassumed\b", r"\bconjectur", r"\bhypothesis (is )?unmet\b",
    r"\bno (single|such|\(t, ?g\)|pair) \w*\s?(has|have)? ?been\b",
    r"\bnot a (proof|new proof|crossing|derivation)\b", r"\bstill\b",
    r"\bmissing\b", r"\blimitation\b", r"\bonly\b", r"\bnot independently\b",
]

CLOSURE_RE = [re.compile(p, re.I) for p in CLOSURE]
LIMIT_RE = [re.compile(p, re.I) for p in LIMIT]

GREEK = {
    "λ": "lambda", "Λ": "lambda", "σ": "sigma", "Σ": "sigma",
    "κ": "kappa", "ω": "omega", "Ω": "omega", "ε": "epsilon",
    "ζ": "zeta", "μ": "mu", "τ": "tau", "ρ": "rho",
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
    "φ": "phi", "π": "pi", "θ": "theta", "ψ": "psi",
}

STOP = set("""the a an and or but of to in on for with as is are was were be been being it its
this that these those which who whom whose from by at not no nor so if then than there here
we i our my one two three all any each both some more most other same such only own very can
could would should may might must will shall do does did done has have had having what when
where how why into out over under again further once about against between during before after
above below up down off through because until while at s t re ve ll d m o y""".split())

TOKEN_RE = re.compile(r"[a-z][a-z0-9_\-]{2,}")


def norm(text):
    for g, a in GREEK.items():
        text = text.replace(g, " " + a + " ")
    return text


def toks(text):
    return set(w for w in TOKEN_RE.findall(norm(text).lower()) if w not in STOP)


SENT_SPLIT = re.compile(r"(?<=[.;!?])\s+|\n{2,}|(?:^|\n)\s*[-*|]\s+")


def sentences(text):
    out = []
    for chunk in SENT_SPLIT.split(norm(text)):
        if not chunk:
            continue
        c = " ".join(chunk.split())
        # split very long chunks on em-dashes so a paragraph-scale line does not
        # trivially contain both a closure and a limitation marker
        parts = re.split(r"\s+--\s+|\s+—\s+", c) if len(c) > 300 else [c]
        for p in parts:
            p = p.strip()
            if 25 <= len(p) <= 900:
                out.append(p)
    return out


def has(res, s):
    return [r.pattern for r in res if r.search(s)]


# ---------------------------------------------------------------- corpus load

def arc_dirs():
    for d in sorted(os.listdir(FRONTIER)):
        p = os.path.join(FRONTIER, d)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "arc_verdict.json")):
            yield d, p


def arc_id(dirname):
    m = re.match(r"(B\d+)", dirname)
    return m.group(1) if m else dirname


def read(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def cell_records(path):
    """Return list of (label, text, cell_verdict) from an arc's machine-readable cells."""
    out = []
    for f in sorted(glob.glob(os.path.join(path, "**", "*.json"), recursive=True)):
        if os.path.basename(f) == "arc_verdict.json":
            continue
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                d = json.load(fh)
        except Exception:
            continue
        cells = None
        if isinstance(d, dict) and isinstance(d.get("cells"), dict):
            cells = d["cells"]
        elif isinstance(d, dict) and d and all(
            isinstance(v, dict) and ("verdict" in v or "caveats" in v) for v in d.values()
        ):
            cells = d
        if not cells:
            continue
        for key, c in cells.items():
            if not isinstance(c, dict):
                continue
            bits = []
            for field in ("headline", "caveats", "evidence", "refutations", "note", "summary"):
                v = c.get(field)
                if isinstance(v, str):
                    bits.append(v)
                elif isinstance(v, list):
                    bits.extend(x for x in v if isinstance(x, str))
            if bits:
                out.append((os.path.basename(f) + ":" + str(key), "\n\n".join(bits),
                            str(c.get("verdict", ""))))
    return out


SETTLED = {"PROVED", "RESOLVED", "RESOLVED-A", "THEOREM", "NEGATIVE", "CLOSED"}
WEAKER = {"PARTIAL", "OPEN", "INCONCLUSIVE", "UNRESOLVED", "PENDING", "MIXED"}


def build():
    arcs = {}
    for d, p in arc_dirs():
        try:
            with open(os.path.join(p, "arc_verdict.json"), encoding="utf-8", errors="replace") as f:
                v = json.load(f)
        except Exception:
            continue
        arcs[arc_id(d)] = {
            "dir": d,
            "path": p,
            "verdict": str(v.get("verdict", "")),
            "claim": str(v.get("claim_one_line", "")),
            "findings": read(os.path.join(p, "FINDINGS.md")),
            "cells": cell_records(p),
        }
    return arcs


def doc_freq(arcs):
    df = collections.Counter()
    for a in arcs.values():
        blob = a["claim"] + "\n" + a["findings"] + "\n" + "\n".join(t for _, t, _ in a["cells"])
        for w in toks(blob):
            df[w] += 1
    return df


# ---------------------------------------------------------------- the detector

def pairs(summary_text, cell_units, df, n_arcs, df_frac):
    """cell_units: list of (label, text, verdict). Yields flag dicts."""
    df_max = df_frac * n_arcs
    ssents = sentences(summary_text)
    prepared_s = []
    for s in ssents:
        cl = has(CLOSURE_RE, s)
        if not cl:
            continue
        if has(LIMIT_RE, s):
            continue           # the summary fences itself -- not a mirror instance
        st = {w for w in toks(s) if 0 < df.get(w, 0) <= df_max}
        if st:
            prepared_s.append((s, cl, st))
    flags = []
    for label, ctext, cverdict in cell_units:
        for c in sentences(ctext):
            lm = has(LIMIT_RE, c)
            if not lm:
                continue
            ct = {w for w in toks(c) if 0 < df.get(w, 0) <= df_max}
            if not ct:
                continue
            for s, cl, st in prepared_s:
                shared = st & ct
                if not shared:
                    continue
                score = sum(math.log(n_arcs / max(1, df.get(w, 1))) for w in shared)
                flags.append({
                    "score": round(score, 2),
                    "shared": sorted(shared, key=lambda w: df.get(w, 0))[:8],
                    "summary": s,
                    "cell": c,
                    "cell_label": label,
                    "cell_verdict": cverdict,
                    "closure_markers": cl[:4],
                    "limit_markers": lm[:4],
                })
    flags.sort(key=lambda f: -f["score"])
    return flags


def run_arm(arcs, df, arm, df_frac, min_shared, only=None):
    n = len(arcs)
    res = {}
    for aid, a in arcs.items():
        if only and aid not in only:
            continue
        if arm == "A":
            summary = a["claim"]
            units = [("FINDINGS.md", a["findings"], "")]
            if not a["findings"].strip():
                continue
        else:
            summary = a["claim"] + "\n\n" + a["findings"]
            units = a["cells"]
            if not units:
                continue
        fl = pairs(summary, units, df, n, df_frac)
        fl = [f for f in fl if len(f["shared"]) >= min_shared]
        # arm B bonus: cell verdict strictly weaker than the arc verdict
        if arm == "B":
            for f in fl:
                if a["verdict"].upper() in SETTLED and f["cell_verdict"].upper() in WEAKER:
                    f["score"] = round(f["score"] + 5.0, 2)
                    f["downgrade"] = a["verdict"].upper() + " > " + f["cell_verdict"].upper()
            fl.sort(key=lambda f: -f["score"])
        if fl:
            res[aid] = fl
    return res


POSITIVE = "B1196"
NEGATIVES = ["B990", "B1202"]
DF_FRAC = 0.25          # a term is "distinctive" if it appears in < 1/4 of arcs
MIN_SHARED = 1

# The sealed positive is not merely "arc B1196 flags" -- it is THE PAIR B1220 found by
# hand.  Flagging the arc on some other pair is not catching the instance; memo 164's
# lesson ("control passing is not instrument working") applies at pair granularity.
REAL_SUMMARY_MARK = "which is WHY they are anchors"
REAL_CELL_MARKS = ("first hypothesis", "read off D")


def caught_real_instance(flags):
    for f in flags:
        if REAL_SUMMARY_MARK.lower() in f["summary"].lower() and any(
                m.lower() in f["cell"].lower() for m in REAL_CELL_MARKS):
            return True
    return False


def main():
    arcs = build()
    df = doc_freq(arcs)
    n = len(arcs)
    print("arcs with arc_verdict.json      : %d" % n)
    print("arcs with FINDINGS.md           : %d" % sum(1 for a in arcs.values() if a["findings"].strip()))
    print("arcs with machine cell records  : %d" % sum(1 for a in arcs.values() if a["cells"]))
    print()

    verdicts = {}
    for arm in ("A", "B"):
        print("=" * 78)
        print("ARM %s -- %s" % (arm, "SEALED substrate: claim_one_line vs FINDINGS.md" if arm == "A"
                                else "REPAIRED substrate: claim+FINDINGS vs the arc's own CELL RECORDS"))
        print("=" * 78)

        # ---- P-1 binding control
        ctl = run_arm(arcs, df, arm, DF_FRAC, MIN_SHARED, only=set([POSITIVE] + NEGATIVES))
        pos_hit = POSITIVE in ctl
        neg_hits = [x for x in NEGATIVES if x in ctl]
        print("P-1 control")
        print("  positive %-6s : %s" % (POSITIVE, "FLAGS (%d)" % len(ctl[POSITIVE]) if pos_hit else "no flag"))
        for x in NEGATIVES:
            print("  negative %-6s : %s" % (x, "FLAGS (%d)" % len(ctl[x]) if x in ctl else "no flag"))
        if pos_hit:
            top = ctl[POSITIVE][0]
            print("  top positive flag  score=%s shared=%s%s" %
                  (top["score"], top["shared"], "  " + top.get("downgrade", "")))
            print("    SUMMARY: %s" % top["summary"][:300])
            print("    CELL   : %s" % top["cell"][:300])
            print("    from   : %s" % top["cell_label"])
        # -- does the arm even HAVE the negatives in its substrate?  A negative that
        #    cannot fire is not a control; this is the Gate-D vacuous-pass failure mode.
        if arm == "A":
            can_fire = [x for x in NEGATIVES if arcs[x]["findings"].strip()]
        else:
            can_fire = [x for x in NEGATIVES if arcs[x]["cells"]]
        vacuous = [x for x in NEGATIVES if x not in can_fire]
        print("  negative-control substrate present for : %s" % (can_fire or "NONE"))
        if vacuous:
            print("  *** VACUITY: %s carry no text on this arm's cell side, so they CANNOT" % vacuous)
            print("      fire at any parameter setting.  Their silence is not discrimination.")

        # -- did it catch THE PAIR, not merely the arc?
        real = caught_real_instance(ctl.get(POSITIVE, []))
        print("  caught B1220's actual pair (summary %r vs cell %r): %s"
              % (REAL_SUMMARY_MARK, REAL_CELL_MARKS[0], "YES" if real else "NO"))

        # -- how selective is the arm on its own domain?
        domain = [k for k, v in arcs.items() if (v["findings"].strip() if arm == "A" else v["cells"])]
        full = run_arm(arcs, df, arm, DF_FRAC, MIN_SHARED)
        print("  selectivity on own domain: %d of %d arcs flagged (%.0f%%)"
              % (len(full), len(domain), 100.0 * len(full) / max(1, len(domain))))

        reasons = []
        if not pos_hit or not real:
            reasons.append("the sealed positive PAIR is not caught")
        if neg_hits:
            reasons.append("negatives fired: %s" % neg_hits)
        if vacuous:
            reasons.append("negative control VACUOUS on this substrate: %s" % vacuous)
        if len(full) == len(domain) and len(domain) > 1:
            reasons.append("flags %d of %d arcs in its own domain (no negative capacity)" % (len(full), len(domain)))
        p1 = "P1-USELESS" if reasons else "P1-DISCRIMINATES"
        print("  => %s%s" % (p1, ("  [" + "; ".join(reasons) + "]") if reasons else ""))
        print()

        if p1 != "P1-DISCRIMINATES":
            print("  P-2 NOT RUN on this arm: the seal makes P-1 binding.")
            verdicts[arm] = (p1, None)
            print()
            continue

        # ---- P-2 blind sweep
        sweep = run_arm(arcs, df, arm, DF_FRAC, MIN_SHARED)
        nflag = sum(len(v) for v in sweep.values())
        print("P-2 sweep: %d arcs flagged, %d flag pairs total" % (len(sweep), nflag))
        ranked = sorted(((max(f["score"] for f in v), k, v) for k, v in sweep.items()), reverse=True)
        for sc, aid, fl in ranked[:12]:
            f = fl[0]
            print("  %-7s score=%-7s %s%s" % (aid, sc, f["shared"][:5],
                                              "  [" + f["downgrade"] + "]" if "downgrade" in f else ""))
            print("      S: %s" % f["summary"][:260])
            print("      C: %s   <%s>" % (f["cell"][:260], f["cell_label"]))
        verdicts[arm] = (p1, (len(sweep), nflag, [(a, s) for s, a, _ in ranked[:25]]))
        print()

    print("=" * 78)
    for arm in ("A", "B"):
        p1, p2 = verdicts[arm]
        print("ARM %s : %s | %s" % (arm, p1, "P-2 not run" if p2 is None else
                                    ("P2-FINDINGS %d arcs / %d pairs" % (p2[0], p2[1]) if p2[1] else "P2-CLEAN")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
