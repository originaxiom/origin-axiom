#!/usr/bin/env python3
"""THE CENSUS BY SLOPE: the generation-shaped backgrounds of a level and their couplings, from the slope function
alone (B1438), fast enough for every signed word state to length twelve.

For a level (eps, word, k):
  * the monodromy-fixed characters of the fibre (Smith form, B1432's `characters`);
  * s(chi) from its definition, modulo two primes above 2*10^9 (classes of equal slope = equal at both);
  * the index of every candidate module by the firing law, the backgrounds as in B1432's census;
  * for every background and every allowed pair of firing sectors, whether the coupling s(l) - s(eta) vanishes.
Nothing here computes an index or a cup product; B1438 proved the two laws and verified them on B1434 and B1435.
"""
import sys, json, itertools, math, pathlib, time
from collections import Counter, defaultdict
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1434_the_architecture_census" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1438_the_slope_law" / "verification"))
import architecture_census as ac
import slope_census as sc
cc = ac.cc
SECT = [s[0] for s in cc.SECT]; CH = {s[0]: (s[1], s[2]) for s in cc.SECT}
SPIN0 = {(1, -2), (-4, -2), (6, -2), (-2, 4), (3, 4), (-1, 2), (4, 2), (-6, 2), (2, -4), (-3, -4), (0, 0), (-5, 0), (5, 0), (-2, -6), (3, -6), (2, 6), (-3, 6)}
PAIRS = [(A, B) for A, B in itertools.combinations_with_replacement(SECT, 2) if (-(CH[A][0] + CH[B][0]), -(CH[A][1] + CH[B][1])) in SPIN0]
BLOCK = {}
for A, B in PAIRS:
    t = lambda s: "ten" if s in ("Q", "uc", "ec") else ("five" if s in ("dc", "L") else "nu")
    BLOCK[(A, B)] = t(A) + "." + t(B)

def mat(eps, w):
    A = [[1, 0], [0, 1]]
    for ch in w:
        M = [[1, 1], [0, 1]] if ch == "L" else [[1, 0], [1, 1]]
        A = [[A[0][0] * M[0][0] + A[0][1] * M[1][0], A[0][0] * M[0][1] + A[0][1] * M[1][1]], [A[1][0] * M[0][0] + A[1][1] * M[1][0], A[1][0] * M[0][1] + A[1][1] * M[1][1]]]
    return [[eps * v for v in r] for r in A]
def mpow(A, k):
    R = [[1, 0], [0, 1]]
    for _ in range(k): R = [[R[0][0] * A[0][0] + R[0][1] * A[1][0], R[0][0] * A[0][1] + R[0][1] * A[1][1]], [R[1][0] * A[0][0] + R[1][1] * A[1][0], R[1][0] * A[0][1] + R[1][1] * A[1][1]]]
    return R
def torsion(eps, w, k):
    P = mpow(mat(eps, w), k); return abs((P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0])

def census(eps, word, k):
    t0 = time.time()
    r, bgs, cls = sc.slope_census(eps, word, k); N = r["N"]
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); neg = lambda x: ((-x[0]) % N, (-x[1]) % N); triv = (0, 0)
    pats = Counter(); blocks = Counter(); mixed = 0; yuk = Counter()
    for key, cnt in bgs.items():
        lc = key[0]; al = dict(zip(SECT, key[1:])); sg = cnt[0]; fire = [s for s, c in zip(SECT, cnt) if c == sg]
        nz = {}
        for A, B in PAIRS:
            if A not in fire or B not in fire: continue
            eta = add(add(al[A], al[B]), neg(lc)); eta = neg(eta) if sg > 0 else eta
            nz[(A, B)] = True if eta == triv else (cls[eta] != cls[lc])
        bl = defaultdict(set)
        for pr, v in nz.items(): bl[BLOCK[pr]].add(v)
        mixed += any(len(v) > 1 for v in bl.values())
        sig = tuple(sorted((b, ("Y" if True in v else "") + ("0" if False in v else "")) for b, v in bl.items()))
        pats[sig] += 1
        for b, v in bl.items():
            for x in v: blocks[(b, x)] += 1
        yuk[(nz[("Q", "uc")], nz[("Q", "dc")], nz[("ec", "L")], nz.get(("L", "nuc")))] += 1
    r.update(patterns={json.dumps(k_): v for k_, v in pats.items()}, blocks={"%s:%s" % k_: v for k_, v in blocks.items()},
             backgrounds_with_a_mixed_block=mixed, yukawa_type={json.dumps(k_): v for k_, v in yuk.items()},
             torsion=r["characters"], seconds=round(time.time() - t0, 1))
    return r

def population(maxlen, tmax, kmax=12):
    out = []
    for w in ac.states(maxlen):
        for eps in (1, -1):
            for k in range(1, kmax + 1):
                t = torsion(eps, w, k)
                if 0 < t <= tmax: out.append((eps, w, k, t))
    return out

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "control":                                   # the 68 levels of B1434, and the couplings of B1435's sealed run
        rec = json.load(open(HERE.parents[1] / "B1434_the_architecture_census" / "verification" / "architecture_census.json"))
        summ = json.load(open(HERE.parents[1] / "B1435_the_interaction_census" / "verification" / "interaction_census_summary.json"))
        b1435 = {(l["state"], l["k"]): l for l in summ["per_level"]}; cols = summ["pattern_columns"]
        bad = 0; n = 0; cbad = 0; cn = 0
        for o in rec:
            if "candidates" not in o: continue
            eps = 1 if o["state"][0] == "+" else -1; r = census(eps, o["state"][1:], o["k"]); n += 1
            norm = lambda v: {str(a): b for a, b in v.items()} if isinstance(v, dict) else v
            d = [f for f in sc.FIELDS if norm(r[f]) != norm(o[f])]; bad += bool(d)
            if (o["state"], o["k"]) in b1435:
                cn += 1
                # block totals of the sealed run against the slope census
                tot = Counter()
                for pat, c in b1435[(o["state"], o["k"])]["patterns"].items():
                    for name, ch in zip(cols, pat):
                        A, B = name.split("."); tot[(BLOCK[(A, B)], ch == "Y")] += c
                mine = Counter()
                r2, bgs, cls = sc.slope_census(eps, o["state"][1:], o["k"]); N = r2["N"]
                add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); neg = lambda x: ((-x[0]) % N, (-x[1]) % N)
                for key, cnt in bgs.items():
                    lc = key[0]; al = dict(zip(SECT, key[1:])); sg = cnt[0]
                    for name in cols:
                        A, B = name.split("."); eta = add(add(al[A], al[B]), neg(lc)); eta = neg(eta) if sg > 0 else eta
                        mine[(BLOCK[(A, B)], True if eta == (0, 0) else cls[eta] != cls[lc])] += 1
                cbad += (tot != mine)
            print(o["state"], o["k"], "OK" if not d else "DIFF %s" % d, flush=True)
        print("control: levels", n, "differing", bad, "; coupling levels", cn, "differing", cbad)
    elif mode == "size":
        pop = population(int(sys.argv[2]), int(sys.argv[3])); print(len(pop), Counter(k for _, _, k, _ in pop))
    elif mode == "run":                                     # run <maxlen> <tmax> <slice> <nslices> <outdir>
        maxlen, tmax, sl, ns, outdir = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), pathlib.Path(sys.argv[6])
        pop = sorted(population(maxlen, tmax), key=lambda t: (t[3], t[1], t[0], t[2])); res = []
        for i, (eps, w, k, t) in enumerate(pop):
            if i % ns != sl: continue
            r = census(eps, w, k); res.append(r)
            print(r["state"], k, "tors", t, "N", r["N"], "firing", r["firing"], "gen", r["generation_backgrounds"], "lifted", r["lifted"],
                  "orbits", r["backgrounds_by_orbit_size"], "yuk", r["yukawa_type"], "sec", r["seconds"], flush=True)
            json.dump(res, open(outdir / ("census_by_slope_%d.json" % sl), "w"))
