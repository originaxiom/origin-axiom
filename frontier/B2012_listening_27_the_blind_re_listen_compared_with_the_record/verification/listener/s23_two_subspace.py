# s23_two_subspace.py -- check T = 3(SP+PS) - 2S exactly (integer matrices x3) and that spec(T) is
# {4,-4,2,-2 on the intersections} u {6t-3 +- 1 : t eigenvalue of P E P on range(P), 0<t<1}, where
# P = projector onto C-invariant functions, E = projector onto S-invariant functions. Float64 for the spectra.
import numpy as np
from modn import orbits
from orbinv import inv, comp
for p, kv in ((7, 5), (11, 6), (13, 9), (17, 3)):
    x, y, z, Li, Ri, k, nc, lab = orbits(p); sizes = np.bincount(lab)
    labs = np.unique(lab[k == kv]); big = max(labs, key=lambda l: sizes[l])
    mem = np.nonzero(lab == big)[0]; n = len(mem)
    pos = {int(m): i for i, m in enumerate(mem)}
    pL = [pos[int(Li[m])] for m in mem]; pR = [pos[int(Ri[m])] for m in mem]
    pr = inv(pR); S = comp(pL, comp(pr, pL)); C = comp(pr, pL)
    def pm(perm):
        M = np.zeros((n, n), dtype=np.int64); M[perm, np.arange(n)] = 1; return M
    T = np.zeros((n, n), dtype=np.int64)
    for q in (pL, pR): T += pm(q) + pm(q).T
    Sm = pm(S); Cm = pm(C)
    P3 = np.eye(n, dtype=np.int64) + Cm + Cm @ Cm   # = 3P
    ok = np.array_equal(3*T, (Sm @ P3 + P3 @ Sm)*3 - 6*Sm) if False else np.array_equal(T, Sm @ P3 + P3 @ Sm - 2*Sm - 0) 
    # T = S J + J S with J = C + C^2 = 3P - 1  ->  T = S(3P) + (3P)S - 2S
    ok = np.array_equal(T, Sm @ P3 + P3 @ Sm - 2*Sm)
    P = P3 / 3.0; E = (np.eye(n) + Sm) / 2.0
    w, V = np.linalg.eigh(P); A = V[:, w > 0.5]
    t = np.linalg.eigvalsh(A.T @ E @ A)
    gen = t[(t > 1e-9) & (t < 1 - 1e-9)]
    pred = np.concatenate([6*gen - 3 + 1, 6*gen - 3 - 1])
    ev = np.linalg.eigvalsh(T.astype(float))
    # remove +-2, +-4 counted from intersections
    n_t1 = np.sum(t > 1 - 1e-9); n_t0 = np.sum(t < 1e-9)
    special = []
    rest = list(ev)
    for val in pred:
        j = int(np.argmin(np.abs(np.array(rest) - val))); 
        if abs(rest[j] - val) < 1e-8: rest.pop(j)
    print("p=%d k=%d n=%d: T == S(3P)+(3P)S-2S exactly: %s; dim range(P)=%d; t=1: %d, t=0: %d, generic t: %d -> %d predicted eigenvalues matched; leftover eigenvalues (should be only 4,-4,2,-2): %s" % (
        p, kv, n, ok, A.shape[1], n_t1, n_t0, len(gen), n - len(rest), sorted(set(np.round(rest, 8)))), flush=True)
