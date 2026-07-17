"""Dev iteration: (1) mod-p row-selection to find a minimal independent row
subset for the combined (str0 + Xv0=0) system: 52-dim kernel; (2) rebuild
EXACTLY just those rows (K = Q(sqrt(-3)) Fraction-pair arithmetic, copied
verbatim from l51_obstruction.py lines 27-123) and run the EXACT nullspace()
on the reduced system, timing it; (3) verify 3 exact kernel vectors satisfy
N(Xx,x,x)=0 exactly for 5 random exact x."""
import os, pickle, time, random
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


# ---- K field + exact linear algebra, copied verbatim from l51_obstruction.py ----
class K:
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a)
        self.b = b if isinstance(b, Fr) else Fr(b)
    def __add__(s, o): return K(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return K(s.a - o.a, s.b - o.b)
    def __neg__(s):    return K(-s.a, -s.b)
    def __mul__(s, o): return K(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    def inv(s):
        dd = s.a * s.a + 3 * s.b * s.b
        return K(s.a / dd, -s.b / dd)
    def __eq__(s, o):  return s.a == o.a and s.b == o.b
    def is_zero(s):    return s.a == 0 and s.b == 0
    def __repr__(s):   return f"({s.a}+{s.b}r)" if s.b else f"({s.a})"


K0, K1 = K(0), K(1)


def rref(M):
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0]) if A else 0
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if not A[i][c].is_zero(): pr = i; break
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]
        iv = A[r][c].inv()
        A[r] = [x * iv for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows: break
    return A[:r], piv


def nullspace(M):
    R, piv = rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        v = [K0] * cols
        v[fc] = K1
        for r_i, pc in enumerate(piv):
            v[pc] = -R[r_i][fc]
        basis.append(v)
    return basis


v0 = [K(*unkser(cache["v0"][i])) for i in range(d)]
CFULL = {}
for key, val in cache["CFULL"].items():
    p_, q_, r_ = (int(x) for x in key.split(","))
    CFULL[(p_, q_, r_)] = K(*unkser(val))
log(f"exact v0, CFULL rebuilt from cache ({len(CFULL)} CFULL entries)")

# ---- redo the mod-p side (prime, conversion, systems) to get the row provenance ----
def is_probable_prime(n, rounds=20):
    for pp in (2,3,5,7,11,13,17,19,23,29,31):
        if n % pp == 0: return n == pp
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
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, rr = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        t2i, i = t, 0
        while t2i != 1:
            t2i = t2i * t2i % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, rr = i, b * b % p, t * b * b % p, rr * b % p
    return rr


x = (1 << 31) - 1
while not (x % 3 == 1 and is_probable_prime(x)):
    x -= 2
p = x
r = tonelli_shanks((-3) % p, p)
assert (r * r - (-3)) % p == 0


def modinv(a, m):
    return pow(a % m, m - 2, m)


def k_to_fp(pair):
    a, b = pair
    av = (a.numerator * modinv(a.denominator, p)) % p
    bv = (b.numerator * modinv(b.denominator, p)) % p
    return (av + bv * r) % p


v0p = [k_to_fp(unkser(cache["v0"][i])) for i in range(d)]
CFULLp = {}
for key, val in cache["CFULL"].items():
    p_, q_, r_ = (int(z) for z in key.split(","))
    CFULLp[(p_, q_, r_)] = k_to_fp(unkser(val))

UN = d * d
def uidx(i, j): return i * d + j

rows_dict = {}
for (pp_, qq, rr), cval in CFULLp.items():
    for a in range(d):
        key = ("str0",) + tuple(sorted((a, qq, rr)))
        row = rows_dict.setdefault(key, {})
        u = uidx(pp_, a)
        row[u] = (row.get(u, 0) + cval) % p

items = [(k, v) for k, v in rows_dict.items() if any(vv % p != 0 for vv in v.values())]
for i in range(d):
    row = {uidx(i, a): v0p[a] % p for a in range(d)}
    items.append((("xv0", i), row))
log(f"combined candidate rows (str0 + Xv0=0): {len(items)}")

# dense mod-p matrix for row-selection
M1 = np.zeros((len(items), UN), dtype=np.int64)
keys = []
for ridx, (key, row) in enumerate(items):
    keys.append(key)
    for u, v in row.items():
        M1[ridx, u] = v % p


def select_independent_rows(M, keys, p):
    pivots = []  # (col, reduced_row)
    selected = []
    t0 = time.time()
    for ridx in range(M.shape[0]):
        v = M[ridx].copy() % p
        for col, prow in pivots:
            if v[col] != 0:
                f = int(v[col])
                v = (v - f * prow) % p
        nz = np.nonzero(v)[0]
        if nz.size == 0:
            continue
        c0 = int(nz[0])
        inv = modinv(int(v[c0]), p)
        v = (v * inv) % p
        newpivots = []
        for col, prow in pivots:
            if prow[c0] != 0:
                f = int(prow[c0])
                prow = (prow - f * v) % p
            newpivots.append((col, prow))
        newpivots.append((c0, v))
        newpivots.sort(key=lambda t: t[0])
        pivots = newpivots
        selected.append(keys[ridx])
        if len(selected) % 100 == 0:
            log(f"  ...selected {len(selected)} independent rows so far "
                f"({ridx+1}/{M.shape[0]} scanned, {time.time()-t0:.1f}s)")
    return selected, len(pivots)


t0 = time.time()
selected_keys, rank = select_independent_rows(M1, keys, p)
log(f"row-selection done: {len(selected_keys)} independent rows selected, rank={rank}  "
    f"[expect rank 677 = 729-52]  ({time.time()-t0:.1f}s)")

# ---- build EXACT rows for just the selected keys ----
eqs_exact = {}
for (pp_, qq, rr), cval in CFULL.items():
    for a in range(d):
        key = ("str0",) + tuple(sorted((a, qq, rr)))
        row = eqs_exact.setdefault(key, {})
        u = uidx(pp_, a)
        row[u] = row.get(u, K0) + cval

exact_rows = []
for key in selected_keys:
    if key[0] == "str0":
        row = eqs_exact.get(key, {})
        exact_rows.append([row.get(u, K0) for u in range(UN)])
    else:
        i = key[1]
        rowvec = [K0] * UN
        for a in range(d):
            rowvec[uidx(i, a)] = v0[a]
        exact_rows.append(rowvec)
log(f"exact reduced system built: {len(exact_rows)} rows x {UN} cols")

t0 = time.time()
ker_exact = nullspace(exact_rows)
log(f"EXACT nullspace on reduced system: dim = {len(ker_exact)}  [expect 52]  "
    f"({time.time()-t0:.1f}s)")

# ---- cross-check: exact kernel vectors reduce mod p into the mod-p kernel's row space
# (i.e. satisfy the *full* mod-p combined system exactly, not just the 677-row subset) ----
def kfp(x):
    av = (x.a.numerator * modinv(x.a.denominator, p)) % p
    bv = (x.b.numerator * modinv(x.b.denominator, p)) % p
    return (av + bv * r) % p


full_rows_modp = M1  # the full 2502 x 729 candidate system mod p, from earlier
mismatch = 0
for vec in ker_exact[:5]:
    vfp = np.array([kfp(x) for x in vec], dtype=np.int64)
    img = (full_rows_modp.astype(object).dot(vfp.astype(object)) % p)
    if not all(int(z) % p == 0 for z in np.asarray(img).reshape(-1)):
        mismatch += 1
log(f"cross-check: exact kernel vectors reduce mod p to satisfy the FULL "
    f"2502-row mod-p system exactly: {'ALL PASS' if mismatch == 0 else f'{mismatch} FAILURES'}")

# ---- exact spot-verify: 3 random exact kernel elements, N(Xx,x,x)=0 for 5 random exact x ----
def C3(u, v):
    cov = [K0] * d
    for (pp_, qq, rr), cval in CFULL.items():
        if not u[pp_].is_zero() and not v[qq].is_zero():
            cov[rr] = cov[rr] + cval * u[pp_] * v[qq]
    return cov


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


def Napply(a, b, c):
    return dot(C3(a, b), c)


random.seed(99)
sample3 = random.sample(range(len(ker_exact)), 3)
xs = []
for trial in range(5):
    xs.append([K(random.randint(-4, 4), random.randint(-3, 3)) for _ in range(d)])

all_zero = True
for si in sample3:
    vec = ker_exact[si]
    Xmat = [[vec[uidx(i, j)] for j in range(d)] for i in range(d)]
    for xi, xv in enumerate(xs):
        Xx = [sum((Xmat[i][k] * xv[k] for k in range(d) if not xv[k].is_zero()), K0)
              for i in range(d)]
        val = Napply(Xx, xv, xv)
        ok = val.is_zero()
        all_zero = all_zero and ok
        log(f"  exact spot-check: kernel[{si}] x sample[{xi}]: N(Xx,x,x) = {val}  "
            f"{'OK (zero)' if ok else 'FAIL (nonzero!)'}")
log(f"EXACT SPOT-VERIFY all zero: {all_zero}")


