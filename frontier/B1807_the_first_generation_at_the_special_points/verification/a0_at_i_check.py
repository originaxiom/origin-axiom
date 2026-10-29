"""Main's check of the P-406 referee's B3 (r6): B1697's a0 = d2R - E4 R/48 at tau = i, exact s2/s1 by SVD (no proxy)."""
import sys, pathlib
from fractions import Fraction as F
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import importlib.util
spec = importlib.util.spec_from_file_location("fg", HERE / "first_generation_near_i.py")
src = (HERE / "first_generation_near_i.py").read_text().split("I = mp.mpc(0, 1); out =")[0]
ns = {"__file__": str(HERE / "first_generation_near_i.py")}; exec(compile(src, "fg", "exec"), ns)
S, Bs, e4, lift, ev, R = ns["S"], ns["Bs"], ns["e4"], ns["lift"], ns["ev"], ns["R"]
a0 = [Bs[2][i] - e4 * Bs[0][i] * S.c(F(1, 48)) for i in range(3)]
I = mp.mpc(0, 1)
for eps in (0, mp.mpf(10) ** -8, mp.mpf(10) ** -3):
    l, m23 = lift(a0, I + eps * mp.exp(0.7j))
    print("eps", mp.nstr(eps, 3), "m2/m3", mp.nstr(m23, 15), "lift", mp.nstr(l, 8))
print("closed form (B1806): x = 3/(2|288 t + 5|), t = -1/48 ->", F(3, 2) / abs(F(288) * F(-1, 48) + 5), "-> min(x, 1/x) = 2/3")
