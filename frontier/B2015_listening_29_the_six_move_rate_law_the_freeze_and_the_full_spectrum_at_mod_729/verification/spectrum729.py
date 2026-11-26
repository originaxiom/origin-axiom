"""B2015, R3 (main, 2026-11-26; data-free): the halving on the full spectrum at mod 729. On the orbit of (3,3,3) (52,488
points), the six-move sum's neutral sector in the orthonormal C-orbit basis (real symmetric, 17,498) and its charged q = 1
sector in the normalised basis b_o = (e_v + w^-1 e_Cv + w^-2 e_C2v)/sqrt 3 (Hermitian, 17,495); all eigenvalues of each in
double precision (scipy eigh, eigenvalues only, run one after the other); the neutral ones halved against the charged ones,
with 3, -3 and 0 set aside once each.
    OMP_NUM_THREADS=6 python3 -B spectrum729.py > spectrum729_run.txt"""
import time, gc
import numpy as np
from scipy.linalg import eigh
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
N = 729
L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
X = lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]); Xi = lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])
C = lambda v: (v[1], v[2], v[0])
moves = (L, R, Li, Ri, X, Xi)
s = (3, 3, 3); seen, todo = {s}, [s]
while todo:
    v = todo.pop()
    for g in (L, R, Li, Ri):
        u = g(v)
        if u not in seen:
            seen.add(u); todo.append(u)
pts = sorted(seen)
orb, reps, sizes = {}, [], []
for v in pts:
    if v in orb:
        continue
    o = len(reps); reps.append(v); u = v; k = 0
    while u not in orb:
        orb[u] = (o, k); u = C(u); k += 1
    sizes.append(k)
n0 = len(reps); fixed = sum(1 for z in sizes if z == 1)
log("mod 729: %d points; %d C-orbits (%d fixed points); neutral dimension %d" % (len(pts), n0, fixed, n0))
A = np.zeros((n0, n0))
for o, v in enumerate(reps):
    for m in moves:
        A[orb[m(v)][0], o] += 1.0                     # Q[o'][o] = #{m : m(v) in o'}
sq = np.sqrt(np.array(sizes, dtype=float))
A = (A * sq[None, :]) / sq[:, None]                   # D^(1/2) Q D^(-1/2), symmetric for symmetric W
log("    neutral matrix built; symmetric to %.1e" % np.abs(A - A.T).max())
ev0 = eigh(A, eigvals_only=True, overwrite_a=True, check_finite=False)
del A; gc.collect()
log("    neutral eigenvalues: %d, largest %.12f, smallest %.12f" % (len(ev0), ev0.max(), ev0.min()))
ch = [o for o in range(n0) if sizes[o] == 3]; ci = {o: i for i, o in enumerate(ch)}; n1 = len(ch)
w = np.exp(2j * np.pi / 3)
H = np.zeros((n1, n1), dtype=complex)
for o in ch:
    v = reps[o]; u = v
    for j in range(3):
        ph = w ** (-j)
        for m in moves:
            o2, jt = orb[m(u)]
            if o2 in ci and jt == 0:
                H[ci[o2], ci[o]] += ph
        u = C(u)
log("    charged matrix built: dimension %d; Hermitian to %.1e" % (n1, np.abs(H - H.conj().T).max()))
ev1 = eigh(H, eigvals_only=True, overwrite_a=True, check_finite=False)
del H; gc.collect()
log("    charged eigenvalues: %d, largest %.12f, smallest %.12f" % (len(ev1), ev1.max(), ev1.min()))
half = np.sort(ev0 / 2)
rest = list(half)
for target in (3.0, -3.0, 0.0):
    i = int(np.argmin([abs(r - target) for r in rest])); removed = rest.pop(i)
    log("    set aside the halved neutral eigenvalue nearest %g: %.3e from it" % (target, abs(removed - target)))
rest = np.array(rest); ev1s = np.sort(ev1)
diff = np.abs(rest - ev1s)
log("R3: halved neutral (less the three) against charged, sorted and matched one to one: %d against %d; largest difference %.2e; pairs within 1e-7: %d of %d" % (
    len(rest), len(ev1s), diff.max(), int((diff < 1e-7).sum()), len(ev1s)))
