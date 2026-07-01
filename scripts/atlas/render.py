"""The Recurrence Atlas -- regenerate docs/RECURRENCE_ATLAS.md from the mined graph.

    python scripts/atlas/render.py        # re-mines and rewrites the map (safe to re-run; it is GENERATED)

The map is DERIVED (navigation, not a claim). The stable *vision* lives in knowledge/K023 (hand-written).
"""
import os
import sys
import datetime
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
import atlas  # noqa: E402
import query  # noqa: E402

OUT = os.path.join(atlas.REPO, "docs", "RECURRENCE_ATLAS.md")
L = atlas.LEXICON


def _table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * len(head)) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def render():
    g = atlas.mine()
    a = atlas.analyze(g)
    P = g["probes"]
    n = a["n_probes"]
    today = datetime.date.today().isoformat()

    S = []
    S.append(f"""# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: {today} from {n} frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.""")

    # 1 -- the context card
    S.append("## Re-orient — the context card\n\n```\n" + query.context_card(g)["text"] + "\n```")

    # 2 -- motif frequency + the conserved-vs-tool split (the honest core)
    freq = sorted(a["freq"].items(), key=lambda kv: -kv[1])
    rows = [(m, c, f"{100*c//n}%", L[m]["kind"], L[m]["conserved"], L[m]["domain"], L[m]["gloss"])
            for m, c in freq]
    S.append("## Motif recurrence — frequency, kind, and conserved-status\n\n"
             "The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically "
             "forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the "
             "transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** "
             "means derived/incidental.\n\n"
             + _table(rows, ["motif", "#probes", "%", "kind", "conserved", "home domain", "gloss"]))

    split = a["conserved_vs_tool"]
    tool_probes = sum("trace_map" in p["motifs"] for p in P.values())
    S.append("### The honest split — unity vs the hammer\n\n"
             f"- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in "
             f"**{a['freq'].get('kappa',0)}** probes ({100*a['freq'].get('kappa',0)//n}%). A first integral is "
             f"*conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.\n"
             f"- **Structural invariants** (the two ends, ω, the Dickson parity, …): "
             f"**{split.get('structural',0)}** mentions — invariants of the object's transforms.\n"
             f"- **The hammer (selection effect):** the trace-map **tool** appears in **{tool_probes}** probes "
             f"({100*tool_probes//n}%). This recurrence is *because it is our method* — it is **not** evidence of "
             f"unity. The atlas keeps this separate on purpose (verify-don't-trust).")

    # 3 -- the cycle: obstacle -> resolving motif
    S.append("## The cycle — obstacle → which motif historically resolved it\n\n"
             "For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the "
             "**banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).")
    crows = []
    for ob in g["obstacles"]:
        r = query.resolutions_for(ob, g)
        if r.get("n_probes"):
            top = ", ".join(f"{m}({c})" for m, c in r["ranked"][:4])
            crows.append((ob, r["n_probes"], r.get("top_conserved") or "—", top))
    S.append(_table(crows, ["obstacle-type", "#banked", "top conserved resolver", "top motifs"]))

    # 4 -- meeting points (candidates)
    mp = atlas.meeting_points(g, top=20)
    S.append("## Candidate meeting-points — cross-domain re-surfacings\n\n"
             "> **These are CANDIDATES for human judgement, never proof.** The detector scores *domain breadth* "
             "+ documented **unity-patterns** (co-occurrence signatures seeded from K007/K021/B67/B121/B261/B293). "
             "Co-occurrence ≠ meeting: a probe can name-check many motifs without identifying them. The famous "
             "meetings land in the top tier, but so do many synthesis probes — that saturation is itself the "
             "'one object seen from many angles' fingerprint. Confirm each by reading the probe.\n")
    mrows = [(r["probe"], r["score"], r["status"], "+".join(r["patterns"]) or "breadth",
              ", ".join(r["domains"])) for r in mp]
    S.append(_table(mrows, ["probe", "score", "status", "unity-patterns fired", "domains"]))
    S.append("**The unity-patterns** (the documented cross-structure identifications the detector looks for):\n\n"
             + "\n".join(f"- `{up['name']}` (weight {up['weight']}) — {up['gloss']}" for up in atlas.UNITY_PATTERNS))

    # 5 -- gaps
    gp = query.gaps(g)
    S.append("## Gaps — the open frontier\n\n"
             "Obstacle-types with few **banked** resolutions (under-resolved ⇒ where the object has *not* yet "
             "been shown to help):\n\n"
             + _table([(ob, f"{bk}/{tot}") for ob, bk, tot in gp["under_resolved"][:8]],
                      ["obstacle-type", "banked / touched"]))

    # footer
    S.append("---\n*Generated by `scripts/atlas/` (mine → analyze → detect → render). "
             "The instrument is re-runnable; the map stays current by regeneration. "
             "See `knowledge/K023` for the vision and the honest tool-bias caveat.*")

    text = "\n\n".join(S) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    return OUT, len(P)


if __name__ == "__main__":
    out, n = render()
    print(f"regenerated {out} from {n} probes")
