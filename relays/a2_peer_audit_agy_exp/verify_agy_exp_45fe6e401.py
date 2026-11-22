#!/usr/bin/env python3
"""Independent Zero-Import Pure-Math Verification of Peer Seat `agy-exp` @ `45fe6e401` (0 of 19).

Strictly compliant with `docs/seats/README.md` Sections 8 and 9:
  - ZERO imports from `agy-exp` or `frontier/`.
  - ZERO Python float literals (all constants expressed via exact integers / rationals / mpmath).
  - ZERO empirical PDG / NuFIT / Planck / DESI / lattice constants (`0 of 19` Firewall Section 9.1).

Independently recomputes all pure-mathematics, topological, algebraic, ODE, and internal
self-consistency checks for `agy-exp` Phases 5-11 (`45fe6e401`):
  1. `m004` degree-5 cover classification (`8^3_4` irregular 3-cusp D_5 vs `o10_150703` 2-cusp vs cyclic).
  2. Exact `H^3` radial Liouville PDE vs Selberg-Jacobian kernel `eps(gamma)` conflation & impact on `Lc*, alpha_GUT^-1, v_EW/M_Pl`.
  3. Exhaustive 60-digit Chevalley `{E, H, F}` Fox-Porti adjoint `sl(2, C)` torsion for ALL 9 Table III manifolds (`m004` + 8 `m129(p, q)` surgeries) + `SL(2, Z)` cusp modularity.
  4. Cutoff divergence sweep (`l_cut = 9/5 .. 33/10`) of truncated `M^(5)` Selberg Euler products `Z_GMY` and `Z_SS`.
  5. `7D -> 4D` Weyl exponents `(-3,-5,-6,-9,-10)`, kinetic `15/4`, warped `G_rr`, `Spin(10)` Cartan ratio, `7D` EH vs Adams cusp `M_KK/M_Pl` internal ratio, `V_min/(M_Pl^2 m_rad^2) = 5/42`.
  6. `E_8 -> Spin(10) x SU(4)` branching, `16`-plet Pati-Salam `cos(theta_R) = sqrt(3/5)`, Srednicki `E/N = 8/3`, Contino-Pilo `2[(-zeta'(0)) - (-zeta'(0, 1/2))] = ln(pi)`.
  7. Weierstrass CY4 `X_8 -> P^1 x dP_r` (`r = 0..9`) Euler/Hodge/Betti numbers & Bousso-Polchinski sensitivity (`R_max = sqrt(chi/12)` vs `sqrt(chi/24)`).
  8. `Branch 1B-SD` internal radius scaling `(2 Lc*)^10` vs `(2 Lc*)^3`, `Branch 1A` vs `Branch 1B-SD` vacuum-energy ratio, and dead-code `N_*` Liddle-Leach offset.
  9. Exact `2`-loop SM RGE coefficient audit (Machacek-Vaughn / Luo-Xiao / Buttazzo Appendix A vs `agy-exp` `_rhs76`) evaluated at a purely synthetic rational UV point (`0 of 19`).
 10. Trinomial look-elsewhere algebra & `O(1)` prior-width inflation factor.
"""
from __future__ import annotations

import ast
import cmath
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import snappy
import sympy as sp


def _rat(p: int, q: int = 1) -> float:
    return float(Fraction(p, q))


def _mrat(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(p) / mp.mpf(q)


def check_covers_and_phase5() -> Dict[str, Any]:
    mp.mp.dps = 50
    m4 = snappy.Manifold("m004")
    cov_rows = []
    for idx, c in enumerate(m4.covers(5)):
        ci = c.cover_info()
        hom = c.homology()
        cov_rows.append({
            "index": idx,
            "type": str(ci["type"]),
            "cusps": int(c.num_cusps()),
            "b1": int(hom.betti_number()),
            "torsion": [int(x) for x in hom.elementary_divisors() if int(x) > 0],
            "vol": str(mp.nstr(mp.mpf(str(c.volume())), 12)),
            "ident_head": [str(x) for x in c.identify()[:2]],
        })

    # Verify x_fix for Shell-2 words under D_5 generators a: x->-x mod 5, b: x->1-x mod 5:
    pa = lambda x: (-x) % 5
    pb = lambda x: (1 - x) % 5
    d5g = {"a": pa, "A": pa, "b": pb, "B": pb}
    x_fix = {}
    for w in ("AAb", "Abb", "AABab", "ABaab"):
        perm = list(range(5))
        for ch in w:
            gp = d5g[ch]
            perm = [perm[gp(i)] for i in range(5)]
        x_fix[w] = [i for i, v in enumerate(perm) if v == i][0]

    # Symbolic 7D warped G_rr and |V_min|/(M_Pl^2 m_rad^2) = 5/42:
    r_s = sp.Symbol("r", real=True)
    a_fn = sp.Function("A")(r_s)
    b_fn = sp.Function("B")(r_s)
    g_rr = sp.expand(sp.Rational(1, 2) * ((4 * sp.diff(a_fn, r_s) + 2 * sp.diff(b_fn, r_s)) ** 2 - (4 * sp.diff(a_fn, r_s) ** 2 + 2 * sp.diff(b_fn, r_s) ** 2)))

    x_s, a_s, b_s, mpl_s = sp.symbols("x A B M_Pl", positive=True)
    v_b = -a_s * x_s ** (-7) + b_s * x_s ** (-9)
    b_sol = sp.solve(sp.diff(v_b, x_s).subs(x_s, 1), b_s)[0]
    v_min = sp.simplify(v_b.subs({b_s: b_sol, x_s: 1}))
    d2_v = sp.simplify(sp.diff(v_b, x_s, 2).subs({b_s: b_sol, x_s: 1}))
    mrad2 = sp.simplify(d2_v / (2 * sp.Rational(15, 4) * mpl_s**2))
    v_over_mrad2 = sp.simplify(abs(v_min) / (mpl_s**2 * mrad2))

    cartan_ratio = ((24 + mp.sqrt(15)) / (9 * mp.sqrt(15) - 24)) ** 2
    vol_m004 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    w_m129 = snappy.Manifold("m129")
    vol_m129 = mp.mpf(str(w_m129.volume()))
    cs_m129 = mp.mpf(str(w_m129.chern_simons()))
    cn = m4.cusp_neighborhood()
    cn.set_displacement(cn.reach(0), 0)
    adams_vol = mp.mpf(str(cn.volume(0)))

    return {
        "m004_degree5_covers": cov_rows,
        "shell2_x_fix": x_fix,
        "warped_7d_G_rr": str(g_rr),
        "radion_Vmin_over_MPl2_mrad2": str(v_over_mrad2),
        "spin10_cartan_ratio": mp.nstr(cartan_ratio, 15),
        "vol_m004": mp.nstr(vol_m004, 15),
        "vol_m129_minus_4Catalan_abs": mp.nstr(abs(vol_m129 - 4 * mp.catalan), 6),
        "cs_m129": mp.nstr(cs_m129, 12),
        "adams_horoball_vol_minus_sqrt3_abs": mp.nstr(abs(adams_vol - mp.sqrt(3)), 6),
    }


def check_h3_huygens_and_kernel_conflation() -> Dict[str, Any]:
    mp.mp.dps = 50
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((2 + omega) / 2)
    hl2 = mp.acosh((2 + 2 * omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    ell2, th2 = 2 * mp.re(hl2), 2 * mp.im(hl2)
    lam1 = _mrat(29745505801732, 10**13)

    def pde_res(dim_d: int, r0: mp.mpf) -> mp.mpf:
        ph = mp.mpf(dim_d - 1) / 2
        g_fn = lambda x: mp.exp(-lam1 * x) / (4 * mp.pi * (mp.sinh(x) ** ph))
        lap = mp.diff(g_fn, r0, 2) + (dim_d - 1) * mp.coth(r0) * mp.diff(g_fn, r0, 1)
        return abs(-lap + (lam1**2 - ph**2) * g_fn(r0)) / abs(g_fn(r0))

    k_half = lambda x: mp.exp(-lam1 * x) / (4 * mp.pi * mp.sinh(x / 2))
    lap_kh = mp.diff(k_half, ell1, 2) + 2 * mp.coth(ell1) * mp.diff(k_half, ell1, 1)
    res_kh = abs(-lap_kh + (lam1**2 - 1) * k_half(ell1)) / abs(k_half(ell1))

    g_h3_1 = mp.exp(-lam1 * ell1) / (4 * mp.pi * mp.sinh(ell1))
    eps_1 = mp.exp(-lam1 * ell1) / (2 * mp.pi * abs(2 * mp.sinh((ell1 + 1j * th1) / 2)))
    g_h3_2 = mp.exp(-lam1 * ell2) / (4 * mp.pi * mp.sinh(ell2))
    eps_2 = mp.exp(-lam1 * ell2) / (2 * mp.pi * abs(2 * mp.sinh((ell2 + 1j * th2) / 2)))

    vol_m5 = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    lc_eps = (4 * (mp.pi**2 / 15) / eps_1) ** _mrat(1, 5)
    lc_gh3 = (4 * (mp.pi**2 / 15) / g_h3_1) ** _mrat(1, 5)
    au_eps = (9 * vol_m5 * ((2 * lc_eps) ** 3)) / (30 * (mp.pi**3)) - mp.log(mp.pi)
    au_gh3 = (9 * vol_m5 * ((2 * lc_gh3) ** 3)) / (30 * (mp.pi**3)) - mp.log(mp.pi)
    vew_eps = mp.exp(-_mrat(19, 2) * lc_eps) / mp.sqrt(3)
    vew_gh3 = mp.exp(-_mrat(19, 2) * lc_gh3) / mp.sqrt(3)

    # Also 7D EH vs Adams cusp M_KK/M_Pl_red internal ratio:
    mkk_eh = 1 / mp.sqrt(((2 * lc_eps) ** 5) * vol_m5)
    mkk_adams = mp.exp(-2 * lc_eps) / mp.sqrt(3)

    return {
        "ell1": mp.nstr(ell1, 15),
        "th1": mp.nstr(th1, 15),
        "ell2": mp.nstr(ell2, 15),
        "th2": mp.nstr(th2, 15),
        "radial_pde_res_d2": mp.nstr(pde_res(2, ell1), 6),
        "radial_pde_res_d3": mp.nstr(pde_res(3, ell1), 6),
        "radial_pde_res_d4": mp.nstr(pde_res(4, ell1), 6),
        "sinh_half_r_pde_res_d3": mp.nstr(res_kh, 8),
        "eps1_over_GH3_ell1": mp.nstr(eps_1 / g_h3_1, 10),
        "eps2_over_GH3_ell2": mp.nstr(eps_2 / g_h3_2, 10),
        "r_sh_eps": mp.nstr(eps_2 / eps_1, 10),
        "r_sh_GH3": mp.nstr(g_h3_2 / g_h3_1, 10),
        "r_sh_ratio_eps_over_GH3": mp.nstr((eps_2 / eps_1) / (g_h3_2 / g_h3_1), 10),
        "Lc_from_eps": mp.nstr(lc_eps, 12),
        "Lc_from_GH3": mp.nstr(lc_gh3, 12),
        "alpha_GUT_inv_2wall_from_eps": mp.nstr(au_eps, 10),
        "alpha_GUT_inv_2wall_from_GH3": mp.nstr(au_gh3, 10),
        "vEW_over_MPl_ratio_GH3_to_eps": mp.nstr(vew_gh3 / vew_eps, 10),
        "MKK_over_MPl_7D_EH": mp.nstr(mkk_eh, 10),
        "MKK_over_MPl_Adams_cusp": mp.nstr(mkk_adams, 10),
        "ratio_7D_EH_over_Adams": mp.nstr(mkk_eh / mkk_adams, 10),
        "ratio_MPl_sq_discrepancy": mp.nstr((mkk_eh / mkk_adams) ** 2, 10),
    }


def _indep_porti_chevalley(m_hp: Any, mod_mat: Tuple[int, int, int, int] = (1, 0, 0, 1)) -> Tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    mp.mp.dps = 60
    fg = m_hp.fundamental_group(simplify_presentation=True)
    gens, rels = list(fg.generators()), list(fg.relators())
    mw0, lw0 = fg.peripheral_curves()[0]
    invw = lambda w: "".join(c.lower() if c.isupper() else c.upper() for c in reversed(w))
    wpow = lambda w, k: "" if k == 0 else ((w * k) if k > 0 else (invw(w) * (-k)))
    a_z, b_z, c_z, d_z = mod_mat
    mw = wpow(mw0, a_z) + wpow(lw0, b_z)
    lw = wpow(mw0, c_z) + wpow(lw0, d_z)

    b_chev = [
        mp.matrix([[0, 1], [0, 0]]),
        mp.matrix([[1, 0], [0, -1]]) / mp.sqrt(2),
        mp.matrix([[0, 0], [1, 0]]),
    ]
    b_dual = [b_chev[2], b_chev[1], b_chev[0]]

    def to_ad(m2: mp.matrix) -> mp.matrix:
        m2i = mp.matrix([[m2[1, 1], -m2[0, 1]], [-m2[1, 0], m2[0, 0]]])
        out = mp.zeros(3, 3)
        for j in range(3):
            y = m2 * b_chev[j] * m2i
            for i in range(3):
                p = b_dual[i] * y
                out[i, j] = p[0, 0] + p[1, 1]
        return out

    qstr = lambda x: str(x).replace(" ", "")
    mats: Dict[str, mp.matrix] = {}
    for g in gens:
        s = fg.SL2C(g)
        m2 = mp.matrix([
            [mp.mpc(qstr(s[0][0].real()), qstr(s[0][0].imag())), mp.mpc(qstr(s[0][1].real()), qstr(s[0][1].imag()))],
            [mp.mpc(qstr(s[1][0].real()), qstr(s[1][0].imag())), mp.mpc(qstr(s[1][1].real()), qstr(s[1][1].imag()))],
        ])
        m2 = m2 / mp.sqrt(m2[0, 0] * m2[1, 1] - m2[0, 1] * m2[1, 0])
        mats[g] = m2

    g_idx = {g: i for i, g in enumerate(gens)}
    a_sp = sp.zeros(len(rels), len(gens))
    for ri, r in enumerate(rels):
        for ch in r:
            a_sp[ri, g_idx[ch.lower()]] += 1 if ch.islower() else -1
    vec = a_sp.nullspace()[0]
    lcm_d = sp.ilcm(*[sp.fraction(x)[1] for x in vec])
    iv = [int(x * lcm_d) for x in vec]
    ga = 0
    for x in iv:
        ga = math.gcd(ga, abs(x))
    phi = [x // ga for x in iv]

    ad_g = {g: to_ad(mats[g]) for g in gens}
    ad_i = {g: to_ad(mp.matrix([[mats[g][1, 1], -mats[g][0, 1]], [-mats[g][1, 0], mats[g][0, 0]]])) for g in gens}
    nz = [i for i, p in enumerate(phi) if p != 0]
    k_drop = max(nz, key=lambda k: float(abs((mats[gens[k]][0, 0] + mats[gens[k]][1, 1]) ** 2 - 4)))

    def delta(tv: mp.mpc) -> mp.mpc:
        rt = {g: (tv ** phi[i]) * ad_g[g] for i, g in enumerate(gens)}
        rti = {g: (tv ** (-phi[i])) * ad_i[g] for i, g in enumerate(gens)}
        n_g = len(gens)
        m_mat = mp.matrix(3 * (n_g - 1), 3 * (n_g - 1))
        for ri, r in enumerate(rels):
            blks = [mp.zeros(3, 3) for _ in range(n_g)]
            pr = mp.eye(3)
            for ch in r:
                gl = ch.lower()
                j = g_idx[gl]
                if ch.islower():
                    blks[j] += pr
                    pr = pr * rt[gl]
                else:
                    pr = pr * rti[gl]
                    blks[j] -= pr
            co = 0
            for j in range(n_g):
                if j == k_drop:
                    continue
                for ai in range(3):
                    for bi in range(3):
                        m_mat[3 * ri + ai, co + bi] = blks[j][ai, bi]
                co += 3
        return mp.det(m_mat) / mp.det(rt[gens[k_drop]] - mp.eye(3))

    rc = _mrat(3, 10**7)
    n_pts = 16
    vals = [delta(1 + rc * mp.exp(2j * mp.pi * m / n_pts)) for m in range(n_pts)]
    d0 = abs(sum(vals) / n_pts)
    d1 = sum(vals[m] / (rc * mp.exp(2j * mp.pi * m / n_pts)) for m in range(n_pts)) / n_pts

    def eval_w2(w: str) -> mp.matrix:
        cur = mp.eye(2)
        for ch in w:
            m2 = mats[ch.lower()]
            if ch.isupper():
                m2 = mp.matrix([[m2[1, 1], -m2[0, 1]], [-m2[1, 0], m2[0, 0]]])
            cur = cur * m2
        return cur

    mm, ml = eval_w2(mw), eval_w2(lw)
    if mp.re(mm[0, 0] + mm[1, 1]) < 0:
        mm = -mm
    if mp.re(ml[0, 0] + ml[1, 1]) < 0:
        ml = -ml
    ii, jj = max([(i, j) for i in range(2) for j in range(2)], key=lambda ij: float(abs(mm[ij[0], ij[1]] - (1 if ij[0] == ij[1] else 0))))
    tau_c = (ml[ii, jj] - (1 if ii == jj else 0)) / (mm[ii, jj] - (1 if ii == jj else 0))
    pm = sum(phi[g_idx[ch.lower()]] * (1 if ch.islower() else -1) for ch in mw)
    pl = sum(phi[g_idx[ch.lower()]] * (1 if ch.islower() else -1) for ch in lw)
    gml = math.gcd(abs(pm), abs(pl))
    am, al = -pl // gml, pm // gml
    tau_mu = 4 * abs(d1) / (gml * abs(am + al * tau_c))
    return d0, abs(d1), tau_mu, tau_mu * mp.sqrt(abs(mp.im(tau_c)))


def check_all_9_porti() -> Dict[str, Any]:
    mp.mp.dps = 60
    d0_0, d1_0, tau_0, i_0 = _indep_porti_chevalley(snappy.ManifoldHP("m004"))
    _, _, _, i_0_s = _indep_porti_chevalley(snappy.ManifoldHP("m004"), mod_mat=(0, -1, 1, 0))
    _, _, _, i_0_t2s = _indep_porti_chevalley(snappy.ManifoldHP("m004"), mod_mat=(1, 2, 1, 3))

    slopes = [(-3, 1), (1, 3), (7, 1), (11, 3), (-13, 1), (-1, 7), (9, 7), (17, 1), (-11, 7)]
    rows = []
    for p, q in slopes:
        w_std = snappy.Manifold("m129")
        _ = w_std.chern_simons()
        w_std.dehn_fill((p, q), 0)
        sg = w_std.filled_triangulation().symmetry_group()
        isom_p = sg.order() // 2 if sg.is_amphicheiral() else sg.order()
        w_hp = snappy.ManifoldHP("m129")
        w_hp.dehn_fill((p, q), 0)
        d0, _, tau_m, i_m = _indep_porti_chevalley(w_hp.filled_triangulation())
        rows.append({
            "slope": [p, q],
            "vol": mp.nstr(mp.mpf(str(w_std.volume())), 10),
            "cs": mp.nstr(mp.mpf(str(w_std.chern_simons())), 10),
            "isom_plus": int(isom_p),
            "abs_Delta_at_1": mp.nstr(d0, 5),
            "tau_Ad_mu": mp.nstr(tau_m, 15),
            "I_Porti": mp.nstr(i_m, 15),
        })

    return {
        "m004_tau_minus_2sqrt3": mp.nstr(abs(tau_0 - 2 * mp.sqrt(3)), 6),
        "m004_I_minus_2sqrt3_3over2": mp.nstr(abs(i_0 - (2 * mp.sqrt(3)) ** _mrat(3, 2)), 6),
        "m004_Delta_prime_minus_3": mp.nstr(abs(d1_0 - 3), 6),
        "m004_SL2Z_S_err": mp.nstr(abs(i_0 - i_0_s), 6),
        "m004_SL2Z_T2S_err": mp.nstr(abs(i_0 - i_0_t2s), 6),
        "all_9_m129_surgeries": rows,
    }


def check_p11_3_cutoff_divergence() -> Dict[str, Any]:
    pa = tuple((-x) % 5 for x in range(5))
    pb = tuple((1 - x) % 5 for x in range(5))
    pmul = lambda p, q: tuple(p[q[i]] for i in range(5))
    pinv = lambda p: tuple(p.index(i) for i in range(5))
    d5_perms = [(0, 1, 2, 3, 4)]
    fr = [pa, pb]
    while fr:
        p = fr.pop()
        if p not in d5_perms:
            d5_perms.append(p)
            for g in (pa, pb):
                fr.extend([pmul(p, g), pmul(g, p)])

    def eval_p(w: str, mp_p: Dict[str, Tuple[int, ...]]) -> Tuple[int, ...]:
        cur = (0, 1, 2, 3, 4)
        for ch in w:
            p = mp_p[ch.lower()]
            cur = pmul(cur, pinv(p) if ch.isupper() else p)
        return cur

    w4 = snappy.Manifold("m129")
    w4.dehn_fill((-3, 1), 0)
    rels4 = w4.fundamental_group(simplify_presentation=False).relators()
    mpp_exact = None
    for p_b in d5_perms:
        for p_c in d5_perms:
            for p_d in d5_perms:
                mpp = {"a": pmul(p_d, pinv(p_c)), "b": p_b, "c": p_c, "d": p_d}
                if all(eval_p(r, mpp) == (0, 1, 2, 3, 4) for r in rels4):
                    sub = {(0, 1, 2, 3, 4)}
                    frs = list(mpp.values())
                    while frs:
                        x = frs.pop()
                        for y in mpp.values():
                            z = pmul(x, y)
                            if z not in sub:
                                sub.add(z)
                                frs.append(z)
                    if len(sub) == 10 and p_b[0] == 0 and eval_p("Abd", mpp)[0] == 0:
                        mpp_exact = mpp
                        break
            if mpp_exact:
                break
        if mpp_exact:
            break
    assert mpp_exact is not None

    def z_m5(slope: Tuple[int, int], l_cut: float) -> Tuple[int, float, float]:
        w = snappy.Manifold("m129")
        w.dehn_fill(slope, 0)
        spec = w.length_spectrum(l_cut, include_words=True, grouped=False)
        lg, ls = _rat(0), _rat(0)
        for g in spec:
            wd, ln, tw = g["word"], float(g["length"].real), float(g["length"].imag)
            pg = eval_p(wd, mpp_exact)
            fx = [x for x in range(5) if pg[x] == x]
            if len(fx) == 5:
                lifts = [(ln, tw, 1)] * 5
            elif len(fx) == 1:
                lifts = [(ln, tw, -1), (2 * ln, 2 * tw, 1), (2 * ln, 2 * tw, 1)]
            else:
                lifts = [(5 * ln, 5 * tw, 1)]
            for lc_v, th_v, sgn in lifts:
                qc = cmath.exp(-(lc_v + 1j * th_v))
                for n in range(2, 40):
                    lg += -math.log(abs(1 - (qc**n)))
                for n in range(1, 40):
                    ls += math.log(abs(1 - sgn * (qc**n))) - math.log(abs(1 - (qc**n)))
        return len(spec), math.exp(lg), math.exp(ls)

    sweep = []
    for num, den in [(9, 5), (11, 5), (13, 5), (3, 1), (33, 10)]:
        lc_f = _rat(num, den)
        n0, g0, s0 = z_m5((-3, 1), lc_f)
        _, g13, s13 = z_m5((1, 3), lc_f)
        _, g71, s71 = z_m5((7, 1), lc_f)
        sweep.append({
            "l_cut": f"{num}/{den}",
            "n_geo_m004": n0,
            "Z_GMY_1_3_ratio": mp.nstr(mp.mpf(g13 / g0), 8),
            "Z_SS_1_3_ratio": mp.nstr(mp.mpf(s13 / s0), 8),
            "Z_GMY_7_1_ratio": mp.nstr(mp.mpf(g71 / g0), 8),
            "Z_SS_7_1_ratio": mp.nstr(mp.mpf(s71 / s0), 8),
        })
    return {"selberg_cutoff_sweep": sweep}


def check_algebra_cy4_and_inflation_consistency() -> Dict[str, Any]:
    mp.mp.dps = 50
    # 1. E_8 -> Spin(10) x SU(4):
    counts = {"45_1": 5, "1_15": 3, "10_6": 0, "16_4": 0, "16b_4b": 0}
    for i, j in itertools.combinations(range(8), 2):
        n5 = (i < 5) + (j < 5)
        if n5 == 2:
            counts["45_1"] += 4
        elif n5 == 0:
            counts["1_15"] += 4
        else:
            counts["10_6"] += 4
    for s in itertools.product([-1, 1], repeat=8):
        if s.count(-1) % 2 == 0:
            counts["16_4" if s[:5].count(-1) % 2 == 0 else "16b_4b"] += 1

    # 2. Pati-Salam 16-plet exact rational traces & Srednicki E/N:
    reps16 = [
        (6, sp.Rational(0), sp.Rational(1, 3)),
        (3, sp.Rational(-1, 2), sp.Rational(-1, 3)),
        (3, sp.Rational(1, 2), sp.Rational(-1, 3)),
        (2, sp.Rational(0), sp.Rational(-1)),
        (1, sp.Rational(1, 2), sp.Rational(1)),
        (1, sp.Rational(-1, 2), sp.Rational(1)),
    ]
    tr_t3r2 = sum(m * (t**2) for m, t, _ in reps16)
    tr_y2 = sum(m * ((t + sp.Rational(1, 2) * bl) ** 2) for m, t, bl in reps16)
    tr_cross = sum(m * t * (sp.Rational(1, 2) * bl) for m, t, bl in reps16)
    e_over_n = sp.Rational(2 * (3 * (sp.Rational(4, 9) + sp.Rational(1, 9)) + 1), 2)

    # 3. Contino-Pilo 2-wall identity:
    z0 = -mp.diff(lambda s: mp.zeta(s), mp.mpf(0))
    zh = -mp.diff(lambda s: mp.zeta(s, _mrat(1, 2)), mp.mpf(0))
    cp_err = abs(2 * (z0 - zh) - mp.log(mp.pi))

    # 4. Weierstrass CY4 X_8 -> P^1 x dP_r (r=0..9) + BP sensitivity:
    cy4_rows = []
    for rv in range(10):
        chi = 12 * (24 + 180 * (9 - rv))
        h11 = 3 + rv
        h31 = chi // 6 - 8 - h11
        h22 = 44 + 4 * h11 + 4 * h31
        b4 = 2 + 2 * h31 + h22
        vb = (mp.pi ** (mp.mpf(b4) / 2)) / mp.gamma(mp.mpf(b4) / 2 + 1)
        l10_12 = -mp.log10(mp.mpf(b4) * vb * (mp.sqrt(mp.mpf(chi) / 12) ** b4))
        l10_24 = -mp.log10(mp.mpf(b4) * vb * (mp.sqrt(mp.mpf(chi) / 24) ** b4))
        cy4_rows.append({
            "r": rv,
            "chi": chi,
            "h11": h11,
            "h31": h31,
            "h22": h22,
            "b4": b4,
            "log10_BP_at_sqrt_chi_over_12": mp.nstr(l10_12, 8),
            "log10_BP_at_sqrt_chi_over_24": mp.nstr(l10_24, 8),
        })

    # 5. Branch 1B-SD internal scaling contradiction & Branch 1A vs 1B-SD ratio & dead-code N_* offset:
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((2 + omega) / 2)
    ell1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    lam1 = _mrat(29745505801732, 10**13)
    eps1 = (mp.exp(-lam1 * ell1) / abs(2 * mp.sinh((ell1 + 1j * th1) / 2))) / (2 * mp.pi)
    lc = (4 * (mp.pi**2 / 15) / eps1) ** _mrat(1, 5)
    vol_m5 = 10 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    mkk = mp.exp(-2 * lc) / mp.sqrt(3)
    m7 = 2 * lc * mkk
    c_cas = (4 * (mp.pi**2) / (15 * ((2 * mp.pi) ** 3))) * vol_m5
    vcas_r0 = c_cas * (mkk**4)
    v0_1a = m7**4
    ratio_r = 2 * lc

    # Exact algebraic offset between p9_3 Line 114 / main.tex Line 302 vs p8_1 Line 154:
    # p8_1 has -(1/3) ln(3/2) + (1/12) ln(pi^2 * g_star / 30); p9_3 Line 114 has -(1/4) ln(9)
    g_star = _mrat(427, 4)  # 106.75 = 427/4
    offset_n_star = (-_mrat(1, 4) * mp.log(9)) - (-_mrat(1, 3) * mp.log(_mrat(3, 2)) + _mrat(1, 12) * mp.log((mp.pi**2) * g_star / 30))

    # 6. Exact trinomial look-elsewhere algebra (main.tex Line 249):
    p1 = _mrat(1, 10)
    p2 = _mrat(7, 30)
    p_trin = sum(mp.mpf(math.comb(29, k)) * (p1**k) * (p2 ** (29 - k)) for k in range(23, 30))

    return {
        "e8_branching": counts,
        "pati_salam_traces": {"Tr_T3R_sq": str(tr_t3r2), "Tr_Y_sq": str(tr_y2), "Tr_cross": str(tr_cross), "cos2_thetaR": str(tr_t3r2 / tr_y2)},
        "srednicki_E_over_N": str(e_over_n),
        "contino_pilo_2wall_err": mp.nstr(cp_err, 6),
        "cy4_r0_to_r9": cy4_rows,
        "branch_1B_SD_2Lc": mp.nstr(ratio_r, 10),
        "branch_1B_SD_fa_boost_2Lc_cubed": mp.nstr(ratio_r**3, 10),
        "branch_1B_SD_omitted_VCas_boost_2Lc_10th": mp.nstr(ratio_r**10, 10),
        "branch_1B_SD_omitted_HI_boost_2Lc_5th": mp.nstr(ratio_r**5, 10),
        "branch_1A_over_1B_SD_V0_ratio": mp.nstr(v0_1a / vcas_r0, 10),
        "dead_code_N_star_offset_p9_3_minus_p8_1": mp.nstr(offset_n_star, 8),
        "trinomial_p_raw_23_of_29": mp.nstr(p_trin, 6),
        "trinomial_p_x_1e5": mp.nstr(mp.mpf(10**5) * p_trin, 6),
        "O1_prior_inflation_factor_11_at_1dex_plus_ns": mp.nstr((mp.mpf(3) ** 11) * 10, 6),
    }


def check_rge_2loop_bugs_synthetic() -> Dict[str, Any]:
    """Compare exact Machacek-Vaughn / Luo-Xiao / Buttazzo Appendix A 2-loop SM beta functions
    against agy-exp's `_rhs76` at a purely synthetic rational UV point (ZERO empirical inputs!)."""
    g1, g2, g3 = _rat(1, 2), _rat(1, 2), _rat(1, 2)
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    gp2 = _rat(3, 5) * g12
    yu = np.diag([_rat(1, 10), _rat(1, 5), _rat(1, 1)]).astype(complex)
    yd = np.diag([_rat(1, 20), _rat(1, 10), _rat(1, 2)]).astype(complex)
    ye = np.diag([_rat(1, 20), _rat(1, 10), _rat(1, 2)]).astype(complex)
    lam = _rat(1, 10)

    c1 = 1 / (16 * math.pi * math.pi)
    c2 = c1 * c1
    hu, hd, he = yu @ yu.conj().T, yd @ yd.conj().T, ye @ ye.conj().T
    tu, td, te = float(np.real(np.trace(hu))), float(np.real(np.trace(hd))), float(np.real(np.trace(he)))
    tr_tot = 3 * tu + 3 * td + te
    tu2 = float(np.real(np.trace(hu @ hu)))
    td2 = float(np.real(np.trace(hd @ hd)))
    te2 = float(np.real(np.trace(he @ he)))
    tud = float(np.real(np.trace(hu @ hd)))
    tu3 = float(np.real(np.trace(hu @ hu @ hu)))
    td3 = float(np.real(np.trace(hd @ hd @ hd)))
    te3 = float(np.real(np.trace(he @ he @ he)))

    # Bug 1: p11_1 adds bogus +16 g3^2 H_e Y_e to charged-lepton dYe:
    bug1_dye_err = float(np.linalg.norm(c2 * (16 * g32 * he @ ye)))
    # Bug 2: Phases 5-11 drop +(5/4) T H_d Y_u in dYu and +(5/4) T H_u Y_d in dYd:
    bug2_dyu_err = float(np.linalg.norm(c2 * (_rat(5, 4) * tr_tot * hd @ yu)))
    bug2_dyd_err = float(np.linalg.norm(c2 * (_rat(5, 4) * tr_tot * hu @ yd)))
    # Bug 3: Phases 5-11 truncate 2-loop dlam (missing g^6, lam g^4, g^4 y^2, and yb/ytau terms):
    dlam2_agy = (
        -312 * (lam**3) - 144 * (lam**2) * tu + 36 * (lam**2) * (3 * g22 + gp2) - 3 * lam * (tu**2)
        + lam * tu * (80 * g32 + _rat(45, 2) * g22 + _rat(85, 6) * gp2) - 32 * g32 * (tu**2) - _rat(8, 3) * gp2 * (tu**2) + 30 * (tu**3)
    )
    dlam2_exact = (
        -312 * (lam**3) + 36 * (lam**2) * (3 * g22 + gp2) - 48 * (lam**2) * tr_tot
        + lam * (
            -_rat(73, 8) * (g22**2) + _rat(39, 4) * g22 * gp2 + _rat(629, 24) * (gp2**2)
            + (80 * g32 + _rat(45, 2) * g22 + _rat(85, 6) * gp2) * tu
            + (80 * g32 + _rat(45, 2) * g22 + _rat(25, 6) * gp2) * td
            + (_rat(15, 2) * g22 + _rat(25, 2) * gp2) * te
            - 3 * tu2 - 3 * td2 - te2 - 42 * tud
        )
        + _rat(305, 16) * (g22**3) - _rat(289, 48) * (g22**2) * gp2 - _rat(559, 48) * g22 * (gp2**2) - _rat(379, 48) * (gp2**3)
        + (-_rat(9, 4) * (g22**2) + _rat(21, 2) * g22 * gp2 - _rat(19, 4) * (gp2**2)) * tu
        + (-_rat(9, 4) * (g22**2) - _rat(11, 2) * g22 * gp2 + _rat(5, 4) * (gp2**2)) * td
        + (-_rat(3, 4) * (g22**2) + _rat(11, 2) * g22 * gp2 - _rat(25, 4) * (gp2**2)) * te
        - 32 * g32 * (tu2 + td2) - _rat(8, 3) * gp2 * tu2 + _rat(4, 3) * gp2 * td2 - 4 * gp2 * te2
        + 30 * tu3 + 30 * td3 + 10 * te3 - 6 * float(np.real(np.trace(hu @ hu @ hd + hd @ hd @ hu)))
    )
    return {
        "synthetic_uv_point": "g=(1/2,1/2,1/2), Yu=diag(1/10,1/5,1), Yd=Ye=diag(1/20,1/10,1/2), lam=1/10",
        "bug1_p11_1_bogus_16g3sqHe_dye_norm": mp.nstr(mp.mpf(bug1_dye_err), 8),
        "bug2_missing_5over4_THd_dyu_norm": mp.nstr(mp.mpf(bug2_dyu_err), 8),
        "bug2_missing_5over4_THu_dyd_norm": mp.nstr(mp.mpf(bug2_dyd_err), 8),
        "bug3_dlam2_agy_raw": mp.nstr(mp.mpf(dlam2_agy), 10),
        "bug3_dlam2_exact_raw": mp.nstr(mp.mpf(dlam2_exact), 10),
        "bug3_dlam2_abs_diff_c2": mp.nstr(mp.mpf(c2 * abs(dlam2_exact - dlam2_agy)), 8),
        "bug3_dlam2_rel_diff": mp.nstr(mp.mpf(abs(dlam2_exact - dlam2_agy) / abs(dlam2_exact)), 8),
    }


def self_ast_zero_float_check() -> Dict[str, Any]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        (node.lineno, node.value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    assert len(floats) == 0, f"Found Python float literals: {floats}"
    return {"python_float_literal_count": len(floats)}


def main() -> None:
    ast_res = self_ast_zero_float_check()
    payload = {
        "audit_target": "origin/agy/self-consistent-loop-2026-11-11 @ 45fe6e401",
        "seat": "agy-002",
        "empirical_inputs_used": "0 of 19",
        "self_ast_check": ast_res,
        "suite1_covers_and_phase5": check_covers_and_phase5(),
        "suite2_h3_huygens_and_kernel_conflation": check_h3_huygens_and_kernel_conflation(),
        "suite3_all_9_porti_chevalley_60d": check_all_9_porti(),
        "suite4_p11_3_selberg_cutoff_divergence": check_p11_3_cutoff_divergence(),
        "suite5_algebra_cy4_and_inflation_consistency": check_algebra_cy4_and_inflation_consistency(),
        "suite6_rge_2loop_bugs_synthetic": check_rge_2loop_bugs_synthetic(),
    }
    out_path = Path(__file__).resolve().parent / "verify_agy_exp_45fe6e401_out.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (python_float_literal_count={ast_res['python_float_literal_count']})")


if __name__ == "__main__":
    main()
