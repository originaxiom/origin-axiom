#!/usr/bin/env python3
"""B1239 — is the 1/4 class a CUSP phenomenon?  (R040 sharpened; L194's mechanism)

Claim under test (derived on the bench from CGHN p.14/p.15, read):
  APS:  3*eta(M) = 2*cs(M) + tau  (mod 2), tau = # of 2-primary summands of H_1(M;Z), M CLOSED.
  eta(M) = 0 for ANY closed M with an orientation-reversing isometry (spectral symmetry; freeness
  irrelevant).  tau is an integer.  Hence 2*cs in Z, cs in {0, 1/2} mod 1, i.e. cs == 0 mod 1/2.
  => CLOSED amphichiral hyperbolic manifolds never show the 1/4 class.  Kawauchi is not needed
  for that; it only decides 0 vs 1/2 mod 1, which SnapPy's mod-1/2 readout cannot see anyway.

Bite control: CUSPED amphichiral manifolds DO show 1/4 (L194: 16/44 of the 112-family), so the
prediction is falsifiable and the test discriminates closed from cusped.

Test 1 (closed): OrientableClosedCensus[:N_CLOSED]; amphichiral iff M ~ mirror(M).
  Prediction: quarter class = 0 among the amphichiral ones.  Report chiral ones' classes too
  (no prediction there; if THOSE never show 1/4 either the test would be vacuous — check).
Test 2 (cusped, the same detector): OrientableCuspedCensus with >= 1 cusp, first N_CUSPED;
  amphichiral ones' quarter rate must be > 0 or the detector is blind.
"""
import json, sys, time
import snappy

N_CLOSED = int(sys.argv[1]) if len(sys.argv) > 1 else 11031
N_CUSPED = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
TOL = 1e-6

def cls(cs):
    """class of cs in R/(1/2)Z: distance to 0 and to 1/4, both mod 1/2."""
    x = cs % 0.5
    d0 = min(x, 0.5 - x)
    dq = abs(x - 0.25)
    if d0 < TOL: return "zero", d0
    if dq < TOL: return "quarter", dq
    return "other", min(d0, dq)

def is_amphichiral(M):
    """B1235's detector.  NOT is_isometric_to(M, mirror) -- that call is orientation-blind (it said
    5_2 ~ mirror(5_2)); symmetry_group() canonizes and classifies by orientation.  Validated here
    against is_isometric_to(M, M, return_isometries=True) cusp-map determinants on 600/600."""
    try:
        return M.symmetry_group().is_amphicheiral()
    except Exception:
        return None

def closed_cs(M):
    """Closed census entries answer 'isn't currently known' to a direct chern_simons(); the kernel
    needs the cusped parent's value first (the same route the 17-cover control used)."""
    P = M.copy(); fill = [tuple(c["filling"]) for c in P.cusp_info()]
    P.dehn_fill([(0, 0)] * P.num_cusps()); P.chern_simons(); P.dehn_fill(fill)
    return float(P.chern_simons())

out = {"tol": TOL, "closed": {}, "cusped": {}}
t0 = time.time()

# ---- Test 1: closed ------------------------------------------------------------------------
tab = {"amphichiral": {"zero": 0, "quarter": 0, "other": 0}, "chiral": {"zero": 0, "quarter": 0, "other": 0}}
undecided = 0; cs_fail = 0; maxd = {"amphichiral": 0.0, "chiral": 0.0}
examples = {"amphichiral_quarter": [], "chiral_quarter": [], "amphichiral_zero": []}
for i, M in enumerate(snappy.OrientableClosedCensus[:N_CLOSED]):
    a = is_amphichiral(M)
    if a is None:
        undecided += 1; continue
    try:
        cs = closed_cs(M)
    except Exception:
        cs_fail += 1; continue
    c, d = cls(cs)
    key = "amphichiral" if a else "chiral"
    tab[key][c] += 1
    if c != "other": maxd[key] = max(maxd[key], d)
    if key == "amphichiral" and c == "quarter": examples["amphichiral_quarter"].append((M.name(), cs))
    if key == "chiral" and c == "quarter" and len(examples["chiral_quarter"]) < 5: examples["chiral_quarter"].append((M.name(), cs))
    if key == "amphichiral" and c == "zero" and len(examples["amphichiral_zero"]) < 5: examples["amphichiral_zero"].append((M.name(), cs))
    if i % 500 == 0:
        print(f"[closed {i}] {tab}  undecided={undecided} cs_fail={cs_fail}  t={time.time()-t0:.0f}s", flush=True)
out["closed"] = {"n": N_CLOSED, "table": tab, "undecided": undecided, "cs_fail": cs_fail,
                 "max_dist_in_class": maxd, "examples": examples}
print("CLOSED:", json.dumps(out["closed"], indent=1), flush=True)

# ---- Test 2: cusped, same detector --------------------------------------------------------
tab2 = {"amphichiral": {"zero": 0, "quarter": 0, "other": 0}, "chiral": {"zero": 0, "quarter": 0, "other": 0}}
und2 = 0
by_cusps = {}
for i, M in enumerate(snappy.OrientableCuspedCensus[:N_CUSPED]):
    a = is_amphichiral(M)
    if a is None:
        und2 += 1; continue
    cs = M.chern_simons()
    c, d = cls(cs)
    key = "amphichiral" if a else "chiral"
    tab2[key][c] += 1
    k = M.num_cusps()
    by_cusps.setdefault(k, {"amphichiral": {"zero": 0, "quarter": 0, "other": 0}, "chiral": {"zero": 0, "quarter": 0, "other": 0}})
    by_cusps[k][key][c] += 1
    if i % 500 == 0:
        print(f"[cusped {i}] {tab2}  undecided={und2}  t={time.time()-t0:.0f}s", flush=True)
out["cusped"] = {"n": N_CUSPED, "table": tab2, "undecided": und2, "by_num_cusps": by_cusps}
print("CUSPED:", json.dumps(out["cusped"], indent=1), flush=True)

# ---- verdict ------------------------------------------------------------------------------
closed_amph_quarter = tab["amphichiral"]["quarter"]
cusped_amph_quarter = tab2["amphichiral"]["quarter"]
out["verdict"] = {
    "closed_amphichiral_quarter": closed_amph_quarter,
    "closed_amphichiral_total": sum(tab["amphichiral"].values()),
    "closed_chiral_quarter": tab["chiral"]["quarter"],
    "cusped_amphichiral_quarter": cusped_amph_quarter,
    "cusped_amphichiral_total": sum(tab2["amphichiral"].values()),
    "prediction_holds": closed_amph_quarter == 0,
    "detector_bites": cusped_amph_quarter > 0,
}
print("VERDICT:", json.dumps(out["verdict"], indent=1))
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1)
print(f"done in {time.time()-t0:.0f}s")
