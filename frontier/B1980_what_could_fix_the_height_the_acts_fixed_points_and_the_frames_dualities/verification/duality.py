"""B1980 part B (main, 2026-11-25; data-free): is frame C at order 30 symmetric under a duality tau -> -K/tau? On the imaginary
axis, the nine log outputs at B1976's 96 points at height y are matched against those at all 899 nonzero points of E[30] at
height K/y; controls C0 (same height) and C1 (Re tau 0 against 1). The card (../CARD.md) fixes the K, the heights and the bar.
    python3 -B duality.py > duality_run.txt"""
import sys, pathlib, json, time, math
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
P96 = sorted((Fr(r["a"]), Fr(r["b"])) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text()))
E30 = [(Fr(j, 30), Fr(k, 30)) for j in range(30) for k in range(30) if (j, k) != (0, 0)]
KS = (1, 2, 3, 5, 6, 10, 15, 30, 60, 900)
def outputs(arg):
    x, y, a, b = arg
    Y = {s: DL.parts(x, y, a, b, s)[2]["S"] for s in ("up", "down", "lep")}
    o = []
    for s in ("up", "down", "lep"):
        sv = sorted(abs(v) for v in mp.svd_c(Y[s], compute_uv=False))
        o += [mp.log(sv[1] / sv[2]) if sv[1] > 0 else None, mp.log(sv[0] / sv[2]) if sv[0] > 0 else None]
    V = CM.U_of(Y["up"]).H * CM.U_of(Y["down"])
    o += [mp.log(abs(V[i, j])) if abs(V[i, j]) > 0 else None for (i, j) in ((0, 1), (1, 2), (0, 2))]
    return [None if v is None else float(v) for v in o]
def table(x, y, pts, pool):
    return dict(zip(pts, pool.map(outputs, [(x, y, a, b) for (a, b) in pts], chunksize=8)))
def dist(u, v):
    m = 0.0
    for p, q in zip(u, v):
        if (p is None) != (q is None): return math.inf
        if p is not None: m = max(m, abs(p - q) / max(1.0, abs(p)))
    return m
def match(src, par):
    ds = sorted(min(dist(u, v) for v in par.values()) for u in src.values())
    return ds[-1], ds[len(ds) // 2]
if __name__ == "__main__":
    t0 = time.time(); res = {}
    with Pool(6) as pool:
        s2 = table("0", 2.0, P96, pool); p2 = table("0", 2.0, E30, pool); q2 = table("1", 2.0, E30, pool)
        res["C0"] = match(s2, p2); res["C1"] = match(s2, q2)
        print("C0 (same height, identity): largest d %.1e, median %.1e  [%.0f s]" % (*res["C0"], time.time() - t0), flush=True)
        print("C1 (Re tau 0 against 1, the T move): largest d %.1e, median %.1e  [%.0f s]" % (*res["C1"], time.time() - t0), flush=True)
        for K in KS:
            r = []
            for f in (1.5, 2.5):
                y = f * math.sqrt(K); yp = K / y
                src = table("0", y, P96, pool); par = table("0", yp, E30, pool)
                big, med = match(src, par); r.append((y, yp, big, med))
                print("K = %d: source height %.4f against %.4f: largest d %.1e, median %.1e  [%.0f s]" % (K, y, yp, big, med, time.time() - t0), flush=True)
            res[K] = r
    print("SUMMARY C0 passes: %s; C1 passes: %s" % (res["C0"][0] == 0.0, res["C1"][0] < 1e-8))
    print("SUMMARY dualities passing (largest d < 1e-8 at both heights): %s" % [K for K in KS if all(x[2] < 1e-8 for x in res[K])])
    print("SUMMARY least largest-d over the K (the nearest to a duality): %s" % sorted(((min(x[2] for x in res[K]), K) for K in KS))[:3])
