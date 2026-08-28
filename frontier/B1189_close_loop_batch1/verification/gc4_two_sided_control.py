#!/usr/bin/env python3
"""GC-4 two-sided control for the NEW instrument used on the localization/law claim
(the class-distance vs L10-cone-Jaccard Spearman test). Synthetic 3-level DAG,
20-20-20 nodes, fixed out-degree k=5 per source at each level-pair, each node given a
scalar "position" in [0,1] (stand-in for abc-distance coordinate).

POSITIVE control: wire each source to its 5 nearest-position targets (deliberately
LOCAL wiring) -> the instrument must recover a strong negative Spearman(|dpos|, cone
Jaccard) at level 1 (close positions -> more shared descendants at level 2).

NEGATIVE/exclusion control: wire each source to 5 uniformly random targets (position
plays NO role) -> the instrument must NOT report a significant correlation (|rho| small,
p not tiny) even though the degree sequence is identical to the positive case.
"""
import numpy as np
from scipy import stats as sps

rng = np.random.default_rng(42)
n0, n1, n2, k = 20, 20, 20, 5
pos0 = rng.random(n0); pos1 = rng.random(n1); pos2 = rng.random(n2)

def wire_local(possrc, postgt, k):
    out = [[] for _ in range(len(possrc))]
    for i, p in enumerate(possrc):
        order = np.argsort(np.abs(postgt - p))[:k]
        out[i] = list(order)
    return out

def wire_random(possrc, postgt, k, rng):
    out = [[] for _ in range(len(possrc))]
    for i in range(len(possrc)):
        out[i] = list(rng.choice(len(postgt), size=k, replace=False))
    return out

def cone_and_law(adj01, adj12, pos1):
    # descendant set at level 2 for each level-1 node = direct targets (level 2 has no further edges)
    cones = {u: set(adj12[u]) for u in range(len(pos1))}
    dpos, jac = [], []
    for i in range(len(pos1)):
        for j in range(i+1, len(pos1)):
            a, b = cones[i], cones[j]
            un = len(a | b); it = len(a & b)
            dpos.append(abs(pos1[i]-pos1[j]))
            jac.append(it/un if un else np.nan)
    rho, p = sps.spearmanr(dpos, jac)
    return rho, p

# POSITIVE control: local wiring at BOTH level-pairs
adj01_L = wire_local(pos0, pos1, k)
adj12_L = wire_local(pos1, pos2, k)
rho_pos, p_pos = cone_and_law(adj01_L, adj12_L, pos1)
print(f"[POSITIVE control -- planted locality] Spearman(|dpos|, cone Jaccard) = {rho_pos:.3f}  p={p_pos:.2e}")
print(f"  -> instrument must show STRONG negative rho, tiny p: {'PASS' if rho_pos < -0.3 and p_pos < 1e-4 else 'FAIL'}")

# NEGATIVE/exclusion control: random wiring, same degree sequence (k per source), position irrelevant
rng2 = np.random.default_rng(7)
adj01_R = wire_random(pos0, pos1, k, rng2)
adj12_R = wire_random(pos1, pos2, k, rng2)
rho_neg, p_neg = cone_and_law(adj01_R, adj12_R, pos1)
print(f"\n[NEGATIVE/exclusion control -- random wiring, locality deliberately ABSENT] "
      f"Spearman = {rho_neg:.3f}  p={p_neg:.2e}")
print(f"  -> instrument must NOT report a significant effect (|rho|<0.3 or p>0.01): "
      f"{'PASS' if abs(rho_neg) < 0.3 or p_neg > 0.01 else 'FAIL'}")

# repeat negative control over 20 random seeds to check it doesn't spuriously fire
rhos = []
for s in range(20):
    rr = np.random.default_rng(100+s)
    a01 = wire_random(pos0, pos1, k, rr); a12 = wire_random(pos1, pos2, k, rr)
    rh, pp = cone_and_law(a01, a12, pos1)
    rhos.append(rh)
rhos = np.array(rhos)
print(f"\n[NEGATIVE control, 20 seeds] mean rho = {rhos.mean():+.3f} +- {rhos.std():.3f} "
      f"(should straddle 0, nowhere near the real -0.612/-0.619)")
