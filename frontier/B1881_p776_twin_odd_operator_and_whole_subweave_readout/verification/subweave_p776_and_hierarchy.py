#!/usr/bin/env python3
"""B1881: P-776 Whole-Subweave Twin-Odd Hyperbolic Laplacian Read-Out, R10-A/B/C Operators,
and Data-Free FR-FIB Structural Hierarchy & CP Test.

Sealed before execution in Commit A (pinned in ARTIFACT_HASHES.txt alongside PREREGISTRATION.md).
Strictly data-free (0 of 19): zero Standard Model measured values, zero chi2 scores, and zero
D11 / P-709 held-out targets are imported, read, or compared.

Importing this module executes nothing and writes nothing.
Run once in Commit B:
    PYTHONDONTWRITEBYTECODE=1 python3 -B frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/verification/subweave_p776_and_hierarchy.py --write
"""

from __future__ import annotations

import os

for _env_var in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_env_var, "1")

import argparse
from collections import deque
import contextlib
from fractions import Fraction as Fr
import importlib.util
import io
import json
import math
import pathlib
import sys
import time
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
import scipy.optimize as sp_opt
import scipy.special as sp_spec
from scipy.special import zeta as hurwitz_zeta

HERE = pathlib.Path(__file__).resolve().parent
ARC_DIR = HERE.parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT_JSON = HERE / "subweave_p776_and_hierarchy.json"

HEJHAL_SL2Z_R1_ODD = 9.533695261353557554
HEJHAL_SL2Z_R1_EVEN = 13.779751351890738644
PHI_GOLDEN = 0.5 * (1.0 + math.sqrt(5.0))
RM_Q_SQRT5_R1_ODD = math.pi / (2.0 * math.log(PHI_GOLDEN))
RM_Q_SQRT5_R1_EVEN = math.pi / math.log(PHI_GOLDEN)

# =============================================================================
# Lazy Instrument Loader (B1667 Canonical Cusp + B1726 / B1723 / B1691 FR-FIB)
# =============================================================================

_INSTRUMENTS: Dict[str, Any] = {}


def load_main_instruments() -> Dict[str, Any]:
    """Loads main's unmodified B1667 canonical-cusp module and B1726 FR-FIB evaluator without side effects."""
    if not _INSTRUMENTS:
        p1726 = ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"
        if str(p1726) not in sys.path:
            sys.path.insert(0, str(p1726))
        import census as K  # type: ignore

        mods = K._modules()
        spec_c = importlib.util.spec_from_file_location(
            "b1667_cusp",
            ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py",
        )
        assert spec_c is not None and spec_c.loader is not None
        C = importlib.util.module_from_spec(spec_c)
        with contextlib.redirect_stdout(io.StringIO()):
            spec_c.loader.exec_module(C)

        cusp_json = json.loads(
            (ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(
                encoding="utf-8"
            )
        )
        _INSTRUMENTS.update(K=K, B=mods["B"], te=mods["te"], col=mods["col"], C=C, cusp_json=cusp_json)
    return _INSTRUMENTS


def min_c_extended(C: Any, Ra: np.ndarray, Rb: np.ndarray, max_power: int = 28) -> float:
    """Computes min |c_gamma| combining B1667's depth-8 word tree with parabolic-collar words Ra^k Rb^{+-1} Ra^m."""
    best = float(C.min_c(Ra, Rb, 8))
    ra_inv = np.linalg.inv(Ra)
    rb_inv = np.linalg.inv(Rb)
    ra_pows = [np.eye(2, dtype=complex)]
    ra_neg = [np.eye(2, dtype=complex)]
    for _ in range(max_power):
        ra_pows.append(ra_pows[-1] @ Ra)
        ra_neg.append(ra_neg[-1] @ ra_inv)
    all_a = ra_pows + ra_neg[1:]
    for ma in all_a:
        c_val = abs(ma[1, 0])
        if c_val > 1e-9 * max(1.0, abs(ma[0, 0])):
            best = min(best, float(c_val))
    for k in range(-12, 13):
        mk = ra_pows[k] if k >= 0 else ra_neg[-k]
        for mid in (Rb, rb_inv):
            m_left = mk @ mid
            for m in range(-12, 13):
                mm = ra_pows[m] if m >= 0 else ra_neg[-m]
                prod = m_left @ mm
                c_val = abs(prod[1, 0])
                if c_val > 1e-9 * max(1.0, abs(prod[0, 0])):
                    best = min(best, float(c_val))
    return best


def exact_cusp_geometry(C: Any, tau: complex, c_acc: complex) -> Dict[str, Any]:
    """Evaluates B1667's exact canonical-cusp radii (L_max, L_2) at (tau, c_acc) without table clamping."""
    lat, z0, Aa, Ab = C.monodromy(tau, c_acc)
    P0 = C.mobius_of(C.puncture_loop(lat, c_acc, z0, 0.05))
    g, Ra, Rb, _RP, lam = C.normalise(Aa, Ab, P0)
    lam_abs = abs(float(np.real(lam)))
    mc = min_c_extended(C, Ra, Rb, max_power=28)
    al, be = C.frobenius(lat, c_acc)
    ib_05 = float(C.local_B(lat, c_acc, z0, g, lam_abs, al, be, 0.05))
    L_max = (2.0 * math.pi / lam_abs) * (1.0 / mc - ib_05)
    L_2 = math.pi - (2.0 * math.pi / lam_abs) * ib_05
    return {
        "L_max": float(L_max),
        "L_2": float(L_2),
        "cusp_area": float(lam_abs * mc),
        "lam": float(lam_abs),
        "min_c": float(mc),
    }


def solve_cusp_radii_for_tau(tau_target: complex) -> Dict[str, Any]:
    """Tracks B1667's uniformising accessory parameter c(tau) off symmetric loci and returns exact (L_max, L_2)."""
    inst = load_main_instruments()
    C = inst["C"]
    cusp_pts = inst["cusp_json"]["points"]
    tgt = complex(tau_target)

    if tgt.imag <= 2.2:
        c_init = C.track(tgt, start=(1j, 0.0), step=0.04)
        c_sol, res = C.solve_accessory(tgt, c_init)
    else:
        # Start from B1667's committed off-symmetric grid point (0.25, 3.0), walk vertically along Re=0.25, then horizontally
        ref_pt = min(
            (p for p in cusp_pts if p["where"] == "grid" and abs(p["tau"][0] - 0.25) < 1e-9 and abs(p["tau"][1] - 3.0) < 1e-9),
            key=lambda p: abs(p["tau"][1] - 3.0),
        )
        cur_tau = complex(ref_pt["tau"][0], ref_pt["tau"][1])
        c_cur = complex(ref_pt["c"][0], ref_pt["c"][1])
        c_cur, _ = C.solve_accessory(cur_tau, c_cur)
        waypoints = [complex(0.25, tgt.imag), tgt]
        for wpnt in waypoints:
            step = 0.25 if abs(wpnt.real - cur_tau.real) < 1e-12 else 0.04
            n_steps = max(1, int(math.ceil(abs(wpnt - cur_tau) / step)))
            for k in range(1, n_steps + 1):
                tk = cur_tau + (wpnt - cur_tau) * (k / float(n_steps))
                c_cur, res_k = C.solve_accessory(tk, c_cur)
                if float(np.max(np.abs(res_k))) > 1e-9:
                    raise RuntimeError(f"Accessory continuation lost at tau={tk}: residual={np.max(np.abs(res_k)):.2e}")
            cur_tau = wpnt
        c_sol, res = C.solve_accessory(tgt, c_cur)

    res_norm = float(np.max(np.abs(res)))
    if res_norm > 1e-9:
        raise RuntimeError(f"Accessory solve failed at tau={tgt}: residual={res_norm:.2e}")
    geom = exact_cusp_geometry(C, tgt, c_sol)
    geom["c_accessory"] = [float(c_sol.real), float(c_sol.imag)]
    geom["accessory_residual"] = res_norm
    return geom

# =============================================================================
# SL_2(Z) Reduction & Non-Cancelling K_{iR}(u) Evaluator (Guardrail 4 Verified)
# =============================================================================


def reduce_to_sl2z_fundamental_domain(tau_in: complex) -> Tuple[complex, Tuple[int, int, int, int]]:
    """Pulls tau_in (Im > 0) into F_{SL_2(Z)} = {|Re z| <= 1/2, |z| >= 1} with exact integer matrix
    gamma = (A, B, C, D) in SL_2(Z) such that tau_red = (A * tau_in + B) / (C * tau_in + D)."""
    z = complex(tau_in)
    a_m, b_m, c_m, d_m = 1, 0, 0, 1
    for _ in range(200):
        n_sh = int(round(z.real))
        if n_sh != 0:
            z -= n_sh
            a_m -= n_sh * c_m
            b_m -= n_sh * d_m
        if (z.real * z.real + z.imag * z.imag) >= 1.0 - 1e-13:
            break
        z = -1.0 / z
        a_m, b_m, c_m, d_m = -c_m, -d_m, a_m, b_m
    n_sh = int(round(z.real))
    if n_sh != 0:
        z -= n_sh
        a_m -= n_sh * c_m
        b_m -= n_sh * d_m
    if z.real < -0.5 + 1e-12:
        z += 1.0
        a_m += c_m
        b_m += d_m
    assert a_m * d_m - b_m * c_m == 1
    return z, (a_m, b_m, c_m, d_m)


def besselk_ir_vec(r_val: float, u_arr: np.ndarray) -> np.ndarray:
    """Evaluates real Macdonald function K_{iR}(u) (R > 0, u > 0) to ~5e-16 scaled precision in float64."""
    shape = np.shape(u_arr)
    u = np.asarray(u_arr, dtype=np.float64).ravel()
    out = np.empty_like(u)
    m1 = u <= 4.0
    if np.any(m1):
        u1 = u[m1]
        ks = np.arange(46, dtype=np.float64)
        lg = sp_spec.loggamma(1.0 + 1j * r_val)
        c0 = np.exp(0.5 * np.pi * r_val - lg)
        cs = np.empty(46, dtype=np.complex128)
        cs[0] = c0
        for k in range(1, 46):
            cs[k] = cs[k - 1] / (k * (k + 1j * r_val))
        half_u = 0.5 * u1
        pows = (half_u[:, None] ** 2) ** ks[None, :]
        series = (pows @ cs) * np.exp(1j * r_val * np.log(half_u))
        pref = -2.0 * np.pi * np.exp(-1.5 * np.pi * r_val) / (1.0 - np.exp(-2.0 * np.pi * r_val))
        out[m1] = pref * np.imag(series)
    m2 = ~m1
    if np.any(m2):
        u2 = u[m2]
        m2_zero = u2 > (r_val * 0.0 + 55.0)
        if np.any(m2_zero):
            out_m2 = np.zeros_like(u2)
            idx_act = ~m2_zero
            if np.any(idx_act):
                ua = u2[idx_act]
                alpha = np.minimum(np.arctan2(r_val, ua), 1.30)
                ca, sa = np.cos(alpha), np.sin(alpha)
                si = np.arccosh(1.0 + 42.0 / np.maximum(ua * ca, 0.5))
                xi = np.linspace(-1.0, 1.0, 280)[None, :]
                s_grid = si[:, None] * xi
                ds = (2.0 * si) / 279.0
                amp = np.exp(-r_val * alpha[:, None] - (ua * ca)[:, None] * np.cosh(s_grid))
                phase = -(ua * sa)[:, None] * np.sinh(s_grid) + r_val * s_grid
                out_m2[idx_act] = 0.5 * ds * np.sum(amp * np.cos(phase), axis=1)
            out[m2] = out_m2
        else:
            alpha = np.minimum(np.arctan2(r_val, u2), 1.30)
            ca, sa = np.cos(alpha), np.sin(alpha)
            si = np.arccosh(1.0 + 42.0 / np.maximum(u2 * ca, 0.5))
            xi = np.linspace(-1.0, 1.0, 280)[None, :]
            s_grid = si[:, None] * xi
            ds = (2.0 * si) / 279.0
            amp = np.exp(-r_val * alpha[:, None] - (u2 * ca)[:, None] * np.cosh(s_grid))
            phase = -(u2 * sa)[:, None] * np.sinh(s_grid) + r_val * s_grid
            out[m2] = 0.5 * ds * np.sum(amp * np.cos(phase), axis=1)
    return out.reshape(shape)


def _pullback_sl2z_xy(x: float, y: float) -> Tuple[float, float]:
    for _ in range(100):
        x -= round(x)
        r2 = x * x + y * y
        if r2 >= 1.0 - 1e-15:
            break
        x, y = -x / r2, y / r2
    return x, y


def solve_sl2z_maass_benchmark(
    r_lo: float, r_hi: float, parity: int, m_trunc: int = 15, y1: float = 0.45, y2: float = 0.39
) -> Tuple[float, float, np.ndarray]:
    """Guardrail 4 benchmark solver on SL_2(Z) (N = 1) reproducing Hejhal (1983) to < 1e-12."""
    q_pts = 2 * m_trunc + 50
    xj = (np.arange(q_pts, dtype=np.float64) + 0.5) / (2.0 * q_pts)
    pb1 = np.array([_pullback_sl2z_xy(float(x), y1) for x in xj], dtype=np.float64)
    pb2 = np.array([_pullback_sl2z_xy(float(x), y2) for x in xj], dtype=np.float64)
    ns = np.arange(1, m_trunc + 1, dtype=np.float64)

    def horo_mat(r_v: float, y_v: float, pb: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        sc = math.exp(0.5 * math.pi * r_v)
        kh = besselk_ir_vec(r_v, 2.0 * np.pi * ns * y_v) * sc * math.sqrt(y_v)
        kp = besselk_ir_vec(r_v, 2.0 * np.pi * pb[:, 1:2] * ns[None, :]) * sc * np.sqrt(pb[:, 1:2])
        if parity == -1:
            tp = np.sin(2.0 * np.pi * pb[:, 0:1] * ns[None, :])
            tj = (2.0 / q_pts) * np.sin(2.0 * np.pi * ns[:, None] * xj[None, :])
        else:
            tp = np.cos(2.0 * np.pi * pb[:, 0:1] * ns[None, :])
            tj = (2.0 / q_pts) * np.cos(2.0 * np.pi * ns[:, None] * xj[None, :])
        return np.diag(kh) - tj @ (kp * tp), kh

    def signed_res(r_v: float) -> float:
        a1, kh1 = horo_mat(r_v, y1, pb1)
        a_rest = np.linalg.solve(a1[1:, 1:] / kh1[1:, None], -a1[1:, 0] / kh1[1:])
        a_vec = np.concatenate([[1.0], a_rest])
        return float((a1[0, :] @ a_vec) / kh1[0])

    grid = np.linspace(r_lo, r_hi, 60)
    gvals = [signed_res(float(r)) for r in grid]
    cands: List[Tuple[float, float, np.ndarray]] = []
    for k in range(len(grid) - 1):
        if gvals[k] * gvals[k + 1] <= 0.0:
            rc = float(sp_opt.brentq(signed_res, float(grid[k]), float(grid[k + 1]), xtol=1e-15, rtol=1e-15))
            a1, kh1 = horo_mat(rc, y1, pb1)
            a_rest = np.linalg.solve(a1[1:, 1:] / kh1[1:, None], -a1[1:, 0] / kh1[1:])
            a_vec = np.concatenate([[1.0], a_rest])
            a2, kh2 = horo_mat(rc, y2, pb2)
            y2_err = float(np.linalg.norm((a2[:8, :] @ a_vec) / kh2[:8]))
            cands.append((y2_err, rc, a_vec))
    cands.sort(key=lambda t: t[0])
    return cands[0][1], cands[0][0], cands[0][2]

def random_haar_su3_u1(rng: np.random.Generator) -> np.ndarray:
    """Generates a random 3x3 Haar unitary matrix in U(3) via QR decomposition with positive R-diagonal."""
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    ph = diag / np.abs(diag)
    return q @ np.diag(ph)


def build_fr_fib_yukawas(tau: complex, a_line: Fr, b_line: Fr, Ls: Dict[str, float]) -> Dict[Tuple[str, str, str], np.ndarray]:
    """Constructs raw 3x3 complex FR-FIB Yukawa matrices Y[(sec, h, rn)] directly from B1656/B1691."""
    inst = load_main_instruments()
    B = inst["B"]
    te = inst["te"]
    K = inst["K"]

    t = complex(tau)
    w = float(a_line) * t + float(b_line)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}

    yukawas: Dict[Tuple[str, str, str], np.ndarray] = {}
    for sec, (lf, rf) in K.SECT.items():
        x_tw, y_tw = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])
        R = B.residues(x_tw, y_tw, t)
        c_reg = B.cA(x_tw, y_tw, t, R)
        for h_name in ("L_max", "L_2"):
            L_val = Ls[h_name]
            u_weights = {
                s: (
                    math.sqrt(2.0 * math.pi * L_val + c_reg[s]) * R[s]
                    if c_reg[s] is not None and 2.0 * math.pi * L_val + c_reg[s] > 0.0
                    else 0.0
                )
                for s in B.UNITS
            }
            Mw = B.weighted_M(u_weights)
            for rn in ("S", "St"):
                yukawas[(sec, h_name, rn)] = B.coupling(readings[rn], Mw)
    return yukawas


def extract_physical_invariants_from_yukawas(
    Yu: np.ndarray, Yd: np.ndarray, Ye: np.ndarray
) -> Dict[str, Any]:
    """Extracts physical singular-value ratios, CKM moduli |V_ij|, and Jarlskog J (ascending mass ordering)."""
    Uu_desc, sv_u, _ = np.linalg.svd(Yu)
    Ud_desc, sv_d, _ = np.linalg.svd(Yd)
    _, sv_e, _ = np.linalg.svd(Ye)

    Uu = Uu_desc[:, ::-1]
    Ud = Ud_desc[:, ::-1]
    V_ckm = np.conj(Uu.T) @ Ud
    J_val = float(np.imag(V_ckm[0, 1] * V_ckm[1, 2] * np.conj(V_ckm[0, 2]) * np.conj(V_ckm[1, 1])))

    return {
        "ratios_up": [float(sv_u[1] / sv_u[0]), float(sv_u[2] / sv_u[0])],
        "ratios_down": [float(sv_d[1] / sv_d[0]), float(sv_d[2] / sv_d[0])],
        "ratios_lep": [float(sv_e[1] / sv_e[0]), float(sv_e[2] / sv_e[0])],
        "sv_up": [float(x) for x in sv_u],
        "sv_down": [float(x) for x in sv_d],
        "sv_lep": [float(x) for x in sv_e],
        "ckm_abs_vus_vcb_vub": [float(abs(V_ckm[0, 1])), float(abs(V_ckm[1, 2])), float(abs(V_ckm[0, 2]))],
        "ckm_abs_vtd": float(abs(V_ckm[2, 0])),
        "J": J_val,
        "abs_J": abs(J_val),
    }

def run_cell_c0_controls() -> Dict[str, Any]:
    """Runs halting Cell C0: Guardrail-4 SL_2(Z) Hejhal benchmark, B1667 control, T & S covariance, and Haar scrambling."""
    inst = load_main_instruments()
    K = inst["K"]
    cusp_pts = inst["cusp_json"]["points"]

    # 1. Guardrail 4 Literature Benchmark Gate on SL_2(Z) (N = 1)
    r_odd, y2_odd, a_odd = solve_sl2z_maass_benchmark(9.2, 9.8, parity=-1)
    r_even, y2_even, a_even = solve_sl2z_maass_benchmark(13.5, 14.0, parity=+1)
    hejhal_odd_err = abs(r_odd - HEJHAL_SL2Z_R1_ODD)
    hejhal_even_err = abs(r_even - HEJHAL_SL2Z_R1_EVEN)
    sl2z_hecke_err = max(
        abs(float(a_odd[1] * a_odd[2] - a_odd[5])),
        abs(float(a_odd[1] ** 2 - a_odd[3] - 1.0)),
        abs(float(a_even[1] * a_even[2] - a_even[5])),
        abs(float(a_even[1] ** 2 - a_even[3] - 1.0)),
    )

    # 2. B1667 canonical-cusp control at 0.25 + 3.0i
    ctl_tau = complex(0.25, 3.0)
    ref_pt = min(
        (p for p in cusp_pts if p["where"] == "grid" and abs(complex(*p["tau"]) - ctl_tau) < 1e-9),
        key=lambda p: abs(complex(*p["tau"]) - ctl_tau),
    )
    geom_ctl = solve_cusp_radii_for_tau(ctl_tau)
    cusp_rel_dev = max(
        abs(geom_ctl["L_max"] / float(ref_pt["L_max"]) - 1.0),
        abs(geom_ctl["L_2"] / float(ref_pt["L_2"]) - 1.0),
    )

    # 3. Modular T-covariance and exact B1667+B1724 S-covariance
    a_test, b_test = Fr(2, 5), Fr(1, 10)
    out_a = K.compute(0.35, 2.75, a_test, b_test)
    out_b = K.compute(1.35, 2.75, a_test, b_test - a_test)
    t_cov_max_diff = max(
        max(abs(float(xa) - float(xb)) for xa, xb in zip(out_a[key], out_b[key])) for key in out_a
    )

    tau_s_probe = complex(0.35, 1.35)
    tau_s_img = -1.0 / tau_s_probe
    g_s0 = solve_cusp_radii_for_tau(tau_s_probe)
    g_s1 = solve_cusp_radii_for_tau(tau_s_img)
    out_s0 = K.compute(
        tau_s_probe.real, tau_s_probe.imag, a_test, b_test, Ls={"L_max": g_s0["L_max"], "L_2": g_s0["L_2"]}
    )
    out_s1 = K.compute(
        tau_s_img.real, tau_s_img.imag, (-b_test) % 1, a_test % 1, Ls={"L_max": g_s1["L_max"], "L_2": g_s1["L_2"]}
    )
    cov_keys = [
        k for k in out_s0
        if (not k.startswith("ckm") and k.endswith(("|S", "|St")))
        or (k.startswith("ckm|") and all(p in ("S", "St") for p in k.split("|")[2:]))
    ]
    s_cov_max_diff = max(
        max(abs(float(xa) - float(xb)) for xa, xb in zip(out_s0[k], out_s1[k])) for k in cov_keys
    )

    # 4. Direct Yukawa builder vs K.compute + 8-draw Haar unitary basis-scrambling (Guardrail 3)
    Ls_probe = {"L_max": geom_ctl["L_max"], "L_2": geom_ctl["L_2"]}
    yuks = build_fr_fib_yukawas(complex(0.35, 2.75), a_test, b_test, Ls_probe)
    k_ref = K.compute(0.35, 2.75, a_test, b_test, Ls=Ls_probe)
    inv_base = extract_physical_invariants_from_yukawas(
        yuks[("up", "L_max", "St")],
        yuks[("down", "L_max", "S")],
        yuks[("lep", "L_max", "S")],
    )
    census_consistency_err = max(
        max(abs(a - b) for a, b in zip(inv_base["ratios_up"], k_ref["up|L_max|St"])),
        max(abs(a - b) for a, b in zip(inv_base["ratios_down"], k_ref["down|L_max|S"])),
        max(abs(a - b) for a, b in zip(inv_base["ratios_lep"], k_ref["lep|L_max|S"])),
        max(abs(a - b) for a, b in zip(inv_base["ckm_abs_vus_vcb_vub"], k_ref["ckm|L_max|St|S"][:3])),
        abs(inv_base["J"] - float(k_ref["ckm|L_max|St|S"][3])),
    )

    rng = np.random.default_rng(20261111)
    Yu0 = yuks[("up", "L_max", "St")]
    Yd0 = yuks[("down", "L_max", "S")]
    Ye0 = yuks[("lep", "L_max", "S")]
    haar_max_err = 0.0
    for _ in range(8):
        UL_Q = random_haar_su3_u1(rng)
        UR_u = random_haar_su3_u1(rng)
        UR_d = random_haar_su3_u1(rng)
        UL_L = random_haar_su3_u1(rng)
        UR_e = random_haar_su3_u1(rng)
        inv_scr = extract_physical_invariants_from_yukawas(
            UL_Q @ Yu0 @ np.conj(UR_u.T),
            UL_Q @ Yd0 @ np.conj(UR_d.T),
            UL_L @ Ye0 @ np.conj(UR_e.T),
        )
        for k_vec in ("ratios_up", "ratios_down", "ratios_lep", "ckm_abs_vus_vcb_vub"):
            for x0, x1 in zip(inv_base[k_vec], inv_scr[k_vec]):
                haar_max_err = max(haar_max_err, abs(x0 - x1))
        haar_max_err = max(
            haar_max_err,
            abs(inv_base["ckm_abs_vtd"] - inv_scr["ckm_abs_vtd"]),
            abs(inv_base["J"] - inv_scr["J"]),
        )

    holds = (
        (hejhal_odd_err < 1e-11)
        and (hejhal_even_err < 1e-11)
        and (sl2z_hecke_err < 1e-11)
        and (cusp_rel_dev < 1e-6)
        and (t_cov_max_diff < 1e-12)
        and (s_cov_max_diff < 1e-11)
        and (census_consistency_err < 1e-12)
        and (haar_max_err < 1e-12)
    )
    return {
        "holds": holds,
        "sl2z_hejhal_benchmark": {
            "R1_odd_computed": r_odd,
            "R1_odd_abs_err": hejhal_odd_err,
            "R1_odd_y2_err": y2_odd,
            "R1_even_computed": r_even,
            "R1_even_abs_err": hejhal_even_err,
            "R1_even_y2_err": y2_even,
            "sl2z_hecke_max_err": sl2z_hecke_err,
        },
        "cusp_control_tau": [0.25, 3.0],
        "cusp_L_max_L_2": [geom_ctl["L_max"], geom_ctl["L_2"]],
        "cusp_rel_dev_vs_B1667_json": cusp_rel_dev,
        "t_covariance_max_abs_diff": t_cov_max_diff,
        "s_covariance_max_abs_diff": s_cov_max_diff,
        "direct_yukawa_vs_B1726_census_err": census_consistency_err,
        "haar_basis_scrambling_8draws_max_err": haar_max_err,
    }

# =============================================================================
# Cell C1: Infinite-PSL(2,Z) Schreier Closure & Galois Fixed-Data Triviality
# =============================================================================


def build_marked_lines(n_level: int) -> List[Tuple[int, int]]:
    """Canonical representatives (a, b) of +-v for primitive order-N vectors in (Z/NZ)^2."""
    reps = set()
    for a in range(n_level):
        for b in range(n_level):
            if math.gcd(math.gcd(a, b), n_level) == 1:
                neg = ((-a) % n_level, (-b) % n_level)
                reps.add(min((a, b), neg))
    return sorted(reps)


def build_eigenlines(n_level: int) -> List[Tuple[int, int]]:
    """Canonical representatives of cyclic order-N subgroups <v> in (Z/NZ)^2 (P^1(Z/NZ))."""
    units = [u for u in range(1, n_level) if math.gcd(u, n_level) == 1]
    reps = set()
    for a in range(n_level):
        for b in range(n_level):
            if math.gcd(math.gcd(a, b), n_level) == 1:
                orbit = [((u * a) % n_level, (u * b) % n_level) for u in units]
                reps.add(min(orbit))
    return sorted(reps)


def act_marked_line(mat: Tuple[int, int, int, int], line: Tuple[int, int], n_level: int) -> Tuple[int, int]:
    a, b, c, d = mat
    x, y = line
    nx = (a * x + b * y) % n_level
    ny = (c * x + d * y) % n_level
    neg = ((-nx) % n_level, (-ny) % n_level)
    return min((nx, ny), neg)


def act_eigenline(mat: Tuple[int, int, int, int], line: Tuple[int, int], n_level: int) -> Tuple[int, int]:
    a, b, c, d = mat
    x, y = line
    nx = (a * x + b * y) % n_level
    ny = (c * x + d * y) % n_level
    units = [u for u in range(1, n_level) if math.gcd(u, n_level) == 1]
    return min(((u * nx) % n_level, (u * ny) % n_level) for u in units)


def _psl_key(m: np.ndarray) -> Tuple[int, int, int, int]:
    t1 = (int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1]))
    t2 = (-t1[0], -t1[1], -t1[2], -t1[3])
    return min(t1, t2)


def _mat_inv_sl2(m: np.ndarray) -> np.ndarray:
    return np.array([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]], dtype=np.int64)


def run_cell_c1_schreier_and_galois() -> Dict[str, Any]:
    """Runs Cell C1: constructive Schreier factorization in infinite PSL(2,Z) and Galois closure across N=2..7."""
    Ls = np.array([[1, 0], [1, 1]], dtype=np.int64)
    Rs = np.array([[1, 1], [0, 1]], dtype=np.int64)
    LR = Ls @ Rs
    w1 = np.linalg.matrix_power(Ls, 6) @ Rs @ LR
    w2 = np.linalg.matrix_power(Ls, 6) @ Rs @ LR @ LR
    w3 = Ls @ np.linalg.matrix_power(Rs, 6) @ LR
    w4 = Ls @ np.linalg.matrix_power(Rs, 6) @ LR @ LR

    lr_inv = _mat_inv_sl2(LR)
    defects_ok = all(
        np.array_equal((w @ np.linalg.matrix_power(lr_inv, k)) % 5, np.eye(2, dtype=np.int64))
        for w, k in ((w1, 2), (w2, 3), (w3, 2), (w4, 3))
    )

    S_mat = np.array([[0, -1], [1, 0]], dtype=np.int64)
    T_mat = Rs.copy()
    T_inv = _mat_inv_sl2(T_mat)
    base_mark = (1, 3)

    transversal: Dict[Tuple[int, int], np.ndarray] = {base_mark: np.eye(2, dtype=np.int64)}
    q_cos = deque([base_mark])
    while q_cos:
        mk = q_cos.popleft()
        rep = transversal[mk]
        for gen in (S_mat, T_mat, T_inv):
            prod = gen @ rep
            tup = (int(prod[0, 0]), int(prod[0, 1]), int(prod[1, 0]), int(prod[1, 1]))
            nxt_mk = act_marked_line(tup, base_mark, 5)
            if nxt_mk not in transversal:
                transversal[nxt_mk] = prod
                q_cos.append(nxt_mk)

    schreier_gens: Dict[Tuple[int, int, int, int], np.ndarray] = {}
    id_key = _psl_key(np.eye(2, dtype=np.int64))
    for _mk, rep in transversal.items():
        for gen in (S_mat, T_mat):
            prod = gen @ rep
            tup = (int(prod[0, 0]), int(prod[0, 1]), int(prod[1, 0]), int(prod[1, 1]))
            nxt_mk = act_marked_line(tup, base_mark, 5)
            sch = _mat_inv_sl2(transversal[nxt_mk]) @ prod
            k_sch = _psl_key(sch)
            if k_sch != id_key:
                schreier_gens[k_sch] = sch

    g1 = _mat_inv_sl2(w1) @ w2
    g2 = w2 @ _mat_inv_sl2(w1) @ _mat_inv_sl2(w1)
    g3 = (w3 @ _mat_inv_sl2(w1)) @ g2
    sub_gens = [
        w1, _mat_inv_sl2(w1),
        w2, _mat_inv_sl2(w2),
        w3, _mat_inv_sl2(w3),
        w4, _mat_inv_sl2(w4),
        g1, _mat_inv_sl2(g1),
        g2, _mat_inv_sl2(g2),
        g3, _mat_inv_sl2(g3),
    ]

    remaining = set(schreier_gens.keys())
    visited = {id_key}
    bfs_q = deque([(np.eye(2, dtype=np.int64), 0)])
    max_depth = 0
    while bfs_q and remaining:
        cur_m, d = bfs_q.popleft()
        if d >= 7:
            continue
        for sg in sub_gens:
            nxt_m = cur_m @ sg
            if int(np.max(np.abs(nxt_m))) > 50000:
                continue
            nk = _psl_key(nxt_m)
            if nk not in visited:
                visited.add(nk)
                if nk in remaining:
                    remaining.remove(nk)
                    max_depth = max(max_depth, d + 1)
                bfs_q.append((nxt_m, d + 1))

    galois_rows: List[Dict[str, Any]] = []
    for n_lv in range(2, 8):
        s_g = (0, (-1) % n_lv, 1 % n_lv, 0)
        t_g = (1 % n_lv, 1 % n_lv, 0, 1 % n_lv)

        def psl_mod_key(g: Tuple[int, int, int, int], n_mod: int = n_lv) -> Tuple[int, int, int, int]:
            neg = ((-g[0]) % n_mod, (-g[1]) % n_mod, (-g[2]) % n_mod, (-g[3]) % n_mod)
            return min(g, neg)

        id_g = psl_mod_key((1 % n_lv, 0, 0, 1 % n_lv))
        psl_elts = {id_g}
        q_g = deque([id_g])
        while q_g:
            a, b, c, d = q_g.popleft()
            for ga, gb, gc, gd in (s_g, t_g):
                nxt = psl_mod_key(
                    (
                        (a * ga + b * gc) % n_lv,
                        (a * gb + b * gd) % n_lv,
                        (c * ga + d * gc) % n_lv,
                        (c * gb + d * gd) % n_lv,
                    )
                )
                if nxt not in psl_elts:
                    psl_elts.add(nxt)
                    q_g.append(nxt)

        omega1 = build_marked_lines(n_lv)
        omega0 = build_eigenlines(n_lv)
        d_mark = (0, 1)
        stab1 = [g for g in psl_elts if act_marked_line(g, d_mark, n_lv) == d_mark]
        fix1 = [m for m in omega1 if all(act_marked_line(g, m, n_lv) == m for g in stab1)]
        stab1_of_fix1 = [g for g in psl_elts if all(act_marked_line(g, m, n_lv) == m for m in fix1)]
        fix1_twice = [m for m in omega1 if all(act_marked_line(g, m, n_lv) == m for g in stab1_of_fix1)]
        stab0 = [g for g in psl_elts if act_eigenline(g, d_mark, n_lv) == d_mark]
        fix0 = [e for e in omega0 if all(act_eigenline(g, e, n_lv) == e for g in stab0)]

        galois_rows.append(
            {
                "N": n_lv,
                "psl2_mod_N_order": len(psl_elts),
                "omega1_size": len(omega1),
                "omega0_size": len(omega0),
                "fix_stab_omega1": [list(x) for x in fix1],
                "extra_marked_lines_outside_eigenline": [list(m) for m in fix1 if m[0] % n_lv != 0],
                "idempotent_cl_cl_eq_cl": fix1_twice == fix1,
                "fix_stab_omega0_size": len(fix0),
            }
        )

    holds = (
        (len(transversal) == 12)
        and defects_ok
        and (len(remaining) == 0)
        and all(r["idempotent_cl_cl_eq_cl"] for r in galois_rows)
    )
    return {
        "holds": holds,
        "index_in_psl2z": len(transversal),
        "defects_strictly_plus_I_mod5": defects_ok,
        "schreier_generator_count": len(schreier_gens),
        "unfactored_schreier_generators": len(remaining),
        "max_word_depth": max_depth,
        "galois_closure_N2_to_7": galois_rows,
    }


# =============================================================================
# Cell C2: R10-A Coset-Coupled Mayer-Selberg Spectrum Across N = 2..11
# =============================================================================


def _chebyshev_basis_matrix(xs: np.ndarray, k_nodes: int) -> np.ndarray:
    u = 2.0 * xs - 1.0
    v_mat = np.zeros((len(xs), k_nodes), dtype=np.float64)
    v_mat[:, 0] = 1.0
    if k_nodes > 1:
        v_mat[:, 1] = u
    for k in range(2, k_nodes):
        v_mat[:, k] = 2.0 * u * v_mat[:, k - 1] - v_mat[:, k - 2]
    return v_mat


def _chebyshev_u_monomial_coeffs(k_nodes: int) -> np.ndarray:
    coeffs = np.zeros((k_nodes, k_nodes), dtype=np.float64)
    coeffs[0, 0] = 1.0
    if k_nodes > 1:
        coeffs[1, 0] = -1.0
        coeffs[1, 1] = 2.0
    for k in range(2, k_nodes):
        coeffs[k, :] = -2.0 * coeffs[k - 1, :] - coeffs[k - 2, :]
        coeffs[k, 1:] += 4.0 * coeffs[k - 1, :-1]
    return coeffs


def build_coset_gauss_and_mayer_operators(
    n_level: int,
    mode: str = "X1",
    s_param: float = 1.0,
    k_nodes: int = 16,
    q_direct_blocks: int = 40,
) -> Tuple[np.ndarray, np.ndarray, List[Tuple[int, int]]]:
    cosets = build_marked_lines(n_level) if mode == "X1" else build_eigenlines(n_level)
    act_fn = act_marked_line if mode == "X1" else act_eigenline
    d_cos = len(cosets)
    cos_to_idx = {c: i for i, c in enumerate(cosets)}

    idx_k = np.arange(k_nodes, dtype=np.float64)
    xs = 0.5 * (1.0 + np.cos(np.pi * (2.0 * idx_k + 1.0) / (2.0 * k_nodes)))
    v_nodes = _chebyshev_basis_matrix(xs, k_nodes)
    v_inv = np.linalg.inv(v_nodes)
    c_mono = _chebyshev_u_monomial_coeffs(k_nodes)

    j_arr = np.arange(k_nodes, dtype=np.float64)
    residue_blocks: List[np.ndarray] = []
    for r in range(1, n_level + 1):
        ns = (np.arange(q_direct_blocks, dtype=np.float64) * n_level + r)[:, None]
        den = ns + xs[None, :]
        u_vals = 1.0 / den
        weights = den ** (-2.0 * s_param)
        t_eval = _chebyshev_basis_matrix(u_vals.ravel(), k_nodes).reshape(q_direct_blocks, k_nodes, k_nodes)
        modal_direct = np.einsum("qi,qik->ik", weights, t_eval)

        a_shift = q_direct_blocks + (r + xs) / float(n_level)
        s_vec = (2.0 * s_param + j_arr)[None, :]
        zeta_mat = (float(n_level) ** (-s_vec)) * hurwitz_zeta(s_vec, a_shift[:, None])
        modal_tail = zeta_mat @ c_mono.T
        residue_blocks.append((modal_direct + modal_tail) @ v_inv)

    g_full = np.zeros((k_nodes * d_cos, k_nodes * d_cos), dtype=np.float64)
    for r_idx, r in enumerate(range(1, n_level + 1)):
        gn_mat = (0, 1 % n_level, 1 % n_level, r % n_level)
        b_r = residue_blocks[r_idx]
        for c_i, c_val in enumerate(cosets):
            target_c = act_fn(gn_mat, c_val, n_level)
            c_j = cos_to_idx[target_c]
            g_full[c_i * k_nodes : (c_i + 1) * k_nodes, c_j * k_nodes : (c_j + 1) * k_nodes] += b_r

    return g_full, g_full @ g_full, cosets

def run_cell_c2_mayer_selberg(levels: Tuple[int, ...] = tuple(range(2, 12))) -> Dict[str, Any]:
    """Runs Cell C2: R10-A Mayer-Selberg non-trivial subweave spectrum across N = 2..11."""
    k_nodes = 16
    rows: List[Dict[str, Any]] = []
    for n_lv in levels:
        entry: Dict[str, Any] = {"N": n_lv}
        for mode in ("X1", "X0"):
            g_op, m_op, cosets = build_coset_gauss_and_mayer_operators(n_lv, mode=mode, s_param=1.0, k_nodes=k_nodes)
            d_cos = len(cosets)
            ones = np.ones((d_cos, 1), dtype=np.float64) / math.sqrt(d_cos)
            q_mat, _ = np.linalg.qr(np.hstack([ones, np.eye(d_cos, d_cos - 1)]), mode="complete")
            p_triv = np.kron(ones, np.eye(k_nodes))
            p_sub = np.kron(q_mat[:, 1:], np.eye(k_nodes))

            m_triv = p_triv.T @ m_op @ p_triv
            m_sub = p_sub.T @ m_op @ p_sub
            g_sub = p_sub.T @ g_op @ p_sub

            ev_triv = np.sort(np.abs(np.linalg.eigvals(m_triv)))[::-1]
            ev_sub = np.sort(np.abs(np.linalg.eigvals(m_sub)))[::-1]
            ev_g_sub = np.sort(np.abs(np.linalg.eigvals(g_sub)))[::-1]
            fredholm_det_sub = float(np.linalg.det(np.eye(m_sub.shape[0]) - m_sub))

            entry[mode] = {
                "index_d": d_cos,
                "trivial_lambda1": float(ev_triv[0]),
                "trivial_lambda2_wirsing_sq": float(ev_triv[1]),
                "subweave_gauss_spectral_radius": float(ev_g_sub[0]),
                "subweave_mayer_spectral_radius": float(ev_sub[0]),
                "subweave_fredholm_det_at_s1": fredholm_det_sub,
            }
        rows.append(entry)

    by_n = {r["N"]: r for r in rows}
    rho_5 = by_n[5]["X1"]["subweave_mayer_spectral_radius"]
    rho_10 = by_n[10]["X1"]["subweave_mayer_spectral_radius"]
    det_5 = by_n[5]["X1"]["subweave_fredholm_det_at_s1"]
    oldspace_tie_err = abs(rho_5 - rho_10)
    n5_10_beat_rest = all(
        rho_5 > by_n[n]["X1"]["subweave_mayer_spectral_radius"] + 1e-3 for n in levels if n not in (5, 10)
    )
    n5_minimizes_det = all(det_5 < by_n[n]["X1"]["subweave_fredholm_det_at_s1"] - 1e-9 for n in levels if n != 5)

    return {
        "holds": (oldspace_tie_err < 1e-12) and n5_10_beat_rest and n5_minimizes_det,
        "oldspace_tie_rho5_minus_rho10_abs": oldspace_tie_err,
        "n5_and_n10_beat_all_other_levels": n5_10_beat_rest,
        "n5_strictly_minimizes_fredholm_det_N2_to_11": n5_minimizes_det,
        "levels": rows,
    }

# =============================================================================
# Cell C3: R10-B & R10-C1/C2 Ray-Singer Analytic Torsion on X_0(N) and X_1(N)
# =============================================================================


def _eta_mp(tau: mp.mpc, n_terms: int = 65) -> mp.mpc:
    q2 = mp.exp(2j * mp.pi * tau)
    prod = mp.mpc(1, 0)
    qn = q2
    for _ in range(n_terms):
        prod *= 1 - qn
        qn *= q2
    return mp.exp(1j * mp.pi * tau / 12) * prod


def _e2_hat_mp(tau: mp.mpc, n_terms: int = 65) -> mp.mpc:
    q2 = mp.exp(2j * mp.pi * tau)
    acc = mp.mpc(0, 0)
    qn = q2
    for n in range(1, n_terms + 1):
        acc += n * qn / (1 - qn)
        qn *= q2
    return (1 - 24 * acc) - 3 / (mp.pi * mp.im(tau))


def siegel_unit_abs_mp(r1: int, r2: int, n_level: int, tau: mp.mpc, n_terms: int = 55) -> mp.mpf:
    t = mp.mpc(tau)
    a1_int = r1 % n_level
    a1 = mp.mpf(a1_int) / mp.mpf(n_level)
    a2 = mp.mpf(r2 % n_level) / mp.mpf(n_level)
    b2 = a1 * a1 - a1 + mp.mpf(1) / 6
    q = mp.exp(2j * mp.pi * t)
    z = mp.exp(2j * mp.pi * a2)

    prod = mp.mpc(1, 0)
    if a1_int == 0:
        prod *= 1 - z
        qm = q
        for _ in range(1, n_terms + 1):
            prod *= (1 - qm * z) * (1 - qm / z)
            qm *= q
    else:
        qm = mp.mpc(1, 0)
        qa = mp.exp(2j * mp.pi * a1 * t)
        qb = mp.exp(2j * mp.pi * (1 - a1) * t)
        for _ in range(0, n_terms + 1):
            prod *= (1 - qm * qa * z) * (1 - qm * qb / z)
            qm *= q

    pref = mp.exp(2j * mp.pi * t * (mp.mpf("0.5") * b2)) * mp.exp(1j * mp.pi * a2 * (a1 - 1))
    return abs(pref * prod)


def v_x1_sheet_kappa_mp(tau0: mp.mpc, r1: int, r2: int, n_level: int, kappa: int = 1, n_terms: int = 45) -> mp.mpf:
    """Zero-parameter Ray-Singer torsion potential: kappa=1 is O (+) L_{1/N}; kappa=2 is O (+) L_{1/N} (+) L_{-1/N}."""
    t = mp.mpc(tau0)
    et = _eta_mp(t, n_terms=n_terms)
    su = siegel_unit_abs_mp(r1, r2, n_level, t, n_terms=n_terms)
    return -mp.log(mp.im(t) * (abs(et) ** 4) * (su ** (2 * kappa)))


def x1_sheet_stationarity_eq_kappa(
    tau0: mp.mpc, r1: int, r2: int, n_level: int, kappa: int = 1, n_terms: int = 45
) -> mp.mpc:
    """Exact holomorphic stationarity equation (1/12)*hat{E}_2(tau0) + (kappa/(2*pi*i))*(g'/g)(tau0) == 0."""
    t = mp.mpc(tau0)
    a1_int = r1 % n_level
    a1 = mp.mpf(a1_int) / mp.mpf(n_level)
    a2 = mp.mpf(r2 % n_level) / mp.mpf(n_level)
    b2 = a1 * a1 - a1 + mp.mpf(1) / 6
    z = mp.exp(2j * mp.pi * a2)

    log_deriv = mp.mpc("0.5") * b2
    m_start = 1 if a1_int == 0 else 0
    for m in range(m_start, n_terms + 1):
        ma = mp.mpf(m) + a1
        w = mp.exp(2j * mp.pi * ma * t) * z
        log_deriv -= ma * w / (1 - w)
    for m in range(0, n_terms + 1):
        mb = mp.mpf(m + 1) - a1
        w = mp.exp(2j * mp.pi * mb * t) / z
        log_deriv -= mb * w / (1 - w)

    return _e2_hat_mp(t, n_terms=n_terms) / 12 + kappa * log_deriv


def _canonicalize_tau_and_sheet(
    t_star: mp.mpc, r1: int, r2: int, n_level: int
) -> Tuple[mp.mpc, Tuple[int, int]]:
    """Wraps Re(tau) into [-0.5, 0.5] via T^m and chooses the CP-canonical Re(tau) >= 0 mirror hand."""
    m_int = int(mp.nint(mp.re(t_star)))
    t_red = t_star - m_int
    # g_{(r1/N, r2/N)}(t_red + m) == g_{(r1/N, (r2 + m*r1)/N)}(t_red)
    nr1 = r1 % n_level
    nr2 = (r2 + m_int * r1) % n_level
    sheet = min((nr1, nr2), ((-nr1) % n_level, (-nr2) % n_level))
    if abs(abs(mp.re(t_red)) - mp.mpf("0.5")) < mp.mpf("1e-24"):
        t_red = mp.mpc(mp.mpf("0.5"), mp.im(t_red))
        # Ensure sheet matches +0.5 if -0.5 was shifted by +1
        if mp.re(t_star - m_int) < 0:
            nr2_p = (nr2 - nr1) % n_level
            sheet = min((nr1, nr2_p), ((-nr1) % n_level, (-nr2_p) % n_level))
    elif mp.re(t_red) < -mp.mpf("1e-24"):
        # Reflect across Re(tau) = 0: (-bar(tau), (r1, -r2 mod N)) has identical V
        t_red = mp.mpc(-mp.re(t_red), mp.im(t_red))
        sheet = min((sheet[0], (-sheet[1]) % n_level), ((-sheet[0]) % n_level, sheet[1] % n_level))
    return t_red, sheet


def run_cell_c3_ray_singer_torsion() -> Dict[str, Any]:
    """Runs Cell C3: R10-B Fricke saddle (N=2..7), Kronecker-Siegel, R10-C1 (kappa=1, N=2..6), and R10-C2 (kappa=2)."""
    old_dps = mp.mp.dps
    mp.mp.dps = 55
    try:
        # 1. R10-B Fricke saddle check & Kronecker-Siegel identity across N = 2..7
        t_probe = mp.mpc("0.19", "0.93")
        r10b_rows: List[Dict[str, Any]] = []
        kronecker_max_err = 0.0
        for n_lv in range(2, 8):
            lhs_ks = mp.mpf(1)
            for k in range(1, n_lv):
                lhs_ks *= siegel_unit_abs_mp(0, k, n_lv, t_probe, n_terms=65)
            rhs_ks = n_lv * (abs(_eta_mp(n_lv * t_probe, n_terms=65) / _eta_mp(t_probe, n_terms=65)) ** 2)
            kronecker_max_err = max(kronecker_max_err, float(abs(lhs_ks - rhs_ks)))

            tau_f = 1j / mp.sqrt(n_lv)
            grad_f = float(abs(_e2_hat_mp(tau_f, 70) + n_lv * _e2_hat_mp(n_lv * tau_f, 70)))
            h_f = mp.mpf("1e-8")

            def _visog(tz: mp.mpc, n_cur: int = n_lv) -> mp.mpf:
                return -mp.log(
                    mp.im(tz) * mp.sqrt(n_cur) * (abs(_eta_mp(tz, 70)) ** 2) * (abs(_eta_mp(n_cur * tz, 70)) ** 2)
                )

            v0 = _visog(tau_f)
            dxx = float((_visog(tau_f + h_f) - 2 * v0 + _visog(tau_f - h_f)) / (h_f * h_f))
            dyy = float((_visog(tau_f + 1j * h_f) - 2 * v0 + _visog(tau_f - 1j * h_f)) / (h_f * h_f))
            r10b_rows.append(
                {
                    "N": n_lv,
                    "fricke_tau_imag": float(mp.im(tau_f)),
                    "fricke_grad_norm": grad_f,
                    "fricke_hessian_dxx_dyy": [dxx, dyy],
                    "fricke_laplacian_err_vs_N": abs((dxx + dyy) - float(n_lv)),
                    "fricke_is_saddle": (dxx < 0.0) and (dyy > 0.0),
                }
            )

        # 2. R10-C1 (kappa = 1, bundle O (+) L_{1/N}) global minima across N = 2..6
        xs_c1 = np.linspace(-0.5, 0.5, 25)
        ys_c1 = np.linspace(0.84, 2.5, 25)
        xg1, yg1 = np.meshgrid(xs_c1, ys_c1, indexing="ij")
        mask1 = (xg1 * xg1 + yg1 * yg1) >= 0.96
        t_flat1 = (xg1[mask1] + 1j * yg1[mask1]).ravel()
        y_flat1 = np.imag(t_flat1)
        q_flat1 = np.exp(2j * np.pi * t_flat1)
        eta_p1 = np.ones_like(t_flat1, dtype=np.complex128)
        qm1 = q_flat1.copy()
        for _ in range(18):
            eta_p1 *= 1.0 - qm1
            qm1 *= q_flat1
        eta_abs4_1 = np.abs(np.exp(1j * np.pi * t_flat1 / 12.0) * eta_p1) ** 4

        r10c1_rows: List[Dict[str, Any]] = []
        tau0_star_n5_mp = mp.mpc("0.112204195", "0.9936851145")
        for n_lv in range(2, 7):
            sheets = build_marked_lines(n_lv)
            best_v = float("inf")
            best_sh = sheets[0]
            best_init = complex(0.0, 1.2)
            for r1, r2 in sheets:
                a1_f = (r1 % n_lv) / float(n_lv)
                a2_f = (r2 % n_lv) / float(n_lv)
                b2_f = a1_f * a1_f - a1_f + (1.0 / 6.0)
                z_f = np.exp(2j * np.pi * a2_f)
                sp = np.ones_like(t_flat1, dtype=np.complex128)
                if r1 % n_lv == 0:
                    sp *= 1.0 - z_f
                    for m in range(1, 16):
                        qm = q_flat1 ** m
                        sp *= (1.0 - qm * z_f) * (1.0 - qm / z_f)
                else:
                    qa1 = np.exp(2j * np.pi * a1_f * t_flat1)
                    qb1 = np.exp(2j * np.pi * (1.0 - a1_f) * t_flat1)
                    for m in range(0, 16):
                        qm = q_flat1 ** m
                        sp *= (1.0 - qm * qa1 * z_f) * (1.0 - qm * qb1 / z_f)
                g_abs2 = np.abs(np.exp(2j * np.pi * t_flat1 * (0.5 * b2_f)) * sp) ** 2
                v_arr = -np.log(y_flat1 * eta_abs4_1 * g_abs2)
                idx = int(np.argmin(v_arr))
                if float(v_arr[idx]) < best_v:
                    best_v = float(v_arr[idx])
                    best_sh = (r1, r2)
                    best_init = complex(t_flat1[idx])

            sol1 = mp.findroot(
                lambda xr, yi, sh=best_sh, nl=n_lv: (
                    mp.re(x1_sheet_stationarity_eq_kappa(xr + 1j * yi, sh[0], sh[1], nl, kappa=1, n_terms=50)),
                    mp.im(x1_sheet_stationarity_eq_kappa(xr + 1j * yi, sh[0], sh[1], nl, kappa=1, n_terms=50)),
                ),
                (mp.mpf(best_init.real), mp.mpf(best_init.imag)),
                tol=mp.mpf("1e-34"),
                maxsteps=200,
            )
            t_pol, sh_can = _canonicalize_tau_and_sheet(mp.mpc(sol1[0], sol1[1]), best_sh[0], best_sh[1], n_lv)
            if n_lv == 5:
                tau0_star_n5_mp = t_pol

            v0_c1 = v_x1_sheet_kappa_mp(t_pol, sh_can[0], sh_can[1], n_lv, kappa=1, n_terms=50)
            grad_c1 = float(abs(x1_sheet_stationarity_eq_kappa(t_pol, sh_can[0], sh_can[1], n_lv, kappa=1, n_terms=50)))
            h_s = mp.mpf("1e-8")
            dxx = float(
                (
                    v_x1_sheet_kappa_mp(t_pol + h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                    - 2 * v0_c1
                    + v_x1_sheet_kappa_mp(t_pol - h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                )
                / (h_s * h_s)
            )
            dyy = float(
                (
                    v_x1_sheet_kappa_mp(t_pol + 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                    - 2 * v0_c1
                    + v_x1_sheet_kappa_mp(t_pol - 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                )
                / (h_s * h_s)
            )
            dxy = float(
                (
                    v_x1_sheet_kappa_mp(t_pol + h_s + 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                    - v_x1_sheet_kappa_mp(t_pol + h_s - 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                    - v_x1_sheet_kappa_mp(t_pol - h_s + 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                    + v_x1_sheet_kappa_mp(t_pol - h_s - 1j * h_s, sh_can[0], sh_can[1], n_lv, 1, 50)
                )
                / (4 * h_s * h_s)
            )
            hess_eigs = np.linalg.eigvalsh(np.array([[dxx, dxy], [dxy, dyy]], dtype=float))
            x_f = float(mp.re(t_pol))
            breaks_mirror = (abs(x_f) > 1e-6) and (abs(abs(x_f) - 0.5) > 1e-6)
            r10c1_rows.append(
                {
                    "N": n_lv,
                    "winning_sheet": list(sh_can),
                    "tau0_star": [x_f, float(mp.im(t_pol))],
                    "abs_tau0_sq": float(abs(t_pol) ** 2),
                    "V_min": float(v0_c1),
                    "grad_norm": grad_c1,
                    "hessian_min_eig": float(np.min(hess_eigs)),
                    "breaks_re_tau_0_and_half": breaks_mirror,
                }
            )

        # 3. R10-C2 (kappa = 2, twin-symmetric rank-3 bundle O (+) L_{1/N} (+) L_{-1/N}):
        #    (a) Verify exact algebraic cusp-slope identity `1/3 + 4*B_2(a1) == (2*a1 - 1)^2` and even-N cusp escape
        even_cusp_escape: List[Dict[str, Any]] = []
        for n_even in (2, 4, 6):
            half_sheet = (n_even // 2, 1)
            v_y10 = float(v_x1_sheet_kappa_mp(mp.mpc("0.25", "10.0"), half_sheet[0], half_sheet[1], n_even, kappa=2, n_terms=25))
            v_y100 = float(v_x1_sheet_kappa_mp(mp.mpc("0.25", "100.0"), half_sheet[0], half_sheet[1], n_even, kappa=2, n_terms=25))
            # Since slope == 0 on a1 = 1/2, V(y=100) - V(y=10) == -ln(10) ~ -2.302585093 -> unbounded below!
            even_cusp_escape.append(
                {
                    "N": n_even,
                    "half_period_sheet": list(half_sheet),
                    "V_at_y10": v_y10,
                    "V_at_y100": v_y100,
                    "delta_V_vs_minus_ln10_err": abs((v_y100 - v_y10) - (-math.log(10.0))),
                    "escapes_to_minus_inf": v_y100 < v_y10 - 2.3,
                }
            )

        #    (b) High-precision 55-dps search + Newton polish for odd levels N = 3 and N = 5
        odd_c2_rows: List[Dict[str, Any]] = []
        tau0_kappa2_n5_mp = mp.mpc("0.25", str(25.0 / math.pi))
        for n_odd in (3, 5):
            sheets_odd = build_marked_lines(n_odd)
            y_asymp = (n_odd * n_odd) / math.pi
            x_grid = [mp.mpf(k) / mp.mpf(16) for k in range(-8, 9)]
            y_grid = [mp.mpf("1.1"), mp.mpf("1.8")] + [
                mp.mpf(str(y_asymp)) * (mp.mpf("0.7") + mp.mpf("0.075") * j) for j in range(9)
            ]
            best_v2 = mp.mpf("inf")
            best_sh2 = sheets_odd[0]
            best_t2 = mp.mpc("0.25", str(y_asymp))
            for sh in sheets_odd:
                for xv in x_grid:
                    for yv in y_grid:
                        if xv * xv + yv * yv < mp.mpf("0.98"):
                            continue
                        val = v_x1_sheet_kappa_mp(xv + 1j * yv, sh[0], sh[1], n_odd, kappa=2, n_terms=30)
                        if val < best_v2:
                            best_v2 = val
                            best_sh2 = sh
                            best_t2 = xv + 1j * yv

            sol2 = mp.findroot(
                lambda xr, yi, sh=best_sh2, nl=n_odd: (
                    mp.re(x1_sheet_stationarity_eq_kappa(xr + 1j * yi, sh[0], sh[1], nl, kappa=2, n_terms=35)),
                    mp.im(x1_sheet_stationarity_eq_kappa(xr + 1j * yi, sh[0], sh[1], nl, kappa=2, n_terms=35)),
                ),
                (mp.re(best_t2), mp.im(best_t2)),
                tol=mp.mpf("1e-34"),
                maxsteps=200,
            )
            t2_pol, sh2_can = _canonicalize_tau_and_sheet(mp.mpc(sol2[0], sol2[1]), best_sh2[0], best_sh2[1], n_odd)
            if n_odd == 5:
                tau0_kappa2_n5_mp = t2_pol

            v0_c2 = v_x1_sheet_kappa_mp(t2_pol, sh2_can[0], sh2_can[1], n_odd, kappa=2, n_terms=40)
            grad_c2 = float(abs(x1_sheet_stationarity_eq_kappa(t2_pol, sh2_can[0], sh2_can[1], n_odd, kappa=2, n_terms=40)))
            h_s2 = mp.mpf("1e-8")
            dxx2 = float(
                (
                    v_x1_sheet_kappa_mp(t2_pol + h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                    - 2 * v0_c2
                    + v_x1_sheet_kappa_mp(t2_pol - h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                )
                / (h_s2 * h_s2)
            )
            dyy2 = float(
                (
                    v_x1_sheet_kappa_mp(t2_pol + 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                    - 2 * v0_c2
                    + v_x1_sheet_kappa_mp(t2_pol - 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                )
                / (h_s2 * h_s2)
            )
            dxy2 = float(
                (
                    v_x1_sheet_kappa_mp(t2_pol + h_s2 + 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                    - v_x1_sheet_kappa_mp(t2_pol + h_s2 - 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                    - v_x1_sheet_kappa_mp(t2_pol - h_s2 + 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                    + v_x1_sheet_kappa_mp(t2_pol - h_s2 - 1j * h_s2, sh2_can[0], sh2_can[1], n_odd, 2, 40)
                )
                / (4 * h_s2 * h_s2)
            )
            hess_eigs2 = np.linalg.eigvalsh(np.array([[dxx2, dxy2], [dxy2, dyy2]], dtype=float))
            x2_f = float(mp.re(t2_pol))
            breaks_mirror2 = (abs(x2_f) > 1e-6) and (abs(abs(x2_f) - 0.5) > 1e-6)
            odd_c2_rows.append(
                {
                    "N": n_odd,
                    "winning_sheet": list(sh2_can),
                    "tau0_kappa2_star": [x2_f, float(mp.im(t2_pol))],
                    "tau0_kappa2_star_30dps": [mp.nstr(mp.re(t2_pol), 30), mp.nstr(mp.im(t2_pol), 30)],
                    "V_min": float(v0_c2),
                    "grad_norm": grad_c2,
                    "hessian_eigs": [float(hess_eigs2[0]), float(hess_eigs2[1])],
                    "hessian_min_eig": float(np.min(hess_eigs2)),
                    "breaks_re_tau_0_and_half": breaks_mirror2,
                }
            )

        c1_by_n = {r["N"]: r for r in r10c1_rows}
        c2_by_n = {r["N"]: r for r in odd_c2_rows}
        holds = (
            all(r["fricke_is_saddle"] and r["fricke_grad_norm"] < 1e-25 for r in r10b_rows)
            and (kronecker_max_err < 1e-25)
            and all(not c1_by_n[n]["breaks_re_tau_0_and_half"] for n in (2, 3, 4, 6))
            and c1_by_n[5]["breaks_re_tau_0_and_half"]
            and (c1_by_n[5]["grad_norm"] < 1e-20)
            and (c1_by_n[5]["hessian_min_eig"] > 0.0)
            and all(e["escapes_to_minus_inf"] and e["delta_V_vs_minus_ln10_err"] < 1e-8 for e in even_cusp_escape)
            and all(r["grad_norm"] < 1e-20 and r["hessian_min_eig"] > 0.0 for r in odd_c2_rows)
        )
        return {
            "holds": holds,
            "kronecker_siegel_max_err": kronecker_max_err,
            "R10B_fricke_saddles": r10b_rows,
            "R10C1_kappa1_minima": r10c1_rows,
            "R10C2_even_N_cusp_escape": even_cusp_escape,
            "R10C2_odd_N_minima": odd_c2_rows,
            "_tau0_star_n5": complex(float(mp.re(tau0_star_n5_mp)), float(mp.im(tau0_star_n5_mp))),
            "_tau0_kappa2_n5": complex(float(mp.re(tau0_kappa2_n5_mp)), float(mp.im(tau0_kappa2_n5_mp))),
            "_winning_sheet_k1": c1_by_n[5]["winning_sheet"],
            "_winning_sheet_k2": c2_by_n[5]["winning_sheet"],
        }
    finally:
        mp.mp.dps = old_dps


# =============================================================================
# Cells H1, H2, H3: Data-Free FR-FIB Structural Hierarchy & CP Invariant Census
# =============================================================================


def build_24_level5_and_spin10_lines() -> List[Dict[str, Any]]:
    """Constructs all 12 primitive order-5 torsion lines in Omega_1(5) and their 12 spin-shifted order-10 companions."""
    omega5 = build_marked_lines(5)
    out: List[Dict[str, Any]] = []
    for r1, r2 in omega5:
        a5 = Fr(r1, 5)
        b5 = Fr(r2, 5)
        out.append({"family": "order_5_primitive", "sheet": [r1, r2], "a": a5, "b": b5, "label": f"({a5}, {b5})"})
    for r1, r2 in omega5:
        a10 = Fr(r1, 5)
        b10 = (Fr(r2, 5) + Fr(1, 2)) % 1
        out.append({"family": "order_10_spin_shifted", "sheet": [r1, r2], "a": a10, "b": b10, "label": f"({a10}, {b10})"})
    return out


def _decade_spans(ratios_2_3_over_1: List[float]) -> Tuple[float, float]:
    """Given [sigma_2/sigma_1, sigma_3/sigma_1], returns (log10(sigma_1/sigma_3), log10(sigma_1/sigma_2))."""
    r21, r31 = ratios_2_3_over_1
    span_13 = -math.log10(max(r31, 1e-300)) if r31 > 0.0 else 300.0
    span_12 = -math.log10(max(r21, 1e-300)) if r21 > 0.0 else 300.0
    return float(span_13), float(span_12)

# =============================================================================
# Cell C4: P-776 Whole-Subweave Twin-Odd Hyperbolic Laplacian on (Gamma_0(5), chi_5)
# =============================================================================


def chi5_int(d_val: int) -> int:
    r = d_val % 5
    if r in (1, 4):
        return 1
    if r in (2, 3):
        return -1
    return 0


def fplus5_y_bottom(x_abs: np.ndarray) -> np.ndarray:
    """Exact lower boundary height y_bot(|x|) of F^+ for |x| <= 0.5."""
    xa = np.abs(np.asarray(x_abs, dtype=np.float64))
    y_c0 = np.sqrt(np.maximum(0.0, 0.2 - xa * xa))
    y_cf2 = np.sqrt(np.maximum(0.0, 0.05 - (0.5 - xa) * (0.5 - xa)))
    return np.maximum(y_c0, y_cf2)


def pullback_gamma0_plus_5_vec(
    x_in: np.ndarray, y_in: np.ndarray, eps5: int
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Pulls z = x + i*y into F^+ = {|x| <= 1/2, x^2+y^2 >= 1/5, (|x|-1/2)^2+y^2 >= 1/20}
    tracking the exact (chi_5, W_5 = eps5) multiplier in {+1, -1}."""
    x = np.array(x_in, dtype=np.float64, copy=True)
    y = np.array(y_in, dtype=np.float64, copy=True)
    mult = np.ones_like(x, dtype=np.float64)
    for _ in range(140):
        x -= np.round(x)
        r2 = x * x + y * y
        m_w5 = r2 < (0.2 - 1e-13)
        if np.any(m_w5):
            r2_m = r2[m_w5]
            x[m_w5] = -x[m_w5] / (5.0 * r2_m)
            y[m_w5] = y[m_w5] / (5.0 * r2_m)
            mult[m_w5] *= float(eps5)
            continue
        u_pos = x - 0.5
        d2_pos = u_pos * u_pos + y * y
        m_pos = (x >= 0.0) & (d2_pos < (0.05 - 1e-13))
        u_neg = x + 0.5
        d2_neg = u_neg * u_neg + y * y
        m_neg = (x < 0.0) & (d2_neg < (0.05 - 1e-13))
        if not (np.any(m_pos) or np.any(m_neg)):
            break
        if np.any(m_pos):
            d2_m = d2_pos[m_pos]
            x[m_pos] = 0.5 - u_pos[m_pos] / (20.0 * d2_m)
            y[m_pos] = y[m_pos] / (20.0 * d2_m)
            mult[m_pos] *= float(-eps5)
        if np.any(m_neg):
            d2_m = d2_neg[m_neg]
            x[m_neg] = -0.5 - u_neg[m_neg] / (20.0 * d2_m)
            y[m_neg] = y[m_neg] / (20.0 * d2_m)
            mult[m_neg] *= float(-eps5)
    x -= np.round(x)
    return x, y, mult


def build_fplus5_quadrature(nx_left: int = 36, nx_right: int = 24, nt: int = 48) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """2D Gauss-Legendre quadrature over F^+ via x in [0, 0.4] U [0.4, 0.5] and t = y_bot(x)/y in (0, 1]
    (doubled by J-symmetry to integrate even functions |psi|^2 over all of F^+)."""
    xl_01, wl_01 = leggauss(nx_left)
    xr_01, wr_01 = leggauss(nx_right)
    tl_01, wt_01 = leggauss(nt)

    xs_l = 0.2 * (xl_01 + 1.0)
    ws_l = 0.2 * wl_01
    xs_r = 0.45 + 0.05 * xr_01
    ws_r = 0.05 * wr_01
    xs = np.concatenate([xs_l, xs_r])
    wxs = np.concatenate([ws_l, ws_r])

    ts = 0.5 * (tl_01 + 1.0)
    wts = 0.5 * wt_01

    yb = fplus5_y_bottom(xs)
    qx = np.repeat(xs[:, None], nt, axis=1).ravel()
    qy = np.minimum(yb[:, None] / ts[None, :], 9.0).ravel()
    # Factor 2.0 accounts for x in [-0.5, 0] U [0, 0.5] on even integrands |psi(z)|^2
    qw = (2.0 * (wxs / yb)[:, None] * wts[None, :]).ravel()
    return qx, qy, qw


def eval_maass_raw_in_fplus(
    r_val: float, a_sc: np.ndarray, eps_j: int, x_arr: np.ndarray, y_arr: np.ndarray
) -> np.ndarray:
    """Evaluates psi(x + i*y) directly from its Fourier expansion (NO pullback applied), using scaled basis
    exp(pi*R/2)*K_{iR}(2*pi*n*y)*sqrt(y)."""
    x = np.asarray(x_arr, dtype=np.float64)
    y = np.asarray(y_arr, dtype=np.float64)
    shape = x.shape
    xr = x.ravel()
    yr = y.ravel()
    m_trunc = len(a_sc)
    ns = np.arange(1, m_trunc + 1, dtype=np.float64)
    sc = math.exp(0.5 * math.pi * r_val)
    k_mat = besselk_ir_vec(r_val, 2.0 * np.pi * yr[:, None] * ns[None, :]) * sc * np.sqrt(yr[:, None])
    if eps_j == -1:
        trig = np.sin(2.0 * np.pi * xr[:, None] * ns[None, :])
    else:
        trig = np.cos(2.0 * np.pi * xr[:, None] * ns[None, :])
    vals = (k_mat * trig) @ a_sc
    return vals.reshape(shape)


def eval_maass_global(
    r_val: float, a_sc: np.ndarray, eps_j: int, eps_5: int, x_arr: np.ndarray, y_arr: np.ndarray
) -> np.ndarray:
    """Evaluates psi(x + i*y) anywhere on H by exact pullback to F^+ followed by Fourier summation."""
    xp, yp, mult = pullback_gamma0_plus_5_vec(np.asarray(x_arr, dtype=np.float64), np.asarray(y_arr, dtype=np.float64), eps_5)
    return mult * eval_maass_raw_in_fplus(r_val, a_sc, eps_j, xp, yp)


def run_cell_c4_p776_twin_odd_maass() -> Dict[str, Any]:
    """Executes sealed Cell C4: P-776 Twin-Odd Maass Operator on L^2_cusp(Gamma_0(5), chi_5)."""
    # 1. Verify F^+ quadrature area == pi and pullback height floor >= 0.20
    qx, qy, qw = build_fplus5_quadrature()
    fplus_area = float(np.sum(qw))
    area_err = abs(fplus_area - math.pi)

    tx_g, ty_g = np.meshgrid(np.linspace(-1.2, 1.2, 55), np.linspace(0.05, 1.4, 35), indexing="ij")
    _, typ_pb, _ = pullback_gamma0_plus_5_vec(tx_g.ravel(), ty_g.ravel(), +1)
    min_pb_height = float(np.min(typ_pb))

    # 2. Scan all 4 (eps_J, eps_5) sectors over R in [0.8, 11.0]
    m_trunc = 30
    q_pts = 160
    y1, y2 = 0.165, 0.143
    xj = (np.arange(q_pts, dtype=np.float64) + 0.5) / (2.0 * q_pts)
    ns = np.arange(1, m_trunc + 1, dtype=np.float64)

    pb1_pos = pullback_gamma0_plus_5_vec(xj, np.full_like(xj, y1), +1)
    pb1_neg = pullback_gamma0_plus_5_vec(xj, np.full_like(xj, y1), -1)
    pb2_pos = pullback_gamma0_plus_5_vec(xj, np.full_like(xj, y2), +1)
    pb2_neg = pullback_gamma0_plus_5_vec(xj, np.full_like(xj, y2), -1)
    pb_map = {
        (y1, +1): pb1_pos,
        (y1, -1): pb1_neg,
        (y2, +1): pb2_pos,
        (y2, -1): pb2_neg,
    }

    tj_sin = (2.0 / q_pts) * np.sin(2.0 * np.pi * ns[:, None] * xj[None, :])
    tj_cos = (2.0 / q_pts) * np.cos(2.0 * np.pi * ns[:, None] * xj[None, :])
    tp_cache: Dict[Tuple[float, int, int], np.ndarray] = {}
    for y_v in (y1, y2):
        for e5 in (+1, -1):
            px, _py, pm = pb_map[(y_v, e5)]
            tp_cache[(y_v, -1, e5)] = pm[:, None] * np.sin(2.0 * np.pi * px[:, None] * ns[None, :])
            tp_cache[(y_v, +1, e5)] = pm[:, None] * np.cos(2.0 * np.pi * px[:, None] * ns[None, :])

    def build_horo_mat(r_v: float, y_v: float, eps_j: int, eps_5: int) -> Tuple[np.ndarray, np.ndarray]:
        _px, py, _pm = pb_map[(y_v, eps_5)]
        sc = math.exp(0.5 * math.pi * r_v)
        kh = besselk_ir_vec(r_v, 2.0 * np.pi * ns * y_v) * sc * math.sqrt(y_v)
        kp = besselk_ir_vec(r_v, 2.0 * np.pi * py[:, None] * ns[None, :]) * sc * np.sqrt(py[:, None])
        tj = tj_sin if eps_j == -1 else tj_cos
        tp = tp_cache[(y_v, eps_j, eps_5)]
        return np.diag(kh) - tj @ (kp * tp), kh

    r_grid = np.linspace(0.8, 11.25, 580)
    py_y1 = pb1_pos[1]
    kh_grid: List[np.ndarray] = []
    kp_grid: List[np.ndarray] = []
    for r_g in r_grid:
        rv = float(r_g)
        sc = math.exp(0.5 * math.pi * rv)
        kh_grid.append(besselk_ir_vec(rv, 2.0 * np.pi * ns * y1) * sc * math.sqrt(y1))
        kp_grid.append(besselk_ir_vec(rv, 2.0 * np.pi * py_y1[:, None] * ns[None, :]) * sc * np.sqrt(py_y1[:, None]))

    def piv_residual_from_mat(a_mat: np.ndarray, kh_vec: np.ndarray, piv: int) -> Tuple[float, np.ndarray]:
        if float(np.min(np.abs(kh_vec[:6]))) < 1e-5:
            return float("nan"), np.empty(0)
        keep = [i for i in range(m_trunc) if i != piv]
        try:
            a_keep = np.linalg.solve(a_mat[np.ix_(keep, keep)] / kh_vec[keep, None], -a_mat[keep, piv] / kh_vec[keep])
        except np.linalg.LinAlgError:
            return float("nan"), np.empty(0)
        a_full = np.empty(m_trunc, dtype=np.float64)
        a_full[piv] = 1.0
        a_full[keep] = a_keep
        return float((a_mat[piv, :] @ a_full) / kh_vec[piv]), a_full

    validated_states: List[Dict[str, Any]] = []
    for eps_j in (-1, +1):
        tj = tj_sin if eps_j == -1 else tj_cos
        for eps_5 in (+1, -1):
            tp = tp_cache[(y1, eps_j, eps_5)]
            mats_sector = [np.diag(kh_g) - tj @ (kp_g * tp) for kh_g, kp_g in zip(kh_grid, kp_grid)]
            sector_roots: List[Dict[str, Any]] = []
            for piv in (0, 1, 2):
                gvals = [piv_residual_from_mat(a_m, kh_g, piv)[0] for a_m, kh_g in zip(mats_sector, kh_grid)]

                def f_scalar(rv: float, ej: int = eps_j, e5: int = eps_5, pv: int = piv) -> float:
                    am, khv = build_horo_mat(rv, y1, ej, e5)
                    return piv_residual_from_mat(am, khv, pv)[0]

                for k in range(len(r_grid) - 1):
                    g0, g1 = gvals[k], gvals[k + 1]
                    if not (np.isfinite(g0) and np.isfinite(g1)):
                        continue
                    if abs(g0) >= 5.0 or abs(g1) >= 5.0 or (g0 * g1 > 0.0):
                        continue
                    try:
                        r_cand = float(
                            sp_opt.brentq(f_scalar, float(r_grid[k]), float(r_grid[k + 1]), xtol=1e-14, rtol=1e-14)
                        )
                    except ValueError:
                        continue
                    am1, kh1 = build_horo_mat(r_cand, y1, eps_j, eps_5)
                    _, a_vec = piv_residual_from_mat(am1, kh1, piv)
                    if a_vec.size == 0 or float(np.max(np.abs(a_vec))) > 35.0:
                        continue
                    a_unit = a_vec / float(np.max(np.abs(a_vec)))
                    if float(np.max(np.abs(a_unit[:6]))) < 0.05:
                        continue
                    am2, kh2 = build_horo_mat(r_cand, y2, eps_j, eps_5)
                    rows_ok = [mi for mi in range(10) if abs(float(kh2[mi])) > 1e-4]
                    if len(rows_ok) < 4:
                        continue
                    y2_err = float(np.linalg.norm((am2[rows_ok, :] @ a_unit) / kh2[rows_ok]))
                    if y2_err < 1e-8:
                        sector_roots.append(
                            {
                                "R": r_cand,
                                "eps_J": eps_j,
                                "eps_5": eps_5,
                                "piv": piv,
                                "y2_err": y2_err,
                                "a_raw": a_vec,
                            }
                        )
            # Deduplicate roots within |R_a - R_b| < 1e-6 in the same (eps_J, eps_5) sector
            sector_roots.sort(key=lambda d: d["R"])
            dedup: List[Dict[str, Any]] = []
            for rt in sector_roots:
                if not dedup or abs(rt["R"] - dedup[-1]["R"]) >= 1e-6:
                    dedup.append(rt)
                elif rt["y2_err"] < dedup[-1]["y2_err"]:
                    dedup[-1] = rt
            validated_states.extend(dedup)

    validated_states.sort(key=lambda d: d["R"])
    if not validated_states:
        return {"holds": False, "error": "No Maass cusp forms found in [0.8, 11.0]"}

    # 3. Cluster eigenstates across sectors into joint Hecke-Maass newform eigenspaces
    clusters: List[Dict[str, Any]] = []
    for st in validated_states:
        vals_q = eval_maass_raw_in_fplus(st["R"], st["a_raw"], st["eps_J"], qx, qy)
        l2_norm = math.sqrt(float(np.sum(qw * (vals_q * vals_q))))
        st["a_l2"] = st["a_raw"] / l2_norm
        st["l2_norm_raw"] = l2_norm
        if not clusters or abs(st["R"] - clusters[-1]["R_mean"]) >= 1e-5:
            clusters.append({"states": [st], "R_mean": st["R"]})
        else:
            clusters[-1]["states"].append(st)
            clusters[-1]["R_mean"] = float(np.mean([x["R"] for x in clusters[-1]["states"]]))
    clusters = [cl for cl in clusters if cl["R_mean"] <= 11.0]

    def analyze_cluster(cl: Dict[str, Any]) -> Dict[str, Any]:
        sts = cl["states"]
        dim_r = len(sts)
        r_mean = cl["R_mean"]
        eps_j = sts[0]["eps_J"]
        max_y2 = max(s["y2_err"] for s in sts)
        if dim_r == 1:
            s0 = sts[0]
            c_vec = (s0["a_l2"] / s0["a_l2"][0]).astype(np.complex128)
            kramers_split = None
        elif dim_r == 2:
            by_e5 = {s["eps_5"]: s for s in sts}
            assert (+1 in by_e5) and (-1 in by_e5) and (by_e5[+1]["eps_J"] == by_e5[-1]["eps_J"])
            ap = by_e5[+1]["a_l2"]
            am = by_e5[-1]["a_l2"]
            kramers_split = abs(by_e5[+1]["R"] - by_e5[-1]["R"])
            best_c = None
            best_score = float("inf")
            for sgn in (+1.0, -1.0):
                cand = (ap + 1j * sgn * am) / (ap[0] + 1j * sgn * am[0])
                sc_h = abs(cand[1].real) + abs(cand[2].real) + abs(cand[1] ** 2 - cand[3] + 1.0)
                if sc_h < best_score:
                    best_score = float(sc_h)
                    best_c = cand
            assert best_c is not None
            c_vec = best_c
        else:
            raise RuntimeError(f"Unexpected cluster multiplicity {dim_r} at R={r_mean}")

        # Direct U_5 operator verification across 3 generic interior points (picking largest |f_1(z)|)
        f_z = 0.0j
        f_u5 = 0.0j
        for z_tx, z_ty in ((0.21, 0.63), (0.13, 0.89), (0.33, 0.52)):
            u5_xs = np.array([(z_tx + b) / 5.0 for b in range(5)], dtype=np.float64)
            u5_ys = np.full(5, z_ty / 5.0, dtype=np.float64)
            if dim_r == 1:
                s0 = sts[0]
                fz_c = complex(eval_maass_global(r_mean, s0["a_l2"], eps_j, s0["eps_5"], np.array([z_tx]), np.array([z_ty]))[0]) / s0["a_l2"][0]
                fu5_c = complex(np.sum(eval_maass_global(r_mean, s0["a_l2"], eps_j, s0["eps_5"], u5_xs, u5_ys)) / math.sqrt(5.0)) / s0["a_l2"][0]
            else:
                by_e5 = {s["eps_5"]: s for s in sts}
                ap = by_e5[+1]["a_l2"]
                am = by_e5[-1]["a_l2"]
                c_plus = (ap + 1j * am) / (ap[0] + 1j * am[0])
                sgn = 1.0 if np.max(np.abs(c_plus - c_vec)) < 1e-9 else -1.0
                denom = ap[0] + 1j * sgn * am[0]
                fp = float(eval_maass_global(r_mean, ap, eps_j, +1, np.array([z_tx]), np.array([z_ty]))[0])
                fm = float(eval_maass_global(r_mean, am, eps_j, -1, np.array([z_tx]), np.array([z_ty]))[0])
                fz_c = (fp + 1j * sgn * fm) / denom
                up_v = float(np.sum(eval_maass_global(r_mean, ap, eps_j, +1, u5_xs, u5_ys))) / math.sqrt(5.0)
                um_v = float(np.sum(eval_maass_global(r_mean, am, eps_j, -1, u5_xs, u5_ys))) / math.sqrt(5.0)
                fu5_c = (up_v + 1j * sgn * um_v) / denom
            if abs(fz_c) > abs(f_z):
                f_z, f_u5 = fz_c, fu5_c

        c5_fourier = complex(c_vec[4])
        c5_u5_op = f_u5 / f_z if abs(f_z) > 1e-12 else c5_fourier
        hecke_errs = {
            "abs_Re_c2": abs(float(c_vec[1].real)),
            "abs_Re_c3": abs(float(c_vec[2].real)),
            "abs_c2sq_minus_c4_plus_1": abs(c_vec[1] ** 2 - c_vec[3] + 1.0),
            "abs_c2c3_minus_c6": abs(c_vec[1] * c_vec[2] - c_vec[5]),
            "abs_norm_c5_minus_1": abs(abs(c5_fourier) - 1.0),
            "abs_u5_op_minus_c5": abs(c5_u5_op - c5_fourier),
        }
        return {
            "R": r_mean,
            "lambda": 0.25 + r_mean * r_mean,
            "dim_R": dim_r,
            "class_label": "Class_A_RM_Qsqrt5" if dim_r == 1 else "Class_B_Kramers_doublet",
            "eps_J": eps_j,
            "eps_5_list": [s["eps_5"] for s in sts],
            "kramers_split": kramers_split,
            "max_y2_err": max_y2,
            "c1_to_c6": [[float(z.real), float(z.imag)] for z in c_vec[:6]],
            "hecke_errors": hecke_errs,
            "hecke_holds": max(hecke_errs.values()) < 1e-9,
            "_states": sts,
        }

    analyzed_clusters = [analyze_cluster(cl) for cl in clusters]
    ground = analyzed_clusters[0]
    class_a_odd = [c for c in analyzed_clusters if c["dim_R"] == 1 and c["eps_J"] == -1]
    class_b_all = [c for c in analyzed_clusters if c["dim_R"] == 2]

    rm_odd1_err = abs(class_a_odd[0]["R"] - RM_Q_SQRT5_R1_ODD) if class_a_odd else float("inf")
    lowest_class_b = class_b_all[0] if class_b_all else None
    class_b_kramers_ok = (
        lowest_class_b is not None
        and lowest_class_b["kramers_split"] is not None
        and lowest_class_b["kramers_split"] < 1e-9
        and lowest_class_b["hecke_holds"]
    )

    # 4. Forced zeros & boundary nodal arcs on ground state (direct raw Fourier series on F^+, ZERO pullback wrapper!)
    ze_x = np.array([0.4, -0.4], dtype=np.float64)
    ze_y = np.array([0.2, 0.2], dtype=np.float64)
    zf1_x, zf1_y = np.array([0.0]), np.array([1.0 / math.sqrt(5.0)])
    zf2_x, zf2_y = np.array([0.5]), np.array([0.5 / math.sqrt(5.0)])
    th_c0 = np.linspace(math.asin(1.0 / math.sqrt(5.0)) + 0.02, 0.5 * math.pi - 0.02, 25)
    c0_x, c0_y = np.cos(th_c0) / math.sqrt(5.0), np.sin(th_c0) / math.sqrt(5.0)
    th_cf2 = np.linspace(0.5 * math.pi + 0.02, math.pi - math.asin(2.0 / math.sqrt(5.0)) - 0.02, 25)
    cf2_x = 0.5 + np.cos(th_cf2) / (2.0 * math.sqrt(5.0))
    cf2_y = np.sin(th_cf2) / (2.0 * math.sqrt(5.0))

    def check_nodal_laws(cl_info: Dict[str, Any]) -> Dict[str, float]:
        max_ze = 0.0
        max_arc = 0.0
        max_zf_forced = 0.0
        for s in cl_info["_states"]:
            rv, al2, ej, e5 = s["R"], s["a_l2"], s["eps_J"], s["eps_5"]
            max_ze = max(max_ze, float(np.max(np.abs(eval_maass_raw_in_fplus(rv, al2, ej, ze_x, ze_y)))))
            if e5 == -ej:
                max_arc = max(max_arc, float(np.max(np.abs(eval_maass_raw_in_fplus(rv, al2, ej, c0_x, c0_y)))))
            if e5 == +ej:
                max_arc = max(max_arc, float(np.max(np.abs(eval_maass_raw_in_fplus(rv, al2, ej, cf2_x, cf2_y)))))
            if e5 == +1 or ej == -1:
                max_zf_forced = max(max_zf_forced, float(np.max(np.abs(eval_maass_raw_in_fplus(rv, al2, ej, zf2_x, zf2_y)))))
            if e5 == -1 or ej == -1:
                max_zf_forced = max(max_zf_forced, float(np.max(np.abs(eval_maass_raw_in_fplus(rv, al2, ej, zf1_x, zf1_y)))))
        return {"max_elliptic_zero_err": max_ze, "max_forced_arc_err": max_arc, "max_forced_fricke_cm_err": max_zf_forced}

    nodal_ground = check_nodal_laws(ground)
    nodal_class_b = check_nodal_laws(lowest_class_b) if lowest_class_b is not None else {}

    # 5. Canonical trace density rho_1(z): O(dim_R E_1) rotation invariance & modular/Fricke/mirror invariance
    g_states = ground["_states"]
    dim_g = ground["dim_R"]

    def rho1_vec(x_in: np.ndarray, y_in: np.ndarray) -> np.ndarray:
        acc = np.zeros_like(np.asarray(x_in, dtype=np.float64))
        for s in g_states:
            v = eval_maass_global(s["R"], s["a_l2"], s["eps_J"], s["eps_5"], x_in, y_in)
            acc = acc + v * v
        return acc / float(dim_g)

    rng_o = np.random.default_rng(77601)
    probe_x = rng_o.uniform(-0.45, 0.45, size=20)
    probe_y = fplus5_y_bottom(probe_x) + rng_o.uniform(0.05, 1.4, size=20)
    base_vals = np.vstack([eval_maass_global(s["R"], s["a_l2"], s["eps_J"], s["eps_5"], probe_x, probe_y) for s in g_states])
    rho_base = np.mean(base_vals * base_vals, axis=0)
    o_rot_max_err = 0.0
    for _ in range(12):
        if dim_g == 1:
            orth = np.array([[-1.0]])
        else:
            th = float(rng_o.uniform(0.0, 2.0 * math.pi))
            det_s = float(rng_o.choice([-1.0, 1.0]))
            orth = np.array([[math.cos(th), -det_s * math.sin(th)], [math.sin(th), det_s * math.cos(th)]])
        rot_vals = orth @ base_vals
        rho_rot = np.mean(rot_vals * rot_vals, axis=0)
        o_rot_max_err = max(o_rot_max_err, float(np.max(np.abs(rho_rot - rho_base))))

    # Check Gamma_0(5), W_5, and J invariance of rho_1 directly on probe points
    z_pr = probe_x + 1j * probe_y
    z_g1 = (3.0 * z_pr + 1.0) / (5.0 * z_pr + 2.0)
    z_w5 = -1.0 / (5.0 * z_pr)
    sym_inv_err = max(
        float(np.max(np.abs(rho1_vec(z_g1.real, z_g1.imag) - rho_base))),
        float(np.max(np.abs(rho1_vec(z_w5.real, z_w5.imag) - rho_base))),
        float(np.max(np.abs(rho1_vec(-probe_x, probe_y) - rho_base))),
    )

    # 6. Global peak optimization of rho_1(z) on F^+ cap {0 <= x <= 0.5}
    gx_1d = np.linspace(0.0, 0.5, 161)
    gy_1d = np.linspace(0.20, 3.20, 201)
    gxx, gyy = np.meshgrid(gx_1d, gy_1d, indexing="ij")
    mask_fp = gyy >= (fplus5_y_bottom(gxx) - 1e-14)
    cand_seeds: List[Tuple[float, float, float]] = []
    fx_m, fy_m = gxx[mask_fp], gyy[mask_fp]
    frho_m = rho1_vec(fx_m, fy_m)
    top_idx = np.argsort(frho_m)[::-1][:30]
    for idx in top_idx:
        cand_seeds.append((float(frho_m[idx]), float(fx_m[idx]), float(fy_m[idx])))

    # Polish in 2D via Nelder-Mead (unconstrained on H since rho_1 is smooth & reflection-symmetric across F^+ walls!)
    polished_pts: List[Tuple[float, float, float]] = []
    for _val0, sx0, sy0 in cand_seeds[:24]:
        opt = sp_opt.minimize(
            lambda xy: -float(rho1_vec(np.array([xy[0]]), np.array([xy[1]]))[0]),
            x0=np.array([sx0, sy0], dtype=np.float64),
            method="Nelder-Mead",
            options={"xatol": 1e-13, "fatol": 1e-15, "maxiter": 800},
        )
        if opt.fun < 0.0 and opt.x[1] > 0.02:
            px_p, py_p, _ = pullback_gamma0_plus_5_vec(np.array([opt.x[0]]), np.array([opt.x[1]]), +1)
            xf_p, yf_p = abs(float(px_p[0])), float(py_p[0])
            polished_pts.append((float(-opt.fun), xf_p, yf_p))

    # Also explicitly optimize along all 4 boundary curves of F^+ cap {0 <= x <= 0.5}
    # (a) x = 0, y in [1/sqrt(5), 3.0]
    r_x0 = sp_opt.minimize_scalar(
        lambda yv: -float(rho1_vec(np.array([0.0]), np.array([yv]))[0]),
        bounds=(1.0 / math.sqrt(5.0), 3.0),
        method="bounded",
        options={"xatol": 1e-13},
    )
    polished_pts.append((float(-r_x0.fun), 0.0, float(r_x0.x)))
    # (b) x = 0.5, y in [1/(2*sqrt(5)), 3.0]
    r_xh = sp_opt.minimize_scalar(
        lambda yv: -float(rho1_vec(np.array([0.5]), np.array([yv]))[0]),
        bounds=(0.5 / math.sqrt(5.0), 3.0),
        method="bounded",
        options={"xatol": 1e-13},
    )
    polished_pts.append((float(-r_xh.fun), 0.5, float(r_xh.x)))
    # (c) Arc C_0: theta in [asin(1/sqrt(5)), pi/2]
    r_c0 = sp_opt.minimize_scalar(
        lambda th: -float(rho1_vec(np.array([math.cos(th) / math.sqrt(5.0)]), np.array([math.sin(th) / math.sqrt(5.0)]))[0]),
        bounds=(math.asin(1.0 / math.sqrt(5.0)), 0.5 * math.pi),
        method="bounded",
        options={"xatol": 1e-13},
    )
    polished_pts.append(
        (float(-r_c0.fun), math.cos(float(r_c0.x)) / math.sqrt(5.0), math.sin(float(r_c0.x)) / math.sqrt(5.0))
    )
    # (d) Arc C_{f,2}^+: theta in [pi/2, pi - asin(2/sqrt(5))]
    r_cf2 = sp_opt.minimize_scalar(
        lambda th: -float(
            rho1_vec(
                np.array([0.5 + math.cos(th) / (2.0 * math.sqrt(5.0))]),
                np.array([math.sin(th) / (2.0 * math.sqrt(5.0))]),
            )[0]
        ),
        bounds=(0.5 * math.pi, math.pi - math.asin(2.0 / math.sqrt(5.0))),
        method="bounded",
        options={"xatol": 1e-13},
    )
    polished_pts.append(
        (
            float(-r_cf2.fun),
            0.5 + math.cos(float(r_cf2.x)) / (2.0 * math.sqrt(5.0)),
            math.sin(float(r_cf2.x)) / (2.0 * math.sqrt(5.0)),
        )
    )

    # Filter to genuine 2D local maxima in H and deduplicate orbits within 5e-4
    ang_chk = np.linspace(0.0, 2.0 * math.pi, 16, endpoint=False)
    local_max_orbits: List[Dict[str, Any]] = []
    polished_pts.sort(key=lambda t: t[0], reverse=True)
    for rho_v, xv, yv in polished_pts:
        if rho_v < 1e-9:
            continue
        ring_vals = rho1_vec(xv + 2e-5 * np.cos(ang_chk), yv + 2e-5 * np.sin(ang_chk))
        if float(np.max(ring_vals)) > rho_v + 1e-11:
            continue
        if any(math.hypot(xv - m["tau_fplus"][0], yv - m["tau_fplus"][1]) < 5e-4 for m in local_max_orbits):
            continue
        local_max_orbits.append({"rho_1": rho_v, "tau_fplus": [xv, yv]})

    win_peak = local_max_orbits[0]
    x_star, y_star = win_peak["tau_fplus"]
    rho_star = win_peak["rho_1"]
    rel_gap = (
        (rho_star - local_max_orbits[1]["rho_1"]) / rho_star if len(local_max_orbits) >= 2 else 1.0
    )

    on_x0 = abs(x_star) < 1e-6
    on_xh = abs(x_star - 0.5) < 1e-6
    on_c0 = abs(x_star * x_star + y_star * y_star - 0.2) < 1e-6
    on_cf2 = abs((x_star - 0.5) ** 2 + y_star * y_star - 0.05) < 1e-6
    at_zf1 = on_x0 and on_c0
    at_zf2 = on_xh and on_cf2
    if at_zf1 or at_zf2:
        x0_orbit_size = 1
        peak_locus = "Fricke_CM_fixed_point"
    elif on_x0 or on_xh or on_c0 or on_cf2:
        x0_orbit_size = 2
        if on_c0:
            peak_locus = "Fricke_circle_C0"
        elif on_cf2:
            peak_locus = "Side_Fricke_circle_Cf2"
        elif on_x0:
            peak_locus = "Mirror_axis_Re_0"
        else:
            peak_locus = "Mirror_axis_Re_half"
    else:
        x0_orbit_size = 4
        peak_locus = "Strict_interior_of_Fplus"

    x1_orbit_size = 2 * x0_orbit_size
    breaks_mirror_cp = not (on_x0 or on_xh)
    tau_maass = complex(x_star, y_star)
    tau_maass_w5 = -1.0 / (5.0 * tau_maass)

    # Strip internal numpy arrays before JSON serialization
    public_clusters = []
    for cl_d in analyzed_clusters[:10]:
        cp_d = {k: v for k, v in cl_d.items() if not k.startswith("_")}
        public_clusters.append(cp_d)

    c4_i_holds = (
        (area_err < 1e-13)
        and (min_pb_height >= 0.2 - 1e-12)
        and (rm_odd1_err < 1e-10)
        and class_b_kramers_ok
        and (ground["max_y2_err"] < 1e-8)
    )
    c4_ii_holds = (
        max(nodal_ground.values()) < 1e-11
        and (max(nodal_class_b.values()) < 1e-11 if nodal_class_b else False)
    )
    c4_iii_holds = ground["hecke_holds"] and (o_rot_max_err < 1e-14) and (sym_inv_err < 1e-11)
    c4_iv_holds = (len(local_max_orbits) >= 1) and (rel_gap > 1e-3)

    return {
        "holds": c4_i_holds and c4_ii_holds and c4_iii_holds and c4_iv_holds,
        "clauses": {
            "C4_i_spectral_and_multiplicity": c4_i_holds,
            "C4_ii_forced_zeros_and_arcs": c4_ii_holds,
            "C4_iii_hecke_atkin_li_and_O_invariance": c4_iii_holds,
            "C4_iv_unique_global_peak_orbit": c4_iv_holds,
        },
        "fplus_hyperbolic_area": fplus_area,
        "fplus_area_err_vs_pi": area_err,
        "pullback_min_height_check": min_pb_height,
        "total_validated_states_in_0p8_to_11": len(validated_states),
        "total_newform_clusters_in_0p8_to_11": len(analyzed_clusters),
        "rm_q_sqrt5_odd1_target": RM_Q_SQRT5_R1_ODD,
        "rm_q_sqrt5_odd1_abs_err": rm_odd1_err,
        "lowest_class_b_doublet": {k: v for k, v in lowest_class_b.items() if not k.startswith("_")} if lowest_class_b else None,
        "ground_state": {k: v for k, v in ground.items() if not k.startswith("_")},
        "nodal_verification_ground": nodal_ground,
        "nodal_verification_lowest_class_b": nodal_class_b,
        "rho1_orthogonal_rotation_12draws_max_err": o_rot_max_err,
        "rho1_gamma05_w5_j_invariance_max_err": sym_inv_err,
        "peak_orbit": {
            "tau_maass_fplus": [x_star, y_star],
            "tau_maass_w5_partner": [float(tau_maass_w5.real), float(tau_maass_w5.imag)],
            "rho1_max": rho_star,
            "relative_gap_to_second_orbit": rel_gap,
            "local_max_orbits_found": local_max_orbits[:6],
            "peak_locus": peak_locus,
            "X0_5_orbit_size": x0_orbit_size,
            "X1_5_orbit_size": x1_orbit_size,
            "breaks_mirror_cp_Re_not_half_Z": breaks_mirror_cp,
        },
        "first_10_newform_clusters": public_clusters,
        "_tau_maass": tau_maass,
        "_tau_maass_w5": tau_maass_w5,
    }

def evaluate_fr_fib_structural_census_at_tau(
    label: str, tau_val: complex, winning_sheet: List[int]
) -> Dict[str, Any]:
    """Evaluates FR-FIB across all 24 lines x 2 horocycles x 2 covariant readings at tau_val (strictly data-free),
    using exact SL_2(Z) reduction (B1667 + B1724) when tau_val lies outside F_{SL_2(Z)}."""
    tau_red, gamma_sl2z = reduce_to_sl2z_fundamental_domain(tau_val)
    a_g, b_g, c_g, d_g = gamma_sl2z
    cusp_geom = solve_cusp_radii_for_tau(tau_red)
    Ls = {"L_max": cusp_geom["L_max"], "L_2": cusp_geom["L_2"]}
    lines_24 = build_24_level5_and_spin10_lines()
    covariant_readings = (
        ("St_S_S", ("St", "S", "S")),
        ("S_S_S", ("S", "S", "S")),
    )

    configs: List[Dict[str, Any]] = []
    passing_s_decade: List[Dict[str, Any]] = []
    passing_h4_joint: List[Dict[str, Any]] = []
    winning_sheet_records: List[Dict[str, Any]] = []

    rng = np.random.default_rng(1881)
    max_haar_err_checked = 0.0

    for ln_idx, ln in enumerate(lines_24):
        a_red = (ln["a"] * d_g - ln["b"] * c_g) % 1
        b_red = (-ln["a"] * b_g + ln["b"] * a_g) % 1
        yuks = build_fr_fib_yukawas(tau_red, a_red, b_red, Ls)
        is_win_sheet = ln["sheet"] == winning_sheet
        for h_name in ("L_max", "L_2"):
            for rd_label, (r_up, r_dn, r_lp) in covariant_readings:
                Yu = yuks[("up", h_name, r_up)]
                Yd = yuks[("down", h_name, r_dn)]
                Ye = yuks[("lep", h_name, r_lp)]
                inv = extract_physical_invariants_from_yukawas(Yu, Yd, Ye)

                sp_u13, sp_u12 = _decade_spans(inv["ratios_up"])
                sp_d13, sp_d12 = _decade_spans(inv["ratios_down"])
                sp_e13, sp_e12 = _decade_spans(inv["ratios_lep"])

                min_span_13 = min(sp_u13, sp_d13, sp_e13)
                min_span_12 = min(sp_u12, sp_d12, sp_e12)
                max_span_13 = max(sp_u13, sp_d13, sp_e13)
                max_span_12 = max(sp_u12, sp_d12, sp_e12)

                clears_floor = (min_span_13 >= 2.5) and (min_span_12 >= 1.0)
                clears_h4a = clears_floor and (max_span_13 <= 7.5) and (max_span_12 <= 4.5)
                clears_h4b = inv["abs_J"] > 1e-8
                clears_joint = clears_h4a and clears_h4b

                vub = inv["ckm_abs_vus_vcb_vub"][2]
                vtd = inv["ckm_abs_vtd"]
                corner_ratio = float(vub / vtd) if vtd > 1e-30 else None

                rec = {
                    "family": ln["family"],
                    "sheet": ln["sheet"],
                    "line": ln["label"],
                    "sl2z_reduced_line": f"({a_red}, {b_red})",
                    "horocycle": h_name,
                    "reading": rd_label,
                    "log10_s1_over_s3": {"up": sp_u13, "down": sp_d13, "lep": sp_e13},
                    "log10_s1_over_s2": {"up": sp_u12, "down": sp_d12, "lep": sp_e12},
                    "min_3sector_span_13": min_span_13,
                    "min_3sector_span_12": min_span_12,
                    "max_3sector_span_13": max_span_13,
                    "max_3sector_span_12": max_span_12,
                    "clears_S_DECADE": clears_floor,
                    "clears_H4a_bounded_S_DECADE": clears_h4a,
                    "clears_H4b_S_CP": clears_h4b,
                    "clears_H4_joint": clears_joint,
                    "ckm_abs_vus_vcb_vub": inv["ckm_abs_vus_vcb_vub"],
                    "ckm_corner_vub_over_vtd": corner_ratio,
                    "J": inv["J"],
                    "abs_J": inv["abs_J"],
                }
                configs.append(rec)
                if clears_floor:
                    passing_s_decade.append(rec)
                if clears_joint:
                    passing_h4_joint.append(rec)
                if is_win_sheet:
                    winning_sheet_records.append(rec)

                if is_win_sheet or clears_joint or ln_idx == 0:
                    UL_Q = random_haar_su3_u1(rng)
                    UR_u = random_haar_su3_u1(rng)
                    UR_d = random_haar_su3_u1(rng)
                    UL_L = random_haar_su3_u1(rng)
                    UR_e = random_haar_su3_u1(rng)
                    inv_scr = extract_physical_invariants_from_yukawas(
                        UL_Q @ Yu @ np.conj(UR_u.T),
                        UL_Q @ Yd @ np.conj(UR_d.T),
                        UL_L @ Ye @ np.conj(UR_e.T),
                    )
                    max_haar_err_checked = max(
                        max_haar_err_checked,
                        max(abs(a - b) for a, b in zip(inv["ratios_up"], inv_scr["ratios_up"])),
                        max(abs(a - b) for a, b in zip(inv["ratios_down"], inv_scr["ratios_down"])),
                        max(abs(a - b) for a, b in zip(inv["ratios_lep"], inv_scr["ratios_lep"])),
                        abs(inv["abs_J"] - inv_scr["abs_J"]),
                    )

    best_by_joint_span = max(configs, key=lambda r: min(r["min_3sector_span_13"] / 2.5, r["min_3sector_span_12"] / 1.0))
    max_abs_J_all = max(r["abs_J"] for r in configs)
    max_abs_J_winning = max((r["abs_J"] for r in winning_sheet_records), default=0.0)
    min_abs_J_winning = min((r["abs_J"] for r in winning_sheet_records), default=0.0)

    return {
        "label": label,
        "tau_input": [float(tau_val.real), float(tau_val.imag)],
        "tau_sl2z_reduced": [float(tau_red.real), float(tau_red.imag)],
        "sl2z_reduction_matrix": list(gamma_sl2z),
        "exact_cusp_geometry": cusp_geom,
        "total_configurations_tested": len(configs),
        "passing_S_DECADE_count": len(passing_s_decade),
        "passing_H4a_bounded_S_DECADE_count": sum(1 for r in configs if r["clears_H4a_bounded_S_DECADE"]),
        "passing_H4b_S_CP_count": sum(1 for r in configs if r["clears_H4b_S_CP"]),
        "passing_H4_joint_count": len(passing_h4_joint),
        "holds_S_DECADE": len(passing_s_decade) >= 1,
        "holds_H4_joint": len(passing_h4_joint) >= 1,
        "max_abs_J_across_96": max_abs_J_all,
        "haar_scrambling_max_err": max_haar_err_checked,
        "winning_sheet": winning_sheet,
        "winning_sheet_max_abs_J": max_abs_J_winning,
        "winning_sheet_min_abs_J": min_abs_J_winning,
        "holds_S_CP_gt_1e8_on_winning_sheet": max_abs_J_winning > 1e-8,
        "winning_sheet_records": winning_sheet_records,
        "best_configuration_by_balanced_span": best_by_joint_span,
        "passing_H4_joint_configurations": passing_h4_joint,
    }


def _json_default(obj: Any) -> Any:
    if isinstance(obj, np.bool_):
        return bool(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def run_all(write_json: bool = False) -> Dict[str, Any]:
    t0 = time.time()
    c0 = run_cell_c0_controls()
    if not c0["holds"]:
        out_void = {
            "arc": "B1881",
            "verdict_by_rule": "OPEN (INSTRUMENT VOID -- Cell C0 failed)",
            "elapsed_sec": round(time.time() - t0, 2),
            "C0": c0,
        }
        if write_json:
            OUT_JSON.write_text(json.dumps(out_void, indent=2, default=_json_default) + "\n", encoding="utf-8")
        return out_void

    c1 = run_cell_c1_schreier_and_galois()
    c2 = run_cell_c2_mayer_selberg()
    c3_raw = run_cell_c3_ray_singer_torsion()
    c4_raw = run_cell_c4_p776_twin_odd_maass()

    tau_k1 = c3_raw.pop("_tau0_star_n5")
    tau_k2 = c3_raw.pop("_tau0_kappa2_n5")
    win_k1 = c3_raw.pop("_winning_sheet_k1")
    win_k2 = c3_raw.pop("_winning_sheet_k2")

    tau_maass = c4_raw.pop("_tau_maass")
    tau_maass_w5 = c4_raw.pop("_tau_maass_w5")

    h1_census = evaluate_fr_fib_structural_census_at_tau("kappa1_O_plus_L1_5", tau_k1, win_k1)
    h2_census = evaluate_fr_fib_structural_census_at_tau("kappa2_twin_symmetric_O_plus_L1_5_plus_Lm1_5", tau_k2, win_k2)
    h3 = {
        "holds": h1_census["holds_S_CP_gt_1e8_on_winning_sheet"] and (not h2_census["holds_S_CP_gt_1e8_on_winning_sheet"]),
        "H3a_kappa1_CP_broken_gt_1e8": h1_census["holds_S_CP_gt_1e8_on_winning_sheet"],
        "H3a_kappa1_winning_sheet_max_abs_J": h1_census["winning_sheet_max_abs_J"],
        "H3b_kappa2_CP_broken_gt_1e8": h2_census["holds_S_CP_gt_1e8_on_winning_sheet"],
        "H3b_kappa2_winning_sheet_max_abs_J": h2_census["winning_sheet_max_abs_J"],
    }

    h4_fplus = evaluate_fr_fib_structural_census_at_tau("P776_Maass_peak_Fplus", tau_maass, [1, 2])
    h4_w5 = evaluate_fr_fib_structural_census_at_tau("P776_Maass_peak_W5_partner", tau_maass_w5, [1, 2])
    h4_holds = (
        (h4_fplus["holds_H4_joint"] or h4_w5["holds_H4_joint"])
        and (h4_fplus["haar_scrambling_max_err"] < 1e-12)
        and (h4_w5["haar_scrambling_max_err"] < 1e-12)
    )
    h4 = {
        "holds_H4_joint": h4_holds,
        "total_joint_passing_configs_across_orbit": h4_fplus["passing_H4_joint_count"] + h4_w5["passing_H4_joint_count"],
        "fplus_representative": h4_fplus,
        "w5_partner_representative": h4_w5,
    }

    math_and_orbit_pass = c0["holds"] and c1["holds"] and c2["holds"] and c3_raw["holds"] and c4_raw["holds"]
    if not math_and_orbit_pass:
        verdict = "NEGATIVE as sealed (a mathematical or P-776 orbit uniqueness cell C1-C4 failed)"
    elif h4_holds:
        verdict = (
            "PROVED as sealed (C0-C4 hold and P-776 Maass peak orbit clears H4a+H4b, "
            "conditional on stated choices: level=5, mark, hyperbolic clock, twin-odd sector, H=I)"
        )
    else:
        verdict = (
            "NEGATIVE as sealed for closing the FR-FIB hierarchy+CP loop at the P-776 Maass peak orbit "
            "(C0-C4 whole-subweave & P-776 twin-odd Maass symmetry/orbit theorems PROVED; H4 fails)"
        )

    result = {
        "arc": "B1881",
        "date": "2026-11-11",
        "data_free": "0 of 19 (zero PDG targets or D11/P-709 values read)",
        "verdict_by_rule": verdict,
        "elapsed_sec": round(time.time() - t0, 2),
        "C0": c0,
        "C1": c1,
        "C2": c2,
        "C3": c3_raw,
        "C4_P776_twin_odd_maass": c4_raw,
        "H1_kappa1_hierarchy": h1_census,
        "H2_kappa2_hierarchy": h2_census,
        "H3_ray_singer_cp_bracket": h3,
        "H4_P776_maass_fr_fib_test": h4,
    }
    if write_json:
        OUT_JSON.write_text(json.dumps(result, indent=2, default=_json_default) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="B1881 sealed P-776 twin-odd Maass & FR-FIB structural hierarchy test.")
    parser.add_argument("--write", action="store_true", help="Write subweave_p776_and_hierarchy.json beside this script.")
    args = parser.parse_args()

    res = run_all(write_json=args.write)
    print(f"B1881 complete in {res['elapsed_sec']}s")
    print("  C0 (controls, SL2Z Hejhal benchmark & Haar):", "PASS" if res["C0"]["holds"] else "FAIL")
    if "C4_P776_twin_odd_maass" in res:
        c4 = res["C4_P776_twin_odd_maass"]
        gs = c4["ground_state"]
        pk = c4["peak_orbit"]
        print("  C1 (Schreier +-Gamma_1(5) & Galois):", "PASS" if res["C1"]["holds"] else "FAIL")
        print("  C2 (R10-A Mayer-Selberg N=2..11):", "PASS" if res["C2"]["holds"] else "FAIL")
        print("  C3 (R10-B/C1/C2 Ray-Singer torsion):", "PASS" if res["C3"]["holds"] else "FAIL")
        print(
            f"  C4 (P-776 Twin-Odd Maass): {'PASS' if c4['holds'] else 'FAIL'} | "
            f"ground R_1={gs['R']:.12f} (lambda_1={gs['lambda']:.12f}, {gs['class_label']}, eps_J={gs['eps_J']}, dim={gs['dim_R']}) | "
            f"peak={pk['tau_maass_fplus']} ({pk['peak_locus']}, X0(5) orbit={pk['X0_5_orbit_size']}, X1(5) orbit={pk['X1_5_orbit_size']})"
        )
        h4 = res["H4_P776_maass_fr_fib_test"]
        f_rep = h4["fplus_representative"]
        w_rep = h4["w5_partner_representative"]
        print(
            f"  H4 (FR-FIB at P-776 orbit): {'PASS' if h4['holds_H4_joint'] else 'FAIL'} | "
            f"F+ joint={f_rep['passing_H4_joint_count']}/96 (best min13={f_rep['best_configuration_by_balanced_span']['min_3sector_span_13']:.3f}, max|J|={f_rep['max_abs_J_across_96']:.2e}) | "
            f"W5 joint={w_rep['passing_H4_joint_count']}/96 (best min13={w_rep['best_configuration_by_balanced_span']['min_3sector_span_13']:.3f}, max|J|={w_rep['max_abs_J_across_96']:.2e})"
        )
    print("  Verdict:", res["verdict_by_rule"])


if __name__ == "__main__":
    main()
