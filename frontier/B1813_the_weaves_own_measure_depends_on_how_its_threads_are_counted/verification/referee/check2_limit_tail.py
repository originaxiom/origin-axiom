"""Check 2: the move-count limit and its tail.
(a) Excursion formula, Y >= 1: time above Y on the closed geodesic = sum over runs i of 2 arccosh(rho_i / Y)_+,
    rho_i = (x_i + y_i)/2.  Verified against reduced-height sampling on the n <= 14 necklaces.
(b) The n -> infinity limit of uniform words = stationary iid Geometric(1/2) runs (both letters; the Minkowski
    question-mark measure's natural extension), weighted by the roof (segment length):
       P(Im > Y) = E[2 arccosh(rho_0/Y)_+] / E[r_0].
    Computed by conditioning on a_0 = a (weight 2^-a) with Monte Carlo over the other digits.
(c) Finite-n uniform random words, n = 20, 40, 80 (Monte Carlo, run-segment sampler), against (b).
(d) Local slope -d log P / dY against 2 ln 2 + 1/(2Y) (the heuristic: run a reaches height ~a/2, P(a) = 2^-a,
    time above Y ~ sqrt(Y)^-1 near threshold)."""
import math, sys, json, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from refcore import lyndon, mat, runs, reduce_vec, segments_from_runs

rng = np.random.default_rng(1813)
out = {}

# (a) excursion formula on n <= 14
def exc_time(a, Y, K=64):
    n = len(a); tot = 0.0
    from refcore import cf_forward
    for i in range(n):
        x = cf_forward(a, i, K); y = 1.0 / cf_forward([a[(i - 1 - k) % n] for k in range(n)], 0, K)
        rho = (x + y) / 2
        if rho > Y: tot += 2 * math.acosh(rho / Y)
    return tot
ws = lyndon(14); num = {Y: 0.0 for Y in (1.5, 2.0, 3.0, 4.0, 6.0)}; den = 0.0
for w in ws:
    M = mat(w); ell = 2 * math.acosh((M[0][0] + M[1][1]) / 2); den += ell; a = runs(w)
    for Y in num: num[Y] += exc_time(a, Y)
out["(a) excursion formula, n<=14"] = {str(Y): round(num[Y] / den, 5) for Y in num}
print("(a)", out["(a) excursion formula, n<=14"], flush=True)

# (b) the limit, vectorised: digits iid Geom(1/2) on {1,2,...}
K = 48
def geom(size): return rng.geometric(0.5, size=size).astype(float)
def cf_vals(D):            # D: (S, K) digits d_0, d_1, ... -> [d_0; d_1, d_2, ...]
    v = D[:, -1].copy()
    for k in range(D.shape[1] - 2, -1, -1): v = D[:, k] + 1.0 / v
    return v
S = 400_000
def sample_given_a(a, S):
    xp = cf_vals(geom((S, K)))                 # x' = [a_1; a_2, ...]
    yi = cf_vals(geom((S, K)))                 # 1/y = [a_-1; a_-2, ...]
    x = a + 1.0 / xp; y = 1.0 / yi
    c, rho = (x - y) / 2, (x + y) / 2
    r = np.arctanh((a - c) / rho) - np.arctanh(-c / rho)
    return rho, r
# E[r] over a ~ Geom(1/2)
Er = 0.0; Er_se2 = 0.0
amax = 60
cache = {}
for a in range(1, amax + 1):
    rho, r = sample_given_a(a, S if a <= 12 else 40_000); cache[a] = rho
    Er += 2.0 ** -a * r.mean(); Er_se2 += (2.0 ** -a) ** 2 * r.var() / len(r)
Ys = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 20.0]
lim = {}
for Y in Ys:
    s = 0.0
    for a, rho in cache.items():
        s += 2.0 ** -a * np.where(rho > Y, 2 * np.arccosh(np.maximum(rho / Y, 1.0)), 0.0).mean()
    lim[Y] = s / Er
out["(b) limit E[r] (mean roof per run)"] = Er; out["(b) E[r] se"] = math.sqrt(Er_se2)
out["(b) limit P(Im>Y)"] = {str(Y): lim[Y] for Y in Ys}
print("(b) E[r] =", Er, "+-", math.sqrt(Er_se2)); print("(b)", {Y: "%.5g" % lim[Y] for Y in Ys}, flush=True)
sl = {}
for Y1, Y2 in zip(Ys[:-1], Ys[1:]):
    if lim[Y2] > 0: sl["%g-%g" % (Y1, Y2)] = round(math.log(lim[Y1] / lim[Y2]) / (Y2 - Y1), 4)
out["(d) local slope"] = sl; out["(d) 2 ln 2"] = 2 * math.log(2)
print("(d) slopes", sl, " 2ln2 =", 2 * math.log(2), flush=True)
# prefactor check: P * 4^Y * sqrt(Y)
out["(d) P*4^Y*sqrt(Y)"] = {str(Y): lim[Y] * 4 ** Y * math.sqrt(Y) for Y in Ys if Y >= 2}
print("(d) P 4^Y sqrt(Y):", {Y: round(lim[Y] * 4 ** Y * math.sqrt(Y), 4) for Y in Ys if Y >= 2}, flush=True)

# (c) finite n uniform random words, cyclic, primitive-or-not (non-primitive fraction negligible), weight = length
def mc_words(n, nw):
    num = {Y: 0.0 for Y in (2.0, 3.0, 4.0, 6.0)}; den = 0.0
    for _ in range(nw):
        w = "".join(rng.choice(["L", "R"], size=n))
        if "L" not in w or "R" not in w: continue
        a = runs(w); den_w = 0.0
        from refcore import cf_forward
        for i in range(len(a)):
            x = cf_forward(a, i); y = 1.0 / cf_forward([a[(i - 1 - k) % len(a)] for k in range(len(a))], 0)
            c, rho = (x - y) / 2, (x + y) / 2
            den_w += math.atanh((a[i] - c) / rho) - math.atanh(-c / rho)
            for Y in num:
                if rho > Y: num[Y] += 2 * math.acosh(rho / Y)
        den += den_w
    return {str(Y): num[Y] / den for Y in num}
for n, nw in ((20, 40000), (40, 20000), (80, 10000)):
    r_ = mc_words(n, nw); out["(c) uniform words n=%d (%d words)" % (n, nw)] = r_
    print("(c) n=%d" % n, {k: "%.5f" % v for k, v in r_.items()}, flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "check2_limit_tail.json"), "w"), indent=1)
