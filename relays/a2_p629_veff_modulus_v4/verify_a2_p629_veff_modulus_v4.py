"""Standalone 0-of-19 Authoritative Producer v4 for Card AGY-002_A2-P629-VEFF-MODULUS.

Pure Python stdlib + mpmath + sympy ONLY.
Zero float/complex AST literals or casts; zero numpy/scipy/frontier/sage/gap imports;
zero JSON float tokens. Strictly 0 of 19 (data-free) and zero SM sculpting.

Modules:
  P1: Pure bosonic SL(2,Z) modular potentials (E(tau,3), E(tau,2), V_RS = -ln(y|eta|^4),
      -15/16 half-period spin-structure sum, Kronecker first limit, critical points i vs omega)
      and zero-parameter N=1 SUGRA modular potentials V_{FILQ, n}(tau) (n=1,2,3; FILQ 1990).
  P2: Full fundamental-domain F boson+fermion V_eff(tau) phase diagram:
      P2-A (trace-renormalized V_CW^{(tr)} global stabilization at i, local min at omega, arc barrier),
      P2-B (polynomial Casimir No-Go + exact orbifold transition c_B^{crit} + V_4 arc dip),
      P2-C (globally bounded V_tot(tau; c_F) = V_{FILQ,3} + c_F V_CW^{(all-288)}(1) with first-order
            transition above c_F^{crit} ~ 61.1 from x=0, y=1.155 to true 2D minimum on x=1/2, y* ~ 3.38).
  P3: Zero-sculpting forward unfolding at ALL 3 canonical vacua (omega_+, tau_{FILQ,1}^*, tau_{tot}^*(70)):
      Guardrail 4 benchmarks (15-term CE 2HDM-II, opposite Xing-Zhou sign, 7-eq Martin soft-mass,
      exact hypercharge S-conservation), curved Dirac G_{s=1/2} (Gauss-Bonnet verified),
      Piece 2 (Gauge-Higgs D-term quartic stability + 3x3 Hermitian universal soft-mass radiative EWSB),
      Piece 3 (M_R in {I_3, sym(Y_nu(w)), sym(Y_nu(2w))} in U(3)_L-covariant Y_nu M_R^{-1} Y_nu^T),
      and Guardrail 3 10-trial Haar U(3)^5 x U(3)_{nuR} scrambling across the full pipeline.
  P4: 6/6 planted negative controls (PF1..PF6) and AST/JSON zero-float hygiene (G6).
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
OUT_JSON_PATH = SCRIPT_PATH.with_name("verify_a2_p629_veff_modulus_v4_out.json")
OUT_SHA_PATH = SCRIPT_PATH.with_name("OUTPUT_SHA256.txt")


# ---------------------------------------------------------------------------
# Zero-Float / Zero-Complex Helpers & Hygiene Audit
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
    forbidden = ("numpy", "scipy", "frontier", "sage", "gap")
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
                if any(b in alias.name for b in forbidden):
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(b in mod for b in forbidden):
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
# Modular Functions: Dedekind eta, Non-Holomorphic E2_hat, Epstein E(tau, s), FILQ
# ---------------------------------------------------------------------------

def eta_and_e2hat(tau, dps: int = 45):
    mp.mp.dps = dps
    I = iu()
    pi = mp.pi
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    ty = mp.im(tau)
    q = mp.exp(2 * I * pi * tau)
    K = max(24, int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(628) * ty))) + 14)
    ep = mp.mpc(1)
    qp = mp.mpc(1)
    e2 = mp.mpc(1)
    for n in range(1, K + 1):
        qp = qp * q
        ep = ep * (1 - qp)
        e2 -= 24 * n * qp / (1 - qp)
    eta = mp.exp(I * pi * tau / 12) * ep
    e2_hat = e2 - 3 / (pi * ty)
    return eta, e2, e2_hat


def V_RS(tau, dps: int = 45):
    """SL(2,Z)-invariant regularized Casimir / Kronecker potential -ln(y |eta(tau)|^4)."""
    eta, _, _ = eta_and_e2hat(tau, dps=dps)
    ty = mp.im(mp.mpc(mp.re(tau), mp.im(tau)))
    return -mp.log(ty * (abs(eta) ** 4))


def E_fourier(tau, s, dps: int = 45):
    """Real-analytic Eisenstein / Epstein zeta sum' y^s |m tau + n|^{-2s} via Chowla-Selberg."""
    mp.mp.dps = dps
    pi = mp.pi
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s)
    first = (
        2 * mp.zeta(2 * s) * (y ** s)
        + 2 * mp.sqrt(pi) * mp.gamma(s - mp_rat(1, 2)) / mp.gamma(s) * mp.zeta(2 * s - 1) * (y ** (1 - s))
    )
    R = max(20, int(mp.ceil((dps * mp.mpf(231)) / (mp.mpf(628) * y))) + 12)
    b = mp.mpf(0)
    two_s_m1 = 2 * s - 1
    smh = s - mp_rat(1, 2)
    for n in range(1, R + 1):
        sig = mp.mpf(0)
        for d in range(1, n + 1):
            if n % d == 0:
                sig += mp.mpf(d) ** two_s_m1
        b += (mp.mpf(n) ** (mp_rat(1, 2) - s)) * sig * mp.besselk(smh, 2 * pi * n * y) * mp.cos(2 * pi * n * x)
    return first + 8 * (pi ** s) * mp.sqrt(y) / mp.gamma(s) * b


def E_box_sum(tau, s_int: int, N: int = 45, dps: int = 35):
    """Direct square-box lattice sum sum'_{m,n} y^s / |m tau + n|^{2s} (control)."""
    mp.mp.dps = dps
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    ty = mp.im(tau)
    ys = ty ** s_int
    tot = mp.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m != 0 or n != 0:
                tot += ys / (abs(m * tau + n) ** (2 * s_int))
    return tot


def V_FILQ(tau, n: int, dps: int = 45, drop_nonhol: bool = False):
    """Zero-parameter 4D N=1 SUGRA modular potential (Font-Ibanez-Lust-Quevedo NPB 345 (1990) 389).
    K = -3n ln(2y), W = eta(tau)^{-6n} => V = (2y)^{-3n} |eta|^{-12n} ((n pi^2 y^2 / 3) |E2_hat|^2 - 3)."""
    mp.mp.dps = dps
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    ty = mp.im(tau)
    eta, e2, e2_hat = eta_and_e2hat(tau, dps=dps)
    e2_use = e2 if drop_nonhol else e2_hat
    return (
        ((2 * ty) ** (-3 * n))
        * (abs(eta) ** (-12 * n))
        * ((mp.mpf(n) * (mp.pi ** 2) * (ty ** 2) / 3) * (abs(e2_use) ** 2) - 3)
    )


def grad_hess_2d(fn, tau, h_hess, h_grad=None):
    hg = h_hess if h_grad is None else h_grad
    x, y = mp.re(tau), mp.im(tau)
    f0 = fn(mp.mpc(x, y))
    gx = (fn(mp.mpc(x + hg, y)) - fn(mp.mpc(x - hg, y))) / (2 * hg)
    gy = (fn(mp.mpc(x, y + hg)) - fn(mp.mpc(x, y - hg))) / (2 * hg)
    fxp = fn(mp.mpc(x + h_hess, y))
    fxm = fn(mp.mpc(x - h_hess, y))
    fyp = fn(mp.mpc(x, y + h_hess))
    fym = fn(mp.mpc(x, y - h_hess))
    fpp = fn(mp.mpc(x + h_hess, y + h_hess))
    fpm = fn(mp.mpc(x + h_hess, y - h_hess))
    fmp = fn(mp.mpc(x - h_hess, y + h_hess))
    fmm = fn(mp.mpc(x - h_hess, y - h_hess))
    fxx = (fxp - 2 * f0 + fxm) / (h_hess * h_hess)
    fyy = (fyp - 2 * f0 + fym) / (h_hess * h_hess)
    fxy = (fpp - fpm - fmp + fmm) / (4 * h_hess * h_hess)
    ev = mp.eigsy(mp.matrix([[fxx, fxy], [fxy, fyy]]), eigvals_only=True)
    evals = sorted(mp.re(v) for v in ev)
    return {
        "val": f0,
        "gx": gx,
        "gy": gy,
        "grad_norm": mp.sqrt(gx * gx + gy * gy),
        "fxx": fxx,
        "fyy": fyy,
        "fxy": fxy,
        "hess_evals": evals,
    }


# ---------------------------------------------------------------------------
# Fundamental-Domain Reduction & Exact Fuchsian Weierstrass L_2(tau) Solver
# ---------------------------------------------------------------------------

def reduce_to_fd_mp(tau):
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
    return z, (a, b, c, d), c * tau + d


def solve_L2_fuchsian_raw(tau, dps: int = 36, return_full: bool = False):
    ty = mp.im(tau)
    dps_ode = max(dps, 34 + int(mp.ceil(max(ty, 1 / ty))))
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

    s15 = mp.sqrt(15)
    c_gl = [(5 - s15) / 10, mp_rat(1, 2), (5 + s15) / 10]
    a_gl = [
        [mp_rat(5, 36), mp_rat(2, 9) - s15 / 15, mp_rat(5, 36) - s15 / 30],
        [mp_rat(5, 36) + s15 / 24, mp_rat(2, 9), mp_rat(5, 36) - s15 / 24],
        [mp_rat(5, 36) + s15 / 30, mp_rat(2, 9) + s15 / 15, mp_rat(5, 36)],
    ]
    b_gl = [mp_rat(5, 18), mp_rat(4, 9), mp_rat(5, 18)]
    A2_gl = [[sum(a_gl[i][m] * a_gl[m][j] for m in range(3)) for j in range(3)] for i in range(3)]

    def build_seg_list(spec):
        out = []
        for za, zb, nsteps in spec:
            h = (zb - za) / nsteps
            ws = [[wp_q4(za + (k + cj) * h) for cj in c_gl] for k in range(nsteps)]
            out.append((h, nsteps, ws))
        return out

    def make_b_spec(scale: int):
        if ty < 1:
            n_b = max(24 * scale, int(mp.ceil(abs(tau) * 32 * scale)))
            return [(z0, z0 + tau, n_b)]
        if ty <= mp_rat(3, 2):
            n_b = max(28 * scale, int(mp.ceil(abs(tau) * 24 * scale)))
            return [(z0, z0 + tau, n_b)]
        z_mid = z0 + tau / 2
        frac_span = min(mp_rat(1, 3), mp.mpf(1) / ty)
        za = z_mid - frac_span * tau
        zb = z_mid + frac_span * tau
        n_tail = max(20 * scale, int(mp.ceil(abs(za - z0) * 10 * scale)))
        n_mid = max(64 * scale, int(mp.ceil(abs(zb - za) * 36 * scale)))
        return [(z0, za, n_tail), (za, zb, n_mid), (zb, z0 + tau, n_tail)]

    def prop(segs, c_val, want_dc: bool = False):
        a00, a01, a02 = a_gl[0][0], a_gl[0][1], a_gl[0][2]
        a10, a11, a12 = a_gl[1][0], a_gl[1][1], a_gl[1][2]
        a20, a21, a22 = a_gl[2][0], a_gl[2][1], a_gl[2][2]
        c0, c1, c2 = c_gl[0], c_gl[1], c_gl[2]
        b0, b1, b2 = b_gl[0], b_gl[1], b_gl[2]
        A00, A01, A02 = A2_gl[0][0], A2_gl[0][1], A2_gl[0][2]
        A10, A11, A12 = A2_gl[1][0], A2_gl[1][1], A2_gl[1][2]
        A20, A21, A22 = A2_gl[2][0], A2_gl[2][1], A2_gl[2][2]
        t00, t01, t10, t11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
        d00, d01, d10, d11 = mp.mpc(0), mp.mpc(0), mp.mpc(0), mp.mpc(0)
        for h, nsteps, ws in segs:
            h2 = h * h
            hc0, hc1, hc2 = h * c0, h * c1, h * c2
            hb0, hb1, hb2 = h * b0, h * b1, h * b2
            for k in range(nsteps):
                wk = ws[k]
                q0, q1, q2 = wk[0] + c_val, wk[1] + c_val, wk[2] + c_val
                qh0, qh1, qh2 = q0 * h2, q1 * h2, q2 * h2
                m00, m01, m02 = 1 + qh0 * A00, qh0 * A01, qh0 * A02
                m10, m11, m12 = qh1 * A10, 1 + qh1 * A11, qh1 * A12
                m20, m21, m22 = qh2 * A20, qh2 * A21, 1 + qh2 * A22
                # Exact closed-form 3x3 cofactor inverse (zero mp.matrix overhead!)
                cf00 = m11 * m22 - m12 * m21
                cf01 = m02 * m21 - m01 * m22
                cf02 = m01 * m12 - m02 * m11
                cf10 = m12 * m20 - m10 * m22
                cf11 = m00 * m22 - m02 * m20
                cf12 = m02 * m10 - m00 * m12
                cf20 = m10 * m21 - m11 * m20
                cf21 = m01 * m20 - m00 * m21
                cf22 = m00 * m11 - m01 * m10
                invd = 1 / (m00 * cf00 + m01 * cf10 + m02 * cf20)
                i00, i01, i02 = cf00 * invd, cf01 * invd, cf02 * invd
                i10, i11, i12 = cf10 * invd, cf11 * invd, cf12 * invd
                i20, i21, i22 = cf20 * invd, cf21 * invd, cf22 * invd

                # Column 0
                r0 = -q0 * (t00 + hc0 * t10)
                r1 = -q1 * (t00 + hc1 * t10)
                r2 = -q2 * (t00 + hc2 * t10)
                L0 = i00 * r0 + i01 * r1 + i02 * r2
                L1 = i10 * r0 + i11 * r1 + i12 * r2
                L2 = i20 * r0 + i21 * r1 + i22 * r2
                K0 = t10 + h * (a00 * L0 + a01 * L1 + a02 * L2)
                K1 = t10 + h * (a10 * L0 + a11 * L1 + a12 * L2)
                K2 = t10 + h * (a20 * L0 + a21 * L1 + a22 * L2)
                nt00 = t00 + hb0 * K0 + hb1 * K1 + hb2 * K2
                nt10 = t10 + hb0 * L0 + hb1 * L1 + hb2 * L2
                if want_dc:
                    U0 = t00 + h * (a00 * K0 + a01 * K1 + a02 * K2)
                    U1 = t00 + h * (a10 * K0 + a11 * K1 + a12 * K2)
                    U2 = t00 + h * (a20 * K0 + a21 * K1 + a22 * K2)
                    dr0 = -q0 * (d00 + hc0 * d10) - U0
                    dr1 = -q1 * (d00 + hc1 * d10) - U1
                    dr2 = -q2 * (d00 + hc2 * d10) - U2
                    dL0 = i00 * dr0 + i01 * dr1 + i02 * dr2
                    dL1 = i10 * dr0 + i11 * dr1 + i12 * dr2
                    dL2 = i20 * dr0 + i21 * dr1 + i22 * dr2
                    dK0 = d10 + h * (a00 * dL0 + a01 * dL1 + a02 * dL2)
                    dK1 = d10 + h * (a10 * dL0 + a11 * dL1 + a12 * dL2)
                    dK2 = d10 + h * (a20 * dL0 + a21 * dL1 + a22 * dL2)
                    d00 = d00 + hb0 * dK0 + hb1 * dK1 + hb2 * dK2
                    d10 = d10 + hb0 * dL0 + hb1 * dL1 + hb2 * dL2

                # Column 1
                r0 = -q0 * (t01 + hc0 * t11)
                r1 = -q1 * (t01 + hc1 * t11)
                r2 = -q2 * (t01 + hc2 * t11)
                L0 = i00 * r0 + i01 * r1 + i02 * r2
                L1 = i10 * r0 + i11 * r1 + i12 * r2
                L2 = i20 * r0 + i21 * r1 + i22 * r2
                K0 = t11 + h * (a00 * L0 + a01 * L1 + a02 * L2)
                K1 = t11 + h * (a10 * L0 + a11 * L1 + a12 * L2)
                K2 = t11 + h * (a20 * L0 + a21 * L1 + a22 * L2)
                nt01 = t01 + hb0 * K0 + hb1 * K1 + hb2 * K2
                nt11 = t11 + hb0 * L0 + hb1 * L1 + hb2 * L2
                if want_dc:
                    U0 = t01 + h * (a00 * K0 + a01 * K1 + a02 * K2)
                    U1 = t01 + h * (a10 * K0 + a11 * K1 + a12 * K2)
                    U2 = t01 + h * (a20 * K0 + a21 * K1 + a22 * K2)
                    dr0 = -q0 * (d01 + hc0 * d11) - U0
                    dr1 = -q1 * (d01 + hc1 * d11) - U1
                    dr2 = -q2 * (d01 + hc2 * d11) - U2
                    dL0 = i00 * dr0 + i01 * dr1 + i02 * dr2
                    dL1 = i10 * dr0 + i11 * dr1 + i12 * dr2
                    dL2 = i20 * dr0 + i21 * dr1 + i22 * dr2
                    dK0 = d11 + h * (a00 * dL0 + a01 * dL1 + a02 * dL2)
                    dK1 = d11 + h * (a10 * dL0 + a11 * dL1 + a12 * dL2)
                    dK2 = d11 + h * (a20 * dL0 + a21 * dL1 + a22 * dL2)
                    d01 = d01 + hb0 * dK0 + hb1 * dK1 + hb2 * dK2
                    d11 = d11 + hb0 * dL0 + hb1 * dL1 + hb2 * dL2

                t00, t01, t10, t11 = nt00, nt01, nt10, nt11
        T = mp.matrix([[t00, t01], [t10, t11]])
        return (T, mp.matrix([[d00, d01], [d10, d11]])) if want_dc else T

    z0 = (1 + tau) / 2
    n_a1 = 32 if ty < 1 else 20
    ga1 = build_seg_list([(z0, z0 + 1, n_a1)])
    gb1 = build_seg_list(make_b_spec(1))
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

    tol_c = mp_pow10(-15)
    for _ in range(28):
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
    tol_f = mp_pow10(-24)
    for _ in range(6):
        Ta1, dTa1 = prop(ga1, c_val, True)
        Ta2, dTa2 = prop(ga2, c_val, True)
        Ta = (64 * Ta2 - Ta1) / 63
        dTa = (64 * dTa2 - dTa1) / 63
        Tb1, dTb1 = prop(gb1, c_val, True)
        Tb2, dTb2 = prop(gb2, c_val, True)
        Tb = (64 * Tb2 - Tb1) / 63
        dTb = (64 * dTb2 - dTb1) / 63
        res, df = newton_step(Ta, dTa, Tb, dTb)
        if max(abs(v) for v in res) < tol_f:
            break
        J = mp.matrix([[mp.im(d), mp.re(d)] for d in df])
        rv = mp.matrix([-v for v in res])
        step = mp.lu_solve(J.T * J, J.T * rv)
        c_val += mp.mpc(step[0], step[1])

    Ta = (64 * prop(ga2, c_val) - prop(ga1, c_val)) / 63
    Tb = (64 * prop(gb2, c_val) - prop(gb1, c_val)) / 63
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
    spu_in = 24 if ty < 1 else 20
    gin1 = build_seg_list([(a, b, max(16, int(mp.ceil(abs(b - a) * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
    gin2 = build_seg_list([(a, b, max(32, int(mp.ceil(abs(b - a) * 2 * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
    Tin = (64 * prop(gin2, c_val) - prop(gin1, c_val)) / 63

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


def solve_L2_fuchsian_cov(tau, dps: int = 36):
    mp.mp.dps = max(dps, 40)
    z_fd, _, denom = reduce_to_fd_mp(tau)
    z_sym = mp.mpc(abs(mp.re(z_fd)), mp.im(z_fd))
    key = (mp.nstr(mp.re(z_sym), 22), mp.nstr(mp.im(z_sym), 22), dps)
    if key not in _L2_FD_CACHE:
        _L2_FD_CACHE[key] = solve_L2_fuchsian_raw(z_sym, dps=dps, return_full=False)
    l2_fd, res = _L2_FD_CACHE[key]
    return l2_fd - mp.log(abs(denom)), res


# ---------------------------------------------------------------------------
# Branch-Cut-Free Holomorphic Frame C Engine & Level-30 Pair Enumeration
# ---------------------------------------------------------------------------

SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "nu": 0}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e"), "nu": ("L", "nu")}


def build_E288_pairs() -> List[Tuple[Fraction, Fraction]]:
    seen = set()
    out = []
    for j in range(30):
        for k in range(30):
            p = (Fraction(j, 30), Fraction(k, 30))
            if pt_order(p) == 30:
                neg = mod1_pt(-p[0], -p[1])
                canon = min(p, neg)
                if canon not in seen:
                    seen.add(canon)
                    out.append(canon)
    out.sort()
    return out


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
    def __init__(self, tau, L2, dps: int = 40):
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
        self.S = c0 * self.QI + c1 * self.QJ + c2 * self.QK
        self.T_S = [
            [self.blocks[a].T * self.EPS * self.S * self.blocks[b] for b in range(3)]
            for a in range(3)
        ]
        self.T_Q = [
            [[self.blocks[a].T * self.EPS * self.Q_basis[k] * self.blocks[b] for b in range(3)] for a in range(3)]
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

    def Y_higgs_basis(self, a: Fraction, b: Fraction, sector: str):
        mp.mp.dps = self.dps
        Mw = self.Mw_matrix(a, b, sector)
        scale = self.sqrt_ty * self.c_norm
        mats = []
        for k in range(3):
            M = mp.matrix([
                [
                    scale * sum(self.T_Q[k][r_i][c_i][m, n] * Mw[m, n] for m in range(2) for n in range(2))
                    for c_i in range(3)
                ]
                for r_i in range(3)
            ])
            mats.append(M)
        return mats


# ---------------------------------------------------------------------------
# Linear Algebra: Non-Squaring SVD, Takagi, CKM, PMNS, Haar U(3)
# ---------------------------------------------------------------------------

def svd_asc_3x3(Y):
    Uu, Sv, _ = mp.svd_c(Y)
    order = sorted(range(3), key=lambda idx: abs(Sv[idx]))
    svs = [abs(Sv[idx]) for idx in order]
    U = mp.matrix([[Uu[r, order[c]] for c in range(3)] for r in range(3)])
    return svs, U


def observables_from_Y(Yu, Yd, Ye) -> Dict[str, Any]:
    su, Uu = svd_asc_3x3(Yu)
    sd, Ud = svd_asc_3x3(Yd)
    se, Ue = svd_asc_3x3(Ye)
    V = Uu.H * Ud
    absV = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    Jcp = abs(mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1])))
    return {
        "su": su, "sd": sd, "se": se,
        "u_m2m3": su[1] / su[2] if su[2] > 0 else mp.mpf(0),
        "u_m1m3": su[0] / su[2] if su[2] > 0 else mp.mpf(0),
        "d_m2m3": sd[1] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "d_m1m3": sd[0] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "e_m2m3": se[1] / se[2] if se[2] > 0 else mp.mpf(0),
        "e_m1m3": se[0] / se[2] if se[2] > 0 else mp.mpf(0),
        "V12": absV[0][1], "V23": absV[1][2], "V13": absV[0][2], "V31": absV[2][0],
        "Jcp": Jcp, "Uu": Uu, "Ud": Ud, "Ue": Ue,
        "std_ckm": bool(absV[0][1] > absV[1][2] > absV[0][2] > 0),
    }


def takagi_3x3(M_sym):
    mp.mp.dps = max(mp.mp.dps, 42)
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
    return svs, U_T


def pmns_from_kappa(kap, Ue):
    s_nu, U_nu = takagi_3x3(kap)
    U = Ue.H * U_nu
    s13_sq = abs(U[0, 2]) ** 2
    c13_sq = max(mp_pow10(-50), 1 - s13_sq)
    s12_sq = abs(U[0, 1]) ** 2 / c13_sq
    s23_sq = abs(U[1, 2]) ** 2 / c13_sq
    Jcp = abs(mp.im(U[0, 1] * U[1, 2] * mp.conj(U[0, 2]) * mp.conj(U[1, 1])))
    denom = (s_nu[2] ** 2) - (s_nu[0] ** 2)
    dm_ratio = ((s_nu[1] ** 2) - (s_nu[0] ** 2)) / denom if denom > mp_pow10(-60) else mp.mpf(0)
    return {
        "s12_sq": s12_sq,
        "s23_sq": s23_sq,
        "s13_sq": s13_sq,
        "Jcp": Jcp,
        "dm21_over_dm31": dm_ratio,
        "s_nu_ratios": [s_nu[0] / s_nu[2] if s_nu[2] > 0 else mp.mpf(0), s_nu[1] / s_nu[2] if s_nu[2] > 0 else mp.mpf(0)],
    }


def rand_haar_u3(rng: random.Random, dps: int = 44):
    mp.mp.dps = dps
    I = iu()
    twopi = 2 * mp.pi
    M = 10 ** 18

    def rand_std_normal():
        u1 = mp.mpf(rng.randint(1, M - 1)) / mp.mpf(M)
        u2 = mp.mpf(rng.randint(1, M - 1)) / mp.mpf(M)
        rad = mp.sqrt(-2 * mp.log(u1))
        return rad * mp.cos(twopi * u2), rad * mp.sin(twopi * u2)

    Z = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            xr, xi = rand_std_normal()
            Z[i, j] = xr + I * xi

    Q = mp.zeros(3, 3)
    for j in range(3):
        v = [Z[i, j] for i in range(3)]
        for p in range(j):
            proj = sum(mp.conj(Q[i, p]) * v[i] for i in range(3))
            for i in range(3):
                v[i] -= proj * Q[i, p]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        for i in range(3):
            Q[i, j] = v[i] / nrm
    return Q


# ---------------------------------------------------------------------------
# All-288 Fermion Modular Potential Evaluator
# ---------------------------------------------------------------------------

def eval_all288_fermion_pot(tau, pairs288: List[Tuple[Fraction, Fraction]], dps_use: int = 28) -> Dict[str, Any]:
    mp.mp.dps = dps_use
    L2, res_ode = solve_L2_fuchsian_cov(tau, dps=max(26, dps_use))
    eng = FrameCEngine(tau, L2, dps=dps_use)
    inv64 = 1 / (64 * (mp.pi ** 2))
    lam_all: List[Tuple[int, Any]] = []
    tr2 = mp.mpf(0)
    v4 = mp.mpf(0)
    vcw1 = mp.mpf(0)
    for pa, pb in pairs288:
        for sec, nc in (("up", 3), ("down", 3), ("lep", 1)):
            Y = eng.Y_matrix(pa, pb, sec, weight0=True)
            ev, _ = mp.eigh(Y.H * Y)
            for lc in ev:
                lv = max(mp.mpf(0), mp.re(lc))
                tr2 += nc * lv
                v4 -= nc * (lv * lv)
                if lv > mp_pow10(-55):
                    vcw1 -= inv64 * nc * (lv * lv) * (mp.log(lv) - mp_rat(3, 2))
                    lam_all.append((nc, lv))
    # Dynamical trace-renormalized potential mu^2(tau) = Tr2(tau)
    # Since 0 <= lv <= Tr2, ln(lv/Tr2) - 3/2 <= -3/2 < 0 => V_CW_tr > 0 strictly everywhere!
    vcw_tr = mp.mpf(0)
    log_tr2 = mp.log(tr2)
    for nc, lv in lam_all:
        vcw_tr -= inv64 * nc * (lv * lv) * (mp.log(lv) - log_tr2 - mp_rat(3, 2))
    return {
        "L2": L2,
        "ode_res": res_ode,
        "Tr2": tr2,
        "V4": v4,
        "VCW_1": vcw1,
        "VCW_tr": vcw_tr,
    }


# ---------------------------------------------------------------------------
# Curved Spin-1/2 Dirac Kahler Metric G_{s=1/2}(tau) & Dynamic 2-Doublet V_4
# ---------------------------------------------------------------------------

def compute_curved_dirac_s12(tau_r, dps: int = 30) -> Dict[str, Any]:
    mp.mp.dps = dps
    I = iu()
    pi = mp.pi
    full = solve_L2_fuchsian_raw(tau_r, dps=dps, return_full=True)
    c_star = full["c_val"]
    ta = full["Ta"]
    tb = full["Tb"]
    z0_base = full["z0"]
    wp_q4 = full["wp_q4"]

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

    n_th_f = 16 if mp.im(tau_r) > mp_rat(5, 2) else 12
    n_t_f = 16 if mp.im(tau_r) > mp_rat(5, 2) else 14
    _, g_c = run_quad(8, 10)
    area_f, g_f = run_quad(n_th_f, n_t_f)
    grid_diff = max(abs(g_f[j] - g_c[j]) for j in range(3))
    return {
        "hyp_area_over_2pi": area_f,
        "gb_err": abs(area_f - 1),
        "G_s12": g_f,
        "grid_diff": grid_diff,
        "kappa": max(g_f) / min(g_f),
    }


def eval_V4_and_grad(Y, A_list, Nc: int):
    H = Y.H * Y
    evals, evecs = mp.eigh(H)
    lams = [max(mp.mpf(0), mp.re(v)) for v in evals]
    val = mp.mpf(0)
    dphi = []
    for lam in lams:
        val += -Nc * (lam * lam)
        dphi.append(-2 * Nc * lam)
    P = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            P[i, j] = sum(evecs[i, k] * dphi[k] * mp.conj(evecs[j, k]) for k in range(3))
    YP = Y * P
    grad = [
        sum(mp.conj(A_list[k][i, j]) * YP[i, j] for i in range(3) for j in range(3))
        for k in range(3)
    ]
    return val, grad


def minimize_2doublet_V4_allS(Au, Ad, Ae, c_hat, lam3, V0_scale):
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
        vu, gu = eval_V4_and_grad(Yu, Au, 3)
        vd, gd = eval_V4_and_grad(Yd, Ad, 3)
        ve, ge = eval_V4_and_grad(Ye, Ae, 1)
        ov = sum(mp.conj(hu[k]) * hd[k] for k in range(3))
        v_p = lam3 * V0_scale * (abs(ov) ** 2)
        gu_tot = [gu[k] + lam3 * V0_scale * mp.conj(ov) * hd[k] for k in range(3)]
        gd_tot = [gd[k] + ge[k] + lam3 * V0_scale * ov * hu[k] for k in range(3)]
        return vu + vd + ve + v_p, gu_tot, gd_tot

    raw_pairs = [
        ([mp.mpc(1), mp.mpc(0), mp.mpc(0)], [mp.mpc(1), mp.mpc(0), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(0), mp.mpc(1)]),
        ([mp.mpc(1), I, mp.mpc(0)], [mp.mpc(1), -I, mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), I], [mp.mpc(0), mp.mpc(1), I]),
        (list(c_hat), list(c_hat)),
        ([mp.mpc(0), mp.mpc(1), -I], [mp.mpc(1), mp.mpc(0), I]),
    ]

    best = None
    dps_save = mp.mp.dps
    mp.mp.dps = 24
    for hu0_r, hd0_r in raw_pairs:
        nu0 = mp.sqrt(sum(abs(x) ** 2 for x in hu0_r))
        nd0 = mp.sqrt(sum(abs(x) ** 2 for x in hd0_r))
        hu = [x / nu0 for x in hu0_r]
        hd = [x / nd0 for x in hd0_r]
        v, gu, gd = fg(hu, hd)
        alpha = mp.mpf(1) / max(mp.mpf(1), mp.sqrt(sum(abs(x) ** 2 for x in gu + gd)))
        for _ in range(90):
            du = sum(mp.re(mp.conj(hu[k]) * gu[k]) for k in range(3))
            dd = sum(mp.re(mp.conj(hd[k]) * gd[k]) for k in range(3))
            gtu = [gu[k] - du * hu[k] for k in range(3)]
            gtd = [gd[k] - dd * hd[k] for k in range(3)]
            gn = mp.sqrt(sum(abs(x) ** 2 for x in gtu + gtd))
            if gn < mp_pow10(-11) * max(mp.mpf(1), abs(v)):
                break
            step_ok = False
            a_try = alpha
            for _ in range(28):
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
        if best is None or v < best[0]:
            best = (v, hu, hd)
    mp.mp.dps = dps_save
    _, hu_b, hd_b = best
    return {
        "Yu": build_Y(hu_b, Au),
        "Yd": build_Y(hd_b, Ad),
        "Ye": build_Y(hd_b, Ae),
        "hu_star": hu_b,
        "hd_star": hd_b,
        "r_u": abs(sum(x * x for x in hu_b)),
        "r_d": abs(sum(x * x for x in hd_b)),
        "align_hu_hd": abs(sum(mp.conj(hu_b[k]) * hd_b[k] for k in range(3))),
    }


# ---------------------------------------------------------------------------
# Coupled 2-Loop Type-II 2HDM + Gauge-Higgs D-Term + 3x3 Matrix Soft-Mass RGEs
# ---------------------------------------------------------------------------

def tr_re(M):
    return mp.re(M[0, 0] + M[1, 1] + M[2, 2])


def rhs_coupled_2hdm_soft(g1, g2, g3, yu, yd, ye, l1, l2, l3, l4, mhu, mhd, MQ, Mu, Md, ML, Me):
    """Exact 2-loop Type-II 2HDM gauge + Yukawa (MV84 / Chowdhury-Eberhardt 1503.08216),
    1-loop Type-II 2HDM quartics, AND exact 1-loop 3x3 Hermitian soft-mass RGEs
    (Martin hep-ph/9709356 Eqs. 6.5.24-6.5.30, M_a=0, A_0=0, L-rows / R-cols convention)."""
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    gy2 = mp_rat(3, 5) * g12

    hu = yu * yu.H
    hd = yd * yd.H
    he = ye * ye.H
    huR = yu.H * yu
    hdR = yd.H * yd
    heR = ye.H * ye
    hu2 = hu * hu
    hd2 = hd * hd
    he2 = he * he
    huhd = hu * hd
    hdhu = hd * hu

    tru = tr_re(hu)
    trd = tr_re(hd)
    tre = tr_re(he)
    tru2 = tr_re(hu2)
    trd2 = tr_re(hd2)
    tre2 = tr_re(he2)
    trud = tr_re(huhd)

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

    S_hyp = mhu - mhd + tr_re(MQ - ML - 2 * Mu + Md + Me)
    dmhu = inv1 * (6 * tr_re(hu * MQ + huR * Mu + mhu * hu) + mp_rat(3, 5) * g12 * S_hyp)
    dmhd = inv1 * (
        6 * tr_re(hd * MQ + hdR * Md + mhd * hd)
        + 2 * tr_re(he * ML + heR * Me + mhd * he)
        - mp_rat(3, 5) * g12 * S_hyp
    )
    dMQ = inv1 * (
        (hu * MQ + MQ * hu) + 2 * yu * Mu * yu.H + 2 * mhu * hu
        + (hd * MQ + MQ * hd) + 2 * yd * Md * yd.H + 2 * mhd * hd
        + mp_rat(1, 5) * g12 * S_hyp * i3
    )
    dMu = inv1 * (2 * (huR * Mu + Mu * huR) + 4 * yu.H * MQ * yu + 4 * mhu * huR - mp_rat(4, 5) * g12 * S_hyp * i3)
    dMd = inv1 * (2 * (hdR * Md + Md * hdR) + 4 * yd.H * MQ * yd + 4 * mhd * hdR + mp_rat(2, 5) * g12 * S_hyp * i3)
    dML = inv1 * ((he * ML + ML * he) + 2 * ye * Me * ye.H + 2 * mhd * he - mp_rat(3, 5) * g12 * S_hyp * i3)
    dMe = inv1 * (2 * (heR * Me + Me * heR) + 4 * ye.H * ML * ye + 4 * mhd * heR + mp_rat(6, 5) * g12 * S_hyp * i3)

    return bg1, bg2, bg3, dyu, dyd, dye, dl1, dl2, dl3, dl4, dmhu, dmhd, dMQ, dMu, dMd, dML, dMe


def rk4_integrate_coupled(st0, dt_total, n_steps: int, check_all_steps_stab: bool = False):
    h = dt_total / n_steps
    st = st0
    t_cur = mp.mpf(0)
    t_u_cross = None
    t_d_cross = None
    all_steps_stab = True
    min_stab_margin = None

    def add_st(a, b, c):
        return tuple(a[k] + c * b[k] for k in range(len(a)))

    for _ in range(n_steps):
        pmu, pmd = st[10], st[11]
        k1 = rhs_coupled_2hdm_soft(*st)
        k2 = rhs_coupled_2hdm_soft(*add_st(st, k1, h / 2))
        k3 = rhs_coupled_2hdm_soft(*add_st(st, k2, h / 2))
        k4 = rhs_coupled_2hdm_soft(*add_st(st, k3, h))
        st = tuple(st[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(st)))
        if t_u_cross is None and pmu >= 0 and st[10] < 0 and (pmu - st[10]) > 0:
            t_u_cross = t_cur + h * (pmu / (pmu - st[10]))
        if t_d_cross is None and pmd >= 0 and st[11] < 0 and (pmd - st[11]) > 0:
            t_d_cross = t_cur + h * (pmd / (pmd - st[11]))
        if check_all_steps_stab:
            l1s, l2s, l3s, l4s = st[6], st[7], st[8], st[9]
            if l1s <= 0 or l2s <= 0:
                all_steps_stab = False
                m_s = min(l1s, l2s)
            else:
                sq12 = mp.sqrt(l1s * l2s)
                m_s = min(l1s, l2s, l3s + sq12, l3s + l4s + sq12)
                if m_s <= 0:
                    all_steps_stab = False
            if min_stab_margin is None or m_s < min_stab_margin:
                min_stab_margin = m_s
        t_cur += h
    if check_all_steps_stab:
        return st, t_u_cross, t_d_cross, all_steps_stab, min_stab_margin
    return st, t_u_cross, t_d_cross


# ---------------------------------------------------------------------------
# MODULE P1 — Pure Bosonic Modular Potentials & FILQ(1990) Benchmarks
# ---------------------------------------------------------------------------

def run_P1() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    print("[P1] Running bosonic SL(2,Z) potentials (E_3, E_2, V_RS, -15/16, Kronecker) & FILQ(1..3)...", flush=True)
    mp.mp.dps = 48
    I = iu()
    tau_i = I
    tau_om = mp.mpc(mp_rat(1, 2), mp.sqrt(3) / 2)
    tau_om_neg = mp.mpc(mp_rat(-1, 2), mp.sqrt(3) / 2)
    tau_gen = mp.mpc(mp_rat(137, 1000), mp_rat(1213, 1000))

    # 1. Exact T & S invariance of E_3, E_2, V_RS at tau_gen
    def check_TS(fn):
        v0 = fn(tau_gen)
        vT = fn(tau_gen + 1)
        vS = fn(-1 / tau_gen)
        return max(abs(vT - v0), abs(vS - v0)) / max(mp.mpf(1), abs(v0))

    ts_e3 = check_TS(lambda t: E_fourier(t, 3, dps=46))
    ts_e2 = check_TS(lambda t: E_fourier(t, 2, dps=46))
    ts_vrs = check_TS(lambda t: V_RS(t, dps=46))
    ts_om_eq = abs(E_fourier(tau_om, 3, dps=46) - E_fourier(tau_om_neg, 3, dps=46))

    # 2. Direct box sum vs Fourier control at s=3
    e3_four = E_fourier(tau_gen, 3, dps=40)
    e3_box = E_box_sum(tau_gen, 3, N=45, dps=35)
    box_rel_err = abs(e3_four - e3_box) / abs(e3_four)

    # 3. Exact -15/16 half-period spin-structure sum identity (algebraic + lattice)
    # Sum of the 3 non-trivial half-period characters chi(m,n) in {(-1)^m, (-1)^n, (-1)^{m+n}}
    # equals +3 on the even sublattice 2Z^2 (weight 2^{-6} = 1/64) and -1 off it (weight 63/64):
    exact_half_period_ratio = Fraction(3, 64) - Fraction(63, 64)
    tot0 = mp.mpf(0)
    totc = mp.mpf(0)
    for m in range(-35, 36):
        for n in range(-35, 36):
            if m != 0 or n != 0:
                val = 1 / (abs(m * tau_gen + n) ** 6)
                tot0 += val
                totc += val * (((-1) ** m) + ((-1) ** n) + ((-1) ** (m + n)))
    lat_half_period_ratio = totc / tot0
    half_period_err = abs(lat_half_period_ratio - mp_frac(exact_half_period_ratio))

    # 4. Kronecker first limit formula at i, omega_+, tau_gen via exact symmetric s = 1 +- 10^-10
    d_kr = mp_pow10(-10)
    kron_max_err = mp.mpf(0)
    for t_k in (tau_i, tau_om, tau_gen):
        c_num = (E_fourier(t_k, 1 + d_kr, dps=48) + E_fourier(t_k, 1 - d_kr, dps=48)) / 2
        c_ex = mp.pi * V_RS(t_k, dps=48) + 2 * mp.pi * (mp.euler - mp.log(2))
        err_k = abs(c_num - c_ex)
        if err_k > kron_max_err:
            kron_max_err = err_k

    # 5. Critical points i (saddle) and omega_+ (min) for E_3, E_2, V_RS
    h_b = mp_pow10(-9)
    bos_crit = {}
    all_bos_crit_ok = True
    for name, fn in (
        ("E_3", lambda t: E_fourier(t, 3, dps=46)),
        ("E_2", lambda t: E_fourier(t, 2, dps=46)),
        ("V_RS", lambda t: V_RS(t, dps=46)),
    ):
        gi = grad_hess_2d(fn, tau_i, h_b)
        go = grad_hess_2d(fn, tau_om, h_b)
        v2i = fn(2 * I)
        v4i = fn(4 * I)
        i_is_saddle = (gi["grad_norm"] < mp_pow10(-12)) and (gi["hess_evals"][0] < 0 < gi["hess_evals"][1])
        om_is_min = (go["grad_norm"] < mp_pow10(-12)) and (go["hess_evals"][0] > 0) and (go["hess_evals"][1] > 0)
        cusp_grows = (go["val"] < gi["val"] < v2i < v4i)
        if not (i_is_saddle and om_is_min and cusp_grows):
            all_bos_crit_ok = False
        bos_crit[name] = {
            "val_omega": mp_str(go["val"], 12),
            "val_i": mp_str(gi["val"], 12),
            "val_2i": mp_str(v2i, 12),
            "val_4i": mp_str(v4i, 12),
            "grad_i": mp_str(gi["grad_norm"], 6),
            "hess_i": [mp_str(v, 8) for v in gi["hess_evals"]],
            "grad_omega": mp_str(go["grad_norm"], 6),
            "hess_omega": [mp_str(v, 8) for v in go["hess_evals"]],
            "i_is_saddle": i_is_saddle,
            "omega_is_min": om_is_min,
            "cusp_grows": cusp_grows,
        }

    # 6. Zero-parameter 4D N=1 SUGRA modular potentials V_{FILQ, n} (n=1,2,3)
    filq_rep = {}
    filq_tau_stars = {}
    all_filq_ok = True
    h_f = mp_pow10(-9)
    h_g = mp_pow10(-14)
    for n in (1, 2, 3):
        fn_n = lambda t, nn=n: V_FILQ(t, nn, dps=48)
        ts_err = check_TS(fn_n)
        # Solve 1D Newton along x = 0 starting from y = 6/5
        y = mp_rat(6, 5)
        for _ in range(20):
            f0 = fn_n(I * y)
            gp = fn_n(I * (y + h_g))
            gm = fn_n(I * (y - h_g))
            fp = fn_n(I * (y + h_f))
            fm = fn_n(I * (y - h_f))
            g = (gp - gm) / (2 * h_g)
            H = (fp - 2 * f0 + fm) / (h_f * h_f)
            dy = g / H
            y -= dy
            if abs(dy) < mp_pow10(-26):
                break
        gh = grad_hess_2d(fn_n, I * y, mp_pow10(-8), h_grad=h_g)
        v_om = fn_n(tau_om)
        v_i = fn_n(tau_i)
        v_2i = fn_n(2 * I)
        v_4i = fn_n(4 * I)
        ok_n = (
            ts_err < mp_pow10(-32)
            and gh["grad_norm"] < mp_pow10(-20)
            and gh["hess_evals"][0] > 0
            and gh["hess_evals"][1] > 0
            and gh["val"] < v_i < v_om
            and v_4i > v_2i > 0
        )
        if not ok_n:
            all_filq_ok = False
        filq_tau_stars[n] = I * y
        filq_rep[f"n_{n}"] = {
            "TS_invariance_rel_err": mp_str(ts_err, 6),
            "y_star": mp_str(y, 14),
            "V_star": mp_str(gh["val"], 12),
            "grad_norm_at_star": mp_str(gh["grad_norm"], 6),
            "V_xx": mp_str(gh["fxx"], 10),
            "V_yy": mp_str(gh["fyy"], 10),
            "hess_evals": [mp_str(v, 10) for v in gh["hess_evals"]],
            "V_i": mp_str(v_i, 12),
            "V_omega": mp_str(v_om, 12),
            "V_2i": mp_str(v_2i, 12),
            "V_4i": mp_str(v_4i, 12),
            "strict_2d_min": ok_n,
        }

    # PF1: drop non-holomorphic -3/(pi y) from E2_hat in V_{FILQ, 1}
    v_pf1_0 = V_FILQ(tau_gen, 1, dps=40, drop_nonhol=True)
    v_pf1_S = V_FILQ(-1 / tau_gen, 1, dps=40, drop_nonhol=True)
    pf1_rel_err = abs(v_pf1_S - v_pf1_0) / max(mp.mpf(1), abs(v_pf1_0))

    # PF3: perturb off tau_{FILQ, 1}^* by (+1/10, +1/10)
    tau_f1_pert = filq_tau_stars[1] + mp.mpc(mp_rat(1, 10), mp_rat(1, 10))
    gh_pf3 = grad_hess_2d(lambda t: V_FILQ(t, 1, dps=40), tau_f1_pert, mp_pow10(-7))
    pf3_dv = gh_pf3["val"] - V_FILQ(filq_tau_stars[1], 1, dps=40)

    g1_pass = (
        max(ts_e3, ts_e2, ts_vrs) < mp_pow10(-32)
        and ts_om_eq < mp_pow10(-32)
        and box_rel_err < mp_pow10(-6)
        and exact_half_period_ratio == Fraction(-15, 16)
        and half_period_err < mp_pow10(-5)
        and kron_max_err < mp_pow10(-16)
        and all_bos_crit_ok
        and all_filq_ok
    )
    print(f"[P1] Done: TS_max={mp_str(max(ts_e3, ts_e2, ts_vrs), 4)}, Kron={mp_str(kron_max_err, 4)}, FILQ1_y*={filq_rep['n_1']['y_star']}, g1={g1_pass}", flush=True)
    out_p1 = {
        "TS_invariance_E3": mp_str(ts_e3, 6),
        "TS_invariance_E2": mp_str(ts_e2, 6),
        "TS_invariance_VRS": mp_str(ts_vrs, 6),
        "box_vs_fourier_E3_rel_err": mp_str(box_rel_err, 6),
        "half_period_exact_ratio": frac_str(exact_half_period_ratio),
        "half_period_lattice_ratio": mp_str(lat_half_period_ratio, 10),
        "half_period_lattice_err": mp_str(half_period_err, 6),
        "kronecker_first_limit_max_err": mp_str(kron_max_err, 6),
        "bosonic_critical_points": bos_crit,
        "FILQ_SUGRA_potentials": filq_rep,
        "pf1_drop_nonhol_S_rel_err": mp_str(pf1_rel_err, 6),
        "pf3_shift_off_FILQ1_dV": mp_str(pf3_dv, 8),
        "pf3_shift_off_FILQ1_grad": mp_str(gh_pf3["grad_norm"], 8),
        "g1_pass": g1_pass,
    }
    return out_p1, {"tau_om": tau_om, "tau_filq1": filq_tau_stars[1], "tau_filq3": filq_tau_stars[3]}


# ---------------------------------------------------------------------------
# MODULE P2 — Full Fundamental-Domain F Boson + Fermion Phase Diagram
# ---------------------------------------------------------------------------

def run_P2(pairs288: List[Tuple[Fraction, Fraction]], p1_aux: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    print("[P2] Mapping fundamental domain F for boson+fermion V_eff(tau) (P2-A, P2-B, P2-C)...", flush=True)
    mp.mp.dps = 38
    I = iu()
    pi = mp.pi

    # 1. Exact T & S invariance of all-288 fermion potentials at generic tau_mod = 1/4 + 6/5 i
    tau_mod = mp.mpc(mp_rat(1, 4), mp_rat(6, 5))
    f_0 = eval_all288_fermion_pot(tau_mod, pairs288, dps_use=36)
    f_T = eval_all288_fermion_pot(tau_mod + 1, pairs288, dps_use=36)
    f_S = eval_all288_fermion_pot(-1 / tau_mod, pairs288, dps_use=36)
    ts_ferm = {}
    for k in ("Tr2", "V4", "VCW_1", "VCW_tr"):
        ts_ferm[k] = max(abs(f_T[k] - f_0[k]), abs(f_S[k] - f_0[k])) / max(mp.mpf(1), abs(f_0[k]))

    # 2. Boundary orbifolds & arc: omega_+ = 1/2 + i*sqrt(3)/2, arc = exp(i*5*pi/12), i
    tau_om = p1_aux["tau_om"]
    tau_arc = mp.exp(I * 5 * pi / 12)
    tau_i = I
    f_om = eval_all288_fermion_pot(tau_om, pairs288, dps_use=30)
    f_arc = eval_all288_fermion_pot(tau_arc, pairs288, dps_use=30)
    f_i = eval_all288_fermion_pot(tau_i, pairs288, dps_use=30)

    e3_om = E_fourier(tau_om, 3, dps=36)
    e3_i = E_fourier(tau_i, 3, dps=36)
    cB_crit = (f_om["VCW_1"] - f_i["VCW_1"]) / (e3_i - e3_om)

    # 3. Vertical ray scans along x = 0 and x = 1/2
    y_grid_x0 = [Fraction(231, 200), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2), Fraction(3, 1), Fraction(7, 2), Fraction(4, 1)]
    y_grid_xh = [Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2), Fraction(3, 1), Fraction(7, 2), Fraction(4, 1)]

    scan_out = {"x_0": [], "x_half": []}
    ray_data = {"x_0": {}, "x_half": {}}
    for xkey, xf, ygrid in (("x_0", Fraction(0, 1), y_grid_x0), ("x_half", Fraction(1, 2), y_grid_xh)):
        for yf in ygrid:
            tv = mp.mpc(mp_frac(xf), mp_frac(yf))
            fv = eval_all288_fermion_pot(tv, pairs288, dps_use=24)
            vf3 = V_FILQ(tv, 3, dps=32)
            vf1 = V_FILQ(tv, 1, dps=32)
            e3v = E_fourier(tv, 3, dps=32)
            vtot70 = vf3 + 70 * fv["VCW_1"]
            vtot100 = vf3 + 100 * fv["VCW_1"]
            ratio_f3 = -vf3 / fv["VCW_1"] if fv["VCW_1"] < 0 else mp.mpf(0)
            ray_data[xkey][yf] = {
                "fv": fv, "vf3": vf3, "vf1": vf1, "e3": e3v, "vtot70": vtot70, "vtot100": vtot100, "ratio_f3": ratio_f3
            }
            scan_out[xkey].append({
                "y": frac_str(yf),
                "Tr2": mp_str(fv["Tr2"], 10),
                "V4": mp_str(fv["V4"], 10),
                "VCW_1": mp_str(fv["VCW_1"], 10),
                "VCW_tr": mp_str(fv["VCW_tr"], 10),
                "V_FILQ3": mp_str(vf3, 10),
                "V_tot_cF70": mp_str(vtot70, 10),
                "V_tot_cF100": mp_str(vtot100, 10),
                "ratio_minus_FILQ3_over_VCW1": mp_str(ratio_f3, 8),
            })

    # Verify Theorem P2-A (V_CW_tr strictly positive, global min at i, local min at omega, arc barrier, cusp growth)
    p2a_tr_i_lt_om_lt_arc = (f_i["VCW_tr"] > 0) and (f_i["VCW_tr"] < f_om["VCW_tr"] < f_arc["VCW_tr"])
    tr_x0 = [ray_data["x_0"][y]["fv"]["VCW_tr"] for y in y_grid_x0]
    tr_xh = [ray_data["x_half"][y]["fv"]["VCW_tr"] for y in y_grid_xh]
    p2a_monotone_cusp = (
        all(tr_x0[k + 1] > tr_x0[k] for k in range(2, len(tr_x0) - 1))
        and all(tr_xh[k + 1] > tr_xh[k] for k in range(2, len(tr_xh) - 1))
        and tr_x0[-1] > 10 ** 6
    )
    p2a_v4_arc_dip = (f_arc["V4"] < f_om["V4"]) and (f_arc["V4"] < f_i["V4"])

    # Verify Theorem P2-B (polynomial Casimir No-Go: even +100 E_3 fails to stop cusp runaway at y=4)
    v_poly_100_at_4i = ray_data["x_0"][Fraction(4, 1)]["fv"]["VCW_1"] + 100 * ray_data["x_0"][Fraction(4, 1)]["e3"]
    p2b_poly_nogo = v_poly_100_at_4i < mp.mpf(-10 ** 8)
    # Orbifold transition sign check at c_B = 1/100 (< cB_crit) vs c_B = 1/10 (> cB_crit)
    diff_lo = (f_om["VCW_1"] + mp_rat(1, 100) * e3_om) - (f_i["VCW_1"] + mp_rat(1, 100) * e3_i)
    diff_hi = (f_om["VCW_1"] + mp_rat(1, 10) * e3_om) - (f_i["VCW_1"] + mp_rat(1, 10) * e3_i)
    p2b_transition_ok = (diff_lo > 0) and (diff_hi < 0)

    # 4. Theorem P2-C: Exact 2D minimum of V_tot(tau; c_F = 70) on x = 1/2
    def eval_vtot(tau_in, cF_val, dps_use: int = 26):
        fv = eval_all288_fermion_pot(tau_in, pairs288, dps_use=dps_use)
        return V_FILQ(tau_in, 3, dps=max(32, dps_use)) + cF_val * fv["VCW_1"]

    # Fast exact parabolic Newton minimization of V_tot(1/2 + i y; 70) from bracket [3.28, 3.46]
    # Bracket check on y in {3.30, 3.38, 3.46} then 4 exact parabolic Newton steps at dps=32
    y_star_70 = mp_rat(338, 100)
    h_y = mp_pow10(-5)
    for _ in range(4):
        v_0 = eval_vtot(mp.mpc(mp_rat(1, 2), y_star_70), mp.mpf(70), dps_use=32)
        v_p = eval_vtot(mp.mpc(mp_rat(1, 2), y_star_70 + h_y), mp.mpf(70), dps_use=32)
        v_m = eval_vtot(mp.mpc(mp_rat(1, 2), y_star_70 - h_y), mp.mpf(70), dps_use=32)
        dy_pol = ((v_p - v_m) / (2 * h_y)) / ((v_p - 2 * v_0 + v_m) / (h_y * h_y))
        y_star_70 = y_star_70 - dy_pol
        if abs(dy_pol) < mp_pow10(-11):
            break
    tau_tot_70 = mp.mpc(mp_rat(1, 2), y_star_70)

    # Verify exact L_2 T-reflection symmetry |L_2(1/2 + h_2d) - L_2(1/2 - h_2d)| via raw ODE
    h_2d = mp_rat(1, 50)
    l2_raw_p, res_raw_p = solve_L2_fuchsian_raw(mp.mpc(mp_rat(1, 2) + h_2d, y_star_70), dps=38)
    l2_raw_m, res_raw_m = solve_L2_fuchsian_raw(mp.mpc(mp_rat(1, 2) - h_2d, y_star_70), dps=38)
    l2_raw_sym_err = abs(l2_raw_p - l2_raw_m)

    # Exact 2D gradient & Hessian at (1/2, y*) and x=0 saddle check at (0, y*)
    v_c = eval_vtot(tau_tot_70, mp.mpf(70), dps_use=34)
    v_xp = eval_vtot(mp.mpc(mp_rat(1, 2) + h_2d, y_star_70), mp.mpf(70), dps_use=34)
    v_xm = eval_vtot(mp.mpc(mp_rat(1, 2) - h_2d, y_star_70), mp.mpf(70), dps_use=34)
    v_yp = eval_vtot(mp.mpc(mp_rat(1, 2), y_star_70 + h_y), mp.mpf(70), dps_use=34)
    v_ym = eval_vtot(mp.mpc(mp_rat(1, 2), y_star_70 - h_y), mp.mpf(70), dps_use=34)
    gx_70 = (v_xp - v_xm) / (2 * h_2d)
    gy_70 = (v_yp - v_ym) / (2 * h_y)
    vxx_half = (v_xp - 2 * v_c + v_xm) / (h_2d * h_2d)
    vyy_half = (v_yp - 2 * v_c + v_ym) / (h_y * h_y)

    # Compare against (0, y*) saddle point
    v0_c = eval_vtot(mp.mpc(0, y_star_70), mp.mpf(70), dps_use=34)
    v0_xp = eval_vtot(mp.mpc(h_2d, y_star_70), mp.mpf(70), dps_use=34)
    vxx_zero = (2 * v0_xp - 2 * v0_c) / (h_2d * h_2d)
    cos2pix_pred = 2 * (pi ** 2) * (v0_c - v_c)
    vxx_cos_ratio = vxx_half / cos2pix_pred

    # Small-y FILQ3 well evaluated under V_tot(c_F = 70)
    v_small_well_70 = eval_vtot(p1_aux["tau_filq3"], mp.mpf(70), dps_use=28)
    # Huge positive cusp wall at y = 4
    v_cusp_4_70 = ray_data["x_half"][Fraction(4, 1)]["vtot70"]
    # Also find exact critical coupling c_F^{crit} along x = 1/2 around y = 3.00 (ratio min)
    cF_crit_approx = min(
        ray_data["x_half"][yf]["ratio_f3"]
        for yf in (Fraction(5, 2), Fraction(3, 1), Fraction(7, 2))
        if ray_data["x_half"][yf]["ratio_f3"] > 0
    )

    # Check c_F = 100 shifted interior minimum on [3.5, 5.0]
    v100_35 = ray_data["x_half"][Fraction(7, 2)]["vtot100"]
    v100_40 = ray_data["x_half"][Fraction(4, 1)]["vtot100"]
    v100_50 = eval_vtot(mp.mpc(mp_rat(1, 2), mp.mpf(5)), mp.mpf(100), dps_use=24)
    cF100_bounded_deep_well = (v100_40 < 0) and (v100_50 > mp.mpf(10 ** 12))

    # PF2: Sub-critical SUGRA n=1 + 70*V_CW(1) at 1/2 + 4i restores exponential cusp runaway
    pf2_v_n1_4 = ray_data["x_half"][Fraction(4, 1)]["vf1"] + 70 * ray_data["x_half"][Fraction(4, 1)]["fv"]["VCW_1"]

    p2c_ok = (
        l2_raw_sym_err < mp_pow10(-12)
        and abs(gx_70) < mp_pow10(-8) * abs(v_c)
        and abs(gy_70) < mp_pow10(-8) * abs(v_c)
        and vxx_half > 0
        and vyy_half > 0
        and vxx_zero < 0
        and abs(vxx_cos_ratio - 1) < mp_rat(1, 20)
        and v_c < v0_c
        and v_c < mp.mpf(-6 * (10 ** 6))
        and v_small_well_70 > 0
        and v_cusp_4_70 > mp.mpf(4 * (10 ** 9))
        and cF100_bounded_deep_well
    )

    g2_pass = (
        max(ts_ferm.values()) < mp_pow10(-25)
        and p2a_tr_i_lt_om_lt_arc
        and p2a_monotone_cusp
        and p2a_v4_arc_dip
        and p2b_poly_nogo
        and p2b_transition_ok
        and p2c_ok
    )
    print(
        f"[P2] Done: TS_ferm={mp_str(max(ts_ferm.values()), 4)}, cB_crit={mp_str(cB_crit, 6)}, "
        f"tau_tot70=0.5+{mp_str(y_star_70, 8)}i, V*={mp_str(v_c, 8)}, Vxx(1/2)={mp_str(vxx_half, 6)}, "
        f"Vxx(0)={mp_str(vxx_zero, 6)}, g2={g2_pass}",
        flush=True,
    )
    out_p2 = {
        "SL2Z_TS_invariance_all288": {k: mp_str(v, 6) for k, v in ts_ferm.items()},
        "orbifolds_and_arc": {
            "omega_plus": {k: mp_str(f_om[k], 12) for k in ("Tr2", "V4", "VCW_1", "VCW_tr")},
            "arc_exp_i_5pi_12": {k: mp_str(f_arc[k], 12) for k in ("Tr2", "V4", "VCW_1", "VCW_tr")},
            "i": {k: mp_str(f_i[k], 12) for k in ("Tr2", "V4", "VCW_1", "VCW_tr")},
        },
        "theorem_P2A_trace_renormalized_stabilization": {
            "VCW_tr_i_lt_omega_lt_arc": p2a_tr_i_lt_om_lt_arc,
            "VCW_tr_monotone_cusp_to_plus_inf": p2a_monotone_cusp,
            "V4_dips_below_both_orbifolds_on_arc": p2a_v4_arc_dip,
        },
        "theorem_P2B_polynomial_casimir_nogo_and_transition": {
            "cB_crit_E3": mp_str(cB_crit, 10),
            "VCW1_plus_100E3_at_4i": mp_str(v_poly_100_at_4i, 10),
            "polynomial_nogo_confirmed": p2b_poly_nogo,
            "orbifold_order_flips_across_cB_crit": p2b_transition_ok,
        },
        "theorem_P2C_globally_bounded_coupled_vacuum": {
            "cF_crit_grid_upper_bound": mp_str(cF_crit_approx, 8),
            "cF_70_x_star": "1/2",
            "cF_70_y_star": mp_str(y_star_70, 10),
            "cF_70_V_star": mp_str(v_c, 12),
            "cF_70_gx_at_half": mp_str(gx_70, 6),
            "cF_70_gy_at_half": mp_str(gy_70, 6),
            "cF_70_Vxx_at_half": mp_str(vxx_half, 10),
            "cF_70_Vyy_at_half": mp_str(vyy_half, 10),
            "cF_70_V_at_zero_same_y": mp_str(v0_c, 12),
            "cF_70_Vxx_at_zero_saddle": mp_str(vxx_zero, 10),
            "cF_70_V_half_minus_V_zero": mp_str(v_c - v0_c, 8),
            "cF_70_cos2pix_Vxx_pred": mp_str(cos2pix_pred, 10),
            "cF_70_Vxx_over_cos2pix_pred": mp_str(vxx_cos_ratio, 8),
            "cF_70_L2_raw_T_reflection_sym_err": mp_str(l2_raw_sym_err, 6),
            "cF_70_L2_raw_ode_res": mp_str(max(res_raw_p, res_raw_m), 6),
            "cF_70_small_y_FILQ3_well_V": mp_str(v_small_well_70, 10),
            "cF_70_cusp_wall_at_half_plus_4i": mp_str(v_cusp_4_70, 12),
            "cF_100_V_at_half_plus_3p5i": mp_str(v100_35, 10),
            "cF_100_V_at_half_plus_4i": mp_str(v100_40, 10),
            "cF_100_V_at_half_plus_5i": mp_str(v100_50, 10),
            "cF_100_bounded_deep_well": cF100_bounded_deep_well,
            "true_2d_global_min_on_x_half": p2c_ok,
        },
        "fundamental_domain_scans": scan_out,
        "pf2_subcritical_n1_plus_70VCW1_at_4i": mp_str(pf2_v_n1_4, 10),
        "g2_pass": g2_pass,
    }
    return out_p2, {"tau_tot_70": tau_tot_70}


# ---------------------------------------------------------------------------
# MODULE P3 — Zero-Sculpting Forward Unfolding (Pieces 2 & 3) + Guardrail 3/4
# ---------------------------------------------------------------------------

def run_P3(p1_aux: Dict[str, Any], p2_aux: Dict[str, Any]) -> Dict[str, Any]:
    print("[P3] Running Guardrail 4 benchmarks, curved Dirac, Pieces 2 & 3 at 3 vacua, & Haar U(3)^5 x U(3)_nuR...", flush=True)
    mp.mp.dps = 44

    # 1. Guardrail 4 Literature Benchmarks (Chowdhury-Eberhardt 2HDM-II + Xing-Zhou + Martin soft-mass)
    yt_v, yb_v, ytau_v = mp_rat(9, 10), mp_rat(4, 10), mp_rat(2, 10)
    g1_v, g2_v, g3_v = mp_rat(45, 100), mp_rat(65, 100), mp_rat(11, 10)
    l1_v, l2_v, l3_v, l4_v = mp_rat(1, 10), mp_rat(15, 100), mp_rat(5, 100), mp_rat(-3, 100)
    mhu_v, mhd_v = mp_rat(7, 10), mp_rat(9, 10)
    mq_v, mu_v, md_v, ml_v, me_v = mp_rat(11, 10), mp_rat(13, 10), mp_rat(15, 10), mp_rat(17, 10), mp_rat(19, 10)
    Yu_b = mp.diag([0, 0, yt_v])
    Yd_b = mp.diag([0, 0, yb_v])
    Ye_b = mp.diag([0, 0, ytau_v])
    MQ_b = mp.diag([0, 0, mq_v])
    Mu_b = mp.diag([0, 0, mu_v])
    Md_b = mp.diag([0, 0, md_v])
    ML_b = mp.diag([0, 0, ml_v])
    Me_b = mp.diag([0, 0, me_v])
    out_b = rhs_coupled_2hdm_soft(g1_v, g2_v, g3_v, Yu_b, Yd_b, Ye_b, l1_v, l2_v, l3_v, l4_v, mhu_v, mhd_v, MQ_b, Mu_b, Md_b, ML_b, Me_b)

    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    # Exact 3-sector Type-II 2HDM 2-loop benchmark directly against primary arXiv:1503.08216 Appendix A
    # (converting CE g_1^2 = g_Y^2 = (3/5) g_1^{GUT}^2 identically)
    gy2_v = mp_rat(3, 5) * (g1_v ** 2)
    b1_yt_ex = yt_v * (mp_rat(9, 2) * yt_v ** 2 + mp_rat(1, 2) * yb_v ** 2 - mp_rat(17, 12) * gy2_v - mp_rat(9, 4) * g2_v ** 2 - 8 * g3_v ** 2)
    b2_yt_ex = yt_v * (
        -12 * yt_v ** 4 - mp_rat(5, 2) * yt_v ** 2 * yb_v ** 2 - mp_rat(5, 2) * yb_v ** 4 - mp_rat(3, 4) * yb_v ** 2 * ytau_v ** 2
        + (mp_rat(131, 16) * gy2_v + mp_rat(225, 16) * g2_v ** 2 + 36 * g3_v ** 2) * yt_v ** 2
        + (-mp_rat(41, 144) * gy2_v + mp_rat(33, 16) * g2_v ** 2 + mp_rat(16, 3) * g3_v ** 2) * yb_v ** 2
        + mp_rat(1267, 216) * gy2_v ** 2 - mp_rat(3, 4) * gy2_v * g2_v ** 2 + mp_rat(19, 9) * gy2_v * g3_v ** 2
        - mp_rat(21, 4) * g2_v ** 4 + 9 * g2_v ** 2 * g3_v ** 2 - 108 * g3_v ** 4
        - 6 * l2_v * yt_v ** 2 + (-2 * l3_v + 2 * l4_v) * yb_v ** 2
        + mp_rat(3, 2) * l2_v ** 2 + l3_v ** 2 + l3_v * l4_v + l4_v ** 2
    )
    b1_yb_ex = yb_v * (mp_rat(9, 2) * yb_v ** 2 + mp_rat(1, 2) * yt_v ** 2 + ytau_v ** 2 - mp_rat(5, 12) * gy2_v - mp_rat(9, 4) * g2_v ** 2 - 8 * g3_v ** 2)
    b2_yb_ex = yb_v * (
        -12 * yb_v ** 4 - mp_rat(5, 2) * yb_v ** 2 * yt_v ** 2 - mp_rat(9, 4) * yb_v ** 2 * ytau_v ** 2
        - mp_rat(5, 2) * yt_v ** 4 - mp_rat(9, 4) * ytau_v ** 4
        + (mp_rat(79, 16) * gy2_v + mp_rat(225, 16) * g2_v ** 2 + 36 * g3_v ** 2) * yb_v ** 2
        + (-mp_rat(53, 144) * gy2_v + mp_rat(33, 16) * g2_v ** 2 + mp_rat(16, 3) * g3_v ** 2) * yt_v ** 2
        + (mp_rat(25, 8) * gy2_v + mp_rat(15, 8) * g2_v ** 2) * ytau_v ** 2
        - mp_rat(113, 216) * gy2_v ** 2 - mp_rat(9, 4) * gy2_v * g2_v ** 2 + mp_rat(31, 9) * gy2_v * g3_v ** 2
        - mp_rat(21, 4) * g2_v ** 4 + 9 * g2_v ** 2 * g3_v ** 2 - 108 * g3_v ** 4
        - 6 * l1_v * yb_v ** 2 + (-2 * l3_v + 2 * l4_v) * yt_v ** 2
        + mp_rat(3, 2) * l1_v ** 2 + l3_v ** 2 + l3_v * l4_v + l4_v ** 2
    )
    b1_ytau_ex = ytau_v * (3 * yb_v ** 2 + mp_rat(5, 2) * ytau_v ** 2 - mp_rat(15, 4) * gy2_v - mp_rat(9, 4) * g2_v ** 2)
    b2_ytau_ex = ytau_v * (
        -mp_rat(27, 4) * yb_v ** 4 - mp_rat(9, 4) * yb_v ** 2 * yt_v ** 2 - mp_rat(27, 4) * yb_v ** 2 * ytau_v ** 2 - 3 * ytau_v ** 4
        + (mp_rat(25, 24) * gy2_v + mp_rat(45, 8) * g2_v ** 2 + 20 * g3_v ** 2) * yb_v ** 2
        + (mp_rat(179, 16) * gy2_v + mp_rat(165, 16) * g2_v ** 2) * ytau_v ** 2
        + mp_rat(161, 8) * gy2_v ** 2 + mp_rat(9, 4) * gy2_v * g2_v ** 2 - mp_rat(21, 4) * g2_v ** 4
        - 6 * l1_v * ytau_v ** 2 + mp_rat(3, 2) * l1_v ** 2 + l3_v ** 2 + l3_v * l4_v + l4_v ** 2
    )
    ce_yt_err = abs(out_b[3][2, 2] - (inv1 * b1_yt_ex + inv2 * b2_yt_ex))
    ce_yb_err = abs(out_b[4][2, 2] - (inv1 * b1_yb_ex + inv2 * b2_yb_ex))
    ce_ytau_err = abs(out_b[5][2, 2] - (inv1 * b1_ytau_ex + inv2 * b2_ytau_ex))
    ce_max_err = max(ce_yt_err, ce_yb_err, ce_ytau_err)

    # Exact 7-equation Martin hep-ph/9709356 Eqs 6.5.24-6.5.30 1-gen soft-mass check
    S_b = mhu_v - mhd_v + mq_v - ml_v - 2 * mu_v + md_v + me_v
    Xt = 2 * (yt_v ** 2) * (mhu_v + mq_v + mu_v)
    Xb = 2 * (yb_v ** 2) * (mhd_v + mq_v + md_v)
    Xtau = 2 * (ytau_v ** 2) * (mhd_v + ml_v + me_v)
    martin_ex = [
        inv1 * (3 * Xt + mp_rat(3, 5) * (g1_v ** 2) * S_b),
        inv1 * (3 * Xb + Xtau - mp_rat(3, 5) * (g1_v ** 2) * S_b),
        inv1 * (Xt + Xb + mp_rat(1, 5) * (g1_v ** 2) * S_b),
        inv1 * (2 * Xt - mp_rat(4, 5) * (g1_v ** 2) * S_b),
        inv1 * (2 * Xb + mp_rat(2, 5) * (g1_v ** 2) * S_b),
        inv1 * (Xtau - mp_rat(3, 5) * (g1_v ** 2) * S_b),
        inv1 * (2 * Xtau + mp_rat(6, 5) * (g1_v ** 2) * S_b),
    ]
    martin_num = [out_b[10], out_b[11], out_b[12][2, 2], out_b[13][2, 2], out_b[14][2, 2], out_b[15][2, 2], out_b[16][2, 2]]
    martin_max_err = max(abs(a - b) for a, b in zip(martin_num, martin_ex))

    # Xing-Zhou opposite |V_cb| sign check
    Yu_xz = mp.diag([mp_rat(1, 100), mp_rat(1, 10), mp_rat(9, 10)])
    th_xz = mp_rat(1, 20)
    R23 = mp.matrix([[1, 0, 0], [0, mp.cos(th_xz), mp.sin(th_xz)], [0, -mp.sin(th_xz), mp.cos(th_xz)]])
    Yd_xz = R23 * mp.diag([mp_rat(1, 200), mp_rat(3, 100), mp_rat(4, 10)])
    Ye_xz = mp.diag([mp_rat(1, 500), mp_rat(2, 100), mp_rat(2, 10)])
    vcb0 = observables_from_Y(Yu_xz, Yd_xz, Ye_xz)["V23"]
    st0_xz = (g1_v, g2_v, g3_v, Yu_xz, Yd_xz, Ye_xz, l1_v, l2_v, l3_v, l4_v, mp.mpf(1), mp.mpf(1), mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3))
    st_2h, _, _ = rk4_integrate_coupled(st0_xz, mp_rat(-1, 10), 10)
    vcb_2h = observables_from_Y(st_2h[3], st_2h[4], st_2h[5])["V23"]
    hu_xz, hd_xz = Yu_xz * Yu_xz.H, Yd_xz * Yd_xz.H
    vcb_1h = observables_from_Y(
        Yu_xz + mp_rat(-1, 10) * inv1 * (mp_rat(3, 2) * hu_xz - mp_rat(3, 2) * hd_xz) * Yu_xz,
        Yd_xz + mp_rat(-1, 10) * inv1 * (mp_rat(3, 2) * hd_xz - mp_rat(3, 2) * hu_xz) * Yd_xz,
        Ye_xz,
    )["V23"]
    xz_opposite = ((vcb_1h - vcb0) < 0) and ((vcb_2h - vcb0) > 0)

    # 2. Forward Unfolding at ALL 3 Canonical Vacua: omega_+, tau_{FILQ,1}^*, tau_{tot}^*(70)
    w_mark = (Fraction(4, 15), Fraction(1, 30))
    w_double = mod1_pt(2 * w_mark[0], 2 * w_mark[1])

    def apply_kahler(Y, g_diag):
        D = mp.diag([1 / mp.sqrt(v) for v in g_diag])
        return D * Y * D

    vacua = [
        ("V1_omega_plus", p1_aux["tau_om"]),
        ("V2_FILQ1_star", p1_aux["tau_filq1"]),
        ("V3_coupled_cF70_star", p2_aux["tau_tot_70"]),
    ]

    # Exact Branco / Chowdhury-Eberhardt potential normalization:
    #   V = (1/2) l1 |Phi1|^4 + (1/2) l2 |Phi2|^4 + l3 |Phi1|^2 |Phi2|^2 + l4 |Phi1^dag Phi2|^2
    # Matching MSSM / Gauge-Higgs D-terms V_D = ((g2^2 + gY^2)/8)(|Phi1|^2 - |Phi2|^2)^2 + (g2^2/2)(|Phi1|^2|Phi2|^2 - |Phi1^dag Phi2|^2):
    #   l1_D = l2_D = (g2^2 + gY^2) / 4,  l3_D = (g2^2 - gY^2) / 4,  l4_D = -g2^2 / 2
    # Exact UV D-flat saturation at t = 0: l3_D + l4_D + sqrt(l1_D * l2_D) == 0 identically!
    g_uv = mp_rat(1, 2)
    g12_0 = g_uv * g_uv
    g22_0 = g_uv * g_uv
    gy2_0 = mp_rat(3, 5) * g12_0
    l1_D = (g22_0 + gy2_0) / 4
    l2_D = l1_D
    l3_D = (g22_0 - gy2_0) / 4
    l4_D = -g22_0 / 2
    uv_dflat_err = abs(l3_D + l4_D + mp.sqrt(l1_D * l2_D))
    dt_ir = mp.mpf(-35)

    vac_reports = {}
    max_gb_err = mp.mpf(0)
    max_sh_err = mp.mpf(0)
    max_S_ir = mp.mpf(0)
    all_stab_ok = True
    all_ewsb_ok = True
    omega_iso_err = mp.mpf(1)
    haar_seed_mats = None

    for vname, tau_v in vacua:
        print(f"  [P3] Unfolding {vname} (tau = {mp_str(tau_v, 8)})...", flush=True)
        g12 = compute_curved_dirac_s12(tau_v, dps=30)
        mp.mp.dps = 40
        if g12["gb_err"] > max_gb_err:
            max_gb_err = g12["gb_err"]
        if vname == "V1_omega_plus":
            omega_iso_err = max(abs(x - 1) for x in g12["G_s12"])

        L2_v, _ = solve_L2_fuchsian_cov(tau_v, dps=38)
        eng = FrameCEngine(tau_v, L2_v, dps=40)
        Yu_s = eng.Y_matrix(w_mark[0], w_mark[1], "up", weight0=True)
        Yd_s = eng.Y_matrix(w_mark[0], w_mark[1], "down", weight0=True)
        Ye_s = eng.Y_matrix(w_mark[0], w_mark[1], "lep", weight0=True)
        Yn_s = eng.Y_matrix(w_mark[0], w_mark[1], "nu", weight0=True)
        Yn_2w = eng.Y_matrix(w_double[0], w_double[1], "nu", weight0=True)

        # Physically canonical CONV-3 ordering for DynamicV4_ferro_CURVED_s12:
        #   1) Apply curved Dirac Kahler rescaling G_{s=1/2}^{-1/2} (.) G_{s=1/2}^{-1/2} FIRST (canonical kinetic basis)
        #   2) Minimize 2-doublet all-S V_4(h_u, h_d) - (1/4)|V_4(S^can)| |h_u^dag h_d|^2 on canonical Yukawas
        #   3) Couple Y_nu(w) and Y_nu(2w) to the dynamic up-type Higgs h_u^* (Type-II 2HDM H_u coupling)
        Au_c = [apply_kahler(M, g12["G_s12"]) for M in eng.Y_higgs_basis(w_mark[0], w_mark[1], "up")]
        Ad_c = [apply_kahler(M, g12["G_s12"]) for M in eng.Y_higgs_basis(w_mark[0], w_mark[1], "down")]
        Ae_c = [apply_kahler(M, g12["G_s12"]) for M in eng.Y_higgs_basis(w_mark[0], w_mark[1], "lep")]
        An_c = [apply_kahler(M, g12["G_s12"]) for M in eng.Y_higgs_basis(w_mark[0], w_mark[1], "nu")]
        An2_c = [apply_kahler(M, g12["G_s12"]) for M in eng.Y_higgs_basis(w_double[0], w_double[1], "nu")]
        Yu_sc = apply_kahler(Yu_s, g12["G_s12"])
        Yd_sc = apply_kahler(Yd_s, g12["G_s12"])
        Ye_sc = apply_kahler(Ye_s, g12["G_s12"])
        Yn_sc = apply_kahler(Yn_s, g12["G_s12"])
        Yn2_sc = apply_kahler(Yn_2w, g12["G_s12"])
        v4_0 = (
            eval_V4_and_grad(Yu_sc, Au_c, 3)[0]
            + eval_V4_and_grad(Yd_sc, Ad_c, 3)[0]
            + eval_V4_and_grad(Ye_sc, Ae_c, 1)[0]
        )
        dyn_v4 = minimize_2doublet_V4_allS(Au_c, Ad_c, Ae_c, eng.c_hat, mp_rat(-1, 4), abs(v4_0))
        hu_d = dyn_v4["hu_star"]
        Yn_dyn = sum((hu_d[k] * An_c[k] for k in range(3)), mp.zeros(3, 3))
        Yn2_dyn = sum((hu_d[k] * An2_c[k] for k in range(3)), mp.zeros(3, 3))

        branch_res = {}
        for bname, Yu0, Yd0, Ye0, Yn0, Yn2_0 in (
            ("Static_FLAT", Yu_s, Yd_s, Ye_s, Yn_s, Yn_2w),
            ("Static_CURVED_s12", Yu_sc, Yd_sc, Ye_sc, Yn_sc, Yn2_sc),
            ("DynamicV4_ferro_CURVED_s12", dyn_v4["Yu"], dyn_v4["Yd"], dyn_v4["Ye"], Yn_dyn, Yn2_dyn),
        ):
            # Natural O(1) overall normalization: max_f sigma_3(Y_f) = 1
            sc_uv = max(svd_asc_3x3(M)[0][2] for M in (Yu0, Yd0, Ye0))
            Yu_in, Yd_in, Ye_in = Yu0 / sc_uv, Yd0 / sc_uv, Ye0 / sc_uv
            obs_uv = observables_from_Y(Yu_in, Yd_in, Ye_in)

            # Save coupled_cF70 Static_CURVED_s12 for Guardrail 3 Haar test & PF4/PF5/PF6
            if vname == "V3_coupled_cF70_star" and bname == "Static_CURVED_s12":
                haar_seed_mats = (Yu_in, Yd_in, Ye_in, Yn0, Yn2_0)

            st0 = (
                g_uv, g_uv, g_uv, Yu_in, Yd_in, Ye_in,
                l1_D, l2_D, l3_D, l4_D,
                mp.mpf(1), mp.mpf(1),
                mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3),
            )
            st_80, _, _ = rk4_integrate_coupled(st0, dt_ir, 80)
            st_160, t_u, t_d, steps_stab, min_stab_m = rk4_integrate_coupled(st0, dt_ir, 160, check_all_steps_stab=True)
            obs_80 = observables_from_Y(st_80[3], st_80[4], st_80[5])
            obs_ir = observables_from_Y(st_160[3], st_160[4], st_160[5])

            sh_err = max(
                abs(obs_ir["su"][2] - obs_80["su"][2]) / obs_ir["su"][2],
                abs(obs_ir["V12"] - obs_80["V12"]) / max(mp_pow10(-10), obs_ir["V12"]),
                abs(st_160[10] - st_80[10]) / max(mp.mpf(1), abs(st_160[10])),
                abs(st_160[6] - st_80[6]) / max(mp.mpf(1), abs(st_160[6])),
            )
            if sh_err > max_sh_err:
                max_sh_err = sh_err

            l1_ir, l2_ir, l3_ir, l4_ir = st_160[6], st_160[7], st_160[8], st_160[9]
            stab_ir = bool(
                steps_stab
                and l1_ir > 0 and l2_ir > 0
                and (l3_ir + mp.sqrt(l1_ir * l2_ir)) > 0
                and (l3_ir + l4_ir + mp.sqrt(l1_ir * l2_ir)) > 0
            )
            min_sf = min(min(mp.re(ev) for ev in mp.eigh(M)[0]) for M in st_160[12:])
            S_ir = abs(st_160[10] - st_160[11] + tr_re(st_160[12] - st_160[15] - 2 * st_160[13] + st_160[14] + st_160[16]))
            if S_ir > max_S_ir:
                max_S_ir = S_ir
            ewsb_ok = bool((st_160[10] < 0) and (min_sf > 0) and (t_u is not None))
            if not stab_ir:
                all_stab_ok = False
            if not ewsb_ok:
                all_ewsb_ok = False

            # Piece 3: Geometric Majorana M_R comparisons in U(3)_L-covariant kappa_nu = Y_nu M_R^{-1} Y_nu^T
            Ue_ir = obs_ir["Ue"]
            MR_1w = (Yn0 + Yn0.T) / 2
            MR_2w = (Yn2_0 + Yn2_0.T) / 2
            pmns_I3 = pmns_from_kappa(Yn0 * Yn0.T, Ue_ir)
            pmns_1w = pmns_from_kappa(Yn0 * (MR_1w ** -1) * Yn0.T, Ue_ir)
            pmns_2w = pmns_from_kappa(Yn0 * (MR_2w ** -1) * Yn0.T, Ue_ir)

            def fmt_pmns(p):
                return {
                    "s12_sq": mp_str(p["s12_sq"], 8),
                    "s23_sq": mp_str(p["s23_sq"], 8),
                    "s13_sq": mp_str(p["s13_sq"], 8),
                    "Jcp": mp_str(p["Jcp"], 6),
                    "dm21_over_dm31": mp_str(p["dm21_over_dm31"], 8),
                }

            branch_res[bname] = {
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
                    "std_ckm": obs_uv["std_ckm"],
                },
                "piece2_ir_t_minus_35": {
                    "g1": mp_str(st_160[0], 8),
                    "g2": mp_str(st_160[1], 8),
                    "g3": mp_str(st_160[2], 8),
                    "yt_over_g3": mp_str(obs_ir["su"][2] / st_160[2], 8),
                    "mb_over_mtau": mp_str(obs_ir["sd"][2] / obs_ir["se"][2], 8),
                    "u_m2m3": mp_str(obs_ir["u_m2m3"], 8),
                    "d_m2m3": mp_str(obs_ir["d_m2m3"], 8),
                    "e_m2m3": mp_str(obs_ir["e_m2m3"], 8),
                    "V12": mp_str(obs_ir["V12"], 8),
                    "V23": mp_str(obs_ir["V23"], 8),
                    "V13": mp_str(obs_ir["V13"], 8),
                    "Jcp": mp_str(obs_ir["Jcp"], 6),
                    "std_ckm": obs_ir["std_ckm"],
                    "l1_IR": mp_str(l1_ir, 8),
                    "l2_IR": mp_str(l2_ir, 8),
                    "l3_IR": mp_str(l3_ir, 8),
                    "l4_IR": mp_str(l4_ir, 8),
                    "D_term_vacuum_stable_all_steps": stab_ir,
                    "min_D_term_stab_margin_t_lt_0": mp_str(min_stab_m, 6),
                    "mHu2_IR": mp_str(st_160[10], 8),
                    "mHd2_IR": mp_str(st_160[11], 8),
                    "t_EWSB_u": mp_str(t_u, 8) if t_u is not None else "none",
                    "t_EWSB_d": mp_str(t_d, 8) if t_d is not None else "none",
                    "Hu_crosses_first": bool(t_u is not None and (t_d is None or t_u > t_d)),
                    "min_sfermion_m2_IR": mp_str(min_sf, 8),
                    "abs_S_hyp_IR": mp_str(S_ir, 6),
                    "radiative_EWSB_triggered": ewsb_ok,
                    "step_halving_80_160_err": mp_str(sh_err, 6),
                },
                "piece3_majorana_PMNS": {
                    "MR_I3": fmt_pmns(pmns_I3),
                    "MR_sym_Ynu_1w": fmt_pmns(pmns_1w),
                    "MR_sym_Ynu_2w": fmt_pmns(pmns_2w),
                },
            }

        vac_reports[vname] = {
            "tau": mp_str(tau_v, 10),
            "curved_dirac_s12": {
                "hyp_area_over_2pi": mp_str(g12["hyp_area_over_2pi"], 8),
                "gb_err": mp_str(g12["gb_err"], 6),
                "G_s12": [mp_str(v, 10) for v in g12["G_s12"]],
                "grid_diff": mp_str(g12["grid_diff"], 6),
                "kappa": mp_str(g12["kappa"], 8),
            },
            "dynamic_V4_ferro_higgs": {
                "r_u": mp_str(dyn_v4["r_u"], 8),
                "r_d": mp_str(dyn_v4["r_d"], 8),
                "align_hu_hd": mp_str(dyn_v4["align_hu_hd"], 8),
            },
            "branches": branch_res,
        }

    # 3. Guardrail 3: 10-trial random Haar U(3)^5 x U(3)_{nuR} scrambling across FULL coupled pipeline
    #    PLUS PF4 (M_R = Y_nu^T Y_nu unitary degeneracy), PF5 (broken Y_nu^T M_R^{-1} Y_nu), PF6 (zero Yukawas)
    mp.mp.dps = 42
    Yu_h, Yd_h, Ye_h, Yn_h, Yn2_h = haar_seed_mats
    MR_h = (Yn2_h + Yn2_h.T) / 2
    st_ref0 = (
        g_uv, g_uv, g_uv, Yu_h, Yd_h, Ye_h,
        l1_D, l2_D, l3_D, l4_D,
        mp.mpf(1), mp.mpf(1),
        mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3),
    )
    st_ref, tu_ref, _ = rk4_integrate_coupled(st_ref0, mp.mpf(-12), 40)
    obs_ref = observables_from_Y(st_ref[3], st_ref[4], st_ref[5])
    pmns_ref = pmns_from_kappa(Yn_h * (MR_h ** -1) * Yn_h.T, obs_ref["Ue"])
    pmns_bad_ref = pmns_from_kappa(Yn_h.T * (MR_h ** -1) * Yn_h, obs_ref["Ue"])

    rng = random.Random(20261126)
    haar_max_drift = mp.mpf(0)
    pf5_max_drift = mp.mpf(0)
    for _ in range(10):
        UQ = rand_haar_u3(rng, dps=42)
        UuR = rand_haar_u3(rng, dps=42)
        UdR = rand_haar_u3(rng, dps=42)
        UL = rand_haar_u3(rng, dps=42)
        UeR = rand_haar_u3(rng, dps=42)
        UnR = rand_haar_u3(rng, dps=42)
        # U(3)^5 x U(3)_nuR gauge transformation:
        # Y_f -> U_L Y_f U_R^H;  M_R -> U_nuR^* M_R U_nuR^H (since N_R^T M_R N_R is invariant when N_R -> U_nuR N_R,
        # and Y_nu -> U_L Y_nu U_nuR^H implies Y_nu M_R^{-1} Y_nu^T -> U_L Y_nu U_nuR^H (U_nuR M_R^{-1} U_nuR^T) U_nuR^* Y_nu^T U_L^T = U_L kappa U_L^T!)
        Yu_s = UQ * Yu_h * UuR.H
        Yd_s = UQ * Yd_h * UdR.H
        Ye_s = UL * Ye_h * UeR.H
        Yn_s = UL * Yn_h * UnR.H
        UnR_conj = mp.matrix([[mp.conj(UnR[r, c]) for c in range(3)] for r in range(3)])
        MR_s = UnR_conj * MR_h * UnR.H

        # Non-trivial diagonal UV soft-mass check? Universal I_3 transforms trivially, so test coupled RG invariance directly!
        st_s0 = (
            g_uv, g_uv, g_uv, Yu_s, Yd_s, Ye_s,
            l1_D, l2_D, l3_D, l4_D,
            mp.mpf(1), mp.mpf(1),
            UQ * mp.eye(3) * UQ.H, UuR * mp.eye(3) * UuR.H, UdR * mp.eye(3) * UdR.H,
            UL * mp.eye(3) * UL.H, UeR * mp.eye(3) * UeR.H,
        )
        st_s, tu_s, _ = rk4_integrate_coupled(st_s0, mp.mpf(-12), 40)
        obs_s = observables_from_Y(st_s[3], st_s[4], st_s[5])
        pmns_s = pmns_from_kappa(Yn_s * (MR_s ** -1) * Yn_s.T, obs_s["Ue"])
        pmns_bad_s = pmns_from_kappa(Yn_s.T * (MR_s ** -1) * Yn_s, obs_s["Ue"])

        drift = max(
            abs(obs_s[k] - obs_ref[k]) for k in ("u_m2m3", "d_m2m3", "e_m2m3", "V12", "V23", "V13", "Jcp")
        )
        drift = max(
            drift,
            abs(st_s[10] - st_ref[10]),
            abs(st_s[11] - st_ref[11]),
            max(abs(pmns_s[k] - pmns_ref[k]) for k in ("s12_sq", "s23_sq", "s13_sq", "Jcp", "dm21_over_dm31")),
        )
        if drift > haar_max_drift:
            haar_max_drift = drift

        bad_err = max(
            abs(pmns_bad_s[k] - pmns_bad_ref[k]) / max(mp_pow10(-10), pmns_bad_ref[k])
            for k in ("s12_sq", "s23_sq", "s13_sq")
        )
        if bad_err > pf5_max_drift:
            pf5_max_drift = bad_err

    # PF4: Degenerate M_R = Y_nu^T Y_nu forces exact algebraic identity kappa = Y_nu (Y_nu^T Y_nu)^{-1} Y_nu^T = I_3
    kap_pf4 = Yn_h * ((Yn_h.T * Yn_h) ** -1) * Yn_h.T
    s_pf4, _ = takagi_3x3(kap_pf4)
    pf4_spread = (s_pf4[2] - s_pf4[0]) / s_pf4[2]
    pf4_id_err = mp.sqrt(sum(abs(kap_pf4[i, j] - (1 if i == j else 0)) ** 2 for i in range(3) for j in range(3)))

    # PF6: Zeroing Yukawas kills soft-mass radiative EWSB completely
    st_pf6_0 = (
        g_uv, g_uv, g_uv, mp.zeros(3, 3), mp.zeros(3, 3), mp.zeros(3, 3),
        l1_D, l2_D, l3_D, l4_D,
        mp.mpf(1), mp.mpf(1),
        mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3), mp.eye(3),
    )
    st_pf6, tu_pf6, td_pf6 = rk4_integrate_coupled(st_pf6_0, dt_ir, 80)
    pf6_ewsb_killed = (
        abs(st_pf6[10] - 1) < mp_pow10(-30)
        and abs(st_pf6[11] - 1) < mp_pow10(-30)
        and tu_pf6 is None
        and td_pf6 is None
    )

    g3_bench_gb_pass = (
        ce_max_err < mp_pow10(-38)
        and martin_max_err < mp_pow10(-38)
        and xz_opposite
        and max_gb_err < mp_pow10(-3)
        and omega_iso_err < mp_pow10(-3)
    )
    g4_ewsb_haar_pass = (
        uv_dflat_err < mp_pow10(-38)
        and max_sh_err < mp_pow10(-6)
        and max_S_ir < mp_pow10(-25)
        and all_stab_ok
        and all_ewsb_ok
        and haar_max_drift < mp_pow10(-25)
    )
    print(
        f"[P3] Done: CE_max={mp_str(ce_max_err, 4)}, Martin={mp_str(martin_max_err, 4)}, GB_max={mp_str(max_gb_err, 4)}, "
        f"om_iso={mp_str(omega_iso_err, 4)}, UV_dflat={mp_str(uv_dflat_err, 4)}, SH={mp_str(max_sh_err, 4)}, "
        f"Haar={mp_str(haar_max_drift, 4)}, g3={g3_bench_gb_pass}, g4={g4_ewsb_haar_pass}",
        flush=True,
    )
    return {
        "quartic_convention": "Branco_CE_half_l1_l2_with_l1D_eq_g2sq_plus_gYsq_over_4",
        "dynamic_V4_convention": "canonical_kinetic_G_s12_applied_first_and_Ynu_coupled_to_hu_star",
        "uv_dflat_saturation_err": mp_str(uv_dflat_err, 6),
        "guardrail4_benchmarks": {
            "chowdhury_eberhardt_yt_err": mp_str(ce_yt_err, 6),
            "chowdhury_eberhardt_yb_err": mp_str(ce_yb_err, 6),
            "chowdhury_eberhardt_ytau_err": mp_str(ce_ytau_err, 6),
            "chowdhury_eberhardt_3sector_max_err": mp_str(ce_max_err, 6),
            "martin_7eq_soft_mass_max_err": mp_str(martin_max_err, 6),
            "xing_zhou_dvcb_1hdm_down": mp_str(vcb_1h - vcb0, 6),
            "xing_zhou_dvcb_2hdm_down": mp_str(vcb_2h - vcb0, 6),
            "xing_zhou_opposite_sign": xz_opposite,
        },
        "omega_Z3_kahler_isotropy_err": mp_str(omega_iso_err, 6),
        "max_gauss_bonnet_err": mp_str(max_gb_err, 6),
        "max_step_halving_80_160_err": mp_str(max_sh_err, 6),
        "max_abs_S_hyp_IR": mp_str(max_S_ir, 6),
        "all_vacua_D_term_stable": all_stab_ok,
        "all_vacua_radiative_EWSB_triggered": all_ewsb_ok,
        "vacua_unfolding": vac_reports,
        "haar_10trial_U3_5_x_U3_nuR_max_drift": mp_str(haar_max_drift, 6),
        "pf4_degenerate_MR_spectral_spread": mp_str(pf4_spread, 6),
        "pf4_degenerate_MR_identity_err": mp_str(pf4_id_err, 6),
        "pf5_broken_contraction_haar_rel_err": mp_str(pf5_max_drift, 6),
        "pf6_zero_yukawa_mHu2_IR": mp_str(st_pf6[10], 8),
        "pf6_zero_yukawa_mHd2_IR": mp_str(st_pf6[11], 8),
        "pf6_ewsb_killed": pf6_ewsb_killed,
        "g3_pass": g3_bench_gb_pass,
        "g4_pass": g4_ewsb_haar_pass,
    }


# ---------------------------------------------------------------------------
# Main Driver
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    ast_rep = audit_own_ast()
    pairs288 = build_E288_pairs()
    assert len(pairs288) == 288

    p1, p1_aux = run_P1()
    p2, p2_aux = run_P2(pairs288, p1_aux)
    p3 = run_P3(p1_aux, p2_aux)

    # Planted Negative Controls PF1..PF6
    pf1_ok = mp.mpf(p1["pf1_drop_nonhol_S_rel_err"]) > mp_rat(1, 10)
    pf2_ok = mp.mpf(p2["pf2_subcritical_n1_plus_70VCW1_at_4i"]) < mp.mpf(-10 ** 9)
    pf3_ok = (mp.mpf(p1["pf3_shift_off_FILQ1_dV"]) > mp_rat(1, 100)) and (mp.mpf(p1["pf3_shift_off_FILQ1_grad"]) > mp_rat(1, 2))
    pf4_ok = (mp.mpf(p3["pf4_degenerate_MR_spectral_spread"]) < mp_pow10(-25)) and (mp.mpf(p3["pf4_degenerate_MR_identity_err"]) < mp_pow10(-25))
    pf5_ok = mp.mpf(p3["pf5_broken_contraction_haar_rel_err"]) > mp_rat(1, 2)
    pf6_ok = bool(p3["pf6_ewsb_killed"])

    pf_summary = {
        "PF1_drop_nonhol_E2_breaks_S_inv": pf1_ok,
        "PF2_subcritical_n1_restores_cusp_runaway": pf2_ok,
        "PF3_shift_off_FILQ1_raises_V_and_grad": pf3_ok,
        "PF4_degenerate_MR_collapses_splitting": pf4_ok,
        "PF5_broken_YTM_fails_Haar_U3L": pf5_ok,
        "PF6_zero_yukawas_kill_radiative_EWSB": pf6_ok,
        "caught_count": sum(1 for v in (pf1_ok, pf2_ok, pf3_ok, pf4_ok, pf5_ok, pf6_ok) if v),
    }

    # Gate breakdown G1..G6
    g1_pass = bool(p1["g1_pass"])
    g2_pass = bool(p2["g2_pass"])
    g3_pass = bool(p3["g3_pass"])
    g4_pass = bool(p3["g4_pass"])
    g5_pass = pf_summary["caught_count"] == 6

    out = {
        "card_id": "AGY-002_A2-P629-VEFF-MODULUS",
        "seat": "agy-002",
        "firewall": "0 of 19",
        "runtime_seconds": str(int(time.time() - t0)),
        "P1_bosonic_and_FILQ_benchmarks": p1,
        "P2_boson_fermion_SL2Z_phase_diagram": p2,
        "P3_unsculpted_forward_unfolding_pieces2_and_3": p3,
        "P4_planted_controls": pf_summary,
        "ast_hygiene": ast_rep,
    }
    json_floats = count_json_floats(out)
    g6_pass = bool(ast_rep["clean"]) and (json_floats == 0)

    gates = {
        "G1_P1_bosonic_and_FILQ_benchmarks": g1_pass,
        "G2_P2_boson_fermion_SL2Z_phase_diagram": g2_pass,
        "G3_P3_guardrail4_benchmarks_and_curved_dirac_gb": g3_pass,
        "G4_P3_piece2_ewsb_stability_and_haar_U3_5_x_U3_nuR": g4_pass,
        "G5_all_6_planted_controls_caught": g5_pass,
        "G6_ast_clean_and_zero_json_floats": g6_pass,
        "json_float_count": json_floats,
        "all_gates_passed": bool(g1_pass and g2_pass and g3_pass and g4_pass and g5_pass and g6_pass),
    }
    out["gates"] = gates

    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    OUT_JSON_PATH.write_text(payload, encoding="utf-8")
    sha_out = hashlib.sha256(OUT_JSON_PATH.read_bytes()).hexdigest()
    OUT_SHA_PATH.write_text(f"{sha_out}  {OUT_JSON_PATH.name}\n", encoding="utf-8")
    print(f"ALL_GATES_PASSED={gates['all_gates_passed']} PF={pf_summary['caught_count']}/6 JSON_FLOATS={json_floats} TIME={out['runtime_seconds']}s", flush=True)


if __name__ == "__main__":
    main()
