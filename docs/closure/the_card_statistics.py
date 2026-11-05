#!/usr/bin/env python3
"""Reference implementations for the closure cards (main's asks 1 and 2(a) of 2026-11-05; the SM seat, relay section 352).
Data-free: everything here runs on planted matrices or synthetic null samples only. It never evaluates the frame and
never reads a measured target. Main implements its own and may use these as a second implementation.

  yb_over_yt(Y, triple)          -- the y_b/y_t extraction under N1-N6 (relay section 349, S1.1)
  r_labelled(Y_nu)               -- r with S2.1's labelling (the ordering read from the frame's own spectrum)
  joint_pv(d_obs, D_null)        -- the joint p_V of section 352 (Fisher product of leave-one-out marginal ranks,
                                    ties against the frame, the data counted in the null, Clopper-Pearson 97.5%)
  python3 -B the_card_statistics.py   -> the planted and calibration controls (deviations and rates only)
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import beta

ONE_HIGGS = ("St", "S", "S")          # (up, down, lepton) readings: S~ = "St"


class NotHeldOut(Exception):
    pass


def yb_over_yt(Y, triple):
    """Y: {sector: {reading: 3x3 complex}} from ONE instrument call at the frozen (tau, line, delta), sectors up and down.
    N1 one call, no constant applied; N2 one Higgs object (S~ = eps conj(S) eps^T); N3 up and down share Q;
    N4 H = I, no field weight; N5 the instrument's residues and weights unchanged; N6 sigma_max from the raw matrices."""
    if tuple(triple) != ONE_HIGGS:
        raise NotHeldOut("y_b/y_t is held out only in the one-Higgs triple (S~, S, S)")
    su = np.linalg.svd(np.asarray(Y["up"]["St"]), compute_uv=False)
    sd = np.linalg.svd(np.asarray(Y["down"]["S"]), compute_uv=False)
    if not (np.all(np.isfinite(su)) and np.all(np.isfinite(sd))) or su.max() <= 0:
        raise FloatingPointError("non-finite or null up matrix")
    return float(sd.max() / su.max())


def r_labelled(Y_nu):
    """S2.1: the pair with the smaller squared splitting is (1, 2), m2 > m1; the third state is 3. Returns (r, ordering)."""
    m = np.sort(np.linalg.svd(np.asarray(Y_nu), compute_uv=False))
    q = m ** 2
    if q[1] - q[0] <= q[2] - q[1]:                     # normal-like: the light pair is (1, 2)
        return float((q[1] - q[0]) / (q[2] - q[0])), "NO"
    return float((q[2] - q[1]) / (q[0] - q[1])), "IO"  # inverted-like: nu1, nu2 = the heavy pair, nu3 = the lightest


def _ranks_le(D):
    """for each column, the count of OTHER rows with D <= D_i (ties counted against the row)"""
    N = D.shape[0]
    out = np.empty_like(D, dtype=float)
    for j in range(D.shape[1]):
        col = D[:, j]
        srt = np.sort(col)
        out[:, j] = np.searchsorted(srt, col, side="right") - 1
    return out


def joint_pv(d_obs, D_null):
    """d_obs: the data's distances |x_t - v_t| (one per target); D_null: N x T null distances |X_t,w - v_t|.
    Marginal rank p_t = (1 + #{w: D_t,w <= d_t}) / (N + 1); null worlds use leave-one-out ranks.
    S = prod_t p_t; p_joint = (1 + #{w: S_w <= S_obs}) / (N + 1); returns (p_joint, its Clopper-Pearson 97.5% upper end,
    the marginal p's)."""
    d_obs = np.asarray(d_obs, float)
    D = np.asarray(D_null, float)
    N, T = D.shape
    p_obs = np.array([(1 + np.sum(D[:, t] <= d_obs[t])) / (N + 1) for t in range(T)])
    # a null world's marginal rank among the other N - 1 worlds plus the data
    pw = (1 + _ranks_le(D) + (d_obs[None, :] <= D)) / (N + 1)
    S_obs, S_w = float(np.prod(p_obs)), np.prod(pw, axis=1)
    k = int(np.sum(S_w <= S_obs))
    p = (1 + k) / (N + 1)
    upper = float(beta.ppf(0.975, k + 2, N - k)) if k < N else 1.0
    return p, upper, p_obs.tolist()


def _haar(n, rng):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def controls():
    rng = np.random.default_rng(352)
    out = {}
    # E1: the extraction on planted matrices
    worst, inv, cov = 0.0, 0.0, 0.0
    for _ in range(5000):
        a, b = np.sort(10 ** rng.uniform(-4, 0, 3)), np.sort(10 ** rng.uniform(-4, 0, 3))
        Yu = _haar(3, rng) @ np.diag(a) @ _haar(3, rng).conj().T
        Yd = _haar(3, rng) @ np.diag(b) @ _haar(3, rng).conj().T
        Y = {"up": {"St": Yu, "S": 0 * Yu}, "down": {"S": Yd, "St": 0 * Yd}}
        v = yb_over_yt(Y, ONE_HIGGS)
        worst = max(worst, abs(v / (b[-1] / a[-1]) - 1))
        Y2 = {"up": {"St": 4.1 * _haar(3, rng) @ Yu @ _haar(3, rng)}, "down": {"S": 4.1 * _haar(3, rng) @ Yd @ _haar(3, rng)}}
        inv = max(inv, abs(yb_over_yt(Y2, ONE_HIGGS) / v - 1))
        Y3 = {"up": {"St": 2.5 * Yu}, "down": {"S": Yd}}
        cov = max(cov, abs(yb_over_yt(Y3, ONE_HIGGS) * 2.5 / v - 1))
    guard = False
    try:
        yb_over_yt(Y, ("St", "St", "St"))
    except NotHeldOut:
        guard = True
    out["E1_planted"] = {"max_rel_dev": worst, "rotation_and_common_scale_invariance": inv,
                         "up_scale_covariance": cov, "two_doublet_triple_refused": guard,
                         "holds": bool(worst < 1e-12 and inv < 1e-12 and cov < 1e-12 and guard)}
    # E2: r's labelling on planted normal- and inverted-like spectra
    wno, wio, nok = 0.0, 0.0, True
    for _ in range(5000):
        m1, m2, m3 = np.sort(10 ** rng.uniform(-3, 0, 3))
        if (m2 ** 2 - m1 ** 2) <= (m3 ** 2 - m2 ** 2):
            r_true, o_true = (m2 ** 2 - m1 ** 2) / (m3 ** 2 - m1 ** 2), "NO"
        else:
            r_true, o_true = (m3 ** 2 - m2 ** 2) / (m1 ** 2 - m2 ** 2), "IO"
        r, o = r_labelled(_haar(3, rng) @ np.diag([m1, m2, m3]) @ _haar(3, rng).conj().T)
        nok &= (o == o_true)
        if o_true == "NO":
            wno = max(wno, abs(r / r_true - 1))
        else:
            wio = max(wio, abs(r / r_true - 1))
    out["E2_labelling"] = {"NO_max_rel_dev": wno, "IO_max_rel_dev": wio, "ordering_recovered": bool(nok),
                           "holds": bool(nok and wno < 1e-8 and wio < 1e-8)}
    # E3: calibration under exchangeability -- the data a null draw; the joint p must be uniform; the rectangle is not
    N, R = 2000, 4000
    for name, rho in (("independent", 0.0), ("correlated_0.8", 0.8)):
        ps, rect = [], []
        for _ in range(R):
            z = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], size=N + 1)
            D = np.abs(z)
            d_obs, Dn = D[0], D[1:]
            p, _, _ = joint_pv(d_obs, Dn)
            ps.append(p)
            rect.append((1 + np.sum(np.all(Dn <= d_obs, axis=1))) / (N + 1))
        ps, rect = np.array(ps), np.array(rect)
        out[f"E3_calibration_{name}"] = {
            "joint_rate_at_0.01": float(np.mean(ps <= 0.01)), "joint_rate_at_0.05": float(np.mean(ps <= 0.05)),
            "rectangle_rate_at_0.01": float(np.mean(rect <= 0.01)), "rectangle_rate_at_0.05": float(np.mean(rect <= 0.05)),
            "replicates": R, "N_null": N}
    here = Path(__file__).resolve().parent
    (here / "the_card_statistics_controls.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    controls()
