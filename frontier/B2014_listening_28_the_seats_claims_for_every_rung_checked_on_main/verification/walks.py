"""B2014, S1, S2, S3, S5 (main, 2026-11-26; data-free): the seats' claims on the two walks, the sister orbits and the
fixed points up the tower, rebuilt on main's own code.
S1: W+ = L + X + R^-1 and W- = R + L^-1 + X^-1 as push-forward matrices (e_v -> e_g(v)), exact integers (scipy sparse,
int64); their commutator, and C W+ C^-1 = W+. S2: on the orbit mod 27 and 81, Pi_q = (1/3) sum_j w^-qj C^j; the largest
entry of Pi_q W Pi_q - c Pi_q sigma Pi_q for c = 3 w^q and c = 3 w^-q (double precision; the matrices have entries in Z[w]/3).
S3: all residues mod 27 with x^2 + y^2 + z^2 - xyz = 0 mod 27, their orbits; on the orbit of (3,3,15) the exact sector
polynomials (B2011's sectors_exact). S5: for elements g = u C^(+-1) u^-1 v^216 (u, v random words) and for random words
with rho != 1, the number of fixed points on the congruence orbit O_(3^k), k = 3 to 8, compared with k = 3.
    python3 -B walks.py > walks_run.txt"""
import pathlib, sys, time, random
import numpy as np
from scipy.sparse import csr_matrix
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(next(ROOT.glob("frontier/B2011_*/verification"))))
import flint
from sectors_exact import leaf, sector_data, exact_charpolys, halved_monic
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)


def mv(N):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    X = lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]); Xi = lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])
    C = lambda v: (v[1], v[2], v[0]); S = lambda v: (v[1], v[0], (v[0] * v[1] - v[2]) % N)
    return dict(L=L, R=R, Li=Li, Ri=Ri, X=X, Xi=Xi, C=C, S=S)


def pmat(pts, f):
    idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    return csr_matrix((np.ones(n, dtype=np.int64), ([idx[f(v)] for v in pts], list(range(n)))), shape=(n, n))


def orbit(N, start):
    m = mv(N); s = tuple(c % N for c in start); seen, todo = {s}, [s]
    while todo:
        v = todo.pop()
        for g in (m["L"], m["R"], m["Li"], m["Ri"]):
            u = g(v)
            if u not in seen:
                seen.add(u); todo.append(u)
    return sorted(seen)


def largest_leaf_orbit(p, k):
    pts = [(x, y, z) for x in range(p) for y in range(p) for z in range(p) if (x * x + y * y + z * z - x * y * z - k) % p == 0]
    left = set(pts); best = []
    while left:
        o = orbit(p, next(iter(left))); left -= set(o)
        if len(o) > len(best):
            best = o
    return best


# S1
for N, pts, lab in ((27, orbit(27, (3, 3, 3)), "orbit of (3,3,3) mod 27"), (81, orbit(81, (3, 3, 3)), "mod 81"), (243, orbit(243, (3, 3, 3)), "mod 243"), (7, largest_leaf_orbit(7, 5), "leaf p = 7, k = 5 (largest orbit)")):
    m = mv(N); P = {k: pmat(pts, f) for k, f in m.items()}
    Wp = P["L"] + P["X"] + P["Ri"]; Wm = P["R"] + P["Li"] + P["Xi"]
    comm = Wp @ Wm - Wm @ Wp
    Cinv = P["C"].T
    cov = P["C"] @ Wp @ Cinv - Wp
    six = P["L"] + P["R"] + P["Li"] + P["Ri"] + P["X"] + P["Xi"]
    log("S1 %s: %d points; [W+, W-] has %d non-zero entries; C W+ C^-1 - W+ has %d; W+ + W- equals the six-move sum: %s; W- = W+ transposed: %s" % (
        lab, len(pts), comm.count_nonzero(), cov.count_nonzero(), (Wp + Wm - six).count_nonzero() == 0, (Wm - Wp.T).count_nonzero() == 0))

# S2
w = np.exp(2j * np.pi / 3)
for N in (27, 81):
    pts = orbit(N, (3, 3, 3)); m = mv(N); P = {k: pmat(pts, f).toarray().astype(complex) for k, f in m.items()}
    Wp = P["L"] + P["X"] + P["Ri"]; Wm = P["R"] + P["Li"] + P["Xi"]
    n = len(pts); I = np.eye(n); C1 = P["C"]; C2 = C1 @ C1
    for q in range(3):
        Pi = (I + w ** (-q) * C1 + w ** (-2 * q) * C2) / 3
        H = Pi @ P["S"] @ Pi
        for name, W in (("W+", Wp), ("W-", Wm)):
            A = Pi @ W @ Pi
            r_plus = np.abs(A - 3 * w ** q * H).max(); r_minus = np.abs(A - 3 * w ** (-q) * H).max()
            log("S2 mod %d, q = %d, %s: max |Pi W Pi - 3 w^q H| = %.1e; max |Pi W Pi - 3 w^-q H| = %.1e" % (N, q, name, r_plus, r_minus))

# S3
N = 27
R = np.arange(N)
Xg, Yg, Zg = [a.ravel() for a in np.meshgrid(R, R, R, indexing="ij")]
on = (Xg * Xg + Yg * Yg + Zg * Zg - Xg * Yg * Zg) % 27 == 0
sols = list(zip(Xg[on].tolist(), Yg[on].tolist(), Zg[on].tolist()))
left = set(sols); orbs = []
while left:
    s = min(left); o = orbit(27, s); left -= set(o); orbs.append((len(o), s))
orbs.sort(reverse=True)
log("S3: %d residues mod 27 on x^2 + y^2 + z^2 = xyz mod 27; all divisible by 3: %s; orbits (size, least point): %s" % (
    len(sols), all(c % 3 == 0 for v in sols for c in v), orbs))
for start in ((3, 3, 15), (3, 3, 12)):
    o = set(orbit(27, start)); same = o == set(orbit(27, (3, 3, 3)))
    kap = (start[0] ** 2 + start[1] ** 2 + start[2] ** 2 - start[0] * start[1] * start[2])
    log("    %s: %d points; the same orbit as (3,3,3): %s; kappa = %d, kappa/27 mod 3 = %d" % (start, len(o), same, kap, (kap // 27) % 3))
d = sector_data(27, (3, 3, 15)); pn, pc = exact_charpolys(d)
h = halved_monic(pn)
d0 = sector_data(27, (3, 3, 3)); pn0, pc0 = exact_charpolys(d0)
X = flint.fmpz_poly([0, 1])
log("    on (3,3,15): C fixes %d; neutral dimension %d, charged %d; p_neutral(2x)/2^d == S(x) exactly: %s; x S_(3,3,15)(x) == (x^2 - 9) S_(3,3,3)(x): %s" % (
    d["fixed"], d["d0"], d["d1"], h == pc, X * pc == flint.fmpz_poly([-9, 0, 1]) * pc0))

# S5
INV9 = None
def level_pts(k, prev):
    Nk = 3 ** k
    if prev is None:
        g = np.array([3, 6]); A, B, Cc = [a.ravel() for a in np.meshgrid(g, g, g, indexing="ij")]
        keep = (A * A + B * B + Cc * Cc - A * B * Cc) % (3 * Nk) == 0
        return A[keep], B[keep], Cc[keep]
    A0, B0, C0 = prev; h = 3 ** (k - 1)
    mm = np.array([(i, j, l) for i in range(3) for j in range(3) for l in range(3)], dtype=np.int64)
    A = (A0[:, None] + h * mm[None, :, 0]).ravel(); B = (B0[:, None] + h * mm[None, :, 1]).ravel(); Cc = (C0[:, None] + h * mm[None, :, 2]).ravel()
    keep = (A * A + B * B + Cc * Cc - A * B * Cc) % (3 * Nk) == 0
    return A[keep] % Nk, B[keep] % Nk, Cc[keep] % Nk

levels = {}; prev = None
for k in range(2, 9):
    prev = level_pts(k, prev); Nk = 3 ** k
    A, B, Cc = prev; code = (A * Nk + B) * Nk + Cc; o = np.argsort(code); A, B, Cc, code = A[o], B[o], Cc[o], code[o]
    def perm(f, A=A, B=B, Cc=Cc, code=code, Nk=Nk):
        a, b, c = f(A, B, Cc); cc = ((a % Nk) * Nk + (b % Nk)) * Nk + (c % Nk); i = np.searchsorted(code, cc); assert (code[i] == cc).all(); return i
    levels[k] = dict(L=perm(lambda a, b, c: (a, c, a * c - b)), R=perm(lambda a, b, c: (c, b, b * c - a)),
                     Li=perm(lambda a, b, c: (a, a * b - c, b)), Ri=perm(lambda a, b, c: (a * b - c, b, a)))
log("S5: the congruence orbits built, k = 2 to 8 (%s points)" % [len(levels[k]["L"]) for k in range(2, 9)])
rhoexp = dict(L=1, R=5, Li=5, Ri=1)          # rho = exp(2 pi i m / 6): rho(C) = w (m = 2), rho(sigma) = -1 (m = 3), L = sigma C^2, R = sigma C
inv = dict(L="Li", R="Ri", Li="L", Ri="R")
def apply_word(k, word):                    # the permutation of the word, letters applied right to left: g = w[0] w[1] ... w[-1]
    p = np.arange(len(levels[k]["L"]))
    for letter in reversed(word):
        p = levels[k][letter][p]
    return p
def compose(p, q): return p[q]              # (p o q)
def power(p, e):
    r = np.arange(len(p)); b = p
    while e:
        if e & 1: r = compose(b, r)
        b = compose(b, b); e >>= 1
    return r
random.seed(2014)
Cw = ["Ri", "L"]                             # C = R^-1 o L
Ciw = ["Li", "R"]
def rand_word(n): return [random.choice("L R Li Ri".split()) for _ in range(n)]
results = {k: [0, 0] for k in range(4, 9)}   # [elements checked, mismatches]
nfix3 = {0: 0, 3: 0}
for trial in range(1200):
    u = rand_word(random.randint(0, 8)); v = rand_word(random.randint(1, 6)); c = random.choice([Cw, Ciw])
    kind = trial % 3
    if kind == 2:                            # a random word with rho != 1
        while True:
            u = rand_word(random.randint(1, 14))
            if sum(rhoexp[x] for x in u) % 6 != 0:
                break
    for k in range(3, 9):
        if k == 8 and trial % 6:
            continue
        if kind == 2:
            g = apply_word(k, u)
        else:
            uu = apply_word(k, u); ui = apply_word(k, [inv[x] for x in reversed(u)])
            g = compose(uu, compose(apply_word(k, c), compose(ui, power(apply_word(k, v), 216))))
        f = int((g == np.arange(len(g))).sum())
        if k == 3:
            f3 = f; nfix3[f] = nfix3.get(f, 0) + 1
        else:
            results[k][0] += 1; results[k][1] += int(f != f3)
log("S5: fixed-point counts at mod 27 over the elements tried: %s; at k = 4..8 (elements checked, mismatches with mod 27): %s" % (nfix3, results))
