"""The Recurrence Atlas -- the query API (the toolset).

Seven uses, each a function that returns STRUCTURED data plus a human-readable `text` field:
  1 re-orient fast .......... context_card()
  2 obstacle -> resolution .. resolutions_for(obstacle_type)     [the 'cycle', queryable]
  3 motif -> recurrence ..... motif_trace(motif)
  4 dead-end revival ........ revive(probe_id)
  5 genuine-unity detector .. meeting_points()                   [candidates, NOT proof]
  6 gap finder .............. gaps()
  7 self-consistency ........ context_card() + the whole graph

Load order: reads scripts/atlas/atlas_data.json if present, else mines fresh.
Run `python scripts/atlas/query.py [card|motif X|obstacle Y|revive B###|gaps|meet]` for a demo.
"""
import os
import sys
import json
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
import atlas  # noqa: E402

L = atlas.LEXICON


def load():
    if os.path.exists(atlas.DATA):
        with open(atlas.DATA, encoding="utf-8") as f:
            return json.load(f)
    return atlas.mine()


def _domains(motifs):
    return sorted({L[m]["domain"] for m in motifs if m in L})


def _banked(P):
    return {pid: p for pid, p in P.items() if p["status"] == "banked"}


# -- 3: motif -> recurrence trace ------------------------------------------------------------------
def motif_trace(motif, g=None):
    g = g or load(); P = g["probes"]
    if motif not in L:
        return dict(motif=motif, error="unknown motif", known=sorted(L), text=f"unknown motif '{motif}'")
    hits = [pid for pid, p in P.items() if motif in p["motifs"]]
    cross = [pid for pid in hits if L[motif]["domain"] not in _domains([motif]) or
             len(_domains(P[pid]["motifs"])) >= 4]   # touched in a cross-domain (>=4 domain) probe
    info = L[motif]
    text = (f"{motif}  [{info['kind']}/{info['conserved']}, home={info['domain']}]  -- {info['gloss']}\n"
            f"  recurs in {len(hits)}/{len(P)} probes ({100*len(hits)//len(P)}%); "
            f"{len(cross)} in cross-domain (>=4 domains) probes\n"
            f"  e.g. {', '.join(sorted(hits)[:16])}")
    return dict(motif=motif, meta=info, count=len(hits), probes=sorted(hits),
                cross_domain_probes=sorted(cross), text=text)


# -- 2: obstacle -> resolution oracle (the cycle) --------------------------------------------------
def resolutions_for(obstacle_type, g=None, banked_only=True):
    g = g or load(); P = g["probes"]
    if obstacle_type not in g["obstacles"]:
        return dict(obstacle=obstacle_type, error="unknown obstacle", known=g["obstacles"],
                    text=f"unknown obstacle '{obstacle_type}'; known: {', '.join(g['obstacles'])}")
    pool = _banked(P) if banked_only else P
    rel = {pid: p for pid, p in pool.items() if p["obstacle"] == obstacle_type}
    motif_counts = Counter(m for p in rel.values() for m in p["motifs"])
    ranked = motif_counts.most_common()
    conserved = [(m, c) for m, c in ranked if L[m]["conserved"] in ("first-integral", "structural")]
    lines = [f"obstacle '{obstacle_type}': {len(rel)} {'banked ' if banked_only else ''}probes touched it"]
    lines += [f"  {m:16s} x{c:<3d} [{L[m]['conserved']}]" for m, c in ranked[:8]]
    top_conserved = conserved[0][0] if conserved else None
    if top_conserved:
        lines.append(f"  -> historically resolved with the conserved motif: {top_conserved}")
    return dict(obstacle=obstacle_type, n_probes=len(rel), ranked=ranked,
                conserved_resolvers=conserved, top_conserved=top_conserved, text="\n".join(lines))


# -- 4: dead-end / DORMANT revival -----------------------------------------------------------------
def revive(probe_id, g=None):
    """Given a dormant/dead lead, suggest the conserved motif(s) that historically resolved
    BANKED probes at the SAME obstacle-type -- the owner's 're-use the same object' move, made queryable."""
    g = g or load(); P = g["probes"]
    p = P.get(probe_id)
    if not p:
        return dict(probe=probe_id, error="unknown probe", text=f"unknown probe '{probe_id}'")
    ob = p["obstacle"]
    own = set(p["motifs"])
    res = resolutions_for(ob, g) if ob else dict(ranked=[], conserved_resolvers=[])
    # motifs that resolved this obstacle-type elsewhere but are ABSENT here = the suggestion
    suggest = [(m, c) for m, c in res.get("conserved_resolvers", []) if m not in own][:5]
    text = [f"revive {probe_id} [{p['status']}]  -- \"{p['slug']}\"",
            f"  obstacle-type: {ob or 'unclassified'};  motifs already tried: {', '.join(sorted(own)) or 'none'}"]
    if suggest:
        text.append("  conserved motifs that resolved this obstacle-type ELSEWHERE (not yet used here):")
        text += [f"    {m:16s} (resolved {c} banked probes) -- {L[m]['gloss']}" for m, c in suggest]
    else:
        text.append("  no unused conserved resolver found for this obstacle-type (already saturated, or novel).")
    return dict(probe=probe_id, status=p["status"], obstacle=ob, own_motifs=sorted(own),
                suggestions=suggest, text="\n".join(text))


# -- 5: genuine-unity detector (wrap) --------------------------------------------------------------
def meeting_points(g=None, top=15):
    g = g or load()
    mp = atlas.meeting_points(g, top=top)
    lines = ["candidate meeting-points (cross-domain re-surfacings) -- CANDIDATES for human judgement, NOT proof:"]
    lines += [f"  {r['probe']:6s} s={r['score']:2d} [{r['status']}] {'+'.join(r['patterns']) or 'breadth'}"
              f"  ({', '.join(r['domains'])})" for r in mp]
    return dict(candidates=mp, text="\n".join(lines))


# -- co-occurrence / neighbors ---------------------------------------------------------------------
def neighbors(motif, g=None, top=8):
    g = g or load(); P = g["probes"]
    if motif not in L:
        return dict(motif=motif, error="unknown motif", text=f"unknown motif '{motif}'")
    co = Counter()
    for p in P.values():
        if motif in p["motifs"]:
            for m in p["motifs"]:
                if m != motif:
                    co[m] += 1
    ranked = co.most_common(top)
    text = f"{motif} co-occurs most with: " + ", ".join(f"{m}({c})" for m, c in ranked)
    return dict(motif=motif, neighbors=ranked, text=text)


def cooccurrence(a, b, g=None):
    g = g or load(); P = g["probes"]
    both = [pid for pid, p in P.items() if a in p["motifs"] and b in p["motifs"]]
    na = sum(a in p["motifs"] for p in P.values()); nb = sum(b in p["motifs"] for p in P.values())
    text = f"{a} & {b} co-occur in {len(both)} probes (of {na} with {a}, {nb} with {b})"
    return dict(a=a, b=b, count=len(both), probes=sorted(both), text=text)


# -- 6: gap finder ---------------------------------------------------------------------------------
def gaps(g=None):
    g = g or load(); P = g["probes"]; B = _banked(P)
    # under-resolved obstacle-types: many probes hit them, few are BANKED
    by_ob = Counter(p["obstacle"] for p in P.values() if p["obstacle"])
    banked_ob = Counter(p["obstacle"] for p in B.values() if p["obstacle"])
    under = sorted(((ob, banked_ob.get(ob, 0), n) for ob, n in by_ob.items()),
                   key=lambda t: (t[1] / max(1, t[2]), -t[2]))
    # motif pairs individually common but rarely co-occurring = a structural gap
    freq = Counter(m for p in P.values() for m in p["motifs"])
    common = [m for m, c in freq.items() if c >= 0.15 * len(P)]
    weak = []
    for i in range(len(common)):
        for j in range(i + 1, len(common)):
            a, b = common[i], common[j]
            c = sum(a in p["motifs"] and b in p["motifs"] for p in P.values())
            exp = freq[a] * freq[b] / len(P)          # expected under independence
            if c < 0.4 * exp:
                weak.append((a, b, c, round(exp, 1)))
    weak.sort(key=lambda t: t[2] / max(1, t[3]))
    lines = ["under-resolved obstacle-types (few banked resolutions -> open frontier):"]
    lines += [f"  {ob:16s} {bk}/{n} banked" for ob, bk, n in under[:6]]
    lines.append("motif pairs that avoid each other (individually common, rarely meet -> a structural gap):")
    lines += [f"  {a} x {b}: {c} obs vs {exp} expected" for a, b, c, exp in weak[:6]]
    return dict(under_resolved=under, avoidant_pairs=weak, text="\n".join(lines))


# -- 1 & 7: the context card -----------------------------------------------------------------------
def context_card(g=None):
    g = g or load(); P = g["probes"]
    a = atlas.analyze(g)
    freq = sorted(a["freq"].items(), key=lambda kv: -kv[1])
    conserved = [(m, c) for m, c in freq if L[m]["conserved"] == "first-integral"]
    status = Counter(p["status"] for p in P.values())
    split = a["conserved_vs_tool"]
    tot = sum(split.values())
    mp = atlas.meeting_points(g, top=6)
    tool_probes = sum("trace_map" in p["motifs"] for p in P.values())
    lines = [
        "THE RECURRENCE ATLAS -- context card",
        f"  corpus: {a['n_probes']} frontier probes; status {dict(status)}",
        f"  the ONE conserved first integral: {conserved[0][0] if conserved else '?'} "
        f"(recurs {conserved[0][1]}x, {100*conserved[0][1]//a['n_probes']}%) -- genuine unity, MUST recur",
        "  top recurring motifs: " + ", ".join(f"{m}({c})" for m, c in freq[:6]),
        f"  recurrence is: structural-invariant {split.get('structural',0)} mentions | "
        f"conserved-integral {split.get('first-integral',0)} | TOOL {split.get('tool',0)}",
        f"  the honest split: the trace-map TOOL is in {tool_probes} probes ({100*tool_probes//a['n_probes']}%) "
        f"= method/selection-effect, NOT unity; only kappa is a forced first integral",
        "  top meeting-point candidates: " + ", ".join(f"{r['probe']}" for r in mp),
        "  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())",
    ]
    return dict(n_probes=a["n_probes"], status=dict(status), conserved_first_integral=conserved,
                top_motifs=freq[:8], conserved_vs_tool=split, meeting_points=mp, text="\n".join(lines))


if __name__ == "__main__":
    argv = sys.argv[1:]
    g = load()
    if not argv or argv[0] == "card":
        print(context_card(g)["text"])
    elif argv[0] == "motif":
        print(motif_trace(argv[1], g)["text"])
    elif argv[0] == "obstacle":
        print(resolutions_for(argv[1], g)["text"])
    elif argv[0] == "revive":
        print(revive(argv[1], g)["text"])
    elif argv[0] == "gaps":
        print(gaps(g)["text"])
    elif argv[0] == "meet":
        print(meeting_points(g)["text"])
    else:
        print(__doc__)
