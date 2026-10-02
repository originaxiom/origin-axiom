#!/usr/bin/env python3
"""B1455 -- the handoff's own side claims, recomputed (its section 0.2 and section 6).

    python3 handoff_claims.py      # prints, writes handoff_claims.json
"""
import itertools, json, math, os, sys
from fractions import Fraction as F
out = {}

# (a) the fixed point of a -> ab, b -> a is the Sturmian word of slope 1/phi^2, at nine intercepts
w = "a"
while len(w) < 400: w = "".join("ab" if c == "a" else "a" for c in w)
phi = (1 + 5 ** 0.5) / 2; alpha = 1 / phi ** 2
def sturm(rho, n): return "".join("b" if math.floor((k + 1) * alpha + rho) - math.floor(k * alpha + rho) == 1 else "a" for k in range(n))
shifts = {}
for j in range(1, 10):
    s = sturm(j * alpha, 80); shifts[j] = w.find(s)
out["sturmian"] = dict(slope="1/phi^2", intercepts="j/phi^2, j = 1..9", position_in_the_fixed_point=shifts,
                       each_is_the_fixed_point_shifted=all(v == j - 1 for j, v in shifts.items()))
# control: another slope is not found
out["sturmian"]["control_other_slope_found"] = w.find("".join("b" if math.floor((k + 1) * 0.3 + 0.3) - math.floor(k * 0.3 + 0.3) == 1 else "a" for k in range(80))) >= 0

# (b) expanding and contracting: |A^10 v_u|, |A^10 v_s| for A = LR
lam = phi ** 2
out["expansion"] = dict(lambda_10=lam ** 10, lambda_minus_10=lam ** -10, lucas_20=15127)

# (c) conjugators of A to its inverse, in GL(2,Z), entries to 3: both determinants occur
A = ((2, 1), (1, 1)); Ai = ((1, -1), (-1, 2))
def mul(X, Y): return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
conj = {1: 0, -1: 0}
for a, b, c, d in itertools.product(range(-3, 4), repeat=4):
    X = ((a, b), (c, d)); dt = a * d - b * c
    if dt in (1, -1) and mul(X, A) == mul(Ai, X): conj[dt] += 1
out["conjugators_of_A_to_its_inverse_entries_to_3"] = {"det +1": conj[1], "det -1": conj[-1], "total": conj[1] + conj[-1]}

# (d) surjections onto SL(2,5): m004 none; m202 some
p = 5
G = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(p), repeat=4) if (a * d - b * c) % p == 1]
def mm(X, Y): return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))
I2 = ((1, 0), (0, 1))
def inv(X): return ((X[1][1], (-X[0][1]) % p), ((-X[1][0]) % p, X[0][0]))
def generated(gens):
    seen = {I2}; frontier = [I2]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mm(x, g)
                if y not in seen: seen.add(y); nxt.append(y)
        frontier = nxt
    return len(seen)
def surjections(name):
    import snappy
    M = snappy.Manifold(name); gp = M.fundamental_group(); gens = gp.generators(); rels = gp.relators()
    n = 0; homs = 0
    for imgs in itertools.product(G, repeat=len(gens)):
        tab = {}
        for g, x in zip(gens, imgs): tab[g] = x; tab[g.upper()] = inv(x)
        ok = True
        for r in rels:
            X = I2
            for c in r: X = mm(X, tab[c])
            if X != I2: ok = False; break
        if not ok: continue
        homs += 1
        if generated(list(imgs)) == 120: n += 1
    return dict(generators=len(gens), homomorphisms=homs, surjections=n, up_to_conjugation_in_SL25=n // 60 if n % 60 == 0 else None)
try:
    out["onto_SL(2,5)"] = {"m004": surjections("m004"), "m202": surjections("m202")}
except Exception as exc:
    out["onto_SL(2,5)"] = "not run: %r" % (exc,)

# (e) plenitude: the mean of the sum of k choices from {-1, 0, 1}
out["plenitude_mean"] = {k: str(F(sum(sum(c) for c in itertools.product((-1, 0, 1), repeat=k)), 3 ** k)) for k in range(1, 6)}
for k, v in out.items(): print(k, v)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "handoff_claims.json"), "w"), indent=1)
