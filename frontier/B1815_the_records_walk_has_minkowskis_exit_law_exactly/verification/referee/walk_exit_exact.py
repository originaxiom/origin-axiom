"""Referee check 2 (B1815): an independent simulation of B1663's walk with exact integers (right-multiplied, X_n = g1..gn,
xi = a/c = X_n(inf), run until an entry exceeds 10^100), at p = 0.1, 0.3, 0.5, 0.7, 0.9, 1.0 (B1663 ran p <= 0.5 only).
Tests, all against the claimed nu_p = (1-p) M + p F_*M:
  (i)   P(xi > 0) against 1 - p;
  (ii)  the probability-integral transform U = G(|xi|) (G = M's exact CDF via ?) is Uniform(0, 1): one-sample KS;
  (iii) digits d_3..d_42 of |xi| (fixed K per walk: no length bias): frequencies of 1..4, >=5 against 2^-k, and the
        lag-1 pair table (independence), chi-square;
  (iv)  the ray's time above Im tau = Y (Y = 2, 3) along the geodesic to xi (run-segment pieces, the time above Y inside
        each piece computed directly as |[s0, s1] cap [-A, A]|, A = arccosh(rho / Y)), pooled as a ratio of sums, against
        the move clock's 0.1676 / 0.03462 (B1813's referee limit).
usage: python3 -I walk_exit_exact.py WALKS SEED"""
import sys, math, random
from fractions import Fraction as Fr
from multiprocessing import Pool

def cfd(num, den):
    out = []
    while den:
        q, r = divmod(num, den); out.append(q); num, den = den, r
    return out

def qm_digits(d):                           # ? of [0; d1, d2, ...] from digits (float is enough for a KS test)
    s = 0.0; acc = 0
    for j, a in enumerate(d):
        acc += a
        if acc > 1060: break
        s += (1 if j % 2 == 0 else -1) * 2.0 * 2.0 ** (-acc)
    return s

def G_digits(d):                            # M([0, x]) for x = [d0; d1, ...]
    n = d[0]
    if n > 1000: return 1.0
    return (1 - 2.0 ** (-n)) + 2.0 ** (-(n + 1)) * qm_digits(d[1:])

def cf_val(ds):
    v = float(ds[-1])
    for a in reversed(ds[:-1]): v = a + 1.0 / v
    return v

def reduce_h(z):                            # height of z in the standard fundamental domain (independent reduction)
    for _ in range(10000):
        z = complex(z.real - math.floor(z.real + 0.5), z.imag)
        if abs(z) < 1 - 1e-13: z = -1 / z
        else: return z.imag
    return z.imag

def ray_time(d, Ys, LOOK=24, dens=12.0):
    """time above Y along the ray, by sampling each run-segment piece densely and REDUCING every sample to the domain
    (no excursion formula), plus the full-excursion formula 2 arccosh(rho/Y) per piece for comparison"""
    tot = 0.0; exc = {Y: 0.0 for Y in Ys}; exf = {Y: 0.0 for Y in Ys}
    for i in range(LOOK, len(d) - LOOK):
        x = cf_val(d[i:i + LOOK]); y = 1.0 / cf_val(d[i - LOOK:i][::-1])
        c, rho = (x - y) / 2, (x + y) / 2
        s0, s1 = math.atanh(-c / rho), math.atanh((d[i] - c) / rho)
        Lp = s1 - s0; tot += Lp; k = max(4, int(math.ceil(dens * Lp))); h = Lp / k
        for j in range(k):
            s = s0 + (j + 0.5) * h
            ht = reduce_h(complex(c + rho * math.tanh(s), rho / math.cosh(s)))
            for Y in Ys:
                if ht > Y: exc[Y] += h
        for Y in Ys:
            if rho > Y: exf[Y] += 2 * math.acosh(rho / Y)
    return exc, exf, tot

def one(job):
    p, seed = job; rng = random.Random(seed)
    a, b, c, d = 1, 0, 0, 1; lim = 10 ** 100; n = 0
    while max(abs(a), abs(b), abs(c), abs(d)) < lim:
        x = rng.random()
        if x < (1 - p) / 2: b, d = a + b, c + d
        elif x < 1 - p: a, c = a + b, c + d
        elif x < 1 - p / 2: b, d = b - a, d - c
        else: a, c = a - b, c - d
        n += 1
    if c == 0: return None
    ds = cfd(abs(a), abs(c)); ds = ds[:max(0, len(ds) - 20)]
    if len(ds) < 100: return None
    U = G_digits(ds)
    exc, exf, tot = ray_time(ds[1:], (2.0, 3.0))
    return dict(pos=(a * c > 0), U=U, dig=ds[3:43], exc2=exc[2.0], exc3=exc[3.0], f2=exf[2.0], f3=exf[3.0], tot=tot, nd=len(ds), steps=n)

def ks_unif(us):
    us = sorted(us); n = len(us)
    return max(max((i + 1) / n - u, u - i / n) for i, u in enumerate(us))

if __name__ == "__main__":
    W = int(sys.argv[1]); seed0 = int(sys.argv[2])
    PS = (0.1, 0.3, 0.5, 0.7, 0.9, 1.0)
    with Pool(4) as pool:
        res = pool.map(one, [(p, seed0 + 100000 * k + w) for k, p in enumerate(PS) for w in range(W)], chunksize=20)
    for k, p in enumerate(PS):
        rs = [r for r in res[k * W:(k + 1) * W] if r]
        N = len(rs); pos = sum(r["pos"] for r in rs) / N
        D = ks_unif([r["U"] for r in rs])
        digs = [x for r in rs for x in r["dig"]]
        cats = [min(x, 5) for x in digs]; nd = len(cats)
        exp = [0.5, 0.25, 0.125, 0.0625, 0.0625]
        chi1 = sum((cats.count(j + 1) - nd * exp[j]) ** 2 / (nd * exp[j]) for j in range(5))
        pr = {}
        for r in rs:
            cs = [min(x, 3) for x in r["dig"]]
            for i in range(0, len(cs) - 1, 2): pr[(cs[i], cs[i + 1])] = pr.get((cs[i], cs[i + 1]), 0) + 1
        npairs = sum(pr.values()); e3 = {1: 0.5, 2: 0.25, 3: 0.25}
        chi2 = sum((pr.get((i, j), 0) - npairs * e3[i] * e3[j]) ** 2 / (npairs * e3[i] * e3[j]) for i in e3 for j in e3)
        T = sum(r["tot"] for r in rs); P2 = sum(r["exc2"] for r in rs) / T; P3 = sum(r["exc3"] for r in rs) / T; F2 = sum(r["f2"] for r in rs) / T; F3 = sum(r["f3"] for r in rs) / T
        # SE of the ratio by the delta method over walks
        def se(key, P):
            m = len(rs); v = [r[key] - P * r["tot"] for r in rs]; mt = T / m
            return math.sqrt(sum(x * x for x in v) / (m - 1) / m) / mt
        print("p=%.1f walks %d  P(xi>0) %.4f (1-p %.2f, SE %.4f)  KS(U) %.4f (5%% crit %.4f)  digit chi2 %.2f (4 df)  pair chi2 %.2f (8 df)  "
              "ray (reduced samples) P(Im>2) %.4f+-%.4f (0.1676)  P(Im>3) %.4f+-%.4f (0.03462)  [excursion formula %.4f %.5f]  mean digits %.0f  mean steps %.0f"
              % (p, N, pos, 1 - p, math.sqrt(max(p * (1 - p), 1e-12) / N), D, 1.358 / math.sqrt(N), chi1, chi2,
                 P2, se("exc2", P2), P3, se("exc3", P3), F2, F3, sum(r["nd"] for r in rs) / N, sum(r["steps"] for r in rs) / N), flush=True)
