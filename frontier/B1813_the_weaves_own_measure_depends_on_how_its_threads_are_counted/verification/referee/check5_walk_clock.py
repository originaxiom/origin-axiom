"""Check 5: the walk's clock (B1662 W3, reading A: L, R, L^-1, R^-1 at equal strength).  The n-th step X_n of the walk,
read as a closed word (its conjugacy class); hyperbolic ones weighted by their length 2 arccosh(|t|/2); the height tail
by the excursion formula on the primitive geodesic's run sequence, obtained exactly from the continued fraction of the
axis endpoint (P + sqrt D)/Q.  Compared with the positive-word (move-count) limit and with hyperbolic area.
Also: the uniform measure on cyclically reduced words of length n in the free group F(L, R) (another 'word length')."""
import math, sys, os, json, random
sys.path.insert(0, os.path.dirname(__file__))
from refcore import cf_forward, hyp_tail

Lm = ((1, 1), (0, 1)); Rm = ((1, 0), (1, 1)); Li = ((1, -1), (0, 1)); Ri = ((1, 0), (-1, 1))
GEN = [Lm, Rm, Li, Ri]; INV = {0: 2, 1: 3, 2: 0, 3: 1}
def mul(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))

def period_runs(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; t = a + d
    if t < 0: a, b, c, d, t = -a, -b, -c, -d, -t
    D = t * t - 4; P, Q = a - d, 2 * c; s = math.isqrt(D); seen = {}; digs = []
    for k in range(100000):
        if (P, Q) in seen: per = digs[seen[(P, Q)]:]; break
        seen[(P, Q)] = k
        q = (P + s) // Q if Q > 0 else -((P + s) // (-Q)) - 1
        digs.append(q); P = q * Q - P; Q = (D - P * P) // Q
    per = [int(x) for x in per]; assert min(per) >= 1
    return per + per if len(per) % 2 else per

def tail_of(runs_, Ys):
    n = len(runs_); exc = {Y: 0.0 for Y in Ys}; ell = 0.0
    for i in range(n):
        x = cf_forward(runs_, i); y = 1.0 / cf_forward([runs_[(i - 1 - k) % n] for k in range(n)], 0)
        c, rho = (x - y) / 2, (x + y) / 2
        ell += math.atanh((runs_[i] - c) / rho) - math.atanh(-c / rho)
        for Y in Ys:
            if rho > Y: exc[Y] += 2 * math.acosh(rho / Y)
    return exc, ell

Ys = [1.5, 2.0, 3.0, 4.0, 6.0]
def run(sampler, n, nw, seed):
    rng = random.Random(seed); num = {Y: 0.0 for Y in Ys}; den = 0.0; hyp = 0
    for _ in range(nw):
        M = ((1, 0), (0, 1))
        for g in sampler(rng, n): M = mul(M, GEN[g])
        t = abs(M[0][0] + M[1][1])
        if t <= 2: continue
        hyp += 1; ellM = 2 * math.acosh(t / 2); exc, ell0 = tail_of(period_runs(M), Ys); j = ellM / ell0
        assert abs(j - round(j)) < 1e-6, (j,)
        for Y in Ys: num[Y] += round(j) * exc[Y]
        den += ellM
    return {"hyperbolic fraction": hyp / nw, "P(Im>Y)": {str(Y): round(num[Y] / den, 5) for Y in Ys}}

def walk(rng, n): return [rng.randrange(4) for _ in range(n)]
def reduced_cyclic(rng, n):
    while True:
        w = [rng.randrange(4)]
        for _ in range(n - 1): w.append(rng.choice([g for g in range(4) if g != INV[w[-1]]]))
        if w[-1] != INV[w[0]]: return w

out = {"hyperbolic area": {str(Y): round(hyp_tail(Y), 5) for Y in Ys},
       "move-count limit (check2)": {"1.5": 0.38291, "2.0": 0.16759, "3.0": 0.034621, "4.0": 0.0075424, "6.0": 0.0003875}}
for n, nw in ((100, 6000), (200, 4000), (400, 2000)):
    r = run(walk, n, nw, 303 + n); out["walk X_n, n=%d" % n] = r; print("walk n=%d" % n, r, flush=True)
for n, nw in ((20, 8000), (40, 4000), (80, 2000)):
    r = run(reduced_cyclic, n, nw, 404 + n); out["cyclically reduced F2 words, n=%d" % n] = r; print("reduced n=%d" % n, r, flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "check5_walk_clock.json"), "w"), indent=1)
