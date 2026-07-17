"""Dev iteration on the mod-p linear algebra, using the cached exact data."""
import os, pickle, time
import numpy as np
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

d = 27
cache = pickle.load(open(os.path.join(HERE, "_exact_cache.pkl"), "rb"))


def unkser(s):
    an, ad, bn, bd = s
    return (Fr(int(an), int(ad)), Fr(int(bn), int(bd)))


# ---------------------------------------------------------------- prime + sqrt(-3)
def is_probable_prime(n, rounds=20):
    import random
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31):
        if n % p == 0: return n == p
    d0, s = n - 1, 0
    while d0 % 2 == 0:
        d0 //= 2; s += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d0, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True


def tonelli_shanks(n, p):
    n %= p
    if n == 0: return 0
    assert pow(n, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        t2i, i = t, 0
        while t2i != 1:
            t2i = t2i * t2i % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


# search for p ~ 2^31, p == 1 mod 3 (so -3 is a QR for p>3), prime
cand = (1 << 31) - 1  # 2147483647, known Mersenne prime
found_p = None
x = cand
while True:
    if x % 3 == 1 and is_probable_prime(x):
        found_p = x
        break
    x -= 2
p = found_p
leg = pow((-3) % p, (p - 1) // 2, p)
log(f"prime p = {p} (2^31 - {(1<<31)-p}); p mod 3 = {p%3}; Euler criterion (-3|p) = {leg} (must be 1)")
assert leg == 1
r = tonelli_shanks((-3) % p, p)
assert (r * r - (-3)) % p == 0
log(f"sqrt(-3) mod p = {r}; check r^2 mod p = {(r*r)%p}, (-3) mod p = {(-3)%p}")


def modinv(a, m):
    return pow(a % m, m - 2, m)


def k_to_fp(pair):
    a, b = pair
    av = (a.numerator * modinv(a.denominator, p)) % p
    bv = (b.numerator * modinv(b.denominator, p)) % p
    return (av + bv * r) % p


A27p = [[k_to_fp(unkser(cache["A27"][i][j])) for j in range(d)] for i in range(d)]
B27p = [[k_to_fp(unkser(cache["B27"][i][j])) for j in range(d)] for i in range(d)]
v0p = [k_to_fp(unkser(cache["v0"][i])) for i in range(d)]
CFULLp = {}
for key, val in cache["CFULL"].items():
    p_, q_, r_ = (int(x) for x in key.split(","))
    CFULLp[(p_, q_, r_)] = k_to_fp(unkser(val))
log(f"converted A27,B27,v0,CFULL to F_p ({len(CFULLp)} CFULL entries)")
log(f"v0p support: {[(i, v0p[i]) for i in range(d) if v0p[i] != 0]}")

# ---------------------------------------------------------------- build str0 system mod p
UN = d * d  # 729 unknowns, X[i][j] -> idx i*d+j


def uidx(i, j):
    return i * d + j


rows_dict = {}
for (pp, qq, rr), cval in CFULLp.items():
    for a in range(d):
        key = tuple(sorted((a, qq, rr)))
        row = rows_dict.setdefault(key, {})
        u = uidx(pp, a)
        row[u] = (row.get(u, 0) + cval) % p

log(f"str0 candidate equation rows (distinct target monomials touched): {len(rows_dict)} "
    f"out of C(29,3)={ (29*28*27)//6 } possible")

nz_rows = [row for row in rows_dict.values() if any(v % p != 0 for v in row.values())]
log(f"nonzero rows: {len(nz_rows)}")

# dense matrix mod p
M0 = np.zeros((len(nz_rows), UN), dtype=np.int64)
for ridx, row in enumerate(nz_rows):
    for u, v in row.items():
        M0[ridx, u] = v % p
log(f"str0 system matrix shape: {M0.shape}")


def rref_modp(mat, p, ncols=None):
    """Fraction-free RREF over F_p via vectorized numpy elimination.
    Returns (pivot_cols list in increasing order, rref_rows array of shape
    (len(pivots), ncols))."""
    M = mat.copy() % p
    nrows = M.shape[0]
    ncols = M.shape[1] if ncols is None else ncols
    pivots = []
    r = 0
    for c in range(ncols):
        if r >= nrows:
            break
        sub = M[r:nrows, c]
        nz = np.nonzero(sub)[0]
        if nz.size == 0:
            continue
        piv_row = r + nz[0]
        if piv_row != r:
            M[[r, piv_row]] = M[[piv_row, r]]
        inv = modinv(int(M[r, c]), p)
        M[r] = (M[r] * inv) % p
        col = M[:, c].copy()
        col[r] = 0
        nzrows = np.nonzero(col)[0]
        if nzrows.size:
            M[nzrows] = (M[nzrows] - np.outer(col[nzrows], M[r])) % p
        pivots.append(c)
        r += 1
    return pivots, M[:r]


def nullspace_modp(mat, p, ncols):
    pivots, R = rref_modp(mat, p, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = np.zeros(ncols, dtype=np.int64)
        v[fc] = 1
        for ri, pc in enumerate(pivots):
            v[pc] = (-int(R[ri, fc])) % p
        basis.append(v)
    return basis, pivots


t0 = time.time()
ker78, piv78 = nullspace_modp(M0, p, UN)
log(f"str0 nullspace mod p: dim = {len(ker78)}  [GATE expect 78]  ({time.time()-t0:.1f}s)")

# ---------------------------------------------------------------- step 2: add X v0 = 0
xv0_rows = np.zeros((d, UN), dtype=np.int64)
for i in range(d):
    for a in range(d):
        xv0_rows[i, uidx(i, a)] = v0p[a] % p
M1 = np.vstack([M0, xv0_rows])
log(f"combined system (str0 + Xv0=0) shape: {M1.shape}")
t0 = time.time()
ker52, piv52 = nullspace_modp(M1, p, UN)
log(f"stab(v0) nullspace mod p: dim = {len(ker52)}  [GATE expect 52]  ({time.time()-t0:.1f}s)")

# ---------------------------------------------------------------- step 3: the branching
basis52 = [vec.reshape(d, d) % p for vec in ker52]   # X[i][j] = vec[i*d+j]


def modmatmul(A, B, p):
    """Overflow-safe mod-p matrix product: int64 entries up to p~2^31 mean a
    plain int64 @ (which accumulates un-reduced partial sums) can overflow
    once the contraction dimension exceeds ~1-2 (single products already ~p^2
    ~ 2^62). Route through Python bigints (object dtype) instead -- exact,
    just not vectorized at BLAS speed; fine at these sizes/call-counts."""
    C = A.astype(object).dot(B.astype(object))
    return (np.asarray(C) % p).astype(np.int64)


def matvec(M, v):
    return modmatmul(M, v, p)


# 3a: span{X v0 : X in basis52} -- expect 0 (trivially, by construction of Xv0=0)
xv0_vals = [matvec(X, np.array(v0p, dtype=np.int64)) % p for X in basis52]
xv0_allzero = all(int(x) == 0 for vec in xv0_vals for x in vec)
log(f"3a: X v0 for all 52 basis elements all exactly zero: {xv0_allzero}")

# 3b: Im = span of all columns of all 52 basis matrices  (= the derived submodule g.V)
im_rows = np.vstack([basis52[k][:, j] for k in range(len(basis52)) for j in range(d)])
piv_im, R_im = rref_modp(im_rows, p, d)
log(f"3b: dim Im = span{{X w : X in basis52, w in R^27}} = {len(piv_im)}  [expect 26]")

# 3c: is v0 independent of Im?  augment with v0 row, rank should go to 27
im_plus_v0 = np.vstack([im_rows, np.array(v0p, dtype=np.int64).reshape(1, d)])
piv_im_v0, _ = rref_modp(im_plus_v0, p, d)
log(f"3c: dim(Im + span(v0)) = {len(piv_im_v0)}  [expect 27 -> v0 independent of Im, "
    f"clean 1+26 split]")


# incremental basis helper (pivot list) for building/testing the smallest invariant subspace
class IncBasis:
    def __init__(self, p, ncols):
        self.p = p
        self.ncols = ncols
        self.pivots = []  # list of (col, row) sorted by col ascending

    def reduce(self, v):
        v = v.copy() % self.p
        for col, row in self.pivots:
            if v[col] != 0:
                f = int(v[col])
                v = (v - f * row) % self.p
        return v

    def try_add(self, v):
        r_ = self.reduce(v)
        nz = np.nonzero(r_)[0]
        if nz.size == 0:
            return False
        c0 = int(nz[0])
        inv = modinv(int(r_[c0]), self.p)
        r_ = (r_ * inv) % self.p
        # back-substitute into existing pivots for a clean RREF-like basis (not required for
        # dimension counting, but keeps reduce() correct)
        newpivots = []
        for col, row in self.pivots:
            if row[c0] != 0:
                f = int(row[c0])
                row = (row - f * r_) % self.p
            newpivots.append((col, row))
        newpivots.append((c0, r_))
        newpivots.sort(key=lambda t: t[0])
        self.pivots = newpivots
        return True

    def dim(self):
        return len(self.pivots)


# 3d: generic vector w in Im -> smallest invariant subspace containing w under basis52
import random
random.seed(20260717)
# Im (the row space spanned by im_rows) already has an explicit basis: the
# nonzero rows of its RREF, R_im (shape = (dim Im, 27)) -- NOT a nullspace/
# free-column construction (that would build ker, not the row space itself).
im_basis_vecs = [R_im[i].copy() % p for i in range(len(piv_im))]
log(f"3d: explicit Im basis reconstructed, size {len(im_basis_vecs)}")

coeffs = [random.randrange(1, p) for _ in im_basis_vecs]
w = np.zeros(d, dtype=np.int64)
for c_, bv in zip(coeffs, im_basis_vecs):
    w = (w + c_ * bv) % p

ib = IncBasis(p, d)
ib.try_add(w)
queue = [w]
while queue:
    v = queue.pop()
    for X in basis52:
        nv = matvec(X, v)
        if ib.try_add(nv):
            queue.append(nv)
log(f"3d: smallest invariant subspace containing generic w in Im has dim = {ib.dim()}  "
    f"[expect 26 -> irreducible]")

# ---------------------------------------------------------------- step 4: holonomy containment
def matinv_modp(M, p):
    n = M.shape[0]
    aug = np.hstack([M.copy() % p, np.eye(n, dtype=np.int64)])
    piv, R = rref_modp(aug, p, 2 * n)
    assert piv == list(range(n)), "matrix not invertible mod p"
    return R[:, n:2 * n] % p


A27p_arr = np.array(A27p, dtype=np.int64)
B27p_arr = np.array(B27p, dtype=np.int64)
A27p_inv = matinv_modp(A27p_arr, p)
B27p_inv = matinv_modp(B27p_arr, p)
assert np.all(modmatmul(A27p_arr, A27p_inv, p) == np.eye(d, dtype=np.int64))
assert np.all(modmatmul(B27p_arr, B27p_inv, p) == np.eye(d, dtype=np.int64))
log("A27p, B27p mod-p inverses computed and verified")


def flatten(M):
    return M.reshape(-1) % p


def check_str0(Xmat):
    v = flatten(Xmat)
    img = modmatmul(M0, v, p)
    return bool(np.all(img == 0))


def check_stabv0(Xmat):
    return bool(np.all(matvec(Xmat, np.array(v0p, dtype=np.int64)) == 0))


random.seed(4242)
n_checks = 3
sample_idx = random.sample(range(len(basis52)), n_checks) if len(basis52) >= n_checks else list(range(len(basis52)))
containment_results = []
for si in sample_idx:
    # random combination based at basis element si to keep it a "random element", but
    # anchor at an actual basis vector per the prereg's "3 random basis elements"
    X = basis52[si]
    for gname, Gp, Gpinv in (("A27", A27p_arr, A27p_inv), ("B27", B27p_arr, B27p_inv)):
        conj = modmatmul(modmatmul(Gp, X, p), Gpinv, p)
        ok1 = check_str0(conj)
        ok2 = check_stabv0(conj)
        containment_results.append((si, gname, ok1, ok2))
        log(f"4: basis[{si}] conj by {gname}: str0-condition={ok1}, Xv0=0-condition={ok2}")
all_contain_ok = all(ok1 and ok2 for _, _, ok1, ok2 in containment_results)
log(f"4: ALL containment checks pass: {all_contain_ok}")

