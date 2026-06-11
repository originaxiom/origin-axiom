"""
B152 — Chern-Simons as a parity order parameter: a census test.

Extends B128 (CS as a chirality/parity order parameter) and B136 (general
amphichirality) with DATA: scan SnapPy's OrientableCuspedCensus[:240] and test
the one-sided law

    amphichiral  =>  CS is 2-torsion   (CS mod 1/2 in {0, 1/4}),

reporting amphichiral count, necessity violations (amphichiral with CS NOT
2-torsion), and converse counterexamples (chiral with CS 2-torsion / CS=0).

Method-bug guard (REPRODUCIBILITY MB / B128): amphichirality MUST be read from
`symmetry_group().is_amphicheiral()` GATED on `is_full_group()`; naive
`is_isometric_to(mirror)` is orientation-blind. CS sign is unsafe (period); we
reduce CS mod 1/2 and test 2-torsion by proximity to {0, 1/4}.

Run:  python frontier/B152_cs_amphichirality_census/probe.py
This is NUMERICAL/census data; nothing promotes to CLAIMS.md.
"""
from __future__ import annotations

import json
import os

import snappy

N = 240
TOL = 1e-6


def _near_mod_half(cs: float, target: float) -> bool:
    """Circular distance of cs to `target`, modulo 1/2 (handles negative cs)."""
    r = cs % 0.5
    return min(abs(r - target), abs(r - target + 0.5), abs(r - target - 0.5)) < TOL


def cs_two_torsion(cs: float) -> bool:
    """Is CS a 2-torsion value: CS mod 1/2 close to 0 or 1/4?"""
    return _near_mod_half(cs, 0.0) or _near_mod_half(cs, 0.25)


def amphichirality(M):
    """Trusted amphichirality, or None if the symmetry group is not full."""
    try:
        G = M.symmetry_group()
    except Exception:
        return None
    try:
        if not G.is_full_group():
            return None
        return bool(G.is_amphicheiral())
    except Exception:
        return None


def scan(n=N):
    rows = []
    for M in snappy.OrientableCuspedCensus[:n]:
        name = M.name()
        amph = amphichirality(M)
        try:
            cs = float(M.chern_simons())
        except Exception:
            cs = None
        rows.append({"name": name, "amphichiral": amph, "cs": cs,
                     "cs_2torsion": (cs_two_torsion(cs) if cs is not None else None)})
    return rows


def summarize(rows):
    amphi = [r for r in rows if r["amphichiral"] is True]
    indet = [r for r in rows if r["amphichiral"] is None]
    # necessity: amphichiral => CS 2-torsion. violation = amphichiral & not 2-torsion
    violations = [r for r in amphi if r["cs_2torsion"] is False]
    # converse counterexamples: chiral but CS == 0 (mod 1/2) -- the strong converse failure
    converse_cs0 = [r for r in rows if r["amphichiral"] is False
                    and r["cs"] is not None and _near_mod_half(r["cs"], 0.0)]
    # for completeness: chiral with CS == 1/4 (the other 2-torsion value)
    chiral_cs_quarter = [r for r in rows if r["amphichiral"] is False
                         and r["cs"] is not None and _near_mod_half(r["cs"], 0.25)]
    return {
        "n_scanned": len(rows),
        "n_amphichiral": len(amphi),
        "amphichiral_names": [r["name"] for r in amphi],
        "n_indeterminate_symgroup": len(indet),
        "necessity_violations": [r["name"] for r in violations],
        "converse_cs0_chiral": [r["name"] for r in converse_cs0],
        "chiral_cs_quarter": [r["name"] for r in chiral_cs_quarter],
    }


def calibration():
    """P9 calibration: m004 (fig-8) CS=0 amphichiral; m003 (sister) CS=1/4."""
    out = {}
    for name, exp_cs in (("m004", 0.0), ("m003", 0.25)):
        M = snappy.Manifold(name)
        out[name] = {"cs": float(M.chern_simons()), "amphichiral": amphichirality(M),
                     "expected_cs_mod_half": exp_cs}
    return out


def main():
    rows = scan()
    summary = summarize(rows)
    cal = calibration()
    result = {"summary": summary, "calibration": cal, "tol": TOL, "N": N}
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "census.json"), "w") as fh:
        json.dump({"result": result, "rows": rows}, fh, indent=1)
    print(json.dumps(result, indent=2))
    print("\nwrote census.json")


if __name__ == "__main__":
    main()
