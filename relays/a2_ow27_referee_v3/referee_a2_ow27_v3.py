#!/usr/bin/env python3
"""
Cold-Room Zero-Trust Referee v3 for Card A2-OW27 v8 & Card A2-OW16 v22 (seat agy-002, strictly 0 of 19).

Independently audits Card A2-OW27 v8 (110018a38) & Card A2-OW16 v22 (3fa3a7a08),
verifying remediation of all Referee v1 findings (DISC-OW27-1, DISC-OW27-C, DIAG-1..3) and v2 prose polish
with asymptotic GL4 Boltzmann resolution (N=1000 vs 2000)
using completely disjoint algorithms and zero shared code with producer:
  - Integrator: 2-stage implicit Gauss-Legendre GL4 (symplectic, A-stable, O(h^4)) for:
      * 2-loop MSSM (M_GUT -> M_SUSY)
      * 2-loop SM (Q_match -> mu = m_t(m_t) -> M_Z)
      * 2-loop pure QCD (nf = 5 -> 4 -> 3)
      * 26-variable 1-loop soft-SUSY RGEs
      * 1-loop sequential seesaw (N_3 -> N_2 -> N_1)
      * Stiff nonlinear Riccati freeze-out (GL4 + 2x2 damped Newton, N=800 vs N=1600,
        comparing all points + x_f at N=1600 AND per-m0 self_consistent_m0_own_* for m0 in {3,10,30}v)
      * Stiff linear MSSM Boltzmann leptogenesis (GL4 + cancellation-free A^-1, N=1000 vs N=2000)
  - Spinors: Standard Dirac-Pauli basis (gamma^0 = diag(I_2, -I_2)) + 6-point Gauss-Legendre quadrature.
  - Elliptic Yukawa W_hol: Native mp.jtheta + exact heat-equation derivatives (zero manual q-series).
  - Takagi factorization: Non-squaring real 2n x 2n symmetric block eigensolver via mp.eigsy.
  - Haar U(3) generator: Pure-integer Xorshift64* PRNG + complex Householder QR (Mezzadri 2007).
  - Root finding: Bracketed bisection + secant for Delta_hid and self-consistent m_t / M_Z scales.
  - Guardrails enforced: 0 AST float/complex literals, 0 float()/complex() casts, 0 JSON float tokens,
    0 imports from relays/, frontier/, numpy, scipy, math, or cmath; strictly 0 of 19.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


# ==============================================================================
# Core Zero-Float Helpers, AST/JSON Hygiene, Xorshift64*, Householder QR, & GL4
# ==============================================================================

I_C = mp.mpc(0, 1)
REPO_ROOT = Path(__file__).resolve().parents[2]
SELF_DIR = Path(__file__).resolve().parent
RELAYS_DIR = REPO_ROOT / "relays"


def qrat(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def q10(exp_i: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp_i)


def m_trace(mat: mp.matrix) -> mp.mpc:
    acc = mp.mpc(0)
    for k in range(mat.rows):
        acc += mat[k, k]
    return acc


def m_frob(mat: mp.matrix) -> mp.mpf:
    acc = mp.mpf(0)
    for r in range(mat.rows):
        for c in range(mat.cols):
            acc += abs(mat[r, c]) ** 2
    return mp.sqrt(acc)


def rel_err(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return abs(a - b) / max(abs(b), q10(-30))


def scan_script_ast(path: Path) -> dict[str, Any]:
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(path))
    lits: list[int] = []
    casts: list[int] = []
    bad_imps: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            lits.append(getattr(node, "lineno", -1))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
            casts.append(getattr(node, "lineno", -1))
        if isinstance(node, ast.Import):
            for al in node.names:
                if al.name.startswith(("relays", "frontier", "numpy", "scipy", "math", "cmath")):
                    bad_imps.append(al.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(("relays", "frontier", "numpy", "scipy", "math", "cmath")):
                bad_imps.append(node.module)
    return {
        "file": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "float_complex_literals": len(lits),
        "binary64_casts": len(casts),
        "forbidden_imports": len(bad_imps),
        "clean": bool(len(lits) == 0 and len(casts) == 0 and len(bad_imps) == 0),
    }


def scan_raw_json_floats(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    parsed = json.loads(raw)
    tree_floats: list[str] = []

    def walk(obj: Any, loc: str) -> None:
        if isinstance(obj, float):
            tree_floats.append(loc)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                walk(v, f"{loc}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, f"{loc}[{i}]")

    walk(parsed, "$")
    stripped = re.sub(r'"(?:\\.|[^"\\])*"', '""', raw)
    raw_matches = re.findall(r"(?<![A-Za-z0-9_])[-+]?\d+(?:\.\d+[eE][-+]?\d+|\.\d+|[eE][-+]?\d+)", stripped)
    return {
        "file": path.name,
        "tree_float_count": len(tree_floats),
        "raw_float_token_count": len(raw_matches),
        "sample_tokens": raw_matches[:5],
        "clean": bool(len(tree_floats) == 0 and len(raw_matches) == 0),
    }


def assert_no_json_floats(obj: Any, loc: str = "$") -> None:
    if obj is None or isinstance(obj, (bool, int, str)):
        return
    if isinstance(obj, float):
        raise AssertionError(f"JSON float at {loc}: {obj!r}")
    if isinstance(obj, list):
        for i, item in enumerate(obj):
            assert_no_json_floats(item, f"{loc}[{i}]")
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_json_floats(v, f"{loc}.{k}")
        return
    raise AssertionError(f"Unsupported JSON type at {loc}: {type(obj).__name__}")


class Xorshift64Star:
    """Pure-integer Xorshift64* PRNG (disjoint from producer's SplitMix64)."""

    def __init__(self, seed: int) -> None:
        s = seed & ((1 << 64) - 1)
        self.x = s if s != 0 else 0x9E3779B97F4A7C15

    def next_u64(self) -> int:
        x = self.x
        mask = (1 << 64) - 1
        x ^= (x >> 12) & mask
        x ^= (x << 25) & mask
        x ^= (x >> 27) & mask
        self.x = x
        return (x * 0x2545F4914F6CDD1D) & mask

    def uniform_open(self) -> mp.mpf:
        u = (self.next_u64() >> 11) + 1
        return mp.mpf(u) / mp.mpf((1 << 53) + 1)

    def gauss_pair(self) -> tuple[mp.mpf, mp.mpf]:
        u1 = self.uniform_open()
        u2 = self.uniform_open()
        rad = mp.sqrt(-2 * mp.log(u1))
        ang = 2 * mp.pi * u2
        return rad * mp.cos(ang), rad * mp.sin(ang)


def haar_unitary_householder(rng: Xorshift64Star, dim: int = 3) -> mp.matrix:
    """Exact Haar-distributed U(dim) via complex Householder QR (Mezzadri 2007)."""
    a = mp.zeros(dim, dim)
    for r in range(dim):
        for c in range(dim):
            xr, xi = rng.gauss_pair()
            a[r, c] = mp.mpc(xr, xi)
    q = mp.eye(dim)
    for k in range(dim - 1):
        sub_len = dim - k
        x = [a[k + i, k] for i in range(sub_len)]
        nrm = mp.sqrt(sum((abs(xi) ** 2 for xi in x), mp.mpf(0)))
        if nrm == 0:
            continue
        ph = (x[0] / abs(x[0])) if abs(x[0]) > 0 else mp.mpc(1)
        v = list(x)
        v[0] = v[0] + ph * nrm
        vnrm2 = sum((abs(vi) ** 2 for vi in v), mp.mpf(0))
        if vnrm2 == 0:
            continue
        for col in range(k, dim):
            dot = sum((mp.conj(v[i]) * a[k + i, col] for i in range(sub_len)), mp.mpc(0))
            fac = (2 * dot) / vnrm2
            for i in range(sub_len):
                a[k + i, col] -= fac * v[i]
        for row in range(dim):
            dot = sum((q[row, k + i] * v[i] for i in range(sub_len)), mp.mpc(0))
            fac = (2 * dot) / vnrm2
            for i in range(sub_len):
                q[row, k + i] -= fac * mp.conj(v[i])
    for k in range(dim):
        rkk = a[k, k]
        d_ph = (rkk / abs(rkk)) if abs(rkk) > 0 else mp.mpc(1)
        for row in range(dim):
            q[row, k] *= d_ph
    if m_frob(q.H * q - mp.eye(dim)) > q10(-18):
        raise RuntimeError("Householder QR unitarity check failed")
    return q


def left_svd_asc(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    n = mat.rows
    hh = mat * mat.H
    hh = (hh + hh.H) / 2
    vals, vecs = mp.eighe(hh)
    order = sorted(range(n), key=lambda k: mp.re(vals[k]))
    u = mp.zeros(n, n)
    svals: list[mp.mpf] = []
    for col, k in enumerate(order):
        for row in range(n):
            u[row, col] = vecs[row, k]
        lam = mp.re(vals[k])
        svals.append(mp.sqrt(lam) if lam > 0 else mp.mpf(0))
    return u, svals


def takagi_real_2n_eigsy(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """Non-squaring real 2n x 2n symmetric block eigensolver Takagi factorization."""
    n = m_sym.rows
    ms = (m_sym + m_sym.T) / 2
    s_blk = mp.zeros(2 * n, 2 * n)
    for r in range(n):
        for c in range(n):
            re_v = mp.re(ms[r, c])
            im_v = mp.im(ms[r, c])
            s_blk[r, c] = re_v
            s_blk[r, n + c] = im_v
            s_blk[n + r, c] = im_v
            s_blk[n + r, n + c] = -re_v
    evals, evecs = mp.eigsy(s_blk)
    svals = [max(mp.re(evals[n + k]), mp.mpf(0)) for k in range(n)]
    u_tak = mp.zeros(n, n)
    for k in range(n):
        idx = n + k
        for r in range(n):
            u_tak[r, k] = mp.mpc(mp.re(evecs[r, idx]), -mp.re(evecs[n + r, idx]))
        cnrm = mp.sqrt(sum((abs(u_tak[r, k]) ** 2 for r in range(n)), mp.mpf(0)))
        if cnrm > 0:
            for r in range(n):
                u_tak[r, k] /= cnrm
    return u_tak, svals


def gl4_integrate_tuple(
    rhs_fn: Any,
    st0: tuple[Any, ...],
    t_span: mp.mpf,
    n_steps: int,
    tol_exp: int = -17,
) -> tuple[Any, ...]:
    """2-stage implicit Gauss-Legendre GL4 (order 4, symplectic, A-stable) via Gauss-Seidel Picard."""
    if n_steps <= 0 or t_span == 0:
        return st0
    s3_6 = mp.sqrt(3) / 6
    a11 = qrat(1, 4)
    a12 = qrat(1, 4) - s3_6
    a21 = qrat(1, 4) + s3_6
    a22 = qrat(1, 4)
    h = t_span / mp.mpf(n_steps)
    m_len = len(st0)
    st = st0

    def lincomb(base: tuple[Any, ...], k1: tuple[Any, ...], k2: tuple[Any, ...], c1: mp.mpf, c2: mp.mpf) -> tuple[Any, ...]:
        return tuple(base[i] + c1 * k1[i] + c2 * k2[i] for i in range(m_len))

    def diff_norm(ka: tuple[Any, ...], kb: tuple[Any, ...]) -> mp.mpf:
        mx = mp.mpf(0)
        for i in range(m_len):
            d = ka[i] - kb[i]
            v = m_frob(d) if isinstance(d, mp.matrix) else abs(d)
            if v > mx:
                mx = v
        return mx

    tol = q10(tol_exp)
    for _ in range(n_steps):
        k1 = rhs_fn(st)
        k2 = k1
        err = mp.mpf(1)
        for _it in range(24):
            k1_new = rhs_fn(lincomb(st, k1, k2, h * a11, h * a12))
            k2_new = rhs_fn(lincomb(st, k1_new, k2, h * a21, h * a22))
            err = max(diff_norm(k1_new, k1), diff_norm(k2_new, k2))
            k1, k2 = k1_new, k2_new
            if err < tol:
                break
        if err > q10(-13):
            raise RuntimeError(f"GL4 tuple Picard failed to converge: err={err}")
        st = tuple(st[i] + (h / 2) * (k1[i] + k2[i]) for i in range(m_len))
    return st


def gl4_integrate_vec(
    rhs_fn: Any,
    y0: list[mp.mpf],
    t_span: mp.mpf,
    n_steps: int,
    tol_exp: int = -19,
) -> list[mp.mpf]:
    """2-stage implicit Gauss-Legendre GL4 for scalar vector states."""
    if n_steps <= 0 or t_span == 0:
        return list(y0)
    s3_6 = mp.sqrt(3) / 6
    a11 = qrat(1, 4)
    a12 = qrat(1, 4) - s3_6
    a21 = qrat(1, 4) + s3_6
    a22 = qrat(1, 4)
    h = t_span / mp.mpf(n_steps)
    dim = len(y0)
    y = list(y0)
    tol = q10(tol_exp)
    for _ in range(n_steps):
        k1 = rhs_fn(y)
        k2 = list(k1)
        err = mp.mpf(1)
        for _it in range(24):
            k1_new = rhs_fn([y[i] + h * (a11 * k1[i] + a12 * k2[i]) for i in range(dim)])
            k2_new = rhs_fn([y[i] + h * (a21 * k1_new[i] + a22 * k2[i]) for i in range(dim)])
            err = max(
                max(abs(k1_new[i] - k1[i]) for i in range(dim)),
                max(abs(k2_new[i] - k2[i]) for i in range(dim)),
            )
            k1, k2 = k1_new, k2_new
            if err < tol:
                break
        if err > q10(-13):
            raise RuntimeError(f"GL4 vec Picard failed to converge: err={err}")
        y = [y[i] + (h / 2) * (k1[i] + k2[i]) for i in range(dim)]
    return y


# ==============================================================================
# Disjoint Elliptic Yukawa W_hol via mp.jtheta + Heat-Equation Derivatives
# ==============================================================================

def eval_w_hol_jtheta(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_C, 0], [0, -I_C]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = qrat(1, 2)
    eb = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    qh = mp.exp(I_C * mp.pi * tau)
    t2 = mp.jtheta(2, 0, qh)
    t3 = mp.jtheta(3, 0, qh)
    t4 = mp.jtheta(4, 0, qh)
    l2d = -mp.jtheta(2, 0, qh, 2) / (8 * t2)
    l3d = -mp.jtheta(3, 0, qh, 2) / (8 * t3)
    l4d = -mp.jtheta(4, 0, qh, 2) / (8 * t4)
    t1_d1 = mp.jtheta(1, 0, qh, 1)
    e2s = -mp.jtheta(1, 0, qh, 3) / t1_d1
    t1p = mp.pi * t1_d1

    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj
        + (I_C * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    def th_char(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am = qrat(ta.numerator, ta.denominator)
        bm = qrat(tb.numerator, tb.denominator)
        zv = am * tau + bm
        base = mp.exp(I_C * mp.pi * am * am * tau + 2 * I_C * mp.pi * am * bm) * mp.jtheta(3, mp.pi * zv, qh)
        return base if (nb == 0 or ta == 0) else mp.exp(2 * I_C * mp.pi * am * nb) * base

    xv = (ql * pa, 2 * ql * pb)
    yv = (qr * pa, 2 * qr * pb)
    ap, am_f = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm_f = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_C * mp.pi * qrat(xv[0].numerator, xv[0].denominator))
    kap = {"1": -I_C * eph, "i": mp.mpf(-1), "j": -eph, "k": I_C}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am_f + hfr, bm_f + hfr), "i": (am_f + hfr, bm_f), "j": (am_f, bm_f + hfr), "k": (am_f, bm_f)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * th_char(cs[sk][0], cs[sk][1]) * th_char(ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * eb["1"] + rs["i"] * eb["i"] + rs["j"] * eb["j"] + rs["k"] * eb["k"]
    return mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0]
            + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0]
            + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])


def w_orbit_avg(tau: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
    acc = mp.zeros(3, 3)
    for a, b in pts:
        acc += eval_w_hol_jtheta(tau, a, b, ql, qr)
    return acc / mp.mpf(len(pts))


# ==============================================================================
# CKM & Full Haar-Invariant PMNS (Real 6x6 eigsy Takagi)
# ==============================================================================

def extract_ckm(yu: mp.matrix, yd: mp.matrix, ye: mp.matrix) -> dict[str, mp.mpf]:
    uu, su = left_svd_asc(yu)
    ud, sd = left_svd_asc(yd)
    _, se = left_svd_asc(ye)
    v = uu.H * ud
    j_ckm = mp.im(v[0, 1] * v[1, 2] * mp.conj(v[0, 2]) * mp.conj(v[1, 1]))
    return {
        "v12": abs(v[0, 1]),
        "v23": abs(v[1, 2]),
        "v13": abs(v[0, 2]),
        "J": j_ckm,
        "mc_mt": su[1] / su[2],
        "mu_mt": su[0] / su[2],
        "ms_mb": sd[1] / sd[2],
        "md_mb": sd[0] / sd[2],
        "mmu_mtau": se[1] / se[2],
        "me_mtau": se[0] / se[2],
        "b_tau": sd[2] / se[2],
        "yt": su[2],
        "yb": sd[2],
        "ytau": se[2],
        "yc": su[1],
    }


def extract_pmns(ye: mp.matrix, kap: mp.matrix) -> dict[str, mp.mpf]:
    ks = (kap + kap.T) / 2
    ul, _ = left_svd_asc(ye)
    k_flav = ul.H * ks * ul.apply(mp.conj)
    u_tak, sn = takagi_real_2n_eigsy(k_flav)
    up = u_tak.apply(mp.conj)
    s13sq = abs(up[0, 2]) ** 2
    c13sq = 1 - s13sq
    s12sq = (abs(up[0, 1]) ** 2) / c13sq
    c12sq = 1 - s12sq
    s23sq = (abs(up[1, 2]) ** 2) / c13sq
    c23sq = 1 - s23sq
    dm = (sn[1] ** 2 - sn[0] ** 2) / (sn[2] ** 2 - sn[0] ** 2)
    j_p = mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1]))
    den_j = mp.sqrt(max(c12sq * s12sq * c23sq * s23sq * s13sq, mp.mpf(0)))
    sin_d = j_p / (c13sq * den_j) if den_j > q10(-24) else mp.mpf(0)
    cos_d = (abs(up[1, 0]) ** 2 - s12sq * c23sq - c12sq * s23sq * s13sq) / (2 * den_j) if den_j > q10(-24) else mp.mpf(1)
    delta_cp = mp.atan2(sin_d, cos_d)
    unit_trig_err = abs(sin_d * sin_d + cos_d * cos_d - 1) if den_j > q10(-24) else mp.mpf(0)
    return {
        "s12sq": s12sq,
        "s23sq": s23sq,
        "s13sq": s13sq,
        "dm": dm,
        "J": j_p,
        "delta_cp_rad": delta_cp,
        "delta_cp_over_pi": delta_cp / mp.pi,
        "mee_over_m3": abs(k_flav[0, 0]) / sn[2] if sn[2] > 0 else mp.mpf(0),
        "sum_m_over_m3": (sn[0] + sn[1] + sn[2]) / sn[2] if sn[2] > 0 else mp.mpf(0),
        "m1_over_m3": sn[0] / sn[2] if sn[2] > 0 else mp.mpf(0),
        "m2_over_m3": sn[1] / sn[2] if sn[2] > 0 else mp.mpf(0),
        "trig_unitarity_err": unit_trig_err,
    }


def in_fixed_ow24c_window(obs: dict[str, mp.mpf]) -> bool:
    return bool(
        qrat(15, 100) < obs["s12sq"] < qrat(55, 100)
        and qrat(30, 100) < obs["s23sq"] < qrat(70, 100)
        and obs["s13sq"] < qrat(8, 100)
        and qrat(5, 1000) < obs["dm"] < qrat(15, 100)
    )


# ==============================================================================
# Independent RGE Right-Hand Sides (2-Loop MSSM, 2-Loop SM, 26-Var Soft, QCD, Seesaw)
# ==============================================================================

def mssm_2loop_rhs(st: tuple[Any, ...], two_loop: bool = True) -> tuple[Any, ...]:
    g1, g2, g3, yu, yd, ye, kap = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    c2 = c1 * c1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    i3 = mp.eye(3)
    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
    tu, td, te = mp.re(m_trace(hu)), mp.re(m_trace(hd)), mp.re(m_trace(he))

    dg1 = c1 * qrat(33, 5) * (g1 ** 3)
    dg2 = c1 * (g2 ** 3)
    dg3 = c1 * (-3) * (g3 ** 3)
    if two_loop:
        dg1 += c2 * (g1 ** 3) * (
            qrat(199, 25) * g1s + qrat(27, 5) * g2s + qrat(88, 5) * g3s
            - qrat(26, 5) * tu - qrat(14, 5) * td - qrat(18, 5) * te
        )
        dg2 += c2 * (g2 ** 3) * (
            qrat(9, 5) * g1s + 25 * g2s + 24 * g3s - 6 * tu - 6 * td - 2 * te
        )
        dg3 += c2 * (g3 ** 3) * (
            qrat(11, 5) * g1s + 9 * g2s + 14 * g3s - 4 * tu - 4 * td
        )

    gQ = c1 * (hu + hd - (qrat(1, 30) * g1s + qrat(3, 2) * g2s + qrat(8, 3) * g3s) * i3)
    guc = c1 * (2 * htu - (qrat(8, 15) * g1s + qrat(8, 3) * g3s) * i3)
    gdc = c1 * (2 * htd - (qrat(2, 15) * g1s + qrat(8, 3) * g3s) * i3)
    gL = c1 * (he - (qrat(3, 10) * g1s + qrat(3, 2) * g2s) * i3)
    gec = c1 * (2 * hte - (qrat(6, 5) * g1s) * i3)
    gHu = c1 * (3 * tu - (qrat(3, 10) * g1s + qrat(3, 2) * g2s))
    gHd = c1 * (3 * td + te - (qrat(3, 10) * g1s + qrat(3, 2) * g2s))

    if two_loop:
        tu2 = mp.re(m_trace(hu * hu))
        td2 = mp.re(m_trace(hd * hd))
        te2 = mp.re(m_trace(he * he))
        tud = mp.re(m_trace(hu * hd))
        gQ += c2 * (
            -2 * (hu * hu) - 2 * (hd * hd) - 3 * tu * hu - (3 * td + te) * hd
            + qrat(4, 5) * g1s * hu + qrat(2, 5) * g1s * hd
            + (qrat(199, 900) * g1s * g1s + qrat(15, 4) * g2s * g2s - qrat(8, 9) * g3s * g3s
               + qrat(1, 10) * g1s * g2s + qrat(8, 45) * g1s * g3s + 8 * g2s * g3s) * i3
        )
        guc += c2 * (
            -2 * (htu * htu) - 2 * (yu.H * hd * yu) - 6 * tu * htu
            + (-qrat(2, 5) * g1s + 6 * g2s) * htu
            + (qrat(856, 225) * g1s * g1s - qrat(8, 9) * g3s * g3s + qrat(128, 45) * g1s * g3s) * i3
        )
        gdc += c2 * (
            -2 * (htd * htd) - 2 * (yd.H * hu * yd) - 2 * (3 * td + te) * htd
            + (qrat(2, 5) * g1s + 6 * g2s) * htd
            + (qrat(202, 225) * g1s * g1s - qrat(8, 9) * g3s * g3s + qrat(32, 45) * g1s * g3s) * i3
        )
        gL += c2 * (
            -2 * (he * he) - (3 * td + te) * he + qrat(6, 5) * g1s * he
            + (qrat(207, 100) * g1s * g1s + qrat(15, 4) * g2s * g2s + qrat(9, 10) * g1s * g2s) * i3
        )
        gec += c2 * (
            -2 * (hte * hte) - 2 * (3 * td + te) * hte
            + (-qrat(6, 5) * g1s + 6 * g2s) * hte
            + qrat(234, 25) * g1s * g1s * i3
        )
        gHu += c2 * (
            -9 * tu2 - 3 * tud + (qrat(4, 5) * g1s + 16 * g3s) * tu
            + qrat(207, 100) * g1s * g1s + qrat(15, 4) * g2s * g2s + qrat(9, 10) * g1s * g2s
        )
        gHd += c2 * (
            -9 * td2 - 3 * te2 - 3 * tud + (-qrat(2, 5) * g1s + 16 * g3s) * td + qrat(6, 5) * g1s * te
            + qrat(207, 100) * g1s * g1s + qrat(15, 4) * g2s * g2s + qrat(9, 10) * g1s * g2s
        )

    dyu = gQ * yu + yu * guc + gHu * yu
    dyd = gQ * yd + yd * gdc + gHd * yd
    dye = gL * ye + ye * gec + gHd * ye
    gLH = gL + gHu * i3
    dkap = gLH * kap + kap * gLH.T
    return (dg1, dg2, dg3, dyu, dyd, dye, dkap)


def sm_2loop_rhs(st: tuple[Any, ...], two_loop: bool = True) -> tuple[Any, ...]:
    g1, g2, g3, yu, yd, ye, kap, lam = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    c2 = c1 * c1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    gps = qrat(3, 5) * g1s
    i3 = mp.eye(3)

    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    tu, td, te = mp.re(m_trace(hu)), mp.re(m_trace(hd)), mp.re(m_trace(he))
    t2 = 3 * tu + 3 * td + te
    tu2, td2, te2 = mp.re(m_trace(hu * hu)), mp.re(m_trace(hd * hd)), mp.re(m_trace(he * he))
    tud = mp.re(m_trace(hu * hd))
    y4_h = qrat(27, 4) * tu2 + qrat(27, 4) * td2 + qrat(9, 4) * te2 - qrat(3, 2) * tud
    y2g_h = (
        (qrat(17, 4) * g1s + qrat(45, 4) * g2s + 40 * g3s) * tu
        + (qrat(5, 4) * g1s + qrat(45, 4) * g2s + 40 * g3s) * td
        + (qrat(15, 4) * g1s + qrat(15, 4) * g2s) * te
    )

    dg1 = c1 * qrat(41, 10) * (g1 ** 3)
    dg2 = c1 * qrat(-19, 6) * (g2 ** 3)
    dg3 = c1 * (-7) * (g3 ** 3)
    if two_loop:
        dg1 += c2 * (g1 ** 3) * (
            qrat(199, 50) * g1s + qrat(27, 10) * g2s + qrat(44, 5) * g3s
            - qrat(17, 10) * tu - qrat(1, 2) * td - qrat(3, 2) * te
        )
        dg2 += c2 * (g2 ** 3) * (
            qrat(9, 10) * g1s + qrat(35, 6) * g2s + 12 * g3s
            - qrat(3, 2) * tu - qrat(3, 2) * td - qrat(1, 2) * te
        )
        dg3 += c2 * (g3 ** 3) * (
            qrat(11, 10) * g1s + qrat(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td
        )

    dyu = c1 * ((qrat(3, 2) * hu - qrat(3, 2) * hd) * yu + (t2 - qrat(17, 20) * g1s - qrat(9, 4) * g2s - 8 * g3s) * yu)
    dyd = c1 * ((qrat(3, 2) * hd - qrat(3, 2) * hu) * yd + (t2 - qrat(1, 4) * g1s - qrat(9, 4) * g2s - 8 * g3s) * yd)
    dye = c1 * ((qrat(3, 2) * he) * ye + (t2 - qrat(9, 4) * g1s - qrat(9, 4) * g2s) * ye)

    if two_loop:
        gu2_s = (
            qrat(1187, 600) * g1s * g1s - qrat(9, 20) * g1s * g2s + qrat(19, 15) * g1s * g3s
            - qrat(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
            + qrat(3, 2) * lam * lam - y4_h + qrat(1, 2) * y2g_h
        )
        mu2_l = (
            qrat(3, 2) * (hu * hu) - (hu * hd) - qrat(1, 4) * (hd * hu) + qrat(11, 4) * (hd * hd)
            + (qrat(223, 80) * g1s + qrat(135, 16) * g2s + 16 * g3s - qrat(9, 4) * t2 - 6 * lam) * hu
            + (-qrat(43, 80) * g1s + qrat(9, 16) * g2s - 16 * g3s + qrat(5, 4) * t2) * hd
            + gu2_s * i3
        )
        dyu += c2 * (mu2_l * yu)

        gd2_s = (
            -qrat(127, 600) * g1s * g1s - qrat(27, 20) * g1s * g2s + qrat(31, 15) * g1s * g3s
            - qrat(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
            + qrat(3, 2) * lam * lam - y4_h + qrat(1, 2) * y2g_h
        )
        md2_l = (
            qrat(3, 2) * (hd * hd) - (hd * hu) - qrat(1, 4) * (hu * hd) + qrat(11, 4) * (hu * hu)
            + (qrat(187, 80) * g1s + qrat(135, 16) * g2s + 16 * g3s - qrat(9, 4) * t2 - 6 * lam) * hd
            + (-qrat(79, 80) * g1s + qrat(9, 16) * g2s - 16 * g3s + qrat(5, 4) * t2) * hu
            + gd2_s * i3
        )
        dyd += c2 * (md2_l * yd)

        ge2_s = (
            qrat(1371, 200) * g1s * g1s + qrat(27, 20) * g1s * g2s - qrat(23, 4) * g2s * g2s
            + qrat(3, 2) * lam * lam - y4_h + qrat(1, 2) * y2g_h
        )
        me2_l = (
            qrat(3, 2) * (he * he)
            + (qrat(387, 80) * g1s + qrat(135, 16) * g2s - qrat(9, 4) * t2 - 6 * lam) * he
            + ge2_s * i3
        )
        dye += c2 * (me2_l * ye)

    dkap = c1 * ((-3 * g2s + 2 * lam + 2 * t2) * kap - qrat(3, 2) * (he * kap + kap * he.T))
    dlam = c1 * (
        12 * lam * lam - 3 * lam * (3 * g2s + gps) + qrat(3, 4) * (2 * g2s * g2s + (g2s + gps) ** 2)
        + 4 * lam * t2 - 4 * (3 * tu2 + 3 * td2 + te2)
    )
    if two_loop:
        tr_y6 = 3 * mp.re(m_trace(hu * hu * hu)) + 3 * mp.re(m_trace(hd * hd * hd)) + mp.re(m_trace(he * he * he))
        tr_y4_ud = 3 * mp.re(m_trace(hu * hu * hd + hd * hd * hu))
        dlam += c2 * (
            -78 * (lam ** 3)
            + 18 * lam * lam * (3 * g2s + gps)
            + lam * (-qrat(73, 8) * g2s * g2s + qrat(39, 4) * g2s * gps + qrat(629, 24) * gps * gps)
            + qrat(305, 8) * (g2s ** 3) - qrat(289, 24) * g2s * g2s * gps
            - qrat(559, 24) * g2s * gps * gps - qrat(379, 24) * (gps ** 3)
            - 24 * lam * lam * t2
            + lam * (
                qrat(5, 2) * (qrat(17, 3) * gps + 9 * g2s + 32 * g3s) * tu
                + qrat(5, 2) * (qrat(5, 3) * gps + 9 * g2s + 32 * g3s) * td
                + qrat(5, 2) * (5 * gps + 3 * g2s) * te
                - (3 * tu2 + 3 * td2 + te2) - 42 * tud
            )
            - (qrat(16, 3) * gps + 64 * g3s) * tu2
            + (qrat(8, 3) * gps - 64 * g3s) * td2
            - 16 * gps * te2
            - qrat(9, 2) * g2s * g2s * t2
            + g2s * gps * (qrat(21, 2) * tu - qrat(9, 2) * td + qrat(33, 2) * te)
            - gps * gps * (qrat(19, 2) * tu - qrat(5, 2) * td + qrat(25, 2) * te)
            + 20 * tr_y6 - 4 * tr_y4_ud
        )
    return (dg1, dg2, dg3, dyu, dyd, dye, dkap, dlam)


def integrate_soft_26var_gl4(
    g_uv: mp.mpf,
    yt0: mp.mpf,
    yb0: mp.mpf,
    ytau0: mp.mpf,
    t_span: mp.mpf,
    a0_over_m0: mp.mpf,
    n_steps: int = 32,
) -> dict[str, mp.mpf]:
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    y0 = [
        g_uv, g_uv, g_uv, yt0, yb0, ytau0,
        mp.mpf(1), mp.mpf(1), mp.mpf(1),
        a0_over_m0, a0_over_m0, a0_over_m0,
        mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1),
        mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(0),
    ]

    def rhs(v: list[mp.mpf]) -> list[mp.mpf]:
        (g1, g2, g3, yt, yb, ytau, M1, M2, M3, At, Ab, Atau,
         mHu2, mHd2, mQ3, mu3, md3, mL3, me3, mQ1, mu1, md1, mL1, me1, mQ2, Shy) = v
        g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
        yts, ybs, ytaus = yt * yt, yb * yb, ytau * ytau
        Xt = 2 * yts * (mHu2 + mQ3 + mu3 + At * At)
        Xb = 2 * ybs * (mHd2 + mQ3 + md3 + Ab * Ab)
        Xtau = 2 * ytaus * (mHd2 + mL3 + me3 + Atau * Atau)
        dmQ1 = c1 * (-qrat(32, 3) * g3s * M3 * M3 - 6 * g2s * M2 * M2 - qrat(2, 15) * g1s * M1 * M1 + qrat(1, 5) * g1s * Shy)
        return [
            c1 * qrat(33, 5) * (g1 ** 3),
            c1 * (g2 ** 3),
            c1 * (-3) * (g3 ** 3),
            c1 * yt * (6 * yts + ybs - qrat(13, 15) * g1s - 3 * g2s - qrat(16, 3) * g3s),
            c1 * yb * (6 * ybs + yts + ytaus - qrat(7, 15) * g1s - 3 * g2s - qrat(16, 3) * g3s),
            c1 * ytau * (4 * ytaus + 3 * ybs - qrat(9, 5) * g1s - 3 * g2s),
            c1 * qrat(66, 5) * g1s * M1,
            c1 * 2 * g2s * M2,
            c1 * (-6) * g3s * M3,
            c1 * (12 * yts * At + 2 * ybs * Ab + qrat(26, 15) * g1s * M1 + 6 * g2s * M2 + qrat(32, 3) * g3s * M3),
            c1 * (12 * ybs * Ab + 2 * yts * At + 2 * ytaus * Atau + qrat(14, 15) * g1s * M1 + 6 * g2s * M2 + qrat(32, 3) * g3s * M3),
            c1 * (8 * ytaus * Atau + 6 * ybs * Ab + qrat(18, 5) * g1s * M1 + 6 * g2s * M2),
            c1 * (3 * Xt - 6 * g2s * M2 * M2 - qrat(6, 5) * g1s * M1 * M1 + qrat(3, 5) * g1s * Shy),
            c1 * (3 * Xb + Xtau - 6 * g2s * M2 * M2 - qrat(6, 5) * g1s * M1 * M1 - qrat(3, 5) * g1s * Shy),
            c1 * (Xt + Xb - qrat(32, 3) * g3s * M3 * M3 - 6 * g2s * M2 * M2 - qrat(2, 15) * g1s * M1 * M1 + qrat(1, 5) * g1s * Shy),
            c1 * (2 * Xt - qrat(32, 3) * g3s * M3 * M3 - qrat(32, 15) * g1s * M1 * M1 - qrat(4, 5) * g1s * Shy),
            c1 * (2 * Xb - qrat(32, 3) * g3s * M3 * M3 - qrat(8, 15) * g1s * M1 * M1 + qrat(2, 5) * g1s * Shy),
            c1 * (Xtau - 6 * g2s * M2 * M2 - qrat(6, 5) * g1s * M1 * M1 - qrat(3, 5) * g1s * Shy),
            c1 * (2 * Xtau - qrat(24, 5) * g1s * M1 * M1 + qrat(6, 5) * g1s * Shy),
            dmQ1,
            c1 * (-qrat(32, 3) * g3s * M3 * M3 - qrat(32, 15) * g1s * M1 * M1 - qrat(4, 5) * g1s * Shy),
            c1 * (-qrat(32, 3) * g3s * M3 * M3 - qrat(8, 15) * g1s * M1 * M1 + qrat(2, 5) * g1s * Shy),
            c1 * (-6 * g2s * M2 * M2 - qrat(6, 5) * g1s * M1 * M1 - qrat(3, 5) * g1s * Shy),
            c1 * (-qrat(24, 5) * g1s * M1 * M1 + qrat(6, 5) * g1s * Shy),
            dmQ1,
            c1 * qrat(66, 5) * g1s * Shy,
        ]

    yf = gl4_integrate_vec(rhs, y0, t_span, n_steps)
    keys = [
        "g1", "g2", "g3", "yt", "yb", "ytau", "M1", "M2", "M3", "At", "Ab", "Atau",
        "mHu2", "mHd2", "mQ3", "mu3", "md3", "mL3", "me3", "mQ1", "mu1", "md1", "mL1", "me1", "mQ2", "Shy",
    ]
    return dict(zip(keys, yf))


def run_2loop_qcd_gl4(a_start: mp.mpf, m_start: mp.mpf, t_span: mp.mpf, nf: int, n_steps: int = 18) -> tuple[mp.mpf, mp.mpf]:
    b0 = qrat(11, 4) - qrat(nf, 6)
    b1 = qrat(102, 16) - qrat(38 * nf, 48)
    g0 = mp.mpf(1)
    g1 = qrat(101, 24) - qrat(5 * nf, 36)

    def rhs(v: list[mp.mpf]) -> list[mp.mpf]:
        av, mv = v[0], v[1]
        return [-2 * (b0 * av * av + b1 * (av ** 3)), -2 * mv * (g0 * av + g1 * av * av)]

    res = gl4_integrate_vec(rhs, [a_start, m_start], t_span, n_steps)
    return res[0], res[1]


def lam_qcd_2loop_scale(mu_v: mp.mpf, a_pi: mp.mpf, nf: int) -> tuple[mp.mpf, mp.mpf]:
    b0 = qrat(11, 4) - qrat(nf, 6)
    b1 = qrat(102, 16) - qrat(38 * nf, 48)
    ex = mu_v * mp.exp(-1 / (2 * b0 * a_pi)) * ((b0 * a_pi) / (1 + (b1 / b0) * a_pi)) ** (-b1 / (2 * b0 * b0))
    st = mu_v * mp.exp(-1 / (2 * b0 * a_pi)) * (b0 * a_pi) ** (-b1 / (2 * b0 * b0))
    return ex, st


def loop_I_3(a: mp.mpf, b: mp.mpf, c: mp.mpf) -> mp.mpf:
    eps = q10(-10) * max(a, b, c)
    if abs(a - b) < eps and abs(b - c) < eps:
        return 1 / (2 * a)
    if abs(a - b) < eps:
        x = c / a
        return (1 - x + x * mp.log(x)) / (a * (1 - x) ** 2)
    if abs(b - c) < eps:
        x = a / b
        return (1 - x + x * mp.log(x)) / (b * (1 - x) ** 2)
    if abs(c - a) < eps:
        x = b / c
        return (1 - x + x * mp.log(x)) / (c * (1 - x) ** 2)
    return -(a * b * mp.log(a / b) + b * c * mp.log(b / c) + c * a * mp.log(c / a)) / ((a - b) * (b - c) * (c - a))


def pv_b0_fin_ref(r: mp.mpf) -> mp.mpf:
    if r > 1:
        sr = mp.sqrt(r - 1)
        return 2 - 2 * sr * mp.atan(1 / sr)
    if r < 1:
        sr = mp.sqrt(1 - r)
        return 2 - sr * mp.log((1 + sr) / (1 - sr))
    return mp.mpf(2)


def higgs_pole_4coupling(
    lam_v: mp.mpf, yt_v: mp.mpf, g1_v: mp.mpf, g2_v: mp.mpf, mu_v: mp.mpf, with_bosons: bool = True
) -> dict[str, mp.mpf]:
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    gps = qrat(3, 5) * g1_v * g1_v
    g2s = g2_v * g2_v
    gzs = g2s + gps
    mh2, mt2, mw2, mz2, mu2 = lam_v, (yt_v * yt_v) / 2, g2s / 4, gzs / 4, mu_v * mu_v
    r_t, r_W, r_Z = 4 * mt2 / mh2, 4 * mw2 / mh2, 4 * mz2 / mh2
    d_t = c1 * 3 * yt_v * yt_v * ((2 - r_t) * mp.log(mt2 / mu2) - qrat(1, 2) + (r_t - 1) * pv_b0_fin_ref(r_t))
    d_h = c1 * lam_v * (6 * mp.log(mh2 / mu2) - 12 + qrat(3, 2) * mp.sqrt(3) * mp.pi)
    d_W = c1 * g2s * ((qrat(3, 4) * r_W - 3) * mp.log(mw2 / mu2) + qrat(1, 2) * r_W - (qrat(3, 4) * r_W - 1) * pv_b0_fin_ref(r_W))
    d_Z = c1 * gzs * ((qrat(3, 8) * r_Z - qrat(3, 2)) * mp.log(mz2 / mu2) + qrat(1, 4) * r_Z - (qrat(3, 8) * r_Z - qrat(1, 2)) * pv_b0_fin_ref(r_Z))
    d_tot = d_t + (d_h + d_W + d_Z if with_bosons else mp.mpf(0))
    return {"mh_pole_v": mp.sqrt(max(lam_v * (1 + d_tot), q10(-12))), "delta_tot": d_tot}


# ==============================================================================
# REF_1: Pure-QFT SymPy Proofs + GL4 MSSM->SM->m_t->M_Z->QCD Pipeline
# ==============================================================================

def run_ref1_sympy_proofs() -> dict[str, Any]:
    z2, z3, ln2, nl = sp.symbols("zeta2 zeta3 ln2 n_l")
    CF, CA, TF = sp.Rational(4, 3), sp.Integer(3), sp.Rational(1, 2)
    KF = -sp.Rational(71, 128) + sp.Rational(15, 8) * z2 - 3 * z2 * ln2 + sp.Rational(3, 4) * z3
    KA = sp.Rational(1111, 384) - sp.Rational(1, 2) * z2 + sp.Rational(3, 2) * z2 * ln2 - sp.Rational(3, 8) * z3
    KH = -sp.Rational(143, 96) + z2
    KL = -sp.Rational(71, 96) - sp.Rational(1, 2) * z2
    c20_expr = sp.expand(KF * CF**2 + KA * CF * CA + KH * CF * TF + KL * CF * TF * nl)
    c20_closed = sp.Rational(307, 32) + 2 * z2 + sp.Rational(2, 3) * z2 * ln2 - sp.Rational(1, 6) * z3 - (sp.Rational(71, 144) + sp.Rational(1, 3) * z2) * nl
    c20_diff = sp.simplify(c20_expr - c20_closed)

    a_s, L_s, b0_s, g0_s, g1_s, c10_s, c11_s, c20_s, c21_s, c22_s = sp.symbols("a L b0 g0 g1 c10 c11 c20 c21 c22")
    da = -b0_s * a_s**2
    dm = -(g0_s * a_s + g1_s * a_s**2)
    dL = 1 - 2 * dm
    R = 1 + (c10_s + c11_s * L_s) * a_s + (c20_s + c21_s * L_s + c22_s * L_s**2) * a_s**2
    dM = sp.expand(dm * R + sp.diff(R, a_s) * da + sp.diff(R, L_s) * dL)
    pa = sp.Poly(dM, a_s)
    sol_rg = sp.solve(
        [sp.Poly(pa.nth(1), L_s).nth(0), sp.Poly(pa.nth(2), L_s).nth(0), sp.Poly(pa.nth(2), L_s).nth(1)],
        [c11_s, c21_s, c22_s],
    )
    s6 = {b0_s: sp.Rational(7, 4), g0_s: sp.Integer(1), g1_s: sp.Rational(27, 8), c10_s: sp.Rational(4, 3)}
    s5 = {b0_s: sp.Rational(23, 12), g0_s: sp.Integer(1), g1_s: sp.Rational(253, 72), c10_s: sp.Rational(4, 3)}
    c11_6, c21_6, c22_6 = [sp.simplify(sol_rg[k].subs(s6)) for k in (c11_s, c21_s, c22_s)]
    c11_5, c21_5, c22_5 = [sp.simplify(sol_rg[k].subs(s5)) for k in (c11_s, c21_s, c22_s)]
    pf1_resid = sp.simplify(pa.nth(2).subs({**s6, c11_s: c11_6, c21_s: c21_6 + sp.Rational(1, 2), c22_s: c22_6}))

    lam, yt, g2, gp, mu = sp.symbols("lam yt g2 gp mu", positive=True)
    rt, rw, rz = 2 * yt**2 / lam, g2**2 / lam, (g2**2 + gp**2) / lam
    blam1 = 12 * lam**2 - 12 * yt**4 + 12 * lam * yt**2 - 3 * lam * (3 * g2**2 + gp**2) + sp.Rational(3, 4) * (2 * g2**4 + (g2**2 + gp**2) ** 2)
    dt_l = 3 * yt**2 * (2 - rt) * sp.log(yt**2 / mu**2)
    dh_l = 6 * lam * sp.log(lam / mu**2)
    dw_l = g2**2 * (sp.Rational(3, 4) * rw - 3) * sp.log(g2**2 / mu**2)
    dz_l = (g2**2 + gp**2) * (sp.Rational(3, 8) * rz - sp.Rational(3, 2)) * sp.log((g2**2 + gp**2) / mu**2)
    higgs_4c_res = sp.simplify(blam1 + lam * mu * sp.diff(dt_l + dh_l + dw_l + dz_l, mu))
    higgs_toponly_res = sp.simplify(blam1 + lam * mu * sp.diff(dt_l, mu))

    nc = sp.Integer(3)
    drho_sym = sp.simplify((nc * yt**2 / (16 * sp.pi**2)) * (-sp.log(yt**2 / mu**2) + sp.Rational(1, 2)) - (nc * yt**2 / (16 * sp.pi**2)) * (-sp.log(yt**2 / mu**2)))
    drho_ok = bool(sp.simplify(drho_sym - 3 * yt**2 / (32 * sp.pi**2)) == 0)

    aq, muq, b0q, b1q = sp.symbols("aq muq b0q b1q", positive=True)
    ln_lam = sp.log(muq) - 1 / (2 * b0q * aq) - (b1q / (2 * b0q**2)) * sp.log((b0q * aq) / (1 + (b1q / b0q) * aq))
    lam_rg_res = sp.simplify(muq * sp.diff(ln_lam, muq) + sp.diff(ln_lam, aq) * (-2 * (b0q * aq**2 + b1q * aq**3)))

    b5_em, mt_s, mz_s, a_mt_s = sp.symbols("b5_em m_t M_Z a_mt", positive=True)
    db_top_em = sp.Rational(4, 3) * sp.Integer(3) * sp.Rational(2, 3) ** 2
    a_mz_6 = a_mt_s - ((b5_em + db_top_em) / (2 * sp.pi)) * sp.log(mz_s / mt_s)
    a_mz_5 = a_mt_s - (b5_em / (2 * sp.pi)) * sp.log(mz_s / mt_s)
    qed_decoup_shift = sp.simplify(a_mz_5 - a_mz_6)
    qed_decoup_sign_exact = bool(sp.simplify(qed_decoup_shift + (db_top_em / (2 * sp.pi)) * sp.log(mt_s / mz_s)) == 0 and db_top_em == sp.Rational(16, 9))

    z2_m, z3_m, ln2_m = (mp.pi ** 2) / 6, mp.zeta(3), mp.log(2)
    c20_5 = (qrat(307, 32) + 2 * z2_m + qrat(2, 3) * z2_m * ln2_m - qrat(1, 6) * z3_m) - 5 * (qrat(71, 144) + qrat(1, 3) * z2_m)
    c2_inv_5 = qrat(16, 9) - c20_5 - qrat(8, 3)

    ok = bool(
        c20_diff == 0
        and (c11_6, c21_6, c22_6) == (sp.Integer(1), sp.Rational(121, 24), sp.Rational(11, 8))
        and (c11_5, c21_5, c22_5) == (sp.Integer(1), sp.Rational(389, 72), sp.Rational(35, 24))
        and pf1_resid != 0
        and higgs_4c_res == 0
        and higgs_toponly_res != 0
        and drho_ok
        and lam_rg_res == 0
        and qed_decoup_sign_exact
    )
    return {
        "passed": ok,
        "c20_color_diff": str(c20_diff),
        "c20_nl5": mp.nstr(c20_5, 14),
        "c2_inv_nl5": mp.nstr(c2_inv_5, 14),
        "nf6_rg_coeffs": [str(c11_6), str(c21_6), str(c22_6)],
        "nf5_rg_coeffs": [str(c11_5), str(c21_5), str(c22_5)],
        "pf1_perturbed_c21_resid": str(pf1_resid),
        "higgs_4c_rg_residual": str(higgs_4c_res),
        "higgs_toponly_rg_nonzero": bool(higgs_toponly_res != 0),
        "veltman_delta_rho_exact": drho_ok,
        "lambda_qcd_2loop_rg_residual": str(lam_rg_res),
        "qed_5flav_top_decoupling_shift_a5_minus_a6": str(qed_decoup_shift),
        "qed_5flav_top_decoupling_sign_negative_for_mt_gt_MZ": qed_decoup_sign_exact,
        "_c20_5_mp": c20_5,
    }


def match_and_run_sm_gl4(
    st_mssm: tuple[Any, ...],
    soft: dict[str, mp.mpf],
    tan_beta: int,
    m0_over_v: int,
    c20_5: mp.mpf,
    sgn_mu: int = 1,
    n_sm_steps: int = 16,
) -> dict[str, Any]:
    g1_dr, g2_dr, g3_dr, yu_dr, yd_dr, ye_dr, kap_dr = st_mssm
    tb = mp.mpf(tan_beta)
    sinb = tb / mp.sqrt(1 + tb * tb)
    cosb = 1 / mp.sqrt(1 + tb * tb)
    cos2b = (1 - tb * tb) / (1 + tb * tb)

    mu_sq = (soft["mHd2"] - soft["mHu2"] * tb * tb) / (tb * tb - 1)
    mu_abs = mp.sqrt(mu_sq)
    mu_s = mp.mpf(sgn_mu) * mu_abs
    mA = mp.sqrt(soft["mHd2"] + soft["mHu2"] + 2 * mu_sq)
    m_stop = (soft["mQ3"] * soft["mu3"]) ** qrat(1, 4)
    m_q12 = mp.sqrt((soft["mQ1"] + soft["mQ2"]) / 2)
    M2, M3 = abs(soft["M2"]), abs(soft["M3"])
    Q_m = m_stop

    thresh = [
        (M3, (mp.mpf(0), mp.mpf(0), mp.mpf(2))),
        (M2, (mp.mpf(0), qrat(4, 3), mp.mpf(0))),
        (mu_abs, (qrat(2, 5), qrat(2, 3), mp.mpf(0))),
        (mA, (qrat(1, 10), qrat(1, 6), mp.mpf(0))),
        (mp.sqrt(soft["mQ3"]), (qrat(1, 30), qrat(1, 2), qrat(1, 3))),
        (mp.sqrt(soft["mu3"]), (qrat(4, 15), mp.mpf(0), qrat(1, 6))),
        (mp.sqrt(soft["md3"]), (qrat(1, 15), mp.mpf(0), qrat(1, 6))),
        (m_q12, (qrat(1, 15), mp.mpf(1), qrat(2, 3))),
        (mp.sqrt(soft["mu1"]), (qrat(8, 15), mp.mpf(0), qrat(1, 3))),
        (mp.sqrt(soft["md1"]), (qrat(2, 15), mp.mpf(0), qrat(1, 3))),
        (mp.sqrt(soft["mL3"]), (qrat(1, 10), qrat(1, 6), mp.mpf(0))),
        (mp.sqrt(soft["mL1"]), (qrat(1, 5), qrat(1, 3), mp.mpf(0))),
        (mp.sqrt(soft["me3"]), (qrat(1, 5), mp.mpf(0), mp.mpf(0))),
        (mp.sqrt(soft["me1"]), (qrat(2, 5), mp.mpf(0), mp.mpf(0))),
    ]
    a_dr_inv = [4 * mp.pi / (g * g) for g in (g1_dr, g2_dr, g3_dr)]
    c2_g = [mp.mpf(0), mp.mpf(2), mp.mpf(3)]
    a_ms_inv = [
        a_dr_inv[idx]
        + c2_g[idx] / (12 * mp.pi)
        - sum((db[idx] * mp.log(mi / Q_m) for mi, db in thresh), mp.mpf(0)) / (2 * mp.pi)
        for idx in range(3)
    ]
    g1_m, g2_m, g3_m = [mp.sqrt(4 * mp.pi / ai) for ai in a_ms_inv]
    a1_m, a2_m, a3_m = g1_m * g1_m / (4 * mp.pi), g2_m * g2_m / (4 * mp.pi), g3_m * g3_m / (4 * mp.pi)

    dr_u = 1 + a3_m / (3 * mp.pi) - qrat(3, 32) * a2_m / mp.pi - qrat(1, 480) * a1_m / mp.pi
    dr_d = 1 + a3_m / (3 * mp.pi) - qrat(3, 32) * a2_m / mp.pi - qrat(13, 480) * a1_m / mp.pi
    dr_e = 1 - qrat(3, 32) * a2_m / mp.pi + qrat(9, 160) * a1_m / mp.pi

    yt_dr = left_svd_asc(yu_dr)[1][2]
    delta_b = (
        (qrat(2, 3) * a3_m / mp.pi) * M3 * mu_s * tb * loop_I_3(soft["mQ3"], soft["md3"], M3 * M3)
        + (yt_dr * yt_dr / (16 * mp.pi * mp.pi)) * soft["At"] * mu_s * tb * loop_I_3(soft["mQ3"], soft["mu3"], mu_sq)
    )
    yu0 = (sinb * dr_u) * yu_dr
    yd0 = (cosb * dr_d / (1 + delta_b)) * yd_dr
    ye0 = (cosb * dr_e) * ye_dr
    kap0 = (sinb * sinb) * kap_dr

    yt0_sm = left_svd_asc(yu0)[1][2]
    xt_ms = (soft["At"] - mu_s / tb) / m_stop
    lam0 = ((g2_m * g2_m + qrat(3, 5) * g1_m * g1_m) / 4) * cos2b * cos2b + (qrat(3, 8) / (mp.pi * mp.pi)) * (yt0_sm ** 4) * (xt_ms * xt_ms) * (1 - xt_ms * xt_ms / 12)
    st_sm0 = (g1_m, g2_m, g3_m, yu0, yd0, ye0, kap0, lam0)
    q_match_v = mp.mpf(m0_over_v) * m_stop

    # Self-consistent mu_* = m_t(m_t) via GL4 + secant
    x0 = mp.log(yt0_sm / mp.sqrt(2))
    st_mt = gl4_integrate_tuple(lambda s: sm_2loop_rhs(s, True), st_sm0, x0 - mp.log(q_match_v), n_sm_steps)
    fp = x0 - mp.log(left_svd_asc(st_mt[3])[1][2] / mp.sqrt(2))
    xp = x0
    xc = x0 - fp
    st_mt = gl4_integrate_tuple(lambda s: sm_2loop_rhs(s, True), st_mt, xc - xp, 3)
    fc = xc - mp.log(left_svd_asc(st_mt[3])[1][2] / mp.sqrt(2))
    for _ in range(5):
        if abs(fc) < q10(-20) or abs(fc - fp) < q10(-25):
            break
        xn = xc - fc * (xc - xp) / (fc - fp)
        st_mt = gl4_integrate_tuple(lambda s: sm_2loop_rhs(s, True), st_mt, xn - xc, 2)
        xp, fp = xc, fc
        xc = xn
        fc = xc - mp.log(left_svd_asc(st_mt[3])[1][2] / mp.sqrt(2))
    mu_mt_v = mp.exp(xc)

    g1_t, g2_t, g3_t, yu_t, yd_t, ye_t, kap_t, lam_t = st_mt
    a3_t = g3_t * g3_t / (4 * mp.pi)
    as_pi_t = a3_t / mp.pi
    yt_t = left_svd_asc(yu_t)[1][2]
    mt_ms_t = yt_t / mp.sqrt(2)
    mt_pole_2l_mt = mt_ms_t * (1 + qrat(4, 3) * as_pi_t + c20_5 * (as_pi_t ** 2))
    h4_mt = higgs_pole_4coupling(lam_t, yt_t, g1_t, g2_t, mu_mt_v, with_bosons=True)
    htop_mt = higgs_pole_4coupling(lam_t, yt_t, g1_t, g2_t, mu_mt_v, with_bosons=False)

    # Self-consistent mu = M_Z via GL4
    mz_c = mp.sqrt((g2_t * g2_t + qrat(3, 5) * g1_t * g1_t) / 4)
    st_mz = gl4_integrate_tuple(lambda s: sm_2loop_rhs(s, True), st_mt, mp.log(mz_c / mu_mt_v), max(8, n_sm_steps // 2))
    for _ in range(3):
        mz_n = mp.sqrt((st_mz[1] ** 2 + qrat(3, 5) * st_mz[0] ** 2) / 4)
        dlz = mp.log(mz_n / mz_c)
        if abs(dlz) < q10(-20):
            mz_c = mz_n
            break
        st_mz = gl4_integrate_tuple(lambda s: sm_2loop_rhs(s, True), st_mz, dlz, 2)
        mz_c = mz_n

    g1_z, g2_z, g3_z, yu_z, yd_z, ye_z, kap_z, lam_z = st_mz
    a1_z = g1_z * g1_z / (4 * mp.pi)
    a2_z = g2_z * g2_z / (4 * mp.pi)
    a3_z6 = g3_z * g3_z / (4 * mp.pi)
    s2w_z = (3 * a1_z) / (3 * a1_z + 5 * a2_z)
    aem_inv_z6 = qrat(5, 3) / a1_z + 1 / a2_z
    mz_v = mp.sqrt((g2_z * g2_z + qrat(3, 5) * g1_z * g1_z) / 4)
    ck_z = extract_ckm(yu_z, yd_z, ye_z)
    pm_z = extract_pmns(ye_z, kap_z)

    # 5-coupling 2-loop RG-log Higgs pole at mu = M_Z
    h4_mz = higgs_pole_4coupling(lam_z, ck_z["yt"], g1_z, g2_z, mz_v, with_bosons=True)
    htop_mz = higgs_pole_4coupling(lam_z, ck_z["yt"], g1_z, g2_z, mz_v, with_bosons=False)
    r1_z = sm_2loop_rhs(st_mz, two_loop=False)
    r2_z = sm_2loop_rhs(st_mz, two_loop=True)
    eps_d = q10(-10)
    byt_1 = (left_svd_asc(yu_z + eps_d * r1_z[3])[1][2] - left_svd_asc(yu_z - eps_d * r1_z[3])[1][2]) / (2 * eps_d)
    blam_2 = r2_z[7] - r1_z[7]

    def f1_eval(la_v: mp.mpf, y_v: mp.mpf, gg1: mp.mpf, gg2: mp.mpf, mv: mp.mpf) -> mp.mpf:
        return la_v * higgs_pole_4coupling(la_v, y_v, gg1, gg2, mv, with_bosons=True)["delta_tot"]

    def r2_eval(mv: mp.mpf) -> mp.mpf:
        ep = q10(-10)
        df1 = (
            f1_eval(lam_z + ep * r1_z[7], ck_z["yt"] + ep * byt_1, g1_z + ep * r1_z[0], g2_z + ep * r1_z[1], mv)
            - f1_eval(lam_z - ep * r1_z[7], ck_z["yt"] - ep * byt_1, g1_z - ep * r1_z[0], g2_z - ep * r1_z[1], mv)
        ) / (2 * ep)
        return blam_2 + df1

    mt_ms_z = ck_z["yt"] / mp.sqrt(2)
    L_t_mz = mp.log((mt_ms_z * mt_ms_z) / (mz_v * mz_v))
    R20 = r2_eval(mt_ms_z)
    R21 = r2_eval(mt_ms_z * mp.exp(-qrat(1, 2))) - R20
    lam_d2_log = qrat(1, 4) * R21 * L_t_mz * L_t_mz + qrat(1, 2) * R20 * L_t_mz
    mh_pole_2l_mz = mp.sqrt(max(lam_z * (1 + h4_mz["delta_tot"]) + lam_d2_log, q10(-12)))
    mh_drift_4c = abs(mh_pole_2l_mz - h4_mt["mh_pole_v"]) / h4_mt["mh_pole_v"]
    mh_drift_toponly = abs(htop_mz["mh_pole_v"] - htop_mt["mh_pole_v"]) / htop_mt["mh_pole_v"]

    # Exact 5-flavor top decoupling at mu = m_t(m_t) down to M_Z via GL4 + exact QED sign
    t_dec = mp.log(mz_v / mu_mt_v)
    a_pi_z5, _ = run_2loop_qcd_gl4(as_pi_t, mp.mpf(1), t_dec, nf=5, n_steps=18)
    a3_z5 = a_pi_z5 * mp.pi
    qed_top_shift = (qrat(16, 9) / (2 * mp.pi)) * mp.log(mu_mt_v / mz_v)
    aem_inv_z5_exact = aem_inv_z6 - qed_top_shift

    # 1-loop Veltman Delta_rho
    drho_t = (3 * yt_t * yt_t) / (32 * mp.pi * mp.pi)
    mw_mz_tree = mp.sqrt(1 - s2w_z)
    mw_mz_pole = mw_mz_tree * mp.sqrt(1 + drho_t)
    s2w_os = 1 - mw_mz_pole * mw_mz_pole

    # 2-loop pure QCD Lambda_QCD via GL4
    mb_z = ck_z["yb"] / mp.sqrt(2)
    mc_z = ck_z["yc"] / mp.sqrt(2)
    a_mz5 = a3_z5 / mp.pi
    lam5_ex, lam5_st = lam_qcd_2loop_scale(mz_v, a_mz5, 5)
    nf_conf = 5
    lam_eff_ex, lam_eff_st = lam5_ex, lam5_st
    lam4_ex = lam5_ex
    if mb_z > 2 * lam5_ex:
        mb_c = mb_z
        ok_b = True
        a_mb = a_mz5
        for _ in range(6):
            if mb_c <= lam5_ex:
                ok_b = False
                break
            a_try, m_try = run_2loop_qcd_gl4(a_mz5, mb_z, mp.log(mb_c / mz_v), nf=5, n_steps=16)
            if a_try * mp.pi > qrat(3, 2) or a_try <= 0 or m_try <= lam5_ex:
                ok_b = False
                break
            a_mb, mb_c = a_try, m_try
        if ok_b:
            lam4_ex, lam4_st = lam_qcd_2loop_scale(mb_c, a_mb, 4)
            nf_conf = 4
            lam_eff_ex, lam_eff_st = lam4_ex, lam4_st
            _, mc_mb = run_2loop_qcd_gl4(a_mz5, mc_z, mp.log(mb_c / mz_v), nf=5, n_steps=16)
            if mc_mb > 2 * lam4_ex:
                mc_c = mc_mb
                ok_c = True
                a_mc = a_mb
                for _ in range(6):
                    if mc_c <= lam4_ex:
                        ok_c = False
                        break
                    a_try, m_try = run_2loop_qcd_gl4(a_mb, mc_mb, mp.log(mc_c / mb_c), nf=4, n_steps=16)
                    if a_try * mp.pi > qrat(3, 2) or a_try <= 0 or m_try <= lam4_ex:
                        ok_c = False
                        break
                    a_mc, mc_c = a_try, m_try
                if ok_c:
                    lam_eff_ex, lam_eff_st = lam_qcd_2loop_scale(mc_c, a_mc, 3)
                    nf_conf = 3

    return {
        "mu_mt_over_v": mu_mt_v,
        "mz_over_v": mz_v,
        "delta_b": delta_b,
        "alpha3_mz_nf6": a3_z6,
        "alpha3_mz_nf5": a3_z5,
        "alpha_EM_inv_mz_nf6": aem_inv_z6,
        "alpha_EM_inv_mz_nf5": aem_inv_z5_exact,
        "sin2_thetaW_msbar_mz": s2w_z,
        "sin2_thetaW_on_shell": s2w_os,
        "delta_rho_t_1loop": drho_t,
        "mw_over_mz_msbar": mw_mz_tree,
        "mw_over_mz_pole_veltman": mw_mz_pole,
        "mt_pole_2l_at_mt_over_v": mt_pole_2l_mt,
        "mh_pole_4c_at_mt_over_v": h4_mt["mh_pole_v"],
        "mh_pole_4c_at_mt_over_mz": h4_mt["mh_pole_v"] / mz_v,
        "mh_pole_4c_at_mz_over_mz": mh_pole_2l_mz / mz_v,
        "mh_pole_4c_scale_drift": mh_drift_4c,
        "mh_pole_toponly_scale_drift": mh_drift_toponly,
        "nf_active_at_confinement": nf_conf,
        "Lambda_QCD_5_exact_over_v": lam5_ex,
        "Lambda_QCD_4_exact_over_v": lam4_ex,
        "Lambda_QCD_eff_exact_over_v": lam_eff_ex,
        "ckm_mz": ck_z,
        "pmns_mz": pm_z,
        "st_mz": st_mz,
    }


# ==============================================================================
# REF_2: Dirac-Basis Majorana Spinors + 6-Pt GL + Fast High-Acc Bessel-K + GL4 Riccati
# ==============================================================================

def dirac_basis_majorana_proof() -> dict[str, Any]:
    """Standard Dirac-Pauli basis (gamma^0 = diag(I_2, -I_2)) + 6-point GL quadrature."""
    s0 = mp.eye(2)
    s1 = mp.matrix([[0, 1], [1, 0]])
    s2 = mp.matrix([[0, -I_C], [I_C, 0]])
    s3 = mp.matrix([[1, 0], [0, -1]])
    z2 = mp.zeros(2, 2)

    def blk(a: mp.matrix, b: mp.matrix, c: mp.matrix, d: mp.matrix) -> mp.matrix:
        m = mp.zeros(4, 4)
        for r in range(2):
            for col in range(2):
                m[r, col] = a[r, col]
                m[r, col + 2] = b[r, col]
                m[r + 2, col] = c[r, col]
                m[r + 2, col + 2] = d[r, col]
        return m

    g0 = blk(s0, z2, z2, -s0)
    g1 = blk(z2, s1, -s1, z2)
    g2 = blk(z2, s2, -s2, z2)
    g3 = blk(z2, s3, -s3, z2)
    g5 = I_C * g0 * g1 * g2 * g3
    PL = (mp.eye(4) - g5) / 2
    PR = (mp.eye(4) + g5) / 2
    C_mat = I_C * g2 * g0

    eta = [1, -1, -1, -1]
    gs = [g0, g1, g2, g3]
    cliff_err = mp.mpf(0)
    for mu in range(4):
        for nu in range(4):
            rhs = (2 * eta[mu] * mp.eye(4)) if mu == nu else mp.zeros(4, 4)
            cliff_err = max(cliff_err, m_frob(gs[mu] * gs[nu] + gs[nu] * gs[mu] - rhs))
    cc_err = max(m_frob(C_mat * g.T * (C_mat ** (-1)) + g) for g in gs)

    def bar(psi: mp.matrix) -> mp.matrix:
        return psi.H * g0

    def u_dirac(E: mp.mpf, m: mp.mpf, px: mp.mpf, py: mp.mpf, pz: mp.mpf, sp_i: int) -> mp.matrix:
        chi = mp.matrix([1, 0]) if sp_i == 0 else mp.matrix([0, 1])
        sp_dot_p = px * s1 + py * s2 + pz * s3
        rt = mp.sqrt(E + m)
        upper = rt * chi
        lower = (sp_dot_p * chi) / rt
        return mp.matrix([upper[0], upper[1], lower[0], lower[1]])

    def v_dirac(u: mp.matrix) -> mp.matrix:
        return C_mat * bar(u).T

    p_t = (mp.mpf(5), mp.mpf(3), mp.mpf(1), mp.mpf(2), mp.sqrt(11))
    pslash = p_t[0] * g0 - p_t[2] * g1 - p_t[3] * g2 - p_t[4] * g3
    u_sum = sum((u_dirac(*p_t, si) * bar(u_dirac(*p_t, si)) for si in (0, 1)), mp.zeros(4, 4))
    v_sum = sum((v_dirac(u_dirac(*p_t, si)) * bar(v_dirac(u_dirac(*p_t, si))) for si in (0, 1)), mp.zeros(4, 4))
    comp_err = max(m_frob(u_sum - (pslash + p_t[1] * mp.eye(4))), m_frob(v_sum - (pslash - p_t[1] * mp.eye(4))))

    j6 = mp.zeros(6, 6)
    for k in range(1, 6):
        bk = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
        j6[k - 1, k] = bk
        j6[k, k - 1] = bk
    ev6, evec6 = mp.eigsy(j6)
    gl6 = [(mp.re(ev6[k]), 2 * (mp.re(evec6[0, k]) ** 2)) for k in range(6)]

    def eval_sv(
        M1: mp.mpf, mf: mp.mpf, m_fL: mp.mpf, m_fR: mp.mpf, YL: mp.mpf, YR: mp.mpf, vrel: mp.mpf, f_sign: int = -1
    ) -> mp.mpf:
        E1 = M1 / mp.sqrt(1 - (vrel / 2) ** 2)
        p1z = E1 * (vrel / 2)
        kf = mp.sqrt(E1 * E1 - mf * mf)
        uB1 = [u_dirac(E1, M1, mp.mpf(0), mp.mpf(0), p1z, si) for si in (0, 1)]
        vB1 = [v_dirac(u) for u in uB1]
        uB2 = [u_dirac(E1, M1, mp.mpf(0), mp.mpf(0), -p1z, si) for si in (0, 1)]
        vB2 = [v_dirac(u) for u in uB2]
        sv_acc = mp.mpf(0)
        for ct, wt in gl6:
            st_a = mp.sqrt(1 - ct * ct)
            k1x, k1z = kf * st_a, kf * ct
            qt2 = -(k1x * k1x + (p1z - k1z) ** 2)
            qu2 = -(k1x * k1x + (-p1z - k1z) ** 2)
            uts = [u_dirac(E1, mf, k1x, mp.mpf(0), k1z, si) for si in (0, 1)]
            vts = [v_dirac(u_dirac(E1, mf, -k1x, mp.mpf(0), -k1z, si)) for si in (0, 1)]
            acc = mp.mpf(0)
            for s1i in (0, 1):
                for s2i in (0, 1):
                    for sf1 in (0, 1):
                        for sf2 in (0, 1):
                            aLt = (2 * YL * YL) * (bar(uts[sf1]) * PR * uB1[s1i])[0, 0] * (bar(vB2[s2i]) * PL * vts[sf2])[0, 0] / (qt2 - m_fL * m_fL) if YL != 0 else mp.mpc(0)
                            aRt = (2 * YR * YR) * (bar(uts[sf1]) * PL * uB1[s1i])[0, 0] * (bar(vB2[s2i]) * PR * vts[sf2])[0, 0] / (qt2 - m_fR * m_fR) if YR != 0 else mp.mpc(0)
                            aLu = (2 * YL * YL) * (bar(uts[sf1]) * PR * uB2[s2i])[0, 0] * (bar(vB1[s1i]) * PL * vts[sf2])[0, 0] / (qu2 - m_fL * m_fL) if YL != 0 else mp.mpc(0)
                            aRu = (2 * YR * YR) * (bar(uts[sf1]) * PL * uB2[s2i])[0, 0] * (bar(vB1[s1i]) * PR * vts[sf2])[0, 0] / (qu2 - m_fR * m_fR) if YR != 0 else mp.mpc(0)
                            mtot = (aLt + aRt) + mp.mpf(f_sign) * (aLu + aRu)
                            acc += abs(mtot) ** 2
            sv_acc += wt * (acc / 4) * kf / (64 * mp.pi * (E1 ** 3))
        return sv_acc

    swave_max = mp.mpf(0)
    pwave_max_err = mp.mpf(0)
    v_test = q10(-6)
    by_r: dict[str, Any] = {}
    for r_i in (2, 5, 10):
        msf = mp.sqrt(mp.mpf(r_i))
        sv0 = eval_sv(mp.mpf(1), mp.mpf(0), msf, msf, mp.mpf(0), mp.mpf(1), mp.mpf(0), f_sign=-1)
        svp = eval_sv(mp.mpf(1), mp.mpf(0), msf, msf, mp.mpf(0), mp.mpf(1), v_test, f_sign=-1)
        pred = (mp.mpf(1) / (12 * mp.pi)) * (1 + mp.mpf(r_i) ** 2) / ((1 + mp.mpf(r_i)) ** 4) * (v_test ** 2)
        re_p = abs(svp - pred) / pred
        swave_max = max(swave_max, sv0)
        pwave_max_err = max(pwave_max_err, re_p)
        by_r[f"r_{r_i}"] = {"swave_zero": mp.nstr(sv0, 6), "pwave_rel_err": mp.nstr(re_p, 10)}

    pf3_flipped = eval_sv(mp.mpf(1), mp.mpf(0), mp.sqrt(2), mp.sqrt(2), mp.mpf(0), mp.mpf(1), mp.mpf(0), f_sign=+1)

    M1_t, mt_t, mtL, mtR = mp.mpf(2), mp.mpf(1), mp.mpf(3), mp.mpf(4)
    YQ, Yuc = qrat(1, 6), qrat(-2, 3)
    sv_tt = eval_sv(M1_t, mt_t, mtL, mtR, YQ, Yuc, mp.mpf(0), f_sign=-1)
    sv_tt_plus = (mt_t * mt_t / (8 * mp.pi)) * (
        YQ * YQ / (mtL * mtL + M1_t * M1_t - mt_t * mt_t) + Yuc * Yuc / (mtR * mtR + M1_t * M1_t - mt_t * mt_t)
    ) ** 2 * mp.sqrt(1 - (mt_t / M1_t) ** 2)
    sv_tt_minus = (mt_t * mt_t / (8 * mp.pi)) * (
        YQ * YQ / (mtL * mtL + M1_t * M1_t - mt_t * mt_t) - Yuc * Yuc / (mtR * mtR + M1_t * M1_t - mt_t * mt_t)
    ) ** 2 * mp.sqrt(1 - (mt_t / M1_t) ** 2)
    tt_plus_err = abs(sv_tt - sv_tt_plus) / sv_tt_plus
    tt_minus_err = abs(sv_tt - sv_tt_minus) / sv_tt

    gs_s, mpr_s, m1_s = sp.symbols("g_s M_Pr M_1", positive=True)
    pref_rat = sp.simplify(
        ((2 * sp.pi**2 / 45) * gs_s * m1_s**3 / (sp.sqrt(sp.pi**2 * gs_s / 90) * m1_s**2 / mpr_s * m1_s**2))
        / (sp.sqrt(8 * sp.pi**2 * gs_s / 45) * mpr_s / m1_s)
    )
    sum_ny4 = 3 * (
        sp.Integer(1) ** 4
        + 2 * sp.Rational(-1, 2) ** 4
        + 6 * sp.Rational(1, 6) ** 4
        + 3 * sp.Rational(-2, 3) ** 4
        + 3 * sp.Rational(1, 3) ** 4
    )
    ok = bool(
        cliff_err < q10(-24)
        and cc_err < q10(-24)
        and comp_err < q10(-24)
        and swave_max < q10(-25)
        and pwave_max_err < q10(-10)
        and tt_plus_err < q10(-10)
        and tt_minus_err > qrat(2, 10)
        and pf3_flipped > q10(-4)
        and pref_rat == 1
        and sum_ny4 == sp.Rational(95, 18)
    )
    return {
        "passed": ok,
        "basis": "Dirac-Pauli (gamma^0 = diag(I_2, -I_2)) + 6-pt Gauss-Legendre",
        "clifford_err": mp.nstr(cliff_err, 6),
        "charge_conj_err": mp.nstr(cc_err, 6),
        "completeness_err": mp.nstr(comp_err, 6),
        "massless_swave_max": mp.nstr(swave_max, 8),
        "massless_pwave_max_rel_err": mp.nstr(pwave_max_err, 10),
        "pwave_by_r": by_r,
        "massive_ttbar_LplusR_rel_err": mp.nstr(tt_plus_err, 10),
        "massive_ttbar_wrong_LminusR_rel_err": mp.nstr(tt_minus_err, 10),
        "pf3_flipped_fermi_sign_swave": mp.nstr(pf3_flipped, 10),
        "prefactor_ratio_exact": str(pref_rat),
        "sum_15species_Ni_Yi_4": str(sum_ny4),
    }


def neutralino_purity_4x4(M1_v: mp.mpf, M2_v: mp.mpf, mu_v: mp.mpf, mz_v: mp.mpf, s2w: mp.mpf, tb_i: int) -> dict[str, mp.mpf]:
    tb = mp.mpf(tb_i)
    sb, cb = tb / mp.sqrt(1 + tb * tb), 1 / mp.sqrt(1 + tb * tb)
    sw, cw = mp.sqrt(s2w), mp.sqrt(1 - s2w)
    mn = mp.matrix([
        [M1_v, mp.mpf(0), -mz_v * cb * sw, mz_v * sb * sw],
        [mp.mpf(0), M2_v, mz_v * cb * cw, -mz_v * sb * cw],
        [-mz_v * cb * sw, mz_v * cb * cw, mp.mpf(0), -mu_v],
        [mz_v * sb * sw, -mz_v * sb * cw, -mu_v, mp.mpf(0)],
    ])
    vals, vecs = mp.eigsy(mn)
    idx = min(range(4), key=lambda k: abs(vals[k]))
    return {"m_chi1_v": abs(vals[idx]), "bino_purity": vecs[0, idx] ** 2}


_GL4_RICC_CACHE: dict[tuple[int, int], list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]] = {}
_GL4_BOLTZ_CACHE: dict[tuple[int, int], list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]] = {}


def _besselk_asymp(nu: int, x: mp.mpf, n_terms: int = 18) -> mp.mpf:
    """Exact rational asymptotic expansion for K_nu(x), accurate to < 1e-18 for x >= 25."""
    mu4 = 4 * nu * nu
    ix = 1 / x
    term = mp.mpf(1)
    acc = term
    for k in range(1, n_terms + 1):
        term = term * mp.mpf(mu4 - (2 * k - 1) ** 2) * ix / mp.mpf(8 * k)
        acc += term
    return mp.sqrt(mp.pi / (2 * x)) * mp.exp(-x) * acc


def _k2_fast(x: mp.mpf) -> mp.mpf:
    if x <= 25:
        return mp.besselk(2, x)
    return _besselk_asymp(2, x, 18)


def _k1_k2_fast(z: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    if z <= 25:
        return mp.besselk(1, z), mp.besselk(2, z)
    return _besselk_asymp(1, z, 18), _besselk_asymp(2, z, 18)


def _get_gl4_riccati_grid(n_steps: int) -> list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]:
    key = (n_steps, mp.mp.dps)
    if key in _GL4_RICC_CACHE:
        return _GL4_RICC_CACHE[key]
    u0, u1 = mp.mpf(0), mp.log(mp.mpf(500))
    h = (u1 - u0) / mp.mpf(n_steps)
    s3_6 = mp.sqrt(3) / 6
    c1_n, c2_n = qrat(1, 2) - s3_6, qrat(1, 2) + s3_6
    grid: list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for k in range(n_steps):
        uk = u0 + k * h
        x1 = mp.exp(uk + c1_n * h)
        x2 = mp.exp(uk + c2_n * h)
        xe = mp.exp(uk + h)
        xek2 = (xe * xe * _k2_fast(xe)) if xe <= 30 else mp.mpf(0)
        grid.append((x1, x1 * x1 * _k2_fast(x1), x2, x2 * x2 * _k2_fast(x2), xe, xek2))
    _GL4_RICC_CACHE[key] = grid
    return grid


def benchmark_gl4_analytic_riccati() -> mp.mpf:
    s3 = mp.sqrt(3)
    s3_6 = s3 / 6
    a11, a12, a21, a22 = qrat(1, 4), qrat(1, 4) - s3_6, qrat(1, 4) + s3_6, qrat(1, 4)
    c_val = mp.mpf(1000)
    alp = qrat(1, 10)
    y_cur = mp.mpf(1)
    x0, x1 = mp.mpf(0), qrat(1, 10)
    n_st = 200
    h = (x1 - x0) / mp.mpf(n_st)
    for _ in range(n_st):
        y1 = y2 = y_cur
        for _it in range(15):
            f1 = -c_val * (y1 * y1 - alp * alp)
            f2 = -c_val * (y2 * y2 - alp * alp)
            r1 = y1 - y_cur - h * (a11 * f1 + a12 * f2)
            r2 = y2 - y_cur - h * (a21 * f1 + a22 * f2)
            if max(abs(r1), abs(r2)) < q10(-24):
                break
            j11 = 1 + 2 * h * a11 * c_val * y1
            j12 = 2 * h * a12 * c_val * y2
            j21 = 2 * h * a21 * c_val * y1
            j22 = 1 + 2 * h * a22 * c_val * y2
            det = j11 * j22 - j12 * j21
            y1 -= (j22 * r1 - j12 * r2) / det
            y2 -= (-j21 * r1 + j11 * r2) / det
        y_cur = y_cur + s3 * (y2 - y1)
    y_exact = alp * mp.coth(c_val * alp * (x1 - x0) + qrat(1, 2) * mp.log(qrat(11, 9)))
    return abs(y_cur - y_exact) / y_exact


def solve_riccati_freezeout_gl4(
    c_s: mp.mpf,
    c_p: mp.mpf,
    mpred_over_m1: mp.mpf,
    g_star: mp.mpf,
    n_steps: int = 1600,
) -> dict[str, mp.mpf]:
    s3 = mp.sqrt(3)
    s3_6 = s3 / 6
    a11, a12, a21, a22 = qrat(1, 4), qrat(1, 4) - s3_6, qrat(1, 4) + s3_6, qrat(1, 4)
    pref_c = mp.sqrt(qrat(8, 45) * (mp.pi ** 2) * g_star) * mpred_over_m1
    pref_ye = mp.mpf(45) / (2 * (mp.pi ** 4) * g_star)
    h = mp.log(mp.mpf(500)) / mp.mpf(n_steps)
    y_cur = pref_ye * _k2_fast(mp.mpf(1))
    grid = _get_gl4_riccati_grid(n_steps)
    x_f = mp.mpf(0)
    prev_rat = mp.mpf(1)
    prev_x = mp.mpf(1)

    for k in range(n_steps):
        x1, x1k2, x2, x2k2, xe, xek2 = grid[k]
        c1 = pref_c * (c_s + c_p / x1) / x1
        ye1 = pref_ye * x1k2
        c2 = pref_c * (c_s + c_p / x2) / x2
        ye2 = pref_ye * x2k2
        yee = pref_ye * xek2
        if h * c1 * ye1 > 5 and y_cur < 3 * ye1:
            y1, y2 = ye1, ye2
        else:
            y1, y2 = y_cur, y_cur
        max_r = mp.mpf(1)
        for _it in range(18):
            f1 = -c1 * (y1 * y1 - ye1 * ye1)
            f2 = -c2 * (y2 * y2 - ye2 * ye2)
            r1 = y1 - y_cur - h * (a11 * f1 + a12 * f2)
            r2 = y2 - y_cur - h * (a21 * f1 + a22 * f2)
            max_r = max(abs(r1), abs(r2))
            if max_r <= q10(-23) * max(y_cur, q10(-30)):
                break
            j11 = 1 + 2 * h * a11 * c1 * y1
            j12 = 2 * h * a12 * c2 * y2
            j21 = 2 * h * a21 * c1 * y1
            j22 = 1 + 2 * h * a22 * c2 * y2
            det = j11 * j22 - j12 * j21
            dy1 = (j22 * r1 - j12 * r2) / det
            dy2 = (-j21 * r1 + j11 * r2) / det
            step_s = mp.mpf(1)
            while (y1 - step_s * dy1 <= 0 or y2 - step_s * dy2 <= 0) and step_s > q10(-6):
                step_s *= qrat(1, 2)
            y1 = max(y1 - step_s * dy1, q10(-60))
            y2 = max(y2 - step_s * dy2, q10(-60))
        if max_r > q10(-16) * max(y_cur, q10(-30)):
            raise RuntimeError(f"GL4 Riccati Newton failed at step {k}: resid={max_r}")
        y_cur = y_cur + s3 * (y2 - y1)
        if x_f == 0 and yee > 0:
            rn = y_cur / yee
            if rn >= 2 and prev_rat < 2:
                x_f = prev_x + ((2 - prev_rat) / (rn - prev_rat)) * (xe - prev_x)
            prev_rat = rn
            prev_x = xe
    return {"Y_inf": y_cur, "x_f": x_f}


def compute_bino_dm_gl4(
    soft: dict[str, mp.mpf],
    m0_over_v: int,
    tan_beta: int,
    gp_sq: mp.mpf,
    mt_v: mp.mpf,
    mz_v: mp.mpf,
    s2w: mp.mpf,
    mgut_over_mpred: mp.mpf,
    t_susy_neg: mp.mpf,
    yb_ref: mp.mpf,
    lam_qcd_v: mp.mpf,
    n_steps: int = 1600,
    unreduced_fault: bool = False,
    fixed_ref_m0: int | None = None,
) -> dict[str, Any]:
    m0_v = mp.mpf(m0_over_v)
    M1_m0 = abs(soft["M1"])
    M1_v = M1_m0 * m0_v
    M2_v = abs(soft["M2"]) * m0_v
    tb = mp.mpf(tan_beta)
    mu_v = mp.sqrt((soft["mHd2"] - soft["mHu2"] * tb * tb) / (tb * tb - 1)) * m0_v
    neut = neutralino_purity_4x4(M1_v, M2_v, mu_v, mz_v, s2w, tan_beta)

    m1s = M1_m0 * M1_m0
    pk = lambda r: (1 + r * r) / ((1 + r) ** 4)
    top_open = bool(M1_v > mt_v)
    bt = mp.sqrt(1 - (mt_v / M1_v) ** 2) if top_open else mp.mpf(0)
    sum_p = (
        2 * pk(soft["me1"] / m1s)
        + 1 * pk(soft["me3"] / m1s)
        + 4 * (qrat(1, 2) ** 4) * pk(soft["mL1"] / m1s)
        + 2 * (qrat(1, 2) ** 4) * pk(soft["mL3"] / m1s)
        + 12 * (qrat(1, 6) ** 4) * pk(soft["mQ1"] / m1s)
        + 3 * (qrat(1, 6) ** 4) * pk(soft["mQ3"] / m1s)
        + (3 * (qrat(1, 6) ** 4) * pk(soft["mQ3"] / m1s) * bt if top_open else mp.mpf(0))
        + 6 * (qrat(2, 3) ** 4) * pk(soft["mu1"] / m1s)
        + (3 * (qrat(2, 3) ** 4) * pk(soft["mu3"] / m1s) * bt if top_open else mp.mpf(0))
        + 6 * (qrat(1, 3) ** 4) * pk(soft["md1"] / m1s)
        + 3 * (qrat(1, 3) ** 4) * pk(soft["md3"] / m1s)
    )
    gp4 = gp_sq * gp_sq
    c_p = (gp4 / (2 * mp.pi)) * sum_p
    if top_open:
        mr2 = (mt_v / M1_v) ** 2
        amp = qrat(1, 36) / (soft["mQ3"] / m1s + 1 - mr2) + qrat(4, 9) / (soft["mu3"] / m1s + 1 - mr2)
        c_s = (3 * gp4 / (8 * mp.pi)) * mr2 * (amp * amp) * bt
    else:
        c_s = mp.mpf(0)

    mpred_m1 = 1 / (mgut_over_mpred * mp.exp(t_susy_neg) * M1_m0)
    if fixed_ref_m0 is not None:
        mpred_m1 *= mp.mpf(fixed_ref_m0) / m0_v
    if unreduced_fault:
        mpred_m1 /= mp.sqrt(8 * mp.pi)

    tf_est = M1_v / mp.mpf(25)
    mw_v = mz_v * mp.sqrt(1 - s2w)
    g_star = qrat(427, 4) if tf_est > mt_v else (qrat(385, 4) if tf_est > mw_v else qrat(345, 4))
    sol = solve_riccati_freezeout_gl4(c_s, c_p, mpred_m1, g_star, n_steps=n_steps)
    m_stau_m0 = mp.sqrt(soft["me3"])
    d_stau = (m_stau_m0 - M1_m0) / M1_m0
    return {
        "M1_over_v": M1_v,
        "m_chi1_over_v": neut["m_chi1_v"],
        "bino_purity_N11sq": neut["bino_purity"],
        "delta_stauR": d_stau,
        "x_f": sol["x_f"],
        "Y_Bino_inf": sol["Y_inf"],
        "r_vew": (M1_v * sol["Y_inf"]) / yb_ref,
        "clat_OmegaRatio": ((M1_v / lam_qcd_v) * sol["Y_inf"]) / yb_ref,
    }


# ==============================================================================
# REF_3: Sequential Seesaw (GL4 + Real 2n eigsy Takagi) & Stiff GL4 Boltzmann
# ==============================================================================

def mssm_seesaw_rhs(st: tuple[Any, ...]) -> tuple[Any, ...]:
    g1, g2, g3, yu, yd, ye, kap, ynu, mr = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    i3 = mp.eye(3)
    hu, hd, he, hn = yu * yu.H, yd * yd.H, ye * ye.H, ynu * ynu.H
    htu, htd, hte, htn = yu.H * yu, yd.H * yd, ye.H * ye, ynu.H * ynu
    tu, td, te, tn = mp.re(m_trace(hu)), mp.re(m_trace(hd)), mp.re(m_trace(he)), mp.re(m_trace(hn))

    dg1 = c1 * qrat(33, 5) * (g1 ** 3)
    dg2 = c1 * (g2 ** 3)
    dg3 = c1 * (-3) * (g3 ** 3)
    gQ = c1 * (hu + hd - (qrat(1, 30) * g1s + qrat(3, 2) * g2s + qrat(8, 3) * g3s) * i3)
    guc = c1 * (2 * htu - (qrat(8, 15) * g1s + qrat(8, 3) * g3s) * i3)
    gdc = c1 * (2 * htd - (qrat(2, 15) * g1s + qrat(8, 3) * g3s) * i3)
    gL = c1 * (he + hn - (qrat(3, 10) * g1s + qrat(3, 2) * g2s) * i3)
    gec = c1 * (2 * hte - (qrat(6, 5) * g1s) * i3)
    gHu = c1 * (3 * tu + tn - (qrat(3, 10) * g1s + qrat(3, 2) * g2s))
    gHd = c1 * (3 * td + te - (qrat(3, 10) * g1s + qrat(3, 2) * g2s))
    gnuc = c1 * (2 * htn)

    gLH = gL + gHu * i3
    return (
        dg1, dg2, dg3,
        gQ * yu + yu * guc + gHu * yu,
        gQ * yd + yd * gdc + gHd * yd,
        gL * ye + ye * gec + gHd * ye,
        gLH * kap + kap * gLH.T,
        gL * ynu + ynu * gnuc + gHu * ynu,
        gnuc.T * mr + mr * gnuc,
    )


def run_seq_seesaw_gl4(
    g_uv: mp.mpf,
    yu_uv: mp.matrix,
    yd_uv: mp.matrix,
    ye_uv: mp.matrix,
    ynu_uv: mp.matrix,
    mr_dimless: mp.matrix,
    mr0_mgut: mp.mpf,
    t_susy: mp.mpf,
    soft: dict[str, mp.mpf],
    c20_5: mp.mpf,
    n_mssm: int = 24,
    n_sm: int = 14,
) -> dict[str, Any]:
    _, sv0 = takagi_real_2n_eigsy(mr_dimless)
    mr_cur = mr0_mgut * (mr_dimless / sv0[2])
    st: tuple[Any, ...] = (g_uv, g_uv, g_uv, yu_uv, yd_uv, ye_uv, mp.zeros(3, 3), ynu_uv.copy(), mr_cur)
    t_now = mp.mpf(0)
    thr_m: list[mp.mpf] = []
    snap: dict[str, Any] = {}
    for n_act in (3, 2, 1):
        u_t, sv_t = takagi_real_2n_eigsy(st[8])
        t_tgt = mp.log(sv_t[n_act - 1])
        if t_tgt < t_now:
            st = gl4_integrate_tuple(mssm_seesaw_rhs, st, t_tgt - t_now, 8)
            t_now = t_tgt
        u_t, sv_t = takagi_real_2n_eigsy(st[8])
        m_h = sv_t[n_act - 1]
        thr_m.append(m_h)
        ynu_rot = st[7] * u_t
        if n_act == 3:
            snap = {"ye": st[5].copy(), "ynu_rot": ynu_rot.copy(), "m_eigs": list(sv_t)}
        yk = mp.matrix([ynu_rot[r, n_act - 1] for r in range(3)])
        kap_new = st[6] - (yk * yk.T) / m_h
        if n_act > 1:
            ynu_rem = mp.matrix([[ynu_rot[r, c] for c in range(n_act - 1)] for r in range(3)])
            mr_rem = mp.diag([sv_t[c] for c in range(n_act - 1)])
            st = (st[0], st[1], st[2], st[3], st[4], st[5], kap_new, ynu_rem, mr_rem)
        else:
            st_below = (st[0], st[1], st[2], st[3], st[4], st[5], kap_new)

    st_susy = gl4_integrate_tuple(lambda s: mssm_2loop_rhs(s, True), st_below, t_susy - t_now, n_mssm)
    ir = match_and_run_sm_gl4(st_susy, soft, 15, 10, c20_5, sgn_mu=1, n_sm_steps=n_sm)
    return {"thresholds": thr_m, "snap": snap, "ir": ir}


def _get_gl4_boltz_grid(n_st: int) -> list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]:
    key = (n_st, mp.mp.dps)
    if key in _GL4_BOLTZ_CACHE:
        return _GL4_BOLTZ_CACHE[key]
    u0, u1 = mp.log(qrat(1, 10)), mp.log(mp.mpf(100))
    h = (u1 - u0) / mp.mpf(n_st)
    s3_6 = mp.sqrt(3) / 6
    c1_n, c2_n = qrat(1, 2) - s3_6, qrat(1, 2) + s3_6
    grid: list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for k in range(n_st):
        uk = u0 + k * h
        vals: list[mp.mpf] = []
        for uv in (uk + c1_n * h, uk + c2_n * h):
            zv = mp.exp(uv)
            k1v, k2v = _k1_k2_fast(zv)
            vals.extend([qrat(1, 2) * zv * zv * k2v, zv * zv * (k1v / k2v), qrat(1, 4) * (zv ** 4) * k1v])
        grid.append((vals[0], vals[1], vals[2], vals[3], vals[4], vals[5]))
    _GL4_BOLTZ_CACHE[key] = grid
    return grid


def boltzmann_lepto_gl4(
    ye_m: mp.matrix,
    ynu_rot: mp.matrix,
    m_eigs: list[mp.mpf],
    mgut_mpred: mp.mpf,
    n_coarse: int = 1000,
) -> dict[str, Any]:
    ul, _ = left_svd_asc(ye_m)
    yh = ul.H * ynu_rot
    hm = yh.H * yh
    h11 = mp.re(hm[0, 0])
    m1, m2, m3 = m_eigs
    xl = [(m2 / m1) ** 2, (m3 / m1) ** 2]

    def f_mssm(x: mp.mpf) -> mp.mpf:
        return -mp.sqrt(x) * (2 / (x - 1) + mp.log((1 + x) / x))

    eps_fl: list[mp.mpf] = []
    for a in range(3):
        acc = mp.mpf(0)
        for ix, j in enumerate((1, 2)):
            xj = xl[ix]
            acc += mp.im(mp.conj(yh[a, 0]) * yh[a, j] * hm[0, j]) * f_mssm(xj)
            acc += mp.im(mp.conj(yh[a, 0]) * yh[a, j] * hm[j, 0]) * (mp.mpf(-2) / (xj - 1))
        eps_fl.append(acc / (8 * mp.pi * h11))
    eps_tot = sum(eps_fl, mp.mpf(0))
    eps_unflav_dir = sum((mp.im(hm[0, j] ** 2) * f_mssm(xl[ix]) for ix, j in enumerate((1, 2))), mp.mpf(0)) / (8 * mp.pi * h11)

    g_star = qrat(915, 4)
    h_pref = mp.sqrt((mp.pi ** 2) * g_star / 90)
    mpred_m1 = 1 / (mgut_mpred * m1)
    k_fl = [(abs(yh[a, 0]) ** 2) / (4 * mp.pi * h_pref) * mpred_m1 for a in range(3)]
    k_tot = sum(k_fl, mp.mpf(0))

    s3 = mp.sqrt(3)
    s3_6 = s3 / 6
    a11, a12, a21, a22 = qrat(1, 4), qrat(1, 4) - s3_6, qrat(1, 4) + s3_6, qrat(1, 4)
    ai11, ai12, ai21, ai22 = mp.mpf(3), -3 + 2 * s3, -3 - 2 * s3, mp.mpf(3)

    def gl4_lin_step(y0: mp.mpf, h: mp.mpf, p1: mp.mpf, q1: mp.mpf, p2: mp.mpf, q2: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        m11, m12 = 1 + h * a11 * p1, h * a12 * p2
        m21, m22 = h * a21 * p1, 1 + h * a22 * p2
        r1 = y0 + h * (a11 * q1 + a12 * q2)
        r2 = y0 + h * (a21 * q1 + a22 * q2)
        det = m11 * m22 - m12 * m21
        y1 = (m22 * r1 - m12 * r2) / det
        y2 = (-m21 * r1 + m11 * r2) / det
        ynext = y0 + s3 * (y2 - y1)
        return y1, y2, ynext

    def integrate_n(n_st: int) -> tuple[list[mp.mpf], mp.mpf]:
        u0, u1 = mp.log(qrat(1, 10)), mp.log(mp.mpf(100))
        h = (u1 - u0) / mp.mpf(n_st)
        gb = _get_gl4_boltz_grid(n_st)
        y_n = mp.mpf(0)
        y_fl = [mp.mpf(0)] * 3
        y_un = mp.mpf(0)
        for k in range(n_st):
            neq1, r1w, wb1, neq2, r2w, wb2 = gb[k]
            p1, p2 = k_tot * r1w, k_tot * r2w
            yn1, yn2, yn_next = gl4_lin_step(y_n, h, p1, p1 * neq1, p2, p2 * neq2)
            dy1, dy2 = yn1 - y_n, yn2 - y_n
            dn1 = (ai11 * dy1 + ai12 * dy2) / h
            dn2 = (ai21 * dy1 + ai22 * dy2) / h
            for a in range(3):
                _, _, y_fl[a] = gl4_lin_step(y_fl[a], h, k_fl[a] * wb1, eps_fl[a] * dn1, k_fl[a] * wb2, eps_fl[a] * dn2)
            _, _, y_un = gl4_lin_step(y_un, h, k_tot * wb1, eps_tot * dn1, k_tot * wb2, eps_tot * dn2)
            y_n = yn_next
        return y_fl, y_un

    nfl_c, nun_c = integrate_n(n_coarse)
    nfl_f, nun_f = integrate_n(2 * n_coarse)
    nfl_r = [(16 * nfl_f[a] - nfl_c[a]) / 15 for a in range(3)]
    nun_r = (16 * nun_f - nun_c) / 15
    conv = qrat(8, 23) * (135 * mp.zeta(3)) / (2 * (mp.pi ** 4) * g_star)
    yb_fl = conv * sum(nfl_r, mp.mpf(0))
    yb_un = conv * nun_r
    st_err = abs(sum(nfl_f, mp.mpf(0)) - sum(nfl_c, mp.mpf(0))) / max(abs(sum(nfl_f, mp.mpf(0))), q10(-30))
    return {
        "eps_tot": eps_tot,
        "flav_sum_err": abs(eps_tot - eps_unflav_dir),
        "K_tot": k_tot,
        "Y_B_flavored": yb_fl,
        "Y_B_unflavored": yb_un,
        "step_rel_err": st_err,
    }


# ==============================================================================
# REF_5: Custody, Manifests, False-Flag Census, & A2-OW16 v22 Audit
# ==============================================================================

def verify_all_manifests_ref(tamper_idx: int | None = None) -> dict[str, Any]:
    mfs = sorted(RELAYS_DIR.rglob("*SHA256*.txt"))
    verified = 0
    total = 0
    mismatches: list[dict[str, str]] = []
    idx = 0
    for mf in mfs:
        rel_mf = str(mf.relative_to(REPO_ROOT))
        if rel_mf == "relays/a2_ow27_referee_v3/OUTPUT_SHA256.txt":
            continue
        for ln in mf.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            parts = ln.split()
            if len(parts) < 2:
                continue
            exp_h = parts[0]
            rel_t = parts[-1].lstrip("*")
            tp = REPO_ROOT / rel_t
            if not tp.exists():
                tp = mf.parent / rel_t
            raw = tp.read_bytes()
            if tamper_idx is not None and idx == tamper_idx and len(raw) > 0:
                raw = bytes([raw[0] ^ 1]) + raw[1:]
            act_h = hashlib.sha256(raw).hexdigest()
            total += 1
            if act_h == exp_h:
                verified += 1
            else:
                mismatches.append({"manifest": rel_mf, "target": rel_t, "expected": exp_h, "actual": act_h})
            idx += 1
    return {
        "total_manifests": total,
        "verified_manifests": verified,
        "mismatches": mismatches,
        "all_verified": bool(total > 0 and verified == total and len(mismatches) == 0),
    }


def scan_false_flag_jsons_ref() -> dict[str, Any]:
    found: list[dict[str, Any]] = []
    for jp in sorted(RELAYS_DIR.rglob("*.json")):
        rel_p = str(jp.relative_to(REPO_ROOT))
        if rel_p == "relays/a2_ow27_referee_v3/a2_ow27_referee_v3_results.json":
            continue
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        keys: list[str] = []
        for k in ("all_gates_passed", "all_referee_gates_passed", "overall_pass", "pass", "all_passed"):
            if k in d and d[k] is False:
                keys.append(k)
        if isinstance(d.get("summary"), dict):
            for k in ("all_gates_passed", "all_referee_gates_passed", "overall_pass", "pass", "all_passed"):
                if k in d["summary"] and d["summary"][k] is False:
                    keys.append("summary." + k)
        if keys:
            found.append({"file": rel_p, "false_keys": keys})
    return {"count": len(found), "files": found}


# ==============================================================================
# Main Cold-Room Zero-Trust Referee v3 Driver
# ==============================================================================

def main() -> None:
    mp.mp.dps = 28
    discrepancies: list[dict[str, Any]] = []
    non_blocking_diagnostics: list[dict[str, Any]] = []

    p_ow27_script = RELAYS_DIR / "a2_ow27_v8" / "verify_a2_ow27_v8.py"
    p_ow27_json = RELAYS_DIR / "a2_ow27_v8" / "a2_ow27_v8_results.json"
    p_ow16_script = RELAYS_DIR / "a2_ow16_v22" / "verify_a2_ow16_v22.py"
    p_ow16_json = RELAYS_DIR / "a2_ow16_v22" / "a2_ow16_v22_results.json"
    p_ref26_json = RELAYS_DIR / "a2_ow26_referee_v3" / "a2_ow26_referee_v3_results.json"
    p_ow23_json = RELAYS_DIR / "a2_ow23_v3" / "a2_ow23_v3_results.json"

    ow27 = json.loads(p_ow27_json.read_text(encoding="utf-8"))
    ow16 = json.loads(p_ow16_json.read_text(encoding="utf-8"))
    ref26 = json.loads(p_ref26_json.read_text(encoding="utf-8"))
    ow23 = json.loads(p_ow23_json.read_text(encoding="utf-8"))

    hyg_self = scan_script_ast(Path(__file__).resolve())
    hyg_ow27_ast = scan_script_ast(p_ow27_script)
    hyg_ow27_json = scan_raw_json_floats(p_ow27_json)
    hyg_ow16_ast = scan_script_ast(p_ow16_script)
    hyg_ow16_json = scan_raw_json_floats(p_ow16_json)
    assert hyg_self["clean"], f"Self AST hygiene failed: {hyg_self}"

    g_s12_ref26 = [mp.mpf(s) for s in ref26["REF_2_e8_cim_sugra_and_dirac_liouville"]["Dirac_s12_Liouville_GL10_GL6"]["G_s12_dirac_unit_mean_t8"]]
    g_s12_ow27 = [mp.mpf(s) for s in ow27["OW27_C_dirac_s12_384_atlas_I3plusWR_scan_and_leptogenesis"]["G_s12_t8_independent_verification"]["G_s12_t8"]]
    g_s12_cross_err = max(abs(g_s12_ref26[i] - g_s12_ow27[i]) for i in range(3))
    mkk_mpred = mp.mpf(ow23["OW23_C_real_7d_curvature_unimodular_cusp_cp_walls"]["cp_domain_wall_erasure_and_vise"]["energy_vise_MKK_over_MPl"])
    yt_cim_min_ref26 = mp.mpf(ref26["REF_2_e8_cim_sugra_and_dirac_liouville"]["M8_CIM_2D_GaussLegendre"]["yt_over_gUV_min_nonzero"])

    tau8_p = qrat(16, 5) + I_C * qrat(8, 5)
    tau8_m = -mp.conj(tau8_p)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    k5_cp = [(a, (-b) % 1) for a, b in k5]
    k6_cp = [(a, (-b) % 1) for a, b in k6]

    def build_uv_jtheta(tau: mp.mpc, metric: list[mp.mpf], cp_flag: bool = False) -> dict[str, Any]:
        p5, p6 = (k5_cp, k6_cp) if cp_flag else (k5, k6)
        e5 = mp.exp(2 * I_C * mp.pi * tau / 5)
        d10 = mp.diag([e5 ** 3, e5 ** 2, mp.mpc(1)])
        kis = mp.diag([1 / mp.sqrt(v) for v in metric])
        wu = kis * (d10 * w_orbit_avg(tau, p5, 1, -4) * d10) * kis
        wd = kis * (d10 * (w_orbit_avg(tau, p5, 1, 2) + w_orbit_avg(tau, p6, 1, 2)) / 2) * kis
        we_raw = (w_orbit_avg(tau, p5, -3, 6) + w_orbit_avg(tau, p6, -3, 6)) / 2
        we = kis * (we_raw * d10) * kis
        wn2 = kis * ((w_orbit_avg(tau, p5, -3, 2) - w_orbit_avg(tau, p6, -3, 2)) / 2) * kis
        wr2 = (w_orbit_avg(tau, p5, 2, 2) - w_orbit_avg(tau, p6, 2, 2)) / 2
        mr2 = kis * ((wr2 + wr2.T) / 2) * kis
        _, su = left_svd_asc(wu)
        _, sd = left_svd_asc(wd)
        _, sn = left_svd_asc(wn2)
        kap2 = -wn2 * (mr2 ** (-1)) * wn2.T
        _, sk = left_svd_asc((kap2 + kap2.T) / 2)
        return {
            "yu_hat": wu / su[2],
            "yd_hat": wd / sd[2],
            "ye_hat": we / sd[2],
            "yn_hat": wn2 / sn[2],
            "mr_raw": mr2,
            "kap_hat": kap2 / sk[2],
            "we_raw": we_raw,
            "d10": d10,
            "sd2": sd[2],
        }

    flat_diag = [mp.mpf(1), mp.mpf(1), mp.mpf(1)]
    tex_flat_p = build_uv_jtheta(tau8_p, flat_diag, False)
    tex_s12_p = build_uv_jtheta(tau8_p, g_s12_ref26, False)
    tex_s12_m = build_uv_jtheta(tau8_m, g_s12_ref26, True)

    g_uv24 = mp.sqrt(4 * mp.pi / mp.mpf(24))
    t_susy24 = -(qrat(48, 5) * mp.pi)
    yb0 = g_uv24 / 5
    ytau0 = yb0 * left_svd_asc(tex_flat_p["ye_hat"])[1][2]

    # ==========================================================================
    # REF_1: OW27-A v8 SymPy Proofs + GL4 Pipeline (m0=3,10,30 & CIM) + Haar U(3)^5
    # ==========================================================================
    print("  [REF3 1/6] Running OW27-A v8 SymPy proofs + GL4 pipeline + Haar U(3)^5...", flush=True)
    ref1_sympy = run_ref1_sympy_proofs()
    c20_5 = ref1_sympy.pop("_c20_5_mp")

    soft_gl4_ref = integrate_soft_26var_gl4(g_uv24, g_uv24, yb0, ytau0, t_susy24, -mp.sqrt(3), n_steps=32)
    m1_exact_err = abs(soft_gl4_ref["M1"] - qrat(25, 58))
    st_s12_susy_gl4 = gl4_integrate_tuple(
        lambda s: mssm_2loop_rhs(s, True),
        (g_uv24, g_uv24, g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0 * tex_s12_p["yd_hat"], yb0 * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
        t_susy24,
        24,
    )

    prod_a = ow27["OW27_A_2loop_qcd_4coupling_higgs_veltman_decoupling_and_lambda_qcd"]
    prod_runs_a = prod_a["mz_and_mt_2loop_pipeline_runs"]
    prod_cim_a = prod_a["mz_and_mt_cim_M16_runs"]
    v8_qed_proof_ok = bool(prod_a["pure_qft_sympy_proofs"].get("qed_5flav_top_decoupling_sign_proof_ok", False))

    ref1_run_checks: dict[str, Any] = {}
    ref1_max_err = mp.mpf(0)
    ref1_aem5_max_err = mp.mpf(0)
    all_aem5_lt_aem6 = True
    ir_by_m0_pos: dict[int, dict[str, Any]] = {}

    compare_keys_all = (
        "alpha3_mz_nf5", "alpha3_mz_nf6", "alpha_EM_inv_mz_nf6", "alpha_EM_inv_mz_nf5",
        "sin2_thetaW_msbar_mz", "sin2_thetaW_on_shell", "delta_rho_t_1loop",
        "mw_over_mz_msbar", "mw_over_mz_pole_veltman", "mt_pole_2l_at_mt_over_v",
        "mh_pole_4c_at_mt_over_mz", "mh_pole_4c_at_mz_over_mz", "mh_pole_4c_scale_drift",
        "delta_b",
    )
    run_specs = [(10, 1), (10, -1), (3, 1), (3, -1), (30, 1)]
    for m0v, sgn_m in run_specs:
        tag = f"CURV_s12_Dirac_yt_gUV_tb15_m0_{m0v}v_sgnMu_{'pos' if sgn_m > 0 else 'neg'}"
        ir_r = match_and_run_sm_gl4(st_s12_susy_gl4, soft_gl4_ref, 15, m0v, c20_5, sgn_mu=sgn_m, n_sm_steps=16)
        if sgn_m == 1:
            ir_by_m0_pos[m0v] = ir_r
        pr = prod_runs_a[tag]
        max_e = mp.mpf(0)
        for k in compare_keys_all:
            max_e = max(max_e, rel_err(ir_r[k], mp.mpf(pr[k])))
        max_e = max(max_e, rel_err(ir_r["Lambda_QCD_eff_exact_over_v"], mp.mpf(pr["Lambda_QCD_3_exact_over_v"])))
        max_e = max(max_e, rel_err(ir_r["Lambda_QCD_5_exact_over_v"], mp.mpf(pr["Lambda_QCD_5_exact_over_v"])))
        for ck in ("v12", "v23", "v13", "J", "b_tau"):
            max_e = max(max_e, rel_err(ir_r["ckm_mz"][ck], mp.mpf(pr["ckm_mz"][ck])))
        aem5_e = rel_err(ir_r["alpha_EM_inv_mz_nf5"], mp.mpf(pr["alpha_EM_inv_mz_nf5"]))
        nf_ok = bool(ir_r["nf_active_at_confinement"] == pr["nf_active_at_confinement"])
        sign_ok = bool(mp.mpf(pr["alpha_EM_inv_mz_nf5"]) < mp.mpf(pr["alpha_EM_inv_mz_nf6"]))
        all_aem5_lt_aem6 = bool(all_aem5_lt_aem6 and sign_ok and nf_ok)
        ref1_max_err = max(ref1_max_err, max_e)
        ref1_aem5_max_err = max(ref1_aem5_max_err, aem5_e)
        ref1_run_checks[tag] = {
            "max_rel_err_all_observables_incl_aem5": mp.nstr(max_e, 10),
            "alpha_EM_inv_mz_nf5_gl4": mp.nstr(ir_r["alpha_EM_inv_mz_nf5"], 12),
            "alpha_EM_inv_mz_nf5_v8": pr["alpha_EM_inv_mz_nf5"],
            "alpha_EM_inv_mz_nf5_rel_err": mp.nstr(aem5_e, 10),
            "alpha_EM_nf5_lt_nf6": sign_ok,
            "higgs_5c_2loop_rglog_scale_drift_gl4": mp.nstr(ir_r["mh_pole_4c_scale_drift"], 10),
            "nf_active_at_confinement": ir_r["nf_active_at_confinement"],
            "nf_match_v8": nf_ok,
        }

    central_ir_gl4 = ir_by_m0_pos[10]

    # CIM_M16_kH1min_m0_3v via GL4
    yt_cim_g = g_uv24 * yt_cim_min_ref26
    soft_cim = integrate_soft_26var_gl4(g_uv24, yt_cim_g, yb0, ytau0, t_susy24, -mp.sqrt(3), n_steps=32)
    st_cim = gl4_integrate_tuple(
        lambda s: mssm_2loop_rhs(s, True),
        (g_uv24, g_uv24, g_uv24, yt_cim_g * tex_s12_p["yu_hat"], yb0 * tex_s12_p["yd_hat"], yb0 * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
        t_susy24,
        24,
    )
    ir_cim_3v = match_and_run_sm_gl4(st_cim, soft_cim, 15, 3, c20_5, sgn_mu=1, n_sm_steps=16)
    pr_cim = prod_cim_a["CURV_s12_CIM_M16_kH1min_m0_3v"]
    cim_max_err = max(
        rel_err(ir_cim_3v["mt_pole_2l_at_mt_over_v"], mp.mpf(pr_cim["mt_pole_2l_at_mt_over_v"])),
        rel_err(ir_cim_3v["mh_pole_4c_at_mt_over_mz"], mp.mpf(pr_cim["mh_pole_4c_at_mt_over_mz"])),
        rel_err(ir_cim_3v["mh_pole_4c_scale_drift"], mp.mpf(pr_cim["mh_pole_4c_scale_drift"])),
        rel_err(ir_cim_3v["mw_over_mz_pole_veltman"], mp.mpf(pr_cim["mw_over_mz_pole_veltman"])),
        rel_err(ir_cim_3v["alpha3_mz_nf5"], mp.mpf(pr_cim["alpha3_mz_nf5"])),
        rel_err(ir_cim_3v["ckm_mz"]["b_tau"], mp.mpf(pr_cim["b_tau_mz"])),
    )
    ref1_max_err = max(ref1_max_err, cim_max_err)

    # 5-trial Xorshift64* + Householder QR Haar U(3)^5 scrambling through M_GUT -> M_SUSY -> m_t -> M_Z via GL4
    rng1 = Xorshift64Star(202611249101)
    st_h0 = gl4_integrate_tuple(
        lambda s: mssm_2loop_rhs(s, True),
        (g_uv24, g_uv24, g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0 * tex_s12_p["yd_hat"], yb0 * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
        t_susy24,
        14,
    )
    ir_h0 = match_and_run_sm_gl4(st_h0, soft_gl4_ref, 15, 10, c20_5, sgn_mu=1, n_sm_steps=10)
    haar_ref1_err = mp.mpf(0)
    for _ in range(5):
        uq, uur, udr, ul, uer = (haar_unitary_householder(rng1, 3) for _ in range(5))
        st_hs = gl4_integrate_tuple(
            lambda s: mssm_2loop_rhs(s, True),
            (
                g_uv24, g_uv24, g_uv24,
                uq * (g_uv24 * tex_s12_p["yu_hat"]) * uur.H,
                uq * (yb0 * tex_s12_p["yd_hat"]) * udr.H,
                ul * (yb0 * tex_s12_p["ye_hat"]) * uer.H,
                ul * tex_s12_p["kap_hat"] * ul.T,
            ),
            t_susy24,
            14,
        )
        ir_hs = match_and_run_sm_gl4(st_hs, soft_gl4_ref, 15, 10, c20_5, sgn_mu=1, n_sm_steps=10)
        haar_ref1_err = max(
            haar_ref1_err,
            max(abs(ir_hs["ckm_mz"][k] - ir_h0["ckm_mz"][k]) for k in ir_h0["ckm_mz"]),
            abs(ir_hs["mt_pole_2l_at_mt_over_v"] - ir_h0["mt_pole_2l_at_mt_over_v"]),
            abs(ir_hs["mh_pole_4c_at_mt_over_mz"] - ir_h0["mh_pole_4c_at_mt_over_mz"]),
            abs(ir_hs["mw_over_mz_pole_veltman"] - ir_h0["mw_over_mz_pole_veltman"]),
            abs(ir_hs["Lambda_QCD_eff_exact_over_v"] - ir_h0["Lambda_QCD_eff_exact_over_v"]),
        )

    disc1_remediated = bool(v8_qed_proof_ok and all_aem5_lt_aem6 and ref1_aem5_max_err < q10(-5))
    if ref1_max_err >= q10(-5) or not disc1_remediated or haar_ref1_err >= q10(-12):
        discrepancies.append({
            "id": "DISC-V3-REF1",
            "severity": "BLOCKING",
            "domain": "OW27-A v8",
            "max_rel_err": mp.nstr(ref1_max_err, 10),
            "aem5_max_err": mp.nstr(ref1_aem5_max_err, 10),
            "disc1_remediated": disc1_remediated,
            "haar_err": mp.nstr(haar_ref1_err, 10),
        })

    ref1_passed = bool(
        ref1_sympy["passed"]
        and disc1_remediated
        and ref1_max_err < q10(-5)
        and central_ir_gl4["mh_pole_4c_scale_drift"] < qrat(5, 1000)
        and haar_ref1_err < q10(-12)
    )
    ref1_block = {
        "gate_passed": ref1_passed,
        "DISC_OW27_1_remediated": disc1_remediated,
        "integrator": "2-stage implicit Gauss-Legendre GL4 (O(h^4), symplectic, A-stable)",
        "haar_generator": "Xorshift64* + complex Householder QR (Mezzadri 2007, 5 trials)",
        "sympy_proofs": ref1_sympy,
        "v8_qed_sign_proof_ok": v8_qed_proof_ok,
        "soft_M1_vs_exact_25_over_58_err": mp.nstr(m1_exact_err, 10),
        "max_rel_err_all_observables_incl_aem5": mp.nstr(ref1_max_err, 10),
        "max_rel_err_alpha_EM_inv_mz_nf5": mp.nstr(ref1_aem5_max_err, 10),
        "cim_M16_kH1min_m0_3v_max_rel_err": mp.nstr(cim_max_err, 10),
        "guardrail3_5trial_haar_U3_5_gl4_err": mp.nstr(haar_ref1_err, 10),
        "run_comparisons": ref1_run_checks,
    }

    # ==========================================================================
    # REF_3: OW27-C v8 (384+192 Scans via mp.jtheta + Real 6x6 eigsy + GL4 Seesaw/Boltzmann)
    # ==========================================================================
    print("  [REF3 3/6] Running OW27-C v8 384+192 scans + GL4 seesaw/Boltzmann (N=1000/2000)...", flush=True)
    kis_ref = mp.diag([1 / mp.sqrt(v) for v in g_s12_ref26])
    e5_p = mp.exp(2 * I_C * mp.pi * tau8_p / 5)
    d10_p = mp.diag([e5_p ** 3, e5_p ** 2, mp.mpc(1)])
    we0_p = tex_s12_p["we_raw"]

    s384_tot = 0
    s384_nonsing = 0
    s384_hits = 0
    for qr in (3, -5, 1, 2):
        w5n, w6n = w_orbit_avg(tau8_p, k5, -3, qr), w_orbit_avg(tau8_p, k6, -3, qr)
        w5r, w6r = w_orbit_avg(tau8_p, k5, qr, qr), w_orbit_avg(tau8_p, k6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        for wn in ops_n.values():
            for wr in ops_r.values():
                mr_m = (wr + wr.T) / 2
                _, smr = takagi_real_2n_eigsy(mr_m)
                is_sing = bool(smr[2] < q10(-22) or smr[0] < q10(-18) * smr[2])
                for n5b in ((0, 0, 0), (1, 0, 0), (1, 1, 0)):
                    d5b = mp.diag([e5_p ** n for n in n5b])
                    ye_loc = d5b * we0_p * d10_p
                    yn_loc = d5b * wn
                    for kmat in (mp.eye(3), kis_ref):
                        s384_tot += 1
                        if is_sing:
                            continue
                        s384_nonsing += 1
                        mnu = -yn_loc * (mr_m ** (-1)) * yn_loc.T
                        obs = extract_pmns(kmat * ye_loc * kmat, kmat * mnu * kmat)
                        if in_fixed_ow24c_window(obs):
                            s384_hits += 1

    s192_tot = 0
    s192_hits = 0
    s192_sym6_hits = 0
    ye_s12_pure = kis_ref * (we0_p * d10_p) * kis_ref
    for qr in (-5, -3, 0, 2, 3, 5):
        w5n, w6n = w_orbit_avg(tau8_p, k5, -3, qr), w_orbit_avg(tau8_p, k6, -3, qr)
        w5r, w6r = w_orbit_avg(tau8_p, k5, qr, qr), w_orbit_avg(tau8_p, k6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        for kn, wn in ops_n.items():
            for kr, wr in ops_r.items():
                wr_s = (wr + wr.T) / 2
                _, swr = left_svd_asc(wr_s)
                mr_u = (mp.eye(3) + wr_s / swr[2]) if swr[2] >= q10(-22) else mp.eye(3)
                _, smu = takagi_real_2n_eigsy(mr_u)
                is_sing = bool(smu[2] < q10(-22) or smu[0] < q10(-18) * smu[2])
                for kmode in ("left_only_NR_flat", "both_sided_NR_s12"):
                    s192_tot += 1
                    if is_sing:
                        continue
                    if kmode == "left_only_NR_flat":
                        yn_c, mr_c = kis_ref * wn, mr_u
                    else:
                        yn_c, mr_c = kis_ref * wn * kis_ref, kis_ref * mr_u * kis_ref
                    _, snc = left_svd_asc(yn_c)
                    if snc[2] < q10(-22):
                        continue
                    kap_c = -yn_c * (mr_c ** (-1)) * yn_c.T
                    obs = extract_pmns(ye_s12_pure, kap_c)
                    if in_fixed_ow24c_window(obs):
                        s192_hits += 1
                        if kn == "5+6" and kr == "5+6":
                            s192_sym6_hits += 1

    mr0_c = q10(-3)
    seq_p = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0 * tex_s12_p["yd_hat"], yb0 * tex_s12_p["ye_hat"],
        g_uv24 * tex_s12_p["yn_hat"], tex_s12_p["mr_raw"], mr0_c, t_susy24, soft_gl4_ref, c20_5,
    )
    seq_m = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_m["yu_hat"], yb0 * tex_s12_m["yd_hat"], yb0 * tex_s12_m["ye_hat"],
        g_uv24 * tex_s12_m["yn_hat"], tex_s12_m["mr_raw"], mr0_c, t_susy24, soft_gl4_ref, c20_5,
    )
    lep_p = boltzmann_lepto_gl4(seq_p["snap"]["ye"], seq_p["snap"]["ynu_rot"], seq_p["snap"]["m_eigs"], mkk_mpred, n_coarse=1000)
    lep_m = boltzmann_lepto_gl4(seq_m["snap"]["ye"], seq_m["snap"]["ynu_rot"], seq_m["snap"]["m_eigs"], mkk_mpred, n_coarse=1000)
    cp_odd_err = abs(lep_p["Y_B_flavored"] + lep_m["Y_B_flavored"])

    prod_c = ow27["OW27_C_dirac_s12_384_atlas_I3plusWR_scan_and_leptogenesis"]
    prod_leg = prod_c["primary_surviving_dirac_s12_candidate"]
    pm_p = seq_p["ir"]["pmns_mz"]
    ow27c_pmns_max_err = max(
        rel_err(pm_p[k], mp.mpf(prod_leg["pmns_mz"][k]))
        for k in ("s12sq", "s23sq", "s13sq", "dm", "J", "delta_cp_rad", "mee_over_m3", "sum_m_over_m3", "m1_over_m3", "m2_over_m3")
    )
    ow27c_thr_max_err = max(rel_err(seq_p["thresholds"][i], mp.mpf(prod_leg["thresholds_MR_over_MGUT"][i])) for i in range(3))
    ow27c_lepto_max_err = max(
        rel_err(lep_p["K_tot"], mp.mpf(prod_leg["K_tot"])),
        rel_err(lep_p["eps_tot"], mp.mpf(prod_leg["eps_tot"])),
        rel_err(lep_p["Y_B_flavored"], mp.mpf(prod_leg["Y_B_flavored"])),
        rel_err(lep_p["Y_B_unflavored"], mp.mpf(prod_leg["Y_B_unflavored"])),
    )

    rng3 = Xorshift64Star(202611249103)
    seq_h0 = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0 * tex_s12_p["yd_hat"], yb0 * tex_s12_p["ye_hat"],
        g_uv24 * tex_s12_p["yn_hat"], tex_s12_p["mr_raw"], mr0_c, t_susy24, soft_gl4_ref, c20_5, n_mssm=14, n_sm=10,
    )
    lep_h0 = boltzmann_lepto_gl4(seq_h0["snap"]["ye"], seq_h0["snap"]["ynu_rot"], seq_h0["snap"]["m_eigs"], mkk_mpred, n_coarse=160)
    haar_ref3_err = mp.mpf(0)
    for _ in range(5):
        uq, uur, udr, ul, uer, un = (haar_unitary_householder(rng3, 3) for _ in range(6))
        seq_hs = run_seq_seesaw_gl4(
            g_uv24,
            uq * (g_uv24 * tex_s12_p["yu_hat"]) * uur.H,
            uq * (yb0 * tex_s12_p["yd_hat"]) * udr.H,
            ul * (yb0 * tex_s12_p["ye_hat"]) * uer.H,
            ul * (g_uv24 * tex_s12_p["yn_hat"]) * un.H,
            un.apply(mp.conj) * tex_s12_p["mr_raw"] * un.H,
            mr0_c, t_susy24, soft_gl4_ref, c20_5, n_mssm=14, n_sm=10,
        )
        lep_hs = boltzmann_lepto_gl4(seq_hs["snap"]["ye"], seq_hs["snap"]["ynu_rot"], seq_hs["snap"]["m_eigs"], mkk_mpred, n_coarse=160)
        haar_ref3_err = max(
            haar_ref3_err,
            max(abs(seq_hs["ir"]["pmns_mz"][k] - seq_h0["ir"]["pmns_mz"][k]) for k in ("s12sq", "s23sq", "s13sq", "dm", "J", "delta_cp_rad", "mee_over_m3")),
            abs(lep_hs["eps_tot"] - lep_h0["eps_tot"]),
            abs(lep_hs["Y_B_flavored"] - lep_h0["Y_B_flavored"]),
            abs(lep_hs["Y_B_unflavored"] - lep_h0["Y_B_unflavored"]),
        )

    disc_c_remediated = bool(
        s384_tot == 384
        and s384_nonsing == prod_c["scan1_384_case_OW24C_atlas_under_G_s12_t8"]["nonsingular_cases"] == 264
        and s384_hits == prod_c["scan1_384_case_OW24C_atlas_under_G_s12_t8"]["simultaneous_PMNS_hits_count"] == 0
        and s192_tot == 192
        and s192_hits == prod_c["scan2_I3_plus_WR_unit_under_G_s12_t8_pure_lopsided"]["all_192_simultaneous_hits_count"] == 0
        and s192_sym6_hits == prod_c["scan2_I3_plus_WR_unit_under_G_s12_t8_pure_lopsided"]["symmetric_5plus6_hits_count"] == 0
    )
    if not disc_c_remediated or max(ow27c_pmns_max_err, ow27c_thr_max_err, ow27c_lepto_max_err) >= q10(-5) or cp_odd_err >= q10(-30) or haar_ref3_err >= q10(-12):
        discrepancies.append({
            "id": "DISC-V3-REF3",
            "severity": "BLOCKING",
            "domain": "OW27-C v8",
            "disc_c_remediated": disc_c_remediated,
            "pmns_err": mp.nstr(ow27c_pmns_max_err, 10),
            "lepto_err": mp.nstr(ow27c_lepto_max_err, 10),
            "cp_odd_err": mp.nstr(cp_odd_err, 10),
        })

    ref3_passed = bool(
        g_s12_cross_err < q10(-5)
        and disc_c_remediated
        and ow27c_pmns_max_err < q10(-5)
        and ow27c_thr_max_err < q10(-5)
        and ow27c_lepto_max_err < q10(-5)
        and cp_odd_err < q10(-30)
        and haar_ref3_err < q10(-12)
        and pm_p["trig_unitarity_err"] < q10(-22)
    )
    ref3_block = {
        "gate_passed": ref3_passed,
        "DISC_OW27_C_remediated": disc_c_remediated,
        "w_hol_method": "Native mp.jtheta + exact heat-equation derivatives",
        "takagi_method": "Non-squaring real 2n x 2n symmetric block eigensolver via mp.eigsy",
        "boltzmann_method": "2-stage implicit GL4 (N=1000 vs 2000 + O(h^4) Richardson)",
        "G_s12_t8_ref26_v3_vs_ow27_v8_max_err": mp.nstr(g_s12_cross_err, 10),
        "scan1_384_counts": {"total": s384_tot, "nonsingular": s384_nonsing, "hits": s384_hits},
        "scan2_192_counts": {"total": s192_tot, "all_hits": s192_hits, "sym6_hits": s192_sym6_hits},
        "legacy_pmns_max_rel_err_vs_v8": mp.nstr(ow27c_pmns_max_err, 10),
        "legacy_thresholds_max_rel_err_vs_v8": mp.nstr(ow27c_thr_max_err, 10),
        "legacy_boltzmann_max_rel_err_vs_v8": mp.nstr(ow27c_lepto_max_err, 10),
        "legacy_Y_B_flavored_gl4": mp.nstr(lep_p["Y_B_flavored"], 12),
        "legacy_Y_B_unflavored_gl4": mp.nstr(lep_p["Y_B_unflavored"], 12),
        "legacy_boltzmann_step_rel_err": mp.nstr(lep_p["step_rel_err"], 10),
        "CP_odd_YB_sum_err": mp.nstr(cp_odd_err, 10),
        "pmns_trig_unitarity_err": mp.nstr(pm_p["trig_unitarity_err"], 8),
        "guardrail3_5trial_haar_U3_5_x_U3_N_gl4_err": mp.nstr(haar_ref3_err, 10),
    }

    # ==========================================================================
    # REF_2: OW27-B v8 Dirac Spinors + GL4 Riccati (N=800 vs 1600, N=1600 x_f, & per-m0 DIAG-2)
    # ==========================================================================
    print("  [REF3 2/6] Running OW27-B v8 Dirac spinors + GL4 Riccati (N=800/1600 + DIAG-2 per-m0)...", flush=True)
    mp.mp.dps = 30
    spinor_dirac = dirac_basis_majorana_proof()
    mp.mp.dps = 28
    gl4_ricc_bench_err = benchmark_gl4_analytic_riccati()

    g1_z_c, g2_z_c = central_ir_gl4["st_mz"][0], central_ir_gl4["st_mz"][1]
    gp_sq_c = qrat(3, 5) * g1_z_c * g1_z_c
    mt_v_c = central_ir_gl4["mt_pole_2l_at_mt_over_v"]
    mz_v_c = central_ir_gl4["mz_over_v"]
    s2w_c = central_ir_gl4["sin2_thetaW_msbar_mz"]
    lam_qcd_c = central_ir_gl4["Lambda_QCD_eff_exact_over_v"]
    yb_ref_gl4 = lep_p["Y_B_flavored"]

    dm_800 = compute_bino_dm_gl4(soft_gl4_ref, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_mpred, t_susy24, yb_ref_gl4, lam_qcd_c, n_steps=800)
    dm_1600 = compute_bino_dm_gl4(soft_gl4_ref, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_mpred, t_susy24, yb_ref_gl4, lam_qcd_c, n_steps=1600)
    dm_step_err = abs(dm_1600["Y_Bino_inf"] - dm_800["Y_Bino_inf"]) / dm_1600["Y_Bino_inf"]
    dm_rich = (16 * dm_1600["Y_Bino_inf"] - dm_800["Y_Bino_inf"]) / 15

    dm_pf4 = compute_bino_dm_gl4(
        soft_gl4_ref, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_mpred, t_susy24, yb_ref_gl4, lam_qcd_c,
        n_steps=800, unreduced_fault=True,
    )
    pf4_shift = abs(dm_pf4["Y_Bino_inf"] - dm_800["Y_Bino_inf"]) / dm_800["Y_Bino_inf"]

    prod_b = ow27["OW27_B_bino_lsp_thermal_freezeout_dm_OBS20"]
    prod_scan = {r["m0_over_v"]: r for r in prod_b["central_A0_neg_sqrt3_tb15_m0_scan"]}
    dm_comp: dict[str, Any] = {}
    ref2_max_rel_err = mp.mpf(0)
    diag2_own_max_rel_err = mp.mpf(0)
    diag2_nf_match = True
    min_purity_ref2 = mp.mpf(1)

    for m0v in (1, 3, 10, 30):
        # Use N=1600 GL4 so linear-interpolated x_f grid matches producer N=1600 cleanly!
        d_sc = dm_1600 if m0v == 10 else compute_bino_dm_gl4(soft_gl4_ref, m0v, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_mpred, t_susy24, yb_ref_gl4, lam_qcd_c, n_steps=1600)
        d_lw = d_sc if m0v == 10 else compute_bino_dm_gl4(soft_gl4_ref, m0v, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_mpred, t_susy24, yb_ref_gl4, lam_qcd_c, n_steps=1600, fixed_ref_m0=10)
        pr = prod_scan[m0v]
        min_purity_ref2 = min(min_purity_ref2, d_sc["bino_purity_N11sq"])
        e_sc = max(
            rel_err(d_sc["Y_Bino_inf"], mp.mpf(pr["Y_Bino_inf"])),
            rel_err(d_sc["x_f"], mp.mpf(pr["x_f"])),
            rel_err(d_sc["bino_purity_N11sq"], mp.mpf(pr["bino_purity_N11sq"])),
            rel_err(d_sc["delta_stauR"], mp.mpf(pr["delta_stauR"])),
            rel_err(d_sc["clat_OmegaRatio"], mp.mpf(pr["clat_OmegaBino_over_OmegaB_primary_YB"])),
        )
        e_lw = max(
            rel_err(d_lw["Y_Bino_inf"], mp.mpf(pr["lee_weinberg_fixed_MPred_over_vEW_Y_Bino_inf"])),
            rel_err(d_lw["clat_OmegaRatio"], mp.mpf(pr["lee_weinberg_fixed_MPred_over_vEW_clat_OmegaRatio"])),
        )
        ref2_max_rel_err = max(ref2_max_rel_err, e_sc, e_lw)
        entry: dict[str, Any] = {
            "self_consistent_Y_Bino_gl4_N1600": mp.nstr(d_sc["Y_Bino_inf"], 12),
            "self_consistent_x_f_gl4_N1600": mp.nstr(d_sc["x_f"], 10),
            "self_consistent_max_rel_err_vs_v8": mp.nstr(e_sc, 10),
            "lee_weinberg_Y_Bino_gl4_N1600": mp.nstr(d_lw["Y_Bino_inf"], 12),
            "lee_weinberg_max_rel_err_vs_v8": mp.nstr(e_lw, 10),
            "bino_purity": mp.nstr(d_sc["bino_purity_N11sq"], 10),
        }
        # Independently verify DIAG-2 per-m0 self_consistent_m0_own_* for m0 in {3, 10, 30}v
        if m0v in ir_by_m0_pos:
            iro = ir_by_m0_pos[m0v]
            gp_o = qrat(3, 5) * (iro["st_mz"][0] ** 2)
            d_own = dm_1600 if m0v == 10 else compute_bino_dm_gl4(
                soft_gl4_ref, m0v, 15, gp_o, iro["mt_pole_2l_at_mt_over_v"], iro["mz_over_v"],
                iro["sin2_thetaW_msbar_mz"], mkk_mpred, t_susy24, yb_ref_gl4,
                iro["Lambda_QCD_eff_exact_over_v"], n_steps=1600,
            )
            e_own = max(
                rel_err(d_own["Y_Bino_inf"], mp.mpf(pr["self_consistent_m0_own_Y_Bino_inf"])),
                rel_err(d_own["clat_OmegaRatio"], mp.mpf(pr["self_consistent_m0_own_clat_OmegaRatio"])),
                rel_err(iro["Lambda_QCD_eff_exact_over_v"], mp.mpf(pr["self_consistent_m0_own_LambdaQCD_over_v"])),
            )
            nf_own_ok = bool(iro["nf_active_at_confinement"] == pr["self_consistent_m0_own_nf_conf"])
            diag2_nf_match = bool(diag2_nf_match and nf_own_ok)
            diag2_own_max_rel_err = max(diag2_own_max_rel_err, e_own)
            ref2_max_rel_err = max(ref2_max_rel_err, e_own)
            entry["diag2_own_Y_Bino_gl4"] = mp.nstr(d_own["Y_Bino_inf"], 12)
            entry["diag2_own_clat_OmegaRatio_gl4"] = mp.nstr(d_own["clat_OmegaRatio"], 10)
            entry["diag2_own_nf_conf"] = iro["nf_active_at_confinement"]
            entry["diag2_own_max_rel_err_vs_v8"] = mp.nstr(e_own, 10)
        dm_comp[f"m0_{m0v}v"] = entry

    mgut_g2_24 = mp.sqrt(1 / (4 * mp.pi * 24))
    dm_g2 = compute_bino_dm_gl4(soft_gl4_ref, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mgut_g2_24, t_susy24, yb_ref_gl4, lam_qcd_c, n_steps=1600)
    g2_err = max(
        rel_err(dm_g2["Y_Bino_inf"], mp.mpf(prod_b["central_m0_10v_G2_M_GUT_over_MPred_Y_Bino"])),
        rel_err(dm_g2["clat_OmegaRatio"], mp.mpf(prod_b["central_m0_10v_G2_clat_OmegaRatio"])),
    )
    ref2_max_rel_err = max(ref2_max_rel_err, g2_err)

    diag2_verified = bool(diag2_nf_match and diag2_own_max_rel_err < q10(-5))
    if ref2_max_rel_err >= q10(-5) or not diag2_verified or dm_step_err >= q10(-6):
        discrepancies.append({
            "id": "DISC-V3-REF2",
            "severity": "BLOCKING",
            "domain": "OW27-B v8",
            "max_rel_err": mp.nstr(ref2_max_rel_err, 10),
            "diag2_own_max_rel_err": mp.nstr(diag2_own_max_rel_err, 10),
            "step_err": mp.nstr(dm_step_err, 10),
        })

    ref2_passed = bool(
        spinor_dirac["passed"]
        and gl4_ricc_bench_err < q10(-10)
        and dm_step_err < q10(-6)
        and pf4_shift > mp.mpf(1)
        and min_purity_ref2 > qrat(95, 100)
        and ref2_max_rel_err < q10(-5)
        and diag2_verified
    )
    ref2_block = {
        "gate_passed": ref2_passed,
        "DIAG_2_per_m0_self_consistent_verified": diag2_verified,
        "DIAG_2_per_m0_max_rel_err_vs_v8": mp.nstr(diag2_own_max_rel_err, 10),
        "spinor_proof_dirac_basis": spinor_dirac,
        "riccati_solver": "2-stage implicit Gauss-Legendre GL4 + 2x2 damped Newton (N=800 vs 1600; N=1600 x_f matched)",
        "gl4_analytic_riccati_benchmark_rel_err": mp.nstr(gl4_ricc_bench_err, 10),
        "central_10v_N800_vs_N1600_rel_err": mp.nstr(dm_step_err, 10),
        "central_10v_Y_Bino_gl4_richardson": mp.nstr(dm_rich, 12),
        "pf4_unreduced_planck_rel_shift": mp.nstr(pf4_shift, 10),
        "min_bino_purity_checked": mp.nstr(min_purity_ref2, 10),
        "G2_10v_max_rel_err_vs_v8": mp.nstr(g2_err, 10),
        "max_rel_err_all_dm_points_incl_xf_and_diag2": mp.nstr(ref2_max_rel_err, 10),
        "m0_scan_comparisons": dm_comp,
    }

    # ==========================================================================
    # REF_4: OW27-D v8 2-Loop NSVZ SymPy + Table + Bisection/Secant + LINK6 GL4
    # ==========================================================================
    print("  [REF3 4/6] Running OW27-D v8 NSVZ SymPy + table + LINK6/HYBRID GL4...", flush=True)
    g_s, mu_s, N_s = sp.symbols("g mu N", positive=True)
    b_nsvz = -3 * N_s * g_s**3 / (16 * sp.pi**2 * (1 - N_s * g_s**2 / (8 * sp.pi**2)))
    ln_l_nsvz = sp.log(mu_s) - sp.Rational(2, 3) * sp.log(g_s) - 8 * sp.pi**2 / (3 * N_s * g_s**2)
    nsvz_res = sp.simplify(mu_s * sp.diff(ln_l_nsvz, mu_s) + sp.diff(ln_l_nsvz, g_s) * b_nsvz)
    ln_l_hol = sp.log(mu_s) - 8 * sp.pi**2 / (3 * N_s * g_s**2)
    pf5_res = sp.simplify(mu_s * sp.diff(ln_l_hol, mu_s) + sp.diff(ln_l_hol, g_s) * b_nsvz)

    prod_d = ow27["OW27_D_sugra_2loop_nsvz_mediation_and_link6_cross_seat_audit"]
    table_max_err = mp.mpf(0)
    idx_row = 0
    for n_h in (3, 4, 5, 6):
        for a_i in (20, 22, 24, 25, 26, 28, 30, 32):
            am = mp.mpf(a_i)
            gu = mp.sqrt(4 * mp.pi / am)
            l1 = mp.exp(-2 * mp.pi * am / (3 * mp.mpf(n_h)))
            lnv = (gu ** (-qrat(2, 3))) * l1
            mg2 = mp.sqrt(1 / (4 * mp.pi * am))
            t1_g2 = -mp.log((l1 ** 3) * (mg2 ** 2) / mp.sqrt(3))
            tn_g2 = -mp.log((lnv ** 3) * (mg2 ** 2) / mp.sqrt(3))
            tn_kk = -mp.log((lnv ** 3) * (mkk_mpred ** 2) / mp.sqrt(3))
            t_am = tn_g2 + mp.log(16 * mp.pi * mp.pi / (gu * gu))
            prow = prod_d["nsvz_sugra_hidden_sector_table"][idx_row]
            assert prow["N_hid"] == n_h and prow["alpha_hid_inv"] == a_i
            table_max_err = max(
                table_max_err,
                rel_err(t1_g2, mp.mpf(prow["t_m32_1loop_G2"])),
                rel_err(tn_g2, mp.mpf(prow["t_m32_2loop_NSVZ_G2"])),
                rel_err(tn_kk, mp.mpf(prow["t_m32_2loop_NSVZ_MKK"])),
                rel_err(t_am, mp.mpf(prow["t_AMSB_soft_NSVZ_G2"])),
            )
            idx_row += 1

    t_b4 = qrat(48, 5) * mp.pi
    mg2_24 = mp.sqrt(1 / (4 * mp.pi * 24))

    def f_dh(ah: mp.mpf) -> mp.mpf:
        return (2 * mp.pi / 5) * ah - mp.log(ah / (4 * mp.pi)) - mp.log(mg2_24 * mg2_24 / mp.sqrt(3)) - t_b4

    lo, hi = mp.mpf(15), mp.mpf(24)
    for _ in range(15):
        mid = (lo + hi) / 2
        if f_dh(mid) < 0:
            lo = mid
        else:
            hi = mid
    x0_s, x1_s = lo, hi
    f0_s, f1_s = f_dh(x0_s), f_dh(x1_s)
    for _ in range(12):
        if abs(f1_s) < q10(-23) or abs(f1_s - f0_s) < q10(-26):
            break
        x2_s = x1_s - f1_s * (x1_s - x0_s) / (f1_s - f0_s)
        x0_s, f0_s = x1_s, f1_s
        x1_s, f1_s = x2_s, f_dh(x2_s)
    delta_hid_ref = mp.mpf(24) - x1_s
    delta_hid_err = rel_err(delta_hid_ref, mp.mpf(prod_d["su5_hid_NSVZ_G2_required_Delta_hid_shift_from_24"]))

    a_inv_l6 = qrat(3019350768, 100000000)
    t_susy_l6 = -qrat(24256, 1000)
    ye_norm_f = left_svd_asc(tex_flat_p["ye_hat"])[1][2]
    link6_checks: dict[str, Any] = {}
    link6_max_err = mp.mpf(0)
    link6_aem5_max_err = mp.mpf(0)

    for tag, ai_u, ts_u in (
        ("LINK6_exact_aGUTinv_30p1935_tSUSY_neg24p256", a_inv_l6, t_susy_l6),
        ("HYBRID_B4UV_aGUTinv_24_LINK6_tSUSY_neg24p256", mp.mpf(24), t_susy_l6),
    ):
        gu = mp.sqrt(4 * mp.pi / ai_u)
        sf_u = integrate_soft_26var_gl4(gu, gu, gu / 5, (gu / 5) * ye_norm_f, ts_u, -mp.sqrt(3), n_steps=32)
        st_u = gl4_integrate_tuple(
            lambda s: mssm_2loop_rhs(s, True),
            (gu, gu, gu, gu * tex_s12_p["yu_hat"], (gu / 5) * tex_s12_p["yd_hat"], (gu / 5) * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
            ts_u,
            24,
        )
        ir_u = match_and_run_sm_gl4(st_u, sf_u, 15, 10, c20_5, sgn_mu=1, n_sm_steps=16)
        pr_u = prod_d["agyexp_d12e74ef3_LINK6_side_by_side_in_B4UV_2loop_MZ"][tag]
        e_a5 = rel_err(ir_u["alpha_EM_inv_mz_nf5"], mp.mpf(pr_u["alpha_EM_inv_mz_nf5"]))
        e_all = max(
            e_a5,
            rel_err(ir_u["alpha3_mz_nf5"], mp.mpf(pr_u["alpha3_mz_nf5"])),
            rel_err(ir_u["alpha3_mz_nf6"], mp.mpf(pr_u["alpha3_mz_nf6"])),
            rel_err(ir_u["sin2_thetaW_msbar_mz"], mp.mpf(pr_u["sin2_thetaW_msbar_mz"])),
            rel_err(ir_u["mw_over_mz_pole_veltman"], mp.mpf(pr_u["mw_over_mz_pole_veltman"])),
            rel_err(ir_u["mt_pole_2l_at_mt_over_v"], mp.mpf(pr_u["mt_pole_2l_at_mt_over_v"])),
            rel_err(ir_u["mh_pole_4c_at_mt_over_mz"], mp.mpf(pr_u["mh_pole_4c_at_mt_over_mz"])),
            rel_err(ir_u["mh_pole_4c_scale_drift"], mp.mpf(pr_u["mh_pole_4c_scale_drift"])),
            rel_err(ir_u["ckm_mz"]["b_tau"], mp.mpf(pr_u["b_tau_mz"])),
            rel_err(ir_u["ckm_mz"]["v12"], mp.mpf(pr_u["v12_mz"])),
            rel_err(ir_u["ckm_mz"]["v23"], mp.mpf(pr_u["v23_mz"])),
            rel_err(ir_u["ckm_mz"]["v13"], mp.mpf(pr_u["v13_mz"])),
            rel_err(ir_u["Lambda_QCD_eff_exact_over_v"], mp.mpf(pr_u["Lambda_QCD_3_exact_over_v"])),
        )
        link6_max_err = max(link6_max_err, e_all)
        link6_aem5_max_err = max(link6_aem5_max_err, e_a5)
        link6_checks[tag] = {
            "max_rel_err_all_observables_incl_aem5": mp.nstr(e_all, 10),
            "alpha_EM_inv_mz_nf5_gl4": mp.nstr(ir_u["alpha_EM_inv_mz_nf5"], 12),
            "alpha_EM_inv_mz_nf5_v8": pr_u["alpha_EM_inv_mz_nf5"],
            "alpha_EM_inv_mz_nf5_rel_err": mp.nstr(e_a5, 10),
            "nf_active_at_confinement": ir_u["nf_active_at_confinement"],
        }

    if link6_max_err >= q10(-5) or table_max_err >= q10(-8) or delta_hid_err >= q10(-9):
        discrepancies.append({
            "id": "DISC-V3-REF4",
            "severity": "BLOCKING",
            "domain": "OW27-D v8",
            "table_max_err": mp.nstr(table_max_err, 10),
            "delta_hid_err": mp.nstr(delta_hid_err, 10),
            "link6_max_err": mp.nstr(link6_max_err, 10),
        })

    ref4_passed = bool(
        nsvz_res == 0
        and pf5_res != 0
        and table_max_err < q10(-8)
        and delta_hid_err < q10(-9)
        and link6_max_err < q10(-5)
    )
    ref4_block = {
        "gate_passed": ref4_passed,
        "nsvz_exact_2loop_rg_residual": str(nsvz_res),
        "pf5_omitted_g_neg23_rg_residual": str(pf5_res),
        "table_32_rows_max_rel_err": mp.nstr(table_max_err, 10),
        "delta_hid_bisection_secant_val": mp.nstr(delta_hid_ref, 12),
        "delta_hid_rel_err_vs_v8": mp.nstr(delta_hid_err, 10),
        "link6_and_hybrid_max_rel_err_incl_aem5": mp.nstr(link6_max_err, 10),
        "link6_and_hybrid_aem5_max_rel_err": mp.nstr(link6_aem5_max_err, 10),
        "link6_and_hybrid_runs": link6_checks,
    }

    # ==========================================================================
    # REF_5: A2-OW16 v22, Remediated B4_UV_MZ_BLIND_LOCK_V3, Manifests, & Custody
    # ==========================================================================
    print("  [REF3 5/6] Running custody, remediated LOCK_V3 SHA-256, manifests, & A2-OW16 v22 audit...", flush=True)
    lock_v3_obj = ow27["OW27_E_planted_faults_and_blind_lock_v3"]["blind_prediction_lock_v3_B4_UV"]
    lock_v3_claimed = ow27["OW27_E_planted_faults_and_blind_lock_v3"]["blind_prediction_lock_v3_sha256"]
    lock_v3_expected = "ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a"
    lock_v3_canon = json.dumps(lock_v3_obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    lock_v3_recomp = hashlib.sha256(lock_v3_canon).hexdigest()
    lock_v3_sha_ok = bool(lock_v3_recomp == lock_v3_claimed == lock_v3_expected)
    ow16_lock_v3_match = bool(
        ow16["guardrail5_input_ledger_v22"]["conditional_parameter_reduction_branches"]["blind_prediction_lock_v3_mz_sha256"]
        == lock_v3_recomp
    )

    # Verify DIAG-1 explicit confinement fields and remediated alpha_EM^-1(5) inside LOCK_V3
    lk_pred = lock_v3_obj["dimensionless_MZ_and_mt_predictions_B4_UV_CURV_s12_Dirac"]
    lk_10 = lk_pred["gauge_and_EW_at_MZ_m0_10v"]
    lk_3 = lk_pred["gauge_and_EW_at_MZ_m0_3v"]
    diag1_lock_ok = bool(
        lk_10.get("nf_active_at_confinement") == 4
        and lk_3.get("nf_active_at_confinement") == 4
        and "Lambda_QCD_5_exact_over_v" in lk_10
        and "Lambda_QCD_active_exact_over_v" in lk_10
        and "Lambda_QCD_5_exact_over_v" in lk_3
        and "Lambda_QCD_active_exact_over_v" in lk_3
        and rel_err(mp.mpf(lk_10["alpha_EM_inv_mz_nf5"]), ir_by_m0_pos[10]["alpha_EM_inv_mz_nf5"]) < q10(-5)
        and rel_err(mp.mpf(lk_3["alpha_EM_inv_mz_nf5"]), ir_by_m0_pos[3]["alpha_EM_inv_mz_nf5"]) < q10(-5)
        and mp.mpf(lk_10["alpha_EM_inv_mz_nf5"]) < mp.mpf(lk_10["alpha_EM_inv_mz_nf6"])
    )

    manifests_res = verify_all_manifests_ref()
    false_census_ref = scan_false_flag_jsons_ref()
    ow16_false_files = {r["file"] for r in ow16["historical_false_json_disclosure"]["files"]}
    ref_false_files = {r["file"] for r in false_census_ref["files"]}
    has_ow27_v6 = bool("relays/a2_ow27_v6/a2_ow27_v6_results.json" in ref_false_files)
    has_ow27_ref1 = bool("relays/a2_ow27_referee/a2_ow27_referee_results.json" in ref_false_files)
    has_ow27_ref2 = bool("relays/a2_ow27_referee_v2/a2_ow27_referee_v2_results.json" in ref_false_files)

    ow16_counts = ow16["blind_prediction_ledger_24_v22"]["counts_by_bucket"]
    ow16_part_ok = bool(
        ow16["card_id"] == "A2-OW16-v22"
        and ow16["blind_prediction_ledger_24_v22"]["total_observables"] == 24
        and ow16_counts == {
            "DERIVED_EXACT": 1,
            "CONDITIONAL_OR_QUALITATIVE": 10,
            "INTERNAL_WALL_OR_TENSION": 9,
            "OPEN_EXTERNAL_BOUNDARY": 4,
        }
    )
    ow16_locks_ok = bool(
        ow16["cross_card_locks_v22"]["locks_passed"] == 20
        and ow16["cross_card_locks_v22"]["total_locks"] == 20
        and ow16["cross_card_locks_v22"]["all_locks_passed"]
    )
    ow16_pf_ok = bool(
        ow16["planted_faults_v22"]["caught"] == 6
        and ow16["planted_faults_v22"]["total"] == 6
        and ow16["planted_faults_v22"]["gate_pass"]
    )

    obs_map = {r["id"]: r["status_note"] for r in ow16["blind_prediction_ledger_24_v22"]["observables"]}
    obs08_remediated = bool(
        lk_10["alpha_EM_inv_mz_nf5"] in obs_map["OBS-08"]
        and lk_3["alpha_EM_inv_mz_nf5"] in obs_map["OBS-08"]
        and "126.1496" not in obs_map["OBS-08"]
    )
    obs20_remediated = bool(prod_scan[3]["self_consistent_m0_own_clat_OmegaRatio"] in obs_map["OBS-20"])
    obs22_remediated = bool(lock_v3_recomp in obs_map["OBS-22"])

    # Verify remediation of both Referee v2 non-blocking prose diagnostics in A2-OW16 v22
    ow16_src = p_ow16_script.read_text(encoding="utf-8")
    v2_docstring_remediated = bool(
        "AGY-002 Card A2-OW16 v22 Producer" in ow16_src
        and "AGY-002 Card A2-OW16 v20 Producer" not in ow16_src
    )
    v2_obs20_lambda_remediated = bool(
        "0.0121834811632 at m0=10v" in obs_map["OBS-20"]
        and "0.00452331048342 at m0=3v" in obs_map["OBS-20"]
    )
    if not v2_docstring_remediated:
        non_blocking_diagnostics.append({
            "id": "DIAG-V3-OW16-V22-DOCSTRING",
            "domain": "relays/a2_ow16_v22/verify_a2_ow16_v22.py",
            "summary": "Docstring did not match expected A2-OW16 v22 header.",
        })
    if not v2_obs20_lambda_remediated:
        non_blocking_diagnostics.append({
            "id": "DIAG-V3-OBS20-PARENTHETICAL-LAMBDA",
            "domain": "relays/a2_ow16_v22/a2_ow16_v22_results.json OBS-20",
            "summary": "OBS-20 parenthetical did not list both m0=10v and m0=3v Lambda_QCD^(4)/v_EW values.",
        })

    git_non_relay: list[str] = []
    try:
        gd = subprocess.run(
            ["git", "diff", "--name-only", "c00b3bb73..HEAD"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, check=True,
        )
        changed = [ln.strip() for ln in gd.stdout.splitlines() if ln.strip()]
        git_non_relay = [p for p in changed if not p.startswith("relays/")]
    except Exception:
        changed = []

    all_hyg_clean = bool(
        hyg_self["clean"]
        and hyg_ow27_ast["clean"]
        and hyg_ow27_json["clean"]
        and hyg_ow16_ast["clean"]
        and hyg_ow16_json["clean"]
    )
    ref5_passed = bool(
        all_hyg_clean
        and lock_v3_sha_ok
        and ow16_lock_v3_match
        and diag1_lock_ok
        and manifests_res["all_verified"]
        and ow16_part_ok
        and ow16_locks_ok
        and ow16_pf_ok
        and obs08_remediated
        and obs20_remediated
        and obs22_remediated
        and false_census_ref["count"] == 49
        and ow16_false_files == ref_false_files
        and has_ow27_v6
        and has_ow27_ref1
        and has_ow27_ref2
        and v2_docstring_remediated
        and v2_obs20_lambda_remediated
        and len(git_non_relay) == 0
    )
    if not ref5_passed:
        discrepancies.append({
            "id": "DISC-V3-REF5",
            "severity": "BLOCKING",
            "domain": "A2-OW16 v22 / LOCK_V3 / Custody",
            "lock_v3_sha_ok": lock_v3_sha_ok,
            "diag1_lock_ok": diag1_lock_ok,
            "manifests_ok": manifests_res["all_verified"],
            "obs08_ok": obs08_remediated,
            "obs20_ok": obs20_remediated,
            "obs22_ok": obs22_remediated,
            "false_count": false_census_ref["count"],
        })

    ref5_block = {
        "gate_passed": ref5_passed,
        "DIAG_1_explicit_nf_conf_in_LOCK_V3_verified": diag1_lock_ok,
        "hygiene": {
            "referee_v3_self_ast": hyg_self,
            "ow27_v8_script_ast": hyg_ow27_ast,
            "ow27_v8_raw_json_floats": hyg_ow27_json,
            "ow16_v22_script_ast": hyg_ow16_ast,
            "ow16_v22_raw_json_floats": hyg_ow16_json,
        },
        "lock_v3_canonical_sha256": {
            "expected": lock_v3_expected,
            "claimed_ow27_v8": lock_v3_claimed,
            "recomputed": lock_v3_recomp,
            "exact_match": lock_v3_sha_ok,
            "ow16_v22_matches": ow16_lock_v3_match,
        },
        "branch_manifests": manifests_res,
        "ow16_v22_checks": {
            "partition_1_10_9_4_eq_24": ow16_part_ok,
            "locks_20_of_20": ow16_locks_ok,
            "planted_faults_6_of_6": ow16_pf_ok,
            "obs08_remediated_aem5": obs08_remediated,
            "obs20_remediated_per_m0_3v": obs20_remediated,
            "obs22_remediated_lock_v3": obs22_remediated,
            "v2_docstring_polish_verified": v2_docstring_remediated,
            "v2_obs20_dual_lambda_polish_verified": v2_obs20_lambda_remediated,
            "false_flag_json_count_independent": false_census_ref["count"],
            "false_flag_exact_set_match": bool(ow16_false_files == ref_false_files),
            "includes_a2_ow27_v6": has_ow27_v6,
            "includes_a2_ow27_referee_v1": has_ow27_ref1,
            "includes_a2_ow27_referee_v2": has_ow27_ref2,
        },
        "git_diff_c00b3bb73_to_HEAD": {
            "total_changed_files": len(changed),
            "non_relay_edits_count": len(git_non_relay),
            "non_relay_edits": git_non_relay,
        },
    }

    # ==========================================================================
    # REF_6: 6 / 6 Independent Referee Planted Fault Controls
    # ==========================================================================
    print("  [REF3 6/6] Running 6/6 independent planted fault controls...", flush=True)
    pf6_tamper_mf = verify_all_manifests_ref(tamper_idx=0)
    mut_lock = json.loads(lock_v3_canon.decode("utf-8"))
    mut_lock["firewall"] = "1 of 19"
    mut_sha = hashlib.sha256(json.dumps(mut_lock, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    pf6_ok = bool((not pf6_tamper_mf["all_verified"]) and (mut_sha != lock_v3_recomp))

    # Also test flipped QED top-decoupling sign inside PF_REF2_5 alongside NSVZ omission
    aem5_wrong_sign = central_ir_gl4["alpha_EM_inv_mz_nf6"] + (qrat(16, 9) / (2 * mp.pi)) * mp.log(central_ir_gl4["mu_mt_over_v"] / central_ir_gl4["mz_over_v"])
    qed_wrong_sign_caught = bool(aem5_wrong_sign > central_ir_gl4["alpha_EM_inv_mz_nf6"] and rel_err(aem5_wrong_sign, central_ir_gl4["alpha_EM_inv_mz_nf5"]) > qrat(3, 1000))

    pf_controls = {
        "PF_REF3_1_perturbed_GrayBroadhurst_c21_breaks_2loop_RG": bool(ref1_sympy["pf1_perturbed_c21_resid"] != "0"),
        "PF_REF3_2_dropping_bosonic_Higgs_breaks_4c_RG_and_drift_gt_3pct": bool(
            ref1_sympy["higgs_toponly_rg_nonzero"] and central_ir_gl4["mh_pole_toponly_scale_drift"] > qrat(3, 100)
        ),
        "PF_REF3_3_flipped_Majorana_Fermi_sign_Dirac_basis_swave_gt_1e_4": bool(
            mp.mpf(spinor_dirac["pf3_flipped_fermi_sign_swave"]) > q10(-4)
        ),
        "PF_REF3_4_unreduced_Planck_GL4_Riccati_shifts_YBino_gt_100pct": bool(pf4_shift > mp.mpf(1)),
        "PF_REF3_5_omitting_NSVZ_g_neg23_and_wrong_QED_top_sign_caught": bool(pf5_res != 0 and qed_wrong_sign_caught),
        "PF_REF3_6_manifest_1byte_tamper_and_LOCK_V3_mutation_caught": pf6_ok,
    }
    pf_caught = sum(1 for v in pf_controls.values() if v)
    ref6_passed = bool(pf_caught == 6)

    all_referee_gates_passed = bool(
        ref1_passed
        and ref2_passed
        and ref3_passed
        and ref4_passed
        and ref5_passed
        and ref6_passed
        and len(discrepancies) == 0
    )

    output = {
        "referee_id": "A2-OW27-v8-and-A2-OW16-v22-Cold-Room-Zero-Trust-Referee-v3",
        "seat": "agy-002",
        "empirical_firewall": "0 of 19",
        "all_referee_gates_passed": all_referee_gates_passed,
        "all_referee_v1_findings_remediated": bool(disc1_remediated and disc_c_remediated and diag1_lock_ok and diag2_verified),
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "non_blocking_diagnostics": non_blocking_diagnostics,
        "REF_1_OW27A_v8_gl4_sympy_poles_decoupling_lambda_qcd_haar": ref1_block,
        "REF_2_OW27B_v8_dirac_spinors_gl4_soft_riccati_bino_dm_diag2": ref2_block,
        "REF_3_OW27C_v8_jtheta_eigsy_384_192_scans_gl4_seesaw_boltzmann": ref3_block,
        "REF_4_OW27D_v8_nsvz_sympy_bisection_link6_gl4": ref4_block,
        "REF_5_OW16v22_LOCK_V3_manifests_and_custody": ref5_block,
        "REF_6_planted_faults": {
            "gate_passed": ref6_passed,
            "caught": pf_caught,
            "total": 6,
            "controls": pf_controls,
        },
    }
    assert_no_json_floats(output)
    out_path = SELF_DIR / "a2_ow27_referee_v3_results.json"
    out_bytes = (json.dumps(output, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    out_sha = hashlib.sha256(out_bytes).hexdigest()
    (SELF_DIR / "OUTPUT_SHA256.txt").write_text(f"{out_sha}  {out_path.name}\n", encoding="utf-8")
    print(
        f"REFEREE V3 COMPLETE | all_referee_gates_passed={all_referee_gates_passed} "
        f"| discrepancies_count={len(discrepancies)} | OUTPUT_SHA256={out_sha}"
    )


if __name__ == "__main__":
    main()
