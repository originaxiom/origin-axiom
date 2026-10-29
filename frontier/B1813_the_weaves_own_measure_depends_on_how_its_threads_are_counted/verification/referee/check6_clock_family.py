"""Check 6: is 'the clock' a two-way choice, or a continuum?  Words of length exactly n (every primitive necklace with
both letters), each weighted by exp(-s * ell(w)) (s = 0 is the move clock; s -> 1 approaches the Farey map's phase
transition, where the geometric clock's measure lives, cf. B852).  Length-weighted height tail P(Im > Y) at n = 16, 18,
20 for s in {0, 0.25, 0.5}.  Also the per-thread-mass-1 variant at s = 0 (the frame card's 'no weight')."""
import math, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from refcore import lyndon, mat, runs, cf_forward

Ys = [1.5, 2.0, 3.0, 4.0, 6.0]
def data(n):
    rows = []
    for w in lyndon(n):
        if len(w) != n: continue
        M = mat(w); ell = 2 * math.acosh((M[0][0] + M[1][1]) / 2); a = runs(w); m = len(a); exc = [0.0] * len(Ys)
        for i in range(m):
            x = cf_forward(a, i, 48); y = 1.0 / cf_forward([a[(i - 1 - k) % m] for k in range(m)], 0, 48); rho = (x + y) / 2
            for j, Y in enumerate(Ys):
                if rho > Y: exc[j] += 2 * math.acosh(rho / Y)
        rows.append((ell, exc))
    return rows
out = {}
for n in (16, 18, 20):
    rows = data(n); res = {}
    for s in (0.0, 0.25, 0.5):
        den = sum(math.exp(-s * e) * e for e, _ in rows)
        res["s=%g" % s] = {str(Y): round(sum(math.exp(-s * e) * x[j] for e, x in rows) / den, 5) for j, Y in enumerate(Ys)}
    den1 = len(rows)
    res["s=0, each thread mass 1"] = {str(Y): round(sum(x[j] / e for e, x in rows) / den1, 5) for j, Y in enumerate(Ys)}
    out[n] = {"necklaces": len(rows), **res}; print(n, json.dumps(out[n]), flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "check6_clock_family.json"), "w"), indent=1)
