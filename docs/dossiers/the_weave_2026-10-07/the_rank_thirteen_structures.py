"""W54 (the rule: W54_RULE.md, committed before this script). Do the rank-13 structures fit at all? Every structure on
record not yet excluded (W52, W53): T (x) T with each k_s in {3, 5, 7} and (k_u, k_d) != (3, 3) (24), and Sym^2 T with
each k_s in {5, 7} (8). A sector's Yukawa is Y_s = sum_i alpha_{s,i} F^_i(tau) over W52's basis at its weight (F^ the
form over its Frobenius norm at tau, alpha_s complex). W53's data, observables and tolerance (a = 0.10).

  H0  the controls: (a) the dimensions (T (x) T at 3, 5, 7: 2, 4, 5; Sym^2 T at 5, 7: 3, 3); (b) the ten shape
      observables of T (x) T (5, 7, 5) at random alpha unchanged under tau -> tau + 1 and -1/tau at five points, to
      1e-8; (c) the 13 x P Jacobian of T (x) T (7, 5, 5) at a random point has rank 13.
  H1  the rank-one test: mu_k(tau) = m2/m3 at the minimum over alpha of the 2 x 2 minors of Y/|Y| (20 starts), at three
      random tau (seed 5401) in x in [-0.4, 0.4], y in [1.05, 2]: mu_7 < 1e-6, mu_5 > 1e-3 and mu_3 > 1e-3 at all three.
  H2  at least one of the 32 structures fits (chi^2_min <= 5.99 at a = 0.10).
  H3  T (x) T (7, 7, 3), (7, 7, 5) and (7, 7, 7) all fit.

  The search (fixed in the rule): a tau grid over the fundamental domain (x in 11 steps, y in 16 geometric steps over
  [0.87, 6], |tau| >= 1); at each grid tau the quark part Q for each quark weight pair (16 starts) and the lepton part
  E for each lepton weight (8 starts), seeds (5400, the pair's or weight's index, the grid index); each structure's
  grid values Q + E; a joint bounded refinement of tau and every alpha from each structure's 8 best grid points.

Run: python3 the_rank_thirteen_structures.py  ->  the_rank_thirteen_structures.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import least_squares  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402  (W53: the data, reduce, the conventions; W52's forms)

OUT = HERE / "the_rank_thirteen_structures.json"
A = FW.A_MAIN
WEIGHTS = {"T (x) T": (3, 5, 7), "Sym^2 T": (5, 7)}
DIMS = {fr: {k: len(FW.FORMS[fr][k]) for k in ks} for fr, ks in WEIGHTS.items()}
STRUCTURES = ([("T (x) T", ks) for ks in itertools.product((3, 5, 7), repeat=3) if ks[:2] != (3, 3)]
              + [("Sym^2 T", ks) for ks in itertools.product((5, 7), repeat=3)])
QPAIRS = [(fr, ku, kd) for fr, ks in WEIGHTS.items() for ku in ks for kd in ks if (fr, ku, kd) != ("T (x) T", 3, 3)]
EWEIGHTS = [(fr, k) for fr, ks in WEIGHTS.items() for k in ks]
NPROC = 4


def grid():
    pts = []
    for y in np.geomspace(0.87, FW.YMAX, 16):
        for x in np.linspace(-0.5, 0.5, 11):
            if abs(complex(x, y)) >= 1 - 1e-12:
                pts.append(complex(float(x), float(y)))
    return pts


GRID = grid()


# ------------------------------------------------------------------------------------------------------------ model
def forms_at(fr, k, tau):
    out = []
    for f in FW.FORMS[fr][k]:
        m = f(tau)
        out.append(m / np.linalg.norm(m))
    return np.array(out)


def coupling(p, F):
    d = F.shape[0]
    alpha = np.asarray(p[:d]) + 1j * np.asarray(p[d:2 * d])
    return np.tensordot(alpha, F, axes=1)


def sector(Y):
    U, sv, _ = np.linalg.svd(Y)
    idx = np.argsort(sv)
    return U[:, idx], np.log(np.maximum(sv[idx], 1e-300))


def mass_res(s, logs, a):
    sig = np.sqrt(FW.DELM[s] ** 2 + a ** 2)
    w = 1 / sig ** 2
    c = np.sum(w * (FW.LOGM[s] - logs)) / np.sum(w)
    return (logs + c - FW.LOGM[s]) / sig


def ckm_res(Uu, Ud, a):
    V = Uu.conj().T @ Ud
    vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in FW.CKM_KEYS], 1e-300))
    return (vlog - FW.LOGV) / np.sqrt(FW.DELV ** 2 + a ** 2)


def q_res(p, Fu, Fd, a=A):
    du = Fu.shape[0]
    Uu, lu = sector(coupling(p[:2 * du], Fu))
    Ud, ld = sector(coupling(p[2 * du:], Fd))
    return np.concatenate([mass_res("u", lu, a), mass_res("d", ld, a), ckm_res(Uu, Ud, a)])


def e_res(p, Fe, a=A):
    _, le = sector(coupling(p, Fe))
    return mass_res("e", le, a)


def split(fr, ks):
    d = [DIMS[fr][k] for k in ks]
    cuts = np.cumsum([2] + [2 * x for x in d])
    return d, cuts


def full_res(theta, fr, ks, a=A):
    tau = FW.reduce(complex(theta[0], theta[1]))
    cache = {k: forms_at(fr, k, tau) for k in set(ks)}
    _, cuts = split(fr, ks)
    Us, res = [], []
    for s, k, lo, hi in zip(FW.SECTORS, ks, cuts[:-1], cuts[1:]):
        U, logs = sector(coupling(theta[lo:hi], cache[k]))
        Us.append(U)
        res.append(mass_res(s, logs, a))
    res.append(ckm_res(Us[0], Us[1], a))
    return np.concatenate(res)


def shape10(tau, fr, ks, alphas):
    cache = {k: forms_at(fr, k, tau) for k in set(ks)}
    Us, out = [], []
    for k, p in zip(ks, alphas):
        U, logs = sector(coupling(p, cache[k]))
        Us.append(U)
        out += list(logs[:2] - logs[2])
    V = Us[0].conj().T @ Us[1]
    return np.array(out + list(np.log([abs(V[i, j]) for _, i, j in FW.CKM_KEYS])))


# --------------------------------------------------------------------------------------------------------------- H0
def H0():
    out = {}
    dims_ok = ([DIMS["T (x) T"][k] for k in (3, 5, 7)] == [2, 4, 5] and [DIMS["Sym^2 T"][k] for k in (5, 7)] == [3, 3])
    out["(a) the dimensions"] = {fr: {str(k): v for k, v in d.items()} for fr, d in DIMS.items()}
    rng = np.random.default_rng(5402)
    fr, ks = "T (x) T", (5, 7, 5)
    worst = 0.0
    for _ in range(5):
        tau = complex(rng.uniform(-0.25, 0.25), rng.uniform(1.0, 1.08))
        alphas = [rng.normal(size=2 * DIMS[fr][k]) for k in ks]
        base = shape10(tau, fr, ks, alphas)
        for t2 in (tau + 1, -1 / tau):
            worst = max(worst, float(np.max(np.abs(shape10(t2, fr, ks, alphas) - base))))
    out["(b) the shape observables at tau + 1 and -1/tau: the largest difference"] = worst
    ks = (7, 5, 5)

    def obs13(th):
        tau = complex(th[0], th[1])
        cache = {k: forms_at(fr, k, tau) for k in set(ks)}
        _, cuts = split(fr, ks)
        Us, logs = [], []
        for k, lo, hi in zip(ks, cuts[:-1], cuts[1:]):
            U, lg = sector(coupling(th[lo:hi], cache[k]))
            Us.append(U)
            logs += list(lg)
        V = Us[0].conj().T @ Us[1]
        return np.array(logs + list(np.log([abs(V[i, j]) for _, i, j in FW.CKM_KEYS])))

    _, cuts = split(fr, ks)
    th0 = np.array([rng.uniform(-0.4, 0.4), rng.uniform(1.05, 1.6)] + list(rng.normal(size=int(cuts[-1]) - 2)))
    J = np.zeros((13, len(th0)))
    for i in range(len(th0)):
        e = np.zeros(len(th0))
        e[i] = 1e-6
        J[:, i] = (obs13(th0 + e) - obs13(th0 - e)) / 2e-6
    s = np.linalg.svd(J, compute_uv=False)
    rank = int(sum(s > 1e-6 * s[0]))
    out["(c) the 13 x P Jacobian of T (x) T (7, 5, 5): rank, and its 13th singular value over the largest"] = [
        rank, float(s[12] / s[0])]
    ok = dims_ok and worst < 1e-8 and rank == 13
    return out, bool(ok)


# --------------------------------------------------------------------------------------------------------------- H1
def minors(p, F):
    Y = coupling(p, F)
    Y = Y / np.linalg.norm(Y)
    pairs = ((0, 1), (0, 2), (1, 2))
    m = [Y[i, k] * Y[j, l] - Y[i, l] * Y[j, k] for i, j in pairs for k, l in pairs]
    m = np.array(m)
    return np.concatenate([m.real, m.imag])


def H1():
    rng = np.random.default_rng(5401)
    taus = [complex(rng.uniform(-0.4, 0.4), rng.uniform(1.05, 2.0)) for _ in range(3)]
    out, mus = {}, {}
    for k in (3, 5, 7):
        row = []
        for i, tau in enumerate(taus):
            F = forms_at("T (x) T", k, tau)
            r2 = np.random.default_rng([5401, k, i])
            best = None
            for _ in range(20):
                q = least_squares(minors, r2.normal(size=2 * F.shape[0]), args=(F,), method="trf", xtol=1e-15,
                                  ftol=1e-15, gtol=1e-15, max_nfev=2000)
                c = float(np.linalg.norm(q.fun))
                if best is None or c < best[0]:
                    best = (c, q.x)
            sv = np.sort(np.linalg.svd(coupling(best[1], F), compute_uv=False))
            row.append({"tau": [tau.real, tau.imag], "the minors' norm at the minimum": best[0],
                        "mu = m2/m3 there": float(sv[1] / sv[2])})
        out[f"k = {k}"] = row
        mus[k] = [r["mu = m2/m3 there"] for r in row]
    ok = all(m < 1e-6 for m in mus[7]) and all(m > 1e-3 for m in mus[5]) and all(m > 1e-3 for m in mus[3])
    return out, bool(ok)


# ---------------------------------------------------------------------------------------------- stage 1: the grid
def stage1_point(g):
    tau = GRID[g]
    F = {(fr, k): forms_at(fr, k, tau) for fr, ks in WEIGHTS.items() for k in ks}
    out = {"Q": [], "E": []}
    for qi, (fr, ku, kd) in enumerate(QPAIRS):
        Fu, Fd = F[(fr, ku)], F[(fr, kd)]
        n = 2 * (Fu.shape[0] + Fd.shape[0])
        rng = np.random.default_rng([5400, qi, g])
        best = None
        for _ in range(16):
            r = least_squares(q_res, rng.normal(size=n), args=(Fu, Fd), method="trf", xtol=1e-10, ftol=1e-10,
                              gtol=1e-10, max_nfev=400)
            c = float(np.sum(r.fun ** 2))
            if best is None or c < best[0]:
                best = (c, [float(x) for x in r.x])
        out["Q"].append(best)
    for ei, (fr, k) in enumerate(EWEIGHTS):
        Fe = F[(fr, k)]
        rng = np.random.default_rng([5400, 100 + ei, g])
        best = None
        for _ in range(8):
            r = least_squares(e_res, rng.normal(size=2 * Fe.shape[0]), args=(Fe,), method="trf", xtol=1e-10,
                              ftol=1e-10, gtol=1e-10, max_nfev=400)
            c = float(np.sum(r.fun ** 2))
            if best is None or c < best[0]:
                best = (c, [float(x) for x in r.x])
        out["E"].append(best)
    return out


def grid_values(rows, si):
    fr, ks = STRUCTURES[si]
    qi = QPAIRS.index((fr, ks[0], ks[1]))
    ei = EWEIGHTS.index((fr, ks[2]))
    vals = []
    for g, row in enumerate(rows):
        (cq, pq), (ce, pe) = row["Q"][qi], row["E"][ei]
        tau = GRID[g]
        vals.append((cq + ce, [tau.real, tau.imag] + pq + pe))
    vals.sort(key=lambda t: t[0])
    return vals


# ----------------------------------------------------------------------------------------- stage 2: the refinement
def stage2_structure(args):
    si, starts = args
    fr, ks = STRUCTURES[si]
    n = len(starts[0])
    lb = [-0.5, FW.H0] + [-np.inf] * (n - 2)
    ub = [0.5, FW.YMAX] + [np.inf] * (n - 2)
    best = None
    for th in starts:
        x0 = np.array(th, dtype=float)
        x0[0] = min(max(x0[0], -0.5 + 1e-9), 0.5 - 1e-9)
        x0[1] = min(max(x0[1], FW.H0 + 1e-9), FW.YMAX - 1e-9)
        r = least_squares(full_res, x0, args=(fr, ks), bounds=(lb, ub), method="trf", xtol=1e-12, ftol=1e-12,
                          gtol=1e-12, max_nfev=1500)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, [float(x) for x in r.x])
    return best


def describe(si, theta, grid_best):
    fr, ks = STRUCTURES[si]
    res = full_res(np.array(theta), fr, ks)
    tau = FW.reduce(complex(theta[0], theta[1]))
    d, _ = split(fr, ks)
    P = 2 + sum(2 * x - 1 for x in d)
    chi = float(np.sum(res ** 2))
    return {"frame": fr, "weights (u, d, e)": list(ks), "P": P, "chi^2_min": chi, "fits": bool(chi <= FW.THRESH),
            "fits exactly": bool(chi <= 0.01), "tau (reduced)": [tau.real, tau.imag],
            "on the box's edge y = 6": bool(abs(theta[1] - FW.YMAX) < 1e-6), "the grid's best": grid_best,
            "pulls": {l: float(x) for l, x in zip(FW.LABELS, res)}}


def main():
    h0, ok0 = H0()
    FW.log(f"H0 done: {ok0}")
    h1, ok1 = H1()
    FW.log(f"H1 done: {ok1}")
    FW.log(f"stage 1 over {len(GRID)} grid points, {len(QPAIRS)} quark pairs, {len(EWEIGHTS)} lepton weights")
    rows = []
    with Pool(NPROC) as pool:
        for i, row in enumerate(pool.imap(stage1_point, range(len(GRID)))):
            rows.append(row)
            if i % 20 == 0:
                FW.log(f"stage 1: {i + 1} of {len(GRID)}")
        tasks = []
        bests = []
        for si in range(len(STRUCTURES)):
            vals = grid_values(rows, si)
            bests.append(vals[0][0])
            tasks.append((si, [v[1] for v in vals[:8]]))
        FW.log("stage 2: the joint refinements")
        refined = pool.map(stage2_structure, tasks, chunksize=1)
    structures = {}
    for si, (c, th) in enumerate(refined):
        fr, ks = STRUCTURES[si]
        if bests[si] < c:                       # the grid's own point is better: keep it
            th = grid_values(rows, si)[0][1]
        structures[f"{fr}: {tuple(ks)}"] = describe(si, th, bests[si])
    parts = {"Q, the quark pairs' best grid values": {
        f"{fr}: ({ku}, {kd})": min(r["Q"][qi][0] for r in rows) for qi, (fr, ku, kd) in enumerate(QPAIRS)},
        "E, the lepton weights' best grid values": {
        f"{fr}: {k}": min(r["E"][ei][0] for r in rows) for ei, (fr, k) in enumerate(EWEIGHTS)}}
    fitting = [k for k, v in structures.items() if v["fits"]]
    h3 = all(structures[f"T (x) T: (7, 7, {k})"]["fits"] for k in (3, 5, 7))
    cells = {"H0: the controls": ok0,
             "H1: the rank-one test (mu_7 < 1e-6; mu_5, mu_3 > 1e-3 at three random tau)": ok1,
             "H2: at least one of the 32 structures fits (chi^2_min <= 5.99)": bool(fitting),
             "H3: T (x) T (7, 7, 3), (7, 7, 5) and (7, 7, 7) all fit": bool(h3)}
    priors = {"H0": 0.95, "H1": 0.65, "H2": 0.85, "H3": 0.70}
    out = {"status": "W54: do the rank-13 structures fit at all? (the rule first; one run)",
           "H0": h0, "H1: the span's closest approach to rank one": h1,
           "the structures (global minimum found)": structures,
           "the structures that fit": fitting,
           "the parts on the grid": parts,
           "cells (as worded)": {k: bool(v) for k, v in cells.items()}, "priors": priors,
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells (as worded)"], indent=1))
    print("fitting:", fitting)


if __name__ == "__main__":
    main()
