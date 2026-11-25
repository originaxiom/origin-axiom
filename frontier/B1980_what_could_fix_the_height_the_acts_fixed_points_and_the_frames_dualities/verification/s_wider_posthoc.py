"""B1980, POST HOC (labelled; written after duality_run.txt was read): the S move (K = 1) with a wider matching. duality.py held
the sector labels and the reading S fixed. Here the partner may permute the three sectors, take either reading (S or St) in
each, and take the mixing between whichever two sectors play up and down (so up/down transposition is included): 48
assignments per partner point, all 899 nonzero points of E[30], heights 1.5 against 2/3 and 2.5 against 0.4, as in the run.
Control: the same matching at one height must give 0.
    python3 -B s_wider_posthoc.py > s_wider_posthoc_run.txt"""
import sys, pathlib, json, math, itertools
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
P96 = sorted((Fr(r["a"]), Fr(r["b"])) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text()))
E30 = [(Fr(j, 30), Fr(k, 30)) for j in range(30) for k in range(30) if (j, k) != (0, 0)]
SEC = ("up", "down", "lep"); RD = ("S", "St")
def L(x): return None if x == 0 else float(mp.log(x))
def data(arg):
    x, y, a, b = arg
    Y = {(s, r): DL.parts(x, y, a, b, s)[2][r] for s in SEC for r in ("S",)}
    for s in SEC:
        rd = DL.parts(x, y, a, b, s)[2]; Y[(s, "St")] = rd["St"]
    m, U = {}, {}
    for k, A in Y.items():
        sv = sorted(abs(v) for v in mp.svd_c(A, compute_uv=False)); m[k] = (L(sv[1] / sv[2]), L(sv[0] / sv[2])); U[k] = CM.U_of(A)
    V = {}
    for k1 in Y:
        for k2 in Y:
            if k1[0] == k2[0]: continue
            W = U[k1].H * U[k2]; V[(k1, k2)] = (L(abs(W[0, 1])), L(abs(W[1, 2])), L(abs(W[0, 2])))
    return m, V
def vec(m, V, perm, rds):
    ks = [(perm[i], rds[i]) for i in range(3)]
    return list(m[ks[0]]) + list(m[ks[1]]) + list(m[ks[2]]) + list(V[(ks[0], ks[1])])
def dist(u, v):
    d = 0.0
    for p, q in zip(u, v):
        if (p is None) != (q is None): return math.inf
        if p is not None: d = max(d, abs(p - q) / max(1.0, abs(p)))
    return d
ASSIGN = [(perm, rds) for perm in itertools.permutations(SEC) for rds in itertools.product(RD, repeat=3)]
def best(src, par):
    out = []
    for (m, V) in src:
        u = vec(m, V, SEC, ("S", "S", "S"))
        out.append(min(dist(u, vec(m2, V2, perm, rds)) for (m2, V2) in par for (perm, rds) in ASSIGN))
    out.sort(); return out[-1], out[len(out) // 2]
if __name__ == "__main__":
    with Pool(6) as pool:
        for (y, yp) in ((1.5, 1 / 1.5), (2.5, 0.4)):
            src = pool.map(data, [("0", y, a, b) for (a, b) in P96], chunksize=8)
            par = pool.map(data, [("0", yp, a, b) for (a, b) in E30], chunksize=8)
            if y == 1.5:
                ctl = pool.map(data, [("0", y, a, b) for (a, b) in E30], chunksize=8)
                print("control (same height 1.5, all 48 assignments): largest d %.1e" % best(src, ctl)[0], flush=True)
            big, med = best(src, par)
            print("S move, height %.4f against %.4f, any sector permutation, reading and up/down order: largest d %.1e, median %.1e" % (y, yp, big, med), flush=True)
