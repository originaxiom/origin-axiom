"""B2017 (main, 2026-11-26; data-free): the census of the halving over every orbit of L, R and their inverses on every leaf,
at mod 27, 25, 5, 7, 11, 13 and 49. For each orbit: its size, its leaf k = x^2 + y^2 + z^2 - xyz mod N, C's fixed points, and
the six-move sum's sector classification:
  (a)  p_neutral(2x)/2^d == (x^2 - 9) x S(x)   (the whole's form)
  (a') p_neutral(2x)/2^d == S(x)                (no left-out modes, B2014's sister)
  (b)  S divides p_neutral(2x)/2^d
  (c)  neither.
Exact (B2011's sectors_exact, FLINT with CRT) for orbits of at most 1200 points; between 1200 and 2400 points, double
precision on the orthonormal sector matrices (marked "num"); above 2400 listed and left out.
    python3 -B census.py > census_run.txt"""
import pathlib, sys, time, collections
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(next(ROOT.glob("frontier/B2011_*/verification"))))
import flint
from sectors_exact import sector_data, exact_charpolys, halved_monic
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
X = flint.fmpz_poly([0, 1]); Q9 = flint.fmpz_poly([-9, 0, 1])


def all_orbits(N):
    R = np.arange(N)
    A, B, C = [a.ravel() for a in np.meshgrid(R, R, R, indexing="ij")]
    n = len(A); code = lambda a, b, c: (a % N * N + b % N) * N + c % N
    imgs = [code(A, C, A * C - B), code(C, B, B * C - A), code(A, A * B - C, B), code(A * B - C, B, A)]
    parent = np.arange(n)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for im in imgs:
        for i in range(n):
            a, b = find(i), find(int(im[i]))
            if a != b:
                parent[a] = b
    roots = np.array([find(i) for i in range(n)])
    out = collections.defaultdict(list)
    for i, r in enumerate(roots):
        out[int(r)].append(i)
    res = []
    for r, mem in out.items():
        i0 = min(mem); v = (int(A[i0]), int(B[i0]), int(C[i0]))
        k = (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % N
        res.append((len(mem), k, v))
    return sorted(res)


def classify_exact(N, v):
    d = sector_data(N, v)
    pn, pc = exact_charpolys(d)
    h = halved_monic(pn)
    if h == Q9 * X * pc:
        c = "a"
    elif h == pc and d["d1"] > 0:
        c = "a'"
    elif d["d1"] > 0 and h % pc == 0:
        c = "b"
    else:
        c = "c"
    return c, d["fixed"]


def classify_num(N, v):
    d = sector_data(N, v)
    Q = np.array(d["Q"], dtype=float)
    # the neutral classes' sizes: 1 for fixed points, 3 otherwise; Q's eigenvalues are W's on the neutral sector
    ev0 = np.sort(np.linalg.eigvals(Q).real) / 2
    w = np.exp(2j * np.pi / 3); n1 = d["d1"]
    H = np.zeros((n1, n1), dtype=complex)
    for r, dct in enumerate(d["Ca"]):
        for cc, (a, b) in dct.items():
            H[r, cc] = a + b * w
    ev1 = np.sort(np.linalg.eigvalsh((H + H.conj().T) / 2))
    def take(arr, t):
        i = int(np.argmin(np.abs(arr - t))); return np.delete(arr, i) if abs(arr[i] - t) < 1e-6 else None
    rest = ev0.copy()
    ok = True
    for t in (3.0, -3.0, 0.0):
        rest = take(rest, t) if rest is not None else None
    if rest is not None and len(rest) == len(ev1) and np.abs(np.sort(rest) - ev1).max() < 1e-7:
        return "a (num)", d["fixed"]
    if len(ev0) == len(ev1) and np.abs(ev0 - ev1).max() < 1e-7:
        return "a' (num)", d["fixed"]
    left = list(ev0); paired = 0
    for m in ev1:
        j = int(np.argmin(np.abs(np.array(left) - m)))
        if abs(left[j] - m) < 1e-7:
            left.pop(j); paired += 1
    return ("b (num)" if paired == len(ev1) and n1 > 0 else "c (num)"), d["fixed"]


grand = collections.Counter()
for N in (27, 25, 5, 7, 11, 13, 49):
    orbs = all_orbits(N)
    log("mod %d: %d residues in %d orbits" % (N, N ** 3, len(orbs)))
    tally = collections.Counter(); halving = []
    for size, k, v in orbs:
        if size > 2400:
            log("    orbit of %d points on k = %d through %s: left out (above 2400)" % (size, k, v)); tally["left out"] += 1; continue
        cat, fx = (classify_exact if size <= 1200 else classify_num)(N, v)
        tally[cat] += 1; grand[(N, cat.split()[0])] += 1
        if cat.split()[0] in ("a", "a'"):
            halving.append((size, k, v, fx, cat))
    log("    categories: %s" % dict(sorted(tally.items())))
    log("    orbits in (a) or (a') (size, leaf k, a point, C's fixed points, category): %s" % halving)
log("over all levels: the orbits in (a) or (a'), by level: %s" % {N: [c for c in ("a", "a'") if grand[(N, c)]] and {c: grand[(N, c)] for c in ("a", "a'")} for N in (27, 25, 5, 7, 11, 13, 49)})
