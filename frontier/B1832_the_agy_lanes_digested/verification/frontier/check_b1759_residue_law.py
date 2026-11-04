"""agy:B1759 Theorem 1 (the residue law), checked on MAIN's b1656_funcs (data-free; no measured number read).

Claim 1 (kernel factorisation): for every charge pair, P_s(u; X, Y) = R_s(X, Y) K_s(u; X + Y), i.e. the normalised kernel
K_s = P_s / R_s depends on the twists only through their sum X + Y (the difference X - Y enters only R_s).
Claim 2: hence the regularised norm c_s depends only on q_L + q_R; with |K_s(-u; -S)| = |K_s(u; S)| the three SM sectors
(sums -3w, +3w, +3w) share c_s.  B1826 item 1 verified claim 2 for the three SM sectors only; here: arbitrary complex twists,
non-SM charge pairs, the kernel itself, and negative controls (different sums must differ)."""
import json, math, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B, SECT

Bf = B()
rng = np.random.default_rng(20261104)
OUT = {}


def kernels(X, Y, t, us):
    x, y = Bf.twist_of(X, t), Bf.twist_of(Y, t)
    R = Bf.residues(x, y, t)
    P = Bf.pairs(x, y, us, t)
    return R, {s: (P[s] / R[s] if abs(R[s]) > 1e-12 else None) for s in Bf.UNITS}


# --- 1. kernel factorisation at generic complex twists (not torsion, not SM) -----------------------------------
worst_same, best_diff, n = 0.0, np.inf, 0
for trial in range(12):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.5))
    S = complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) * (0.3 + abs(t))
    us = (rng.uniform(-0.45, 0.45, 40) + rng.uniform(-0.45, 0.45, 40) * t) + 0.07   # points of the period cell, off 0
    ref = None
    for k in range(4):
        D = complex(rng.uniform(-1.5, 1.5), rng.uniform(-1.5, 1.5)) * (0.3 + abs(t))
        _, K = kernels((S + D) / 2, (S - D) / 2, t, us)
        if ref is None:
            ref = K; continue
        for s in Bf.UNITS:
            if K[s] is None or ref[s] is None: continue
            rel = np.max(np.abs(K[s] - ref[s])) / np.max(np.abs(ref[s])); worst_same = max(worst_same, rel); n += 1
    # negative control: same difference, a different sum
    D = complex(0.31, 0.17); S2 = S + complex(0.137, 0.091)
    _, K1 = kernels((S + D) / 2, (S - D) / 2, t, us); _, K2 = kernels((S2 + D) / 2, (S2 - D) / 2, t, us)
    for s in Bf.UNITS:
        if K1[s] is not None and K2[s] is not None:
            best_diff = min(best_diff, np.max(np.abs(K1[s] - K2[s])) / np.max(np.abs(K1[s])))
OUT["kernel_same_sum_max_rel_dev"] = worst_same
OUT["kernel_same_sum_comparisons"] = n
OUT["control_different_sum_min_rel_dev"] = float(best_diff)
print("1. K_s = P_s/R_s at equal sums X+Y, generic complex twists: max rel dev %.2e over %d channel comparisons" % (worst_same, n))
print("   control, sum shifted by 0.137+0.091i: min rel dev %.3f (must be O(1))" % best_diff)

# --- 2. c_s for non-SM charge pairs of equal sum, and the sign flip -------------------------------------------
pairs_by_sum = {3: [(1, 2), (-3, 6), (5, -2), (-1, 4), (7, -4)], -3: [(1, -4), (2, -5), (-6, 3)], 1: [(1, 0), (3, -2), (-2, 3)]}
rows = []
for trial in range(3):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 2.2)); w = complex(rng.uniform(-.5, .5), 0) + rng.uniform(0.05, 0.45) * t
    cs = {}
    for ssum, prs in pairs_by_sum.items():
        for ql, qr in prs:
            x, y = Bf.sector_twists(w, t, ql, qr); R = Bf.residues(x, y, t); c = Bf.cA(x, y, t, R)
            cs[(ql, qr)] = c
    def spread(keys):
        out = 0.0
        for s in Bf.UNITS:
            v = [cs[k][s] for k in keys if cs[k][s] is not None]
            if len(v) > 1: out = max(out, max(v) - min(v))
        return out
    same3 = spread(pairs_by_sum[3]); samem3 = spread(pairs_by_sum[-3]); both = spread(pairs_by_sum[3] + pairs_by_sum[-3])
    diff = max(abs(cs[(1, 2)][s] - cs[(1, 0)][s]) for s in Bf.UNITS if cs[(1, 2)][s] is not None and cs[(1, 0)][s] is not None)
    rows.append({"tau": [t.real, t.imag], "w": [w.real, w.imag], "spread_sum+3": same3, "spread_sum-3": samem3,
                 "spread_sum+-3": both, "control_sum3_vs_sum1": diff})
    print("2. tau=%.3f%+.3fi: c_s spread within sum +3 (5 pairs) %.1e, within -3 (3 pairs) %.1e, across +-3 %.1e; control sum 3 vs 1: %.3f"
          % (t.real, t.imag, same3, samem3, both, diff))
OUT["c_s_rows"] = rows

# --- 3. the sign flip |K_s(-u; -S)| = |K_s(u; S)| ----------------------------------------------------------------
worst = 0.0
for trial in range(6):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.5)); S = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
    D = complex(rng.uniform(-1, 1), rng.uniform(-1, 1)); us = (rng.uniform(-0.45, 0.45, 30) + rng.uniform(-0.45, 0.45, 30) * t) + 0.05
    _, Kp = kernels((S + D) / 2, (S - D) / 2, t, us); _, Km = kernels((-S + D) / 2, (-S - D) / 2, t, -us)
    for s in Bf.UNITS:
        if Kp[s] is not None and Km[s] is not None:
            worst = max(worst, np.max(np.abs(np.abs(Kp[s]) - np.abs(Km[s]))) / np.max(np.abs(Kp[s])))
OUT["sign_flip_max_rel_dev"] = worst
print("3. |K_s(-u; -S)| vs |K_s(u; S)|: max rel dev %.2e" % worst)
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("exit 0")
