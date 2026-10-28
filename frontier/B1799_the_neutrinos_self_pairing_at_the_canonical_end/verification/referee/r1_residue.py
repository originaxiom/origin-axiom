"""Referee B1799, check 1(a): the residue matrix of b1656_funcs.bil at u = 0, against the closed form
   Res = v_x v_y^T / theta1'(0),  v_x = (X0(0), e^{i pi b_x} X1(0) / (i e^{-i pi t/2}))
derived from theta1(u + t) = -e^{-i pi t} e^{-2 i pi u} theta1(u).  So the residue is rank one for EVERY twist pair (not only
equal twists), and symmetric (v (x) v) when x = y, phases included.  R_1 = v_x^T eps v_y / theta1'(0).
Read-only; imports B1723's b1656_funcs."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, pathlib
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
sys.path.insert(0, str(ROOT / "frontier/B1723_the_golden_valley/verification")); _a = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _a
rng = np.random.default_rng(7101)


def closed(x, y, t):
    (ax, bx), (ay, by) = x, y; T = 2 * t
    h = 1e-6; d1 = (B.th1(h, t) - B.th1(-h, t)) / (2 * h)          # theta1'(0)
    al = 1j * np.exp(-1j * np.pi * t / 2)
    vx = np.array([B.thc(ax, bx, 0.0, T), np.exp(1j * np.pi * bx) * B.thc(ax, bx, t, T) / al])
    vy = np.array([B.thc(ay, by, 0.0, T), np.exp(1j * np.pi * by) * B.thc(ay, by, t, T) / al])
    return np.outer(vx, vy) / d1, vx, vy, d1


def num_res(x, y, t, rad=0.01, N=256):
    u = rad * np.exp(2j * np.pi * np.arange(N) / N); M = B.bil(x, y, u, t)
    return np.array([[np.mean(M[i][j] * u) for j in range(2)] for i in range(2)])


worst_gen = worst_eq = worst_sym = worst_R1 = worst_rank = 0.0
for trial in range(40):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 3.2))
    x = (rng.uniform(-3, 3), rng.uniform(-6, 6)); y = (rng.uniform(-3, 3), rng.uniform(-6, 6))
    Rn = num_res(x, y, t); Rc, vx, vy, d1 = closed(x, y, t)
    worst_gen = max(worst_gen, np.linalg.norm(Rn - Rc) / np.linalg.norm(Rn))
    sv = np.linalg.svd(Rn, compute_uv=False); worst_rank = max(worst_rank, sv[1] / sv[0])
    Rn2 = num_res(x, x, t); Rc2, v, _, _ = closed(x, x, t)
    worst_eq = max(worst_eq, np.linalg.norm(Rn2 - Rc2) / np.linalg.norm(Rn2))
    worst_sym = max(worst_sym, np.linalg.norm(Rn2 - Rn2.T) / np.linalg.norm(Rn2))
    Rd = B.residues(x, x, t); worst_R1 = max(worst_R1, abs(Rd["1"]) / math.sqrt(B.nR2(Rd)))
print("general twist pairs (40): |Res_num - v_x v_y^T/th1'| / |Res| max %.2e;  sigma2/sigma1 of Res max %.2e" % (worst_gen, worst_rank))
print("equal twists (40): closed form %.2e; |Res - Res^T|/|Res| max %.2e; R1/|R| (B.residues) max %.2e" % (worst_eq, worst_sym, worst_R1))
# R_s = sum_{mn} (eps C_s)_{mn} Res_{mn} = v_x^T (eps C_s) v_y / th1': the '1' channel is v^T eps v = 0 for x = y
t = complex(0.37, 2.2); x = (0.4, -1.3)
Rc, v, _, d1 = closed(x, x, t)
print("check R1 = v^T eps v / th1' at x = y:", abs(v @ B.EPS @ v / d1))
# the sectors' actual twists: LL (-3w, -3w) and nucnuc ((0,0),(0,0)) are bitwise equal float tuples?
for (a, b) in ((0.4, 49 / 60), (1 / 7, 3 / 7)):
    w = a * t + b
    xl, yl = B.sector_twists(w, t, -3, -3); x0, y0 = B.sector_twists(w, t, 0, 0)
    print("line (%.4f, %.4f): LL twists identical %s; nucnuc twists %s %s" % (a, b, xl == yl, x0, y0))
print("r1 exit 0")
