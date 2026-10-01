#!/usr/bin/env python3
"""THE SEVERAL-CUSPED LEVELS: main's class index of the frame's rank-two non-split modules on manifolds with more than
one cusp.

MANIFOLDS.  (a) every connected cover of degree 2..6 with at least two cusps of m004, m003, m009, m010 (the four
smallest word states), in SnapPy's order;  (b) m202, s959, o10_150726, m129, m125.
CHARACTERS.  Hom(H_1(M), mu_N),  N = max(exponent of the torsion of H_1(M), 2)  (tier 1);  for the five manifolds of
(b) also N = 12 (tier 2, the group B1418 used).  A manifold with more than MAXCHARS characters is skipped and listed.
MODULES.  V(l, alpha) = [[alpha, c beta], [0, beta]], beta = alpha / l, for l non-trivial with H^1(M; l) != 0 and
alpha, beta non-trivial; c runs over a basis of H^1(M; l) and, when its dimension exceeds one, two random combinations.
INDEX.  main's B1333 code (`mc_lib.check`): I = n(V) - n(V*), every identity asserted on every module; the cusp data
(which cusps are live for V and for V*) recorded for every module with I != 0.
Every module with |I| >= 2 is recomputed at two further primes.
"""
import sys, json, itertools, math, pathlib, warnings, collections, random, time
warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1333_the_index_on_several_cusps" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1432_the_three_fold_cover_fires_off_the_lift" / "verification"))
import mc_lib
from index_lib import rank, nullspace
import cover_census as cc
MAXCHARS = 600
ROOTS = ("m004", "m003", "m009", "m010"); NAMED = ("m202", "s959", "o10_150726", "m129", "m125")

def toint(w): return [(ord(ch) - 96) if ch.islower() else -(ord(ch) - 64) for ch in w]

def group_data(C):
    G = C.fundamental_group(); gens = list(G.generators()); rels = list(G.relators())
    per = [tuple(pc) for pc in G.peripheral_curves()]
    return gens, rels, per

def homology(gens, rels):
    ng = len(gens); A = [cc.expvec(toint(r), ng) for r in rels]; diag, V = cc.smith_cols(A, ng)
    tors = [d for d in diag if d > 1]; N = 1
    for d in tors: N = N * d // math.gcd(N, d)
    return ng - len(diag), tors, N

def characters(gens, rels, N):
    """all characters of the group with values in mu_N, as exponent vectors on the generators"""
    ng = len(gens); words = [toint(r) for r in rels]
    A = [cc.expvec(w, ng) for w in words]; diag, V = cc.smith_cols(A, ng); ranges = []
    for i in range(ng):
        if i < len(diag): ranges.append(range(0, N, N // math.gcd(diag[i], N)))
        else: ranges.append(range(N))
    out = set()
    for y in itertools.product(*ranges):
        x = tuple(sum(V[i][j] * y[j] for j in range(ng)) % N for i in range(ng)); out.add(x)
    out = sorted(out)
    for x in out:
        for a in A: assert sum(p_ * q_ for p_, q_ in zip(a, x)) % N == 0
    return out

def classes(gens, rels, vals, p):
    ng = len(gens); rho = {g: [[vals[i]]] for i, g in enumerate(gens)}
    J = [[mc_lib.fox(r, g, rho, p, 1)[0][0] for g in gens] for r in rels]
    Z = nullspace(J, p, ng); b = [(v - 1) % p for v in vals]; cur = [b] if any(b) else []; rk = rank(cur, p) if cur else 0; out = []
    for z in Z:
        r2 = rank(cur + [z], p)
        if r2 > rk: cur.append(z); rk = r2; out.append(z)
    return out

def module(gens, val_al, val_be, ct, p):
    return {g: [[val_al[i], ct[i] * val_be[i] % p], [0, val_be[i]]] for i, g in enumerate(gens)}

def census(C, N=None, pstart=3000, seed=1):
    t0 = time.time(); gens, rels, per = group_data(C); ng = len(gens); b1, tors, Nt = homology(gens, rels)
    N = max(Nt, 2) if N is None else N
    nchar = (N ** b1) * math.prod(math.gcd(d, N) for d in tors)
    base = dict(cusps=len(per), b1=b1, torsion=tors, N=N, characters=nchar)
    if nchar > MAXCHARS: return dict(base, skipped="more than %d characters" % MAXCHARS)
    P = cc.primes_1mod(N, 3, pstart); p = P[0]; zeta = {q: pow(cc.primroot(q), (q - 1) // N, q) for q in P}
    chars = characters(gens, rels, N); assert len(chars) == nchar, (len(chars), nchar); triv = tuple([0] * ng)
    val = {q: {c: [pow(zeta[q], e % N, q) for e in c] for c in chars} for q in P}
    H = {c: classes(gens, rels, val[p][c], p) for c in chars}
    rnd = random.Random(seed); hist = collections.Counter(); wit = []; nmod = 0; live_hist = collections.Counter(); recheck_bad = 0
    for lc in chars:
        if lc == triv or not H[lc]: continue
        m = len(H[lc]); combos = [[int(i == j) for j in range(m)] for i in range(m)]
        if m > 1: combos += [[rnd.randrange(1, 50) for _ in range(m)] for _ in range(2)]
        for al in chars:
            be = tuple((a - b) % N for a, b in zip(al, lc))
            if al == triv or be == triv: continue
            for co in combos:
                ct = [sum(k * z[i] for k, z in zip(co, H[lc])) % p for i in range(ng)]
                A_, B_, ids = mc_lib.check(gens, rels, per, module(gens, val[p][al], val[p][be], ct, p), p, 2); nmod += 1
                assert all(ids.values()), ("identity failed", ids)
                I = A_["I_exact"]; hist[I] += 1
                if I:
                    live_hist[(abs(I), tuple(A_["t0s"]), tuple(B_["t0s"]))] += 1
                if abs(I) >= 2:
                    same = []
                    for q in P[1:]:
                        Hq = classes(gens, rels, val[q][lc], q)
                        if len(Hq) != m: same.append(None); continue
                        ctq = [sum(k * z[i] for k, z in zip(co, Hq)) % q for i in range(ng)]
                        Aq, Bq, idq = mc_lib.check(gens, rels, per, module(gens, val[q][al], val[q][be], ctq, q), q, 2)
                        same.append(Aq["I_exact"])
                    # with h^1 > 1 the classes at another prime are another basis: only m == 1 is a like-for-like recheck
                    if m == 1 and any(s != I for s in same): recheck_bad += 1
                    wit.append(dict(I=I, l=list(lc), alpha=list(al), combo=co, h1_l=m, t0s=A_["t0s"], t0s_dual=B_["t0s"],
                                    n=A_["n"], n_dual=B_["n"], a1=A_["a1"], r1=A_["r1"], other_primes=same))
    return dict(base, primes=P, h1_hist={str(k): v for k, v in sorted(collections.Counter(len(v) for v in H.values()).items())},
                modules=nmod, I_hist={str(k): v for k, v in sorted(hist.items())}, max_abs_I=max([abs(k) for k in hist] or [0]),
                firing_by_live_cusps={"|I|=%d live %s dual %s" % k: v for k, v in sorted(live_hist.items())},
                witnesses_abs_I_ge_2=len(wit), witnesses=wit[:12], rechecks_differing=recheck_bad, seconds=round(time.time() - t0, 1))

def population():
    out = []
    for name in ROOTS:
        M = snappy.Manifold(name)
        for d in range(2, 7):
            for i, C in enumerate(M.covers(d)):
                if C.num_cusps() >= 2: out.append(("%s deg %d #%d" % (name, d, i), name, d, i, None))
    for name in NAMED:
        out.append((name, name, None, None, None)); out.append((name + " N=12", name, None, None, 12))
    return out

def get(name, d, i): return snappy.Manifold(name) if d is None else snappy.Manifold(name).covers(d)[i]

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "control":                                    # one-cusped levels whose answers are banked (B1432)
        for n, expect in ((2, 8), (3, 72)):
            C = snappy.Manifold("m004").covers(n, cover_type="cyclic")[0]; gens, rels, per = group_data(C)
            # the banked census used characters trivial on the cusp: here all characters of order | N, so count those
            r = census(C); print("control M%d: cusps %d N %d characters %d modules %d I-histogram %s max|I| %d" % (n, r["cusps"], r["N"], r["characters"], r["modules"], r["I_hist"], r["max_abs_I"]), flush=True)
            assert r["max_abs_I"] == 1                       # B1440: one cusp, rank two
        print("size:", len(population()), "entries;", collections.Counter(get(nm, d, i).num_cusps() for tag, nm, d, i, N in population() if N is None))
        print("CONTROL OK")
    elif mode == "run":                                      # run <slice> <nslices> <outdir>
        sl, ns, outdir = int(sys.argv[2]), int(sys.argv[3]), pathlib.Path(sys.argv[4]); res = []
        for k, (tag, nm, d, i, N) in enumerate(population()):
            if k % ns != sl: continue
            C = get(nm, d, i); r = census(C, N=N); r.update(tag=tag, root=nm, degree=d, index_in_snappy_list=i, homology=str(C.homology()), volume=round(float(C.volume()), 8))
            res.append(r)
            print(tag, "cusps", r["cusps"], "chars", r["characters"], r.get("skipped") or ("modules %d I %s max %d" % (r["modules"], r["I_hist"], r["max_abs_I"])), flush=True)
            json.dump(res, open(outdir / ("several_cusps_%d.json" % sl), "w"), indent=1)
