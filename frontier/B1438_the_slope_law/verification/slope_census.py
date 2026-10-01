#!/usr/bin/env python3
"""The architecture census from the slope function alone.

No index is computed here.  The slope s(chi) of every monodromy-fixed character is computed from its definition modulo
two large primes; the firing law gives the index of every candidate module,
        I(l, alpha) = [s(alpha) = s(l)] - [s(1/beta) = s(l)]     (l, alpha, beta = alpha/l non-trivial; else 0),
and the backgrounds are assembled exactly as in B1432's census.  The result is compared, field by field, with B1434's
record (computed with main's index code at three small primes).
"""
import sys, json, itertools, math, pathlib, time
from collections import Counter, defaultdict
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1434_the_architecture_census" / "verification"))
import architecture_census as ac
cc = ac.cc
SECT = cc.SECT

def big_primes(N, count=2, start=2 * 10 ** 9):
    out = []; q = start - (start % N) + 1
    while len(out) < count:
        q += N
        if sympy_isprime(q): out.append(q)
    return out
def sympy_isprime(q):
    import sympy
    return sympy.isprime(q)

def fixed_characters(Phi, N, rels):
    """the characters (i, j) of the fibre fixed by the monodromy: the characters of the level trivial on the meridian
    (Smith form, B1432's `characters`), each checked against the definition"""
    ex = lambda w: (sum((q == 1) - (q == -1) for q in w), sum((q == 2) - (q == -2) for q in w))
    px, py = ex(Phi[1]), ex(Phi[2]); out = []
    for c in cc.characters(rels, [ac.T], 3, N):
        i, j, t = c; assert t == 0
        assert (px[0] * i + px[1] * j - i) % N == 0 and (py[0] * i + py[1] * j - j) % N == 0, "fixed by the monodromy"
        out.append((i, j))
    return out

def slopes_mod_p(Phi, N, p, chars):
    """{(i, j): s mod p} for the non-trivial monodromy-fixed characters; zeta a primitive N-th root of unity mod p"""
    g = cc.primroot(p); zeta = pow(g, (p - 1) // N, p); out = {}
    inv = lambda v: pow(v, p - 2, p)
    for i, j in chars:
        if (i, j) == (0, 0): continue
        val = {1: pow(zeta, i, p), 2: pow(zeta, j, p)}; val[-1] = inv(val[1]); val[-2] = inv(val[2])
        u = {1: 0, 2: inv(val[1] - 1)} if i % N else {1: inv(1 - val[2]), 2: 0}
        def ev(w):
            tot = 0; pre = 1
            for q in w:
                if q > 0: tot = (tot + pre * u[q]) % p; pre = pre * val[q] % p
                else: pre = pre * val[q] % p; tot = (tot - pre * u[-q]) % p
            return tot
        assert ev((1, 2, -1, -2)) == 1
        gq = 1 if i % N else 2
        out[(i, j)] = (u[gq] - ev(Phi[gq])) * inv(val[gq] - 1) % p
    return out

def slope_census(eps, word, k):
    ng, rels, mu, lam, tau, A, tors = ac.level(eps, word, k); N = max(1, ac.torsion_exponent(A))
    phi = ac.monodromy(eps, word); P = ac.IDENT
    for _ in range(k): P = ac.compose(phi, P)
    Phi = {1: tuple(P[ac.X]), 2: tuple(P[ac.Y])}
    fixed = fixed_characters(Phi, N, rels)
    primes = big_primes(N); Sp = [slopes_mod_p(Phi, N, p, fixed) for p in primes]
    chars = [(0, 0)] + sorted(Sp[0]); assert len(chars) == tors == len(fixed), (len(chars), tors)
    # slope classes: equal at both primes
    cls = {c: (Sp[0][c], Sp[1][c]) for c in Sp[0]}
    one_prime_only = sum(1 for a, b in itertools.combinations(sorted(Sp[0]), 2) if (Sp[0][a] == Sp[0][b]) != (Sp[1][a] == Sp[1][b])) if len(chars) <= 400 else None
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); mul = lambda x, m: ((m * x[0]) % N, (m * x[1]) % N); triv = (0, 0)
    I = {}
    for lc in chars:
        if lc == triv: continue
        for al in chars:
            be = add(al, mul(lc, -1))
            if al == triv or be == triv: continue
            v = int(cls[al] == cls[lc]) - int(cls[mul(be, -1)] == cls[lc])
            if v: I[(lc, al)] = v
    squares = set(mul(c, 2) for c in chars)
    S = defaultdict(dict)
    for (lc, al), i in I.items(): S[lc][al] = i
    fifth = defaultdict(list)
    for c in chars: fifth[mul(c, 5)].append(c)
    bgs = {}
    for lc, Sl in S.items():
        for ad, Id in Sl.items():
            for aL, IL in Sl.items():
                if Id != IL: continue
                for pY in fifth.get(add(ad, mul(aL, -1)), []):
                    th = add(ad, mul(pY, -2)); Wc = add(mul(th, 2), mul(lc, -1)); al_s = []
                    for (lab, sy, sg) in SECT: al_s.append(add(add(th, mul(pY, sy)), mul(Wc, (sg - 1) // 2)))
                    cnt = tuple(Sl.get(a, 0) for a in al_s)
                    if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] != 0: bgs[(lc,) + tuple(al_s)] = cnt
    # the deck: chi -> chi o phi  (the level's deck generator), on exponents
    ex = lambda w: (sum((q == 1) - (q == -1) for q in w), sum((q == 2) - (q == -2) for q in w))
    dx, dy = ex(phi[ac.X]), ex(phi[ac.Y])
    tch = lambda c: ((dx[0] * c[0] + dx[1] * c[1]) % N, (dy[0] * c[0] + dy[1] * c[1]) % N)
    orbit_sizes = Counter(); seen = set()
    for key in bgs:
        if key in seen: continue
        orb = [key]; kk = tuple(tch(c) for c in key)
        while kk != key: orb.append(kk); kk = tuple(tch(c) for c in kk)
        seen.update(orb); orbit_sizes[len(orb)] += 1
    nuc = Counter((c[5] == c[0], c[5] != 0) for c in bgs.values())
    return dict(state=("+" if eps > 0 else "-") + word, k=k, N=N, primes=primes, characters=len(chars), firing=len(I),
                firing_on_square_loci=sum(1 for (lc, al) in I if lc in squares),
                generation_backgrounds=len(bgs), lifted=sum(1 for kq in bgs if kq[0] in squares),
                signs={str(k_): v for k_, v in Counter(c[0] for c in bgs.values()).items()},
                abs_counts={str(k_): v for k_, v in Counter(abs(c[0]) for c in bgs.values()).items()},
                nuc={"same_sign_as_generation": sum(v for (same, nz), v in nuc.items() if same),
                     "zero": sum(v for (same, nz), v in nuc.items() if not nz),
                     "opposite_sign": sum(v for (same, nz), v in nuc.items() if nz and not same)},
                backgrounds_by_orbit_size={str(k_): k_ * v for k_, v in orbit_sizes.items()},
                slope_classes=len(set(cls.values())), slope_coincidences_at_one_prime_only=one_prime_only), bgs, cls

FIELDS = ["characters", "firing", "generation_backgrounds", "lifted", "signs", "abs_counts", "nuc", "backgrounds_by_orbit_size"]
if __name__ == "__main__":
    rec = json.load(open(HERE.parents[1] / "B1434_the_architecture_census" / "verification" / "architecture_census.json"))
    res = []; bad = 0; t0 = time.time(); tot_mod = 0
    for o in rec:
        if "candidates" not in o: continue
        eps = 1 if o["state"][0] == "+" else -1
        r, _, _ = slope_census(eps, o["state"][1:], o["k"])
        diff = [f for f in FIELDS if json.loads(json.dumps(r[f])) != json.loads(json.dumps({str(a): b for a, b in o[f].items()} if isinstance(o[f], dict) else o[f]))]
        r["agrees_with_B1434"] = not diff; r["differing_fields"] = diff; res.append(r); bad += bool(diff); tot_mod += o["candidates"]
        print(o["state"], o["k"], "chars", r["characters"], "firing", r["firing"], o["firing"], "gen", r["generation_backgrounds"], o["generation_backgrounds"],
              "OK" if not diff else "DIFF %s" % diff, flush=True)
    print("levels", len(res), "candidate modules covered", tot_mod, "levels differing", bad, "seconds", round(time.time() - t0, 1))
    json.dump(res, open(HERE / "slope_census.json", "w"), indent=1)
