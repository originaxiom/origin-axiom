"""B1949, R4 (main, 2026-11-15; data-free; card ddee39436): the frame's Georgi-Jarlskog factor in the cusp limit.
Frame C's average over the points of exact order N (N = 5, 10, 15) of sigma2/sigma3 and sigma1/sigma3 for the leptons and
the down quarks, the same Higgs reading in both (as in both declared worlds), at heights 16, 22 and 28 on the column
x = 0.13, at 40 + 3.5 Im tau digits; the ratios lepton / down are printed with their drift between heights. Nothing is
set beside a measured number."""
import sys, json, inspect, pathlib
from fractions import Fraction as Fr
from math import gcd
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp
src = inspect.getsource(DL.parts).replace("mp.mp.dps = int(30 + 2 * ty)", "mp.mp.dps = int(40 + 3.5 * ty)")
assert "40 + 3.5 * ty" in src
ns = dict(DL.__dict__); exec(src, ns); parts = ns["parts"]
def ratios(Y):
    s = sorted((abs(v) for v in mp.svd_c(Y, compute_uv=False)), reverse=True)
    return [s[1] / s[0], s[2] / s[0]]
out = {}
for N in (5, 10, 15):
    pts = [(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
    for y in (16.0, 22.0, 28.0):
        acc = {}
        for a, b in pts:
            for sec in ("lep", "down"):
                _, _, Ys, *_ = parts("0.13", y, a, b, sec)
                for rd in ("S", "St"):
                    r = ratios(Ys[rd])
                    k = (sec, rd); acc[k] = [p + q for p, q in zip(acc.get(k, [0, 0]), r)]
        for rd in ("S", "St"):
            l = [v / len(pts) for v in acc[("lep", rd)]]; d = [v / len(pts) for v in acc[("down", rd)]]
            out["%d|%s|%s" % (N, rd, y)] = {"lep": [float(v) for v in l], "down": [float(v) for v in d], "ratio": [float(l[0] / d[0]), float(l[1] / d[1])]}
            print("N = %2d, reading %-2s, height %4.0f: lepton/down average  m2/m3 %.6f   m1/m3 %.6f" % (N, rd, y, float(l[0] / d[0]), float(l[1] / d[1])), flush=True)
(pathlib.Path(__file__).resolve().parent / "r4_gj_factor.json").write_text(json.dumps(out, indent=1))
