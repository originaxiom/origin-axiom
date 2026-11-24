#!/usr/bin/env python3
"""
Cold-Room Zero-Trust Referee v3 for Card A2-OW26 v8 & Card A2-OW16 v18
Repository: origin-axiom-stage3-branch (branch agy-002/verify)

Strict Operational & Scientific Rules Enforced:
  - Strictly 0 of 19 Blind Firewall: ZERO PDG, NuFIT, Planck, DESI, or CODATA numbers.
  - Guardrail 6 (Zero-Trust / Zero Shared Code): ZERO imports from relays/ or frontier/;
    disjoint numerical algorithms across all 4 domains:
      * 2-stage implicit Gauss-Legendre GL4 ODE integrator (MSSM, SM, soft-SUSY, seesaw,
        and stiff flavored/unflavored MSSM Boltzmann equations at N=600 vs 1200 + Richardson).
      * Xorshift64* PRNG + complex Householder QR Haar U(3) generator (Mezzadri).
      * Real 2n x 2n symmetric block eigensolver for complex symmetric Takagi factorization.
      * Composite 2D Gauss-Legendre quadrature (7x7 cells x 9x9 Newton-Raphson Legendre
        nodes, coprime to M=8,16) for M=8 CIM L^2 overlaps.
      * 5-stage implicit Gauss-Legendre GL10 (order 10, symplectic) & 3-stage GL6 (rays)
        Fuchsian ODE integrators with e_3-form Weierstrass wp(z) and 2-trace Newton for c_*
        (48/72 uniform steps & step_frac=1/12 at 38 dps, cleanly resolving Referee v2's
        tr_comm and z2_evenness self-precision limits).
      * Heat-equation mp.jtheta / Jacobi triple-product evaluation of W_hol(tau) & Legendre
        lambda-invariant j(tau_0).
  - Pure-Precision Hygiene: 0 AST float/complex literals, 0 float()/complex()/np.float64 casts,
    0 JSON float tokens (all non-integer numbers serialized as decimal strings).
  - Full First-Principles Verification of ALL 8 Referee v1..v2 Remediations:
      * DISC-1..5 & DISC-NUM-1 (Referee v1)
      * DISC-V7-1: Consistent reduced-Planck Hubble H(M_1) = sqrt(pi^2 g_* / 90) M_1^2 / M_{P,red}
      * DISC-V7-2: Exact 1-loop top-Yukawa RG-invariant Higgs pole-to-MSbar shift & mu=M_Z vs m_t check
      * Plus independent non-perturbative SUGRA mu=M_Z vs mu=m_t floor-clamp audit & 6/6 planted faults.
"""

from __future__ import annotations

import ast
import hashlib
import json
import subprocess
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


# ==============================================================================
# Core Pure-Precision Primitives (Zero Float/Complex Literals or Casts)
# ==============================================================================

I_UNIT = mp.mpc(0, 1)


def q_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def p10(exp_int: int) -> mp.mpf:
    return mp.mpf(10) ** exp_int


def frac_text(q: Fr) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def tr_mp(mat: mp.matrix) -> mp.mpc:
    acc = mp.mpc(0)
    for idx in range(mat.rows):
        acc += mat[idx, idx]
    return acc


def frob_mp(mat: mp.matrix) -> mp.mpf:
    acc = mp.mpf(0)
    for r in range(mat.rows):
        for c in range(mat.cols):
            acc += abs(mat[r, c]) ** 2
    return mp.sqrt(acc)


def rel_diff_mp(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    denom = max(abs(a), abs(b), p10(-30))
    return abs(a - b) / denom


def fmt_mp(val: mp.mpf, sig: int = 12) -> str:
    return mp.nstr(val, sig)


def assert_no_json_floats_obj(obj: Any, path: str = "$") -> None:
    if obj is None or isinstance(obj, (bool, int, str)):
        return
    if isinstance(obj, float):
        raise AssertionError(f"JSON float detected at {path}: {obj!r}")
    if isinstance(obj, list):
        for idx, item in enumerate(obj):
            assert_no_json_floats_obj(item, f"{path}[{idx}]")
        return
    if isinstance(obj, dict):
        for key, val in obj.items():
            assert_no_json_floats_obj(val, f"{path}.{key}")
        return
    raise AssertionError(f"Unexpected JSON type at {path}: {type(obj).__name__}")


def scan_raw_json_float_tokens(json_text: str) -> dict[str, Any]:
    float_tokens: list[str] = []

    def catch_float(tok: str) -> str:
        float_tokens.append(tok)
        return tok

    json.loads(json_text, parse_float=catch_float)
    return {
        "raw_float_token_count": len(float_tokens),
        "sample_tokens": float_tokens[:10],
        "clean": bool(len(float_tokens) == 0),
    }


def ast_audit_script(script_path: Path) -> dict[str, Any]:
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_complex_lines: list[int] = []
    cast_lines: list[int] = []
    forbidden_imports: list[str] = []
    banned_prefixes = ("frontier", "relays", "numpy", "scipy", "math", "cmath")
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_complex_lines.append(getattr(node, "lineno", -1))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                cast_lines.append(getattr(node, "lineno", -1))
            if isinstance(node.func, ast.Attribute) and node.func.attr in (
                "float64", "complex128", "float32", "complex64"
            ):
                cast_lines.append(getattr(node, "lineno", -1))
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith(banned_prefixes):
                    forbidden_imports.append(alias.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(banned_prefixes):
                forbidden_imports.append(node.module)
    return {
        "file": script_path.name,
        "sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "float_complex_literals": len(float_complex_lines),
        "binary64_casts": len(cast_lines),
        "forbidden_imports": len(forbidden_imports),
        "clean": bool(
            len(float_complex_lines) == 0
            and len(cast_lines) == 0
            and len(forbidden_imports) == 0
        ),
    }


# ==============================================================================
# Disjoint PRNG (Xorshift64*) + Complex Householder QR Haar U(3) Generator
# ==============================================================================

class Xorshift64Star:
    """Pure-integer 64-bit Xorshift64* PRNG (disjoint from producer's SplitMix64)."""

    def __init__(self, seed: int) -> None:
        self.mask = (1 << 64) - 1
        self.state = (seed & self.mask) or 0x2545F4914F6CDD1D

    def next_u64(self) -> int:
        x = self.state
        x ^= (x >> 12) & self.mask
        x ^= (x << 25) & self.mask
        x ^= (x >> 27) & self.mask
        self.state = x
        return (x * 0x2545F4914F6CDD1D) & self.mask

    def uniform_open(self) -> mp.mpf:
        val = (self.next_u64() >> 11) + 1
        return mp.mpf(val) / mp.mpf((1 << 53) + 1)

    def std_normal_pair(self) -> tuple[mp.mpf, mp.mpf]:
        u1 = self.uniform_open()
        u2 = self.uniform_open()
        rad = mp.sqrt(-2 * mp.log(u1))
        ang = 2 * mp.pi * u2
        return rad * mp.cos(ang), rad * mp.sin(ang)


def haar_unitary_householder(rng: Xorshift64Star, dim: int = 3) -> mp.matrix:
    """
    Mezzadri Haar-distributed unitary via complex Householder reflections
    (disjoint from producer's Gram-Schmidt QR).
    """
    a = mp.zeros(dim, dim)
    for r in range(dim):
        for c in range(dim):
            xr, xi = rng.std_normal_pair()
            a[r, c] = mp.mpc(xr, xi)
    q = mp.eye(dim)
    r_mat = a.copy()
    for k in range(dim):
        sub_len = dim - k
        x = mp.matrix([r_mat[k + i, k] for i in range(sub_len)])
        norm_x = mp.sqrt(sum((abs(x[i]) ** 2 for i in range(sub_len)), mp.mpf(0)))
        if norm_x == 0:
            continue
        x0 = x[0]
        phase = (x0 / abs(x0)) if abs(x0) > 0 else mp.mpc(1)
        alpha = -phase * norm_x
        v = x.copy()
        v[0] = v[0] - alpha
        v_norm_sq = sum((abs(v[i]) ** 2 for i in range(sub_len)), mp.mpf(0))
        if v_norm_sq == 0:
            continue
        h_full = mp.eye(dim)
        fac = mp.mpf(2) / v_norm_sq
        for i in range(sub_len):
            for j in range(sub_len):
                h_full[k + i, k + j] -= fac * v[i] * mp.conj(v[j])
        r_mat = h_full * r_mat
        q = q * h_full
    d_ph = mp.zeros(dim, dim)
    for k in range(dim):
        rk = r_mat[k, k]
        d_ph[k, k] = (rk / abs(rk)) if abs(rk) > 0 else mp.mpc(1)
    return q * d_ph


# ==============================================================================
# Disjoint Linear Algebra: SVD + Real 2n x 2n Symmetric Block Takagi Eigensolver
# ==============================================================================

def left_svd_asc(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    n = mat.rows
    gram = mat * mat.H
    gram = (gram + gram.H) / 2
    evals, evecs = mp.eighe(gram)
    order = sorted(range(n), key=lambda k: mp.re(evals[k]))
    u_mat = mp.zeros(n, n)
    svals: list[mp.mpf] = []
    for col, idx in enumerate(order):
        for row in range(n):
            u_mat[row, col] = evecs[row, idx]
        lv = mp.re(evals[idx])
        svals.append(mp.sqrt(lv) if lv > 0 else mp.mpf(0))
    return u_mat, svals


def takagi_real_2n_block(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """
    Disjoint Takagi factorization U_T^T M_sym U_T = diag(s_0 <= ... <= s_{n-1})
    via real 2n x 2n symmetric block H = [[Re M, Im M], [Im M, -Re M]] + mp.eigsy.
    """
    n = m_sym.rows
    ms = (m_sym + m_sym.T) / 2
    h_real = mp.zeros(2 * n, 2 * n)
    for r in range(n):
        for c in range(n):
            ar = mp.re(ms[r, c])
            bi = mp.im(ms[r, c])
            h_real[r, c] = ar
            h_real[r, n + c] = bi
            h_real[n + r, c] = bi
            h_real[n + r, n + c] = -ar
    evals, evecs = mp.eigsy(h_real)
    idx_sorted = sorted(range(2 * n), key=lambda k: mp.re(evals[k]))
    pos_indices = idx_sorted[n:]
    svals: list[mp.mpf] = []
    cols: list[mp.matrix] = []
    for k_idx in pos_indices:
        sig = mp.re(evals[k_idx])
        svals.append(sig if sig > 0 else mp.mpf(0))
        vec = mp.matrix(
            [mp.mpc(mp.re(evecs[r, k_idx]), -mp.re(evecs[n + r, k_idx])) for r in range(n)]
        )
        for prev in cols:
            proj = sum((mp.conj(prev[r]) * vec[r] for r in range(n)), mp.mpc(0))
            for r in range(n):
                vec[r] -= proj * prev[r]
        nrm = mp.sqrt(sum((abs(vec[r]) ** 2 for r in range(n)), mp.mpf(0)))
        if nrm > 0:
            for r in range(n):
                vec[r] /= nrm
        cols.append(vec)
    u_tak = mp.zeros(n, n)
    for c in range(n):
        for r in range(n):
            u_tak[r, c] = cols[c][r]
    diag_chk = u_tak.T * ms * u_tak
    for c in range(n):
        dc = diag_chk[c, c]
        if abs(dc) > p10(-25):
            ang = mp.arg(dc)
            fac = mp.exp(-I_UNIT * ang / 2)
            for r in range(n):
                u_tak[r, c] *= fac
    return u_tak, svals


# ==============================================================================
# Disjoint Gauss-Legendre Nodes/Weights (Newton-Raphson on P_n(x)) & GL-s Tableaux
# ==============================================================================

def gauss_legendre_newton(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """
    n-point Gauss-Legendre nodes & weights on [-1, 1] by Newton-Raphson on
    Legendre polynomials P_n(x) (disjoint from producer's Golub-Welsch eigsy).
    """
    nodes: list[mp.mpf] = []
    weights: list[mp.mpf] = []
    half_m = (n + 1) // 2
    for i in range(1, half_m + 1):
        th = mp.pi * (mp.mpf(4 * i - 1) / mp.mpf(4 * n + 2))
        x = mp.cos(th)
        for _ in range(45):
            p0 = mp.mpf(1)
            p1 = x
            for k in range(2, n + 1):
                pk = (mp.mpf(2 * k - 1) * x * p1 - mp.mpf(k - 1) * p0) / mp.mpf(k)
                p0, p1 = p1, pk
            dp = mp.mpf(n) * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < p10(-(mp.mp.dps - 4)):
                break
        p0 = mp.mpf(1)
        p1 = x
        for k in range(2, n + 1):
            pk = (mp.mpf(2 * k - 1) * x * p1 - mp.mpf(k - 1) * p0) / mp.mpf(k)
            p0, p1 = p1, pk
        dp = mp.mpf(n) * (x * p1 - p0) / (x * x - 1)
        w = mp.mpf(2) / ((1 - x * x) * dp * dp)
        nodes.append(-x)
        weights.append(w)
        if i != n + 1 - i:
            nodes.append(x)
            weights.append(w)
    paired = sorted(zip(nodes, weights), key=lambda pr: pr[0])
    return [pr[0] for pr in paired], [pr[1] for pr in paired]


def build_gl_tableau(stages: int) -> tuple[list[mp.mpf], list[mp.mpf], mp.matrix]:
    """Exact s-stage implicit Gauss-Legendre (order 2s) Butcher tableau (c, b, A) on [0, 1]."""
    xn, wn = gauss_legendre_newton(stages)
    c_vec = [(x + 1) / 2 for x in xn]
    b_vec = [w / 2 for w in wn]
    a_mat = mp.zeros(stages, stages)
    for j in range(stages):
        poly = [mp.mpf(1)]
        denom = mp.mpf(1)
        for m in range(stages):
            if m == j:
                continue
            denom *= (c_vec[j] - c_vec[m])
            new_poly = [mp.mpf(0)] * (len(poly) + 1)
            for deg, coeff in enumerate(poly):
                new_poly[deg] -= coeff * c_vec[m]
                new_poly[deg + 1] += coeff
            poly = new_poly
        for i in range(stages):
            ci = c_vec[i]
            val = mp.mpf(0)
            p_pow = ci
            for deg, coeff in enumerate(poly):
                val += coeff * p_pow / mp.mpf(deg + 1)
                p_pow *= ci
            a_mat[i, j] = val / denom
    return c_vec, b_vec, a_mat


# ==============================================================================
# Disjoint 2-Stage Implicit Gauss-Legendre GL4 ODE Integrator (General Tuple State)
# ==============================================================================

def _state_norm(s1: tuple[Any, ...], s2: tuple[Any, ...]) -> mp.mpf:
    acc = mp.mpf(0)
    for a, b in zip(s1, s2):
        diff = a - b
        val = frob_mp(diff) if isinstance(diff, mp.matrix) else abs(diff)
        if val > acc:
            acc = val
    return acc


def _state_lincomb(
    base: tuple[Any, ...],
    d1: tuple[Any, ...],
    f1: mp.mpf,
    d2: tuple[Any, ...],
    f2: mp.mpf,
) -> tuple[Any, ...]:
    return tuple(base[i] + f1 * d1[i] + f2 * d2[i] for i in range(len(base)))


def gl4_integrate_tuple(
    rhs_fn: Any,
    st0: tuple[Any, ...],
    t_span: mp.mpf,
    n_steps: int,
    tol_exp: int = -24,
) -> tuple[Any, ...]:
    """
    2-stage implicit Gauss-Legendre GL4 ODE integrator (order O(h^4), A-stable, symplectic)
    solved by high-precision fixed-point iteration at every step (disjoint from explicit RK4).
    """
    s3 = mp.sqrt(3)
    a11 = q_mp(1, 4)
    a12 = (mp.mpf(3) - 2 * s3) / 12
    a21 = (mp.mpf(3) + 2 * s3) / 12
    a22 = q_mp(1, 4)
    h = t_span / mp.mpf(n_steps)
    h_half = h / 2
    tol = p10(tol_exp)
    st = st0
    for _ in range(n_steps):
        f0 = rhs_fn(st)
        k1 = f0
        k2 = f0
        for _it in range(50):
            y1 = _state_lincomb(st, k1, h * a11, k2, h * a12)
            y2 = _state_lincomb(st, k1, h * a21, k2, h * a22)
            nk1 = rhs_fn(y1)
            nk2 = rhs_fn(y2)
            err = max(_state_norm(nk1, k1), _state_norm(nk2, k2))
            k1, k2 = nk1, nk2
            if err < tol:
                break
        st = _state_lincomb(st, k1, h_half, k2, h_half)
    return st


# ==============================================================================
# Disjoint Heat-Equation Theta Evaluation of Holomorphic Yukawa Block W_hol(tau)
# ==============================================================================

def eval_sh_heat_eq(tau: mp.mpc) -> tuple[mp.matrix, list[mp.mpc]]:
    """
    Independent evaluation of quaternion Higgs factor S_H(tau) using mp.jtheta heat-equation
    second derivatives and Jacobi triple-product identity E_2/24 = (l2 + l3 + l4)/3.
    """
    qi = mp.matrix([[I_UNIT, 0], [0, -I_UNIT]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    q_half = mp.exp(I_UNIT * mp.pi * tau)
    t2 = mp.jtheta(2, 0, q_half)
    t3 = mp.jtheta(3, 0, q_half)
    t4 = mp.jtheta(4, 0, q_half)
    l2 = -mp.jtheta(2, 0, q_half, 2) / (8 * t2)
    l3 = -mp.jtheta(3, 0, q_half, 2) / (8 * t3)
    l4 = -mp.jtheta(4, 0, q_half, 2) / (8 * t4)
    e2_over_24 = (l2 + l3 + l4) / 3
    c1 = (-t2 / (t3 * t4)) * (l2 - l3 - l4 + e2_over_24)
    c2 = (-t4 / (t2 * t3)) * (l4 - l2 - l3 + e2_over_24)
    c3 = (I_UNIT * t3 / (t2 * t4)) * (l3 - l2 - l4 + e2_over_24)
    return c1 * qi + c2 * qj + c3 * qk, [c1, c2, c3]


def eval_w_hol_independent(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    """
    Independent construction of the 3x3 holomorphic elliptic Yukawa block W_hol(tau; a,b; qL,qR)
    via heat-equation mp.jtheta and theta-characteristic reduction to mp.jtheta(3, ...).
    """
    qi = mp.matrix([[I_UNIT, 0], [0, -I_UNIT]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    half_mp = q_mp(1, 2)
    ed = {"1": half_mp * qj, "i": half_mp * qk, "j": -half_mp * mp.eye(2), "k": -half_mp * qi}
    blks = [qj, qi, qk]

    sh, _ = eval_sh_heat_eq(tau)
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    q_half = mp.exp(I_UNIT * mp.pi * tau)
    t1p = mp.pi * mp.jtheta(2, 0, q_half) * mp.jtheta(3, 0, q_half) * mp.jtheta(4, 0, q_half)

    def theta_char(ca: Fr, cb: Fr) -> mp.mpc:
        ta = ca % 1
        tb = cb % 1
        nb = int(cb - tb)
        am = q_mp(ta.numerator, ta.denominator)
        bm = q_mp(tb.numerator, tb.denominator)
        z_arg = mp.pi * (am * tau + bm)
        base = mp.exp(
            I_UNIT * mp.pi * am * am * tau + 2 * I_UNIT * mp.pi * am * bm
        ) * mp.jtheta(3, z_arg, q_half)
        return base if (nb == 0 or ta == 0) else mp.exp(2 * I_UNIT * mp.pi * am * nb) * base

    xv = (ql * pa, 2 * ql * pb)
    yv = (qr * pa, 2 * qr * pb)
    ap = xv[0] + yv[0]
    am = xv[0] - yv[0]
    bp = (xv[1] + yv[1]) / 2
    bm = (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_UNIT * mp.pi * q_mp(xv[0].numerator, xv[0].denominator))
    kap = {"1": -I_UNIT * eph, "i": mp.mpf(-1), "j": -eph, "k": I_UNIT}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * theta_char(cs[sk][0], cs[sk][1]) * theta_char(ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    out = mp.zeros(3, 3)
    for ra in range(3):
        for cb in range(3):
            out[ra, cb] = (
                ct[ra][cb][0, 0] * mw[0, 0]
                + ct[ra][cb][0, 1] * mw[0, 1]
                + ct[ra][cb][1, 0] * mw[1, 0]
                + ct[ra][cb][1, 1] * mw[1, 1]
            )
    return out


# ==============================================================================
# Observable Extractors (CKM & Full PMNS including delta_CP & |m_ee|/m_3)
# ==============================================================================

def extract_ckm_obs(yu: mp.matrix, yd: mp.matrix, ye: mp.matrix) -> dict[str, mp.mpf]:
    uu, su = left_svd_asc(yu)
    ud, sd = left_svd_asc(yd)
    _, se = left_svd_asc(ye)
    vc = uu.H * ud
    j_ckm = mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))
    return {
        "v12": abs(vc[0, 1]),
        "v23": abs(vc[1, 2]),
        "v13": abs(vc[0, 2]),
        "J": j_ckm,
        "u13": su[0] / su[2],
        "u23": su[1] / su[2],
        "d13": sd[0] / sd[2],
        "d23": sd[1] / sd[2],
        "e13": se[0] / se[2],
        "e23": se[1] / se[2],
        "b_tau": sd[2] / se[2],
        "yt": su[2],
        "yb": sd[2],
        "ytau": se[2],
    }


def extract_pmns_obs(ye: mp.matrix, kappa: mp.matrix) -> dict[str, mp.mpf]:
    ks = (kappa + kappa.T) / 2
    ul, _ = left_svd_asc(ye)
    k_flav = ul.H * ks * ul.apply(mp.conj)
    u_tak, sn = takagi_real_2n_block(k_flav)
    up = u_tak.apply(mp.conj)
    s13sq = abs(up[0, 2]) ** 2
    c13sq = 1 - s13sq
    s12sq = (abs(up[0, 1]) ** 2) / c13sq
    c12sq = 1 - s12sq
    s23sq = (abs(up[1, 2]) ** 2) / c13sq
    c23sq = 1 - s23sq
    dm = (sn[1] ** 2 - sn[0] ** 2) / (sn[2] ** 2 - sn[0] ** 2)
    j_p = mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1]))
    denom_j = mp.sqrt(max(c12sq * s12sq * c23sq * s23sq * s13sq, mp.mpf(0)))
    sin_d = j_p / (c13sq * denom_j) if denom_j > p10(-30) else mp.mpf(0)
    cos_d = (
        (abs(up[1, 0]) ** 2 - s12sq * c23sq - c12sq * s23sq * s13sq) / (2 * denom_j)
        if denom_j > p10(-30)
        else mp.mpf(1)
    )
    delta_cp = mp.atan2(sin_d, cos_d)
    mee_over_m3 = abs(k_flav[0, 0]) / sn[2] if sn[2] > 0 else mp.mpf(0)
    sum_m_over_m3 = (sn[0] + sn[1] + sn[2]) / sn[2] if sn[2] > 0 else mp.mpf(0)
    return {
        "s12sq": s12sq,
        "s23sq": s23sq,
        "s13sq": s13sq,
        "dm": dm,
        "J": j_p,
        "delta_cp_rad": delta_cp,
        "delta_cp_over_pi": delta_cp / mp.pi,
        "mee_over_m3": mee_over_m3,
        "sum_m_over_m3": sum_m_over_m3,
        "m1_over_m3": sn[0] / sn[2] if sn[2] > 0 else mp.mpf(0),
        "m2_over_m3": sn[1] / sn[2] if sn[2] > 0 else mp.mpf(0),
    }


# ==============================================================================
# REF-1: First-Principles 2-Loop SM & MSSM Theory Audits + GL4 RGE Pipeline
# ==============================================================================

def first_principles_sm_rge_and_dr_ms_audits(ow26_res: dict[str, Any]) -> dict[str, Any]:
    """
    Independent first-principles SymPy + exact Fraction derivations of:
      1. 1-loop & 2-loop SM gauge beta coefficients (b1, b2, c_{a,f}) & MSSM-SM threshold sum.
      2. 2HDM -> SM scalar-loop vacuum-polarization shifts in beta_Y^(2)|_{g_a^4}.
      3. 4-real-scalar SU(2) contraction for gamma_S^(2) (-27/4, +3/2).
      4. O(4) pure-scalar quartic beta coefficients (12, -78) in V = (lam/2)|H|^4.
      5. Exact 8x8 symmetric Weyl Machacek-Vaughn II 2-loop non-commuting Yukawa order (DISC-1).
      6. Exact overdetermined 6x3 Machacek-Vaughn III g^4 Y^2 quartic trace (+27/5, DISC-2).
      7. Exact Martin-Vaughn (hep-ph/9308222 Eq. 2.8) DR -> MS Yukawa matching Casimirs (DISC-3).
      8. Exact 1-loop top-Yukawa Higgs pole RG invariance rg_resid == 0 (DISC-V7-2).
      9. Exact reduced vs unreduced Planck Hubble ratio 2*sqrt(2)*sqrt(pi) (DISC-V7-1).
    """
    weyl = [
        (3, 3, 2, Fr(1, 6), "Q"),
        (3, 3, 1, Fr(-2, 3), "uc"),
        (3, 3, 1, Fr(1, 3), "dc"),
        (3, 1, 2, Fr(-1, 2), "L"),
        (3, 1, 1, Fr(1, 1), "ec"),
    ]
    scalars = [(1, 1, 2, Fr(1, 2), "H")]

    def c2_rep(d3: int, d2: int, y: Fr) -> list[Fr]:
        return [Fr(3, 5) * y * y, Fr(3, 4) if d2 == 2 else Fr(0), Fr(4, 3) if d3 == 3 else Fr(0)]

    def s2_rep(d3: int, d2: int, y: Fr) -> list[Fr]:
        return [
            d3 * d2 * Fr(3, 5) * y * y,
            (d3 * Fr(1, 2)) if d2 == 2 else Fr(0),
            (d2 * Fr(1, 2)) if d3 == 3 else Fr(0),
        ]

    c_adj = [Fr(0), Fr(2), Fr(3)]
    sf = [sum((m * s2_rep(d3, d2, y)[a] for m, d3, d2, y, _ in weyl), Fr(0)) for a in range(3)]
    ss = [sum((m * s2_rep(d3, d2, y)[a] for m, d3, d2, y, _ in scalars), Fr(0)) for a in range(3)]
    b1 = [Fr(-11, 3) * c_adj[a] + Fr(2, 3) * sf[a] + Fr(1, 3) * ss[a] for a in range(3)]
    b2 = [[Fr(0)] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            acc = (
                sum((m * 2 * s2_rep(d3, d2, y)[a] * c2_rep(d3, d2, y)[b] for m, d3, d2, y, _ in weyl), Fr(0))
                + sum((m * 4 * s2_rep(d3, d2, y)[a] * c2_rep(d3, d2, y)[b] for m, d3, d2, y, _ in scalars), Fr(0))
            )
            if a == b:
                acc += Fr(-34, 3) * c_adj[a] ** 2 + Fr(10, 3) * c_adj[a] * sf[a] + Fr(2, 3) * c_adj[a] * ss[a]
            b2[a][b] = acc

    # Verify sparticle decoupling beta shifts sum exactly to b1_MSSM - b1_SM = (5/2, 25/6, 4)
    spart_db = [
        (Fr(0), Fr(0), Fr(2)),
        (Fr(0), Fr(4, 3), Fr(0)),
        (Fr(2, 5), Fr(2, 3), Fr(0)),
        (Fr(1, 10), Fr(1, 6), Fr(0)),
        (Fr(1, 30), Fr(1, 2), Fr(1, 3)),
        (Fr(4, 15), Fr(0), Fr(1, 6)),
        (Fr(1, 15), Fr(0), Fr(1, 6)),
        (Fr(11, 15), Fr(1), Fr(4, 3)),
        (Fr(3, 10), Fr(1, 2), Fr(0)),
        (Fr(3, 5), Fr(0), Fr(0)),
    ]
    b1_mssm = [Fr(33, 5), Fr(1, 1), Fr(-3, 1)]
    spart_sum = [sum((row[a] for row in spart_db), Fr(0)) for a in range(3)]
    spart_sum_exact = bool(all(spart_sum[a] == b1_mssm[a] - b1[a] for a in range(3)))

    c_map = {nm: c2_rep(d3, d2, y) for _, d3, d2, y, nm in weyl + scalars}
    d_adj = [Fr(1), Fr(3), Fr(8)]
    yuk_specs = [("u", 3, "Q", "uc"), ("d", 3, "Q", "dc"), ("e", 1, "L", "ec")]
    c_af: dict[str, list[Fr]] = {}
    for nm, nc, fl, fr in yuk_specs:
        c_af[nm] = [Fr(2 * nc) * (c_map[fl][a] + c_map[fr][a]) / d_adj[a] for a in range(3)]
    c_af_ok = bool(
        c_af["u"] == [Fr(17, 10), Fr(3, 2), Fr(2, 1)]
        and c_af["d"] == [Fr(1, 2), Fr(3, 2), Fr(2, 1)]
        and c_af["e"] == [Fr(3, 2), Fr(1, 2), Fr(0, 1)]
    )

    sh = s2_rep(1, 2, Fr(1, 2))
    ch = c2_rep(1, 2, Fr(1, 2))
    dg1_u = Fr(11, 6) * sh[0] * (c_map["Q"][0] + c_map["uc"][0]) - Fr(1, 2) * sh[0] * ch[0]
    dg1_d = Fr(11, 6) * sh[0] * (c_map["Q"][0] + c_map["dc"][0]) - Fr(1, 2) * sh[0] * ch[0]
    dg1_e = Fr(11, 6) * sh[0] * (c_map["L"][0] + c_map["ec"][0]) - Fr(1, 2) * sh[0] * ch[0]
    dg2_f = Fr(11, 6) * sh[1] * (c_map["Q"][1] + c_map["uc"][1]) - Fr(1, 2) * sh[1] * ch[1]

    # 4-real-scalar SU(2) contraction for gamma_S^(2)
    yu_s, yd_s = sp.symbols("yu yd", real=True)
    s2inv = 1 / sp.sqrt(2)
    yr = [
        s2inv * sp.Matrix([[0, yd_s], [-yu_s, 0]]),
        s2inv * sp.Matrix([[0, sp.I * yd_s], [sp.I * yu_s, 0]]),
        s2inv * sp.Matrix([[yu_s, 0], [0, yd_s]]),
        s2inv * sp.Matrix([[-sp.I * yu_s, 0], [0, sp.I * yd_s]]),
    ]
    yyh = sum((m * m.H for m in yr), sp.zeros(2, 2))
    yhy = sum((m.H * m for m in yr), sp.zeros(2, 2))
    y3 = yr[2]
    h2_33 = sp.simplify(sp.Rational(1, 2) * ((y3 * y3.H * yyh).trace() + (y3.H * y3 * yhy).trace()))
    hb2_33 = sp.simplify(
        sum(((y3 * m.H * y3 * m.H).trace() + (y3.H * m * y3.H * m).trace() for m in yr), sp.Integer(0)) / 2
    )
    gs2_expr = sp.expand(3 * (-3 * h2_33 - 2 * hb2_33))
    gs2_yu4 = sp.Poly(gs2_expr, yu_s, yd_s).coeff_monomial(yu_s ** 4)
    gs2_yu2yd2 = sp.Poly(gs2_expr, yu_s, yd_s).coeff_monomial(yu_s ** 2 * yd_s ** 2)

    o4_b1 = Fr(4 + 8, 1)
    o4_b2 = -3 * Fr(3 * 4 + 14, 1)

    # AUDIT 1 (DISC-1): Exact 8x8 symmetric Weyl Machacek-Vaughn II 2-loop non-commuting Yukawa order
    yu_num = sp.Matrix([[3, -2 * sp.I], [1 + 2 * sp.I, 5]])
    yd_num = sp.Matrix([[4, 3], [-2 * sp.I, 7]])
    z2 = sp.zeros(2, 2)
    z4 = sp.zeros(4, 4)

    def blk(a_m: sp.Matrix, b_m: sp.Matrix, c_m: sp.Matrix, d_m: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([[a_m, b_m], [c_m, d_m]])

    yt_4 = [
        blk(z2, yd_num, -yu_num, z2) * s2inv,
        blk(z2, sp.I * yd_num, sp.I * yu_num, z2) * s2inv,
        blk(yu_num, z2, z2, yd_num) * s2inv,
        blk(-sp.I * yu_num, z2, z2, sp.I * yd_num) * s2inv,
    ]
    m_sym_8 = [blk(z4, yt, yt.T, z4) for yt in yt_4]
    mb_8 = [m.conjugate() for m in m_sym_8]
    a_idx = 2
    v_xbox = sum((m_sym_8[b] * mb_8[c] * m_sym_8[a_idx] * mb_8[b] * m_sym_8[c] for b in range(4) for c in range(4)), sp.zeros(8, 8))
    v_top = sum((m_sym_8[b] * mb_8[c] * m_sym_8[a_idx] * mb_8[c] * m_sym_8[b] for b in range(4) for c in range(4)), sp.zeros(8, 8))
    v_int = sum(
        (
            m_sym_8[b] * mb_8[c] * m_sym_8[c] * mb_8[a_idx] * m_sym_8[b]
            + m_sym_8[b] * mb_8[a_idx] * m_sym_8[c] * mb_8[c] * m_sym_8[b]
            for b in range(4) for c in range(4)
        ),
        sp.zeros(8, 8),
    )
    rain = sum(
        (
            m_sym_8[b] * mb_8[c] * m_sym_8[c] * mb_8[b] * m_sym_8[a_idx]
            + m_sym_8[a_idx] * mb_8[b] * m_sym_8[c] * mb_8[c] * m_sym_8[b]
            for b in range(4) for c in range(4)
        ),
        sp.zeros(8, 8),
    )
    b2_weyl = 2 * v_xbox - 2 * v_top - v_int - sp.Rational(1, 8) * rain
    b2_u_exact = sp.simplify(b2_weyl[0:2, 4:6] * sp.sqrt(2))
    b2_d_exact = sp.simplify(b2_weyl[2:4, 6:8] * sp.sqrt(2))
    hu_n = yu_num * yu_num.H
    hd_n = yd_num * yd_num.H
    u_true_expr = (sp.Rational(3, 2) * hu_n * hu_n - sp.Rational(1, 4) * hu_n * hd_n - hd_n * hu_n + sp.Rational(11, 4) * hd_n * hd_n) * yu_num
    d_true_expr = (sp.Rational(3, 2) * hd_n * hd_n - sp.Rational(1, 4) * hd_n * hu_n - hu_n * hd_n + sp.Rational(11, 4) * hu_n * hu_n) * yd_num
    mv2_exact_ok = bool(sp.simplify(b2_u_exact - u_true_expr) == z2 and sp.simplify(b2_d_exact - d_true_expr) == z2)

    # AUDIT 2 (DISC-2): Overdetermined 6x3 gauge-invariant MV III g^4 Y^2 quartic trace system
    def real_scalar_gen(t_c: sp.Matrix) -> sp.Matrix:
        mat_a = sp.zeros(4, 4)
        for rr in range(2):
            for cc in range(2):
                rt = sp.re(t_c[rr, cc])
                it = sp.im(t_c[rr, cc])
                mat_a[2 * rr, 2 * cc] = -it
                mat_a[2 * rr, 2 * cc + 1] = -rt
                mat_a[2 * rr + 1, 2 * cc] = rt
                mat_a[2 * rr + 1, 2 * cc + 1] = -it
        return -sp.I * mat_a

    sig_half = [
        sp.Matrix([[0, 1], [1, 0]]) / 2,
        sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2,
        sp.Matrix([[1, 0], [0, -1]]) / 2,
    ]
    th_w = [real_scalar_gen(s) for s in sig_half]
    th_y = real_scalar_gen(sp.Matrix([[sp.Rational(1, 2), 0], [0, sp.Rational(1, 2)]]))

    def mv3_traces(kind: str) -> dict[str, tuple[sp.Rational, sp.Rational, sp.Rational]]:
        if kind == "u":
            yl_q, yc_q = sp.Rational(1, 6), sp.Rational(-2, 3)
            yv = [(0, -s2inv), (0, -sp.I * s2inv), (s2inv, 0), (sp.I * s2inv, 0)]
        elif kind == "d":
            yl_q, yc_q = sp.Rational(1, 6), sp.Rational(1, 3)
            yv = [(s2inv, 0), (-sp.I * s2inv, 0), (0, s2inv), (0, -sp.I * s2inv)]
        else:
            yl_q, yc_q = sp.Rational(-1, 2), sp.Rational(1, 1)
            yv = [(s2inv, 0), (-sp.I * s2inv, 0), (0, s2inv), (0, -sp.I * s2inv)]
        m_f = [sp.Matrix([[0, 0, c0], [0, 0, c1], [c0, c1, 0]]) for c0, c1 in yv]
        mb_f = [m.conjugate() for m in m_f]
        tf_w = [sp.diag(s, sp.Matrix([[0]])) for s in sig_half]
        tf_y = sp.diag(yl_q, yl_q, yc_q)
        for ta_f, th_a in [(tf_y, th_y)] + list(zip(tf_w, th_w)):
            for a_i in range(4):
                chk = ta_f.T * m_f[a_i] + m_f[a_i] * ta_f + sum((th_a[b_i, a_i] * m_f[b_i] for b_i in range(4)), sp.zeros(3, 3))
                assert sp.simplify(chk) == sp.zeros(3, 3)
        res_t: dict[str, tuple[sp.Rational, sp.Rational, sp.Rational]] = {}
        for pair_name in ("YY", "WY", "WW"):
            if pair_name == "YY":
                plist = [(tf_y, th_y, tf_y, th_y)]
            elif pair_name == "WY":
                plist = [(tf_w[k], th_w[k], tf_y, th_y) for k in range(3)] + [(tf_y, th_y, tf_w[k], th_w[k]) for k in range(3)]
            else:
                plist = [(tf_w[k], th_w[k], tf_w[k], th_w[k]) for k in range(3)]
            ia = ib = ic = sp.Integer(0)
            for tfa, tha, tfb, thb in plist:
                sf_val = (tha * thb + thb * tha)[2, 2]
                ia += sp.simplify(sf_val * ((tfa * tfb + tfb * tfa) * (m_f[2] * mb_f[2])).trace())
                ib += sp.simplify(sf_val * (tfa * m_f[2] * (-tfb.T) * mb_f[2] + tfb * m_f[2] * (-tfa.T) * mb_f[2]).trace())
                ic += sp.simplify(sf_val * (m_f[2] * mb_f[2]).trace())
            res_t[pair_name] = (sp.simplify(ia), sp.simplify(ib), sp.simplify(ic))
        return res_t

    tr_data = {k: mv3_traces(k) for k in ("u", "d", "e")}
    ca_s, cb_s, cc_s = sp.symbols("ca cb cc")
    eqs_6 = [
        ca_s * tr_data["u"]["YY"][0] + cb_s * tr_data["u"]["YY"][1] + cc_s * tr_data["u"]["YY"][2] - sp.Rational(-19, 6),
        ca_s * tr_data["u"]["WY"][0] + cb_s * tr_data["u"]["WY"][1] + cc_s * tr_data["u"]["WY"][2] - sp.Integer(7),
        ca_s * tr_data["u"]["WW"][0] + cb_s * tr_data["u"]["WW"][1] + cc_s * tr_data["u"]["WW"][2] - sp.Rational(-3, 2),
        ca_s * tr_data["e"]["YY"][0] + cb_s * tr_data["e"]["YY"][1] + cc_s * tr_data["e"]["YY"][2] - sp.Rational(-25, 2),
        ca_s * tr_data["e"]["WY"][0] + cb_s * tr_data["e"]["WY"][1] + cc_s * tr_data["e"]["WY"][2] - sp.Integer(11),
        ca_s * tr_data["e"]["WW"][0] + cb_s * tr_data["e"]["WW"][1] + cc_s * tr_data["e"]["WW"][2] - sp.Rational(-3, 2),
    ]
    sol_mv3 = sp.solve(eqs_6, (ca_s, cb_s, cc_s))
    d_wy_gp = 3 * (sol_mv3[ca_s] * tr_data["d"]["WY"][0] + sol_mv3[cb_s] * tr_data["d"]["WY"][1] + sol_mv3[cc_s] * tr_data["d"]["WY"][2])
    d_wy_g1g2 = sp.simplify(d_wy_gp * sp.Rational(3, 5))
    d_yy_g14 = sp.simplify(3 * (sol_mv3[ca_s] * tr_data["d"]["YY"][0] + sol_mv3[cb_s] * tr_data["d"]["YY"][1]) * sp.Rational(9, 25))

    # AUDIT 3 (DISC-3): Exact Martin-Vaughn (hep-ph/9308222 Eq. 2.8) DR -> MS Yukawa matching Casimirs
    mv_drms = {
        "quark_alpha3": frac_text(Fr(1, 8) * (c_map["Q"][2] + c_map["uc"][2] - 2 * c_map["H"][2])),
        "quark_alpha2": frac_text(Fr(1, 8) * (c_map["Q"][1] + c_map["uc"][1] - 2 * c_map["H"][1])),
        "lepton_alpha2": frac_text(Fr(1, 8) * (c_map["L"][1] + c_map["ec"][1] - 2 * c_map["H"][1])),
        "u_alpha1": frac_text(Fr(1, 8) * (c_map["Q"][0] + c_map["uc"][0] - 2 * c_map["H"][0])),
        "d_alpha1": frac_text(Fr(1, 8) * (c_map["Q"][0] + c_map["dc"][0] - 2 * c_map["H"][0])),
        "e_alpha1": frac_text(Fr(1, 8) * (c_map["L"][0] + c_map["ec"][0] - 2 * c_map["H"][0])),
    }

    # AUDIT 4 (DISC-V7-2): Symbolic 1-loop top-Yukawa RG invariance of m_h^{pole,2}/v_{phys}^2
    lam_s, yt_s, mu_s, mt_s = sp.symbols("lam yt mu mt", positive=True)
    r_s = 2 * yt_s * yt_s / lam_s
    loop_f = 1 / (16 * sp.pi ** 2)
    beta_lam_top = loop_f * (12 * lam_s * yt_s ** 2 - 12 * yt_s ** 4)
    delta_top_exact = (3 * yt_s ** 2 * loop_f) * ((2 - r_s) * sp.log(mt_s ** 2 / mu_s ** 2) - sp.Rational(1, 2))
    delta_top_trunc_bad = (3 * yt_s ** 2 * loop_f) * (sp.log(mt_s ** 2 / mu_s ** 2) - 1)
    rg_resid_exact = sp.simplify(beta_lam_top + lam_s * mu_s * sp.diff(delta_top_exact, mu_s))
    rg_resid_trunc_bad = sp.simplify(beta_lam_top + lam_s * mu_s * sp.diff(delta_top_trunc_bad, mu_s))

    # AUDIT 5 (DISC-V7-1): Symbolic reduced vs unreduced Planck Hubble ratio
    g_st_s = sp.Rational(915, 4)
    h_unred_over_red_sym = sp.simplify(
        sp.sqrt(4 * (sp.pi ** 3) * g_st_s / 45) / sp.sqrt((sp.pi ** 2) * g_st_s / 90)
    )

    prod_g4 = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["guardrail4_2loop_sm_benchmarks"]
    v8_mv2_match = bool(mv2_exact_ok and prod_g4["mv2_8x8_weyl_noncommuting_order_exact"] is True)
    v8_mv3_match = bool(
        d_wy_g1g2 == sp.Rational(27, 5)
        and d_yy_g14 == sp.Rational(9, 10)
        and prod_g4["mv3_6x3_quartic_g1sq_g2sq_trd_exact"] == "27/5"
    )
    v8_drms_match = bool(prod_g4["mv9308222_dr_to_ms_yukawa_coeffs_over_pi"] == mv_drms)
    v8_higgs_rg_match = bool(
        rg_resid_exact == 0
        and prod_g4["higgs_pole_1loop_top_rg_invariance_resid"] == "0"
    )
    v8_hubble_ratio_match = bool(
        sp.simplify(h_unred_over_red_sym - 2 * sp.sqrt(2) * sp.sqrt(sp.pi)) == 0
        and prod_g4["hubble_unred_over_red_planck_ratio"] == str(h_unred_over_red_sym)
    )

    gt_ok = bool(
        b1 == [Fr(41, 10), Fr(-19, 6), Fr(-7, 1)]
        and b2 == [
            [Fr(199, 50), Fr(27, 10), Fr(44, 5)],
            [Fr(9, 10), Fr(35, 6), Fr(12, 1)],
            [Fr(11, 10), Fr(9, 2), Fr(-26, 1)],
        ]
        and spart_sum_exact
        and c_af_ok
        and (Fr(1267, 600) - dg1_u == Fr(1187, 600))
        and (Fr(-113, 600) - dg1_d == Fr(-127, 600))
        and (Fr(1449, 200) - dg1_e == Fr(1371, 200))
        and (Fr(-21, 4) - dg2_f == Fr(-23, 4))
        and gs2_yu4 == sp.Rational(-27, 4)
        and gs2_yu2yd2 == sp.Rational(3, 2)
        and o4_b1 == Fr(12, 1)
        and o4_b2 == Fr(-78, 1)
    )
    return {
        "group_theory_and_o4_exact": gt_ok,
        "sparticle_decoupling_beta_sum_exact": spart_sum_exact,
        "b1_sm": [frac_text(x) for x in b1],
        "b2_sm_diag": [frac_text(b2[i][i]) for i in range(3)],
        "c_af_exact": c_af_ok,
        "delta_2hdm_to_sm_g1_4": [frac_text(dg1_u), frac_text(dg1_d), frac_text(dg1_e)],
        "gamma_s2_yu4_and_yu2yd2": [str(gs2_yu4), str(gs2_yu2yd2)],
        "o4_scalar_b1_b2": [frac_text(o4_b1), frac_text(o4_b2)],
        "disc1_mv2_8x8_exact_and_v8_fixed": v8_mv2_match,
        "disc2_mv3_6x3_solution": {str(k): str(v) for k, v in sol_mv3.items()},
        "disc2_exact_d_g1sq_g2sq_trd_coeff": str(d_wy_g1g2),
        "disc2_exact_d_g14_trd_coeff": str(d_yy_g14),
        "disc2_v8_fixed": v8_mv3_match,
        "disc3_exact_mv9308222_dr_to_ms_coeffs_over_pi": mv_drms,
        "disc3_v8_fixed": v8_drms_match,
        "disc_v7_2_exact_1loop_top_mh_pole_rg_residual": str(rg_resid_exact),
        "disc_v7_2_planted_truncated_rg_residual": str(rg_resid_trunc_bad),
        "disc_v7_2_v8_fixed": v8_higgs_rg_match,
        "disc_v7_1_hubble_unred_over_red_exact": str(h_unred_over_red_sym),
        "disc_v7_1_v8_symbolic_ratio_match": v8_hubble_ratio_match,
    }


def make_sm_2loop_rhs(
    two_loop: bool = True,
    corrupt_o4_sign: bool = False,
    corrupt_mv3_trd: bool = False,
) -> Any:
    """Exact 2-loop SM RGEs (Machacek-Vaughn II/III + Luo-Xiao + Antusch) in V = (lam/2)|H|^4."""
    def rhs(state: tuple[Any, ...]) -> tuple[Any, ...]:
        g1, g2, g3, yu, yd, ye, kap, lam = state
        c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
        c2 = (c1 * c1) if two_loop else mp.mpf(0)
        g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
        gp2 = q_mp(3, 5) * g1s
        eye3 = mp.eye(3)

        hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
        hu2, hd2, he2 = hu * hu, hd * hd, he * he
        huhd, hdhu = hu * hd, hd * hu

        tru = mp.re(tr_mp(hu))
        trd = mp.re(tr_mp(hd))
        tre = mp.re(tr_mp(he))
        t_all = 3 * tru + 3 * trd + tre
        tru2 = mp.re(tr_mp(hu2))
        trd2 = mp.re(tr_mp(hd2))
        tre2 = mp.re(tr_mp(he2))
        trud = mp.re(tr_mp(huhd))
        tru3 = mp.re(tr_mp(hu2 * hu))
        trd3 = mp.re(tr_mp(hd2 * hd))
        tre3 = mp.re(tr_mp(he2 * he))
        tru2d = mp.re(tr_mp(hu2 * hd))
        trud2 = mp.re(tr_mp(hu * hd2))

        dg1 = c1 * q_mp(41, 10) * (g1 ** 3) + c2 * (g1 ** 3) * (
            q_mp(199, 50) * g1s + q_mp(27, 10) * g2s + q_mp(44, 5) * g3s
            - q_mp(17, 10) * tru - q_mp(1, 2) * trd - q_mp(3, 2) * tre
        )
        dg2 = c1 * q_mp(-19, 6) * (g2 ** 3) + c2 * (g2 ** 3) * (
            q_mp(9, 10) * g1s + q_mp(35, 6) * g2s + 12 * g3s
            - q_mp(3, 2) * tru - q_mp(3, 2) * trd - q_mp(1, 2) * tre
        )
        dg3 = c1 * (-7) * (g3 ** 3) + c2 * (g3 ** 3) * (
            q_mp(11, 10) * g1s + q_mp(9, 2) * g2s - 26 * g3s - 2 * tru - 2 * trd
        )

        mu1 = q_mp(3, 2) * hu - q_mp(3, 2) * hd + (t_all - q_mp(17, 20) * g1s - q_mp(9, 4) * g2s - 8 * g3s) * eye3
        md1 = q_mp(3, 2) * hd - q_mp(3, 2) * hu + (t_all - q_mp(1, 4) * g1s - q_mp(9, 4) * g2s - 8 * g3s) * eye3
        me1 = q_mp(3, 2) * he + (t_all - q_mp(9, 4) * g1s - q_mp(9, 4) * g2s) * eye3

        y2_g_h = (
            (q_mp(17, 8) * g1s + q_mp(45, 8) * g2s + 20 * g3s) * tru
            + (q_mp(5, 8) * g1s + q_mp(45, 8) * g2s + 20 * g3s) * trd
            + (q_mp(15, 8) * g1s + q_mp(15, 8) * g2s) * tre
        )
        y4_s = q_mp(9, 4) * (3 * tru2 + 3 * trd2 + tre2) - q_mp(3, 2) * trud
        chi_h = y2_g_h - y4_s + q_mp(3, 2) * lam * lam

        mu2 = (
            q_mp(3, 2) * hu2 - q_mp(1, 4) * huhd - hdhu + q_mp(11, 4) * hd2
            + (q_mp(5, 4) * hd - q_mp(9, 4) * hu) * t_all
            + (q_mp(223, 80) * g1s + q_mp(135, 16) * g2s + 16 * g3s - 6 * lam) * hu
            + (-q_mp(43, 80) * g1s + q_mp(9, 16) * g2s - 16 * g3s) * hd
            + (
                q_mp(1187, 600) * g1s * g1s - q_mp(9, 20) * g1s * g2s + q_mp(19, 15) * g1s * g3s
                - q_mp(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s + chi_h
            ) * eye3
        )
        md2 = (
            q_mp(3, 2) * hd2 - q_mp(1, 4) * hdhu - huhd + q_mp(11, 4) * hu2
            + (q_mp(5, 4) * hu - q_mp(9, 4) * hd) * t_all
            + (q_mp(187, 80) * g1s + q_mp(135, 16) * g2s + 16 * g3s - 6 * lam) * hd
            + (-q_mp(79, 80) * g1s + q_mp(9, 16) * g2s - 16 * g3s) * hu
            + (
                -q_mp(127, 600) * g1s * g1s - q_mp(27, 20) * g1s * g2s + q_mp(31, 15) * g1s * g3s
                - q_mp(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s + chi_h
            ) * eye3
        )
        me2 = (
            q_mp(3, 2) * he2 - q_mp(9, 4) * t_all * he
            + (q_mp(387, 80) * g1s + q_mp(135, 16) * g2s - 6 * lam) * he
            + (
                q_mp(1371, 200) * g1s * g1s + q_mp(27, 20) * g1s * g2s - q_mp(23, 4) * g2s * g2s + chi_h
            ) * eye3
        )

        dyu = (c1 * mu1 + c2 * mu2) * yu
        dyd = (c1 * md1 + c2 * md2) * yd
        dye = (c1 * me1 + c2 * me2) * ye

        alpha_k = -3 * g2s + 2 * lam + 2 * t_all
        dkap = c1 * (alpha_k * kap - q_mp(3, 2) * (he * kap + kap * he.T))

        o4_c2 = mp.mpf(78) if corrupt_o4_sign else mp.mpf(-78)
        trd_g1g2 = q_mp(-27, 5) if corrupt_mv3_trd else q_mp(27, 5)
        blam1 = (
            12 * lam * lam + 4 * lam * t_all - 4 * (3 * tru2 + 3 * trd2 + tre2)
            - 3 * lam * (3 * g2s + gp2)
            + q_mp(3, 4) * (2 * g2s * g2s + (g2s + gp2) ** 2)
        )
        blam2 = (
            o4_c2 * (lam ** 3)
            + 18 * (lam ** 2) * (3 * g2s + gp2)
            - 24 * (lam ** 2) * t_all
            + lam * (q_mp(1887, 200) * g1s * g1s + q_mp(117, 20) * g1s * g2s - q_mp(73, 8) * g2s * g2s)
            + 4 * lam * y2_g_h
            - lam * (3 * tru2 + 3 * trd2 + tre2)
            - 42 * lam * trud
            + q_mp(305, 8) * (g2s ** 3)
            - q_mp(289, 40) * g1s * g2s * g2s
            - q_mp(1677, 200) * g1s * g1s * g2s
            - q_mp(3411, 1000) * (g1s ** 3)
            + (-q_mp(171, 50) * g1s * g1s + q_mp(63, 5) * g1s * g2s - q_mp(9, 2) * g2s * g2s) * tru
            + (q_mp(9, 10) * g1s * g1s + trd_g1g2 * g1s * g2s - q_mp(9, 2) * g2s * g2s) * trd
            + (-q_mp(9, 2) * g1s * g1s + q_mp(33, 5) * g1s * g2s - q_mp(3, 2) * g2s * g2s) * tre
            - 64 * g3s * (tru2 + trd2)
            - q_mp(16, 5) * g1s * tru2 + q_mp(8, 5) * g1s * trd2 - q_mp(24, 5) * g1s * tre2
            + 60 * (tru3 + trd3) + 20 * tre3 - 12 * (tru2d + trud2)
        )
        dlam = c1 * blam1 + c2 * blam2
        return (dg1, dg2, dg3, dyu, dyd, dye, dkap, dlam)

    return rhs


def make_mssm_2loop_rhs(two_loop: bool = True) -> Any:
    def rhs(state: tuple[Any, ...]) -> tuple[Any, ...]:
        g1, g2, g3, yu, yd, ye, kap = state
        c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
        c2 = (c1 * c1) if two_loop else mp.mpf(0)
        g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
        eye3 = mp.eye(3)

        hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
        htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
        tu, td, te = mp.re(tr_mp(hu)), mp.re(tr_mp(hd)), mp.re(tr_mp(he))
        tu2, td2, te2 = mp.re(tr_mp(hu * hu)), mp.re(tr_mp(hd * hd)), mp.re(tr_mp(he * he))
        tud = mp.re(tr_mp(hu * hd))

        dg1 = c1 * q_mp(33, 5) * (g1 ** 3) + c2 * (g1 ** 3) * (
            q_mp(199, 25) * g1s + q_mp(27, 5) * g2s + q_mp(88, 5) * g3s
            - q_mp(26, 5) * tu - q_mp(14, 5) * td - q_mp(18, 5) * te
        )
        dg2 = c1 * (g2 ** 3) + c2 * (g2 ** 3) * (
            q_mp(9, 5) * g1s + 25 * g2s + 24 * g3s - 6 * tu - 6 * td - 2 * te
        )
        dg3 = c1 * (-3) * (g3 ** 3) + c2 * (g3 ** 3) * (
            q_mp(11, 5) * g1s + 9 * g2s + 14 * g3s - 4 * tu - 4 * td
        )

        gq1 = hu + hd - (q_mp(1, 30) * g1s + q_mp(3, 2) * g2s + q_mp(8, 3) * g3s) * eye3
        guc1 = 2 * htu - (q_mp(8, 15) * g1s + q_mp(8, 3) * g3s) * eye3
        gdc1 = 2 * htd - (q_mp(2, 15) * g1s + q_mp(8, 3) * g3s) * eye3
        gl1 = he - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s) * eye3
        gec1 = 2 * hte - (q_mp(6, 5) * g1s) * eye3
        ghu1 = 3 * tu - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s)
        ghd1 = 3 * td + te - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s)

        if two_loop:
            gq2 = (
                -2 * (hu * hu) - 2 * (hd * hd) - 3 * tu * hu - (3 * td + te) * hd
                + q_mp(4, 5) * g1s * hu + q_mp(2, 5) * g1s * hd
                + (
                    q_mp(199, 900) * g1s * g1s + q_mp(15, 4) * g2s * g2s - q_mp(8, 9) * g3s * g3s
                    + q_mp(1, 10) * g1s * g2s + q_mp(8, 45) * g1s * g3s + 8 * g2s * g3s
                ) * eye3
            )
            guc2 = (
                -2 * (htu * htu) - 2 * (yu.H * hd * yu) - 6 * tu * htu
                + (-q_mp(2, 5) * g1s + 6 * g2s) * htu
                + (q_mp(856, 225) * g1s * g1s - q_mp(8, 9) * g3s * g3s + q_mp(128, 45) * g1s * g3s) * eye3
            )
            gdc2 = (
                -2 * (htd * htd) - 2 * (yd.H * hu * yd) - 2 * (3 * td + te) * htd
                + (q_mp(2, 5) * g1s + 6 * g2s) * htd
                + (q_mp(202, 225) * g1s * g1s - q_mp(8, 9) * g3s * g3s + q_mp(32, 45) * g1s * g3s) * eye3
            )
            gl2 = (
                -2 * (he * he) - (3 * td + te) * he + q_mp(6, 5) * g1s * he
                + (q_mp(207, 100) * g1s * g1s + q_mp(15, 4) * g2s * g2s + q_mp(9, 10) * g1s * g2s) * eye3
            )
            gec2 = (
                -2 * (hte * hte) - 2 * (3 * td + te) * hte
                + (-q_mp(6, 5) * g1s + 6 * g2s) * hte
                + (q_mp(234, 25) * g1s * g1s) * eye3
            )
            ghu2 = (
                -9 * tu2 - 3 * tud + (q_mp(4, 5) * g1s + 16 * g3s) * tu
                + q_mp(207, 100) * g1s * g1s + q_mp(15, 4) * g2s * g2s + q_mp(9, 10) * g1s * g2s
            )
            ghd2 = (
                -9 * td2 - 3 * te2 - 3 * tud + (-q_mp(2, 5) * g1s + 16 * g3s) * td + q_mp(6, 5) * g1s * te
                + q_mp(207, 100) * g1s * g1s + q_mp(15, 4) * g2s * g2s + q_mp(9, 10) * g1s * g2s
            )
            gq = c1 * gq1 + c2 * gq2
            guc = c1 * guc1 + c2 * guc2
            gdc = c1 * gdc1 + c2 * gdc2
            gl = c1 * gl1 + c2 * gl2
            gec = c1 * gec1 + c2 * gec2
            ghu = c1 * ghu1 + c2 * ghu2
            ghd = c1 * ghd1 + c2 * ghd2
        else:
            gq, guc, gdc, gl, gec, ghu, ghd = c1 * gq1, c1 * guc1, c1 * gdc1, c1 * gl1, c1 * gec1, c1 * ghu1, c1 * ghd1

        dyu = gq * yu + yu * guc + ghu * yu
        dyd = gq * yd + yd * gdc + ghd * yd
        dye = gl * ye + ye * gec + ghd * ye
        glh = gl + ghu * eye3
        dkap = glh * kap + kap * glh.T
        return (dg1, dg2, dg3, dyu, dyd, dye, dkap)

    return rhs


def integrate_soft_susy_gl4(
    g_uv: mp.mpf,
    yt0: mp.mpf,
    yb0: mp.mpf,
    ytau0: mp.mpf,
    t_span: mp.mpf,
    n_steps: int,
    a0_over_m0: mp.mpf,
    mq1_sq0: mp.mpf = mp.mpf(1),
    mq2_sq0: mp.mpf = mp.mpf(1),
) -> dict[str, mp.mpf]:
    """1-loop MSSM soft-SUSY RGEs integrated via 2-stage implicit Gauss-Legendre GL4."""
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    st0 = (
        g_uv, g_uv, g_uv, yt0, yb0, ytau0,
        mp.mpf(1), mp.mpf(1), mp.mpf(1),
        a0_over_m0, a0_over_m0, a0_over_m0,
        mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1),
        mq1_sq0, mq2_sq0, mp.mpf(0),
    )

    def rhs(v: tuple[mp.mpf, ...]) -> tuple[mp.mpf, ...]:
        (
            g1, g2, g3, yt, yb, ytau, m1, m2, m3, at, ab, atau,
            mhu2, mhd2, mq3, mu3, md3, ml3, me3, mq1, mq2, shy,
        ) = v
        g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
        yts, ybs, ytaus = yt * yt, yb * yb, ytau * ytau
        dg1 = c1 * q_mp(33, 5) * (g1 ** 3)
        dg2 = c1 * (g2 ** 3)
        dg3 = c1 * (-3) * (g3 ** 3)
        dyt = c1 * yt * (6 * yts + ybs - q_mp(13, 15) * g1s - 3 * g2s - q_mp(16, 3) * g3s)
        dyb = c1 * yb * (6 * ybs + yts + ytaus - q_mp(7, 15) * g1s - 3 * g2s - q_mp(16, 3) * g3s)
        dytau = c1 * ytau * (4 * ytaus + 3 * ybs - q_mp(9, 5) * g1s - 3 * g2s)
        dm1 = c1 * q_mp(66, 5) * g1s * m1
        dm2 = c1 * 2 * g2s * m2
        dm3 = c1 * (-6) * g3s * m3
        dat = c1 * (12 * yts * at + 2 * ybs * ab + q_mp(26, 15) * g1s * m1 + 6 * g2s * m2 + q_mp(32, 3) * g3s * m3)
        dab = c1 * (12 * ybs * ab + 2 * yts * at + 2 * ytaus * atau + q_mp(14, 15) * g1s * m1 + 6 * g2s * m2 + q_mp(32, 3) * g3s * m3)
        datau = c1 * (8 * ytaus * atau + 6 * ybs * ab + q_mp(18, 5) * g1s * m1 + 6 * g2s * m2)
        xt = 2 * yts * (mhu2 + mq3 + mu3 + at * at)
        xb = 2 * ybs * (mhd2 + mq3 + md3 + ab * ab)
        xtau = 2 * ytaus * (mhd2 + ml3 + me3 + atau * atau)
        dmhu2 = c1 * (3 * xt - 6 * g2s * m2 * m2 - q_mp(6, 5) * g1s * m1 * m1 + q_mp(3, 5) * g1s * shy)
        dmhd2 = c1 * (3 * xb + xtau - 6 * g2s * m2 * m2 - q_mp(6, 5) * g1s * m1 * m1 - q_mp(3, 5) * g1s * shy)
        dmq3 = c1 * (xt + xb - q_mp(32, 3) * g3s * m3 * m3 - 6 * g2s * m2 * m2 - q_mp(2, 15) * g1s * m1 * m1 + q_mp(1, 5) * g1s * shy)
        dmu3 = c1 * (2 * xt - q_mp(32, 3) * g3s * m3 * m3 - q_mp(32, 15) * g1s * m1 * m1 - q_mp(4, 5) * g1s * shy)
        dmd3 = c1 * (2 * xb - q_mp(32, 3) * g3s * m3 * m3 - q_mp(8, 15) * g1s * m1 * m1 + q_mp(2, 5) * g1s * shy)
        dml3 = c1 * (xtau - 6 * g2s * m2 * m2 - q_mp(6, 5) * g1s * m1 * m1 - q_mp(3, 5) * g1s * shy)
        dme3 = c1 * (2 * xtau - q_mp(24, 5) * g1s * m1 * m1 + q_mp(6, 5) * g1s * shy)
        dmq1 = c1 * (-q_mp(32, 3) * g3s * m3 * m3 - 6 * g2s * m2 * m2 - q_mp(2, 15) * g1s * m1 * m1 + q_mp(1, 5) * g1s * shy)
        dmq2 = dmq1
        dshy = c1 * q_mp(66, 5) * g1s * shy
        return (
            dg1, dg2, dg3, dyt, dyb, dytau, dm1, dm2, dm3, dat, dab, datau,
            dmhu2, dmhd2, dmq3, dmu3, dmd3, dml3, dme3, dmq1, dmq2, dshy,
        )

    sol = gl4_integrate_tuple(rhs, st0, t_span, n_steps, tol_exp=-24)
    keys = [
        "g1", "g2", "g3", "yt", "yb", "ytau", "M1", "M2", "M3", "At", "Ab", "Atau",
        "mHu2", "mHd2", "mQ3", "mu3", "md3", "mL3", "me3", "mQ1", "mQ2", "Shy",
    ]
    return dict(zip(keys, sol))


def pv_loop_i3(a: mp.mpf, b: mp.mpf, c: mp.mpf) -> mp.mpf:
    eps = p10(-10) * max(a, b, c)
    if abs(a - b) < eps and abs(b - c) < eps:
        return mp.mpf(1) / (2 * a)
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


def exact_1loop_top_higgs_pole_detail(
    lam_mu: mp.mpf, yt_mu: mp.mpf, mt_over_mu: mp.mpf
) -> tuple[mp.mpf, mp.mpf, bool]:
    """
    Exact 1-loop RG-invariant top-quark pole shift for m_h^{pole,2}/v_{phys}^2 at arbitrary scale mu:
      m_h^{pole,2}/v_{phys}^2 = lam(mu) * [ 1 + (3 yt^2 / (16 pi^2)) * ( (2 - r) ln(m_t^2/mu^2)
                                           - 1/2 + (r - 1) * b_0(r) ) ],
    where r = 4 m_t^2 / m_h^2 = 2 yt^2 / lam.
    Returns (mh_pole_over_v, delta_top, hit_positivity_floor).
    """
    r = (2 * yt_mu * yt_mu) / lam_mu
    ln_mt2_mu2 = 2 * mp.log(mt_over_mu)
    if r > 1:
        sr = mp.sqrt(r - 1)
        b0_const = 2 - 2 * sr * mp.atan(mp.mpf(1) / sr)
    elif r < 1:
        sr = mp.sqrt(1 - r)
        b0_const = 2 - sr * mp.log((1 + sr) / (1 - sr))
    else:
        b0_const = mp.mpf(2)
    delta_top = (3 * yt_mu * yt_mu / (16 * mp.pi * mp.pi)) * (
        (2 - r) * ln_mt2_mu2 - q_mp(1, 2) + (r - 1) * b0_const
    )
    raw_sq = lam_mu * (1 + delta_top)
    floor_val = p10(-10)
    clamped = bool(raw_sq <= floor_val)
    return mp.sqrt(raw_sq if raw_sq > floor_val else floor_val), delta_top, clamped


def match_and_run_sm_gl4(
    st_mssm: tuple[Any, ...],
    soft: dict[str, mp.mpf],
    tan_beta: int,
    m0_over_v: int,
    sgn_mu: int = 1,
    n_sm_steps: int = 28,
    scale_factor_over_mz: mp.mpf = mp.mpf(1),
) -> dict[str, Any]:
    """
    Exact Martin-Vaughn DR->MS + sparticle + Delta_b threshold matching at Q_match = M_stop,
    followed by full exact 2-loop SM running via GL4 down to Q = scale_factor_over_mz * M_Z,
    using the exact 1-loop RG-invariant top-Yukawa Higgs pole formula (and returning the
    broken truncated formula separately solely for Planted Fault PF_REF3_1).
    """
    g1_dr, g2_dr, g3_dr, yu_dr, yd_dr, ye_dr, kap_dr = st_mssm
    tb = mp.mpf(tan_beta)
    sinb = tb / mp.sqrt(1 + tb * tb)
    cosb = mp.mpf(1) / mp.sqrt(1 + tb * tb)
    cos2b = (1 - tb * tb) / (1 + tb * tb)

    mu_sq = (soft["mHd2"] - soft["mHu2"] * tb * tb) / (tb * tb - 1)
    mu_abs = mp.sqrt(mu_sq)
    mu_signed = mp.mpf(sgn_mu) * mu_abs
    ma_sq = soft["mHd2"] + soft["mHu2"] + 2 * mu_sq
    ma_mass = mp.sqrt(ma_sq) if ma_sq > 0 else mp.mpf(1)
    m_stop = (soft["mQ3"] * soft["mu3"]) ** q_mp(1, 4)
    m_q12 = mp.sqrt((soft["mQ1"] + soft["mQ2"]) / 2)
    m_l = mp.sqrt(soft["mL3"])
    m_e = mp.sqrt(soft["me3"])
    m2_g, m3_g = abs(soft["M2"]), abs(soft["M3"])
    q_m = m_stop

    thresh_list = [
        (m3_g, (mp.mpf(0), mp.mpf(0), mp.mpf(2))),
        (m2_g, (mp.mpf(0), q_mp(4, 3), mp.mpf(0))),
        (mu_abs, (q_mp(2, 5), q_mp(2, 3), mp.mpf(0))),
        (ma_mass, (q_mp(1, 10), q_mp(1, 6), mp.mpf(0))),
        (mp.sqrt(soft["mQ3"]), (q_mp(1, 30), q_mp(1, 2), q_mp(1, 3))),
        (mp.sqrt(soft["mu3"]), (q_mp(4, 15), mp.mpf(0), q_mp(1, 6))),
        (mp.sqrt(soft["md3"]), (q_mp(1, 15), mp.mpf(0), q_mp(1, 6))),
        (m_q12, (q_mp(11, 15), mp.mpf(1), q_mp(4, 3))),
        (m_l, (q_mp(3, 10), q_mp(1, 2), mp.mpf(0))),
        (m_e, (q_mp(3, 5), mp.mpf(0), mp.mpf(0))),
    ]
    a_dr_inv = [4 * mp.pi / (g * g) for g in (g1_dr, g2_dr, g3_dr)]
    c2_g = [mp.mpf(0), mp.mpf(2), mp.mpf(3)]
    a_ms_inv: list[mp.mpf] = []
    for idx_g in range(3):
        dr_sh = c2_g[idx_g] / (12 * mp.pi)
        sp_sh = -sum((db[idx_g] * mp.log(mi / q_m) for mi, db in thresh_list), mp.mpf(0)) / (2 * mp.pi)
        a_ms_inv.append(a_dr_inv[idx_g] + dr_sh + sp_sh)
    g1_m, g2_m, g3_m = [mp.sqrt(4 * mp.pi / ai) for ai in a_ms_inv]

    a1_m = g1_m * g1_m / (4 * mp.pi)
    a2_m = g2_m * g2_m / (4 * mp.pi)
    a3_m = g3_m * g3_m / (4 * mp.pi)

    # Exact Martin-Vaughn hep-ph/9308222 Eq. (2.8) DR -> MS Yukawa matching
    dr_u_fac = 1 + a3_m / (3 * mp.pi) - q_mp(3, 32) * a2_m / mp.pi - q_mp(1, 480) * a1_m / mp.pi
    dr_d_fac = 1 + a3_m / (3 * mp.pi) - q_mp(3, 32) * a2_m / mp.pi - q_mp(13, 480) * a1_m / mp.pi
    dr_l_fac = 1 - q_mp(3, 32) * a2_m / mp.pi + q_mp(9, 160) * a1_m / mp.pi

    i_sbot = pv_loop_i3(soft["mQ3"], soft["md3"], m3_g * m3_g)
    i_stop = pv_loop_i3(soft["mQ3"], soft["mu3"], mu_sq)
    yt_ms_approx = left_svd_asc(yu_dr)[1][2]
    delta_b = (
        (q_mp(2, 3) * a3_m / mp.pi) * m3_g * mu_signed * tb * i_sbot
        + (yt_ms_approx * yt_ms_approx / (16 * mp.pi * mp.pi)) * soft["At"] * mu_signed * tb * i_stop
    )

    yu_sm0 = (sinb * dr_u_fac) * yu_dr
    yd_sm0 = (cosb * dr_d_fac / (1 + delta_b)) * yd_dr
    ye_sm0 = (cosb * dr_l_fac) * ye_dr
    kap_sm0 = (sinb * sinb) * kap_dr

    yt_sm0_3 = left_svd_asc(yu_sm0)[1][2]
    xt_over_ms = (soft["At"] - mu_signed / tb) / m_stop
    x2 = xt_over_ms * xt_over_ms
    lam_tree = ((g2_m * g2_m + q_mp(3, 5) * g1_m * g1_m) / 4) * (cos2b * cos2b)
    lam_stop = (q_mp(3, 8) / (mp.pi * mp.pi)) * (yt_sm0_3 ** 4) * x2 * (1 - x2 / 12)
    lam_sm0 = lam_tree + lam_stop

    mz_over_v_approx = mp.sqrt((g2_m * g2_m + q_mp(3, 5) * g1_m * g1_m) / 4)
    q_match_over_mz = (mp.mpf(m0_over_v) * m_stop) / mz_over_v_approx
    t_sm = -mp.log(q_match_over_mz / scale_factor_over_mz)
    sm_rhs = make_sm_2loop_rhs(two_loop=True)
    st_q = gl4_integrate_tuple(
        sm_rhs,
        (g1_m, g2_m, g3_m, yu_sm0, yd_sm0, ye_sm0, kap_sm0, lam_sm0),
        t_sm,
        n_sm_steps,
        tol_exp=-24,
    )
    g1_z, g2_z, g3_z, yu_z, yd_z, ye_z, kap_z, lam_z = st_q

    a1_z = g1_z * g1_z / (4 * mp.pi)
    a2_z = g2_z * g2_z / (4 * mp.pi)
    a3_z = g3_z * g3_z / (4 * mp.pi)
    s2w_z = (3 * a1_z) / (3 * a1_z + 5 * a2_z)
    aem_inv_z = q_mp(5, 3) / a1_z + mp.mpf(1) / a2_z
    mz_over_v_z = mp.sqrt((g2_z * g2_z + q_mp(3, 5) * g1_z * g1_z) / 4)
    mw_over_mz_z = mp.sqrt(1 - s2w_z)

    ck_z = extract_ckm_obs(yu_z, yd_z, ye_z)
    pm_z = extract_pmns_obs(ye_z, kap_z)

    mt_ms_over_v = ck_z["yt"] / mp.sqrt(2)
    mt_over_q = (mt_ms_over_v / mz_over_v_z) / scale_factor_over_mz
    mt_pole_over_v = mt_ms_over_v * (
        1 + q_mp(4, 3) * (a3_z / mp.pi) * (1 + q_mp(3, 2) * mp.log(mp.mpf(1) / mt_over_q))
    )
    mh_ms_over_v = mp.sqrt(lam_z) if lam_z > 0 else mp.mpf(0)
    mh_ms_over_mz = mh_ms_over_v / mz_over_v_z

    if lam_z > 0:
        mh_pole_over_v, delta_top_val, hit_floor = exact_1loop_top_higgs_pole_detail(
            lam_z, ck_z["yt"], mt_over_q
        )
    else:
        mh_pole_over_v, delta_top_val, hit_floor = mp.mpf(0), mp.mpf(0), True
    mh_pole_over_mz = mh_pole_over_v / mz_over_v_z

    # Planted broken truncated formula (solely for PF_REF3_1 regression control):
    mh_pole_trunc_fac = mp.sqrt(
        max(1 + (3 * ck_z["yt"] * ck_z["yt"] / (16 * mp.pi * mp.pi)) * (2 * mp.log(mt_over_q) - 1), q_mp(1, 10))
    )
    mh_pole_trunc_over_v = mh_ms_over_v * mh_pole_trunc_fac

    return {
        "q_match_over_mz": q_match_over_mz,
        "delta_b": delta_b,
        "alpha1_inv_mz": mp.mpf(1) / a1_z,
        "alpha2_inv_mz": mp.mpf(1) / a2_z,
        "alpha3_mz": a3_z,
        "sin2_thetaW_mz": s2w_z,
        "alpha_EM_inv_mz": aem_inv_z,
        "mw_over_mz": mw_over_mz_z,
        "mz_over_v": mz_over_v_z,
        "lam_q": lam_z,
        "delta_top": delta_top_val,
        "higgs_pole_hit_floor": hit_floor,
        "mt_ms_over_v": mt_ms_over_v,
        "mt_pole_over_v": mt_pole_over_v,
        "mh_ms_over_mz": mh_ms_over_mz,
        "mh_pole_over_mz": mh_pole_over_mz,
        "mh_pole_over_v": mh_pole_over_v,
        "mh_pole_trunc_over_v": mh_pole_trunc_over_v,
        "ckm_mz": ck_z,
        "pmns_mz": pm_z,
    }


# ==============================================================================
# REF-2: E_8 240-Root Clebsch, M=8 CIM 2D Gauss-Legendre, B3 SUGRA, GL10/GL6 Liouville
# ==============================================================================

def run_ref2_e8_cim_and_dirac_liouville(ow26_res: dict[str, Any]) -> dict[str, Any]:
    mp.mp.dps = 30

    # --- 1. E_8 240-Root Construction & Exact SU(5)_vis x SU(5)_hid Dynkin Classification ---
    roots: list[tuple[Fr, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    vec = [Fr(0)] * 8
                    vec[i], vec[j] = Fr(s1), Fr(s2)
                    roots.append(tuple(vec))
    for mask in range(256):
        sgn = [1 if ((mask >> k) & 1) else -1 for k in range(8)]
        if sum(1 for s in sgn if s == -1) % 2 == 0:
            roots.append(tuple(Fr(s, 2) for s in sgn))

    def rdot(a: tuple[Fr, ...], b: tuple[Fr, ...]) -> Fr:
        return sum((a[k] * b[k] for k in range(8)), Fr(0))

    vis_simple = [
        (Fr(1), Fr(-1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)),
        (Fr(0), Fr(1), Fr(-1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)),
        (Fr(0), Fr(0), Fr(1), Fr(-1), Fr(0), Fr(0), Fr(0), Fr(0)),
        (Fr(0), Fr(0), Fr(0), Fr(1), Fr(-1), Fr(0), Fr(0), Fr(0)),
    ]
    vis_a4 = [r for r in roots if r[5] == 0 and r[6] == 0 and r[7] == 0 and sum(r[:5]) == 0]
    hid_a4 = [r for r in roots if r[0] == r[1] == r[2] == r[3] == r[4]]
    w_z5 = (Fr(1, 5), Fr(1, 5), Fr(1, 5), Fr(1, 5), Fr(-4, 5), Fr(0), Fr(0), Fr(0))
    buckets: dict[Fr, list[tuple[Fr, ...]]] = {}
    for r in roots:
        buckets.setdefault(rdot(r, w_z5) % 1, []).append(r)

    sector_vis_highest: dict[str, tuple[int, ...]] = {}
    for q_idx in (1, 2, 3, 4):
        q_val = Fr(q_idx, 5)
        dynkins = [tuple(int(rdot(r, a_i)) for a_i in vis_simple) for r in buckets[q_val]]
        pos_dom = sorted({d for d in dynkins if all(x >= 0 for x in d)})
        sector_vis_highest[f"q_{q_idx}_over_5"] = pos_dom[0] if len(pos_dom) == 1 else tuple()

    root_set = set(roots)
    rep_10_5bar = buckets[Fr(2, 5)]
    rep_5bar_10bar = buckets[Fr(4, 5)]

    up_10_10_5h = 0
    for a in rep_10_5bar:
        for b in rep_10_5bar:
            if rdot(a, b) == -1:
                g = tuple(-(a[k] + b[k]) for k in range(8))
                if g in root_set and (rdot(g, w_z5) % 1) == Fr(1, 5):
                    up_10_10_5h += 1

    dn_10_5bar_5barh = 0
    for a in rep_10_5bar:
        for b in rep_5bar_10bar:
            if rdot(a, b) == -1:
                g = tuple(-(a[k] + b[k]) for k in range(8))
                if g in root_set and (rdot(g, w_z5) % 1) == Fr(4, 5):
                    dn_10_5bar_5barh += 1

    x1, x2, gs = sp.symbols("x1 x2 g", positive=True)
    e12 = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    e23 = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
    phi1 = x1 * e12 / sp.sqrt(2)
    phi2 = x2 * e23 / sp.sqrt(2)
    a_mats = [
        (phi1 + phi1.H) / sp.sqrt(2),
        (phi1 - phi1.H) / (sp.I * sp.sqrt(2)),
        (phi2 + phi2.H) / sp.sqrt(2),
        (phi2 - phi2.H) / (sp.I * sp.sqrt(2)),
    ]
    v_ym = sp.simplify(
        sum(
            (-gs * gs * ((a_mats[i] * a_mats[j] - a_mats[j] * a_mats[i]) ** 2).trace() for i in range(4) for j in range(i + 1, 4)),
            sp.Integer(0),
        )
    )
    d_comm = (phi1.H * phi1 - phi1 * phi1.H) + (phi2.H * phi2 - phi2 * phi2.H)
    v_d_exact = sp.simplify(gs * gs * (d_comm * d_comm).trace())
    y_root_sq_over_g2 = sp.simplify((v_ym - v_d_exact) / (gs * gs * x1 * x1 * x2 * x2))
    v_d_wrong = sp.Rational(1, 2) * v_d_exact
    vf_wrong_poly = sp.expand(v_ym - v_d_wrong)
    pf3_vd_wrong_caught = bool(sp.Poly(vf_wrong_poly, x1, x2).coeff_monomial(x1 ** 4) != 0)

    e8_ok = bool(
        len(roots) == 240
        and len(vis_a4) == 20
        and len(hid_a4) == 20
        and sector_vis_highest["q_1_over_5"] == (1, 0, 0, 0)
        and sector_vis_highest["q_2_over_5"] == (0, 1, 0, 0)
        and sector_vis_highest["q_3_over_5"] == (0, 0, 1, 0)
        and sector_vis_highest["q_4_over_5"] == (0, 0, 0, 1)
        and up_10_10_5h == 600
        and dn_10_5bar_5barh == 600
        and y_root_sq_over_g2 == 1
    )

    # --- 2. M = 8 Magnetized T^2/Z_2 CIM Overlap via Composite 2D Gauss-Legendre ---
    mp.mp.dps = 28
    tau0 = q_mp(2, 5) + I_UNIT * q_mp(1, 5)
    im_t0 = mp.im(tau0)
    q_8_c = mp.exp(I_UNIT * mp.pi * 8 * tau0)
    q_16_c = mp.exp(I_UNIT * mp.pi * 16 * tau0)
    pref_8 = (16 * im_t0) ** q_mp(1, 4)
    pref_16 = (32 * im_t0) ** q_mp(1, 4)

    def psi_mag_jtheta(j: int, m_flux: int, x: mp.mpf, y: mp.mpf) -> mp.mpc:
        z = x + y * tau0
        pref = pref_8 if m_flux == 8 else pref_16
        q_m = q_8_c if m_flux == 8 else q_16_c
        jm = q_mp(j, m_flux)
        th = mp.exp(I_UNIT * mp.pi * m_flux * tau0 * jm * jm + 2 * I_UNIT * mp.pi * j * z) * mp.jtheta(
            3, mp.pi * (m_flux * z + j * tau0), q_m
        )
        return pref * mp.exp(I_UNIT * mp.pi * m_flux * z * y) * th

    n_sub, n_gl = 7, 9
    gl_x, gl_w = gauss_legendre_newton(n_gl)
    cell_h = q_mp(1, n_sub)
    pts_1d: list[tuple[mp.mpf, mp.mpf]] = []
    for c_i in range(n_sub):
        x_lo = c_i * cell_h
        for gx, gw in zip(gl_x, gl_w):
            pts_1d.append((x_lo + (gx + 1) * cell_h / 2, gw * cell_h / 2))

    gram_odd = mp.zeros(3, 3)
    raw_112_gl = mp.mpc(0)
    odd_112_gl = mp.mpc(0)
    inv_s2 = mp.mpf(1) / mp.sqrt(2)
    for xv, wx in pts_1d:
        for yv, wy in pts_1d:
            wt = wx * wy
            p1 = psi_mag_jtheta(1, 8, xv, yv)
            p7 = psi_mag_jtheta(7, 8, xv, yv)
            p2 = psi_mag_jtheta(2, 8, xv, yv)
            p6 = psi_mag_jtheta(6, 8, xv, yv)
            p3 = psi_mag_jtheta(3, 8, xv, yv)
            p5 = psi_mag_jtheta(5, 8, xv, yv)
            odd_v = [(p1 - p7) * inv_s2, (p2 - p6) * inv_s2, (p3 - p5) * inv_s2]
            for r_i in range(3):
                for c_i in range(3):
                    gram_odd[r_i, c_i] += wt * odd_v[r_i] * mp.conj(odd_v[c_i])
            h2_raw = psi_mag_jtheta(2, 16, xv, yv)
            h14_raw = psi_mag_jtheta(14, 16, xv, yv)
            h2_even = (h2_raw + h14_raw) * inv_s2
            raw_112_gl += wt * p1 * p1 * mp.conj(h2_raw)
            odd_112_gl += wt * odd_v[0] * odd_v[0] * mp.conj(h2_even)

    gram_odd_err = max(abs(gram_odd[r, c] - (1 if r == c else 0)) for r in range(3) for c in range(3))

    def cim_raw_analytic(j1: int, j2: int, j3: int) -> mp.mpc:
        if (j1 + j2 - j3) % 8 != 0:
            return mp.mpc(0)
        r_par = ((j3 - j1 - j2) // 8) % 2
        a_f = q_mp((j1 - j2 + 8 * r_par) % 16, 16)
        th_v = mp.exp(I_UNIT * mp.pi * 16 * tau0 * a_f * a_f) * mp.jtheta(3, mp.pi * 16 * a_f * tau0, q_16_c)
        return ((8 * im_t0) ** q_mp(1, 4)) * th_v

    def cim_ooe(k1: int, k2: int, kh: int) -> mp.mpc:
        t1 = [(k1, 1), (8 - k1, -1)]
        t2 = [(k2, 1), (8 - k2, -1)]
        th = [(kh, 1)] if kh in (0, 8) else [(kh, 1), (16 - kh, 1)]
        nf = q_mp(1, 2) if kh in (0, 8) else (mp.mpf(1) / (2 * mp.sqrt(2)))
        acc = mp.mpc(0)
        for j1, s1 in t1:
            for j2, s2 in t2:
                for j3, s3 in th:
                    acc += s1 * s2 * s3 * cim_raw_analytic(j1, j2, j3)
        return nf * acc

    cim_raw_gl_err = abs(raw_112_gl - cim_raw_analytic(1, 1, 2))
    cim_ooe_gl_err = abs(odd_112_gl - cim_ooe(1, 1, 2))
    cim_max_yt = mp.mpf(0)
    cim_min_yt = mp.mpf(10)
    cim_svds_max_diff = mp.mpf(0)
    prod_cim = ow26_res["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B2_M8_cim_L2_triple_overlap"]
    for kh in range(9):
        ym = mp.matrix([[cim_ooe(r + 1, c + 1, kh) for c in range(3)] for r in range(3)])
        _, sv = left_svd_asc(ym)
        p_sv = [mp.mpf(s) for s in prod_cim["all_9_Z2_even_Higgs_svds"][f"kH_{kh}"]]
        for j_i in range(3):
            cim_svds_max_diff = max(cim_svds_max_diff, abs(sv[j_i] - p_sv[j_i]))
        if sv[2] > cim_max_yt:
            cim_max_yt = sv[2]
        if sv[2] > p10(-10) and sv[2] < cim_min_yt:
            cim_min_yt = sv[2]

    # --- 2b. Independent B3 SUGRA m_{3/2} Planck-Factor Audit ---
    prod_b3 = ow26_res["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B3_sugra_m32_planck_factor"]
    b3_max_rel_diff = mp.mpf(0)
    for row in prod_b3:
        a_inv = mp.mpf(row["alpha_UV_inv"])
        lam_hid = mp.exp(-q_mp(2, 15) * mp.pi * a_inv)
        mg_g2 = mp.sqrt(mp.mpf(1) / (4 * mp.pi * a_inv))
        mkk_red = mp.mpf(row["M_KK_over_M_Pl_OW23C"])
        m32_g2 = (lam_hid ** 3) * (mg_g2 ** 2) / mp.sqrt(3)
        m32_mkk = (lam_hid ** 3) * (mkk_red ** 2) / mp.sqrt(3)
        t_ow25 = q_mp(2, 5) * mp.pi * a_inv
        t_g2 = -mp.log(m32_g2)
        t_mkk = -mp.log(m32_mkk)
        b3_max_rel_diff = max(
            b3_max_rel_diff,
            rel_diff_mp(lam_hid, mp.mpf(row["Lambda_hid_over_M_GUT"])),
            rel_diff_mp(mg_g2, mp.mpf(row["M_GUT_over_M_Pl_sqrt_aUV_4pi"])),
            rel_diff_mp(m32_g2, mp.mpf(row["m32_over_M_GUT_using_G2"])),
            rel_diff_mp(m32_mkk, mp.mpf(row["m32_over_M_GUT_using_MKK"])),
            rel_diff_mp(t_ow25, mp.mpf(row["t_OW25_no_Planck_factor"])),
            rel_diff_mp(t_g2, mp.mpf(row["t_SUGRA_using_G2"])),
            rel_diff_mp(t_mkk, mp.mpf(row["t_SUGRA_using_MKK"])),
        )

    # --- 3. Disjoint 5-Stage GL10 / 3-Stage GL6 Fuchsian ODE & Polar-Cusp Quadrature ---
    # 5-stage GL10 (O(h^10), symplectic) at 38 dps, 48/72 steps & step_frac=1/12 resolves
    # Referee v2's tr_comm (~1e-20) and z2_evenness (~1e-15) precision limits cleanly!
    mp.mp.dps = 38
    tau8_p = q_mp(16, 5) + I_UNIT * q_mp(8, 5)
    tau_r = q_mp(1, 5) + I_UNIT * q_mp(8, 5)
    q_r = mp.exp(I_UNIT * mp.pi * tau_r)
    q_8 = mp.exp(I_UNIT * mp.pi * tau8_p)
    t20 = mp.jtheta(2, 0, q_r)
    t30 = mp.jtheta(3, 0, q_r)
    e3_w = -(mp.pi ** 2) * (t20 ** 4 + t30 ** 4) / 3

    def wp_e3(z: mp.mpc) -> mp.mpc:
        pz = mp.pi * z
        return e3_w + (mp.pi * t20 * t30 * mp.jtheta(4, pz, q_r) / mp.jtheta(1, pz, q_r)) ** 2

    def dist_lat(z: mp.mpc) -> mp.mpf:
        b = mp.im(z) / mp.im(tau_r)
        a = mp.re(z) - b * mp.re(tau_r)
        a -= mp.nint(a)
        b -= mp.nint(b)
        zc = a + b * tau_r
        return min(abs(zc + m + n * tau_r) for m in (-1, 0, 1) for n in (-1, 0, 1))

    c10, b10, a10 = build_gl_tableau(5)
    a10_sq = a10 * a10

    def gl_fuchsian_step(
        z0: mp.mpc,
        dz: mp.mpc,
        c_val: mp.mpc,
        c_tab: list[mp.mpf],
        b_tab: list[mp.mpf],
        a_tab: mp.matrix,
        a_sq: mp.matrix,
    ) -> mp.matrix:
        s = len(c_tab)
        qv = [q_mp(1, 4) * (c_val - wp_e3(z0 + c_tab[i] * dz)) for i in range(s)]
        dz2 = dz * dz
        l_mat = mp.eye(s)
        for i in range(s):
            for j in range(s):
                l_mat[i, j] -= dz2 * a_sq[i, j] * qv[j]
        rhs_2 = mp.zeros(s, 2)
        for i in range(s):
            rhs_2[i, 0] = mp.mpc(1)
            rhs_2[i, 1] = dz * c_tab[i]
        u_sol = (l_mat ** (-1)) * rhs_2
        step_m = mp.zeros(2, 2)
        for col in range(2):
            u0 = mp.mpc(1) if col == 0 else mp.mpc(0)
            v0 = mp.mpc(0) if col == 0 else mp.mpc(1)
            qu = [qv[i] * u_sol[i, col] for i in range(s)]
            v_st = [v0 + dz * sum((a_tab[i, j] * qu[j] for j in range(s)), mp.mpc(0)) for i in range(s)]
            step_m[0, col] = u0 + dz * sum((b_tab[i] * v_st[i] for i in range(s)), mp.mpc(0))
            step_m[1, col] = v0 + dz * sum((b_tab[i] * qu[i] for i in range(s)), mp.mpc(0))
        return step_m

    def prop_uniform_gl10(zs: mp.mpc, ze: mp.mpc, c_val: mp.mpc, n_st: int) -> mp.matrix:
        dz = (ze - zs) / mp.mpf(n_st)
        m = mp.eye(2)
        for s_i in range(n_st):
            m = gl_fuchsian_step(zs + s_i * dz, dz, c_val, c10, b10, a10, a10_sq) * m
        return m

    def prop_adaptive_gl10(zs: mp.mpc, ze: mp.mpc, c_val: mp.mpc, step_frac: Fr = Fr(1, 12)) -> mp.matrix:
        m = mp.eye(2)
        zc = zs
        sf = q_mp(step_frac.numerator, step_frac.denominator)
        sf_mid = q_mp(3 * step_frac.numerator, 2 * step_frac.denominator)
        for _ in range(500):
            rem = ze - zc
            d_rem = abs(rem)
            if d_rem < p10(-30):
                break
            max_st = sf * dist_lat(zc)
            step = rem if d_rem <= max_st else rem * (max_st / d_rem)
            while abs(step) > sf_mid * dist_lat(zc + q_mp(1, 2) * step):
                step *= q_mp(1, 2)
            m = gl_fuchsian_step(zc, step, c_val, c10, b10, a10, a10_sq) * m
            zc = zc + step
        return m

    z0_base = (1 + tau_r) / 2

    def resid_2trace(cr: mp.mpf, ci: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        cv = mp.mpc(cr, ci)
        ma = prop_uniform_gl10(z0_base, z0_base + 1, cv, 48)
        mb = prop_uniform_gl10(z0_base, z0_base + tau_r, cv, 72)
        return mp.im(ma[0, 0] + ma[1, 1]), mp.im(mb[0, 0] + mb[1, 1])

    c_star = mp.mpc(-1, -q_mp(1, 10))
    h_fd = p10(-8)
    for _ in range(16):
        r0a, r0b = resid_2trace(mp.re(c_star), mp.im(c_star))
        nrm = mp.sqrt(r0a * r0a + r0b * r0b)
        if nrm < p10(-28):
            break
        dra, drb = resid_2trace(mp.re(c_star) + h_fd, mp.im(c_star))
        dia, dib = resid_2trace(mp.re(c_star), mp.im(c_star) + h_fd)
        j11, j12 = (dra - r0a) / h_fd, (dia - r0a) / h_fd
        j21, j22 = (drb - r0b) / h_fd, (dib - r0b) / h_fd
        det_j = j11 * j22 - j12 * j21
        dcr = -(j22 * r0a - j12 * r0b) / det_j
        dci = -(-j21 * r0a + j11 * r0b) / det_j
        c_star += mp.mpc(dcr, dci)
        if nrm < p10(-12):
            h_fd = p10(-16)

    ta = prop_uniform_gl10(z0_base, z0_base + 1, c_star, 48)
    tb = prop_uniform_gl10(z0_base, z0_base + tau_r, c_star, 72)
    tab = ta * tb
    im_tr_ab_independent = abs(mp.im(tab[0, 0] + tab[1, 1]))
    comm_ab = ta * tb * (ta ** (-1)) * (tb ** (-1))
    tr_comm_err = abs(comm_ab[0, 0] + comm_ab[1, 1] + 2)
    symplectic_det_err = max(
        abs(ta[0, 0] * ta[1, 1] - ta[0, 1] * ta[1, 0] - 1),
        abs(tb[0, 0] * tb[1, 1] - tb[0, 1] * tb[1, 0] - 1),
    )

    tr_a = mp.re(ta[0, 0] + ta[1, 1])
    disc = mp.sqrt(tr_a * tr_a - 4)
    lam1, lam2 = (tr_a + disc) / 2, (tr_a - disc) / 2
    v1 = mp.matrix([ta[0, 1], lam1 - ta[0, 0]]) if abs(ta[0, 1]) > p10(-5) else mp.matrix([lam1 - ta[1, 1], ta[1, 0]])
    v2 = mp.matrix([ta[0, 1], lam2 - ta[0, 0]]) if abs(ta[0, 1]) > p10(-5) else mp.matrix([lam2 - ta[1, 1], ta[1, 0]])
    v_mat = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    v_mat = v_mat / mp.sqrt(v_mat[0, 0] * v_mat[1, 1] - v_mat[0, 1] * v_mat[1, 0])
    tb_p = (v_mat ** (-1)) * tb * v_mat
    ph_r = mp.arg(tb_p[0, 1])
    p_mat = v_mat * mp.matrix([[mp.exp(I_UNIT * ph_r / 2), 0], [0, mp.exp(-I_UNIT * ph_r / 2)]])

    def eval_e2phi_gl10(z_pt: mp.mpc, step_frac: Fr = Fr(1, 12)) -> mp.mpf:
        m_p = prop_adaptive_gl10(z0_base, z_pt, c_star, step_frac=step_frac)
        u1 = m_p[0, 0] * p_mat[0, 0] + m_p[0, 1] * p_mat[1, 0]
        u2 = m_p[0, 0] * p_mat[0, 1] + m_p[0, 1] * p_mat[1, 1]
        im_p = mp.im(u1 * mp.conj(u2))
        return mp.mpf(1) / (im_p * im_p)

    z_chk = q_mp(23, 100) + q_mp(31, 100) * tau_r
    z2_even_err = abs(eval_e2phi_gl10(z_chk, step_frac=Fr(1, 12)) - eval_e2phi_gl10(-z_chk, step_frac=Fr(1, 12)))
    r4, r5 = p10(-4), p10(-5)
    bc_r4 = mp.mpf(1) / (r4 * mp.sqrt(eval_e2phi_gl10(r4, step_frac=Fr(1, 10)))) + mp.log(r4)
    bc_r5 = mp.mpf(1) / (r5 * mp.sqrt(eval_e2phi_gl10(r5, step_frac=Fr(1, 10)))) + mp.log(r5)
    bc_star = (100 * bc_r5 - bc_r4) / 99

    # Polar-cusp quadrature at 24 dps with Newton-Raphson Legendre roots + GL6 ray propagation
    mp.mp.dps = 24
    c6_q, b6_q, a6_q = build_gl_tableau(3)
    a6_q_sq = a6_q * a6_q

    def prop_ray_gl6(zs: mp.mpc, ze: mp.mpc, m_init: mp.matrix) -> mp.matrix:
        m = m_init
        zc = zs
        sf = q_mp(1, 4)
        sf_mid = q_mp(3, 8)
        for _ in range(120):
            rem = ze - zc
            d_rem = abs(rem)
            if d_rem < p10(-20):
                break
            max_st = sf * dist_lat(zc)
            step = rem if d_rem <= max_st else rem * (max_st / d_rem)
            while abs(step) > sf_mid * dist_lat(zc + q_mp(1, 2) * step):
                step *= q_mp(1, 2)
            m = gl_fuchsian_step(zc, step, c_star, c6_q, b6_q, a6_q, a6_q_sq) * m
            zc = zc + step
        return m

    corners = [
        q_mp(1, 2) + q_mp(1, 2) * tau_r,
        -q_mp(1, 2) + q_mp(1, 2) * tau_r,
        -q_mp(1, 2) - q_mp(1, 2) * tau_r,
        q_mp(1, 2) - q_mp(1, 2) * tau_r,
    ]
    ang_s = sorted(mp.arg(c_pt) % (2 * mp.pi) for c_pt in corners)
    half_sectors = [(ang_s[0], ang_s[1]), (ang_s[1], ang_s[2])]

    def r_bdy(th: mp.mpf) -> mp.mpf:
        db = mp.sin(th) / mp.im(tau_r)
        da = mp.cos(th) - db * mp.re(tau_r)
        return q_mp(1, 2) / max(abs(da), abs(db))

    def e2_dens(z_pt: mp.mpc, q_use: mp.mpc) -> list[mp.mpf]:
        yv = mp.im(z_pt)
        t2v = mp.im(tau_r)
        fac = mp.sqrt(2 * t2v) * mp.exp(-2 * mp.pi * yv * yv / t2v)
        pz = mp.pi * z_pt
        return [fac * (abs(mp.jtheta(k, pz, q_use)) ** 2) for k in (4, 2, 3)]

    def run_polar_gl6(n_th: int, n_t: int) -> dict[str, Any]:
        gx_th, gw_th = gauss_legendre_newton(n_th)
        gx_t, gw_t = gauss_legendre_newton(n_t)
        hyp_area = mp.mpf(0)
        k_s0_tr = [mp.mpf(0)] * 3
        k_s0_t8 = [mp.mpf(0)] * 3
        k_s12_tr = [mp.mpf(0)] * 3
        k_s12_t8 = [mp.mpf(0)] * 3
        for th_a, th_b in half_sectors:
            h_th = (th_b - th_a) / 2
            m_th = (th_b + th_a) / 2
            for ix in range(n_th):
                th = m_th + h_th * gx_th[ix]
                w_th = 2 * h_th * gw_th[ix]
                rmax = r_bdy(th)
                tmax = mp.mpf(1) / (-mp.log(rmax) + bc_star)
                h_t = tmax / 2
                t_nodes = [h_t + h_t * gx_t[it] for it in range(n_t)]
                r_nodes = [mp.exp(bc_star - mp.mpf(1) / tv) for tv in t_nodes]
                z_cur = z0_base
                m_cur = mp.eye(2)
                dir_c = mp.exp(I_UNIT * th)
                for it in range(n_t - 1, -1, -1):
                    tv = t_nodes[it]
                    rv = r_nodes[it]
                    wt = h_t * gw_t[it]
                    zv = rv * dir_c
                    jac_t = (rv * rv) / (tv * tv)
                    if rv < p10(-6):
                        w_s0 = mp.mpf(1)
                        w_s12 = rv / tv
                    else:
                        m_cur = prop_ray_gl6(z_cur, zv, m_cur)
                        z_cur = zv
                        u1 = m_cur[0, 0] * p_mat[0, 0] + m_cur[0, 1] * p_mat[1, 0]
                        u2 = m_cur[0, 0] * p_mat[0, 1] + m_cur[0, 1] * p_mat[1, 1]
                        im_p = mp.im(u1 * mp.conj(u2))
                        e2om = mp.mpf(1) / (im_p * im_p)
                        w_s0 = jac_t * e2om
                        w_s12 = jac_t * mp.sqrt(e2om)
                    d_tr = e2_dens(zv, q_r)
                    d_t8 = e2_dens(zv, q_8)
                    hyp_area += w_th * wt * w_s0
                    for j in range(3):
                        k_s0_tr[j] += (w_th * wt * w_s0 / (2 * mp.pi)) * d_tr[j]
                        k_s0_t8[j] += (w_th * wt * w_s0 / (2 * mp.pi)) * d_t8[j]
                        k_s12_tr[j] += (w_th * wt * w_s12) * d_tr[j]
                        k_s12_t8[j] += (w_th * wt * w_s12) * d_t8[j]
        mean_tr = sum(k_s12_tr, mp.mpf(0)) / 3
        mean_t8 = sum(k_s12_t8, mp.mpf(0)) / 3
        return {
            "hyp_area_over_2pi": hyp_area / (2 * mp.pi),
            "K_s0_tr": k_s0_tr,
            "K_s0_t8": k_s0_t8,
            "G_s12_um_tr": [v / mean_tr for v in k_s12_tr],
            "G_s12_um_t8": [v / mean_t8 for v in k_s12_t8],
        }

    qc = run_polar_gl6(10, 12)
    qf = run_polar_gl6(14, 16)
    gb_err = abs(qf["hyp_area_over_2pi"] - 1)
    s12_grid_diff = max(abs(qf["G_s12_um_t8"][j] - qc["G_s12_um_t8"][j]) for j in range(3))

    mp.mp.dps = 30
    prod_b4 = ow26_res["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B4_spin_half_dirac_liouville_kahler"]
    prod_g_t8 = [mp.mpf(s) for s in prod_b4["G_s12_dirac_unit_mean_t8"]]
    prod_k_s0_t8 = [mp.mpf(s) for s in prod_b4["K_s0_scalar_recomputed_t8"]]
    prod_k_s0_tr = [mp.mpf(s) for s in prod_b4["K_s0_scalar_recomputed_tr"]]
    g_s12_t8_vs_prod_err = max(abs(qf["G_s12_um_t8"][j] - prod_g_t8[j]) for j in range(3))
    k_s0_t8_vs_prod_err = max(abs(qf["K_s0_t8"][j] - prod_k_s0_t8[j]) for j in range(3))
    k_s0_tr_vs_prod_err = max(abs(qf["K_s0_tr"][j] - prod_k_s0_tr[j]) for j in range(3))

    phi_s = sp.Symbol("phi", real=True)
    w_kin_s12 = sp.simplify(sp.exp(2 * phi_s) * sp.exp(-phi_s / 2) * sp.exp(-phi_s / 2))
    w_yuk_s12 = sp.simplify(sp.exp(2 * phi_s) * sp.exp(-phi_s / 2) * sp.exp(-phi_s) * sp.exp(-phi_s / 2))
    weyl_ok = bool(w_kin_s12 == sp.exp(phi_s) and w_yuk_s12 == 1)
    weyl_scalar_diff_ok = bool(sp.simplify(sp.exp(2 * phi_s) - w_kin_s12) != 0)

    return {
        "E8_240root_clebsch": {
            "passed": e8_ok,
            "total_roots": len(roots),
            "vis_A4_roots": len(vis_a4),
            "hid_A4_roots": len(hid_a4),
            "actual_SU5_vis_highest_dynkin_by_z5_sector": {k: list(v) for k, v in sector_vis_highest.items()},
            "up_10_10_5H_ordered_triplets": up_10_10_5h,
            "dn_10_5bar_5barH_ordered_triplets": dn_10_5bar_5barh,
            "VF_plus_VD_eq_VYM_y_root_sq_over_g2": str(y_root_sq_over_g2),
        },
        "M8_CIM_2D_GaussLegendre": {
            "quadrature_rule": "Composite 2D Gauss-Legendre (7x7 cells x 9x9 Newton-Raphson Legendre nodes, coprime to M=8,16)",
            "Z2_odd_3x3_Gram_err": fmt_mp(gram_odd_err, 10),
            "raw_112_GL2D_vs_analytic_err": fmt_mp(cim_raw_gl_err, 10),
            "odd_odd_even_112_GL2D_vs_analytic_err": fmt_mp(cim_ooe_gl_err, 10),
            "all_9_Higgs_SVDs_max_diff_vs_producer": fmt_mp(cim_svds_max_diff, 10),
            "yt_over_gUV_min_nonzero": fmt_mp(cim_min_yt, 12),
            "yt_over_gUV_max": fmt_mp(cim_max_yt, 12),
            "passed": bool(
                gram_odd_err < p10(-15)
                and cim_raw_gl_err < p10(-15)
                and cim_ooe_gl_err < p10(-15)
                and cim_svds_max_diff < p10(-11)
            ),
        },
        "B3_SUGRA_Planck_Factor": {
            "max_rel_diff_vs_producer_all_3_rows": fmt_mp(b3_max_rel_diff, 10),
            "passed": bool(b3_max_rel_diff < p10(-10)),
        },
        "Dirac_s12_Liouville_GL10_GL6": {
            "ode_method": "5-stage GL10 (38 dps, 48/72-step c_* 2-trace Newton & step_frac=1/12 z2_evenness) + 3-stage GL6 rays with e_3-form wp(z)",
            "weyl_6D_identity_ok": weyl_ok,
            "c_star_re": fmt_mp(mp.re(c_star), 18),
            "c_star_im": fmt_mp(mp.im(c_star), 18),
            "im_tr_TaTb_independent_check": fmt_mp(im_tr_ab_independent, 10),
            "tr_comm_err": fmt_mp(tr_comm_err, 10),
            "symplectic_det_err": fmt_mp(symplectic_det_err, 10),
            "z2_evenness_err": fmt_mp(z2_even_err, 10),
            "bc_star_tau8": fmt_mp(bc_star, 14),
            "gauss_bonnet_area_over_2pi": fmt_mp(qf["hyp_area_over_2pi"], 12),
            "gauss_bonnet_err": fmt_mp(gb_err, 10),
            "G_s12_dirac_unit_mean_t8": [fmt_mp(v, 12) for v in qf["G_s12_um_t8"]],
            "G_s12_dirac_unit_mean_tr": [fmt_mp(v, 12) for v in qf["G_s12_um_tr"]],
            "K_s0_scalar_t8": [fmt_mp(v, 12) for v in qf["K_s0_t8"]],
            "K_s0_scalar_tr": [fmt_mp(v, 12) for v in qf["K_s0_tr"]],
            "G_s12_t8_max_diff_vs_producer": fmt_mp(g_s12_t8_vs_prod_err, 10),
            "K_s0_t8_max_diff_vs_producer": fmt_mp(k_s0_t8_vs_prod_err, 10),
            "K_s0_tr_max_diff_vs_producer": fmt_mp(k_s0_tr_vs_prod_err, 10),
            "s12_coarse_vs_fine_err": fmt_mp(s12_grid_diff, 10),
            "passed": bool(
                weyl_ok
                and tr_comm_err < p10(-18)
                and symplectic_det_err < p10(-28)
                and z2_even_err < p10(-14)
                and gb_err < p10(-6)
                and g_s12_t8_vs_prod_err < p10(-6)
                and k_s0_t8_vs_prod_err < p10(-6)
                and k_s0_tr_vs_prod_err < p10(-6)
            ),
        },
        "_internal": {
            "G_s12_tr": qf["G_s12_um_tr"],
            "G_s12_t8": qf["G_s12_um_t8"],
            "K_s0_t8": qf["K_s0_t8"],
            "K_s0_tr": qf["K_s0_tr"],
            "yt_cim_max": cim_max_yt,
            "yt_cim_min": cim_min_yt,
            "pf3_vd_wrong_caught": pf3_vd_wrong_caught,
            "weyl_scalar_diff_ok": weyl_scalar_diff_ok,
        },
    }


# ==============================================================================
# REF-3: Sequential Seesaw (GL4 + Real 6x6 Takagi), Weisskopf-Wigner, Stiff GL4 Boltzmann
# ==============================================================================

def mssm_seesaw_rhs(st: tuple[Any, ...]) -> tuple[Any, ...]:
    g1, g2, g3, yu, yd, ye, kap, ynu, mr = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = mp.eye(3)
    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
    hn, htn = ynu * ynu.H, ynu.H * ynu
    tu, td, te, tn = mp.re(tr_mp(hu)), mp.re(tr_mp(hd)), mp.re(tr_mp(he)), mp.re(tr_mp(hn))

    dg1 = c1 * q_mp(33, 5) * (g1 ** 3)
    dg2 = c1 * (g2 ** 3)
    dg3 = c1 * (-3) * (g3 ** 3)
    gq = c1 * (hu + hd - (q_mp(1, 30) * g1s + q_mp(3, 2) * g2s + q_mp(8, 3) * g3s) * eye3)
    guc = c1 * (2 * htu - (q_mp(8, 15) * g1s + q_mp(8, 3) * g3s) * eye3)
    gdc = c1 * (2 * htd - (q_mp(2, 15) * g1s + q_mp(8, 3) * g3s) * eye3)
    gl = c1 * (he + hn - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s) * eye3)
    gec = c1 * (2 * hte - (q_mp(6, 5) * g1s) * eye3)
    ghu = c1 * (3 * tu + tn - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s))
    ghd = c1 * (3 * td + te - (q_mp(3, 10) * g1s + q_mp(3, 2) * g2s))
    gnuc = c1 * (2 * htn)

    dyu = gq * yu + yu * guc + ghu * yu
    dyd = gq * yd + yd * gdc + ghd * yd
    dye = gl * ye + ye * gec + ghd * ye
    glh = gl + ghu * eye3
    dkap = glh * kap + kap * glh.T
    dynu = gl * ynu + ynu * gnuc + ghu * ynu
    dmr = gnuc.T * mr + mr * gnuc
    return (dg1, dg2, dg3, dyu, dyd, dye, dkap, dynu, dmr)


def run_seq_seesaw_gl4(
    g_uv: mp.mpf,
    yu_uv: mp.matrix,
    yd_uv: mp.matrix,
    ye_uv: mp.matrix,
    ynu_uv: mp.matrix,
    mr_uv_dimless: mp.matrix,
    mr0_over_mgut: mp.mpf,
    t_gut_to_susy: mp.mpf,
    soft: dict[str, mp.mpf],
    tan_beta: int,
    m0_over_v: int,
    sgn_mu: int = 1,
    n_seg_steps: int = 12,
    n_mssm_steps: int = 32,
    n_sm_steps: int = 24,
) -> dict[str, Any]:
    _, mr_sv0 = takagi_real_2n_block(mr_uv_dimless)
    mr_cur = mr0_over_mgut * (mr_uv_dimless / mr_sv0[2])
    st_cur: tuple[Any, ...] = (g_uv, g_uv, g_uv, yu_uv, yd_uv, ye_uv, mp.zeros(3, 3), ynu_uv.copy(), mr_cur)
    t_now = mp.mpf(0)
    thresholds: list[mp.mpf] = []
    lepto_snap: dict[str, Any] = {}

    for n_act in (3, 2, 1):
        u_t, sv_t = takagi_real_2n_block(st_cur[8])
        m_heavy = sv_t[n_act - 1]
        t_target = mp.log(m_heavy)
        if t_target < t_now:
            st_cur = gl4_integrate_tuple(mssm_seesaw_rhs, st_cur, t_target - t_now, n_seg_steps, tol_exp=-24)
            t_now = t_target
        u_t, sv_t = takagi_real_2n_block(st_cur[8])
        m_heavy = sv_t[n_act - 1]
        thresholds.append(m_heavy)
        ynu_rot = st_cur[7] * u_t
        if n_act == 3:
            lepto_snap = {
                "ye_at_MR3": st_cur[5].copy(),
                "ynu_rot_at_MR3": ynu_rot.copy(),
                "M_R_eigs_over_MGUT": list(sv_t),
            }
        yk = mp.matrix([ynu_rot[r, n_act - 1] for r in range(3)])
        kap_new = st_cur[6] - (yk * yk.T) / m_heavy
        if n_act > 1:
            ynu_rem = mp.matrix([[ynu_rot[r, c] for c in range(n_act - 1)] for r in range(3)])
            mr_rem = mp.diag([sv_t[c] for c in range(n_act - 1)])
            st_cur = (st_cur[0], st_cur[1], st_cur[2], st_cur[3], st_cur[4], st_cur[5], kap_new, ynu_rem, mr_rem)
        else:
            st_below = (st_cur[0], st_cur[1], st_cur[2], st_cur[3], st_cur[4], st_cur[5], kap_new)

    mssm_rhs = make_mssm_2loop_rhs(two_loop=True)
    st_susy = gl4_integrate_tuple(mssm_rhs, st_below, t_gut_to_susy - t_now, n_mssm_steps, tol_exp=-24)
    ir_mz = match_and_run_sm_gl4(st_susy, soft, tan_beta, m0_over_v, sgn_mu=sgn_mu, n_sm_steps=n_sm_steps)
    return {
        "thresholds_MR_over_MGUT": thresholds,
        "lepto_snapshot": lepto_snap,
        "ir_mz": ir_mz,
    }


def independent_weisskopf_wigner_lnc_proof() -> dict[str, Any]:
    """
    Independent first-principles Weisskopf-Wigner H = M - (i/2) Gamma unitarity proof
    at 35 dps with cancellation-free discriminant (h00 - h11)^2 + 4 h01 h10 (< 1e-30 residual!).
    """
    old_dps = mp.mp.dps
    mp.mp.dps = 35
    try:
        eps_w = p10(-6)
        y_mat = eps_w * mp.matrix([
            [mp.mpc(1, 0), mp.mpc(3, 2)],
            [mp.mpc(2, -1), mp.mpc(-1, 4)],
        ])
        m1_w, m2_w = mp.mpf(1), mp.mpf(1) + p10(-4)
        gam_w = y_mat.H * y_mat + y_mat.T * y_mat.apply(mp.conj)
        h_eff = mp.diag([m1_w, m2_w]) - (I_UNIT / 2) * gam_w
        tr_h = h_eff[0, 0] + h_eff[1, 1]
        diff_h = h_eff[0, 0] - h_eff[1, 1]
        disc_h = mp.sqrt(diff_h * diff_h + 4 * h_eff[0, 1] * h_eff[1, 0])
        l_a, l_b = (tr_h + disc_h) / 2, (tr_h - disc_h) / 2
        lam1 = l_a if abs(l_a - m1_w) < abs(l_b - m1_w) else l_b
        v1 = mp.matrix([mp.mpc(1), -h_eff[1, 0] / (h_eff[1, 1] - lam1)])
        eig_resid = frob_mp(h_eff * v1 - lam1 * v1)
        amp_l = y_mat * v1
        amp_lb = y_mat.apply(mp.conj) * v1
        rl = [abs(amp_l[a]) ** 2 for a in range(2)]
        rlb = [abs(amp_lb[a]) ** 2 for a in range(2)]
        gtot = sum(rl, mp.mpf(0)) + sum(rlb, mp.mpf(0))
        asym_exact = [(rl[a] - rlb[a]) / gtot for a in range(2)]

        h_yuk = y_mat.H * y_mat
        h11 = mp.re(h_yuk[0, 0])
        dm = m2_w - m1_w
        same_sign_err = mp.mpf(0)
        wrong_sign_err = mp.mpf(0)
        for a in range(2):
            lnv_a = mp.im(mp.conj(y_mat[a, 0]) * y_mat[a, 1] * h_yuk[0, 1])
            lnc_a = mp.im(mp.conj(y_mat[a, 0]) * y_mat[a, 1] * h_yuk[1, 0])
            pred_same = -(lnv_a + lnc_a) / (h11 * dm)
            pred_opp = -(lnv_a - lnc_a) / (h11 * dm)
            same_sign_err = max(same_sign_err, abs(asym_exact[a] - pred_same) / abs(asym_exact[a]))
            wrong_sign_err = max(wrong_sign_err, abs(asym_exact[a] - pred_opp) / abs(asym_exact[a]))
        return {
            "working_dps": 35,
            "eigenvector_residual": fmt_mp(eig_resid, 10),
            "exact_same_sign_LNV_LNC_rel_err": fmt_mp(same_sign_err, 10),
            "wrong_opposite_LNC_sign_rel_err": fmt_mp(wrong_sign_err, 10),
            "passed": bool(eig_resid < p10(-30) and same_sign_err < p10(-10) and wrong_sign_err > mp.mpf(1)),
            "_wrong_sign_err_mp": wrong_sign_err,
        }
    finally:
        mp.mp.dps = old_dps


_BESSEL_GL4_GRID_CACHE: dict[int, tuple[mp.mpf, mp.mpf, list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]]] = {}


def _get_boltzmann_gl4_grid(
    n_st: int,
) -> tuple[mp.mpf, mp.mpf, list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]]]:
    """Precompute pure-z Bessel K_1, K_2 grid points for GL4 Boltzmann integration on [ln(1/10), ln(100)]."""
    if n_st in _BESSEL_GL4_GRID_CACHE:
        return _BESSEL_GL4_GRID_CACHE[n_st]
    s3 = mp.sqrt(3)
    c1_gl, c2_gl = (mp.mpf(3) - s3) / 6, (mp.mpf(3) + s3) / 6
    u0 = mp.log(q_mp(1, 10))
    u1 = mp.log(mp.mpf(100))
    h = (u1 - u0) / mp.mpf(n_st)

    def eval_z_funcs(u_val: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        zv = mp.exp(u_val)
        if zv > 60:
            pref = mp.sqrt(mp.pi / (2 * zv)) * mp.exp(-zv)
            k1v = pref * (1 + q_mp(3, 8) / zv - q_mp(15, 128) / (zv * zv))
            k2v = pref * (1 + q_mp(15, 8) / zv + q_mp(105, 128) / (zv * zv))
        else:
            k1v = mp.besselk(1, zv)
            k2v = mp.besselk(2, zv)
        neq = q_mp(1, 2) * zv * zv * k2v
        p_unit = zv * zv * (k1v / k2v)
        wb = q_mp(1, 4) * (zv ** 4) * k1v
        return neq, p_unit, wb

    neq0, _, _ = eval_z_funcs(u0)
    steps: list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for k in range(n_st):
        uk = u0 + k * h
        neq1, pu1, wb1 = eval_z_funcs(uk + c1_gl * h)
        neq2, pu2, wb2 = eval_z_funcs(uk + c2_gl * h)
        steps.append((neq1, pu1, wb1, neq2, pu2, wb2))
    val = (h, neq0, steps)
    _BESSEL_GL4_GRID_CACHE[n_st] = val
    return val


def solve_mssm_boltzmann_gl4(
    ye_m: mp.matrix,
    ynu_rot: mp.matrix,
    mr_eigs_over_mgut: list[mp.mpf],
    mgut_over_mpl_red: mp.mpf,
    n_coarse: int = 600,
    use_consistent_reduced_mpl: bool = True,
    compute_thermal: bool = True,
) -> dict[str, Any]:
    """
    Independent 2-stage implicit Gauss-Legendre GL4 stiff Boltzmann solver
    (disjoint from producer's Radau IIA!) with exact 2x2 linear stage solve and O(h^4) Richardson.
      - Always uses exact Weisskopf-Wigner LNC sign -2/(x_j - 1).
      - use_consistent_reduced_mpl=True (default): exact reduced-Planck Hubble
        H(M_1) = sqrt(pi^2 g_* / 90) M_1^2 / M_{P,red} (DISC-V7-1 remediated).
      - use_consistent_reduced_mpl=False: planted unreduced-Planck sqrt(8 pi) mismatch
        for PF_REF3_5 regression control only.
    """
    ul, _ = left_svd_asc(ye_m)
    yh = ul.H * ynu_rot
    h_mat = yh.H * yh
    h11 = mp.re(h_mat[0, 0])
    m1, m2, m3 = mr_eigs_over_mgut[0], mr_eigs_over_mgut[1], mr_eigs_over_mgut[2]
    x_list = [(m2 / m1) ** 2, (m3 / m1) ** 2]

    def f_mssm(x: mp.mpf) -> mp.mpf:
        return -mp.sqrt(x) * (mp.mpf(2) / (x - 1) + mp.log((1 + x) / x))

    eps_flav: list[mp.mpf] = []
    for alpha in range(3):
        acc = mp.mpf(0)
        for idx_j, j in enumerate((1, 2)):
            xj = x_list[idx_j]
            t1 = mp.im(mp.conj(yh[alpha, 0]) * yh[alpha, j] * h_mat[0, j]) * f_mssm(xj)
            t2 = mp.im(mp.conj(yh[alpha, 0]) * yh[alpha, j] * h_mat[j, 0]) * (mp.mpf(-2) / (xj - 1))
            acc += t1 + t2
        eps_flav.append(acc / (8 * mp.pi * h11))
    eps_tot = sum(eps_flav, mp.mpf(0))
    eps_unflav_direct = sum(
        (mp.im(h_mat[0, j] ** 2) * f_mssm(x_list[idx_j]) for idx_j, j in enumerate((1, 2))),
        mp.mpf(0),
    ) / (8 * mp.pi * h11)
    flav_sum_err = abs(eps_tot - eps_unflav_direct)

    g_star = q_mp(915, 4)
    if use_consistent_reduced_mpl:
        h_pref = mp.sqrt((mp.pi ** 2) * g_star / 90)
    else:
        h_pref = mp.sqrt(4 * (mp.pi ** 3) * g_star / 45)
    mpl_over_m1 = mp.mpf(1) / (mgut_over_mpl_red * m1)
    k_flav = [(abs(yh[alpha, 0]) ** 2) / (4 * mp.pi * h_pref) * mpl_over_m1 for alpha in range(3)]
    k_tot = sum(k_flav, mp.mpf(0))

    s3 = mp.sqrt(3)
    a11, a12 = q_mp(1, 4), (mp.mpf(3) - 2 * s3) / 12
    a21, a22 = (mp.mpf(3) + 2 * s3) / 12, q_mp(1, 4)

    def gl4_linear_step(
        y0: mp.mpf, h: mp.mpf, p1: mp.mpf, q1: mp.mpf, p2: mp.mpf, q2: mp.mpf
    ) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        m11, m12 = 1 + h * a11 * p1, h * a12 * p2
        m21, m22 = h * a21 * p1, 1 + h * a22 * p2
        r1 = y0 + h * (a11 * q1 + a12 * q2)
        r2 = y0 + h * (a21 * q1 + a22 * q2)
        det = m11 * m22 - m12 * m21
        y1 = (m22 * r1 - m12 * r2) / det
        y2 = (-m21 * r1 + m11 * r2) / det
        k1 = -p1 * y1 + q1
        k2 = -p2 * y2 + q2
        return y0 + (h / 2) * (k1 + k2), k1, k2

    def integrate_gl4(n_st: int, thermal_init: bool = False) -> tuple[list[mp.mpf], mp.mpf]:
        h, neq0, steps = _get_boltzmann_gl4_grid(n_st)
        y_n = neq0 if thermal_init else mp.mpf(0)
        y_fl = [mp.mpf(0)] * 3
        y_un = mp.mpf(0)
        for neq1, pu1, wb1, neq2, pu2, wb2 in steps:
            p1 = k_tot * pu1
            p2 = k_tot * pu2
            y_n, dn1, dn2 = gl4_linear_step(y_n, h, p1, p1 * neq1, p2, p2 * neq2)
            for a in range(3):
                y_fl[a], _, _ = gl4_linear_step(
                    y_fl[a], h, k_flav[a] * wb1, eps_flav[a] * dn1, k_flav[a] * wb2, eps_flav[a] * dn2
                )
            y_un, _, _ = gl4_linear_step(
                y_un, h, k_tot * wb1, eps_tot * dn1, k_tot * wb2, eps_tot * dn2
            )
        return y_fl, y_un

    fl_c, un_c = integrate_gl4(n_coarse, thermal_init=False)
    fl_f, un_f = integrate_gl4(2 * n_coarse, thermal_init=False)
    fl_rich = [(16 * fl_f[a] - fl_c[a]) / 15 for a in range(3)]
    un_rich = (16 * un_f - un_c) / 15

    conv_yb = q_mp(8, 23) * (135 * mp.zeta(3)) / (2 * (mp.pi ** 4) * g_star)
    yb_fl = conv_yb * sum(fl_rich, mp.mpf(0))
    yb_un = conv_yb * un_rich
    if compute_thermal:
        fl_th_c, _ = integrate_gl4(n_coarse, thermal_init=True)
        fl_th_f, _ = integrate_gl4(2 * n_coarse, thermal_init=True)
        fl_th_rich = [(16 * fl_th_f[a] - fl_th_c[a]) / 15 for a in range(3)]
        yb_th = conv_yb * sum(fl_th_rich, mp.mpf(0))
    else:
        yb_th = mp.mpf(0)
    step_rel_err = abs(sum(fl_f, mp.mpf(0)) - sum(fl_c, mp.mpf(0))) / max(abs(sum(fl_f, mp.mpf(0))), p10(-30))
    return {
        "eps_flav": eps_flav,
        "eps_tot": eps_tot,
        "flav_sum_err": flav_sum_err,
        "K_flav": k_flav,
        "K_tot": k_tot,
        "Y_B_flavored_zero_init": yb_fl,
        "Y_B_flavored_thermal_init": yb_th,
        "Y_B_unflavored": yb_un,
        "Y_B_gl4_step_halving_rel_err": step_rel_err,
    }


# ==============================================================================
# REF-4: Borromean Chain, Cross-Seat Seam Checks, Lock SHA, Custody, OW16 v18
# ==============================================================================

def verify_all_manifests_independent(repo_root: Path, tamper_idx: int | None = None) -> dict[str, Any]:
    relays_dir = repo_root / "relays"
    manifest_files = sorted(relays_dir.rglob("*SHA256*.txt"))
    total = 0
    verified = 0
    mismatches: list[dict[str, str]] = []
    idx = 0
    for mf in manifest_files:
        rel_mf = str(mf.relative_to(repo_root))
        if rel_mf == "relays/a2_ow26_referee_v3/OUTPUT_SHA256.txt":
            continue
        for raw_ln in mf.read_text(encoding="utf-8").splitlines():
            ln = raw_ln.strip()
            if not ln:
                continue
            parts = ln.split()
            if len(parts) < 2:
                continue
            exp_hex = parts[0]
            rel_tgt = parts[-1].lstrip("*")
            tgt = repo_root / rel_tgt
            if not tgt.exists():
                tgt = mf.parent / rel_tgt
            if not tgt.exists():
                total += 1
                mismatches.append({"manifest": rel_mf, "target": rel_tgt, "error": "missing_target"})
                idx += 1
                continue
            data = tgt.read_bytes()
            if tamper_idx is not None and idx == tamper_idx and len(data) > 0:
                data = bytes([data[0] ^ 1]) + data[1:]
            act_hex = hashlib.sha256(data).hexdigest()
            total += 1
            if act_hex == exp_hex:
                verified += 1
            else:
                mismatches.append({"manifest": rel_mf, "target": rel_tgt, "expected": exp_hex, "actual": act_hex})
            idx += 1
    return {
        "total_manifests": total,
        "verified_manifests": verified,
        "mismatches": mismatches,
        "all_verified": bool(total > 0 and verified == total and len(mismatches) == 0),
    }


def independent_historical_false_flag_scan(repo_root: Path) -> set[str]:
    relays_dir = repo_root / "relays"
    flagged: set[str] = set()
    for jp in sorted(relays_dir.rglob("*.json")):
        rel_p = str(jp.relative_to(repo_root))
        if rel_p in (
            "relays/a2_ow16_v18/a2_ow16_v18_results.json",
            "relays/a2_ow26_referee_v3/a2_ow26_referee_v3_results.json",
        ):
            continue
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        has_false = any(
            k in d and d[k] is False
            for k in ("all_gates_passed", "all_referee_gates_passed", "overall_pass", "pass", "all_passed")
        )
        if not has_false and isinstance(d.get("summary"), dict):
            has_false = any(
                k in d["summary"] and d["summary"][k] is False
                for k in ("all_gates_passed", "all_referee_gates_passed", "overall_pass", "pass", "all_passed")
            )
        if has_false:
            flagged.add(rel_p)
    return flagged


def run_ref4_borromean_cross_seat_custody_and_ow16(
    repo_root: Path,
    ow26_res: dict[str, Any],
    ow16_res: dict[str, Any],
    g_s12_t8: list[mp.mpf],
    k_s0_t8: list[mp.mpf],
    fcnc_s12_t8: dict[str, mp.mpf],
    fcnc_s0_t8: dict[str, mp.mpf],
    cim_kH1min_m0_3v_mh_pole: mp.mpf,
    seq_s12_pmns_s12sq: mp.mpf,
    seq_s0_pmns_s12sq: mp.mpf,
    lep_s12_K_tot: mp.mpf,
    lep_s12_YB_zero: mp.mpf,
    g_uv24: mp.mpf,
    t_susy24: mp.mpf,
    soft_ref: dict[str, mp.mpf],
) -> dict[str, Any]:
    mp.mp.dps = 45
    I_sp = sp.I

    # 1. Borromean 6^3_2 Quotient Chain (SymPy exact + Legendre lambda j-invariant + Phi2b/Phi0)
    a_b = sp.Matrix([[1, 2], [0, 1]])
    b_b = sp.Matrix([[1, 0], [I_sp, 1]])
    c_b = sp.Matrix([[2 - I_sp, 2], [I_sp, I_sp]])
    la_b = sp.expand(b_b.inv() * c_b * b_b * c_b.inv())
    tau_cusp = sp.simplify((la_b[0, 1] / la_b[0, 0]) / (a_b[0, 1] / a_b[0, 0]))
    q2 = sp.Matrix([[1, 0], [0, 2]])
    gam = sp.Matrix([[1, 0], [2, 1]])
    c8 = sp.Matrix([[8, 0], [0, 1]])
    m_comp = sp.expand(c8 * gam * q2)

    def mob(m_mat: sp.Matrix, z_v: Any) -> Any:
        return sp.simplify((m_mat[0, 0] * z_v + m_mat[0, 1]) / (m_mat[1, 0] * z_v + m_mat[1, 1]))

    tau_sq = mob(q2, tau_cusp)
    tau_0 = mob(gam, tau_sq)
    tau_8 = mob(c8, tau_0)
    tau_8_comp = mob(m_comp, tau_cusp)

    conj_m = lambda mat: mat.applyfunc(sp.conjugate)
    phi2b_ok = bool(
        sp.expand(conj_m(a_b) - a_b) == sp.zeros(2, 2)
        and sp.expand(conj_m(la_b) - la_b.inv()) == sp.zeros(2, 2)
    )
    m_phi0 = sp.Matrix([[1, 2 * I_sp], [0, -1]])
    phi0_ok = bool(
        sp.expand(m_phi0 * conj_m(la_b) * m_phi0.inv() - la_b) == sp.zeros(2, 2)
        and sp.expand(m_phi0 * conj_m(a_b) * m_phi0.inv() - a_b.inv()) == sp.zeros(2, 2)
    )

    tau0_mp = q_mp(2, 5) + I_UNIT * q_mp(1, 5)
    q0_mp = mp.exp(I_UNIT * mp.pi * tau0_mp)
    lam_leg = (mp.jtheta(2, 0, q0_mp) / mp.jtheta(3, 0, q0_mp)) ** 4
    j_tau0 = 256 * ((1 - lam_leg + lam_leg * lam_leg) ** 3) / ((lam_leg ** 2) * ((1 - lam_leg) ** 2))
    j_tau0_err = abs(j_tau0 - 1728)

    borr_ok = bool(
        tau_cusp == 2 * I_sp
        and tau_sq == I_sp
        and tau_0 == sp.Rational(2, 5) + sp.Rational(1, 5) * I_sp
        and tau_8 == sp.Rational(16, 5) + sp.Rational(8, 5) * I_sp
        and tau_8_comp == tau_8
        and int(m_comp.det()) == 16
        and m_comp == sp.Matrix([[8, 0], [2, 2]])
        and j_tau0_err < p10(-40)
        and phi2b_ok
        and phi0_ok
    )

    # 2. chat1 W-H1 Exact Mirror Theorem via independent heat-equation eval_sh_heat_eq
    tau8_p = q_mp(16, 5) + I_UNIT * q_mp(8, 5)
    tau8_m = -mp.conj(tau8_p)
    sh_p, cs_p = eval_sh_heat_eq(tau8_p)
    sh_m, cs_m = eval_sh_heat_eq(tau8_m)
    qi_m = mp.matrix([[I_UNIT, 0], [0, -I_UNIT]])
    qj_m = mp.matrix([[0, 1], [-1, 0]])
    qk_m = qi_m * qj_m
    sh_tilde = mp.conj(cs_p[0]) * qi_m + mp.conj(cs_p[1]) * qj_m + mp.conj(cs_p[2]) * qk_m
    chat1_mirror_err = frob_mp(sh_tilde - (-qk_m * sh_m * (qk_m ** (-1))))
    chat1_sigma_err = max(
        abs(mp.conj(cs_p[0]) - cs_m[0]),
        abs(mp.conj(cs_p[1]) - cs_m[1]),
        abs(mp.conj(cs_p[2]) + cs_m[2]),
    )

    # 3. physical 32514763f 4*eps^5 infinite-cusp relaxation vs B4_UV L-independent D-term bound
    eps_s = sp.Symbol("eps", positive=True)
    y_s = sp.Symbol("y", real=True)
    l_s = 1 / eps_s
    b_tr = (eps_s ** 2) * y_s * (1 - y_s / l_s) ** 2
    e_cusp = sp.simplify(sp.integrate(sp.diff(b_tr, y_s, 2) ** 2, (y_s, 0, l_s)))
    lam_d_ref = (mp.pi * (q_mp(1, 29) + q_mp(3, 5) * q_mp(1, 56))) * (q_mp(1 - 225, 1 + 225) ** 2)
    phys_ok = bool(e_cusp == 4 * (eps_s ** 5) and lam_d_ref > q_mp(1, 10))

    # 4. Faithful agy-exp abf9fdae0 8^3_4 side-by-side propagation via GL4
    mp.mp.dps = 28
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]

    def w_avg_tau(tau_v: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
        acc = mp.zeros(3, 3)
        for a_f, b_f in pts:
            acc += eval_w_hol_independent(tau_v, a_f, b_f, ql, qr)
        return acc / mp.mpf(len(pts))

    eps5 = mp.exp(2 * I_UNIT * mp.pi * tau8_p / 5)
    d10_834 = mp.diag([eps5 ** 2, mp.mpc(1), eps5 ** 3])
    wu0 = w_avg_tau(tau8_p, k5, 1, -4)
    wd0 = (w_avg_tau(tau8_p, k5, 1, 2) + w_avg_tau(tau8_p, k6, 1, 2)) / 2
    we0 = (w_avg_tau(tau8_p, k5, -3, 6) + w_avg_tau(tau8_p, k6, -3, 6)) / 2
    wnu_834 = (w_avg_tau(tau8_p, k5, 3, -5) + w_avg_tau(tau8_p, k6, 3, -5)) / 2
    wr_raw = (w_avg_tau(tau8_p, k5, 3, 3) + w_avg_tau(tau8_p, k6, 3, 3)) / 2
    wr_sym = (wr_raw + wr_raw.T) / 2
    _, sv_wr = left_svd_asc(wr_sym)
    mr_834 = mp.eye(3) + (wr_sym / sv_wr[2])
    kis_t8 = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_s12_t8])
    yu_8 = kis_t8 * (d10_834 * wu0 * d10_834) * kis_t8
    yd_8 = kis_t8 * (d10_834 * wd0) * kis_t8
    ye_8 = kis_t8 * (we0 * d10_834) * kis_t8
    yn_8 = kis_t8 * wnu_834
    _, su8 = left_svd_asc(yu_8)
    _, sd8 = left_svd_asc(yd_8)
    _, sn8 = left_svd_asc(yn_8)
    yu_8u = g_uv24 * (yu_8 / su8[2])
    yd_8u = (g_uv24 / 5) * (yd_8 / sd8[2])
    ye_8u = (g_uv24 / 5) * (ye_8 / sd8[2])
    yn_8u = g_uv24 * (yn_8 / sn8[2])
    kap_8u = -yn_8u * (mr_834 ** (-1)) * yn_8u.T
    _, sk8 = left_svd_asc((kap_8u + kap_8u.T) / 2)
    kap_8u = kap_8u / sk8[2]
    mssm_rhs = make_mssm_2loop_rhs(two_loop=True)
    st_8_susy = gl4_integrate_tuple(
        mssm_rhs, (g_uv24, g_uv24, g_uv24, yu_8u, yd_8u, ye_8u, kap_8u), t_susy24, 36, tol_exp=-24
    )
    mz_834 = match_and_run_sm_gl4(st_8_susy, soft_ref, 15, 10, sgn_mu=1, n_sm_steps=32)
    prod_834 = ow26_res["OW26_D_borromean_quotient_and_cross_seat_checks"]["agyexp_abf9fdae0_834_lopsided_side_by_side_in_B4UV_MZ"]
    diff_834_ckm = max(rel_diff_mp(mz_834["ckm_mz"][k], mp.mpf(prod_834["ckm_mz"][k])) for k in prod_834["ckm_mz"])
    diff_834_pmns = max(
        rel_diff_mp(mz_834["pmns_mz"][k], mp.mpf(prod_834["pmns_mz"][k]))
        for k in ("s12sq", "s23sq", "s13sq", "dm", "delta_cp_over_pi", "mee_over_m3")
    )

    # 5. Byte-exact recomputation of blind_prediction_lock_v2_sha256 from raw payload
    lock_payload = ow26_res["OW26_E_planted_faults_and_blind_lock_v2"]["blind_prediction_lock_v2_B4_UV"]
    lock_claimed = ow26_res["OW26_E_planted_faults_and_blind_lock_v2"]["blind_prediction_lock_v2_sha256"]
    lock_canonical = json.dumps(lock_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    lock_recomputed = hashlib.sha256(lock_canonical).hexdigest()
    lock_expected_v8 = "dab1f7e24f2057d54e63edd76feaab24ffc8997fc464c08e9ca31321d9639658"
    lock_match = bool(lock_recomputed == lock_claimed == lock_expected_v8)

    mutated_payload = dict(lock_payload)
    mutated_payload["firewall"] = "1 of 19"
    mutated_sha = hashlib.sha256(
        json.dumps(mutated_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    custody_ok_dict = verify_all_manifests_independent(repo_root, tamper_idx=None)
    custody_tamper = verify_all_manifests_independent(repo_root, tamper_idx=0)
    pf6_caught = bool(mutated_sha != lock_claimed and not custody_tamper["all_verified"])

    # 6. Git diff check on 27f5d89fa..HEAD (0 non-relay edits)
    git_proc = subprocess.run(
        ["git", "diff", "--name-only", "27f5d89fa..HEAD"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=True,
    )
    changed_files = [ln.strip() for ln in git_proc.stdout.splitlines() if ln.strip()]
    non_relay_edits = [f for f in changed_files if not f.startswith("relays/")]

    # 7. A2-OW16 v18 Audit (19/19 locks, 1/10/9/4 partition, 46 false-flag JSONs, OBS-09/15/17/18/22 consistency!)
    locks_v18 = ow16_res["cross_card_locks_v18"]
    ledger_v18 = ow16_res["blind_prediction_ledger_24_v18"]
    g5_v18 = ow16_res["guardrail5_input_ledger_v18"]
    obs_list = ledger_v18["observables"]
    bucket_counts: dict[str, int] = {}
    for row in obs_list:
        bucket_counts[row["bucket"]] = bucket_counts.get(row["bucket"], 0) + 1
    expected_partition = {
        "DERIVED_EXACT": 1,
        "CONDITIONAL_OR_QUALITATIVE": 10,
        "INTERNAL_WALL_OR_TENSION": 9,
        "OPEN_EXTERNAL_BOUNDARY": 4,
    }
    sole_derived = [row["id"] for row in obs_list if row["bucket"] == "DERIVED_EXACT"]
    obs_by_id = {row["id"]: row for row in obs_list}
    obs09_row = obs_by_id["OBS-09"]
    obs15_row = obs_by_id["OBS-15"]
    obs17_row = obs_by_id["OBS-17"]
    obs18_row = obs_by_id["OBS-18"]
    obs22_row = obs_by_id["OBS-22"]

    # OBS-09 consistency with v8 exact Higgs pole (DISC-V7-2!)
    prod_cim_kH1_3v = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["mz_cim_M16_yt_runs"]["CURV_s12_CIM_M16_kH1min_m0_3v"]["mh_pole_over_mz"]
    obs09_consistent = bool(
        prod_cim_kH1_3v in obs09_row["status_note"]
        and rel_diff_mp(cim_kH1min_m0_3v_mh_pole, mp.mpf(prod_cim_kH1_3v)) < p10(-5)
    )

    # OBS-15 consistency with v8 reduced-Planck Boltzmann (DISC-V7-1!)
    prod_c12_boltz = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s12_Dirac_CP_selected"]["boltzmann_leptogenesis"]
    obs15_consistent = bool(
        prod_c12_boltz["K_tot"] in obs15_row["status_note"]
        and prod_c12_boltz["Y_B_flavored_zero_init"] in obs15_row["status_note"]
        and rel_diff_mp(lep_s12_K_tot, mp.mpf(prod_c12_boltz["K_tot"])) < p10(-5)
        and rel_diff_mp(lep_s12_YB_zero, mp.mpf(prod_c12_boltz["Y_B_flavored_zero_init"])) < p10(-5)
    )

    # OBS-17 consistency on true tau_8^+ Gramian G_s12_t8 & K_s0_t8 (DISC-4!)
    uv_split_t8 = abs(g_s12_t8[0] - g_s12_t8[1]) / (g_s12_t8[0] + g_s12_t8[1])
    uv_split_s0_t8 = abs(k_s0_t8[0] - k_s0_t8[1]) / (k_s0_t8[0] + k_s0_t8[1])
    prod_fcnc = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["dirac_s12_vs_scalar_s0_fcnc_dilution"]
    prod_uv_s12 = mp.mpf(prod_fcnc["CURV_s12_Dirac_uv_12_split"])
    prod_ir_s12 = mp.mpf(prod_fcnc["CURV_s12_Dirac_ir_diluted_12_split"])
    prod_uv_s0 = mp.mpf(prod_fcnc["CURV_s0_Scalar_uv_12_split"])
    obs17_consistent = bool(
        "1.07020250193" in obs17_row["status_note"]
        and prod_fcnc["CURV_s12_Dirac_uv_12_split"] in obs17_row["status_note"]
        and prod_fcnc["CURV_s12_Dirac_ir_diluted_12_split"] in obs17_row["status_note"]
        and prod_fcnc["CURV_s0_Scalar_uv_12_split"] in obs17_row["status_note"]
        and rel_diff_mp(uv_split_t8, prod_uv_s12) < p10(-5)
        and rel_diff_mp(fcnc_s12_t8["ir_split"], prod_ir_s12) < p10(-5)
        and rel_diff_mp(uv_split_s0_t8, prod_uv_s0) < p10(-5)
        and rel_diff_mp(fcnc_s0_t8["uv_split"], prod_uv_s0) < p10(-5)
    )

    # OBS-18 consistency with v8 true tau_8^+ sequential seesaw PMNS
    prod_s12_pm = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s12_Dirac_CP_selected"]["pmns_mz_sequential"]
    prod_s0_pm = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s0_ScalarLegacy_CP_selected"]["pmns_mz_sequential"]
    obs18_consistent = bool(
        prod_s12_pm["s12sq"] in obs18_row["status_note"]
        and prod_s0_pm["s12sq"] in obs18_row["status_note"]
        and prod_s12_pm["mee_over_m3"] in obs18_row["status_note"]
        and rel_diff_mp(seq_s12_pmns_s12sq, mp.mpf(prod_s12_pm["s12sq"])) < p10(-5)
        and rel_diff_mp(seq_s0_pmns_s12sq, mp.mpf(prod_s0_pm["s12sq"])) < p10(-5)
    )

    # Historical false-flag JSON census against A2-OW16 v18 (expect exact set equality, 46 files!)
    indep_false_set = independent_historical_false_flag_scan(repo_root)
    ow16_false_set = {row["file"] for row in ow16_res["historical_false_json_disclosure"]["files"]}
    false_census_exact_match = bool(
        indep_false_set == ow16_false_set
        and len(indep_false_set) == ow16_res["historical_false_json_disclosure"]["total_historical_false_flag_jsons"]
        and len(indep_false_set) == 46
    )

    ow16_v18_ok = bool(
        ow16_res["all_gates_passed"] is True
        and locks_v18["locks_passed"] == 19
        and locks_v18["total_locks"] == 19
        and locks_v18["all_locks_passed"] is True
        and locks_v18["locks"].get("LOCK_19_ow26_v8_all_referee_v1_v2_remediated_mz_2loop_sm_boltzmann_lock_v2") is True
        and len(obs_list) == 24
        and len({r["id"] for r in obs_list}) == 24
        and bucket_counts == expected_partition
        and sole_derived == ["OBS-07"]
        and "-76/3" in obs22_row["value"]
        and "-151/6" not in obs22_row["value"]
        and lock_expected_v8 in obs22_row["status_note"]
        and g5_v18["dimensionful_anchor_count"] == 1
        and g5_v18["total_priced_continuous_ratios_baseline_4d"] == 15
        and g5_v18["conditional_parameter_reduction_branches"]["blind_prediction_lock_v2_mz_sha256"] == lock_expected_v8
        and ow16_res["planted_faults_v18"]["caught"] == 6
        and ow16_res["planted_faults_v18"]["total"] == 6
        and obs09_consistent
        and obs15_consistent
        and obs17_consistent
        and obs18_consistent
        and false_census_exact_match
    )

    caveat_v2_wording_note = (
        "awaiting Cold-Room Referee v2" in g5_v18["conditional_parameter_reduction_branches"]["honest_caveat"]
    )

    return {
        "borromean_quotient_chain": {
            "passed": borr_ok,
            "tau_cusp": str(tau_cusp),
            "tau_sq": str(tau_sq),
            "tau_0": str(tau_0),
            "tau_8": str(tau_8),
            "composite_det": int(m_comp.det()),
            "Phi2b_ok": phi2b_ok,
            "Phi0_ok": phi0_ok,
            "j_tau0_err_via_legendre_lambda": fmt_mp(j_tau0_err, 10),
        },
        "chat1_mirror_theorem": {
            "mirror_S_tilde_err_45dps": fmt_mp(chat1_mirror_err, 10),
            "sigma_err_45dps": fmt_mp(chat1_sigma_err, 10),
            "passed": bool(chat1_mirror_err < p10(-40) and chat1_sigma_err < p10(-40)),
        },
        "physical_32514763f_vs_B4UV_Dterm": {
            "cusp_energy_scaling": str(e_cusp),
            "B4UV_Dterm_bound_tb15": fmt_mp(lam_d_ref, 10),
            "passed": phys_ok,
        },
        "agyexp_834_faithful_side_by_side_GL4": {
            "max_rel_diff_ckm_vs_producer": fmt_mp(diff_834_ckm, 10),
            "max_rel_diff_pmns_vs_producer": fmt_mp(diff_834_pmns, 10),
            "gl4_pmns_s12_s23_s13_dm": [
                fmt_mp(mz_834["pmns_mz"]["s12sq"], 10),
                fmt_mp(mz_834["pmns_mz"]["s23sq"], 10),
                fmt_mp(mz_834["pmns_mz"]["s13sq"], 10),
                fmt_mp(mz_834["pmns_mz"]["dm"], 10),
            ],
            "strict_CKM_ordered": bool(
                mz_834["ckm_mz"]["v12"] > mz_834["ckm_mz"]["v23"] > mz_834["ckm_mz"]["v13"] > 0
            ),
            "passed": bool(diff_834_ckm < p10(-5) and diff_834_pmns < p10(-5)),
        },
        "blind_prediction_lock_v2_sha256": {
            "recomputed": lock_recomputed,
            "claimed": lock_claimed,
            "exact_match": lock_match,
        },
        "git_diff_27f5d89fa_to_HEAD": {
            "total_changed_files": len(changed_files),
            "non_relay_edits_count": len(non_relay_edits),
            "non_relay_edits": non_relay_edits,
            "passed": bool(len(non_relay_edits) == 0),
        },
        "branch_custody_manifests": custody_ok_dict,
        "a2_ow16_v18_audit": {
            "all_structural_and_internal_checks_ok": ow16_v18_ok,
            "obs09_exact_higgs_pole_consistent": obs09_consistent,
            "obs15_reduced_planck_boltzmann_consistent": obs15_consistent,
            "obs17_true_tau8_G_s12_vs_FCNC_consistent": obs17_consistent,
            "obs18_true_tau8_dirac_pmns_consistent": obs18_consistent,
            "historical_false_flag_count_independent": len(indep_false_set),
            "historical_false_flag_exact_set_match_46": false_census_exact_match,
            "uv_12_split_true_tau8_G_s12_t8": fmt_mp(uv_split_t8, 12),
            "ir_12_split_true_tau8_G_s12_t8": fmt_mp(fcnc_s12_t8["ir_split"], 12),
            "uv_12_split_true_tau8_K_s0_t8": fmt_mp(uv_split_s0_t8, 12),
            "minor_prose_note_honest_caveat_says_referee_v2": caveat_v2_wording_note,
        },
        "_pf6_caught": pf6_caught,
    }


# ==============================================================================
# Main Cold-Room Referee v3 Driver
# ==============================================================================

def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    ow26_script = repo_root / "relays" / "a2_ow26_v8" / "verify_a2_ow26_v8.py"
    ow16_script = repo_root / "relays" / "a2_ow16_v18" / "verify_a2_ow16_v18.py"
    ow26_json_path = repo_root / "relays" / "a2_ow26_v8" / "a2_ow26_v8_results.json"
    ow16_json_path = repo_root / "relays" / "a2_ow16_v18" / "a2_ow16_v18_results.json"

    ast_self = ast_audit_script(script_path)
    ast_ow26 = ast_audit_script(ow26_script)
    ast_ow16 = ast_audit_script(ow16_script)
    assert ast_self["clean"], f"Referee v3 self-hygiene violation: {ast_self}"

    ow26_raw_text = ow26_json_path.read_text(encoding="utf-8")
    ow16_raw_text = ow16_json_path.read_text(encoding="utf-8")
    json_scan_ow26 = scan_raw_json_float_tokens(ow26_raw_text)
    json_scan_ow16 = scan_raw_json_float_tokens(ow16_raw_text)
    ow26_res = json.loads(ow26_raw_text)
    ow16_res = json.loads(ow16_raw_text)

    # --- REF-2: E_8 240-root, M=8 CIM 7x7x9x9 GL2D, B3 SUGRA, GL10/GL6 Dirac s=1/2 Liouville ---
    ref2 = run_ref2_e8_cim_and_dirac_liouville(ow26_res)
    r2_int = ref2.pop("_internal")
    g_s12_t8 = r2_int["G_s12_t8"]
    k_s0_t8 = r2_int["K_s0_t8"]

    # --- REF-1: First-Principles SM/DR->MS Audits + GL4 Full Pipeline (17 runs) + Matched Haar ---
    mp.mp.dps = 28
    sm_audits = first_principles_sm_rge_and_dr_ms_audits(ow26_res)

    tau8_p = q_mp(16, 5) + I_UNIT * q_mp(8, 5)
    tau8_m = -mp.conj(tau8_p)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    k5_cp = [(a, (-b) % 1) for a, b in k5]
    k6_cp = [(a, (-b) % 1) for a, b in k6]

    def build_uv_textures(tau_v: mp.mpc, metric_diag: list[mp.mpf], cp_orbits: bool = False) -> dict[str, mp.matrix]:
        k5_u = k5_cp if cp_orbits else k5
        k6_u = k6_cp if cp_orbits else k6

        def w_avg(pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
            acc = mp.zeros(3, 3)
            for a_f, b_f in pts:
                acc += eval_w_hol_independent(tau_v, a_f, b_f, ql, qr)
            return acc / mp.mpf(len(pts))

        eps5 = mp.exp(2 * I_UNIT * mp.pi * tau_v / 5)
        d10 = mp.diag([eps5 ** 3, eps5 ** 2, mp.mpc(1)])
        kis = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in metric_diag])
        wu = kis * (d10 * w_avg(k5_u, 1, -4) * d10) * kis
        wd = kis * (d10 * (w_avg(k5_u, 1, 2) + w_avg(k6_u, 1, 2)) / 2) * kis
        we = kis * (((w_avg(k5_u, -3, 6) + w_avg(k6_u, -3, 6)) / 2) * d10) * kis
        wn2 = kis * ((w_avg(k5_u, -3, 2) - w_avg(k6_u, -3, 2)) / 2) * kis
        wr2_raw = (w_avg(k5_u, 2, 2) - w_avg(k6_u, 2, 2)) / 2
        mr2 = kis * ((wr2_raw + wr2_raw.T) / 2) * kis
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
        }

    flat_diag = [mp.mpf(1), mp.mpf(1), mp.mpf(1)]
    tex_flat_p = build_uv_textures(tau8_p, flat_diag, cp_orbits=False)
    tex_s12_t8_p = build_uv_textures(tau8_p, g_s12_t8, cp_orbits=False)
    tex_s12_t8_m = build_uv_textures(tau8_m, g_s12_t8, cp_orbits=True)
    tex_s12_bad_m = build_uv_textures(tau8_m, g_s12_t8, cp_orbits=False)
    tex_s0_t8_p = build_uv_textures(tau8_p, k_s0_t8, cp_orbits=False)

    g_uv24 = mp.sqrt(4 * mp.pi / mp.mpf(24))
    t_susy24 = -(q_mp(2, 5) * mp.pi * mp.mpf(24))
    yb0_ref = g_uv24 / 5
    ytau0_ref = (g_uv24 / 5) * left_svd_asc(tex_flat_p["ye_hat"])[1][2]
    soft_ref_guv = integrate_soft_susy_gl4(g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 48, -mp.sqrt(3))

    def eval_fcnc_gl4(diag_k: list[mp.mpf]) -> dict[str, mp.mpf]:
        ik0, ik1 = mp.mpf(1) / diag_k[0], mp.mpf(1) / diag_k[1]
        mean_ik = (ik0 + ik1) / 2
        mq1_uv, mq2_uv = ik0 / mean_ik, ik1 / mean_ik
        uv_sp = abs(mq2_uv - mq1_uv) / (mq2_uv + mq1_uv)
        sft = integrate_soft_susy_gl4(
            g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 48, mp.mpf(0), mq1_sq0=mq1_uv, mq2_sq0=mq2_uv
        )
        ir_sp = abs(sft["mQ2"] - sft["mQ1"]) / (sft["mQ2"] + sft["mQ1"])
        return {"uv_split": uv_sp, "ir_split": ir_sp, "dilution": uv_sp / ir_sp}

    fcnc_s12_t8 = eval_fcnc_gl4(g_s12_t8)
    fcnc_s0_t8 = eval_fcnc_gl4(k_s0_t8)
    prod_fcnc = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["dirac_s12_vs_scalar_s0_fcnc_dilution"]
    fcnc_t8_vs_prod_err = max(
        rel_diff_mp(fcnc_s12_t8["uv_split"], mp.mpf(prod_fcnc["CURV_s12_Dirac_uv_12_split"])),
        rel_diff_mp(fcnc_s12_t8["ir_split"], mp.mpf(prod_fcnc["CURV_s12_Dirac_ir_diluted_12_split"])),
        rel_diff_mp(fcnc_s0_t8["uv_split"], mp.mpf(prod_fcnc["CURV_s0_Scalar_uv_12_split"])),
        rel_diff_mp(fcnc_s0_t8["ir_split"], mp.mpf(prod_fcnc["CURV_s0_Scalar_ir_diluted_12_split"])),
    )

    # Disjoint GL4 Reproduction of ALL 10 standard + 4 CIM_M16 + 3 SUGRA = 17 OW26-A Runs
    mssm_rhs = make_mssm_2loop_rhs(two_loop=True)
    st_s12_t8 = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            g_uv24 * tex_s12_t8_p["yu_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["yd_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["ye_hat"],
            tex_s12_t8_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )
    st_flat = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            g_uv24 * tex_flat_p["yu_hat"],
            (g_uv24 / 5) * tex_flat_p["yd_hat"],
            (g_uv24 / 5) * tex_flat_p["ye_hat"],
            tex_flat_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )
    st_s0_t8 = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            g_uv24 * tex_s0_t8_p["yu_hat"],
            (g_uv24 / 5) * tex_s0_t8_p["yd_hat"],
            (g_uv24 / 5) * tex_s0_t8_p["ye_hat"],
            tex_s0_t8_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )

    prod_runs = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["mz_2loop_pipeline_runs"]
    layer1_run_diffs: dict[str, str] = {}
    max_layer1_run_diff = mp.mpf(0)
    run_specs = [
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_3v_sgnMu_pos", st_s12_t8, 3, 1),
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_3v_sgnMu_neg", st_s12_t8, 3, -1),
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos", st_s12_t8, 10, 1),
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_neg", st_s12_t8, 10, -1),
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_30v_sgnMu_pos", st_s12_t8, 30, 1),
        ("CURV_s12_Dirac_yt_gUV_tb15_m0_30v_sgnMu_neg", st_s12_t8, 30, -1),
        ("FLAT_yt_gUV_tb15_m0_10v_sgnMu_pos", st_flat, 10, 1),
        ("FLAT_yt_gUV_tb15_m0_10v_sgnMu_neg", st_flat, 10, -1),
        ("CURV_s0_ScalarLegacy_yt_gUV_tb15_m0_10v_sgnMu_pos", st_s0_t8, 10, 1),
        ("CURV_s0_ScalarLegacy_yt_gUV_tb15_m0_10v_sgnMu_neg", st_s0_t8, 10, -1),
    ]
    scalar_cmp_keys = [
        "q_match_over_mz", "delta_b", "alpha1_inv_mz", "alpha2_inv_mz", "alpha3_mz",
        "sin2_thetaW_mz", "alpha_EM_inv_mz", "mw_over_mz", "mt_ms_over_v",
        "mt_pole_over_v", "mh_ms_over_mz", "mh_pole_over_mz", "mh_pole_over_v",
    ]
    gl4_saved_runs: dict[str, dict[str, Any]] = {}
    perturbative_floor_hits = 0
    for tag, st_u, m0v, sgn_m in run_specs:
        res_l1 = match_and_run_sm_gl4(st_u, soft_ref_guv, 15, m0v, sgn_mu=sgn_m, n_sm_steps=28)
        gl4_saved_runs[tag] = res_l1
        if res_l1["higgs_pole_hit_floor"]:
            perturbative_floor_hits += 1
        pr = prod_runs[tag]
        d_sc = max(rel_diff_mp(res_l1[k], mp.mpf(pr[k])) for k in scalar_cmp_keys)
        d_ck = max(rel_diff_mp(res_l1["ckm_mz"][k], mp.mpf(pr["ckm_mz"][k])) for k in pr["ckm_mz"])
        d_pm = max(rel_diff_mp(res_l1["pmns_mz"][k], mp.mpf(pr["pmns_mz"][k])) for k in pr["pmns_mz"])
        d_tot = max(d_sc, d_ck, d_pm)
        layer1_run_diffs[tag] = fmt_mp(d_tot, 10)
        max_layer1_run_diff = max(max_layer1_run_diff, d_tot)

    # CIM_M16 GL4 comparison
    yt0_cim_max = g_uv24 * r2_int["yt_cim_max"]
    yt0_cim_min = g_uv24 * r2_int["yt_cim_min"]
    soft_cim_max = integrate_soft_susy_gl4(g_uv24, yt0_cim_max, yb0_ref, ytau0_ref, t_susy24, 48, -mp.sqrt(3))
    soft_cim_min = integrate_soft_susy_gl4(g_uv24, yt0_cim_min, yb0_ref, ytau0_ref, t_susy24, 48, -mp.sqrt(3))
    st_cim_max = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            yt0_cim_max * tex_s12_t8_p["yu_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["yd_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["ye_hat"],
            tex_s12_t8_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )
    st_cim_min = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            yt0_cim_min * tex_s12_t8_p["yu_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["yd_hat"],
            (g_uv24 / 5) * tex_s12_t8_p["ye_hat"],
            tex_s12_t8_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )
    prod_cim_runs = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["mz_cim_M16_yt_runs"]
    cim_run_diffs: dict[str, str] = {}
    gl4_cim_runs: dict[str, dict[str, Any]] = {}
    for ctag, st_u, sf_u in (("CIM_M16_kH2max", st_cim_max, soft_cim_max), ("CIM_M16_kH1min", st_cim_min, soft_cim_min)):
        for m0v in (3, 10):
            key_c = f"CURV_s12_{ctag}_m0_{m0v}v"
            rc = match_and_run_sm_gl4(st_u, sf_u, 15, m0v, sgn_mu=1, n_sm_steps=28)
            gl4_cim_runs[key_c] = rc
            if rc["higgs_pole_hit_floor"]:
                perturbative_floor_hits += 1
            pc = prod_cim_runs[key_c]
            dc = max(
                rel_diff_mp(rc["ckm_mz"]["yt"], mp.mpf(pc["yt_MZ"])),
                rel_diff_mp(rc["mt_pole_over_v"], mp.mpf(pc["mt_pole_over_v"])),
                rel_diff_mp(rc["mh_pole_over_mz"], mp.mpf(pc["mh_pole_over_mz"])),
                rel_diff_mp(rc["mh_pole_over_v"], mp.mpf(pc["mh_pole_over_v"])),
                rel_diff_mp(rc["alpha3_mz"], mp.mpf(pc["alpha3_mz"])),
                rel_diff_mp(rc["sin2_thetaW_mz"], mp.mpf(pc["sin2_thetaW_mz"])),
                rel_diff_mp(rc["ckm_mz"]["b_tau"], mp.mpf(pc["b_tau_mz"])),
            )
            cim_run_diffs[key_c] = fmt_mp(dc, 10)
            max_layer1_run_diff = max(max_layer1_run_diff, dc)

    # SUGRA GL4 comparison with fine 64/96 GL4 steps on steep aUVinv=23 Landau tail
    # PLUS independent non-perturbative mu=M_Z vs mu=m_t floor-clamp audit!
    mkk_over_mpl_red = mp.mpf(
        ow26_res["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B3_sugra_m32_planck_factor"][0]["M_KK_over_M_Pl_OW23C"]
    )
    prod_sugra_runs = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["mz_sugra_planck_factor_runs"]
    sugra_run_diffs: dict[str, str] = {}
    sugra_floor_audit: dict[str, Any] = {}
    for a_inv in (23, 24, 25):
        g_u = mp.sqrt(4 * mp.pi / mp.mpf(a_inv))
        lam_h = mp.exp(-q_mp(2, 15) * mp.pi * mp.mpf(a_inv))
        t_sug = mp.log((lam_h ** 3) * (mkk_over_mpl_red ** 2) / mp.sqrt(3))
        n_m_sg = 64 if a_inv == 23 else 48
        n_s_sg = 96 if a_inv == 23 else 64
        st_sg = gl4_integrate_tuple(
            mssm_rhs,
            (
                g_u, g_u, g_u,
                g_u * tex_s12_t8_p["yu_hat"],
                (g_u / 5) * tex_s12_t8_p["yd_hat"],
                (g_u / 5) * tex_s12_t8_p["ye_hat"],
                tex_s12_t8_p["kap_hat"],
            ),
            t_sug, n_m_sg, tol_exp=-24,
        )
        sf_sg = integrate_soft_susy_gl4(
            g_u, g_u, g_u / 5, (g_u / 5) * left_svd_asc(tex_flat_p["ye_hat"])[1][2], t_sug, 64, -mp.sqrt(3)
        )
        rsg = match_and_run_sm_gl4(st_sg, sf_sg, 15, 10, sgn_mu=1, n_sm_steps=n_s_sg)
        tag_sg = f"aUVinv{a_inv}_SUGRA_MKK_m0_10v"
        psg = prod_sugra_runs[tag_sg]
        dsg = max(
            rel_diff_mp(rsg["alpha3_mz"], mp.mpf(psg["alpha3_mz"])),
            rel_diff_mp(rsg["sin2_thetaW_mz"], mp.mpf(psg["sin2_thetaW_mz"])),
            rel_diff_mp(rsg["alpha_EM_inv_mz"], mp.mpf(psg["alpha_EM_inv_mz"])),
            rel_diff_mp(rsg["ckm_mz"]["b_tau"], mp.mpf(psg["b_tau_mz"])),
            rel_diff_mp(rsg["mh_pole_over_mz"], mp.mpf(psg["mh_pole_over_mz"])),
            rel_diff_mp(rsg["mt_pole_over_v"], mp.mpf(psg["mt_pole_over_v"])),
        )
        sugra_run_diffs[tag_sg] = fmt_mp(dsg, 10)
        max_layer1_run_diff = max(max_layer1_run_diff, dsg)

        # Evaluate at mu = m_t(MSbar) for non-perturbative diagnostic comparison
        sf_mt_sg = rsg["mt_ms_over_v"] / rsg["mz_over_v"]
        rsg_mt = match_and_run_sm_gl4(
            st_sg, sf_sg, 15, 10, sgn_mu=1, n_sm_steps=n_s_sg, scale_factor_over_mz=sf_mt_sg
        )
        sugra_floor_audit[tag_sg] = {
            "alpha3_mz": fmt_mp(rsg["alpha3_mz"], 8),
            "yt_mz": fmt_mp(rsg["ckm_mz"]["yt"], 8),
            "lam_mz": fmt_mp(rsg["lam_q"], 8),
            "delta_top_at_mu_MZ": fmt_mp(rsg["delta_top"], 8),
            "hit_1e_neg10_floor_at_mu_MZ": rsg["higgs_pole_hit_floor"],
            "mh_pole_over_mz_at_mu_MZ_clamped": fmt_mp(rsg["mh_pole_over_mz"], 10),
            "alpha3_at_mu_mt": fmt_mp(rsg_mt["alpha3_mz"], 8),
            "delta_top_at_mu_mt": fmt_mp(rsg_mt["delta_top"], 8),
            "mh_pole_over_mz_at_mu_mt_perturbative": fmt_mp(rsg_mt["mh_pole_over_v"] / rsg["mz_over_v"], 10),
        }

    # Independent mu = M_Z vs mu = m_t Higgs pole scale-invariance check (DISC-V7-2 verification!)
    c10_mz = gl4_saved_runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    sf_mt_10 = c10_mz["mt_pole_over_v"] / c10_mz["mz_over_v"]
    c10_mt = match_and_run_sm_gl4(
        st_s12_t8, soft_ref_guv, 15, 10, sgn_mu=1, n_sm_steps=28, scale_factor_over_mz=sf_mt_10
    )
    mh_ex_at_mz = c10_mz["mh_pole_over_v"]
    mh_ex_at_mt = c10_mt["mh_pole_over_v"]
    exact_mh_scale_drift = rel_diff_mp(mh_ex_at_mz, mh_ex_at_mt)
    trunc_mh_scale_drift_pf1 = rel_diff_mp(c10_mz["mh_pole_trunc_over_v"], c10_mt["mh_pole_trunc_over_v"])

    prod_g4 = ow26_res["OW26_A_2loop_sm_mz_thresholds_and_poles"]["guardrail4_2loop_sm_benchmarks"]
    higgs_scale_vs_v8_diff = max(
        rel_diff_mp(mh_ex_at_mz, mp.mpf(prod_g4["higgs_pole_mh_over_v_at_mu_MZ"])),
        rel_diff_mp(mh_ex_at_mt, mp.mpf(prod_g4["higgs_pole_mh_over_v_at_mu_mt"])),
        rel_diff_mp(exact_mh_scale_drift, mp.mpf(prod_g4["higgs_pole_mu_MZ_vs_mt_rel_diff"])),
    )

    # Guardrail-3 10-trial Haar U(3)^5 end-to-end scrambling with MATCHED GL4 step count (32 MSSM, 28 SM)
    rng_h1 = Xorshift64Star(202611240301)
    mz_ref_h1 = gl4_saved_runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    haar_u35_max_err = mp.mpf(0)
    for _ in range(10):
        uq = haar_unitary_householder(rng_h1)
        uur = haar_unitary_householder(rng_h1)
        udr = haar_unitary_householder(rng_h1)
        ul = haar_unitary_householder(rng_h1)
        uer = haar_unitary_householder(rng_h1)
        st_sc = gl4_integrate_tuple(
            mssm_rhs,
            (
                g_uv24, g_uv24, g_uv24,
                uq * (g_uv24 * tex_s12_t8_p["yu_hat"]) * uur.H,
                uq * ((g_uv24 / 5) * tex_s12_t8_p["yd_hat"]) * udr.H,
                ul * ((g_uv24 / 5) * tex_s12_t8_p["ye_hat"]) * uer.H,
                ul * tex_s12_t8_p["kap_hat"] * ul.T,
            ),
            t_susy24, 32, tol_exp=-24,
        )
        mz_sc = match_and_run_sm_gl4(st_sc, soft_ref_guv, 15, 10, sgn_mu=1, n_sm_steps=28)
        e_c = max(abs(mz_sc["ckm_mz"][k] - mz_ref_h1["ckm_mz"][k]) for k in mz_ref_h1["ckm_mz"])
        e_p = max(abs(mz_sc["pmns_mz"][k] - mz_ref_h1["pmns_mz"][k]) for k in mz_ref_h1["pmns_mz"])
        e_g = max(
            abs(mz_sc["mh_pole_over_mz"] - mz_ref_h1["mh_pole_over_mz"]),
            abs(mz_sc["alpha3_mz"] - mz_ref_h1["alpha3_mz"]),
        )
        haar_u35_max_err = max(haar_u35_max_err, e_c, e_p, e_g)

    # Planted Fault PF-2: Broken Haar (U_Q_u != U_Q_d) must fail invariance
    uq_bad1 = haar_unitary_householder(rng_h1)
    uq_bad2 = haar_unitary_householder(rng_h1)
    st_bad_h = gl4_integrate_tuple(
        mssm_rhs,
        (
            g_uv24, g_uv24, g_uv24,
            uq_bad1 * (g_uv24 * tex_s12_t8_p["yu_hat"]),
            uq_bad2 * ((g_uv24 / 5) * tex_s12_t8_p["yd_hat"]),
            (g_uv24 / 5) * tex_s12_t8_p["ye_hat"],
            tex_s12_t8_p["kap_hat"],
        ),
        t_susy24, 32, tol_exp=-24,
    )
    mz_bad_h = match_and_run_sm_gl4(st_bad_h, soft_ref_guv, 15, 10, sgn_mu=1, n_sm_steps=28)
    pf2_broken_haar_drift = max(abs(mz_bad_h["ckm_mz"][k] - mz_ref_h1["ckm_mz"][k]) for k in ("v12", "v23", "v13"))

    # Planted Fault PF-1: Corrupt 2-loop SM O(4) sign, MV III trd sign, AND truncated Higgs pole
    i3_0 = mp.zeros(3, 3)
    yd_test = mp.diag([mp.mpc(0), mp.mpc(0), mp.mpc(1)])
    st_pf1 = (q_mp(1, 2), q_mp(3, 5), mp.mpf(0), i3_0, yd_test, i3_0, i3_0, q_mp(1, 4))
    dlam_clean = make_sm_2loop_rhs(two_loop=True, corrupt_o4_sign=False, corrupt_mv3_trd=False)(st_pf1)[7]
    dlam_bad_o4 = make_sm_2loop_rhs(two_loop=True, corrupt_o4_sign=True, corrupt_mv3_trd=False)(st_pf1)[7]
    dlam_bad_mv3 = make_sm_2loop_rhs(two_loop=True, corrupt_o4_sign=False, corrupt_mv3_trd=True)(st_pf1)[7]
    pf1_o4_diff = abs(dlam_clean - dlam_bad_o4)
    pf1_mv3_diff = abs(dlam_clean - dlam_bad_mv3)

    # --- REF-3: Sequential Seesaw GL4 + Real 6x6 Takagi + 35-dps WW Proof + Stiff GL4 Boltzmann ---
    ww_proof = independent_weisskopf_wigner_lnc_proof()
    ww_wrong_err_mp = ww_proof.pop("_wrong_sign_err_mp")

    mr0_c = p10(-3)
    seq_s12_p = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_t8_p["yu_hat"], (g_uv24 / 5) * tex_s12_t8_p["yd_hat"], (g_uv24 / 5) * tex_s12_t8_p["ye_hat"],
        g_uv24 * tex_s12_t8_p["yn_hat"], tex_s12_t8_p["mr_raw"], mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
    )
    seq_s12_m = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_t8_m["yu_hat"], (g_uv24 / 5) * tex_s12_t8_m["yd_hat"], (g_uv24 / 5) * tex_s12_t8_m["ye_hat"],
        g_uv24 * tex_s12_t8_m["yn_hat"], tex_s12_t8_m["mr_raw"], mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
    )
    seq_s12_bad_m = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s12_bad_m["yu_hat"], (g_uv24 / 5) * tex_s12_bad_m["yd_hat"], (g_uv24 / 5) * tex_s12_bad_m["ye_hat"],
        g_uv24 * tex_s12_bad_m["yn_hat"], tex_s12_bad_m["mr_raw"], mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
    )
    seq_s0_p = run_seq_seesaw_gl4(
        g_uv24, g_uv24 * tex_s0_t8_p["yu_hat"], (g_uv24 / 5) * tex_s0_t8_p["yd_hat"], (g_uv24 / 5) * tex_s0_t8_p["ye_hat"],
        g_uv24 * tex_s0_t8_p["yn_hat"], tex_s0_t8_p["mr_raw"], mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
    )
    seq_sup_m = run_seq_seesaw_gl4(
        g_uv24,
        (g_uv24 * tex_s12_t8_m["yu_hat"]).apply(mp.conj),
        ((g_uv24 / 5) * tex_s12_t8_m["yd_hat"]).apply(mp.conj),
        ((g_uv24 / 5) * tex_s12_t8_m["ye_hat"]).apply(mp.conj),
        (g_uv24 * tex_s12_t8_m["yn_hat"]).apply(mp.conj),
        tex_s12_t8_m["mr_raw"].apply(mp.conj),
        mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
    )

    # Consistent reduced-Planck Stiff GL4 Boltzmann (N=600 vs 1200 + Richardson, DISC-V7-1 verified!)
    lep_p = solve_mssm_boltzmann_gl4(
        seq_s12_p["lepto_snapshot"]["ye_at_MR3"],
        seq_s12_p["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_s12_p["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=True,
    )
    lep_m = solve_mssm_boltzmann_gl4(
        seq_s12_m["lepto_snapshot"]["ye_at_MR3"],
        seq_s12_m["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_s12_m["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=False,
    )
    lep_s0_p = solve_mssm_boltzmann_gl4(
        seq_s0_p["lepto_snapshot"]["ye_at_MR3"],
        seq_s0_p["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_s0_p["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=False,
    )
    lep_sup_m = solve_mssm_boltzmann_gl4(
        seq_sup_m["lepto_snapshot"]["ye_at_MR3"],
        seq_sup_m["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_sup_m["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=False,
    )
    # Planted Fault PF-5 controls: broken CP mirror AND unreduced-Planck Hubble mismatch!
    lep_bad_m = solve_mssm_boltzmann_gl4(
        seq_s12_bad_m["lepto_snapshot"]["ye_at_MR3"],
        seq_s12_bad_m["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_s12_bad_m["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=False,
    )
    lep_unred_pf5 = solve_mssm_boltzmann_gl4(
        seq_s12_p["lepto_snapshot"]["ye_at_MR3"],
        seq_s12_p["lepto_snapshot"]["ynu_rot_at_MR3"],
        seq_s12_p["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=False, compute_thermal=False,
    )

    dirac_vs_sup_cp_inv_err = max(
        abs(lep_sup_m["Y_B_flavored_zero_init"] - lep_p["Y_B_flavored_zero_init"]),
        abs(seq_sup_m["ir_mz"]["ckm_mz"]["J"] - seq_s12_p["ir_mz"]["ckm_mz"]["J"]),
        abs(seq_sup_m["ir_mz"]["pmns_mz"]["delta_cp_rad"] - seq_s12_p["ir_mz"]["pmns_mz"]["delta_cp_rad"]),
    )
    cp_odd_err = abs(lep_p["Y_B_flavored_zero_init"] + lep_m["Y_B_flavored_zero_init"])
    pf5_bad_mirror_sum = abs(lep_p["Y_B_flavored_zero_init"] + lep_bad_m["Y_B_flavored_zero_init"])
    pf5_unred_k_ratio = lep_p["K_tot"] / lep_unred_pf5["K_tot"]
    pf5_unred_yb_rel_shift = rel_diff_mp(lep_p["Y_B_flavored_zero_init"], lep_unred_pf5["Y_B_flavored_zero_init"])

    prod_c12 = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s12_Dirac_CP_selected"]
    prod_c0 = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s0_ScalarLegacy_CP_selected"]
    seq_pmns_s12_diff = max(
        rel_diff_mp(seq_s12_p["ir_mz"]["pmns_mz"][k], mp.mpf(prod_c12["pmns_mz_sequential"][k]))
        for k in prod_c12["pmns_mz_sequential"]
    )
    seq_pmns_s0_diff = max(
        rel_diff_mp(seq_s0_p["ir_mz"]["pmns_mz"][k], mp.mpf(prod_c0["pmns_mz_sequential"][k]))
        for k in prod_c0["pmns_mz_sequential"]
    )
    k_tot_rel_diff = rel_diff_mp(lep_p["K_tot"], mp.mpf(prod_c12["boltzmann_leptogenesis"]["K_tot"]))
    yb_flav_rel_diff = rel_diff_mp(
        lep_p["Y_B_flavored_zero_init"], mp.mpf(prod_c12["boltzmann_leptogenesis"]["Y_B_flavored_zero_init"])
    )
    yb_th_rel_diff = rel_diff_mp(
        lep_p["Y_B_flavored_thermal_init"], mp.mpf(prod_c12["boltzmann_leptogenesis"]["Y_B_flavored_thermal_init"])
    )
    yb_un_rel_diff = rel_diff_mp(
        lep_p["Y_B_unflavored"], mp.mpf(prod_c12["boltzmann_leptogenesis"]["Y_B_unflavored"])
    )
    yb_s0_rel_diff = rel_diff_mp(
        lep_s0_p["Y_B_flavored_zero_init"], mp.mpf(prod_c0["boltzmann_leptogenesis"]["Y_B_flavored_zero_init"])
    )

    # 10-trial Haar U(3)^5 x U(3)_N scrambling through sequential seesaw + reduced-Planck GL4 Boltzmann
    rng_h2 = Xorshift64Star(202611240302)
    haar_seesaw_err = mp.mpf(0)
    for _ in range(10):
        uq = haar_unitary_householder(rng_h2)
        uur = haar_unitary_householder(rng_h2)
        udr = haar_unitary_householder(rng_h2)
        ul = haar_unitary_householder(rng_h2)
        uer = haar_unitary_householder(rng_h2)
        un = haar_unitary_householder(rng_h2)
        seq_sc = run_seq_seesaw_gl4(
            g_uv24,
            uq * (g_uv24 * tex_s12_t8_p["yu_hat"]) * uur.H,
            uq * ((g_uv24 / 5) * tex_s12_t8_p["yd_hat"]) * udr.H,
            ul * ((g_uv24 / 5) * tex_s12_t8_p["ye_hat"]) * uer.H,
            ul * (g_uv24 * tex_s12_t8_p["yn_hat"]) * un.H,
            un.apply(mp.conj) * tex_s12_t8_p["mr_raw"] * un.H,
            mr0_c, t_susy24, soft_ref_guv, 15, 10, sgn_mu=1,
        )
        lep_sc = solve_mssm_boltzmann_gl4(
            seq_sc["lepto_snapshot"]["ye_at_MR3"],
            seq_sc["lepto_snapshot"]["ynu_rot_at_MR3"],
            seq_sc["lepto_snapshot"]["M_R_eigs_over_MGUT"],
            mkk_over_mpl_red, n_coarse=600, use_consistent_reduced_mpl=True, compute_thermal=False,
        )
        ep = max(abs(seq_sc["ir_mz"]["pmns_mz"][k] - seq_s12_p["ir_mz"]["pmns_mz"][k]) for k in seq_s12_p["ir_mz"]["pmns_mz"])
        el = max(
            abs(lep_sc["eps_tot"] - lep_p["eps_tot"]),
            abs(lep_sc["Y_B_flavored_zero_init"] - lep_p["Y_B_flavored_zero_init"]),
            abs(lep_sc["Y_B_unflavored"] - lep_p["Y_B_unflavored"]),
        )
        haar_seesaw_err = max(haar_seesaw_err, ep, el)

    # 12/12 Neutral Bino LSP via GL4 Soft-SUSY & d=6 Proton Decay Ratios
    bino_count = 0
    lsp_max_diff = mp.mpf(0)
    prod_lsp = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["lsp_identity_spectrum"]["benchmarks"]
    idx_l = 0
    for a0_v in (mp.mpf(0), -mp.sqrt(3), -mp.sqrt(6)):
        sft = integrate_soft_susy_gl4(g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 48, a0_v)
        for tb_i in (5, 15, 30, 50):
            tb_m = mp.mpf(tb_i)
            mu_s = mp.sqrt((sft["mHd2"] - sft["mHu2"] * tb_m * tb_m) / (tb_m * tb_m - 1))
            spec = {
                "M1_bino": abs(sft["M1"]),
                "M2_wino": abs(sft["M2"]),
                "M3_gluino": abs(sft["M3"]),
                "mu_higgsino": mu_s,
                "m_stau_R": mp.sqrt(sft["me3"]),
                "m_slep_L": mp.sqrt(sft["mL3"]),
                "m_stop_R": mp.sqrt(sft["mu3"]),
                "m_sbot_R": mp.sqrt(sft["md3"]),
                "m_Q3": mp.sqrt(sft["mQ3"]),
                "m_gravitino_ref": mp.mpf(1),
            }
            lsp_nm = min(spec, key=lambda k: spec[k])
            if lsp_nm == "M1_bino" and spec["M1_bino"] < mp.mpf(1):
                bino_count += 1
            lsp_max_diff = max(
                lsp_max_diff,
                rel_diff_mp(spec["M1_bino"], mp.mpf(prod_lsp[idx_l]["M1_over_m0"])),
                rel_diff_mp(spec["mu_higgsino"], mp.mpf(prod_lsp[idx_l]["mu_over_m0"])),
                rel_diff_mp(spec["m_stau_R"], mp.mpf(prod_lsp[idx_l]["m_stauR_over_m0"])),
            )
            idx_l += 1

    a_uv24 = q_mp(1, 24)
    mgut_over_msusy = mp.exp(-t_susy24)
    prod_prot = ow26_res["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["d6_proton_decay_dimensionless_ratios"]
    prot_max_diff = mp.mpf(0)
    for m0v in (3, 10, 30):
        rat4 = (mgut_over_msusy * mp.mpf(m0v)) ** 4
        prot_max_diff = max(
            prot_max_diff,
            rel_diff_mp(rat4, mp.mpf(prod_prot[f"m0_{m0v}v_MGUT_over_vEW_4"])),
            rel_diff_mp(rat4 / (a_uv24 ** 2), mp.mpf(prod_prot[f"m0_{m0v}v_MGUT_over_vEW_4_over_aUV2"])),
        )

    # --- REF-4: Borromean, Cross-Seat, Faithful 8^3_4, Lock SHA, Custody (269/269), A2-OW16 v18 ---
    ref4 = run_ref4_borromean_cross_seat_custody_and_ow16(
        repo_root,
        ow26_res,
        ow16_res,
        g_s12_t8,
        k_s0_t8,
        fcnc_s12_t8,
        fcnc_s0_t8,
        gl4_cim_runs["CURV_s12_CIM_M16_kH1min_m0_3v"]["mh_pole_over_mz"],
        seq_s12_p["ir_mz"]["pmns_mz"]["s12sq"],
        seq_s0_p["ir_mz"]["pmns_mz"]["s12sq"],
        lep_p["K_tot"],
        lep_p["Y_B_flavored_zero_init"],
        g_uv24,
        t_susy24,
        soft_ref_guv,
    )
    pf6_caught = ref4.pop("_pf6_caught")

    # --- 6 / 6 Independent Planted Fault Controls (including DISC-V7-1 & DISC-V7-2 regressions!) ---
    pf4_scalar_vs_dirac_diff = abs(fcnc_s0_t8["uv_split"] - fcnc_s12_t8["uv_split"])
    planted_faults = {
        "PF_REF3_1_corrupt_2loop_sm_o4_mv3_and_truncated_higgs_pole_caught": bool(
            pf1_o4_diff > p10(-5)
            and pf1_mv3_diff > p10(-5)
            and sm_audits["disc_v7_2_planted_truncated_rg_residual"] != "0"
            and trunc_mh_scale_drift_pf1 > q_mp(1, 10)
        ),
        "PF_REF3_2_broken_haar_nonunitary_caught": bool(pf2_broken_haar_drift > p10(-3)),
        "PF_REF3_3_wrong_e8_vd_normalization_caught": bool(r2_int["pf3_vd_wrong_caught"]),
        "PF_REF3_4_wrong_dirac_liouville_weight_e2phi_caught": bool(
            r2_int["weyl_scalar_diff_ok"] and pf4_scalar_vs_dirac_diff > q_mp(15, 100)
        ),
        "PF_REF3_5_wrong_cp_mirror_lnc_sign_and_unreduced_planck_hubble_caught": bool(
            pf5_bad_mirror_sum > p10(-10)
            and ww_wrong_err_mp > mp.mpf(1)
            and abs(pf5_unred_k_ratio - mp.sqrt(8 * mp.pi)) < p10(-10)
            and pf5_unred_yb_rel_shift > q_mp(1, 2)
        ),
        "PF_REF3_6_mutated_blind_lock_v2_and_manifest_tamper_caught": bool(pf6_caught),
    }
    pf_caught_count = sum(1 for v in planted_faults.values() if v)

    # --- Dynamically Assemble Discrepancies Ledger (Guardrail 2: ZERO literal hard-coding!) ---
    discrepancies: list[dict[str, Any]] = []

    if not sm_audits["disc1_mv2_8x8_exact_and_v8_fixed"]:
        discrepancies.append({"id": "REG-DISC-1", "domain": "REF-1 / OW26-A", "severity": "REAL_PHYSICS_BUG", "summary": "DISC-1 MV II non-commuting Yukawa order regression detected."})
    if not sm_audits["disc2_v8_fixed"]:
        discrepancies.append({"id": "REG-DISC-2", "domain": "REF-1 / OW26-A", "severity": "REAL_PHYSICS_BUG", "summary": "DISC-2 MV III +27/5 quartic trace regression detected."})
    if not sm_audits["disc3_v8_fixed"]:
        discrepancies.append({"id": "REG-DISC-3", "domain": "REF-1 / OW26-A", "severity": "HIGH_IMPACT_PHYSICS_BUG", "summary": "DISC-3 Martin-Vaughn DR->MS Yukawa Casimir regression detected."})
    if not (ref4["a2_ow16_v18_audit"]["obs17_true_tau8_G_s12_vs_FCNC_consistent"] and fcnc_t8_vs_prod_err < p10(-5)):
        discrepancies.append({"id": "REG-DISC-4", "domain": "REF-2 / OW16 v18 OBS-17", "severity": "CONVENTION_INDEX_MISMATCH", "summary": "DISC-4 tau_8^+ vs tau_r Kahler index regression detected."})
    if not (ww_proof["passed"] and yb_flav_rel_diff < p10(-5)):
        discrepancies.append({"id": "REG-DISC-5", "domain": "REF-3 / OW26-C", "severity": "REAL_PHYSICS_BUG", "summary": f"DISC-5 Boltzmann LNC/Radau regression: yb_flav_rel_diff={fmt_mp(yb_flav_rel_diff, 8)}."})
    if max_layer1_run_diff > p10(-5):
        discrepancies.append({"id": "REG-DISC-NUM-1", "domain": "REF-1 / OW26-A", "severity": "NUMERICAL_DISCREPANCY", "summary": f"GL4 vs v8 RK4 exceeded 1e-5: {fmt_mp(max_layer1_run_diff, 8)}."})
    if not (
        sm_audits["disc_v7_1_v8_symbolic_ratio_match"]
        and k_tot_rel_diff < p10(-6)
        and yb_flav_rel_diff < p10(-5)
        and yb_th_rel_diff < p10(-5)
        and yb_un_rel_diff < 2 * p10(-5)
        and yb_s0_rel_diff < 2 * p10(-5)
        and cp_odd_err < p10(-30)
        and lep_p["Y_B_flavored_zero_init"] > 0
        and prod_c12["selected_CP_branch_by_YB_gt_0"] == "tau8_plus"
    ):
        discrepancies.append({
            "id": "REG-DISC-V7-1",
            "domain": "REF-3 / OW26-C",
            "severity": "HIGH_IMPACT_PHYSICS_BUG",
            "summary": f"DISC-V7-1 reduced-Planck Boltzmann mismatch: K_tot_diff={fmt_mp(k_tot_rel_diff, 8)}, yb_fl_diff={fmt_mp(yb_flav_rel_diff, 8)}, yb_un_diff={fmt_mp(yb_un_rel_diff, 8)}.",
        })
    if not (
        sm_audits["disc_v7_2_v8_fixed"]
        and higgs_scale_vs_v8_diff < p10(-5)
        and exact_mh_scale_drift < q_mp(5, 100)
        and perturbative_floor_hits == 0
    ):
        discrepancies.append({
            "id": "REG-DISC-V7-2",
            "domain": "REF-1 / OW26-A",
            "severity": "HIGH_IMPACT_PHYSICS_BUG",
            "summary": f"DISC-V7-2 1-loop RG-invariant Higgs pole mismatch: scale_vs_v8_diff={fmt_mp(higgs_scale_vs_v8_diff, 8)}, drift={fmt_mp(exact_mh_scale_drift, 8)}.",
        })
    if not ref2["Dirac_s12_Liouville_GL10_GL6"]["passed"]:
        discrepancies.append({"id": "REF2-LIOUVILLE", "domain": "REF-2 / OW26-B4", "severity": "NUMERICAL_DISCREPANCY", "summary": "GL10/GL6 Dirac Liouville check failed."})
    if not (ref2["E8_240root_clebsch"]["passed"] and ref2["M8_CIM_2D_GaussLegendre"]["passed"] and ref2["B3_SUGRA_Planck_Factor"]["passed"]):
        discrepancies.append({"id": "REF2-E8-CIM-B3", "domain": "REF-2 / OW26-B1..B3", "severity": "NUMERICAL_DISCREPANCY", "summary": "E8, CIM, or B3 SUGRA check failed."})
    if not (
        seq_pmns_s12_diff < p10(-5)
        and seq_pmns_s0_diff < p10(-5)
        and dirac_vs_sup_cp_inv_err < p10(-24)
        and haar_seesaw_err < p10(-12)
        and bino_count == 12
        and lsp_max_diff < p10(-6)
        and prot_max_diff < p10(-10)
    ):
        discrepancies.append({"id": "REF3-SEESAW-LSP-PROTON", "domain": "REF-3 / OW26-C", "severity": "NUMERICAL_DISCREPANCY", "summary": "Seesaw, Haar, LSP, or proton check failed."})
    if not (
        ref4["borromean_quotient_chain"]["passed"]
        and ref4["chat1_mirror_theorem"]["passed"]
        and ref4["physical_32514763f_vs_B4UV_Dterm"]["passed"]
        and ref4["agyexp_834_faithful_side_by_side_GL4"]["passed"]
        and ref4["blind_prediction_lock_v2_sha256"]["exact_match"]
        and ref4["git_diff_27f5d89fa_to_HEAD"]["passed"]
        and ref4["branch_custody_manifests"]["all_verified"]
        and ref4["a2_ow16_v18_audit"]["all_structural_and_internal_checks_ok"]
    ):
        discrepancies.append({"id": "REF4-CUSTODY-OW16", "domain": "REF-4 / OW26-D,E & OW16 v18", "severity": "CUSTODY_OR_CONSISTENCY_FAILURE", "summary": "REF-4 cross-seat, lock SHA, custody, or A2-OW16 v18 audit failed."})

    # Transparent non-blocking scientific caveats (reported unvarnished without altering equation validity)
    non_blocking_diagnostics: list[dict[str, Any]] = []
    clamped_sugra_tags = [k for k, v in sugra_floor_audit.items() if v["hit_1e_neg10_floor_at_mu_MZ"]]
    if clamped_sugra_tags:
        non_blocking_diagnostics.append({
            "id": "DIAG-SUGRA-FLOOR-CLAMP",
            "domain": "REF-1 / OW26-A mz_sugra_planck_factor_runs (auxiliary, NOT in B4_UV_MZ_BLIND_LOCK_V2)",
            "affected_runs": clamped_sugra_tags,
            "summary": "All 3 auxiliary SUGRA sensitivity runs (aUVinv=23,24,25; alpha_3(M_Z) in [0.54, 1.11]) enter strong QCD coupling below m_t so 1-loop delta_top(mu=M_Z) < -1 hits the 10^-10 positivity clamp (reporting mh_pole/M_Z ~ 2.7e-5 vs perturbative mu=m_t O(2.3-2.5)). All 14 perturbative runs and 100% of B4_UV_MZ_BLIND_LOCK_V2 are completely unclamped (0/14 floor hits).",
        })
    if ref4["a2_ow16_v18_audit"]["minor_prose_note_honest_caveat_says_referee_v2"]:
        non_blocking_diagnostics.append({
            "id": "DIAG-OW16-V18-PROSE-TYPO",
            "domain": "REF-4 / A2-OW16 v18 guardrail5_input_ledger_v18.conditional_parameter_reduction_branches.honest_caveat",
            "summary": "Minor prose wording note: honest_caveat ends with 'awaiting Cold-Room Referee v2' instead of 'v3' (zero numerical or structural impact).",
        })

    all_8_prior_findings_remediated = bool(
        sm_audits["disc1_mv2_8x8_exact_and_v8_fixed"]
        and sm_audits["disc2_v8_fixed"]
        and sm_audits["disc3_v8_fixed"]
        and ref4["a2_ow16_v18_audit"]["obs17_true_tau8_G_s12_vs_FCNC_consistent"]
        and fcnc_t8_vs_prod_err < p10(-5)
        and ww_proof["passed"]
        and max_layer1_run_diff < p10(-5)
        and sm_audits["disc_v7_1_v8_symbolic_ratio_match"]
        and k_tot_rel_diff < p10(-6)
        and yb_flav_rel_diff < p10(-5)
        and yb_th_rel_diff < p10(-5)
        and yb_un_rel_diff < 2 * p10(-5)
        and sm_audits["disc_v7_2_v8_fixed"]
        and higgs_scale_vs_v8_diff < p10(-5)
        and perturbative_floor_hits == 0
    )

    all_referee_gates_passed = bool(
        all_8_prior_findings_remediated
        and len(discrepancies) == 0
        and sm_audits["group_theory_and_o4_exact"]
        and haar_u35_max_err < p10(-12)
        and ref2["E8_240root_clebsch"]["passed"]
        and ref2["M8_CIM_2D_GaussLegendre"]["passed"]
        and ref2["B3_SUGRA_Planck_Factor"]["passed"]
        and ref2["Dirac_s12_Liouville_GL10_GL6"]["passed"]
        and seq_pmns_s12_diff < p10(-5)
        and seq_pmns_s0_diff < p10(-5)
        and yb_s0_rel_diff < 2 * p10(-5)
        and cp_odd_err < p10(-30)
        and dirac_vs_sup_cp_inv_err < p10(-24)
        and haar_seesaw_err < p10(-12)
        and bino_count == 12
        and lsp_max_diff < p10(-6)
        and prot_max_diff < p10(-10)
        and ref4["borromean_quotient_chain"]["passed"]
        and ref4["chat1_mirror_theorem"]["passed"]
        and ref4["physical_32514763f_vs_B4UV_Dterm"]["passed"]
        and ref4["agyexp_834_faithful_side_by_side_GL4"]["passed"]
        and ref4["blind_prediction_lock_v2_sha256"]["exact_match"]
        and ref4["git_diff_27f5d89fa_to_HEAD"]["passed"]
        and ref4["branch_custody_manifests"]["all_verified"]
        and ref4["a2_ow16_v18_audit"]["all_structural_and_internal_checks_ok"]
        and ast_self["clean"]
        and ast_ow26["clean"]
        and ast_ow16["clean"]
        and json_scan_ow26["clean"]
        and json_scan_ow16["clean"]
        and pf_caught_count == 6
    )

    output = {
        "referee_id": "A2-OW26-v8-and-A2-OW16-v18-Cold-Room-Zero-Trust-Referee-v3",
        "empirical_firewall": "0 of 19",
        "all_8_referee_v1_v2_findings_remediated": all_8_prior_findings_remediated,
        "discrepancies_count": len(discrepancies),
        "all_referee_gates_passed": all_referee_gates_passed,
        "discrepancies": discrepancies,
        "non_blocking_diagnostics": non_blocking_diagnostics,
        "planted_faults_caught": pf_caught_count,
        "planted_faults_total": 6,
        "planted_faults": planted_faults,
        "hygiene_and_raw_json_audits": {
            "referee_v3_script_ast": ast_self,
            "ow26_v8_script_ast": ast_ow26,
            "ow16_v18_script_ast": ast_ow16,
            "ow26_v8_raw_json_floats": json_scan_ow26,
            "ow16_v18_raw_json_floats": json_scan_ow16,
        },
        "REF_1_2loop_sm_mssm_gl4_and_first_principles_audits": {
            "integrator": "2-stage implicit Gauss-Legendre GL4 (O(h^4), symplectic, A-stable)",
            "haar_generator": "Xorshift64* + complex Householder QR (Mezzadri, matched GL4 step count)",
            "first_principles_sm_and_dr_ms_audits": sm_audits,
            "gl4_vs_v8_max_rel_diff_all_17_runs": fmt_mp(max_layer1_run_diff, 10),
            "standard_10_run_diffs": layer1_run_diffs,
            "cim_M16_4_run_diffs": cim_run_diffs,
            "sugra_3_run_diffs": sugra_run_diffs,
            "all_14_perturbative_runs_unclamped": bool(perturbative_floor_hits == 0),
            "sugra_nonperturbative_mu_MZ_vs_mt_floor_clamp_audit": sugra_floor_audit,
            "higgs_pole_mu_MZ_vs_mt_scale_invariance": {
                "mu_mt_over_MZ_central_10v": fmt_mp(sf_mt_10, 10),
                "exact_mh_pole_over_v_at_MZ_vs_mt": [fmt_mp(mh_ex_at_mz, 12), fmt_mp(mh_ex_at_mt, 12)],
                "exact_scale_drift_rel": fmt_mp(exact_mh_scale_drift, 10),
                "max_rel_diff_vs_v8": fmt_mp(higgs_scale_vs_v8_diff, 10),
                "planted_v7_truncated_scale_drift_rel": fmt_mp(trunc_mh_scale_drift_pf1, 8),
            },
            "fcnc_dilution_true_tau8": {
                "max_rel_diff_vs_v8": fmt_mp(fcnc_t8_vs_prod_err, 10),
                "CURV_s12_true_tau8_uv_ir_dilution": [
                    fmt_mp(fcnc_s12_t8["uv_split"], 12),
                    fmt_mp(fcnc_s12_t8["ir_split"], 12),
                    fmt_mp(fcnc_s12_t8["dilution"], 12),
                ],
                "CURV_s0_true_tau8_uv_ir_dilution": [
                    fmt_mp(fcnc_s0_t8["uv_split"], 12),
                    fmt_mp(fcnc_s0_t8["ir_split"], 12),
                    fmt_mp(fcnc_s0_t8["dilution"], 12),
                ],
            },
            "guardrail3_10trial_haar_U3_5_end_to_end_GL4_matched_err": fmt_mp(haar_u35_max_err, 10),
        },
        "REF_2_e8_cim_sugra_and_dirac_liouville": ref2,
        "REF_3_sequential_seesaw_gl4_boltzmann_lsp_proton": {
            "takagi_method": "Real 6x6 symmetric block eigensolver [[Re M, Im M], [Im M, -Re M]]",
            "boltzmann_method": "2-stage implicit Gauss-Legendre GL4 (N=600 vs 1200 + O(h^4) Richardson, consistent reduced Planck)",
            "weisskopf_wigner_independent_LNC_proof": ww_proof,
            "dirac_vs_superpotential_CP_branch_invariance_err": fmt_mp(dirac_vs_sup_cp_inv_err, 10),
            "seq_seesaw_s12_pmns_max_rel_diff_vs_v8": fmt_mp(seq_pmns_s12_diff, 10),
            "seq_seesaw_s0_pmns_max_rel_diff_vs_v8": fmt_mp(seq_pmns_s0_diff, 10),
            "s12_vs_s0_true_tau8_s12sq_shift": {
                "s0_scalar_t8_s12sq": fmt_mp(seq_s0_p["ir_mz"]["pmns_mz"]["s12sq"], 12),
                "s12_dirac_t8_s12sq": fmt_mp(seq_s12_p["ir_mz"]["pmns_mz"]["s12sq"], 12),
            },
            "boltzmann_gl4_vs_v8_radau_consistent_reduced_MPl": {
                "K_flav_gl4": [fmt_mp(v, 12) for v in lep_p["K_flav"]],
                "K_tot_gl4": fmt_mp(lep_p["K_tot"], 12),
                "K_tot_rel_diff_vs_v8": fmt_mp(k_tot_rel_diff, 10),
                "eps_tot_gl4": fmt_mp(lep_p["eps_tot"], 12),
                "flav_sum_err": fmt_mp(lep_p["flav_sum_err"], 10),
                "Y_B_flavored_zero_init_gl4": fmt_mp(lep_p["Y_B_flavored_zero_init"], 12),
                "Y_B_flavored_thermal_init_gl4": fmt_mp(lep_p["Y_B_flavored_thermal_init"], 12),
                "Y_B_unflavored_gl4": fmt_mp(lep_p["Y_B_unflavored"], 12),
                "Y_B_s0_flavored_zero_init_gl4": fmt_mp(lep_s0_p["Y_B_flavored_zero_init"], 12),
                "Y_B_gl4_step_halving_rel_err": fmt_mp(lep_p["Y_B_gl4_step_halving_rel_err"], 10),
                "Y_B_flav_rel_diff_vs_v8_radau": fmt_mp(yb_flav_rel_diff, 10),
                "Y_B_thermal_rel_diff_vs_v8_radau": fmt_mp(yb_th_rel_diff, 10),
                "Y_B_unflav_rel_diff_vs_v8_radau": fmt_mp(yb_un_rel_diff, 10),
                "Y_B_s0_flav_rel_diff_vs_v8_radau": fmt_mp(yb_s0_rel_diff, 10),
                "CP_odd_YB_plus_plus_YB_minus_err": fmt_mp(cp_odd_err, 10),
                "tau8_plus_YB_gt_0_selected": bool(lep_p["Y_B_flavored_zero_init"] > 0),
                "planted_unreduced_MPl_K_ratio_vs_sqrt_8pi": fmt_mp(pf5_unred_k_ratio, 12),
                "planted_unreduced_MPl_YB_rel_shift": fmt_mp(pf5_unred_yb_rel_shift, 8),
            },
            "guardrail3_10trial_haar_U3_5_x_U3_N_matched_err": fmt_mp(haar_seesaw_err, 10),
            "lsp_neutral_bino_count_out_of_12": bino_count,
            "lsp_gl4_vs_v8_max_rel_diff": fmt_mp(lsp_max_diff, 10),
            "d6_proton_ratios_max_rel_diff": fmt_mp(prot_max_diff, 10),
        },
        "REF_4_borromean_cross_seat_custody_and_ow16_v18": ref4,
    }

    assert_no_json_floats_obj(output)
    out_text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    self_json_scan = scan_raw_json_float_tokens(out_text)
    assert self_json_scan["clean"], f"Referee v3 JSON float token leak: {self_json_scan}"

    out_path = script_path.parent / "a2_ow26_referee_v3_results.json"
    out_path.write_text(out_text, encoding="utf-8")
    print("REF-A2-OW26-V3 COMPLETE: output written to a2_ow26_referee_v3_results.json (seal OUTPUT_SHA256 & git commit before reading).")


if __name__ == "__main__":
    main()
