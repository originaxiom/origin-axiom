#!/usr/bin/env python3
"""B808 — margin-preserving permutation null for the empty (face, motif) cells.
Prereg 68d1aef066a0f555. Thresholds sealed and not adjustable here."""
import json, os, random
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NPERM, P_ARTIFACT, VACUOUS_N, SUBSTANTIVE_N = 10000, 0.10, 30, 6   # sealed


def load():
    kg = json.load(open(os.path.join(ROOT, "frontier", "B738_pathfinder_compiler",
                                     "kill_graph.json"), encoding="utf-8"))
    at = json.load(open(os.path.join(ROOT, "scripts", "atlas", "atlas_data.json"),
                        encoding="utf-8"))["probes"]
    rows = []
    for r in kg:
        fs = [f for f in r["faces_consulted"] if f != "none"]
        ms = (at.get(r["id"]) or {}).get("motifs", [])
        if fs and ms:
            rows.append((fs, ms))
    return rows


def cells(rows):
    s = set()
    for fs, ms in rows:
        for f in fs:
            for m in ms:
                s.add((f, m))
    return s


def main():
    rows = load()
    face_pool = [f for fs, _ in rows for f in fs]
    motif_pool = [m for _, ms in rows for m in ms]
    FACES, MOTIFS = sorted(set(face_pool)), sorted(set(motif_pool))
    obs = cells(rows)
    allc = [(f, m) for f in FACES for m in MOTIFS]
    empty = [c for c in allc if c not in obs]
    print("=" * 78); print("B808 — the empty-cell null test"); print("=" * 78)
    print(f"\n  arcs with both labels {len(rows)} | cells {len(allc)} | populated {len(obs)} "
          f"| EMPTY {len(empty)}")

    rng = random.Random(808)
    empty_count = Counter()
    face_full = Counter()
    for _ in range(NPERM):
        perm = []
        for fs, ms in rows:
            perm.append((rng.sample(face_pool, len(fs)), rng.sample(motif_pool, len(ms))))
        pc = cells(perm)
        for c in empty:
            if c not in pc:
                empty_count[c] += 1
        for f in FACES:
            if all((f, m) in pc for m in MOTIFS):
                face_full[f] += 1

    art, real = [], []
    for c in empty:
        p = empty_count[c] / NPERM
        (art if p >= P_ARTIFACT else real).append((c, p))
    print(f"\n  sealed: ARTIFACT if p_empty >= {P_ARTIFACT};  VACUOUS if >= {VACUOUS_N} artifact;"
          f"  SUBSTANTIVE if >= {SUBSTANTIVE_N} real")
    print(f"  ARTIFACT {len(art)}   REAL GAP {len(real)}")
    verdict = ("VACUOUS" if len(art) >= VACUOUS_N else
               "SUBSTANTIVE" if len(real) >= SUBSTANTIVE_N else "MIXED")
    print(f"\n  VERDICT: {verdict}")
    if real:
        print(f"\n  REAL GAPS (emptier than chance):")
        for (f, m), p in sorted(real, key=lambda x: x[1]):
            print(f"    {f:24} x {m:20} p_empty={p:.4f}")
    print(f"\n  §4 — is motif-completeness of the large faces surprising?")
    arcs_per_face = Counter(f for fs, _ in rows for f in fs)
    for f in sorted(FACES, key=lambda x: -arcs_per_face[x])[:5]:
        n_empty = sum(1 for m in MOTIFS if (f, m) not in obs)
        print(f"    {f:24} arcs={arcs_per_face[f]:4}  empty={n_empty:2}  "
              f"p_full(null)={face_full[f]/NPERM:.4f}"
              f"{'   <- complete, and RARE under the null' if n_empty==0 and face_full[f]/NPERM<0.05 else ''}")
    json.dump({"verdict": verdict, "artifact": len(art), "real": len(real),
               "real_gaps": [[list(c), p] for c, p in real],
               "p_full": {f: face_full[f] / NPERM for f in FACES}},
              open(os.path.join(os.path.dirname(__file__), "null_test.json"), "w"), indent=1)
    return verdict


if __name__ == "__main__":
    main()
