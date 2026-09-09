#!/usr/bin/env python3
"""B1239 — the equivariant-filling corollary, bite-tested.

COROLLARY (derived on the bench; inputs: CGHN p.14 filling decomposition + analyticity of the
non-torsion term, Thurston hyperbolic Dehn filling, APS relation + spectral symmetry for closed
manifolds — all read/standard, none ours):
  If cusped orientable hyperbolic M admits an orientation-reversing isometry t with t(c) != c for
  EVERY cusp c (t fixes no cusp setwise), then cs(M) == 0 mod 1/2 (the 1/4 class is excluded).
  Proof sketch: fill (c, t(c)) with (s, t(s)); t extends to the closed M'_s (orientation-reversing)
  so cs(M'_s) in (1/2)Z; the two added core geodesics are swapped by t with torsions theta, -theta
  (exact cancellation); the analytic term at s is therefore in (1/2)Z, and it tends to cs(M) as
  s -> infinity.  Continuity + discreteness => cs(M) in (1/2)Z.
  If t fixes some cusp, only two t-invariant slopes exist there: no limit argument.  NO PREDICTION.

Buckets over multi-cusped census manifolds:
  A: some orientation-reversing self-isometry fixes no cusp   -> PREDICTED zero class, always
  B: amphichiral but every reversing isometry fixes a cusp     -> no prediction
  C: chiral                                                     -> no prediction
Bite: A must be 0 quarter; B or C should contain quarter cases (else the detector is blind here).
"""
import json, sys, time
import snappy
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
TOL = 1e-6

def cls(cs):
    x = cs % 0.5; d0 = min(x, 0.5 - x); dq = abs(x - 0.25)
    return ("zero" if d0 < TOL else "quarter" if dq < TOL else "other"), min(d0, dq)

def reversing_isos(M):
    """All self-isometries (canonical triangulation; validated = symmetry_group().order() on 600/600),
    kept if orientation-reversing = cusp-map determinant -1 (consistent across cusps, checked).
    isomorphisms_to() is NOT used: it does not canonize (m006: 2 of 4)."""
    try:
        isos = M.is_isometric_to(M, return_isometries=True)
    except Exception:
        return None
    return [i for i in isos if round(i.cusp_maps()[0].det()) == -1]

t0 = time.time()
buckets = {"A": {"zero": 0, "quarter": 0, "other": 0}, "B": {"zero": 0, "quarter": 0, "other": 0}, "C": {"zero": 0, "quarter": 0, "other": 0}}
examples = {"A": [], "B_quarter": [], "C_quarter": []}
undecided = 0; seen = 0; maxdA = 0.0
by_cusps = {}
for i, M in enumerate(snappy.OrientableCuspedCensus[:N]):
    k = M.num_cusps()
    if k < 2: continue
    seen += 1
    isos = reversing_isos(M)
    if isos is None:
        undecided += 1; continue
    if len(isos) == 0:
        b = "C"
    else:
        free = [iso for iso in isos if all(iso.cusp_images()[j] != j for j in range(k))]
        b = "A" if free else "B"
    cs = M.chern_simons(); c, d = cls(cs)
    buckets[b][c] += 1
    by_cusps.setdefault(k, {"A": {"zero": 0, "quarter": 0, "other": 0}, "B": {"zero": 0, "quarter": 0, "other": 0}, "C": {"zero": 0, "quarter": 0, "other": 0}})
    by_cusps[k][b][c] += 1
    if b == "A":
        maxdA = max(maxdA, d)
        if len(examples["A"]) < 12: examples["A"].append((M.name(), k, cs, c, [iso.cusp_images() for iso in free][:2]))
    if b == "B" and c == "quarter" and len(examples["B_quarter"]) < 8: examples["B_quarter"].append((M.name(), k, cs))
    if b == "C" and c == "quarter" and len(examples["C_quarter"]) < 5: examples["C_quarter"].append((M.name(), k, cs))
    if seen % 500 == 0:
        print(f"[{i} seen={seen}] {buckets} undecided={undecided} t={time.time()-t0:.0f}s", flush=True)
out = {"N_scanned": N, "multi_cusped_seen": seen, "undecided": undecided, "buckets": buckets,
       "by_num_cusps": by_cusps, "max_dist_A": maxdA, "examples": examples,
       "verdict": {"A_quarter": buckets["A"]["quarter"], "A_total": sum(buckets["A"].values()),
                   "prediction_holds": buckets["A"]["quarter"] == 0,
                   "detector_bites": (buckets["B"]["quarter"] + buckets["C"]["quarter"]) > 0}}
print(json.dumps(out, indent=1, default=str))
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1, default=str)
print(f"done in {time.time()-t0:.0f}s")
