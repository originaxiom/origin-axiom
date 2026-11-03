"""Parametric re-implementation harness around the agy seat's committed pipeline (dfe4c6f90).

Uses agy's own building blocks (sector_residues, closed_form_cA, _f10_st_and_scalar,
quaternionic_4d_yukawa, ckm_full_diagnostics) from the frozen snapshot so that every
number is the agy model's own number; what we vary is what agy held fixed by hand
(tau, the scalar-Higgs characters c_u, c_d, c_e, the line).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

SNAP = Path("/Users/dri/.gemini/antigravity/scratch/agy-snapshot-dfe4c6f90/src")
sys.path.insert(0, str(SNAP))

from origin_axiom.operator_gate import ckm_full_diagnostics, quaternionic_4d_yukawa  # noqa: E402
from origin_axiom.sm_19_gate import (  # noqa: E402
    C3_SHIFTED_TARGETS_10,
    SIGMA_LOG_10,
    _f10_st_and_scalar,
    sector_residues,
)
from origin_axiom.twisted_norms import closed_form_cA  # noqa: E402

GATE_SIX = 16.811893829770927
GATE_CKM = 15.086272469388987
GATE_TEN = 23.209251158954356
PHI = (1 + 5 ** 0.5) / 2
TAU_GOLDEN = complex(1 / 5 ** 0.5, PHI ** 2)
TAU_FIT_TREE = complex(0.44643117, 2.60792242)

L2_IM = [2.0, 2.25, 2.5, 2.75, 3.0]
L2_VAL = [2.4404154646430865, 2.406639297403933, 2.3796454106029277, 2.3577376878276057, 2.3397188997332714]

CU7 = -np.sqrt(np.exp(1j * math.pi) - 1.0)
CD7 = -np.sqrt(np.exp(1j * math.pi / 4.0) - 1.0)
CE7 = -1.0 + 0.0j


def l2_of(im_tau: float) -> float:
    return float(np.interp(im_tau, L2_IM, L2_VAL))


def matter(tau: complex, p1: float, p2: str, l2: float, n_terms=10, dps=15, n_pts=48):
    """Return dict sector -> (m1, m_perp) exactly as agy builds them."""
    p1s = {0.4: "2/5"}.get(round(p1, 6), None)
    c_vals = closed_form_cA(tau, p1s if p1s else str(p1), p2, n_terms=n_terms, dps=dps)
    out = {}
    for sn, ql, qr in [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]:
        res = sector_residues(p1, float(eval(p2)), tau, ql, qr, n_pts=n_pts)
        u = {
            k: (math.sqrt(2.0 * math.pi * l2 + float(c_vals[k])) * res[k] if abs(res[k]) > 1e-12 else 0.0j)
            for k in ("1", "i", "j", "k")
        }
        out[sn] = (u["1"], np.array([u["j"], u["i"], u["k"]], dtype=complex))
    return out


def observables(tau: complex, cu=CU7, cd=CD7, ce=CE7, mats=None, l2=None):
    if l2 is None:
        l2 = l2_of(tau.imag)
    if mats is None:
        mats = matter(tau, 0.4, "0", l2)
    h_st, b_st = _f10_st_and_scalar(tau)
    yu = quaternionic_4d_yukawa(cu * b_st, h_st, *mats["up"])
    yd = quaternionic_4d_yukawa(cd * b_st, h_st, *mats["down"])
    ye = quaternionic_4d_yukawa(ce * b_st, h_st, *mats["lepton"])
    diag = ckm_full_diagnostics(yu, yd)
    se = np.sort(np.linalg.svd(ye, compute_uv=False))
    raw = np.array(
        [
            diag["up_ratios"][1], diag["up_ratios"][0], diag["down_ratios"][1], diag["down_ratios"][0],
            se[1] / se[2], se[0] / se[2], diag["V_us"], diag["V_cb"], diag["V_ub"], diag["abs_J"],
        ],
        dtype=float,
    )
    return raw


def chi2(raw: np.ndarray, gamma=None, I=0.0):
    obs = raw.copy()
    if gamma is not None:
        obs = obs * np.exp(np.asarray(gamma) * I)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (np.log(obs) - np.log(C3_SHIFTED_TARGETS_10)) / SIGMA_LOG_10
    z = np.where(np.isfinite(z), z, 1e3)
    six = float(np.sum(z[:6] ** 2))
    ckm = float(np.sum(z[6:] ** 2))
    return six, ckm, six + ckm, z


def passes(six, ckm, ten):
    return six <= GATE_SIX and ckm <= GATE_CKM and ten <= GATE_TEN


if __name__ == "__main__":
    import time

    t = time.time()
    raw = observables(TAU_GOLDEN)
    print("golden", chi2(raw)[:3], time.time() - t)
    t = time.time()
    raw = observables(TAU_FIT_TREE)
    print("fit", chi2(raw)[:3], time.time() - t)
