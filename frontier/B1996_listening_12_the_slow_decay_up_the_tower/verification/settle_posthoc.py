"""B1996, POST HOC (labelled; written after tower_decay_run.txt showed the 3-tower's slowest decay unchanged from mod 81 to
mod 243): (a) the eigenvalues of W+ of modulus near 1.9153 on the largest orbit mod 81 (dense), with their arguments;
(b) a search for a small integer polynomial they satisfy (mpmath findpoly on the dense eigenvalue, degree <= 12);
(c) the slowest decay on the largest orbit mod 729 (k = 6), by sparse Arnoldi.
    python3 -B settle_posthoc.py > settle_posthoc_run.txt"""
import numpy as np, mpmath as mp, time, cmath
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("td", str(pathlib.Path(__file__).with_name("tower_decay.py")))
src = pathlib.Path(__file__).with_name("tower_decay.py").read_text().split("t0 = time.time()")[0]
ns = {}; exec(src, ns); orbits = ns["orbits_over_common_point"]
t0 = time.time()
N, n, Lm, Rm, roots = orbits(3, 4)
r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]; m = len(mem)
loc = -np.ones(n, dtype=int); loc[mem] = np.arange(m)
W = np.zeros((m, m)); W[loc[Lm[mem]], np.arange(m)] += 1; W[loc[Rm[mem]], np.arange(m)] += 1
ev = np.linalg.eigvals(W)
near = sorted([z for z in ev if abs(abs(z) - 1.9153) < 5e-3], key=lambda z: cmath.phase(z))
print("(a) mod 81, largest orbit %d: eigenvalues of modulus near 1.9153: %s; arguments (turns): %s" % (m, [complex(round(z.real, 6), round(z.imag, 6)) for z in near], [round(cmath.phase(z) / (2 * np.pi), 6) for z in near]))
mp.mp.dps = 15
for z in near[:1] + [z for z in near if abs(z.imag) < 1e-9][:1]:
    x = abs(z)
    poly = mp.findpoly(mp.mpf(x), 8, maxcoeff=200)
    print("(b) modulus %.12f: integer polynomial of degree <= 8 with coefficients <= 200 found by findpoly (double precision input): %s" % (x, poly))
    poly3 = mp.findpoly(mp.mpf(x) ** 2, 8, maxcoeff=200)
    print("(b) its square %.12f: %s" % (x * x, poly3))
N, n, Lm, Rm, roots = orbits(3, 6)
r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]; m = len(mem)
loc = -np.ones(n, dtype=int); loc[mem] = np.arange(m)
Ws = csr_matrix((np.ones(2 * m), (np.concatenate([loc[Lm[mem]], loc[Rm[mem]]]), np.concatenate([np.arange(m), np.arange(m)]))), shape=(m, m))
ev6 = eigs(Ws, k=8, which="LM", return_eigenvectors=False, tol=1e-10, maxiter=200000)
mods = sorted(np.abs(ev6), reverse=True); slow = max(x for x in mods if x < 2 - 1e-6)
print("(c) mod 729: %d points over the common point; largest orbit %d; W+ largest moduli %s; slowest decay ratio %.4f  [%.0f s]" % (n, m, [round(x, 4) for x in mods[:6]], slow / 2, time.time() - t0))
