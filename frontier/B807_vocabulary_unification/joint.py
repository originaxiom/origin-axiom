#!/usr/bin/env python3
"""B807 — the joint distribution of (face, motif). Prereg 40b7ff01274b4c01.

Decides, against thresholds fixed BEFORE the run, whether the zero overlap between the
kill-graph's 11 faces and the atlas's 18 motifs means the vocabularies are REDUNDANT (merge)
or ORTHOGONAL (declare a two-layer structure; merging would destroy information).

Thresholds, quoted from the sealed prereg §2 and not adjustable here:
    SPREAD       if P >= 60 populated pairs AND top5 <= 0.50
    CONCENTRATED if P < 60 OR top5 > 0.50
    disagreement => AMBIGUOUS, and NEITHER action is taken
"""
import json
import math
import os
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
P_FLOOR = 60          # sealed
TOP5_CEIL = 0.50      # sealed


def load():
    kg = json.load(open(os.path.join(ROOT, "frontier", "B738_pathfinder_compiler",
                                     "kill_graph.json"), encoding="utf-8"))
    atlas = json.load(open(os.path.join(ROOT, "scripts", "atlas", "atlas_data.json"),
                          encoding="utf-8"))["probes"]
    faces = {r["id"]: [f for f in r["faces_consulted"] if f != "none"] for r in kg}
    motifs = {k: v.get("motifs", []) for k, v in atlas.items()}
    return faces, motifs


def joint(faces, motifs):
    pairs = Counter()
    both = 0
    for aid, fs in faces.items():
        ms = motifs.get(aid) or []
        if not fs or not ms:
            continue
        both += 1
        for f in fs:
            for m in ms:
                pairs[(f, m)] += 1
    return pairs, both


def mutual_information(pairs):
    """Normalised I(face; motif) / min(H(face), H(motif)). Corroborator, not the criterion."""
    tot = sum(pairs.values())
    if not tot:
        return 0.0
    pf, pm = Counter(), Counter()
    for (f, m), c in pairs.items():
        pf[f] += c
        pm[m] += c
    I = 0.0
    for (f, m), c in pairs.items():
        pxy = c / tot
        I += pxy * math.log2(pxy / ((pf[f] / tot) * (pm[m] / tot)))
    Hf = -sum((c / tot) * math.log2(c / tot) for c in pf.values())
    Hm = -sum((c / tot) * math.log2(c / tot) for c in pm.values())
    return I / min(Hf, Hm) if min(Hf, Hm) > 0 else 0.0


def observer_spread(faces, motifs):
    """Is `observer` a THIRD axis (cuts across) or a missing member of one vocabulary?"""
    fdir = os.path.join(ROOT, "frontier")
    hits = []
    for d in sorted(os.listdir(fdir)):
        fp = os.path.join(fdir, d, "FINDINGS.md")
        if not os.path.isfile(fp):
            continue
        import re
        m = re.match(r"(B\d+)[a-zA-Z]?_", d)
        if not m:
            continue
        if re.search(r"\bobserver\b", open(fp, encoding="utf-8").read(), re.I):
            hits.append(m.group(1))
    fc, mc = Counter(), Counter()
    for a in hits:
        for f in faces.get(a, []):
            fc[f] += 1
        for mo in motifs.get(a, []):
            mc[mo] += 1
    return hits, fc, mc


def main():
    faces, motifs = load()
    pairs, both = joint(faces, motifs)
    P = len(pairs)
    tot = sum(pairs.values())
    top5 = sum(c for _, c in pairs.most_common(5)) / tot if tot else 1.0
    nmi = mutual_information(pairs)

    print("=" * 78)
    print("B807 — the joint distribution of (face, motif)")
    print("=" * 78)
    print(f"\n  arcs carrying BOTH a face and a motif : {both}")
    print(f"  populated (face, motif) pairs P       : {P}  of 11 x 18 = 198 possible")
    print(f"  share carried by the top 5 pairs      : {top5:.3f}")
    print(f"  normalised mutual information         : {nmi:.3f}   (corroborator only)")

    spread = (P >= P_FLOOR) and (top5 <= TOP5_CEIL)
    conc = (P < P_FLOOR) or (top5 > TOP5_CEIL)
    verdict = "SPREAD" if spread else ("CONCENTRATED" if conc else "AMBIGUOUS")
    if spread and conc:
        verdict = "AMBIGUOUS"
    print(f"\n  sealed thresholds: P >= {P_FLOOR} AND top5 <= {TOP5_CEIL}")
    print(f"  P >= {P_FLOOR}      : {P >= P_FLOOR}")
    print(f"  top5 <= {TOP5_CEIL} : {top5 <= TOP5_CEIL}")
    print(f"\n  VERDICT: {verdict}")
    print("  " + ("=> ORTHOGONAL AXES (WHERE x WHAT). Declare the two-layer structure."
                  " DO NOT MERGE -- merging would destroy information."
                  if verdict == "SPREAD" else
                  "=> REDUNDANT LABELS. Merge into one vocabulary."
                  if verdict == "CONCENTRATED" else
                  "=> AMBIGUOUS. Neither action taken, per prereg section 2."))

    print(f"\n  the 8 commonest pairs:")
    for (f, m), c in pairs.most_common(8):
        print(f"    {f:22} x {m:18} {c:>4}")

    hits, fc, mc = observer_spread(faces, motifs)
    print(f"\n  OBSERVER — third axis, or missing member?")
    print(f"    arcs mentioning it        : {len(hits)}")
    print(f"    distinct faces they touch : {len(fc)} of 11   {dict(fc.most_common(5))}")
    print(f"    distinct motifs they touch: {len(mc)} of 18   {dict(mc.most_common(5))}")
    broad = len(fc) >= 4 and len(mc) >= 6
    print(f"    => {'THIRD AXIS (cuts across both)' if broad else 'MISSING MEMBER of one vocabulary'}")

    json.dump({"both": both, "P": P, "top5": top5, "nmi": nmi, "verdict": verdict,
               "pairs": {f"{f}|{m}": c for (f, m), c in pairs.items()},
               "observer": {"arcs": len(hits), "faces": dict(fc), "motifs": dict(mc),
                            "third_axis": broad}},
              open(os.path.join(os.path.dirname(__file__), "joint.json"), "w"), indent=1)
    return verdict


if __name__ == "__main__":
    main()
