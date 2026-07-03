"""B391 -- numpy F_p census at q = 243 and 625 (2 primes each, overflow-checked).

Port of local_censuses.census: ord check (vs P59 prediction), trace-DFT dims, doublet
search (mult-1 pair with 2-dim D/WR-closure), line search (exponent 0 first)."""
import json, os
import numpy as np

def is_prime(n):
    if n < 2: return False
    for sp in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % sp == 0: return n == sp
    d, s, m = n-1, 0, n
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def primes_1_mod(m, count, start):
    out, k = [], (start // m + 1)
    while len(out) < count:
        c = k*m + 1
        if is_prime(c): out.append(c)
        k += 1
    return out

def primitive_root(p):
    fac = []
    n, d = p-1, 2
    while d*d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: fac.append(n)
    g = 2
    while True:
        if all(pow(g, (p-1)//f, p) != 1 for f in fac): return g
        g += 1

def census(q, ord_pred, p, g):
    zq = pow(g, (p-1)//q, p)
    j = np.arange(q, dtype=np.int64)
    Dd = np.array([pow(zq, int((jj*(jj-1)//2) % q), p) for jj in j], dtype=np.int64)
    F  = np.empty((q, q), dtype=np.int64)
    zrow = np.array([pow(zq, int(k), p) for k in range(q)], dtype=np.int64)
    for i in range(q):
        F[i] = zrow[(i*j) % q]
    iq = pow(q, p-2, p)
    Fi = np.empty((q, q), dtype=np.int64)
    for i in range(q):
        Fi[i] = zrow[(-i*j) % q] * iq % p
    Din = np.array([pow(int(x), p-2, p) for x in Dd], dtype=np.int64)
    def mm(A, B):
        # overflow guard: entries < p, sum of q products < q*p^2 must fit int64 -> chunk
        C = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
        step = max(1, (2**62) // (p*p))
        for s in range(0, A.shape[1], step):
            C = (C + A[:, s:s+step] @ B[s:s+step, :]) % p
        return C
    WR = mm(F * Din[None, :] % p, Fi)      # F D^-1 F^-1  (D^-1 applied as column scaling of F)
    W1 = WR * Dd[None, :] % p              # (WR D): column scaling
    # order via matvec on a random vector first (candidate), then confirm on full matrix power
    I = np.eye(q, dtype=np.int64)
    P, o = W1.copy(), 1
    while not np.array_equal(P, I):
        P = mm(P, W1); o += 1
        assert o <= ord_pred + 5, f"order exceeds prediction at q={q}"
    tr = []
    P = I.copy()
    pw_tr = []
    for k in range(o):
        pw_tr.append(int(np.trace(P) % p))
        P = mm(P, W1)
    zo = pow(g, (p-1)//o, p)
    io = pow(o, p-2, p)
    dims = {}
    for a in range(o):
        s = 0
        for k in range(o):
            s = (s + pow(zo, (-k*a) % o, p) * pw_tr[k]) % p
        dims[a] = s * io % p
    # line at exponent 0: eigvector via projector applied to a seed, scalar check
    rng = np.random.default_rng(5)
    def eig(a):
        v = rng.integers(1, p, size=q, dtype=np.int64)
        out = np.zeros(q, dtype=np.int64); w = v.copy()
        for k in range(o):
            c = pow(zo, (-k*a) % o, p) * io % p
            out = (out + c * w) % p
            w = (W1 @ w) % p if p*p*q < 2**62 else np.array([int(sum(int(W1[i,t])*int(w[t]) for t in range(q)) % p) for i in range(q)])
        return out
    def scalar_on(v, M):
        Mv = (M @ v) % p
        nz = int(np.nonzero(v)[0][0])
        lam = Mv[nz] * pow(int(v[nz]), p-2, p) % p
        return bool(np.array_equal(Mv, lam * v % p))
    line0 = False
    if dims.get(0, 0) and dims[0] <= 3:
        v = eig(0)
        if v.any():
            Dv_ok = scalar_on(v, np.diag(Dd))
            W_ok  = scalar_on(v, WR)
            line0 = Dv_ok and W_ok
    # doublet: mult-1 pairs (a, o-a), 2-dim closure under D, WR
    doublet = None
    cand = [a for a in range(1, (o+1)//2) if dims.get(a) == 1 and dims.get((o-a) % o) == 1]
    for a in cand:
        va, vb = eig(a), eig((o-a) % o)
        if not (va.any() and vb.any()): continue
        Bm = np.stack([va, vb])
        def in_span(w):
            i1 = int(np.nonzero(va)[0][0])
            i2 = next(i for i in range(q) if i != i1 and (int(va[i1])*int(vb[i]) - int(va[i])*int(vb[i1])) % p)
            det = (int(va[i1])*int(vb[i2]) - int(va[i2])*int(vb[i1])) % p
            di = pow(det, p-2, p)
            x = (int(w[i1])*int(vb[i2]) - int(w[i2])*int(vb[i1])) * di % p
            y = (int(va[i1])*int(w[i2]) - int(va[i2])*int(w[i1])) * di % p
            return bool(np.array_equal((x*va + y*vb) % p, w % p))
        ok = True
        for M in (np.diag(Dd), WR):
            for v in (va, vb):
                if not in_span((M @ v) % p): ok = False; break
            if not ok: break
        if ok:
            doublet = (a, (o-a) % o); break
    return dict(ord=o, line0=bool(line0), doublet=list(doublet) if doublet else None,
                doublet_deg=(360.0*doublet[0]/o if doublet else None))

CASES = [(243, 324), (625, 1250)]
res = {}
for q, ord_pred in CASES:
    prs = primes_1_mod(4*q, 2, start=3*10**7)
    for p in prs:
        assert (p-1) % q == 0
        g = primitive_root(p)
        r = census(q, ord_pred, p, g)
        res.setdefault(str(q), []).append(dict(prime=p, **r))
        print(q, p, r, flush=True)
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "census_big.json"), "w"), indent=1)
print("DONE", flush=True)
