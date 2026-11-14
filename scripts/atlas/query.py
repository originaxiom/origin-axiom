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


# CHANGED 2026-11-12 (Review 80; found by a reading of this file, made again before it was mended).  Review 79 took the
# atlas's tag out of the head of an arc's card, because the tag is a guess from the arc's words and disagrees with the
# verdict for hundreds of arcs.  The same tag was still printed as a status in four places: by `revive`, by the meeting
# points, in the context card's tally, and wherever a probe is counted as "banked".  Each prints it as the tag now.  The
# keys of what the functions return are not changed.
TAG = "the atlas's tag, a guess from the arc's words and not a verdict"


def _banked(P):
    """the probes whose TAG is "banked": a guess from their words.  It is not the set of arcs with a positive verdict."""
    return {pid: p for pid, p in P.items() if p["status"] == "banked"}


def _verdicts_of(arc_id):
    """(folder, verdict or None, claim line or None, unreadable) for every folder under frontier/ that carries the id"""
    import glob
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = []
    for d in sorted(glob.glob(os.path.join(root, "frontier", arc_id + "_*"))):
        if not os.path.isdir(d):
            continue
        h = os.path.join(d, "arc_verdict.json")
        if not os.path.isfile(h):
            out.append((os.path.relpath(d, root), None, None, False))
            continue
        try:
            v = json.load(open(h, encoding="utf-8"))
            out.append((os.path.relpath(d, root), v.get("verdict"), v.get("claim_one_line", ""), False))
        except ValueError:
            out.append((os.path.relpath(d, root), None, None, True))
    return out


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
    lines = [f"obstacle '{obstacle_type}': {len(rel)} probes {'tagged banked ' if banked_only else ''}touched it"
             + (f"  ('banked' is {TAG})" if banked_only else "")]
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
    verdicts = [v or "no verdict" for _, v, _, _ in _verdicts_of(probe_id)]
    text = [f"revive {probe_id} [{'; '.join(verdicts) or 'no verdict file'}]  -- \"{p['slug']}\"",
            f"  atlas tag (a guess from the arc's words, not a verdict): {p['status']}",
            f"  obstacle-type: {ob or 'unclassified'};  motifs already tried: {', '.join(sorted(own)) or 'none'}"]
    if suggest:
        text.append("  conserved motifs that resolved this obstacle-type ELSEWHERE (not yet used here):")
        text += [f"    {m:16s} (in {c} probes tagged banked) -- {L[m]['gloss']}" for m, c in suggest]
    else:
        text.append("  no unused conserved resolver found for this obstacle-type (already saturated, or novel).")
    return dict(probe=probe_id, status=p["status"], obstacle=ob, own_motifs=sorted(own),
                suggestions=suggest, text="\n".join(text))


# -- 5: genuine-unity detector (wrap) --------------------------------------------------------------
def meeting_points(g=None, top=15):
    g = g or load()
    mp = atlas.meeting_points(g, top=top)
    lines = ["candidate meeting-points (cross-domain re-surfacings) -- CANDIDATES for human judgement, NOT proof:",
             f"  (the word after 'tag' is {TAG})"]
    lines += [f"  {r['probe']:6s} s={r['score']:2d} [tag {r['status']}] {'+'.join(r['patterns']) or 'breadth'}"
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
    lines = [f"under-resolved obstacle-types (few probes tagged banked -> open frontier; 'banked' is {TAG}):"]
    lines += [f"  {ob:16s} {bk}/{n} tagged banked" for ob, bk, n in under[:6]]
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
        f"  corpus: {a['n_probes']} frontier probes; atlas tags (guesses from the arcs' words, not verdicts) {dict(status)}",
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


def arc_card(arc_id, g=None):
    """One arc: its verdict file's verdict and claim line, and the atlas's tag for it. Added 2026-11-10 (B1862; the
    advisor seat's audit, E10): `card B1812`, as the front page gives it, printed the corpus card whatever the id.
    CHANGED 2026-11-12 (Review 79): the head of the card printed the atlas's tag in brackets, as if it were the arc's
    status. The tag is a guess from the arc's words (the first of four word lists that matches) and it disagrees with
    the verdict for hundreds of arcs: 218 proved arcs were shown as dead and 198 negative ones as banked. The head now
    carries the verdict, and the tag is printed as what it is."""
    g = g or load(); p = g["probes"].get(arc_id)
    if not p:
        return dict(probe=arc_id, error="unknown arc", text=f"unknown arc '{arc_id}'")
    # CHANGED 2026-11-12 (Review 80; found by a reading of this function, made again before it was mended).  The card read
    # the first verdict file of the folders that carry the id, and no other.  One id, B58, is carried by three folders, one
    # of them RETRACTED: its card printed one folder's verdict under another folder's name, and the retracted folder never
    # appeared.  Every folder that carries the id is on the card now, each with its own verdict and claim line; the head
    # carries every verdict; and where there is more than one folder the card says that the atlas keeps one name for them.
    folders = _verdicts_of(arc_id)
    v = None
    if len(folders) == 1 and folders[0][1]:
        v = {"verdict": folders[0][1]}
    head = "; ".join(x[1] or ("unreadable" if x[3] else "no verdict") for x in folders) or "no verdict"
    text = [f"{arc_id} [{head}]  -- \"{p['slug']}\"" + (f"   ({len(folders)} folders carry this id; the atlas keeps one name for them)" if len(folders) > 1 else ""),
            f"  atlas tag (a guess from the arc's words, not a verdict): {p['status']}",
            f"  obstacle-type: {p['obstacle'] or 'unclassified'};  motifs: {', '.join(sorted(p['motifs'])) or 'none'}"]
    for folder, verdict, claim, unreadable in folders:
        if unreadable:
            text.append(f"  verdict file unreadable: {folder}/arc_verdict.json")
        elif verdict is None and claim is None:
            text.append(f"  no verdict file in {folder}")
        else:
            text.append(f"  verdict: {verdict}   folder: {folder}")
            text.append("  claim: " + str(claim))
    if not folders:
        text.append("  no verdict file under frontier/")
    # 2026-11-12 (Review 79's second round): the key "status" is the atlas's tag, a guess from the arc's words.  It is returned
    # under a name that says so as well; the old key stays for the callers that read it.
    # the key "verdict" holds the one verdict where one folder carries the id, as before; where several do it holds none, and
    # "verdicts_by_folder" holds each
    return dict(probe=arc_id, status=p["status"], atlas_tag_a_guess_from_words=p["status"], verdict=(v or {}).get("verdict"),
                verdicts_by_folder={x[0]: x[1] for x in folders}, text="\n".join(text))


if __name__ == "__main__":
    argv = sys.argv[1:]
    g = load()
    if not argv or (argv[0] == "card" and len(argv) == 1):
        print(context_card(g)["text"])
    elif argv[0] == "card":
        print(arc_card(argv[1], g)["text"])
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
