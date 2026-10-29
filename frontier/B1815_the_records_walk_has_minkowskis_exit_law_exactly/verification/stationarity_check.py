"""Stationarity check of the derived exit law of B1663's walk.

Claim: nu_p = (1-p) M + p F_*M, M = Minkowski's measure on [0, inf] (law of
[G-1; G, G, ...] with G i.i.d. Geometric(1/2) on {1,2,...}), F(x) = -x.
Test: E_nu[phi(xi)] - sum_s mu(s) E_nu[phi(s.xi)] = 0 for smooth phi on the
circle (phi = cos/sin of k*theta, theta = 2*arctan(x)), with common samples.
Control: the same with the wrong side weight p' = 1 - p + 0.1 must fail.
"""
import math, random, sys

def sample_M(rng, depth=48):
    g = [1]
    while True:
        k = 1
        while rng.random() < 0.5: k += 1
        g.append(k)
        if len(g) > depth: break
    digits = [g[1] - 1] + g[2:]
    x = float(digits[-1])
    for a in reversed(digits[:-1]):
        x = a + 1.0 / x if x != 0 else float('inf')
    return x

def mob(m, x):
    a, b, c, d = m
    if math.isinf(x): return a / c if c else math.inf
    den = c * x + d
    return (a * x + b) / den if den != 0 else math.inf

def theta(x):
    return math.pi if math.isinf(x) else 2.0 * math.atan(x)

L = (1, 1, 0, 1); R = (1, 0, 1, 1); Li = (1, -1, 0, 1); Ri = (1, 0, -1, 1)

def run(p, side_pos, n, seed):
    rng = random.Random(seed)
    steps = [(L, (1 - p) / 2), (R, (1 - p) / 2), (Li, p / 2), (Ri, p / 2)]
    ks = (1, 2, 3)
    acc = {(f, k): [0.0, 0.0] for f in ('c', 's') for k in ks}
    for _ in range(n):
        x = sample_M(rng)
        if rng.random() >= side_pos: x = -x
        t0 = theta(x)
        ts = [(theta(mob(m, x)), w) for m, w in steps]
        for k in ks:
            for f, fn in (('c', math.cos), ('s', math.sin)):
                d = fn(k * t0) - sum(w * fn(k * t) for t, w in ts)
                acc[(f, k)][0] += d; acc[(f, k)][1] += d * d
    out = {}
    for key, (s1, s2) in acc.items():
        mean = s1 / n; se = math.sqrt(max(s2 / n - mean ** 2, 0) / n)
        out[f"{key[0]}{key[1]}"] = round(mean / se, 2)
    return out

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    for p in (0.0, 0.25, 0.5):
        print("p", p, "claimed side 1-p:", run(p, 1 - p, n, 11), flush=True)
        print("p", p, "control side 1-p+0.1 (min 1):", run(p, min(1.0, 1 - p + 0.1) if p > 0 else 0.9, n, 12), flush=True)
