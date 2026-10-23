"""B1745 (P-358, data-free): main's own check of the web seat's THE_NEXT_ATTACK frame locks K1, K3, K4 and K7.
K1: F^dagger Y F in rho(T)'s eigenframe (f1 = n-bar, f2 = e1, f3 = n) equals the seat's canonical matrix, exactly (sympy),
    for Y = u h^T + h u^T - (u.h) 1 + w [h]_x, h = f3 + delta f2 + eps f1, u = a3 f3 + a2 f2 + a1 f1.
K3: under the null Higgs n, |V_cb| from the SVD of main's own coupling (B1723's b1656_funcs via B1742's channels) against
    |kappa_u - kappa_d| with kappa_s = [(a2 - i w) conj(2 a3) - a1 conj(a2 + i w)] / (4|a3|^2 + |a2 + i w|^2), on random
    points of B1742's grid, both horocycles; both signs of w = +-u1 are tried (B1736 part D writes -u1 [h]_x in the
    permuted (i, j, k) order; in coupling()'s own order the sign flips) and reported -- the wrong sign is the control.
K4: the up channel on the ten (2/5, k/10) lines: u1 = 0 exactly on order-5 lines, a2 = u.e1 = 0 exactly on order-10 lines.
K7: the cusp coefficients of R and DR (B1691): delta/r^(1/2) and eps/r at Im tau 3.5 and 4.0 (R: 2 sqrt2 and 4; DR: 4 sqrt2
    and 20)."""
import sys, json, math, pathlib
import numpy as np
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1742_two_higgs_verified_on_main" / "verification"))
import repro as R      # noqa: E402
import scan as SC      # noqa: E402


def k1():
    d, e, a1, a2, a3, w = sp.symbols("delta epsilon a1 a2 a3 w")
    s2 = sp.sqrt(2); f1 = sp.Matrix([0, 1, -sp.I]) / s2; f2 = sp.Matrix([1, 0, 0]); f3 = sp.Matrix([0, 1, sp.I]) / s2
    F = sp.Matrix.hstack(f1, f2, f3)
    h = f3 + d * f2 + e * f1; u = a3 * f3 + a2 * f2 + a1 * f1
    cross = lambda v: sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]]); dot = lambda x, y: (x.T * y)[0]
    Y = u * h.T + h * u.T - dot(u, h) * sp.eye(3) + w * cross(h)
    M = sp.simplify(F.H * Y * F)
    I = sp.I
    seat = sp.Matrix([[d * (I * w - a2), d * a1 + e * (a2 - I * w), 2 * e * a1],
                      [a2 - I * w + d * a3, d * a2 - e * a3 - a1, d * a1 + e * (a2 + I * w)],
                      [2 * a3, a2 + I * w + d * a3, -d * (a2 + I * w)]])
    return {"F^dagger Y F - seat's matrix (simplified, max entry)": str(sp.simplify(M - seat))}


P3 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)


def kappa(u1, u, sign):
    w = sign * u1; a3, a2, a1 = u @ F1, u @ F2, u @ F3          # bilinear: u = a3 f3 + a2 f2 + a1 f1, f1.f3 = 1
    return ((a2 - 1j * w) * np.conj(2 * a3) - a1 * np.conj(a2 + 1j * w)) / (4 * abs(a3) ** 2 + abs(a2 + 1j * w) ** 2)


def point(task):
    k, re_t, im_t = task; a, b = SC.LINES[k]; B = R.CEN._modules()["B"]
    t = complex(re_t, im_t); w = float(a) * t + float(b); col = R.CEN._modules()["col"]; out = []
    S = R.Smat([0, 1 / math.sqrt(2), 1j / math.sqrt(2)], B)
    for hor, ix in (("L_max", 1), ("L_2", 2)):
        L = float(np.interp(im_t, [q[0] for q in col], [q[ix] for q in col])); Y, ch = {}, {}
        for sec, (lf, rf) in R.SECT.items():
            x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
            uu = {s: (math.sqrt(2 * math.pi * L + c[s]) * Rr[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            Y[sec] = B.coupling(S, B.weighted_M(uu)); ch[sec] = (uu["1"], np.array([uu["i"], uu["j"], uu["k"]]))
        Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
        vcb = abs(V[1, 2]); row = {"line": k, "tau": [re_t, im_t], "hor": hor, "Vcb_svd": float(vcb)}
        for sign in (-1, 1):
            ku, kd = kappa(*ch["up"], sign), kappa(*ch["down"], sign)
            row["rel_err_sign%+d" % sign] = float(abs(abs(ku - kd) - vcb) / vcb)
        out.append(row)
    return out


def k4():
    B = R.CEN._modules()["B"]; col = R.CEN._modules()["col"]; out = {"order 5 max |u1|/|u|": 0.0, "order 10 max |a2|/|u|": 0.0, "order 5 min |a2|/|u|": 9.0, "order 10 min |u1|/|u|": 9.0}
    for k in range(10):
        a, b = SC.LINES[k]
        for re_t in (0.1875, 0.5625, 0.8125):
            for im_t in (2.0, 2.7, 3.4):
                t = complex(re_t, im_t); w = float(a) * t + float(b); L = float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))
                x, yy = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["u"]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
                uu = {s: (math.sqrt(2 * math.pi * L + c[s]) * Rr[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
                u = np.array([uu["i"], uu["j"], uu["k"]]); nu = np.linalg.norm(u); a2 = abs(u @ F2) / nu; u1 = abs(uu["1"]) / nu
                if k % 2 == 0: out["order 5 max |u1|/|u|"] = max(out["order 5 max |u1|/|u|"], u1); out["order 5 min |a2|/|u|"] = min(out["order 5 min |a2|/|u|"], a2)
                else: out["order 10 max |a2|/|u|"] = max(out["order 10 max |a2|/|u|"], a2); out["order 10 min |u1|/|u|"] = min(out["order 10 min |u1|/|u|"], u1)
    return out


def k7():
    import mpmath as mp
    te = R.CEN._modules()["te"]; out = {}
    for nm, ix in (("R", 0), ("DR", 1)):
        for im_t in (3.5, 4.0):
            t = complex(0.3, im_t); h = np.array([complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[ix]])
            c1, c0, c0b = np.vdot(F2, h), np.vdot(F3, h), np.vdot(F1, h); lead, other = (c0, c0b) if abs(c0) >= abs(c0b) else (c0b, c0)
            r = math.exp(-math.pi * im_t); out["%s at 0.3 + %.1fi" % (nm, im_t)] = [abs(c1 / lead) / math.sqrt(r), abs(other / lead) / r]
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    HERE = pathlib.Path(__file__).resolve().parent
    res = {"K1": k1(), "K4": k4(), "K7": k7()}
    for kk in ("K1", "K4", "K7"): print(kk, res[kk], flush=True)
    rng = np.random.default_rng(358); tasks = [(int(rng.integers(10)), 0.0625 + 0.125 * int(rng.integers(8)), round(2.0 + 0.1 * int(rng.integers(16)), 10)) for _ in range(96)]
    with Pool(8) as Pp: rows = [r for o in Pp.map(point, tasks) for r in o]
    res["K3 rows"] = rows
    for sign in (-1, 1):
        e = np.array([r["rel_err_sign%+d" % sign] for r in rows])
        res["K3 sign %+d" % sign] = {"median rel err": float(np.median(e)), "max": float(e.max()), "rows": len(e)}
        print("K3 w = %+d u1: |V_cb| vs |kappa_u - kappa_d| median %.4f, max %.4f over %d rows" % (sign, np.median(e), e.max(), len(e)))
    (HERE / "frame_locks.json").write_text(json.dumps(res, indent=1) + "\n")
