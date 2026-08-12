"""supersession — the arc graph must carry what the bodies know.

Two defects, one shape: metadata that does not carry what an arc's own body says.

(A) THE SUPERSESSION GRAPH IS ONE-WAY. 42 arcs declare `supersedes`; 5 carry the back-link. So a
    reader of `Y.superseded_by` cannot tell a live arc from one its successor refuted -- and 11 of
    the superseded targets are cited on curated surfaces. B1037 caught B123 by READING A BODY;
    B1043 missed B564 because no body said so. This graph is what should have said so.

(B) SELF-CORRECTING ARCS ARE UNREGISTERED. 35 FINDINGS carry a CORRECTION/REFUTED/WITHDRAWN banner
    BELOW their own headline; 31 have no `docs/RETRACTIONS.md` row, whose maintenance rule reads
    "every future retraction adds its row in the PR that banks the correction". The worst case is
    B408, whose body opens "THE SEAM DOES NOT CONTRACT -- the one scale lever stands" and 27 lines
    later says "the seam CONTRACTS -- persistence was an artifact ... the object has NO scale lever
    in any tested channel". A pass that reads bodies top-down meets the refuted headline first.

TRIAGED, NOT CAPPED -- the B821/B823 posture, as in `law_siblings.py`: this fails only on
UNTRIAGED items, asking for a judgement rather than a number.

DELIBERATELY NOT AUTOMATED: the back-links are not written. `supersedes` conflates REPLACES with
EXTENDS -- B142 "supersedes" B141 and B1039 correctly restored BOTH -- so auto-filling
`superseded_by` would mark live arcs dead.

  sweep() -> [(kind, arc, detail)] for items with no row in docs/consolidation/SUPERSESSIONS.md
"""
import glob
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs" / "consolidation" / "SUPERSESSIONS.md"
RETRACTIONS = ROOT / "docs" / "RETRACTIONS.md"
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]

# A banner that INVERTS the arc's own headline. Anchored to a markdown heading so that a passing
# mention of the word "corrected" in prose does not fire.
BANNER = re.compile(r"^#+\s*\**\s*(CORRECTION|CORRECTED|RETRACT|REFUTED|WITHDRAWN)", re.M | re.I)


def _arcs():
    """Distinct B-number -> verdict dict. Same idiom as law_siblings._arcs()."""
    out, seen = {}, set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        p = pathlib.Path(d) / "arc_verdict.json"
        if not m or not p.is_file():
            continue
        b = "B" + m.group(1)
        if b in seen:
            continue
        seen.add(b)
        try:
            out[b] = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
    return out


def _refs(v):
    """`supersedes`/`superseded_by` are written as a string, a list, or null."""
    if not v:
        return []
    if isinstance(v, str):
        return re.findall(r"B\d+", v)
    return [x for e in v for x in re.findall(r"B\d+", str(e))]


def _curated_blob():
    return "\n".join((ROOT / p).read_text(encoding="utf-8") for p in CURATED
                     if (ROOT / p).is_file())


def one_way_links():
    """X says `supersedes: Y` and Y does not say `superseded_by: X`."""
    arcs = _arcs()
    blob = _curated_blob()
    out = []
    for b, d in sorted(arcs.items(), key=lambda kv: int(kv[0][1:])):
        for t in _refs(d.get("supersedes")):
            if t in arcs and b not in _refs(arcs[t].get("superseded_by")):
                live = bool(re.search(rf"\b{t}\b", blob))
                out.append(("one-way", t, "superseded by %s; target %s on a curated surface"
                            % (b, "IS CITED" if live else "is not cited")))
    return out


def unregistered_self_corrections():
    """A FINDINGS body that inverts its own headline, with no RETRACTIONS row."""
    reg = RETRACTIONS.read_text(encoding="utf-8") if RETRACTIONS.is_file() else ""
    out = []
    for f in sorted(ROOT.glob("frontier/B*/FINDINGS.md")):
        m = re.match(r"(B\d+)_", f.parent.name)
        if not m:
            continue
        arc = m.group(1)
        txt = f.read_text(errors="ignore")
        hit = BANNER.search(txt)
        if not hit:
            continue
        if re.search(rf"\b{arc}\b", reg):
            continue
        out.append(("self-correction", arc,
                    "banner at %.0f%% of file, no RETRACTIONS row"
                    % (100 * hit.start() / max(1, len(txt)))))
    return sorted(set(out), key=lambda r: int(r[1][1:]))


def headline_vs_verdict():
    """A self-correcting arc whose VERDICT is not PROVED -- so its FINDINGS headline is the first
    thing a body-reading pass meets, and the arc itself concluded against it.

    NO SENTIMENT CLASSIFIER. A first draft tried to detect a "positive" headline by regex and had
    to hardcode "SCALE LEVER" to catch B408, whose headline reads "THE SEAM DOES NOT CONTRACT --
    the one scale lever stands": it CONTAINS a negation and ASSERTS a positive. That hack would
    have been an arc-specific rule inside a general instrument. Whether a headline misleads is a
    JUDGEMENT, and this instrument's whole posture is that judgements live in the registry. So all
    non-PROVED self-corrections are surfaced and each gets a disposition.
    """
    arcs = _arcs()
    out = []
    for _, arc, _ in unregistered_self_corrections():
        v = (arcs.get(arc, {}) or {}).get("verdict", "")
        if v in ("PROVED", "", None):
            continue
        fs = list(ROOT.glob(f"frontier/{arc}_*/FINDINGS.md"))
        if not fs:
            continue
        head = fs[0].read_text(errors="ignore").split("\n", 1)[0]
        out.append(("headline-vs-verdict", arc, "verdict %s; headline: %s" % (v, head[:88])))
    return out


def load_bearing():
    """What the gate fails on: items a reader would actually be misled by."""
    blob = _curated_blob()
    ow = [c for c in one_way_links() if "IS CITED" in c[2]]
    return ow + headline_vs_verdict()


def triaged():
    if not REGISTRY.is_file():
        return set()
    return {m.group(1) for m in
            (re.match(r"\|\s*`?(B\d+)`?\s*\|", ln.strip())
             for ln in REGISTRY.read_text(encoding="utf-8").splitlines()) if m}


def candidates():
    return one_way_links() + unregistered_self_corrections()


def sweep():
    """The gate's failure set: LOAD-BEARING items only, untriaged.

    Triaging all 72 candidates would mean writing 72 judgements without reading 72 bodies, which
    is the claim-line sin this instrument exists to name. The gate therefore asks for judgement
    where a reader is actually misled -- a superseded arc still CITED on a curated surface, or a
    positive headline over a negative verdict -- and the remainder is published as a measured
    backlog in the registry. Same shape as the blind-arc gate: substantial items are triaged, the
    count is not capped."""
    done = triaged()
    return [c for c in load_bearing() if c[1] not in done]


if __name__ == "__main__":
    cs, lb, miss = candidates(), load_bearing(), sweep()
    ow = [c for c in cs if c[0] == "one-way"]
    sc = [c for c in cs if c[0] == "self-correction"]
    print("supersession: %d one-way link(s), %d unregistered self-correction(s)" % (len(ow), len(sc)))
    print("              %d LOAD-BEARING (the gate's scope), %d untriaged" % (len(lb), len(miss)))
    for kind, arc, detail in lb:
        mark = "UNTRIAGED" if any(arc == m[1] for m in miss) else "triaged  "
        print("  [%s] %-18s %-6s %s" % (mark, kind, arc, detail))
