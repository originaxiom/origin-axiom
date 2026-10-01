#!/usr/bin/env python3
"""The value law on every generation-shaped background, with the backgrounds taken from the slope census (no index
is computed):   Y(A, B) = (n_A n_B h(lam) / c(lam)) (s(l) - s(eta))   at a prime, pair by pair, both signs;
with every class normalised on the longitude this reads  Y = s(l) - s(eta).
Y is computed by B1435's sealed instrument (relcup.py, interaction_census.py); the slopes by slope_census.py."""
import sys, json, itertools, pathlib, time, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1435_the_interaction_census" / "verification"))
import interaction_census as ic
from relcup import Bundle, Cocycle, relative_lift, X, Y
import slope_census as sc
cc = ic.cc

def value_law(eps, word, k, pstart=3000):
    r, bgs2, cls = sc.slope_census(eps, word, k); N = r["N"]
    ng, rels, mu, lam_w, tau, A, tors = ic.ac.level(eps, word, k)
    p = cc.primes_1mod(N, 1, pstart)[0]; zeta = pow(cc.primroot(p), (p - 1) // N, p); inv = lambda v: pow(v, p - 2, p)
    B = Bundle(ic.Phi_of(eps, word, k)); C, z, _ = B.fundamental(); plan = ic.Plan(B, C, z); lam = (B.lam, 0)
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x); triv = (0, 0, 0)
    H = {}; ok = tot = zero = 0; cache = {}; last = None
    def hig(c):
        if c not in H:
            Vh = ic.char_module(B, c, N, zeta, p); hs = ic.classes(Vh); assert len(hs) == 1
            H[c] = (ic.Evaluator(Vh, hs[0], plan), hs[0])
        return H[c]
    for key2, cnt in sorted(bgs2.items()):
        key = tuple(c + (0,) for c in key2); lc = key[0]; al = dict(zip(ic.SECT, key[1:])); sg = cnt[0]
        if lc != last: cache = {}; last = lc
        h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p); assert ct is not None
        cco = Cocycle(ic.char_module(B, lc, N, zeta, p), [ct[0]], [ct[1]], [ct[2]]); cl = cco(lam)[0]; sl = cco.vt[0] * inv(cl) % p
        E = {}
        for s_, c_ in zip(ic.SECT, cnt):
            if c_ != sg: continue
            ck = (al[s_], sg)
            if ck not in cache:
                V = ic.my_module(B, lc, al[s_], ct, N, zeta, p, dual=(sg < 0)); reps = ic.classes(V); assert len(reps) == 1
                a = reps[0]; e = relative_lift(a); assert e is not None, "the class of a firing sector is interior"
                q, sub = (1, 0) if sg > 0 else (0, 1)
                qc = add(al[s_], neg(lc)) if sg > 0 else neg(al[s_])
                qx = pow(zeta, qc[0] % N, p); qy = pow(zeta, qc[1] % N, p)
                v = a.v[X][q] * inv(qx - 1) % p if (qx - 1) % p else a.v[Y][q] * inv(qy - 1) % p
                nrm = (a(lam)[sub] - (cl if sg > 0 else -cl) * v) % p
                cache[ck] = (ic.Evaluator(V, a, plan), e, nrm)
            E[s_] = cache[ck]
        for A_, B_ in itertools.combinations_with_replacement([s_ for s_ in ic.SECT if s_ in E], 2):
            eta = add(add(al[A_], al[B_]), neg(lc)); eta = neg(eta) if sg > 0 else eta
            Eh, h = hig(eta); hl = h(lam)[0]
            Yv = ic.Yfast(plan, E[A_][0], E[B_][0], Eh, E[A_][1], p)
            if eta == triv: pred = (-E[A_][2] * E[B_][2] * h.vt[0] * inv(cl)) % p
            else: pred = E[A_][2] * E[B_][2] % p * hl % p * inv(cl) % p * ((sl - h.vt[0] * inv(hl)) % p) % p
            tot += 1; ok += (Yv == pred); zero += (Yv == 0)
    return dict(state=r["state"], k=k, N=N, prime=p, backgrounds=len(bgs2), pairs=tot, value_law_holds=ok, zero_couplings=zero, cells=len(C))

if __name__ == "__main__":
    sl, ns = int(sys.argv[1]), int(sys.argv[2]); outdir = pathlib.Path(sys.argv[3])
    rec = json.load(open(HERE.parents[1] / "B1434_the_architecture_census" / "verification" / "architecture_census.json"))
    pop = sorted([(o["state"], o["k"], o["generation_backgrounds"]) for o in rec if o.get("generation_backgrounds")], key=lambda t: t[2])
    for i, (st, k, nb) in enumerate(pop):
        if i % ns != sl: continue
        t0 = time.time(); r = value_law(1 if st[0] == "+" else -1, st[1:], k); r["seconds"] = round(time.time() - t0, 1)
        assert r["backgrounds"] == nb
        print(json.dumps(r), flush=True)
        json.dump(r, open(outdir / ("value_%s_%d.json" % (st.replace("+", "p").replace("-", "m"), k)), "w"))
