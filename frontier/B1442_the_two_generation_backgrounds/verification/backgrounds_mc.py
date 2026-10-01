#!/usr/bin/env python3
"""Generation-shaped backgrounds on manifolds with several cusps.

A background is (l, c, theta, psi_Y, W): an extension character l = theta^2 / W with a class c of H^1(M; l), and the
six sector modules V(l, alpha_s), alpha_s = theta psi_Y^{s_Y} W^{(s_g - 1)/2} (B1432's frame, unchanged).  It is
GENERATION-SHAPED OF COUNT g when its five charged sectors all have class index g != 0.  On one cusp |g| = 1 always
(B1440).  The index is B1333's several-cusp code, as in B1441.

When H^1(M; l) has dimension m > 1 the class matters.  Classes tried: the m basis classes, and three seeded random
combinations (a generic class); the class is part of the background's name.
"""
import sys, json, itertools, math, pathlib, warnings, collections, random, time
warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1441_the_several_cusped_levels" / "verification"))
import several_cusps as sc
mc_lib, cc = sc.mc_lib, sc.cc
SECT = cc.SECT

def backgrounds(C, N=None, pstart=3000, seed=1):
    t0 = time.time(); gens, rels, per = sc.group_data(C); ng = len(gens); b1, tors, Nt = sc.homology(gens, rels)
    N = max(Nt, 2) if N is None else N
    P = cc.primes_1mod(N, 1, pstart); p = P[0]; zeta = pow(cc.primroot(p), (p - 1) // N, p)
    chars = sc.characters(gens, rels, N); triv = tuple([0] * ng)
    val = {c: [pow(zeta, e % N, p) for e in c] for c in chars}
    H = {c: sc.classes(gens, rels, val[c], p) for c in chars}
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); mul = lambda x, k: tuple((k * a) % N for a in x)
    fifth = collections.defaultdict(list)
    for c in chars: fifth[mul(c, 5)].append(c)
    rnd = random.Random(seed); bgs = {}; firing = 0; maxI = 0
    for lc in chars:
        if lc == triv or not H[lc]: continue
        m = len(H[lc]); combos = [tuple(int(i == j) for j in range(m)) for i in range(m)]
        if m > 1: combos += [tuple(rnd.randrange(1, 50) for _ in range(m)) for _ in range(3)]
        for co in combos:
            ct = [sum(k * z[i] for k, z in zip(co, H[lc])) % p for i in range(ng)]; Sl = {}
            for al in chars:
                be = add(al, mul(lc, -1))
                if al == triv or be == triv: continue
                A_, B_, ids = mc_lib.check(gens, rels, per, sc.module(gens, val[al], val[be], ct, p), p, 2)
                assert all(ids.values())
                if A_["I_exact"]: Sl[al] = A_["I_exact"]; firing += 1; maxI = max(maxI, abs(A_["I_exact"]))
            for ad, Id in Sl.items():
                for aL, IL in Sl.items():
                    if Id != IL: continue
                    for pY in fifth.get(add(ad, mul(aL, -1)), []):
                        th = add(ad, mul(pY, -2)); Wc = add(mul(th, 2), mul(lc, -1))
                        al_s = [add(add(th, mul(pY, sy)), mul(Wc, (sg - 1) // 2)) for (lab, sy, sg) in SECT]
                        cnt = tuple(Sl.get(a, 0) for a in al_s)
                        if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] != 0: bgs[(lc, co) + tuple(al_s)] = cnt
    by = collections.Counter(c[0] for c in bgs.values()); nu = collections.Counter((c[0], c[5]) for c in bgs.values())
    generic = collections.Counter(c[0] for k, c in bgs.items() if len(H[k[0]]) == 1 or sum(1 for x in k[1] if x) > 1)
    ex = [dict(l=list(k[0]), combo=list(k[1]), h1_l=len(H[k[0]]), alphas=[list(a) for a in k[2:]], counts=list(c)) for k, c in bgs.items() if abs(c[0]) >= 2][:8]
    return dict(cusps=len(per), N=N, prime=p, characters=len(chars), firing_modules_over_classes=firing, max_abs_I=maxI,
                backgrounds=len(bgs), by_count={str(k): v for k, v in sorted(by.items())},
                by_count_generic_class_only={str(k): v for k, v in sorted(generic.items())},
                by_count_and_singlet={"%d,%d" % k: v for k, v in sorted(nu.items())}, examples_abs_count_ge_2=ex, seconds=round(time.time() - t0, 1))

if __name__ == "__main__":
    import snappy
    mode = sys.argv[1]
    if mode == "control":                                    # one-cusped: s961 must give its 48, M4 its 256, all of count +-1
        for n, expect in ((3, 48), (4, 256)):
            r = backgrounds(snappy.Manifold("m004").covers(n, cover_type="cyclic")[0])
            print("control M%d: characters %d backgrounds %d by count %s (banked %d)" % (n, r["characters"], r["backgrounds"], r["by_count"], expect), flush=True)
            assert r["backgrounds"] == expect and set(r["by_count"]) == {"-1", "1"}
        print("CONTROL OK")
    elif mode == "run":                                      # run <slice> <nslices> <outdir>: the seventeen carriers of B1441
        sl, ns, outdir = int(sys.argv[2]), int(sys.argv[3]), pathlib.Path(sys.argv[4])
        rows = []
        for i in range(6): rows += json.load(open(HERE.parents[1] / "B1441_the_several_cusped_levels" / "verification" / ("several_cusps_%d.json" % i)))
        car = sorted([r for r in rows if "skipped" not in r and r["max_abs_I"] >= 2], key=lambda r: (r["characters"], r["tag"])); res = []
        for k, r in enumerate(car):
            if k % ns != sl: continue
            o = backgrounds(sc.get(r["root"], r["degree"], r["index_in_snappy_list"])); o.update(tag=r["tag"]); res.append(o)
            print(r["tag"], "cusps", o["cusps"], "chars", o["characters"], "backgrounds", o["backgrounds"], "by count", o["by_count"], "generic class", o["by_count_generic_class_only"], flush=True)
            json.dump(res, open(outdir / ("backgrounds_%d.json" % sl), "w"), indent=1)
