"""B2012, N1, N2, N3, N6, N8, M1 (main, 2026-11-26; data-free): the blind listener's new observations, rebuilt on main's
own code (the listener's scripts in listener/ are read, not run).
N1: on an orbit, T4 = L + R + L^-1 + R^-1 (push-forwards) against S(C + C^2) + (C + C^2)S, pointwise as multisets of
images (this is 3(SP + PS) - 2S); then charpoly(T4) against R(x + 4) R(x + 2) (x - 4)^d1 (x + 4)^d2 (x + 2)^d3 (x - 2)^d4,
with A = 3 P(1 + S)P on the C-orbit-sum basis (integer), d1 = mult of 6 in A, d2 = mult of 0, R = charpoly(A) without
them, d3 = (n + f_S)/2 - d1 - deg R, d4 = (n - f_S)/2 - d2 - deg R (f_S = fixed points of S). Exact over Z where the orbit
has at most 648 points; modulo three 62-bit primes at mod 135 (2880 points).
N2: the orbit of (t, 0, 0) for symbolic t. N3: point counts of every leaf over F_p, 3 <= p <= 71. N6: residues mod 4 and 9;
the listener's 15 leaves: solvability modulo 8, 16, 27, 81, 5, 25, 7, 49, 11, 13, and integer points with |x|, |y| <= 3000.
N8: orbits on k = 5, 13, 29 mod 2^5, 2^6, 2^7. M1: the 40-point orbits over Q(sqrt 5) reduced with sqrt 5 -> 0.
    python3 -B blind_checks.py > blind_checks_run.txt"""
import time
from fractions import Fraction as Fr
import numpy as np, sympy as sp, flint
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)


def moves_mod(N):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    S = lambda v: (v[1], v[0], (v[0] * v[1] - v[2]) % N); C = lambda v: (v[1], v[2], v[0])
    return L, R, Li, Ri, S, C


def orbit_of(N, start):
    L, R, Li, Ri, S, C = moves_mod(N)
    s = tuple(c % N for c in start); seen, todo = {s}, [s]
    while todo:
        v = todo.pop()
        for g in (L, R, Li, Ri):
            u = g(v)
            if u not in seen:
                seen.add(u); todo.append(u)
    return sorted(seen)


def largest_on_leaf(p, k):
    pts = [(x, y, z) for x in range(p) for y in range(p) for z in range(p) if (x * x + y * y + z * z - x * y * z - k) % p == 0]
    left = set(pts); best = []
    while left:
        o = orbit_of(p, next(iter(left))); left -= set(o)
        if len(o) > len(best):
            best = o
    return best


def n1(N, pts, label, exact=True):
    L, R, Li, Ri, S, C = moves_mod(N)
    idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    ident = all(sorted([L(v), R(v), Li(v), Ri(v)]) == sorted([S(C(v)), S(C(C(v))), C(S(v)), C(C(S(v)))]) for v in pts)
    orb, sizes = {}, []
    for v in pts:
        if v in orb:
            continue
        o = len(sizes); u = v; members = []
        while u not in orb:
            orb[u] = o; members.append(u); u = C(u)
        sizes.append(len(members))
    m = len(sizes)
    A = [[0] * m for _ in range(m)]
    for v in pts:                     # P(1+S)b_o = sum over u in o of (e_u + e_Su), projected: coefficient on b_o' is count/|o'|
        o = orb[v]
        for w in (v, S(v)):
            A[orb[w]][o] += 3 // sizes[orb[w]]
    fS = sum(1 for v in pts if S(v) == v)
    T = [[0] * n for _ in range(n)]
    for v in pts:
        for g in (L, R, Li, Ri):
            T[idx[g(v)]][idx[v]] += 1
    x = flint.fmpz_poly([0, 1])
    def strip(f, root):
        e = 0; lin = flint.fmpz_poly([-root, 1])
        while True:
            q, r = divmod(f, lin)
            if r != 0:
                return f, e
            f, e = q, e + 1
    if exact:
        pA = flint.fmpz_mat(A).charpoly()
        Rp, d1 = strip(pA, 6); Rp, d2 = strip(Rp, 0)
        g = Rp.degree(); d3 = (n + fS) // 2 - d1 - g; d4 = (n - fS) // 2 - d2 - g
        cs = [int(c) for c in Rp.coeffs()]
        shift = lambda a: sum((flint.fmpz_poly([a, 1]) ** i) * c for i, c in enumerate(cs))
        rhs = shift(4) * shift(2) * flint.fmpz_poly([-4, 1]) ** d1 * flint.fmpz_poly([4, 1]) ** d2 * flint.fmpz_poly([2, 1]) ** d3 * flint.fmpz_poly([-2, 1]) ** d4
        ok = flint.fmpz_mat(T).charpoly() == rhs
        log("N1 %s: %d points, %d C-orbits, S fixes %d; T4 = S(C+C^2) + (C+C^2)S pointwise: %s; d1..d4 = %d, %d, %d, %d, generic pairs %d; charpoly(T4) == R(x+4) R(x+2) (x-4)^d1 (x+4)^d2 (x+2)^d3 (x-2)^d4 over Z: %s" % (
            label, n, m, fS, ident, d1, d2, d3, d4, g, ok))
    else:
        oks = []; pr = int(sp.nextprime(1 << 61)); dd = None
        for _ in range(3):
            pA = flint.nmod_mat(A, pr).charpoly()
            def strip_m(f, root):
                e = 0; lin = flint.nmod_poly([(-root) % pr, 1], pr)
                while f % lin == 0:
                    f = f // lin; e += 1
                return f, e
            Rp, d1 = strip_m(pA, 6); Rp, d2 = strip_m(Rp, 0)
            g = Rp.degree(); d3 = (n + fS) // 2 - d1 - g; d4 = (n - fS) // 2 - d2 - g
            cs = [int(c) for c in Rp.coeffs()]
            shift = lambda a: sum(((flint.nmod_poly([a % pr, 1], pr)) ** i) * c for i, c in enumerate(cs))
            lin = lambda a: flint.nmod_poly([a % pr, 1], pr)
            rhs = shift(4) * shift(2) * lin(-4) ** d1 * lin(4) ** d2 * lin(2) ** d3 * lin(-2) ** d4
            oks.append(flint.nmod_mat(T, pr).charpoly() == rhs); dd = (d1, d2, d3, d4, g)
            pr = int(sp.nextprime(pr + 1000003))
        log("N1 %s: %d points, %d C-orbits, S fixes %d; T4 = S(C+C^2) + (C+C^2)S pointwise: %s; d1..d4 = %d, %d, %d, %d, generic pairs %d; the factorisation modulo three 62-bit primes: %s" % (
            label, n, m, fS, ident, dd[0], dd[1], dd[2], dd[3], dd[4], oks))


for p, k in ((7, 5), (11, 6), (13, 9)):
    n1(p, largest_on_leaf(p, k), "p = %d, k = %d (largest orbit)" % (p, k))
for N in (27, 81):
    n1(N, orbit_of(N, (3, 3, 3)), "orbit of (3,3,3) mod %d" % N)
n1(135, orbit_of(135, (3, 3, 3)), "orbit of (3,3,3) mod 135", exact=False)

# N2
t = sp.Symbol("t")
Ls = lambda v: (v[0], v[2], sp.expand(v[0] * v[2] - v[1])); Rs = lambda v: (v[2], v[1], sp.expand(v[1] * v[2] - v[0]))
Lis = lambda v: (v[0], sp.expand(v[0] * v[1] - v[2]), v[1]); Ris = lambda v: (sp.expand(v[0] * v[1] - v[2]), v[1], v[0])
seen = {(t, sp.Integer(0), sp.Integer(0))}; todo = list(seen)
while todo and len(seen) < 100:
    v = todo.pop()
    for g in (Ls, Rs, Lis, Ris):
        u = g(v)
        if u not in seen:
            seen.add(u); todo.append(u)
kk = {sp.expand(a * a + b * b + c * c - a * b * c) for a, b, c in seen}
log("N2: the orbit of (t, 0, 0) for symbolic t has %d points %s; their k: %s" % (len(seen), sorted(map(str, seen)), kk))

# N3
bad = []
for p in sp.primerange(3, 72):
    chi = np.zeros(p, dtype=np.int64)
    for a in range(1, p):
        chi[(a * a) % p] = 1
    chi = np.where(chi == 1, 1, -1); chi[0] = 0
    X, Y = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    for k in range(p):
        disc = (X * X * Y * Y - 4 * (X * X + Y * Y - k)) % p
        cnt = int((1 + chi[disc]).sum())
        want = p * p + p * (3 * int(chi[(k - 4) % p]) + int(chi[(k * (k - 4)) % p])) + 1
        if cnt != want:
            bad.append((p, k, cnt, want))
log("N3: #X_k(F_p) == p^2 + p(3 chi(k-4) + chi(k(k-4))) + 1 for every k and every prime 3 <= p <= 71: %s (failures %s)" % (not bad, bad[:5]))

# N6a
for m in (4, 9):
    r = sorted({(x * x + y * y + z * z - x * y * z) % m for x in range(m) for y in range(m) for z in range(m)})
    log("N6a: residues of x^2 + y^2 + z^2 - xyz mod %d: %s" % (m, r))
# N6b
fifteen = [-54, -47, -44, -38, -26, -19, -18, -14, -8, -4, 46, 56, 86, 124, 126]
mods = (8, 16, 27, 81, 5, 25, 7, 49, 11, 13)
B = 3000
xs = np.arange(-B, B + 1, dtype=np.int64)
rows = []
for k in fifteen:
    loc = []
    for m in mods:
        a = np.arange(m)
        Xm, Ym, Zm = np.meshgrid(a, a, a, indexing="ij")
        loc.append(bool(((Xm * Xm + Ym * Ym + Zm * Zm - Xm * Ym * Zm - k) % m == 0).any()))
    found = 0
    for x0 in range(-B, B + 1):
        disc = x0 * x0 * xs * xs - 4 * (x0 * x0 + xs * xs - k)
        ok = disc >= 0
        r = np.floor(np.sqrt(disc[ok].astype(np.float64))).astype(np.int64)
        d = disc[ok]
        hit = ((r * r == d) | ((r + 1) * (r + 1) == d) | ((r - 1) * (r - 1) == d))
        found += int(hit.sum())
    rows.append((k, all(loc), found))
log("N6b: (k, solvable at all ten moduli, integer points with |x|, |y| <= %d): %s" % (B, rows))

# N8
for k in (5, 13, 29):
    out = []
    for a in (5, 6, 7):
        N = 2 ** a
        pts = [(x, y, z) for x in range(N) for y in range(N) for z in range(N) if (x * x + y * y + z * z - x * y * z - k) % N == 0]
        left = set(pts); sizes = []
        while left:
            o = orbit_of(N, next(iter(left))); left -= set(o); sizes.append(len(o))
        out.append((N, sorted(sizes, reverse=True)))
    log("N8: k = %d: orbit sizes on the leaf mod 2^5, 2^6, 2^7: %s" % (k, out))

# M1: Q(sqrt 5) numbers as (a, b) = a + b sqrt5 with rationals
def mul(u, v): return (u[0] * v[0] + 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])
def sub(u, v): return (u[0] - v[0], u[1] - v[1])
def Lq(v): return (v[0], v[2], sub(mul(v[0], v[2]), v[1]))
def Rq(v): return (v[2], v[1], sub(mul(v[1], v[2]), v[0]))
def Liq(v): return (v[0], sub(mul(v[0], v[1]), v[2]), v[1])
def Riq(v): return (sub(mul(v[0], v[1]), v[2]), v[1], v[0])
O5 = set(orbit_of(5, (3, 3, 3)))
for sgn in (1, -1):
    phi = (Fr(1, 2), Fr(sgn, 2)); one = (Fr(1), Fr(0)); zero = (Fr(0), Fr(0))
    start = (phi, one, zero)
    seen = {start}; todo = [start]
    while todo and len(seen) < 1000:
        v = todo.pop()
        for g in (Lq, Rq, Liq, Riq):
            u = g(v)
            if u not in seen:
                seen.add(u); todo.append(u)
    kval = {sub(sub(sub(sub((Fr(0), Fr(0)), (Fr(0), Fr(0))), (Fr(0), Fr(0))), (Fr(0), Fr(0))), (Fr(0), Fr(0)))}
    ks = set()
    for a, b, c in seen:
        s2 = (mul(a, a)[0] + mul(b, b)[0] + mul(c, c)[0] - mul(mul(a, b), c)[0], mul(a, a)[1] + mul(b, b)[1] + mul(c, c)[1] - mul(mul(a, b), c)[1])
        ks.add(s2)
    red = lambda u: int((u[0].numerator * pow(u[0].denominator, -1, 5)) % 5)   # sqrt 5 -> 0
    img = {(red(a), red(b), red(c)) for a, b, c in seen}
    log("M1: the orbit of (%s, 1, 0) over Q(sqrt 5): %d points, k = %s; reduced with sqrt 5 -> 0: %d distinct points; equals the orbit of (3,3,3) mod 5 (%d points): %s" % (
        "phi" if sgn == 1 else "1 - phi", len(seen), sorted((str(a), str(b)) for a, b in ks), len(img), len(O5), img == O5))
