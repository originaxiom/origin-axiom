#!/usr/bin/env python3
"""B739 Stage-B recompute -- TOMB-L310 (the causal-set poset reading, probation P20 / firewalled L21).

BANKED KILL (TOMBSTONES.md L310-313, citing B159; per the Stage-A citation-chain check the actual
computation lives in B189 omega_causal_dimension.py): the Omega strict-full class DAG (B156/B159,
levels L4-L10, N=474 classes) has a Myrheim-Meyer dimension that is NOT manifoldlike -- the
d_MM ~ 3.94 is a generic graded-DAG / truncation artifact; no emergent spacetime /
causal-set-gravity signal.

THE DISCRIMINATING FACT (identified per E19): NOT the raw d_MM value (alone, d_MM ~ 3.94 would
READ as "manifoldlike 4D"!) but the artifact diagnosis that defeats it:
  (F1) TRUNCATION DRIFT -- d_MM rises monotonically with included depth (banked: L<=6..10 gives
       2.08 -> 2.70 -> 3.28 -> 3.63 -> 3.94), never converging: the value tracks the number of
       layers. A genuine sprinkling's d_MM is STABLE as the sample grows (computed here as the
       direct contrast, S2 -- a check the original arc did not run).
  (F2) NULL CONTROL -- a RANDOM graded DAG with the same per-level node counts and the same
       consecutive-level edge counts gives d_MM of the same order (~3.8), with Omega sitting
       significantly ABOVE the null (sparser transitive reach / more tree-like = even LESS
       manifoldlike than noise of its shape).
If F1 and F2 recompute true (with the estimator verified correct on genuine Lorentzian
sprinklings, else the diagnosis is vacuous), the kill is RECONFIRMED. If d_MM converged under
truncation, or Omega matched a sprinkling profile rather than the layered null, REVIVED.

E19 COMPUTE-NOT-CITE: independent re-derivation -- own Meyer closed form with exact rational
anchors, own vectorized rejection-sampled Minkowski-diamond calibration (own seed) PLUS the
stability-under-N contrast, own iterative bitset transitive closure (B189 used recursive
set-union), own bisection inversion, own null sampler in TWO declared variants with FRESH seeds.
Input data: ONLY the banked B159 CSVs (independently verified in B159 by from-scratch
re-enumeration at L4-L7); their declared structure is re-verified here before use.

DECLARED CONVENTIONS (E1 -- the arc's where declared, re-declared or chosen where implicit):
 1. Ordering fraction, DIRECTED-pair convention (declared in B189): r = |{(u,v): u < v strictly}|
    / (N(N-1)). Meyer closed form under this convention f(d) = Gamma(d+1)Gamma(d/2)/(4 Gamma(3d/2));
    exact anchors f(2)=1/4, f(4)=1/20; calibrated on sprinklings rather than trusted.
 2. Poset = transitive closure of the B159 class-DAG accretion edges, unweighted (declared in
    B189; the history-multiplicity-weighted poset is B189's declared not-run variant).
 3. d_MM = the unique d in [1.5, 8] with f(d) = r (f strictly decreasing; bisection, 60 steps --
    B189's bracket, re-declared).
 4. Null model (B189 FINDINGS wording: "same level sizes ... same consecutive-level edge counts"):
    B189's implementation drew m (source,target) pairs uniformly WITH replacement into a set, so
    duplicates COLLAPSE (realized distinct edges <= m) -- an UNDECLARED implementation convention.
    Both variants are run and declared here:
      variant A (collapse): m uniform draws with replacement, duplicates collapsed (B189's model);
      variant B (exact):    exactly m DISTINCT uniform pairs per consecutive level pair.
    30 seeds each. CHOSEN here: numpy default_rng seeds 101..130 -- deliberately NOT B189's 0..29,
    to demonstrate seed-independence of the verdict (draw order differs anyway).
 5. "sigma" = (d_Omega - mean_null)/std_null with std_null the POPULATION std (ddof=0) over the
    30 seeds -- the spread convention behind the banked "~12 sigma".
 6. Sprinkling: causal diamond between (0,vec0) and (1,vec0) in d-dim Minkowski; rejection
    sampling t~U(0,1), x~U(-1,1)^(d-1), accept iff |x| < min(t,1-t); relation i<j iff t_j > t_i
    and (t_j-t_i)^2 > |x_j-x_i|^2. CHOSEN: seed 42; N=250 x 4 trials for the closed-form match;
    stability check in d=4 at N in {100,200,400} (3 trials each).
Deterministic: fixed seeds only; no wall-clock; no network. Gate 5: combinatorial/geometric
mathematics only -- no SM quantity anywhere.
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
B159 = os.path.normpath(os.path.join(HERE, "..", "..", "..", "B159_omega_class_dag"))

ok = True
def check(name, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

# ---------------------------------------------------------------- Meyer form
def meyer_f(d):
    """Expected directed-pair ordering fraction of a d-dim Minkowski causal-diamond sprinkling."""
    return math.gamma(d + 1) * math.gamma(d / 2) / (4.0 * math.gamma(1.5 * d))

def d_mm(r, lo=1.5, hi=8.0):
    """Invert the strictly decreasing Meyer form by bisection (60 steps on [1.5, 8])."""
    if r >= meyer_f(lo):
        return lo
    if r <= meyer_f(hi):
        return hi
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if meyer_f(mid) > r:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

print("== S0: Meyer closed form -- exact rational anchors (independent of any sampling) ==")
print(f"   f(2) = {meyer_f(2):.10f}  (exact: Gamma(3)Gamma(1)/(4 Gamma(3)) = 1/4)")
print(f"   f(4) = {meyer_f(4):.10f}  (exact: Gamma(5)Gamma(2)/(4 Gamma(6)) = 24/480 = 1/20)")
check("S0 exact anchors f(2)=1/4, f(4)=1/20", abs(meyer_f(2) - 0.25) < 1e-12 and abs(meyer_f(4) - 0.05) < 1e-12)

# ------------------------------------------------- sprinkling calibration
def diamond_sprinkle_r(d, n_pts, n_trials, rng):
    """Directed ordering fraction of n_pts uniform points in a d-dim causal diamond (vectorized)."""
    fracs = []
    for _ in range(n_trials):
        ts = np.empty(n_pts)
        xs = np.empty((n_pts, d - 1))
        have = 0
        while have < n_pts:
            batch = 4 * (n_pts - have) + 16
            t = rng.random(batch)
            x = rng.uniform(-1.0, 1.0, size=(batch, d - 1))
            acc = np.linalg.norm(x, axis=1) < np.minimum(t, 1.0 - t)
            take = min(int(acc.sum()), n_pts - have)
            ts[have:have + take] = t[acc][:take]
            xs[have:have + take] = x[acc][:take]
            have += take
        dt = ts[None, :] - ts[:, None]                       # dt[i,j] = t_j - t_i
        dx2 = ((xs[None, :, :] - xs[:, None, :]) ** 2).sum(axis=2)
        related = (dt > 0) & (dt ** 2 > dx2)
        fracs.append(related.sum() / (n_pts * (n_pts - 1)))
    return float(np.mean(fracs))

rng = np.random.default_rng(42)
print("\n== S1: estimator calibrated on ground truth (Minkowski diamond sprinklings, seed 42) ==")
cal_ok = True
for d in (2, 3, 4):
    r_s = diamond_sprinkle_r(d, 250, 4, rng)
    cal_ok = cal_ok and abs(r_s - meyer_f(d)) < 0.02
    print(f"   d={d}: sprinkled r = {r_s:.4f}   Meyer f(d) = {meyer_f(d):.4f}   d_MM = {d_mm(r_s):.3f}")
check("S1 sprinkled r matches the Meyer closed form to <0.02 for d=2,3,4 "
      "(the estimator MEANS a dimension on ground truth)", cal_ok)

print("\n== S2: on ground truth d_MM is STABLE as the sample grows -- the property Omega must match ==")
stab = []
for n_pts in (100, 200, 400):
    r_s = diamond_sprinkle_r(4, n_pts, 3, rng)
    stab.append(d_mm(r_s))
    print(f"   d=4 sprinkling, N={n_pts:3d}: r = {r_s:.4f}   d_MM = {stab[-1]:.3f}")
spread = max(stab) - min(stab)
check("S2 sprinkling d_MM spread over a 4x sample-size range is < 0.35 (converged; no drift)",
      spread < 0.35, detail=f"spread = {spread:.3f}")

# ------------------------------------------------- load + re-verify the B159 DAG
print("\n== S3: load the banked B159 class DAG; re-verify its declared structure before use ==")
node_level = {}
with open(os.path.join(B159, "omega_strict_full_class_nodes_L4_L10.csv")) as fh:
    for row in csv.DictReader(fh):
        node_level[row["id"]] = int(row["level"])
names = sorted(node_level)                     # own canonical node order (lexicographic id)
index = {nm: k for k, nm in enumerate(names)}
lev = [node_level[nm] for nm in names]
N = len(names)
edges = []
nonconsec = 0
with open(os.path.join(B159, "omega_strict_full_class_edges_L4_L10.csv")) as fh:
    for row in csv.DictReader(fh):
        u, v = index[row["source"]], index[row["target"]]
        edges.append((u, v))
        if lev[v] != lev[u] + 1:
            nonconsec += 1
sizes = {}
for L in lev:
    sizes[L] = sizes.get(L, 0) + 1
print(f"   N = {N} nodes; {len(edges)} edges; level sizes " +
      ", ".join(f"L{L}:{sizes[L]}" for L in sorted(sizes)))
check("S3a N = 474 classes with per-level counts 1,2,6,18,49,115,283 (the B159 table)",
      N == 474 and [sizes[L] for L in sorted(sizes)] == [1, 2, 6, 18, 49, 115, 283])
check("S3b every edge is strictly graded (level L -> L+1), so the null's consecutive-level "
      "edge-count constraint captures ALL edges", nonconsec == 0,
      detail=f"non-consecutive edges: {nonconsec}")

# ------------------------------------------------- own transitive closure (bitsets)
def ordering_fraction(node_ids, edge_list):
    """r = (# ordered comparable pairs)/(n(n-1)) via iterative bitset closure, levels top-down."""
    keep = set(node_ids)
    succ = [[] for _ in range(N)]
    for u, v in edge_list:
        if u in keep and v in keep:
            succ[u].append(v)
    reach = {}
    for u in sorted(keep, key=lambda w: -lev[w]):   # descending level: successors always done first
        acc = 0
        for v in succ[u]:
            acc |= (1 << v) | reach[v]
        reach[u] = acc
    rel = sum(r.bit_count() for r in reach.values())
    n = len(keep)
    return rel / (n * (n - 1)), n

# ------------------------------------------------- F1: raw number + truncation drift
print("\n== S4 (F1): Omega d_MM by truncation level -- the DRIFT half of the discriminating fact ==")
dseq = []
for Lmax in (6, 7, 8, 9, 10):
    ids = [u for u in range(N) if lev[u] <= Lmax]
    r_t, n_t = ordering_fraction(ids, edges)
    dseq.append(d_mm(r_t))
    print(f"   L4..L{Lmax}: n={n_t:3d}  r = {r_t:.5f}  d_MM = {dseq[-1]:.3f}")
r_full, _ = ordering_fraction(range(N), edges)
d_full = d_mm(r_full)
banked_seq = [2.08, 2.70, 3.28, 3.63, 3.94]
check("S4a raw number: full poset r ~ 0.053 -> d_MM ~ 3.94 ('suspiciously close to 4')",
      abs(r_full - 0.053) < 0.002 and 3.5 < d_full < 4.3,
      detail=f"r = {r_full:.5f}, d_MM = {d_full:.3f}")
check("S4b banked truncation sequence (2.08, 2.70, 3.28, 3.63, 3.94) reproduced to <0.05 each",
      all(abs(a - b) < 0.05 for a, b in zip(dseq, banked_seq)),
      detail="recomputed: " + ", ".join(f"{x:.2f}" for x in dseq))
gaps = [dseq[i + 1] - dseq[i] for i in range(len(dseq) - 1)]
check("S4c DRIFT: d_MM strictly increases with depth and the final step is still large (> 0.2): "
      "NO convergence -- contrast S2's ground-truth stability",
      all(g > 0 for g in gaps) and gaps[-1] > 0.2,
      detail="steps = " + ", ".join(f"+{g:.2f}" for g in gaps) +
             f"; total drift {dseq[-1] - dseq[0]:.2f} vs sprinkling spread {spread:.3f}")

# ------------------------------------------------- F2: null control
consec = {}
for u, v in edges:
    consec[(lev[u], lev[v])] = consec.get((lev[u], lev[v]), 0) + 1
by_level = {L: [u for u in range(N) if lev[u] == L] for L in sorted(sizes)}

def null_d(seed, variant):
    g = np.random.default_rng(seed)
    e = set()
    for (La, Lb) in sorted(consec):
        m = consec[(La, Lb)]
        A, B = by_level[La], by_level[Lb]
        if variant == "collapse":       # B189's implementation: with replacement, set-collapsed
            si = g.integers(0, len(A), size=m)
            ti = g.integers(0, len(B), size=m)
            for a, b in zip(si, ti):
                e.add((A[int(a)], B[int(b)]))
        else:                           # exact: m distinct uniform pairs
            flat = g.choice(len(A) * len(B), size=m, replace=False)
            for f in flat:
                e.add((A[int(f) // len(B)], B[int(f) % len(B)]))
    r_n, _ = ordering_fraction(range(N), list(e))
    return d_mm(r_n)

print("\n== S5 (F2): null control -- random graded DAGs of the SAME shape "
      "(30 fresh seeds 101..130, two declared variants) ==")
for variant in ("collapse", "exact"):
    ds = np.array([null_d(s, variant) for s in range(101, 131)])
    mu, sd = float(np.mean(ds)), float(np.std(ds))          # population std (ddof=0), declared
    z = (d_full - mu) / sd
    print(f"   variant {variant:8s}: null d_MM = {mu:.3f} +/- {sd:.3f}   Omega = {d_full:.3f}   "
          f"gap = {d_full - mu:+.3f}  ({z:.1f} null-sigma)")
    if variant == "collapse":
        check("S5a (collapse = the B189 model): null mean in [3.7, 3.9], std < 0.03 -- the SAME "
              "ORDER as Omega's ~3.94: a '~4' is generic layering, not geometry",
              3.7 < mu < 3.9 and sd < 0.03, detail=f"null = {mu:.3f} +/- {sd:.3f}")
        check("S5b Omega sits ABOVE the null by ~0.1-0.3 at > 5 null-sigma (sparser transitive "
              "reach / more tree-like => even LESS manifoldlike; banked ~12 sigma)",
              0.05 < d_full - mu < 0.3 and z > 5, detail=f"gap = {d_full - mu:.3f}, z = {z:.1f}")
    else:
        check("S5c (exact-distinct variant): same qualitative verdict -- the undeclared collapse "
              "convention is NOT load-bearing",
              3.4 < mu < 4.2 and d_full > mu and z > 5, detail=f"z = {z:.1f}")

# ------------------------------------------------- verdict
print("\n== VERDICT (TOMB-L310 discriminating fact, recomputed independently) ==")
print(f"   The Omega strict-full class poset's d_MM = {d_full:.3f} is NOT a dimension:")
print(f"   (F1) it DRIFTS {dseq[0]:.2f} -> {dseq[-1]:.2f} with truncation depth, never converging,")
print(f"        while a genuine d=4 sprinkling holds d_MM to a {spread:.3f} spread over a 4x")
print("        sample-size range; and")
print("   (F2) a random graded DAG of identical layer profile gives the same order (~3.8) under")
print("        BOTH declared null variants, with Omega significantly ABOVE the null -- even LESS")
print("        manifoldlike than noise of its shape.")
print("   A graded 7-layer DAG is not a Lorentzian sprinkling; the '~4' is generic layering.")
print("   No emergent spacetime / causal-set-gravity signal. The banked kill is upheld.")
print("   Combinatorial mathematics only; no physics quantity; Gate 5 clean.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
sys.exit(0 if ok else 1)
