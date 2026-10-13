"""W57 (the rule: W57_RULE.md, committed with its data before this script). The field of maximality: is the world a
typical draw from the seed's own measure, against anarchy?

  The seed's measure (S_mix): W56's four placements at the geometry's weight, (H_u, H_d) in {(B, B), (B, D), (D, B),
  (D, D)}, each with weight 1/4; tau from the hyperbolic measure on the whole fundamental domain (exact sampler); at
  each tau the invariant complex Gaussian on the coupling span the seed allows there (B: W53's two forms at k = 3; D:
  R_D's eight forms at 9/2 with a Gaussian direction h, d and e sharing h_d). Anarchy: independent complex Gaussian
  3 x 3 Yukawas.

  Ten shape numbers (log m1/m3, log m2/m3 by sector; log |V_us|, |V_cb|, |V_ub|, |V_td|), logs floored at log 1e-16;
  the tolerance sigma_i = sqrt(delta_i^2 + a^2), a = 0.10; d(x, t) = max_i |x_i - t_i| / sigma_i.
  T1  R = A_S(eps*) / A_A(eps*) >= 10, eps* the smallest rung of {2, 4, 8, 16, 32, 64} where S_mix accepts >= 20
      draws around the data at M_Z (A_A -> 3/N if anarchy accepts none).
  T2  p < 0.05: p = (1 + #{pseudo-data whose count within eps* <= the data's}) / 201, 200 pseudo-data from S_mix.
  T3  every two-sided marginal p of the ten data under S_mix >= 0.01 (F with one count added at each end).
  T4  anarchy's two-sided marginal p for log(m_u/m_t) < 0.001.
  Read-outs (no prior): each placement; the data at 1e12 GeV; the observer-conditioned version (every sector's
  m1/m3 < 1e-2).

Run: python3 the_field_of_maximality.py  ->  the_field_of_maximality.json beside it.
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_higgs_and_the_generation_index as HG  # noqa: E402  (W56: R_D's forms at 9/2, rho_T)

FW = HG.FW                                    # W53: the data, the conventions, the k = 3 forms
PG = FW.PG
WF = HG.WF
OUT = HERE / "the_field_of_maximality.json"
A_TOL = 0.10
LADDER = (2, 4, 8, 16, 32, 64)
N_PER = 250_000
N_ANARCHY = 1_000_000
N_PSEUDO = 200
BATCH = 5000
FLOOR = np.log(1e-16)
PLACEMENTS = [("B", "B"), ("B", "D"), ("D", "B"), ("D", "D")]
NPROC = 4
LABELS = ["log m_u/m_t", "log m_c/m_t", "log m_d/m_b", "log m_s/m_b", "log m_e/m_tau", "log m_mu/m_tau",
          "log |V_us|", "log |V_cb|", "log |V_ub|", "log |V_td|"]
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", flush=True)


# ------------------------------------------------------------------------------------------------------- the forms
def b_pieces():
    """W53's two k = 3 forms (O+ then O-), with a vectorised evaluator: tau array -> (N, 2, 9)"""
    rS9, rT9 = np.kron(HG.CA, HG.CA), np.kron(HG.CT, HG.CT)
    pcs = PG.pieces()
    out = []
    for name in ("O+", "O-"):
        Bp = pcs[name]
        rS, rT = Bp.conj().T @ rS9 @ Bp, Bp.conj().T @ rT9 @ Bp
        null, Z, evv, _ = WF.forms_vec(rS, rT, 3)
        assert null == 1
        out.append((Bp, Z[:, 0], evv))
    return out


BP = b_pieces()


def forms_B(t):
    return np.stack([(Bp @ evv(c, t)).T for Bp, c, evv in BP], axis=1)          # (N, 2, 9)


def forms_D(t):
    return np.stack([HG.EV_D(HG.Z_D[:, a], t).T for a in range(HG.ND)], axis=1)  # (N, 8, 27)


# ------------------------------------------------------------------------------------------------------ the draws
def gauss(rng, shape):
    return (rng.normal(size=shape) + 1j * rng.normal(size=shape)) / np.sqrt(2)


def sample_tau(rng, n):
    th = rng.uniform(-np.pi / 6, np.pi / 6, size=n)
    u = 1.0 - rng.random(size=n)                                                    # (0, 1]
    return np.sin(th) + 1j * np.cos(th) / u


def degenerate(R):
    """draws deep enough in the cusp that a form underflows: the span's R has a diagonal below 1e-200 of its largest"""
    d = np.abs(np.diagonal(R, axis1=1, axis2=2))
    return d.min(axis=1) <= 1e-200 * d.max(axis=1)


def yukawa_B(F, rng):
    Q, R = np.linalg.qr(np.transpose(F, (0, 2, 1)))                                   # (N, 9, 2)
    return np.einsum("nab,nb->na", Q, gauss(rng, (F.shape[0], 2))).reshape(-1, 3, 3), degenerate(R)


def yukawa_D(F, h, rng):
    Q, R = np.linalg.qr(np.transpose(F, (0, 2, 1)))                                   # (N, 27, 8)
    W = np.einsum("nab,nb->na", Q, gauss(rng, (F.shape[0], F.shape[1]))).reshape(-1, 3, 3, 3)
    return np.einsum("nijk,nk->nij", W, h), degenerate(R)


def shapes(Yu, Yd, Ye):
    """the ten shape numbers, (N, 10)"""
    cols, Us = [], []
    for Y in (Yu, Yd, Ye):
        U, s, _ = np.linalg.svd(Y)
        idx = np.argsort(s, axis=1)
        s = np.take_along_axis(s, idx, axis=1)
        U = np.take_along_axis(U, idx[:, None, :], axis=2)
        Us.append(U)
        with np.errstate(divide="ignore", invalid="ignore"):
            cols.append(np.fmax(np.log(s[:, 0] / s[:, 2]), FLOOR))
            cols.append(np.fmax(np.log(s[:, 1] / s[:, 2]), FLOOR))
    V = np.einsum("nji,njk->nik", Us[0].conj(), Us[1])
    for _, i, j in FW.CKM_KEYS:
        with np.errstate(divide="ignore", invalid="ignore"):
            cols.append(np.fmax(np.log(np.abs(V[:, i, j])), FLOOR))
    return np.stack(cols, axis=1)


def seed_batch(args):
    pi, b, n = args
    hu, hd = PLACEMENTS[pi]
    rng = np.random.default_rng([5700, pi, b])
    t = sample_tau(rng, n)
    FB = forms_B(t) if "B" in (hu, hd) else None
    FD = forms_D(t) if "D" in (hu, hd) else None
    hu_v = gauss(rng, (n, 3)) if hu == "D" else None
    hd_v = gauss(rng, (n, 3)) if hd == "D" else None
    Yu, gu = yukawa_B(FB, rng) if hu == "B" else yukawa_D(FD, hu_v, rng)
    Yd, gd = yukawa_B(FB, rng) if hd == "B" else yukawa_D(FD, hd_v, rng)
    Ye, ge = yukawa_B(FB, rng) if hd == "B" else yukawa_D(FD, hd_v, rng)
    X = shapes(Yu, Yd, Ye)
    X[gu | gd | ge] = FLOOR                         # the rule's floor: hierarchies far below 1e-16
    return pi, X, t.imag


def anarchy_batch(args):
    b, n = args
    rng = np.random.default_rng([5701, b])
    return shapes(gauss(rng, (n, 3, 3)), gauss(rng, (n, 3, 3)), gauss(rng, (n, 3, 3)))


def pseudo_draws(key, placements, n):
    """n draws from a uniform mixture of the given placements, an independent stream"""
    rng = np.random.default_rng(key)
    which = rng.integers(len(placements), size=n)
    out = np.zeros((n, 10))
    for k, pi in enumerate(placements):
        sel = np.where(which == k)[0]
        if len(sel):
            _, X, _ = seed_batch((pi, 10_000 + int(rng.integers(1 << 30)), len(sel)))
            out[sel] = X
    return out


# ---------------------------------------------------------------------------------------------------- the targets
def target(mass_file):
    m = json.loads((HERE / "received" / mass_file).read_text(encoding="utf-8"))["masses_GeV"]
    b = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))["ckm_abs"]
    v, s = m["value"], m["sigma"]
    t, d = [], []
    for light, mid, heavy in (("u", "c", "t"), ("d", "s", "b"), ("e", "mu", "tau")):
        for x in (light, mid):
            t.append(np.log(v[x] / v[heavy]))
            d.append(np.hypot(s[x] / v[x], s[heavy] / v[heavy]))
    for _, i, j in FW.CKM_KEYS:
        t.append(np.log(b["value"][i][j]))
        d.append(b["sigma"][i][j] / b["value"][i][j])
    return np.array(t), np.sqrt(np.array(d) ** 2 + A_TOL ** 2)


def dist(X, t, sig):
    return np.max(np.abs(X - t) / sig, axis=1)


def analyse(S, A, t, sig, pseudo):
    """T1-T3 for a seed sample S against anarchy A at target t"""
    dS, dA = dist(S, t, sig), dist(A, t, sig)
    ladder = {str(e): [int(np.sum(dS <= e)), int(np.sum(dA <= e))] for e in LADDER}
    eps = next((e for e in LADDER if ladder[str(e)][0] >= 20), None)
    out = {"accepted on the ladder (seed, anarchy)": ladder, "eps*": eps}
    if eps is not None:
        aS = ladder[str(eps)][0] / len(S)
        nA = ladder[str(eps)][1]
        aA = nA / len(A) if nA else 3.0 / len(A)
        out["T1: R = A_S / A_A at eps*"] = aS / aA
        out["T1: anarchy accepted none (A_A set to 3/N)"] = bool(nA == 0)
        count = int(np.sum(dS <= eps))
        counts = [int(np.sum(dist(S, x, sig) <= eps)) for x in pseudo]
        out["T2: the data's count, and the pseudo-data's counts (min, median, max)"] = [
            count, [int(min(counts)), float(np.median(counts)), int(max(counts))]]
        out["T2: p"] = (1 + sum(c <= count for c in counts)) / (len(pseudo) + 1)
    F = (np.sum(S <= t, axis=0) + 1) / (len(S) + 2)
    out["T3: two-sided marginal p of each datum"] = {lab: float(2 * min(f, 1 - f)) for lab, f in zip(LABELS, F)}
    return out


def main():
    log(f"R_D's forms: {HG.ND}; the seed's draws ({len(PLACEMENTS)} x {N_PER}) and anarchy's ({N_ANARCHY})")
    tasks = [(pi, b, BATCH) for pi in range(len(PLACEMENTS)) for b in range(N_PER // BATCH)]
    with Pool(NPROC) as pool:
        rows = pool.map(seed_batch, tasks, chunksize=1)
        arows = pool.map(anarchy_batch, [(b, BATCH) for b in range(N_ANARCHY // BATCH)], chunksize=4)
    by = {pi: np.concatenate([X for p2, X, _ in rows if p2 == pi]) for pi in range(len(PLACEMENTS))}
    ys = np.concatenate([y for _, _, y in rows])
    S = np.concatenate([by[pi] for pi in range(len(PLACEMENTS))])
    A = np.concatenate(arows)
    log("draws done")

    # controls (construction checks, not cells)
    t3 = np.array([0.13 + 1.21j, -0.31 + 1.7j, 0.45 + 3.2j])
    fb = forms_B(t3)
    ok_b = all(np.allclose(fb[n, 0], FW.FP_RAW(t3[n]).ravel(), atol=1e-10)
               and np.allclose(fb[n, 1], FW.FM_RAW(t3[n]).ravel(), atol=1e-10) for n in range(3))
    frac6 = float(np.mean(ys > 6))
    vus2 = float(np.mean(np.exp(2 * A[:, 6])))
    floored = float(np.mean(np.all(S == FLOOR, axis=1)))
    controls = {"(a) the vectorised k = 3 forms equal W53's": bool(ok_b),
                "(b) the fraction of tau with y > 6, and the measure's 3/(6 pi)": [frac6, 3 / (6 * np.pi)],
                "(c) anarchy's mean |V_us|^2, and Haar's 1/3": [vus2, 1 / 3],
                "(d) the fraction of seed draws set to the floor (a form underflowed in the cusp)": floored}
    log(f"controls: {controls}")

    tZ, sZ = target("HZ2021_running_masses_MZ.json")
    t12, s12 = target("HZ2021_running_masses_1e12.json")
    pseudo = pseudo_draws([5702, 99], list(range(len(PLACEMENTS))), N_PSEUDO)
    main_res = analyse(S, A, tZ, sZ, pseudo)
    log(f"main: eps* = {main_res['eps*']}")
    FA = (np.sum(A[:, 0] <= tZ[0]) + 1) / (len(A) + 2)
    t4 = float(2 * min(FA, 1 - FA))

    per = {}
    for pi, pl in enumerate(PLACEMENTS):
        ps = pseudo_draws([5702, pi], [pi], N_PSEUDO)
        per[str(pl)] = analyse(by[pi], A, tZ, sZ, ps)
    robust = analyse(S, A, t12, s12, pseudo)

    cond = lambda X: np.all(X[:, [0, 2, 4]] < np.log(1e-2), axis=1)  # noqa: E731
    Sc, Ac = S[cond(S)], A[cond(A)]
    rng = np.random.default_rng(5703)
    pc = []
    while len(pc) < N_PSEUDO:
        cand = pseudo_draws([5703, int(rng.integers(1 << 30))], list(range(len(PLACEMENTS))), 2000)
        pc.extend(list(cand[cond(cand)]))
    pc = np.array(pc[:N_PSEUDO])
    conditioned = {"kept (seed, anarchy)": [int(len(Sc)), int(len(Ac))]}
    if len(Ac):
        conditioned.update(analyse(Sc, Ac, tZ, sZ, pc))
    else:
        conditioned["anarchy keeps no draw"] = True
    log("read-outs done")

    eps = main_res["eps*"]
    marg = main_res["T3: two-sided marginal p of each datum"]
    cells = {
        "T1: R >= 10 at eps*": bool(eps is not None and main_res["T1: R = A_S / A_A at eps*"] >= 10),
        "T2: p < 0.05 (the data are not a typical draw from S_mix)": bool(eps is not None and main_res["T2: p"] < 0.05),
        "T3: every two-sided marginal p >= 0.01 under S_mix": bool(all(v >= 0.01 for v in marg.values())),
        "T4: anarchy's two-sided marginal p for log(m_u/m_t) < 0.001": bool(t4 < 0.001)}
    out = {"status": "W57: the field of maximality (the rule first; one run)",
           "the draws": {"seed, per placement": N_PER, "anarchy": N_ANARCHY, "pseudo-data": N_PSEUDO,
                         "R_D's forms": HG.ND},
           "the data at M_Z: target and sigma": [list(map(float, tZ)), list(map(float, sZ))],
           "the data at 1e12 GeV: target and sigma": [list(map(float, t12)), list(map(float, s12))],
           "controls": controls,
           "main (S_mix against anarchy, the data at M_Z)": main_res,
           "T4: anarchy's two-sided marginal p for log(m_u/m_t)": t4,
           "read-out: each placement": per,
           "read-out: the data at 1e12 GeV": robust,
           "read-out: observer-conditioned (every m1/m3 < 1e-2; labelled; cannot rescue T2)": conditioned,
           "cells (as worded)": cells,
           "priors": {"T1": 0.85, "T2": 0.70, "T3": 0.60, "T4": 0.95},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(cells, indent=1))


if __name__ == "__main__":
    main()
