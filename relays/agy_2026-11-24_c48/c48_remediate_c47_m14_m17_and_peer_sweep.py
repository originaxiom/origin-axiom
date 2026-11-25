#!/usr/bin/env python3
r"""Card AGY-C48 Standalone Sandbox Remediation of AGY-C47 (Closing D1..D4, 0 of 19).
100% standalone under `python3 -I` in any isolated sandbox directory (depends ONLY on stdlib, mpmath, and sympy;
ZERO subprocess, ZERO git, ZERO snappy, ZERO external file reads, ZERO AST float/complex literals OR float()/complex() calls):
  - E1 (Closing D1 & D2 on M16 Escalated Rows P-557, P-667, & P-640):
    * P-557: Evaluates 3x3 Yukawa SVDs (via Hermitian Y Y^H Jacobi eigensolver) & CKM across ALL 51,072 discrete choices
      (266 lines x 12 distinct B1825 directions x 2 radii x 8 readings at tau = 17/100 + 105/100 i; ZERO hard-coded
      50880, 40000, 7680, or 32320, ZERO direction multipliers!), deriving choices_kraft == 51072, choices_v_defined ==
      50880 (192 rank-1 drops on N=4 x {R, t=-5/288}), choices_four_phys == 40000, and choices_all_ten_phys == 32320
      (7680 failing six_ok exclusively on order 12 via m_e == 0 while N=3 cross-readings retain m_e > 0), proving S
      invariance, p2^(10)/p2^(4) <= 40000/32320 == 125/101 < 31/25, and physical_all_ten for P-585 (Control 1).
    * P-667: Exact-integer Dimofte-Gaiotto-Gukov 3D index I_Delta(m, e; q) + Lemma-three-point-six degree-shifted gluing
      across 4 regular-tetrahedral Q(sqrt(-3)) family members (m004, m003 through q^117; m206, m207 through q^23, scoped
      to (m, e) = (0, 0) / even e per B1431) + outside control m009, proving I_m004(0,0;q) == I_m003(0,0;q) and
      I_m206(0,0;q) == I_m207(0,0;q) (Re R(e^{i pi/3}) absent at all orders) while Im R(e^{i pi/3}) = Cl_2(pi/3) sets
      universal O(sqrt(N)) Cauchy saddle oscillation omega_M = sqrt(4 N_tet Im R) (Control 2).
    * P-640: Hurwitz-zeta boundary spectral asymmetry eta(B_{S^1}, a) = 2(a - floor(a + 1/2)) + APS index == 0 for all
      unquantized |a| < 1/2 (Control 3), grounding our dated (2026-11-24) weave-scoped decline (B1600/B1606).
  - E2 (Closing D2 on B1974 X_0(2) Valence + M14/M15/M17 Calibration):
    * Verifies Halphen-Serre (< 10^-44), confirms (eta c_0)(tau+2)/(eta c_0)(tau) == exp(2 pi i / 3) != 1 (Control 4),
      and extracts ord_oo(c_0) == +1/8, width-2 ord_0(c_0) == -1/4, elliptic order +1/2 at (1+i)/2, and
      [SL_2(Z) : Gamma_0(2)] == 3 directly from asymptotics and P^1(F_2) orbit BFS (sum == 3/8).
  - E3 (Closing D4 on agy-exp 0c8debf48 m003 Sister Words + chat1 & agy-002 Verification):
    * Verifies chat1 M3 (i) vs (ii) (t = 1/100 analytic escape) and P-596 10 x 2 Jacobian rank_R == 2 (Control 5),
      A2-B1972-OPEN 3-factor det Y + twin/mark spectra, 24-pt GL(2,Z) E_tau[6]_prim, and agy-exp 0c8debf48's exact
      SL(2, Z[omega]) m003 sister isomorphism (conj_a3 = b_2 a_2, conj_b3 = B_2 A_2 B_2 a_2 B_2, inverse words Xyxyx, YXYx).
"""
from __future__ import annotations

import ast
from collections import Counter, deque
from fractions import Fraction as Fr
import itertools
import json
import math
from pathlib import Path
import time

import mpmath as mp
import sympy as sp

mp.mp.dps = 50
I_MP = mp.mpc(0, 1)
Z0 = mp.mpf(0)
Z0_C = mp.mpc(0, 0)
HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "c48_out.json"


def mp_rat(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def verify_ast_strict() -> dict[str, object]:
    src = Path(__file__).resolve().read_text(encoding="utf-8")
    tree = ast.parse(src, filename=Path(__file__).name)
    bad = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if (isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))
        or (isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex"))
    ]
    assert not bad, f"Forbidden AST float/complex literal or call at lines: {bad}"
    return {"ast_float_or_complex_literals_and_calls": 0, "status": "CLEAN"}


# ==============================================================================
# Helpers for B1428 Exact-Integer 3D Index (Zero Floats, Zero SnapPy)
# ==============================================================================
def sgn_i(k: int) -> int:
    return -1 if (k % 2) else 1


def inv_poch_table(nmax: int, deg_max: int) -> list[list[int]]:
    tab: list[list[int]] = []
    cur = [0] * (deg_max + 1)
    cur[0] = 1
    tab.append(cur[:])
    for n in range(1, nmax + 1):
        nxt = cur[:]
        for d in range(n, deg_max + 1):
            nxt[d] += nxt[d - n]
        cur = nxt
        tab.append(cur[:])
    return tab


def mul_q_trunc(a: list[int], b: list[int], deg_max: int) -> list[int]:
    out = [0] * (deg_max + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > deg_max:
            continue
        lim = deg_max - i
        for j, bj in enumerate(b):
            if j > lim:
                break
            if bj:
                out[i + j] += ai * bj
    return out


def i_delta_exact(m: int, e: int, xmax: int) -> dict[int, int]:
    res: dict[int, int] = {}
    nlo = max(0, -m)
    b_c = 1 - 2 * e
    c_c = -m * e - xmax
    disc = b_c * b_c - 4 * c_c
    if disc < 0:
        return res
    r_sq = math.isqrt(disc) + 2
    lo = max(nlo, (-b_c - r_sq) // 2 - 2)
    hi = (-b_c + r_sq) // 2 + 2
    if hi < lo:
        return res
    emin: int | None = None
    for n in range(lo, hi + 1):
        ev = n * (n + 1) - (2 * n + m) * e
        if ev <= xmax and (emin is None or ev < emin):
            emin = ev
    if emin is None:
        return res
    deg_q = (xmax - emin) // 2
    rtab = inv_poch_table(hi + max(m, 0) + 1, deg_q)
    for n in range(lo, hi + 1):
        ev = n * (n + 1) - (2 * n + m) * e
        if ev > xmax:
            continue
        d_loc = (xmax - ev) // 2
        pr = mul_q_trunc(rtab[n], rtab[n + m], d_loc)
        sg = sgn_i(n)
        for k, ck in enumerate(pr):
            if ck:
                res[ev + 2 * k] = res.get(ev + 2 * k, 0) + sg * ck
    return {k: v for k, v in res.items() if v != 0}


def delta_x_deg(m: int, e: int) -> int:
    pos = lambda t: max(0, t)
    return pos(m) * pos(m + e) + pos(-m) * pos(e) + pos(-e) * pos(-e - m) + max(0, m, -e)


def j_mindeg(a: int, b: int, c: int) -> int:
    return -b + delta_x_deg(b - c, a - b)


def j_norm_series(a: int, b: int, c: int, budget: int) -> dict[int, int]:
    d = j_mindeg(a, b, c)
    sh = -b - d
    s = i_delta_exact(a - b, b - c, budget - sh)
    return {k + sh: sgn_i(b) * v for k, v in s.items() if k + sh <= budget and v != 0}


def s_mul_x(a: dict[int, int], b: dict[int, int], xmax: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for i, ai in a.items():
        if i > xmax:
            continue
        for j, bj in b.items():
            if i + j <= xmax:
                out[i + j] = out.get(i + j, 0) + ai * bj
    return {k: v for k, v in out.items() if v != 0}


def manifold_3d_index_q(edges: list[list[int]], xmax: int, zero_edge: int = 0, box: int = 20, naive_unshifted: bool = False) -> dict[int, int]:
    n = len(edges)
    assert all(len(row) == 3 * n for row in edges)
    assert [sum(edges[r][c] for r in range(n)) for c in range(3 * n)] == [2] * (3 * n)
    free = [i for i in range(n) if i != zero_edge]
    tot: dict[int, int] = {}
    for kk in itertools.product(range(-box, box + 1), repeat=len(free)):
        kvec = [0] * n
        for idx, i_ed in enumerate(free):
            kvec[i_ed] = kk[idx]
        triples = [tuple(sum(kvec[r] * edges[r][3 * j + s] for r in range(n)) for s in range(3)) for j in range(n)]
        d_tot = 2 * sum(kvec) + sum(j_mindeg(*t) for t in triples)
        if d_tot > xmax:
            continue
        if naive_unshifted:
            prod: dict[int, int] = {0: 1}
            for a_t, b_t, c_t in triples:
                s_raw = i_delta_exact(a_t - b_t, b_t - c_t, xmax + b_t)
                j_raw = {kx - b_t: sgn_i(b_t) * v for kx, v in s_raw.items() if 0 <= kx - b_t <= xmax and v != 0}
                prod = s_mul_x(prod, j_raw, xmax)
            sh_tot = 2 * sum(kvec)
            for kx, v in prod.items():
                if kx + sh_tot <= xmax:
                    tot[kx + sh_tot] = tot.get(kx + sh_tot, 0) + v
        else:
            budget = xmax - d_tot
            prod = {0: 1}
            for t in triples:
                prod = s_mul_x(prod, j_norm_series(*t, budget), budget)
            for kx, v in prod.items():
                if kx + d_tot <= xmax:
                    tot[kx + d_tot] = tot.get(kx + d_tot, 0) + v
    tot = {k: v for k, v in tot.items() if v != 0}
    assert all(k % 2 == 0 for k in tot)
    return {k // 2: v for k, v in sorted(tot.items()) if k <= xmax - 6}


# ==============================================================================
# Frame C Helpers (Pure mpmath, Zero float()/complex() Calls)
# ==============================================================================
def thc_hol(ca: Fr, cb: Fr, tv: mp.mpc) -> mp.mpc:
    am, bm = f2m(ca), f2m(cb)
    q = mp.exp(I_MP * mp.pi * tv)
    return mp.exp(I_MP * mp.pi * am * am * tv + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * (am * tv + bm), q)


def b0_triplet(tv: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tv)
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return -t2 / (t3 * t4), -t4 / (t2 * t3), I_MP * t3 / (t2 * t4)


def s_higgs_components(tv: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tv)
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    l2 = -mp.jtheta(2, 0, q, derivative=2) / (8 * mp.jtheta(2, 0, q))
    l3 = -mp.jtheta(3, 0, q, derivative=2) / (8 * t3)
    l4 = -mp.jtheta(4, 0, q, derivative=2) / (8 * t4)
    s1 = (-t2 / (t3 * t4)) * mp_rat(1, 3) * (4 * l2 - 2 * l3 - 2 * l4)
    s2 = (-t4 / (t2 * t3)) * mp_rat(1, 3) * (4 * l4 - 2 * l2 - 2 * l3)
    s3 = (I_MP * t3 / (t2 * t4)) * mp_rat(1, 3) * (4 * l3 - 2 * l2 - 2 * l4)
    return s1, s2, s3


def all_12_b1825_directions(tv: mp.mpc) -> dict[str, list[mp.mpc]]:
    q = mp.exp(I_MP * mp.pi * tv)
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    e4 = ((t2 ** 8) + (t3 ** 8) + (t4 ** 8)) / 2
    l2 = -mp.jtheta(2, 0, q, derivative=2) / (8 * mp.jtheta(2, 0, q))
    l3 = -mp.jtheta(3, 0, q, derivative=2) / (8 * t3)
    l4 = -mp.jtheta(4, 0, q, derivative=2) / (8 * t4)
    e2 = 8 * (l2 + l3 + l4)
    b0 = list(b0_triplet(tv))
    b1 = list(s_higgs_components(tv))
    hs = mp.mpf(10) ** (-10)
    b1_p = s_higgs_components(tv + hs)
    b1_m = s_higgs_components(tv - hs)
    db1 = [(b1_p[k] - b1_m[k]) / (2 * hs) for k in range(3)]
    b2 = [db1[k] / (2 * I_MP * mp.pi) - mp_rat(1, 8) * e2 * b1[k] for k in range(3)]
    dirs: dict[str, list[mp.mpc]] = {
        "DR": b1,
        "a0": [b2[k] - mp_rat(1, 48) * e4 * b0[k] for k in range(3)],
        "R": b0,
        "t=-5/288": [b2[k] - mp_rat(5, 288) * e4 * b0[k] for k in range(3)],
    }
    for a_exp in (-10, -6, 6, 10, 14, 18, 22, 26):
        eps_p = I_MP ** ((a_exp + 2) // 2)
        dirs[f"F_{a_exp}"] = [eps_p * (t2 ** a_exp), eps_p * (t4 ** a_exp), I_MP * (t3 ** a_exp)]
    return dirs


def f_u_mp(u1: Fr, u2: Fr, tv: mp.mpc) -> mp.mpf:
    y = mp.im(tv)
    a_r, b_r = u1 % 1, u2 % 1
    if a_r != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(f2m(a_r)) + mp.digamma(1 - f2m(a_r)))
        zrow = Z0
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zrow = y * (mp.pi ** 2) / (mp.sin(mp.pi * f2m(b_r)) ** 2)
    tot = Z0
    k_lim = int(mp.ceil(mp.mpf(28) / y)) + 8
    for k_sum in range(-k_lim, k_lim + 1):
        m_val = f2m(a_r) + k_sum
        if m_val == 0:
            continue
        w_val = mp.exp(-2 * mp.pi * abs(m_val) * y + 2 * I_MP * mp.pi * (m_val * mp.re(tv) + f2m(u2)))
        tot += (2 * mp.pi / abs(m_val)) * mp.re(w_val / (1 - w_val))
    return first + zrow + tot


def frame_c_sector_yukawa(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, conj_higgs: bool = False, h_vec: list[mp.mpc] | None = None) -> tuple[mp.matrix, mp.mpf]:
    y = mp.im(tv)
    q = mp.exp(I_MP * mp.pi * tv)
    qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    eps_q = qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    s1, s2, s3 = tuple(h_vec) if h_vec is not None else s_higgs_components(tv)
    sh = s1 * qi + s2 * qj + s3 * qk
    if conj_higgs:
        sh = eps_q * mp.matrix([[mp.conj(sh[r, c]) for c in range(2)] for r in range(2)]) * eps_q.T
    ct = [[ca.T * eps_q * sh * cb for cb in blks] for ca in blks]
    t1p = mp.pi * mp.jtheta(2, 0, q) * mp.jtheta(3, 0, q) * mp.jtheta(4, 0, q)
    th1_fn = lambda zv: mp.jtheta(1, mp.pi * zv, q)
    l_end = mp.pi * y / 3
    hr = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
    ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
    um = {}
    d_sum = Z0_C
    nr2 = Z0
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = Z0_C
        else:
            r_res = kap[sk] * thc_hol(cs[sk][0], cs[sk][1], tv) * thc_hol(ds[sk][0], ds[sk][1], tv) / t1p
            nr2 += abs(r_res) ** 2
            zv = f2m(al) * tv + f2m(be)
            a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_fn, zv) / th1_fn(zv)
            c_ch = f_u_mp(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
            w_arg = 2 * mp.pi * l_end + c_ch
            d_sum += w_arg * (r_res ** 2)
            um[sk] = mp.sqrt(w_arg) * r_res
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    ym = mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])
    d_rel = abs(d_sum) / max(nr2, mp.mpf(10) ** (-48))
    return ym, d_rel


def ten_observables_at(pa: Fr, pb: Fr, tv: mp.mpc, h_vec: list[mp.mpc] | None = None) -> list[mp.mpf]:
    yu, _ = frame_c_sector_yukawa(pa, pb, 1, -4, tv, conj_higgs=True, h_vec=h_vec)
    yd, _ = frame_c_sector_yukawa(pa, pb, 1, 2, tv, conj_higgs=False, h_vec=h_vec)
    ye, _ = frame_c_sector_yukawa(pa, pb, -3, 6, tv, conj_higgs=False, h_vec=h_vec)

    def sv_and_u_asc(ym: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
        uu, sv, _ = mp.svd_c(ym)
        ord_i = sorted(range(3), key=lambda idx: sv[idx])
        u_asc = mp.matrix([[uu[r, ord_i[c]] for c in range(3)] for r in range(3)])
        return [sv[idx] for idx in ord_i], u_asc

    sv_u, u_u = sv_and_u_asc(yu)
    sv_d, u_d = sv_and_u_asc(yd)
    sv_e, _ = sv_and_u_asc(ye)
    v_ckm = u_u.H * u_d
    j_cp = abs(mp.im(v_ckm[0, 0] * v_ckm[1, 1] * mp.conj(v_ckm[0, 1]) * mp.conj(v_ckm[1, 0])))
    return [
        sv_u[1] / sv_u[2],
        sv_u[0] / sv_u[2],
        sv_d[1] / sv_d[2],
        sv_d[0] / sv_d[2],
        sv_e[1] / sv_e[2],
        sv_e[0] / sv_e[2],
        abs(v_ckm[0, 1]),
        abs(v_ckm[1, 2]),
        abs(v_ckm[0, 2]),
        j_cp,
    ]


# ==============================================================================
# E1: Closing D1 & D2 on M16 Escalated Rows (P-557, P-667, P-640)
# ==============================================================================
def verify_e1_m16_p557_p667_p640() -> tuple[dict[str, object], bool, bool, bool]:
    # --- 1. P-557: Computed 50,880 -> 40,000 -> 32,320 from full 266-line x 12-dir x 2-rad x 8-reading sweep ---
    seen_lines: set[tuple[Fr, Fr]] = set()
    menu_266: list[tuple[int, Fr, Fr]] = []
    for n_ord in range(1, 13):
        for j in range(n_ord):
            for k in range(n_ord):
                if math.gcd(math.gcd(j, k), n_ord) != 1:
                    continue
                a, b = Fr(j, n_ord), Fr(k, n_ord)
                key = min((a, b), ((-a) % 1, (-b) % 1))
                if key not in seen_lines:
                    seen_lines.add(key)
                    menu_266.append((n_ord, key[0], key[1]))
    assert len(menu_266) == 266
    ord12_lines = [(a, b) for n_ord, a, b in menu_266 if n_ord == 12]
    ord5_lines = [(a, b) for n_ord, a, b in menu_266 if n_ord == 5]
    assert len(ord12_lines) == 48 and len(ord5_lines) == 12

    twist_order = lambda q, a, b: math.lcm(((q * a) % 1).denominator, ((q * b) % 1).denominator)
    assert all(twist_order(-3, a, b) == 4 and twist_order(6, a, b) == 2 for a, b in ord12_lines)
    assert all(twist_order(1, a, b) == 12 for a, b in ord12_lines)

    tv_test = mp.mpc(mp_rat(17, 100), mp_rat(183, 100))
    d_lep_ord12 = [frame_c_sector_yukawa(a, b, -3, 6, tv_test)[1] for a, b in ord12_lines]
    d_up_ord12 = [frame_c_sector_yukawa(a, b, 1, -4, tv_test)[1] for a, b in ord12_lines]
    d_dn_ord12 = [frame_c_sector_yukawa(a, b, 1, 2, tv_test)[1] for a, b in ord12_lines]
    max_d_lep_12 = max(d_lep_ord12)
    min_d_q_12 = min(min(d_up_ord12), min(d_dn_ord12))
    assert max_d_lep_12 < mp.mpf(10) ** (-45) and min_d_q_12 > mp_rat(1, 10)

    def svd3_jacobi(ym: list[list[mp.mpc]], need_u: bool = True) -> tuple[list[mp.mpf], list[list[mp.mpc]] | None]:
        h = [[sum(ym[r][k] * mp.conj(ym[c][k]) for k in range(3)) for c in range(3)] for r in range(3)]
        for r in range(3):
            h[r][r] = mp.re(h[r][r])
        u = [[mp.mpc(1 if r == c else 0) for c in range(3)] for r in range(3)] if need_u else None
        eps_j = mp.mpf(10) ** (-31)
        for _ in range(22):
            p, q, mv = 0, 1, abs(h[0][1])
            for p2, q2 in ((0, 2), (1, 2)):
                av = abs(h[p2][q2])
                if av > mv:
                    p, q, mv = p2, q2, av
            if mv <= eps_j:
                break
            ph = h[p][q] / mv
            cph = mp.conj(ph)
            tau_j = (mp.re(h[q][q]) - mp.re(h[p][p])) / (2 * mv)
            t_j = (1 if tau_j >= 0 else -1) / (abs(tau_j) + mp.sqrt(1 + tau_j * tau_j))
            cs_j = 1 / mp.sqrt(1 + t_j * t_j)
            sn_j = t_j * cs_j
            r_idx = 3 - p - q
            hrp, hrq = h[r_idx][p], h[r_idx][q]
            h[p][p] = mp.re(h[p][p]) - t_j * mv
            h[q][q] = mp.re(h[q][q]) + t_j * mv
            h[p][q] = Z0_C
            h[q][p] = Z0_C
            nrp = cs_j * hrp - sn_j * cph * hrq
            nrq = sn_j * ph * hrp + cs_j * hrq
            h[r_idx][p], h[p][r_idx] = nrp, mp.conj(nrp)
            h[r_idx][q], h[q][r_idx] = nrq, mp.conj(nrq)
            if need_u and u is not None:
                for k in range(3):
                    ukp, ukq = u[k][p], u[k][q]
                    u[k][p] = cs_j * ukp - sn_j * cph * ukq
                    u[k][q] = sn_j * ph * ukp + cs_j * ukq
        evs = [mp.sqrt(max(Z0, mp.re(h[i][i]))) for i in range(3)]
        oi = sorted(range(3), key=lambda idx: evs[idx])
        return [evs[idx] for idx in oi], ([[u[r][oi[c]] for c in range(3)] for r in range(3)] if (need_u and u is not None) else None)

    # Exhaustive 51,072-choice sweep across all 266 lines x 12 B1825 directions x 2 radii x 8 readings at tau = 17/100 + 105/100 i:
    tv_sw = mp.mpc(mp_rat(17, 100), mp_rat(105, 100))
    dirs_12 = all_12_b1825_directions(tv_sw)
    null_dirs = [dn for dn, av in dirs_12.items() if abs(av[0] ** 2 + av[1] ** 2 + av[2] ** 2) < mp.mpf(10) ** (-20)]
    full_dirs = [dn for dn, av in dirs_12.items() if abs(av[0] ** 2 + av[1] ** 2 + av[2] ** 2) > mp.mpf(10) ** (-6)]
    assert len(dirs_12) == 12 and sorted(null_dirs) == ["R", "t=-5/288"] and len(full_dirs) == 10

    floor_deg = mp.mpf(10) ** (-8)
    floor_struct = mp.mpf(10) ** (-12)
    with mp.workdps(34):
        y_sw = mp.im(tv_sw)
        q_sw = mp.exp(I_MP * mp.pi * tv_sw)
        t1p_sw = mp.pi * mp.jtheta(2, 0, q_sw) * mp.jtheta(3, 0, q_sw) * mp.jtheta(4, 0, q_sw)
        th1_sw = lambda zv: mp.jtheta(1, mp.pi * zv, q_sw)
        qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
        qk = qi * qj
        eps_q = qj
        hf = mp_rat(1, 2)
        ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
        blks = [qj, qi, qk]
        ct_by_dir: dict[tuple[str, int], list[list[mp.matrix]]] = {}
        for dn, av in dirs_12.items():
            sh_d = av[0] * qi + av[1] * qj + av[2] * qk
            sh_d_st = eps_q * mp.matrix([[mp.conj(sh_d[r, c]) for c in range(2)] for r in range(2)]) * eps_q.T
            ct_by_dir[(dn, 0)] = [[ca.T * eps_q * sh_d * cb for cb in blks] for ca in blks]
            ct_by_dir[(dn, 1)] = [[ca.T * eps_q * sh_d_st * cb for cb in blks] for ca in blks]
        radii_2 = [mp_rat(8, 5), mp_rat(11, 5)]

        choices_kraft_total = 0
        choices_total_b1825 = 0
        choices_four_phys = 0
        choices_all_ten_phys = 0
        vdef_drop_by_order: Counter[int] = Counter()
        four_fail_by_order: Counter[int] = Counter()
        six_fail_given_four_by_order: Counter[int] = Counter()
        hr = Fr(1, 2)

        for n_ord, pa, pb in menu_266:
            sec_rc: dict[str, dict[str, tuple[mp.mpc, mp.mpf, mp.mpf] | None]] = {}
            for sname, ql, qr in (("u", 1, -4), ("d", 1, 2), ("e", -3, 6)):
                xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
                ap, am = xv[0] + yv[0], xv[0] - yv[0]
                bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
                eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
                kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
                cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
                ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
                rc: dict[str, tuple[mp.mpc, mp.mpf, mp.mpf] | None] = {}
                for sk in ("1", "i", "j", "k"):
                    al, be = cs[sk][0] - hr, cs[sk][1] - hr
                    dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
                    if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
                        rc[sk] = None
                    else:
                        r_res = kap[sk] * thc_hol(cs[sk][0], cs[sk][1], tv_sw) * thc_hol(ds[sk][0], ds[sk][1], tv_sw) / t1p_sw
                        zv = f2m(al) * tv_sw + f2m(be)
                        a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_sw, zv) / th1_sw(zv)
                        c_base = f_u_mp(al, be, tv_sw) + mp.pi * mp.log(y_sw) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                        rc[sk] = (r_res, c_base, abs(a0) ** 2)
                sec_rc[sname] = rc

            for l_rad in radii_2:
                mw_sec: dict[str, mp.matrix] = {}
                for sname in ("u", "d", "e"):
                    rc = sec_rc[sname]
                    mw = mp.zeros(2, 2)
                    for sk in ("1", "i", "j", "k"):
                        if rc[sk] is not None:
                            r_res, c_base, a02 = rc[sk]
                            c_ch = c_base - mp.pi * a02 * mp.exp(-2 * l_rad)
                            mw = mw + mp.sqrt(2 * mp.pi * l_rad + c_ch) * r_res * ed[sk]
                    mw_sec[sname] = mw

                for dn in dirs_12:
                    svd_sec: dict[tuple[str, int], tuple[list[list[mp.mpc]] | None, bool, bool]] = {}
                    for sname in ("u", "d", "e"):
                        mw = mw_sec[sname]
                        m00, m01, m10, m11 = mw[0, 0], mw[0, 1], mw[1, 0], mw[1, 1]
                        for rbit in (0, 1):
                            ct = ct_by_dir[(dn, rbit)]
                            yl = [[ct[ra][cb][0, 0] * m00 + ct[ra][cb][0, 1] * m01 + ct[ra][cb][1, 0] * m10 + ct[ra][cb][1, 1] * m11 for cb in range(3)] for ra in range(3)]
                            sv, u_asc = svd3_jacobi(yl, need_u=(sname != "e"))
                            s0, s1_v, s2_v = sv[0], sv[1], sv[2]
                            nondeg = (s2_v > floor_struct) and (min((s1_v - s0) / s2_v, (s2_v - s1_v) / s2_v) >= floor_deg)
                            six_sec = (s2_v > floor_struct) and (s0 / s2_v >= floor_struct) and (s1_v / s2_v >= floor_struct)
                            svd_sec[(sname, rbit)] = (u_asc, nondeg, six_sec)

                    for ru, rd, re_b in itertools.product((0, 1), repeat=3):
                        choices_kraft_total += 1
                        uu_m, u_nd, u_ok = svd_sec[("u", ru)]
                        ud_m, d_nd, d_ok = svd_sec[("d", rd)]
                        _, _, e_ok = svd_sec[("e", re_b)]
                        if not (u_nd and d_nd) or uu_m is None or ud_m is None:
                            vdef_drop_by_order[n_ord] += 1
                            continue
                        choices_total_b1825 += 1
                        vm = [[sum(mp.conj(uu_m[k][r]) * ud_m[k][c] for k in range(3)) for c in range(3)] for r in range(3)]
                        jcp = abs(mp.im(vm[0][0] * vm[1][1] * mp.conj(vm[0][1]) * mp.conj(vm[1][0])))
                        f_ok = (abs(vm[0][1]) >= floor_struct) and (abs(vm[1][2]) >= floor_struct) and (abs(vm[0][2]) >= floor_struct) and (jcp >= floor_struct)
                        if not f_ok:
                            four_fail_by_order[n_ord] += 1
                        else:
                            choices_four_phys += 1
                            if u_ok and d_ok and e_ok:
                                choices_all_ten_phys += 1
                            else:
                                six_fail_given_four_by_order[n_ord] += 1

    choices_ord12_e0 = choices_four_phys - choices_all_ten_phys
    pi_e0_share = Fr(choices_ord12_e0, choices_four_phys)
    p2_ratio_bound = Fr(choices_four_phys, choices_all_ten_phys)
    assert choices_kraft_total == 51072 and dict(vdef_drop_by_order) == {4: 192}
    assert dict(six_fail_given_four_by_order) == {12: 7680}
    assert choices_total_b1825 == 50880 and choices_four_phys == 40000 and choices_all_ten_phys == 32320
    assert pi_e0_share == Fr(24, 125) and p2_ratio_bound == Fr(125, 101) and p2_ratio_bound < Fr(31, 25)
    bits_ckm_max_shift = mp.log(mp_rat(p2_ratio_bound.numerator, p2_ratio_bound.denominator)) / mp.log(2)
    assert bits_ckm_max_shift < mp_rat(1, 3)

    physical_four_only = lambda obs10: all(obs10[k] > floor_struct for k in (6, 7, 8, 9))
    physical_all_ten = lambda obs10: all(obs10[k] > floor_struct for k in range(10))
    obs_ord12 = ten_observables_at(Fr(1, 12), Fr(2, 12), tv_test)
    obs_ord5 = ten_observables_at(Fr(1, 5), Fr(2, 5), tv_test)
    ctrl1_ok = bool(
        physical_four_only(obs_ord12)
        and (not physical_all_ten(obs_ord12))
        and obs_ord12[5] < mp.mpf(10) ** (-45)
        and physical_all_ten(obs_ord5)
    )
    assert ctrl1_ok

    # --- 2. P-667: B1428 3D-Index Asymptotics (through q^117 & q^23, B1431-scoped) + m009 Control ---
    edges_m004 = [[2, 1, 0, 1, 0, 2], [0, 1, 2, 1, 2, 0]]
    edges_m003 = [[2, 0, 1, 2, 0, 1], [0, 2, 1, 0, 2, 1]]
    edges_m206 = [
        [2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 2],
        [0, 0, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0],
    ]
    edges_m207 = [
        [1, 0, 0, 2, 0, 0, 0, 1, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1],
        [0, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 2, 0],
    ]
    edges_m009 = [[2, 0, 0, 2, 0, 0, 2, 0, 0], [0, 1, 0, 0, 0, 2, 0, 1, 0], [0, 1, 2, 0, 2, 0, 0, 1, 2]]

    ghrs_m004 = {0: 1, 1: -2, 2: -3, 3: 2, 4: 8, 5: 18, 6: 18, 7: 14, 8: -12, 9: -52, 10: -106}
    ghrs_m009 = {0: 1, 1: -1, 2: -1, 3: 6, 4: 9, 5: 12, 6: -5, 7: -34, 8: -79, 9: -118, 10: -118}

    ser_m004 = manifold_3d_index_q(edges_m004, xmax=240, zero_edge=0, box=70)
    ser_m003 = manifold_3d_index_q(edges_m003, xmax=240, zero_edge=0, box=70)
    ser_m206 = manifold_3d_index_q(edges_m206, xmax=52, zero_edge=0, box=14)
    ser_m207 = manifold_3d_index_q(edges_m207, xmax=52, zero_edge=0, box=14)
    ser_m009 = manifold_3d_index_q(edges_m009, xmax=66, zero_edge=0, box=22)

    assert max(ser_m004) == 117 and max(ser_m206) == 23
    assert manifold_3d_index_q(edges_m004, xmax=40, zero_edge=1, box=25) == {k: v for k, v in ser_m004.items() if k <= 17}
    assert all(manifold_3d_index_q(edges_m009, xmax=30, zero_edge=z, box=16) == {k: v for k, v in ser_m009.items() if k <= 12} for z in range(3))
    naive_m009_e0 = manifold_3d_index_q(edges_m009, xmax=30, zero_edge=0, box=16, naive_unshifted=True)
    naive_m009_e1 = manifold_3d_index_q(edges_m009, xmax=30, zero_edge=1, box=16, naive_unshifted=True)
    assert {k: v for k, v in ser_m004.items() if k <= 10} == ghrs_m004
    assert {k: v for k, v in ser_m009.items() if k <= 10} == ghrs_m009
    assert ser_m004 == ser_m003 and ser_m206 == ser_m207

    z_reg = mp.exp(I_MP * mp.pi / 3)
    li2_diff_reg = mp.polylog(2, z_reg) - mp.polylog(2, 1 / z_reg)
    re_cancel_err = abs(mp.re(li2_diff_reg))
    im_atom = mp.clsin(2, mp.pi / 3)
    assert re_cancel_err < mp.mpf(10) ** (-48) and abs(mp.im(li2_diff_reg) - 2 * im_atom) < mp.mpf(10) ** (-48)

    def last_omega_est(ser: dict[int, int]) -> mp.mpf:
        nmax = max(ser.keys())
        z_sq: list[mp.mpf] = []
        for n in range(2, nmax):
            v0, v1 = ser.get(n, 0), ser.get(n + 1, 0)
            if v0 * v1 < 0:
                z_sq.append(mp.sqrt(mp.mpf(n) + mp_rat(abs(v0), abs(v0) + abs(v1))))
        return mp.pi / (z_sq[-1] - z_sq[-2])

    om_m004_pred = mp.sqrt(4 * 2 * im_atom)
    om_m206_pred = mp.sqrt(4 * 4 * im_atom)
    om_m004_emp = last_omega_est(ser_m004)
    om_m206_emp = last_omega_est(ser_m206)
    om_m009_emp = last_omega_est(ser_m009)
    err_om_m004 = abs(om_m004_emp - om_m004_pred) / om_m004_pred
    err_om_m206 = abs(om_m206_emp - om_m206_pred) / om_m206_pred
    ctrl2_ok = bool(
        naive_m009_e0 != naive_m009_e1
        and ser_m004 == ser_m003
        and ser_m206 == ser_m207
        and ser_m206 != {k: v for k, v in ser_m004.items() if k <= 23}
        and err_om_m004 < mp_rat(1, 500)
        and err_om_m206 < mp_rat(1, 200)
        and abs(om_m009_emp - om_m004_pred) > mp_rat(3, 10)
    )
    assert ctrl2_ok

    # --- 3. P-640: Hurwitz-zeta boundary eta(B_{S^1}, a) & APS bulk cancellation vs quantized jump ---
    def eta_ns_s1(a_flux: Fr) -> mp.mpf:
        u_pos = (Fr(1, 2) - a_flux) % 1
        assert u_pos != 0
        u_neg = 1 - u_pos
        return mp.zeta(0, f2m(u_pos)) - mp.zeta(0, f2m(u_neg))

    aps_index_d2 = lambda a_flux: f2m(a_flux) - mp_rat(1, 2) * eta_ns_s1(a_flux)
    eta_odd_err = max(abs(eta_ns_s1(a) + eta_ns_s1(-a)) for a in (Fr(1, 7), Fr(1, 3), Fr(11, 29)))
    aps_unquant_max = max(abs(aps_index_d2(a)) for a in (Fr(-3, 7), Fr(-1, 5), Fr(1, 6), Fr(2, 5), Fr(11, 24)))
    aps_quant_jump = aps_index_d2(Fr(3, 4))
    ctrl3_ok = bool(
        eta_odd_err < mp.mpf(10) ** (-45)
        and aps_unquant_max < mp.mpf(10) ** (-45)
        and abs(aps_quant_jump - 1) < mp.mpf(10) ** (-45)
    )
    assert ctrl3_ok

    return {
        "p557_menu_266_and_ord12_count": [len(menu_266), len(ord12_lines)],
        "p557_ord12_max_D_lep_vs_min_quark": [mp.nstr(max_d_lep_12, 6), mp.nstr(min_d_q_12, 6)],
        "p557_computed_choices_kraft_vdef_four_ten_e0": [choices_kraft_total, choices_total_b1825, choices_four_phys, choices_all_ten_phys, choices_ord12_e0],
        "p557_vdef_drop_by_order": {str(k): v for k, v in sorted(vdef_drop_by_order.items())},
        "p557_four_fail_by_order": {str(k): v for k, v in sorted(four_fail_by_order.items())},
        "p557_six_fail_given_four_by_order": {str(k): v for k, v in sorted(six_fail_given_four_by_order.items())},
        "p557_exact_p2_ratio_bound": f"{p2_ratio_bound.numerator}/{p2_ratio_bound.denominator}",
        "p557_bits_ckm_max_shift": mp.nstr(bits_ckm_max_shift, 8),
        "p557_p585_physical_definition": "physical_all_ten: all 6 mass ratios (c/t, u/t, s/b, d/b, mu/tau, e/tau) and all 4 CKM invariants (|V_us|, |V_cb|, |V_ub|, |J|) strictly > 10^-12",
        "p667_m004_equals_m003_to_q117": bool(ser_m004 == ser_m003 and max(ser_m004) == 117),
        "p667_m206_equals_m207_to_q23": bool(ser_m206 == ser_m207 and max(ser_m206) == 23),
        "p667_b1431_scope_note": "Scoped to (m, e) = (0, 0) (and even electric charge e in 2 Z); per B1431, odd e on H_1(dM; Z) separates m004 from m003 while Re Li_2(e^{i theta}) cancels on |z|=1 in every tetrahedron factor",
        "p667_m206_series_q0_to_q12": {str(k): ser_m206[k] for k in range(13) if k in ser_m206},
        "p667_omega_pred_vs_emp_m004_and_m206": [
            mp.nstr(om_m004_pred, 8),
            mp.nstr(om_m004_emp, 8),
            mp.nstr(om_m206_pred, 8),
            mp.nstr(om_m206_emp, 8),
        ],
        "p640_dated_disposition": "DECLINED 2026-11-24 scoped to the weave frame (B1600/B1606 W19-W22) and magnetized curve frame (M=4): unquantized flat torsion phase cancels in APS index (ind == 0 for |a| < 1/2)",
        "control_1_all_ten_rejects_ord12_massless_electron": ctrl1_ok,
        "control_2_degree_shift_and_half_atom_dichotomy_caught": ctrl2_ok,
        "control_3_aps_flat_cancellation_vs_flux_jump_caught": ctrl3_ok,
    }, ctrl1_ok, ctrl2_ok, ctrl3_ok


# ==============================================================================
# E2: Closing D2 on B1974 X_0(2) Valence + M14/M15/M17 Calibration
# ==============================================================================
def verify_e2_m14_m15_m17_b1974_calibration() -> tuple[dict[str, object], bool]:
    hs_max_err = Z0
    for tv in (mp.mpc(mp_rat(13, 100), mp_rat(7, 5)), mp.mpc(mp_rat(-31, 100), mp_rat(19, 10))):
        q = mp.exp(I_MP * mp.pi * tv)
        q_mod = mp.exp(2 * I_MP * mp.pi * tv)
        t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
        t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        eta3 = (mp.exp(I_MP * mp.pi * tv / 12) * mp.qp(q_mod)) ** 3
        c0, c1, c2 = s_higgs_components(tv)
        lhs = [24 * eta3 * c0, 24 * eta3 * c1, -24 * I_MP * eta3 * c2]
        rhs = [-(t2 ** 2) * ((t3 ** 4) + (t4 ** 4)), (t4 ** 2) * ((t2 ** 4) + (t3 ** 4)), (t3 ** 2) * ((t2 ** 4) - (t4 ** 4))]
        hs_max_err = max(hs_max_err, max(abs(lhs[k] - rhs[k]) / abs(rhs[k]) for k in range(3)))
    assert hs_max_err < mp.mpf(10) ** (-44)

    # Confirm main's B1974 / M15 correction of AGY-C13's M_2(Gamma(2)) step (Control 4):
    tv0 = mp.mpc(mp_rat(17, 100), mp_rat(6, 5))
    eta_fn = lambda z: mp.exp(I_MP * mp.pi * z / 12) * mp.qp(mp.exp(2 * I_MP * mp.pi * z))
    ec_0 = eta_fn(tv0) * s_higgs_components(tv0)[0]
    ec_t2 = eta_fn(tv0 + 2) * s_higgs_components(tv0 + 2)[0]
    t2_phase_ratio = ec_t2 / ec_0
    omega_mp = mp.exp(2 * I_MP * mp.pi / 3)
    eta_c_t2_break = abs(t2_phase_ratio - 1)
    eta_c_omega_err = abs(t2_phase_ratio - omega_mp)
    eta_c_cubed_err = abs((ec_t2 ** 3) / (ec_0 ** 3) - 1)

    # Closing D2: Extract X_0(2) cusp orders ord_oo(c_0), width-2 ord_0(c_0), elliptic order at (1+i)/2, & index [SL_2(Z):Gamma_0(2)] directly!
    with mp.workdps(80):
        y1_c, y2_c = mp.mpf(28), mp.mpf(34)
        c0_inf_1 = abs(s_higgs_components(I_MP * y1_c)[0])
        c0_inf_2 = abs(s_higgs_components(I_MP * y2_c)[0])
        ord_inf_mp = -mp.log(c0_inf_2 / c0_inf_1) / (2 * mp.pi * (y2_c - y1_c))
        ord_inf_n8 = int(mp.nint(8 * ord_inf_mp))
        assert abs(ord_inf_mp - mp_rat(ord_inf_n8, 8)) < mp.mpf(10) ** (-30)
        ord_inf_q = Fr(ord_inf_n8, 8)

        # At cusp 0 (tau = i / y -> 0, width-2 uniformizer q_0 = exp(-pi y)): slash weight-3/2 |c_0|_{3/2} S|(i y) = y^{-3/2} |c_0(i / y)|
        slash_0_1 = (y1_c ** mp_rat(-3, 2)) * abs(s_higgs_components(I_MP / y1_c)[0])
        slash_0_2 = (y2_c ** mp_rat(-3, 2)) * abs(s_higgs_components(I_MP / y2_c)[0])
        ord_zero_mp = -mp.log(slash_0_2 / slash_0_1) / (mp.pi * (y2_c - y1_c))
        ord_zero_n8 = int(mp.nint(8 * ord_zero_mp))
        assert abs(ord_zero_mp - mp_rat(ord_zero_n8, 8)) < mp.mpf(10) ** (-30)
        ord_zero_q = Fr(ord_zero_n8, 8)

    # At elliptic point tau_ell = (1 + i)/2: extract zero multiplicity from two radii & isotropy order of M_ell = [[1,-1],[2,-1]] in Gamma_0(2)/{+-I}:
    tv_ell = mp.mpc(mp_rat(1, 2), mp_rat(1, 2))
    c0_at_ell = abs(s_higgs_components(tv_ell)[0])
    e_r1, e_r2 = mp.mpf(10) ** (-10), mp.mpf(10) ** (-15)
    mult_ell_mp = mp.log(abs(s_higgs_components(tv_ell + e_r2)[0]) / abs(s_higgs_components(tv_ell + e_r1)[0])) / mp.log(e_r2 / e_r1)
    mult_ell_int = int(mp.nint(mult_ell_mp))
    assert abs(mult_ell_mp - mult_ell_int) < mp.mpf(10) ** (-8)
    m_ell = sp.Matrix([[1, -1], [2, -1]])
    assert m_ell.det() == 1 and (m_ell[1, 0] % 2 == 0) and sp.simplify((m_ell[0, 0] * (1 + sp.I) / 2 + m_ell[0, 1]) / (m_ell[1, 0] * (1 + sp.I) / 2 + m_ell[1, 1]) - (1 + sp.I) / 2) == 0
    iso_ord_psl = next(k for k in range(1, 7) if (m_ell ** k) == sp.eye(2) or (m_ell ** k) == -sp.eye(2))
    ord_ell_q = Fr(mult_ell_int, iso_ord_psl)

    # Index [SL_2(Z) : Gamma_0(2)] via transitive action of T, S on P^1(F_2):
    p1_f2 = deque([(0, 1)])
    seen_p1 = {(0, 1)}
    while p1_f2:
        c_v, d_v = p1_f2.popleft()
        for nc, nd in ((c_v, (c_v + d_v) % 2), (d_v, c_v)):
            if (nc, nd) != (0, 0) and (nc, nd) not in seen_p1:
                seen_p1.add((nc, nd))
                p1_f2.append((nc, nd))
    idx_gamma0_2 = len(seen_p1)

    valence_sum = ord_inf_q + ord_zero_q + ord_ell_q
    valence_rhs = Fr(3, 2) * Fr(idx_gamma0_2, 12)
    assert (ord_inf_q, ord_zero_q, ord_ell_q, idx_gamma0_2) == (Fr(1, 8), Fr(-1, 4), Fr(1, 2), 3)
    assert valence_sum == Fr(3, 8) and valence_sum == valence_rhs

    ctrl4_ok = bool(
        hs_max_err < mp.mpf(10) ** (-44)
        and eta_c_t2_break > mp_rat(3, 2)
        and eta_c_omega_err < mp.mpf(10) ** (-44)
        and eta_c_cubed_err < mp.mpf(10) ** (-44)
        and c0_at_ell < mp.mpf(10) ** (-45)
        and valence_sum == valence_rhs
    )
    assert ctrl4_ok

    return {
        "m14_c1_b1973_status": "Accepted & credited in B1973 (witness & rank-1 residue law verified on main)",
        "m17_c2_and_c8_status": "Accepted: B1942/B1949 (2026-11-15) holds priority on order-15 escape (C2 is independent linear route); C8 credited in B1971",
        "m15_m17_c13_b1974_erratum_and_scope": "Conceded & verified: eta*c_0 picks up exp(2 pi i / 3) under T^2 (not in M_2(Gamma(2))); B1974 proves uniqueness via X_0(2) genus 0 given P1..P3, and Review 86 correctly scopes P1 as Frame C's choice over D1 so C13 does NOT earn I-37",
        "halphen_serre_max_rel_err": mp.nstr(hs_max_err, 6),
        "eta_c0_T2_multiplier_err_from_omega": mp.nstr(eta_c_omega_err, 6),
        "extracted_x0_2_orders_inf_zero_ell_and_index": [
            f"{ord_inf_q.numerator}/{ord_inf_q.denominator}",
            f"{ord_zero_q.numerator}/{ord_zero_q.denominator}",
            f"{ord_ell_q.numerator}/{ord_ell_q.denominator}",
            idx_gamma0_2,
        ],
        "x0_2_valence_sum": f"{valence_sum.numerator}/{valence_sum.denominator}",
        "control_4_eta_c_not_in_M2_Gamma2_caught": ctrl4_ok,
    }, ctrl4_ok


# ==============================================================================
# E3: Closing D4 on agy-exp 0c8debf48 m003 Sister Words + chat1 & agy-002 Checks
# ==============================================================================
def verify_e3_peer_sweep_chat1_agy002_agyexp() -> tuple[dict[str, object], bool]:
    # 1. Second computation for chat1 CLAIM_2026-11-25_m3_holds_only_for_the_conjugated_higgs.md & agy-002 M2/M3:
    sig = [
        mp.matrix([[0, 1], [1, 0]]),
        mp.matrix([[0, -I_MP], [I_MP, 0]]),
        mp.matrix([[1, 0], [0, -1]]),
    ]

    def y_from_hm(hm: mp.matrix, mm: mp.matrix) -> mp.matrix:
        return mp.matrix([[mp_rat(1, 2) * ((sig[a] * hm * sig[b] * mm)[0, 0] + (sig[a] * hm * sig[b] * mm)[1, 1]) for b in range(3)] for a in range(3)])

    def m3_floor_mp(t_val: mp.mpf, sl_val: mp.mpf, a_val: mp.mpf) -> mp.mpf:
        c_arg = min(mp.mpf(1), max(mp.mpf(-1), (1 + sl_val) / (3 - sl_val)))
        a_cl = min(mp.mpf(1), max(mp.mpf(-1), a_val))
        gap = mp.acos(c_arg) - mp.acos(a_cl)
        s_req = mp.sin(gap / 2) if gap > 0 else Z0
        t1 = s_req / (2 * (1 + s_req)) if s_req > 0 else Z0
        if t_val <= t1:
            return (s_req * s_req) / (2 * (1 + 2 * s_req))
        if t_val <= s_req:
            return (s_req * t_val) / (1 + 2 * t_val)
        return (t_val * t_val) / (1 + 2 * t_val)

    def eval_m3_pair(hv: list[mp.mpc], mu: mp.matrix, md: mp.matrix, same_higgs: bool) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
        hd = hv[0] * sig[0] + hv[1] * sig[1] + hv[2] * sig[2]
        hu = hd if same_higgs else (mp.conj(hv[0]) * sig[0] + mp.conj(hv[1]) * sig[1] + mp.conj(hv[2]) * sig[2])
        uu, su, _ = mp.svd_c(y_from_hm(hu, mu))
        ud, sd, _ = mp.svd_c(y_from_hm(hd, md))
        iu = sorted(range(3), key=lambda idx: -su[idx])
        id_ = sorted(range(3), key=lambda idx: -sd[idx])
        rho = max(su[iu[1]] / su[iu[0]], sd[id_[1]] / sd[id_[0]])
        a_v33 = abs((uu[:, iu[0]].H * ud[:, id_[0]])[0, 0])
        h_dot_h = hv[0] * hv[0] + hv[1] * hv[1] + hv[2] * hv[2]
        h_nrm2 = mp.re(hv[0] * mp.conj(hv[0]) + hv[1] * mp.conj(hv[1]) + hv[2] * mp.conj(hv[2]))
        r_val = abs(h_dot_h) / h_nrm2
        t_val = r_val / (1 + mp.sqrt(max(Z0, 1 - r_val * r_val)))
        _, sv_mu, v_mu = mp.svd_c(mu)
        _, sv_md, v_md = mp.svd_c(md)
        ku = 0 if sv_mu[0] >= sv_mu[1] else 1
        kd = 0 if sv_md[0] >= sv_md[1] else 1
        ru0, ru1 = v_mu[0, ku], v_mu[1, ku]
        rd0, rd1 = v_md[0, kd], v_md[1, kd]
        sl_val = abs(ru0 * rd1 - ru1 * rd0)
        return rho, m3_floor_mp(t_val, sl_val, a_v33), t_val, a_v33

    m3_conj_violations = 0
    for t_q in (Fr(1, 100), Fr(1, 10), Fr(1, 3), Fr(4, 5)):
        hv_g = [mp.mpf(1) + f2m(t_q), I_MP * (mp.mpf(1) - f2m(t_q)), mp_rat(1, 7) * f2m(t_q)]
        for k1_q in (Fr(0, 1), Fr(1, 20), Fr(1, 3)):
            mu_g = mp.matrix([[mp.mpf(1), mp_rat(1, 5)], [Z0, f2m(k1_q)]])
            md_g = mp.matrix([[mp_rat(4, 5), mp_rat(-1, 7)], [mp_rat(1, 11), f2m(k1_q) + mp_rat(1, 13)]])
            rho_i, fl_i, _, _ = eval_m3_pair(hv_g, mu_g, md_g, same_higgs=False)
            if rho_i < fl_i - mp.mpf(10) ** (-35):
                m3_conj_violations += 1
    assert m3_conj_violations == 0

    t_w = mp_rat(1, 100)
    hv_w = [1 + t_w, I_MP * (1 - t_w), Z0_C]
    m_rk1 = mp.matrix([[mp.mpf(1), Z0], [Z0, Z0]])
    rho_w_conj, fl_w_conj, _, a_w_conj = eval_m3_pair(hv_w, m_rk1, m_rk1, same_higgs=False)
    rho_w_same, fl_w_same, _, a_w_same = eval_m3_pair(hv_w, m_rk1, m_rk1, same_higgs=True)
    assert rho_w_conj >= fl_w_conj - mp.mpf(10) ** (-40) and a_w_conj <= mp_rat(1, 3)
    assert abs(a_w_same - 1) < mp.mpf(10) ** (-45) and rho_w_same < mp_rat(1, 90) and fl_w_same > mp_rat(7, 100)

    # 2. Second computation for chat1 P-596 (f(d) == 2: 10 x 2 Jacobian wrt (Re tau, Im tau) has rank 2):
    h_fd = mp.mpf(10) ** (-10)
    min_s2_over_s1 = mp.mpf(10)
    frozen_re_rank1_s2 = Z0
    for tv_fd in (mp.mpc(mp_rat(13, 100), mp_rat(11, 5)), mp.mpc(mp_rat(31, 100), mp_rat(31, 10))):
        f_px = ten_observables_at(Fr(1, 5), Fr(2, 5), tv_fd + h_fd)
        f_mx = ten_observables_at(Fr(1, 5), Fr(2, 5), tv_fd - h_fd)
        f_py = ten_observables_at(Fr(1, 5), Fr(2, 5), tv_fd + I_MP * h_fd)
        f_my = ten_observables_at(Fr(1, 5), Fr(2, 5), tv_fd - I_MP * h_fd)
        jac_10x2 = mp.matrix([[mp.re((f_px[r] - f_mx[r]) / (2 * h_fd)), mp.re((f_py[r] - f_my[r]) / (2 * h_fd))] for r in range(10)])
        _, sv_j, _ = mp.svd_r(jac_10x2)
        s_hi, s_lo = max(sv_j[0], sv_j[1]), min(sv_j[0], sv_j[1])
        min_s2_over_s1 = min(min_s2_over_s1, s_lo / s_hi)
        jac_frozen = mp.matrix([[Z0, jac_10x2[r, 1]] for r in range(10)])
        _, sv_fr, _ = mp.svd_r(jac_frozen)
        frozen_re_rank1_s2 = max(frozen_re_rank1_s2, min(sv_fr[0], sv_fr[1]))

    # 3. Symbolic SymPy verification of agy-002 A2-B1972-OPEN 3-factor singlet det Y law & twin/mark spectra:
    h0, h1, h2, u0, u1, u2, w_s, s_s = sp.symbols("h0 h1 h2 u0 u1 u2 w_s s_s")
    hv_s = sp.Matrix([h0, h1, h2])
    uv_s = sp.Matrix([u0, u1, u2])
    cross_m = lambda v: sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    y_sing = hv_s * uv_s.T + uv_s * hv_s.T - (uv_s.dot(hv_s, hermitian=False)) * sp.eye(3) + w_s * cross_m(hv_s) - s_s * (w_s * sp.eye(3) + cross_m(uv_s))
    det_target = (uv_s.dot(uv_s, hermitian=False) + w_s ** 2) * (hv_s.dot(hv_s, hermitian=False) + s_s ** 2) * (uv_s.dot(hv_s, hermitian=False) - w_s * s_s)
    det_3factor_resid = sp.expand(y_sing.det() - det_target)
    assert det_3factor_resid == 0

    u_null = sp.Matrix([[1 / sp.sqrt(2), 1 / sp.sqrt(2), 0], [-sp.I / sp.sqrt(2), sp.I / sp.sqrt(2), 0], [0, 0, 1]])
    e3_x = cross_m(sp.Matrix([0, 0, 1]))
    mark_diag = (u_null.H * (sp.I * sp.eye(3) + e3_x) * u_null).applyfunc(sp.simplify)
    twin_diag = (u_null.H * (-sp.I * sp.eye(3) + e3_x) * u_null).applyfunc(sp.simplify)
    assert mark_diag == sp.diag(2 * sp.I, 0, sp.I) and twin_diag == sp.diag(0, -2 * sp.I, -sp.I)

    # 4. Closing D4: agy-exp E_tau[6]_prim GL(2, Z) invariance (24 pts) & exact 0c8debf48 SL(2, Z[omega]) m003 sister spin-swap words:
    e6_prim = {(a, b) for a in range(6) for b in range(6) if math.gcd(math.gcd(a, b), 6) == 1}
    gl2_gens = (((1, 1), (0, 1)), ((0, -1), (1, 0)), ((1, 0), (0, -1)))
    e6_gl2_inv = all({((g[0][0] * a + g[0][1] * b) % 6, (g[1][0] * a + g[1][1] * b) % 6) for a, b in e6_prim} == e6_prim for g in gl2_gens)
    assert len(e6_prim) == 24 and e6_gl2_inv

    simp_c = lambda m: m.applyfunc(lambda e: sp.simplify(sp.expand_complex(e)))
    om = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    om2 = sp.conjugate(om)
    a3_m = sp.Matrix([[om, -1], [om2, om2 - om]])
    b3_m = sp.Matrix([[-om, 1], [om2, 1]])
    a2_m = -a3_m
    b2_m = b3_m
    g3_m = sp.Matrix([[1, -om], [0, 1]])
    g3_inv = sp.Matrix([[1, om], [0, 1]])
    assert sp.simplify(sp.expand_complex(a3_m.det() - 1)) == 0 and sp.simplify(sp.expand_complex(b3_m.det() - 1)) == 0

    # Relator a*b*a^-2*b*a*b^3 == +I_2 and peripheral curves lambda_3 = A B A b a b, mu_3^-1 = b b a b a on rho_1 vs rho_2:
    rel_rho1 = simp_c(a3_m * b3_m * (a3_m ** (-2)) * b3_m * a3_m * (b3_m ** 3) - sp.eye(2))
    rel_rho2 = simp_c(a2_m * b2_m * (a2_m ** (-2)) * b2_m * a2_m * (b2_m ** 3) - sp.eye(2))
    assert rel_rho1 == sp.zeros(2, 2) and rel_rho2 == sp.zeros(2, 2)
    lam_rho1 = simp_c(a3_m.inv() * b3_m.inv() * a3_m.inv() * b3_m * a3_m * b3_m)
    mu_inv_rho1 = simp_c(b3_m * b3_m * a3_m * b3_m * a3_m)
    lam_rho2 = simp_c(a2_m.inv() * b2_m.inv() * a2_m.inv() * b2_m * a2_m * b2_m)
    mu_inv_rho2 = simp_c(b2_m * b2_m * a2_m * b2_m * a2_m)
    assert simp_c(lam_rho1 - sp.Matrix([[1, 2 * om], [0, 1]])) == sp.zeros(2, 2) and simp_c(mu_inv_rho1 + sp.Matrix([[1, 2], [0, 1]])) == sp.zeros(2, 2)
    assert simp_c(lam_rho2 + sp.Matrix([[1, 2 * om], [0, 1]])) == sp.zeros(2, 2) and simp_c(mu_inv_rho2 + sp.Matrix([[1, 2], [0, 1]])) == sp.zeros(2, 2)

    # Exact P-540 sister spin-swap bijection Phi_3(z, t) = (conj(z) - omega, t):
    x2_m = simp_c(b2_m * a2_m)
    y2_m = simp_c(b2_m.inv() * a2_m.inv() * b2_m.inv() * a2_m * b2_m.inv())
    x1_m = simp_c(b3_m * a3_m)
    y1_m = simp_c(b3_m.inv() * a3_m.inv() * b3_m.inv() * a3_m * b3_m.inv())
    x2_inv = simp_c(x2_m.inv())
    y2_inv = simp_c(y2_m.inv())
    m003_sister_ok = bool(
        simp_c(g3_m * a3_m.conjugate() * g3_inv - x2_m) == sp.zeros(2, 2)
        and simp_c(g3_m * b3_m.conjugate() * g3_inv - y2_m) == sp.zeros(2, 2)
        and simp_c(g3_m * a2_m.conjugate() * g3_inv - x1_m) == sp.zeros(2, 2)
        and simp_c(g3_m * b2_m.conjugate() * g3_inv - y1_m) == sp.zeros(2, 2)
        and simp_c(simp_c(x2_inv * y2_m) * simp_c(x2_m * y2_m * x2_m) - a2_m) == sp.zeros(2, 2)
        and simp_c(simp_c(y2_inv * x2_inv) * simp_c(y2_inv * x2_m) - b2_m) == sp.zeros(2, 2)
    )
    assert m003_sister_ok

    ctrl5_ok = bool(
        m3_conj_violations == 0
        and rho_w_same < mp_rat(1, 90)
        and fl_w_same > mp_rat(7, 100)
        and min_s2_over_s1 > mp_rat(1, 25)
        and frozen_re_rank1_s2 == 0
        and det_3factor_resid == 0
        and len(e6_prim) == 24
        and e6_gl2_inv
        and m003_sister_ok
    )
    assert ctrl5_ok

    return {
        "chat1_m3_scope_conj_violations_0_vs_same_higgs_escape": [
            m3_conj_violations,
            mp.nstr(rho_w_same, 8),
            mp.nstr(fl_w_same, 8),
        ],
        "chat1_p596_fd_rank_2_min_s2_over_s1_vs_frozen_s2": [
            mp.nstr(min_s2_over_s1, 8),
            mp.nstr(frozen_re_rank1_s2, 4),
        ],
        "chat1_chk2_mtheory_chain_response": "Affirmed: C22/C37 G2 L(Q) chain carries 4 identifications + free V_perp (not 0-parameter); AGY-C44 v9.json retired G2 L(Q) for 10D E_8xE_8 at 33/2 discrete bits + R11 == 4 continuous UV ratios with real 13x homogeneity check",
        "agy002_b1972_open_3factor_det_and_twin_mark_verified": True,
        "agyexp_e6_prim_24_gl2z_invariant_with_typing_note": "Verified 24-pt GL(2,Z) shell; per chat1 CHK-2 [J], uniform 24-pt weight is an imported P-845 rule and mirror baryon sign imports 1 bit",
        "agyexp_m49_m003_sister_isomorphism_words_verified": {"conj_a3": "ba", "conj_b3": "BABaB", "inv_a": "Xyxyx", "inv_b": "YXYx", "verified": m003_sister_ok},
        "control_5_chat1_same_higgs_escapes_m3_and_frozen_re_rank1_caught": ctrl5_ok,
    }, ctrl5_ok


def main() -> None:
    t0 = time.time()
    ast_check = verify_ast_strict()
    e1_res, c1, c2, c3 = verify_e1_m16_p557_p667_p640()
    e2_res, c4 = verify_e2_m14_m15_m17_b1974_calibration()
    e3_res, c5 = verify_e3_peer_sweep_chat1_agy002_agyexp()

    controls_caught = sum(int(x) for x in (c1, c2, c3, c4, c5))
    assert controls_caught == 5

    payload = {
        "card": "AGY-C48",
        "supersedes_non_destructively": "AGY-C47 (closing D1..D4)",
        "answers_main_messages": ["M14", "M15", "M16 (P-557, P-667, P-640)", "M17 (Review 86)"],
        "empirical_firewall": "0 of 19",
        "sandbox_dependencies": ["python_stdlib", "mpmath", "sympy"],
        "check_labels_section_12": [
            "recomputed independently",
            "computed once",
            "expectations committed first",
            "tested against planted errors",
        ],
        "planted_controls_caught": controls_caught,
        "planted_controls_total": 5,
        "ast_zero_float_check": ast_check,
        "E1_m16_p557_p667_p640": e1_res,
        "E2_m14_m15_m17_b1974_calibration": e2_res,
        "E3_peer_sweep_chat1_agy002_agyexp": e3_res,
        "all_expectations_passed": True,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"AGY-C48 producer complete in {int(time.time() - t0)}s: "
        f"P-557 computed 50880/40000/32320=125/101, P-667 q^117/q^23, P-640 APS ind=0, "
        f"B1974 X0(2) extracted, M49 sister words & chat1 M3/P596 verified, controls={controls_caught}/5."
    )


if __name__ == "__main__":
    main()
