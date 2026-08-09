"""B1008 — the atlas lexicon's descriptive power is EPOCH-SPECIFIC, and the tripwire caught it.

WHY THIS RAN
------------
test_b806_lexicon's concentration lock fired: top-3 motif coverage fell to 0.8496, through
the 0.85 floor it defended. B829 set the precedent for this exact tripwire -- when it fires,
RE-DERIVE B806's numbers, do not bump the threshold. This script is the re-derivation.

Usage:  python3 epoch.py
"""
from __future__ import annotations

import glob
import json
import os
import re
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))

BANDS = [(1, 200), (201, 400), (401, 600), (601, 800), (801, 900), (901, 1010)]

# The concepts the B800+ corpus is demonstrably about. Chosen from the campaign's own
# vocabulary (the SM-structure cascade, the value layer, the spectral work) BEFORE counting,
# so the list is not fitted to the result.
CONCEPTS = {
    "the_27": r"\b27\b", "e6": r"\bE6\b|\be6\b|E₆", "chirality": r"chiral",
    "measurement": r"measurement", "rank": r"\brank\b", "generation": r"generation",
    "cascade": r"\bcascade", "centralizer": r"centraliz", "observer": r"observer",
    "hypercharge": r"hypercharge", "anomaly": r"anomal", "higgs": r"[Hh]iggs",
    "value_layer": r"value layer", "maass": r"[Mm]aass",
}


def atlas():
    with open(os.path.join(_REPO, "scripts", "atlas", "atlas_data.json")) as fh:
        return json.load(fh)


def _bnum(k):
    m = re.search(r"B(\d+)", k)
    return int(m.group(1)) if m else None


def concentration(A):
    """B806's headline statistic, recomputed: fraction of probes carrying a top-3 motif."""
    P = A["probes"]
    mot = Counter(m for v in P.values() for m in v.get("motifs", []))
    top3 = {m for m, _ in mot.most_common(3)}
    cov = sum(1 for v in P.values() if set(v.get("motifs", [])) & top3) / len(P)
    return cov, top3, len(P)


def by_epoch(A):
    """The discriminating table: is recent work UNDER-LABELLED or merely DIFFERENTLY labelled?"""
    P = A["probes"]
    _, top3, _ = concentration(A)
    out = []
    for lo, hi in BANDS:
        sel = [v for k, v in P.items() if (b := _bnum(k)) and lo <= b <= hi]
        if not sel:
            continue
        out.append({
            "band": f"B{lo}-{hi}", "n": len(sel),
            "top3_cov": sum(1 for v in sel if set(v.get("motifs", [])) & top3) / len(sel),
            "any_motif": sum(1 for v in sel if v.get("motifs")) / len(sel),
            "motifs_per_probe": sum(len(v.get("motifs", [])) for v in sel) / len(sel),
            "local_top3": [m for m, _ in Counter(
                m for v in sel for m in v.get("motifs", [])).most_common(3)],
        })
    return out


def vocabulary_gap(A):
    """How many of the recent corpus's own concepts have NO word in the frozen lexicon."""
    lex = set(A["lexicon"])
    verdicts = []
    for f in glob.glob(os.path.join(_REPO, "frontier", "*", "arc_verdict.json")):
        try:
            with open(f) as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        m = re.search(r"B(\d+)", d.get("id", "") or "")
        if m and int(m.group(1)) >= 800:
            verdicts.append(d.get("claim_one_line", ""))
    rows = []
    for name, pat in CONCEPTS.items():
        rx = re.compile(pat)
        rows.append({"concept": name, "arcs": sum(1 for c in verdicts if rx.search(c)),
                     "in_lexicon": name in lex})
    rows.sort(key=lambda r: -r["arcs"])
    return rows, len(verdicts)


def main():
    A = atlas()
    cov, top3, n = concentration(A)
    print(f"CONCENTRATION (B806's statistic, re-derived)")
    print(f"  top-3 = {sorted(top3)}")
    print(f"  coverage = {cov:.4f} over {n} probes   [B806 stated 0.933; B829 re-derived 0.8845]")
    print(f"  the 0.85 floor is BREACHED: {cov:.4f} < 0.85\n")

    print("BY EPOCH -- the discriminating table")
    print(f"  {'band':<12}{'n':>5}{'top3':>8}{'any':>7}{'mot/probe':>11}   local top-3")
    for r in by_epoch(A):
        print(f"  {r['band']:<12}{r['n']:>5}{r['top3_cov']:>8.3f}{r['any_motif']:>7.3f}"
              f"{r['motifs_per_probe']:>11.2f}   {r['local_top3']}")

    rows, tot = vocabulary_gap(A)
    missing = sum(1 for r in rows if not r["in_lexicon"])
    print(f"\nVOCABULARY GAP over {tot} arcs at B800+")
    print(f"  {'concept':<14}{'arcs':>6}{'in lexicon?':>13}")
    for r in rows:
        print(f"  {r['concept']:<14}{r['arcs']:>6}{'YES' if r['in_lexicon'] else 'NO':>13}")
    print(f"\n  {missing}/{len(rows)} of the recent corpus's own concepts have NO word "
          f"in the frozen lexicon.")


if __name__ == "__main__":
    main()
