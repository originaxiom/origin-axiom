#!/usr/bin/env python3
"""THE RANK BOUND, tested.

For a module V of a once-punctured-torus bundle with no invariants and no coinvariants on the fibre group,
        |I(V)|  <=  min(r, n - r),      n = dim V,   r = rank(rho(lam) - 1),
from:   n(V) <= r,   n(V*) <= r,   I = t0(V*) - r1(V) <= t0(V*) <= n - r,   -I <= t0(V) <= n - r.
Each inequality is checked separately on random triangular modules of rank 2..6 (built one superdiagonal at a time),
on direct sums of them up to rank 8, and on exterior squares; and the two-step formula n(W) = dim(D cap Im C) is
checked against the index code.  Levels: four small ones of the architecture.
"""
import sys, json, random, collections, pathlib
from modules import *
HERE = pathlib.Path(__file__).resolve().parent
LEVELS = [(1, "LR", 2), (-1, "LR", 1), (-1, "LLR", 1), (1, "LLR", 2)]

def rk_lambda(V, L):
    A = V.word(L.Llam); d = V.d
    return rank_and_null([[(A[i][j] - (i == j)) % V.p for j in range(d)] for i in range(d)], d, V.p)[0]

def check(V, L, tab, tag):
    I, (a0, a1, t0, r1), (b0, b1, s0, q1) = index(V, L.Lr, L.Lmu, L.Llam)
    n = V.d; r = rk_lambda(V, L)
    if a0 or b0: tab["%s rank %d: outside the hypothesis (invariants)" % (tag, n)] += 1; return None
    ok = (a1 - r1 <= r) and (b1 - q1 <= r) and (I <= s0 <= n - r) and (-I <= t0 <= n - r) and abs(I) <= min(r, n - r)
    tab["%s rank %d: %s" % (tag, n, "holds" if ok else "FAILS")] += 1
    key = "%s rank %d: max |I|" % (tag, n); tab[key] = max(tab[key], abs(I))
    tab["%s rank %d: bound attained" % (tag, n)] += (I != 0 and abs(I) == min(r, n - r))
    return I

def run(seed=7, per_rank=60, quiet=False):
    random.seed(seed); tab = collections.Counter(); two = collections.Counter()
    for (eps, word, k) in LEVELS:
        L = Level(eps, word, k); nt = [c for c in L.chars if c != (0, 0, 0)]; made = []
        for n in (2, 3, 4, 5, 6):
            got = tries = 0
            while got < per_rank and tries < 25 * per_rank:
                tries += 1
                chars = [random.choice(nt) for _ in range(n)]
                coeff = {(i, j): random.choice([0, 1, random.randrange(1, L.p)]) for i in range(n) for j in range(i + 1, n)}
                V = build(L, chars, coeff)
                if V is None: tab["triangular rank %d: obstructed" % n] += 1; continue
                got += 1; check(V, L, tab, "triangular"); made.append(V)
        for _ in range(2 * per_rank):
            V, W = random.choice(made), random.choice(made)
            if V.d + W.d <= 8: check(dsum(V, W), L, tab, "direct sum")
        for V in made:
            if 3 <= V.d <= 4: check(ext2(V), L, tab, "exterior square of rank %d," % V.d)
        # the two-step formula against the index code
        for _ in range(3 * per_rank):
            a = random.choice([1, 2, 3, 4]); b = random.choice([1, 2, 3]) if a < 4 else 1
            alphas = [random.choice(nt) for _ in range(a)]; betas = [random.choice(nt) for _ in range(b)]
            if any(al == be for al in alphas for be in betas): continue
            gamma = {(i, j): random.choice([0, 1, random.randrange(1, L.p)]) for i in range(a) for j in range(b)}
            V = two_step(L, alphas, betas, gamma)
            I, (a0, a1, t0, r1), (b0, b1, s0, q1) = index(V, L.Lr, L.Lmu, L.Llam)
            da, db, dg = dual_data(L, alphas, betas, gamma)
            good = (a1 - r1 == n_formula(L, alphas, betas, gamma)) and (b1 - q1 == n_formula(L, da, db, dg)) and (a1 - r1 <= min(a, b))
            two["two-step formula %s" % ("holds" if good else "FAILS")] += 1
            two["two-step max |I|"] = max(two["two-step max |I|"], abs(I))
        if not quiet: print(("+" if eps > 0 else "-") + word, k, "done", flush=True)
    return dict(tab), dict(two)

if __name__ == "__main__":
    tab, two = run()
    for key in sorted(tab): print(key, tab[key])
    for key in sorted(two): print(key, two[key])
    ok = not any("FAILS" in k for k in list(tab) + list(two))
    json.dump(dict(table=tab, two_step=two, holds=ok), open(HERE / "rank_bound.json", "w"), indent=1, sort_keys=True)
    print("THE RANK BOUND HOLDS ON EVERY MODULE TESTED" if ok else "FAILURE")
