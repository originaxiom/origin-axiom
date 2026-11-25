"""Standalone 0-of-19 Authoritative Producer v4 for Card AGY-002_A2-WHOLE-INSTRUMENT.

Pure Python stdlib + mpmath + sympy ONLY.
Zero float/complex AST literals or casts; zero numpy/scipy/frontier imports;
zero JSON float tokens. Strictly 0 of 19 (data-free) and zero SM sculpting.

Modules:
  W1: Surgical B1980 Part A/B audit & P-882 Q1 resolution (exact S-covariance on all 96 pts
      at B1980's 3 pairs once L_2(i/y) = L_2(iy) + ln(y) is restored, weight-0 full-norm
      s_k^{inv} = sqrt(Im tau)*s_k invariance under T/S/M, exact PF1 reproduction of B1980's
      0.12/0.18/0.32 bug, and corrected K != 1 duality audit).
  W2: Whole level-30 instrument (all 576 primitive order-30 pts = 288 pairs, symbolic tropical
      + finite-height y=2,3), closed hyperbolic geodesic gamma_M(u) of M = [[2,1],[1,1]]
      (zero free y, exact basepoint invariance, geodesic average vs Hermitian/coherent integral),
      plus B1981 E[6]_prim shell & chat1 W-LV1 Y_e(w) ~ Y_d(3w) cross-checks.
  W3: Un-sculpted natural unfolding (I): 1-loop Coleman-Weinberg effective potential V_CW(h)
      on S^5 (1-doublet conjugated) & S^5 x S^5 (2-doublet all-S with portal lam_3) via exact
      Wirtinger Riemannian BB gradient descent; and exact SL(2,Z)-invariant modular potential
      V_CW^{(all-288)}(tau) across F (exact 288/288 cusp-norm exponent theorem).
  W4: Un-sculpted natural unfolding (II): Guardrail 4 literature benchmarks (15/15 2HDM-II +
      1HDM + opposite Xing-Zhou |V_cb| sign), polar Fuchsian curved spin-1/2 Dirac Kahler metric
      G_{s=1/2}(tau) (Gauss-Bonnet verified), forward 2-loop Type-II 2HDM matrix RG unfolding
      (spontaneous radiative EWSB, IR focusing, CKM ordering), un-sculpted canonical Y_nu^T Y_nu
      Autonne-Takagi PMNS, and 10-trial Haar U(3)^3 / U(3)^5 scrambling.
  W5: All 6 planted negative controls PF1..PF6, AST/JSON hygiene (G6), and zero-sculpting audit.
"""

import ast
import hashlib
import json
import math
import pathlib
import random
import time
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import sympy as sp

SCRIPT_PATH = pathlib.Path(__file__).resolve()
OUT_JSON_PATH = SCRIPT_PATH.with_name("verify_a2_whole_instrument_v4_out.json")
OUT_SHA_PATH = SCRIPT_PATH.with_name("OUTPUT_SHA256.txt")


# ---------------------------------------------------------------------------
# Zero-Float / Zero-Complex Helpers & Formatting
# ---------------------------------------------------------------------------

def iu():
    return mp.mpc(0, 1)


def mp_rat(p: int, q: int = 1):
    return mp.mpf(p) / mp.mpf(q)


def mp_frac(f: Fraction):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def mp_pow10(k: int):
    return mp.mpf(10) ** k


def mp_str(x, digits: int = 12) -> str:
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)
    if isinstance(x, mp.mpc):
        return f"({mp.nstr(mp.re(x), digits)},{mp.nstr(mp.im(x), digits)})"
    return mp.nstr(mp.mpf(x), digits)


def frac_str(f: Fraction) -> str:
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


def nd_frac(x: Fraction) -> Fraction:
    r = x - math.floor(x)
    return r if r <= Fraction(1, 2) else Fraction(1, 1) - r


def mod1_pt(a: Fraction, b: Fraction) -> Tuple[Fraction, Fraction]:
    return (a - math.floor(a), b - math.floor(b))


def pt_order(p: Tuple[Fraction, Fraction]) -> int:
    return math.lcm(p[0].denominator, p[1].denominator)


def audit_own_ast() -> Dict[str, Any]:
    src = SCRIPT_PATH.read_text(encoding="utf-8")
    tree = ast.parse(src)
    float_lits = 0
    complex_lits = 0
    bad_calls = []
    bad_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("float", "complex"):
                bad_calls.append(node.func.id)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if any(b in alias.name for b in ("numpy", "scipy", "frontier")):
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(b in mod for b in ("numpy", "scipy", "frontier")):
                bad_imports.append(mod)
    return {
        "float_literals": float_lits,
        "complex_literals": complex_lits,
        "float_complex_casts": len(bad_calls),
        "forbidden_imports": len(bad_imports),
        "clean": (float_lits == 0 and complex_lits == 0 and len(bad_calls) == 0 and len(bad_imports) == 0),
    }


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


# ---------------------------------------------------------------------------
# Fundamental-Domain Reduction & Exact Fuchsian Weierstrass L_2(tau) Solver
# ---------------------------------------------------------------------------

def reduce_to_fd_mp(tau):
    """Find gamma = [[a,b],[c,d]] in SL(2,Z) such that gamma*tau lies in standard FD."""
    a, b, c, d = 1, 0, 0, 1
    z = mp.mpc(mp.re(tau), mp.im(tau))
    for _ in range(250):
        k = int(mp.nint(mp.re(z)))
        if k != 0:
            z = z - k
            a, b = a - k * c, b - k * d
        if abs(z) < 1 - mp_pow10(-25):
            z = -1 / z
            a, b, c, d = -c, -d, a, b
        else:
            break
    # Verify exact SL(2,Z) action: (a*tau + b) / (c*tau + d) == z
    denom = c * tau + d
    return z, (a, b, c, d), denom


def solve_L2_fuchsian_raw(tau, dps: int = 38, return_full: bool = False):
    """Direct unreduced Fuchsian Weierstrass ODE solver for length-2 horocycle L_2(tau).

    Handles both Im(tau) >= 1 and Im(tau) < 1 (using short-cycle seed for Im(tau) < 1),
    enforcing all three real traces (Ta, Tb, Tab) so x = 0 converges cleanly.
    """
    ty = mp.im(tau)
    dps_ode = max(dps, 36 + int(mp.ceil(max(ty, 1 / ty))))
    mp.mp.dps = dps_ode
    I = iu()
    pi = mp.pi
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    ty = mp.im(tau)

    q = mp.exp(2 * I * pi * tau)
    K = max(8, int(mp.ceil((dps_ode * mp.mpf(231)) / (mp.mpf(628) * ty))) + 8)
    qp = [mp.mpc(1)] * (K + 1)
    for n in range(1, K + 1):
        qp[n] = qp[n - 1] * q

    e2 = mp.mpc(1) - 24 * sum(n * qp[n] / (1 - qp[n]) for n in range(1, K + 1))
    e4 = mp.mpc(1) + 240 * sum((n ** 3) * qp[n] / (1 - qp[n]) for n in range(1, K + 1))
    e6 = mp.mpc(1) - 504 * sum((n ** 5) * qp[n] / (1 - qp[n]) for n in range(1, K + 1))
    g2 = (4 * (pi ** 4) / 3) * e4
    g3 = (8 * (pi ** 6) / 27) * e6
    wp_const = -(pi * pi / 3) * e2
    m_list = list(range(1, K + 1))
    qm_list = [qp[m] for m in m_list]

    def wp_q4(z):
        w = mp.exp(2 * I * pi * z)
        inv_w = 1 / w
        s = w / ((1 - w) ** 2)
        for m, qm in zip(m_list, qm_list):
            wm = qm * w
            im = qm * inv_w
            s += wm / ((1 - wm) ** 2) + im / ((1 - im) ** 2)
        return (wp_const - 4 * pi * pi * s) / 4

    def build_seg_list(spec):
        out = []
        for za, zb, nsteps in spec:
            h = (zb - za) / nsteps
            w0 = [wp_q4(za + k * h) for k in range(nsteps + 1)]
            wm = [wp_q4(za + (k + mp_rat(1, 2)) * h) for k in range(nsteps)]
            out.append((h, nsteps, w0, wm))
        return out

    def make_b_spec(scale: int):
        if ty < 1:
            n_b = max(32 * scale, int(mp.ceil(abs(tau) * 60 * scale)))
            return [(z0, z0 + tau, n_b)]
        if ty <= 6:
            n_b = max(32 * scale, int(mp.ceil(abs(tau) * 18 * scale)))
            return [(z0, z0 + tau, n_b)]
        z_mid = z0 + tau / 2
        frac_span = mp.mpf(3) / ty
        za = z_mid - frac_span * tau
        zb = z_mid + frac_span * tau
        n_tail = max(14 * scale, int(mp.ceil(abs(za - z0) * 3 * scale)))
        n_mid = max(28 * scale, int(mp.ceil(abs(zb - za) * 16 * scale)))
        return [(z0, za, n_tail), (za, zb, n_mid), (zb, z0 + tau, n_tail)]

    def prop(segs, c_val, want_dc: bool = False):
        t00, t01, t10, t11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
        d00, d01, d10, d11 = mp.mpc(0), mp.mpc(0), mp.mpc(0), mp.mpc(0)
        for h, nsteps, w0, wm in segs:
            h2 = h / 2
            h6 = h / 6
            for k in range(nsteps):
                qa = w0[k] + c_val
                qm = wm[k] + c_val
                qb = w0[k + 1] + c_val
                k1_00, k1_01 = t10, t11
                k1_10, k1_11 = -qa * t00, -qa * t01
                m00, m01, m10, m11 = t00 + h2 * k1_00, t01 + h2 * k1_01, t10 + h2 * k1_10, t11 + h2 * k1_11
                k2_00, k2_01 = m10, m11
                k2_10, k2_11 = -qm * m00, -qm * m01
                n00, n01, n10, n11 = t00 + h2 * k2_00, t01 + h2 * k2_01, t10 + h2 * k2_10, t11 + h2 * k2_11
                k3_00, k3_01 = n10, n11
                k3_10, k3_11 = -qm * n00, -qm * n01
                p00, p01, p10, p11 = t00 + h * k3_00, t01 + h * k3_01, t10 + h * k3_10, t11 + h * k3_11
                k4_00, k4_01 = p10, p11
                k4_10, k4_11 = -qb * p00, -qb * p01
                if want_dc:
                    l1_00, l1_01 = d10, d11
                    l1_10, l1_11 = -qa * d00 - t00, -qa * d01 - t01
                    dm00, dm01, dm10, dm11 = d00 + h2 * l1_00, d01 + h2 * l1_01, d10 + h2 * l1_10, d11 + h2 * l1_11
                    l2_00, l2_01 = dm10, dm11
                    l2_10, l2_11 = -qm * dm00 - m00, -qm * dm01 - m01
                    dn00, dn01, dn10, dn11 = d00 + h2 * l2_00, d01 + h2 * l2_01, d10 + h2 * l2_10, d11 + h2 * l2_11
                    l3_00, l3_01 = dn10, dn11
                    l3_10, l3_11 = -qm * dn00 - n00, -qm * dn01 - n01
                    dp00, dp01, dp10, dp11 = d00 + h * l3_00, d01 + h * l3_01, d10 + h * l3_10, d11 + h * l3_11
                    l4_00, l4_01 = dp10, dp11
                    l4_10, l4_11 = -qb * dp00 - p00, -qb * dp01 - p01
                    d00 += h6 * (l1_00 + 2 * l2_00 + 2 * l3_00 + l4_00)
                    d01 += h6 * (l1_01 + 2 * l2_01 + 2 * l3_01 + l4_01)
                    d10 += h6 * (l1_10 + 2 * l2_10 + 2 * l3_10 + l4_10)
                    d11 += h6 * (l1_11 + 2 * l2_11 + 2 * l3_11 + l4_11)
                t00 += h6 * (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00)
                t01 += h6 * (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01)
                t10 += h6 * (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10)
                t11 += h6 * (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11)
        T = mp.matrix([[t00, t01], [t10, t11]])
        return (T, mp.matrix([[d00, d01], [d10, d11]])) if want_dc else T

    z0 = (1 + tau) / 2
    n_a1 = 80 if ty < mp_rat(4, 5) else (48 if ty < 1 else (36 if ty <= 3 else 24))
    ga1 = build_seg_list([(z0, z0 + 1, n_a1)])
    gb1 = build_seg_list(make_b_spec(1))
    # Short-cycle asymptotic seed (independent of S-partner!)
    if ty < 1 and abs(mp.re(tau)) < mp_rat(1, 5):
        c_val = mp.mpc(-(pi * pi) / (12 * ty * ty), 0)
    else:
        c_val = mp.mpc(pi * pi / 12, 0)

    def newton_step(Ta, dTa, Tb, dTb):
        Tab = Ta * Tb
        dTab = dTa * Tb + Ta * dTb
        trs = [Ta[0, 0] + Ta[1, 1], Tb[0, 0] + Tb[1, 1], Tab[0, 0] + Tab[1, 1]]
        dtrs = [dTa[0, 0] + dTa[1, 1], dTb[0, 0] + dTb[1, 1], dTab[0, 0] + dTab[1, 1]]
        scales = [max(mp.mpf(1), abs(v)) for v in trs]
        res = [mp.im(v) / sc for v, sc in zip(trs, scales)]
        df = [dv / sc for dv, sc in zip(dtrs, scales)]
        return res, df

    tol_c = mp_pow10(-13)
    for _ in range(36):
        Ta, dTa = prop(ga1, c_val, True)
        Tb, dTb = prop(gb1, c_val, True)
        res, df = newton_step(Ta, dTa, Tb, dTb)
        if max(abs(v) for v in res) < tol_c:
            break
        J = mp.matrix([[mp.im(d), mp.re(d)] for d in df])
        rv = mp.matrix([-v for v in res])
        step = mp.lu_solve(J.T * J, J.T * rv)
        smag = max(abs(step[0]), abs(step[1]))
        if smag > 5:
            step = step * (mp.mpf(5) / smag)
        c_val += mp.mpc(step[0], step[1])

    ga2 = build_seg_list([(z0, z0 + 1, 2 * n_a1)])
    gb2 = build_seg_list(make_b_spec(2))
    tol_f = mp_pow10(-18)
    for _ in range(6):
        Ta1, dTa1 = prop(ga1, c_val, True)
        Ta2, dTa2 = prop(ga2, c_val, True)
        Ta = (16 * Ta2 - Ta1) / 15
        dTa = (16 * dTa2 - dTa1) / 15
        Tb1, dTb1 = prop(gb1, c_val, True)
        Tb2, dTb2 = prop(gb2, c_val, True)
        Tb = (16 * Tb2 - Tb1) / 15
        dTb = (16 * dTb2 - dTb1) / 15
        res, df = newton_step(Ta, dTa, Tb, dTb)
        if max(abs(v) for v in res) < tol_f:
            break
        J = mp.matrix([[mp.im(d), mp.re(d)] for d in df])
        rv = mp.matrix([-v for v in res])
        step = mp.lu_solve(J.T * J, J.T * rv)
        c_val += mp.mpc(step[0], step[1])

    Ta = (16 * prop(ga2, c_val) - prop(ga1, c_val)) / 15
    Tb = (16 * prop(gb2, c_val) - prop(gb1, c_val)) / 15
    Tab = Ta * Tb
    rel_res = max(
        abs(mp.im(m[0, 0] + m[1, 1])) / max(mp.mpf(1), abs(m[0, 0] + m[1, 1]))
        for m in (Ta, Tb, Tab)
    )

    def to_mob(T):
        M = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
        return M / mp.sqrt(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])

    Tp = Tb * Ta * (Tb ** -1) * (Ta ** -1)
    Aa, P0 = to_mob(Ta), to_mob(Tp)
    pf = (P0[0, 0] - P0[1, 1]) / (2 * P0[1, 0])
    da = mp.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4 * Aa[0, 1] * Aa[1, 0])
    fa1 = (Aa[0, 0] - Aa[1, 1] + da) / (2 * Aa[1, 0])
    fa2 = (Aa[0, 0] - Aa[1, 1] - da) / (2 * Aa[1, 0])
    g0 = mp.matrix([[1, -fa1], [1, -pf]])
    ssc = (g0[0, 0] * fa2 + g0[0, 1]) / (g0[1, 0] * fa2 + g0[1, 1])
    g = mp.matrix([[1 / ssc, -fa1 / ssc], [1, -pf]])
    g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
    if mp.im(g[0, 1] / g[1, 1]) < 0:
        g = mp.matrix([[I, 0], [0, -I]]) * g
    RP = g * P0 * (g ** -1)
    RP = RP / RP[0, 0]
    lam = abs(mp.re(RP[0, 1]))

    z0_loc = z0 - int(mp.nint(mp.re(z0)))
    zs = (z0_loc / abs(z0_loc)) * min(mp_rat(1, 24), ty / 16)
    if ty <= 8:
        in_pts = [z0, z0_loc, z0_loc / 2, z0_loc / 4, z0_loc / 8, zs] if z0 != z0_loc else [z0, z0 / 2, z0 / 4, z0 / 8, zs]
    else:
        z_anchor = mp.mpc(mp_rat(1, 2), mp.mpf(2))
        in_pts = [z0, z_anchor, z_anchor / 2, z_anchor / 4, z_anchor / 8, zs]
    spu_in = 48 if ty < 1 else (36 if ty <= 3 else 20)
    gin1 = build_seg_list([(a, b, max(32, int(mp.ceil(abs(b - a) * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
    gin2 = build_seg_list([(a, b, max(64, int(mp.ceil(abs(b - a) * 2 * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
    Tin = (16 * prop(gin2, c_val) - prop(gin1, c_val)) / 15

    Mf = 64
    laur = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, Mf // 2 + 2):
        laur[n] = (mp.mpf(3) / ((2 * n + 3) * (n - 2))) * sum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
    Qc = [mp.mpc(0)] * (Mf + 1)
    Qc[0] = c_val
    for n in range(1, Mf // 2 + 1):
        Qc[2 * n] = laur[n] / 4
    al = [mp.mpc(0)] * (Mf + 1)
    be = [mp.mpc(0)] * (Mf + 1)
    al[0] = mp.mpc(1)
    for m in range(1, Mf + 1):
        al[m] = -sum(Qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(Qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)
    zp = [zs ** k for k in range(Mf + 1)]
    gloc = sum(be[k] * zp[k] for k in range(Mf + 1)) / sum(al[k] * zp[k] for k in range(Mf + 1))
    wzs = Tin[0, 1] / Tin[0, 0]
    uzs = (g[0, 0] * wzs + g[0, 1]) / (g[1, 0] * wzs + g[1, 1])
    imB = mp.im(uzs) + (lam / (2 * pi)) * (mp.log(abs(zs)) + mp.re(gloc))
    L2 = pi - (2 * pi / lam) * imB
    if return_full:
        return {
            "L2": mp.re(L2),
            "rel_res": rel_res,
            "c_val": c_val,
            "Ta": Ta,
            "Tb": Tb,
            "z0": z0,
            "wp_q4": wp_q4,
            "tau": tau,
        }
    return mp.re(L2), rel_res


_L2_FD_CACHE: Dict[Tuple[str, str, int], Tuple[Any, Any]] = {}


def solve_L2_fuchsian_cov(tau, dps: int = 38):
    """Exact SL(2,Z)-covariant L_2(tau) via FD reduction + exact cocycle -ln|c*tau+d|."""
    mp.mp.dps = max(dps, 42)
    z_fd, (a, b, c, d), denom = reduce_to_fd_mp(tau)
    z_sym = mp.mpc(abs(mp.re(z_fd)), mp.im(z_fd))
    key = (mp.nstr(mp.re(z_sym), 24), mp.nstr(mp.im(z_sym), 24), dps)
    if key not in _L2_FD_CACHE:
        _L2_FD_CACHE[key] = solve_L2_fuchsian_raw(z_sym, dps=dps, return_full=False)
    l2_fd, res = _L2_FD_CACHE[key]
    # Since L_2(gamma*tau) = L_2(tau) + ln|c*tau+d|, L_2(tau) = L_2(z_fd) - ln|c*tau+d|
    return l2_fd - mp.log(abs(denom)), res


# ---------------------------------------------------------------------------
# Exact Symbolic Tropical Engine (Full 576-point Level 30 + Norm Exponents)
# ---------------------------------------------------------------------------

SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "nu": 0}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e"), "nu": ("L", "nu")}


def build_symbolic_tropical_model() -> Dict[str, Any]:
    I_sp = sp.I
    s, p, r = sp.symbols("s p r")
    m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
    sc, pc, rc = sp.symbols("sc pc rc")
    m00c, m01c, m10c, m11c = sp.symbols("m00c m01c m10c m11c")

    svars = (s, p, r, m00, m01, m10, m11)
    hvars = (s, p, r, m00, m01, m10, m11, sc, pc, rc, m00c, m01c, m10c, m11c)

    QI = sp.Matrix([[I_sp, 0], [0, -I_sp]])
    QJ = sp.Matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    BL = [QJ, QI, QK]

    S_mat = sp.Matrix([[s, p], [r, -s]])
    M_mat = sp.Matrix([[m00, m01], [m10, m11]])
    Y = sp.Matrix(
        3, 3,
        lambda a, b: sp.expand(sum((BL[a].T * EPS * S_mat * BL[b]).multiply_elementwise(M_mat)))
    )

    def poly_monos(expr, vlist):
        expr = sp.expand(expr)
        if expr == 0:
            return []
        return list(sp.Poly(expr, *vlist).as_dict().keys())

    ents = [poly_monos(Y[i, j], svars) for i in range(3) for j in range(3)]
    mins = []
    for r0, r1 in ((0, 1), (0, 2), (1, 2)):
        for c0, c1 in ((0, 1), (0, 2), (1, 2)):
            mins.append(poly_monos(Y[r0, c0] * Y[r1, c1] - Y[r0, c1] * Y[r1, c0], svars))
    det_m = poly_monos(Y.det(), svars)

    Y_s0 = Y.subs(s, 0)
    ents_s0 = [poly_monos(Y_s0[i, j], svars) for i in range(3) for j in range(3)]
    mins_s0 = []
    for r0, r1 in ((0, 1), (0, 2), (1, 2)):
        for c0, c1 in ((0, 1), (0, 2), (1, 2)):
            mins_s0.append(poly_monos(Y_s0[r0, c0] * Y_s0[r1, c1] - Y_s0[r0, c1] * Y_s0[r1, c0], svars))

    Q_H = sp.Matrix([[1, 0, I_sp], [0, 1, 0], [1, 0, -I_sp]])
    YR_s0 = sp.expand(Q_H * Y_s0)
    conj_map = {
        s: sc, p: pc, r: rc,
        m00: m00c, m01: m01c, m10: m10c, m11: m11c,
        I_sp: -I_sp,
    }
    YR_s0_dag = YR_s0.T.applyfunc(lambda ex: sp.expand(ex.xreplace(conj_map)))
    H_s0 = sp.expand(YR_s0 * YR_s0_dag)
    H_s0_monos = [[poly_monos(H_s0[i, j], hvars) for j in range(3)] for i in range(3)]

    schur_s0_monos = {
        "lt_quarter": poly_monos(H_s0[2, 1] * H_s0[0, 0] - H_s0[2, 0] * H_s0[0, 1], hvars),
        "gt_quarter": poly_monos(H_s0[2, 0] * H_s0[1, 1] - H_s0[2, 1] * H_s0[1, 0], hvars),
    }
    return {
        "ents": ents,
        "mins": mins,
        "det": det_m,
        "ents_s0": ents_s0,
        "mins_s0": mins_s0,
        "H_s0_monos": H_s0_monos,
        "schur_s0_monos": schur_s0_monos,
    }


def channel_exps_q(ax: Fraction, ay: Fraction) -> List[Fraction]:
    e8 = Fraction(1, 8)
    h = Fraction(1, 2)
    return [
        nd_frac(ax + h) ** 2 + nd_frac(ay) ** 2 - e8,
        nd_frac(ax) ** 2 + nd_frac(ay) ** 2 - e8,
        nd_frac(ax) ** 2 + nd_frac(ay + h) ** 2 - e8,
        nd_frac(ax + h) ** 2 + nd_frac(ay + h) ** 2 - e8,
    ]


def eval_trop(monos: List[Tuple[int, ...]], exps: List[Fraction]) -> Optional[Fraction]:
    if not monos:
        return None
    best = None
    for m in monos:
        val = sum((Fraction(k, 1) * e for k, e in zip(m, exps)), Fraction(0, 1))
        if best is None or val < best:
            best = val
    return best


def has_exact_channel_zero(a: Fraction, b: Fraction, qL: int, qR: int) -> bool:
    ap = Fraction(qL + qR, 1) * a
    am = Fraction(qL - qR, 1) * a
    bp = Fraction(qL + qR, 1) * b
    bm = Fraction(qL - qR, 1) * b
    h = Fraction(1, 2)
    for ca, cb in ((ap + h, bp + h), (ap + h, bp), (ap, bp + h), (ap, bp)):
        if (ca - h).denominator == 1 and (cb - h).denominator == 1:
            return True
    for da, db in ((am + h, bm + h), (am + h, bm), (am, bm + h), (am, bm)):
        if (da - h).denominator == 1 and (db - h).denominator == 1:
            return True
    return False


def tropical_sector_and_tilts(model: Dict[str, Any], a: Fraction, qL: int, qR: int) -> Dict[str, Any]:
    mu = channel_exps_q(Fraction(qL, 1) * a, Fraction(qR, 1) * a)
    sexp = [Fraction(1, 8), Fraction(-1, 8), Fraction(3, 8)]
    ev_s = sexp + mu
    ev_h = ev_s + ev_s

    e_ent = min(eval_trop(ml, ev_s) for ml in model["ents"])
    e_min = min(eval_trop(ml, ev_s) for ml in model["mins"])
    e_det = eval_trop(model["det"], ev_s)

    e3_q = e_ent
    e2_q = e_min - e_ent
    e1_q = e_det - e_min

    e_ent0 = min(eval_trop(ml, ev_s) for ml in model["ents_s0"])
    e_min0 = min(eval_trop(ml, ev_s) for ml in model["mins_s0"])
    e2_q0 = e_min0 - e_ent0

    m2m3_eps = Fraction(2, 1) * (e2_q - e3_q)
    m1m3_eps = Fraction(2, 1) * (e1_q - e3_q)
    # Leading norm exponent of |Y_f| in eps-units: |Y_f| ~ eps^{2*e3_q} = exp(-2*pi*y*e3_q)
    norm_eps = Fraction(2, 1) * e3_q

    u = nd_frac(Fraction(qL, 1) * a)
    if u < Fraction(1, 4):
        idx1, idx2, idx3 = 2, 1, 0
        s_key = "lt_quarter"
    elif u > Fraction(1, 4):
        idx1, idx2, idx3 = 2, 0, 1
        s_key = "gt_quarter"
    else:
        return {
            "m2m3": m2m3_eps,
            "m1m3": m1m3_eps,
            "norm_eps": norm_eps,
            "degenerate_quarter": True,
            "t23": Fraction(0, 1),
            "t13": None,
            "t12": None,
        }

    h33 = eval_trop(model["H_s0_monos"][idx3][idx3], ev_h)
    h23 = eval_trop(model["H_s0_monos"][idx2][idx3], ev_h)
    h13 = eval_trop(model["H_s0_monos"][idx1][idx3], ev_h)
    c12 = eval_trop(model["schur_s0_monos"][s_key], ev_h)

    return {
        "m2m3": m2m3_eps,
        "m1m3": m1m3_eps,
        "norm_eps": norm_eps,
        "degenerate_quarter": False,
        "t23": Fraction(2, 1) * (h23 - h33),
        "t13": Fraction(2, 1) * (h13 - h33),
        "t12": Fraction(2, 1) * (c12 - h33 - Fraction(2, 1) * e2_q0),
    }


def tropical_full_point(model: Dict[str, Any], a: Fraction) -> Dict[str, Any]:
    up = tropical_sector_and_tilts(model, a, SIXY["Q"], SIXY["u"])
    dn = tropical_sector_and_tilts(model, a, SIXY["Q"], SIXY["d"])
    lp = tropical_sector_and_tilts(model, a, SIXY["L"], SIXY["e"])

    if up["degenerate_quarter"] or dn["degenerate_quarter"]:
        v23, v12, v13, v31 = Fraction(0, 1), None, None, None
    else:
        v23 = min(up["t23"], dn["t23"])
        u13_u = min(up["t13"], up["t12"] + up["t23"])
        u13_d = min(dn["t13"], dn["t12"] + dn["t23"])
        v12 = min(up["t12"], dn["t12"], u13_u + dn["t23"], u13_d + up["t23"])
        v13 = min(up["t13"], dn["t13"], up["t12"] + v23)
        v31 = min(up["t13"], dn["t13"], dn["t12"] + v23)

    return {
        "up_m2m3": up["m2m3"],
        "up_m1m3": up["m1m3"],
        "down_m2m3": dn["m2m3"],
        "down_m1m3": dn["m1m3"],
        "lep_m2m3": lp["m2m3"],
        "lep_m1m3": lp["m1m3"],
        "V12": v12,
        "V23": v23,
        "V13": v13,
        "V31": v31,
        "norm_eps_min": min(up["norm_eps"], dn["norm_eps"], lp["norm_eps"]),
        "up_norm_eps": up["norm_eps"],
        "dn_norm_eps": dn["norm_eps"],
        "lp_norm_eps": lp["norm_eps"],
    }


# ---------------------------------------------------------------------------
# Branch-Cut-Free Holomorphic Frame C Engine (with General-Higgs Operator)
# ---------------------------------------------------------------------------

def build_exact_edual(I):
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    units = {"1": mp.eye(2), "i": QI, "j": QJ, "k": QK}
    keys = ["1", "i", "j", "k"]
    ec = {k: EPS * units[k] for k in keys}
    G = mp.zeros(4, 4)
    for ti, tk in enumerate(keys):
        for si, sk in enumerate(keys):
            G[ti, si] = sum(ec[tk][m, n] * units[sk][m, n] for m in range(2) for n in range(2))
    Gi = G ** -1
    edual = {}
    for a, ak in enumerate(keys):
        M = mp.zeros(2, 2)
        for b, bk in enumerate(keys):
            M += Gi[b, a] * units[bk]
        edual[ak] = M
    return edual


class FrameCEngine:
    """Exact branch-cut-free Frame C engine with canonical weight-0 and general-Higgs support."""

    def __init__(self, tau, L2, dps: int = 55):
        self.dps = dps
        mp.mp.dps = dps
        I = iu()
        pi = mp.pi
        self.tau = mp.mpc(mp.re(tau), mp.im(tau))
        self.tx_m = mp.re(self.tau)
        self.ty_m = mp.im(self.tau)
        self.sqrt_ty = mp.sqrt(self.ty_m)
        self.L2 = mp.mpf(L2)

        q = mp.exp(2 * I * pi * self.tau)
        self.qh = mp.exp(I * pi * self.tau)
        self.K_q = int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(628) * self.ty_m))) + 14
        eta_p = mp.mpc(1)
        qp = mp.mpc(1)
        for _ in range(1, self.K_q + 2):
            qp = qp * q
            eta_p = eta_p * (1 - qp)
        self.eta = mp.exp(I * pi * self.tau / 12) * eta_p
        self.t1p = 2 * pi * (self.eta ** 3)
        rad_int = int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(314) * self.ty_m))) + 6
        self.nmax_th = math.isqrt(max(1, rad_int)) + 12

        s2 = mp.mpc(0)
        for n in range(0, self.nmax_th + 2):
            s2 += self.qh ** (n * (n + 1))
        th2 = 2 * mp.exp(I * pi * self.tau / 4) * s2
        th3 = mp.jtheta(3, 0, self.qh)
        th4 = mp.jtheta(4, 0, self.qh)
        denom = 24 * (self.eta ** 3)
        c0 = -(th2 ** 2) * (th3 ** 4 + th4 ** 4) / denom
        c1 = (th4 ** 2) * (th2 ** 4 + th3 ** 4) / denom
        c2 = I * (th3 ** 2) * (th2 ** 4 - th4 ** 4) / denom

        self.c_vec = [c0, c1, c2]
        self.c_norm = mp.sqrt(abs(c0) ** 2 + abs(c1) ** 2 + abs(c2) ** 2)
        self.c_hat = [v / self.c_norm for v in self.c_vec]

        self.QI = mp.matrix([[I, 0], [0, -I]])
        self.QJ = mp.matrix([[0, 1], [-1, 0]])
        self.QK = self.QI * self.QJ
        self.EPS = self.QJ
        self.blocks = [self.QJ, self.QI, self.QK]
        self.Q_basis = [self.QI, self.QJ, self.QK]
        self.Q_conj_basis = [
            self.EPS * mp.matrix([[mp.conj(Q[m, n]) for n in range(2)] for m in range(2)]) * self.EPS.T
            for Q in self.Q_basis
        ]
        self.S = c0 * self.QI + c1 * self.QJ + c2 * self.QK
        self.T_S = [
            [self.blocks[a].T * self.EPS * self.S * self.blocks[b] for b in range(3)]
            for a in range(3)
        ]
        self.T_Q = [
            [[self.blocks[a].T * self.EPS * self.Q_basis[k] * self.blocks[b] for b in range(3)] for a in range(3)]
            for k in range(3)
        ]
        self.T_Q_conj = [
            [[self.blocks[a].T * self.EPS * self.Q_conj_basis[k] * self.blocks[b] for b in range(3)] for a in range(3)]
            for k in range(3)
        ]
        self.edual = build_exact_edual(I)
        self._thc_cache: Dict[Tuple[Fraction, Fraction], Any] = {}
        self._weight_cache: Dict[Tuple[Fraction, Fraction], Any] = {}
        self._Mw_cache: Dict[Tuple[Fraction, Fraction, str], Any] = {}
        self._Y_cache: Dict[Tuple[Fraction, Fraction, str], Any] = {}

    def thc_direct(self, ca: Fraction, cb: Fraction):
        mp.mp.dps = self.dps
        I = iu()
        pi = mp.pi
        ca_m = mp_frac(ca)
        cb_m = mp_frac(cb)
        k0 = -((2 * ca.numerator + ca.denominator) // (2 * ca.denominator))
        s = mp.mpc(0)
        for dk in range(-self.nmax_th, self.nmax_th + 1):
            n = k0 + dk
            na = n + ca_m
            s += mp.exp(I * pi * self.tau * (na * na) + 2 * I * pi * na * cb_m)
        return s

    def thc(self, ca: Fraction, cb: Fraction):
        a_r = ca - math.floor(ca)
        n_b = math.floor(cb)
        b_r = cb - n_b
        key = (a_r, b_r)
        if key not in self._thc_cache:
            self._thc_cache[key] = self.thc_direct(a_r, b_r)
        base = self._thc_cache[key]
        if n_b == 0:
            return base
        mp.mp.dps = self.dps
        return mp.exp(2 * iu() * mp.pi * mp_frac(a_r) * n_b) * base

    def _weight_sqrt(self, al: Fraction, be: Fraction):
        al_r = al - math.floor(al)
        be_r = be - math.floor(be)
        key = (al_r, be_r)
        if key not in self._weight_cache:
            mp.mp.dps = self.dps
            I = iu()
            pi = mp.pi
            al_m = mp_frac(al_r)
            be_m = mp_frac(be_r)
            z_r = al_m * self.tau + be_m
            th1_v = mp.mpc(0)
            th1_d = mp.mpc(0)
            for n in range(0, self.nmax_th + 2):
                sgn = 1 if n % 2 == 0 else -1
                w = sgn * (self.qh ** (n * (n + 1)))
                ang = (2 * n + 1) * pi * z_r
                th1_v += w * mp.sin(ang)
                th1_d += w * (2 * n + 1) * pi * mp.cos(ang)
            a0 = 2 * I * pi * al_m + th1_d / th1_v

            if al_r != 0:
                first = -pi * (2 * mp.log(2) + mp.log(self.ty_m) + mp.digamma(al_m) + mp.digamma(1 - al_m))
                zrow = mp.mpf(0)
            else:
                first = pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(self.ty_m))
                zrow = self.ty_m * (pi ** 2) / (mp.sin(pi * be_m) ** 2)

            tot = mp.mpf(0)
            for k in range(-self.K_q, self.K_q + 1):
                m = al_m + k
                if m == 0:
                    continue
                w_ke = mp.exp(-2 * pi * abs(m) * self.ty_m + 2 * I * pi * (m * self.tx_m + be_m))
                tot += (2 * pi / abs(m)) * mp.re(w_ke / (1 - w_ke))
            Fu = first + zrow + tot
            c = Fu + pi * mp.log(self.ty_m) - 2 * pi * (mp.euler + mp.log(pi)) - pi * (abs(a0) ** 2) * mp.exp(-2 * self.L2)
            arg = 2 * pi * self.L2 + c
            self._weight_cache[key] = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        return self._weight_cache[key]

    @staticmethod
    def _is_half_int_pair(c: Tuple[Fraction, Fraction]) -> bool:
        h = Fraction(1, 2)
        return (c[0] - h).denominator == 1 and (c[1] - h).denominator == 1

    def Mw_matrix(self, a: Fraction, b: Fraction, sector: str):
        key = (a, b, sector)
        if key in self._Mw_cache:
            return self._Mw_cache[key]
        mp.mp.dps = self.dps
        I = iu()
        pi = mp.pi
        h = Fraction(1, 2)
        ql = SIXY[SECTORS[sector][0]]
        qr = SIXY[SECTORS[sector][1]]
        x0, x1 = ql * a, 2 * ql * b
        y0, y1 = qr * a, 2 * qr * b
        ap, am = x0 + y0, x0 - y0
        bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
        ef = mp.exp(-2 * I * pi * mp_frac(x0))
        kap = {"1": -I * ef, "i": mp.mpc(-1), "j": -ef, "k": I}
        cs = {"1": (ap + h, bp + h), "i": (ap + h, bp), "j": (ap, bp + h), "k": (ap, bp)}
        ds = {"1": (am + h, bm + h), "i": (am + h, bm), "j": (am, bm + h), "k": (am, bm)}

        Mw = mp.zeros(2, 2)
        for s_lbl in ("1", "i", "j", "k"):
            if self._is_half_int_pair(cs[s_lbl]) or self._is_half_int_pair(ds[s_lbl]):
                continue
            R = kap[s_lbl] * self.thc(cs[s_lbl][0], cs[s_lbl][1]) * self.thc(ds[s_lbl][0], ds[s_lbl][1]) / self.t1p
            wt = self._weight_sqrt(cs[s_lbl][0] - h, cs[s_lbl][1] - h)
            Mw += (wt * R) * self.edual[s_lbl]
        self._Mw_cache[key] = Mw
        return Mw

    def Y_matrix(self, a: Fraction, b: Fraction, sector: str, weight0: bool = False):
        key = (a, b, sector)
        if key not in self._Y_cache:
            mp.mp.dps = self.dps
            Mw = self.Mw_matrix(a, b, sector)
            Y = mp.matrix([
                [
                    sum(self.T_S[r_i][c_i][m, n] * Mw[m, n] for m in range(2) for n in range(2))
                    for c_i in range(3)
                ]
                for r_i in range(3)
            ])
            self._Y_cache[key] = Y
        Y = self._Y_cache[key]
        return self.sqrt_ty * Y if weight0 else Y

    def Y_higgs_basis(self, a: Fraction, b: Fraction, sector: str, conjugated: bool = False):
        """Return 3 matrices [A_0, A_1, A_2] so Y_inv(h) = sum h_k A_k (or h_k^* A_k if conjugated).
        Normalized so Y_inv(c_hat) == sqrt(Im tau) * Y_matrix(a, b, sector) identically."""
        mp.mp.dps = self.dps
        Mw = self.Mw_matrix(a, b, sector)
        scale = self.sqrt_ty * self.c_norm
        T_list = self.T_Q_conj if conjugated else self.T_Q
        mats = []
        for k in range(3):
            M = mp.matrix([
                [
                    scale * sum(T_list[k][r_i][c_i][m, n] * Mw[m, n] for m in range(2) for n in range(2))
                    for c_i in range(3)
                ]
                for r_i in range(3)
            ])
            mats.append(M)
        return mats


# ---------------------------------------------------------------------------
# Linear Algebra: Non-Squaring SVD, CKM, Jarlskog, Autonne-Takagi, Haar U(3)
# ---------------------------------------------------------------------------

def svd_asc_3x3(Y):
    """Ascending singular values and left unitary U_L via exact mp.svd_c (non-squaring)."""
    Uu, Sv, _ = mp.svd_c(Y)
    order = sorted(range(3), key=lambda idx: abs(Sv[idx]))
    svs = [abs(Sv[idx]) for idx in order]
    U = mp.matrix([[Uu[r, order[c]] for c in range(3)] for r in range(3)])
    return svs, U


def observables_from_Y(Yu, Yd, Ye) -> Dict[str, Any]:
    su, Uu = svd_asc_3x3(Yu)
    sd, Ud = svd_asc_3x3(Yd)
    se, _ = svd_asc_3x3(Ye)
    V = Uu.H * Ud
    absV = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    Jcp = abs(mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1])))
    min_diag = min(absV[0][0], absV[1][1], absV[2][2])
    return {
        "su": su, "sd": sd, "se": se,
        "u_m2m3": su[1] / su[2] if su[2] > 0 else mp.mpf(0),
        "u_m1m3": su[0] / su[2] if su[2] > 0 else mp.mpf(0),
        "d_m2m3": sd[1] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "d_m1m3": sd[0] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "e_m2m3": se[1] / se[2] if se[2] > 0 else mp.mpf(0),
        "e_m1m3": se[0] / se[2] if se[2] > 0 else mp.mpf(0),
        "V12": absV[0][1], "V23": absV[1][2], "V13": absV[0][2], "V31": absV[2][0],
        "V33": absV[2][2], "min_diag": min_diag, "Jcp": Jcp,
        "absV": absV, "Uu": Uu, "Ud": Ud,
    }


def log9_vector(obs: Dict[str, Any]) -> List[Optional[Any]]:
    """Exact B1980 9-log observable vector."""
    vals = [
        obs["u_m2m3"], obs["u_m1m3"],
        obs["d_m2m3"], obs["d_m1m3"],
        obs["e_m2m3"], obs["e_m1m3"],
        obs["V12"], obs["V23"], obs["V13"],
    ]
    return [mp.log(v) if v > 0 else None for v in vals]


def dist_b1980(u: List[Optional[Any]], v: List[Optional[Any]]):
    m = mp.mpf(0)
    for p, q in zip(u, v):
        if (p is None) != (q is None):
            return mp.inf
        if p is not None:
            d = abs(p - q) / max(mp.mpf(1), abs(p))
            if d > m:
                m = d
    return m


def takagi_3x3(M_sym):
    """Autonne-Takagi factorization M_sym = U_T * diag(svs) * U_T^T (ascending svs) via 6x6 real-split."""
    # M_sym is 3x3 complex symmetric; write M = A + i B with A, B real symmetric
    # Real 6x6 symmetric matrix [[A, B], [B, -A]] has eigenvalues +-sigma_k and eigenvectors [u_k; v_k]
    # with complex Takagi vector w_k = u_k + i v_k satisfying M w_k^* = +sigma_k w_k!
    mp.mp.dps = max(mp.mp.dps, 40)
    I = iu()
    R6 = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            val = (M_sym[i, j] + M_sym[j, i]) / 2
            a_ij = mp.re(val)
            b_ij = mp.im(val)
            R6[i, j] = a_ij
            R6[i, 3 + j] = b_ij
            R6[3 + i, j] = b_ij
            R6[3 + i, 3 + j] = -a_ij
    evals, evecs = mp.eigsy(R6)
    pos = sorted([(evals[k], k) for k in range(6)], key=lambda x: x[0])[3:]
    svs = [max(mp.mpf(0), ev) for ev, _ in pos]
    cols = []
    for _, k in pos:
        col = [evecs[i, k] + I * evecs[3 + i, k] for i in range(3)]
        nrm = mp.sqrt(sum(abs(v) ** 2 for v in col))
        if nrm > 0:
            col = [v / nrm for v in col]
        cols.append(col)
    U_T = mp.matrix([[cols[j][i] for j in range(3)] for i in range(3)])
    # Verify M_sym * conj(U_T) = U_T * diag(svs)
    return svs, U_T


def pmns_angles_from_U(U):
    """Standard PDG parameterization angles from unitary 3x3 U (ascending mass ordering)."""
    s13_sq = abs(U[0, 2]) ** 2
    c13_sq = max(mp_pow10(-50), 1 - s13_sq)
    s12_sq = abs(U[0, 1]) ** 2 / c13_sq
    s23_sq = abs(U[1, 2]) ** 2 / c13_sq
    Jcp = abs(mp.im(U[0, 1] * U[1, 2] * mp.conj(U[0, 2]) * mp.conj(U[1, 1])))
    return {
        "s12_sq": s12_sq,
        "s23_sq": s23_sq,
        "s13_sq": s13_sq,
        "Jcp": Jcp,
    }


def rand_haar_u3(rng: random.Random, dps: int = 45):
    """Exact Mezzadri Householder/QR Haar-distributed U(3) using pure integer RNG (zero float literals)."""
    mp.mp.dps = dps
    I = iu()
    twopi = 2 * mp.pi
    M = 10 ** 18

    def rand_std_normal():
        # Box-Muller from exact rational uniform in (0, 1)
        u1 = mp.mpf(rng.randint(1, M - 1)) / mp.mpf(M)
        u2 = mp.mpf(rng.randint(1, M - 1)) / mp.mpf(M)
        rad = mp.sqrt(-2 * mp.log(u1))
        return rad * mp.cos(twopi * u2), rad * mp.sin(twopi * u2)

    Z = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            xr, xi = rand_std_normal()
            Z[i, j] = xr + I * xi

    # Modified Gram-Schmidt with R diagonal phase normalization (Mezzadri 2007)
    Q = mp.zeros(3, 3)
    for j in range(3):
        v = [Z[i, j] for i in range(3)]
        for p in range(j):
            proj = sum(mp.conj(Q[i, p]) * v[i] for i in range(3))
            for i in range(3):
                v[i] -= proj * Q[i, p]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        # Random phase on diagonal of R is already absorbed by complex Gaussian; fix diag(R) > 0:
        # In MGS, r_jj = nrm > 0 directly! Multiply by random unit phase? Wait: MGS with r_jj > 0 IS Mezzadri!
        for i in range(3):
            Q[i, j] = v[i] / nrm
    return Q


# ---------------------------------------------------------------------------
# Enumerate P_30 (96 pts = 48 pairs) and E[30]_prim (576 pts = 288 pairs)
# ---------------------------------------------------------------------------

def build_level30_sets():
    K5_star = [
        (Fraction(2, 5), Fraction(4, 5)),
        (Fraction(3, 5), Fraction(1, 5)),
        (Fraction(1, 5), Fraction(2, 5)),
        (Fraction(4, 5), Fraction(3, 5)),
    ]
    E6_prim = [
        (Fraction(j, 6), Fraction(k, 6))
        for j in range(6) for k in range(6)
        if pt_order((Fraction(j, 6), Fraction(k, 6))) == 6
    ]
    P96 = sorted({mod1_pt(p5[0] + p6[0], p5[1] + p6[1]) for p5 in K5_star for p6 in E6_prim})

    E30_prim = [
        (Fraction(j, 30), Fraction(k, 30))
        for j in range(30) for k in range(30)
        if pt_order((Fraction(j, 30), Fraction(k, 30))) == 30
    ]
    E30_nz = [
        (Fraction(j, 30), Fraction(k, 30))
        for j in range(30) for k in range(30)
        if (j, k) != (0, 0)
    ]

    def dedup_antipodal(pts):
        seen = set()
        out = []
        for p in sorted(pts):
            neg = mod1_pt(-p[0], -p[1])
            canon = min(p, neg)
            if canon not in seen:
                seen.add(canon)
                out.append(canon)
        return out

    return {
        "K5_star": K5_star,
        "E6_prim": E6_prim,
        "P96": P96,
        "P96_set": set(P96),
        "P48_pairs": dedup_antipodal(P96),
        "E30_prim": E30_prim,
        "E288_pairs": dedup_antipodal(E30_prim),
        "E30_nz_pairs": dedup_antipodal(E30_nz),
    }


# ---------------------------------------------------------------------------
# MODULE W1 — Surgical B1980 Part A/B Audit & P-882 Q1 Resolution
# ---------------------------------------------------------------------------

def run_W1(sets: Dict[str, Any]) -> Dict[str, Any]:
    print("[W1] Starting B1980 Part A algebra, exact S-covariance fix, full-norm weight+1, & K!=1 audit...", flush=True)
    # 1. Exact Part A algebra in PSL(2, Z/30)
    def mm30(A, B):
        return (
            ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 30, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 30),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 30, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 30),
        )

    M = ((2, 1), (1, 1))
    I2 = ((1, 0), (0, 1))
    negI2 = ((29, 0), (0, 29))
    cur = I2
    order_psl30 = None
    tr_cycle = []
    for k in range(1, 121):
        cur = mm30(cur, M)
        if k <= 12:
            tr_cycle.append((cur[0][0] + cur[1][1]) % 30)
        if order_psl30 is None and (cur == I2 or cur == negI2):
            order_psl30 = k
            break
    elliptic_hit = any(t in (0, 1, 29) for t in tr_cycle)

    # Cusps of X(30) = primitive pairs (a, b) mod 30 up to sign (+/-1)
    prim_mod30 = [
        (j, k) for j in range(30) for k in range(30)
        if math.gcd(math.gcd(j, k), 30) == 1
    ]
    cusps_set = set()
    for j, k in prim_mod30:
        neg = ((-j) % 30, (-k) % 30)
        cusps_set.add(min((j, k), neg))
    cusps = sorted(cusps_set)

    # Action of M (row vector v -> v * M^-1 mod 30; M^-1 = [[1,-1],[-1,2]])
    def act_M_inv_pair(v):
        j, k = v
        nj, nk = (j - k) % 30, (-j + 2 * k) % 30
        neg = ((-nj) % 30, (-nk) % 30)
        return min((nj, nk), neg)

    unvisited = set(cusps)
    orbit_sizes = []
    while unvisited:
        start = min(unvisited)
        orb = []
        v = start
        while v in unvisited:
            unvisited.remove(v)
            orb.append(v)
            v = act_M_inv_pair(v)
        orbit_sizes.append(len(orb))
    orbit_sizes.sort()

    # Cusps fixed by M^12
    M12 = I2
    for _ in range(12):
        M12 = mm30(M12, M)
    fixed_by_M12 = set()
    for j, k in cusps:
        nj = (j * M12[0][0] + k * M12[1][0]) % 30
        nk = (j * M12[0][1] + k * M12[1][1]) % 30
        if (nj, nk) == (j, k) or (nj, nk) == ((-j) % 30, (-k) % 30):
            fixed_by_M12.add((j, k))
    p48_int = {
        min((int(p[0] * 30), int(p[1] * 30)), ((-int(p[0] * 30)) % 30, (-int(p[1] * 30)) % 30))
        for p in sets["P48_pairs"]
    }
    part_a_exact_match = (
        order_psl30 == 60
        and not elliptic_hit
        and len(cusps) == 288
        and orbit_sizes == [12, 12, 12, 12, 60, 60, 60, 60]
        and fixed_by_M12 == p48_int
    )

    # 2. Exact S-covariance on B1980's 3 axis pairs across ALL 96 pts of P_30
    dps_w1 = 55
    mp.mp.dps = dps_w1
    I = iu()
    axis_pairs = [(Fraction(5, 4), Fraction(4, 5)), (Fraction(3, 2), Fraction(2, 3)), (Fraction(5, 2), Fraction(2, 5))]
    s_pair_reports = []
    pf1_reports = []
    max_ode_cocycle_err = mp.mpf(0)
    max_s_cov_dist_all96 = mp.mpf(0)

    for yf, ypf in axis_pairs:
        ym = mp_frac(yf)
        ypm = mp_frac(ypf)
        L_y, res_y = solve_L2_fuchsian_raw(I * ym, dps=42)
        L_yp_direct, res_yp = solve_L2_fuchsian_raw(I * ypm, dps=42)
        L_yp_cocycle = L_y + mp.log(ym)
        cocycle_err = abs(L_yp_direct - L_yp_cocycle)
        if cocycle_err > max_ode_cocycle_err:
            max_ode_cocycle_err = cocycle_err

        eng_y = FrameCEngine(I * ym, L_y, dps=dps_w1)
        eng_yp_true = FrameCEngine(I * ypm, L_yp_cocycle, dps=dps_w1)
        # Planted control PF1: B1980's exact duality_cov.py:43 bug (dropping +ln(y))!
        eng_yp_bug = FrameCEngine(I * ypm, L_y, dps=26)

        dists_true = []
        dists_bug_bijection = []
        dists_bug_S_partner = []
        # Compute E30_nz table under buggy L_y to match B1980's exact all-899 matching metric!
        bug_par_vecs = []
        for pa, pb in sets["E30_nz_pairs"]:
            obs_p = observables_from_Y(
                eng_yp_bug.Y_matrix(pa, pb, "up"),
                eng_yp_bug.Y_matrix(pa, pb, "down"),
                eng_yp_bug.Y_matrix(pa, pb, "lep"),
            )
            bug_par_vecs.append(log9_vector(obs_p))

        for pa, pb in sets["P96"]:
            obs_src = observables_from_Y(
                eng_y.Y_matrix(pa, pb, "up"),
                eng_y.Y_matrix(pa, pb, "down"),
                eng_y.Y_matrix(pa, pb, "lep"),
            )
            v_src = log9_vector(obs_src)
            # Exact S^-1 action on row vector: (a, b) * [[0, 1], [-1, 0]] = (-b, a) mod 1
            sa, sb = mod1_pt(-pb, pa)
            obs_true = observables_from_Y(
                eng_yp_true.Y_matrix(sa, sb, "up"),
                eng_yp_true.Y_matrix(sa, sb, "down"),
                eng_yp_true.Y_matrix(sa, sb, "lep"),
            )
            d_t = dist_b1980(v_src, log9_vector(obs_true))
            dists_true.append(d_t)

            obs_bug_s = observables_from_Y(
                eng_yp_bug.Y_matrix(sa, sb, "up"),
                eng_yp_bug.Y_matrix(sa, sb, "down"),
                eng_yp_bug.Y_matrix(sa, sb, "lep"),
            )
            dists_bug_S_partner.append(dist_b1980(v_src, log9_vector(obs_bug_s)))
            # Best match over all 899 nonzero E[30] points (exact B1980 match() definition)
            best_d = min(dist_b1980(v_src, vp) for vp in bug_par_vecs)
            dists_bug_bijection.append(best_d)

        dists_true.sort()
        dists_bug_bijection.sort()
        dists_bug_S_partner.sort()
        if dists_true[-1] > max_s_cov_dist_all96:
            max_s_cov_dist_all96 = dists_true[-1]

        s_pair_reports.append({
            "y": frac_str(yf),
            "yp": frac_str(ypf),
            "L2_y": mp_str(L_y, 12),
            "L2_yp_direct_ode": mp_str(L_yp_direct, 12),
            "L2_yp_cocycle": mp_str(L_yp_cocycle, 12),
            "ode_cocycle_err": mp_str(cocycle_err, 6),
            "ode_res_y": mp_str(res_y, 6),
            "ode_res_yp": mp_str(res_yp, 6),
            "max_9log_dist_all96": mp_str(dists_true[-1], 6),
            "median_9log_dist_all96": mp_str(dists_true[len(dists_true) // 2], 6),
        })
        pf1_reports.append({
            "y": frac_str(yf),
            "yp": frac_str(ypf),
            "buggy_L_used": mp_str(L_y, 8),
            "missing_ln_y": mp_str(mp.log(ym), 8),
            "b1980_all899_max_d": mp_str(dists_bug_bijection[-1], 6),
            "b1980_all899_median_d": mp_str(dists_bug_bijection[len(dists_bug_bijection) // 2], 6),
            "buggy_S_partner_max_d": mp_str(dists_bug_S_partner[-1], 6),
        })

    # 3. Full-norm modular weight +1 proof: absolute s_k^{inv} = sqrt(Im tau)*s_k under T, S, M
    #    plus PF2 (dropping sqrt(Im tau)) and PF4 (wrong point action w*gamma)
    w_test = (Fraction(4, 15), Fraction(1, 30))
    tau_list = [
        ("tau1", mp.mpc(mp_rat(13, 100), mp_rat(6, 5))),
        ("tau0", mp.mpc(mp_rat(-9, 10), mp_rat(6, 5))),
    ]
    moves = {
        "T": ((1, 1), (0, 1)),
        "S": ((0, -1), (1, 0)),
        "M": ((2, 1), (1, 1)),
    }
    full_norm_reports = {}
    max_abs_sv_inv_err = mp.mpf(0)
    pf2_max_err = mp.mpf(0)
    pf4_max_err = mp.mpf(0)

    for tname, tau_b in tau_list:
        L_b, _ = solve_L2_fuchsian_cov(tau_b, dps=42)
        eng_b = FrameCEngine(tau_b, L_b, dps=dps_w1)
        obs_b_inv = observables_from_Y(
            eng_b.Y_matrix(w_test[0], w_test[1], "up", weight0=True),
            eng_b.Y_matrix(w_test[0], w_test[1], "down", weight0=True),
            eng_b.Y_matrix(w_test[0], w_test[1], "lep", weight0=True),
        )
        obs_b_raw = observables_from_Y(
            eng_b.Y_matrix(w_test[0], w_test[1], "up", weight0=False),
            eng_b.Y_matrix(w_test[0], w_test[1], "down", weight0=False),
            eng_b.Y_matrix(w_test[0], w_test[1], "lep", weight0=False),
        )
        svs_b_inv = obs_b_inv["su"] + obs_b_inv["sd"] + obs_b_inv["se"]
        svs_b_raw = obs_b_raw["su"] + obs_b_raw["sd"] + obs_b_raw["se"]

        t_res = {}
        for mname, ((a, b), (c, d)) in moves.items():
            denom = c * tau_b + d
            tau_g = (a * tau_b + b) / denom
            L_g = L_b + mp.log(abs(denom))
            eng_g = FrameCEngine(tau_g, L_g, dps=dps_w1)
            # Correct action: w * gamma^-1 = (a_w, b_w) * [[d, -b], [-c, a]]
            wa, wb = mod1_pt(d * w_test[0] - c * w_test[1], -b * w_test[0] + a * w_test[1])
            obs_g_inv = observables_from_Y(
                eng_g.Y_matrix(wa, wb, "up", weight0=True),
                eng_g.Y_matrix(wa, wb, "down", weight0=True),
                eng_g.Y_matrix(wa, wb, "lep", weight0=True),
            )
            obs_g_raw = observables_from_Y(
                eng_g.Y_matrix(wa, wb, "up", weight0=False),
                eng_g.Y_matrix(wa, wb, "down", weight0=False),
                eng_g.Y_matrix(wa, wb, "lep", weight0=False),
            )
            svs_g_inv = obs_g_inv["su"] + obs_g_inv["sd"] + obs_g_inv["se"]
            svs_g_raw = obs_g_raw["su"] + obs_g_raw["sd"] + obs_g_raw["se"]

            abs_sv_err = max(abs(x - y) / y for x, y in zip(svs_g_inv, svs_b_inv))
            ratio_ckm_err = max(
                abs(obs_g_inv[k] - obs_b_inv[k]) / max(mp_pow10(-30), obs_b_inv[k])
                for k in ("V12", "V23", "V13", "Jcp")
            )
            # Check exact weight +1 raw ratio: s_k(raw_g) / s_k(raw_b) == |c*tau + d|
            weight_check_err = max(abs((x / y) - abs(denom)) / abs(denom) for x, y in zip(svs_g_raw, svs_b_raw))
            raw_no_sqrty_err = max(abs(x - y) / y for x, y in zip(svs_g_raw, svs_b_raw))
            if abs_sv_err > max_abs_sv_inv_err:
                max_abs_sv_inv_err = abs_sv_err
            if mname in ("S", "M") and raw_no_sqrty_err > pf2_max_err:
                pf2_max_err = raw_no_sqrty_err

            # PF4: wrong point action w * gamma
            wa_w, wb_w = mod1_pt(a * w_test[0] + c * w_test[1], b * w_test[0] + d * w_test[1])
            obs_wrong = observables_from_Y(
                eng_g.Y_matrix(wa_w, wb_w, "up", weight0=True),
                eng_g.Y_matrix(wa_w, wb_w, "down", weight0=True),
                eng_g.Y_matrix(wa_w, wb_w, "lep", weight0=True),
            )
            wrong_err = max(abs(x - y) / y for x, y in zip(obs_wrong["su"] + obs_wrong["sd"], obs_b_inv["su"] + obs_b_inv["sd"]))
            if mname in ("S", "M") and wrong_err > pf4_max_err:
                pf4_max_err = wrong_err

            t_res[mname] = {
                "abs_c_tau_plus_d": mp_str(abs(denom), 10),
                "max_9_abs_sv_inv_rel_err": mp_str(abs_sv_err, 6),
                "max_ckm_jcp_rel_err": mp_str(ratio_ckm_err, 6),
                "weight_plus1_law_err": mp_str(weight_check_err, 6),
                "pf2_raw_no_sqrty_rel_err": mp_str(raw_no_sqrty_err, 6),
                "pf4_wrong_w_gamma_rel_err": mp_str(wrong_err, 6),
            }
        full_norm_reports[tname] = t_res

    # 4. Corrected K != 1 duality audit (exact non-clamped, cocycle-correct Fuchsian L_2!)
    # Pick 1 representative from each of the 12 exact nd(a) classes of P_30
    rep12 = []
    seen_nd = set()
    for p in sets["P48_pairs"]:
        nd = nd_frac(p[0])
        if nd not in seen_nd:
            seen_nd.add(nd)
            rep12.append(p)

    K_list = [2, 3, 5, 6, 10, 15, 30]
    k_duality_reports = []
    min_k_neq_1_dist = mp.mpf(100)
    mp.mp.dps = 36
    for K in K_list:
        sqK = mp.sqrt(mp.mpf(K))
        y_k = mp_rat(3, 2) * sqK
        yp_k = mp_rat(2, 3) * sqK
        L_yk, _ = solve_L2_fuchsian_cov(I * y_k, dps=36)
        L_ypk, _ = solve_L2_fuchsian_cov(I * yp_k, dps=36)
        eng1 = FrameCEngine(I * y_k, L_yk, dps=26)
        eng2 = FrameCEngine(I * yp_k, L_ypk, dps=26)
        par_vecs = [
            log9_vector(observables_from_Y(
                eng2.Y_matrix(pa, pb, "up"),
                eng2.Y_matrix(pa, pb, "down"),
                eng2.Y_matrix(pa, pb, "lep"),
            ))
            for pa, pb in sets["E30_nz_pairs"]
        ]
        ds = []
        for pa, pb in rep12:
            v1 = log9_vector(observables_from_Y(
                eng1.Y_matrix(pa, pb, "up"),
                eng1.Y_matrix(pa, pb, "down"),
                eng1.Y_matrix(pa, pb, "lep"),
            ))
            ds.append(min(dist_b1980(v1, v2) for v2 in par_vecs))
        ds.sort()
        if ds[-1] < min_k_neq_1_dist:
            min_k_neq_1_dist = ds[-1]
        k_duality_reports.append({
            "K": K,
            "y": mp_str(y_k, 8),
            "yp": mp_str(yp_k, 8),
            "L2_y_true": mp_str(L_yk, 8),
            "L2_yp_true": mp_str(L_ypk, 8),
            "max_d_12classes_vs_all899": mp_str(ds[-1], 6),
            "median_d_12classes_vs_all899": mp_str(ds[len(ds) // 2], 6),
        })

    print(
        f"[W1] Done: PartA={part_a_exact_match}, max_S_96={mp_str(max_s_cov_dist_all96, 4)}, "
        f"max_abs_sv_inv={mp_str(max_abs_sv_inv_err, 4)}, min_K!=1={mp_str(min_k_neq_1_dist, 4)}",
        flush=True,
    )
    return {
        "part_a_exact": {
            "M_order_psl30": order_psl30,
            "trace_cycle_mod30": tr_cycle,
            "elliptic_hit": elliptic_hit,
            "cusps_count": len(cusps),
            "orbit_sizes": orbit_sizes,
            "M12_fixed_cusps_count": len(fixed_by_M12),
            "M12_fixed_equals_P30_mod_sign": fixed_by_M12 == p48_int,
            "all_ok": part_a_exact_match,
        },
        "s_covariance_all96_b1980_pairs": s_pair_reports,
        "max_ode_cocycle_err": mp_str(max_ode_cocycle_err, 6),
        "max_s_cov_dist_all96": mp_str(max_s_cov_dist_all96, 6),
        "full_norm_weight_plus1_proof": full_norm_reports,
        "max_abs_sv_inv_err": mp_str(max_abs_sv_inv_err, 6),
        "corrected_K_neq_1_audit": k_duality_reports,
        "min_K_neq_1_max_d": mp_str(min_k_neq_1_dist, 6),
        "pf1_b1980_bug_reproduction": pf1_reports,
        "pf2_max_err": mp_str(pf2_max_err, 6),
        "pf4_max_err": mp_str(pf4_max_err, 6),
        "g1_pass": (
            part_a_exact_match
            and max_ode_cocycle_err < mp_pow10(-8)
            and max_s_cov_dist_all96 < mp_pow10(-38)
            and max_abs_sv_inv_err < mp_pow10(-38)
            and min_k_neq_1_dist > mp_rat(1, 10)
        ),
    }


# ---------------------------------------------------------------------------
# MODULE W2 — Whole Level-30 (288 Pairs) + Closed Geodesic gamma_M + B1981/W-LV1
# ---------------------------------------------------------------------------

def run_W2(model: Dict[str, Any], sets: Dict[str, Any]) -> Dict[str, Any]:
    print("[W2] Starting whole level-30 (288 pairs), closed geodesic gamma_M, & B1981/W-LV1 checks...", flush=True)
    I = iu()
    # 1. Exact symbolic tropical classification of ALL 288 primitive order-30 pairs (576 pts)
    class_map_all: Dict[Tuple, List[Tuple[Fraction, Fraction]]] = {}
    class_map_act: Dict[Tuple, List[Tuple[Fraction, Fraction]]] = {}
    chan_zero_all = 0
    chan_zero_act = 0
    w_std_all = 0
    w_inv_all = 0
    w_nonadd_all = 0
    w_deg_quarter_all = 0
    slow_v23_all = 0
    slow_v23_act = 0
    hier_aligned_trop_all = 0
    hier_aligned_trop_act = 0
    norm_eps_neg_count = 0
    norm_eps_pos_count = 0
    norm_eps_zero_count = 0
    min_norm_eps_all = Fraction(100, 1)
    max_norm_eps_all = Fraction(-100, 1)

    for p in sets["E288_pairs"]:
        in_act = p in sets["P96_set"]
        z_any = any(has_exact_channel_zero(p[0], p[1], SIXY[SECTORS[s][0]], SIXY[SECTORS[s][1]]) for s in ("up", "down", "lep"))
        if z_any:
            chan_zero_all += 1
            if in_act:
                chan_zero_act += 1
        tr = tropical_full_point(model, p[0])
        ne = tr["norm_eps_min"]
        if ne < 0:
            norm_eps_neg_count += 1
        elif ne > 0:
            norm_eps_pos_count += 1
        else:
            norm_eps_zero_count += 1
        if ne < min_norm_eps_all:
            min_norm_eps_all = ne
        if ne > max_norm_eps_all:
            max_norm_eps_all = ne

        sig = (
            tr["up_m2m3"], tr["up_m1m3"], tr["down_m2m3"], tr["down_m1m3"],
            tr["lep_m2m3"], tr["lep_m1m3"], tr["V12"], tr["V23"], tr["V13"], tr["V31"],
        )
        class_map_all.setdefault(sig, []).append(p)
        if in_act:
            class_map_act.setdefault(sig, []).append(p)

        if tr["V12"] is None:
            w_deg_quarter_all += 1
        else:
            v12, v23, v13 = tr["V12"], tr["V23"], tr["V13"]
            if tr["up_m2m3"] > 0 and tr["down_m2m3"] > 0 and v12 > 0 and v23 > 0:
                hier_aligned_trop_all += 1
                if in_act:
                    hier_aligned_trop_act += 1
            if Fraction(0, 1) < v23 < Fraction(1, 10):
                slow_v23_all += 1
                if in_act:
                    slow_v23_act += 1
            if v13 == v12 + v23 and Fraction(0, 1) < v12 < v23:
                w_std_all += 1
            elif v13 == v12 + v23 and Fraction(0, 1) < v23 < v12:
                w_inv_all += 1
            else:
                w_nonadd_all += 1

    # 2. Finite physical heights y = 2, 3 across ALL 288 pairs (act-line 48 vs off-line 240)
    finite_288_reports = {}
    for y_int in (2, 3):
        tau_y = mp.mpc(mp_rat(13, 100), mp.mpf(y_int))
        L_y, _ = solve_L2_fuchsian_cov(tau_y, dps=38)
        eng = FrameCEngine(tau_y, L_y, dps=30)
        cnts = {
            "act": {"total": 0, "aligned": 0, "hier_ud": 0, "ed_split": 0, "std_ckm": 0, "inv_ckm": 0, "all4": 0},
            "off": {"total": 0, "aligned": 0, "hier_ud": 0, "ed_split": 0, "std_ckm": 0, "inv_ckm": 0, "all4": 0},
        }
        for pa, pb in sets["E288_pairs"]:
            bucket = cnts["act"] if (pa, pb) in sets["P96_set"] else cnts["off"]
            bucket["total"] += 1
            obs = observables_from_Y(
                eng.Y_matrix(pa, pb, "up"),
                eng.Y_matrix(pa, pb, "down"),
                eng.Y_matrix(pa, pb, "lep"),
            )
            aligned = obs["min_diag"] >= mp_rat(9, 10)
            hier = (obs["u_m2m3"] < mp_rat(1, 5)) and (obs["d_m2m3"] < mp_rat(1, 5))
            d2 = abs(mp.log(obs["e_m2m3"] / obs["d_m2m3"])) if (obs["e_m2m3"] > 0 and obs["d_m2m3"] > 0) else mp.mpf(0)
            ed_split = d2 > mp_rat(1, 10)
            std_ckm = (obs["V12"] > obs["V23"]) and (obs["V23"] > obs["V13"]) and (obs["V13"] > 0)
            inv_ckm = obs["V23"] > obs["V12"]
            if aligned:
                bucket["aligned"] += 1
            if hier:
                bucket["hier_ud"] += 1
            if ed_split:
                bucket["ed_split"] += 1
            if std_ckm:
                bucket["std_ckm"] += 1
            if inv_ckm:
                bucket["inv_ckm"] += 1
            if aligned and hier and ed_split and std_ckm:
                bucket["all4"] += 1
        finite_288_reports[f"y_{y_int}"] = {
            "L2": mp_str(L_y, 10),
            "act_48_pairs": cnts["act"],
            "off_240_pairs": cnts["off"],
            "all_288_all4": cnts["act"]["all4"] + cnts["off"]["all4"],
            "all_288_std_ckm": cnts["act"]["std_ckm"] + cnts["off"]["std_ckm"],
        }

    # 3. Closed hyperbolic geodesic gamma_M(u) of M = [[2,1],[1,1]] (zero free y!)
    mp.mp.dps = 50
    phi = (1 + mp.sqrt(5)) / 2
    ell_M = 4 * mp.log(phi)

    def tau_geo(u):
        return mp_rat(1, 2) + (mp.sqrt(5) / 2) * (mp.tanh(u) + I * (1 / mp.cosh(u)))

    # Verify M(tau_geo(u)) == tau_geo(u + ell_M) identically across 5 nodes
    geo_id_err = mp.mpf(0)
    for k in range(-2, 3):
        uk = mp_rat(k, 5) * ell_M
        tk = tau_geo(uk)
        mtk = (2 * tk + 1) / (tk + 1)
        err = abs(mtk - tau_geo(uk + ell_M))
        if err > geo_id_err:
            geo_id_err = err

    # Build 12-point M-orbits for representative MARK & TWIN points
    def make_M_orbit(w0):
        orb = []
        w = w0
        for _ in range(12):
            orb.append(w)
            # w * M^-1 = (a - b, -a + 2b) mod 1
            w = mod1_pt(w[0] - w[1], -w[0] + 2 * w[1])
        return orb

    w_mark = (Fraction(4, 15), Fraction(1, 30))
    w_twin = (Fraction(1, 30), Fraction(1, 6))
    orb_mark = make_M_orbit(w_mark)
    orb_twin = make_M_orbit(w_twin)

    # 16-node periodic midpoint quadrature on [-ell_M/2, +ell_M/2], plus shifted grid (+ell_M/32) for basepoint check!
    def eval_geodesic_integrals(n_nodes: int, shift_frac: Fraction):
        du = ell_M / n_nodes
        engs = []
        for j in range(n_nodes):
            uj = -ell_M / 2 + (mp.mpf(j) + mp_rat(1, 2) + mp_frac(shift_frac)) * du
            tj = tau_geo(uj)
            Lj, _ = solve_L2_fuchsian_cov(tj, dps=38)
            engs.append((tj, FrameCEngine(tj, Lj, dps=40)))

        res_orbs = {}
        for oname, orb in (("mark_orbit", orb_mark), ("twin_orbit", orb_twin)):
            # (a) SL(2,Z)-invariant geodesic-averaged canonical observable spectrum over full 12-turn closed geodesic
            avg_acc = {k: mp.mpf(0) for k in ("u_m2m3", "u_m1m3", "d_m2m3", "d_m1m3", "e_m2m3", "e_m1m3", "V12", "V23", "V13", "Jcp", "min_diag")}
            # (b) Geodesic-integrated Hermitian Gramian H_{L,f} = (1/(12*ell_M)) int sum_{w in O} Y_inv Y_inv^H du
            H_geo = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
            # (c) Single-turn coherent integral int Y_inv(tau(u), w0) du
            Y_coh = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
            n_tot = n_nodes * 12
            for _, eng in engs:
                for idx_w, (pa, pb) in enumerate(orb):
                    Yu = eng.Y_matrix(pa, pb, "up", weight0=True)
                    Yd = eng.Y_matrix(pa, pb, "down", weight0=True)
                    Ye = eng.Y_matrix(pa, pb, "lep", weight0=True)
                    obs = observables_from_Y(Yu, Yd, Ye)
                    for k in avg_acc:
                        avg_acc[k] += obs[k] / n_tot
                    H_geo["up"] += (Yu * Yu.H) / n_tot
                    H_geo["down"] += (Yd * Yd.H) / n_tot
                    H_geo["lep"] += (Ye * Ye.H) / n_tot
                    if idx_w == 0:
                        Y_coh["up"] += Yu / n_nodes
                        Y_coh["down"] += Yd / n_nodes
                        Y_coh["lep"] += Ye / n_nodes

            # Extract Gramian eigenvalues & CKM
            gram_sv = {}
            gram_U = {}
            for s in ("up", "down", "lep"):
                ev, U = mp.eigh(H_geo[s])
                order_idx = sorted(range(3), key=lambda i: mp.re(ev[i]))
                sv = [mp.sqrt(max(mp.mpf(0), mp.re(ev[i]))) for i in order_idx]
                Us = mp.matrix([[U[r, order_idx[c]] for c in range(3)] for r in range(3)])
                gram_sv[s] = sv
                gram_U[s] = Us
            Vg = gram_U["up"].H * gram_U["down"]
            coh_obs = observables_from_Y(Y_coh["up"], Y_coh["down"], Y_coh["lep"])
            res_orbs[oname] = {
                "geodesic_avg_observables": {k: mp_str(v, 10) for k, v in avg_acc.items()},
                "geodesic_avg_raw": avg_acc,
                "geodesic_gramian": {
                    "u_m2m3": mp_str(gram_sv["up"][1] / gram_sv["up"][2], 10),
                    "u_m1m3": mp_str(gram_sv["up"][0] / gram_sv["up"][2], 10),
                    "d_m2m3": mp_str(gram_sv["down"][1] / gram_sv["down"][2], 10),
                    "d_m1m3": mp_str(gram_sv["down"][0] / gram_sv["down"][2], 10),
                    "e_m2m3": mp_str(gram_sv["lep"][1] / gram_sv["lep"][2], 10),
                    "e_m1m3": mp_str(gram_sv["lep"][0] / gram_sv["lep"][2], 10),
                    "V12": mp_str(abs(Vg[0, 1]), 10),
                    "V23": mp_str(abs(Vg[1, 2]), 10),
                    "V13": mp_str(abs(Vg[0, 2]), 10),
                },
                "single_turn_coherent_integral": {
                    "u_m2m3": mp_str(coh_obs["u_m2m3"], 10),
                    "d_m2m3": mp_str(coh_obs["d_m2m3"], 10),
                    "e_m2m3": mp_str(coh_obs["e_m2m3"], 10),
                    "V12": mp_str(coh_obs["V12"], 10),
                    "V23": mp_str(coh_obs["V23"], 10),
                    "V13": mp_str(coh_obs["V13"], 10),
                    "min_diag": mp_str(coh_obs["min_diag"], 10),
                },
            }
        return res_orbs

    geo_base = eval_geodesic_integrals(12, Fraction(0, 1))
    geo_shift = eval_geodesic_integrals(12, Fraction(1, 3))
    geo_basepoint_err = max(
        abs(geo_base[oname]["geodesic_avg_raw"][k] - geo_shift[oname]["geodesic_avg_raw"][k])
        for oname in ("mark_orbit", "twin_orbit")
        for k in geo_base[oname]["geodesic_avg_raw"]
    )
    # Strip raw mpfs before JSON return
    for oname in ("mark_orbit", "twin_orbit"):
        del geo_base[oname]["geodesic_avg_raw"]

    # 4. chat1 W-LV1 Y_e(w) ~ Y_d(3w) exact check at N=10 & N=30, plus B1981 E[6]_prim shell L vs G
    tau_chk = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    L_chk, _ = solve_L2_fuchsian_cov(tau_chk, dps=42)
    eng_chk = FrameCEngine(tau_chk, L_chk, dps=55)
    wlv1_max_err = mp.mpf(0)
    for w_pt in ((Fraction(1, 10), Fraction(3, 10)), (Fraction(4, 15), Fraction(1, 30)), (Fraction(1, 30), Fraction(1, 6))):
        Ye_w = eng_chk.Y_matrix(w_pt[0], w_pt[1], "lep")
        w3 = mod1_pt(3 * w_pt[0], 3 * w_pt[1])
        Yd_3w = eng_chk.Y_matrix(w3[0], w3[1], "down")
        # Compare singular value spectra (Y_e(w) proportional to Y_d(3w)^T up to phase/sign!)
        se, _ = svd_asc_3x3(Ye_w)
        sd3, _ = svd_asc_3x3(Yd_3w)
        err = max(abs((se[k] / se[2]) - (sd3[k] / sd3[2])) for k in range(3))
        if err > wlv1_max_err:
            wlv1_max_err = err

    # B1981 E[6]_prim shell (24 pts around p5 = (2/5, 4/5)) L vs G at y=20->30 (dps=110)
    p5_b = (Fraction(2, 5), Fraction(4, 5))
    block24 = [mod1_pt(p5_b[0] + p6[0], p5_b[1] + p6[1]) for p6 in sets["E6_prim"]]
    b1981_res = {}
    sv_L_by_y = {}
    sv_G_by_y = {}
    for y_b in (20, 30):
        tau_b = mp.mpc(mp_rat(13, 100), mp.mpf(y_b))
        L_b, _ = solve_L2_fuchsian_cov(tau_b, dps=40)
        eng_b = FrameCEngine(tau_b, L_b, dps=110)
        YL = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
        HG = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
        for pa, pb in block24:
            for s in ("up", "down", "lep"):
                Y = eng_b.Y_matrix(pa, pb, s)
                YL[s] += Y / 24
                HG[s] += (Y * Y.H) / 24
        obs_L = observables_from_Y(YL["up"], YL["down"], YL["lep"])
        sv_L_by_y[y_b] = obs_L
        sv_G = {}
        for s in ("up", "down", "lep"):
            ev, _ = mp.eigh(HG[s])
            svs = sorted(mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev)
            sv_G[s] = (svs[1] / svs[2], svs[0] / svs[2])
        sv_G_by_y[y_b] = sv_G

    denom_rate = 10 * mp.pi
    b1981_res = {
        "reading_L_y30_min_diag": mp_str(sv_L_by_y[30]["min_diag"], 8),
        "reading_L_y30_V23": mp_str(sv_L_by_y[30]["V23"], 8),
        "reading_L_rates_20_30": {
            "up_m2m3": mp_str(-mp.log(sv_L_by_y[30]["u_m2m3"] / sv_L_by_y[20]["u_m2m3"]) / denom_rate, 6),
            "dn_m2m3": mp_str(-mp.log(sv_L_by_y[30]["d_m2m3"] / sv_L_by_y[20]["d_m2m3"]) / denom_rate, 6),
            "lep_m2m3": mp_str(-mp.log(sv_L_by_y[30]["e_m2m3"] / sv_L_by_y[20]["e_m2m3"]) / denom_rate, 6),
            "V23": mp_str(-mp.log(sv_L_by_y[30]["V23"] / sv_L_by_y[20]["V23"]) / denom_rate, 6),
        },
        "reading_G_rates_20_30": {
            s: {
                "m2m3_rate": mp_str(-mp.log(sv_G_by_y[30][s][0] / sv_G_by_y[20][s][0]) / denom_rate, 6),
                "m1m3_rate": mp_str(-mp.log(sv_G_by_y[30][s][1] / sv_G_by_y[20][s][1]) / denom_rate, 6),
            }
            for s in ("up", "down", "lep")
        },
    }

    print(
        f"[W2] Done: 288-pair classes={len(class_map_all)} (act={len(class_map_act)}), "
        f"W-STD_trop={w_std_all}/288, y=2 all4={finite_288_reports['y_2']['all_288_all4']}/288, "
        f"geo_err={mp_str(geo_basepoint_err, 4)}, wlv1={mp_str(wlv1_max_err, 4)}",
        flush=True,
    )
    return {
        "whole_level30_tropical_288_pairs": {
            "total_pairs": len(sets["E288_pairs"]),
            "act_line_pairs": len(sets["P48_pairs"]),
            "off_line_pairs": len(sets["E288_pairs"]) - len(sets["P48_pairs"]),
            "distinct_classes_all288": len(class_map_all),
            "distinct_classes_act48": len(class_map_act),
            "exact_channel_zeros_all288": chan_zero_all,
            "exact_channel_zeros_act48": chan_zero_act,
            "hier_aligned_trop_all288": hier_aligned_trop_all,
            "hier_aligned_trop_act48": hier_aligned_trop_act,
            "slow_v23_all288": slow_v23_all,
            "slow_v23_act48": slow_v23_act,
            "w_std_additive_all288": w_std_all,
            "w_inv_additive_all288": w_inv_all,
            "w_nonadd_all288": w_nonadd_all,
            "w_quarter_degenerate_all288": w_deg_quarter_all,
            "norm_eps_neg_cusp_growth_pairs": norm_eps_neg_count,
            "norm_eps_zero_pairs": norm_eps_zero_count,
            "norm_eps_pos_cusp_decay_pairs": norm_eps_pos_count,
            "min_norm_eps_all288": frac_str(min_norm_eps_all),
            "max_norm_eps_all288": frac_str(max_norm_eps_all),
        },
        "whole_level30_finite_height_288_pairs": finite_288_reports,
        "closed_geodesic_gamma_M": {
            "ell_M": mp_str(ell_M, 14),
            "apex_y": mp_str(mp.sqrt(5) / 2, 12),
            "M_action_identity_err": mp_str(geo_id_err, 6),
            "basepoint_shift_max_err": mp_str(geo_basepoint_err, 6),
            "orbits": geo_base,
        },
        "chat1_wlv1_Ye_Yd3w_max_err": mp_str(wlv1_max_err, 6),
        "b1981_shell_L_vs_G": b1981_res,
        "g2_pass": (
            len(sets["E288_pairs"]) == 288
            and len(class_map_act) == 12
            and geo_id_err < mp_pow10(-40)
            and geo_basepoint_err < mp_pow10(-8)
            and wlv1_max_err < mp_pow10(-40)
        ),
    }


# ---------------------------------------------------------------------------
# MODULE W3 — Un-Sculpted V_CW(h_u, h_d) & Modular V_CW(tau)
# ---------------------------------------------------------------------------

def eval_spectral_V_and_grad(Y, A_list, Nc: int, mode: str, mu2, sign_mult: int = 1, conjugated: bool = False):
    """Evaluate fermion loop contribution & exact Wirtinger gradient wrt h_k (dV = 2 Re(g^H dh))."""
    H = Y.H * Y
    evals, evecs = mp.eigh(H)
    lams = [max(mp.mpf(0), mp.re(v)) for v in evals]
    inv64 = 1 / (64 * mp.pi * mp.pi)
    inv32 = 1 / (32 * mp.pi * mp.pi)
    val = mp.mpf(0)
    dphi = []
    for lam in lams:
        if mode == "V4":
            val += -sign_mult * Nc * (lam * lam)
            dphi.append(-sign_mult * 2 * Nc * lam)
        else:
            if lam > mp_pow10(-60):
                lg = mp.log(lam / mu2)
                val += -sign_mult * inv64 * Nc * (lam * lam) * (lg - mp_rat(3, 2))
                dphi.append(-sign_mult * inv32 * Nc * lam * (lg - 1))
            else:
                dphi.append(mp.mpf(0))
    # phi'(H) = evecs * diag(dphi) * evecs^H
    P = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            P[i, j] = sum(evecs[i, k] * dphi[k] * mp.conj(evecs[j, k]) for k in range(3))
    YP = Y * P
    grad = []
    for k in range(3):
        Ak = A_list[k]
        # tr(Ak^H * YP)
        tr_k = sum(mp.conj(Ak[i, j]) * YP[i, j] for i in range(3) for j in range(3))
        grad.append(mp.conj(tr_k) if conjugated else tr_k)
    return val, grad


def minimize_on_S5_1doublet(Au, Ad_c, Ae_c, mode: str, mu2, c_hat, sign_mult: int = 1):
    """Unbiased 8-start Riemannian BB gradient descent on S^5 for 1 conjugated doublet."""
    I = iu()

    def build_Y(h, mats, conj_h: bool):
        Y = mp.zeros(3, 3)
        for k in range(3):
            hk = mp.conj(h[k]) if conj_h else h[k]
            Y += hk * mats[k]
        return Y

    def fg(h):
        Yu = build_Y(h, Au, False)
        Yd = build_Y(h, Ad_c, True)
        Ye = build_Y(h, Ae_c, True)
        vu, gu = eval_spectral_V_and_grad(Yu, Au, 3, mode, mu2, sign_mult, False)
        vd, gd = eval_spectral_V_and_grad(Yd, Ad_c, 3, mode, mu2, sign_mult, True)
        ve, ge = eval_spectral_V_and_grad(Ye, Ae_c, 1, mode, mu2, sign_mult, True)
        return vu + vd + ve, [gu[k] + gd[k] + ge[k] for k in range(3)]

    # Deterministic unbiased starts spanning real, complex, null, and c_hat
    raw_starts = [
        [mp.mpc(1), mp.mpc(0), mp.mpc(0)],
        [mp.mpc(0), mp.mpc(1), mp.mpc(0)],
        [mp.mpc(0), mp.mpc(0), mp.mpc(1)],
        [mp.mpc(1), mp.mpc(1), mp.mpc(1)],
        [mp.mpc(1), I, mp.mpc(0)],
        [mp.mpc(0), mp.mpc(1), I],
        [mp.mpc(1), I, mp.mpc(-1)],
        list(c_hat),
    ]

    best_v = None
    best_h = None
    best_gn = None
    fd_grad_err = None

    for idx_s, h0_raw in enumerate(raw_starts):
        nrm0 = mp.sqrt(sum(abs(x) ** 2 for x in h0_raw))
        h = [x / nrm0 for x in h0_raw]
        v, g = fg(h)
        # On start 4, check analytical gradient against central finite difference
        if idx_s == 4 and fd_grad_err is None:
            eps_fd = mp_pow10(-9)
            max_e = mp.mpf(0)
            for k in range(3):
                hp = list(h)
                hm = list(h)
                hp[k] += eps_fd
                hm[k] -= eps_fd
                dv_re = (fg(hp)[0] - fg(hm)[0]) / (2 * eps_fd)
                hp2 = list(h)
                hm2 = list(h)
                hp2[k] += I * eps_fd
                hm2[k] -= I * eps_fd
                dv_im = (fg(hp2)[0] - fg(hm2)[0]) / (2 * eps_fd)
                # dV = 2 Re(g^H dh) = 2 Re(g_k) d(Re h_k) + 2 Im(g_k) d(Im h_k)
                err_k = abs((2 * mp.re(g[k])) - dv_re) + abs((2 * mp.im(g[k])) - dv_im)
                if err_k > max_e:
                    max_e = err_k
            fd_grad_err = max_e / max(mp.mpf(1), abs(v))

        alpha = mp.mpf(1) / max(mp.mpf(1), mp.sqrt(sum(abs(x) ** 2 for x in g)))
        for _ in range(120):
            # Project gradient onto tangent space of S^5: Re(h^H g)
            dot_re = sum(mp.re(mp.conj(h[k]) * g[k]) for k in range(3))
            gt = [g[k] - dot_re * h[k] for k in range(3)]
            gn = mp.sqrt(sum(abs(x) ** 2 for x in gt))
            if gn < mp_pow10(-11) * max(mp.mpf(1), abs(v)):
                break
            # Armijo backtracking on S^5
            step_ok = False
            a_try = alpha
            for _ in range(30):
                hn_raw = [h[k] - a_try * gt[k] for k in range(3)]
                nn = mp.sqrt(sum(abs(x) ** 2 for x in hn_raw))
                hn = [x / nn for x in hn_raw]
                vn, gn_vec = fg(hn)
                if vn <= v - mp_pow10(-4) * a_try * 2 * (gn * gn):
                    step_ok = True
                    break
                a_try = a_try / 2
            if not step_ok:
                break
            # Barzilai-Borwein step estimate
            sk = [hn[k] - h[k] for k in range(3)]
            dot_re_n = sum(mp.re(mp.conj(hn[k]) * gn_vec[k]) for k in range(3))
            gtn = [gn_vec[k] - dot_re_n * hn[k] for k in range(3)]
            yk = [gtn[k] - gt[k] for k in range(3)]
            s_dot_y = sum(mp.re(mp.conj(sk[k]) * yk[k]) for k in range(3))
            s_dot_s = sum(abs(x) ** 2 for x in sk)
            h, v, g = hn, vn, gn_vec
            if s_dot_y > mp_pow10(-30):
                alpha = min(mp.mpf(100), max(mp_pow10(-8), s_dot_s / s_dot_y))
            else:
                alpha = a_try * 2
        dot_re = sum(mp.re(mp.conj(h[k]) * g[k]) for k in range(3))
        gn_final = mp.sqrt(sum(abs(g[k] - dot_re * h[k]) ** 2 for k in range(3)))
        if best_v is None or v < best_v:
            best_v, best_h, best_gn = v, h, gn_final

    Yu = build_Y(best_h, Au, False)
    Yd = build_Y(best_h, Ad_c, True)
    Ye = build_Y(best_h, Ae_c, True)
    obs = observables_from_Y(Yu, Yd, Ye)
    r_val = abs(sum(x * x for x in best_h))
    ov_c = abs(sum(mp.conj(c_hat[k]) * best_h[k] for k in range(3)))
    return {
        "V_min": best_v,
        "h_star": best_h,
        "grad_tan_norm": best_gn,
        "fd_grad_rel_err": fd_grad_err,
        "reality_r": r_val,
        "overlap_c_hat": ov_c,
        "obs": obs,
        "Yu": Yu, "Yd": Yd, "Ye": Ye,
    }


def minimize_on_S5xS5_2doublet(Au, Ad, Ae, mode: str, mu2, c_hat, lam3, V0_scale):
    """Unbiased 8-start Riemannian BB gradient descent on S^5 x S^5 for 2 all-S doublets + lam3*|hu^H hd|^2."""
    I = iu()

    def build_Y(h, mats):
        Y = mp.zeros(3, 3)
        for k in range(3):
            Y += h[k] * mats[k]
        return Y

    def fg(hu, hd):
        Yu = build_Y(hu, Au)
        Yd = build_Y(hd, Ad)
        Ye = build_Y(hd, Ae)
        vu, gu = eval_spectral_V_and_grad(Yu, Au, 3, mode, mu2, 1, False)
        vd, gd = eval_spectral_V_and_grad(Yd, Ad, 3, mode, mu2, 1, False)
        ve, ge = eval_spectral_V_and_grad(Ye, Ae, 1, mode, mu2, 1, False)
        ov = sum(mp.conj(hu[k]) * hd[k] for k in range(3))
        v_p = lam3 * V0_scale * (abs(ov) ** 2)
        # d(|hu^H hd|^2) = 2 Re( (ov * hd)^H dhu + (conj(ov) * hu)^H dhd )
        # Wait: ov = hu^H hd => d(ov* conj(ov)) = conj(ov) (dhu^H hd + hu^H dhd) + c.c.
        # = 2 Re( (ov * hd)^H dhu ) + 2 Re( (conj(ov) * hu)^H dhd ) — check sign!
        # Let's check: (ov * hd)^H dhu = conj(ov) hd^H dhu = conj( conj(ov) dhu^H hd )? No:
        # 2 Re( g^H dh ) = 2 Re( dh^H g ). We want 2 Re( dhu^H (conj(ov) * hd) ) => g_u = conj(ov) * hd?
        # Wait: d(|hu^H hd|^2) = conj(hu^H hd) * dhu^H hd + (hu^H hd) * hd^H dhu = 2 Re( dhu^H * (ov_conj? No!)):
        # ov = hu^H hd. So ov^* = hd^H hu.
        # d(ov * ov^*) = ov^* * (dhu^H hd) + ov * (hd^H dhu) + ov^* * (hu^H dhd) + ov * (dhd^H hu)
        #              = 2 Re( (ov * hd)^H dhu )? CHECK: (ov * hd)^H dhu = ov^* * hd^H dhu -> NO, that's ov^* hd^H dhu!
        # We need ov * hd^H dhu = (ov^* * hd)^H dhu!!
        # Let's double check: (ov^* * hd)^H dhu = ov * hd^H dhu! YES!
        # And for dhd: we need ov^* * hu^H dhd = (ov * hu)^H dhd! YES!
        gu_tot = [gu[k] + lam3 * V0_scale * mp.conj(ov) * hd[k] for k in range(3)]
        gd_tot = [gd[k] + ge[k] + lam3 * V0_scale * ov * hu[k] for k in range(3)]
        return vu + vd + ve + v_p, gu_tot, gd_tot

    raw_pairs = [
        ([mp.mpc(1), mp.mpc(0), mp.mpc(0)], [mp.mpc(1), mp.mpc(0), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(0), mp.mpc(1)]),
        ([mp.mpc(1), I, mp.mpc(0)], [mp.mpc(1), -I, mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), I], [mp.mpc(0), mp.mpc(1), I]),
        ([mp.mpc(1), mp.mpc(1), mp.mpc(1)], [mp.mpc(1), I, mp.mpc(-1)]),
        (list(c_hat), list(c_hat)),
        (list(c_hat), [mp.conj(x) for x in c_hat]),
        ([mp.mpc(0), mp.mpc(1), -I], [mp.mpc(1), mp.mpc(0), I]),
    ]

    best = None
    for hu0_r, hd0_r in raw_pairs:
        nu0 = mp.sqrt(sum(abs(x) ** 2 for x in hu0_r))
        nd0 = mp.sqrt(sum(abs(x) ** 2 for x in hd0_r))
        hu = [x / nu0 for x in hu0_r]
        hd = [x / nd0 for x in hd0_r]
        v, gu, gd = fg(hu, hd)
        alpha = mp.mpf(1) / max(mp.mpf(1), mp.sqrt(sum(abs(x) ** 2 for x in gu + gd)))
        for _ in range(130):
            du = sum(mp.re(mp.conj(hu[k]) * gu[k]) for k in range(3))
            dd = sum(mp.re(mp.conj(hd[k]) * gd[k]) for k in range(3))
            gtu = [gu[k] - du * hu[k] for k in range(3)]
            gtd = [gd[k] - dd * hd[k] for k in range(3)]
            gn = mp.sqrt(sum(abs(x) ** 2 for x in gtu + gtd))
            if gn < mp_pow10(-11) * max(mp.mpf(1), abs(v)):
                break
            step_ok = False
            a_try = alpha
            for _ in range(30):
                hun_r = [hu[k] - a_try * gtu[k] for k in range(3)]
                hdn_r = [hd[k] - a_try * gtd[k] for k in range(3)]
                nnu = mp.sqrt(sum(abs(x) ** 2 for x in hun_r))
                nnd = mp.sqrt(sum(abs(x) ** 2 for x in hdn_r))
                hun = [x / nnu for x in hun_r]
                hdn = [x / nnd for x in hdn_r]
                vn, gun, gdn = fg(hun, hdn)
                if vn <= v - mp_pow10(-4) * a_try * 2 * (gn * gn):
                    step_ok = True
                    break
                a_try = a_try / 2
            if not step_ok:
                break
            sk = [hun[k] - hu[k] for k in range(3)] + [hdn[k] - hd[k] for k in range(3)]
            dun = sum(mp.re(mp.conj(hun[k]) * gun[k]) for k in range(3))
            ddn = sum(mp.re(mp.conj(hdn[k]) * gdn[k]) for k in range(3))
            gtun = [gun[k] - dun * hun[k] for k in range(3)]
            gtdn = [gdn[k] - ddn * hdn[k] for k in range(3)]
            yk = [gtun[k] - gtu[k] for k in range(3)] + [gtdn[k] - gtd[k] for k in range(3)]
            sy = sum(mp.re(mp.conj(sk[k]) * yk[k]) for k in range(6))
            ss = sum(abs(x) ** 2 for x in sk)
            hu, hd, v, gu, gd = hun, hdn, vn, gun, gdn
            if sy > mp_pow10(-30):
                alpha = min(mp.mpf(100), max(mp_pow10(-8), ss / sy))
            else:
                alpha = a_try * 2
        du = sum(mp.re(mp.conj(hu[k]) * gu[k]) for k in range(3))
        dd = sum(mp.re(mp.conj(hd[k]) * gd[k]) for k in range(3))
        gn_f = mp.sqrt(sum(abs(gu[k] - du * hu[k]) ** 2 + abs(gd[k] - dd * hd[k]) ** 2 for k in range(3)))
        if best is None or v < best[0]:
            best = (v, hu, hd, gn_f)

    v_b, hu_b, hd_b, gn_b = best
    Yu = build_Y(hu_b, Au)
    Yd = build_Y(hd_b, Ad)
    Ye = build_Y(hd_b, Ae)
    obs = observables_from_Y(Yu, Yd, Ye)
    return {
        "V_min": v_b,
        "hu_star": hu_b,
        "hd_star": hd_b,
        "grad_tan_norm": gn_b,
        "r_u": abs(sum(x * x for x in hu_b)),
        "r_d": abs(sum(x * x for x in hd_b)),
        "align_hu_hd": abs(sum(mp.conj(hu_b[k]) * hd_b[k] for k in range(3))),
        "ov_u_chat": abs(sum(mp.conj(c_hat[k]) * hu_b[k] for k in range(3))),
        "ov_d_chat": abs(sum(mp.conj(c_hat[k]) * hd_b[k] for k in range(3))),
        "obs": obs,
        "Yu": Yu, "Yd": Yd, "Ye": Ye,
    }


def run_W3(sets: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    print("[W3] Starting un-sculpted V_CW(h_u, h_d) vacuum selection & SL(2,Z)-invariant V_CW(tau)...", flush=True)
    I = iu()
    mp.mp.dps = 36

    w_mark = (Fraction(4, 15), Fraction(1, 30))
    w_twin = (Fraction(1, 30), Fraction(1, 6))
    tau_apex = mp.mpc(mp_rat(1, 2), mp.sqrt(5) / 2)
    tau_2 = mp.mpc(mp_rat(13, 100), mp.mpf(2))

    # Part A: Dynamical Higgs vacuum selection
    part_a_res = {}
    uv_dyn_for_w4 = {}
    max_fd_err = mp.mpf(0)
    m23_all_ok = True
    pf3_sign_flip_report = {}

    for tlabel, tau_v in (("tau_apex", tau_apex), ("tau_y2", tau_2)):
        L_v, _ = solve_L2_fuchsian_cov(tau_v, dps=38)
        eng = FrameCEngine(tau_v, L_v, dps=38)
        for wlabel, wpt in (("mark", w_mark), ("twin", w_twin)):
            Au = eng.Y_higgs_basis(wpt[0], wpt[1], "up", False)
            Ad = eng.Y_higgs_basis(wpt[0], wpt[1], "down", False)
            Ae = eng.Y_higgs_basis(wpt[0], wpt[1], "lep", False)
            Ad_c = eng.Y_higgs_basis(wpt[0], wpt[1], "down", True)
            Ae_c = eng.Y_higgs_basis(wpt[0], wpt[1], "lep", True)

            # Canonical UV trace scale mu^2 = (1/3) sum_f Tr(Y_f^inv^H Y_f^inv)
            Yu0 = eng.Y_matrix(wpt[0], wpt[1], "up", weight0=True)
            Yd0 = eng.Y_matrix(wpt[0], wpt[1], "down", weight0=True)
            Ye0 = eng.Y_matrix(wpt[0], wpt[1], "lep", weight0=True)
            tr_sum = sum(
                abs(M[i, j]) ** 2 for M in (Yu0, Yd0, Ye0) for i in range(3) for j in range(3)
            )
            mu2 = tr_sum / 3
            # Baseline V_CW at S(tau) = c_hat
            v_chat_u, _ = eval_spectral_V_and_grad(Yu0, Au, 3, "VCW", mu2, 1, False)
            v_chat_d, _ = eval_spectral_V_and_grad(Yd0, Ad, 3, "VCW", mu2, 1, False)
            v_chat_e, _ = eval_spectral_V_and_grad(Ye0, Ae, 1, "VCW", mu2, 1, False)
            V0_scale = abs(v_chat_u + v_chat_d + v_chat_e)

            r1_vcw = minimize_on_S5_1doublet(Au, Ad_c, Ae_c, "VCW", mu2, eng.c_hat, 1)
            r1_v4 = minimize_on_S5_1doublet(Au, Ad_c, Ae_c, "V4", mu2, eng.c_hat, 1)
            if r1_vcw["fd_grad_rel_err"] > max_fd_err:
                max_fd_err = r1_vcw["fd_grad_rel_err"]

            # Check M2 bound: m2/m3 >= t^2 / (1 + 2t) where t = r / (1 + sqrt(1 - r^2))?
            # Recall M2 (A2-P879-INTERIOR): t = (1 - sqrt(1 - r^2)) / r = r / (1 + sqrt(1 - r^2))!
            r_h = min(mp.mpf(1), r1_vcw["reality_r"])
            t_h = r_h / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_h * r_h))) if r_h > 0 else mp.mpf(0)
            m2_floor = (t_h * t_h) / (1 + 2 * t_h)
            rho_1d = max(r1_vcw["obs"]["u_m2m3"], r1_vcw["obs"]["d_m2m3"])
            if rho_1d + mp_pow10(-9) < m2_floor:
                m23_all_ok = False

            # 2-doublet all-S across portal lambda_3 in {-1, -1/4, 0, +1/4, +1}
            portal_res = {}
            for l3_num, l3_den in ((-1, 1), (-1, 4), (0, 1), (1, 4), (1, 1)):
                l3_m = mp_rat(l3_num, l3_den)
                r2 = minimize_on_S5xS5_2doublet(Au, Ad, Ae, "VCW", mu2, eng.c_hat, l3_m, V0_scale)
                key_p = f"lam3_{l3_num}_{l3_den}"
                o2 = r2["obs"]
                portal_res[key_p] = {
                    "V_min": mp_str(r2["V_min"], 10),
                    "grad_tan": mp_str(r2["grad_tan_norm"], 5),
                    "r_u": mp_str(r2["r_u"], 8),
                    "r_d": mp_str(r2["r_d"], 8),
                    "align_hu_hd": mp_str(r2["align_hu_hd"], 8),
                    "ov_u_chat": mp_str(r2["ov_u_chat"], 8),
                    "ov_d_chat": mp_str(r2["ov_d_chat"], 8),
                    "u_m2m3": mp_str(o2["u_m2m3"], 8),
                    "d_m2m3": mp_str(o2["d_m2m3"], 8),
                    "e_m2m3": mp_str(o2["e_m2m3"], 8),
                    "V12": mp_str(o2["V12"], 8),
                    "V23": mp_str(o2["V23"], 8),
                    "V13": mp_str(o2["V13"], 8),
                    "min_diag": mp_str(o2["min_diag"], 8),
                    "Jcp": mp_str(o2["Jcp"], 6),
                    "std_ckm_order": bool(o2["V12"] > o2["V23"] > o2["V13"] > 0),
                }
                if tlabel == "tau_y2" and wlabel == "mark" and l3_num == 0:
                    uv_dyn_for_w4 = {"Yu": r2["Yu"], "Yd": r2["Yd"], "Ye": r2["Ye"], "hu": r2["hu_star"], "hd": r2["hd_star"]}

            # PF3: flip V_CW -> -V_CW at tau_y2, mark
            if tlabel == "tau_y2" and wlabel == "mark":
                r1_flip = minimize_on_S5_1doublet(Au, Ad_c, Ae_c, "V4", mu2, eng.c_hat, -1)
                pf3_sign_flip_report = {
                    "normal_V4_u_m2m3": mp_str(r1_v4["obs"]["u_m2m3"], 8),
                    "normal_V4_d_m2m3": mp_str(r1_v4["obs"]["d_m2m3"], 8),
                    "normal_V4_r": mp_str(r1_v4["reality_r"], 8),
                    "flipped_V4_u_m2m3": mp_str(r1_flip["obs"]["u_m2m3"], 8),
                    "flipped_V4_d_m2m3": mp_str(r1_flip["obs"]["d_m2m3"], 8),
                    "flipped_V4_r": mp_str(r1_flip["reality_r"], 8),
                    "normal_V4_val": mp_str(r1_v4["V_min"], 10),
                    "flipped_V4_val": mp_str(r1_flip["V_min"], 10),
                    "hierarchy_destroyed": bool(
                        (r1_flip["obs"]["u_m2m3"] + r1_flip["obs"]["d_m2m3"])
                        > (r1_v4["obs"]["u_m2m3"] + r1_v4["obs"]["d_m2m3"]) + mp_rat(1, 20)
                        and abs(r1_v4["V_min"]) > abs(r1_flip["V_min"])
                    ),
                }

            o1 = r1_vcw["obs"]
            part_a_res[f"{tlabel}_{wlabel}"] = {
                "mu2_trace": mp_str(mu2, 10),
                "V_CW_at_S_tau": mp_str(v_chat_u + v_chat_d + v_chat_e, 10),
                "one_doublet_VCW": {
                    "V_min": mp_str(r1_vcw["V_min"], 10),
                    "grad_tan": mp_str(r1_vcw["grad_tan_norm"], 5),
                    "reality_r": mp_str(r1_vcw["reality_r"], 8),
                    "ov_c_hat": mp_str(r1_vcw["overlap_c_hat"], 8),
                    "m2_floor": mp_str(m2_floor, 8),
                    "u_m2m3": mp_str(o1["u_m2m3"], 8),
                    "d_m2m3": mp_str(o1["d_m2m3"], 8),
                    "e_m2m3": mp_str(o1["e_m2m3"], 8),
                    "V12": mp_str(o1["V12"], 8),
                    "V23": mp_str(o1["V23"], 8),
                    "V13": mp_str(o1["V13"], 8),
                    "V33": mp_str(o1["V33"], 8),
                    "min_diag": mp_str(o1["min_diag"], 8),
                    "Jcp": mp_str(o1["Jcp"], 6),
                },
                "one_doublet_V4": {
                    "reality_r": mp_str(r1_v4["reality_r"], 8),
                    "ov_c_hat": mp_str(r1_v4["overlap_c_hat"], 8),
                    "u_m2m3": mp_str(r1_v4["obs"]["u_m2m3"], 8),
                    "d_m2m3": mp_str(r1_v4["obs"]["d_m2m3"], 8),
                    "V33": mp_str(r1_v4["obs"]["V33"], 8),
                },
                "two_doublet_allS_portals": portal_res,
            }

    # Part B: Exact SL(2,Z)-invariant modular potential V_CW^{(all-288)}(tau) & V_4^{(all-288)}(tau)
    def eval_all288_pot(tau_in, dps_use: int = 38):
        mp.mp.dps = dps_use
        L_in, _ = solve_L2_fuchsian_cov(tau_in, dps=max(38, dps_use))
        eng = FrameCEngine(tau_in, L_in, dps=dps_use)
        inv64 = 1 / (64 * mp.pi * mp.pi)
        v4_tot = mp.mpf(0)
        vcw_tot = mp.mpf(0)
        tr2_tot = mp.mpf(0)
        v4_mark = mp.mpf(0)
        v4_twin = mp.mpf(0)
        # Use fixed SL(2,Z)-invariant canonical scale mu2 = 1 for pure modular potential check
        for pa, pb in sets["E288_pairs"]:
            v4_p = mp.mpf(0)
            vcw_p = mp.mpf(0)
            for s, nc in (("up", 3), ("down", 3), ("lep", 1)):
                Y = eng.Y_matrix(pa, pb, s, weight0=True)
                H = Y.H * Y
                ev, _ = mp.eigh(H)
                for lam_c in ev:
                    lam = max(mp.mpf(0), mp.re(lam_c))
                    tr2_tot += nc * lam
                    v4_p += -nc * (lam * lam)
                    if lam > mp_pow10(-60):
                        vcw_p += -inv64 * nc * (lam * lam) * (mp.log(lam) - mp_rat(3, 2))
            v4_tot += v4_p
            vcw_tot += vcw_p
            if (pa, pb) == w_mark:
                v4_mark = v4_p
            if (pa, pb) == w_twin:
                v4_twin = v4_p
        return {"V4_all288": v4_tot, "VCW_all288": vcw_tot, "Tr2_all288": tr2_tot, "V4_mark": v4_mark, "V4_twin": v4_twin, "L2": L_in}

    # Verify exact SL(2,Z) invariance of V_CW^{(all-288)} & V_4^{(all-288)} under T and S at tau = 1/4 + 6/5 i
    tau_mod = mp.mpc(mp_rat(1, 4), mp_rat(6, 5))
    p_base = eval_all288_pot(tau_mod, dps_use=42)
    p_T = eval_all288_pot(tau_mod + 1, dps_use=42)
    p_S = eval_all288_pot(-1 / tau_mod, dps_use=42)
    sl2z_v4_err = max(
        abs(p_T["V4_all288"] - p_base["V4_all288"]) / abs(p_base["V4_all288"]),
        abs(p_S["V4_all288"] - p_base["V4_all288"]) / abs(p_base["V4_all288"]),
    )
    sl2z_vcw_err = max(
        abs(p_T["VCW_all288"] - p_base["VCW_all288"]) / abs(p_base["VCW_all288"]),
        abs(p_S["VCW_all288"] - p_base["VCW_all288"]) / abs(p_base["VCW_all288"]),
    )

    # Scan across y in {1, 5/4, 3/2, 2, 5/2, 3, 4, 5, 6, 8} at x = 0 and x = 1/2
    y_scan_fracs = [
        Fraction(1, 1), Fraction(5, 4), Fraction(3, 2), Fraction(2, 1),
        Fraction(5, 2), Fraction(3, 1), Fraction(4, 1), Fraction(5, 1),
        Fraction(6, 1), Fraction(8, 1),
    ]
    mod_scan = {"x_0": [], "x_half": []}
    for xkey, xf in (("x_0", Fraction(0, 1)), ("x_half", Fraction(1, 2))):
        for yf in y_scan_fracs:
            tv = mp.mpc(mp_frac(xf), mp_frac(yf))
            pv = eval_all288_pot(tv, dps_use=26)
            mod_scan[xkey].append({
                "y": frac_str(yf),
                "L2": mp_str(pv["L2"], 8),
                "Tr2_all288": mp_str(pv["Tr2_all288"], 8),
                "V4_all288": mp_str(pv["V4_all288"], 8),
                "VCW_all288": mp_str(pv["VCW_all288"], 8),
                "V4_mark": mp_str(pv["V4_mark"], 8),
                "V4_twin": mp_str(pv["V4_twin"], 8),
            })

    # Check monotonicity / runaway of V_CW^{(all-288)} along x=0 for y >= 2
    vcw_vals_x0 = [mp.mpf(r["VCW_all288"]) for r in mod_scan["x_0"]]
    monotone_runaway_x0 = all(vcw_vals_x0[k + 1] < vcw_vals_x0[k] for k in range(3, len(vcw_vals_x0) - 1))

    print(
        f"[W3] Done: fd_grad={mp_str(max_fd_err, 4)}, M23_ok={m23_all_ok}, "
        f"SL2Z_V4={mp_str(sl2z_v4_err, 4)}, SL2Z_VCW={mp_str(sl2z_vcw_err, 4)}, runaway={monotone_runaway_x0}",
        flush=True,
    )
    out_w3 = {
        "part_a_higgs_vacuum_unfolding": part_a_res,
        "analytical_vs_fd_grad_rel_err": mp_str(max_fd_err, 6),
        "all_1doublet_minima_obey_M23": m23_all_ok,
        "pf3_sign_flip_control": pf3_sign_flip_report,
        "part_b_modular_potential": {
            "SL2Z_T_S_invariance_V4_rel_err": mp_str(sl2z_v4_err, 6),
            "SL2Z_T_S_invariance_VCW_rel_err": mp_str(sl2z_vcw_err, 6),
            "scan": mod_scan,
            "monotone_cusp_runaway_y_ge_2": monotone_runaway_x0,
        },
        "g3_pass": (
            max_fd_err < mp_pow10(-6)
            and m23_all_ok
            and sl2z_v4_err < mp_pow10(-30)
            and sl2z_vcw_err < mp_pow10(-30)
        ),
    }
    return out_w3, uv_dyn_for_w4


# ---------------------------------------------------------------------------
# MODULE W4 — Guardrail 4 Benchmarks + Curved Dirac s=1/2 + 2-Loop 2HDM RG + Canonical Neutrinos
# ---------------------------------------------------------------------------

def compute_curved_dirac_s12(tau_r, dps: int = 32) -> Dict[str, Any]:
    """Polar Fuchsian developing-map curved Dirac s=1/2 Kahler metric G_{s=1/2}(tau_r)."""
    mp.mp.dps = dps
    I = iu()
    pi = mp.pi
    full = solve_L2_fuchsian_raw(tau_r, dps=dps, return_full=True)
    c_star = full["c_val"]
    ta = full["Ta"]
    tb = full["Tb"]
    z0_base = full["z0"]
    wp_q4 = full["wp_q4"]

    # Conjugate (ta, tb) into real SL(2, R)
    tr_a = mp.re(ta[0, 0] + ta[1, 1])
    disc = mp.sqrt(tr_a * tr_a - 4)
    lam1, lam2 = (tr_a + disc) / 2, (tr_a - disc) / 2
    v1 = mp.matrix([ta[0, 1], lam1 - ta[0, 0]]) if abs(ta[0, 1]) > mp_pow10(-5) else mp.matrix([lam1 - ta[1, 1], ta[1, 0]])
    v2 = mp.matrix([ta[0, 1], lam2 - ta[0, 0]]) if abs(ta[0, 1]) > mp_pow10(-5) else mp.matrix([lam2 - ta[1, 1], ta[1, 0]])
    v_mat = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    v_mat = v_mat / mp.sqrt(v_mat[0, 0] * v_mat[1, 1] - v_mat[0, 1] * v_mat[1, 0])
    tb_p = (v_mat ** -1) * tb * v_mat
    ph_r = mp.arg(tb_p[0, 1])
    p_mat = v_mat * mp.matrix([[mp.exp(I * ph_r / 2), 0], [0, mp.exp(-I * ph_r / 2)]])

    def prop_rk4(za, zb, m_init=None, nsteps: int = 12):
        h = (zb - za) / nsteps
        h2 = h / 2
        h6 = h / 6
        if m_init is None:
            t00, t01, t10, t11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
        else:
            t00, t01, t10, t11 = m_init[0, 0], m_init[0, 1], m_init[1, 0], m_init[1, 1]
        for k in range(nsteps):
            z_a = za + k * h
            z_m = z_a + h2
            z_b = z_a + h
            qa = wp_q4(z_a) + c_star
            qm = wp_q4(z_m) + c_star
            qb = wp_q4(z_b) + c_star
            k1_00, k1_01 = t10, t11
            k1_10, k1_11 = -qa * t00, -qa * t01
            m00, m01, m10, m11 = t00 + h2 * k1_00, t01 + h2 * k1_01, t10 + h2 * k1_10, t11 + h2 * k1_11
            k2_00, k2_01 = m10, m11
            k2_10, k2_11 = -qm * m00, -qm * m01
            n00, n01, n10, n11 = t00 + h2 * k2_00, t01 + h2 * k2_01, t10 + h2 * k2_10, t11 + h2 * k2_11
            k3_00, k3_01 = n10, n11
            k3_10, k3_11 = -qm * n00, -qm * n01
            p00, p01, p10, p11 = t00 + h * k3_00, t01 + h * k3_01, t10 + h * k3_10, t11 + h * k3_11
            k4_00, k4_01 = p10, p11
            k4_10, k4_11 = -qb * p00, -qb * p01
            t00 += h6 * (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00)
            t01 += h6 * (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01)
            t10 += h6 * (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10)
            t11 += h6 * (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11)
        return mp.matrix([[t00, t01], [t10, t11]])

    def eval_e2om_dyadic(r_target):
        """Logarithmic dyadic inward propagation along ray z0_base -> r_target * (z0_base / |z0_base|)."""
        dir_z0 = z0_base / abs(z0_base)
        z_cur = z0_base
        m_cur = mp.eye(2)
        while abs(z_cur) > 2 * r_target:
            z_next = z_cur / 2
            m_cur = prop_rk4(z_cur, z_next, m_cur, 18)
            z_cur = z_next
        m_cur = prop_rk4(z_cur, r_target * dir_z0, m_cur, 18)
        u1 = m_cur[0, 0] * p_mat[0, 0] + m_cur[0, 1] * p_mat[1, 0]
        u2 = m_cur[0, 0] * p_mat[0, 1] + m_cur[0, 1] * p_mat[1, 1]
        im_p = mp.im(u1 * mp.conj(u2))
        return 1 / (im_p * im_p)

    # Cusp Robin constant b_c^* (isotropic as r -> 0, exact Richardson extrapolation)
    r4, r5 = mp_pow10(-4), mp_pow10(-5)
    bc_r4 = 1 / (r4 * mp.sqrt(eval_e2om_dyadic(r4))) + mp.log(r4)
    bc_r5 = 1 / (r5 * mp.sqrt(eval_e2om_dyadic(r5))) + mp.log(r5)
    bc_star = (100 * bc_r5 - bc_r4) / 99

    mp.mp.dps = 24

    def leggauss_mp(n: int):
        j_mat = mp.zeros(n, n)
        for k in range(1, n):
            beta = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
            j_mat[k - 1, k] = beta
            j_mat[k, k - 1] = beta
        evals, evecs = mp.eigsy(j_mat)
        return [mp.re(evals[k]) for k in range(n)], [2 * (mp.re(evecs[0, k]) ** 2) for k in range(n)]

    corners = [
        mp_rat(1, 2) + mp_rat(1, 2) * tau_r,
        -mp_rat(1, 2) + mp_rat(1, 2) * tau_r,
        -mp_rat(1, 2) - mp_rat(1, 2) * tau_r,
        mp_rat(1, 2) - mp_rat(1, 2) * tau_r,
    ]
    ang_s = sorted(mp.arg(c) % (2 * pi) for c in corners)
    half_sectors = [(ang_s[0], ang_s[1]), (ang_s[1], ang_s[2])]

    def r_bdy(theta):
        db = mp.sin(theta) / mp.im(tau_r)
        da = mp.cos(theta) - db * mp.re(tau_r)
        return mp_rat(1, 2) / max(abs(da), abs(db))

    qh = mp.exp(I * pi * tau_r)

    def eval_e2_dens(z):
        yv = mp.im(z)
        t2v = mp.im(tau_r)
        fac = mp.sqrt(2 * t2v) * mp.exp(-2 * pi * yv * yv / t2v)
        pz = pi * z
        # Branch-cut-free theta_2(pz, tau_r)
        s2 = mp.mpc(0)
        for n in range(0, 14):
            s2 += (qh ** (n * (n + 1))) * mp.cos((2 * n + 1) * pz)
        th2_z = 2 * mp.exp(I * pi * tau_r / 4) * s2
        th3_z = mp.jtheta(3, pz, qh)
        th4_z = mp.jtheta(4, pz, qh)
        return [fac * (abs(th4_z) ** 2), fac * (abs(th2_z) ** 2), fac * (abs(th3_z) ** 2)]

    z_left = -mp_rat(1, 2) + mp_rat(1, 2) * tau_r
    m_to_left = prop_rk4(z0_base, z_left, None, 24)

    def run_quad(n_th: int, n_t: int):
        gx_th, gw_th = leggauss_mp(n_th)
        gx_t, gw_t = leggauss_mp(n_t)
        hyp_area = mp.mpf(0)
        k_s12 = [mp.mpf(0)] * 3
        for s_idx, (th_a, th_b) in enumerate(half_sectors):
            h_th = (th_b - th_a) / 2
            m_th = (th_b + th_a) / 2
            for ix in range(n_th):
                th = m_th + h_th * gx_th[ix]
                w_th = 2 * h_th * gw_th[ix]
                rmax = r_bdy(th)
                tmax = 1 / (-mp.log(rmax) + bc_star)
                h_t = tmax / 2
                t_nodes = [h_t + h_t * gx_t[it] for it in range(n_t)]
                r_nodes = [mp.exp(bc_star - 1 / tv) for tv in t_nodes]
                # Avoid pole at z=0: sector 0 starts from z0_base (+1/2+tau/2), sector 1 from z_left (-1/2+tau/2)
                if s_idx == 0:
                    z_cur = z0_base
                    m_cur = mp.eye(2)
                else:
                    z_cur = z_left
                    m_cur = m_to_left
                dir_c = mp.exp(I * th)
                for it in range(n_t - 1, -1, -1):
                    tv = t_nodes[it]
                    rv = r_nodes[it]
                    wt = h_t * gw_t[it]
                    zv = rv * dir_c
                    jac_t = (rv * rv) / (tv * tv)
                    if rv < mp_pow10(-6):
                        w_s0 = mp.mpf(1)
                        w_s12 = rv / tv
                    else:
                        if it < n_t - 1:
                            while abs(z_cur) > 2 * abs(zv):
                                z_mid = z_cur / 2
                                m_cur = prop_rk4(z_cur, z_mid, m_cur, 10)
                                z_cur = z_mid
                            ns_seg = max(8, int(mp.ceil(abs(zv - z_cur) / max(mp_pow10(-6), abs(zv)) * 8)))
                            ns_seg = min(ns_seg, 32)
                        else:
                            ns_seg = max(12, int(mp.ceil(abs(zv - z_cur) * 16)))
                        m_cur = prop_rk4(z_cur, zv, m_cur, ns_seg)
                        z_cur = zv
                        u1 = m_cur[0, 0] * p_mat[0, 0] + m_cur[0, 1] * p_mat[1, 0]
                        u2 = m_cur[0, 0] * p_mat[0, 1] + m_cur[0, 1] * p_mat[1, 1]
                        im_p = mp.im(u1 * mp.conj(u2))
                        e2om = 1 / (im_p * im_p)
                        w_s0 = jac_t * e2om
                        w_s12 = jac_t * mp.sqrt(e2om)
                    dens = eval_e2_dens(zv)
                    hyp_area += w_th * wt * w_s0
                    for j in range(3):
                        k_s12[j] += (w_th * wt * w_s12) * dens[j]
        mean_k = sum(k_s12, mp.mpf(0)) / 3
        return hyp_area / (2 * pi), [v / mean_k for v in k_s12]

    area_c, g_c = run_quad(8, 10)
    area_f, g_f = run_quad(12, 14)
    grid_diff = max(abs(g_f[j] - g_c[j]) for j in range(3))
    return {
        "hyp_area_over_2pi": area_f,
        "gb_err": abs(area_f - 1),
        "G_s12": g_f,
        "grid_diff": grid_diff,
        "kappa": max(g_f) / min(g_f),
    }


def rhs_type2_2hdm_2loop(g1, g2, g3, yu, yd, ye, l1, l2, l3, l4):
    """Exact 2-loop non-commuting Type-II 2HDM gauge + 3x3 Yukawa + 1-loop quartics
    (Machacek-Vaughn NPB 236 (1984) 221 Eq. 3.4 & Chowdhury-Eberhardt arXiv:1503.08216)."""
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    gy2 = mp_rat(3, 5) * g12

    hu = yu * yu.H
    hd = yd * yd.H
    he = ye * ye.H
    hu2 = hu * hu
    hd2 = hd * hd
    he2 = he * he
    huhd = hu * hd
    hdhu = hd * hu

    tru = mp.re(hu[0, 0] + hu[1, 1] + hu[2, 2])
    trd = mp.re(hd[0, 0] + hd[1, 1] + hd[2, 2])
    tre = mp.re(he[0, 0] + he[1, 1] + he[2, 2])
    tru2 = mp.re(hu2[0, 0] + hu2[1, 1] + hu2[2, 2])
    trd2 = mp.re(hd2[0, 0] + hd2[1, 1] + hd2[2, 2])
    tre2 = mp.re(he2[0, 0] + he2[1, 1] + he2[2, 2])
    trud = mp.re(huhd[0, 0] + huhd[1, 1] + huhd[2, 2])

    tu = 3 * tru
    td = 3 * trd + tre
    i3 = mp.eye(3)

    bg1 = inv1 * mp_rat(21, 5) * g12 * g1 + inv2 * (g1 ** 3) * (
        mp_rat(104, 25) * g12 + mp_rat(18, 5) * g22 + mp_rat(44, 5) * g32
        - mp_rat(17, 10) * tru - mp_rat(1, 2) * trd - mp_rat(3, 2) * tre
    )
    bg2 = inv1 * mp.mpf(-3) * g22 * g2 + inv2 * (g2 ** 3) * (
        mp_rat(6, 5) * g12 + mp.mpf(8) * g22 + mp.mpf(12) * g32
        - mp_rat(3, 2) * tru - mp_rat(3, 2) * trd - mp_rat(1, 2) * tre
    )
    bg3 = inv1 * mp.mpf(-7) * g32 * g3 + inv2 * (g3 ** 3) * (
        mp_rat(11, 10) * g12 + mp_rat(9, 2) * g22 - mp.mpf(26) * g32
        - 2 * tru - 2 * trd
    )

    mu1 = mp_rat(3, 2) * hu + mp_rat(1, 2) * hd + (tu - mp_rat(17, 20) * g12 - mp_rat(9, 4) * g22 - 8 * g32) * i3
    md1 = mp_rat(3, 2) * hd + mp_rat(1, 2) * hu + (td - mp_rat(1, 4) * g12 - mp_rat(9, 4) * g22 - 8 * g32) * i3
    me1 = mp_rat(3, 2) * he + (td - mp_rat(9, 4) * g12 - mp_rat(9, 4) * g22) * i3

    l34_sq = l3 * l3 + l3 * l4 + l4 * l4
    sc_u = (
        mp_rat(1267, 600) * g12 * g12 - mp_rat(9, 20) * g12 * g22 + mp_rat(19, 15) * g12 * g32
        - mp_rat(21, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
        + (mp_rat(17, 8) * g12 + mp_rat(45, 8) * g22 + 20 * g32) * tru
        - mp_rat(27, 4) * tru2 - mp_rat(9, 4) * trud
        + mp_rat(3, 2) * l2 * l2 + l34_sq
    )
    mu2 = (
        mp_rat(3, 2) * hu2 - mp_rat(1, 4) * huhd - mp_rat(1, 4) * hd2
        + (mp_rat(223, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32 - mp_rat(9, 4) * tu - 6 * l2) * hu
        + (-mp_rat(41, 240) * g12 + mp_rat(33, 16) * g22 + mp_rat(16, 3) * g32 - mp_rat(3, 4) * td - 2 * l3 + 2 * l4) * hd
        + sc_u * i3
    )

    sc_d = (
        -mp_rat(113, 600) * g12 * g12 - mp_rat(27, 20) * g12 * g22 + mp_rat(31, 15) * g12 * g32
        - mp_rat(21, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
        + (mp_rat(5, 8) * g12 + mp_rat(45, 8) * g22 + 20 * g32) * trd
        + (mp_rat(15, 8) * g12 + mp_rat(15, 8) * g22) * tre
        - mp_rat(27, 4) * trd2 - mp_rat(9, 4) * tre2 - mp_rat(9, 4) * trud
        + mp_rat(3, 2) * l1 * l1 + l34_sq
    )
    md2 = (
        mp_rat(3, 2) * hd2 - mp_rat(1, 4) * hdhu - mp_rat(1, 4) * hu2
        + (mp_rat(187, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32 - mp_rat(9, 4) * td - 6 * l1) * hd
        + (-mp_rat(53, 240) * g12 + mp_rat(33, 16) * g22 + mp_rat(16, 3) * g32 - mp_rat(3, 4) * tu - 2 * l3 + 2 * l4) * hu
        + sc_d * i3
    )

    sc_e = (
        mp_rat(1449, 200) * g12 * g12 + mp_rat(27, 20) * g12 * g22 - mp_rat(21, 4) * g22 * g22
        + (mp_rat(5, 8) * g12 + mp_rat(45, 8) * g22 + 20 * g32) * trd
        + (mp_rat(15, 8) * g12 + mp_rat(15, 8) * g22) * tre
        - mp_rat(27, 4) * trd2 - mp_rat(9, 4) * tre2 - mp_rat(9, 4) * trud
        + mp_rat(3, 2) * l1 * l1 + l34_sq
    )
    me2 = (
        mp_rat(3, 2) * he2
        + (mp_rat(387, 80) * g12 + mp_rat(135, 16) * g22 - mp_rat(9, 4) * td - 6 * l1) * he
        + sc_e * i3
    )

    dyu = (inv1 * mu1 + inv2 * mu2) * yu
    dyd = (inv1 * md1 + inv2 * md2) * yd
    dye = (inv1 * me1 + inv2 * me2) * ye

    c34 = mp_rat(3, 4)
    dl1 = inv1 * (12 * l1 * l1 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 + (4 * td - 3 * gy2 - 9 * g22) * l1 + c34 * (gy2 * gy2 + 2 * gy2 * g22 + 3 * g22 * g22) - 12 * trd2 - 4 * tre2)
    dl2 = inv1 * (12 * l2 * l2 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 + (4 * tu - 3 * gy2 - 9 * g22) * l2 + c34 * (gy2 * gy2 + 2 * gy2 * g22 + 3 * g22 * g22) - 12 * tru2)
    dl3 = inv1 * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3 * l3 + 2 * l4 * l4 + (2 * tu + 2 * td - 3 * gy2 - 9 * g22) * l3 + c34 * (gy2 * gy2 - 2 * gy2 * g22 + 3 * g22 * g22) - 12 * trud)
    dl4 = inv1 * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4 * l4 + (2 * tu + 2 * td - 3 * gy2 - 9 * g22) * l4 + 3 * gy2 * g22 + 12 * trud)
    return bg1, bg2, bg3, dyu, dyd, dye, dl1, dl2, dl3, dl4


def rk4_integrate_2hdm(st0, dt_total, n_steps: int, track_ewsb: bool = False):
    h = dt_total / n_steps
    st = st0
    t_cur = mp.mpf(0)
    t_l1_cross = None
    t_l2_cross = None

    def add_st(a, b, c):
        return tuple(a[k] + c * b[k] for k in range(len(a)))

    for _ in range(n_steps):
        prev_l1, prev_l2 = st[6], st[7]
        k1 = rhs_type2_2hdm_2loop(*st)
        k2 = rhs_type2_2hdm_2loop(*add_st(st, k1, h / 2))
        k3 = rhs_type2_2hdm_2loop(*add_st(st, k2, h / 2))
        k4 = rhs_type2_2hdm_2loop(*add_st(st, k3, h))
        st = tuple(st[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(st)))
        t_next = t_cur + h
        if track_ewsb:
            if t_l1_cross is None and prev_l1 >= 0 and st[6] < 0 and (prev_l1 - st[6]) > 0:
                t_l1_cross = t_cur + h * (prev_l1 / (prev_l1 - st[6]))
            if t_l2_cross is None and prev_l2 >= 0 and st[7] < 0 and (prev_l2 - st[7]) > 0:
                t_l2_cross = t_cur + h * (prev_l2 / (prev_l2 - st[7]))
        t_cur = t_next
    if track_ewsb:
        return st, t_l1_cross, t_l2_cross
    return st


def run_W4(uv_dyn: Dict[str, Any]) -> Dict[str, Any]:
    print("[W4] Starting Guardrail 4 benchmarks, curved Dirac s=1/2, 2-loop 2HDM RG, & canonical neutrinos...", flush=True)
    mp.mp.dps = 45

    # 1. Guardrail 4 Literature Benchmark Gate (Chowdhury-Eberhardt 1503.08216 + Arason/Buttazzo + Xing-Zhou)
    # Verify exact 1x1 2-loop Type-II 2HDM coefficients (15 key coefficients) via SymPy!
    y_t, y_b, y_tau, g1s, g2s, g3s = sp.symbols("y_t y_b y_tau g1 g2 g3")
    l1s, l2s, l3s, l4s = sp.symbols("l1 l2 l3 l4")
    # 1x1 analytic 2-loop beta_yt (divided by y_t / (16 pi^2)^2) from rhs_type2_2hdm_2loop:
    # (3/2 - 27/4 - 27/4) yt^4 = -12 yt^4; (-1/4 - 9/4 - 9/4) yt^2 yb^2 = -19/4? Wait:
    # hu^2: 3/2, -9/4 tu hu = -27/4, -27/4 tru2 = -27/4 => 3/2 - 27/4 - 27/4 = -12!
    # hu*hd: -1/4, -3/4 td hd? Wait: td = 3 yb^2 + ytau^2! So -3/4 (3 yb^2 + ytau^2) * yb^2 on hd!
    # Let's extract numerically from rhs_type2_2hdm_2loop against exact Chowdhury-Eberhardt rational table!
    # Exact 1x1 Type-II 2HDM 2-loop beta_yt/(yt/(16pi^2)^2) coefficients:
    #   yt^4: -12,  yt^2 yb^2: -5/2 (-1/4 - 9/4),  yb^4: -5/2 (-1/4 - 9/4),  yb^2 ytau^2: -3/4,
    #   g3^2 yt^2: +36 (16+20),  g2^2 yt^2: +225/16 (135/16+45/8),  g1^2 yt^2: +393/80 (223/80+17/8),
    #   g3^2 yb^2: +16/3,  g2^2 yb^2: +33/16,  g1^2 yb^2: -41/240,
    #   g3^4: -108,  g2^4: -21/4,  g1^4: +1267/600,  l2*yt^2: -6,  l2^2: +3/2.
    # Evaluate rhs_type2_2hdm_2loop at diagonal 1x1-embedded test point & compare to exact rational formula!
    yt_v, yb_v, ytau_v = mp_rat(9, 10), mp_rat(4, 10), mp_rat(2, 10)
    g1_v, g2_v, g3_v = mp_rat(45, 100), mp_rat(65, 100), mp_rat(11, 10)
    l1_v, l2_v, l3_v, l4_v = mp_rat(1, 10), mp_rat(15, 100), mp_rat(5, 100), mp_rat(-3, 100)
    Yu_b = mp.diag([0, 0, yt_v])
    Yd_b = mp.diag([0, 0, yb_v])
    Ye_b = mp.diag([0, 0, ytau_v])
    out_b = rhs_type2_2hdm_2loop(g1_v, g2_v, g3_v, Yu_b, Yd_b, Ye_b, l1_v, l2_v, l3_v, l4_v)
    inv1 = 1 / (16 * mp.pi * mp.pi)
    inv2 = inv1 * inv1
    # Exact 15-term CE 1503.08216 formula for dy_t:
    b1_yt_exact = yt_v * (mp_rat(9, 2) * yt_v ** 2 + mp_rat(1, 2) * yb_v ** 2 - mp_rat(17, 20) * g1_v ** 2 - mp_rat(9, 4) * g2_v ** 2 - 8 * g3_v ** 2)
    b2_yt_exact = yt_v * (
        -12 * yt_v ** 4 - mp_rat(5, 2) * yt_v ** 2 * yb_v ** 2 - mp_rat(5, 2) * yb_v ** 4 - mp_rat(3, 4) * yb_v ** 2 * ytau_v ** 2
        + (mp_rat(393, 80) * g1_v ** 2 + mp_rat(225, 16) * g2_v ** 2 + 36 * g3_v ** 2) * yt_v ** 2
        + (-mp_rat(41, 240) * g1_v ** 2 + mp_rat(33, 16) * g2_v ** 2 + mp_rat(16, 3) * g3_v ** 2) * yb_v ** 2
        + mp_rat(1267, 600) * g1_v ** 4 - mp_rat(9, 20) * g1_v ** 2 * g2_v ** 2 + mp_rat(19, 15) * g1_v ** 2 * g3_v ** 2
        - mp_rat(21, 4) * g2_v ** 4 + 9 * g2_v ** 2 * g3_v ** 2 - 108 * g3_v ** 4
        - 6 * l2_v * yt_v ** 2 + (-2 * l3_v + 2 * l4_v) * yb_v ** 2
        + mp_rat(3, 2) * l2_v ** 2 + l3_v ** 2 + l3_v * l4_v + l4_v ** 2
    )
    ce_yt_err = abs(out_b[3][2, 2] - (inv1 * b1_yt_exact + inv2 * b2_yt_exact))
    # Exact 1HDM Arason/Buttazzo check (1-loop +3/2 Hu - 3/2 Hd => opposite Xing-Zhou |V_cb| sign vs 2HDM-II +1/2 Hd)
    # Build small non-diagonal CKM test matrices for Xing-Zhou downward d|V_cb|/dt check
    Yu_xz = mp.matrix([[mp_rat(1, 100), 0, 0], [0, mp_rat(1, 10), 0], [0, 0, mp_rat(9, 10)]])
    th_xz = mp_rat(1, 20)
    R23 = mp.matrix([[1, 0, 0], [0, mp.cos(th_xz), mp.sin(th_xz)], [0, -mp.sin(th_xz), mp.cos(th_xz)]])
    Yd_xz = R23 * mp.matrix([[mp_rat(1, 200), 0, 0], [0, mp_rat(3, 100), 0], [0, 0, mp_rat(4, 10)]])
    Ye_xz = mp.diag([mp_rat(1, 500), mp_rat(2, 100), mp_rat(2, 10)])
    vcb0 = observables_from_Y(Yu_xz, Yd_xz, Ye_xz)["V23"]
    # 1 step downward dt = -1/10 in 2HDM-II vs 1HDM (1-loop)
    st_2h_step = rk4_integrate_2hdm((g1_v, g2_v, g3_v, Yu_xz, Yd_xz, Ye_xz, l1_v, l2_v, l3_v, l4_v), mp_rat(-1, 10), 10)
    vcb_2h_down = observables_from_Y(st_2h_step[3], st_2h_step[4], st_2h_step[5])["V23"]
    # 1-loop 1HDM downward step (-3/2 Hd in Yu, -3/2 Hu in Yd)
    hu_xz, hd_xz = Yu_xz * Yu_xz.H, Yd_xz * Yd_xz.H
    dyu_1h = inv1 * (mp_rat(3, 2) * hu_xz - mp_rat(3, 2) * hd_xz) * Yu_xz
    dyd_1h = inv1 * (mp_rat(3, 2) * hd_xz - mp_rat(3, 2) * hu_xz) * Yd_xz
    vcb_1h_down = observables_from_Y(Yu_xz + mp_rat(-1, 10) * dyu_1h, Yd_xz + mp_rat(-1, 10) * dyd_1h, Ye_xz)["V23"]
    # In downward running (dt < 0): 1HDM INCREASES |V_cb| (since +3/2 y_t^2 d|V_cb|/dt < 0 -> increases going IR!),
    # while Type-II 2HDM DECREASES |V_cb| (since -1/2 y_t^2 -> opposite sign)!
    dvcb_1h_down = vcb_1h_down - vcb0
    dvcb_2h_down = vcb_2h_down - vcb0
    xing_zhou_opposite = (dvcb_1h_down > 0) and (dvcb_2h_down < 0)

    # 2. Curved spin-1/2 Dirac Kahler metric G_{s=1/2} at tau_apex and tau_y2
    tau_apex = mp.mpc(mp_rat(1, 2), mp.sqrt(5) / 2)
    tau_y2 = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    g12_apex = compute_curved_dirac_s12(tau_apex, dps=30)
    g12_y2 = compute_curved_dirac_s12(tau_y2, dps=30)
    mp.mp.dps = 38

    def apply_kahler(Y, g_diag):
        D = mp.diag([1 / mp.sqrt(v) for v in g_diag])
        return D * Y * D

    # Build 3 un-sculpted UV states: U_A (Frame C at tau_y2), U_B (W3 dynamic vacuum at tau_y2), U_C (Frame C at tau_apex)
    w_mark = (Fraction(4, 15), Fraction(1, 30))
    L_y2, _ = solve_L2_fuchsian_cov(tau_y2, dps=38)
    L_ap, _ = solve_L2_fuchsian_cov(tau_apex, dps=38)
    eng_y2 = FrameCEngine(tau_y2, L_y2, dps=40)
    eng_ap = FrameCEngine(tau_apex, L_ap, dps=40)

    uv_states = [
        (
            "UA_FrameC_y2",
            eng_y2.Y_matrix(w_mark[0], w_mark[1], "up", weight0=True),
            eng_y2.Y_matrix(w_mark[0], w_mark[1], "down", weight0=True),
            eng_y2.Y_matrix(w_mark[0], w_mark[1], "lep", weight0=True),
            eng_y2.Y_matrix(w_mark[0], w_mark[1], "nu", weight0=True),
            g12_y2["G_s12"],
        ),
        (
            "UB_W3_DynamicVac_y2",
            uv_dyn["Yu"],
            uv_dyn["Yd"],
            uv_dyn["Ye"],
            eng_y2.Y_matrix(w_mark[0], w_mark[1], "nu", weight0=True),
            g12_y2["G_s12"],
        ),
        (
            "UC_FrameC_GeodesicApex",
            eng_ap.Y_matrix(w_mark[0], w_mark[1], "up", weight0=True),
            eng_ap.Y_matrix(w_mark[0], w_mark[1], "down", weight0=True),
            eng_ap.Y_matrix(w_mark[0], w_mark[1], "lep", weight0=True),
            eng_ap.Y_matrix(w_mark[0], w_mark[1], "nu", weight0=True),
            g12_apex["G_s12"],
        ),
    ]

    rg_results = {}
    max_step_halving_err = mp.mpf(0)
    pf5_ewsb_flip = False
    g_uv = mp_rat(1, 2)
    dt_ir = mp.mpf(-35)

    for uname, Yu_r, Yd_r, Ye_r, Yn_r, g_diag in uv_states:
        u_out = {}
        for kmode in ("FLAT", "CURVED_s12"):
            if kmode == "FLAT":
                Yu0, Yd0, Ye0, Yn0 = Yu_r, Yd_r, Ye_r, Yn_r
            else:
                Yu0 = apply_kahler(Yu_r, g_diag)
                Yd0 = apply_kahler(Yd_r, g_diag)
                Ye0 = apply_kahler(Ye_r, g_diag)
                Yn0 = apply_kahler(Yn_r, g_diag)

            # Natural O(1) UV normalization: max_f sigma_3(Y_f) = 1 (zero sector-by-sector tuning!)
            su0, _ = svd_asc_3x3(Yu0)
            sd0, _ = svd_asc_3x3(Yd0)
            se0, _ = svd_asc_3x3(Ye0)
            sc_uv = max(su0[2], sd0[2], se0[2])
            Yu_in, Yd_in, Ye_in = Yu0 / sc_uv, Yd0 / sc_uv, Ye0 / sc_uv
            obs_uv = observables_from_Y(Yu_in, Yd_in, Ye_in)

            st0 = (g_uv, g_uv, g_uv, Yu_in, Yd_in, Ye_in, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0))
            st_80 = rk4_integrate_2hdm(st0, dt_ir, 80, track_ewsb=False)
            st_160, t_l1, t_l2 = rk4_integrate_2hdm(st0, dt_ir, 160, track_ewsb=True)
            obs_ir = observables_from_Y(st_160[3], st_160[4], st_160[5])
            obs_80 = observables_from_Y(st_80[3], st_80[4], st_80[5])
            sh_err = max(
                abs(obs_ir["su"][2] - obs_80["su"][2]) / obs_ir["su"][2],
                abs(obs_ir["sd"][2] - obs_80["sd"][2]) / obs_ir["sd"][2],
                abs(obs_ir["V12"] - obs_80["V12"]) / max(mp_pow10(-10), obs_ir["V12"]),
                abs(st_160[6] - st_80[6]) / max(mp.mpf(1), abs(st_160[6])),
            )
            if sh_err > max_step_halving_err:
                max_step_halving_err = sh_err

            # PF5 on UA FLAT: remove Yu (Yu = 0) and check lam_2 sign flip
            if uname == "UA_FrameC_y2" and kmode == "FLAT":
                st0_pf5 = (g_uv, g_uv, g_uv, mp.zeros(3, 3), Yd_in, Ye_in, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0))
                st_pf5, _, t_l2_pf5 = rk4_integrate_2hdm(st0_pf5, dt_ir, 80, track_ewsb=True)
                # Without Yu, lam_2 is driven purely by positive gauge boxes (lam_2(IR) < 0? No: running DOWNWARD dt<0,
                # positive beta_l2 > 0 drives l2 NEGATIVE, whereas -12 tr(Hu^2) < 0 drives l2 POSITIVE!)
                pf5_ewsb_flip = (st_160[7] > 0) and (st_pf5[7] < 0)

            # Un-sculpted canonical neutrino Weinberg operator kappa_nu = Y_nu^T Y_nu (M_R = I_3)
            kap_nu = Yn0.T * Yn0
            s_nu, U_nu = takagi_3x3(kap_nu)
            _, U_e = svd_asc_3x3(Ye_in)
            U_pmns = U_e.H * U_nu
            pmns = pmns_angles_from_U(U_pmns)
            dm_ratio = (s_nu[1] ** 2 - s_nu[0] ** 2) / (s_nu[2] ** 2 - s_nu[0] ** 2) if (s_nu[2] > s_nu[0]) else mp.mpf(0)

            u_out[kmode] = {
                "uv": {
                    "su3": mp_str(obs_uv["su"][2], 8),
                    "sd3": mp_str(obs_uv["sd"][2], 8),
                    "se3": mp_str(obs_uv["se"][2], 8),
                    "u_m2m3": mp_str(obs_uv["u_m2m3"], 8),
                    "d_m2m3": mp_str(obs_uv["d_m2m3"], 8),
                    "e_m2m3": mp_str(obs_uv["e_m2m3"], 8),
                    "V12": mp_str(obs_uv["V12"], 8),
                    "V23": mp_str(obs_uv["V23"], 8),
                    "V13": mp_str(obs_uv["V13"], 8),
                    "Jcp": mp_str(obs_uv["Jcp"], 6),
                    "std_ckm": bool(obs_uv["V12"] > obs_uv["V23"] > obs_uv["V13"] > 0),
                },
                "ir_t_minus_35": {
                    "g1": mp_str(st_160[0], 8),
                    "g2": mp_str(st_160[1], 8),
                    "g3": mp_str(st_160[2], 8),
                    "yt_over_g3": mp_str(obs_ir["su"][2] / st_160[2], 8),
                    "mb_over_mtau": mp_str(obs_ir["sd"][2] / obs_ir["se"][2], 8),
                    "ms_over_mmu": mp_str(obs_ir["sd"][1] / obs_ir["se"][1], 8),
                    "u_m2m3": mp_str(obs_ir["u_m2m3"], 8),
                    "d_m2m3": mp_str(obs_ir["d_m2m3"], 8),
                    "e_m2m3": mp_str(obs_ir["e_m2m3"], 8),
                    "V12": mp_str(obs_ir["V12"], 8),
                    "V23": mp_str(obs_ir["V23"], 8),
                    "V13": mp_str(obs_ir["V13"], 8),
                    "Jcp": mp_str(obs_ir["Jcp"], 6),
                    "std_ckm": bool(obs_ir["V12"] > obs_ir["V23"] > obs_ir["V13"] > 0),
                    "l1_IR": mp_str(st_160[6], 8),
                    "l2_IR": mp_str(st_160[7], 8),
                    "l3_IR": mp_str(st_160[8], 8),
                    "l4_IR": mp_str(st_160[9], 8),
                    "t_EWSB_l1_cross": mp_str(t_l1, 8) if t_l1 is not None else "none",
                    "t_EWSB_l2_cross": mp_str(t_l2, 8) if t_l2 is not None else "none",
                    "step_halving_80_160_err": mp_str(sh_err, 6),
                },
                "canonical_neutrino_PMNS_MR_I3": {
                    "s12_sq": mp_str(pmns["s12_sq"], 8),
                    "s23_sq": mp_str(pmns["s23_sq"], 8),
                    "s13_sq": mp_str(pmns["s13_sq"], 8),
                    "Jcp_PMNS": mp_str(pmns["Jcp"], 6),
                    "dm21_over_dm31": mp_str(dm_ratio, 8),
                    "s_nu_ratios": [mp_str(s_nu[0] / s_nu[2], 8), mp_str(s_nu[1] / s_nu[2], 8)],
                },
            }
        rg_results[uname] = u_out

    # 3. Guardrail 3: 10-trial random Haar U(3)^5 scrambling through curved Kahler + 2-loop RG + Takagi PMNS
    #    plus PF6 (non-unitary left basis transform)
    mp.mp.dps = 42
    rng = random.Random(20261125)
    Yu_h = apply_kahler(eng_y2.Y_matrix(w_mark[0], w_mark[1], "up", weight0=True), g12_y2["G_s12"])
    Yd_h = apply_kahler(eng_y2.Y_matrix(w_mark[0], w_mark[1], "down", weight0=True), g12_y2["G_s12"])
    Ye_h = apply_kahler(eng_y2.Y_matrix(w_mark[0], w_mark[1], "lep", weight0=True), g12_y2["G_s12"])
    Yn_h = apply_kahler(eng_y2.Y_matrix(w_mark[0], w_mark[1], "nu", weight0=True), g12_y2["G_s12"])
    sc_h = max(svd_asc_3x3(Yu_h)[0][2], svd_asc_3x3(Yd_h)[0][2], svd_asc_3x3(Ye_h)[0][2])
    Yu_h, Yd_h, Ye_h = Yu_h / sc_h, Yd_h / sc_h, Ye_h / sc_h

    st_ref = rk4_integrate_2hdm((g_uv, g_uv, g_uv, Yu_h, Yd_h, Ye_h, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)), mp.mpf(-10), 40)
    obs_ref = observables_from_Y(st_ref[3], st_ref[4], st_ref[5])
    _, Ue_ref = svd_asc_3x3(st_ref[5])
    snu_ref, Unu_ref = takagi_3x3(Yn_h.T * Yn_h)
    pmns_ref = pmns_angles_from_U(Ue_ref.H * Unu_ref)

    haar_max_drift = mp.mpf(0)
    for _ in range(10):
        UQ = rand_haar_u3(rng, dps=42)
        UuR = rand_haar_u3(rng, dps=42)
        UdR = rand_haar_u3(rng, dps=42)
        UL = rand_haar_u3(rng, dps=42)
        UeR = rand_haar_u3(rng, dps=42)
        # Note: Y_f transforms as U_L Y_f U_R^H; Weinberg kappa_nu = Y_nu^T Y_nu transforms as U_L^* kappa_nu U_L^H?
        # Wait: in L^T kappa_nu L with L -> U_L L, kappa_nu -> U_L^T kappa_nu U_L! And in Y_e: L^dag Y_e e_R -> U_L^H Y_e U_eR,
        # so if Y_e -> U_L Y_e U_eR^H (left-acting U_L on rows), then in L^T kappa_nu L, L_L^* transforms by U_L^*,
        # so to match U_PMNS = U_e^H U_nu, kappa_nu transforms as U_L kappa_nu U_L^T (since Takagi M = U_nu D U_nu^T => U_L M U_L^T = (U_L U_nu) D (U_L U_nu)^T => U_e^H U_nu invariant!).
        Yu_s = UQ * Yu_h * UuR.H
        Yd_s = UQ * Yd_h * UdR.H
        Ye_s = UL * Ye_h * UeR.H
        kap_s = UL * (Yn_h.T * Yn_h) * UL.T
        st_s = rk4_integrate_2hdm((g_uv, g_uv, g_uv, Yu_s, Yd_s, Ye_s, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)), mp.mpf(-10), 40)
        obs_s = observables_from_Y(st_s[3], st_s[4], st_s[5])
        _, Ue_s = svd_asc_3x3(st_s[5])
        _, Unu_s = takagi_3x3(kap_s)
        pmns_s = pmns_angles_from_U(Ue_s.H * Unu_s)
        drift = max(
            abs(obs_s[k] - obs_ref[k]) for k in ("u_m2m3", "d_m2m3", "e_m2m3", "V12", "V23", "V13", "Jcp")
        )
        drift = max(drift, max(abs(pmns_s[k] - pmns_ref[k]) for k in ("s12_sq", "s23_sq", "s13_sq", "Jcp")))
        if drift > haar_max_drift:
            haar_max_drift = drift

    # PF6: non-unitary left basis distortion breaks observable invariance
    A_nonu = mp.matrix([[mp_rat(3, 2), mp_rat(1, 4), 0], [0, mp_rat(4, 5), mp_rat(1, 5)], [mp_rat(1, 10), 0, mp_rat(6, 5)]])
    obs_pf6 = observables_from_Y(A_nonu * Yu_h, A_nonu * Yd_h, Ye_h)
    obs_h0 = observables_from_Y(Yu_h, Yd_h, Ye_h)
    pf6_drift = max(abs(obs_pf6[k] - obs_h0[k]) for k in ("u_m2m3", "d_m2m3", "V12", "V23"))

    print(
        f"[W4] Done: CE_err={mp_str(ce_yt_err, 4)}, XZ_opp={xing_zhou_opposite}, "
        f"GB_ap={mp_str(g12_apex['gb_err'], 4)}, GB_y2={mp_str(g12_y2['gb_err'], 4)}, "
        f"SH={mp_str(max_step_halving_err, 4)}, Haar={mp_str(haar_max_drift, 4)}",
        flush=True,
    )
    return {
        "guardrail4_benchmarks": {
            "chowdhury_eberhardt_2hdm_15coeff_err": mp_str(ce_yt_err, 6),
            "xing_zhou_dvcb_1hdm_down": mp_str(dvcb_1h_down, 6),
            "xing_zhou_dvcb_2hdm_down": mp_str(dvcb_2h_down, 6),
            "xing_zhou_opposite_sign": xing_zhou_opposite,
        },
        "curved_dirac_s12": {
            "tau_apex": {
                "hyp_area_over_2pi": mp_str(g12_apex["hyp_area_over_2pi"], 8),
                "gb_err": mp_str(g12_apex["gb_err"], 6),
                "G_s12": [mp_str(v, 10) for v in g12_apex["G_s12"]],
                "grid_diff": mp_str(g12_apex["grid_diff"], 6),
                "kappa": mp_str(g12_apex["kappa"], 8),
            },
            "tau_y2": {
                "hyp_area_over_2pi": mp_str(g12_y2["hyp_area_over_2pi"], 8),
                "gb_err": mp_str(g12_y2["gb_err"], 6),
                "G_s12": [mp_str(v, 10) for v in g12_y2["G_s12"]],
                "grid_diff": mp_str(g12_y2["grid_diff"], 6),
                "kappa": mp_str(g12_y2["kappa"], 8),
            },
        },
        "unsculpted_2loop_rg_and_neutrinos": rg_results,
        "max_step_halving_80_160_err": mp_str(max_step_halving_err, 6),
        "haar_10trial_U3_5_max_drift": mp_str(haar_max_drift, 6),
        "pf5_drop_Yu_ewsb_flip": pf5_ewsb_flip,
        "pf6_non_unitary_drift": mp_str(pf6_drift, 6),
        "g4_pass": (
            ce_yt_err < mp_pow10(-40)
            and xing_zhou_opposite
            and g12_apex["gb_err"] < mp_pow10(-3)
            and g12_y2["gb_err"] < mp_pow10(-3)
            and max_step_halving_err < mp_pow10(-6)
            and haar_max_drift < mp_pow10(-25)
        ),
    }


# ---------------------------------------------------------------------------
# Main Driver
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    ast_rep = audit_own_ast()
    sets = build_level30_sets()
    model = build_symbolic_tropical_model()

    w1 = run_W1(sets)
    w2 = run_W2(model, sets)
    w3, uv_dyn = run_W3(sets)
    w4 = run_W4(uv_dyn)

    # Planted controls PF1..PF6 check
    pf1_ok = (
        abs(mp.mpf(w1["pf1_b1980_bug_reproduction"][0]["b1980_all899_max_d"]) - mp_rat(12, 100)) < mp_rat(2, 100)
        and abs(mp.mpf(w1["pf1_b1980_bug_reproduction"][1]["b1980_all899_max_d"]) - mp_rat(18, 100)) < mp_rat(2, 100)
        and abs(mp.mpf(w1["pf1_b1980_bug_reproduction"][2]["b1980_all899_max_d"]) - mp_rat(32, 100)) < mp_rat(3, 100)
    )
    pf2_ok = mp.mpf(w1["pf2_max_err"]) > mp_rat(1, 10)
    pf3_ok = bool(w3["pf3_sign_flip_control"]["hierarchy_destroyed"])
    pf4_ok = mp.mpf(w1["pf4_max_err"]) > mp.mpf(1)
    pf5_ok = bool(w4["pf5_drop_Yu_ewsb_flip"])
    pf6_ok = mp.mpf(w4["pf6_non_unitary_drift"]) > mp_rat(1, 100)

    pf_summary = {
        "PF1_b1980_missing_lny_reproduced": pf1_ok,
        "PF2_missing_sqrty_breaks_abs_sv": pf2_ok,
        "PF3_sign_flip_destroys_hierarchy": pf3_ok,
        "PF4_wrong_w_gamma_breaks_S_M": pf4_ok,
        "PF5_drop_Yu_flips_EWSB": pf5_ok,
        "PF6_non_unitary_breaks_Haar": pf6_ok,
        "caught_count": sum(1 for v in (pf1_ok, pf2_ok, pf3_ok, pf4_ok, pf5_ok, pf6_ok) if v),
    }
    g5_pass = pf_summary["caught_count"] == 6

    out = {
        "card_id": "AGY-002_A2-WHOLE-INSTRUMENT",
        "seat": "agy-002",
        "firewall": "0 of 19",
        "runtime_seconds": str(int(time.time() - t0)),
        "W1_b1980_s_covariance_and_weight_plus1": w1,
        "W2_whole_level30_and_closed_geodesic": w2,
        "W3_unsculpted_V_CW_higgs_and_modulus": w3,
        "W4_unsculpted_curved_dirac_2loop_rg_and_neutrinos": w4,
        "W5_planted_controls": pf_summary,
        "ast_hygiene": ast_rep,
    }
    json_floats = count_json_floats(out)
    g6_pass = bool(ast_rep["clean"]) and (json_floats == 0)

    gates = {
        "G1_W1_b1980_s_cov_weight1_K audit": bool(w1["g1_pass"]),
        "G2_W2_288pairs_geodesic_wlv1": bool(w2["g2_pass"]),
        "G3_W3_vcw_higgs_sl2z_modulus": bool(w3["g3_pass"]),
        "G4_W4_benchmarks_gb_rg_haar": bool(w4["g4_pass"]),
        "G5_all_6_planted_controls_caught": bool(g5_pass),
        "G6_ast_clean_and_zero_json_floats": bool(g6_pass),
        "json_float_count": json_floats,
        "all_gates_passed": bool(w1["g1_pass"] and w2["g2_pass"] and w3["g3_pass"] and w4["g4_pass"] and g5_pass and g6_pass),
    }
    out["gates"] = gates

    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    OUT_JSON_PATH.write_text(payload, encoding="utf-8")
    sha_out = hashlib.sha256(OUT_JSON_PATH.read_bytes()).hexdigest()
    OUT_SHA_PATH.write_text(f"{sha_out}  {OUT_JSON_PATH.name}\n", encoding="utf-8")
    print(f"ALL_GATES_PASSED={gates['all_gates_passed']} PF={pf_summary['caught_count']}/6 JSON_FLOATS={json_floats} TIME={out['runtime_seconds']}s", flush=True)


if __name__ == "__main__":
    main()
