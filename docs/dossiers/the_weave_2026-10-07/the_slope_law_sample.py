#!/usr/bin/env python3
"""W14's check on the largest level: the slope law against sm:B1374's engine index on a random sample of +LLRLRR's
tick-3 modules.

+LLRLRR is the one odd-trace state to length six whose tick-3 level carries no F-CI generation-shaped background
(`the_slope_law.json`). Its level has 3 328 cusp-trivial characters, so the engine's full census (about eleven million
modules) is out of reach. The law is checked here on 300 modules: twelve extension characters lambda at random, and for
each, half its alphas from lambda's own slope class (where the law can fire) and half at random. The engine runs at one
prime above 20 000; the slopes are tuples over three such primes.

    python3 the_slope_law_sample.py   ->  the_slope_law_sample.json beside it
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_slope_law as SL  # noqa: E402

LV, IL = SL.LV, SL.IL


def engine_index(Gr, F, z, lam, a, cache):
    if lam not in cache:
        val = {g: pow(z, x, F.p) for g, x in zip(Gr.gens, lam)}
        cache[lam] = IL.h1_and_cocycle(F, Gr.gens, Gr.rels, Gr.mu, Gr.lam, val)[1]
    b = Gr.add(a, lam, coeffs=[1, -1])
    V = IL.Rep(F, Gr.gens, LV.ext_rep(F, z, Gr.gens, a, b, cache[lam], Gr.N))
    assert V.check_relators(Gr.rels)
    return IL.index(V, Gr.rels, Gr.mu, Gr.lam)[0]


def run(sw="+LLRLRR", n_lam=12, n_per=25, seed=1):
    t0 = time.time()
    Gr = SL.CuspTrivial(sw, 3)
    s, primes = SL.slopes(Gr.gens, Gr.rels, Gr.mu, Gr.lam, Gr.chars, Gr.N)
    p = LV.primes_for(Gr.N, k=1, start=20000)[0]
    F = IL.GF(p)
    z = F.root_of_unity(Gr.N)
    rng = random.Random(seed)
    nonzero = [c for c in Gr.chars if any(c)]
    cache, rows = {}, []
    for lam in rng.sample(nonzero, n_lam):
        same = [c for c in nonzero if s[c] == s[lam] and c != lam]
        k = min(len(same), n_per // 2)
        for a in rng.sample(same, k) + rng.sample(nonzero, n_per - k):
            rows.append((SL.law_index(s, Gr.add, Gr.zero, lam, a), engine_index(Gr, F, z, lam, a, cache)))
    return {"state": sw, "tick": 3, "|G|": len(Gr.chars), "slope primes": primes, "engine prime": p,
            "sampled": len(rows), "agree": sum(1 for x, y in rows if x == y),
            "firing by the law": sum(1 for x, _ in rows if x), "firing by the engine": sum(1 for _, y in rows if y),
            "seconds": round(time.time() - t0, 1)}


if __name__ == "__main__":
    out = run()
    out["all agree"] = out["agree"] == out["sampled"]
    with open(HERE / "the_slope_law_sample.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out))
