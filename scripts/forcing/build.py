#!/usr/bin/env python3
"""The forcing graph — K024 made live.

K024 ("The forcing map: the object's anatomy, and what can escape it") was built 2026-07-08 on
the owner's directive: *measure the whole body -- every emergence, convergence, knot, residue --
and see its self-triggering structure.* It has sat as 916 words of static prose with 15 nodes,
15 arrows, and zero edges marked PROVEN/KNOWN/OPEN. This assembles it from the record.

WHAT THIS IS, STATED PRECISELY SO IT IS NOT OVERSOLD:

  A CITATION IS NOT A FORCING.

This builds the ATTACHMENT graph -- which arcs attach to which face of the object, and what
cites what -- from five existing sources. That is the substrate a forcing graph needs, and it
is enough to make GAPS VISIBLE, which is the property the owner asked for: a branch that is not
in the graph shows up as a hole rather than being quietly forgotten.

Genuine FORCING edges ("X forces Y") must be AUTHORED, exactly like the arc verdicts. The graph
marks which edges are authored and which are merely attachment, and never conflates them.

NODES
  faces        the 12 faces kill_graph already uses to classify 217 negatives -- the object's
               anatomy, already named and already in use
  facets       the K-layer explainers (K001..K025)
  bits         the saturated discrete menu: B733 proved it BOUNDED and depth-independent,
               B766 proved it RANK-SATURATED at exactly 3 -- conjugation, reversal, the golden
               branch. This is the whole closing set, not a sample of it.

EDGES (all attachment unless marked authored)
  arc -> face      kill_graph faces_consulted
  law -> arc       LAW_MAP row citations
  facet -> arc     K-layer anchors
  chain -> arc     THEOREM_LEDGER link citations
  arc -> arc       arc_verdict depends_on   [AUTHORED]
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# The saturated discrete menu -- B733 (bounded, depth-independent) + B766 (rank-saturated at 3).
BITS = [("c", "conjugation"), ("theta", "reversal"), ("gamma5", "the golden branch")]



_FINDINGS_NAMES = ("FINDINGS.md", "VERDICT.md", "README.md", "WORK.md", "SCOUT.md",
                   "SYNTHESIS.md", "PREREGISTRATION.md")


def _findings_doc(d):
    """The arc's write-up, whatever it is called (B985).

    Exact-name matching lost 42 arcs. Prefer the canonical name, then the known variants,
    then any FINDINGS-ish file, so an arc is ingested on having content rather than on
    having guessed the filename convention of its year.
    """
    import glob as _glob
    for n in _FINDINGS_NAMES:
        p = os.path.join(d, n)
        if os.path.isfile(p):
            return p
    hits = sorted(_glob.glob(os.path.join(d, "*FINDINGS*.md")))
    return hits[0] if hits else None


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def build():
    G = {"faces": defaultdict(set), "facets": {}, "laws": {}, "chain": {},
         "authored": [], "arcs": {}}

    # --- arcs and their verdicts (the status layer) -----------------------------------------
    fdir = os.path.join(ROOT, "frontier")
    for d in sorted(os.listdir(fdir)):
        m = re.match(r"(B\d+)[a-zA-Z]?_", d)
        # B985 (cc3 decision 1): this once required the exact name "FINDINGS.md" and silently
        # skipped 42 arcs carrying real content under another name -- including B1-B5, the first
        # five arcs of the programme (README.md only), B68 (FINDINGS_E.md), B473 (FINDINGS_C1.md),
        # B511 (D3_FINDINGS.md). Hygiene, not discovery: cc3 checked and the 77% figure moves only
        # between 58-79% either way. But any re-run of the attachment inherits the blind spot until
        # this is fixed, so it is fixed before the re-run rather than after.
        if not m or not _findings_doc(os.path.join(fdir, d)):
            continue
        aid = m.group(1)
        rec = {"dir": d, "verdict": None, "instrument": False}
        vp = os.path.join(fdir, d, "arc_verdict.json")
        if os.path.isfile(vp):
            v = json.load(open(vp, encoding="utf-8"))
            rec["verdict"] = v.get("verdict")
            rec["instrument"] = bool(v.get("instrument"))
            for dep in (v.get("depends_on") or []):
                G["authored"].append((aid, dep))          # AUTHORED forcing-candidate edge
        G["arcs"][aid] = rec

    # --- arc -> face, from the kill graph ---------------------------------------------------
    kg = json.load(open(os.path.join(fdir, "B738_pathfinder_compiler", "kill_graph.json"),
                       encoding="utf-8"))
    for r in kg:
        for f in r["faces_consulted"]:
            if f != "none":
                G["faces"][f].add(r["id"])

    # --- facet -> arc, from the K-layer -----------------------------------------------------
    kdir = os.path.join(ROOT, "knowledge")
    for f in sorted(os.listdir(kdir)):
        km = re.match(r"(K\d{3})_", f)
        if km:
            G["facets"][km.group(1)] = set(re.findall(r"\bB\d{2,3}\b", _read(f"knowledge/{f}")))

    # --- law -> arc -------------------------------------------------------------------------
    for line in _read("docs/LAW_MAP.md").splitlines():
        if line.startswith("|") and "---" not in line:
            name = re.search(r"\*\*(.+?)\*\*", line)
            if name:
                G["laws"][name.group(1)[:60]] = set(re.findall(r"\bB\d{2,3}\b", line))

    # --- chain link -> arc ------------------------------------------------------------------
    t = _read("docs/THEOREM_LEDGER.md")
    for b in re.split(r"(?=^\*\*C\d+ \[)", t, flags=re.M):
        cm = re.match(r"\*\*(C\d+) \[([A-Z-]+)", b)
        if cm:
            G["chain"][cm.group(1)] = {"label": cm.group(2),
                                       "arcs": set(re.findall(r"\bB\d{2,3}\b", b))}
    return G


def gaps(G):
    """The property the owner asked for: what is MISSING shows up, rather than being forgotten."""
    out = {}
    # a face with no positively-verdicted arc attached
    pos = {a for a, r in G["arcs"].items() if r["verdict"] == "PROVED"}
    out["faces_with_no_proved_arc"] = sorted(
        f for f, arcs in G["faces"].items() if not (arcs & pos))
    # arcs attached to no face at all -- invisible to the anatomy
    attached = set().union(*G["faces"].values()) if G["faces"] else set()
    out["arcs_on_no_face"] = sorted(set(G["arcs"]) - attached)
    # arcs with no verdict -- invisible to the status layer
    out["arcs_with_no_verdict"] = sorted(a for a, r in G["arcs"].items() if r["verdict"] is None)
    # chain links citing arcs that carry no verdict
    out["chain_links_on_unverdicted_arcs"] = sorted(
        c for c, d in G["chain"].items()
        if d["arcs"] and not any(G["arcs"].get(a, {}).get("verdict") for a in d["arcs"]))
    return out


def main():
    G = build()
    gp = gaps(G)
    print("=" * 78)
    print("THE FORCING GRAPH — K024 assembled from the record")
    print("=" * 78)
    print(f"\n  NODES")
    print(f"    faces  (the object's anatomy) : {len(G['faces'])}")
    print(f"    facets (K-layer explainers)   : {len(G['facets'])}")
    print(f"    arcs                          : {len(G['arcs'])}")
    print(f"    bits (SATURATED menu, B733+B766): {len(BITS)}  "
          f"-- {', '.join(n for _, n in BITS)}")
    print(f"\n  EDGES")
    print(f"    arc -> face     : {sum(len(v) for v in G['faces'].values())}")
    print(f"    facet -> arc    : {sum(len(v) for v in G['facets'].values())}")
    print(f"    law -> arc      : {sum(len(v) for v in G['laws'].values())}")
    print(f"    chain -> arc    : {sum(len(d['arcs']) for d in G['chain'].values())}")
    print(f"    arc -> arc      : {len(G['authored'])}   [AUTHORED -- the only forcing-grade edges]")

    print(f"\n  THE FACES, by attached arcs and how many carry a verdict")
    for f, arcs in sorted(G["faces"].items(), key=lambda kv: -len(kv[1])):
        v = sum(1 for a in arcs if G["arcs"].get(a, {}).get("verdict"))
        print(f"    {f:24} {len(arcs):4} arcs   {v:3} verdicted")

    print(f"\n  GAPS — what is missing, made visible")
    print(f"    faces with NO proved arc      : {len(gp['faces_with_no_proved_arc'])}"
          f"  {gp['faces_with_no_proved_arc'][:6]}")
    print(f"    arcs on NO face               : {len(gp['arcs_on_no_face'])}"
          f"   (invisible to the anatomy)")
    print(f"    arcs with NO verdict          : {len(gp['arcs_with_no_verdict'])}"
          f"   (invisible to the status layer)")
    print(f"    chain links on unverdicted arcs: {len(gp['chain_links_on_unverdicted_arcs'])}")

    print(f"\n  HONEST SCOPE: every edge above except `arc -> arc` is ATTACHMENT (a citation),")
    print(f"  NOT a forcing. A citation is not a forcing. Genuine forcing edges must be authored,")
    print(f"  exactly like the verdicts -- and there are currently {len(G['authored'])} of them.")

    out = {"faces": {k: sorted(v) for k, v in G["faces"].items()},
           "facets": {k: sorted(v) for k, v in G["facets"].items()},
           "chain": {k: {"label": d["label"], "arcs": sorted(d["arcs"])}
                     for k, d in G["chain"].items()},
           "authored_edges": G["authored"], "bits": BITS, "gaps": gp}
    p = os.path.join(ROOT, "scripts", "forcing", "forcing_graph.json")
    json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)
    print(f"\n  written: scripts/forcing/forcing_graph.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
