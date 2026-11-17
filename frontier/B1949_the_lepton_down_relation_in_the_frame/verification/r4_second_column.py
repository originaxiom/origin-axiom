"""B1949, R4's robustness check, added after the sealed run was read (not blind; main, 2026-11-17): the order-10
lepton/down ratio of the averaged sigma2/sigma3 on a second column, x = 0.37, at height 22. If the constant is free of
tau it must equal the first column's 0.634644 (S) and 1.575687 (S-tilde)."""
import sys, inspect, pathlib
from fractions import Fraction as Fr
from math import gcd
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp
src = inspect.getsource(DL.parts).replace("mp.mp.dps = int(30 + 2 * ty)", "mp.mp.dps = int(40 + 3.5 * ty)")
assert "40 + 3.5 * ty" in src
ns = dict(DL.__dict__); exec(src, ns); parts = ns["parts"]
N = 10; pts = [(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
acc = {}
for a, b in pts:
    for sec in ("lep", "down"):
        _, _, Ys, *_ = parts("0.37", 22.0, a, b, sec)
        for rd in ("S", "St"):
            s = sorted((abs(v) for v in mp.svd_c(Ys[rd], compute_uv=False)), reverse=True)
            acc[(sec, rd)] = acc.get((sec, rd), 0) + s[1] / s[0]
for rd in ("S", "St"):
    print("N = 10, reading %-2s, x = 0.37, height 22: lepton/down average m2/m3 %.6f" % (rd, float(acc[("lep", rd)] / acc[("down", rd)])))
