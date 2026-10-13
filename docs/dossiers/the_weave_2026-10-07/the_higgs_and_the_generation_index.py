"""W56 (the rule: W56_RULE.md, committed before this script). The Higgs carrying the generation index.

  K1  the E6 identity: from the explicit trinification cubic I3 = det Q_L + det Q_R + det L - tr(Q_L L Q_R^T), the
      6 x 6 down-type and charged-lepton mass matrices have singular values in one common ratio c, for 200 random
      cases (1, 2 or 3 Higgs 27s, random flavour tensors, random vacuum values in the five neutral components of L), to
      1e-10, with the same c in every case; the control (one neutral component x -3 in the lepton block only) breaks it
      by more than 1e-3 in every case.
  K2  the parity and the dimensions: dim M_k for R_G = conj(rho_T)^(x)3 and R_D = conj(rho_T) (x) conj(rho_T) (x)
      rho_T at k = 1/2, 3/2, ..., 15/2 (W50's solver); R_G has none at k = 1/2 mod 2, R_D none at k = 3/2 mod 2, and
      n = dim M_9/2(R_D) >= 2; the control T (x) T at k = 3, 5, 7 gives 2, 4, 5.
  K3  the census at the geometry's weight, the Standard Model frame, (H_u, H_d) in {(D, D), (B, D), (D, B)}: B is
      flavour-blind (W53's forms at k = 3), D the dual triplet at 3/2 (R_D's forms at 9/2, contracted with a free
      direction h; d and e share h_d). W53's 13 observables, a = 0.10, threshold 5.99, domain y <= 6. (D, D) and
      (B, D) fit; (D, B) does not.
  K4  each structure's 13 x P Jacobian has rank 13 at three random points.

  The search (fixed in the rule): W54's tau grid; at each grid tau the other parameters from 4 random starts (seeds
  (5600, the structure's index, the grid index)); a joint bounded refinement over tau and every parameter from each
  structure's 8 best grid points. A trial tau is mapped into the domain by gamma, with h -> conj(rho_T(gamma)) h.

Run: python3 the_higgs_and_the_generation_index.py  ->  the_higgs_and_the_generation_index.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import least_squares  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402  (W53: the data, the observables, the k = 3 forms)
import the_rank_thirteen_structures as RT  # noqa: E402  (W54: the tau grid)
import the_weaves_functionals_on_tau as WF  # noqa: E402  (W51: the vectorised form evaluator)

PG = FW.PG                                   # W50: rho_T in the basis t_p, the form solver
GM, H = PG.GM, PG.H
OUT = HERE / "the_higgs_and_the_generation_index.json"
A_TOL = FW.A_MAIN
NPROC = 4
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", flush=True)


def rho_T():
    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    return PG.rho_T(Ct)


AS, TM = rho_T()
CA, CT = AS.conj(), TM.conj()
REPS = {"R_G": (np.kron(np.kron(CA, CA), CA), np.kron(np.kron(CT, CT), CT)),
        "R_D": (np.kron(np.kron(CA, CA), AS), np.kron(np.kron(CT, CT), TM))}
KS_HALF = [0.5 + i for i in range(8)]


# ---------------------------------------------------------------------------------------------------------- K1: E6
def qL(a, al):
    return 3 * a + al


def qR(a, be):
    return 9 + 3 * a + be


def lL(al, be):
    return 18 + 3 * al + be


NEUTRAL = [lL(0, 0), lL(1, 1), lL(1, 2), lL(2, 1), lL(2, 2)]


def charges():
    q = np.zeros(27)
    cl, cr = (2 / 3, -1 / 3, -1 / 3), (-2 / 3, 1 / 3, 1 / 3)
    for a in range(3):
        for i in range(3):
            q[qL(a, i)], q[qR(a, i)] = cl[i], cr[i]
    for al in range(3):
        for be in range(3):
            q[lL(al, be)] = -(cl[al] + cr[be])
    return q


def I3(x):
    QL, QR, L = x[:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:].reshape(3, 3)
    return np.linalg.det(QL) + np.linalg.det(QR) + np.linalg.det(L) - np.trace(QL @ L @ QR.T)


def polar(X, Y, Z):
    """the symmetric trilinear form d with d(X, X, X) = I3(X)"""
    return (I3(X + Y + Z) - I3(X + Y) - I3(X + Z) - I3(Y + Z) + I3(X) + I3(Y) + I3(Z)) / 6


E27 = np.eye(27, dtype=complex)
DOWN = ([qL(0, 1), qL(0, 2)], [qR(0, 1), qR(0, 2)])          # Q_L's d, D (charge -1/3); Q_R's d^c, D^c (+1/3)
LEPT = ([lL(0, 1), lL(0, 2)], [lL(1, 0), lL(2, 0)])          # L's charge -1 entries; L's charge +1 entries


def block(rows, cols, v):
    return np.array([[polar(E27[x], E27[y], v) for y in cols] for x in rows])


def mass6(Ys, vs, which, deform=None):
    """the 6 x 6 mass matrix (flavour (x) gauge) from W = sum_m sum_ijk Y^m_ijk d(Phi_i, Phi_j, H^m_k)"""
    rows, cols = which
    M = np.zeros((6, 6), dtype=complex)
    for Y, v in zip(Ys, vs):
        S = Y + Y.transpose(1, 0, 2)
        for k in range(3):
            vk = v[k].copy()
            if deform is not None:
                vk[deform] *= -3
            B = block(rows, cols, vk)
            M += np.kron(S[:, :, k], B)
    return M


def K1(n=200, seed=5601):
    rng = np.random.default_rng(seed)
    q = charges()
    leak = 0.0                                   # charge-violating entries of d(e_x, e_y, v) for a neutral v
    v = np.zeros(27, dtype=complex)
    v[NEUTRAL] = rng.normal(size=5) + 1j * rng.normal(size=5)
    for x in range(27):
        for y in range(27):
            if abs(q[x] + q[y]) > 1e-9:
                leak = max(leak, abs(polar(E27[x], E27[y], v)))
    spreads, cs, ctrl = [], [], []
    for t in range(n):
        m = 1 + t % 3
        Ys = [rng.normal(size=(3, 3, 3)) + 1j * rng.normal(size=(3, 3, 3)) for _ in range(m)]
        vs = []
        for _ in range(m):
            vm = np.zeros((3, 27), dtype=complex)
            vm[:, NEUTRAL] = rng.normal(size=(3, 5)) + 1j * rng.normal(size=(3, 5))
            vs.append(vm)
        sd = np.sort(np.linalg.svd(mass6(Ys, vs, DOWN), compute_uv=False))
        se = np.sort(np.linalg.svd(mass6(Ys, vs, LEPT), compute_uv=False))
        r = se / sd
        spreads.append(float(np.max(np.abs(r / r[0] - 1))))
        cs.append(float(r[0]))
        sc = np.sort(np.linalg.svd(mass6(Ys, vs, LEPT, deform=lL(1, 1)), compute_uv=False))
        rc = sc / sd
        ctrl.append(float(np.max(np.abs(rc / rc[0] - 1))))
    c_spread = float(np.max(np.abs(np.array(cs) / cs[0] - 1)))
    out = {"the largest charge-violating entry of the cubic at a neutral vacuum value": leak,
           "the largest spread of sigma(M_e)/sigma(M_d) within a case": max(spreads),
           "the common ratio c (first case), and its largest relative spread across cases": [cs[0], c_spread],
           "the control (one neutral component x -3 in the lepton block): the smallest spread": min(ctrl)}
    ok = max(spreads) < 1e-10 and c_spread < 1e-10 and min(ctrl) > 1e-3
    return out, bool(ok)


# ------------------------------------------------------------------------------------------------- K2: the forms
def K2():
    dims = {}
    for name, (rS, rT) in REPS.items():
        dims[name] = {}
        for k in KS_HALF:
            null, gap, _, _ = PG.forms(rS, rT, k)
            dims[name][f"{k:g}"] = {"dim": null, "gap": gap}
        log(f"K2: {name} " + " ".join(f"{k:g}:{dims[name][f'{k:g}']['dim']}" for k in KS_HALF))
    rS9, rT9 = np.kron(CA, CA), np.kron(CT, CT)
    ctrl = [PG.forms(rS9, rT9, k)[0] for k in (3, 5, 7)]
    zero_G = all(dims["R_G"][f"{k:g}"]["dim"] == 0 for k in (0.5, 2.5, 4.5, 6.5))
    zero_D = all(dims["R_D"][f"{k:g}"]["dim"] == 0 for k in (1.5, 3.5, 5.5, 7.5))
    n = dims["R_D"]["4.5"]["dim"]
    ok = zero_G and zero_D and n >= 2 and ctrl == [2, 4, 5]
    return dims, ctrl, n, bool(ok)


# --------------------------------------------------------------------------------------------- K3, K4: the census
null_D, Z_D, EV_D, _ = WF.forms_vec(*REPS["R_D"], 4.5)
ND = null_D
STRUCTS = [("(D, D)", ("D", "D")), ("(B, D)", ("B", "D")), ("(D, B)", ("D", "B"))]


def forms_B(tau):
    return np.array([m / np.linalg.norm(m) for m in (f(tau) for f in FW.FORMS["T (x) T"][3])])


def forms_D(tau):
    out = []
    for a in range(ND):
        f = EV_D(Z_D[:, a], tau)[:, 0]
        out.append((f / np.linalg.norm(f)).reshape(3, 3, 3))
    return np.array(out)


def layout(pl):
    """the raw parameter layout: [h_u (6) if D] [h_d (6) if D] [alpha_u] [alpha_d] [alpha_e]"""
    hu, hd = pl
    sizes = {"u": 2 * (ND if hu == "D" else 2), "d": 2 * (ND if hd == "D" else 2), "e": 2 * (ND if hd == "D" else 2)}
    cuts, pos = {}, 0
    for key, size in (("hu", 6 if hu == "D" else 0), ("hd", 6 if hd == "D" else 0),
                      ("u", sizes["u"]), ("d", sizes["d"]), ("e", sizes["e"])):
        cuts[key] = (pos, pos + size)
        pos += size
    return cuts, pos


def p_eff(pl):
    hu, hd = pl
    d = {"u": ND if hu == "D" else 2, "d": ND if hd == "D" else 2, "e": ND if hd == "D" else 2}
    return 2 + 4 * [hu, hd].count("D") + sum(2 * x - 1 for x in d.values())


def cplx(p):
    h = len(p) // 2
    return np.asarray(p[:h]) + 1j * np.asarray(p[h:])


def yukawas(p, pl, FB, FD, R=None):
    """Y_u, Y_d, Y_e; R (if given) is rho_T(gamma) for the reduction, h -> conj(R) h"""
    cuts, _ = layout(pl)
    hs = {}
    for key, which in (("hu", pl[0]), ("hd", pl[1])):
        if which == "D":
            h = cplx(p[slice(*cuts[key])])
            hs[key] = R.conj() @ h if R is not None else h
    out = []
    for s, which, hk in (("u", pl[0], "hu"), ("d", pl[1], "hd"), ("e", pl[1], "hd")):
        al = cplx(p[slice(*cuts[s])])
        if which == "B":
            out.append(np.tensordot(al, FB, axes=1))
        else:
            out.append(np.einsum("a,aijk,k->ij", al, FD, hs[hk]))
    return out


def observables(Ys):
    logs, Us = [], []
    for Y in Ys:
        U, sv, _ = np.linalg.svd(Y)
        idx = np.argsort(sv)
        Us.append(U[:, idx])
        logs.append(np.log(np.maximum(sv[idx], 1e-300)))
    V = Us[0].conj().T @ Us[1]
    vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in FW.CKM_KEYS], 1e-300))
    return logs, vlog


def res_fixed(p, pl, FB, FD):
    logs, vlog = observables(yukawas(p, pl, FB, FD))
    return FW.residuals_from(logs, vlog, A_TOL)


def reduce_track(tau):
    """W53's reduction, with rho_T(gamma) of the map applied"""
    R = np.eye(3, dtype=complex)
    for _ in range(60):
        n = round(tau.real)
        tau = complex(tau.real - n, tau.imag)
        R = np.linalg.matrix_power(TM, -n) @ R if n else R
        if abs(tau) < 1 - 1e-15:
            tau = -1 / tau
            R = AS @ R
        else:
            break
    return tau, R


def res_joint(theta, pl):
    tau, R = reduce_track(complex(theta[0], theta[1]))
    FB = forms_B(tau) if "B" in pl else None
    FD = forms_D(tau) if "D" in pl else None
    logs, vlog = observables(yukawas(theta[2:], pl, FB, FD, R))
    return FW.residuals_from(logs, vlog, A_TOL)


def grid_task(args):
    si, gi = args
    pl = STRUCTS[si][1]
    tau = RT.GRID[gi]
    FB = forms_B(tau) if "B" in pl else None
    FD = forms_D(tau) if "D" in pl else None
    _, npar = layout(pl)
    rng = np.random.default_rng([5600, si, gi])
    best = None
    for _ in range(4):
        r = least_squares(res_fixed, rng.normal(size=npar), args=(pl, FB, FD), method="trf", xtol=1e-10,
                          ftol=1e-10, gtol=1e-10, max_nfev=400)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, r.x)
    return si, gi, best[0], best[1]


def refine_task(args):
    si, tau, p = args
    pl = STRUCTS[si][1]
    th0 = np.concatenate([[min(max(tau.real, -0.5 + 1e-9), 0.5 - 1e-9), max(tau.imag, FW.H0 + 1e-9)], p])
    n = len(p)
    lb, ub = [-0.5, FW.H0] + [-np.inf] * n, [0.5, FW.YMAX] + [np.inf] * n
    r = least_squares(res_joint, th0, args=(pl,), bounds=(lb, ub), method="trf", xtol=1e-12, ftol=1e-12,
                      gtol=1e-12, max_nfev=2000)
    return si, float(np.sum(r.fun ** 2)), r.x


def K4(si, seed=5602):
    pl = STRUCTS[si][1]
    _, npar = layout(pl)
    rng = np.random.default_rng([seed, si])
    rows = []
    for _ in range(3):
        th0 = np.array([rng.uniform(-0.4, 0.4), rng.uniform(1.05, 1.6)] + list(rng.normal(size=npar)))

        def obs13(th):
            tau = complex(th[0], th[1])
            FB = forms_B(tau) if "B" in pl else None
            FD = forms_D(tau) if "D" in pl else None
            logs, vlog = observables(yukawas(th[2:], pl, FB, FD))
            return np.concatenate(logs + [vlog])

        J = np.zeros((13, len(th0)))
        for i in range(len(th0)):
            e = np.zeros(len(th0))
            e[i] = 1e-6
            J[:, i] = (obs13(th0 + e) - obs13(th0 - e)) / 2e-6
        s = np.linalg.svd(J, compute_uv=False)
        rank = int(sum(s > 1e-6 * s[0]))
        rows.append([rank, float(s[12] / s[0])])
    return rows


def describe(si, chi, theta):
    pl = STRUCTS[si][1]
    tau, R = reduce_track(complex(theta[0], theta[1]))
    res = res_joint(theta, pl)
    return {"chi^2_min": chi, "tau (reduced)": [tau.real, tau.imag], "P (effective)": p_eff(pl),
            "fits (chi^2_min <= 5.99)": bool(chi <= FW.THRESH),
            "on the box's edge (y = 6)": bool(theta[1] >= FW.YMAX - 1e-6),
            "pulls": {lab: float(x) for lab, x in zip(FW.LABELS, res)}}


def main():
    log("K1: the E6 identity")
    k1, k1_ok = K1()
    log(f"K1 done: {k1_ok}")
    dims, ctrl, n, k2_ok = K2()
    log(f"K2 done: n = {n}, solver's n for the census = {ND}; ok = {k2_ok}")
    live = [si for si, (_, pl) in enumerate(STRUCTS) if ND > 0 or "D" not in pl]
    tasks = [(si, gi) for si in live for gi in range(len(RT.GRID))]
    with Pool(NPROC) as pool:
        grid_rows = pool.map(grid_task, tasks, chunksize=4)
    log("K3: grid done")
    best_grid = {}
    for si, gi, c, p in grid_rows:
        best_grid.setdefault(si, []).append((c, gi, p))
    rtasks = []
    for si in live:
        best_grid[si].sort(key=lambda r: r[0])
        for c, gi, p in best_grid[si][:8]:
            rtasks.append((si, RT.GRID[gi], p))
    with Pool(NPROC) as pool:
        ref = pool.map(refine_task, rtasks, chunksize=1)
    log("K3: refinement done")
    census = {}
    for si, (name, pl) in enumerate(STRUCTS):
        if "D" in pl and ND == 0:
            census[name] = {"no coupling exists at 9/2": True, "fits (chi^2_min <= 5.99)": False}
            continue
        cands = [(c, th) for s2, c, th in ref if s2 == si]
        c0, gi0, p0 = best_grid[si][0]
        g0 = RT.GRID[gi0]
        cands.append((c0, np.concatenate([[g0.real, g0.imag], p0])))
        chi, theta = min(cands, key=lambda r: r[0])
        census[name] = describe(si, chi, theta)
        census[name]["the grid's best (chi^2, tau)"] = [c0, [g0.real, g0.imag]]
        census[name]["(H_u, H_d)"] = list(pl)
    ranks = {STRUCTS[si][0]: K4(si) for si in live}
    log("K4 done")
    fits = {name: census[name]["fits (chi^2_min <= 5.99)"] for name, _ in STRUCTS}
    cells = {
        "K1: the E6 identity on all 200 cases (one c, 1e-10); the deformed control breaks it on all 200": k1_ok,
        "K2: R_G none at k = 1/2 mod 2, R_D none at k = 3/2 mod 2, n >= 2 at 9/2; control 2, 4, 5": k2_ok,
        "K3a: (D, D) fits": fits["(D, D)"],
        "K3b: (B, D) fits": fits["(B, D)"],
        "K3c: (D, B) does not fit": not fits["(D, B)"],
        "K4: every structure run has rank 13 at all three points": all(r[0] == 13 for v in ranks.values() for r in v)}
    out = {"status": "W56: the Higgs carrying the generation index (the rule first; one run)",
           "rho_T(S)^2 (the convention read before the rule)": [[str(complex(z)) for z in row]
                                                               for row in np.round(AS @ AS, 12)],
           "K1: the E6 identity": k1,
           "K2: dim M_k (R_G, R_D)": dims, "K2: the control T (x) T at k = 3, 5, 7": ctrl,
           "K2: n = dim M_9/2 (R_D)": n,
           "K3: the census (Standard Model frame, the geometry's weight)": census,
           "K4: rank and the 13th singular value over the largest, at three random points": ranks,
           "cells (as worded)": {k: bool(v) for k, v in cells.items()},
           "priors": {"K1": 0.90, "K2": 0.90, "K3a": 0.80, "K3b": 0.70, "K3c": 0.80, "K4": 0.90},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells (as worded)"], indent=1))


if __name__ == "__main__":
    main()
