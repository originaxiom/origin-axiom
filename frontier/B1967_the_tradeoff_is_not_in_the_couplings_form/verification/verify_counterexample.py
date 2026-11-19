"""B1967 (main, 2026-11-19; data-free): the counterexample to the trade-off's every-channel form, recomputed at 50 digits.
B1736's coupling Y(h; u, w) = u h^T + h u^T - (u.h) 1 + w [h]_x; the charge rule: up takes conj(h) with its channels
(u_u, w_u), down takes h with (u_d, w_d).  h = (cos t, i sin t, 0) with cos 2t = r = 0.003 (|h| = 1, |h.h| = r).
The channels are the ones the search saved (counterexample_channels.json).  Printed: r, each sector's singular values
in ascending order and their ratios, the mixing |U_up^H U_down| and its smallest diagonal.
    python3 verify_counterexample.py > verify_counterexample_run.txt"""
import json, pathlib
import mpmath as mp
mp.mp.dps = 50
HERE = pathlib.Path(__file__).resolve().parent
p = [mp.mpf(repr(v)) for v in json.loads((HERE / "counterexample_channels.json").read_text())["0.003"]]
r = mp.mpf("0.003"); t = mp.acos(r) / 2
h = mp.matrix([mp.cos(t), mp.mpc(0, 1) * mp.sin(t), 0])
def cross(v): return mp.matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def Y(hh, u, w): return u * hh.T + hh * u.T - (u.T * hh)[0] * mp.eye(3) + w * cross(hh)
c = lambda a, b: mp.mpc(a, b)
uu = mp.matrix([c(p[0], p[3]), c(p[1], p[4]), c(p[2], p[5])]); wu = c(p[6], p[7])
ud = mp.matrix([c(p[8], p[11]), c(p[9], p[12]), c(p[10], p[13])]); wd = c(p[14], p[15])
hbar = mp.matrix([mp.conj(x) for x in h])
def lsv(M):
    U, S, V = mp.svd_c(M); o = sorted(range(3), key=lambda i: S[i]); return mp.matrix([[U[i, j] for j in o] for i in range(3)]), [S[i] for i in o]
Uu, su = lsv(Y(hbar, uu, wu)); Ud, sd = lsv(Y(h, ud, wd))
V = Uu.H * Ud
print("r = |h.h| = %s" % mp.nstr(abs((h.T * h)[0]), 12))
for name, s in (("up (conj h)", su), ("down (h)", sd)):
    print("%-12s singular values %s; m1/m2 = %s, m2/m3 = %s" % (name, [mp.nstr(x, 10) for x in s], mp.nstr(s[0] / s[1], 6), mp.nstr(s[1] / s[2], 6)))
print("|V| =", [[mp.nstr(abs(V[i, j]), 6) for j in range(3)] for i in range(3)])
print("smallest diagonal |V| = %s" % mp.nstr(min(abs(V[k, k]) for k in range(3)), 8))
