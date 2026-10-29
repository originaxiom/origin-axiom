"""Main's verification of T4's claim (audit/drafts/t2/T3_T4_REPORT.md): B1663's walk (L, R at (1-p)/2, L^-1, R^-1 at p/2,
right-multiplied: X_n = g1 ... gn) has exit law nu_p = (1-p) M + p F_*M, with M = the p = 0 exit law (Minkowski's measure
on [0, inf]) and F(x) = -x.  (1) The algebra: F L F = L^-1 and F R F = R^-1 as Mobius maps.  (2) Simulation: exit points
xi = lim X_n(i) by composing the sampled word from the inside out; the KS distance between the p-walk's exit points and
samples of the mixture (1-p) M + p (-M); P(xi > 0) against 1 - p."""
import random, cmath, json, pathlib
def mob(g, z):
    if g == "L": return z + 1
    if g == "R": return z / (z + 1)
    if g == "l": return z - 1
    return z / (1 - z)
F = lambda z: -z.conjugate()          # the reflection x -> -x, acting on the upper half-plane
alg = max(abs(F(mob("L", F(z))) - mob("l", z)) + abs(F(mob("R", F(z))) - mob("r", z)) for z in (0.3 + 1.1j, -2.2 + 0.4j, 5.0 + 3j))
def exit_point(p, rng, n=400):
    w = []
    for _ in range(n):
        x = rng.random()
        w.append("L" if x < (1 - p) / 2 else "R" if x < 1 - p else "l" if x < 1 - p / 2 else "r")
    z = 1j
    for g in reversed(w): z = mob(g, z)
    return z.real
def ks(a, b):
    a, b = sorted(a), sorted(b); i = j = 0; d = 0.0; na, nb = len(a), len(b)
    while i < na and j < nb:
        if a[i] <= b[j]: i += 1
        else: j += 1
        d = max(d, abs(i / na - j / nb))
    return d
import sys; rng = random.Random(int(sys.argv[1])); NS = int(sys.argv[2])
M = [exit_point(0.0, rng) for _ in range(NS)]
out = {"algebra: max |F L F - L^-1| + |F R F - R^-1| on three points": alg, "M: P(xi >= 0) at p = 0": sum(x >= 0 for x in M) / NS}
for p in (0.25, 0.75, 0.9):
    walk = [exit_point(p, rng) for _ in range(NS)]
    mix = [(-m if rng.random() < p else m) for m in [exit_point(0.0, rng) for _ in range(NS)]]
    out["p = %g" % p] = {"P(xi > 0)": round(sum(x > 0 for x in walk) / NS, 4), "1 - p": 1 - p,
                         "KS(walk, (1-p)M + p(-M))": round(ks(walk, mix), 4), "KS noise scale ~ 1.36 sqrt(2/N)": round(1.36 * (2 / NS) ** 0.5, 4),
                         "control: KS(walk, M)": round(ks(walk, M), 4)}
print(json.dumps(out, indent=1)); pass
