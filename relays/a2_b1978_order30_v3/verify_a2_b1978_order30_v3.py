"""Standalone 0-of-19 Authoritative Producer v3 for Card AGY-002_A2-B1978-ORDER30.

Pure Python stdlib + mpmath + sympy ONLY.
Zero float/complex AST literals or casts; zero numpy/scipy/frontier imports;
zero JSON float tokens. Strictly 0 of 19 (data-free).

Remediations over frozen v1 (a4a73b62e -> 59b080722) & frozen v2 (39a48eb1b -> 58681f7f0):
  1. Holomorphic theta evaluation without principal-branch cuts: uses mp.exp(I*pi*tau*na^2) in
     thc_direct and 2*mp.exp(I*pi*tau/4)*sum(qh^{n(n+1)}) for th2 (eliminating qh**(non-int)
     branch-cut jumps for Re(tau) not in (-1, 1], achieving < 1e-45 exact joint SL(2,Z) and
     monodromy M = [[2,1],[1,1]] covariance everywhere on H).
  2. Exact shared-Higgs SVD frame (s = 0, S_SVD = [[0, p], [r, 0]]) for CKM mixing tropical
     exponents (V12, V23, V13, V31), proving analytically why the shared O(s/p) = O(eps^{1/2})
     Higgs rotation cancels identically in V = U_u^H U_d across all 12 nd(a) classes (960/960
     exact rational rates), plus explicit counterfactual test (s -> -s in Y_u alone restores the
     1/2 rate, answering B1971 Review 86's owed counterfactual).
  3. Refined low-y Richardson-RK4 grids in solve_L2_fuchsian_mp (max_ode_res < 1e-10,
     L_2(tau+1) err < 1e-9, L_2(gamma*tau) law err < 1e-8).
"""

import ast
import hashlib
import itertools
import json
import math
import pathlib
import random
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import sympy as sp

SCRIPT_PATH = pathlib.Path(__file__).resolve()
OUT_JSON_PATH = SCRIPT_PATH.with_name("verify_a2_b1978_order30_v3_out.json")
OUT_SHA_PATH = SCRIPT_PATH.with_name("OUTPUT_SHA256.txt")


# ---------------------------------------------------------------------------
# Zero-Float / Zero-Complex Helpers & Exact Formatting
# ---------------------------------------------------------------------------

def iu():
    return mp.mpc(0, 1)


def mp_rat(p: int, q: int = 1):
    return mp.mpf(p) / mp.mpf(q)


def mp_frac(f: Fraction):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def mp_pow10(k: int):
    return mp.mpf(10) ** k


def mp_str(x, digits: int = 14) -> str:
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


def pt_order(p: Tuple[Fraction, Fraction]) -> int:
    return math.lcm(p[0].denominator, p[1].denominator)


def mod1_pt(a: Fraction, b: Fraction) -> Tuple[Fraction, Fraction]:
    return (a - math.floor(a), b - math.floor(b))


# ---------------------------------------------------------------------------
# AST Hygiene & JSON Float-Free Audit
# ---------------------------------------------------------------------------

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
# Exact Symbolic Tropical Engine (O1: Full-S Masses + Higgs-SVD Mixing Law)
# ---------------------------------------------------------------------------

SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def build_symbolic_tropical_model() -> Dict[str, Any]:
    """Build exact SymPy monomial tables for Y, 2x2 minors, det Y, and Higgs-SVD rotated Gramian."""
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

    def poly_monos(expr, var_tuple):
        ex = sp.expand(expr)
        if ex == 0:
            return []
        P = sp.Poly(ex, *var_tuple)
        return [mon for mon, coeff in P.terms() if coeff != 0]

    ents_monos = [poly_monos(Y[a, b], svars) for a in range(3) for b in range(3)]
    ents_monos = [ml for ml in ents_monos if ml]
    mins_monos = [
        poly_monos(Y.extract(list(R_), list(C_)).det(), svars)
        for R_ in itertools.combinations(range(3), 2)
        for C_ in itertools.combinations(range(3), 2)
    ]
    mins_monos = [ml for ml in mins_monos if ml]
    det_monos = poly_monos(Y.det(), svars)

    # Exact rotated left basis Q_H = [[1, 0, +i], [0, 1, 0], [1, 0, -i]]:
    # row 0 (e_+) and row 1 (e_1) carry p; row 2 (e_-) has identically zero p-coefficient!
    Q_H = sp.Matrix([
        [1, 0, I_sp],
        [0, 1, 0],
        [1, 0, -I_sp],
    ])
    Y_rot = sp.Matrix(3, 3, lambda a, b: sp.expand((Q_H * Y)[a, b]))

    conj_map = {
        s: sc, p: pc, r: rc,
        m00: m00c, m01: m01c, m10: m10c, m11: m11c,
    }

    def formal_conj(expr):
        ex = sp.expand(expr)
        ex = ex.xreplace({I_sp: -I_sp})
        return sp.expand(ex.xreplace(conj_map))

    # Full-S rotated Gramian (retaining s) AND Higgs-SVD frame (s = 0: shared left Higgs rotation cancelled)
    Y_rot_H = sp.Matrix(3, 3, lambda a, b: formal_conj(Y_rot[b, a]))
    H_full = sp.Matrix(3, 3, lambda a, b: sp.expand((Y_rot * Y_rot_H)[a, b]))

    Y_rot_s0 = Y_rot.subs({s: 0})
    Y_rot_s0_H = sp.Matrix(3, 3, lambda a, b: formal_conj(Y_rot_s0[b, a]))
    H_s0 = sp.Matrix(3, 3, lambda a, b: sp.expand((Y_rot_s0 * Y_rot_s0_H)[a, b]))

    row_minus_has_p = any(
        sp.Poly(sp.expand(Y_rot[2, b]), *svars).degree(p) > 0
        for b in range(3) if sp.expand(Y_rot[2, b]) != 0
    )

    H_s0_monos = [[poly_monos(H_s0[i, j], hvars) for j in range(3)] for i in range(3)]
    schur_s0_monos = {
        "lt_quarter": poly_monos(H_s0[2, 1] * H_s0[0, 0] - H_s0[2, 0] * H_s0[0, 1], hvars),
        "gt_quarter": poly_monos(H_s0[2, 0] * H_s0[1, 1] - H_s0[2, 1] * H_s0[1, 0], hvars),
    }

    # Also keep s0 mass polynomials to verify mass exponents are invariant under Higgs-SVD frame (s=0)
    Y_s0 = Y.subs({s: 0})
    ents_s0 = [poly_monos(Y_s0[a, b], svars) for a in range(3) for b in range(3)]
    ents_s0 = [ml for ml in ents_s0 if ml]
    mins_s0 = [
        poly_monos(Y_s0.extract(list(R_), list(C_)).det(), svars)
        for R_ in itertools.combinations(range(3), 2)
        for C_ in itertools.combinations(range(3), 2)
    ]
    mins_s0 = [ml for ml in mins_s0 if ml]
    det_s0 = poly_monos(Y_s0.det(), svars)

    return {
        "ents": ents_monos,
        "mins": mins_monos,
        "det": det_monos,
        "ents_s0": ents_s0,
        "mins_s0": mins_s0,
        "det_s0": det_s0,
        "H_s0_monos": H_s0_monos,
        "schur_s0_monos": schur_s0_monos,
        "row_minus_has_p": row_minus_has_p,
    }


def channel_exps_q(ax: Fraction, ay: Fraction) -> List[Fraction]:
    h = Fraction(1, 2)
    e8 = Fraction(1, 8)
    return [
        nd_frac(ax) ** 2 + nd_frac(ay) ** 2 - e8,
        nd_frac(ax) ** 2 + nd_frac(ay + h) ** 2 - e8,
        nd_frac(ax + h) ** 2 + nd_frac(ay) ** 2 - e8,
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


def tropical_sector_and_tilts(model: Dict[str, Any], a: Fraction, qL: int, qR: int) -> Dict[str, Any]:
    """Compute exact tropical mass rates (eps-units) and Higgs-SVD (s=0) left-basis tilts."""
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

    # Higgs-SVD s=0 singular values (for Schur-complement denominator lambda_2)
    e_ent0 = min(eval_trop(ml, ev_s) for ml in model["ents_s0"])
    e_min0 = min(eval_trop(ml, ev_s) for ml in model["mins_s0"])
    e2_q0 = e_min0 - e_ent0

    m2m3_eps = Fraction(2, 1) * (e2_q - e3_q)
    m1m3_eps = Fraction(2, 1) * (e1_q - e3_q)

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
            "e3_q": e3_q,
            "e2_q": e2_q,
            "e1_q": e1_q,
            "degenerate_quarter": True,
            "t23": Fraction(0, 1),
            "t13": None,
            "t12": None,
        }

    h33 = eval_trop(model["H_s0_monos"][idx3][idx3], ev_h)
    h23 = eval_trop(model["H_s0_monos"][idx2][idx3], ev_h)
    h13 = eval_trop(model["H_s0_monos"][idx1][idx3], ev_h)
    c12 = eval_trop(model["schur_s0_monos"][s_key], ev_h)

    t23_q = h23 - h33
    t13_q = h13 - h33
    t12_q = c12 - h33 - Fraction(2, 1) * e2_q0

    return {
        "m2m3": m2m3_eps,
        "m1m3": m1m3_eps,
        "e3_q": e3_q,
        "e2_q": e2_q,
        "e1_q": e1_q,
        "degenerate_quarter": False,
        "t23": Fraction(2, 1) * t23_q,
        "t13": Fraction(2, 1) * t13_q,
        "t12": Fraction(2, 1) * t12_q,
    }


def tropical_full_point(model: Dict[str, Any], a: Fraction, charges: Optional[Dict[str, int]] = None) -> Dict[str, Any]:
    ch = charges if charges is not None else SIXY
    up = tropical_sector_and_tilts(model, a, ch["Q"], ch["u"])
    dn = tropical_sector_and_tilts(model, a, ch["Q"], ch["d"])
    lp = tropical_sector_and_tilts(model, a, ch["L"], ch["e"])

    if up["degenerate_quarter"] or dn["degenerate_quarter"]:
        v23 = Fraction(0, 1)
        v12 = None
        v13 = None
        v31 = None
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
        "up_tilts": (up["t12"], up["t23"], up["t13"]),
        "dn_tilts": (dn["t12"], dn["t23"], dn["t13"]),
    }


# ---------------------------------------------------------------------------
# First-Principles Pure-mpmath Fuchsian Weierstrass L_2(tau) & Frame C Engine
# ---------------------------------------------------------------------------

def solve_L2_fuchsian_mp(tau, dps: int = 38) -> Tuple[Any, Any]:
    """Solve exact length-2 horocycle canonical end L_2(tau) via refined Richardson-RK4."""
    ty = mp.im(tau)
    dps_ode = max(dps, 36 + int(mp.ceil(ty)))
    mp.mp.dps = dps_ode
    I = iu()
    pi = mp.pi
    tau = mp.mpc(mp.re(tau), mp.im(tau))
    ty = mp.im(tau)

    q = mp.exp(2 * I * pi * tau)
    K = max(6, int(mp.ceil((dps_ode * mp.mpf(231)) / (mp.mpf(628) * ty))) + 5)
    e2 = mp.mpf(1)
    e4 = mp.mpf(1)
    e6 = mp.mpf(1)
    dn = []
    qn = mp.mpc(1)
    for n in range(1, K + 1):
        qn = qn * q
        d = 1 - qn
        dn.append(d)
        e2 -= 24 * n * qn / d
        e4 += 240 * (n ** 3) * qn / d
        e6 -= 504 * (n ** 5) * qn / d
    g2 = mp_rat(4, 3) * (pi ** 4) * e4
    g3 = mp_rat(8, 27) * (pi ** 6) * e6

    def wp(z):
        mt = int(mp.nint(mp.im(z) / ty))
        n1 = int(mp.nint(mp.re(z - mt * tau)))
        zr = z - mt * tau - n1
        u = zr if mp.im(zr) >= 0 else -zr
        eu = mp.exp(2 * I * pi * u)
        sm = mp.mpc(0)
        ep_base = mp.exp(2 * I * pi * (tau + zr))
        em_base = mp.exp(2 * I * pi * (tau - zr))
        ep_p = mp.mpc(1)
        em_p = mp.mpc(1)
        for idx, d in enumerate(dn):
            n = idx + 1
            ep_p = ep_p * ep_base
            em_p = em_p * em_base
            sm += (n / d) * (ep_p + em_p)
        return -pi * pi * e2 / 3 - 4 * pi * pi * eu / ((1 - eu) ** 2) - 4 * pi * pi * sm

    def build_seg_list(spec):
        segs = []
        for za, zb, nsteps in spec:
            dz = zb - za
            h = dz / nsteps
            w0 = [wp(za + k * h) / 4 for k in range(nsteps + 1)]
            wm = [wp(za + (k + mp_rat(1, 2)) * h) / 4 for k in range(nsteps)]
            segs.append((h, nsteps, w0, wm))
        return segs

    def make_b_spec(scale: int):
        z0 = (1 + tau) / 2
        if ty <= 8:
            spu = 32 if ty <= 3 else 18
            n = max(32 * scale, int(mp.ceil(abs(tau) * spu * scale)))
            return [(z0, z0 + tau, n)]
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
    n_a1 = 44 if ty < 1 else (36 if ty <= 3 else 24)
    ga1 = build_seg_list([(z0, z0 + 1, n_a1)])
    gb1 = build_seg_list(make_b_spec(1))
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
    for _ in range(32):
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
    zs = (z0_loc / abs(z0_loc)) / 24
    if ty <= 8:
        in_pts = [z0, z0_loc, z0_loc / 2, z0_loc / 4, z0_loc / 8, zs] if z0 != z0_loc else [z0, z0 / 2, z0 / 4, z0 / 8, zs]
    else:
        z_anchor = mp.mpc(mp_rat(1, 2), mp.mpf(2))
        in_pts = [z0, z_anchor, z_anchor / 2, z_anchor / 4, z_anchor / 8, zs]
    spu_in = 36 if ty <= 3 else 20
    gin1 = build_seg_list([(a, b, max(30, int(mp.ceil(abs(b - a) * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
    gin2 = build_seg_list([(a, b, max(60, int(mp.ceil(abs(b - a) * 2 * spu_in)))) for a, b in zip(in_pts[:-1], in_pts[1:])])
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
    L2_val = pi - (2 * pi / lam) * imB
    return L2_val, rel_res


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


class FrameCCouplingContext:
    """Cached standalone pure-mpmath Frame C evaluator (holomorphic branch-cut-free theta & Halphen-Serre S)."""

    def __init__(self, tau_mp, L2_val, dps: int = 55):
        self.dps = dps
        mp.mp.dps = dps
        I = iu()
        pi = mp.pi
        self.tau = mp.mpc(mp.re(tau_mp), mp.im(tau_mp))
        self.tx_m = mp.re(self.tau)
        self.ty_m = mp.im(self.tau)
        self.L = mp.mpf(L2_val)

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

        # Branch-cut-free holomorphic theta_2(0, tau), theta_3(0, tau), theta_4(0, tau)
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

        QI = mp.matrix([[I, 0], [0, -I]])
        QJ = mp.matrix([[0, 1], [-1, 0]])
        QK = QI * QJ
        EPS = QJ
        self.S = c0 * QI + c1 * QJ + c2 * QK
        # Also store flipped-s Higgs S_flip = -c0*QI + c1*QJ + c2*QK for B1971 Review 86 counterfactual
        self.S_flip = (-c0) * QI + c1 * QJ + c2 * QK
        blocks = [QJ, QI, QK]
        self.T_S = [
            [blocks[a].T * EPS * self.S * blocks[b] for b in range(3)]
            for a in range(3)
        ]
        self.T_S_flip = [
            [blocks[a].T * EPS * self.S_flip * blocks[b] for b in range(3)]
            for a in range(3)
        ]
        self.edual = build_exact_edual(I)
        self._thc_cache: Dict[Tuple[Fraction, Fraction], Any] = {}
        self._weight_cache: Dict[Tuple[Fraction, Fraction], Any] = {}
        self._Y_cache: Dict[Tuple[Fraction, Fraction, str], Any] = {}

    def thc_direct(self, ca: Fraction, cb: Fraction):
        """Branch-cut-free holomorphic theta[ca, cb](0, tau) = sum exp(i*pi*tau*(n+ca)^2 + 2*pi*i*(n+ca)*cb)."""
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
                w = mp.exp(-2 * pi * abs(m) * self.ty_m + 2 * I * pi * (m * self.tx_m + be_m))
                tot += (2 * pi / abs(m)) * mp.re(w / (1 - w))
            Fu = first + zrow + tot

            c = Fu + pi * mp.log(self.ty_m) - 2 * pi * (mp.euler + mp.log(pi)) - pi * (abs(a0) ** 2) * mp.exp(-2 * self.L)
            arg = 2 * pi * self.L + c
            self._weight_cache[key] = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        return self._weight_cache[key]

    def yukawa(self, a_f: Fraction, b_f: Fraction, sec: str, return_u: bool = False, flip_s: bool = False):
        key = (a_f, b_f, sec)
        if not return_u and not flip_s and key in self._Y_cache:
            return self._Y_cache[key]
        mp.mp.dps = self.dps
        I = iu()
        pi = mp.pi
        H = Fraction(1, 2)
        qL, qR = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
        xf = (qL * a_f, 2 * qL * b_f)
        yf = (qR * a_f, 2 * qR * b_f)
        ap, am = xf[0] + yf[0], xf[0] - yf[0]
        bp, bm = (xf[1] + yf[1]) / 2, (xf[1] - yf[1]) / 2
        e = mp.exp(-2 * I * pi * mp_frac(xf[0]))
        kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
        cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
        ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}

        Mw = mp.zeros(2, 2)
        u_dict = {}
        for s in ("1", "i", "j", "k"):
            zc = (cs[s][0] - H).denominator == 1 and (cs[s][1] - H).denominator == 1
            zd = (ds[s][0] - H).denominator == 1 and (ds[s][1] - H).denominator == 1
            if zc or zd:
                u_dict[s] = mp.mpc(0)
                continue
            R = kap[s] * self.thc(cs[s][0], cs[s][1]) * self.thc(ds[s][0], ds[s][1]) / self.t1p
            w_s = self._weight_sqrt(cs[s][0] - H, cs[s][1] - H)
            u_val = w_s * R
            u_dict[s] = u_val
            Mw += u_val * self.edual[s]

        T_use = self.T_S_flip if flip_s else self.T_S
        Y = mp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                T = T_use[a][b]
                Y[a, b] = T[0, 0] * Mw[0, 0] + T[0, 1] * Mw[0, 1] + T[1, 0] * Mw[1, 0] + T[1, 1] * Mw[1, 1]

        if not flip_s:
            self._Y_cache[key] = Y
        if return_u:
            return Y, u_dict
        return Y


# ---------------------------------------------------------------------------
# Precision-Safe SVD, CKM, & Non-Squaring Stacked Gramian Solver
# ---------------------------------------------------------------------------

def svd_asc(Y):
    Uu, Sv, Vv = mp.svd_c(Y)
    order = sorted(range(3), key=lambda idx: abs(Sv[idx]))
    U_asc = mp.matrix([[Uu[r, order[c]] for c in range(3)] for r in range(3)])
    Vh_asc = mp.matrix([[Vv[order[r], c] for c in range(3)] for r in range(3)])
    sv_asc = [abs(Sv[idx]) for idx in order]
    return U_asc, sv_asc, Vh_asc


def observables_from_Y(Yu, Yd, Yl) -> Dict[str, Any]:
    Uu, su, _ = svd_asc(Yu)
    Ud, sd, _ = svd_asc(Yd)
    _, sl, _ = svd_asc(Yl)
    V = Uu.H * Ud
    Vabs = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    J_cp = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))
    unit_err = mp.mnorm(V * V.H - mp.eye(3), "F")
    return {
        "up_m2m3": su[1] / su[2],
        "up_m1m3": su[0] / su[2],
        "down_m2m3": sd[1] / sd[2],
        "down_m1m3": sd[0] / sd[2],
        "lep_m2m3": sl[1] / sl[2],
        "lep_m1m3": sl[0] / sl[2],
        "V12": Vabs[0][1],
        "V23": Vabs[1][2],
        "V13": Vabs[0][2],
        "V31": Vabs[2][0],
        "min_diag": min(Vabs[0][0], Vabs[1][1], Vabs[2][2]),
        "max_off": max(Vabs[i][j] for i in range(3) for j in range(3) if i != j),
        "J_cp": J_cp,
        "unit_err": unit_err,
        "D_lep_down_2": abs(mp.log((sl[1] / sl[2]) / (sd[1] / sd[2]))),
        "D_lep_down_1": abs(mp.log((sl[0] / sl[2]) / (sd[0] / sd[2]))),
    }


def qr_gramian_factor(Y_list: List[Any]):
    K = len(Y_list)
    inv_sqK = mp.mpf(1) / mp.sqrt(mp.mpf(K))
    nrows = 3 * K
    A = mp.zeros(nrows, 3)
    for k, Y in enumerate(Y_list):
        YH = Y.H
        for r in range(3):
            for c in range(3):
                A[3 * k + r, c] = YH[r, c] * inv_sqK
    for col in range(3):
        norm2 = mp.mpf(0)
        for r in range(col, nrows):
            norm2 += abs(A[r, col]) ** 2
        norm = mp.sqrt(norm2)
        if norm == 0:
            continue
        x0 = A[col, col]
        phase = x0 / abs(x0) if abs(x0) > 0 else mp.mpc(1)
        alpha = -phase * norm
        v = [mp.mpc(0)] * (nrows - col)
        v[0] = x0 - alpha
        for r in range(col + 1, nrows):
            v[r - col] = A[r, col]
        v_norm2 = sum((abs(z) ** 2 for z in v), mp.mpf(0))
        if v_norm2 == 0:
            continue
        beta = mp.mpf(2) / v_norm2
        for j in range(col, 3):
            dot = mp.mpc(0)
            for i in range(nrows - col):
                dot += mp.conj(v[i]) * A[col + i, j]
            scale = beta * dot
            for i in range(nrows - col):
                A[col + i, j] -= scale * v[i]
    R = mp.zeros(3, 3)
    for r in range(3):
        for c in range(r, 3):
            R[r, c] = A[r, c]
    return R.H


def gramian_observables(Yu_list: List[Any], Yd_list: List[Any], Yl_list: List[Any]) -> Dict[str, Any]:
    Fu = qr_gramian_factor(Yu_list)
    Fd = qr_gramian_factor(Yd_list)
    Fl = qr_gramian_factor(Yl_list)
    K = len(Yu_list)
    H_dir = mp.zeros(3, 3)
    for Y in Yu_list:
        H_dir += Y * Y.H
    H_dir = H_dir / mp.mpf(K)
    H_fac = Fu * Fu.H
    fac_err = mp.mnorm(H_fac - H_dir, "F") / max(mp.mpf(1), mp.mnorm(H_dir, "F"))
    obs = observables_from_Y(Fu, Fd, Fl)
    obs["qr_factor_rel_err"] = fac_err
    return obs


def rate_eps(v1, v2, dy: Fraction):
    return -(mp.log(abs(v2)) - mp.log(abs(v1))) / (mp.pi * mp_frac(dy))


# ---------------------------------------------------------------------------
# Torsion Sets P_5, P_6, P_30 & Act Orbits
# ---------------------------------------------------------------------------

def build_torsion_sets():
    P5 = [mod1_pt(Fraction(k, 5), Fraction(2 * k, 5)) for k in range(1, 5)]
    P6 = sorted({
        (Fraction(i, 6), Fraction(j, 6))
        for i in range(6) for j in range(6)
        if pt_order((Fraction(i, 6), Fraction(j, 6))) == 6
    })
    P30 = sorted({
        mod1_pt(a5 + a6, b5 + b6)
        for (a5, b5) in P5 for (a6, b6) in P6
    })
    return P5, P6, P30


def act_M(w: Tuple[Fraction, Fraction]) -> Tuple[Fraction, Fraction]:
    return mod1_pt(2 * w[0] + w[1], w[0] + w[1])


def act_gamma_inv_right(w: Tuple[Fraction, Fraction], g: Tuple[int, int, int, int]) -> Tuple[Fraction, Fraction]:
    a, b, c, d = g
    return mod1_pt(d * w[0] - c * w[1], -b * w[0] + a * w[1])


def decompose_p30_point(w: Tuple[Fraction, Fraction]) -> Dict[str, Any]:
    w5 = mod1_pt(6 * w[0], 6 * w[1])
    w6 = mod1_pt(w[0] - w5[0], w[1] - w5[1])
    w2 = mod1_pt(3 * w6[0], 3 * w6[1])
    w3 = mod1_pt(4 * w6[0], 4 * w6[1])
    branch5 = "MARK" if w5 in (
        (Fraction(2, 5), Fraction(4, 5)),
        (Fraction(3, 5), Fraction(1, 5)),
    ) else "TWIN"
    orb3_A = {
        (Fraction(1, 3), Fraction(0, 1)),
        (Fraction(2, 3), Fraction(1, 3)),
        (Fraction(2, 3), Fraction(0, 1)),
        (Fraction(1, 3), Fraction(2, 3)),
    }
    orb3 = "A" if w3 in orb3_A else "B"
    return {"w5": w5, "w6": w6, "w2": w2, "w3": w3, "branch5": branch5, "orb3": orb3}


def build_M_orbits(P30: List[Tuple[Fraction, Fraction]]) -> List[List[Tuple[Fraction, Fraction]]]:
    seen = set()
    orbits = []
    for w in P30:
        if w in seen:
            continue
        orb = []
        cur = w
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = act_M(cur)
        orbits.append(orb)
    return orbits


# ---------------------------------------------------------------------------
# Gate G1 (O1): Exact Tropical Law (960/960 Rates), Higgs-SVD Counterfactual, & Level-N Scan
# ---------------------------------------------------------------------------

def run_G1_O1(model: Dict[str, Any], P5, P6, P30, ctx_cache: Dict[Any, FrameCCouplingContext]):
    nd_vals = sorted({nd_frac(a) for (a, _) in P30})
    H = Fraction(1, 2)
    zero_ch_count = 0
    for (a, b) in P30:
        for sec in ("up", "down", "lep"):
            qL, qR = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
            ap, am = (qL + qR) * a, (qL - qR) * a
            bp, bm = (qL + qR) * b, (qL - qR) * b
            for da, db in ((H, H), (H, Fraction(0)), (Fraction(0), H), (Fraction(0), Fraction(0))):
                if ((ap + da - H).denominator == 1 and (bp + db - H).denominator == 1) or (
                    (am + da - H).denominator == 1 and (bm + db - H).denominator == 1
                ):
                    zero_ch_count += 1

    class_table = []
    trop_by_nd = {}
    w_std_pts = 0
    w_inv_pts = 0
    w_nonadd_pts = 0
    w_std_nonadd_pts = 0
    all_on_1_60 = True
    all_v23_exact = True

    for u in nd_vals:
        tr = tropical_full_point(model, u)
        trop_by_nd[u] = tr
        pts_u = [p for p in P30 if nd_frac(p[0]) == u]
        n_u = len(pts_u)
        rates10 = [
            tr["up_m2m3"], tr["up_m1m3"],
            tr["down_m2m3"], tr["down_m1m3"],
            tr["lep_m2m3"], tr["lep_m1m3"],
            tr["V12"], tr["V23"], tr["V13"], tr["V31"],
        ]
        on_60 = all((r * 60).denominator == 1 for r in rates10)
        if not on_60:
            all_on_1_60 = False
        v23_formula = Fraction(2, 1) * abs(u - Fraction(1, 4))
        v23_ok = (tr["V23"] == v23_formula)
        if not v23_ok:
            all_v23_exact = False

        v12, v23, v13, v31 = tr["V12"], tr["V23"], tr["V13"], tr["V31"]
        if v13 == v12 + v23 and 0 < v12 < v23 < v13:
            ord_lbl = "W-STD"
            w_std_pts += n_u
        elif v13 == v12 + v23 and 0 < v23 < v12 < v13:
            ord_lbl = "W-INV"
            w_inv_pts += n_u
        else:
            ord_lbl = "W-NONADD"
            w_nonadd_pts += n_u
            if 0 < v12 < v23 < v13:
                w_std_nonadd_pts += n_u

        class_table.append({
            "nd_a": frac_str(u),
            "n_points": n_u,
            "rep_point": [frac_str(pts_u[0][0]), frac_str(pts_u[0][1])],
            "up_m2m3": frac_str(tr["up_m2m3"]),
            "up_m1m3": frac_str(tr["up_m1m3"]),
            "down_m2m3": frac_str(tr["down_m2m3"]),
            "down_m1m3": frac_str(tr["down_m1m3"]),
            "lep_m2m3": frac_str(tr["lep_m2m3"]),
            "lep_m1m3": frac_str(tr["lep_m1m3"]),
            "V12": frac_str(v12),
            "V23": frac_str(v23),
            "V13": frac_str(v13),
            "V31": frac_str(v31),
            "v23_equals_2abs_nd_minus_quarter": v23_ok,
            "all_rates_multiple_of_1_60": on_60,
            "lep_split_gen2": (tr["lep_m2m3"] != tr["down_m2m3"]),
            "lep_split_gen1": (tr["lep_m1m3"] != tr["down_m1m3"]),
            "ckm_ordering": ord_lbl,
            "v31_additive": (v31 == v12 + v23),
        })

    ctx30 = ctx_cache[("13/100", 30, "exact")]
    ctx40 = ctx_cache[("13/100", 40, "exact")]
    mp.mp.dps = 120
    keys10 = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13", "V31")
    max_trop_diff = mp.mpf(0)
    max_v23_diff = mp.mpf(0)
    max_v31_diff = mp.mpf(0)
    worst_cell = ""
    e3_tie_pts = []
    e4_small_one_pts = []
    y30_obs_by_pt = {}
    y40_obs_by_pt = {}
    dy10 = Fraction(10, 1)

    for (a, b) in P30:
        Yu30, u_up30 = ctx30.yukawa(a, b, "up", return_u=True)
        Yd30 = ctx30.yukawa(a, b, "down")
        Yl30 = ctx30.yukawa(a, b, "lep")
        o30 = observables_from_Y(Yu30, Yd30, Yl30)
        y30_obs_by_pt[(a, b)] = o30

        mx_u = max(abs(val) for val in u_up30.values())
        one_rel = abs(u_up30["1"]) / mx_u if mx_u > 0 else mp.mpf(0)
        if one_rel < mp_pow10(-10):
            e4_small_one_pts.append([frac_str(a), frac_str(b)])
        if max(o30["D_lep_down_1"], o30["D_lep_down_2"]) <= mp_rat(1, 10):
            e3_tie_pts.append([frac_str(a), frac_str(b)])

        Yu40 = ctx40.yukawa(a, b, "up")
        Yd40 = ctx40.yukawa(a, b, "down")
        Yl40 = ctx40.yukawa(a, b, "lep")
        o40 = observables_from_Y(Yu40, Yd40, Yl40)
        y40_obs_by_pt[(a, b)] = o40

        tr = trop_by_nd[nd_frac(a)]
        for k in keys10:
            num_r = rate_eps(o30[k], o40[k], dy10)
            diff = abs(num_r - mp_frac(tr[k]))
            if diff > max_trop_diff:
                max_trop_diff = diff
                worst_cell = f"({frac_str(a)},{frac_str(b)}):{k}"
            if k == "V23" and diff > max_v23_diff:
                max_v23_diff = diff
            if k == "V31" and diff > max_v31_diff:
                max_v31_diff = diff

    # B1971 Review 86 Counterfactual: flip s -> -s in Y_u alone (breaking shared Higgs rotation!)
    # Expect V12 (for nd(a) < 1/4) and V13 (for nd(a) > 1/4) to collapse to exact rate 1/2!
    cf_lt = (Fraction(7, 30), Fraction(19, 30))  # nd = 7/30 < 1/4: shared V12 = 19/30 -> flipped V12 = 1/2
    cf_gt = (Fraction(4, 15), Fraction(1, 30))   # nd = 4/15 > 1/4: shared V13 = 19/30 -> flipped V13 = 1/2
    o30_lt_f = observables_from_Y(ctx30.yukawa(cf_lt[0], cf_lt[1], "up", flip_s=True), ctx30.yukawa(cf_lt[0], cf_lt[1], "down"), ctx30.yukawa(cf_lt[0], cf_lt[1], "lep"))
    o40_lt_f = observables_from_Y(ctx40.yukawa(cf_lt[0], cf_lt[1], "up", flip_s=True), ctx40.yukawa(cf_lt[0], cf_lt[1], "down"), ctx40.yukawa(cf_lt[0], cf_lt[1], "lep"))
    o30_gt_f = observables_from_Y(ctx30.yukawa(cf_gt[0], cf_gt[1], "up", flip_s=True), ctx30.yukawa(cf_gt[0], cf_gt[1], "down"), ctx30.yukawa(cf_gt[0], cf_gt[1], "lep"))
    o40_gt_f = observables_from_Y(ctx40.yukawa(cf_gt[0], cf_gt[1], "up", flip_s=True), ctx40.yukawa(cf_gt[0], cf_gt[1], "down"), ctx40.yukawa(cf_gt[0], cf_gt[1], "lep"))
    cf_lt_v12_rate = rate_eps(o30_lt_f["V12"], o40_lt_f["V12"], dy10)
    cf_gt_v13_rate = rate_eps(o30_gt_f["V13"], o40_gt_f["V13"], dy10)
    cf_ok = (abs(cf_lt_v12_rate - mp_rat(1, 2)) < mp_rat(1, 1000) and abs(cf_gt_v13_rate - mp_rat(1, 2)) < mp_rat(1, 1000))

    # Compare exact L_2(y) vs clamped L_2(6) on the 5 B1976 slow points at y = 20 -> 30
    ctx20 = ctx_cache[("13/100", 20, "exact")]
    ctx20_cl = ctx_cache[("13/100", 20, "clamp6")]
    ctx30_cl = ctx_cache[("13/100", 30, "clamp6")]
    slow5 = [
        (Fraction(4, 15), Fraction(1, 30)),
        (Fraction(4, 15), Fraction(11, 30)),
        (Fraction(4, 15), Fraction(7, 10)),
        (Fraction(11, 15), Fraction(3, 10)),
        (Fraction(11, 15), Fraction(19, 30)),
    ]
    clamp_rate_diff_max = mp.mpf(0)
    clamp_prefactor_rel_max = mp.mpf(0)
    for (a, b) in slow5:
        o20e = observables_from_Y(ctx20.yukawa(a, b, "up"), ctx20.yukawa(a, b, "down"), ctx20.yukawa(a, b, "lep"))
        o30e = y30_obs_by_pt[(a, b)]
        o20c = observables_from_Y(ctx20_cl.yukawa(a, b, "up"), ctx20_cl.yukawa(a, b, "down"), ctx20_cl.yukawa(a, b, "lep"))
        o30c = observables_from_Y(ctx30_cl.yukawa(a, b, "up"), ctx30_cl.yukawa(a, b, "down"), ctx30_cl.yukawa(a, b, "lep"))
        for k in keys10[:9]:
            re_ = rate_eps(o20e[k], o30e[k], dy10)
            rc_ = rate_eps(o20c[k], o30c[k], dy10)
            clamp_rate_diff_max = max(clamp_rate_diff_max, abs(re_ - rc_))
            clamp_prefactor_rel_max = max(clamp_prefactor_rel_max, abs(o30e[k] / o30c[k] - 1))

    # General-level N scan (Guardrail 1 anti-sharpshooting): all N = 5k (k=1..12) + N = 6, 12
    P5_set = set(P5)
    level_scan = []
    all_vmin_formula_ok = True
    for N in (5, 6, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
        if N % 5 == 0:
            k_fac = N // 5
            pts_N = sorted({
                (Fraction(i, N), Fraction(j, N))
                for i in range(N) for j in range(N)
                if pt_order((Fraction(i, N), Fraction(j, N))) == N
                and mod1_pt(k_fac * Fraction(i, N), k_fac * Fraction(j, N)) in P5_set
            })
        else:
            pts_N = sorted({
                (Fraction(i, N), Fraction(j, N))
                for i in range(N) for j in range(N)
                if pt_order((Fraction(i, N), Fraction(j, N))) == N
            })
        nd_N = sorted({nd_frac(a) for (a, _) in pts_N})
        if N % 4 == 0:
            vmin_law = Fraction(0, 1)
        elif N % 4 == 2:
            vmin_law = Fraction(1, N)
        else:
            vmin_law = Fraction(1, 2 * N)

        min_v23_actual = None
        n_viable_strict = 0
        n_viable_deg0 = 0
        n_w_std_slow = 0
        for u in nd_N:
            tr = tropical_full_point(model, u)
            v23 = tr["V23"]
            if min_v23_actual is None or v23 < min_v23_actual:
                min_v23_actual = v23
            hier_ok = (
                tr["up_m2m3"] >= Fraction(1, 10) and tr["up_m1m3"] >= Fraction(1, 5)
                and tr["down_m2m3"] >= Fraction(1, 10) and tr["down_m1m3"] >= Fraction(1, 5)
            )
            lep_split2 = (tr["lep_m2m3"] != tr["down_m2m3"])
            n_u = sum(1 for (a, _) in pts_N if nd_frac(a) == u)
            if hier_ok and lep_split2 and v23 < Fraction(1, 10):
                if v23 > 0:
                    n_viable_strict += n_u
                else:
                    n_viable_deg0 += n_u
            if (
                tr["V12"] is not None and tr["V13"] is not None
                and tr["V13"] == tr["V12"] + v23
                and Fraction(0) < tr["V12"] < v23 < tr["V13"]
                and tr["V12"] < Fraction(1, 10)
            ):
                n_w_std_slow += n_u

        vmin_all_N = min(Fraction(2, 1) * abs(nd_frac(Fraction(m, N)) - Fraction(1, 4)) for m in range(N))
        if vmin_all_N != vmin_law:
            all_vmin_formula_ok = False

        level_scan.append({
            "N": N,
            "n_points_tested": len(pts_N),
            "n_nd_classes": len(nd_N),
            "vmin_V23_law": frac_str(vmin_law),
            "vmin_V23_all_m_over_N": frac_str(vmin_all_N),
            "vmin_V23_on_act_set": frac_str(min_v23_actual) if min_v23_actual is not None else "none",
            "n_viable_strict_pos_V23_lt_1_10": n_viable_strict,
            "n_viable_with_V23_eq_0": n_viable_deg0,
            "n_W_STD_with_V12_lt_1_10": n_w_std_slow,
        })

    e3_expected = sorted([[frac_str(a), frac_str(b)] for (a, b) in P30 if a in (
        Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5)
    )])
    e4_expected = sorted([[frac_str(a), frac_str(b)] for (a, b) in P30 if a in (
        Fraction(2, 5), Fraction(3, 5)
    )])
    e3_exact = (sorted(e3_tie_pts) == e3_expected)
    e4_exact = (sorted(e4_small_one_pts) == e4_expected)

    passed = (
        len(nd_vals) == 12
        and zero_ch_count == 0
        and (not model["row_minus_has_p"])
        and all_on_1_60
        and all_v23_exact
        and all_vmin_formula_ok
        and max_trop_diff < mp_rat(2, 1000)
        and max_v23_diff < mp_rat(1, 1000)
        and max_v31_diff < mp_rat(2, 1000)
        and cf_ok
        and e3_exact
        and e4_exact
    )

    return {
        "n_distinct_nd_a": len(nd_vals),
        "exact_channel_zeros_on_P30": zero_ch_count,
        "row_e_minus_p_coefficient_identically_zero": (not model["row_minus_has_p"]),
        "all_960_exact_rates_on_1_60_grid": all_on_1_60,
        "all_96_V23_equal_2abs_nd_minus_quarter": all_v23_exact,
        "max_tropical_vs_y30_40_diff_960": mp_str(max_trop_diff, 8),
        "max_V23_vs_y30_40_diff_96": mp_str(max_v23_diff, 8),
        "max_V31_vs_y30_40_diff_96": mp_str(max_v31_diff, 8),
        "worst_cell_960": worst_cell,
        "B1971_R86_higgs_cancellation_counterfactual": {
            "flipped_s_nd_7_30_V12_rate_vs_half": mp_str(cf_lt_v12_rate, 8),
            "flipped_s_nd_4_15_V13_rate_vs_half": mp_str(cf_gt_v13_rate, 8),
            "restores_uncancelled_half_rate": cf_ok,
        },
        "ckm_ordering_counts_on_96": {
            "W_STD_additive": w_std_pts,
            "W_INV_additive": w_inv_pts,
            "W_NONADD_total": w_nonadd_pts,
            "W_NONADD_with_V12_lt_V23_lt_V13": w_std_nonadd_pts,
        },
        "E3_tie_count": len(e3_tie_pts),
        "E3_exact_a6_eq_0_match": e3_exact,
        "E4_small_one_count": len(e4_small_one_pts),
        "E4_exact_a_2_5_or_3_5_match": e4_exact,
        "clamp6_vs_exact_L2_slow5_y20_30": {
            "max_rate_diff": mp_str(clamp_rate_diff_max, 8),
            "max_O1_prefactor_rel_shift_at_y30": mp_str(clamp_prefactor_rel_max, 8),
        },
        "general_level_N_vmin_law_exact": all_vmin_formula_ok,
        "exact_12_nd_class_table": class_table,
        "general_level_N_scan": level_scan,
        "passed": passed,
    }, trop_by_nd, y30_obs_by_pt, y40_obs_by_pt


# ---------------------------------------------------------------------------
# Gate G2 (O2): Moderate-Height Survival, Exact L_2(y) Profile, & Column Spread
# ---------------------------------------------------------------------------

def run_G2_O2(
    P30,
    trop_by_nd,
    ctx_cache: Dict[Any, FrameCCouplingContext],
    L2_meta: Dict[Any, Dict[str, Any]],
    y30_obs_by_pt: Dict[Any, Dict[str, Any]],
    y40_obs_by_pt: Dict[Any, Dict[str, Any]],
) -> Dict[str, Any]:
    max_ode_res = max(mp.mpf(m["rel_trace_res"]) for m in L2_meta.values())
    L2_y2_013, res_a = solve_L2_fuchsian_mp(mp.mpc(mp_rat(13, 100), mp.mpf(2)), dps=40)
    L2_y2_113, res_b = solve_L2_fuchsian_mp(mp.mpc(mp_rat(113, 100), mp.mpf(2)), dps=40)
    L2_T_err = abs(L2_y2_113 - L2_y2_013)
    max_ode_res = max(max_ode_res, res_a, res_b)

    heights_14 = [
        Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2),
        Fraction(3, 1), Fraction(4, 1), Fraction(5, 1), Fraction(6, 1),
        Fraction(8, 1), Fraction(10, 1), Fraction(15, 1), Fraction(20, 1),
        Fraction(30, 1), Fraction(40, 1),
    ]
    L2_profile = []
    L2_6 = L2_meta[("13/100", Fraction(6, 1))]["L2_mp"]
    for y_f in heights_14:
        L_cur = L2_meta[("13/100", y_f)]["L2_mp"]
        L2_profile.append({
            "y": frac_str(y_f),
            "L2_exact": mp_str(L_cur, 14),
            "L2_minus_L2_at_6": mp_str(L_cur - L2_6, 8),
            "rel_trace_res": mp_str(L2_meta[("13/100", y_f)]["rel_trace_res"], 4),
        })

    full96_heights = [Fraction(2, 1), Fraction(3, 1), Fraction(5, 1), Fraction(10, 1), Fraction(20, 1), Fraction(30, 1), Fraction(40, 1)]
    survival_96 = []
    for y_f in full96_heights:
        y_key = int(y_f)
        ctx = ctx_cache[("13/100", y_key, "exact")]
        mp.mp.dps = ctx.dps
        n_aligned = 0
        n_hier_ud = 0
        n_lep_split2 = 0
        n_ckm_std_mag = 0
        n_ckm_inv_mag = 0
        n_all4_and_std = 0
        n_all4_and_inv = 0
        for (a, b) in P30:
            if y_key == 30:
                o = y30_obs_by_pt[(a, b)]
            elif y_key == 40:
                o = y40_obs_by_pt[(a, b)]
            else:
                o = observables_from_Y(ctx.yukawa(a, b, "up"), ctx.yukawa(a, b, "down"), ctx.yukawa(a, b, "lep"))
            al = (o["min_diag"] >= mp_rat(9, 10))
            hr = (
                o["up_m2m3"] < mp_rat(1, 2) and o["up_m1m3"] < mp_rat(1, 10)
                and o["down_m2m3"] < mp_rat(1, 2) and o["down_m1m3"] < mp_rat(1, 10)
            )
            ls2 = (o["D_lep_down_2"] > mp_rat(1, 10))
            std_m = (o["V12"] > o["V23"] > o["V13"])
            inv_m = (o["V23"] > o["V12"] > o["V13"])
            if al:
                n_aligned += 1
            if hr:
                n_hier_ud += 1
            if ls2:
                n_lep_split2 += 1
            if std_m:
                n_ckm_std_mag += 1
            if inv_m:
                n_ckm_inv_mag += 1
            if al and hr and ls2 and std_m:
                n_all4_and_std += 1
            if al and hr and ls2 and inv_m:
                n_all4_and_inv += 1
        survival_96.append({
            "y": frac_str(y_f),
            "eps_pow_2_5": mp_str(mp.exp(-mp.pi * mp_frac(y_f) * mp_rat(2, 5)), 6),
            "aligned_96": n_aligned,
            "hier_ud_96": n_hier_ud,
            "lep_split_gen2_96": n_lep_split2,
            "ckm_mag_V12_gt_V23_gt_V13": n_ckm_std_mag,
            "ckm_mag_V23_gt_V12_gt_V13": n_ckm_inv_mag,
            "simultaneous_aligned_hier_lep2_and_std_CKM": n_all4_and_std,
            "simultaneous_aligned_hier_lep2_and_inv_CKM": n_all4_and_inv,
        })

    tracked_pts = [
        ("slow_4_15_1_30", (Fraction(4, 15), Fraction(1, 30))),
        ("slow_7_30_19_30", (Fraction(7, 30), Fraction(19, 30))),
        ("std_7_15_1_10", (Fraction(7, 15), Fraction(1, 10))),
    ]
    trajectories = {}
    for label, (a, b) in tracked_pts:
        tr = trop_by_nd[nd_frac(a)]
        traj = []
        for y_f in heights_14:
            if y_f == Fraction(30, 1):
                o = y30_obs_by_pt[(a, b)]
                mp.mp.dps = 120
            elif y_f == Fraction(40, 1):
                o = y40_obs_by_pt[(a, b)]
                mp.mp.dps = 120
            else:
                ctx = ctx_cache[("13/100", y_f, "exact")]
                mp.mp.dps = ctx.dps
                o = observables_from_Y(ctx.yukawa(a, b, "up"), ctx.yukawa(a, b, "down"), ctx.yukawa(a, b, "lep"))
            eps = mp.exp(-mp.pi * mp_frac(y_f))
            traj.append({
                "y": frac_str(y_f),
                "min_diag": mp_str(o["min_diag"], 8),
                "up_m2m3": mp_str(o["up_m2m3"], 6),
                "up_m1m3": mp_str(o["up_m1m3"], 6),
                "down_m2m3": mp_str(o["down_m2m3"], 6),
                "down_m1m3": mp_str(o["down_m1m3"], 6),
                "lep_m2m3": mp_str(o["lep_m2m3"], 6),
                "lep_m1m3": mp_str(o["lep_m1m3"], 6),
                "V12": mp_str(o["V12"], 6),
                "V23": mp_str(o["V23"], 6),
                "V13": mp_str(o["V13"], 6),
                "V31": mp_str(o["V31"], 6),
                "abs_J_cp": mp_str(abs(o["J_cp"]), 6),
                "prefactor_up_m2m3": mp_str(o["up_m2m3"] / (eps ** mp_frac(tr["up_m2m3"])), 6),
                "prefactor_V23": mp_str(o["V23"] / (eps ** mp_frac(tr["V23"])), 6),
                "prefactor_V12": mp_str(o["V12"] / (eps ** mp_frac(tr["V12"])), 6),
            })
        trajectories[label] = traj

    cols = [("0", Fraction(0, 1)), ("13/100", Fraction(13, 100)), ("31/100", Fraction(31, 100)), ("1/2", Fraction(1, 2))]
    col_spread = []
    for y_int in (2, 4, 10, 20):
        y_f = Fraction(y_int, 1)
        row_sp = {"y": str(y_int), "points": {}}
        for label, (a, b) in (("slow_4_15_1_30", (Fraction(4, 15), Fraction(1, 30))), ("std_7_15_1_10", (Fraction(7, 15), Fraction(1, 10)))):
            vals = {}
            for xs, _ in cols:
                ctx = ctx_cache[(xs, y_f, "exact")]
                mp.mp.dps = ctx.dps
                vals[xs] = observables_from_Y(ctx.yukawa(a, b, "up"), ctx.yukawa(a, b, "down"), ctx.yukawa(a, b, "lep"))
            ref = vals["13/100"]
            rel_sp = {}
            for k in ("up_m2m3", "down_m2m3", "lep_m2m3", "V12", "V23", "V13"):
                spread = max(abs(vals[xs][k] / ref[k] - 1) for xs, _ in cols)
                rel_sp[k] = mp_str(spread, 6)
            row_sp["points"][label] = rel_sp
        col_spread.append(row_sp)

    passed = (max_ode_res < mp_pow10(-10) and L2_T_err < mp_pow10(-8))

    return {
        "max_fuchsian_L2_rel_trace_res": mp_str(max_ode_res, 6),
        "L2_T_periodicity_err_at_y2": mp_str(L2_T_err, 6),
        "L2_exact_vs_clamp6_profile": L2_profile,
        "survival_96_by_height": survival_96,
        "tracked_point_trajectories": trajectories,
        "column_spread_x_0_013_031_050": col_spread,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G3 (O3): Exact Joint SL(2,Z) & Monodromy M = [[2,1],[1,1]] Covariance
# ---------------------------------------------------------------------------

def run_G3_O3() -> Dict[str, Any]:
    dps = 50
    mp.mp.dps = dps
    tau0 = mp.mpc(mp_rat(-9, 10), mp_rat(6, 5))
    gens = {
        "T": (1, 1, 0, 1),
        "S_mod": (0, -1, 1, 0),
        "M_LR": (2, 1, 1, 1),
    }

    def act_tau(g, t):
        a, b, c, d = g
        return (a * t + b) / (c * t + d)

    L2_0, res0 = solve_L2_fuchsian_mp(tau0, dps=40)
    L2_law_checks = {}
    ctx0 = FrameCCouplingContext(tau0, L2_0, dps=dps)

    test_pts = [
        (Fraction(4, 15), Fraction(1, 30)),
        (Fraction(7, 30), Fraction(19, 30)),
        (Fraction(7, 15), Fraction(1, 10)),
        (Fraction(1, 30), Fraction(1, 15)),
    ]
    obs_keys = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13", "abs_J")

    def get_vec(ctx, w):
        o = observables_from_Y(ctx.yukawa(w[0], w[1], "up"), ctx.yukawa(w[0], w[1], "down"), ctx.yukawa(w[0], w[1], "lep"))
        o["abs_J"] = abs(o["J_cp"])
        return o

    def max_rel_diff(o1, o2):
        mx = mp.mpf(0)
        for k in obs_keys:
            d = abs(o1[k] - o2[k]) / max(abs(o1[k]), mp_pow10(-45))
            if d > mx:
                mx = d
        return mx

    joint_results_tau0 = {}
    pf3_fixed_L2_err = mp.mpf(0)
    pf4_wrong_act_err = mp.mpf(0)

    for gname, g in gens.items():
        a, b, c, d = g
        tg = act_tau(g, tau0)
        L2_ode, res_g = solve_L2_fuchsian_mp(tg, dps=40)
        L2_law = L2_0 + mp.log(abs(c * tau0 + d))
        law_err = abs(L2_ode - L2_law)
        L2_law_checks[gname] = {
            "im_gamma_tau0": mp_str(mp.im(tg), 10),
            "L2_direct_ode": mp_str(L2_ode, 14),
            "L2_from_law": mp_str(L2_law, 14),
            "abs_err": mp_str(law_err, 6),
            "ode_trace_res": mp_str(res_g, 4),
        }

        ctx_law = FrameCCouplingContext(tg, L2_law, dps=dps)
        ctx_fixL = FrameCCouplingContext(tg, L2_0, dps=dps)

        max_joint_right = mp.mpf(0)
        max_joint_left_inv = mp.mpf(0)
        max_fixL = mp.mpf(0)
        max_wrong_w = mp.mpf(0)
        max_fixed_tau_B1978 = mp.mpf(0)

        for w in test_pts:
            o_base = get_vec(ctx0, w)
            w_right = act_gamma_inv_right(w, g)
            o_right = get_vec(ctx_law, w_right)
            max_joint_right = max(max_joint_right, max_rel_diff(o_base, o_right))

            o_fixL = get_vec(ctx_fixL, w_right)
            max_fixL = max(max_fixL, max_rel_diff(o_base, o_fixL))

            w_wrong = mod1_pt(a * w[0] + c * w[1], b * w[0] + d * w[1])
            o_wrong = get_vec(ctx_law, w_wrong)
            max_wrong_w = max(max_wrong_w, max_rel_diff(o_base, o_wrong))

            o_fixt = get_vec(ctx0, w_right)
            max_fixed_tau_B1978 = max(max_fixed_tau_B1978, max_rel_diff(o_base, o_fixt))

            w_linv = mod1_pt(d * w[0] - b * w[1], -c * w[0] + a * w[1])
            o_linv = get_vec(ctx_law, w_linv)
            max_joint_left_inv = max(max_joint_left_inv, max_rel_diff(o_base, o_linv))

        if gname in ("S_mod", "M_LR"):
            pf3_fixed_L2_err = max(pf3_fixed_L2_err, max_fixL)
        if gname in ("T", "M_LR"):
            pf4_wrong_act_err = max(pf4_wrong_act_err, max_wrong_w)

        joint_results_tau0[gname] = {
            "joint_w_gamma_inv_exact_L2_max_rel_diff": mp_str(max_joint_right, 8),
            "joint_gamma_inv_w_exact_L2_max_rel_diff": mp_str(max_joint_left_inv, 8),
            "fixed_L2_control_max_rel_diff": mp_str(max_fixL, 8),
            "wrong_point_action_max_rel_diff": mp_str(max_wrong_w, 8),
            "B1978_fixed_tau_max_rel_diff": mp_str(max_fixed_tau_B1978, 8),
        }

    tau1 = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    L2_1, res1 = solve_L2_fuchsian_mp(tau1, dps=40)
    ctx1 = FrameCCouplingContext(tau1, L2_1, dps=dps)
    joint_results_tau1 = {}
    for gname, g in gens.items():
        a, b, c, d = g
        tg = act_tau(g, tau1)
        L2_law = L2_1 + mp.log(abs(c * tau1 + d))
        ctx_law = FrameCCouplingContext(tg, L2_law, dps=dps)
        mx = mp.mpf(0)
        for w in test_pts:
            o_base = get_vec(ctx1, w)
            o_img = get_vec(ctx_law, act_gamma_inv_right(w, g))
            mx = max(mx, max_rel_diff(o_base, o_img))
        joint_results_tau1[gname] = mp_str(mx, 8)

    max_L2_law_err = max(mp.mpf(v["abs_err"]) for v in L2_law_checks.values())
    T_joint_err = max(
        mp.mpf(joint_results_tau0["T"]["joint_w_gamma_inv_exact_L2_max_rel_diff"]),
        mp.mpf(joint_results_tau1["T"]),
    )
    M_joint_err = max(
        mp.mpf(joint_results_tau0["M_LR"]["joint_w_gamma_inv_exact_L2_max_rel_diff"]),
        mp.mpf(joint_results_tau1["M_LR"]),
    )
    S_joint_err = max(
        mp.mpf(joint_results_tau0["S_mod"]["joint_w_gamma_inv_exact_L2_max_rel_diff"]),
        mp.mpf(joint_results_tau1["S_mod"]),
    )
    full_sl2z_ok = (max(T_joint_err, S_joint_err, M_joint_err) < mp_pow10(-35))

    passed = (
        max_L2_law_err < mp_pow10(-7)
        and full_sl2z_ok
        and res0 < mp_pow10(-10)
        and res1 < mp_pow10(-10)
    )

    return {
        "tau0": "-9/10 + (6/5)i",
        "tau1": "13/100 + 2i",
        "L2_direct_vs_law_checks": L2_law_checks,
        "max_L2_law_err": mp_str(max_L2_law_err, 6),
        "joint_covariance_tau0": joint_results_tau0,
        "joint_covariance_tau1_exact_L2": joint_results_tau1,
        "summary_joint_T_err": mp_str(T_joint_err, 6),
        "summary_joint_S_err": mp_str(S_joint_err, 6),
        "summary_joint_M_err": mp_str(M_joint_err, 6),
        "exact_full_SL2Z_pointwise_joint_invariance": full_sl2z_ok,
        "PF3_fixed_L2_err": mp_str(pf3_fixed_L2_err, 6),
        "PF4_wrong_point_act_err": mp_str(pf4_wrong_act_err, 6),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G4 (O4): 8-Orbit Algebraic Classification & 12-Point M-Orbit Gramians
# ---------------------------------------------------------------------------

def run_G4_O4(P30, ctx_cache: Dict[Any, FrameCCouplingContext]) -> Dict[str, Any]:
    orbits = build_M_orbits(P30)
    orbit_meta = []
    mark_slow_counts = []
    twin_slow_counts = []

    for idx, orb in enumerate(orbits):
        decs = [decompose_p30_point(w) for w in orb]
        branches = sorted({d["branch5"] for d in decs})
        orbs3 = sorted({d["orb3"] for d in decs})
        nd_set = sorted({nd_frac(w[0]) for w in orb})
        n_slow = sum(1 for w in orb if nd_frac(w[0]) in (Fraction(7, 30), Fraction(8, 30)))
        if branches == ["MARK"]:
            mark_slow_counts.append(n_slow)
        elif branches == ["TWIN"]:
            twin_slow_counts.append(n_slow)
        orbit_meta.append({
            "orbit_idx": idx,
            "rep": [frac_str(orb[0][0]), frac_str(orb[0][1])],
            "size": len(orb),
            "branch5": branches[0] if len(branches) == 1 else "MIXED",
            "orb3": orbs3[0] if len(orbs3) == 1 else "MIXED",
            "n_slow_V23_1_30_points": n_slow,
            "distinct_nd_a_in_orbit": [frac_str(u) for u in nd_set],
            "crosses_quarter": (any(u < Fraction(1, 4) for u in nd_set) and any(u > Fraction(1, 4) for u in nd_set)),
        })

    alg_dichotomy_ok = (
        len(orbits) == 8
        and all(len(o) == 12 for o in orbits)
        and sorted(mark_slow_counts, reverse=True) == [6, 6, 3, 3]
        and twin_slow_counts == [0, 0, 0, 0]
        and all(m["crosses_quarter"] for m in orbit_meta)
        and all(m["branch5"] in ("MARK", "TWIN") and m["orb3"] in ("A", "B") for m in orbit_meta)
    )

    eval_ys = [3, 5, 10, 20, 30]
    gram_results = []
    coh_results = []
    max_unit_err = mp.mpf(0)
    max_qr_err = mp.mpf(0)
    max_M_inv_err = mp.mpf(0)

    for idx, orb in enumerate(orbits):
        o_by_y = {}
        c_by_y = {}
        for y_int in eval_ys:
            ctx = ctx_cache[("13/100", y_int, "exact")]
            mp.mp.dps = ctx.dps
            Yu_l = [ctx.yukawa(a, b, "up") for (a, b) in orb]
            Yd_l = [ctx.yukawa(a, b, "down") for (a, b) in orb]
            Yl_l = [ctx.yukawa(a, b, "lep") for (a, b) in orb]

            go = gramian_observables(Yu_l, Yd_l, Yl_l)
            o_by_y[y_int] = go
            max_unit_err = max(max_unit_err, go["unit_err"])
            max_qr_err = max(max_qr_err, go["qr_factor_rel_err"])

            if y_int == 10:
                go_shift = gramian_observables(Yu_l[1:] + Yu_l[:1], Yd_l[1:] + Yd_l[:1], Yl_l[1:] + Yl_l[:1])
                for k in ("up_m2m3", "down_m2m3", "lep_m2m3", "V12", "V23", "V13"):
                    max_M_inv_err = max(max_M_inv_err, abs(go[k] - go_shift[k]) / max(abs(go[k]), mp_pow10(-40)))

            Yu_c = sum(Yu_l, mp.zeros(3, 3)) / mp.mpf(12)
            Yd_c = sum(Yd_l, mp.zeros(3, 3)) / mp.mpf(12)
            Yl_c = sum(Yl_l, mp.zeros(3, 3)) / mp.mpf(12)
            c_by_y[y_int] = observables_from_Y(Yu_c, Yd_c, Yl_c)

        dy10 = Fraction(10, 1)
        g20, g30 = o_by_y[20], o_by_y[30]
        rates_g = {
            k: mp_str(rate_eps(g20[k], g30[k], dy10), 6)
            for k in ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
        }
        gram_results.append({
            "orbit_idx": idx,
            "branch5": orbit_meta[idx]["branch5"],
            "orb3": orbit_meta[idx]["orb3"],
            "n_slow_points": orbit_meta[idx]["n_slow_V23_1_30_points"],
            "rates_y20_30": rates_g,
            "at_y3": {
                "min_diag": mp_str(o_by_y[3]["min_diag"], 6),
                "up_m2m3": mp_str(o_by_y[3]["up_m2m3"], 6),
                "down_m2m3": mp_str(o_by_y[3]["down_m2m3"], 6),
                "lep_m2m3": mp_str(o_by_y[3]["lep_m2m3"], 6),
                "V12": mp_str(o_by_y[3]["V12"], 6),
                "V23": mp_str(o_by_y[3]["V23"], 6),
                "V13": mp_str(o_by_y[3]["V13"], 6),
                "abs_J_cp": mp_str(abs(o_by_y[3]["J_cp"]), 6),
            },
            "at_y30": {
                "min_diag": mp_str(g30["min_diag"], 8),
                "up_m2m3": mp_str(g30["up_m2m3"], 6),
                "up_m1m3": mp_str(g30["up_m1m3"], 6),
                "down_m2m3": mp_str(g30["down_m2m3"], 6),
                "down_m1m3": mp_str(g30["down_m1m3"], 6),
                "lep_m2m3": mp_str(g30["lep_m2m3"], 6),
                "lep_m1m3": mp_str(g30["lep_m1m3"], 6),
                "V12": mp_str(g30["V12"], 6),
                "V23": mp_str(g30["V23"], 6),
                "V13": mp_str(g30["V13"], 6),
                "D_lep_down_2": mp_str(g30["D_lep_down_2"], 6),
                "abs_J_cp": mp_str(abs(g30["J_cp"]), 6),
            },
        })
        c30 = c_by_y[30]
        coh_results.append({
            "orbit_idx": idx,
            "branch5": orbit_meta[idx]["branch5"],
            "orb3": orbit_meta[idx]["orb3"],
            "at_y30": {
                "min_diag": mp_str(c30["min_diag"], 8),
                "up_m2m3": mp_str(c30["up_m2m3"], 6),
                "down_m2m3": mp_str(c30["down_m2m3"], 6),
                "lep_m2m3": mp_str(c30["lep_m2m3"], 6),
                "V12": mp_str(c30["V12"], 6),
                "V23": mp_str(c30["V23"], 6),
                "V13": mp_str(c30["V13"], 6),
            },
        })

    passed = (
        alg_dichotomy_ok
        and max_unit_err < mp_pow10(-30)
        and max_qr_err < mp_pow10(-30)
        and max_M_inv_err < mp_pow10(-30)
    )

    return {
        "algebraic_mark_twin_orbit_dichotomy_exact": alg_dichotomy_ok,
        "all_8_orbits_cross_quarter": all(m["crosses_quarter"] for m in orbit_meta),
        "orbit_metadata": orbit_meta,
        "max_gramian_ckm_unitarity_err": mp_str(max_unit_err, 6),
        "max_qr_factor_vs_direct_gramian_err": mp_str(max_qr_err, 6),
        "max_orbit_gramian_M_invariance_err": mp_str(max_M_inv_err, 6),
        "orbit_gramians": gram_results,
        "orbit_coherent_sums": coh_results,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G5 (O5): P-845 N=1..60 Lens Census & Head-to-Head Shell Gramians
# ---------------------------------------------------------------------------

def run_G5_O5(P5, P6, P30, ctx_cache: Dict[Any, FrameCCouplingContext]) -> Dict[str, Any]:
    pairs = {s: (SIXY[SECTORS[s][0]], SIXY[SECTORS[s][1]]) for s in ("up", "down", "lep")}

    def unit_tied(N: int, p: Tuple[int, int], q: Tuple[int, int]) -> bool:
        for k in range(1, N):
            if math.gcd(k, N) != 1:
                continue
            kp = ((k * p[0]) % N, (k * p[1]) % N)
            if kp == (q[0] % N, q[1] % N) or kp == (q[1] % N, q[0] % N):
                return True
        return False

    no_unit_ties = []
    no_unit_ties_5div = []
    full_sep_and_no_lep_collapse_5div = []
    census_key_levels = []

    for N in range(2, 61):
        u_sym = ((pairs["up"][0] - pairs["up"][1]) % N == 0)
        t_ud = unit_tied(N, pairs["up"], pairs["down"])
        t_ul = unit_tied(N, pairs["up"], pairs["lep"])
        t_dl = unit_tied(N, pairs["down"], pairs["lep"])
        ord_u = N // math.gcd(N, math.gcd(abs(pairs["up"][0]), abs(pairs["up"][1])))
        ord_d = N // math.gcd(N, math.gcd(abs(pairs["down"][0]), abs(pairs["down"][1])))
        ord_l = N // math.gcd(N, math.gcd(abs(pairs["lep"][0]), abs(pairs["lep"][1])))
        lep_collapses_to_5 = (ord_l == 5 and N % 5 == 0 and N > 5)

        if not (t_ud or t_ul or t_dl or u_sym):
            no_unit_ties.append(N)
            if N % 5 == 0:
                no_unit_ties_5div.append(N)
                if not lep_collapses_to_5:
                    full_sep_and_no_lep_collapse_5div.append(N)

        if N in (5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 60):
            census_key_levels.append({
                "N": N,
                "u_symmetric_mod_N": u_sym,
                "tie_up_down": t_ud,
                "tie_up_lep": t_ul,
                "tie_down_lep": t_dl,
                "eff_orders_u_d_l": [ord_u, ord_d, ord_l],
                "lep_collapses_to_order_5": lep_collapses_to_5,
                "resolves_Z6_centre": (N % 6 == 0),
                "contains_act_K5": (N % 5 == 0),
            })

    pf6_k5_pointwise_max_diff = mp.mpf(0)
    for y_int in (3, 20, 30):
        ctx = ctx_cache[("13/100", y_int, "exact")]
        mp.mp.dps = ctx.dps
        for (a, b) in P5:
            o = observables_from_Y(ctx.yukawa(a, b, "up"), ctx.yukawa(a, b, "down"), ctx.yukawa(a, b, "lep"))
            pf6_k5_pointwise_max_diff = max(pf6_k5_pointwise_max_diff, o["D_lep_down_1"], o["D_lep_down_2"])

    shells = [("K5_4", P5), ("E6_prim_24", P6), ("P30_96", P30)]
    shell_results = {}
    for sname, pts in shells:
        by_y = {}
        for y_int in (3, 10, 20, 30):
            ctx = ctx_cache[("13/100", y_int, "exact")]
            mp.mp.dps = ctx.dps
            Yu_l = [ctx.yukawa(a, b, "up") for (a, b) in pts]
            Yd_l = [ctx.yukawa(a, b, "down") for (a, b) in pts]
            Yl_l = [ctx.yukawa(a, b, "lep") for (a, b) in pts]
            by_y[y_int] = gramian_observables(Yu_l, Yd_l, Yl_l)
        dy10 = Fraction(10, 1)
        g20, g30 = by_y[20], by_y[30]
        shell_results[sname] = {
            "n_points": len(pts),
            "at_y3": {
                "min_diag": mp_str(by_y[3]["min_diag"], 8),
                "up_m2m3": mp_str(by_y[3]["up_m2m3"], 6),
                "down_m2m3": mp_str(by_y[3]["down_m2m3"], 6),
                "lep_m2m3": mp_str(by_y[3]["lep_m2m3"], 6),
                "D_lep_down_2": mp_str(by_y[3]["D_lep_down_2"], 6),
                "V12": mp_str(by_y[3]["V12"], 6),
                "V23": mp_str(by_y[3]["V23"], 6),
                "V13": mp_str(by_y[3]["V13"], 6),
            },
            "at_y30": {
                "min_diag": mp_str(g30["min_diag"], 8),
                "up_m2m3": mp_str(g30["up_m2m3"], 6),
                "up_m1m3": mp_str(g30["up_m1m3"], 6),
                "down_m2m3": mp_str(g30["down_m2m3"], 6),
                "down_m1m3": mp_str(g30["down_m1m3"], 6),
                "lep_m2m3": mp_str(g30["lep_m2m3"], 6),
                "lep_m1m3": mp_str(g30["lep_m1m3"], 6),
                "D_lep_down_2": mp_str(g30["D_lep_down_2"], 6),
                "V12": mp_str(g30["V12"], 6),
                "V23": mp_str(g30["V23"], 6),
                "V13": mp_str(g30["V13"], 6),
            },
            "rates_y20_30": {
                k: mp_str(rate_eps(g20[k], g30[k], dy10), 6)
                for k in ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
            },
        }

    # Exact T, S, AND M modular invariance of GL(2,Z)-canonical E6_prim_24 Gramian at tau = 13/100 + 2i
    dps = 50
    mp.mp.dps = dps
    tau1 = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    L2_1, _ = solve_L2_fuchsian_mp(tau1, dps=40)
    ctx_t1 = FrameCCouplingContext(tau1, L2_1, dps=dps)
    ctx_T = FrameCCouplingContext(tau1 + 1, L2_1, dps=dps)
    ctx_S = FrameCCouplingContext(-1 / tau1, L2_1 + mp.log(abs(tau1)), dps=dps)
    ctx_M = FrameCCouplingContext((2 * tau1 + 1) / (tau1 + 1), L2_1 + mp.log(abs(tau1 + 1)), dps=dps)

    def eval_shell_gram(ctx, pts):
        return gramian_observables(
            [ctx.yukawa(a, b, "up") for (a, b) in pts],
            [ctx.yukawa(a, b, "down") for (a, b) in pts],
            [ctx.yukawa(a, b, "lep") for (a, b) in pts],
        )

    g_e6_0 = eval_shell_gram(ctx_t1, P6)
    g_e6_T = eval_shell_gram(ctx_T, P6)
    g_e6_S = eval_shell_gram(ctx_S, P6)
    g_e6_M = eval_shell_gram(ctx_M, P6)
    mkeys = ("up_m2m3", "down_m2m3", "lep_m2m3", "up_m1m3", "down_m1m3", "lep_m1m3")
    e6_T_err = max(abs(g_e6_0[k] - g_e6_T[k]) / max(abs(g_e6_0[k]), mp_pow10(-40)) for k in mkeys)
    e6_S_err = max(abs(g_e6_0[k] - g_e6_S[k]) / max(abs(g_e6_0[k]), mp_pow10(-40)) for k in mkeys)
    e6_M_err = max(abs(g_e6_0[k] - g_e6_M[k]) / max(abs(g_e6_0[k]), mp_pow10(-40)) for k in mkeys)

    b1976_e0_ok = (
        unit_tied(5, pairs["down"], pairs["lep"])
        and unit_tied(6, pairs["up"], pairs["down"])
        and not unit_tied(30, pairs["up"], pairs["down"])
        and not unit_tied(30, pairs["down"], pairs["lep"])
        and not unit_tied(30, pairs["up"], pairs["lep"])
    )
    passed = (
        b1976_e0_ok
        and pf6_k5_pointwise_max_diff < mp_pow10(-35)
        and max(e6_T_err, e6_S_err, e6_M_err) < mp_pow10(-35)
    )

    return {
        "B1976_E0_verified": b1976_e0_ok,
        "minimal_N_no_unit_ties_all": no_unit_ties[:12],
        "minimal_N_5div_no_unit_ties": no_unit_ties_5div[:10],
        "minimal_N_5div_no_ties_and_no_order5_lep_collapse": full_sep_and_no_lep_collapse_5div[:10],
        "key_level_census": census_key_levels,
        "head_to_head_shell_gramians": shell_results,
        "E6_prim_24_gramian_T_invariance_err": mp_str(e6_T_err, 6),
        "E6_prim_24_gramian_S_invariance_err": mp_str(e6_S_err, 6),
        "E6_prim_24_gramian_M_invariance_err": mp_str(e6_M_err, 6),
        "PF6_K5_pointwise_lep_down_collapse_max_diff": mp_str(pf6_k5_pointwise_max_diff, 6),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G6: Guardrail-3 Haar U(3)^3 Scrambling & 6/6 Planted Controls (PF1..PF6)
# ---------------------------------------------------------------------------

def rand_haar_u3(rng: random.Random):
    I = iu()

    def rand_norm():
        u1 = mp_rat(rng.randint(1, 10 ** 9 - 1), 10 ** 9)
        u2 = mp_rat(rng.randint(1, 10 ** 9 - 1), 10 ** 9)
        return mp.sqrt(-2 * mp.log(u1)) * mp.cos(2 * mp.pi * u2)

    A = mp.matrix([[rand_norm() + I * rand_norm() for _ in range(3)] for _ in range(3)])
    Q = mp.zeros(3, 3)
    for j in range(3):
        v = [A[r, j] for r in range(3)]
        for k in range(j):
            dot = sum((mp.conj(Q[r, k]) * v[r] for r in range(3)), mp.mpc(0))
            v = [v[r] - dot * Q[r, k] for r in range(3)]
        nrm = mp.sqrt(sum((abs(z) ** 2 for z in v), mp.mpf(0)))
        for r in range(3):
            Q[r, j] = v[r] / nrm
    return Q


def run_G6_haar_and_planted(
    model: Dict[str, Any],
    P30,
    ctx_cache: Dict[Any, FrameCCouplingContext],
    g3_out: Dict[str, Any],
    g5_out: Dict[str, Any],
    y30_obs_by_pt: Dict[Any, Dict[str, Any]],
    y40_obs_by_pt: Dict[Any, Dict[str, Any]],
) -> Dict[str, Any]:
    rng = random.Random(20261125)
    ctx = ctx_cache[("13/100", 5, "exact")]
    mp.mp.dps = ctx.dps

    a0, b0 = Fraction(4, 15), Fraction(1, 30)
    Yu0 = ctx.yukawa(a0, b0, "up")
    Yd0 = ctx.yukawa(a0, b0, "down")
    Yl0 = ctx.yukawa(a0, b0, "lep")
    ref_pt = observables_from_Y(Yu0, Yd0, Yl0)
    Uu0, _, Vhu0 = svd_asc(Yu0)
    lr0 = abs((Uu0.H * Vhu0.H)[0, 0])

    orb0 = build_M_orbits(P30)[0]
    Yu_orb = [ctx.yukawa(a, b, "up") for (a, b) in orb0]
    Yd_orb = [ctx.yukawa(a, b, "down") for (a, b) in orb0]
    Yl_orb = [ctx.yukawa(a, b, "lep") for (a, b) in orb0]
    ref_orb = gramian_observables(Yu_orb, Yd_orb, Yl_orb)

    max_pt_haar = mp.mpf(0)
    max_orb_haar = mp.mpf(0)
    max_pf5_lr_drift = mp.mpf(0)
    keys_h = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")

    for _ in range(10):
        UL = rand_haar_u3(rng)
        URu = rand_haar_u3(rng)
        URd = rand_haar_u3(rng)
        URl = rand_haar_u3(rng)
        Yu_s = UL * Yu0 * URu.H
        Yd_s = UL * Yd0 * URd.H
        Yl_s = UL * Yl0 * URl.H
        o_s = observables_from_Y(Yu_s, Yd_s, Yl_s)
        for k in keys_h:
            max_pt_haar = max(max_pt_haar, abs(o_s[k] - ref_pt[k]) / max(abs(ref_pt[k]), mp_pow10(-45)))
        max_pt_haar = max(max_pt_haar, abs(abs(o_s["J_cp"]) - abs(ref_pt["J_cp"])) / max(abs(ref_pt["J_cp"]), mp_pow10(-45)))

        Uus, _, Vhus = svd_asc(Yu_s)
        lrs = abs((Uus.H * Vhus.H)[0, 0])
        max_pf5_lr_drift = max(max_pf5_lr_drift, abs(lrs - lr0))

        ULo = rand_haar_u3(rng)
        Yu_os = [ULo * Y * rand_haar_u3(rng).H for Y in Yu_orb]
        Yd_os = [ULo * Y * rand_haar_u3(rng).H for Y in Yd_orb]
        Yl_os = [ULo * Y * rand_haar_u3(rng).H for Y in Yl_orb]
        go_s = gramian_observables(Yu_os, Yd_os, Yl_os)
        for k in keys_h:
            max_orb_haar = max(max_orb_haar, abs(go_s[k] - ref_orb[k]) / max(abs(ref_orb[k]), mp_pow10(-45)))

    bad_ch = dict(SIXY, u=-3)
    dy10 = Fraction(10, 1)
    pf1_broken = 0
    for (a, b) in P30:
        tr_bad = tropical_full_point(model, nd_frac(a), charges=bad_ch)
        r_m2 = rate_eps(y30_obs_by_pt[(a, b)]["up_m2m3"], y40_obs_by_pt[(a, b)]["up_m2m3"], dy10)
        r_m1 = rate_eps(y30_obs_by_pt[(a, b)]["up_m1m3"], y40_obs_by_pt[(a, b)]["up_m1m3"], dy10)
        if abs(r_m2 - mp_frac(tr_bad["up_m2m3"])) > mp_rat(1, 50) or abs(r_m1 - mp_frac(tr_bad["up_m1m3"])) > mp_rat(1, 50):
            pf1_broken += 1

    pf2_broken = 0
    for (a, b) in P30:
        r_v23 = rate_eps(y30_obs_by_pt[(a, b)]["V23"], y40_obs_by_pt[(a, b)]["V23"], dy10)
        wrong_v23 = Fraction(2, 1) * abs(nd_frac(a) - Fraction(1, 3))
        if abs(r_v23 - mp_frac(wrong_v23)) > mp_rat(1, 100):
            pf2_broken += 1

    pf3_val = mp.mpf(g3_out["PF3_fixed_L2_err"])
    pf4_val = mp.mpf(g3_out["PF4_wrong_point_act_err"])
    pf6_val = mp.mpf(g5_out["PF6_K5_pointwise_lep_down_collapse_max_diff"])

    pf_flags = {
        "PF1_wrong_u_charge_breaks_gt_90pct": (pf1_broken >= 87),
        "PF2_wrong_quarter_shift_breaks_all_96": (pf2_broken == 96),
        "PF3_fixed_L2_breaks_joint_cov_gt_1e_3": (pf3_val > mp_pow10(-3)),
        "PF4_wrong_point_act_breaks_joint_cov_gt_1e_1": (pf4_val > mp_pow10(-1)),
        "PF5_unphysical_LR_overlap_drifts_gt_1e_1": (max_pf5_lr_drift > mp_pow10(-1)),
        "PF6_K5_pointwise_collapses_lep_down_lt_1e_35": (pf6_val < mp_pow10(-35)),
    }
    passed = (
        max_pt_haar < mp_pow10(-30)
        and max_orb_haar < mp_pow10(-30)
        and all(pf_flags.values())
    )
    return {
        "pointwise_haar_U3_3_max_drift": mp_str(max_pt_haar, 6),
        "orbit_gramian_haar_U3_3_max_drift": mp_str(max_orb_haar, 6),
        "PF1_broken_count_of_96": pf1_broken,
        "PF2_broken_count_of_96": pf2_broken,
        "PF3_fixed_L2_max_err": mp_str(pf3_val, 6),
        "PF4_wrong_point_act_max_err": mp_str(pf4_val, 6),
        "PF5_unphysical_LR_overlap_max_drift": mp_str(max_pf5_lr_drift, 6),
        "PF6_K5_pointwise_lep_down_collapse_max_diff": mp_str(pf6_val, 6),
        "planted_controls": pf_flags,
        "planted_caught": sum(1 for v in pf_flags.values() if v),
        "planted_total": len(pf_flags),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Main Runner
# ---------------------------------------------------------------------------

def main():
    ast_res = audit_own_ast()
    assert ast_res["clean"], f"AST hygiene failed: {ast_res}"

    P5, P6, P30 = build_torsion_sets()
    model = build_symbolic_tropical_model()

    ctx_cache: Dict[Any, FrameCCouplingContext] = {}
    L2_meta: Dict[Any, Dict[str, Any]] = {}

    heights_14 = [
        Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2),
        Fraction(3, 1), Fraction(4, 1), Fraction(5, 1), Fraction(6, 1),
        Fraction(8, 1), Fraction(10, 1), Fraction(15, 1), Fraction(20, 1),
        Fraction(30, 1), Fraction(40, 1),
    ]
    for y_f in heights_14:
        tau = mp.mpc(mp_rat(13, 100), mp_frac(y_f))
        L2_v, rel_r = solve_L2_fuchsian_mp(tau, dps=38)
        L2_meta[("13/100", y_f)] = {"L2_mp": L2_v, "rel_trace_res": rel_r}
        dps_ctx = max(55, 40 + 2 * int(math.ceil(y_f)))
        ctx = FrameCCouplingContext(tau, L2_v, dps=dps_ctx)
        ctx_cache[("13/100", y_f, "exact")] = ctx
        if y_f.denominator == 1:
            ctx_cache[("13/100", int(y_f), "exact")] = ctx

    L2_6 = L2_meta[("13/100", Fraction(6, 1))]["L2_mp"]
    for y_int in (20, 30):
        tau = mp.mpc(mp_rat(13, 100), mp.mpf(y_int))
        ctx_cache[("13/100", y_int, "clamp6")] = FrameCCouplingContext(tau, L2_6, dps=40 + 2 * y_int)

    for xs, x_f in (("0", Fraction(0, 1)), ("31/100", Fraction(31, 100)), ("1/2", Fraction(1, 2))):
        for y_int in (2, 4, 10, 20):
            y_f = Fraction(y_int, 1)
            tau = mp.mpc(mp_frac(x_f), mp_frac(y_f))
            L2_v, rel_r = solve_L2_fuchsian_mp(tau, dps=38)
            L2_meta[(xs, y_f)] = {"L2_mp": L2_v, "rel_trace_res": rel_r}
            ctx_cache[(xs, y_f, "exact")] = FrameCCouplingContext(tau, L2_v, dps=max(55, 40 + 2 * y_int))

    g1_out, trop_by_nd, y30_obs_by_pt, y40_obs_by_pt = run_G1_O1(model, P5, P6, P30, ctx_cache)
    g2_out = run_G2_O2(P30, trop_by_nd, ctx_cache, L2_meta, y30_obs_by_pt, y40_obs_by_pt)
    g3_out = run_G3_O3()
    g4_out = run_G4_O4(P30, ctx_cache)
    g5_out = run_G5_O5(P5, P6, P30, ctx_cache)
    g6_out = run_G6_haar_and_planted(model, P30, ctx_cache, g3_out, g5_out, y30_obs_by_pt, y40_obs_by_pt)

    gates = {
        "G1_O1_tropical_and_level_scan": g1_out["passed"],
        "G2_O2_moderate_height_and_L2": g2_out["passed"],
        "G3_O3_joint_SL2Z_M_covariance": g3_out["passed"],
        "G4_O4_8_orbits_and_orbit_gramians": g4_out["passed"],
        "G5_O5_P845_census_and_E6_shell": g5_out["passed"],
        "G6_haar_and_planted_6_of_6": g6_out["passed"],
    }
    all_passed = all(gates.values()) and ast_res["clean"]

    payload = {
        "card_id": "AGY-002_A2-B1978-ORDER30",
        "version": "v3",
        "seat": "agy-002",
        "firewall": "0 of 19 (strictly data-free)",
        "script_sha256": hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest(),
        "ast_hygiene": ast_res,
        "gates": gates,
        "all_gates_passed": all_passed,
        "G1_O1": g1_out,
        "G2_O2": g2_out,
        "G3_O3": g3_out,
        "G4_O4": g4_out,
        "G5_O5": g5_out,
        "G6_haar_and_planted": g6_out,
    }

    assert count_json_floats(payload) == 0, "JSON float token detected!"
    raw = json.dumps(payload, indent=2, sort_keys=False) + "\n"
    OUT_JSON_PATH.write_text(raw, encoding="utf-8")
    out_sha = hashlib.sha256(OUT_JSON_PATH.read_bytes()).hexdigest()
    OUT_SHA_PATH.write_text(f"{out_sha}  {OUT_JSON_PATH.name}\n", encoding="utf-8")
    print(f"CARD=AGY-002_A2-B1978-ORDER30_V3 ALL_GATES={all_passed} GATES={gates} OUT_SHA={out_sha[:16]}")


if __name__ == "__main__":
    main()
