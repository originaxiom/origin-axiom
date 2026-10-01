#!/usr/bin/env python3
"""Independent census of Standard-Model-frame backgrounds on the cyclic covers M_n of m004, WITHOUT the lift.

A background is a flat connection with holonomy in the image G' of SL(2)_beta x U(1)_Y x U(1)_gamma in E6.
E6 contains (SU(2) x SU(6))/Z2 and Q_gamma is odd on every doublet sector, so the pair (x, w_gamma) is defined only
up to a common sign.  Well-defined data: theta = x*w_gamma, psi_Y, W = w_gamma^2, with extension character
lambda = theta^2 / W.  Sector s with charges (s_Y, s_g), s_g odd:
    alpha_s = theta * psi_Y^{s_Y} * W^{(s_g - 1)/2},   beta_s = alpha_s / lambda,
and the sector module is the non-split extension [[alpha_s, u],[0, beta_s]].
The background lifts to SL(2) x U(1)^2 iff W (equivalently lambda) is a square.

Own code: own Reidemeister-Schreier, own Smith form, main's B1427 index code (myindex.py), own primes.
"""
import sys, json, time, itertools, pathlib
from collections import Counter, defaultdict
REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'frontier/B1427_the_towers_generation_count_verified/verification'))
from myindex import Mod, index, rank_and_null

SECT = [("Q", 1, 3), ("uc", -4, 3), ("ec", 6, 3), ("dc", 2, 1), ("L", -3, 1), ("nuc", 0, -5)]

# ------------------------------------------------------------------ m004 and its cyclic covers
# pi_1(m004) = <a, b | a w b^-1 w^-1>, w = b a^-1 b^-1 a ; meridian a ; longitude w w*, w* = a b^-1 a^-1 b
W_ = [2, -1, -2, 1]
REL = [1] + W_ + [-2] + [-x for x in reversed(W_)]
LONG = W_ + [1, -2, -1, 2]

def schreier(word, n, k=0):
    """Rewrite a word in a,b read from coset a^k into Schreier generators of ker(pi_1 -> Z/n):
    1 = z = a^n ; 2+k = y_k = a^k b a^-(k+1) for k < n-1 and y_{n-1} = a^{n-1} b."""
    out = []
    for L in word:
        if L == 1:
            if k == n - 1: out.append(1)
            k = (k + 1) % n
        elif L == -1:
            k = (k - 1) % n
            if k == n - 1: out.append(-1)
        elif L == 2:
            out.append(2 + k); k = (k + 1) % n
        else:
            k = (k - 1) % n; out.append(-(2 + k))
    return out, k

def base_word(g, n):
    if g == 1: return [1] * n
    k = g - 2
    return [1] * k + [2] + ([-1] * (k + 1) if k < n - 1 else [])

def letters(word):
    return ''.join(chr(ord('a') + L - 1) if L > 0 else chr(ord('A') - L - 1) for L in word)

def cover(n):
    ng = n + 1
    for g in range(1, ng + 1):
        assert schreier(base_word(g, n), n, 0) == ([g], 0), g
    rels = [schreier(REL, n, k)[0] for k in range(n)]
    lam, kend = schreier(LONG, n, 0); assert kend == 0
    tau = {}
    for g in range(1, ng + 1):
        w, kend = schreier([1] + base_word(g, n) + [-1], n, 0); assert kend == 0
        tau[g] = w
    return ng, rels, [1], lam, tau

def expvec(word, ng):
    v = [0] * ng
    for L in word: v[abs(L) - 1] += 1 if L > 0 else -1
    return v

# ------------------------------------------------------------------ Smith form with the column transform
def smith_cols(A, ncols):
    """Return (diag, V): V unimodular (ncols x ncols), and the solutions of A x = 0 mod N are x = V y with
    diag[i]*y_i = 0 mod N for i < len(diag) and y_i free beyond."""
    A = [list(r) for r in A]; m = len(A)
    V = [[1 if i == j else 0 for j in range(ncols)] for i in range(ncols)]
    def colop(j, i, q):                     # col_j -= q * col_i
        for r in A: r[j] -= q * r[i]
        for r in V: r[j] -= q * r[i]
    def colswap(i, j):
        for r in A: r[i], r[j] = r[j], r[i]
        for r in V: r[i], r[j] = r[j], r[i]
    diag = []; t = 0
    while t < min(m, ncols):
        piv = None
        for i in range(t, m):
            for j in range(t, ncols):
                if A[i][j] and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])): piv = (i, j)
        if piv is None: break
        A[t], A[piv[0]] = A[piv[0]], A[t]; colswap(t, piv[1])
        while True:
            done = True
            for i in range(t + 1, m):
                if A[i][t]:
                    q = A[i][t] // A[t][t]
                    A[i] = [x - q * y for x, y in zip(A[i], A[t])]
                    if A[i][t]: A[t], A[i] = A[i], A[t]; done = False
            for j in range(t + 1, ncols):
                if A[t][j]:
                    q = A[t][j] // A[t][t]; colop(j, t, q)
                    if A[t][j]: colswap(t, j); done = False
            if done: break
        diag.append(abs(A[t][t])); t += 1
    return diag, V

def characters(rels, mu, ng, N):
    """Characters of pi_1 with values in mu_N and trivial on the meridian, as exponent vectors mod N."""
    A = [expvec(r, ng) for r in rels] + [expvec(mu, ng)]
    diag, V = smith_cols(A, ng)
    ranges = []
    for i in range(ng):
        if i < len(diag):
            d = diag[i]; step = N // __import__('math').gcd(d, N)
            ranges.append(range(0, N, step))
        else:
            ranges.append(range(N))
    out = set()
    for y in itertools.product(*ranges):
        x = tuple(sum(V[i][j] * y[j] for j in range(ng)) % N for i in range(ng))
        out.add(x)
    out = sorted(out)
    for x in out:
        for a in A: assert sum(p * q for p, q in zip(a, x)) % N == 0
    return out

# ------------------------------------------------------------------ fields
def is_prime(q): return q > 1 and all(q % d for d in range(2, int(q ** .5) + 1))
def primes_1mod(N, k, start):
    out = []; q = start
    while len(out) < k:
        q += 1
        if q % N == 1 % N and is_prime(q): out.append(q)
    return out
def primroot(p):
    f = []; m = p - 1; d = 2
    while d * d <= m:
        if m % d == 0:
            f.append(d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: f.append(m)
    return next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in f))

def fox1(word, val, ng, p):
    D = [0] * ng; pre = 1
    for L in word:
        g = abs(L) - 1
        if L > 0: D[g] = (D[g] + pre) % p; pre = pre * val[g] % p
        else: pre = pre * pow(val[g], p - 2, p) % p; D[g] = (D[g] - pre) % p
    return D

def cocycle(lam_exp, rels, ng, N, zeta, p):
    """(h1, a non-coboundary 1-cocycle) for the rank-one character lam."""
    val = [pow(zeta, e % N, p) for e in lam_exp]
    rows = [fox1(r, val, ng, p) for r in rels]
    rk, NS = rank_and_null(rows, ng, p, want_null=True)
    b = [(v - 1) % p for v in val]; rb = 1 if any(b) else 0
    h1 = len(NS) - rb
    for z in NS:
        if rb == 0: return h1, z
        if rank_and_null([b, z], ng, p)[0] == 2: return h1, z
    return h1, None

def module(lam_exp, al_exp, ct, ng, N, zeta, p):
    gens = [chr(ord('a') + i) for i in range(ng)]
    mats = {}
    for i, g in enumerate(gens):
        a = pow(zeta, al_exp[i] % N, p); b = pow(zeta, (al_exp[i] - lam_exp[i]) % N, p)
        mats[g] = [[a, ct[i] * b % p], [0, b]]
    return Mod(gens, mats, p)

# ------------------------------------------------------------------ the census
def census(n, N, pstart, nprimes=3, verbose=True):
    t0 = time.time()
    ng, rels, mu, lam, tau = cover(n)
    L_rels = [letters(r) for r in rels]; L_mu = letters(mu); L_lam = letters(lam)
    chars = characters(rels, mu, ng, N)
    P = primes_1mod(N, nprimes, pstart)
    zeta = {p: pow(primroot(p), (p - 1) // N, p) for p in P}
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y))
    mul = lambda x, k: tuple((k * a) % N for a in x)
    squares = set(mul(c, 2) for c in chars)
    # loci and their cocycles, every prime
    coc = {p: {} for p in P}; h1s = Counter()
    for c in chars:
        hs = []
        for p in P:
            h1, ct = cocycle(c, rels, ng, N, zeta[p], p); hs.append(h1); coc[p][c] = ct
        assert len(set(hs)) == 1, ("h1 differs across primes", c, hs)
        h1s[hs[0]] += 1
    loci = [c for c in chars if coc[P[0]][c] is not None]
    # every candidate module at the first prime
    p = P[0]; I = {}; sig = Counter(); nmod = 0
    for lc in loci:
        for al in chars:
            V = module(lc, al, coc[p][lc], ng, N, zeta[p], p)
            assert V.ok(L_rels), ("not a representation", lc, al)
            i, dV, dVs = index(V, L_rels, L_mu, L_lam); nmod += 1
            if i: I[(lc, al)] = i; sig[(i, dV, dVs)] += 1
    # recheck every firing module at the other primes; and a sample of silent ones
    differ = 0
    for q in P[1:]:
        for (lc, al), i in I.items():
            i2, _, _ = index(module(lc, al, coc[q][lc], ng, N, zeta[q], q), L_rels, L_mu, L_lam)
            if i2 != i: differ += 1
    firing_by_locus = Counter(lc for (lc, al) in I)
    fire_sq = sum(1 for (lc, al) in I if lc in squares)
    # backgrounds
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
                    th = add(ad, mul(pY, -2)); Wc = add(mul(th, 2), mul(lc, -1))
                    al_s = []
                    for (lab, sy, sg) in SECT:
                        al_s.append(add(add(th, mul(pY, sy)), mul(Wc, (sg - 1) // 2)))
                    cnt = tuple(Sl.get(a, 0) for a in al_s)
                    if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] != 0:
                        key = (lc,) + tuple(al_s)
                        if key in bgs: assert bgs[key] == cnt
                        bgs[key] = cnt
    lifted = sum(1 for k in bgs if k[0] in squares)
    signs = Counter(c[0] for c in bgs.values()); nuc = Counter((c[5] == c[0], c[5] != 0) for c in bgs.values())
    # the deck: tau = conjugation by a
    def tchar(c): return tuple(sum(e * x for e, x in zip(expvec(tau[g], ng), c)) % N for g in range(1, ng + 1))
    for c in chars: assert tchar(c) in set(chars)
    inv_ok = all(I.get((tchar(lc), tchar(al)), 0) == i for (lc, al), i in I.items())
    def torbit(key):
        orb = [key]; k = tuple(tchar(c) for c in key)
        while k != key: orb.append(k); k = tuple(tchar(c) for c in k)
        return orb
    seen = set(); orbit_sizes = Counter(); orbit_closed = True
    for key in bgs:
        if key in seen: continue
        orb = torbit(key); seen.update(orb); orbit_sizes[len(orb)] += 1
        if not all(o in bgs and bgs[o] == bgs[key] for o in orb): orbit_closed = False
    mod_orbits = Counter()
    seenm = set()
    for (lc, al) in I:
        if (lc, al) in seenm: continue
        k = (lc, al); orb = [k]; kk = (tchar(lc), tchar(al))
        while kk != k: orb.append(kk); kk = (tchar(kk[0]), tchar(kk[1]))
        seenm.update(orb); mod_orbits[len(orb)] += len(orb)
    # the fence: within an orbit, are the extension characters distinct, and of what order are their ratios?
    def order(c):
        k = 1; x = c
        while any(x): x = add(x, c); k += 1
        return k
    ratio_orders = Counter()
    seen = set()
    for key in bgs:
        if key in seen: continue
        orb = torbit(key); seen.update(orb)
        lams = [o[0] for o in orb]
        ratio_orders[(len(orb), len(set(lams)), tuple(sorted(order(add(lams[i], mul(lams[0], -1))) for i in range(1, len(lams)))))] += 1
    out = dict(n=n, N=N, primes=P, characters=len(chars), h1_multiset={str(k): v for k, v in h1s.items()},
               loci=len(loci), loci_nonsquare=sum(1 for c in loci if c not in squares),
               candidates=nmod, firing=len(I), firing_on_square_loci=fire_sq, firing_on_nonsquare_loci=len(I) - fire_sq,
               firing_per_locus=dict(Counter(firing_by_locus.values())), differing_at_other_primes=differ,
               signatures={str(k): v for k, v in sig.items()},
               generation_backgrounds=len(bgs), lifted=lifted, not_lifted=len(bgs) - lifted,
               signs=dict(signs), abs_counts=dict(Counter(abs(c[0]) for c in bgs.values())),
               nuc={"same_sign_as_generation": sum(v for (same, nz), v in nuc.items() if same),
                    "zero": sum(v for (same, nz), v in nuc.items() if not nz),
                    "opposite_sign": sum(v for (same, nz), v in nuc.items() if nz and not same)},
               index_deck_invariant=inv_ok, background_orbits_closed=orbit_closed,
               backgrounds_by_orbit_size={str(k): k * v for k, v in orbit_sizes.items()},
               background_orbits={str(k): v for k, v in orbit_sizes.items()},
               firing_modules_by_orbit_size={str(k): v for k, v in mod_orbits.items()},
               orbit_lambda_structure={str(k): v for k, v in ratio_orders.items()},
               tau={str(g): w for g, w in tau.items()}, seconds=round(time.time() - t0, 1))
    if verbose: print(json.dumps(out, indent=1), flush=True)
    return out, bgs, I, chars, (ng, rels, mu, lam, tau)

if __name__ == '__main__':
    jobs = eval(sys.argv[1])           # e.g. "[(3,4,5000)]"
    res = {}
    for (n, N, pstart) in jobs:
        o, *_ = census(n, N, pstart); res["M%d" % n] = o
    if len(sys.argv) > 2: json.dump(res, open(sys.argv[2], 'w'), indent=1)
