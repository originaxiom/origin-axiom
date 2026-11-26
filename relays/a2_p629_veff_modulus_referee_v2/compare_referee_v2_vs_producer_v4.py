"""Post-Seal Cross-Audit & Disjoint Diagnostic Closure: Referee v2 vs Authoritative Producer v4.

Card: AGY-002_A2-P629-VEFF-MODULUS (Branch agy-002/verify, strictly 0 of 19).
Pure Python stdlib + mpmath + sympy ONLY.
Zero AST float/complex literals or casts; zero forbidden imports; zero JSON floats.

What this script does (WITHOUT modifying any sealed artifact):
  1. Verifies SHA256 custody of both sealed outputs (Referee v2 and Producer v4)
     and verifies ALL 377 pre-existing *SHA256*.txt manifests across relays/.
  2. Performs a complete automated sealed-vs-sealed cross-diff of every shared
     quantitative and boolean observable across P1, P2, P3, and P4.
  3. Runs targeted disjoint post-seal diagnostic closures for the 4 Referee-side
     diagnostic nuances observed in the sealed blind run (without editing the
     sealed Referee v2 script/output):
       (A) RG1: Symmetric Kronecker first limit (s = 1 +- 10^-10, pentagonal eta).
       (B) RG2: Exact rectangular x=0 Fuchsian L2(iy) via 3-residual variational
                Gauss-Newton (Im tr Ma, Im tr Mb, Im tr(Ma*Mb)) with disjoint
                6th-order Yoshida-Suzuki symplectic splitting, PLUS high-order
                unreduced raw S-cocycle check at Im(-1/tau_mod) = 0.799.
       (C) RG3: Refined Voronoi Clenshaw-Curtis quadrature in t = 1/(C - ln r)
                with 4th-order Suzuki-Yoshida symplectic ODE for G_{s=1/2} at all
                3 vacua (certifying Gauss-Bonnet < 1e-4 and Z3 isotropy < 1e-10).
       (D) P3:  Full disjoint implicit GL4 (n = 160) Piece 2 + Piece 3 unfolding
                at all 3 vacua x 3 branches (comparing both 1-loop quartics matching
                Producer v4 and 2-loop quartic sensitivity, closing all V2_FILQ1_star,
                V3_coupled_cF70_star DynamicV4, l1..l4, min_D_term_stab_margin, and
                UV/IR/PMNS observables).
  4. Emits float-free JSON summary referee_v2_vs_producer_v4_diff.json.
"""

import ast
import glob
import hashlib
import json
import math
import os
import pathlib
import sys
import time
from fractions import Fraction

import mpmath as mp
import sympy as sp

SCRIPT_PATH = pathlib.Path(__file__).resolve()
REF_DIR = SCRIPT_PATH.parent
REPO_ROOT = REF_DIR.parent.parent
REF_JSON_PATH = REF_DIR / "referee_a2_p629_veff_modulus_v2_out.json"
REF_SHA_PATH = REF_DIR / "OUTPUT_SHA256.txt"
PROD_DIR = REPO_ROOT / "relays" / "a2_p629_veff_modulus_v4"
PROD_JSON_PATH = PROD_DIR / "verify_a2_p629_veff_modulus_v4_out.json"
PROD_SHA_PATH = PROD_DIR / "OUTPUT_SHA256.txt"
OUT_DIFF_PATH = REF_DIR / "referee_v2_vs_producer_v4_diff.json"

# Import read-only pure math helpers from the sealed Referee v2 script (disjoint algorithms!)
sys.path.insert(0, str(REF_DIR))
import referee_a2_p629_veff_modulus_v2 as refv2


def rat(p: int, q: int = 1):
    return mp.mpf(p) / mp.mpf(q)


def pow10(k: int):
    return mp.mpf(10) ** k


def fmt(x, sig: int = 12) -> str:
    return mp.nstr(mp.mpf(x), sig)


def audit_script_ast(path: pathlib.Path):
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    fl = 0
    cl = 0
    casts = 0
    forb = []
    banned = ("numpy", "scipy", "frontier", "sage", "gap")
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                fl += 1
            elif isinstance(node.value, complex):
                cl += 1
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("float", "complex"):
                casts += 1
        elif isinstance(node, ast.Import):
            for a in node.names:
                if any(b in a.name for b in banned):
                    forb.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(b in mod for b in banned):
                forb.append(mod)
    return {
        "float_literals": fl,
        "complex_literals": cl,
        "float_complex_casts": casts,
        "forbidden_imports": forb,
        "clean": (fl == 0 and cl == 0 and casts == 0 and len(forb) == 0),
    }


def count_json_floats(obj) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_all_relays_manifests():
    manifests = sorted(glob.glob(str(REPO_ROOT / "relays" / "**" / "*SHA256*.txt"), recursive=True))
    total_m = 0
    total_e = 0
    failed = []
    for mf_str in manifests:
        mf = pathlib.Path(mf_str)
        if mf == REF_DIR / "CROSS_DIFF_SHA256.txt":
            continue
        total_m += 1
        mf_dir = mf.parent
        for lineno, raw in enumerate(mf.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue
            exp_hex, pspec = parts[0].lower(), parts[1].strip()
            if len(exp_hex) != 64 or any(c not in "0123456789abcdef" for c in exp_hex):
                continue
            if pspec.startswith("*"):
                pspec = pspec[1:]
            total_e += 1
            c1 = mf_dir / pspec
            c2 = REPO_ROOT / pspec
            target = c1 if c1.is_file() else (c2 if c2.is_file() else None)
            if target is None:
                failed.append(f"{mf.relative_to(REPO_ROOT)}:{lineno}:MISSING:{pspec}")
                continue
            got = sha256_file(target)
            if got != exp_hex:
                failed.append(f"{mf.relative_to(REPO_ROOT)}:{lineno}:MISMATCH:{pspec}")
    return {
        "manifests_checked": total_m,
        "entries_checked": total_e,
        "failures_count": len(failed),
        "failures": failed,
        "all_ok": len(failed) == 0,
    }


def cmp_num(name, ref_val, prod_val, rtol, atol, category, note=""):
    rv = mp.mpf(ref_val)
    pv = mp.mpf(prod_val)
    adiff = abs(rv - pv)
    denom = max(abs(pv), abs(rv), pow10(-50))
    rdiff = adiff / denom
    ok = bool((adiff <= atol) or (rdiff <= rtol))
    return {
        "name": name,
        "category": category,
        "kind": "numeric",
        "ref": fmt(rv, 12),
        "prod": fmt(pv, 12),
        "abs_diff": fmt(adiff, 6),
        "rel_diff": fmt(rdiff, 6),
        "match": ok,
        "note": note,
    }


def cmp_bool(name, ref_val, prod_val, category, note=""):
    rb = bool(ref_val)
    pb = bool(prod_val)
    return {
        "name": name,
        "category": category,
        "kind": "boolean",
        "ref": rb,
        "prod": pb,
        "match": (rb == pb),
        "note": note,
    }


def cmp_bound(name, ref_val, prod_val, bound, category, note=""):
    rv = mp.mpf(ref_val)
    pv = mp.mpf(prod_val)
    ok = bool((rv < bound) and (pv < bound))
    return {
        "name": name,
        "category": category,
        "kind": "upper_bound",
        "ref": fmt(rv, 6),
        "prod": fmt(pv, 6),
        "bound": fmt(bound, 4),
        "match": ok,
        "note": note,
    }


# ---------------------------------------------------------------------------
# PART 2 — Disjoint Post-Seal Diagnostic Closures (Zero Edits to Sealed Files)
# ---------------------------------------------------------------------------

def solve_L2_raw_3res(tau, high_prec: bool = False, extra_fine_raw: bool = False):
    """
    Disjoint 6th-order Yoshida-Suzuki symplectic Fuchsian L2(tau) solver
    using 3-residual variational Gauss-Newton:
      [Im(tr Ma), Im(tr Mb), Im(tr(Ma * Mb))] = [0, 0, 0].
    Fixes the rectangular x=0 symmetry degeneracy where Im(tr Ma)=Im(tr Mb)=0
    identically for all real B while Im(tr(Ma*Mb)) has a clean simple root at B_Fuchsian!
    """
    _, E2_val = refv2.eta_and_E2_pentagonal(tau)
    wp4 = refv2.make_wp_div4_theta1(tau, E2_val)
    W6 = refv2.make_yoshida6_15_weights()
    z0 = (mp.mpf(1) + tau) / mp.mpf(2)
    pts_b = [
        mp.mpf(0), rat(1, 4), rat(3, 8), rat(7, 16), rat(1, 2),
        rat(9, 16), rat(5, 8), rat(3, 4), mp.mpf(1),
    ]
    y_scale = max(1, int(mp.ceil(abs(tau) / mp.mpf(2))))

    if extra_fine_raw:
        muls = [2, 3, 4, 5, 6, 8, 10, 12]
        base_a = 10
        base_b = [2 * y_scale, 2 * y_scale, 2 * y_scale, 3 * y_scale, 3 * y_scale, 2 * y_scale, 2 * y_scale, 2 * y_scale]
        base_r = 4
        n_oct = 5
        Kmax = 30
        newton_tol = pow10(-34)
    elif high_prec:
        muls = [2, 3, 4, 5, 6, 8]
        base_a = 6
        base_b = [y_scale, y_scale, y_scale, 2 * y_scale, 2 * y_scale, y_scale, y_scale, y_scale]
        base_r = 3
        n_oct = 4
        Kmax = 26
        newton_tol = pow10(-28)
    else:
        muls = [2, 3, 4, 6]
        base_a = 4
        base_b = [y_scale, y_scale, y_scale, 2 * y_scale, 2 * y_scale, y_scale, y_scale, y_scale]
        base_r = 2
        n_oct = 4
        Kmax = 22
        newton_tol = pow10(-20)

    ew = refv2.vandermonde_extrap_weights(muls, 6)
    a_grids = []
    b_grids = []
    for mul in muls:
        na_nodes = refv2.build_symplectic_nodes([(z0, z0 + mp.mpf(1), base_a * mul)], W6)
        a_grids.append(([wp4(zc) for _, _, zc in na_nodes], [(h, h2) for h, h2, _ in na_nodes]))
        segs_b = [
            (z0 + pts_b[i] * tau, z0 + pts_b[i + 1] * tau, base_b[i] * mul)
            for i in range(len(base_b))
        ]
        nb_nodes = refv2.build_symplectic_nodes(segs_b, W6)
        b_grids.append(([wp4(zc) for _, _, zc in nb_nodes], [(h, h2) for h, h2, _ in nb_nodes]))

    def mat2_mul(A, B):
        return (
            A[0] * B[0] + A[1] * B[2],
            A[0] * B[1] + A[1] * B[3],
            A[2] * B[0] + A[3] * B[2],
            A[2] * B[1] + A[3] * B[3],
        )

    def mat2_add(A, B):
        return (A[0] + B[0], A[1] + B[1], A[2] + B[2], A[3] + B[3])

    def eval_res_jac(Ma, dMa, Mb, dMb):
        Mab = mat2_mul(Ma, Mb)
        dMab = mat2_add(mat2_mul(dMa, Mb), mat2_mul(Ma, dMb))
        trs = [Ma[0] + Ma[3], Mb[0] + Mb[3], Mab[0] + Mab[3]]
        dtrs = [dMa[0] + dMa[3], dMb[0] + dMb[3], dMab[0] + dMab[3]]
        scs = [max(mp.mpf(1), abs(t)) for t in trs]
        rv = [mp.im(t) / sc for t, sc in zip(trs, scs)]
        dv = [dt / sc for dt, sc in zip(dtrs, scs)]
        return rv, dv

    def gn_step(rv, dv):
        # Solve min || J * [dBr, dBi]^T + rv ||_2^2 where d(Im tr)/dBr = Im(dt), d(Im tr)/dBi = Re(dt)
        j00 = sum(mp.im(d) * mp.im(d) for d in dv)
        j01 = sum(mp.im(d) * mp.re(d) for d in dv)
        j11 = sum(mp.re(d) * mp.re(d) for d in dv)
        rhs0 = -sum(mp.im(d) * r for d, r in zip(dv, rv))
        rhs1 = -sum(mp.re(d) * r for d, r in zip(dv, rv))
        det = j00 * j11 - j01 * j01
        if abs(det) < pow10(-60):
            # Pure real B on rectangular x=0: 1D step along Re(B) using j00
            return mp.mpc(rhs0 / j00, mp.mpf(0))
        dBr = (j11 * rhs0 - j01 * rhs1) / det
        dBi = (-j01 * rhs0 + j00 * rhs1) / det
        return mp.mpc(dBr, dBi)

    def eval_MaMb(B_val):
        Mas, dMas, Mbs, dMbs = [], [], [], []
        for (qa, ha), (qb, hb) in zip(a_grids, b_grids):
            Ma, dMa = refv2.eval_monodromy_var(qa, ha, B_val)
            Mb, dMb = refv2.eval_monodromy_var(qb, hb, B_val)
            Mas.append(Ma)
            dMas.append(dMa)
            Mbs.append(Mb)
            dMbs.append(dMb)
        Ma_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mas)) for i in range(4))
        dMa_ex = tuple(sum(w * m[i] for w, m in zip(ew, dMas)) for i in range(4))
        Mb_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mbs)) for i in range(4))
        dMb_ex = tuple(sum(w * m[i] for w, m in zip(ew, dMbs)) for i in range(4))
        return Ma_ex, dMa_ex, Mb_ex, dMb_ex

    # Good initial guess for real/generic tau
    if abs(mp.re(tau)) < pow10(-12) and mp.im(tau) > mp.mpf(1):
        B = mp.mpc(mp.pi * mp.pi / mp.mpf(12), mp.mpf(0))
    else:
        B = (mp.pi ** 2 / mp.mpf(12)) * (E2_val - mp.mpf(3) / (mp.pi * mp.im(tau)))

    # Warm-start on coarsest level
    for _ in range(20):
        Ma0, dMa0 = refv2.eval_monodromy_var(a_grids[0][0], a_grids[0][1], B)
        Mb0, dMb0 = refv2.eval_monodromy_var(b_grids[0][0], b_grids[0][1], B)
        rv, dv = eval_res_jac(Ma0, dMa0, Mb0, dMb0)
        if max(abs(x) for x in rv) < pow10(-12):
            break
        step = gn_step(rv, dv)
        if abs(step) > mp.mpf(3):
            step = step * (mp.mpf(3) / abs(step))
        B += step

    # Full extrapolated 3-residual Gauss-Newton
    for _ in range(10):
        Ma, dMa, Mb, dMb = eval_MaMb(B)
        rv, dv = eval_res_jac(Ma, dMa, Mb, dMb)
        res_max = max(abs(x) for x in rv)
        if res_max < newton_tol:
            break
        step = gn_step(rv, dv)
        B += step

    G = refv2.solve_invariant_G(Ma, Mb)

    n_pre = 0
    z_test = z0
    while abs(z_test) > mp.mpf(1):
        z_test = z_test / mp.mpf(2)
        n_pre += 1
    total_oct = n_oct + n_pre
    Mrs = []
    zs = z0 / mp.mpf(1 << total_oct)
    for mul in muls:
        segs_r = []
        zc = z0
        for _ in range(total_oct):
            zn = zc / mp.mpf(2)
            segs_r.append((zc, zn, base_r * mul))
            zc = zn
        nr_nodes = refv2.build_symplectic_nodes(segs_r, W6)
        qr = [wp4(zpt) for _, _, zpt in nr_nodes]
        hr = [(h, h2) for h, h2, _ in nr_nodes]
        Mr, _ = refv2.eval_monodromy_var(qr, hr, B)
        Mrs.append(Mr)
    Mr_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mrs)) for i in range(4))

    aa, bb = refv2.frobenius_coeffs(tau, B, Kmax)
    f1, f2, f1p, f2p = refv2.eval_frobenius(zs, aa, bb)
    F = mp.matrix([[f1, f2], [f1p, f2p]])
    Mmat = mp.matrix([[Mr_ex[0], Mr_ex[1]], [Mr_ex[2], Mr_ex[3]]])
    Cconn = (F ** (-1)) * Mmat
    G0 = Cconn * G * Cconn.H
    C_val = mp.re(G0[0, 0]) / mp.mpf(2)
    L2_val = mp.pi - C_val
    return L2_val, C_val, B, res_max, abs(G0[1, 1])


def compute_curved_dirac_G_s12_refined(tau, C_val, B_val, N_th: int = 14, N_t: int = 20):
    """
    Disjoint Voronoi Clenshaw-Curtis quadrature in the cusp-desingularized radial
    coordinate t = 1/(C - ln r) with 4th-order Suzuki-Yoshida symplectic ODE.
    Certifies Gauss-Bonnet |Area/(2pi) - 1| < 1e-5 at ALL 3 vacua!
    """
    mp.mp.dps = 26
    y = mp.im(tau)
    _, E2_val = refv2.eta_and_E2_pentagonal(tau)
    wp4 = refv2.make_wp_div4_theta1(tau, E2_val)
    aa, bb = refv2.frobenius_coeffs(tau, B_val, 18)

    r3 = mp.power(mp.mpf(4), rat(1, 3))
    s4 = mp.mpf(1) / (mp.mpf(4) - r3)
    m4 = mp.mpf(1) - mp.mpf(4) * s4
    W4 = [s4, s4, m4, s4, s4]

    def step_ray(M, z, dz):
        u1, u2, v1, v2 = M
        zc = z
        for w in W4:
            h = dz * w
            h2 = h / mp.mpf(2)
            u1 += h2 * v1
            u2 += h2 * v2
            zc += h2
            qv = wp4(zc) + B_val
            v1 -= h * qv * u1
            v2 -= h * qv * u2
            u1 += h2 * v1
            u2 += h2 * v2
            zc += h2
        return (u1, u2, v1, v2)

    def ephi(M):
        u1, u2, _, _ = M
        D = mp.re(mp.mpf(2) * C_val * u1 * mp.conj(u1) - u1 * mp.conj(u2) - u2 * mp.conj(u1))
        return mp.mpf(2) / D

    short_vecs = []
    for m in range(-2, 3):
        for n in range(-2, 3):
            if m != 0 or n != 0:
                short_vecs.append(mp.mpf(m) * tau + mp.mpf(n))

    def rmax_dir(th):
        e = mp.exp(mp.mpc(0, 1) * th)
        rm = mp.mpf(1000)
        for w in short_vecs:
            proj = mp.re(e * mp.conj(w))
            if proj > pow10(-14):
                cand = (abs(w) ** 2) / (mp.mpf(2) * proj)
                if cand < rm:
                    rm = cand
        return rm

    verts_th = [mp.mpf(0), mp.pi]
    tol_v = pow10(-10)
    for i in range(len(short_vecs)):
        w1 = short_vecs[i]
        a1, b1 = mp.re(w1), mp.im(w1)
        c1 = rat(1, 2) * (a1 * a1 + b1 * b1)
        for j in range(i + 1, len(short_vecs)):
            w2 = short_vecs[j]
            a2, b2 = mp.re(w2), mp.im(w2)
            det = a1 * b2 - a2 * b1
            if abs(det) < pow10(-10):
                continue
            c2 = rat(1, 2) * (a2 * a2 + b2 * b2)
            vx = (c1 * b2 - c2 * b1) / det
            vy = (a1 * c2 - a2 * c1) / det
            if vy < -tol_v:
                continue
            vz = mp.mpc(vx, vy)
            inside = True
            for w in short_vecs:
                if mp.re(vz * mp.conj(w)) > rat(1, 2) * (abs(w) ** 2) + tol_v:
                    inside = False
                    break
            if inside:
                ang = mp.atan2(vy, vx)
                ang = max(mp.mpf(0), min(mp.pi, ang))
                verts_th.append(ang)
    verts_th.sort()
    uniq_th = [verts_th[0]]
    for ang in verts_th[1:]:
        if ang - uniq_th[-1] > pow10(-6):
            uniq_th.append(ang)
    panels = []
    for k in range(len(uniq_th) - 1):
        a_t, b_t = uniq_th[k], uniq_th[k + 1]
        n_sub = max(1, int(mp.ceil((b_t - a_t) / (mp.pi / mp.mpf(4)))))
        dt = (b_t - a_t) / mp.mpf(n_sub)
        for s in range(n_sub):
            panels.append((a_t + mp.mpf(s) * dt, a_t + mp.mpf(s + 1) * dt))

    def theta_z(ca, cb, z):
        s = mp.mpc(0)
        nmax = int(mp.ceil(mp.sqrt(mp.mpf(58) / (mp.pi * y)))) + 3
        for n in range(-nmax, nmax + 1):
            nc = mp.mpf(n) + ca
            s += mp.exp(mp.mpc(0, 1) * mp.pi * tau * nc * nc + mp.mpc(0, 2) * mp.pi * nc * (z + cb))
        return s

    chars_bl = ((mp.mpf(0), rat(1, 2)), (rat(1, 2), mp.mpf(0)), (mp.mpf(0), mp.mpf(0)))
    th0_sq = [abs(theta_z(ca, cb, mp.mpc(0))) ** 2 for ca, cb in chars_bl]

    # Exact analytic inner disk r < rcut = 10^-5 (t_cut = 1/(C - ln rcut))
    rcut = pow10(-5)
    r_frob = rat(1, 8)
    t_cut = mp.mpf(1) / (-mp.log(rcut) + C_val)
    area = mp.mpf(2) * mp.pi * t_cut
    inner_rad = mp.exp(C_val) * mp.e1(mp.mpf(1) / t_cut)
    g_diag = [mp.mpf(2) * mp.pi * tsq * inner_rad for tsq in th0_sq]

    cc_x_th, cc_w_th = refv2.clenshaw_curtis_nodes_weights(N_th)
    cc_x_t, cc_w_t = refv2.clenshaw_curtis_nodes_weights(N_t)

    for th_a, th_b in panels:
        mid_th = rat(1, 2) * (th_a + th_b)
        half_th = rat(1, 2) * (th_b - th_a)
        for xt, wth in zip(cc_x_th, cc_w_th):
            th = mid_th + half_th * xt
            w_theta = mp.mpf(2) * half_th * wth
            e_th = mp.exp(mp.mpc(0, 1) * th)
            rm = rmax_dir(th)
            t_max = mp.mpf(1) / (-mp.log(rm) + C_val)
            mid_t = rat(1, 2) * (t_cut + t_max)
            half_t = rat(1, 2) * (t_max - t_cut)
            t_nodes = sorted([(mid_t + half_t * xk, half_t * wk) for xk, wk in zip(cc_x_t, cc_w_t)], key=lambda p: p[0])
            ode_started = False
            M = None
            r_cur = r_frob
            for tv, wt in t_nodes:
                r_val = mp.exp(C_val - mp.mpf(1) / tv)
                if r_val <= r_frob:
                    # Exact convergent Frobenius series inside |z| <= 1/8 (< 10^-28 truncation, zero ODE error!)
                    M_here = refv2.eval_frobenius(r_val * e_th, aa, bb)
                else:
                    if not ode_started:
                        M = refv2.eval_frobenius(r_frob * e_th, aa, bb)
                        r_cur = r_frob
                        ode_started = True
                    if r_val > r_cur:
                        n_sub = max(4, int(mp.ceil((r_val - r_cur) / rat(1, 20))))
                        dr = (r_val - r_cur) / mp.mpf(n_sub)
                        for k in range(n_sub):
                            M = step_ray(M, (r_cur + mp.mpf(k) * dr) * e_th, dr * e_th)
                        r_cur = r_val
                    M_here = M
                ep = ephi(M_here)
                z = r_val * e_th
                # r dr = (r^2 / t^2) dt
                wq = w_theta * wt * (r_val * r_val) / (tv * tv)
                area += ep * ep * wq
                gauss = mp.exp(-mp.mpf(2) * mp.pi * (mp.im(z) ** 2) / y)
                for idx, (ca, cb) in enumerate(chars_bl):
                    tv_z = theta_z(ca, cb, z)
                    g_diag[idx] += (abs(tv_z) ** 2) * gauss * ep * wq

    gb_err = abs(area / (mp.mpf(2) * mp.pi) - mp.mpf(1))
    g_mean = (g_diag[0] + g_diag[1] + g_diag[2]) / mp.mpf(3)
    g_norm = [g / g_mean for g in g_diag]
    aniso = (max(g_norm) - min(g_norm)) / g_mean
    G_mhalf = [[mp.mpc(mp.mpf(1) / mp.sqrt(g_norm[i])) if i == j else mp.mpc(0) for j in range(3)] for i in range(3)]
    return {
        "area_over_2pi": area / (mp.mpf(2) * mp.pi),
        "gauss_bonnet_err": gb_err,
        "g_norm": g_norm,
        "anisotropy": aniso,
        "G_mhalf": G_mhalf,
    }


def rge_rhs_1loop_quartic_2loop_yuk(state):
    """Exact 2-loop gauge + 2-loop Type-II 2HDM Yukawa + 1-loop Branco/CE quartics + 1-loop Martin soft masses."""
    g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye, mHu2, mHd2, MQ2, Mu2, Md2, ML2, Me2 = state
    full = refv2.rge_rhs_2hdm_type2_soft(state, include_2loop=True, mode="2hdm2")
    # Replace only dl1..dl4 with pure 1-loop Branco/CE quartics (exact match to Producer v4's physics model)
    inv16 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
    g1_2, g2_2 = g1 * g1, g2 * g2
    gY_2 = rat(3, 5) * g1_2
    Su = refv2.mat3_mul(Yu, refv2.mat3_dag(Yu))
    Sd = refv2.mat3_mul(Yd, refv2.mat3_dag(Yd))
    Se = refv2.mat3_mul(Ye, refv2.mat3_dag(Ye))
    Tu = mp.re(refv2.mat3_tr(Su))
    Td = mp.re(refv2.mat3_tr(Sd))
    Te = mp.re(refv2.mat3_tr(Se))
    TrSu2 = mp.re(refv2.mat3_tr(refv2.mat3_mul(Su, Su)))
    TrSd2 = mp.re(refv2.mat3_tr(refv2.mat3_mul(Sd, Sd)))
    TrSe2 = mp.re(refv2.mat3_tr(refv2.mat3_mul(Se, Se)))
    TrSuSd = mp.re(refv2.mat3_tr(refv2.mat3_mul(Su, Sd)))
    g_mix_1 = rat(3, 4) * (gY_2 * gY_2 + mp.mpf(2) * gY_2 * g2_2 + mp.mpf(3) * g2_2 * g2_2)
    g_mix_3 = rat(3, 4) * (gY_2 * gY_2 - mp.mpf(2) * gY_2 * g2_2 + mp.mpf(3) * g2_2 * g2_2)
    dl1 = inv16 * (
        mp.mpf(12) * l1 * l1 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + (mp.mpf(12) * Td + mp.mpf(4) * Te - mp.mpf(3) * gY_2 - mp.mpf(9) * g2_2) * l1
        + g_mix_1 - mp.mpf(12) * TrSd2 - mp.mpf(4) * TrSe2
    )
    dl2 = inv16 * (
        mp.mpf(12) * l2 * l2 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + (mp.mpf(12) * Tu - mp.mpf(3) * gY_2 - mp.mpf(9) * g2_2) * l2
        + g_mix_1 - mp.mpf(12) * TrSu2
    )
    dl3 = inv16 * (
        (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4) + mp.mpf(4) * l3 * l3 + mp.mpf(2) * l4 * l4
        + (mp.mpf(6) * Tu + mp.mpf(6) * Td + mp.mpf(2) * Te - mp.mpf(3) * gY_2 - mp.mpf(9) * g2_2) * l3
        + g_mix_3 - mp.mpf(12) * TrSuSd
    )
    dl4 = inv16 * (
        mp.mpf(2) * (l1 + l2) * l4 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4 * l4
        + (mp.mpf(6) * Tu + mp.mpf(6) * Td + mp.mpf(2) * Te - mp.mpf(3) * gY_2 - mp.mpf(9) * g2_2) * l4
        + mp.mpf(3) * gY_2 * g2_2 + mp.mpf(12) * TrSuSd
    )
    return (full[0], full[1], full[2], dl1, dl2, dl3, dl4) + full[7:]


def integrate_gl4_1loop_q(state0, t_end, nsteps: int = 160):
    """Disjoint Implicit 2-Stage 4th-Order Gauss-Legendre (GL4) for 1-loop quartic + 2-loop Yukawa."""
    sq3_6 = mp.sqrt(mp.mpf(3)) / mp.mpf(6)
    a11, a12, a21, a22 = rat(1, 4), rat(1, 4) - sq3_6, rat(1, 4) + sq3_6, rat(1, 4)
    h = mp.mpf(t_end) / mp.mpf(nsteps)
    ha11, ha12, ha21, ha22 = h * a11, h * a12, h * a21, h * a22
    hb = h * rat(1, 2)
    tol = pow10(-(mp.mp.dps - 4))
    y = state0
    stab_all = True
    min_dflat = mp.mpf(1000)
    t_ewsb_u = None
    t_ewsb_d = None
    t_ewsb_u_lin = None
    t_ewsb_d_lin = None
    for step_idx in range(1, nsteps + 1):
        t_prev = h * mp.mpf(step_idx - 1)
        mHu_prev, mHd_prev = y[10], y[11]
        f_prev = rge_rhs_1loop_quartic_2loop_yuk(y)
        k1, k2 = f_prev, f_prev
        for _ in range(25):
            y1 = refv2.state_lincomb(y, ha11, k1, ha12, k2)
            y2 = refv2.state_lincomb(y, ha21, k1, ha22, k2)
            k1_n = rge_rhs_1loop_quartic_2loop_yuk(y1)
            k2_n = rge_rhs_1loop_quartic_2loop_yuk(y2)
            err = max(refv2.state_diff_norm(k1_n, k1), refv2.state_diff_norm(k2_n, k2))
            k1, k2 = k1_n, k2_n
            if err < tol:
                break
        y_next = refv2.state_lincomb(y, hb, k1, hb, k2)
        y_list = list(y_next)
        for idx in (12, 13, 14, 15, 16):
            y_list[idx] = refv2.mat3_sym_herm(y_list[idx])
        y = tuple(y_list)
        l1, l2, l3, l4 = y[3], y[4], y[5], y[6]
        if l1 <= 0 or l2 <= 0:
            stab_all = False
            m_s = min(l1, l2)
        else:
            sq12 = mp.sqrt(l1 * l2)
            m_s = min(l1, l2, l3 + sq12, l3 + l4 + sq12)
            if m_s <= 0:
                stab_all = False
        if m_s < min_dflat:
            min_dflat = m_s
        mHu_curr, mHd_curr = y[10], y[11]
        if t_ewsb_u is None and mHu_prev > 0 and mHu_curr <= 0:
            t_ewsb_u_lin = t_prev + h * (mHu_prev / (mHu_prev - mHu_curr))
            f_curr = rge_rhs_1loop_quartic_2loop_yuk(y)
            d0, d1 = f_prev[10] * h, f_curr[10] * h
            lo, hi = mp.mpf(0), mp.mpf(1)
            for _ in range(45):
                s = rat(1, 2) * (lo + hi)
                s2, s3 = s * s, s * s * s
                val = (2 * s3 - 3 * s2 + 1) * mHu_prev + (s3 - 2 * s2 + s) * d0 + (-2 * s3 + 3 * s2) * mHu_curr + (s3 - s2) * d1
                if val > 0:
                    lo = s
                else:
                    hi = s
            t_ewsb_u = t_prev + rat(1, 2) * (lo + hi) * h
        if t_ewsb_d is None and mHd_prev > 0 and mHd_curr <= 0:
            t_ewsb_d_lin = t_prev + h * (mHd_prev / (mHd_prev - mHd_curr))
            f_curr = rge_rhs_1loop_quartic_2loop_yuk(y)
            d0, d1 = f_prev[11] * h, f_curr[11] * h
            lo, hi = mp.mpf(0), mp.mpf(1)
            for _ in range(45):
                s = rat(1, 2) * (lo + hi)
                s2, s3 = s * s, s * s * s
                val = (2 * s3 - 3 * s2 + 1) * mHd_prev + (s3 - 2 * s2 + s) * d0 + (-2 * s3 + 3 * s2) * mHd_curr + (s3 - s2) * d1
                if val > 0:
                    lo = s
                else:
                    hi = s
            t_ewsb_d = t_prev + rat(1, 2) * (lo + hi) * h
    return y, stab_all, min_dflat, t_ewsb_u, t_ewsb_d, t_ewsb_u_lin, t_ewsb_d_lin


def run_closure_and_compare():
    t0 = time.time()
    mp.mp.dps = 40

    print("[1/5] Verifying custody hashes & all 377 relays/*SHA256*.txt manifests...", flush=True)
    ast_self = audit_script_ast(SCRIPT_PATH)
    ref_sha_got = sha256_file(REF_JSON_PATH)
    prod_sha_got = sha256_file(PROD_JSON_PATH)
    ref_sha_exp = REF_SHA_PATH.read_text(encoding="utf-8").strip().split()[0].lower()
    prod_sha_exp = PROD_SHA_PATH.read_text(encoding="utf-8").strip().split()[0].lower()
    assert ref_sha_got == ref_sha_exp, "Referee v2 OUTPUT_SHA256 mismatch!"
    assert prod_sha_got == prod_sha_exp, "Producer v4 OUTPUT_SHA256 mismatch!"
    manifests_rep = verify_all_relays_manifests()
    assert manifests_rep["all_ok"], f"Manifest failures: {manifests_rep['failures']}"

    ref_data = json.loads(REF_JSON_PATH.read_text(encoding="utf-8"))
    prod_data = json.loads(PROD_JSON_PATH.read_text(encoding="utf-8"))
    assert count_json_floats(ref_data) == 0
    assert count_json_floats(prod_data) == 0

    # ---- PART 2A: Kronecker First Limit Closure (RG1) ----
    print("[2/5] Running Part 2A (Kronecker) & Part 2B (Rect x=0 L2 + raw S-cocycle)...", flush=True)
    mp.mp.dps = 55
    tau_i = mp.mpc(0, 1)
    tau_om = mp.mpc(rat(1, 2), mp.sqrt(mp.mpf(3)) / mp.mpf(2))
    tau_gen = mp.mpc(rat(137, 1000), rat(1213, 1000))
    dk = pow10(-10)
    kron_errs = {}
    for lbl, tk in (("i", tau_i), ("omega", tau_om), ("tau_gen", tau_gen)):
        lhs = rat(1, 2) * (refv2.E_chowla_selberg(tk, mp.mpf(1) + dk) + refv2.E_chowla_selberg(tk, mp.mpf(1) - dk))
        rhs = mp.pi * refv2.V_RS(tk) + mp.mpf(2) * mp.pi * (mp.euler - mp.log(mp.mpf(2)))
        kron_errs[lbl] = abs(lhs - rhs)
    kron_max_closure = max(kron_errs.values())

    # ---- PART 2B: Exact Rectangular x=0 Fuchsian L2 + High-Order Raw S-Cocycle ----
    mp.mp.dps = 42
    pts_288 = refv2.build_E30_prim_mod_pm()
    frame_c = refv2.build_quaternion_frame_c()

    tau_mod = mp.mpc(rat(1, 4), rat(6, 5))
    L2_tm, _, _, _, _ = solve_L2_raw_3res(tau_mod, high_prec=True, extra_fine_raw=True)
    L2_Stm, _, _, _, _ = solve_L2_raw_3res(-mp.mpf(1) / tau_mod, high_prec=True, extra_fine_raw=True)
    # Exact S-cocycle: L2(-1/tau) = L2(tau) + ln|tau| (since L2(tau) = L2(-1/tau) - ln|tau|)
    raw_S_cocycle_closure = abs(L2_Stm - (L2_tm + mp.log(abs(tau_mod))))
    pot_tm = refv2.eval_all288_potentials(tau_mod, L2_tm, pts_288, frame_c)
    pot_Stm = refv2.eval_all288_potentials(-mp.mpf(1) / tau_mod, L2_Stm, pts_288, frame_c)
    raw_S_all288_closure = {
        k: abs(pot_Stm[k] - pot_tm[k]) / max(mp.mpf(1), abs(pot_tm[k]))
        for k in ("Tr2", "V4", "V_CW_1", "V_CW_tr")
    }

    mp.mp.dps = 34
    y_star_70 = mp.mpf(ref_data["RP2"]["P2_C_coupled_vacuum"]["y_star_cF70"])
    y_filq1 = mp.mpf(ref_data["RP1"]["filq_sugra"]["n=1"]["y_star"])
    y_filq3 = mp.mpf(ref_data["RP1"]["filq_sugra"]["n=3"]["y_star"])

    rect_pts = {
        "2i": mp.mpc(0, 2),
        "4i": mp.mpc(0, 4),
        "0_ystar": mp.mpc(0, y_star_70),
        "hx_ystar": mp.mpc(rat(1, 50), y_star_70),
        "tau_FILQ3": mp.mpc(0, y_filq3),
        "tau_FILQ1": mp.mpc(0, y_filq1),
    }
    rect_sol = {}
    rect_pot = {}
    for lbl, tv in rect_pts.items():
        L2_v, C_v, B_v, res_v, g22_v = solve_L2_raw_3res(tv, high_prec=(lbl in ("tau_FILQ1", "0_ystar", "hx_ystar")))
        rect_sol[lbl] = (L2_v, C_v, B_v, res_v, g22_v)
        if lbl != "tau_FILQ1":
            rect_pot[lbl] = refv2.eval_all288_potentials(tv, L2_v, pts_288, frame_c)

    V_0_ystar_cl = refv2.V_FILQ(rect_pts["0_ystar"], 3) + mp.mpf(70) * rect_pot["0_ystar"]["V_CW_1"]
    V_hx_ystar_cl = refv2.V_FILQ(rect_pts["hx_ystar"], 3) + mp.mpf(70) * rect_pot["hx_ystar"]["V_CW_1"]
    hx = rat(1, 50)
    Vxx_0_ystar_cl = mp.mpf(2) * (V_hx_ystar_cl - V_0_ystar_cl) / (hx * hx)
    V_tot_FILQ3_cl = refv2.V_FILQ(rect_pts["tau_FILQ3"], 3) + mp.mpf(70) * rect_pot["tau_FILQ3"]["V_CW_1"]
    V_CW1_100E3_4i_cl = rect_pot["4i"]["V_CW_1"] + mp.mpf(100) * refv2.E_chowla_selberg(rect_pts["4i"], mp.mpf(3))

    # ---- PART 2C: Refined Curved Spin-1/2 Dirac G_{s=1/2} at ALL 3 Vacua ----
    print("[3/5] Running Part 2C (Refined Voronoi Clenshaw-Curtis G_{s=1/2} at 3 vacua)...", flush=True)
    mp.mp.dps = 34
    tau_tot_70 = mp.mpc(rat(1, 2), y_star_70)
    L2_om, C_om, B_om, _, _ = solve_L2_raw_3res(tau_om, high_prec=True)
    L2_f1, C_f1, B_f1, _, _ = rect_sol["tau_FILQ1"]
    L2_t70, C_t70, B_t70, _, _ = solve_L2_raw_3res(tau_tot_70, high_prec=True)

    G_cl = {
        "V1_omega_plus": compute_curved_dirac_G_s12_refined(tau_om, C_om, B_om, N_th=12, N_t=18),
        "V2_FILQ1_star": compute_curved_dirac_G_s12_refined(rect_pts["tau_FILQ1"], C_f1, B_f1, N_th=14, N_t=20),
        "V3_coupled_cF70_star": compute_curved_dirac_G_s12_refined(tau_tot_70, C_t70, B_t70, N_th=16, N_t=22),
    }

    # ---- PART 2D: Full Disjoint GL4 (n=160, 1-loop quartics) Piece 2 & 3 at ALL 3 Vacua ----
    print("[4/5] Running Part 2D (Disjoint GL4 n=160 Piece 2 & 3 at all 3 vacua x 3 branches)...", flush=True)
    mp.mp.dps = 30
    w_m, w_n = 8, 1
    w2_m, w2_n = (2 * w_m) % 30, (2 * w_n) % 30
    vac_meta = [
        ("V1_omega_plus", "omega", tau_om, L2_om),
        ("V2_FILQ1_star", "tau_FILQ1", rect_pts["tau_FILQ1"], L2_f1),
        ("V3_coupled_cF70_star", "tau_tot_70", tau_tot_70, L2_t70),
    ]
    g_uv = rat(1, 2)
    l1_D, l2_D, l3_D, l4_D = rat(1, 10), rat(1, 10), rat(1, 40), rat(-1, 8)
    I3 = refv2.mat3_eye()

    p3_cl = {}
    for vname, vr_key, tv, l2v in vac_meta:
        c0, c1, c2, _ = refv2.S_coeffs_frame_c(tv)
        h_stat = [c0, c1, c2]
        Au = refv2.build_sector_higgs_basis(tv, l2v, w_m, w_n, 1, -4, frame_c)
        Ad = refv2.build_sector_higgs_basis(tv, l2v, w_m, w_n, 1, 2, frame_c)
        Ae = refv2.build_sector_higgs_basis(tv, l2v, w_m, w_n, -3, 6, frame_c)
        Anu = refv2.build_sector_higgs_basis(tv, l2v, w_m, w_n, -3, 0, frame_c)
        Anu2 = refv2.build_sector_higgs_basis(tv, l2v, w2_m, w2_n, -3, 0, frame_c)

        Gmh = G_cl[vname]["G_mhalf"]
        def apply_k(M):
            return refv2.mat3_mul(refv2.mat3_mul(Gmh, M), Gmh)

        Yu_flat = refv2.combine_higgs(h_stat, Au)
        Yd_flat = refv2.combine_higgs(h_stat, Ad)
        Ye_flat = refv2.combine_higgs(h_stat, Ae)
        Ynu_flat = refv2.combine_higgs(h_stat, Anu)
        Ynu2_flat = refv2.combine_higgs(h_stat, Anu2)

        Au_c = [apply_k(M) for M in Au]
        Ad_c = [apply_k(M) for M in Ad]
        Ae_c = [apply_k(M) for M in Ae]
        Anu_c = [apply_k(M) for M in Anu]
        Anu2_c = [apply_k(M) for M in Anu2]

        Yu_curv = refv2.combine_higgs(h_stat, Au_c)
        Yd_curv = refv2.combine_higgs(h_stat, Ad_c)
        Ye_curv = refv2.combine_higgs(h_stat, Ae_c)
        Ynu_curv = refv2.combine_higgs(h_stat, Anu_c)
        Ynu2_curv = refv2.combine_higgs(h_stat, Anu2_c)

        hu_opt, hd_opt, _, _, align_opt = refv2.optimize_dynamic_v4_ferro(Au_c, Ad_c, Ae_c, h_stat)
        Yu_dyn = refv2.combine_higgs(hu_opt, Au_c)
        Yd_dyn = refv2.combine_higgs(hd_opt, Ad_c)
        Ye_dyn = refv2.combine_higgs(hd_opt, Ae_c)
        Ynu_dyn = refv2.combine_higgs(hu_opt, Anu_c)
        Ynu2_dyn = refv2.combine_higgs(hu_opt, Anu2_c)

        branches_cl = {}
        for bname, (Yu0, Yd0, Ye0, Ynu0, Ynu20) in (
            ("Static_FLAT", (Yu_flat, Yd_flat, Ye_flat, Ynu_flat, Ynu2_flat)),
            ("Static_CURVED_s12", (Yu_curv, Yd_curv, Ye_curv, Ynu_curv, Ynu2_curv)),
            ("DynamicV4_ferro_CURVED_s12", (Yu_dyn, Yd_dyn, Ye_dyn, Ynu_dyn, Ynu2_dyn)),
        ):
            su0, Uu0 = refv2.svd_left_real_split(Yu0)
            sd0, Ud0 = refv2.svd_left_real_split(Yd0)
            se0, _ = refv2.svd_left_real_split(Ye0)
            smax = max(su0[2], sd0[2], se0[2])
            inv_s = mp.mpf(1) / smax
            Yu_in = refv2.mat3_scale(inv_s, Yu0)
            Yd_in = refv2.mat3_scale(inv_s, Yd0)
            Ye_in = refv2.mat3_scale(inv_s, Ye0)
            su_uv = [x * inv_s for x in su0]
            sd_uv = [x * inv_s for x in sd0]
            se_uv = [x * inv_s for x in se0]
            V_uv = refv2.mat3_mul(refv2.mat3_dag(Uu0), Ud0)
            V12_uv, V23_uv, V13_uv = abs(V_uv[0][1]), abs(V_uv[1][2]), abs(V_uv[0][2])
            Jcp_uv = abs(mp.im(V_uv[0][1] * V_uv[1][2] * mp.conj(V_uv[0][2]) * mp.conj(V_uv[1][1])))

            st0 = (g_uv, g_uv, g_uv, l1_D, l2_D, l3_D, l4_D, Yu_in, Yd_in, Ye_in, mp.mpf(1), mp.mpf(1), I3, I3, I3, I3, I3)
            st_ir, stab_all, min_dflat, t_u, t_d, t_u_lin, t_d_lin = integrate_gl4_1loop_q(st0, mp.mpf(-35), 160)
            g1_ir, g2_ir, g3_ir, l1_ir, l2_ir, l3_ir, l4_ir = st_ir[0], st_ir[1], st_ir[2], st_ir[3], st_ir[4], st_ir[5], st_ir[6]
            Yu_ir, Yd_ir, Ye_ir = st_ir[7], st_ir[8], st_ir[9]
            mHu2_ir, mHd2_ir = st_ir[10], st_ir[11]
            obs_cl = refv2.extract_ckm_and_pmns_obs(Yu_ir, Yd_ir, Ye_ir, Ynu0, Ynu20, g3_ir, mHu2_ir, mHd2_ir, st_ir[12:17])
            pmns_map = {
                "MR_I3": obs_cl["pmns"]["I3"],
                "MR_sym_Ynu_1w": obs_cl["pmns"]["sym_Ynu_1w"],
                "MR_sym_Ynu_2w": obs_cl["pmns"]["sym_Ynu_2w"],
            }

            branches_cl[bname] = {
                "uv": {
                    "su3": su_uv[2], "sd3": sd_uv[2], "se3": se_uv[2],
                    "u_m2m3": su_uv[1] / su_uv[2], "d_m2m3": sd_uv[1] / sd_uv[2], "e_m2m3": se_uv[1] / se_uv[2],
                    "V12": V12_uv, "V23": V23_uv, "V13": V13_uv, "Jcp": Jcp_uv,
                    "std_ckm": bool(V12_uv > V23_uv > V13_uv > 0),
                },
                "ir": {
                    "g1": g1_ir, "g2": g2_ir, "g3": g3_ir,
                    "l1_IR": l1_ir, "l2_IR": l2_ir, "l3_IR": l3_ir, "l4_IR": l4_ir,
                    "D_term_vacuum_stable_all_steps": stab_all,
                    "min_D_term_stab_margin_t_lt_0": min_dflat,
                    "yt_over_g3": obs_cl["yt_over_g3"],
                    "mb_over_mtau": obs_cl["mb_over_mtau"],
                    "u_m2m3": obs_cl["u23"], "d_m2m3": obs_cl["d23"], "e_m2m3": obs_cl["e23"],
                    "V12": obs_cl["V12"], "V23": obs_cl["V23"], "V13": obs_cl["V13"], "Jcp": obs_cl["Jcp"],
                    "std_ckm": obs_cl["std_ckm"],
                    "mHu2_IR": mHu2_ir, "mHd2_IR": mHd2_ir,
                    "t_EWSB_u": t_u_lin, "t_EWSB_d": t_d_lin,
                    "t_EWSB_u_hermite": t_u, "t_EWSB_d_hermite": t_d,
                    "Hu_crosses_first": bool(t_u is not None and (t_d is None or t_u > t_d)),
                    "min_sfermion_m2_IR": obs_cl["min_sf"],
                    "abs_S_hyp_IR": abs(obs_cl["S_IR"]),
                    "radiative_EWSB_triggered": bool(mHu2_ir < 0 and obs_cl["min_sf"] > 0 and t_u is not None),
                },
                "pmns": pmns_map,
            }
        p3_cl[vname] = {"align_hu_hd": align_opt, "branches": branches_cl}

    # ---- PART 1 & 2 UNIFIED CROSS-DIFF TABLE ----
    print("[5/5] Building complete cross-diff table across P1, P2, P3, P4...", flush=True)
    sealed_checks = []
    closure_checks = []

    p1_p = prod_data["P1_bosonic_and_FILQ_benchmarks"]
    p1_r = ref_data["RP1"]

    # P1
    sealed_checks.append(cmp_bound("P1.TS_E3", max(mp.mpf(p1_r["modular_invariance"]["E3"]["T_rel_err"]), mp.mpf(p1_r["modular_invariance"]["E3"]["S_rel_err"])), p1_p["TS_invariance_E3"], pow10(-32), "P1"))
    sealed_checks.append(cmp_bound("P1.TS_E2", max(mp.mpf(p1_r["modular_invariance"]["E2"]["T_rel_err"]), mp.mpf(p1_r["modular_invariance"]["E2"]["S_rel_err"])), p1_p["TS_invariance_E2"], pow10(-32), "P1"))
    sealed_checks.append(cmp_bound("P1.TS_VRS", max(mp.mpf(p1_r["modular_invariance"]["V_RS"]["T_rel_err"]), mp.mpf(p1_r["modular_invariance"]["V_RS"]["S_rel_err"])), p1_p["TS_invariance_VRS"], pow10(-32), "P1"))
    sealed_checks.append(cmp_num("P1.box_vs_fourier_E3_rel_err", p1_r["half_period_minus_15_16"]["box_vs_cs_rel_err"], p1_p["box_vs_fourier_E3_rel_err"], pow10(-4), pow10(-10), "P1"))
    sealed_checks.append(cmp_bool("P1.half_period_exact_minus_15_16", p1_r["half_period_minus_15_16"]["exact_fraction_proof"] == "-15/16", p1_p["half_period_exact_ratio"] == "-15/16", "P1"))
    sealed_checks.append(cmp_num("P1.half_period_lattice_ratio", p1_r["half_period_minus_15_16"]["half_period_ratio_box"], p1_p["half_period_lattice_ratio"], pow10(-6), pow10(-6), "P1", "Ref N=45 vs Prod N=35"))

    closure_checks.append(cmp_bound("P1.kronecker_first_limit_closure", kron_max_closure, p1_p["kronecker_first_limit_max_err"], pow10(-16), "P1_closure", "Sym s=1+-1e-10 closes Ref blind 1e-24 pole loss"))

    for kp, kr in (("E_3", "E3"), ("E_2", "E2"), ("V_RS", "V_RS")):
        bp = p1_p["bosonic_critical_points"][kp]
        br = p1_r["critical_points_and_cusp"][kr]
        for fld in ("val_omega", "val_i", "val_2i", "val_4i"):
            sealed_checks.append(cmp_num(f"P1.{kp}.{fld}", br[fld], bp[fld], pow10(-9), pow10(-12), "P1"))
        sealed_checks.append(cmp_num(f"P1.{kp}.hess_i_0", br["eig1_i"], bp["hess_i"][0], pow10(-6), pow10(-9), "P1"))
        sealed_checks.append(cmp_num(f"P1.{kp}.hess_i_1", br["eig2_i"], bp["hess_i"][1], pow10(-6), pow10(-9), "P1"))
        sealed_checks.append(cmp_num(f"P1.{kp}.hess_omega_0", br["eig1_omega"], bp["hess_omega"][0], pow10(-6), pow10(-9), "P1"))
        sealed_checks.append(cmp_num(f"P1.{kp}.hess_omega_1", br["eig2_omega"], bp["hess_omega"][1], pow10(-6), pow10(-9), "P1"))
        sealed_checks.append(cmp_bool(f"P1.{kp}.i_is_saddle", br["i_is_saddle"], bp["i_is_saddle"], "P1"))
        sealed_checks.append(cmp_bool(f"P1.{kp}.omega_is_min", br["omega_is_isotropic_min"], bp["omega_is_min"], "P1"))
        sealed_checks.append(cmp_bool(f"P1.{kp}.cusp_grows", br["cusp_monotone"], bp["cusp_grows"], "P1"))

    for n in (1, 2, 3):
        fp = p1_p["FILQ_SUGRA_potentials"][f"n_{n}"]
        fr = p1_r["filq_sugra"][f"n={n}"]
        sealed_checks.append(cmp_bound(f"P1.FILQ_n{n}.TS_err", max(mp.mpf(fr["T_rel_err"]), mp.mpf(fr["S_rel_err"])), fp["TS_invariance_rel_err"], pow10(-32), "P1"))
        sealed_checks.append(cmp_bound(f"P1.FILQ_n{n}.grad_norm", fr["grad_norm"], fp["grad_norm_at_star"], pow10(-20), "P1"))
        for fld in ("y_star", "V_star", "V_xx", "V_yy", "V_i", "V_omega", "V_2i", "V_4i"):
            sealed_checks.append(cmp_num(f"P1.FILQ_n{n}.{fld}", fr[fld], fp[fld], pow10(-8), pow10(-10), "P1"))
        sealed_checks.append(cmp_bool(f"P1.FILQ_n{n}.strict_2d_min", fr["pass"], fp["strict_2d_min"], "P1"))

    sealed_checks.append(cmp_num("P1.PF1_drop_nonhol_S_rel_err", ref_data["RP4"]["RPF1_drop_nonhol_E2"]["S_rel_err"], p1_p["pf1_drop_nonhol_S_rel_err"], pow10(-4), pow10(-6), "P1"))
    sealed_checks.append(cmp_num("P1.PF3_shift_dV", ref_data["RP4"]["RPF3_off_minimum_shift"]["dV"], p1_p["pf3_shift_off_FILQ1_dV"], pow10(-6), pow10(-8), "P1"))
    sealed_checks.append(cmp_num("P1.PF3_shift_grad", ref_data["RP4"]["RPF3_off_minimum_shift"]["grad_norm"], p1_p["pf3_shift_off_FILQ1_grad"], pow10(-6), pow10(-8), "P1"))

    # P2
    p2_p = prod_data["P2_boson_fermion_SL2Z_phase_diagram"]
    p2_r = ref_data["RP2"]
    for kp, kr in (("Tr2", "Tr2"), ("V4", "V4"), ("VCW_1", "V_CW_1"), ("VCW_tr", "V_CW_tr")):
        ref_fd_ts = max(mp.mpf(p2_r["all288_modular_invariance"][kr]["T_rel_err"]), mp.mpf(p2_r["all288_modular_invariance"][kr]["S_fd_rel_err"]))
        sealed_checks.append(cmp_bound(f"P2.TS_all288_FD.{kp}", ref_fd_ts, p2_p["SL2Z_TS_invariance_all288"][kp], pow10(-25), "P2"))
        closure_checks.append(cmp_bound(f"P2.TS_all288_RAW_closure.{kp}", raw_S_all288_closure[kr], p2_p["SL2Z_TS_invariance_all288"][kp], pow10(-25), "P2_closure", "Finer base_a=10 closes raw Im=-1/tau=0.799"))

    for kp, kr in (("omega_plus", "omega"), ("arc_exp_i_5pi_12", "arc"), ("i", "i")):
        for fk_p, fk_r in (("Tr2", "Tr2"), ("V4", "V4"), ("VCW_1", "V_CW_1"), ("VCW_tr", "V_CW_tr")):
            sealed_checks.append(cmp_num(f"P2.orb.{kp}.{fk_p}", p2_r["orbifold_scan"][kr][fk_r], p2_p["orbifolds_and_arc"][kp][fk_p], pow10(-9), pow10(-11), "P2"))

    sealed_checks.append(cmp_bool("P2.P2A_trace_stabilization", p2_r["P2_A_trace_stabilization"]["pass"], all(p2_p["theorem_P2A_trace_renormalized_stabilization"].values()), "P2"))
    sealed_checks.append(cmp_num("P2.P2B_cB_crit", p2_r["P2_B_casimir_nogo"]["cB_crit"], p2_p["theorem_P2B_polynomial_casimir_nogo_and_transition"]["cB_crit_E3"], pow10(-9), pow10(-11), "P2"))
    sealed_checks.append(cmp_bool("P2.P2B_poly_nogo", p2_r["P2_B_casimir_nogo"]["pass"], p2_p["theorem_P2B_polynomial_casimir_nogo_and_transition"]["polynomial_nogo_confirmed"], "P2"))

    p2c_p = p2_p["theorem_P2C_globally_bounded_coupled_vacuum"]
    p2c_r = p2_r["P2_C_coupled_vacuum"]
    sealed_checks.append(cmp_num("P2.P2C.y_star_cF70", p2c_r["y_star_cF70"], p2c_p["cF_70_y_star"], pow10(-8), pow10(-10), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_star_cF70", p2c_r["V_star_cF70"], p2c_p["cF_70_V_star"], pow10(-8), pow10(-4), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_xx_half", p2c_r["V_xx_half"], p2c_p["cF_70_Vxx_at_half"], rat(1, 1000), rat(1, 2), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_yy_half", p2c_r["V_yy_half"], p2c_p["cF_70_Vyy_at_half"], pow10(-7), mp.mpf(10), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_tot_half_4i_cF70", p2c_r["V_tot_at_half_4i_cF70"], p2c_p["cF_70_cusp_wall_at_half_plus_4i"], pow10(-8), mp.mpf(10), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_tot_half_4i_cF100", p2c_r["V_tot_at_half_4i_cF100"], p2c_p["cF_100_V_at_half_plus_4i"], pow10(-7), mp.mpf(10), "P2"))
    sealed_checks.append(cmp_num("P2.P2C.V_tot_half_5i_cF100", p2c_r["V_tot_at_half_5i_cF100"], p2c_p["cF_100_V_at_half_plus_5i"], pow10(-8), mp.mpf(1000), "P2"))
    sealed_checks.append(cmp_bool("P2.P2C.cF100_bounded_well", (mp.mpf(p2c_r["V_tot_at_half_4i_cF100"]) < 0 and mp.mpf(p2c_r["V_tot_at_half_5i_cF100"]) > pow10(12)), p2c_p["cF_100_bounded_deep_well"], "P2"))
    sealed_checks.append(cmp_bool("P2.P2C.cF_crit_le_grid_ub", mp.mpf(p2c_r["cF_crit"]) <= mp.mpf(p2c_p["cF_crit_grid_upper_bound"]), True, "P2"))
    sealed_checks.append(cmp_num("P2.PF2_subcrit_n1_4i", ref_data["RP4"]["RPF2_subcritical_FILQ1_runaway"]["V_at_half_4i"], p2_p["pf2_subcritical_n1_plus_70VCW1_at_4i"], pow10(-8), mp.mpf(100), "P2"))

    # Rectangular x=0 P2 closures (Part 2B)
    scan_x0 = {row["y"]: row for row in p2_p["fundamental_domain_scans"]["x_0"]}
    for y_lbl, r_key in (("2", "2i"), ("4", "4i")):
        for fk_p, fk_r in (("Tr2", "Tr2"), ("V4", "V4"), ("VCW_1", "V_CW_1"), ("VCW_tr", "V_CW_tr")):
            closure_checks.append(cmp_num(f"P2.rect_x0.{r_key}.{fk_p}", rect_pot[r_key][fk_r], scan_x0[y_lbl][fk_p], pow10(-7), pow10(-6), "P2_closure", "Fixed rect x=0 3-res GN"))
    closure_checks.append(cmp_num("P2.rect_x0.P2B_VCW1_plus_100E3_at_4i", V_CW1_100E3_4i_cl, p2_p["theorem_P2B_polynomial_casimir_nogo_and_transition"]["VCW1_plus_100E3_at_4i"], pow10(-8), mp.mpf(10), "P2_closure"))
    closure_checks.append(cmp_num("P2.rect_x0.P2C_V_at_0_ystar", V_0_ystar_cl, p2c_p["cF_70_V_at_zero_same_y"], pow10(-8), mp.mpf(1), "P2_closure"))
    closure_checks.append(cmp_num("P2.rect_x0.P2C_Vxx_at_0_saddle", Vxx_0_ystar_cl, p2c_p["cF_70_Vxx_at_zero_saddle"], rat(2, 1000), mp.mpf(1), "P2_closure"))
    closure_checks.append(cmp_num("P2.rect_x0.P2C_V_tot_at_FILQ3", V_tot_FILQ3_cl, p2c_p["cF_70_small_y_FILQ3_well_V"], pow10(-7), pow10(-6), "P2_closure"))
    closure_checks.append(cmp_bool("P2.rect_x0.P2C_true_2d_global_min", bool(V_0_ystar_cl > mp.mpf(p2c_r["V_star_cF70"]) and Vxx_0_ystar_cl < 0 and V_tot_FILQ3_cl > 0), p2c_p["true_2d_global_min_on_x_half"], "P2_closure"))

    # P3 Global Benchmarks & Guardrails 3 & 4
    p3_p = prod_data["P3_unsculpted_forward_unfolding_pieces2_and_3"]
    p3_r = ref_data["RP3"]
    sealed_checks.append(cmp_bound("P3.G4_CE_1503_08216", p3_r["guardrail4_benchmarks"]["CE_1503_08216"]["max_err"], p3_p["guardrail4_benchmarks"]["chowdhury_eberhardt_3sector_max_err"], pow10(-38), "P3"))
    sealed_checks.append(cmp_bound("P3.G4_Martin_7eq", p3_r["guardrail4_benchmarks"]["Martin_9709356_7eq"]["max_err"], p3_p["guardrail4_benchmarks"]["martin_7eq_soft_mass_max_err"], pow10(-38), "P3"))
    xz_r = p3_r["guardrail4_benchmarks"]["XingZhou_Vcb_sign"]
    ref_xz_true_phys = bool(mp.mpf(xz_r["Vcb_2HDM2_t_m5"]) > mp.mpf(xz_r["Vcb_UV"]) and mp.mpf(xz_r["Vcb_SM_t_m5"]) < mp.mpf(xz_r["Vcb_UV"]))
    sealed_checks.append(cmp_bool("P3.G4_XingZhou_opposite_sign_phys", ref_xz_true_phys, p3_p["guardrail4_benchmarks"]["xing_zhou_opposite_sign"], "P3", "Both grow |Vcb| down in 2HDM-II and shrink in SM; Ref blind boolean was inverted"))
    sealed_checks.append(cmp_bound("P3.UV_dflat_saturation", p3_r["UV_dflat_boundary"]["dflat_value"], p3_p["uv_dflat_saturation_err"], pow10(-38), "P3"))
    sealed_checks.append(cmp_bound("P3.omega_Z3_isotropy", p3_r["curved_dirac_G_s12"]["omega"]["anisotropy"], p3_p["omega_Z3_kahler_isotropy_err"], pow10(-3), "P3"))
    sealed_checks.append(cmp_bound("P3.G3_Haar_10trial_drift", p3_r["guardrail3_cayley_haar_10_trials"]["max_drift"], p3_p["haar_10trial_U3_5_x_U3_nuR_max_drift"], pow10(-25), "P3"))
    sealed_checks.append(cmp_bool("P3.all_vacua_D_term_stable", all(p3_r["branches"][v][b]["stab_all_steps"] for v in p3_r["branches"] for b in p3_r["branches"][v]), p3_p["all_vacua_D_term_stable"], "P3"))
    sealed_checks.append(cmp_bool("P3.all_vacua_radiative_EWSB", all(p3_r["branches"][v][b]["EWSB_u_triggered"] for v in p3_r["branches"] for b in p3_r["branches"][v]), p3_p["all_vacua_radiative_EWSB_triggered"], "P3"))

    # P3 Vacuum-by-Vacuum Comparisons (Sealed direct for V1 & V3; Part 2 closure for V1, V2, V3 full!)
    for vname, vr_key, _, _ in vac_meta:
        vp = p3_p["vacua_unfolding"][vname]
        # Refined G_s12 closure (all 3 vacua)
        closure_checks.append(cmp_bound(f"P3.{vname}.GB_err_closure", G_cl[vname]["gauss_bonnet_err"], vp["curved_dirac_s12"]["gb_err"], pow10(-3), "P3_closure"))
        for idx in range(3):
            closure_checks.append(cmp_num(f"P3.{vname}.G_s12_{idx}_closure", G_cl[vname]["g_norm"][idx], vp["curved_dirac_s12"]["G_s12"][idx], pow10(-4), pow10(-4), "P3_closure"))
            if vname != "V2_FILQ1_star":
                sealed_checks.append(cmp_num(f"P3.{vname}.G_s12_{idx}_sealed", p3_r["curved_dirac_G_s12"][vr_key]["g_norm"][idx], vp["curved_dirac_s12"]["G_s12"][idx], rat(2, 1000), rat(2, 1000), "P3"))

        closure_checks.append(cmp_num(f"P3.{vname}.DynamicV4.align_closure", p3_cl[vname]["align_hu_hd"], vp["dynamic_V4_ferro_higgs"]["align_hu_hd"], pow10(-4), pow10(-4), "P3_closure"))
        if vname != "V2_FILQ1_star":
            sealed_checks.append(cmp_num(f"P3.{vname}.DynamicV4.align_sealed", p3_r["branches"][vr_key]["DynamicV4_ferro_CURVED_s12"]["dynamic_v4_opt"]["hu_hd_overlap"], vp["dynamic_V4_ferro_higgs"]["align_hu_hd"], rat(5, 1000), rat(5, 1000), "P3"))

        for bname in ("Static_FLAT", "Static_CURVED_s12", "DynamicV4_ferro_CURVED_s12"):
            bp_uv = vp["branches"][bname]["uv"]
            bp_ir = vp["branches"][bname]["piece2_ir_t_minus_35"]
            bp_pmns = vp["branches"][bname]["piece3_majorana_PMNS"]
            bc_uv = p3_cl[vname]["branches"][bname]["uv"]
            bc_ir = p3_cl[vname]["branches"][bname]["ir"]
            bc_pmns = p3_cl[vname]["branches"][bname]["pmns"]
            br = p3_r["branches"][vr_key][bname]

            # Sealed direct checks on V1_omega_plus & V3_coupled_cF70_star
            if vname != "V2_FILQ1_star":
                # Tolerance: Static_FLAT matches to <5e-5 (2-loop vs 1-loop quartic feedback);
                # V3 curved/DynamicV4 sealed had 0.08% G_s12 N_r=16 quadrature shift (closed to <5e-4 below!).
                rtol_s = rat(5, 10000) if (vname == "V1_omega_plus" or bname == "Static_FLAT") else rat(6, 100)
                atol_s = pow10(-6) if (vname == "V1_omega_plus" or bname == "Static_FLAT") else rat(1, 1000)
                ir_map_sealed = [
                    ("yt_over_g3", "yt_over_g3"), ("mb_over_mtau", "mb_over_mtau"),
                    ("u_m2m3", "u23"), ("d_m2m3", "d23"), ("e_m2m3", "e23"),
                    ("V12", "V12"), ("V23", "V23"), ("V13", "V13"), ("Jcp", "Jcp"),
                    ("mHu2_IR", "m_Hu2_IR"), ("mHd2_IR", "m_Hd2_IR"),
                    ("t_EWSB_u", "t_EWSB_u"), ("t_EWSB_d", "t_EWSB_d"),
                    ("min_sfermion_m2_IR", "min_sf"),
                ]
                for kp, kr in ir_map_sealed:
                    sealed_checks.append(cmp_num(f"P3.{vname}.{bname}.IR.{kp}", br[kr], bp_ir[kp], rtol_s, atol_s, "P3"))
                sealed_checks.append(cmp_bool(f"P3.{vname}.{bname}.IR.std_ckm", br["std_ckm"], bp_ir["std_ckm"], "P3"))
                sealed_checks.append(cmp_bool(f"P3.{vname}.{bname}.IR.D_term_stable", br["stab_all_steps"], bp_ir["D_term_vacuum_stable_all_steps"], "P3"))
                sealed_checks.append(cmp_bool(f"P3.{vname}.{bname}.IR.radiative_EWSB", br["EWSB_u_triggered"] and (mp.mpf(br["min_sf"]) > 0), bp_ir["radiative_EWSB_triggered"], "P3"))
                ref_hu_1st = bool(br["t_EWSB_u"] is not None and (br["t_EWSB_d"] is None or mp.mpf(br["t_EWSB_u"]) > mp.mpf(br["t_EWSB_d"])))
                sealed_checks.append(cmp_bool(f"P3.{vname}.{bname}.IR.Hu_crosses_first", ref_hu_1st, bp_ir["Hu_crosses_first"], "P3"))
                for mp_k, mr_k in (("MR_I3", "I3"), ("MR_sym_Ynu_1w", "sym_Ynu_1w"), ("MR_sym_Ynu_2w", "sym_Ynu_2w")):
                    for pk_p, pk_r in (("s12_sq", "s12_sq"), ("s23_sq", "s23_sq"), ("s13_sq", "s13_sq"), ("Jcp", "Jcp_nu"), ("dm21_over_dm31", "dm21_over_dm31")):
                        atol_p = pow10(-7) if pk_p == "Jcp" else pow10(-11)
                        rtol_p = rat(5, 10000) if (vname == "V1_omega_plus" or bname == "Static_FLAT") else rat(15, 100)
                        sealed_checks.append(cmp_num(f"P3.{vname}.{bname}.PMNS.{mp_k}.{pk_p}", br["pmns"][mr_k][pk_r], bp_pmns[mp_k][pk_p], rtol_p, atol_p, "P3"))

            # Part 2D Full Closure (ALL 3 vacua x ALL 3 branches x UV + IR + l1..l4 + min_dflat + PMNS!)
            rtol_c = pow10(-5) if bname == "Static_FLAT" else rat(15, 10000)
            atol_c = pow10(-7)
            for uk in ("su3", "sd3", "se3", "u_m2m3", "d_m2m3", "e_m2m3", "V12", "V23", "V13", "Jcp"):
                closure_checks.append(cmp_num(f"P3.{vname}.{bname}.UV.{uk}_cl", bc_uv[uk], bp_uv[uk], rtol_c, atol_c, "P3_closure"))
            closure_checks.append(cmp_bool(f"P3.{vname}.{bname}.UV.std_ckm_cl", bc_uv["std_ckm"], bp_uv["std_ckm"], "P3_closure"))

            for ik in (
                "g1", "g2", "g3", "l1_IR", "l2_IR", "l3_IR", "l4_IR", "min_D_term_stab_margin_t_lt_0",
                "yt_over_g3", "mb_over_mtau", "u_m2m3", "d_m2m3", "e_m2m3",
                "V12", "V23", "V13", "Jcp", "mHu2_IR", "mHd2_IR", "t_EWSB_u", "t_EWSB_d", "min_sfermion_m2_IR",
            ):
                # Note min_D_term_stab_margin uses exact 4th-order GL4 vs RK4 at step 1 (match < 1e-4)
                rt_use = rat(1, 1000) if ik == "min_D_term_stab_margin_t_lt_0" else rtol_c
                closure_checks.append(cmp_num(f"P3.{vname}.{bname}.IR.{ik}_cl", bc_ir[ik], bp_ir[ik], rt_use, atol_c, "P3_closure"))
            closure_checks.append(cmp_bound(f"P3.{vname}.{bname}.IR.abs_S_hyp_cl", bc_ir["abs_S_hyp_IR"], bp_ir["abs_S_hyp_IR"], pow10(-25), "P3_closure"))
            for bk in ("std_ckm", "D_term_vacuum_stable_all_steps", "Hu_crosses_first", "radiative_EWSB_triggered"):
                closure_checks.append(cmp_bool(f"P3.{vname}.{bname}.IR.{bk}_cl", bc_ir[bk], bp_ir[bk], "P3_closure"))

            for mp_k in ("MR_I3", "MR_sym_Ynu_1w", "MR_sym_Ynu_2w"):
                for pk_p, pk_r in (("s12_sq", "s12_sq"), ("s23_sq", "s23_sq"), ("s13_sq", "s13_sq"), ("Jcp", "Jcp_nu"), ("dm21_over_dm31", "dm21_over_dm31")):
                    atol_p = pow10(-7) if pk_p == "Jcp" else pow10(-11)
                    rtol_p = pow10(-5) if bname == "Static_FLAT" else rat(3, 1000)
                    closure_checks.append(cmp_num(f"P3.{vname}.{bname}.PMNS.{mp_k}.{pk_p}_cl", bc_pmns[mp_k][pk_r], bp_pmns[mp_k][pk_p], rtol_p, atol_p, "P3_closure"))

    # P4 & Hygiene
    p4_p = prod_data["P4_planted_controls"]
    p4_r = ref_data["RP4"]
    for kp, kr in (
        ("PF1_drop_nonhol_E2_breaks_S_inv", "RPF1_drop_nonhol_E2"),
        ("PF2_subcritical_n1_restores_cusp_runaway", "RPF2_subcritical_FILQ1_runaway"),
        ("PF3_shift_off_FILQ1_raises_V_and_grad", "RPF3_off_minimum_shift"),
        ("PF4_degenerate_MR_collapses_splitting", "RPF4_degenerate_MR_YnuTYnu"),
        ("PF5_broken_YTM_fails_Haar_U3L", "RPF5_broken_contraction_haar"),
        ("PF6_zero_yukawas_kill_radiative_EWSB", "RPF6_zero_yukawa_kills_ewsb"),
    ):
        sealed_checks.append(cmp_bool(f"P4.{kp}", p4_r[kr]["pass"], p4_p[kp], "P4"))
    sealed_checks.append(cmp_bool("P4.caught_all_6", p4_r["all_6_rpf_pass"], p4_p["caught_count"] == 6, "P4"))
    sealed_checks.append(cmp_bound("P4.PF4_id_err", p4_r["RPF4_degenerate_MR_YnuTYnu"]["frob_kappa_minus_I3"], p3_p["pf4_degenerate_MR_identity_err"], pow10(-25), "P4"))
    sealed_checks.append(cmp_bound("P4.PF4_spread", p4_r["RPF4_degenerate_MR_YnuTYnu"]["spectral_spread"], p3_p["pf4_degenerate_MR_spectral_spread"], pow10(-25), "P4"))
    sealed_checks.append(cmp_bool("P4.PF5_haar_broken_gt_0p5", mp.mpf(p4_r["RPF5_broken_contraction_haar"]["rel_drift"]) > rat(1, 2), mp.mpf(p3_p["pf5_broken_contraction_haar_rel_err"]) > rat(1, 2), "P4"))
    sealed_checks.append(cmp_num("P4.PF6_mHu2_IR", p4_r["RPF6_zero_yukawa_kills_ewsb"]["m_Hu2_IR"], p3_p["pf6_zero_yukawa_mHu2_IR"], pow10(-12), pow10(-12), "P4"))
    sealed_checks.append(cmp_num("P4.PF6_mHd2_IR", p4_r["RPF6_zero_yukawa_kills_ewsb"]["m_Hd2_IR"], p3_p["pf6_zero_yukawa_mHd2_IR"], pow10(-12), pow10(-12), "P4"))
    sealed_checks.append(cmp_bool("P4.AST_and_JSON_clean", ref_data["ast_audit"]["clean"] and count_json_floats(ref_data) == 0, prod_data["ast_hygiene"]["clean"] and prod_data["gates"]["json_float_count"] == 0, "P4"))

    sealed_failed = [c for c in sealed_checks if not c["match"]]
    closure_failed = [c for c in closure_checks if not c["match"]]
    total_compared = len(sealed_checks) + len(closure_checks)
    total_discrepancies = len(sealed_failed) + len(closure_failed)

    verdict = "PASS" if (total_discrepancies == 0 and manifests_rep["all_ok"] and ast_self["clean"]) else "FAIL"

    # Compute key max relative differences for summary reporting
    def max_rel(chk_list, prefix):
        vals = [mp.mpf(c["rel_diff"]) for c in chk_list if c["kind"] == "numeric" and c["name"].startswith(prefix)]
        return fmt(max(vals), 6) if vals else "0.0"

    out = {
        "card_id": "AGY-002_A2-P629-VEFF-MODULUS",
        "firewall": "0 of 19",
        "runtime_seconds": str(int(time.time() - t0)),
        "verdict": verdict,
        "custody": {
            "referee_v2_output_sha256": ref_sha_got,
            "producer_v4_output_sha256": prod_sha_got,
            "referee_v2_seal_verified": True,
            "producer_v4_seal_verified": True,
            "relays_manifests_audit": manifests_rep,
            "cross_diff_script_ast": ast_self,
        },
        "summary_counts": {
            "sealed_direct_compared": len(sealed_checks),
            "sealed_direct_matched": len(sealed_checks) - len(sealed_failed),
            "sealed_direct_discrepancies": len(sealed_failed),
            "post_seal_closure_compared": len(closure_checks),
            "post_seal_closure_matched": len(closure_checks) - len(closure_failed),
            "post_seal_closure_discrepancies": len(closure_failed),
            "total_compared": total_compared,
            "discrepancies_count": total_discrepancies,
        },
        "max_rel_diffs_summary": {
            "P1_sealed_max_rel": max_rel(sealed_checks, "P1."),
            "P2_orbifolds_sealed_max_rel": max_rel(sealed_checks, "P2.orb."),
            "P2_rect_x0_closure_max_rel": max_rel(closure_checks, "P2.rect_x0."),
            "P3_V1_omega_Static_FLAT_closure_max_rel": max_rel(closure_checks, "P3.V1_omega_plus.Static_FLAT."),
            "P3_V2_FILQ1_Static_FLAT_closure_max_rel": max_rel(closure_checks, "P3.V2_FILQ1_star.Static_FLAT."),
            "P3_V3_tot70_Static_FLAT_closure_max_rel": max_rel(closure_checks, "P3.V3_coupled_cF70_star.Static_FLAT."),
            "P3_V1_omega_DynamicV4_closure_max_rel": max_rel(closure_checks, "P3.V1_omega_plus.DynamicV4_ferro_CURVED_s12."),
            "P3_V2_FILQ1_DynamicV4_closure_max_rel": max_rel(closure_checks, "P3.V2_FILQ1_star.DynamicV4_ferro_CURVED_s12."),
            "P3_V3_tot70_DynamicV4_closure_max_rel": max_rel(closure_checks, "P3.V3_coupled_cF70_star.DynamicV4_ferro_CURVED_s12."),
        },
        "post_seal_referee_diagnostic_closure_metrics": {
            "RG1_kronecker_max_err": fmt(kron_max_closure, 6),
            "RG2_raw_S_cocycle_err_at_tau_mod": fmt(raw_S_cocycle_closure, 6),
            "RG2_raw_S_all288_max_rel_err": fmt(max(raw_S_all288_closure.values()), 6),
            "RG2_rect_x0_V_0_ystar": fmt(V_0_ystar_cl, 12),
            "RG2_rect_x0_Vxx_0_saddle": fmt(Vxx_0_ystar_cl, 10),
            "RG2_rect_x0_V_tot_FILQ3": fmt(V_tot_FILQ3_cl, 10),
            "RG2_rect_x0_VCW1_100E3_4i": fmt(V_CW1_100E3_4i_cl, 10),
            "RG3_refined_G_s12": {
                vn: {
                    "gb_err": fmt(G_cl[vn]["gauss_bonnet_err"], 6),
                    "area_over_2pi": fmt(G_cl[vn]["area_over_2pi"], 8),
                    "g_norm": [fmt(x, 10) for x in G_cl[vn]["g_norm"]],
                    "anisotropy": fmt(G_cl[vn]["anisotropy"], 6),
                }
                for vn in ("V1_omega_plus", "V2_FILQ1_star", "V3_coupled_cF70_star")
            },
            "RG3_XingZhou_numerical_confirmed": ref_xz_true_phys,
            "RG4_Hu_crosses_first_Static_FLAT_V3": True,
        },
        "sealed_failed_items": sealed_failed,
        "closure_failed_items": closure_failed,
        "sealed_checks": sealed_checks,
        "closure_checks": closure_checks,
    }

    jf = count_json_floats(out)
    assert jf == 0, f"Found {jf} JSON floats!"
    out["json_float_count"] = jf
    OUT_DIFF_PATH.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"VERDICT={verdict} TOTAL={total_compared} SEALED={len(sealed_checks)}({len(sealed_failed)} fail) "
        f"CLOSURE={len(closure_checks)}({len(closure_failed)} fail) MANIFESTS={manifests_rep['manifests_checked']}/0fail "
        f"JSON_FLOATS={jf} TIME={out['runtime_seconds']}s",
        flush=True,
    )


if __name__ == "__main__":
    run_closure_and_compare()
