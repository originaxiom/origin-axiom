#!/usr/bin/env python3
"""Second presentation: SnapPy's own presentation of the cyclic covers (as main's B1427 used), same census code.
The deck is not computed here (tau = identity placeholder), so only the counts are read."""
import sys, json, warnings
warnings.filterwarnings("ignore")
import snappy
import cover_census as cc
def toint(w): return [(ord(ch) - ord('a') + 1) if ch.islower() else -(ord(ch) - ord('A') + 1) for ch in w]
res = {}
for (n, N, pstart) in eval(sys.argv[1]):
    Y = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]
    G = Y.fundamental_group(); gens = list(G.generators()); ng = len(gens)
    rels = [toint(r) for r in G.relators()]; mu, lam = [toint(w) for w in G.peripheral_curves()[0]]
    # characters trivial on the whole cusp: use mu*lam-row trick by appending lam to the relators for the character
    # enumeration only (the module relators stay the true ones).
    true_cover = cc.cover
    def fake_cover(_n, rels=rels, mu=mu, lam=lam, ng=ng):
        return ng, rels, mu, lam, {g: [g] for g in range(1, ng + 1)}
    true_chars = cc.characters
    def chars_cusp(rels_, mu_, ng_, N_, lam=lam):
        A = true_chars(rels_, mu_, ng_, N_)
        return [c for c in A if sum(e * x for e, x in zip(cc.expvec(lam, ng_), c)) % N_ == 0]
    cc.cover = fake_cover; cc.characters = chars_cusp
    o, bgs, I, chars, _ = cc.census(n, N, pstart, verbose=False)
    cc.cover = true_cover; cc.characters = true_chars
    res["M%d" % n] = {k: o[k] for k in ("primes", "characters", "loci", "loci_nonsquare", "candidates", "firing",
                                        "firing_on_square_loci", "firing_on_nonsquare_loci", "differing_at_other_primes",
                                        "generation_backgrounds", "lifted", "not_lifted", "signs", "abs_counts", "nuc")}
    res["M%d" % n]["H1"] = str(Y.homology()); res["M%d" % n]["census_name"] = str(Y.identify()[:1])
    print("M%d" % n, json.dumps(res["M%d" % n]), flush=True)
json.dump(res, open(sys.argv[2], 'w'), indent=1)
