"""B1971 (main, 2026-11-24; data-free): the all-S frame in B1736's variables.
For each sector at the mark and the twin: (u, w) from the channel matrix (B1968's conversion, in mpmath), h solved from
Y = u h^T + h u^T - (u.h) 1 + w [h]_x (linear in h; residual printed), then the rates (eps units) of the invariants
h.h, u.u + w^2, u.h, each component of h and u, and of the Hermitian quantities |h|, |u|."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
from fractions import Fraction as Fr
mp = DL.mp

def cross(v): return mp.matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def dot(a, b): return sum(a[i] * b[i] for i in range(3))
def Yof(h, u, w):
    M = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3): M[i, j] = u[i] * h[j] + h[i] * u[j] + w * cross(h)[i, j]
    for i in range(3): M[i, i] -= dot(u, h)
    return M

def vars_of(y, a, b, sec):
    RD, Mw, Ys, *_ = DL.parts("0.13", y, a, b, sec)
    m0 = (Mw[0, 0] + Mw[1, 1]) / 2; m1 = (Mw[0, 0] - Mw[1, 1]) / (2j); m2 = (Mw[0, 1] - Mw[1, 0]) / 2; m3 = (Mw[0, 1] + Mw[1, 0]) / (2j)
    u = [-2 * m0, 2 * m3, -2 * m1]; w = -2 * m2
    Yf = Ys["S"]
    A = mp.zeros(9, 3); rhs = mp.zeros(9, 1)
    for k in range(3):
        e = [mp.mpf(0)] * 3; e[k] = mp.mpf(1)
        Bk = Yof(e, u, w)
        for i in range(3):
            for j in range(3): A[3 * i + j, k] = Bk[i, j]
    for i in range(3):
        for j in range(3): rhs[3 * i + j] = Yf[i, j]
    h = mp.lu_solve(A.H * A, A.H * rhs); h = [h[0], h[1], h[2]]
    res = mp.mnorm(Yof(h, u, w) - Yf, 1) / mp.mnorm(Yf, 1)
    return dict(u=u, w=w, h=h, res=res, Y=Yf)

def rate(v1, v2, y1, y2):
    v1, v2 = abs(v1), abs(v2)
    if v1 == 0 or v2 == 0: return None
    return round(float(-(mp.log(v2) - mp.log(v1)) / (mp.pi * (y2 - y1))), 4)

if __name__ == "__main__":
    y1, y2 = 20.0, 30.0
    for name, (a, b) in {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}.items():
        for sec in ("up", "down"):
            A_, B_ = vars_of(y1, a, b, sec), vars_of(y2, a, b, sec)
            print("== %s %s: closed-form residual %.1e, %.1e" % (name, sec, float(A_["res"]), float(B_["res"])))
            inv = lambda V: dict(hh=dot(V["h"], V["h"]), uuww=dot(V["u"], V["u"]) + V["w"] ** 2, uh=dot(V["u"], V["h"]), w=V["w"],
                                 h1=V["h"][0], h2=V["h"][1], h3=V["h"][2], u1=V["u"][0], u2=V["u"][1], u3=V["u"][2],
                                 h2pih3=V["h"][1] + 1j * V["h"][2], h2mih3=V["h"][1] - 1j * V["h"][2],
                                 u2piu3=V["u"][1] + 1j * V["u"][2], u2miu3=V["u"][1] - 1j * V["u"][2],
                                 hxu1=(V["h"][1] * V["u"][2] - V["h"][2] * V["u"][1]))
            I1, I2 = inv(A_), inv(B_)
            print("   rates:", {k: rate(I1[k], I2[k], y1, y2) for k in I1})
            for yy, VV in ((y1, A_), (y2, B_)):
                tt = mp.mpc(mp.mpf("0.13"), mp.mpf(yy)); eta = mp.exp(1j * mp.pi * tt / 12) * mp.qp(mp.exp(2j * mp.pi * tt))
                print("   height %s: h.h / (eta^6/4) = %s   (B1739's identity)" % (yy, mp.nstr(dot(VV["h"], VV["h"]) / (eta ** 6 / 4), 12)))
            print("   at y2: h ratios h2/h3 = %s ; u2/u3 = %s" % (mp.nstr(B_["h"][1] / B_["h"][2], 8), mp.nstr(B_["u"][1] / B_["u"][2], 8) if B_["u"][2] != 0 else "-"))
