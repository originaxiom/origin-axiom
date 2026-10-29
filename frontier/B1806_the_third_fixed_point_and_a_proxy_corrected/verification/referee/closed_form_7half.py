"""The weight-7/2 family a = alpha E4 R + gamma D2R at tau = i in closed form (referee's derivation, checked here):
singular values at i on rho(S)'s double eigenspace are |a.R| and 2|a.Rbar|; a.R(i) = -gamma DR.DR(i); a.Rbar(i) =
E4(i)|R(i)|^2 (alpha + 5/288 gamma) (alpha* = -5/288 is the identically isotropic section); so with t = alpha/gamma
m2/m3(i) = min(x, 1/x), x = c / |t + 5/288|, c = |DR(i)|^2 / (2 E4(i) |R(i)|^2). Checks c = 1/192 and the formula on the draft's seeds."""
import json, pathlib, random
from fractions import Fraction as F
import mpmath as mp
src = (pathlib.Path(__file__).with_name("referee_check.py")).read_text().split("# ---- 1.")[0]
ns = {"__file__": str(pathlib.Path(__file__).with_name("referee_check.py"))}; exec(src, ns)
mp.mp.dps = 50
I = mp.mpc(0, 1); basis, masses, E4, nrm, dot = ns["basis"], ns["masses"], ns["E4"], ns["nrm"], ns["dot"]
b = basis(I); e4 = E4(I)
c = abs(nrm(b[1]) / (2 * e4 * nrm(b[0])))
out = {"c": mp.nstr(c, 40), "c - 1/192": mp.nstr(c - mp.mpf(1) / 192, 3),
       "D2R(i).conjR(i) / (E4(i)|R(i)|^2) - 5/288": mp.nstr(dot(b[2], [mp.conj(x) for x in b[0]]) / (e4 * nrm(b[0])) - mp.mpf(5) / 288, 3),
       "|DR.DR(i)| - |DR(i)|^2": mp.nstr(abs(dot(b[1], b[1])) - nrm(b[1]), 3)}
# the draft's weight-7/2 seeds: alpha (E4 R) and gamma (D2R) from B1691's RNG
for seed in (1, 2):
    rng = random.Random(1000 * seed + 2); cs = []
    # Mbasis(4) = [E4], Mbasis(2) = [], Mbasis(0) = [1]
    cs = {}
    for j, w in ((0, 4), (1, 2), (2, 0)):
        nb = {4: 1, 2: 0, 0: 1}[w]
        for _ in range(nb):
            re = F(rng.randint(-9, 9) or 1, rng.randint(1, 5)); im = F(rng.randint(-9, 9), rng.randint(1, 5))
            cs[j] = complex(re) + 1j * complex(im)
    t = mp.mpc(cs[0]) / mp.mpc(cs[2]); x = c / abs(t + mp.mpf(5) / 288)
    a = [mp.mpc(cs[0]) * e4 * b[0][k] + mp.mpc(cs[2]) * b[2][k] for k in range(3)]
    out["seed%d" % seed] = {"t": mp.nstr(t, 8), "formula": mp.nstr(min(x, 1 / x), 12), "svd": mp.nstr(masses(a, b[0])[1], 12)}
pathlib.Path(__file__).with_name("closed_form_7half.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
