"""B1980 correction, the card's second step (plain matching failed): the S move with the covariant end and the wider matching
of s_wider_posthoc.py (any permutation of the three sectors, either reading S or St in each, the mixing between whichever two
sectors play up and down), vectorised. Heights 1.25/0.8, 1.5/(2/3), 2.5/0.4. Control: the same matching at one height gives 0.
    python3 -B s_wider_cov.py > s_wider_cov_run.txt"""
import sys, pathlib, itertools
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import duality_cov as D
mp = D.mp; SEC = ("up", "down", "lep"); RD = ("S", "St"); ZERO = -1e6
def L(x): return ZERO if x == 0 else float(mp.log(x))
def data(arg):
    x, y, a, b, Lend = arg
    Y = {}
    for s in SEC:
        rd = D.parts_L(x, y, a, b, s, Lend)[2]
        for r in RD: Y[(s, r)] = rd[r]
    m, U = {}, {}
    for k, A in Y.items():
        sv = sorted(abs(v) for v in mp.svd_c(A, compute_uv=False)); m[k] = (L(sv[1] / sv[2]), L(sv[0] / sv[2])); U[k] = D.CM.U_of(A)
    V = {}
    for k1 in Y:
        for k2 in Y:
            if k1[0] != k2[0]:
                W = U[k1].H * U[k2]; V[(k1, k2)] = (L(abs(W[0, 1])), L(abs(W[1, 2])), L(abs(W[0, 2])))
    return m, V
ASSIGN = [(perm, rds) for perm in itertools.permutations(SEC) for rds in itertools.product(RD, repeat=3)]
def vec(m, V, perm, rds):
    ks = [(perm[i], rds[i]) for i in range(3)]
    return list(m[ks[0]]) + list(m[ks[1]]) + list(m[ks[2]]) + list(V[(ks[0], ks[1])])
def best(src, par):
    P = np.array([vec(m, V, perm, rds) for (m, V) in par for (perm, rds) in ASSIGN])
    out = []
    for (m, V) in src:
        u = np.array(vec(m, V, SEC, ("S", "S", "S")))
        d = np.abs(P - u) / np.maximum(1.0, np.abs(u))
        out.append(float(d.max(axis=1).min()))
    out.sort(); return out[-1], out[len(out) // 2]
if __name__ == "__main__":
    with Pool(6) as pool:
        for i, (y, yp) in enumerate(((1.25, 0.8), (1.5, 1 / 1.5), (2.5, 0.4))):
            Ls = D.L_cov("0", y); Lp = D.L_cov("0", yp)
            src = pool.map(data, [("0", y, a, b, Ls) for (a, b) in D.P96], chunksize=8)
            if i == 0:
                ctl = pool.map(data, [("0", y, a, b, Ls) for (a, b) in D.E30], chunksize=8)
                print("control (same height %.2f, all 48 assignments): largest d %.1e" % (y, best(src, ctl)[0]), flush=True)
            par = pool.map(data, [("0", yp, a, b, Lp) for (a, b) in D.E30], chunksize=8)
            big, med = best(src, par)
            print("S move, covariant end, wider matching: height %.4f against %.4f: largest d %.1e, median %.1e" % (y, yp, big, med), flush=True)
