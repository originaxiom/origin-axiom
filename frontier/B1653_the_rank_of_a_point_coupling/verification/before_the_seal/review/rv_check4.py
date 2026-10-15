"""Reviewer check 4: U2(d) by contour residues (reviewer's own series instrument); the seeded PAIRS and U0(b)'s margin;
U3 shown to follow from the frame algebra alone (it holds even when the closed form is replaced by garbage)."""
import sys
sys.path.insert(0, ".")
import numpy as np
from rv_core import *

def twist_of(w, t): return (mp.im(w) / mp.im(t), 2 * (mp.re(w) - mp.re(t) * mp.im(w) / mp.im(t)))
def residues(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = {s: 0 for s in "1ijk"}
    for m in range(N):
        z = rad * mp.exp(2 * J * mp.pi * m / N); P = pairings(x, y, z, t)
        for s in acc: acc[s] += P[s] * z
    return {s: acc[s] / N for s in acc}

t = mp.mpc(0.13, 1.07); yb = (mp.mpf("0.11"), mp.mpf("0.37")); u0 = mp.mpc(0.6, 0.35); wy = wpt(yb, t)
epss = [mp.mpf(10) ** (-k) for k in (1, 2, 3, 4)]; vals = []
for ep in epss:
    xb = twist_of(ep * u0 - wy, t)
    vals.append(rel_rr(residues(xb, yb, t)))
sl = [float((mp.log(vals[k + 1]) - mp.log(vals[k])) / (mp.log(epss[k + 1]) - mp.log(epss[k]))) for k in range(3)]
print("U2(d) by contour: slopes", sl, " all |s-2|<0.05:", all(abs(s - 2) < 0.05 for s in sl))

rng = np.random.default_rng(1653)
def rnd_twist(): return (mp.mpf(rng.uniform(-0.5, 0.5)), mp.mpf(rng.uniform(-1, 1)))
PAIRS = [(rnd_twist(), rnd_twist()) for _ in range(5)]
print("\nseeded PAIRS (a, b):", [([float(v) for v in x], [float(v) for v in y]) for x, y in PAIRS])

def naive_tau_err(x, y, z, tt):
    (ax, bx), (ay, by) = x, y
    B0 = bil(x, y, z, tt, False); Bt = bil(x, y, z + tt, tt, False)
    lb = mp.exp(-J * mp.pi * (bx + by)); E = Bt - lb * QJ * B0 * QJ.T
    return max(abs(E[m, k]) for m in range(2) for k in range(2)) / max(abs(B0[m, k]) for m in range(2) for k in range(2))
TAUS = [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.88)]
PTS = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29)]
print("U0(b) naive tau-law min error over the seeded set:", mp.nstr(min(naive_tau_err(x, y, z, tt) for tt in TAUS for (x, y) in PAIRS for z in PTS), 4))

print("\nU3 is frame algebra: the half-period shifts' four-vectors are signed permutations of the old ones whatever the")
print("closed form says; shown directly from the bilinears (no closed form used):")
def four(x, y, z, tt): P = pairings(x, y, z, tt); return [P[s] for s in "1ijk"]
x, y = PAIRS[0]; z = PTS[0]; tt = TAUS[0]
v = four(x, y, z, tt)
for sh in [(0, 1), (mp.mpf(1) / 2, 0), (mp.mpf(1) / 2, 1)]:
    w = four((x[0] + sh[0], x[1] + sh[1]), y, z, tt)
    # report the ratio pattern w_k / v_p(k) for the best permutation
    import itertools
    best = None
    for p in itertools.permutations(range(4)):
        r = [w[k] / v[p[k]] for k in range(4)]
        sp = max(abs(abs(r[k] / r[0]) - 1) for k in range(4)) + max(min(abs(r[k] / r[0] - 1), abs(r[k] / r[0] + 1)) for k in range(4))
        if best is None or sp < best[0]: best = (sp, p, [mp.nstr(r[k] / r[0], 6) for k in range(4)], mp.nstr(r[0], 8))
    print(f"  shift {[float(s) for s in sh]}: perm {best[1]}, ratios/first {best[2]}, scalar {best[3]}, misfit {mp.nstr(best[0],3)}")
print("  e^{2 pi i a_x} =", mp.nstr(mp.exp(2 * J * mp.pi * x[0]), 8))
