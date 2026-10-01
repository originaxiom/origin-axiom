#!/usr/bin/env python3
"""B1434 -- the two states that carry generation-shaped backgrounds at their OWN level, checked two further ways:
(1) on SnapPy's own presentation of the census manifold (no word state, no mapping torus built here);
(2) in exact arithmetic over Q(zeta_N) on this arc's presentation (main's cyclo.py, no prime field).
Run after the sealed census; this is verification of its P3 outcome, not part of the sealed population."""
import os, sys, json, warnings, pathlib
warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
import architecture_census as ac
import cover_census as cc
import snappy

def toint(w): return [(ord(ch) - ord('a') + 1) if ch.islower() else -(ord(ch) - ord('A') + 1) for ch in w]

def on_snappy_presentation(name, N, pstart):
    M = snappy.Manifold(name); G = M.fundamental_group(); ng = len(G.generators())
    rels = [toint(r) for r in G.relators()]; mu, lam = [toint(w) for w in G.peripheral_curves()[0]]
    saved_cover, saved_chars = cc.cover, cc.characters
    def chars_cusp(rels_, mu_, ng_, N_):
        return [c for c in saved_chars(rels_, mu_, ng_, N_) if sum(e * x for e, x in zip(cc.expvec(lam, ng_), c)) % N_ == 0]
    cc.cover = lambda _n: (ng, rels, mu, lam, {g: [g] for g in range(1, ng + 1)}); cc.characters = chars_cusp
    try: o, bgs, I, chars, _ = cc.census(1, N, pstart, verbose=False)
    finally: cc.cover, cc.characters = saved_cover, saved_chars
    return dict(manifold=name, identified=str(M.identify()[:1]), H1=str(M.homology()), primes=o["primes"], characters=o["characters"],
                loci=o["loci"], loci_nonsquare=o["loci_nonsquare"], firing=o["firing"], generation_backgrounds=o["generation_backgrounds"],
                lifted=o["lifted"], signs={str(k): v for k, v in o["signs"].items()}, abs_counts={str(k): v for k, v in o["abs_counts"].items()},
                differing_at_other_primes=o["differing_at_other_primes"])

def exact_table(eps, word, N):
    os.environ["OA_CYC"] = str(N)
    import importlib, exact_lib
    E = importlib.reload(exact_lib)
    ng, rels, mu, lam, tau, A, tors = ac.level(eps, word, 1)
    saved = cc.cover; cc.cover = lambda _n: (ng, rels, mu, lam, tau)
    try:
        chars = cc.characters(rels, mu, ng, N); exact = {}
        for lc in chars:
            for al in chars:
                i = E.exact_index(1, N, lc, al)
                if i: exact[(lc, al)] = i
        o, bgs, I, _, _ = cc.census(1, N, 3000, verbose=False)
    finally: cc.cover = saved
    return dict(state=("+" if eps > 0 else "-") + word, field=f"Q(zeta_{N})", candidates=len(chars) ** 2, firing_exact=len(exact),
                identical_to_prime_field_table=(exact == I), generation_backgrounds=o["generation_backgrounds"])

out = dict(snappy=[on_snappy_presentation("m369", 12, 9000), on_snappy_presentation("s639", 15, 9000),
                   on_snappy_presentation("m004", 1, 9000), on_snappy_presentation("m003", 5, 9000)],
           exact=[exact_table(-1, "LLRLR", 12), exact_table(-1, "LLLRLR", 15)])
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "own_level_checks.json", "w"), indent=1)
