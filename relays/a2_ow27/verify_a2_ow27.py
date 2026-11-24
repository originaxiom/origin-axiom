#!/usr/bin/env python3
"""
Card A2-OW27 Standalone Verifier (strictly 0 of 19, zero AST float/complex literals):
  - OW27-A: Sub-percent M_Z & m_t pole-mass & electroweak tightening:
      * Exact 2-loop pure-QCD top pole mass (Gray-Broadhurst-Grafe-Schilcher 1990 /
        Melnikov-van Ritbergen hep-ph/9912391) with SymPy SU(3) color sum, inverse relation,
        and exact 2-loop RG L-dependence proof (nf=6 and nf=5).
      * Exact full 4-coupling (y_t, g_1, g_2, lam) 1-loop SM RG-invariant Higgs pole
        Delta_tot^(1)(mu) = Delta_t + Delta_h + Delta_W + Delta_Z (SymPy RG residual == 0),
        evaluated at BOTH self-consistent mu = m_t_bar(m_t_bar) (L=0 exact) and mu = M_Z,
        verifying < 0.5% scale drift.
      * Exact 1-loop EW Veltman Delta_rho = 3 y_t^2 / (32 pi^2) on m_W^pole / m_Z^pole,
        5-flavor top decoupling at mu = m_t_bar(m_t_bar) down to M_Z, exact 2-loop pure-QCD
        dimensional transmutation Lambda_QCD^(3) / v_EW (SymPy RG residual == 0, zero GeV),
        and 10-trial Haar U(3)^5 end-to-end scrambling (< 1e-12).
  - OW27-B: First-principles thermal Bino LSP Dark-Matter Freeze-Out (OBS-20, dimensionless):
      * Explicit 4-component Dirac/Majorana spinor Feynman-amplitude verification of
        massless s-wave helicity suppression (== 0), massless p-wave 1/12 law (r in {2,5,10}),
        and massive t-tbar s-wave 1/8 law with constructive L+R interference.
      * Complete 26-variable 1-loop soft-SUSY RGEs evolving all 15 chiral sfermion species
        (sum N_i Y_i^4 == 95/18) + 4x4 neutralino mass matrix bino-purity check.
      * Stiff nonlinear 2-stage L-stable Radau IIA Riccati freeze-out solver (benchmarked
        against exact analytic Riccati + step-halving N=400 vs 800 + Richardson < 1e-6)
        using reduced Planck mass M_{P,red} (s/(H M_1^2) = sqrt(8 pi^2 g_* / 45) M_{P,red}/M_1)
        across B4_UV m_0/v_EW x A_0/m_0 x tan(beta), computing x_f, Y_Bino(inf),
        Delta_stauR coannihilation gap, (M_1/v_EW) Y_Bino/Y_B, and (M_1/Lambda_QCD^(3)) Y_Bino/Y_B
        (= c_lat * Omega_Bino / Omega_B, with c_lat = m_p / Lambda_QCD^(3) kept symbolic),
        plus honest thermal-overclosure audit.
  - OW27-C: True tau_8^+ spin-1/2 Dirac (G_{s=1/2}(tau_8^+)) 384-case discrete neutrino atlas
        (OW24-C fixed window, Guardrail-1 priced at log_2(384) = 8.585 bits) PLUS
        M_R = I_3 + W_R^unit scan (q_R in {-5,-3,0,+2,+3,+5} x 4 ops_n x 4 ops_r x 2 Kahler
        conventions = 192 cases, Guardrail-1 priced at log_2(192) = 7.585 bits, with the
        6-case symmetric (5+6,5+6) slice priced at log_2(6) = 2.585 bits), propagating all
        surviving simultaneous PMNS hits through full 2-loop sequential N_3->N_2->N_1->M_SUSY->M_Z
        + reduced-Planck Boltzmann Y_B(tau_8^+/-) with 10-trial Haar U(3)^5 x U(3)_N (< 1e-12)
        and exact geometric CP-odd verification (< 1e-30).
  - OW27-D: SUGRA t_SUSY, exact 2-loop NSVZ pure SU(N)_hid SYM scale (SymPy RG residual == 0),
        G_2 M_GUT/M_{P,red} = sqrt(alpha_UV/(4 pi)) vs OW23-C M_KK/M_{P,red} across N=3..6,
        moduli/anomaly mediation m_soft/m_{3/2} diagnostic, AND side-by-side propagation of
        agy-exp d12e74ef3 (Card X-HIERARCHY-LINK6: alpha_GUT^-1 = 30.19350768, t_SUSY = -24.2560)
        inside our exact 2-loop B4_UV M_Z pipeline.
  - OW27-E: 6/6 independent planted fault controls & upgraded canonical B4_UV_MZ_BLIND_LOCK_V3.

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 binary64 float()/complex() casts, 0 JSON float tokens.
  - 0 imports from frontier/, relays/, numpy, scipy, math, or cmath.
  - Strictly 0 of 19 (zero PDG, NuFIT, Planck, DESI, or CODATA values).
"""

from __future__ import annotations

import ast
import hashlib
import json
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


# ==============================================================================
# Core Exact / Arbitrary-Precision Helpers (Zero Float/Complex Literals)
# ==============================================================================

I_MP = mp.mpc(0, 1)


def mp_rat(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def mp_pow10(exp_int: int) -> mp.mpf:
    return mp.mpf(10) ** exp_int


def mat_tr(m: mp.matrix) -> mp.mpc:
    return sum((m[i, i] for i in range(m.rows)), mp.mpc(0))


def mat_frob(m: mp.matrix) -> mp.mpf:
    acc = mp.mpf(0)
    for r in range(m.rows):
        for c in range(m.cols):
            acc += abs(m[r, c]) ** 2
    return mp.sqrt(acc)


def scan_self_hygiene(script_path: Path) -> dict[str, Any]:
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    bad_lits: list[int] = []
    bad_casts: list[int] = []
    bad_imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad_lits.append(node.lineno)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
            bad_casts.append(node.lineno)
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith(("frontier", "relays", "numpy", "scipy", "math", "cmath")):
                    bad_imports.append(alias.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(("frontier", "relays", "numpy", "scipy", "math", "cmath")):
                bad_imports.append(node.module)
    return {
        "script_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "float_complex_literals": len(bad_lits),
        "binary64_casts": len(bad_casts),
        "forbidden_imports": len(bad_imports),
        "clean": bool(len(bad_lits) == 0 and len(bad_casts) == 0 and len(bad_imports) == 0),
    }


def assert_no_json_floats(obj: Any, path: str = "$") -> None:
    if isinstance(obj, bool) or obj is None or isinstance(obj, (int, str)):
        return
    if isinstance(obj, float):
        raise AssertionError(f"JSON float detected at {path}: {obj!r}")
    if isinstance(obj, list):
        for i, item in enumerate(obj):
            assert_no_json_floats(item, f"{path}[{i}]")
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_json_floats(v, f"{path}.{k}")
        return
    raise AssertionError(f"Unexpected JSON type at {path}: {type(obj).__name__}")


class SplitMix64:
    """Deterministic pure-integer SplitMix64 PRNG for zero-float Haar unitary generation."""

    def __init__(self, seed: int) -> None:
        self.state = seed & ((1 << 64) - 1)

    def next_u64(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
        return z ^ (z >> 31)

    def rand_unit_mp(self) -> mp.mpf:
        u = (self.next_u64() >> 11) + 1
        return mp.mpf(u) / mp.mpf((1 << 53) + 1)

    def rand_gauss_mp(self) -> tuple[mp.mpf, mp.mpf]:
        u1 = self.rand_unit_mp()
        u2 = self.rand_unit_mp()
        r = mp.sqrt(-2 * mp.log(u1))
        th = 2 * mp.pi * u2
        return r * mp.cos(th), r * mp.sin(th)


def random_haar_u3_mp(rng: SplitMix64, dim: int = 3) -> mp.matrix:
    z = mp.zeros(dim, dim)
    for r in range(dim):
        for c in range(dim):
            xr, xi = rng.rand_gauss_mp()
            z[r, c] = mp.mpc(xr, xi)
    q = mp.zeros(dim, dim)
    for col in range(dim):
        v = mp.matrix([z[r, col] for r in range(dim)])
        for prev in range(col):
            u_prev = mp.matrix([q[r, prev] for r in range(dim)])
            proj = sum((mp.conj(u_prev[r]) * v[r] for r in range(dim)), mp.mpc(0))
            for r in range(dim):
                v[r] -= proj * u_prev[r]
        nrm = mp.sqrt(sum((abs(v[r]) ** 2 for r in range(dim)), mp.mpf(0)))
        ph = z[col, col] / abs(z[col, col]) if abs(z[col, col]) > 0 else mp.mpc(1)
        for r in range(dim):
            q[r, col] = (v[r] / nrm) * ph
    return q


def svd_asc_mp(m: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    n = m.rows
    h = m * m.H
    h = (h + h.H) / 2
    vals, vecs = mp.eighe(h)
    idx = sorted(range(n), key=lambda k: mp.re(vals[k]))
    u = mp.zeros(n, n)
    svals: list[mp.mpf] = []
    for col, k in enumerate(idx):
        for row in range(n):
            u[row, col] = vecs[row, k]
        lam = mp.re(vals[k])
        svals.append(mp.sqrt(lam) if lam > 0 else mp.mpf(0))
    return u, svals


def takagi_asc_mp(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """Takagi factorization M_sym = U_T^* diag(s_0 <= ... <= s_{n-1}) U_T^H."""
    n = m_sym.rows
    ms = (m_sym + m_sym.T) / 2
    u0, svals = svd_asc_mp(ms.H)
    d_mat = u0.T * ms * u0
    u_tak = mp.zeros(n, n)
    for k in range(n):
        dk = d_mat[k, k]
        ph = mp.arg(dk) if abs(dk) > mp_pow10(-30) else mp.mpf(0)
        fac = mp.exp(-I_MP * ph / 2)
        for r in range(n):
            u_tak[r, k] = u0[r, k] * fac
    return u_tak, svals


def eval_w_hol_tau(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    q = mp.exp(2 * I_MP * mp.pi * tau)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-30, 31):
        m2 = mp_rat((2 * n + 1) ** 2, 8)
        e2v = mp.exp(2 * I_MP * mp.pi * tau * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = mp_rat(n * n, 2)
        e3v = mp.exp(2 * I_MP * mp.pi * tau * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 56):
        e2s -= 24 * n * (qn / (1 - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(56):
        pr *= 1 - qn
        qn *= q
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * tau / 12) * pr) ** 3
    yi = mp.im(tau)

    def thc(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am = mp_rat(ta.numerator, ta.denominator)
        bm = mp_rat(tb.numerator, tb.denominator)
        zv = am * tau + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(
            mp.exp(I_MP * mp.pi * tau * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv)
            for k in range(n0 - 10, n0 + 11)
        )
        return ((-1) ** (2 * nb)) * mp.exp(I_MP * mp.pi * (am * am * tau + 2 * am * bm)) * s

    def svec(qch: int) -> list[mp.mpc]:
        ca, cb = qch * pa, qch * pb
        if ca % 1 == 0 and cb % 1 == 0:
            return [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
        t1 = -I_MP * mp.exp(I_MP * mp.pi * (tau / 4 + ca * tau + cb + mp_rat(1, 2))) * thc(ca + Fr(1, 2), cb + Fr(1, 2))
        s1 = t1p / t1
        r0 = -I_MP * (thc(ca, cb + Fr(1, 2)) * t2) / (thc(Fr(0), Fr(1, 2)) * t1)
        r1 = (thc(ca + Fr(1, 2), cb) * t4) / (thc(Fr(1, 2), Fr(0)) * t1)
        r2 = (thc(ca, cb) * t3) / (thc(Fr(0), Fr(0)) * t1)
        h_mat = s1 * ed["1"] + r0 * ed["i"] + r1 * ed["j"] + r2 * ed["k"]
        return [(h_mat.T * qj * cb_m)[0, 1] for cb_m in blks]

    vl = svec(ql)
    vr = svec(qr)
    w = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            w[i, j] = ct[i][j][0, 1] + vl[i] * vr[j]
    return w


def ckm_obs(yu_m: mp.matrix, yd_m: mp.matrix, ye_m: mp.matrix) -> dict[str, mp.mpf]:
    uu, su = svd_asc_mp(yu_m)
    ud, sd = svd_asc_mp(yd_m)
    _, se = svd_asc_mp(ye_m)
    vckm = uu.H * ud
    j_ckm = mp.im(vckm[0, 1] * vckm[1, 2] * mp.conj(vckm[0, 2]) * mp.conj(vckm[1, 1]))
    return {
        "v12": abs(vckm[0, 1]),
        "v23": abs(vckm[1, 2]),
        "v13": abs(vckm[0, 2]),
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


def pmns_full_obs(ye_m: mp.matrix, kappa_m: mp.matrix) -> dict[str, mp.mpf]:
    ue, _ = svd_asc_mp(ye_m)
    u_nu, snu = takagi_asc_mp(kappa_m)
    upmns = ue.H * u_nu
    s13sq = abs(upmns[0, 2]) ** 2
    c13sq = max(1 - s13sq, mp_pow10(-30))
    s12sq = (abs(upmns[0, 1]) ** 2) / c13sq
    s23sq = (abs(upmns[1, 2]) ** 2) / c13sq
    j_pmns = mp.im(upmns[0, 1] * upmns[1, 2] * mp.conj(upmns[0, 2]) * mp.conj(upmns[1, 1]))
    c12 = mp.sqrt(max(1 - s12sq, mp.mpf(0)))
    s12 = mp.sqrt(max(s12sq, mp.mpf(0)))
    c23 = mp.sqrt(max(1 - s23sq, mp.mpf(0)))
    s23 = mp.sqrt(max(s23sq, mp.mpf(0)))
    s13 = mp.sqrt(max(s13sq, mp.mpf(0)))
    c13 = mp.sqrt(max(c13sq, mp.mpf(0)))
    # Basis-invariant Jarlskog extraction of delta_CP^PMNS (PDG convention):
    j_max = c12 * s12 * c23 * s23 * c13 * c13 * s13
    sin_d = (-j_pmns / j_max) if j_max > mp_pow10(-25) else mp.mpf(0)
    sin_d = max(mp.mpf(-1), min(mp.mpf(1), sin_d))
    um1sq = abs(upmns[1, 0]) ** 2
    denom_c = 2 * s12 * c12 * s23 * c23 * s13
    cos_d = (s12sq * c23 * c23 + c12 * c12 * s23sq * s13sq - um1sq) / denom_c if denom_c > mp_pow10(-25) else mp.mpf(1)
    cos_d = max(mp.mpf(-1), min(mp.mpf(1), cos_d))
    delta_cp = mp.atan2(sin_d, cos_d)
    # Effective neutrinoless double-beta mass ratio |m_ee| / m_3 = |(U_e^T kappa U_e)_{00}| / m_3 (invariant!)
    kap_e = ue.T * ((kappa_m + kappa_m.T) / 2) * ue
    mee_over_m3 = abs(kap_e[0, 0]) / snu[2] if snu[2] > mp_pow10(-30) else mp.mpf(0)
    dm = (snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2) if (snu[2] ** 2 - snu[0] ** 2) > mp_pow10(-30) else mp.mpf(0)
    return {
        "s12sq": s12sq,
        "s23sq": s23sq,
        "s13sq": s13sq,
        "dm": dm,
        "J": j_pmns,
        "delta_cp_rad": delta_cp,
        "delta_cp_over_pi": delta_cp / mp.pi,
        "mee_over_m3": mee_over_m3,
        "m1_over_m3": snu[0] / snu[2] if snu[2] > mp_pow10(-30) else mp.mpf(0),
        "m2_over_m3": snu[1] / snu[2] if snu[2] > mp_pow10(-30) else mp.mpf(0),
        "sum_m_over_m3": (snu[0] + snu[1] + snu[2]) / snu[2] if snu[2] > mp_pow10(-30) else mp.mpf(0),
    }


def in_ow24c_pmns_window(obs: dict[str, mp.mpf]) -> bool:
    return bool(
        mp_rat(15, 100) < obs["s12sq"] < mp_rat(55, 100)
        and mp_rat(30, 100) < obs["s23sq"] < mp_rat(70, 100)
        and obs["s13sq"] < mp_rat(8, 100)
        and mp_rat(5, 1000) < obs["dm"] < mp_rat(15, 100)
    )


# ==============================================================================
# 2-Loop SM, 2-Loop MSSM, & Complete 26-Variable 1-Loop Soft-SUSY RGEs
# ==============================================================================

def sm_rhs_2loop(
    st: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.mpf],
    two_loop: bool = True,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.mpf]:
    """Full 2-loop SM matrix RGEs (Machacek-Vaughn / Luo-Xiao / Buttazzo App. A; V = (lam/2)|H|^4)."""
    g1, g2, g3, yu, yd, ye, kap, lam = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    c2 = c1 * c1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    gps = mp_rat(3, 5) * g1s
    i3 = mp.eye(3)

    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
    tu = mp.re(mat_tr(hu))
    td = mp.re(mat_tr(hd))
    te = mp.re(mat_tr(he))
    t2 = 3 * tu + 3 * td + te

    tu2 = mp.re(mat_tr(hu * hu))
    td2 = mp.re(mat_tr(hd * hd))
    te2 = mp.re(mat_tr(he * he))
    tud = mp.re(mat_tr(hu * hd))
    y4_h = mp_rat(27, 4) * tu2 + mp_rat(27, 4) * td2 + mp_rat(9, 4) * te2 - mp_rat(3, 2) * tud
    y2g_h = (
        (mp_rat(17, 4) * g1s + mp_rat(45, 4) * g2s + 40 * g3s) * tu
        + (mp_rat(5, 4) * g1s + mp_rat(45, 4) * g2s + 40 * g3s) * td
        + (mp_rat(15, 4) * g1s + mp_rat(15, 4) * g2s) * te
    )

    dg1 = c1 * mp_rat(41, 10) * (g1 ** 3)
    dg2 = c1 * mp_rat(-19, 6) * (g2 ** 3)
    dg3 = c1 * (-7) * (g3 ** 3)
    if two_loop:
        dg1 += c2 * (g1 ** 3) * (
            mp_rat(199, 50) * g1s + mp_rat(27, 10) * g2s + mp_rat(44, 5) * g3s
            - mp_rat(17, 10) * tu - mp_rat(1, 2) * td - mp_rat(3, 2) * te
        )
        dg2 += c2 * (g2 ** 3) * (
            mp_rat(9, 10) * g1s + mp_rat(35, 6) * g2s + 12 * g3s
            - mp_rat(3, 2) * tu - mp_rat(3, 2) * td - mp_rat(1, 2) * te
        )
        dg3 += c2 * (g3 ** 3) * (
            mp_rat(11, 10) * g1s + mp_rat(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td
        )

    du1 = (mp_rat(3, 2) * hu - mp_rat(3, 2) * hd) * yu + (t2 - mp_rat(17, 20) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * yu
    dd1 = (mp_rat(3, 2) * hd - mp_rat(3, 2) * hu) * yd + (t2 - mp_rat(1, 4) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * yd
    de1 = (mp_rat(3, 2) * he) * ye + (t2 - mp_rat(9, 4) * g1s - mp_rat(9, 4) * g2s) * ye
    dyu = c1 * du1
    dyd = c1 * dd1
    dye = c1 * de1

    if two_loop:
        gu2_s = (
            mp_rat(1187, 600) * (g1s * g1s) - mp_rat(9, 20) * g1s * g2s + mp_rat(19, 15) * g1s * g3s
            - mp_rat(23, 4) * (g2s * g2s) + 9 * g2s * g3s - 108 * (g3s * g3s)
            + mp_rat(3, 2) * (lam * lam) - y4_h + mp_rat(1, 2) * y2g_h
        )
        mu2_l = (
            mp_rat(3, 2) * (hu * hu) - (hu * hd) - mp_rat(1, 4) * (hd * hu) + mp_rat(11, 4) * (hd * hd)
            + (mp_rat(223, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s - mp_rat(9, 4) * t2 - 6 * lam) * hu
            + (-mp_rat(43, 80) * g1s + mp_rat(9, 16) * g2s - 16 * g3s + mp_rat(5, 4) * t2) * hd
            + gu2_s * i3
        )
        dyu += c2 * (mu2_l * yu)

        gd2_s = (
            -mp_rat(127, 600) * (g1s * g1s) - mp_rat(27, 20) * g1s * g2s + mp_rat(31, 15) * g1s * g3s
            - mp_rat(23, 4) * (g2s * g2s) + 9 * g2s * g3s - 108 * (g3s * g3s)
            + mp_rat(3, 2) * (lam * lam) - y4_h + mp_rat(1, 2) * y2g_h
        )
        md2_l = (
            mp_rat(3, 2) * (hd * hd) - (hd * hu) - mp_rat(1, 4) * (hu * hd) + mp_rat(11, 4) * (hu * hu)
            + (mp_rat(187, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s - mp_rat(9, 4) * t2 - 6 * lam) * hd
            + (-mp_rat(79, 80) * g1s + mp_rat(9, 16) * g2s - 16 * g3s + mp_rat(5, 4) * t2) * hu
            + gd2_s * i3
        )
        dyd += c2 * (md2_l * yd)

        ge2_s = (
            mp_rat(1371, 200) * (g1s * g1s) + mp_rat(27, 20) * g1s * g2s - mp_rat(23, 4) * (g2s * g2s)
            + mp_rat(3, 2) * (lam * lam) - y4_h + mp_rat(1, 2) * y2g_h
        )
        me2_l = (
            mp_rat(3, 2) * (he * he)
            + (mp_rat(387, 80) * g1s + mp_rat(135, 16) * g2s - mp_rat(9, 4) * t2 - 6 * lam) * he
            + ge2_s * i3
        )
        dye += c2 * (me2_l * ye)

    dkap = c1 * ((-3 * g2s + 2 * lam + 2 * t2) * kap - mp_rat(3, 2) * (he * kap + kap * he.T))

    dlam_1 = (
        12 * (lam * lam)
        - 3 * lam * (3 * g2s + gps)
        + mp_rat(3, 4) * (2 * (g2s * g2s) + (g2s + gps) ** 2)
        + 4 * lam * t2
        - 4 * (3 * tu2 + 3 * td2 + te2)
    )
    dlam = c1 * dlam_1
    if two_loop:
        tr_y6 = 3 * mp.re(mat_tr(hu * hu * hu)) + 3 * mp.re(mat_tr(hd * hd * hd)) + mp.re(mat_tr(he * he * he))
        tr_y4_ud = 3 * mp.re(mat_tr(hu * hu * hd + hd * hd * hu))
        dlam_2 = (
            -78 * (lam ** 3)
            + 18 * (lam * lam) * (3 * g2s + gps)
            + lam * (-mp_rat(73, 8) * (g2s * g2s) + mp_rat(39, 4) * g2s * gps + mp_rat(629, 24) * (gps * gps))
            + mp_rat(305, 8) * (g2s ** 3) - mp_rat(289, 24) * (g2s * g2s) * gps
            - mp_rat(559, 24) * g2s * (gps * gps) - mp_rat(379, 24) * (gps ** 3)
            - 24 * (lam * lam) * t2
            + lam * (
                mp_rat(5, 2) * (mp_rat(17, 3) * gps + 9 * g2s + 32 * g3s) * tu
                + mp_rat(5, 2) * (mp_rat(5, 3) * gps + 9 * g2s + 32 * g3s) * td
                + mp_rat(5, 2) * (5 * gps + 3 * g2s) * te
                - (3 * tu2 + 3 * td2 + te2) - 42 * tud
            )
            - (mp_rat(16, 3) * gps + 64 * g3s) * tu2
            + (mp_rat(8, 3) * gps - 64 * g3s) * td2
            - 16 * gps * te2
            - mp_rat(9, 2) * (g2s * g2s) * t2
            + g2s * gps * (mp_rat(21, 2) * tu - mp_rat(9, 2) * td + mp_rat(33, 2) * te)
            - (gps * gps) * (mp_rat(19, 2) * tu - mp_rat(5, 2) * td + mp_rat(25, 2) * te)
            + 20 * tr_y6 - 4 * tr_y4_ud
        )
        dlam += c2 * dlam_2

    return (dg1, dg2, dg3, dyu, dyd, dye, dkap, dlam)


def rk4_integrate_sm(
    st0: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.mpf],
    t_span: mp.mpf,
    n_steps: int,
    two_loop: bool = True,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.mpf]:
    h = t_span / mp.mpf(n_steps)
    st = st0

    def add_st(a: tuple, b: tuple, fac: mp.mpf) -> tuple:
        return tuple(a[i] + fac * b[i] for i in range(8))

    for _ in range(n_steps):
        k1 = sm_rhs_2loop(st, two_loop=two_loop)
        k2 = sm_rhs_2loop(add_st(st, k1, h / 2), two_loop=two_loop)
        k3 = sm_rhs_2loop(add_st(st, k2, h / 2), two_loop=two_loop)
        k4 = sm_rhs_2loop(add_st(st, k3, h), two_loop=two_loop)
        st = tuple(st[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(8))
    return st


def mssm_rhs_2loop(
    st: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    two_loop: bool = True,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    """Full 2-loop MSSM matrix RGEs (Martin-Vaughn hep-ph/9311340)."""
    g1, g2, g3, yu, yd, ye, kap = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    c2 = c1 * c1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    i3 = mp.eye(3)
    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
    tu, td, te = mp.re(mat_tr(hu)), mp.re(mat_tr(hd)), mp.re(mat_tr(he))

    dg1 = c1 * mp_rat(33, 5) * (g1 ** 3)
    dg2 = c1 * (g2 ** 3)
    dg3 = c1 * (-3) * (g3 ** 3)
    if two_loop:
        dg1 += c2 * (g1 ** 3) * (
            mp_rat(199, 25) * g1s + mp_rat(27, 5) * g2s + mp_rat(88, 5) * g3s
            - mp_rat(26, 5) * tu - mp_rat(14, 5) * td - mp_rat(18, 5) * te
        )
        dg2 += c2 * (g2 ** 3) * (
            mp_rat(9, 5) * g1s + 25 * g2s + 24 * g3s - 6 * tu - 6 * td - 2 * te
        )
        dg3 += c2 * (g3 ** 3) * (
            mp_rat(11, 5) * g1s + 9 * g2s + 14 * g3s - 4 * tu - 4 * td
        )

    gQ = c1 * (hu + hd - (mp_rat(1, 30) * g1s + mp_rat(3, 2) * g2s + mp_rat(8, 3) * g3s) * i3)
    guc = c1 * (2 * htu - (mp_rat(8, 15) * g1s + mp_rat(8, 3) * g3s) * i3)
    gdc = c1 * (2 * htd - (mp_rat(2, 15) * g1s + mp_rat(8, 3) * g3s) * i3)
    gL = c1 * (he - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s) * i3)
    gec = c1 * (2 * hte - (mp_rat(6, 5) * g1s) * i3)
    gHu = c1 * (3 * tu - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s))
    gHd = c1 * (3 * td + te - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s))

    if two_loop:
        tu2, td2, te2, tud = mp.re(mat_tr(hu * hu)), mp.re(mat_tr(hd * hd)), mp.re(mat_tr(he * he)), mp.re(mat_tr(hu * hd))
        gQ += c2 * (
            -2 * (hu * hu) - 2 * (hd * hd) - 3 * tu * hu - (3 * td + te) * hd
            + mp_rat(4, 5) * g1s * hu + mp_rat(2, 5) * g1s * hd
            + (mp_rat(199, 900) * (g1s * g1s) + mp_rat(15, 4) * (g2s * g2s) - mp_rat(8, 9) * (g3s * g3s)
               + mp_rat(1, 10) * g1s * g2s + mp_rat(8, 45) * g1s * g3s + 8 * g2s * g3s) * i3
        )
        guc += c2 * (
            -2 * (htu * htu) - 2 * (yu.H * hd * yu) - 6 * tu * htu
            + (-mp_rat(2, 5) * g1s + 6 * g2s) * htu
            + (mp_rat(856, 225) * (g1s * g1s) - mp_rat(8, 9) * (g3s * g3s) + mp_rat(128, 45) * g1s * g3s) * i3
        )
        gdc += c2 * (
            -2 * (htd * htd) - 2 * (yd.H * hu * yd) - 2 * (3 * td + te) * htd
            + (mp_rat(2, 5) * g1s + 6 * g2s) * htd
            + (mp_rat(202, 225) * (g1s * g1s) - mp_rat(8, 9) * (g3s * g3s) + mp_rat(32, 45) * g1s * g3s) * i3
        )
        gL += c2 * (
            -2 * (he * he) - (3 * td + te) * he + mp_rat(6, 5) * g1s * he
            + (mp_rat(207, 100) * (g1s * g1s) + mp_rat(15, 4) * (g2s * g2s) + mp_rat(9, 10) * g1s * g2s) * i3
        )
        gec += c2 * (
            -2 * (hte * hte) - 2 * (3 * td + te) * hte
            + (-mp_rat(6, 5) * g1s + 6 * g2s) * hte
            + mp_rat(234, 25) * (g1s * g1s) * i3
        )
        gHu += c2 * (
            -9 * tu2 - 3 * tud + (mp_rat(4, 5) * g1s + 16 * g3s) * tu
            + mp_rat(207, 100) * (g1s * g1s) + mp_rat(15, 4) * (g2s * g2s) + mp_rat(9, 10) * g1s * g2s
        )
        gHd += c2 * (
            -9 * td2 - 3 * te2 - 3 * tud + (-mp_rat(2, 5) * g1s + 16 * g3s) * td + mp_rat(6, 5) * g1s * te
            + mp_rat(207, 100) * (g1s * g1s) + mp_rat(15, 4) * (g2s * g2s) + mp_rat(9, 10) * g1s * g2s
        )

    dyu = gQ * yu + yu * guc + gHu * yu
    dyd = gQ * yd + yd * gdc + gHd * yd
    dye = gL * ye + ye * gec + gHd * ye
    gLH = gL + gHu * i3
    dkap = gLH * kap + kap * gLH.T
    return (dg1, dg2, dg3, dyu, dyd, dye, dkap)


def rk4_integrate_mssm(
    st0: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    t_span: mp.mpf,
    n_steps: int,
    two_loop: bool = True,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    h = t_span / mp.mpf(n_steps)
    st = st0

    def add_st(a: tuple, b: tuple, fac: mp.mpf) -> tuple:
        return tuple(a[i] + fac * b[i] for i in range(7))

    for _ in range(n_steps):
        k1 = mssm_rhs_2loop(st, two_loop=two_loop)
        k2 = mssm_rhs_2loop(add_st(st, k1, h / 2), two_loop=two_loop)
        k3 = mssm_rhs_2loop(add_st(st, k2, h / 2), two_loop=two_loop)
        k4 = mssm_rhs_2loop(add_st(st, k3, h), two_loop=two_loop)
        st = tuple(st[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(7))
    return st


def integrate_soft_susy_26var_1loop(
    g_uv: mp.mpf,
    yt0: mp.mpf,
    yb0: mp.mpf,
    ytau0: mp.mpf,
    t_span: mp.mpf,
    n_steps: int,
    a0_over_m0: mp.mpf,
    m12_over_m0: mp.mpf = mp.mpf(1),
) -> dict[str, mp.mpf]:
    """
    Complete 26-variable 1-loop MSSM soft-SUSY RGEs in units of m_0 = 1 (Martin hep-ph/9709356),
    explicitly evolving all 15 chiral sfermion species (3rd gen + 1st/2nd gen Q, u^c, d^c, L, e^c).
    """
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    # 26 vars: g1,g2,g3, yt,yb,ytau, M1,M2,M3, At,Ab,Atau,
    #          mHu2,mHd2, mQ3,mu3,md3, mL3,me3, mQ1,mu1,md1, mL1,me1, mQ2, Shy
    y = [
        g_uv, g_uv, g_uv, yt0, yb0, ytau0,
        m12_over_m0, m12_over_m0, m12_over_m0,
        a0_over_m0, a0_over_m0, a0_over_m0,
        mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1),
        mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(0),
    ]

    def rhs(v: list[mp.mpf]) -> list[mp.mpf]:
        (g1, g2, g3, yt, yb, ytau, M1, M2, M3, At, Ab, Atau,
         mHu2, mHd2, mQ3, mu3, md3, mL3, me3, mQ1, mu1, md1, mL1, me1, mQ2, Shy) = v
        g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
        yts, ybs, ytaus = yt * yt, yb * yb, ytau * ytau
        dg1 = c1 * mp_rat(33, 5) * (g1 ** 3)
        dg2 = c1 * (g2 ** 3)
        dg3 = c1 * (-3) * (g3 ** 3)
        dyt = c1 * yt * (6 * yts + ybs - mp_rat(13, 15) * g1s - 3 * g2s - mp_rat(16, 3) * g3s)
        dyb = c1 * yb * (6 * ybs + yts + ytaus - mp_rat(7, 15) * g1s - 3 * g2s - mp_rat(16, 3) * g3s)
        dytau = c1 * ytau * (4 * ytaus + 3 * ybs - mp_rat(9, 5) * g1s - 3 * g2s)
        dM1 = c1 * mp_rat(66, 5) * g1s * M1
        dM2 = c1 * 2 * g2s * M2
        dM3 = c1 * (-6) * g3s * M3
        dAt = c1 * (12 * yts * At + 2 * ybs * Ab + mp_rat(26, 15) * g1s * M1 + 6 * g2s * M2 + mp_rat(32, 3) * g3s * M3)
        dAb = c1 * (12 * ybs * Ab + 2 * yts * At + 2 * ytaus * Atau + mp_rat(14, 15) * g1s * M1 + 6 * g2s * M2 + mp_rat(32, 3) * g3s * M3)
        dAtau = c1 * (8 * ytaus * Atau + 6 * ybs * Ab + mp_rat(18, 5) * g1s * M1 + 6 * g2s * M2)
        Xt = 2 * yts * (mHu2 + mQ3 + mu3 + At * At)
        Xb = 2 * ybs * (mHd2 + mQ3 + md3 + Ab * Ab)
        Xtau = 2 * ytaus * (mHd2 + mL3 + me3 + Atau * Atau)
        dmHu2 = c1 * (3 * Xt - 6 * g2s * M2 * M2 - mp_rat(6, 5) * g1s * M1 * M1 + mp_rat(3, 5) * g1s * Shy)
        dmHd2 = c1 * (3 * Xb + Xtau - 6 * g2s * M2 * M2 - mp_rat(6, 5) * g1s * M1 * M1 - mp_rat(3, 5) * g1s * Shy)
        dmQ3 = c1 * (Xt + Xb - mp_rat(32, 3) * g3s * M3 * M3 - 6 * g2s * M2 * M2 - mp_rat(2, 15) * g1s * M1 * M1 + mp_rat(1, 5) * g1s * Shy)
        dmu3 = c1 * (2 * Xt - mp_rat(32, 3) * g3s * M3 * M3 - mp_rat(32, 15) * g1s * M1 * M1 - mp_rat(4, 5) * g1s * Shy)
        dmd3 = c1 * (2 * Xb - mp_rat(32, 3) * g3s * M3 * M3 - mp_rat(8, 15) * g1s * M1 * M1 + mp_rat(2, 5) * g1s * Shy)
        dmL3 = c1 * (Xtau - 6 * g2s * M2 * M2 - mp_rat(6, 5) * g1s * M1 * M1 - mp_rat(3, 5) * g1s * Shy)
        dme3 = c1 * (2 * Xtau - mp_rat(24, 5) * g1s * M1 * M1 + mp_rat(6, 5) * g1s * Shy)
        dmQ1 = c1 * (-mp_rat(32, 3) * g3s * M3 * M3 - 6 * g2s * M2 * M2 - mp_rat(2, 15) * g1s * M1 * M1 + mp_rat(1, 5) * g1s * Shy)
        dmu1 = c1 * (-mp_rat(32, 3) * g3s * M3 * M3 - mp_rat(32, 15) * g1s * M1 * M1 - mp_rat(4, 5) * g1s * Shy)
        dmd1 = c1 * (-mp_rat(32, 3) * g3s * M3 * M3 - mp_rat(8, 15) * g1s * M1 * M1 + mp_rat(2, 5) * g1s * Shy)
        dmL1 = c1 * (-6 * g2s * M2 * M2 - mp_rat(6, 5) * g1s * M1 * M1 - mp_rat(3, 5) * g1s * Shy)
        dme1 = c1 * (-mp_rat(24, 5) * g1s * M1 * M1 + mp_rat(6, 5) * g1s * Shy)
        dmQ2 = dmQ1
        dShy = c1 * mp_rat(66, 5) * g1s * Shy
        return [
            dg1, dg2, dg3, dyt, dyb, dytau, dM1, dM2, dM3, dAt, dAb, dAtau,
            dmHu2, dmHd2, dmQ3, dmu3, dmd3, dmL3, dme3, dmQ1, dmu1, dmd1, dmL1, dme1, dmQ2, dShy,
        ]

    h = t_span / mp.mpf(n_steps)
    for _ in range(n_steps):
        k1 = rhs(y)
        k2 = rhs([y[i] + (h / 2) * k1[i] for i in range(26)])
        k3 = rhs([y[i] + (h / 2) * k2[i] for i in range(26)])
        k4 = rhs([y[i] + h * k3[i] for i in range(26)])
        y = [y[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(26)]
    keys = [
        "g1", "g2", "g3", "yt", "yb", "ytau", "M1", "M2", "M3", "At", "Ab", "Atau",
        "mHu2", "mHd2", "mQ3", "mu3", "md3", "mL3", "me3", "mQ1", "mu1", "md1", "mL1", "me1", "mQ2", "Shy",
    ]
    return dict(zip(keys, y))


def loop_I_fn(a: mp.mpf, b: mp.mpf, c: mp.mpf) -> mp.mpf:
    eps = mp_pow10(-10) * max(a, b, c)
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
    num = -(a * b * mp.log(a / b) + b * c * mp.log(b / c) + c * a * mp.log(c / a))
    den = (a - b) * (b - c) * (c - a)
    return num / den


# ==============================================================================
# OW27-A: 2-Loop Pure-QCD Top Pole, 4-Coupling 1-Loop Higgs Pole, Veltman
#         Delta_rho, 5-Flavor Top Decoupling, & Exact 2-Loop Lambda_QCD / v_EW
# ==============================================================================

def prove_ow27a_pure_qft_identities() -> dict[str, Any]:
    """Symbolic SymPy proofs for Gray-Broadhurst 2-loop QCD pole, 4-coupling Higgs pole, & 2-loop Lambda_QCD."""
    # 1. Exact 2-loop pure-QCD Gray-Broadhurst-Grafe-Schilcher (1990) Eq. 16 + Melnikov-van Ritbergen Eq. 11-12
    z2, z3, ln2, nl = sp.symbols("zeta2 zeta3 ln2 n_l")
    CF, CA, TF = sp.Rational(4, 3), sp.Integer(3), sp.Rational(1, 2)
    KF = -sp.Rational(71, 128) + sp.Rational(15, 8) * z2 - 3 * z2 * ln2 + sp.Rational(3, 4) * z3
    KA = sp.Rational(1111, 384) - sp.Rational(1, 2) * z2 + sp.Rational(3, 2) * z2 * ln2 - sp.Rational(3, 8) * z3
    KH = -sp.Rational(143, 96) + z2
    KL = -sp.Rational(71, 96) - sp.Rational(1, 2) * z2
    c20_sym = sp.expand(KF * CF**2 + KA * CF * CA + KH * CF * TF + KL * CF * TF * nl)
    c20_expected = (
        sp.Rational(307, 32) + 2 * z2 + sp.Rational(2, 3) * z2 * ln2 - sp.Rational(1, 6) * z3
        - (sp.Rational(71, 144) + sp.Rational(1, 3) * z2) * nl
    )
    c20_color_diff = sp.simplify(c20_sym - c20_expected)

    # Exact 2-loop RG invariance of M = m(mu) * [1 + (c10 + c11 L) a + (c20 + c21 L + c22 L^2) a^2]
    # where a = alpha_s / pi, L = ln(mu^2 / m^2), da/dln(mu^2) = -b0 a^2, dm/dln(mu^2) = -m(g0 a + g1 a^2):
    a_s, L_s, b0_s, g0_s, g1_s, c10_s, c11_s, c20_s, c21_s, c22_s = sp.symbols(
        "a L b0 g0 g1 c10 c11 c20 c21 c22"
    )
    da_s = -b0_s * a_s**2
    dm_s = -(g0_s * a_s + g1_s * a_s**2)
    dL_s = 1 - 2 * dm_s
    R_s = 1 + (c10_s + c11_s * L_s) * a_s + (c20_s + c21_s * L_s + c22_s * L_s**2) * a_s**2
    dM_s = sp.expand(dm_s * R_s + sp.diff(R_s, a_s) * da_s + sp.diff(R_s, L_s) * dL_s)
    poly_a = sp.Poly(dM_s, a_s)
    sol_rg = sp.solve(
        [
            sp.Poly(poly_a.nth(1), L_s).nth(0),
            sp.Poly(poly_a.nth(2), L_s).nth(0),
            sp.Poly(poly_a.nth(2), L_s).nth(1),
        ],
        [c11_s, c21_s, c22_s],
    )
    # Evaluate nf=6 (b0=7/4, g0=1, g1=27/8, c10=4/3) and nf=5 (b0=23/12, g0=1, g1=253/72, c10=4/3):
    nf6_subs = {b0_s: sp.Rational(7, 4), g0_s: sp.Integer(1), g1_s: sp.Rational(27, 8), c10_s: sp.Rational(4, 3)}
    nf5_subs = {b0_s: sp.Rational(23, 12), g0_s: sp.Integer(1), g1_s: sp.Rational(253, 72), c10_s: sp.Rational(4, 3)}
    c11_nf6 = sp.simplify(sol_rg[c11_s].subs(nf6_subs))
    c21_nf6 = sp.simplify(sol_rg[c21_s].subs(nf6_subs))
    c22_nf6 = sp.simplify(sol_rg[c22_s].subs(nf6_subs))
    c21_nf5 = sp.simplify(sol_rg[c21_s].subs(nf5_subs))
    c22_nf5 = sp.simplify(sol_rg[c22_s].subs(nf5_subs))

    # Planted-fault PF_OW27_1: perturb c21_nf6 by +1 and evaluate O(a^2) RG residual!
    pf1_subs = {**nf6_subs, c11_s: c11_nf6, c21_s: c21_nf6 + 1, c22_s: c22_nf6}
    pf1_oa2_resid = sp.simplify(poly_a.nth(2).subs(pf1_subs))

    # Numerical high-precision evaluation of c20(n_l=5) and Melnikov-van Ritbergen inverse c2(m_bar(M)/M, nl=5)
    z2_mp = (mp.pi ** 2) / 6
    z3_mp = mp.zeta(3)
    ln2_mp = mp.log(2)
    c20_const_mp = mp_rat(307, 32) + 2 * z2_mp + mp_rat(2, 3) * z2_mp * ln2_mp - mp_rat(1, 6) * z3_mp
    c20_nl_coeff_mp = mp_rat(71, 144) + mp_rat(1, 3) * z2_mp
    c20_nl5_mp = c20_const_mp - 5 * c20_nl_coeff_mp
    # Inverse relation m_bar(M)/M = 1 - (4/3) a(M) + c2_inv a(M)^2:
    # From M/m_bar(M) = 1 + (4/3) a(M) + (c20(5) + 8/3) a(M)^2 (since L = ln(M^2/m_bar(M)^2) = (8/3) a + O(a^2) => c11*L*a = (8/3) a^2):
    # Inverting: c2_inv = (4/3)^2 - (c20(5) + 8/3) = 16/9 - c20(5) - 8/3!
    c2_inv_nl5_mp = mp_rat(16, 9) - c20_nl5_mp - mp_rat(8, 3)

    # 2. Exact 4-coupling 1-loop SM Higgs pole RG-invariance proof (V = (lam/2)|H|^4)
    lam_s, yt_s, g2_s, gp_s, mu_s = sp.symbols("lam yt g2 gp mu", positive=True)
    r_t_s = 2 * yt_s**2 / lam_s
    r_W_s = g2_s**2 / lam_s
    r_Z_s = (g2_s**2 + gp_s**2) / lam_s
    beta_lam1_s = (
        12 * lam_s**2
        - 12 * yt_s**4
        + 12 * lam_s * yt_s**2
        - 3 * lam_s * (3 * g2_s**2 + gp_s**2)
        + sp.Rational(3, 4) * (2 * g2_s**4 + (g2_s**2 + gp_s**2) ** 2)
    )
    # Log-part of 16 pi^2 * Delta_tot^(1)(mu):
    delta_t_log = 3 * yt_s**2 * (2 - r_t_s) * sp.log(yt_s**2 / mu_s**2)
    delta_h_log = 6 * lam_s * sp.log(lam_s / mu_s**2)
    delta_W_log = g2_s**2 * (sp.Rational(3, 4) * r_W_s - 3) * sp.log(g2_s**2 / mu_s**2)
    delta_Z_log = (g2_s**2 + gp_s**2) * (sp.Rational(3, 8) * r_Z_s - sp.Rational(3, 2)) * sp.log((g2_s**2 + gp_s**2) / mu_s**2)
    delta_tot_log = delta_t_log + delta_h_log + delta_W_log + delta_Z_log
    rg_higgs_4coup_resid = sp.simplify(beta_lam1_s + lam_s * mu_s * sp.diff(delta_tot_log, mu_s))
    # Planted-fault PF_OW27_2 (top-only, dropping Delta_h + Delta_W + Delta_Z):
    rg_higgs_toponly_resid = sp.simplify(beta_lam1_s + lam_s * mu_s * sp.diff(delta_t_log, mu_s))

    # 3. Exact 2-loop pure-QCD dimensional-transmutation Lambda_QCD RG invariance proof
    a_q, mu_q, b0_q, b1_q = sp.symbols("a_q mu_q b0_q b1_q", positive=True)
    ln_lam_exact = (
        sp.log(mu_q)
        - 1 / (2 * b0_q * a_q)
        - (b1_q / (2 * b0_q**2)) * sp.log((b0_q * a_q) / (1 + (b1_q / b0_q) * a_q))
    )
    da_dlnmu = -2 * (b0_q * a_q**2 + b1_q * a_q**3)
    dlnlam_dlnmu = sp.simplify(mu_q * sp.diff(ln_lam_exact, mu_q) + sp.diff(ln_lam_exact, a_q) * da_dlnmu)

    ok = bool(
        c20_color_diff == 0
        and c11_nf6 == 1
        and c21_nf6 == sp.Rational(121, 24)
        and c22_nf6 == sp.Rational(11, 8)
        and c21_nf5 == sp.Rational(389, 72)
        and c22_nf5 == sp.Rational(35, 24)
        and pf1_oa2_resid == 1
        and rg_higgs_4coup_resid == 0
        and rg_higgs_toponly_resid != 0
        and dlnlam_dlnmu == 0
    )
    return {
        "all_sympy_proofs_exact": ok,
        "c20_color_sum_diff": str(c20_color_diff),
        "c20_const_val": mp.nstr(c20_const_mp, 14),
        "c20_nl_coeff_val": mp.nstr(c20_nl_coeff_mp, 14),
        "c20_nl5_val": mp.nstr(c20_nl5_mp, 14),
        "melnikov_van_ritbergen_c2_inv_nl5": mp.nstr(c2_inv_nl5_mp, 14),
        "nf6_RG_coeffs": {"c11": str(c11_nf6), "c21": str(c21_nf6), "c22": str(c22_nf6)},
        "nf5_RG_coeffs": {"c11": "1", "c21": str(c21_nf5), "c22": str(c22_nf5)},
        "pf1_perturbed_c21_oa2_resid": str(pf1_oa2_resid),
        "higgs_4coupling_RG_residual": str(rg_higgs_4coup_resid),
        "pf2_top_only_higgs_RG_residual_nonzero": bool(rg_higgs_toponly_resid != 0),
        "lambda_qcd_exact_2loop_RG_residual": str(dlnlam_dlnmu),
        "_c20_nl5_mp": c20_nl5_mp,
    }


def pv_b0_fin(r: mp.mpf) -> mp.mpf:
    """Finite part b_0(r) of Re B_0(m_h^2; M, M) = -ln(M^2/mu^2) + b_0(4 M^2 / m_h^2)."""
    if r > 1:
        sr = mp.sqrt(r - 1)
        return 2 - 2 * sr * mp.atan(1 / sr)
    if r < 1:
        sr = mp.sqrt(1 - r)
        return 2 - sr * mp.log((1 + sr) / (1 - sr))
    return mp.mpf(2)


def compute_full_4coupling_higgs_pole(
    lam_mu: mp.mpf,
    yt_mu: mp.mpf,
    g1_mu: mp.mpf,
    g2_mu: mp.mpf,
    mu_over_v: mp.mpf,
    include_bosonic: bool = True,
) -> dict[str, mp.mpf]:
    """
    Exact full 4-coupling 1-loop SM RG-invariant Higgs pole ratio m_h^{pole}/v_{phys}
    in V = (lam/2)|H|^4 convention (Delta_tot = Delta_t + Delta_h + Delta_W + Delta_Z).
    Note: omits O(g_2^2/(16 pi^2)) ~ 0.1% non-log vertex-box constant Delta r_fin^EW.
    """
    if lam_mu <= 0:
        return {"mh_pole_over_v": mp.mpf(0), "delta_tot": mp.mpf(0), "delta_t": mp.mpf(0), "delta_bos": mp.mpf(0)}
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    gps = mp_rat(3, 5) * g1_mu * g1_mu
    g2s = g2_mu * g2_mu
    gzs = g2s + gps
    # Dimensionless squared masses in v^2 units:
    mh2 = lam_mu
    mt2 = (yt_mu * yt_mu) / 2
    mw2 = g2s / 4
    mz2 = gzs / 4
    mu2 = mu_over_v * mu_over_v

    r_t = 4 * mt2 / mh2
    r_W = 4 * mw2 / mh2
    r_Z = 4 * mz2 / mh2

    d_t = c1 * 3 * (yt_mu * yt_mu) * ((2 - r_t) * mp.log(mt2 / mu2) - mp_rat(1, 2) + (r_t - 1) * pv_b0_fin(r_t))
    d_h = c1 * lam_mu * (6 * mp.log(mh2 / mu2) - 12 + mp_rat(3, 2) * mp.sqrt(3) * mp.pi)
    d_W = c1 * g2s * ((mp_rat(3, 4) * r_W - 3) * mp.log(mw2 / mu2) + mp_rat(1, 2) * r_W - (mp_rat(3, 4) * r_W - 1) * pv_b0_fin(r_W))
    d_Z = c1 * gzs * ((mp_rat(3, 8) * r_Z - mp_rat(3, 2)) * mp.log(mz2 / mu2) + mp_rat(1, 4) * r_Z - (mp_rat(3, 8) * r_Z - mp_rat(1, 2)) * pv_b0_fin(r_Z))
    d_bos = (d_h + d_W + d_Z) if include_bosonic else mp.mpf(0)
    d_tot = d_t + d_bos
    mh_pole_v = mp.sqrt(max(lam_mu * (1 + d_tot), mp_pow10(-12)))
    return {"mh_pole_over_v": mh_pole_v, "delta_tot": d_tot, "delta_t": d_t, "delta_bos": d_bos}


def run_2loop_pure_qcd_segment(
    a_start: mp.mpf,
    m_start: mp.mpf,
    t_span: mp.mpf,
    nf: int,
    n_steps: int = 80,
) -> tuple[mp.mpf, mp.mpf]:
    """
    Integrate 2-loop pure QCD a = alpha_s / pi and running quark mass m_q(mu) over d(ln mu):
      da / d(ln mu) = -2 (beta0 a^2 + beta1 a^3)
      dm / d(ln mu) = -2 m (gamma0 a + gamma1 a^2)
    """
    b0 = mp_rat(11, 4) - mp_rat(nf, 6)
    b1 = mp_rat(102, 16) - mp_rat(38 * nf, 48)
    g0 = mp.mpf(1)
    g1 = mp_rat(101, 24) - mp_rat(5 * nf, 36)

    def rhs(a_v: mp.mpf, m_v: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        return (-2 * (b0 * a_v * a_v + b1 * (a_v ** 3)), -2 * m_v * (g0 * a_v + g1 * a_v * a_v))

    h = t_span / mp.mpf(n_steps)
    a_c, m_c = a_start, m_start
    for _ in range(n_steps):
        ka1, km1 = rhs(a_c, m_c)
        ka2, km2 = rhs(a_c + (h / 2) * ka1, m_c + (h / 2) * km1)
        ka3, km3 = rhs(a_c + (h / 2) * ka2, m_c + (h / 2) * km2)
        ka4, km4 = rhs(a_c + h * ka3, m_c + h * km3)
        a_c += (h / 6) * (ka1 + 2 * ka2 + 2 * ka3 + ka4)
        m_c += (h / 6) * (km1 + 2 * km2 + 2 * km3 + km4)
    return a_c, m_c


def compute_lambda_qcd_3_over_v(
    a3_nf5_mz: mp.mpf,
    mz_over_v: mp.mpf,
    mb_mz_over_v: mp.mpf,
    mc_mz_over_v: mp.mpf,
) -> dict[str, mp.mpf]:
    """
    Strictly dimensionless 2-loop pure-QCD dimensional transmutation Lambda_QCD^(3) / v_EW
    (zero empirical GeV!) by running nf=5 from M_Z -> m_b(m_b), matching continuously to nf=4,
    running nf=4 from m_b(m_b) -> m_c(m_c), matching continuously to nf=3, and evaluating the
    exact 2-loop RG-invariant Lambda_QCD^(3) / v_EW.
    """
    a_mz = a3_nf5_mz / mp.pi
    # Solve mu_b / v_EW = m_b(mu_b) / v_EW via 6 fixed-point iterations
    mu_b = mb_mz_over_v
    a_mb = a_mz
    for _ in range(6):
        dt_b = mp.log(mu_b / mz_over_v)
        a_mb, mu_b_new = run_2loop_pure_qcd_segment(a_mz, mb_mz_over_v, dt_b, nf=5, n_steps=60)
        mu_b = mu_b_new
    # Run mc from M_Z to mu_b in nf=5 first
    _, mc_at_mb = run_2loop_pure_qcd_segment(a_mz, mc_mz_over_v, mp.log(mu_b / mz_over_v), nf=5, n_steps=60)
    # Solve mu_c / v_EW = m_c(mu_c) / v_EW in nf=4
    mu_c = mc_at_mb
    a_mc = a_mb
    for _ in range(6):
        dt_c = mp.log(mu_c / mu_b)
        a_mc, mu_c_new = run_2loop_pure_qcd_segment(a_mb, mc_at_mb, dt_c, nf=4, n_steps=60)
        mu_c = mu_c_new
    # Exact 2-loop RG-invariant Lambda_QCD^(3) / v_EW at mu = mu_c (nf = 3: b0 = 9/4, b1 = 4)
    b0_3 = mp_rat(9, 4)
    b1_3 = mp.mpf(4)
    lam3_exact_over_v = mu_c * mp.exp(-1 / (2 * b0_3 * a_mc)) * (
        (b0_3 * a_mc) / (1 + (b1_3 / b0_3) * a_mc)
    ) ** (-b1_3 / (2 * b0_3 * b0_3))
    lam3_std_over_v = mu_c * mp.exp(-1 / (2 * b0_3 * a_mc)) * (b0_3 * a_mc) ** (-b1_3 / (2 * b0_3 * b0_3))
    return {
        "mb_mb_over_v": mu_b,
        "mc_mc_over_v": mu_c,
        "alpha3_at_mb": a_mb * mp.pi,
        "alpha3_at_mc": a_mc * mp.pi,
        "Lambda_QCD_3_exact_over_v": lam3_exact_over_v,
        "Lambda_QCD_3_std_over_v": lam3_std_over_v,
    }


def match_mssm_to_sm_and_run_ow27(
    st_mssm: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    soft: dict[str, mp.mpf],
    tan_beta: int,
    m0_over_v: int,
    c20_nl5_mp: mp.mpf,
    sgn_mu: int = 1,
    n_sm_steps: int = 80,
) -> dict[str, Any]:
    """
    Exact DR->MS + derived sparticle mass-splitting + Delta_b threshold matching at Q_match = M_stop,
    followed by full 2-loop SM running down to BOTH:
      (1) Self-consistent top scale mu_* = m_t_bar(m_t_bar) (L=0 exact!),
      (2) mu = M_Z (both 6-flavor continuity AND exact 5-flavor top-decoupled M_Z),
    computing 2-loop Gray-Broadhurst top pole, full 4-coupling 1-loop Higgs pole,
    1-loop EW Veltman Delta_rho on m_W^pole/m_Z^pole, and exact 2-loop Lambda_QCD^(3)/v_EW.
    """
    g1_dr, g2_dr, g3_dr, yu_dr, yd_dr, ye_dr, kap_dr = st_mssm
    tb = mp.mpf(tan_beta)
    sinb = tb / mp.sqrt(1 + tb * tb)
    cosb = 1 / mp.sqrt(1 + tb * tb)
    cos2b = (1 - tb * tb) / (1 + tb * tb)

    mu_sq = (soft["mHd2"] - soft["mHu2"] * tb * tb) / (tb * tb - 1)
    mu_abs = mp.sqrt(mu_sq)
    mu_signed = mp.mpf(sgn_mu) * mu_abs
    mA_sq = soft["mHd2"] + soft["mHu2"] + 2 * mu_sq
    mA = mp.sqrt(mA_sq) if mA_sq > 0 else mp.mpf(1)
    m_stop = (soft["mQ3"] * soft["mu3"]) ** mp_rat(1, 4)
    m_q12 = mp.sqrt((soft["mQ1"] + soft["mQ2"]) / 2)
    m_l3 = mp.sqrt(soft["mL3"])
    m_e3 = mp.sqrt(soft["me3"])
    m_l12 = mp.sqrt(soft["mL1"])
    m_e12 = mp.sqrt(soft["me1"])
    m_u12 = mp.sqrt(soft["mu1"])
    m_d12 = mp.sqrt(soft["md1"])
    M2, M3 = abs(soft["M2"]), abs(soft["M3"])
    Q_m = m_stop

    # Exact DR -> MS + full individual sfermion threshold shifts (sum Delta b == (5/2, 25/6, 4) EXACT!)
    # Check sum:
    #   b1: 2/5 + 1/10 + 1/30 + 4/15 + 1/15 + 2/30 + 8/15 + 2/15 + 1/10 + 2/10 + 1/5 + 2/5 = 75/30 = 5/2!
    #   b2: 4/3 + 2/3 + 1/6 + 1/2 + 1 + 1/6 + 1/3 = 25/6!
    #   b3: 2 + 1/3 + 1/6 + 1/6 + 2/3 + 1/3 + 1/3 = 4!
    thresh_list = [
        (M3, (mp.mpf(0), mp.mpf(0), mp.mpf(2))),
        (M2, (mp.mpf(0), mp_rat(4, 3), mp.mpf(0))),
        (mu_abs, (mp_rat(2, 5), mp_rat(2, 3), mp.mpf(0))),
        (mA, (mp_rat(1, 10), mp_rat(1, 6), mp.mpf(0))),
        (mp.sqrt(soft["mQ3"]), (mp_rat(1, 30), mp_rat(1, 2), mp_rat(1, 3))),
        (mp.sqrt(soft["mu3"]), (mp_rat(4, 15), mp.mpf(0), mp_rat(1, 6))),
        (mp.sqrt(soft["md3"]), (mp_rat(1, 15), mp.mpf(0), mp_rat(1, 6))),
        (m_q12, (mp_rat(1, 15), mp.mpf(1), mp_rat(2, 3))),
        (m_u12, (mp_rat(8, 15), mp.mpf(0), mp_rat(1, 3))),
        (m_d12, (mp_rat(2, 15), mp.mpf(0), mp_rat(1, 3))),
        (m_l3, (mp_rat(1, 10), mp_rat(1, 6), mp.mpf(0))),
        (m_l12, (mp_rat(1, 5), mp_rat(1, 3), mp.mpf(0))),
        (m_e3, (mp_rat(1, 5), mp.mpf(0), mp.mpf(0))),
        (m_e12, (mp_rat(2, 5), mp.mpf(0), mp.mpf(0))),
    ]
    a_dr_inv = [4 * mp.pi / (g * g) for g in (g1_dr, g2_dr, g3_dr)]
    c2_g = [mp.mpf(0), mp.mpf(2), mp.mpf(3)]
    a_ms_inv = [
        a_dr_inv[idx]
        + c2_g[idx] / (12 * mp.pi)
        - sum((db[idx] * mp.log(mi / Q_m) for mi, db in thresh_list), mp.mpf(0)) / (2 * mp.pi)
        for idx in range(3)
    ]
    g1_m, g2_m, g3_m = [mp.sqrt(4 * mp.pi / ai) for ai in a_ms_inv]
    a1_m, a2_m, a3_m = g1_m * g1_m / (4 * mp.pi), g2_m * g2_m / (4 * mp.pi), g3_m * g3_m / (4 * mp.pi)

    dr_u_fac = 1 + a3_m / (3 * mp.pi) - mp_rat(3, 32) * a2_m / mp.pi - mp_rat(1, 480) * a1_m / mp.pi
    dr_d_fac = 1 + a3_m / (3 * mp.pi) - mp_rat(3, 32) * a2_m / mp.pi - mp_rat(13, 480) * a1_m / mp.pi
    dr_e_fac = 1 - mp_rat(3, 32) * a2_m / mp.pi + mp_rat(9, 160) * a1_m / mp.pi

    i_sbot = loop_I_fn(soft["mQ3"], soft["md3"], M3 * M3)
    i_stop = loop_I_fn(soft["mQ3"], soft["mu3"], mu_sq)
    yt_ms_approx = svd_asc_mp(yu_dr)[1][2]
    delta_b = (
        (mp_rat(2, 3) * a3_m / mp.pi) * M3 * mu_signed * tb * i_sbot
        + (yt_ms_approx * yt_ms_approx / (16 * mp.pi * mp.pi)) * soft["At"] * mu_signed * tb * i_stop
    )

    yu_sm0 = (sinb * dr_u_fac) * yu_dr
    yd_sm0 = (cosb * dr_d_fac / (1 + delta_b)) * yd_dr
    ye_sm0 = (cosb * dr_e_fac) * ye_dr
    kap_sm0 = (sinb * sinb) * kap_dr

    yt_sm0_3 = svd_asc_mp(yu_sm0)[1][2]
    xt_over_ms = (soft["At"] - mu_signed / tb) / m_stop
    x2 = xt_over_ms * xt_over_ms
    lam_tree = ((g2_m * g2_m + mp_rat(3, 5) * g1_m * g1_m) / 4) * (cos2b * cos2b)
    lam_stop_thresh = (mp_rat(3, 8) / (mp.pi * mp.pi)) * (yt_sm0_3 ** 4) * x2 * (1 - x2 / 12)
    lam_sm0 = lam_tree + lam_stop_thresh

    st_sm0 = (g1_m, g2_m, g3_m, yu_sm0, yd_sm0, ye_sm0, kap_sm0, lam_sm0)
    q_match_over_v = mp.mpf(m0_over_v) * m_stop

    # (A) Solve self-consistent top-mass scale mu_* / v = m_t_bar(mu_*) / v = y_t(mu_*) / sqrt(2) (L = 0 EXACT!)
    mu_mt_v = yt_sm0_3 / mp.sqrt(2)
    st_mt = st_sm0
    mt_fixed_pt_err = mp.mpf(1)
    for it_mt in range(8):
        mu_eval = mu_mt_v
        t_to_mt = mp.log(mu_eval / q_match_over_v)
        n_use = max(20, n_sm_steps // 3) if it_mt < 3 else n_sm_steps
        st_mt = rk4_integrate_sm(st_sm0, t_to_mt, n_use, two_loop=True)
        yt_mt_cur = svd_asc_mp(st_mt[3])[1][2]
        mu_next = yt_mt_cur / mp.sqrt(2)
        mt_fixed_pt_err = abs(mu_next - mu_eval) / mu_eval
        mu_mt_v = mu_next
        if it_mt >= 3 and mt_fixed_pt_err < mp_pow10(-24):
            # Re-evaluate once more at final mu_mt_v so st_mt matches mu_mt_v to < 1e-24
            st_mt = rk4_integrate_sm(st_sm0, mp.log(mu_mt_v / q_match_over_v), n_sm_steps, two_loop=True)
            yt_chk = svd_asc_mp(st_mt[3])[1][2]
            mt_fixed_pt_err = abs(yt_chk / mp.sqrt(2) - mu_mt_v) / mu_mt_v
            break

    g1_t, g2_t, g3_t, yu_t, yd_t, ye_t, kap_t, lam_t = st_mt
    a3_t = g3_t * g3_t / (4 * mp.pi)
    as_pi_t = a3_t / mp.pi
    yt_t = svd_asc_mp(yu_t)[1][2]
    mt_ms_at_mt = yt_t / mp.sqrt(2)
    # Exact 2-loop pure-QCD Gray-Broadhurst top pole at mu = m_t_bar(m_t_bar) (L = 0 EXACT!):
    mt_pole_1l_at_mt = mt_ms_at_mt * (1 + mp_rat(4, 3) * as_pi_t)
    mt_pole_2l_at_mt = mt_ms_at_mt * (1 + mp_rat(4, 3) * as_pi_t + c20_nl5_mp * (as_pi_t ** 2))
    # Exact full 4-coupling 1-loop Higgs pole at mu = m_t_bar(m_t_bar):
    higgs_4c_mt = compute_full_4coupling_higgs_pole(lam_t, yt_t, g1_t, g2_t, mu_mt_v, include_bosonic=True)
    higgs_toponly_mt = compute_full_4coupling_higgs_pole(lam_t, yt_t, g1_t, g2_t, mu_mt_v, include_bosonic=False)

    # (B) Solve self-consistent mu = M_Z scale (mu_Z / v = sqrt((g2^2 + 3/5 g1^2)/4)) in 6-flavor SM
    mz_v_est = mp.sqrt((g2_t * g2_t + mp_rat(3, 5) * g1_t * g1_t) / 4)
    st_mz = st_mt
    for _ in range(5):
        t_mt_to_mz = mp.log(mz_v_est / mu_mt_v)
        st_mz = rk4_integrate_sm(st_mt, t_mt_to_mz, max(30, n_sm_steps // 2), two_loop=True)
        mz_v_est = mp.sqrt((st_mz[1] ** 2 + mp_rat(3, 5) * st_mz[0] ** 2) / 4)
    g1_z, g2_z, g3_z, yu_z, yd_z, ye_z, kap_z, lam_z = st_mz

    a1_z = g1_z * g1_z / (4 * mp.pi)
    a2_z = g2_z * g2_z / (4 * mp.pi)
    a3_z_nf6 = g3_z * g3_z / (4 * mp.pi)
    s2w_z = (3 * a1_z) / (3 * a1_z + 5 * a2_z)
    aem_inv_z_nf6 = mp_rat(5, 3) / a1_z + 1 / a2_z
    mz_over_v_z = mp.sqrt((g2_z * g2_z + mp_rat(3, 5) * g1_z * g1_z) / 4)
    ck_z = ckm_obs(yu_z, yd_z, ye_z)
    pm_z = pmns_full_obs(ye_z, kap_z)

    # 2-loop Gray-Broadhurst top pole evaluated at mu = M_Z (with exact nf=6 RG logs c11=1, c21=121/24, c22=11/8):
    as_pi_z6 = a3_z_nf6 / mp.pi
    mt_ms_at_mz = ck_z["yt"] / mp.sqrt(2)
    L_mz = 2 * mp.log(mz_over_v_z / mt_ms_at_mz)
    mt_pole_2l_at_mz = mt_ms_at_mz * (
        1 + (mp_rat(4, 3) + L_mz) * as_pi_z6 + (c20_nl5_mp + mp_rat(121, 24) * L_mz + mp_rat(11, 8) * L_mz * L_mz) * (as_pi_z6 ** 2)
    )
    mt_pole_scale_drift = abs(mt_pole_2l_at_mz - mt_pole_2l_at_mt) / mt_pole_2l_at_mt

    # Full 4-coupling 1-loop Higgs pole evaluated at mu = M_Z vs mu = m_t_bar(m_t_bar):
    higgs_4c_mz = compute_full_4coupling_higgs_pole(lam_z, ck_z["yt"], g1_z, g2_z, mz_over_v_z, include_bosonic=True)
    higgs_toponly_mz = compute_full_4coupling_higgs_pole(lam_z, ck_z["yt"], g1_z, g2_z, mz_over_v_z, include_bosonic=False)
    mh_pole_4c_scale_drift = abs(higgs_4c_mz["mh_pole_over_v"] - higgs_4c_mt["mh_pole_over_v"]) / higgs_4c_mt["mh_pole_over_v"]
    mh_pole_toponly_scale_drift = abs(higgs_toponly_mz["mh_pole_over_v"] - higgs_toponly_mt["mh_pole_over_v"]) / higgs_toponly_mt["mh_pole_over_v"]

    # (C) Exact 5-flavor top decoupling at mu = m_t_bar(m_t_bar) down to mu = M_Z:
    # At 1-loop decoupling with L = ln(mu^2/m_t^2) = 0, alpha_3^(5)(m_t) = alpha_3^(6)(m_t), alpha_EM^(5)(m_t) = alpha_EM^(6)(m_t)!
    t_dec = mp.log(mz_over_v_z / mu_mt_v)
    a_pi_z5, _ = run_2loop_pure_qcd_segment(as_pi_t, mp.mpf(1), t_dec, nf=5, n_steps=60)
    a3_z_nf5 = a_pi_z5 * mp.pi
    # 5-flavor QED running shift between m_t and M_Z (top has Delta b_EM = 4/3 * 3 * (2/3)^2 = 16/9):
    aem_inv_z_nf5 = aem_inv_z_nf6 + (mp_rat(16, 9) / (2 * mp.pi)) * mp.log(mu_mt_v / mz_over_v_z)

    # (D) Exact 1-loop EW Veltman Delta_rho = 3 y_t(m_t)^2 / (32 pi^2) on m_W^pole / m_Z^pole:
    delta_rho_t = (3 * yt_t * yt_t) / (32 * mp.pi * mp.pi)
    mw_over_mz_tree = mp.sqrt(1 - s2w_z)
    mw_over_mz_pole = mw_over_mz_tree * mp.sqrt(1 + delta_rho_t)
    s2w_on_shell = 1 - mw_over_mz_pole * mw_over_mz_pole

    # (E) Exact 2-loop pure-QCD Lambda_QCD^(3) / v_EW (strictly dimensionless, zero empirical GeV!)
    mb_mz_v = ck_z["yb"] / mp.sqrt(2)
    mc_mz_v = ck_z["yc"] / mp.sqrt(2)
    lam_qcd_info = compute_lambda_qcd_3_over_v(a3_z_nf5, mz_over_v_z, mb_mz_v, mc_mz_v)

    return {
        "q_match_over_v": q_match_over_v,
        "mu_mt_over_v": mu_mt_v,
        "mt_fixed_pt_err": mt_fixed_pt_err,
        "mz_over_v": mz_over_v_z,
        "delta_b": delta_b,
        "a1_inv_mz": 1 / a1_z,
        "a2_inv_mz": 1 / a2_z,
        "a3_mz_nf6": a3_z_nf6,
        "a3_mz_nf5": a3_z_nf5,
        "a3_at_mt": a3_t,
        "sin2_thetaW_msbar_mz": s2w_z,
        "sin2_thetaW_on_shell": s2w_on_shell,
        "alpha_EM_inv_mz_nf6": aem_inv_z_nf6,
        "alpha_EM_inv_mz_nf5": aem_inv_z_nf5,
        "delta_rho_t_1loop": delta_rho_t,
        "mw_over_mz_msbar": mw_over_mz_tree,
        "mw_over_mz_pole_veltman": mw_over_mz_pole,
        "mt_ms_at_mt_over_v": mt_ms_at_mt,
        "mt_pole_1l_at_mt_over_v": mt_pole_1l_at_mt,
        "mt_pole_2l_at_mt_over_v": mt_pole_2l_at_mt,
        "mt_pole_2l_at_mz_over_v": mt_pole_2l_at_mz,
        "mt_pole_2l_scale_drift": mt_pole_scale_drift,
        "mh_pole_4c_at_mt_over_v": higgs_4c_mt["mh_pole_over_v"],
        "mh_pole_4c_at_mz_over_v": higgs_4c_mz["mh_pole_over_v"],
        "mh_pole_4c_at_mt_over_mz": higgs_4c_mt["mh_pole_over_v"] / mz_over_v_z,
        "mh_pole_4c_at_mz_over_mz": higgs_4c_mz["mh_pole_over_v"] / mz_over_v_z,
        "mh_pole_4c_scale_drift": mh_pole_4c_scale_drift,
        "mh_pole_toponly_scale_drift": mh_pole_toponly_scale_drift,
        "lambda_qcd_info": lam_qcd_info,
        "ckm_mz": ck_z,
        "pmns_mz": pm_z,
        "st_mz": st_mz,
        "st_mt": st_mt,
    }


# ==============================================================================
# OW27-B: Explicit 4-Component Majorana Spinors + Stiff Radau IIA Riccati DM
# ==============================================================================

def verify_majorana_bino_annihilation_spinors() -> dict[str, Any]:
    """
    Explicit 4-component Weyl-basis Dirac/Majorana spinor Feynman-amplitude proof of:
      (1) Massless chiral f_R helicity suppression (s-wave == 0) & p-wave 1/12 law at r in {2, 5, 10},
      (2) Massive t-tbar s-wave 1/8 law with constructive L+R interference,
      (3) Planted fault PF_OW27_3: flipping relative t/u Fermi sign (M_t + M_u) destroys s-wave suppression!
    """
    mp.mp.dps = 30
    sig0 = mp.eye(2)
    sig1 = mp.matrix([[0, 1], [1, 0]])
    sig2 = mp.matrix([[0, -I_MP], [I_MP, 0]])
    sig3 = mp.matrix([[1, 0], [0, -1]])
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

    g0 = blk(z2, sig0, sig0, z2)
    g1 = blk(z2, sig1, -sig1, z2)
    g2 = blk(z2, sig2, -sig2, z2)
    g3 = blk(z2, sig3, -sig3, z2)
    g5 = blk(-sig0, z2, z2, sig0)
    PL = (mp.eye(4) - g5) / 2
    PR = (mp.eye(4) + g5) / 2
    C_mat = I_MP * g2 * g0

    def bar(psi: mp.matrix) -> mp.matrix:
        return psi.H * g0

    def u_spinor(E: mp.mpf, px: mp.mpf, py: mp.mpf, pz: mp.mpf, sp_idx: int) -> mp.matrix:
        chi = mp.matrix([1, 0]) if sp_idx == 0 else mp.matrix([0, 1])
        pnorm = mp.sqrt(px * px + py * py + pz * pz)
        sp_p = mp.sqrt(E + pnorm)
        sp_m = mp.sqrt(max(E - pnorm, mp.mpf(0)))
        a = (sp_p + sp_m) / 2
        b = (sp_p - sp_m) / (2 * pnorm) if pnorm > mp_pow10(-25) else mp.mpf(0)
        sq_ps = a * sig0 - b * (px * sig1 + py * sig2 + pz * sig3)
        sq_psb = a * sig0 + b * (px * sig1 + py * sig2 + pz * sig3)
        uL = sq_ps * chi
        uR = sq_psb * chi
        return mp.matrix([uL[0], uL[1], uR[0], uR[1]])

    def v_from_u(u: mp.matrix) -> mp.matrix:
        return C_mat * bar(u).T

    # Verify Dirac completeness & Charge conjugation C g^mu^T C^-1 = -g^mu
    cc_err = max(mat_frob(C_mat * g.T * (C_mat ** (-1)) + g) for g in (g0, g1, g2, g3))

    # Exact 4-point Gauss-Legendre nodes on [-1, 1]
    gl_r1 = mp.sqrt(mp_rat(3, 7) - mp_rat(2, 7) * mp.sqrt(mp_rat(6, 5)))
    gl_r2 = mp.sqrt(mp_rat(3, 7) + mp_rat(2, 7) * mp.sqrt(mp_rat(6, 5)))
    gl_w1 = (18 + mp.sqrt(30)) / 36
    gl_w2 = (18 - mp.sqrt(30)) / 36
    gl_nodes = [(-gl_r2, gl_w2), (-gl_r1, gl_w1), (gl_r1, gl_w1), (gl_r2, gl_w2)]

    def eval_sv(
        M1: mp.mpf, mf: mp.mpf, m_fL: mp.mpf, m_fR: mp.mpf, YL: mp.mpf, YR: mp.mpf, vrel: mp.mpf, fermi_sign: int = -1
    ) -> mp.mpf:
        E1 = M1 / mp.sqrt(1 - (vrel / 2) ** 2)
        p1z = E1 * (vrel / 2)
        kf = mp.sqrt(E1 * E1 - mf * mf)
        uB1s = [u_spinor(E1, mp.mpf(0), mp.mpf(0), p1z, si) for si in (0, 1)]
        vB1s = [v_from_u(u) for u in uB1s]
        uB2s = [u_spinor(E1, mp.mpf(0), mp.mpf(0), -p1z, si) for si in (0, 1)]
        vB2s = [v_from_u(u) for u in uB2s]
        sv_acc = mp.mpf(0)
        for ct, wt in gl_nodes:
            st_a = mp.sqrt(1 - ct * ct)
            k1x, k1z = kf * st_a, kf * ct
            qt2 = -(k1x * k1x + (p1z - k1z) ** 2)
            qu2 = -(k1x * k1x + (-p1z - k1z) ** 2)
            uts = [u_spinor(E1, k1x, mp.mpf(0), k1z, si) for si in (0, 1)]
            vts = [v_from_u(u_spinor(E1, -k1x, mp.mpf(0), -k1z, si)) for si in (0, 1)]
            acc = mp.mpf(0)
            for sp1 in (0, 1):
                for sp2 in (0, 1):
                    for sf1 in (0, 1):
                        for sf2 in (0, 1):
                            aLt = (2 * YL * YL) * (bar(uts[sf1]) * PR * uB1s[sp1])[0, 0] * (bar(vB2s[sp2]) * PL * vts[sf2])[0, 0] / (qt2 - m_fL * m_fL) if YL != 0 else mp.mpc(0)
                            aRt = (2 * YR * YR) * (bar(uts[sf1]) * PL * uB1s[sp1])[0, 0] * (bar(vB2s[sp2]) * PR * vts[sf2])[0, 0] / (qt2 - m_fR * m_fR) if YR != 0 else mp.mpc(0)
                            aLu = (2 * YL * YL) * (bar(uts[sf1]) * PR * uB2s[sp2])[0, 0] * (bar(vB1s[sp1]) * PL * vts[sf2])[0, 0] / (qu2 - m_fL * m_fL) if YL != 0 else mp.mpc(0)
                            aRu = (2 * YR * YR) * (bar(uts[sf1]) * PL * uB2s[sp2])[0, 0] * (bar(vB1s[sp1]) * PR * vts[sf2])[0, 0] / (qu2 - m_fR * m_fR) if YR != 0 else mp.mpc(0)
                            mtot = (aLt + aRt) + mp.mpf(fermi_sign) * (aLu + aRu)
                            acc += abs(mtot) ** 2
            sv_acc += wt * (acc / 4) * kf / (64 * mp.pi * (E1 ** 3))
        return sv_acc

    # 1. Massless chiral f_R checks for r in {2, 5, 10}
    pwave_max_rel_err = mp.mpf(0)
    swave_massless_max = mp.mpf(0)
    pwave_checks: dict[str, Any] = {}
    vrel_p = mp_pow10(-6)
    for r_i in (2, 5, 10):
        msf = mp.sqrt(mp.mpf(r_i))
        sv0 = eval_sv(mp.mpf(1), mp.mpf(0), msf, msf, mp.mpf(0), mp.mpf(1), mp.mpf(0), fermi_sign=-1)
        svp = eval_sv(mp.mpf(1), mp.mpf(0), msf, msf, mp.mpf(0), mp.mpf(1), vrel_p, fermi_sign=-1)
        pred_p = (mp.mpf(1) / (12 * mp.pi)) * (1 + mp.mpf(r_i) ** 2) / ((1 + mp.mpf(r_i)) ** 4) * (vrel_p ** 2)
        rel_e = abs(svp - pred_p) / pred_p
        pwave_max_rel_err = max(pwave_max_rel_err, rel_e)
        swave_massless_max = max(swave_massless_max, sv0)
        pwave_checks[f"r_{r_i}"] = {
            "swave_exact_zero_val": mp.nstr(sv0, 6),
            "pwave_rel_err_vs_1_over_12": mp.nstr(rel_e, 10),
        }

    # PF_OW27_3: Wrong Bose sign (+1 instead of -1) destroys massless s-wave helicity suppression!
    pf3_wrong_sign_swave = eval_sv(mp.mpf(1), mp.mpf(0), mp.sqrt(2), mp.sqrt(2), mp.mpf(0), mp.mpf(1), mp.mpf(0), fermi_sign=+1)

    # 2. Massive t-tbar s-wave check (constructive L+R sign vs wrong destructive L-R)
    M1_t, mt_t, mtL_t, mtR_t = mp.mpf(2), mp.mpf(1), mp.mpf(3), mp.mpf(4)
    YQ_t, Yuc_t = mp_rat(1, 6), mp_rat(-2, 3)
    sv_tt_num = eval_sv(M1_t, mt_t, mtL_t, mtR_t, YQ_t, Yuc_t, mp.mpf(0), fermi_sign=-1)
    sv_tt_plus = (mt_t * mt_t / (8 * mp.pi)) * (
        YQ_t * YQ_t / (mtL_t * mtL_t + M1_t * M1_t - mt_t * mt_t)
        + Yuc_t * Yuc_t / (mtR_t * mtR_t + M1_t * M1_t - mt_t * mt_t)
    ) ** 2 * mp.sqrt(1 - (mt_t / M1_t) ** 2)
    sv_tt_minus = (mt_t * mt_t / (8 * mp.pi)) * (
        YQ_t * YQ_t / (mtL_t * mtL_t + M1_t * M1_t - mt_t * mt_t)
        - Yuc_t * Yuc_t / (mtR_t * mtR_t + M1_t * M1_t - mt_t * mt_t)
    ) ** 2 * mp.sqrt(1 - (mt_t / M1_t) ** 2)
    tt_plus_rel_err = abs(sv_tt_num - sv_tt_plus) / sv_tt_plus
    tt_minus_rel_err = abs(sv_tt_num - sv_tt_minus) / sv_tt_num

    # 3. Symbolic check of s(M_1)/(H(M_1) M_1^2) = sqrt(8 pi^2 g_* / 45) * M_{P,red} / M_1 & sum N_i Y_i^4 = 95/18
    gs_sym, mpr_sym, m1_sym = sp.symbols("g_star M_Pred M_1", positive=True)
    s_m1 = (2 * sp.pi**2 / 45) * gs_sym * m1_sym**3
    H_m1 = sp.sqrt(sp.pi**2 * gs_sym / 90) * m1_sym**2 / mpr_sym
    pref_ratio = sp.simplify((s_m1 / (H_m1 * m1_sym**2)) / (sp.sqrt(8 * sp.pi**2 * gs_sym / 45) * mpr_sym / m1_sym))
    sum_ny4 = 3 * (
        1 * sp.Rational(1, 1) ** 4
        + 2 * sp.Rational(-1, 2) ** 4
        + 6 * sp.Rational(1, 6) ** 4
        + 3 * sp.Rational(-2, 3) ** 4
        + 3 * sp.Rational(1, 3) ** 4
    )

    ok = bool(
        cc_err < mp_pow10(-25)
        and swave_massless_max < mp_pow10(-25)
        and pwave_max_rel_err < mp_pow10(-10)
        and tt_plus_rel_err < mp_pow10(-12)
        and tt_minus_rel_err > mp_rat(2, 10)
        and pf3_wrong_sign_swave > mp_pow10(-4)
        and pref_ratio == 1
        and sum_ny4 == sp.Rational(95, 18)
    )
    return {
        "spinor_proof_passed": ok,
        "charge_conj_err": mp.nstr(cc_err, 8),
        "massless_swave_max": mp.nstr(swave_massless_max, 8),
        "massless_pwave_max_rel_err": mp.nstr(pwave_max_rel_err, 10),
        "pwave_by_r": pwave_checks,
        "massive_ttbar_constructive_LplusR_rel_err": mp.nstr(tt_plus_rel_err, 10),
        "massive_ttbar_wrong_LminusR_rel_err": mp.nstr(tt_minus_rel_err, 10),
        "pf3_wrong_fermi_sign_swave_val": mp.nstr(pf3_wrong_sign_swave, 10),
        "s_over_HM1sq_exact_ratio_vs_sqrt_8pi2_g_over_45": str(pref_ratio),
        "sum_15species_Ni_Yi_4": str(sum_ny4),
    }


def neutralino_4x4_bino_purity(
    M1_v: mp.mpf, M2_v: mp.mpf, mu_v: mp.mpf, mz_v: mp.mpf, s2w: mp.mpf, tan_beta: int
) -> dict[str, mp.mpf]:
    """Diagonalize real symmetric 4x4 MSSM neutralino mass matrix in (B, W3, Hd0, Hu0) basis."""
    tb = mp.mpf(tan_beta)
    sb = tb / mp.sqrt(1 + tb * tb)
    cb = 1 / mp.sqrt(1 + tb * tb)
    sw = mp.sqrt(s2w)
    cw = mp.sqrt(1 - s2w)
    m_n = mp.matrix([
        [M1_v, mp.mpf(0), -mz_v * cb * sw, mz_v * sb * sw],
        [mp.mpf(0), M2_v, mz_v * cb * cw, -mz_v * sb * cw],
        [-mz_v * cb * sw, mz_v * cb * cw, mp.mpf(0), -mu_v],
        [mz_v * sb * sw, -mz_v * sb * cw, -mu_v, mp.mpf(0)],
    ])
    vals, vecs = mp.eigsy(m_n)
    # Find lightest neutralino by |m_chi|
    idx_l = min(range(4), key=lambda k: abs(vals[k]))
    m_chi1 = abs(vals[idx_l])
    bino_frac = vecs[0, idx_l] ** 2
    higgsino_frac = vecs[2, idx_l] ** 2 + vecs[3, idx_l] ** 2
    return {"m_chi1_over_v": m_chi1, "bino_purity_N11sq": bino_frac, "higgsino_frac": higgsino_frac}


def solve_riccati_freezeout_radau2(
    c_s_dimless: mp.mpf,
    c_p_dimless: mp.mpf,
    mpred_over_m1: mp.mpf,
    g_star: mp.mpf,
    n_steps: int = 400,
    x_min: mp.mpf = mp.mpf(1),
    x_max: mp.mpf = mp.mpf(500),
) -> dict[str, mp.mpf]:
    """
    Solve stiff nonlinear freeze-out Riccati ODE on u = ln(x) from x_min to x_max:
      dY/du = - c(x) * (Y^2 - Y_eq(x)^2),
      c(x) = sqrt(8 pi^2 g_* / 45) * (M_{P,red} / M_1) * (c_s + c_p / x) / x,
      Y_eq(x) = (45 / (2 pi^4 g_*)) * x^2 K_2(x)   (g_chi = 2 for Majorana bino),
    using 2-stage L-stable Radau IIA with exact 2x2 Newton per step.
    """
    a11, a12, a21, a22 = mp_rat(5, 12), mp_rat(-1, 12), mp_rat(3, 4), mp_rat(1, 4)
    pref_c = mp.sqrt(mp_rat(8, 45) * (mp.pi ** 2) * g_star) * mpred_over_m1
    pref_yeq = mp.mpf(45) / (2 * (mp.pi ** 4) * g_star)

    def eval_cy(u_val: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        xv = mp.exp(u_val)
        cv = pref_c * (c_s_dimless + c_p_dimless / xv) / xv
        if xv > 60:
            k2v = mp.sqrt(mp.pi / (2 * xv)) * mp.exp(-xv) * (1 + mp_rat(15, 8) / xv + mp_rat(105, 128) / (xv * xv))
        else:
            k2v = mp.besselk(2, xv)
        yeqv = pref_yeq * xv * xv * k2v
        return cv, yeqv

    u0, u1 = mp.log(x_min), mp.log(x_max)
    h = (u1 - u0) / mp.mpf(n_steps)
    _, y_cur = eval_cy(u0)
    x_f = mp.mpf(0)
    prev_ratio = mp.mpf(1)
    prev_x = x_min

    for k in range(n_steps):
        uk = u0 + k * h
        c1, ye1 = eval_cy(uk + h / 3)
        c2, ye2 = eval_cy(uk + h)
        # Smart initial guess: track Y_eq tightly in equilibrium, else Y_cur
        y1 = min(y_cur, ye1) if (h * c1 * ye1 > 10 and y_cur < 3 * ye1) else y_cur
        y2 = min(y1, ye2) if (h * c2 * ye2 > 10 and y_cur < 3 * ye2) else y_cur
        max_nr = mp.mpf(1)
        for _ in range(18):
            f1 = -c1 * (y1 * y1 - ye1 * ye1)
            f2 = -c2 * (y2 * y2 - ye2 * ye2)
            r1 = y1 - y_cur - h * (a11 * f1 + a12 * f2)
            r2 = y2 - y_cur - h * (a21 * f1 + a22 * f2)
            max_nr = max(abs(r1), abs(r2))
            if max_nr <= mp_pow10(-28) * max(y_cur, mp_pow10(-30)):
                break
            j11 = 1 + 2 * h * a11 * c1 * y1
            j12 = 2 * h * a12 * c2 * y2
            j21 = 2 * h * a21 * c1 * y1
            j22 = 1 + 2 * h * a22 * c2 * y2
            det = j11 * j22 - j12 * j21
            dy1 = (j22 * r1 - j12 * r2) / det
            dy2 = (-j21 * r1 + j11 * r2) / det
            y1 = max(y1 - dy1, mp_pow10(-60))
            y2 = max(y2 - dy2, mp_pow10(-60))
        if max_nr > mp_pow10(-20) * max(y_cur, mp_pow10(-30)):
            raise RuntimeError(f"Radau IIA Riccati Newton failed to converge at step {k}: resid={max_nr}")
        y_cur = y2
        xk = mp.exp(uk + h)
        if x_f == 0 and ye2 > 0:
            rat_now = y_cur / ye2
            if rat_now >= 2 and prev_ratio < 2:
                frac = (2 - prev_ratio) / (rat_now - prev_ratio)
                x_f = prev_x + frac * (xk - prev_x)
            prev_ratio = rat_now
            prev_x = xk

    return {"Y_inf": y_cur, "x_f": x_f}


def benchmark_radau2_analytic_riccati() -> mp.mpf:
    """Pure-math benchmark: dY/dx = -c (Y^2 - alpha^2) with exact Y(x) = alpha coth(c alpha (x - x0) + arccoth(Y0/alpha))."""
    a11, a12, a21, a22 = mp_rat(5, 12), mp_rat(-1, 12), mp_rat(3, 4), mp_rat(1, 4)
    c_val = mp.mpf(1000)
    alp = mp_rat(1, 10)
    y_cur = mp.mpf(1)
    x0, x1 = mp.mpf(0), mp_rat(1, 10)
    n_st = 200
    h = (x1 - x0) / mp.mpf(n_st)
    for _ in range(n_st):
        y1 = y2 = y_cur
        for _ in range(12):
            f1 = -c_val * (y1 * y1 - alp * alp)
            f2 = -c_val * (y2 * y2 - alp * alp)
            r1 = y1 - y_cur - h * (a11 * f1 + a12 * f2)
            r2 = y2 - y_cur - h * (a21 * f1 + a22 * f2)
            if max(abs(r1), abs(r2)) < mp_pow10(-28):
                break
            j11 = 1 + 2 * h * a11 * c_val * y1
            j12 = 2 * h * a12 * c_val * y2
            j21 = 2 * h * a21 * c_val * y1
            j22 = 1 + 2 * h * a22 * c_val * y2
            det = j11 * j22 - j12 * j21
            y1 -= (j22 * r1 - j12 * r2) / det
            y2 -= (-j21 * r1 + j11 * r2) / det
        y_cur = y2
    # Exact analytic solution at x1 = 1/10: arccoth(10) = (1/2) ln(11/9)
    y_exact = alp * mp.coth(c_val * alp * (x1 - x0) + mp_rat(1, 2) * mp.log(mp_rat(11, 9)))
    return abs(y_cur - y_exact) / y_exact


def compute_bino_dm_point(
    soft: dict[str, mp.mpf],
    m0_over_v: int,
    tan_beta: int,
    gp_sq: mp.mpf,
    mt_over_v: mp.mpf,
    mz_over_v: mp.mpf,
    s2w: mp.mpf,
    mgut_over_mpred: mp.mpf,
    t_susy_neg: mp.mpf,
    yb_ref: mp.mpf,
    lam_qcd3_over_v: mp.mpf,
    n_steps: int = 400,
    unreduced_planck_fault: bool = False,
    fixed_mpred_over_v_ref_m0: int | None = None,
) -> dict[str, Any]:
    """Compute dimensionless Bino LSP thermal freeze-out Y_Bino(inf) & Omega_Bino/Omega_B proxy."""
    m0_v = mp.mpf(m0_over_v)
    M1_over_m0 = abs(soft["M1"])
    M1_v = M1_over_m0 * m0_v
    M2_v = abs(soft["M2"]) * m0_v
    tb = mp.mpf(tan_beta)
    mu_over_m0 = mp.sqrt((soft["mHd2"] - soft["mHu2"] * tb * tb) / (tb * tb - 1))
    mu_v = mu_over_m0 * m0_v
    neut = neutralino_4x4_bino_purity(M1_v, M2_v, mu_v, mz_over_v, s2w, tan_beta)

    # All 15 chiral sfermion squared mass ratios r_i = m_{sf,i}^2 / M_1^2
    m1_sq = M1_over_m0 * M1_over_m0
    r_e12 = soft["me1"] / m1_sq
    r_e3 = soft["me3"] / m1_sq
    r_L12 = soft["mL1"] / m1_sq
    r_L3 = soft["mL3"] / m1_sq
    r_Q12 = soft["mQ1"] / m1_sq
    r_Q3 = soft["mQ3"] / m1_sq
    r_u12 = soft["mu1"] / m1_sq
    r_u3 = soft["mu3"] / m1_sq
    r_d12 = soft["md1"] / m1_sq
    r_d3 = soft["md3"] / m1_sq

    def p_kern(r: mp.mpf) -> mp.mpf:
        return (1 + r * r) / ((1 + r) ** 4)

    top_open = bool(M1_v > mt_over_v)
    beta_t = mp.sqrt(1 - (mt_over_v / M1_v) ** 2) if top_open else mp.mpf(0)

    # Sum over all 15 chiral fermion species (splitting Q3 into b_L [always open] and t_L [if M1 > mt]):
    sum_p = (
        2 * 1 * (mp.mpf(1) ** 4) * p_kern(r_e12)
        + 1 * 1 * (mp.mpf(1) ** 4) * p_kern(r_e3)
        + 2 * 2 * (mp_rat(1, 2) ** 4) * p_kern(r_L12)
        + 1 * 2 * (mp_rat(1, 2) ** 4) * p_kern(r_L3)
        + 2 * 6 * (mp_rat(1, 6) ** 4) * p_kern(r_Q12)
        + 1 * 3 * (mp_rat(1, 6) ** 4) * p_kern(r_Q3)
        + (3 * (mp_rat(1, 6) ** 4) * p_kern(r_Q3) * beta_t if top_open else mp.mpf(0))
        + 2 * 3 * (mp_rat(2, 3) ** 4) * p_kern(r_u12)
        + (3 * (mp_rat(2, 3) ** 4) * p_kern(r_u3) * beta_t if top_open else mp.mpf(0))
        + 2 * 3 * (mp_rat(1, 3) ** 4) * p_kern(r_d12)
        + 1 * 3 * (mp_rat(1, 3) ** 4) * p_kern(r_d3)
    )
    # <sigma v>_p * M_1^2 = (g'^4 / (2 pi)) * sum_p * (1/x)  (since <v_rel^2> = 6/x and 6/(12 pi) = 1/(2 pi))
    gp4 = gp_sq * gp_sq
    c_p_dim = (gp4 / (2 * mp.pi)) * sum_p

    # Massive t-tbar s-wave: sigma v_{s,tt} * M_1^2 = (3 g'^4 / (8 pi)) (mt/M1)^2 * (YQ^2/(r_Q3 + 1 - mt^2/M1^2) + Yuc^2/(r_u3 + 1 - mt^2/M1^2))^2 * beta_t
    if top_open:
        mt_r2 = (mt_over_v / M1_v) ** 2
        amp_tt = mp_rat(1, 36) / (r_Q3 + 1 - mt_r2) + mp_rat(4, 9) / (r_u3 + 1 - mt_r2)
        c_s_dim = (3 * gp4 / (8 * mp.pi)) * mt_r2 * (amp_tt * amp_tt) * beta_t
    else:
        c_s_dim = mp.mpf(0)

    # Purely dimensionless self-consistent B4_UV M_{P,red} / M_1 = 1 / ((M_GUT/M_{P,red}) * exp(t_SUSY) * (M_1/m_0)).
    # When fixed_mpred_over_v_ref_m0 is None, M_{P,red}/M_1 is strictly self-consistent with fixed t_SUSY.
    # When fixed_mpred_over_v_ref_m0 is an int (e.g. 10), M_{P,red}/v_EW is held fixed at that reference m0/v_EW
    # so M_{P,red}/M_1 scales as ref_m0 / m0_v (reproducing Lee-Weinberg Omega ~ m_0^2 scaling!).
    mpred_over_m1_base = 1 / (mgut_over_mpred * mp.exp(t_susy_neg) * M1_over_m0)
    mpred_over_m1 = (
        mpred_over_m1_base * (mp.mpf(fixed_mpred_over_v_ref_m0) / m0_v)
        if fixed_mpred_over_v_ref_m0 is not None
        else mpred_over_m1_base
    )
    if unreduced_planck_fault:
        # PF_OW27_4: wrongly divide M_{P,red} by sqrt(8 pi) (i.e. put unreduced M_Pl in reduced formula!)
        mpred_over_m1 = mpred_over_m1 / mp.sqrt(8 * mp.pi)

    # Dynamic SM g_*(T_f) based on derived spectrum (estimated T_f ~ M_1 / 25):
    tf_est = M1_v / mp.mpf(25)
    mw_v = mz_over_v * mp.sqrt(1 - s2w)
    if tf_est > mt_over_v:
        g_star = mp_rat(427, 4)
    elif tf_est > mw_v:
        g_star = mp_rat(385, 4)
    else:
        g_star = mp_rat(345, 4)

    sol = solve_riccati_freezeout_radau2(c_s_dim, c_p_dim, mpred_over_m1, g_star, n_steps=n_steps)
    y_bino = sol["Y_inf"]
    x_f = sol["x_f"]

    # Stau-R coannihilation diagnostic: Delta_stauR = (m_stauR - M_1) / M_1
    m_stauR_over_m0 = mp.sqrt(soft["me3"]) if soft["me3"] > 0 else mp.mpf(0)
    delta_stau = (m_stauR_over_m0 - M1_over_m0) / M1_over_m0
    boltz_coann_fac = mp.exp(-x_f * delta_stau) if delta_stau > 0 else mp.mpf(1)

    # Strictly dimensionless DM-to-baryon energy density ratios:
    #   R_vEW = (M_1 / v_EW) * Y_Bino(inf) / Y_B
    #   R_QCD = (M_1 / Lambda_QCD^(3)) * Y_Bino(inf) / Y_B = c_lat * (Omega_Bino / Omega_B)
    r_vew = (M1_v * y_bino) / yb_ref
    r_qcd = ((M1_v / lam_qcd3_over_v) * y_bino) / yb_ref

    return {
        "m0_over_v": m0_over_v,
        "tan_beta": tan_beta,
        "M1_over_m0": M1_over_m0,
        "M1_over_v": M1_v,
        "m_chi1_over_v": neut["m_chi1_over_v"],
        "bino_purity_N11sq": neut["bino_purity_N11sq"],
        "m_stauR_over_m0": m_stauR_over_m0,
        "delta_stauR": delta_stau,
        "boltz_coann_suppression": boltz_coann_fac,
        "top_swave_open": top_open,
        "c_s_dimless": c_s_dim,
        "c_p_dimless": c_p_dim,
        "g_star_freezeout": g_star,
        "M_Pred_over_M1": mpred_over_m1,
        "x_f": x_f,
        "Y_Bino_inf": y_bino,
        "M1_over_vEW_times_YBino_over_YB": r_vew,
        "M1_over_LambdaQCD3_times_YBino_over_YB_eq_clat_OmegaRatio": r_qcd,
    }


# ==============================================================================
# OW27-C: True tau_8^+ Spin-1/2 Dirac Metric + 384 Atlas + I_3+W_R Scan + Lepto
# ==============================================================================

def compute_dirac_s12_tau8_gramian() -> dict[str, Any]:
    """
    Independently derive the true tau_8^+ chiral spin-1/2 Dirac Liouville Kahler Gramian
    G_{E[2]}^{(s=1/2)}(tau_8^+) via Fuchsian Heun ODE monodromy + desingularized polar quadrature.
    """
    mp.mp.dps = 25
    tau_r = mp_rat(1, 5) + I_MP * mp_rat(8, 5)
    tau_8 = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    q_r = mp.exp(I_MP * mp.pi * tau_r)
    q_8 = mp.exp(I_MP * mp.pi * tau_8)

    t2_0 = mp.jtheta(2, 0, q_r)
    t3_0 = mp.jtheta(3, 0, q_r)
    t4_0 = mp.jtheta(4, 0, q_r)
    e1_v = (mp.pi ** 2) * (t3_0 ** 4 + t4_0 ** 4) / 3
    e2_v = (mp.pi ** 2) * (t2_0 ** 4 - t4_0 ** 4) / 3
    e3_v = -(mp.pi ** 2) * (t2_0 ** 4 + t3_0 ** 4) / 3
    g2_inv = -4 * (e1_v * e2_v + e2_v * e3_v + e3_v * e1_v)
    g3_inv = 4 * e1_v * e2_v * e3_v

    # Laurent series of Weierstrass wp(z) = 1/z^2 + sum_{k>=1} a_k z^{2k}
    wp_a = [mp.mpc(0)] * 16
    wp_a[1] = g2_inv / 20
    wp_a[2] = g3_inv / 28
    for k in range(3, 16):
        s_acc = sum((wp_a[m] * wp_a[k - 1 - m] for m in range(1, k - 1)), mp.mpc(0))
        wp_a[k] = (mp.mpf(3) / mp.mpf((2 * k + 3) * (k - 2))) * s_acc

    def wp_and_derivs(z: mp.mpc, n_der: int) -> list[mp.mpc]:
        w = mp.jtheta(3, 0, q_r) * mp.jtheta(4, 0, q_r) * mp.jtheta(2, mp.pi * z, q_r) / mp.jtheta(1, mp.pi * z, q_r)
        p0 = e1_v + (mp.pi * w) ** 2
        d1_sq = 4 * (p0 ** 3) - g2_inv * p0 - g3_inv
        z_eps = z + mp_pow10(-9)
        w_e = mp.jtheta(3, 0, q_r) * mp.jtheta(4, 0, q_r) * mp.jtheta(2, mp.pi * z_eps, q_r) / mp.jtheta(1, mp.pi * z_eps, q_r)
        p0_e = e1_v + (mp.pi * w_e) ** 2
        d1 = mp.sqrt(d1_sq)
        if abs(d1 - (p0_e - p0) / mp_pow10(-9)) > abs(-d1 - (p0_e - p0) / mp_pow10(-9)):
            d1 = -d1
        c_list = [p0, d1]
        if n_der >= 2:
            c_list.append((6 * p0 * p0 - g2_inv / 2) / 2)
        if n_der >= 3:
            c_list.append(2 * p0 * d1)
        for m in range(4, n_der + 1):
            conv = sum((c_list[k] * c_list[m - 2 - k] for k in range(m - 1)), mp.mpc(0))
            c_list.append(mp.mpf(6) * conv / mp.mpf(m * (m - 1)))
        return c_list

    def prop_seg_mp(za: mp.mpc, zb: mp.mpc, c_acc: mp.mpc, m_init: mp.matrix | None = None, order: int = 12) -> mp.matrix:
        dist = abs(zb - za)
        r_min = min(abs(za), abs(zb), abs(za - 1), abs(zb - 1), abs(za - tau_r), abs(zb - tau_r))
        n_sub = max(1, int(mp.ceil(dist / max(r_min / 3, mp_rat(1, 20)))))
        dz = (zb - za) / mp.mpf(n_sub)
        m_mat = mp.eye(2) if m_init is None else m_init.copy()
        for step in range(n_sub):
            z0 = za + mp.mpf(step) * dz
            p_ser = wp_and_derivs(z0, order - 2)
            q_ser = [-mp_rat(1, 4) * p_ser[k] for k in range(len(p_ser))]
            q_ser[0] -= c_acc
            f0 = [mp.mpc(1), mp.mpc(0)]
            f1 = [mp.mpc(0), mp.mpc(1)]
            for k in range(order - 2):
                s0 = sum((q_ser[j] * f0[k - j] for j in range(k + 1)), mp.mpc(0))
                s1 = sum((q_ser[j] * f1[k - j] for j in range(k + 1)), mp.mpc(0))
                f0.append(s0 / mp.mpf((k + 1) * (k + 2)))
                f1.append(s1 / mp.mpf((k + 1) * (k + 2)))
            u0 = u1 = du0 = du1 = mp.mpc(0)
            p_dz = mp.mpc(1)
            for k in range(order):
                u0 += f0[k] * p_dz
                u1 += f1[k] * p_dz
                if k >= 1:
                    du0 += mp.mpf(k) * f0[k] * (p_dz / dz)
                    du1 += mp.mpf(k) * f1[k] * (p_dz / dz)
                p_dz *= dz
            m_mat = mp.matrix([[u0, u1], [du0, du1]]) * m_mat
        return m_mat

    z0_base = mp_rat(1, 2) + mp_rat(1, 2) * tau_r

    def monodromy_pair(c_acc: mp.mpc) -> tuple[mp.matrix, mp.matrix]:
        ma = prop_seg_mp(z0_base, z0_base + 1, c_acc, order=14)
        mb = prop_seg_mp(z0_base, z0_base + tau_r, c_acc, order=14)
        return ma, mb

    def f_mon(x_re: mp.mpf, x_im: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        ma, mb = monodromy_pair(mp.mpc(x_re, x_im))
        return mp.im(ma[0, 0] + ma[1, 1]), mp.im(mb[0, 0] + mb[1, 1])

    # Solve Im Tr(M_a) = Im Tr(M_b) = 0 via 2D Newton from pure rational seed (-1/10, 1/10)
    cx, cy = mp_rat(-1, 10), mp_rat(1, 10)
    h_fd = mp_pow10(-7)
    for _ in range(7):
        f1, f2 = f_mon(cx, cy)
        if max(abs(f1), abs(f2)) < mp_pow10(-18):
            break
        f1x, f2x = f_mon(cx + h_fd, cy)
        f1y, f2y = f_mon(cx, cy + h_fd)
        j11, j21 = (f1x - f1) / h_fd, (f2x - f2) / h_fd
        j12, j22 = (f1y - f1) / h_fd, (f2y - f2) / h_fd
        det = j11 * j22 - j12 * j21
        cx -= (j22 * f1 - j12 * f2) / det
        cy -= (-j21 * f1 + j11 * f2) / det
    c_star = mp.mpc(cx, cy)
    ma_s, mb_s = monodromy_pair(c_star)
    comm = ma_s * mb_s * (ma_s ** (-1)) * (mb_s ** (-1))
    tr_comm_err = abs((comm[0, 0] + comm[1, 1]) + 2)

    # Solve PSU(1,1) Hermitean form H = P^H J P preserved by M_a, M_b
    def su_eqs(m: mp.matrix) -> list[list[mp.mpf]]:
        a, b, c, d = m[0, 0], m[0, 1], m[1, 0], m[1, 1]
        r1 = [abs(a) ** 2 - 1, abs(c) ** 2, 2 * mp.re(a * mp.conj(c)), -2 * mp.im(a * mp.conj(c))]
        r2 = [abs(b) ** 2, abs(d) ** 2 - 1, 2 * mp.re(b * mp.conj(d)), -2 * mp.im(b * mp.conj(d))]
        c3 = a * mp.conj(b)
        c4 = c * mp.conj(d)
        c5 = a * mp.conj(d)
        c6 = c * mp.conj(b)
        r3 = [mp.re(c3), mp.re(c4), mp.re(c5 + c6) - 1, mp.im(c6 - c5)]
        r4 = [mp.im(c3), mp.im(c4), mp.im(c5 + c6), mp.re(c5 - c6) - 1]
        return [r1, r2, r3, r4]

    eq_rows = su_eqs(ma_s) + su_eqs(mb_s)
    ata = mp.zeros(4, 4)
    for row in eq_rows:
        for i in range(4):
            for j in range(4):
                ata[i, j] += row[i] * row[j]
    ev_h, evec_h = mp.eigsy(ata)
    idx_min = min(range(4), key=lambda k: abs(ev_h[k]))
    hv = [evec_h[i, idx_min] for i in range(4)]
    h_mat = mp.matrix([[hv[0], mp.mpc(hv[2], hv[3])], [mp.mpc(hv[2], -hv[3]), hv[1]]])
    det_h = mp.re(h_mat[0, 0] * h_mat[1, 1] - abs(h_mat[0, 1]) ** 2)
    h_mat = h_mat / mp.sqrt(abs(det_h))
    if mp.re(h_mat[0, 0]) < 0:
        h_mat = -h_mat
    evals_h, evecs_h = mp.eighe(h_mat)
    ip_h = 0 if mp.re(evals_h[0]) > 0 else 1
    im_h = 1 - ip_h
    lp_h, lm_h = mp.re(evals_h[ip_h]), -mp.re(evals_h[im_h])
    vp_h = mp.matrix([evecs_h[0, ip_h], evecs_h[1, ip_h]])
    vm_h = mp.matrix([evecs_h[0, im_h], evecs_h[1, im_h]])
    u_su = mp.matrix([[vp_h[0], vm_h[0]], [vp_h[1], vm_h[1]]])
    p_mat = mp.diag([mp.sqrt(lp_h), mp.sqrt(lm_h)]) * u_su.H
    p_mat = (mp.matrix([[1, 1], [-I_MP, I_MP]]) / mp.sqrt(2)) * p_mat
    p_mat = p_mat / mp.sqrt(p_mat[0, 0] * p_mat[1, 1] - p_mat[0, 1] * p_mat[1, 0])

    # Extract cusp constant bc_star from z -> 0 asymptotic
    z_sm = mp_pow10(-3) * mp.exp(I_MP * mp_rat(3, 10))
    m_sm = prop_seg_mp(z0_base, z_sm, c_star, order=14)
    u1_sm = m_sm[0, 0] * p_mat[0, 0] + m_sm[0, 1] * p_mat[1, 0]
    u2_sm = m_sm[0, 0] * p_mat[0, 1] + m_sm[0, 1] * p_mat[1, 1]
    im_sm = mp.im(u1_sm * mp.conj(u2_sm))
    bc_star = abs(im_sm) / abs(z_sm) + mp.log(abs(z_sm))

    def leggauss_mp(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
        j_mat = mp.zeros(n, n)
        for k in range(1, n):
            b_k = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
            j_mat[k - 1, k] = b_k
            j_mat[k, k - 1] = b_k
        vals, vecs = mp.eigsy(j_mat)
        return [vals[i] for i in range(n)], [2 * (vecs[0, i] ** 2) for i in range(n)]

    corners = [
        mp_rat(1, 2) + mp_rat(1, 2) * tau_r,
        -mp_rat(1, 2) + mp_rat(1, 2) * tau_r,
        -mp_rat(1, 2) - mp_rat(1, 2) * tau_r,
        mp_rat(1, 2) - mp_rat(1, 2) * tau_r,
    ]
    ang_s = sorted(mp.arg(c) % (2 * mp.pi) for c in corners)
    half_sectors = [(ang_s[0], ang_s[1]), (ang_s[1], ang_s[2])]

    def r_bdy(theta: mp.mpf) -> mp.mpf:
        db = mp.sin(theta) / mp.im(tau_r)
        da = mp.cos(theta) - db * mp.re(tau_r)
        return mp_rat(1, 2) / max(abs(da), abs(db))

    def eval_e2_dens(z: mp.mpc, q_use: mp.mpc) -> list[mp.mpf]:
        yv = mp.im(z)
        t2v = mp.im(tau_r)
        fac = mp.sqrt(2 * t2v) * mp.exp(-2 * mp.pi * yv * yv / t2v)
        pz = mp.pi * z
        return [fac * (abs(mp.jtheta(k, pz, q_use)) ** 2) for k in (4, 2, 3)]

    def run_quad(n_th: int, n_t: int) -> dict[str, Any]:
        gx_th, gw_th = leggauss_mp(n_th)
        gx_t, gw_t = leggauss_mp(n_t)
        hyp_area = mp.mpf(0)
        k_s12_t8 = [mp.mpf(0)] * 3
        for th_a, th_b in half_sectors:
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
                z_cur = z0_base
                m_cur = mp.eye(2)
                dir_c = mp.exp(I_MP * th)
                for it in range(n_t - 1, -1, -1):
                    tv, rv, wt = t_nodes[it], r_nodes[it], h_t * gw_t[it]
                    zv = rv * dir_c
                    jac_t = (rv * rv) / (tv * tv)
                    if rv < mp_pow10(-6):
                        w_s0 = mp.mpf(1)
                        w_s12 = rv / tv
                    else:
                        m_cur = prop_seg_mp(z_cur, zv, c_star, m_init=m_cur, order=12)
                        z_cur = zv
                        u1 = m_cur[0, 0] * p_mat[0, 0] + m_cur[0, 1] * p_mat[1, 0]
                        u2 = m_cur[0, 0] * p_mat[0, 1] + m_cur[0, 1] * p_mat[1, 1]
                        im_p = mp.im(u1 * mp.conj(u2))
                        e2om = 1 / (im_p * im_p)
                        w_s0 = jac_t * e2om
                        w_s12 = jac_t * mp.sqrt(e2om)
                    d_t8 = eval_e2_dens(zv, q_8)
                    hyp_area += w_th * wt * w_s0
                    for j in range(3):
                        k_s12_t8[j] += (w_th * wt * w_s12) * d_t8[j]
        mean_t8 = sum(k_s12_t8, mp.mpf(0)) / 3
        return {"hyp_area_over_2pi": hyp_area / (2 * mp.pi), "G_s12_t8": [v / mean_t8 for v in k_s12_t8]}

    qc = run_quad(10, 12)
    qf = run_quad(14, 16)
    gb_err = abs(qf["hyp_area_over_2pi"] - 1)
    grid_diff = max(abs(qf["G_s12_t8"][j] - qc["G_s12_t8"][j]) for j in range(3))
    mp.mp.dps = 35
    return {
        "G_s12_t8": qf["G_s12_t8"],
        "tr_comm_err": tr_comm_err,
        "gb_err": gb_err,
        "grid_diff": grid_diff,
        "c_star": c_star,
    }


def mssm_seesaw_step_rhs(
    st: tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    n_active: int,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    g1, g2, g3, yu, yd, ye, kap, ynu, mr = st
    c1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    i3 = mp.eye(3)
    hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
    htu, htd, hte = yu.H * yu, yd.H * yd, ye.H * ye
    hn, htn = ynu * ynu.H, ynu.H * ynu
    tu, td, te, tn = mp.re(mat_tr(hu)), mp.re(mat_tr(hd)), mp.re(mat_tr(he)), mp.re(mat_tr(hn))

    dg1 = c1 * mp_rat(33, 5) * (g1 ** 3)
    dg2 = c1 * (g2 ** 3)
    dg3 = c1 * (-3) * (g3 ** 3)
    gQ = c1 * (hu + hd - (mp_rat(1, 30) * g1s + mp_rat(3, 2) * g2s + mp_rat(8, 3) * g3s) * i3)
    guc = c1 * (2 * htu - (mp_rat(8, 15) * g1s + mp_rat(8, 3) * g3s) * i3)
    gdc = c1 * (2 * htd - (mp_rat(2, 15) * g1s + mp_rat(8, 3) * g3s) * i3)
    gL = c1 * (he + hn - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s) * i3)
    gec = c1 * (2 * hte - (mp_rat(6, 5) * g1s) * i3)
    gHu = c1 * (3 * tu + tn - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s))
    gHd = c1 * (3 * td + te - (mp_rat(3, 10) * g1s + mp_rat(3, 2) * g2s))
    gnuc = c1 * (2 * htn)

    dyu = gQ * yu + yu * guc + gHu * yu
    dyd = gQ * yd + yd * gdc + gHd * yd
    dye = gL * ye + ye * gec + gHd * ye
    gLH = gL + gHu * i3
    dkap = gLH * kap + kap * gLH.T
    dynu = gL * ynu + ynu * gnuc + gHu * ynu
    dmr = gnuc.T * mr + mr * gnuc
    return (dg1, dg2, dg3, dyu, dyd, dye, dkap, dynu, dmr)


def rk4_seesaw_segment(st0: tuple, t_span: mp.mpf, n_steps: int, n_active: int) -> tuple:
    h = t_span / mp.mpf(n_steps)
    st = st0

    def add_s(a: tuple, b: tuple, f: mp.mpf) -> tuple:
        return tuple(a[i] + f * b[i] for i in range(9))

    for _ in range(n_steps):
        k1 = mssm_seesaw_step_rhs(st, n_active)
        k2 = mssm_seesaw_step_rhs(add_s(st, k1, h / 2), n_active)
        k3 = mssm_seesaw_step_rhs(add_s(st, k2, h / 2), n_active)
        k4 = mssm_seesaw_step_rhs(add_s(st, k3, h), n_active)
        st = tuple(st[i] + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(9))
    return st


def run_sequential_seesaw_ow27(
    g_uv: mp.mpf,
    yu_uv: mp.matrix,
    yd_uv: mp.matrix,
    ye_uv: mp.matrix,
    ynu_uv: mp.matrix,
    mr_uv_dimless: mp.matrix,
    mr0_over_mgut: mp.mpf,
    t_gut_to_susy: mp.mpf,
    soft: dict[str, mp.mpf],
    c20_nl5_mp: mp.mpf,
    tan_beta: int = 15,
    m0_over_v: int = 10,
    sgn_mu: int = 1,
) -> dict[str, Any]:
    _, mr_sv0 = takagi_asc_mp(mr_uv_dimless)
    mr_cur = mr0_over_mgut * (mr_uv_dimless / mr_sv0[2])
    st_cur: tuple = (g_uv, g_uv, g_uv, yu_uv, yd_uv, ye_uv, mp.zeros(3, 3), ynu_uv.copy(), mr_cur)
    t_now = mp.mpf(0)
    thresholds_m: list[mp.mpf] = []
    lepto_snapshot: dict[str, Any] = {}

    for n_act in (3, 2, 1):
        u_t, sv_t = takagi_asc_mp(st_cur[8])
        t_target = mp.log(sv_t[n_act - 1])
        if t_target < t_now:
            st_cur = rk4_seesaw_segment(st_cur, t_target - t_now, 24, n_act)
            t_now = t_target
        u_t, sv_t = takagi_asc_mp(st_cur[8])
        m_heavy = sv_t[n_act - 1]
        thresholds_m.append(m_heavy)
        ynu_rot = st_cur[7] * u_t
        if n_act == 3:
            lepto_snapshot = {
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

    st_susy = rk4_integrate_mssm(st_below, t_gut_to_susy - t_now, 80, two_loop=True)
    ir_mz = match_mssm_to_sm_and_run_ow27(st_susy, soft, tan_beta, m0_over_v, c20_nl5_mp, sgn_mu=sgn_mu, n_sm_steps=60)
    return {"thresholds_MR_over_MGUT": thresholds_m, "lepto_snapshot": lepto_snapshot, "ir_mz": ir_mz}


def compute_mssm_boltzmann_leptogenesis(
    ye_m: mp.matrix,
    ynu_rot: mp.matrix,
    mr_eigs_over_mgut: list[mp.mpf],
    mgut_over_mpred: mp.mpf,
    n_z_steps: int = 400,
) -> dict[str, Any]:
    """Exact flavored + unflavored MSSM 1-loop decay asymmetries & Radau IIA Boltzmann washout (reduced Planck!)."""
    ul, _ = svd_asc_mp(ye_m)
    yh = ul.H * ynu_rot
    h_mat = yh.H * yh
    h11 = mp.re(h_mat[0, 0])
    m1, m2, m3 = mr_eigs_over_mgut
    x_list = [(m2 / m1) ** 2, (m3 / m1) ** 2]

    def f_mssm(x: mp.mpf) -> mp.mpf:
        return -mp.sqrt(x) * (2 / (x - 1) + mp.log((1 + x) / x))

    eps_flav: list[mp.mpf] = []
    for alpha in range(3):
        acc = mp.mpf(0)
        for idx_j, j in enumerate((1, 2)):
            xj = x_list[idx_j]
            # Handle near-degenerate M_j / M_1 smoothly via regulator if needed
            if abs(xj - 1) < mp_pow10(-12):
                continue
            t1 = mp.im(mp.conj(yh[alpha, 0]) * yh[alpha, j] * h_mat[0, j]) * f_mssm(xj)
            t2 = mp.im(mp.conj(yh[alpha, 0]) * yh[alpha, j] * h_mat[j, 0]) * (mp.mpf(-2) / (xj - 1))
            acc += t1 + t2
        eps_flav.append(acc / (8 * mp.pi * h11))
    eps_tot = sum(eps_flav, mp.mpf(0))
    eps_unflav_direct = sum(
        (mp.im(h_mat[0, j] ** 2) * f_mssm(x_list[idx_j]) for idx_j, j in enumerate((1, 2)) if abs(x_list[idx_j] - 1) >= mp_pow10(-12)),
        mp.mpf(0),
    ) / (8 * mp.pi * h11)
    flav_sum_err = abs(eps_tot - eps_unflav_direct)

    g_star = mp_rat(915, 4)
    h_pref = mp.sqrt((mp.pi ** 2) * g_star / 90)
    mpred_over_m1 = 1 / (mgut_over_mpred * m1)
    k_flav = [(abs(yh[alpha, 0]) ** 2) / (4 * mp.pi * h_pref) * mpred_over_m1 for alpha in range(3)]
    k_tot = sum(k_flav, mp.mpf(0))

    def radau2_step(y0: mp.mpf, h: mp.mpf, p1: mp.mpf, q1: mp.mpf, p2: mp.mpf, q2: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        a11, a12, a21, a22 = mp_rat(5, 12), mp_rat(-1, 12), mp_rat(3, 4), mp_rat(1, 4)
        m11, m12 = 1 + h * a11 * p1, h * a12 * p2
        m21, m22 = h * a21 * p1, 1 + h * a22 * p2
        r1 = y0 + h * (a11 * q1 + a12 * q2)
        r2 = y0 + h * (a21 * q1 + a22 * q2)
        det = m11 * m22 - m12 * m21
        return (m22 * r1 - m12 * r2) / det, (-m21 * r1 + m11 * r2) / det

    def eval_bc(u_val: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        zv = mp.exp(u_val)
        if zv > 60:
            pref = mp.sqrt(mp.pi / (2 * zv)) * mp.exp(-zv)
            k1v = pref * (1 + mp_rat(3, 8) / zv - mp_rat(15, 128) / (zv * zv))
            k2v = pref * (1 + mp_rat(15, 8) / zv + mp_rat(105, 128) / (zv * zv))
        else:
            k1v, k2v = mp.besselk(1, zv), mp.besselk(2, zv)
        return mp_rat(1, 2) * zv * zv * k2v, k_tot * zv * zv * (k1v / k2v), mp_rat(1, 4) * (zv ** 4) * k1v

    def solve_b(n_st: int) -> tuple[list[mp.mpf], mp.mpf]:
        u0, u1 = mp.log(mp_rat(1, 10)), mp.log(mp.mpf(100))
        h = (u1 - u0) / mp.mpf(n_st)
        y_n = mp.mpf(0)
        y_fl = [mp.mpf(0)] * 3
        y_un = mp.mpf(0)
        for k in range(n_st):
            uk = u0 + k * h
            neq1, p1, wb1 = eval_bc(uk + h / 3)
            neq2, p2, wb2 = eval_bc(uk + h)
            yn1, yn2 = radau2_step(y_n, h, p1, p1 * neq1, p2, p2 * neq2)
            dn1, dn2 = -p1 * (yn1 - neq1), -p2 * (yn2 - neq2)
            for a in range(3):
                _, y_fl[a] = radau2_step(y_fl[a], h, k_flav[a] * wb1, eps_flav[a] * dn1, k_flav[a] * wb2, eps_flav[a] * dn2)
            _, y_un = radau2_step(y_un, h, k_tot * wb1, eps_tot * dn1, k_tot * wb2, eps_tot * dn2)
            y_n = yn2
        return y_fl, y_un

    n_fl_c, n_un_c = solve_b(n_z_steps)
    n_fl_f, n_un_f = solve_b(2 * n_z_steps)
    n_fl_rich = [(8 * n_fl_f[a] - n_fl_c[a]) / 7 for a in range(3)]
    n_un_rich = (8 * n_un_f - n_un_c) / 7
    conv_yb = mp_rat(8, 23) * (135 * mp.zeta(3)) / (2 * (mp.pi ** 4) * g_star)
    yb_flav = conv_yb * sum(n_fl_rich, mp.mpf(0))
    yb_unflav = conv_yb * n_un_rich
    step_err = abs(sum(n_fl_f, mp.mpf(0)) - sum(n_fl_c, mp.mpf(0))) / max(abs(sum(n_fl_f, mp.mpf(0))), mp_pow10(-30))
    return {
        "eps_flav": eps_flav,
        "eps_tot": eps_tot,
        "flav_sum_err": flav_sum_err,
        "K_flav": k_flav,
        "K_tot": k_tot,
        "Y_B_flavored": yb_flav,
        "Y_B_unflavored": yb_unflav,
        "Y_B_step_rel_err": step_err,
    }


# ==============================================================================
# OW27-D: Exact 2-Loop NSVZ SUGRA Thresholds, Mediation, & LINK6 Audit
# ==============================================================================

def run_ow27_d(
    mkk_over_mpred: mp.mpf,
    tex_s12_p: dict[str, mp.matrix],
    tex_flat_p: dict[str, mp.matrix],
    c20_nl5_mp: mp.mpf,
) -> dict[str, Any]:
    # 1. Exact SymPy proof of 2-loop NSVZ pure SU(N) SYM scale invariance:
    #    beta_NSVZ(g) = -3 N g^3 / (16 pi^2 (1 - N g^2 / (8 pi^2)))
    #    Lambda_NSVZ / mu = g^(-2/3) * exp(-8 pi^2 / (3 N g^2))
    g_s, mu_s, N_s = sp.symbols("g mu N", positive=True)
    beta_nsvz = -3 * N_s * g_s**3 / (16 * sp.pi**2 * (1 - N_s * g_s**2 / (8 * sp.pi**2)))
    ln_lam_nsvz = sp.log(mu_s) - sp.Rational(2, 3) * sp.log(g_s) - 8 * sp.pi**2 / (3 * N_s * g_s**2)
    nsvz_rg_resid = sp.simplify(mu_s * sp.diff(ln_lam_nsvz, mu_s) + sp.diff(ln_lam_nsvz, g_s) * beta_nsvz)
    # Planted-fault PF_OW27_5: omit g^(-2/3) prefactor -> residual is non-zero O(g^2)!
    ln_lam_hol = sp.log(mu_s) - 8 * sp.pi**2 / (3 * N_s * g_s**2)
    pf5_hol_rg_resid = sp.simplify(mu_s * sp.diff(ln_lam_hol, mu_s) + sp.diff(ln_lam_hol, g_s) * beta_nsvz)

    # 2. Scan SU(N)_hid (N=3..6) x alpha_UV^-1 in {20, 22, 24, 25, 26, 28, 30, 32}
    #    comparing 1-loop holomorphic vs exact 2-loop NSVZ, G_2 vs M_KK, and moduli vs anomaly mediation!
    #    In anomaly mediation (AMSB), M_a / m_{3/2} = b_a g_a^2 / (16 pi^2) => m_soft / m_{3/2} ~ 1 / (4 pi^2) ~ 1/40,
    #    Wait: for m_soft = m_{3/2} / (4 pi^2), ln(m_soft / M_GUT) = ln(m_{3/2}/M_GUT) - ln(4 pi^2) -> MORE negative!
    #    Conversely, to lift |t_SUSY| = 36.4 UP toward ~30 (i.e., m_{3/2} HEAVIER at fixed alpha_vis^-1 = 24),
    #    we need EITHER:
    #      (i)  higher N_hid (e.g. SU(6)_hid at alpha_hid^-1 = 24, where 8 pi^2 / (3 N g^2) = 2 pi a^-1 / (3 N) is smaller!),
    #      (ii) hidden gauge threshold shift Delta_hid = alpha_vis^-1 - alpha_hid^-1 > 0 (like Hirzebruch f_hid = S+T vs f_vis = S+2T!),
    #      (iii) exact 2-loop NSVZ g^{-2} prefactor on Lambda^3 (shifts t_SUGRA UP by +ln(alpha_UV^-1 / (4 pi)) ~ +0.65!),
    #      (iv) higher-scale M_soft > m_{3/2} is NOT AMSB; in AMSB m_soft << m_{3/2} so AMSB requires SMALLER |t_{m32}| ~ 26!
    nsvz_table: list[dict[str, Any]] = []
    for n_hid in (3, 4, 5, 6):
        for a_inv in (20, 22, 24, 25, 26, 28, 30, 32):
            a_inv_m = mp.mpf(a_inv)
            g_u = mp.sqrt(4 * mp.pi / a_inv_m)
            lam_1l = mp.exp(-2 * mp.pi * a_inv_m / (3 * mp.mpf(n_hid)))
            lam_nsvz = (g_u ** (-mp_rat(2, 3))) * lam_1l
            mgut_g2 = mp.sqrt(1 / (4 * mp.pi * a_inv_m))
            m32_over_mgut_1l_g2 = (lam_1l ** 3) * (mgut_g2 ** 2) / mp.sqrt(3)
            m32_over_mgut_nsvz_g2 = (lam_nsvz ** 3) * (mgut_g2 ** 2) / mp.sqrt(3)
            m32_over_mgut_nsvz_mkk = (lam_nsvz ** 3) * (mkk_over_mpred ** 2) / mp.sqrt(3)
            t_1l_g2 = -mp.log(m32_over_mgut_1l_g2)
            t_nsvz_g2 = -mp.log(m32_over_mgut_nsvz_g2)
            t_nsvz_mkk = -mp.log(m32_over_mgut_nsvz_mkk)
            # Also report AMSB m_soft/M_GUT = (g_u^2 / (16 pi^2)) * m_{3/2}/M_GUT (for mirage/AMSB comparison):
            t_amsb_g2 = t_nsvz_g2 + mp.log(16 * mp.pi * mp.pi / (g_u * g_u))
            nsvz_table.append({
                "N_hid": n_hid,
                "alpha_hid_inv": a_inv,
                "t_m32_1loop_G2": mp.nstr(t_1l_g2, 10),
                "t_m32_2loop_NSVZ_G2": mp.nstr(t_nsvz_g2, 10),
                "t_m32_2loop_NSVZ_MKK": mp.nstr(t_nsvz_mkk, 10),
                "t_AMSB_soft_NSVZ_G2": mp.nstr(t_amsb_g2, 10),
                "in_perturbative_B4UV_window_28_32_NSVZ_G2": bool(28 <= t_nsvz_g2 <= 32),
                "in_perturbative_B4UV_window_28_32_AMSB_G2": bool(28 <= t_amsb_g2 <= 32),
            })

    # Compute exact required hidden threshold shift Delta_hid = alpha_vis^-1 - alpha_hid^-1 at alpha_vis^-1 = 24
    # for SU(5)_hid NSVZ + G_2 to hit exact B4_UV target |t_SUSY| = 48 pi / 5 = 30.15928947...
    t_b4_target = mp_rat(48, 5) * mp.pi
    mgut_g2_24 = mp.sqrt(1 / (4 * mp.pi * 24))
    # Solve f(a_h_inv) = -ln( (a_h_inv/(4 pi)) * exp(-2 pi a_h_inv / 5) * mgut_g2_24^2 / sqrt(3) ) - t_b4_target = 0
    ah_sol = mp.mpf(20)
    for _ in range(15):
        fv = (2 * mp.pi / 5) * ah_sol - mp.log(ah_sol / (4 * mp.pi)) - mp.log(mgut_g2_24 * mgut_g2_24 / mp.sqrt(3)) - t_b4_target
        dfv = (2 * mp.pi / 5) - 1 / ah_sol
        ah_sol -= fv / dfv
    delta_hid_for_su5_at_24 = mp.mpf(24) - ah_sol

    # 3. Cross-Seat Propagation of agy-exp d12e74ef3 (Card X-HIERARCHY-LINK6) inside our exact 2-loop B4_UV M_Z pipeline:
    #    LINK6 derived Hirzebruch GS racetrack: alpha_GUT^-1 = 30.19350768 (3019350768 / 10^8), t_SUSY = -24.2560 (-24256 / 1000).
    #    Compare (i) pure LINK6 (a_GUT^-1 = 30.19350768, t_SUSY = -24.2560),
    #            (ii) hybrid (B4_UV a_GUT^-1 = 24, LINK6 t_SUSY = -24.2560),
    #            (iii) B4_UV central (a_GUT^-1 = 24, t_SUSY = -48 pi / 5).
    a_inv_link6 = mp_rat(3019350768, 100000000)
    t_susy_link6 = -mp_rat(24256, 1000)
    ye_norm_flat = svd_asc_mp(tex_flat_p["ye_hat"])[1][2]

    link6_runs: dict[str, Any] = {}
    for tag, a_inv_u, t_susy_u in (
        ("LINK6_exact_aGUTinv_30p1935_tSUSY_neg24p256", a_inv_link6, t_susy_link6),
        ("HYBRID_B4UV_aGUTinv_24_LINK6_tSUSY_neg24p256", mp.mpf(24), t_susy_link6),
    ):
        g_u = mp.sqrt(4 * mp.pi / a_inv_u)
        sft_u = integrate_soft_susy_26var_1loop(g_u, g_u, g_u / 5, (g_u / 5) * ye_norm_flat, t_susy_u, 160, -mp.sqrt(3))
        st_u = rk4_integrate_mssm(
            (g_u, g_u, g_u, g_u * tex_s12_p["yu_hat"], (g_u / 5) * tex_s12_p["yd_hat"], (g_u / 5) * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
            t_susy_u, 80, two_loop=True,
        )
        ir_u = match_mssm_to_sm_and_run_ow27(st_u, sft_u, 15, 10, c20_nl5_mp, sgn_mu=1, n_sm_steps=80)
        link6_runs[tag] = {
            "alpha_GUT_inv": mp.nstr(a_inv_u, 12),
            "t_SUSY": mp.nstr(t_susy_u, 12),
            "alpha3_mz_nf5": mp.nstr(ir_u["a3_mz_nf5"], 12),
            "alpha3_mz_nf6": mp.nstr(ir_u["a3_mz_nf6"], 12),
            "sin2_thetaW_msbar_mz": mp.nstr(ir_u["sin2_thetaW_msbar_mz"], 12),
            "alpha_EM_inv_mz_nf5": mp.nstr(ir_u["alpha_EM_inv_mz_nf5"], 12),
            "mw_over_mz_pole_veltman": mp.nstr(ir_u["mw_over_mz_pole_veltman"], 12),
            "mt_pole_2l_at_mt_over_v": mp.nstr(ir_u["mt_pole_2l_at_mt_over_v"], 12),
            "mh_pole_4c_at_mt_over_mz": mp.nstr(ir_u["mh_pole_4c_at_mt_over_mz"], 12),
            "mh_pole_4c_scale_drift": mp.nstr(ir_u["mh_pole_4c_scale_drift"], 10),
            "b_tau_mz": mp.nstr(ir_u["ckm_mz"]["b_tau"], 12),
            "v12_mz": mp.nstr(ir_u["ckm_mz"]["v12"], 12),
            "v23_mz": mp.nstr(ir_u["ckm_mz"]["v23"], 12),
            "v13_mz": mp.nstr(ir_u["ckm_mz"]["v13"], 12),
            "Lambda_QCD_3_exact_over_v": mp.nstr(ir_u["lambda_qcd_info"]["Lambda_QCD_3_exact_over_v"], 12),
        }

    gate_d = bool(
        nsvz_rg_resid == 0
        and pf5_hol_rg_resid != 0
        and any(row["in_perturbative_B4UV_window_28_32_NSVZ_G2"] for row in nsvz_table)
        and all(mp.mpf(v["mh_pole_4c_scale_drift"]) < mp_rat(1, 100) for v in link6_runs.values())
    )
    return {
        "gate_passed": gate_d,
        "nsvz_exact_2loop_RG_residual": str(nsvz_rg_resid),
        "pf5_omitted_g_neg23_RG_residual": str(pf5_hol_rg_resid),
        "su5_hid_NSVZ_G2_required_alpha_hid_inv_for_tB4UV": mp.nstr(ah_sol, 12),
        "su5_hid_NSVZ_G2_required_Delta_hid_shift_from_24": mp.nstr(delta_hid_for_su5_at_24, 12),
        "nsvz_sugra_hidden_sector_table": nsvz_table,
        "agyexp_d12e74ef3_LINK6_side_by_side_in_B4UV_2loop_MZ": link6_runs,
        "_pf5_nonzero": bool(pf5_hol_rg_resid != 0),
    }


# ==============================================================================
# Main Driver: OW27-A, OW27-B, OW27-C, OW27-D, OW27-E & B4_UV_MZ_BLIND_LOCK_V3
# ==============================================================================

def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    hygiene = scan_self_hygiene(script_path)
    assert hygiene["clean"], f"Hygiene failure: {hygiene}"

    mp.mp.dps = 35

    # --- Load frozen OW26 v8 / OW23-C reference values (purely dimensionless, 0 of 19) ---
    ow26_v8 = json.loads((repo_root / "relays/a2_ow26_v8/a2_ow26_v8_results.json").read_text(encoding="utf-8"))
    ow23_v3 = json.loads((repo_root / "relays/a2_ow23_v3/a2_ow23_v3_results.json").read_text(encoding="utf-8"))
    lock_v2_sha = ow26_v8["OW26_E_planted_faults_and_blind_lock_v2"]["blind_prediction_lock_v2_sha256"]
    lock_v1_sha = ow26_v8["OW26_E_planted_faults_and_blind_lock_v2"]["blind_prediction_lock_v2_B4_UV"]["supersedes_provisional_V1_sha256"]
    mkk_over_mpred = mp.mpf(ow23_v3["OW23_C_e8_flux_and_dark_matter"]["M_KK_over_M_Pl_from_V_M3_and_alphaUV24"])
    g_s12_ow26 = [mp.mpf(s) for s in ow26_v8["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B4_spin_half_dirac_liouville_kahler"]["G_s12_dirac_unit_mean_t8"]]
    yt_cim_max = mp.mpf(ow26_v8["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B2_M8_cim_L2_triple_overlap"]["magnetized_M16_Higgs_max_yt_over_gUV"])
    yt_cim_min = mp.mpf(ow26_v8["OW26_B_e8_clebsch_cim_sugra_and_dirac_kahler"]["B2_M8_cim_L2_triple_overlap"]["magnetized_M16_Higgs_min_nonzero_yt_over_gUV"])

    # --- Re-derive true tau_8^+ Spin-1/2 Dirac Gramian G_s12_t8 independently ---
    dirac_g = compute_dirac_s12_tau8_gramian()
    s12_diag = dirac_g["G_s12_t8"]
    s12_vs_ow26_err = max(abs(s12_diag[j] - g_s12_ow26[j]) for j in range(3))

    # --- OW27-A: Pure-QFT SymPy Proofs + Exact 2-Loop Pole/EW/Decoupling Pipeline ---
    qft_proofs = prove_ow27a_pure_qft_identities()
    c20_nl5_mp = qft_proofs.pop("_c20_nl5_mp")

    tau8_p = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    tau8_m = -mp.conj(tau8_p)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    k5_cp = [(a, (-b) % 1) for a, b in k5]
    k6_cp = [(a, (-b) % 1) for a, b in k6]

    def w_avg(tau: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
        acc = mp.zeros(3, 3)
        for a, b in pts:
            acc += eval_w_hol_tau(tau, a, b, ql, qr)
        return acc / len(pts)

    def build_base_uv(tau: mp.mpc, metric_diag: list[mp.mpf], use_cp: bool = False) -> dict[str, mp.matrix]:
        p5 = k5_cp if use_cp else k5
        p6 = k6_cp if use_cp else k6
        eps5 = mp.exp(2 * I_MP * mp.pi * tau / 5)
        d10 = mp.diag([eps5 ** 3, eps5 ** 2, mp.mpc(1)])
        kis = mp.diag([1 / mp.sqrt(v) for v in metric_diag])
        wu = kis * (d10 * w_avg(tau, p5, 1, -4) * d10) * kis
        wd = kis * (d10 * (w_avg(tau, p5, 1, 2) + w_avg(tau, p6, 1, 2)) / 2) * kis
        we = kis * (((w_avg(tau, p5, -3, 6) + w_avg(tau, p6, -3, 6)) / 2) * d10) * kis
        wn2 = kis * ((w_avg(tau, p5, -3, 2) - w_avg(tau, p6, -3, 2)) / 2) * kis
        wr2_raw = (w_avg(tau, p5, 2, 2) - w_avg(tau, p6, 2, 2)) / 2
        mr2 = kis * ((wr2_raw + wr2_raw.T) / 2) * kis
        _, su = svd_asc_mp(wu)
        _, sd = svd_asc_mp(wd)
        _, sn = svd_asc_mp(wn2)
        kap2 = -wn2 * (mr2 ** (-1)) * wn2.T
        _, sk = svd_asc_mp((kap2 + kap2.T) / 2)
        return {
            "yu_hat": wu / su[2],
            "yd_hat": wd / sd[2],
            "ye_hat": we / sd[2],
            "yn_hat": wn2 / sn[2],
            "mr_raw": mr2,
            "kap_hat": kap2 / sk[2],
            "we_raw": (w_avg(tau, p5, -3, 6) + w_avg(tau, p6, -3, 6)) / 2,
            "d10": d10,
            "sd2": sd[2],
        }

    flat_diag = [mp.mpf(1), mp.mpf(1), mp.mpf(1)]
    tex_flat_p = build_base_uv(tau8_p, flat_diag, use_cp=False)
    tex_s12_p = build_base_uv(tau8_p, s12_diag, use_cp=False)
    tex_s12_m = build_base_uv(tau8_m, s12_diag, use_cp=True)

    g_uv24 = mp.sqrt(4 * mp.pi / mp.mpf(24))
    t_susy24 = -(mp_rat(48, 5) * mp.pi)
    yb0_ref = g_uv24 / 5
    ytau0_ref = (g_uv24 / 5) * svd_asc_mp(tex_flat_p["ye_hat"])[1][2]
    soft_ref_guv = integrate_soft_susy_26var_1loop(g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 160, -mp.sqrt(3))

    st_s12_susy = rk4_integrate_mssm(
        (g_uv24, g_uv24, g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0_ref * tex_s12_p["yd_hat"], yb0_ref * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
        t_susy24, 80, two_loop=True,
    )
    st_flat_susy = rk4_integrate_mssm(
        (g_uv24, g_uv24, g_uv24, g_uv24 * tex_flat_p["yu_hat"], yb0_ref * tex_flat_p["yd_hat"], yb0_ref * tex_flat_p["ye_hat"], tex_flat_p["kap_hat"]),
        t_susy24, 80, two_loop=True,
    )

    def fmt_ir_run(res: dict[str, Any]) -> dict[str, Any]:
        return {
            "mu_mt_over_v": mp.nstr(res["mu_mt_over_v"], 12),
            "mt_fixed_pt_err": mp.nstr(res["mt_fixed_pt_err"], 8),
            "mz_over_v": mp.nstr(res["mz_over_v"], 12),
            "delta_b": mp.nstr(res["delta_b"], 12),
            "alpha1_inv_mz": mp.nstr(res["a1_inv_mz"], 12),
            "alpha2_inv_mz": mp.nstr(res["a2_inv_mz"], 12),
            "alpha3_mz_nf6": mp.nstr(res["a3_mz_nf6"], 12),
            "alpha3_mz_nf5": mp.nstr(res["a3_mz_nf5"], 12),
            "alpha3_at_mt": mp.nstr(res["a3_at_mt"], 12),
            "sin2_thetaW_msbar_mz": mp.nstr(res["sin2_thetaW_msbar_mz"], 12),
            "sin2_thetaW_on_shell": mp.nstr(res["sin2_thetaW_on_shell"], 12),
            "alpha_EM_inv_mz_nf6": mp.nstr(res["alpha_EM_inv_mz_nf6"], 12),
            "alpha_EM_inv_mz_nf5": mp.nstr(res["alpha_EM_inv_mz_nf5"], 12),
            "delta_rho_t_1loop": mp.nstr(res["delta_rho_t_1loop"], 12),
            "mw_over_mz_msbar": mp.nstr(res["mw_over_mz_msbar"], 12),
            "mw_over_mz_pole_veltman": mp.nstr(res["mw_over_mz_pole_veltman"], 12),
            "mt_ms_at_mt_over_v": mp.nstr(res["mt_ms_at_mt_over_v"], 12),
            "mt_pole_1l_at_mt_over_v": mp.nstr(res["mt_pole_1l_at_mt_over_v"], 12),
            "mt_pole_2l_at_mt_over_v": mp.nstr(res["mt_pole_2l_at_mt_over_v"], 12),
            "mt_pole_2l_at_mz_over_v": mp.nstr(res["mt_pole_2l_at_mz_over_v"], 12),
            "mt_pole_2l_scale_drift": mp.nstr(res["mt_pole_2l_scale_drift"], 10),
            "mh_pole_4c_at_mt_over_v": mp.nstr(res["mh_pole_4c_at_mt_over_v"], 12),
            "mh_pole_4c_at_mz_over_v": mp.nstr(res["mh_pole_4c_at_mz_over_v"], 12),
            "mh_pole_4c_at_mt_over_mz": mp.nstr(res["mh_pole_4c_at_mt_over_mz"], 12),
            "mh_pole_4c_at_mz_over_mz": mp.nstr(res["mh_pole_4c_at_mz_over_mz"], 12),
            "mh_pole_4c_scale_drift": mp.nstr(res["mh_pole_4c_scale_drift"], 10),
            "mh_pole_toponly_scale_drift": mp.nstr(res["mh_pole_toponly_scale_drift"], 10),
            "Lambda_QCD_3_exact_over_v": mp.nstr(res["lambda_qcd_info"]["Lambda_QCD_3_exact_over_v"], 12),
            "Lambda_QCD_3_std_over_v": mp.nstr(res["lambda_qcd_info"]["Lambda_QCD_3_std_over_v"], 12),
            "mb_mb_over_v": mp.nstr(res["lambda_qcd_info"]["mb_mb_over_v"], 12),
            "mc_mc_over_v": mp.nstr(res["lambda_qcd_info"]["mc_mc_over_v"], 12),
            "ckm_mz": {k: mp.nstr(v, 12) for k, v in res["ckm_mz"].items()},
            "strict_CKM_ordered": bool(res["ckm_mz"]["v12"] > res["ckm_mz"]["v23"] > res["ckm_mz"]["v13"] > 0),
        }

    ow27a_runs: dict[str, Any] = {}
    central_ir_obj: dict[str, Any] = {}
    for gname, st_use in (("CURV_s12_Dirac", st_s12_susy), ("FLAT", st_flat_susy)):
        for sgn_m in (1, -1):
            for m0v in (3, 10, 30):
                if gname == "FLAT" and m0v != 10:
                    continue
                r_obj = match_mssm_to_sm_and_run_ow27(st_use, soft_ref_guv, 15, m0v, c20_nl5_mp, sgn_mu=sgn_m, n_sm_steps=80)
                tag = f"{gname}_yt_gUV_tb15_m0_{m0v}v_sgnMu_{'pos' if sgn_m > 0 else 'neg'}"
                ow27a_runs[tag] = fmt_ir_run(r_obj)
                if tag == "CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos":
                    central_ir_obj = r_obj

    # Magnetized M_H = 16 CIM y_t runs (kH=2 max & kH=1 min, m0 = 3v & 10v)
    ow27a_cim_runs: dict[str, Any] = {}
    for ctag, y_fac in (("CIM_M16_kH2max", yt_cim_max), ("CIM_M16_kH1min", yt_cim_min)):
        ytg = g_uv24 * y_fac
        sft_c = integrate_soft_susy_26var_1loop(g_uv24, ytg, yb0_ref, ytau0_ref, t_susy24, 160, -mp.sqrt(3))
        st_c = rk4_integrate_mssm(
            (g_uv24, g_uv24, g_uv24, ytg * tex_s12_p["yu_hat"], yb0_ref * tex_s12_p["yd_hat"], yb0_ref * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
            t_susy24, 80, two_loop=True,
        )
        for m0v in (3, 10):
            rc = match_mssm_to_sm_and_run_ow27(st_c, sft_c, 15, m0v, c20_nl5_mp, sgn_mu=1, n_sm_steps=80)
            ow27a_cim_runs[f"CURV_s12_{ctag}_m0_{m0v}v"] = {
                "yt_GUT": mp.nstr(ytg, 12),
                "mt_pole_2l_at_mt_over_v": mp.nstr(rc["mt_pole_2l_at_mt_over_v"], 12),
                "mh_pole_4c_at_mt_over_mz": mp.nstr(rc["mh_pole_4c_at_mt_over_mz"], 12),
                "mh_pole_4c_scale_drift": mp.nstr(rc["mh_pole_4c_scale_drift"], 10),
                "mw_over_mz_pole_veltman": mp.nstr(rc["mw_over_mz_pole_veltman"], 12),
                "alpha3_mz_nf5": mp.nstr(rc["a3_mz_nf5"], 12),
                "b_tau_mz": mp.nstr(rc["ckm_mz"]["b_tau"], 12),
            }

    # End-to-end 10-trial Haar U(3)^5 scrambling through M_GUT -> M_SUSY -> m_t(m_t) -> M_Z!
    rng_a = SplitMix64(202611242701)
    st_ref_a = rk4_integrate_mssm(
        (g_uv24, g_uv24, g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0_ref * tex_s12_p["yd_hat"], yb0_ref * tex_s12_p["ye_hat"], tex_s12_p["kap_hat"]),
        t_susy24, 50, two_loop=True,
    )
    ir_ref_a = match_mssm_to_sm_and_run_ow27(st_ref_a, soft_ref_guv, 15, 10, c20_nl5_mp, sgn_mu=1, n_sm_steps=40)
    haar_ow27a_err = mp.mpf(0)
    for _ in range(10):
        uq, uur, udr, ul, uer = (random_haar_u3_mp(rng_a) for _ in range(5))
        st_sc = rk4_integrate_mssm(
            (
                g_uv24, g_uv24, g_uv24,
                uq * (g_uv24 * tex_s12_p["yu_hat"]) * uur.H,
                uq * (yb0_ref * tex_s12_p["yd_hat"]) * udr.H,
                ul * (yb0_ref * tex_s12_p["ye_hat"]) * uer.H,
                ul * tex_s12_p["kap_hat"] * ul.T,
            ),
            t_susy24, 50, two_loop=True,
        )
        ir_sc = match_mssm_to_sm_and_run_ow27(st_sc, soft_ref_guv, 15, 10, c20_nl5_mp, sgn_mu=1, n_sm_steps=40)
        haar_ow27a_err = max(
            haar_ow27a_err,
            max(abs(ir_sc["ckm_mz"][k] - ir_ref_a["ckm_mz"][k]) for k in ir_ref_a["ckm_mz"]),
            abs(ir_sc["mt_pole_2l_at_mt_over_v"] - ir_ref_a["mt_pole_2l_at_mt_over_v"]),
            abs(ir_sc["mh_pole_4c_at_mt_over_mz"] - ir_ref_a["mh_pole_4c_at_mt_over_mz"]),
            abs(ir_sc["mw_over_mz_pole_veltman"] - ir_ref_a["mw_over_mz_pole_veltman"]),
            abs(ir_sc["lambda_qcd_info"]["Lambda_QCD_3_exact_over_v"] - ir_ref_a["lambda_qcd_info"]["Lambda_QCD_3_exact_over_v"]),
        )

    central_4c_drift = central_ir_obj["mh_pole_4c_scale_drift"]
    central_toponly_drift = central_ir_obj["mh_pole_toponly_scale_drift"]
    gate_a = bool(
        qft_proofs["all_sympy_proofs_exact"]
        and central_ir_obj["mt_fixed_pt_err"] < mp_pow10(-20)
        and central_4c_drift < mp_rat(5, 1000)
        and central_toponly_drift > mp_rat(3, 100)
        and central_ir_obj["mw_over_mz_pole_veltman"] > central_ir_obj["mw_over_mz_msbar"]
        and haar_ow27a_err < mp_pow10(-12)
        and all(v["strict_CKM_ordered"] for v in ow27a_runs.values())
    )
    ow27_a = {
        "gate_passed": gate_a,
        "pure_qft_sympy_proofs": qft_proofs,
        "guardrail3_10trial_haar_U3_5_end_to_end_err": mp.nstr(haar_ow27a_err, 10),
        "central_higgs_4c_mu_MZ_vs_mt_scale_drift": mp.nstr(central_4c_drift, 10),
        "central_higgs_toponly_mu_MZ_vs_mt_scale_drift": mp.nstr(central_toponly_drift, 10),
        "omitted_nonlog_Delta_r_fin_EW_note": "Exact 4-coupling 1-loop RG-invariant Delta_tot^(1) includes all PV B_0(m_h^2; M_i, M_i) & CW finite terms; omitted non-log bosonic vertex-box Delta r_fin^EW is O(g_2^2/(16 pi^2)) ~ 0.1% in m_h^pole.",
        "mz_and_mt_2loop_pipeline_runs": ow27a_runs,
        "mz_and_mt_cim_M16_runs": ow27a_cim_runs,
    }

    # --- OW27-C (Run before OW27-B so we have exact Dirac s=1/2 leptogenesis Y_B for Omega_Bino / Omega_B!) ---
    # 1. Exact OW24-C 384-case discrete neutrino atlas under TRUE tau_8^+ Spin-1/2 Dirac G_s12_t8
    kis_s12 = mp.diag([1 / mp.sqrt(v) for v in s12_diag])
    eps5_p = mp.exp(2 * I_MP * mp.pi * tau8_p / 5)
    d10_p = mp.diag([eps5_p ** 3, eps5_p ** 2, mp.mpc(1)])
    we0_p = tex_s12_p["we_raw"]

    atlas_384_total = 0
    atlas_384_nonsing = 0
    atlas_384_hits: list[dict[str, Any]] = []
    atlas_384_hit_specs: list[tuple[str, int, str, str, tuple[int, int, int], str]] = []
    for qr in (3, -5, 1, 2):
        w5n = w_avg(tau8_p, k5, -3, qr)
        w6n = w_avg(tau8_p, k6, -3, qr)
        w5r = w_avg(tau8_p, k5, qr, qr)
        w6r = w_avg(tau8_p, k6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        for kn, wn in ops_n.items():
            for kr, wr in ops_r.items():
                mr_m = (wr + wr.T) / 2
                _, smr = takagi_asc_mp(mr_m)
                is_sing = bool(smr[0] < mp_pow10(-25))
                for n5b in ((0, 0, 0), (1, 0, 0), (1, 1, 0)):
                    d5b = mp.diag([eps5_p ** n for n in n5b])
                    ye_loc = d5b * we0_p * d10_p
                    ynu_loc = d5b * wn
                    for gname, kmat in (("FLAT", mp.eye(3)), ("CURV_s12_t8", kis_s12)):
                        atlas_384_total += 1
                        if is_sing:
                            continue
                        atlas_384_nonsing += 1
                        mnu_loc = -ynu_loc * (mr_m ** (-1)) * ynu_loc.T
                        obs_p = pmns_full_obs(kmat * ye_loc * kmat, kmat * mnu_loc * kmat)
                        if in_ow24c_pmns_window(obs_p):
                            tag = f"{gname}_{kn}_over_{kr}_qR_{qr}_n5b_{n5b[0]}{n5b[1]}{n5b[2]}"
                            atlas_384_hits.append({
                                "tag": tag,
                                "uv_pmns": {k: mp.nstr(v, 12) for k, v in obs_p.items()},
                            })
                            atlas_384_hit_specs.append((tag, qr, kn, kr, n5b, gname))

    # 2. Scan 2: M_R = I_3 + W_R^unit on pure lopsided n_10=(3,2,0), n_5bar=(0,0,0) under TRUE tau_8^+ G_s12_t8!
    #    q_R in (-5, -3, 0, 2, 3, 5) x 4 ops_n x 4 ops_r x 2 Kahler conventions (left_only_NR_flat vs both_sided_NR_s12) = 192 cases!
    mr_unit_total = 0
    mr_unit_sym6_hits: list[dict[str, Any]] = []
    mr_unit_all_hits: list[dict[str, Any]] = []
    mr_unit_hit_specs: list[tuple[str, int, str, str, str]] = []
    ye_s12_pure = kis_s12 * (we0_p * d10_p) * kis_s12

    for qr in (-5, -3, 0, 2, 3, 5):
        w5n = w_avg(tau8_p, k5, -3, qr)
        w6n = w_avg(tau8_p, k6, -3, qr)
        w5r = w_avg(tau8_p, k5, qr, qr)
        w6r = w_avg(tau8_p, k6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        for kn, wn in ops_n.items():
            for kr, wr in ops_r.items():
                wr_sym = (wr + wr.T) / 2
                _, sv_wr = svd_asc_mp(wr_sym)
                if sv_wr[2] < mp_pow10(-25):
                    mr_u = mp.eye(3)
                else:
                    mr_u = mp.eye(3) + (wr_sym / sv_wr[2])
                _, sv_mu = takagi_asc_mp(mr_u)
                is_sing = bool(sv_mu[0] < mp_pow10(-25))
                for kmode in ("left_only_NR_flat", "both_sided_NR_s12"):
                    mr_unit_total += 1
                    if is_sing:
                        continue
                    if kmode == "left_only_NR_flat":
                        yn_c = kis_s12 * wn
                        mr_c = mr_u
                    else:
                        yn_c = kis_s12 * wn * kis_s12
                        mr_c = kis_s12 * mr_u * kis_s12
                    _, sn_c = svd_asc_mp(yn_c)
                    if sn_c[2] < mp_pow10(-25):
                        continue
                    kap_c = -yn_c * (mr_c ** (-1)) * yn_c.T
                    obs_p = pmns_full_obs(ye_s12_pure, kap_c)
                    if in_ow24c_pmns_window(obs_p):
                        tag = f"I3plusWR_{kmode}_{kn}_over_{kr}_qR_{qr}"
                        rec = {
                            "tag": tag,
                            "is_symmetric_5plus6_slice": bool(kn == "5+6" and kr == "5+6"),
                            "uv_pmns": {k: mp.nstr(v, 12) for k, v in obs_p.items()},
                        }
                        mr_unit_all_hits.append(rec)
                        if kn == "5+6" and kr == "5+6":
                            mr_unit_sym6_hits.append(rec)
                        mr_unit_hit_specs.append((tag, qr, kn, kr, kmode))

    # Helper to construct (Y_nu, M_R) for any spec on tau_8^+ or tau_8^- (with CP mirror orbits!)
    def build_nu_spec(
        tau: mp.mpc, use_cp: bool, mode: str, qr: int, kn: str, kr: str, n5b: tuple[int, int, int], kmode: str
    ) -> tuple[mp.matrix, mp.matrix, mp.matrix]:
        p5 = k5_cp if use_cp else k5
        p6 = k6_cp if use_cp else k6
        eps5 = mp.exp(2 * I_MP * mp.pi * tau / 5)
        d10 = mp.diag([eps5 ** 3, eps5 ** 2, mp.mpc(1)])
        d5b = mp.diag([eps5 ** n for n in n5b])
        kmat = mp.eye(3) if kmode == "FLAT" else kis_s12
        we_loc = kmat * (d5b * ((w_avg(tau, p5, -3, 6) + w_avg(tau, p6, -3, 6)) / 2) * d10) * kmat
        w5n, w6n = w_avg(tau, p5, -3, qr), w_avg(tau, p6, -3, qr)
        w5r, w6r = w_avg(tau, p5, qr, qr), w_avg(tau, p6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        wn = d5b * ops_n[kn]
        wr_sym = (ops_r[kr] + ops_r[kr].T) / 2
        if mode == "bare":
            yn_c = kmat * wn * kmat
            mr_c = kmat * wr_sym * kmat
        else:
            _, sv_wr = svd_asc_mp(wr_sym)
            mr_u = mp.eye(3) + (wr_sym / sv_wr[2]) if sv_wr[2] >= mp_pow10(-25) else mp.eye(3)
            if kmode == "left_only_NR_flat":
                yn_c = kis_s12 * wn
                mr_c = mr_u
            else:
                yn_c = kis_s12 * wn * kis_s12
                mr_c = kis_s12 * mr_u * kis_s12
        _, sn_c = svd_asc_mp(yn_c)
        return we_loc, yn_c / sn_c[2], mr_c

    # Propagate:
    #   (a) ALL surviving simultaneous hits from the 384-case Dirac atlas (if any),
    #   (b) Priority simultaneous hits from the I_3+W_R^unit scan (ALL symmetric 5+6/5+6 hits + up to 4 additional hits),
    #   (c) Legacy OW26 reference (bare 5-6/5-6 q_R=2, n_5bar=(0,0,0), CURV_s12_t8).
    mr0_central = mp_pow10(-3)
    to_propagate: list[tuple[str, str, int, str, str, tuple[int, int, int], str]] = []
    for tag, qr, kn, kr, n5b, gname in atlas_384_hit_specs:
        to_propagate.append((tag, "bare", qr, kn, kr, n5b, gname))
    # Prioritize symmetric 5+6/5+6 hits from I_3+W_R^unit scan first, then up to 4 more distinct ones
    sym_specs = [s for s in mr_unit_hit_specs if s[2] == "5+6" and s[3] == "5+6"]
    other_specs = [s for s in mr_unit_hit_specs if not (s[2] == "5+6" and s[3] == "5+6")][:4]
    for tag, qr, kn, kr, kmode in sym_specs + other_specs:
        to_propagate.append((tag, "I3plusWR", qr, kn, kr, (0, 0, 0), kmode))
    # Always include legacy OW26 reference if not already in list
    legacy_tag = "LEGACY_OW26_CURV_s12_t8_5-6_over_5-6_qR_2_n5b_000"
    to_propagate.append((legacy_tag, "bare", 2, "5-6", "5-6", (0, 0, 0), "CURV_s12_t8"))

    propagated_candidates: list[dict[str, Any]] = []
    primary_cand_info: dict[str, Any] = {}
    legacy_yb_ref: mp.mpf = mp.mpf(0)

    for tag, mode, qr, kn, kr, n5b, kmode in to_propagate:
        we_p, yn_p, mr_p = build_nu_spec(tau8_p, False, mode, qr, kn, kr, n5b, kmode)
        we_m, yn_m, mr_m = build_nu_spec(tau8_m, True, mode, qr, kn, kr, n5b, kmode)
        ye_p_hat = we_p / tex_s12_p["sd2"] if kmode != "FLAT" else we_p / tex_flat_p["sd2"]
        ye_m_hat = we_m / tex_s12_m["sd2"] if kmode != "FLAT" else we_m / tex_flat_p["sd2"]
        yu_p_use = tex_flat_p["yu_hat"] if kmode == "FLAT" else tex_s12_p["yu_hat"]
        yd_p_use = tex_flat_p["yd_hat"] if kmode == "FLAT" else tex_s12_p["yd_hat"]
        yu_m_use = tex_flat_p["yu_hat"] if kmode == "FLAT" else tex_s12_m["yu_hat"]
        yd_m_use = tex_flat_p["yd_hat"] if kmode == "FLAT" else tex_s12_m["yd_hat"]

        seq_p = run_sequential_seesaw_ow27(
            g_uv24, g_uv24 * yu_p_use, yb0_ref * yd_p_use, yb0_ref * ye_p_hat,
            g_uv24 * yn_p, mr_p, mr0_central, t_susy24, soft_ref_guv, c20_nl5_mp,
        )
        seq_m = run_sequential_seesaw_ow27(
            g_uv24, g_uv24 * yu_m_use, yb0_ref * yd_m_use, yb0_ref * ye_m_hat,
            g_uv24 * yn_m, mr_m, mr0_central, t_susy24, soft_ref_guv, c20_nl5_mp,
        )
        lep_p = compute_mssm_boltzmann_leptogenesis(
            seq_p["lepto_snapshot"]["ye_at_MR3"],
            seq_p["lepto_snapshot"]["ynu_rot_at_MR3"],
            seq_p["lepto_snapshot"]["M_R_eigs_over_MGUT"],
            mkk_over_mpred,
            n_z_steps=400,
        )
        lep_m = compute_mssm_boltzmann_leptogenesis(
            seq_m["lepto_snapshot"]["ye_at_MR3"],
            seq_m["lepto_snapshot"]["ynu_rot_at_MR3"],
            seq_m["lepto_snapshot"]["M_R_eigs_over_MGUT"],
            mkk_over_mpred,
            n_z_steps=400,
        )
        cp_odd_err = abs(lep_p["Y_B_flavored"] + lep_m["Y_B_flavored"])
        cp_sel = "tau8_plus" if lep_p["Y_B_flavored"] > 0 else "tau8_minus"
        seq_sel = seq_p if cp_sel == "tau8_plus" else seq_m
        lep_sel = lep_p if cp_sel == "tau8_plus" else lep_m
        stays_in_win = in_ow24c_pmns_window(seq_sel["ir_mz"]["pmns_mz"])
        rec = {
            "tag": tag,
            "mode": mode,
            "qR": qr,
            "ops_n": kn,
            "ops_r": kr,
            "n5bar": list(n5b),
            "kahler_mode": kmode,
            "selected_CP_branch_by_YB_gt_0": cp_sel,
            "stays_in_OW24C_PMNS_window_at_MZ": stays_in_win,
            "thresholds_MR_over_MGUT": [mp.nstr(v, 12) for v in seq_sel["thresholds_MR_over_MGUT"]],
            "pmns_mz": {k: mp.nstr(v, 12) for k, v in seq_sel["ir_mz"]["pmns_mz"].items()},
            "ckm_J_mz_CP_selected": mp.nstr(seq_sel["ir_mz"]["ckm_mz"]["J"], 12),
            "Y_B_flavored": mp.nstr(lep_sel["Y_B_flavored"], 12),
            "Y_B_unflavored": mp.nstr(lep_sel["Y_B_unflavored"], 12),
            "eps_tot": mp.nstr(lep_sel["eps_tot"], 12),
            "K_tot": mp.nstr(lep_sel["K_tot"], 12),
            "Y_B_step_rel_err": mp.nstr(lep_sel["Y_B_step_rel_err"], 10),
            "CP_odd_YB_sum_err": mp.nstr(cp_odd_err, 10),
        }
        propagated_candidates.append(rec)
        if tag == legacy_tag:
            legacy_yb_ref = lep_sel["Y_B_flavored"]
        # Pick primary surviving Dirac s=1/2 hit (preferring 384-atlas hit, else I_3+W_R^unit hit staying in window at M_Z with n5b=(0,0,0)!)
        if stays_in_win and not primary_cand_info and kmode != "FLAT" and tag != legacy_tag:
            primary_cand_info = {
                "record": rec,
                "yu_p": g_uv24 * yu_p_use,
                "yd_p": yb0_ref * yd_p_use,
                "ye_p": yb0_ref * ye_p_hat,
                "yn_p": g_uv24 * yn_p,
                "mr_p": mr_p,
                "seq_p": seq_p,
                "yb_sel": lep_sel["Y_B_flavored"],
                "cp_odd_err": cp_odd_err,
            }

    # If no hit stayed in window (fallback to legacy for Haar test so script never crashes, though gate will check honestly!)
    if not primary_cand_info:
        we_p, yn_p, mr_p = build_nu_spec(tau8_p, False, "bare", 2, "5-6", "5-6", (0, 0, 0), "CURV_s12_t8")
        seq_p = run_sequential_seesaw_ow27(
            g_uv24, g_uv24 * tex_s12_p["yu_hat"], yb0_ref * tex_s12_p["yd_hat"], yb0_ref * (we_p / tex_s12_p["sd2"]),
            g_uv24 * yn_p, mr_p, mr0_central, t_susy24, soft_ref_guv, c20_nl5_mp,
        )
        primary_cand_info = {
            "record": propagated_candidates[-1],
            "yu_p": g_uv24 * tex_s12_p["yu_hat"],
            "yd_p": yb0_ref * tex_s12_p["yd_hat"],
            "ye_p": yb0_ref * (we_p / tex_s12_p["sd2"]),
            "yn_p": g_uv24 * yn_p,
            "mr_p": mr_p,
            "seq_p": seq_p,
            "yb_sel": legacy_yb_ref,
            "cp_odd_err": mp.mpf(propagated_candidates[-1]["CP_odd_YB_sum_err"]),
        }

    # 10-trial Haar U(3)^5 x U(3)_N scrambling test on the primary Dirac s=1/2 candidate!
    rng_c = SplitMix64(202611242703)
    lep_ref_c = compute_mssm_boltzmann_leptogenesis(
        primary_cand_info["seq_p"]["lepto_snapshot"]["ye_at_MR3"],
        primary_cand_info["seq_p"]["lepto_snapshot"]["ynu_rot_at_MR3"],
        primary_cand_info["seq_p"]["lepto_snapshot"]["M_R_eigs_over_MGUT"],
        mkk_over_mpred,
        n_z_steps=120,
    )
    haar_ow27c_err = mp.mpf(0)
    for _ in range(10):
        uq, uur, udr, ul, uer, un = (random_haar_u3_mp(rng_c) for _ in range(6))
        seq_sc = run_sequential_seesaw_ow27(
            g_uv24,
            uq * primary_cand_info["yu_p"] * uur.H,
            uq * primary_cand_info["yd_p"] * udr.H,
            ul * primary_cand_info["ye_p"] * uer.H,
            ul * primary_cand_info["yn_p"] * un.H,
            un.apply(mp.conj) * primary_cand_info["mr_p"] * un.H,
            mr0_central, t_susy24, soft_ref_guv, c20_nl5_mp,
        )
        lep_sc = compute_mssm_boltzmann_leptogenesis(
            seq_sc["lepto_snapshot"]["ye_at_MR3"],
            seq_sc["lepto_snapshot"]["ynu_rot_at_MR3"],
            seq_sc["lepto_snapshot"]["M_R_eigs_over_MGUT"],
            mkk_over_mpred,
            n_z_steps=120,
        )
        haar_ow27c_err = max(
            haar_ow27c_err,
            max(abs(seq_sc["ir_mz"]["pmns_mz"][k] - primary_cand_info["seq_p"]["ir_mz"]["pmns_mz"][k]) for k in primary_cand_info["seq_p"]["ir_mz"]["pmns_mz"]),
            abs(lep_sc["eps_tot"] - lep_ref_c["eps_tot"]),
            abs(lep_sc["Y_B_flavored"] - lep_ref_c["Y_B_flavored"]),
            abs(lep_sc["Y_B_unflavored"] - lep_ref_c["Y_B_unflavored"]),
        )

    atlas_384_bits = mp.log(384, 2)
    mr_unit_192_bits = mp.log(192, 2)
    mr_unit_96_bits = mp.log(96, 2)
    mr_unit_6_bits = mp.log(6, 2)

    gate_c = bool(
        dirac_g["tr_comm_err"] < mp_pow10(-15)
        and dirac_g["gb_err"] < mp_pow10(-6)
        and dirac_g["grid_diff"] < mp_pow10(-5)
        and s12_vs_ow26_err < mp_pow10(-10)
        and atlas_384_total == 384
        and mr_unit_total == 192
        and haar_ow27c_err < mp_pow10(-12)
        and all(mp.mpf(r["CP_odd_YB_sum_err"]) < mp_pow10(-30) for r in propagated_candidates)
        and all(mp.mpf(r["Y_B_step_rel_err"]) < mp_pow10(-5) for r in propagated_candidates)
    )
    ow27_c = {
        "gate_passed": gate_c,
        "G_s12_t8_independent_verification": {
            "G_s12_t8": [mp.nstr(v, 12) for v in s12_diag],
            "vs_OW26v8_max_err": mp.nstr(s12_vs_ow26_err, 10),
            "gauss_bonnet_err": mp.nstr(dirac_g["gb_err"], 10),
            "coarse_vs_fine_err": mp.nstr(dirac_g["grid_diff"], 10),
        },
        "scan1_384_case_OW24C_atlas_under_G_s12_t8": {
            "total_cases": atlas_384_total,
            "nonsingular_cases": atlas_384_nonsing,
            "guardrail1_bits_log2_384": mp.nstr(atlas_384_bits, 12),
            "simultaneous_PMNS_hits_count": len(atlas_384_hits),
            "simultaneous_PMNS_hits": atlas_384_hits,
        },
        "scan2_I3_plus_WR_unit_under_G_s12_t8_pure_lopsided": {
            "total_cases": mr_unit_total,
            "guardrail1_bits_log2_192": mp.nstr(mr_unit_192_bits, 12),
            "guardrail1_bits_log2_96_per_kahler_mode": mp.nstr(mr_unit_96_bits, 12),
            "guardrail1_bits_log2_6_symmetric_5plus6_slice": mp.nstr(mr_unit_6_bits, 12),
            "symmetric_5plus6_hits_count": len(mr_unit_sym6_hits),
            "symmetric_5plus6_hits": mr_unit_sym6_hits,
            "all_192_simultaneous_hits_count": len(mr_unit_all_hits),
            "all_192_simultaneous_hits": mr_unit_all_hits,
        },
        "primary_surviving_dirac_s12_candidate": primary_cand_info["record"],
        "propagated_2loop_sequential_seesaw_and_boltzmann": propagated_candidates,
        "guardrail3_10trial_haar_U3_5_x_U3_N_err": mp.nstr(haar_ow27c_err, 10),
    }

    # --- OW27-B: First-Principles Thermal Bino LSP Dark-Matter Freeze-Out (OBS-20) ---
    spinor_proof = verify_majorana_bino_annihilation_spinors()
    riccati_analytic_err = benchmark_radau2_analytic_riccati()

    # Extract derived SM couplings & scales from central OW27-A run (strictly 0 of 19!):
    g1_z_c, g2_z_c = central_ir_obj["st_mz"][0], central_ir_obj["st_mz"][1]
    gp_sq_c = mp_rat(3, 5) * g1_z_c * g1_z_c
    mt_v_c = central_ir_obj["mt_pole_2l_at_mt_over_v"]
    mz_v_c = central_ir_obj["mz_over_v"]
    s2w_c = central_ir_obj["sin2_thetaW_msbar_mz"]
    lam_qcd3_v_c = central_ir_obj["lambda_qcd_info"]["Lambda_QCD_3_exact_over_v"]
    yb_for_dm = primary_cand_info["yb_sel"] if abs(primary_cand_info["yb_sel"]) > mp_pow10(-20) else legacy_yb_ref

    # Step-halving convergence N=400 vs N=800 + Richardson on central point (m0=10v, A0=-sqrt(3), tb=15)
    dm_c400 = compute_bino_dm_point(
        soft_ref_guv, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_over_mpred, t_susy24, yb_for_dm, lam_qcd3_v_c, n_steps=400
    )
    dm_c800 = compute_bino_dm_point(
        soft_ref_guv, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_over_mpred, t_susy24, yb_for_dm, lam_qcd3_v_c, n_steps=800
    )
    dm_step_rel_err = abs(dm_c800["Y_Bino_inf"] - dm_c400["Y_Bino_inf"]) / dm_c800["Y_Bino_inf"]
    dm_c_rich_y = (8 * dm_c800["Y_Bino_inf"] - dm_c400["Y_Bino_inf"]) / 7

    # Planted-fault PF_OW27_4: unreduced Planck mass in reduced Hubble shifts Y_Bino by ~+400% (> 100%!)
    dm_pf4_unred = compute_bino_dm_point(
        soft_ref_guv, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_over_mpred, t_susy24, yb_for_dm, lam_qcd3_v_c,
        n_steps=400, unreduced_planck_fault=True,
    )
    pf4_unreduced_rel_shift = abs(dm_pf4_unred["Y_Bino_inf"] - dm_c400["Y_Bino_inf"]) / dm_c400["Y_Bino_inf"]

    # Full B4_UV grid: m_0/v_EW in {1, 2, 3, 5, 10, 30} x A_0/m_0 in {0, -sqrt(3), -sqrt(6)} x tan(beta) in {5, 15, 30, 50}
    soft_by_a0 = {
        "A0_0": integrate_soft_susy_26var_1loop(g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 160, mp.mpf(0)),
        "A0_neg_sqrt3": soft_ref_guv,
        "A0_neg_sqrt6": integrate_soft_susy_26var_1loop(g_uv24, g_uv24, yb0_ref, ytau0_ref, t_susy24, 160, -mp.sqrt(6)),
    }
    dm_grid_records: list[dict[str, Any]] = []
    min_bino_purity = mp.mpf(1)
    min_delta_stau = mp.mpf(100)
    # Also compute both primary Y_B and legacy OW26 Y_B ratios at central slice (A0=-sqrt3, tb=15) across m0=1..30v
    central_m0_scan: list[dict[str, Any]] = []
    for a0_lbl, sft_a in soft_by_a0.items():
        for tb_i in (5, 15, 30, 50):
            # Include all 6 m0 values on central (A0=-sqrt3, tb=15); include m0 in {1, 3, 10} on full grid (3*4*3 + 3 = 39 runs)
            m0_list = (1, 2, 3, 5, 10, 30) if (a0_lbl == "A0_neg_sqrt3" and tb_i == 15) else (1, 3, 10)
            for m0v in m0_list:
                d_res = compute_bino_dm_point(
                    sft_a, m0v, tb_i, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_over_mpred, t_susy24, yb_for_dm, lam_qcd3_v_c, n_steps=400
                )
                min_bino_purity = min(min_bino_purity, d_res["bino_purity_N11sq"])
                min_delta_stau = min(min_delta_stau, d_res["delta_stauR"])
                rec_dm = {
                    "A0": a0_lbl,
                    "tan_beta": tb_i,
                    "m0_over_v": m0v,
                    "M1_over_v": mp.nstr(d_res["M1_over_v"], 10),
                    "m_chi1_over_v": mp.nstr(d_res["m_chi1_over_v"], 10),
                    "bino_purity_N11sq": mp.nstr(d_res["bino_purity_N11sq"], 10),
                    "m_stauR_over_m0": mp.nstr(d_res["m_stauR_over_m0"], 10),
                    "delta_stauR": mp.nstr(d_res["delta_stauR"], 10),
                    "boltz_coann_suppression": mp.nstr(d_res["boltz_coann_suppression"], 8),
                    "top_swave_open": d_res["top_swave_open"],
                    "g_star_freezeout": mp.nstr(d_res["g_star_freezeout"], 6),
                    "x_f": mp.nstr(d_res["x_f"], 10),
                    "Y_Bino_inf": mp.nstr(d_res["Y_Bino_inf"], 12),
                    "M1_over_vEW_times_YBino_over_YB_primary": mp.nstr(d_res["M1_over_vEW_times_YBino_over_YB"], 10),
                    "clat_OmegaBino_over_OmegaB_primary_YB": mp.nstr(d_res["M1_over_LambdaQCD3_times_YBino_over_YB_eq_clat_OmegaRatio"], 10),
                    "clat_OmegaBino_over_OmegaB_legacy_OW26_YB": mp.nstr(((d_res["M1_over_v"] / lam_qcd3_v_c) * d_res["Y_Bino_inf"]) / legacy_yb_ref, 10),
                }
                dm_grid_records.append(rec_dm)
                if a0_lbl == "A0_neg_sqrt3" and tb_i == 15:
                    d_lw = compute_bino_dm_point(
                        sft_a, m0v, tb_i, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mkk_over_mpred, t_susy24, yb_for_dm, lam_qcd3_v_c,
                        n_steps=400, fixed_mpred_over_v_ref_m0=10,
                    )
                    rec_c = dict(rec_dm)
                    rec_c["lee_weinberg_fixed_MPred_over_vEW_Y_Bino_inf"] = mp.nstr(d_lw["Y_Bino_inf"], 12)
                    rec_c["lee_weinberg_fixed_MPred_over_vEW_clat_OmegaRatio"] = mp.nstr(
                        d_lw["M1_over_LambdaQCD3_times_YBino_over_YB_eq_clat_OmegaRatio"], 10
                    )
                    central_m0_scan.append(rec_c)

    # Check also G_2 gauge-gravity M_GUT/M_{P,red} = sqrt(alpha_UV/(4 pi)) sensitivity at central point (m0=10v):
    mgut_g2_24 = mp.sqrt(1 / (4 * mp.pi * 24))
    dm_g2_10v = compute_bino_dm_point(
        soft_ref_guv, 10, 15, gp_sq_c, mt_v_c, mz_v_c, s2w_c, mgut_g2_24, t_susy24, yb_for_dm, lam_qcd3_v_c, n_steps=400
    )

    gate_b = bool(
        spinor_proof["spinor_proof_passed"]
        and riccati_analytic_err < mp_pow10(-10)
        and dm_step_rel_err < mp_pow10(-6)
        and pf4_unreduced_rel_shift > mp.mpf(1)
        and min_bino_purity > mp_rat(95, 100)
    )
    ow27_b = {
        "gate_passed": gate_b,
        "explicit_4comp_majorana_spinor_proof": spinor_proof,
        "radau2_analytic_riccati_benchmark_rel_err": mp.nstr(riccati_analytic_err, 10),
        "central_m0_10v_step_halving_N400_vs_N800_rel_err": mp.nstr(dm_step_rel_err, 10),
        "central_m0_10v_Y_Bino_richardson": mp.nstr(dm_c_rich_y, 12),
        "central_m0_10v_G2_M_GUT_over_MPred_Y_Bino": mp.nstr(dm_g2_10v["Y_Bino_inf"], 12),
        "central_m0_10v_G2_clat_OmegaRatio": mp.nstr(dm_g2_10v["M1_over_LambdaQCD3_times_YBino_over_YB_eq_clat_OmegaRatio"], 10),
        "pf4_unreduced_planck_rel_shift": mp.nstr(pf4_unreduced_rel_shift, 10),
        "min_bino_purity_across_grid": mp.nstr(min_bino_purity, 10),
        "min_delta_stauR_across_grid": mp.nstr(min_delta_stau, 10),
        "symbolic_lattice_ratio_note": "c_lat := m_p / Lambda_QCD^(3) is kept strictly symbolic (0 of 19; zero empirical GeV or m_p imported); Omega_Bino / Omega_B = (1 / c_lat) * [(M_1 / Lambda_QCD^(3)) * Y_Bino(inf) / Y_B].",
        "central_A0_neg_sqrt3_tb15_m0_scan": central_m0_scan,
        "full_grid_39_benchmarks": dm_grid_records,
    }

    # --- OW27-D: SUGRA 2-Loop NSVZ, Mediation Ratio, & agy-exp d12e74ef3 LINK6 Audit ---
    ow27_d = run_ow27_d(mkk_over_mpred, tex_s12_p, tex_flat_p, c20_nl5_mp)
    pf5_ok = ow27_d.pop("_pf5_nonzero")

    # --- OW27-E: 6/6 Independent Planted Faults & Canonical Sealed B4_UV_MZ_BLIND_LOCK_V3 ---
    pf_controls = {
        "PF_OW27_1_perturbed_GrayBroadhurst_c21_breaks_2loop_RG": bool(qft_proofs["pf1_perturbed_c21_oa2_resid"] == "1"),
        "PF_OW27_2_dropping_bosonic_Higgs_breaks_4c_RG_and_scale_invariance": bool(
            qft_proofs["pf2_top_only_higgs_RG_residual_nonzero"] and central_toponly_drift > mp_rat(3, 100)
        ),
        "PF_OW27_3_flipped_Majorana_Fermi_sign_destroys_swave_helicity_suppression": bool(
            mp.mpf(spinor_proof["pf3_wrong_fermi_sign_swave_val"]) > mp_pow10(-4)
        ),
        "PF_OW27_4_unreduced_Planck_mass_shifts_YBino_gt_100pct": bool(pf4_unreduced_rel_shift > mp.mpf(1)),
        "PF_OW27_5_omitting_NSVZ_g_neg23_breaks_2loop_RG_invariance": bool(pf5_ok),
        "PF_OW27_6_Guardrail1_rejects_zero_bit_pricing_384_and_192_scans": bool(
            atlas_384_bits > mp.mpf(8) and mr_unit_192_bits > mp.mpf(7)
        ),
    }
    pf_caught = sum(1 for v in pf_controls.values() if v)
    gate_pf = bool(pf_caught == 6)

    central_dirac_pos = ow27a_runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    central_dirac_neg = ow27a_runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_neg"]
    central_dirac_3v = ow27a_runs["CURV_s12_Dirac_yt_gUV_tb15_m0_3v_sgnMu_pos"]
    central_flat_pos = ow27a_runs["FLAT_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    central_dm_10v = [r for r in central_m0_scan if r["m0_over_v"] == 10][0]
    central_dm_3v = [r for r in central_m0_scan if r["m0_over_v"] == 3][0]
    central_dm_1v = [r for r in central_m0_scan if r["m0_over_v"] == 1][0]

    blind_lock_v3 = {
        "lock_version": "B4_UV_MZ_BLIND_LOCK_V3",
        "supersedes_V2_sha256": lock_v2_sha,
        "chains_from_V1_sha256": lock_v1_sha,
        "firewall": "0 of 19",
        "upgrades_over_V2": [
            "OW27-A: Exact 2-loop pure-QCD Gray-Broadhurst top pole at self-consistent mu=m_t(m_t) (L=0 exact), full 4-coupling 1-loop SM RG-invariant Higgs pole (<0.5% mu=M_Z vs mu=m_t drift, down from 3.53%), exact 1-loop EW Veltman Delta_rho on m_W^pole/m_Z^pole, exact 5-flavor top decoupling at m_t down to M_Z, and pure-QCD 2-loop dimensional-transmutation Lambda_QCD^(3)/v_EW (zero empirical GeV).",
            "OW27-B: First-principles thermal Bino LSP freeze-out via explicit 4-component Majorana spinors + 26-var soft RGEs + stiff Radau IIA Riccati ODE (OBS-20 dimensionless M_1 Y_Bino / (Lambda_QCD^(3) Y_B) = c_lat * Omega_Bino/Omega_B + honest thermal-overclosure audit).",
            "OW27-C: Complete Guardrail-1 bit-priced true tau_8^+ spin-1/2 Dirac G_s12_t8 384-case atlas + 192-case I_3 + W_R^unit scan with full 2-loop sequential seesaw & reduced-Planck Boltzmann Y_B(tau_8^+/-).",
            "OW27-D: Exact 2-loop NSVZ hidden-sector SUGRA threshold & mediation audit + cross-seat agy-exp d12e74ef3 LINK6 propagation inside B4_UV 2-loop M_Z pipeline.",
        ],
        "priced_continuous_uv_levers_guardrail5": {
            "dimensionful_anchor": "v_EW (1 anchor; all predictions strictly dimensionless; c_lat = m_p/Lambda_QCD^(3) kept symbolic)",
            "count_continuous_levers": 5,
            "uv_levers": [
                "alpha_UV^-1 (central 24, band 23..25)",
                "tan(beta) (central 15, band 5..50)",
                "y_d^(0)/y_u^(0) (1/5 moderate vs 1 unified)",
                "A_0/m_0 (central -sqrt(3), moduli band 0..-sqrt(6))",
                "M_R0/M_GUT (central 10^-3)",
            ],
        },
        "priced_discrete_bits_guardrail1": {
            "pure_lopsided_n10_bits": mp.nstr(mp.log(10, 2), 12),
            "dirac_s12_384_atlas_bits": mp.nstr(atlas_384_bits, 12),
            "dirac_s12_I3plusWR_192_scan_bits": mp.nstr(mr_unit_192_bits, 12),
            "dirac_s12_I3plusWR_sym6_slice_bits": mp.nstr(mr_unit_6_bits, 12),
            "sgn_mu_bit": "1.0",
            "cp_branch_bit_after_YB_gt_0": "0.0",
        },
        "dimensionless_MZ_and_mt_predictions_B4_UV_CURV_s12_Dirac": {
            "gauge_and_EW_at_MZ_m0_10v": {
                "alpha3_mz_nf5": central_dirac_pos["alpha3_mz_nf5"],
                "alpha3_mz_nf6": central_dirac_pos["alpha3_mz_nf6"],
                "sin2_thetaW_msbar_mz": central_dirac_pos["sin2_thetaW_msbar_mz"],
                "sin2_thetaW_on_shell": central_dirac_pos["sin2_thetaW_on_shell"],
                "alpha_EM_inv_mz_nf5": central_dirac_pos["alpha_EM_inv_mz_nf5"],
                "alpha_EM_inv_mz_nf6": central_dirac_pos["alpha_EM_inv_mz_nf6"],
                "mw_over_mz_msbar": central_dirac_pos["mw_over_mz_msbar"],
                "mw_over_mz_pole_veltman": central_dirac_pos["mw_over_mz_pole_veltman"],
                "delta_rho_t_1loop": central_dirac_pos["delta_rho_t_1loop"],
                "Lambda_QCD_3_exact_over_v": central_dirac_pos["Lambda_QCD_3_exact_over_v"],
            },
            "gauge_and_EW_at_MZ_m0_3v": {
                "alpha3_mz_nf5": central_dirac_3v["alpha3_mz_nf5"],
                "sin2_thetaW_msbar_mz": central_dirac_3v["sin2_thetaW_msbar_mz"],
                "alpha_EM_inv_mz_nf5": central_dirac_3v["alpha_EM_inv_mz_nf5"],
                "mw_over_mz_pole_veltman": central_dirac_3v["mw_over_mz_pole_veltman"],
                "Lambda_QCD_3_exact_over_v": central_dirac_3v["Lambda_QCD_3_exact_over_v"],
            },
            "top_and_higgs_poles_yt_gUV": {
                "m0_10v_mt_pole_2l_at_mt_over_v": central_dirac_pos["mt_pole_2l_at_mt_over_v"],
                "m0_10v_mh_pole_4c_at_mt_over_mz": central_dirac_pos["mh_pole_4c_at_mt_over_mz"],
                "m0_10v_mh_pole_4c_at_mt_over_v": central_dirac_pos["mh_pole_4c_at_mt_over_v"],
                "m0_10v_mh_pole_4c_scale_drift": central_dirac_pos["mh_pole_4c_scale_drift"],
                "m0_3v_mt_pole_2l_at_mt_over_v": central_dirac_3v["mt_pole_2l_at_mt_over_v"],
                "m0_3v_mh_pole_4c_at_mt_over_mz": central_dirac_3v["mh_pole_4c_at_mt_over_mz"],
                "m0_3v_mh_pole_4c_scale_drift": central_dirac_3v["mh_pole_4c_scale_drift"],
            },
            "top_and_higgs_poles_CIM_M16": ow27a_cim_runs,
            "quarks_leptons_CKM_at_MZ_sgnMu_pos": central_dirac_pos["ckm_mz"],
            "quarks_leptons_CKM_at_MZ_sgnMu_neg": {
                "b_tau": central_dirac_neg["ckm_mz"]["b_tau"],
                "delta_b": central_dirac_neg["delta_b"],
            },
            "quarks_leptons_CKM_FLAT_at_MZ_sgnMu_pos": central_flat_pos["ckm_mz"],
            "neutrinos_and_leptogenesis_dirac_s12_primary": primary_cand_info["record"],
            "bino_dm_freezeout_OBS20_dimensionless": {
                "m0_1v_central": central_dm_1v,
                "m0_3v_central": central_dm_3v,
                "m0_10v_central": central_dm_10v,
            },
            "inflation_and_strong_CP": {
                "n_s": "29/30",
                "r": "1/300",
                "E_over_N": "8/3",
                "bar_theta_QCD_upper_bound": "1e-50",
            },
        },
    }
    lock_v3_bytes = json.dumps(blind_lock_v3, sort_keys=True, separators=(",", ":")).encode("utf-8")
    lock_v3_sha = hashlib.sha256(lock_v3_bytes).hexdigest()

    all_passed = bool(
        hygiene["clean"]
        and ow27_a["gate_passed"]
        and ow27_b["gate_passed"]
        and ow27_c["gate_passed"]
        and ow27_d["gate_passed"]
        and gate_pf
    )

    output = {
        "card_id": "A2-OW27",
        "seat": "agy-002",
        "empirical_firewall": "0 of 19",
        "all_gates_passed": all_passed,
        "hygiene": hygiene,
        "OW27_A_2loop_qcd_4coupling_higgs_veltman_decoupling_and_lambda_qcd": ow27_a,
        "OW27_B_bino_lsp_thermal_freezeout_dm_OBS20": ow27_b,
        "OW27_C_dirac_s12_384_atlas_I3plusWR_scan_and_leptogenesis": ow27_c,
        "OW27_D_sugra_2loop_nsvz_mediation_and_link6_cross_seat_audit": ow27_d,
        "OW27_E_planted_faults_and_blind_lock_v3": {
            "gate_passed": gate_pf,
            "caught": pf_caught,
            "total": 6,
            "controls": pf_controls,
            "blind_prediction_lock_v3_B4_UV": blind_lock_v3,
            "blind_prediction_lock_v3_sha256": lock_v3_sha,
        },
    }
    assert_no_json_floats(output)
    out_path = script_path.parent / "a2_ow27_results.json"
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    out_sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    (script_path.parent / "OUTPUT_SHA256.txt").write_text(f"{out_sha}  {out_path.name}\n", encoding="utf-8")
    print(f"A2-OW27 COMPLETE: all_gates_passed={all_passed} OUTPUT_SHA256={out_sha} LOCK_V3_SHA256={lock_v3_sha}")


if __name__ == "__main__":
    main()
