"""rf4: an independent numerical route for the channel data at (i, (1/2, 1/2)) and (i, 0), up sector: residues from
B1653's mpmath bilinear (bil_mp, mp.jtheta-based, not the numpy truncated sums) on a contour of radius 0.03 with 96
points; regularised norms from route B (cB: Gauss-Legendre on the four strips with the Laurent subtraction, not route A's
log-polar quadrature).  Then the coupling assembled by my own einsum (not B.coupling/B.weighted_M) and the a0 / F_10
exception rows recomputed against the draft's JSON."""
import json, math, time
import numpy as np, mpmath as mp
from rf_common import *
mp.mp.dps = 20
EPS = np.array([[0, 1], [-1, 0]], dtype=complex); QI = np.diag([1j, -1j]); QJ = EPS.copy(); QK = QI @ QJ
UN = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}; BL = [QJ, QI, QK]
def resid_mp(x, y, t, s, rho=0.03, N=96):
    acc = mp.mpc(0)
    for n in range(N):
        z = rho * mp.expjpi(2 * mp.mpf(n) / N); acc += B.pair_mp(B.bil_mp(x, y, z, t), s) * z
    return complex(acc / N)
def my_coupling(Sm, u):
    G = np.array([[np.sum((EPS @ UN[t]) * UN[s]) for s in UN] for t in UN]); Gi = np.linalg.inv(G); keys = list(UN)
    Ed = {keys[a]: sum(Gi[b, a] * UN[keys[b]] for b in range(4)) for a in range(4)}
    M = sum(u[s] * Ed[s] for s in UN)
    return np.array([[np.einsum("mn,mn->", Ca.T @ EPS @ Sm @ Cb, M) for Cb in BL] for Ca in BL])
res = {}
draft = {(r["config"], r["direction"], r["radius"], r["reading"]): r for r in json.load(open(pathlib.Path(__file__).resolve().parents[1] / "symmetry_selection_table_second_launch.json"))["rows"]}
for cn, p in (("(i, (1/2, 1/2))", (0.5, 0.5)), ("(i, 0)", (0, 0))):
    t = 1j; w = B.line_w(p[0], p[1], t); x, y = B.sector_twists(w, t, 1, -4)
    xm = (mp.mpf(x[0]), mp.mpf(x[1])); ym = (mp.mpf(y[0]), mp.mpf(y[1])); tm = mp.mpc(0, 1)
    RA, cAv = channels(t, p, 1, -4)
    RB, cBv = {}, {}
    for s in UN:
        t0 = time.time(); RB[s] = resid_mp(xm, ym, tm, s)
        cBv[s] = cB(*(None,)) if False else (B.cB(x, y, t, s, RB[s]) if abs(RB[s]) > 1e-12 else None)
        print(cn, s, "R: route A %s  mp %s | c: route A %s  route B %s  (%.0fs)" % (np.round(RA[s], 9), np.round(RB[s], 9), cAv[s], cBv[s], time.time() - t0), flush=True)
    res[cn] = {s: {"R_A": str(RA[s]), "R_mp": str(RB[s]), "c_A": cAv[s], "c_B": cBv[s]} for s in UN}
    for d in ("a0", "F_10", "R"):
        a = direction(d, I)
        for Ln, L in zip(("L_max", "L_2"), RADII[I]):
            u = {s: (math.sqrt(2 * math.pi * L + cBv[s]) * RB[s] if cBv[s] is not None else 0) for s in UN}
            Sm = a[0] * QI + a[1] * QJ + a[2] * QK; St = EPS @ Sm.conj() @ EPS.T
            Uu, su, _ = svd_sorted(my_coupling(St, u)); Ud, sd, _ = svd_sorted(my_coupling(Sm, u))
            Vm = np.abs(Uu.conj().T @ Ud)
            mine = [su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2], Vm[0, 1], Vm[1, 2], Vm[0, 2]]
            dr = draft[(cn, d, Ln, "S~SS")]
            theirs = dr["up"] + dr["down"] + dr["|V_us|, |V_cb|, |V_ub|"]
            print("  %s %s %s  route-B: %s\n%s draft  : %s  max|diff| %.1e" % (cn, d, Ln, np.round(mine, 6), " " * len(cn + d + Ln), np.round(theirs, 6), max(abs(np.array(mine) - np.array(theirs)))), flush=True)
json.dump(res, open(HERE / "rf4_route_B.json", "w"), indent=1)
