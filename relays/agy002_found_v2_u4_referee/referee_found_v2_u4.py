"""Cold-Room Zero-Trust Referee for Gate F-U4 (AGY-002_FOUND-V2-U4).

Independently verifies:
- Section 0: AST zero-float/zero-complex & import hygiene, 20/20 SHA-256 manifests,
  and unreduced Cauchy-Riemann Richardson RK4 + Frobenius shooting L_2(tau) T & S covariance.
- Section 1: P-862 SymPy Cholesky SOS theorem, 16-pt FD grid x 4 (m_gal, reading) states
  at dps=50 using cyclic Hermitian Jacobi K^{-1/2} (cross-checked vs M-coupled Newton-Schulz)
  and GEPP determinants (cross-checked vs mp.det), UF-1..UF-4.
- Section 2: W-P1c 64 length-6 words (2 parabolic + 62 hyperbolic incl. Pell words LRRLRR/RRLRRL)
  and Process Clocks A (move-count), B (geodesic length), C (2D Clenshaw-Curtis on F_6).
- Section 3: 58-node Epistemic DAG v2 via Tarjan SCC + Kahn rank propagation (Guardrails 1 & 5).
- Section 4: Planted Fault Controls PFU4-1..PFU4-5.
"""

import ast
import hashlib
import json
import random
import sys
import time
from itertools import combinations, product
from pathlib import Path

import mpmath as mp
import sympy as sp


ALLOWED_EXTERNAL_IMPORTS = {"mpmath", "sympy", "numpy"}


# ---------------------------------------------------------------------------
# Section 0 helpers: AST audit & SHA-256 manifest custody
# ---------------------------------------------------------------------------

def audit_ast_and_imports(script_path):
    """Verify 0 float/complex AST literals and 0 disallowed imports."""
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_complex_literals = []
    disallowed_imports = []
    stdlib_names = getattr(sys, "stdlib_module_names", set())

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_complex_literals.append((node.lineno, repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top not in stdlib_names and top not in ALLOWED_EXTERNAL_IMPORTS:
                    disallowed_imports.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0 or node.module is None:
                disallowed_imports.append((node.lineno, f"relative:{node.module}"))
            else:
                top = node.module.split(".")[0]
                if top not in stdlib_names and top not in ALLOWED_EXTERNAL_IMPORTS:
                    disallowed_imports.append((node.lineno, node.module))

    assert len(float_complex_literals) == 0, f"Float/complex AST literals found: {float_complex_literals}"
    assert len(disallowed_imports) == 0, f"Disallowed imports found: {disallowed_imports}"
    return {
        "float_complex_literal_count": len(float_complex_literals),
        "disallowed_import_count": len(disallowed_imports),
        "ast_clean": True,
    }


def verify_sha256_manifests(repo_root, self_output_sha_path):
    """Dynamically verify all committed relays/agy002_found_v2_*/*SHA256.txt manifests."""
    relays_dir = repo_root / "relays"
    all_manifests = [
        p for p in sorted(relays_dir.glob("agy002_found_v2_*/*SHA256.txt"))
        if p.resolve() != self_output_sha_path.resolve()
    ]
    verified = []
    mismatches = []
    for mpath in all_manifests:
        lines = [ln.strip() for ln in mpath.read_text(encoding="utf-8").splitlines() if ln.strip()]
        if not lines:
            mismatches.append({"manifest": str(mpath), "error": "empty manifest"})
            continue
        for ln in lines:
            parts = ln.split()
            if len(parts) < 2:
                mismatches.append({"manifest": str(mpath), "error": f"malformed line: {ln}"})
                continue
            expected_hex = parts[0].lower()
            target_rel = parts[1]
            target_path = repo_root / target_rel
            if not target_path.is_file():
                mismatches.append({"manifest": str(mpath), "target": target_rel, "error": "missing file"})
                continue
            actual_hex = hashlib.sha256(target_path.read_bytes()).hexdigest().lower()
            if actual_hex != expected_hex:
                mismatches.append({
                    "manifest": str(mpath),
                    "target": target_rel,
                    "expected": expected_hex,
                    "actual": actual_hex,
                })
            else:
                verified.append({
                    "manifest": str(mpath.relative_to(repo_root)),
                    "target": target_rel,
                    "sha256": actual_hex,
                })
    assert len(mismatches) == 0, f"SHA-256 mismatches: {mismatches}"
    assert len(all_manifests) == 20, f"Expected 20 manifests (19 prior + self SCRIPT), got {len(all_manifests)}"
    return {
        "manifest_count": len(all_manifests),
        "verified_entries": len(verified),
        "mismatch_count": len(mismatches),
        "manifests": [v["manifest"] for v in verified],
    }


# ---------------------------------------------------------------------------
# Independent L_2(tau) ODE solver: Richardson RK4 + Frobenius shooting
# ---------------------------------------------------------------------------

def eisenstein_series(tau):
    """Compute E_2, E_4, E_6 and q = exp(2*pi*i*tau) dynamically to working precision."""
    q = mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 8))
    s2 = mp.mpc(0)
    s4 = mp.mpc(0)
    s6 = mp.mpc(0)
    qn = q
    n = 1
    while True:
        tb = qn / (1 - qn)
        t2 = n * tb
        t4 = (n ** 3) * tb
        t6 = (n ** 5) * tb
        s2 += t2
        s4 += t4
        s6 += t6
        if abs(t6) < tol and abs(qn) < tol:
            break
        n += 1
        qn *= q
    return 1 - 24 * s2, 1 + 240 * s4, 1 - 504 * s6, q


def wp_tau(z, tau, E2, q):
    """Evaluate Weierstrass P-function wp(z; tau) stably via lattice shift."""
    y = mp.im(tau)
    m_tau = int(mp.nint(mp.im(z) / y))
    z_p = z - m_tau * tau
    n1 = int(mp.nint(mp.re(z_p)))
    z_r = z_p - n1
    u = z_r if mp.im(z_r) >= 0 else -z_r
    eu = mp.exp(2 * mp.pi * mp.mpc(0, 1) * u)
    val = -(mp.pi ** 2 / 3) * E2 - (4 * mp.pi ** 2 * eu) / ((1 - eu) ** 2)
    ez = mp.exp(2 * mp.pi * mp.mpc(0, 1) * z_r)
    emz = 1 / ez
    tol = mp.mpf(10) ** (-(mp.mp.dps + 8))
    qn = q
    ezn = ez
    emzn = emz
    n = 1
    s = mp.mpc(0)
    while True:
        term = (n * qn / (1 - qn)) * (ezn + emzn)
        s += term
        if abs(term) < tol:
            break
        n += 1
        qn *= q
        ezn *= ez
        emzn *= emz
    return val - 4 * (mp.pi ** 2) * s


def precompute_wp_grid(z_start, z_end, n_max, tau, E2, q):
    """Precompute wp(z)/4 on 2*n_max + 1 uniform nodes for RK4 + Richardson."""
    dz = (z_end - z_start) / (2 * n_max)
    return [wp_tau(z_start + k * dz, tau, E2, q) / 4 for k in range(2 * n_max + 1)]


def rk4_from_grid(dz_total, wp_grid, stride, y_init, c_val, with_var=False):
    """Propagate psi'' + (wp/4 + c)*psi = 0 (and optionally d/dc variational ODE) via RK4."""
    n_steps = (len(wp_grid) - 1) // (2 * stride)
    dz = dz_total / n_steps
    y = list(y_init)
    if not with_var:
        for k in range(n_steps):
            idx = 2 * k * stride
            Q0 = wp_grid[idx] + c_val
            Qm = wp_grid[idx + stride] + c_val
            Q1 = wp_grid[idx + 2 * stride] + c_val
            y0, y1, y2, y3 = y
            k1_0 = dz * y1
            k1_1 = -dz * Q0 * y0
            k1_2 = dz * y3
            k1_3 = -dz * Q0 * y2
            k2_0 = dz * (y1 + k1_1 / 2)
            k2_1 = -dz * Qm * (y0 + k1_0 / 2)
            k2_2 = dz * (y3 + k1_3 / 2)
            k2_3 = -dz * Qm * (y2 + k1_2 / 2)
            k3_0 = dz * (y1 + k2_1 / 2)
            k3_1 = -dz * Qm * (y0 + k2_0 / 2)
            k3_2 = dz * (y3 + k2_3 / 2)
            k3_3 = -dz * Qm * (y2 + k2_2 / 2)
            k4_0 = dz * (y1 + k3_1)
            k4_1 = -dz * Q1 * (y0 + k3_0)
            k4_2 = dz * (y3 + k3_3)
            k4_3 = -dz * Q1 * (y2 + k3_2)
            y = [
                y0 + (k1_0 + 2 * k2_0 + 2 * k3_0 + k4_0) / 6,
                y1 + (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6,
                y2 + (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6,
                y3 + (k1_3 + 2 * k2_3 + 2 * k3_3 + k4_3) / 6,
            ]
    else:
        for k in range(n_steps):
            idx = 2 * k * stride
            Q0 = wp_grid[idx] + c_val
            Qm = wp_grid[idx + stride] + c_val
            Q1 = wp_grid[idx + 2 * stride] + c_val
            y0, y1, y2, y3, y4, y5, y6, y7 = y
            k1_0 = dz * y1
            k1_1 = -dz * Q0 * y0
            k1_2 = dz * y3
            k1_3 = -dz * Q0 * y2
            k1_4 = dz * y5
            k1_5 = -dz * (Q0 * y4 + y0)
            k1_6 = dz * y7
            k1_7 = -dz * (Q0 * y6 + y2)
            k2_0 = dz * (y1 + k1_1 / 2)
            k2_1 = -dz * Qm * (y0 + k1_0 / 2)
            k2_2 = dz * (y3 + k1_3 / 2)
            k2_3 = -dz * Qm * (y2 + k1_2 / 2)
            k2_4 = dz * (y5 + k1_5 / 2)
            k2_5 = -dz * (Qm * (y4 + k1_4 / 2) + (y0 + k1_0 / 2))
            k2_6 = dz * (y7 + k1_7 / 2)
            k2_7 = -dz * (Qm * (y6 + k1_6 / 2) + (y2 + k1_2 / 2))
            k3_0 = dz * (y1 + k2_1 / 2)
            k3_1 = -dz * Qm * (y0 + k2_0 / 2)
            k3_2 = dz * (y3 + k2_3 / 2)
            k3_3 = -dz * Qm * (y2 + k2_2 / 2)
            k3_4 = dz * (y5 + k2_5 / 2)
            k3_5 = -dz * (Qm * (y4 + k2_4 / 2) + (y0 + k2_0 / 2))
            k3_6 = dz * (y7 + k2_7 / 2)
            k3_7 = -dz * (Qm * (y6 + k2_6 / 2) + (y2 + k2_2 / 2))
            k4_0 = dz * (y1 + k3_1)
            k4_1 = -dz * Q1 * (y0 + k3_0)
            k4_2 = dz * (y3 + k3_3)
            k4_3 = -dz * Q1 * (y2 + k3_2)
            k4_4 = dz * (y5 + k3_5)
            k4_5 = -dz * (Q1 * (y4 + k3_4) + (y0 + k3_0))
            k4_6 = dz * (y7 + k3_7)
            k4_7 = -dz * (Q1 * (y6 + k3_6) + (y2 + k3_2))
            y = [
                y0 + (k1_0 + 2 * k2_0 + 2 * k3_0 + k4_0) / 6,
                y1 + (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6,
                y2 + (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6,
                y3 + (k1_3 + 2 * k2_3 + 2 * k3_3 + k4_3) / 6,
                y4 + (k1_4 + 2 * k2_4 + 2 * k3_4 + k4_4) / 6,
                y5 + (k1_5 + 2 * k2_5 + 2 * k3_5 + k4_5) / 6,
                y6 + (k1_6 + 2 * k2_6 + 2 * k3_6 + k4_6) / 6,
                y7 + (k1_7 + 2 * k2_7 + 2 * k3_7 + k4_7) / 6,
            ]
    return y


def richardson_from_grid(dz_total, wp_grid, strides, y_init, c_val, with_var=False):
    """Apply multi-level Richardson extrapolation to classical RK4 outputs."""
    rows = [[rk4_from_grid(dz_total, wp_grid, st, y_init, c_val, with_var) for st in strides]]
    for lvl in range(1, len(strides)):
        p = 3 + lvl
        fac = 2 ** p
        prev = rows[-1]
        cur = [
            [(fac * prev[i + 1][j] - prev[i][j]) / (fac - 1) for j in range(len(y_init))]
            for i in range(len(prev) - 1)
        ]
        rows.append(cur)
    val = rows[-1][0]
    err = max(abs(val[j] - rows[-2][-1][j]) for j in range(len(y_init)))
    return val, err


def half_to_full_monodromy(s):
    """Use half-period symmetry Q(z_mid + s) = Q(z_mid - s) to double integration span."""
    a, c_, b, d = s[0], s[1], s[2], s[3]
    da, dc_, db, dd = s[4], s[5], s[6], s[7]
    T = mp.matrix([[a * d + b * c_, 2 * b * d], [2 * a * c_, a * d + b * c_]])
    d00 = da * d + a * dd + db * c_ + b * dc_
    dT = mp.matrix([[d00, 2 * (db * d + b * dd)], [2 * (da * c_ + a * dc_), d00]])
    return T, dT


def solve_L2_rk4_direct(tau_raw, target_dps=50, high_acc=True):
    """Solve punctured-torus uniformization L_2(tau) directly via RK4 + Frobenius shooting."""
    old_dps = mp.mp.dps
    # Stage 1: fast low-precision Newton for accessory parameter c(tau)
    mp.mp.dps = 22
    tau22 = mp.mpc(tau_raw)
    E2, E4, E6, q = eisenstein_series(tau22)
    z0 = (1 + tau22) / 2
    na_22 = 16
    nb_22 = max(16, min(48, int(mp.ceil(16 * abs(tau22) / 4)) * 4))
    wp_a22 = precompute_wp_grid(z0, z0 + mp.mpf(1) / 2, na_22, tau22, E2, q)
    wp_b22 = precompute_wp_grid(z0, z0 + tau22 / 2, nb_22, tau22, E2, q)
    c_val = (mp.pi ** 2) / 12
    yv = [
        mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1),
        mp.mpc(0), mp.mpc(0), mp.mpc(0), mp.mpc(0),
    ]
    for it in range(12):
        sa = rk4_from_grid(mp.mpc(1) / 2, wp_a22, 1, yv, c_val, True)
        sb = rk4_from_grid(tau22 / 2, wp_b22, 1, yv, c_val, True)
        Ta, dTa = half_to_full_monodromy(sa)
        Tb, dTb = half_to_full_monodromy(sb)
        Tab = Ta * Tb
        dTab = dTa * Tb + Ta * dTb
        trA = Ta[0, 0] + Ta[1, 1]
        trB = Tb[0, 0] + Tb[1, 1]
        trAB = Tab[0, 0] + Tab[1, 1]
        dtrA = dTa[0, 0] + dTa[1, 1]
        dtrB = dTb[0, 0] + dTb[1, 1]
        dtrAB = dTab[0, 0] + dTab[1, 1]
        res = mp.matrix([[mp.im(trA)], [mp.im(trB)], [mp.im(trAB)]])
        rn = max(abs(res[0, 0]), abs(res[1, 0]), abs(res[2, 0]))
        if rn < mp.mpf(10) ** (-12):
            break
        J = mp.matrix([
            [mp.im(dtrA), mp.re(dtrA)],
            [mp.im(dtrB), mp.re(dtrB)],
            [mp.im(dtrAB), mp.re(dtrAB)],
        ])
        dc = -mp.lu_solve(J.T * J, J.T * res)
        c_val += mp.mpc(dc[0, 0], dc[1, 0])

    # Stage 2: polish c(tau) and shoot inward to Frobenius matching radius
    mp.mp.dps = target_dps
    tau = mp.mpc(tau_raw)
    c_val = mp.mpc(c_val)
    E2, E4, E6, q = eisenstein_series(tau)
    z0 = (1 + tau) / 2
    if high_acc:
        na_max = 128
        nb_max = max(128, min(512, int(mp.ceil(128 * abs(tau) / 8)) * 8))
        strides = [8, 4, 2, 1]
        n_seg_in = 64
        M_frob = 80
        polish_iters = 5
        tol_rn = mp.mpf(10) ** (-(target_dps - 12))
    else:
        na_max = 16
        nb_max = max(16, min(48, int(mp.ceil(8 * abs(tau) / 4)) * 4))
        strides = [4, 2, 1]
        n_seg_in = 16
        M_frob = 40
        polish_iters = 3
        tol_rn = mp.mpf(10) ** (-12)

    wp_a = precompute_wp_grid(z0, z0 + mp.mpf(1) / 2, na_max, tau, E2, q)
    wp_b = precompute_wp_grid(z0, z0 + tau / 2, nb_max, tau, E2, q)
    for it in range(polish_iters):
        sa, _ = richardson_from_grid(mp.mpc(1) / 2, wp_a, strides, yv, c_val, True)
        sb, _ = richardson_from_grid(tau / 2, wp_b, strides, yv, c_val, True)
        Ta, dTa = half_to_full_monodromy(sa)
        Tb, dTb = half_to_full_monodromy(sb)
        Tab = Ta * Tb
        dTab = dTa * Tb + Ta * dTb
        trA = Ta[0, 0] + Ta[1, 1]
        trB = Tb[0, 0] + Tb[1, 1]
        trAB = Tab[0, 0] + Tab[1, 1]
        dtrA = dTa[0, 0] + dTa[1, 1]
        dtrB = dTb[0, 0] + dTb[1, 1]
        dtrAB = dTab[0, 0] + dTab[1, 1]
        res = mp.matrix([[mp.im(trA)], [mp.im(trB)], [mp.im(trAB)]])
        rn = max(abs(res[0, 0]), abs(res[1, 0]), abs(res[2, 0]))
        if rn < tol_rn and it >= 1:
            break
        J = mp.matrix([
            [mp.im(dtrA), mp.re(dtrA)],
            [mp.im(dtrB), mp.re(dtrB)],
            [mp.im(dtrAB), mp.re(dtrAB)],
        ])
        dc = -mp.lu_solve(J.T * J, J.T * res)
        c_val += mp.mpc(dc[0, 0], dc[1, 0])

    # Final monodromy check without variational derivatives if needed
    sa, _ = richardson_from_grid(mp.mpc(1) / 2, wp_a, strides, yv, c_val, True)
    sb, _ = richardson_from_grid(tau / 2, wp_b, strides, yv, c_val, True)
    Ta, _ = half_to_full_monodromy(sa)
    Tb, _ = half_to_full_monodromy(sb)
    Tab = Ta * Tb
    rn = max(
        abs(mp.im(Ta[0, 0] + Ta[1, 1])),
        abs(mp.im(Tb[0, 0] + Tb[1, 1])),
        abs(mp.im(Tab[0, 0] + Tab[1, 1])),
    )
    det_err = max(
        abs(Ta[0, 0] * Ta[1, 1] - Ta[0, 1] * Ta[1, 0] - 1),
        abs(Tb[0, 0] * Tb[1, 1] - Tb[0, 1] * Tb[1, 0] - 1),
    )

    def mobius(T):
        d = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
        return mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]]) / d

    Aa = mobius(Ta)
    P0 = mobius(Tb * Ta * (Tb ** (-1)) * (Ta ** (-1)))
    pf = (P0[0, 0] - P0[1, 1]) / (2 * P0[1, 0])
    sdisc = mp.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4 * Aa[0, 1] * Aa[1, 0])
    f1 = (Aa[0, 0] - Aa[1, 1] + sdisc) / (2 * Aa[1, 0])
    f2 = (Aa[0, 0] - Aa[1, 1] - sdisc) / (2 * Aa[1, 0])
    g0 = mp.matrix([[1, -f1], [1, -pf]])
    sc = (g0[0, 0] * f2 + g0[0, 1]) / (g0[1, 0] * f2 + g0[1, 1])
    g_raw = mp.matrix([[1 / sc, -f1 / sc], [1, -pf]])
    g = g_raw / mp.sqrt(g_raw[0, 0] * g_raw[1, 1] - g_raw[0, 1] * g_raw[1, 0])
    if mp.im(g[0, 1] / g[1, 1]) < 0:
        g = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]]) * g
    gPg = g * P0 * (g ** (-1))
    lam = abs(mp.re(gPg[0, 1] / gPg[0, 0]))

    zs = (mp.mpf(1) / 5) * z0 / abs(z0)
    pts = [z0]
    cur = z0
    while abs(cur) / 2 > abs(zs) * mp.mpf(11) / 10:
        cur = cur / 2
        pts.append(cur)
    pts.append(zs)
    st = [mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)]
    for a_pt, b_pt in zip(pts[:-1], pts[1:]):
        wp_seg = precompute_wp_grid(a_pt, b_pt, n_seg_in, tau, E2, q)
        st, _ = richardson_from_grid(b_pt - a_pt, wp_seg, strides, st, c_val, False)
    w_zs = st[2] / st[0]
    u_zs = (g[0, 0] * w_zs + g[0, 1]) / (g[1, 0] * w_zs + g[1, 1])

    g2 = (mp.mpf(4) / 3) * (mp.pi ** 4) * E4
    g3 = (mp.mpf(8) / 27) * (mp.pi ** 6) * E6
    c_wp = [mp.mpc(0)] * (M_frob // 2 + 2)
    c_wp[1] = g2 / 20
    c_wp[2] = g3 / 28
    for n in range(3, M_frob // 2 + 2):
        s_wp = sum(c_wp[m] * c_wp[n - 1 - m] for m in range(1, n - 1))
        c_wp[n] = (mp.mpf(3) / ((2 * n + 3) * (n - 2))) * s_wp
    Q_frob = [mp.mpc(0)] * (M_frob + 1)
    Q_frob[0] = c_val
    for n in range(1, M_frob // 2 + 1):
        if 2 * n <= M_frob:
            Q_frob[2 * n] = c_wp[n] / 4
    alpha = [mp.mpc(0)] * (M_frob + 1)
    beta = [mp.mpc(0)] * (M_frob + 1)
    alpha[0] = mp.mpc(1)
    for m in range(2, M_frob + 1):
        alpha[m] = -sum(Q_frob[j] * alpha[m - 2 - j] for j in range(m - 1)) / (m * m)
        beta[m] = -(2 * m * alpha[m] + sum(Q_frob[j] * beta[m - 2 - j] for j in range(m - 1))) / (m * m)
    num_g = mp.mpc(0)
    den_g = mp.mpc(0)
    zp = mp.mpc(1)
    for m in range(M_frob + 1):
        num_g += beta[m] * zp
        den_g += alpha[m] * zp
        zp *= zs
    im_B = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(num_g / den_g))
    L2_val = mp.pi - (2 * mp.pi / lam) * im_B
    mp.mp.dps = old_dps
    return L2_val, rn, det_err


def gauss_reduce_sl2z(tau):
    """Left-SL_2(Z) Gauss reduction returning (tau_FD, log_factor) with L_2(tau) = L_2(tau_FD) - log_factor."""
    z = mp.mpc(tau)
    log_fac = mp.mpf(0)
    tol = mp.mpf(10) ** (-(mp.mp.dps - 8))
    for _ in range(200):
        k = int(mp.nint(mp.re(z)))
        if k != 0:
            z = z - k
        if abs(z) < 1 - tol:
            log_fac += mp.log(abs(z))
            z = -1 / z
        else:
            break
    if mp.re(z) < -mp.mpf(1) / 2 - tol:
        z += 1
    elif mp.re(z) > mp.mpf(1) / 2 + tol:
        z -= 1
    return z, log_fac


def eval_L2_gauss_reduced(tau, fd_cache, target_dps=50, high_acc=True):
    """Evaluate L_2(tau) via left-SL_2(Z) Gauss reduction + ODE solve on FD."""
    tau_fd, log_fac = gauss_reduce_sl2z(tau)
    key = (mp.nstr(mp.re(tau_fd), target_dps - 5), mp.nstr(mp.im(tau_fd), target_dps - 5), target_dps, high_acc)
    if key not in fd_cache:
        L2_fd, _, _ = solve_L2_rk4_direct(tau_fd, target_dps=target_dps, high_acc=high_acc)
        fd_cache[key] = L2_fd
    return fd_cache[key] - log_fac


# ---------------------------------------------------------------------------
# Independent Linear Algebra: GEPP det, Cyclic Hermitian Jacobi, M-Coupled NS
# ---------------------------------------------------------------------------

def det_gepp(A):
    """Exact Gaussian elimination with partial pivoting for determinant."""
    n = A.rows
    M = [[A[i, j] for j in range(n)] for i in range(n)]
    det = mp.mpc(1)
    for k in range(n):
        piv = max(range(k, n), key=lambda r: abs(M[r][k]))
        if abs(M[piv][k]) == 0:
            return mp.mpc(0)
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
            det = -det
        pv = M[k][k]
        det *= pv
        for i in range(k + 1, n):
            fac = M[i][k] / pv
            for j in range(k + 1, n):
                M[i][j] -= fac * M[k][j]
    return det


def jacobi_hermitian_inv_sqrt(K_in):
    """Cyclic Hermitian Jacobi eigensolver for K^{-1/2} (never calls mp.eighe)."""
    n = K_in.rows
    old_dps = mp.mp.dps
    mp.mp.dps = old_dps + 30
    H = [[mp.mpc(K_in[i, j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        H[i][i] = mp.mpc(mp.re(H[i][i]), 0)
        for j in range(i + 1, n):
            avg = (H[i][j] + mp.conj(H[j][i])) / 2
            H[i][j] = avg
            H[j][i] = mp.conj(avg)
    V = [[mp.mpc(1 if i == j else 0) for j in range(n)] for i in range(n)]
    tol = mp.mpf(10) ** (-(mp.mp.dps - 5))
    for _ in range(50):
        max_off = mp.mpf(0)
        for p in range(n):
            for q in range(p + 1, n):
                b = H[p][q]
                r = abs(b)
                if r > max_off:
                    max_off = r
                if r <= tol:
                    continue
                u = b / r
                uc = mp.conj(u)
                a = mp.re(H[p][p])
                d = mp.re(H[q][q])
                tau = (a - d) / (2 * r)
                sgn = mp.mpf(1) if tau >= 0 else mp.mpf(-1)
                t = sgn / (abs(tau) + mp.sqrt(1 + tau * tau))
                c = 1 / mp.sqrt(1 + t * t)
                s = c * t
                g00 = u * c
                g01 = -u * s
                g10 = mp.mpc(s)
                g11 = mp.mpc(c)
                for i in range(n):
                    hp = H[i][p]
                    hq = H[i][q]
                    H[i][p] = hp * g00 + hq * g10
                    H[i][q] = hp * g01 + hq * g11
                gc00 = uc * c
                gc01 = mp.mpc(s)
                gc10 = -uc * s
                gc11 = mp.mpc(c)
                for j in range(n):
                    hp = H[p][j]
                    hq = H[q][j]
                    H[p][j] = gc00 * hp + gc01 * hq
                    H[q][j] = gc10 * hp + gc11 * hq
                H[p][q] = mp.mpc(0)
                H[q][p] = mp.mpc(0)
                H[p][p] = mp.mpc(mp.re(H[p][p]), 0)
                H[q][q] = mp.mpc(mp.re(H[q][q]), 0)
                for i in range(n):
                    vp = V[i][p]
                    vq = V[i][q]
                    V[i][p] = vp * g00 + vq * g10
                    V[i][q] = vp * g01 + vq * g11
        if max_off <= tol:
            break
    evals = [mp.re(H[i][i]) for i in range(n)]
    assert min(evals) > 0, f"Non-positive eigenvalue in K: {evals}"
    inv_sq = [1 / mp.sqrt(ev) for ev in evals]
    out = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            out[i, j] = sum(V[i][k] * inv_sq[k] * mp.conj(V[j][k]) for k in range(n))
    mp.mp.dps = old_dps
    return mp.matrix([[mp.mpc(out[i, j]) for j in range(n)] for i in range(n)])


def newton_schulz_inv_sqrt(K_in):
    """Unconditionally stable M-coupled Newton-Schulz iteration for K^{-1/2}."""
    n = K_in.rows
    old_dps = mp.mp.dps
    mp.mp.dps = old_dps + 30
    K = mp.matrix([[mp.mpc(K_in[i, j]) for j in range(n)] for i in range(n)])
    alpha = mp.re(sum(K[i, i] for i in range(n)))
    A = K / alpha
    I = mp.eye(n)
    Z = I
    M = A
    tol = mp.mpf(10) ** (-(old_dps + 12))
    for _ in range(160):
        err = max(abs(M[i, j] - I[i, j]) for i in range(n) for j in range(n))
        if err < tol:
            break
        T = (3 * I - M) / 2
        Z = Z * T
        M = T * M * T
    res = Z / mp.sqrt(alpha)
    mp.mp.dps = old_dps
    return mp.matrix([[mp.mpc(res[i, j]) for j in range(n)] for i in range(n)])


# ---------------------------------------------------------------------------
# Quaternion Yukawa & Fock-Weil Construction
# ---------------------------------------------------------------------------

def build_yukawa_helpers():
    """Construct dual quaternion spin-structure tensors for S and tilde_S readings."""
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = mp.matrix([[0, mp.mpc(0, 1)], [mp.mpc(0, 1), 0]])
    eps = QJ
    U = [I2, QI, QJ, QK]
    B_gen = [QJ, QI, QK]
    E = [eps * u for u in U]

    def ip(A, B):
        return sum(A[r, c] * B[r, c] for r in range(2) for c in range(2))

    G = mp.matrix([[ip(E[t], U[s]) for s in range(4)] for t in range(4)])
    G_inv = G ** (-1)
    E_dual = []
    for a in range(4):
        M = mp.zeros(2, 2)
        for b in range(4):
            M += G_inv[b, a] * U[b]
        E_dual.append(M)

    q_S = [QI, QJ, QK]
    q_tS = [eps * Q.apply(mp.conj) * eps.T for Q in q_S]

    def build_C(q_list):
        C = [[[[mp.mpc(0) for _ in range(3)] for _ in range(3)] for _ in range(4)] for _ in range(3)]
        for qi in range(3):
            for a in range(3):
                for b in range(3):
                    M = B_gen[a].T * eps * q_list[qi] * B_gen[b]
                    for si in range(4):
                        C[qi][si][a][b] = ip(M, E_dual[si])
        return C

    return E, build_C(q_S), build_C(q_tS)


def dedekind_eta_hat_E2(tau):
    """Compute Delta_hat = 2*pi*eta(tau)^3, E_2(tau), and q = exp(2*pi*i*tau)."""
    q = mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 10))
    prod_q = mp.mpc(1)
    s2 = mp.mpc(0)
    qm = q
    m = 1
    while True:
        prod_q *= (1 - qm)
        t2 = m * qm / (1 - qm)
        s2 += t2
        if abs(qm) < tol and abs(t2) < tol:
            break
        m += 1
        qm *= q
    eta = mp.exp(mp.mpc(0, 1) * mp.pi * tau / 12) * prod_q
    return 2 * mp.pi * (eta ** 3), 1 - 24 * s2, q


def theta_c_and_d(a, b, tau):
    """Compute Jacobi theta_c(a, b) and half-derivative dtheta_c(a, b)."""
    a = mp.mpf(a)
    b = mp.mpf(b)
    y = mp.im(tau)
    k_max = int(mp.ceil(mp.sqrt((mp.mp.dps + 10) * mp.log(10) / (mp.pi * y)))) + 3
    th = mp.mpc(0)
    dth = mp.mpc(0)
    for k in range(-k_max, k_max + 1):
        ka = k + a
        term = mp.exp(mp.mpc(0, 1) * mp.pi * (ka ** 2) * tau + 2 * mp.pi * mp.mpc(0, 1) * ka * b)
        th += term
        dth += (ka ** 2) * term
    return th, dth / 2


def X01(a, b, tau):
    """Evaluate two-theta functions X_0(a, b) and X_1(a, b)."""
    a = mp.mpf(a)
    b = mp.mpf(b)
    y = mp.im(tau)
    k_max = int(mp.ceil(mp.sqrt((mp.mp.dps + 10) * mp.log(10) / (2 * mp.pi * y)))) + 3
    x0 = mp.mpc(0)
    x1 = mp.mpc(0)
    for n in range(-k_max, k_max + 1):
        na = n + a
        x0 += mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau * (na ** 2) + 2 * mp.pi * mp.mpc(0, 1) * na * b)
        na1 = na + mp.mpf(1) / 2
        x1 += mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau * (na1 ** 2) + 2 * mp.pi * mp.mpc(0, 1) * na * b)
    return x0, x1


def prepare_tau_yukawa(tau, L2_val, E):
    """Precompute tau-only factors for Y(tau, w_L, w_R, reading)."""
    x_r = mp.re(tau)
    y_r = mp.im(tau)
    Delta_hat, E2, q = dedekind_eta_hat_E2(tau)
    th2, dth2 = theta_c_and_d(mp.mpf(1) / 2, 0, tau)
    th4, dth4 = theta_c_and_d(0, mp.mpf(1) / 2, tau)
    th3, dth3 = theta_c_and_d(0, 0, tau)
    Rh = [-(th2 ** 2) / Delta_hat, -(th4 ** 2) / Delta_hat, mp.mpc(0, 1) * (th3 ** 2) / Delta_hat]
    dNh = [-2 * th2 * dth2 / Delta_hat, -2 * th4 * dth4 / Delta_hat, 2 * mp.mpc(0, 1) * th3 * dth3 / Delta_hat]
    c3_S = [dNh[qi] - (E2 / 12) * Rh[qi] for qi in range(3)]
    c3_tS = [mp.conj(v) for v in c3_S]
    s_old = 2 * mp.pi * (L2_val + mp.log(y_r) / 2 - mp.euler - mp.log(mp.pi))
    exp_m2L2 = mp.exp(-2 * L2_val)
    return {
        "tau": tau,
        "x_r": x_r,
        "y_r": y_r,
        "Delta_hat": Delta_hat,
        "q": q,
        "c3_S": c3_S,
        "c3_tS": c3_tS,
        "s_old": s_old,
        "exp_m2L2": exp_m2L2,
        "E": E,
    }


def Y_from_tau_ctx(ctx, w_L, w_R, C_S, C_tS=None):
    """Compute Y(tau, w_L, w_R) for reading S (and tilde_S if C_tS provided)."""
    tau = ctx["tau"]
    x_r = ctx["x_r"]
    y_r = ctx["y_r"]
    Delta_hat = ctx["Delta_hat"]
    q = ctx["q"]
    E = ctx["E"]

    ax, bx = w_L[0], 2 * w_L[1]
    ay, by = w_R[0], 2 * w_R[1]
    X0, X1 = X01(ax, bx, tau)
    Y0, Y1 = X01(ay, by, tau)
    iDh = mp.mpc(0, 1) * Delta_hat
    Mm = mp.matrix([
        [X0 * Y0 / Delta_hat, mp.exp(mp.mpc(0, 1) * mp.pi * by) * X0 * Y1 / iDh],
        [mp.exp(mp.mpc(0, 1) * mp.pi * bx) * X1 * Y0 / iDh, -mp.exp(mp.mpc(0, 1) * mp.pi * (bx + by)) * X1 * Y1 / Delta_hat],
    ])
    Rch = [sum(E[si][r, c] * Mm[r, c] for r in range(2) for c in range(2)) for si in range(4)]

    sig = [
        (mp.mpf(0), mp.mpf(0)),
        (mp.mpf(0), mp.mpf(-1) / 2),
        (mp.mpf(-1) / 2, mp.mpf(0)),
        (mp.mpf(-1) / 2, mp.mpf(-1) / 2),
    ]
    tol = mp.mpf(10) ** (-(mp.mp.dps + 10))
    uch = []
    for si in range(4):
        ua = (w_L[0] + w_R[0] + sig[si][0]) % 1
        ub = (w_L[1] + w_R[1] + sig[si][1]) % 1
        if ua == 0 and ub == 0:
            uch.append(mp.mpc(0))
            continue
        if ua == 0:
            fu = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y_r)) + (mp.pi ** 2 * y_r) / (mp.sin(mp.pi * ub) ** 2)
            m = 1
            while True:
                wp_p = mp.exp(2 * mp.pi * mp.mpc(0, 1) * (m * x_r + ub) - 2 * mp.pi * m * y_r)
                wp_m = mp.exp(2 * mp.pi * mp.mpc(0, 1) * (-m * x_r + ub) - 2 * mp.pi * m * y_r)
                fu += (2 * mp.pi / m) * (mp.re(wp_p / (1 - wp_p)) + mp.re(wp_m / (1 - wp_m)))
                if abs(wp_p) < tol and abs(wp_m) < tol:
                    break
                m += 1
        else:
            fu = -mp.pi * (mp.psi(0, ua) + mp.psi(0, 1 - ua) + 2 * mp.log(2) + mp.log(y_r))
            k_max = int(mp.ceil((mp.mp.dps + 10) * mp.log(10) / (2 * mp.pi * y_r))) + 5
            for k in range(-k_max, k_max + 1):
                ka = k + ua
                wk = mp.exp(2 * mp.pi * mp.mpc(0, 1) * (ka * x_r + ub) - 2 * mp.pi * abs(ka) * y_r)
                fu += (2 * mp.pi / abs(ka)) * mp.re(wk / (1 - wk))
        nu = ua if ua <= mp.mpf(1) / 2 else ua - 1
        Bm = (-ub) % 1
        wz = nu * tau - Bm
        s_a0 = mp.mpc(0)
        m = 1
        while True:
            t1 = mp.exp(2 * mp.pi * mp.mpc(0, 1) * m * (tau + wz))
            t2 = mp.exp(2 * mp.pi * mp.mpc(0, 1) * m * (tau - wz))
            term = (t1 - t2) / (2 * mp.mpc(0, 1) * (1 - q ** m))
            s_a0 += term
            if abs(term) < tol and abs(q ** m) < tol:
                break
            m += 1
        a0 = mp.pi * mp.cot(mp.pi * wz) + 4 * mp.pi * s_a0 + 2 * mp.pi * mp.mpc(0, 1) * nu
        rad = ctx["s_old"] + fu - mp.pi * (abs(a0) ** 2) * ctx["exp_m2L2"]
        uch.append(mp.sqrt(rad) * Rch[si])

    YS = mp.zeros(3, 3)
    c3_S = ctx["c3_S"]
    if C_tS is None:
        for a in range(3):
            for b in range(3):
                vS = mp.mpc(0)
                for qi in range(3):
                    for si in range(4):
                        vS += c3_S[qi] * uch[si] * C_S[qi][si][a][b]
                YS[a, b] = vS
        return YS, None

    YtS = mp.zeros(3, 3)
    c3_tS = ctx["c3_tS"]
    for a in range(3):
        for b in range(3):
            vS = mp.mpc(0)
            vtS = mp.mpc(0)
            for qi in range(3):
                for si in range(4):
                    vS += c3_S[qi] * uch[si] * C_S[qi][si][a][b]
                    vtS += c3_tS[qi] * uch[si] * C_tS[qi][si][a][b]
            YS[a, b] = vS
            YtS[a, b] = vtS
    return YS, YtS


def build_weil(m_gal):
    """Construct projected D_m(a, b) blocks on W_3^+ and W_2^- and physical phase phi(a, b)."""
    zeta = mp.exp(2 * mp.pi * mp.mpc(0, 1) / 5)
    zm = zeta ** m_gal
    X = mp.zeros(5, 5)
    Z = mp.zeros(5, 5)
    for j in range(5):
        X[(j + 1) % 5, j] = 1
        Z[j, j] = zm ** j
    s2 = mp.sqrt(2)
    B3 = mp.matrix([
        [1, 0, 0],
        [0, 1 / s2, 0],
        [0, 0, 1 / s2],
        [0, 0, 1 / s2],
        [0, 1 / s2, 0],
    ])
    B2 = mp.matrix([
        [0, 0],
        [1 / s2, 0],
        [0, 1 / s2],
        [0, -1 / s2],
        [-1 / s2, 0],
    ])
    D3 = {}
    D2 = {}
    phi = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            Dm = (zm ** ((3 * a * b) % 5)) * (X ** a) * (Z ** b)
            D3[(a, b)] = B3.H * Dm * B3
            D2[(a, b)] = B2.H * Dm * B2
            phi[(a, b)] = zeta ** ((-a * b) % 5)
    return D3, D2, phi


def build_gramians_from_Yw(Yw_dict, D3, D2, phi):
    """Build O_3, O_2, phased sum S_ph, and dimension-normalized Gramians G_{a,X}."""
    Sph = mp.zeros(3, 3)
    O3 = mp.zeros(9, 9)
    O2 = mp.zeros(6, 6)
    for (a, b), Yw in Yw_dict.items():
        ph = phi[(a, b)]
        Sph += ph * Yw
        d3 = D3[(a, b)]
        d2 = D2[(a, b)]
        for i in range(3):
            for j in range(3):
                val = ph * Yw[i, j]
                for ca in range(3):
                    for cb in range(3):
                        O3[3 * i + ca, 3 * j + cb] += val * d3[ca, cb]
                for wa in range(2):
                    for wb in range(2):
                        O2[2 * i + wa, 2 * j + wb] += val * d2[wa, wb]
    G3L = mp.zeros(3, 3)
    G2L = mp.zeros(3, 3)
    G3R = mp.zeros(3, 3)
    G2R = mp.zeros(3, 3)
    for i in range(3):
        for k in range(3):
            G3L[i, k] = sum(
                O3[3 * i + ca, 3 * j + cb] * mp.conj(O3[3 * k + ca, 3 * j + cb])
                for ca in range(3) for j in range(3) for cb in range(3)
            ) / 3
            G2L[i, k] = sum(
                O2[2 * i + wa, 2 * j + wb] * mp.conj(O2[2 * k + wa, 2 * j + wb])
                for wa in range(2) for j in range(3) for wb in range(2)
            ) / 2
            G3R[i, k] = sum(
                mp.conj(O3[3 * j + ca, 3 * i + cb]) * O3[3 * j + ca, 3 * k + cb]
                for j in range(3) for ca in range(3) for cb in range(3)
            ) / 3
            G2R[i, k] = sum(
                mp.conj(O2[2 * j + wa, 2 * i + wb]) * O2[2 * j + wa, 2 * k + wb]
                for j in range(3) for wa in range(2) for wb in range(2)
            ) / 2
    return Sph, G3L, G2L, G3R, G2R


def eval_full_state_at_tau(tau, L2_val, E, C_S, C_tS, weil_data, check_ns=True):
    """Evaluate all 4 (m_gal, reading) states at tau with Jacobi, NS, and GEPP cross-checks."""
    ctx = prepare_tau_yukawa(tau, L2_val, E)
    Yb_S, Yb_tS = Y_from_tau_ctx(ctx, (mp.mpf(0), mp.mpf(0)), (mp.mpf(0), mp.mpf(0)), C_S, C_tS)
    Yw_S = {}
    Yw_tS = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            ac = a if a <= 2 else a - 5
            bc = b if b <= 2 else b - 5
            wL = (mp.mpf(ac) / 5, mp.mpf(bc) / 5)
            wR = (mp.mpf(2 * ac) / 5, mp.mpf(2 * bc) / 5)
            Yw_S[(a, b)], Yw_tS[(a, b)] = Y_from_tau_ctx(ctx, wL, wR, C_S, C_tS)

    out = {}
    for m_gal in (1, 3):
        D3, D2, phi = weil_data[m_gal]
        for rdg, Ybase, Yw_dict in [("S", Yb_S, Yw_S), ("tilde_S", Yb_tS, Yw_tS)]:
            Sph, G3L, G2L, G3R, G2R = build_gramians_from_Yw(Yw_dict, D3, D2, phi)
            K_QL = G3L + G2L
            K_LL = 3 * G3L + G2L
            K_uR = 2 * G3R
            K_dR = 2 * G3R + 2 * G2R
            K_eR = 2 * G2R

            det_err = mp.mpf(0)
            for mat in (G3L, G2L, G3R, G2R, K_QL, K_LL, K_uR, K_dR, K_eR):
                d_ge = det_gepp(mat)
                d_mp = mp.det(mat)
                rel = abs(d_ge - d_mp) / abs(d_mp)
                if rel > det_err:
                    det_err = rel

            Rud = mp.sqrt(mp.re(det_gepp(G3R + G2R) / det_gepp(G3R)))
            Red = mp.sqrt(mp.re((det_gepp(G3L + G2L) * det_gepp(G3R + G2R)) / (det_gepp(3 * G3L + G2L) * det_gepp(G2R))))

            inv_sq = {}
            max_ns_err = mp.mpf(0)
            for kname, Kmat in [("QL", K_QL), ("LL", K_LL), ("uR", K_uR), ("dR", K_dR), ("eR", K_eR)]:
                invJ = jacobi_hermitian_inv_sqrt(Kmat)
                inv_sq[kname] = invJ
                if check_ns:
                    invNS = newton_schulz_inv_sqrt(Kmat)
                    e_ns = max(abs(invJ[r, c] - invNS[r, c]) for r in range(3) for c in range(3))
                    if e_ns > max_ns_err:
                        max_ns_err = e_ns

            id_errs = {}
            phys_mats = {}
            for hol_name, Yhol in [("base_w0", Ybase), ("phased_sum", Sph)]:
                Yu = inv_sq["QL"] * Yhol * inv_sq["uR"]
                Yd = inv_sq["QL"] * Yhol * inv_sq["dR"]
                Ye = inv_sq["LL"] * Yhol * inv_sq["eR"]
                rat_ud = abs(det_gepp(Yu) / det_gepp(Yd))
                rat_ed = abs(det_gepp(Ye) / det_gepp(Yd))
                id_errs[hol_name] = max(abs(rat_ud - Rud), abs(rat_ed - Red))
                phys_mats[hol_name] = (Yu, Yd, Ye)

            out[(m_gal, rdg)] = {
                "Rud": Rud,
                "Red": Red,
                "id_err_base": id_errs["base_w0"],
                "id_err_phased": id_errs["phased_sum"],
                "ns_err": max_ns_err,
                "det_err": det_err,
                "Ybase": Ybase,
                "Sph": Sph,
                "G": (G3L, G2L, G3R, G2R),
                "K": (K_QL, K_LL, K_uR, K_dR, K_eR),
                "phys_mats": phys_mats,
            }
    return out


# ---------------------------------------------------------------------------
# Section 1: SymPy Cholesky SOS & 16-pt FD Grid
# ---------------------------------------------------------------------------

def verify_sympy_cholesky_sos():
    """Prove Cauchy-Binet SOS & diagonal positivity for 3x3 SPD matrices in SymPy."""
    d1, d2, d3 = sp.symbols("d1 d2 d3", positive=True)
    e1, e2, e3 = sp.symbols("e1 e2 e3", positive=True)
    a21, a31, a32 = sp.symbols("a21 a31 a32", real=True)
    b21, b31, b32 = sp.symbols("b21 b31 b32", real=True)
    L3 = sp.Matrix([[d1, 0, 0], [a21, d2, 0], [a31, a32, d3]])
    L2 = sp.Matrix([[e1, 0, 0], [b21, e2, 0], [b31, b32, e3]])
    G3 = L3 * L3.T
    G2 = L2 * L2.T
    diff_det = sp.expand(sp.det(G3 + G2) - sp.det(G3))

    B = sp.Matrix.hstack(L3, L2)
    minors_sq = []
    det_G2_term_found = False
    for cols in combinations(range(6), 3):
        if cols == (0, 1, 2):
            continue
        m = sp.det(B[:, list(cols)])
        m_sq = sp.expand(m ** 2)
        minors_sq.append(m_sq)
        if cols == (3, 4, 5):
            assert sp.expand(m_sq - (e1 * e2 * e3) ** 2) == 0
            det_G2_term_found = True

    sos_diff = sp.expand(sum(minors_sq) - diff_det)
    assert sos_diff == 0 and det_G2_term_found

    diag_subs = {a21: 0, a31: 0, a32: 0, b21: 0, b31: 0, b32: 0}
    diag_diff = sp.expand(diff_det.subs(diag_subs))
    expected_diag = sp.expand(
        (d1 ** 2 + e1 ** 2) * (d2 ** 2 + e2 ** 2) * (d3 ** 2 + e3 ** 2)
        - (d1 * d2 * d3) ** 2
    )
    assert sp.expand(diag_diff - expected_diag) == 0
    # Verify all 7 coefficients in (d_i^2, e_i^2) are strictly +1
    poly_diag = sp.Poly(diag_diff, d1, d2, d3, e1, e2, e3)
    assert len(poly_diag.coeffs()) == 7 and all(c == 1 for c in poly_diag.coeffs())

    M = L3.inv() * L2
    ratio_diff = sp.simplify(sp.det(G3 + G2) / sp.det(G3) - sp.det(sp.eye(3) + M * M.T))
    assert ratio_diff == 0

    lam1, lam2, lam3 = sp.symbols("lam1 lam2 lam3", real=True)
    e_1 = lam1 ** 2 + lam2 ** 2 + lam3 ** 2
    e_2 = (lam1 * lam2) ** 2 + (lam1 * lam3) ** 2 + (lam2 * lam3) ** 2
    e_3 = (lam1 * lam2 * lam3) ** 2
    eig_diff = sp.expand((1 + lam1 ** 2) * (1 + lam2 ** 2) * (1 + lam3 ** 2) - (1 + e_1 + e_2 + e_3))
    assert eig_diff == 0

    return {
        "cauchy_binet_19_minors_sos_exact": True,
        "diagonal_7_positive_terms_exact": True,
        "ratio_I_plus_MMT_exact": True,
        "eigenvalue_elementary_symm_exact": True,
    }


def haar_su3(rng):
    """Generate a random Haar SU(3) matrix at active mpmath precision via Mezzadri QR."""
    M = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u1 = mp.mpf(rng.randint(1, 10 ** 16)) / (10 ** 16 + 1)
            u2 = mp.mpf(rng.randint(0, 10 ** 16 - 1)) / (10 ** 16)
            u3 = mp.mpf(rng.randint(1, 10 ** 16)) / (10 ** 16 + 1)
            u4 = mp.mpf(rng.randint(0, 10 ** 16 - 1)) / (10 ** 16)
            re_v = mp.sqrt(-2 * mp.log(u1)) * mp.cos(2 * mp.pi * u2)
            im_v = mp.sqrt(-2 * mp.log(u3)) * mp.sin(2 * mp.pi * u4)
            M[r, c] = mp.mpc(re_v, im_v)
    Q, R = mp.qr(M)
    for j in range(3):
        ph = R[j, j] / abs(R[j, j])
        for i in range(3):
            Q[i, j] *= ph
    detQ = det_gepp(Q)
    return Q * (detQ ** (-mp.mpf(1) / 3))


def run_section_1(fd_cache, E, C_S, C_tS, weil_data):
    """Run P-862 symbolic Cholesky + 16-pt FD grid (UF-1..UF-4) at dps=50."""
    sym_res = verify_sympy_cholesky_sos()
    mp.mp.dps = 50
    F16 = [
        ("0+11/10i", mp.mpc(0, mp.mpf(11) / 10)),
        ("0+3/2i", mp.mpc(0, mp.mpf(3) / 2)),
        ("0+5/2i", mp.mpc(0, mp.mpf(5) / 2)),
        ("0+5i", mp.mpc(0, mp.mpf(5))),
        ("1/2+i", mp.mpc(mp.mpf(1) / 2, 1)),
        ("-1/2+7/5i", mp.mpc(-mp.mpf(1) / 2, mp.mpf(7) / 5)),
        ("1/2+2i", mp.mpc(mp.mpf(1) / 2, 2)),
        ("-1/2+4i", mp.mpc(-mp.mpf(1) / 2, 4)),
        ("5/13+12/13i", mp.mpc(mp.mpf(5) / 13, mp.mpf(12) / 13)),
        ("-7/25+24/25i", mp.mpc(-mp.mpf(7) / 25, mp.mpf(24) / 25)),
        ("13/100+17/10i", mp.mpc(mp.mpf(13) / 100, mp.mpf(17) / 10)),
        ("-1/5+2i", mp.mpc(-mp.mpf(1) / 5, 2)),
        ("1/3+3i", mp.mpc(mp.mpf(1) / 3, 3)),
        ("-2/5+4i", mp.mpc(-mp.mpf(2) / 5, 4)),
        ("1/10+5i", mp.mpc(mp.mpf(1) / 10, 5)),
        ("13/100+6i", mp.mpc(mp.mpf(13) / 100, 6)),
    ]

    max_id_err = mp.mpf(0)
    max_ns_err = mp.mpf(0)
    max_det_err = mp.mpf(0)
    min_Rud_all = mp.mpf(10) ** 9
    min_Red_all = mp.mpf(10) ** 9
    min_Rud_m1 = mp.mpf(10) ** 9
    min_Red_m1 = mp.mpf(10) ** 9
    max_Red_m1 = mp.mpf(0)
    min_Rud_m3 = mp.mpf(10) ** 9
    max_Rud_m3 = mp.mpf(0)
    min_Red_m3 = mp.mpf(10) ** 9

    tau0_state = None
    grid_summary = []

    for label, tau in F16:
        L2_v = eval_L2_gauss_reduced(tau, fd_cache, target_dps=50, high_acc=True)
        res = eval_full_state_at_tau(tau, L2_v, E, C_S, C_tS, weil_data, check_ns=True)
        if label == "13/100+17/10i":
            tau0_state = (tau, L2_v, res)
        pt_rec = {"label": label, "L2": mp.nstr(L2_v, 18), "states": {}}
        for (m_gal, rdg), st in res.items():
            Rud = st["Rud"]
            Red = st["Red"]
            max_id_err = max(max_id_err, st["id_err_base"], st["id_err_phased"])
            max_ns_err = max(max_ns_err, st["ns_err"])
            max_det_err = max(max_det_err, st["det_err"])
            min_Rud_all = min(min_Rud_all, Rud)
            min_Red_all = min(min_Red_all, Red)
            if m_gal == 1:
                min_Rud_m1 = min(min_Rud_m1, Rud)
                min_Red_m1 = min(min_Red_m1, Red)
                max_Red_m1 = max(max_Red_m1, Red)
            else:
                min_Rud_m3 = min(min_Rud_m3, Rud)
                max_Rud_m3 = max(max_Rud_m3, Rud)
                min_Red_m3 = min(min_Red_m3, Red)
            pt_rec["states"][f"m{m_gal}_{rdg}"] = {
                "Rud": mp.nstr(Rud, 16),
                "Red": mp.nstr(Red, 16),
                "id_err": mp.nstr(max(st["id_err_base"], st["id_err_phased"]), 4),
                "ns_err": mp.nstr(st["ns_err"], 4),
            }
        grid_summary.append(pt_rec)

    assert max_id_err < mp.mpf(1) / (10 ** 25), f"max_id_err={max_id_err}"
    assert max_ns_err < mp.mpf(1) / (10 ** 35), f"max_ns_err={max_ns_err}"
    assert max_det_err < mp.mpf(1) / (10 ** 30), f"max_det_err={max_det_err}"
    # UF-1
    assert min_Rud_all > mp.mpf(51) / 50 and min_Red_all > mp.mpf(3) / 2
    # UF-2
    assert min_Rud_m1 > mp.mpf(3) / 2 and min_Red_m1 > mp.mpf(3) / 2 and max_Red_m1 < mp.mpf(5)
    assert min_Rud_m3 > mp.mpf(1) and max_Rud_m3 < mp.mpf(5) / 4 and min_Red_m3 > mp.mpf(10)

    # UF-3: Removable-singularity continuity at i and rho
    uf3_res = {}
    eps_orb = mp.mpf(1) / (10 ** 6)
    for orb_name, tau_orb in [
        ("i", mp.mpc(0, 1)),
        ("rho", mp.mpc(-mp.mpf(1) / 2, mp.sqrt(3) / 2)),
    ]:
        L2_orb = eval_L2_gauss_reduced(tau_orb, fd_cache, target_dps=50, high_acc=True)
        st_orb = eval_full_state_at_tau(tau_orb, L2_orb, E, C_S, C_tS, weil_data, check_ns=True)[(1, "S")]
        _, sv_b, _ = mp.svd_c(st_orb["Ybase"])
        _, sv_s, _ = mp.svd_c(st_orb["Sph"])
        rat_base = sv_b[2] / sv_b[0]
        rat_sph = sv_s[2] / sv_s[0]
        assert rat_base < mp.mpf(1) / (10 ** 35)
        assert rat_sph < mp.mpf(1) / (10 ** 35)
        assert st_orb["Rud"] > mp.mpf(3) / 2
        # Note: at tau_orb in {i, rho}, det(Y_hol) == 0 (forced null mode), so det(Y_u)/det(Y_d) has the removable 0/0 singularity;
        # we verify the exact cancellation identity at the nearby non-singular point tau_pert = tau_orb + (1/10)^6 i below.
        assert st_orb["ns_err"] < mp.mpf(1) / (10 ** 35)

        tau_pert = tau_orb + mp.mpc(0, eps_orb)
        L2_pert = eval_L2_gauss_reduced(tau_pert, fd_cache, target_dps=50, high_acc=True)
        st_pert = eval_full_state_at_tau(tau_pert, L2_pert, E, C_S, C_tS, weil_data, check_ns=False)[(1, "S")]
        assert max(st_pert["id_err_base"], st_pert["id_err_phased"]) < mp.mpf(1) / (10 ** 25)
        diff_pert = abs(st_pert["Rud"] - st_orb["Rud"])
        assert diff_pert < mp.mpf(1) / (10 ** 4), f"UF-3 continuity failed at {orb_name}: {diff_pert}"
        uf3_res[orb_name] = {
            "sv3_over_sv1_base": mp.nstr(rat_base, 6),
            "sv3_over_sv1_phased": mp.nstr(rat_sph, 6),
            "Rud_orb": mp.nstr(st_orb["Rud"], 16),
            "Rud_pert_diff": mp.nstr(diff_pert, 6),
            "pert_id_err": mp.nstr(max(st_pert["id_err_base"], st_pert["id_err_phased"]), 6),
        }

    # UF-4: Modular T, S & 10-trial Haar SU(3)^5 invariance at tau_0
    tau0, L2_0, res0 = tau0_state
    tauT = tau0 + 1
    tauS = -1 / tau0
    L2_T = eval_L2_gauss_reduced(tauT, fd_cache, target_dps=50, high_acc=True)
    L2_S = eval_L2_gauss_reduced(tauS, fd_cache, target_dps=50, high_acc=True)
    resT = eval_full_state_at_tau(tauT, L2_T, E, C_S, C_tS, weil_data, check_ns=False)
    resS = eval_full_state_at_tau(tauS, L2_S, E, C_S, C_tS, weil_data, check_ns=False)
    max_T_drift = mp.mpf(0)
    max_S_drift = mp.mpf(0)
    for k_st in res0:
        max_T_drift = max(max_T_drift, abs(resT[k_st]["Rud"] - res0[k_st]["Rud"]), abs(resT[k_st]["Red"] - res0[k_st]["Red"]))
        max_S_drift = max(max_S_drift, abs(resS[k_st]["Rud"] - res0[k_st]["Rud"]), abs(resS[k_st]["Red"] - res0[k_st]["Red"]))
    assert max_T_drift < mp.mpf(1) / (10 ** 25)
    assert max_S_drift < mp.mpf(1) / (10 ** 25)

    st_1S = res0[(1, "S")]
    K_QL, K_LL, K_uR, K_dR, K_eR = st_1S["K"]
    Sph = st_1S["Sph"]
    Yu_0, Yd_0, Ye_0 = st_1S["phys_mats"]["phased_sum"]
    ref_ud = abs(det_gepp(Yu_0) / det_gepp(Yd_0))
    ref_ed = abs(det_gepp(Ye_0) / det_gepp(Yd_0))
    rng = random.Random(20261119)
    max_haar_err = mp.mpf(0)
    for _ in range(10):
        U_QL = haar_su3(rng)
        U_LL = haar_su3(rng)
        U_uR = haar_su3(rng)
        U_dR = haar_su3(rng)
        U_eR = haar_su3(rng)
        inv_QL = jacobi_hermitian_inv_sqrt(U_QL * K_QL * U_QL.H)
        inv_LL = jacobi_hermitian_inv_sqrt(U_LL * K_LL * U_LL.H)
        inv_uR = jacobi_hermitian_inv_sqrt(U_uR * K_uR * U_uR.H)
        inv_dR = jacobi_hermitian_inv_sqrt(U_dR * K_dR * U_dR.H)
        inv_eR = jacobi_hermitian_inv_sqrt(U_eR * K_eR * U_eR.H)
        Yu_p = inv_QL * (U_QL * Sph * U_uR.H) * inv_uR
        Yd_p = inv_QL * (U_QL * Sph * U_dR.H) * inv_dR
        Ye_p = inv_LL * (U_LL * Sph * U_eR.H) * inv_eR
        ud_p = abs(det_gepp(Yu_p) / det_gepp(Yd_p))
        ed_p = abs(det_gepp(Ye_p) / det_gepp(Yd_p))
        max_haar_err = max(max_haar_err, abs(ud_p - ref_ud), abs(ed_p - ref_ed))
    assert max_haar_err < mp.mpf(1) / (10 ** 30)

    return {
        "sympy_cholesky": sym_res,
        "max_id_err": mp.nstr(max_id_err, 6),
        "max_ns_err": mp.nstr(max_ns_err, 6),
        "max_det_err": mp.nstr(max_det_err, 6),
        "UF1": {"min_Rud": mp.nstr(min_Rud_all, 12), "min_Red": mp.nstr(min_Red_all, 12)},
        "UF2": {
            "m1_Rud_min": mp.nstr(min_Rud_m1, 12),
            "m1_Red_range": [mp.nstr(min_Red_m1, 12), mp.nstr(max_Red_m1, 12)],
            "m3_Rud_range": [mp.nstr(min_Rud_m3, 12), mp.nstr(max_Rud_m3, 12)],
            "m3_Red_min": mp.nstr(min_Red_m3, 12),
        },
        "UF3": uf3_res,
        "UF4": {
            "T_drift": mp.nstr(max_T_drift, 6),
            "S_drift": mp.nstr(max_S_drift, 6),
            "haar_10_trial_max_err": mp.nstr(max_haar_err, 6),
        },
        "grid_64": grid_summary,
        "tau0_state": tau0_state,
    }


# ---------------------------------------------------------------------------
# Section 2: W-P1c Process Clocks A, B, C
# ---------------------------------------------------------------------------

def clenshaw_curtis_lobatto(M):
    """Return M+1 Clenshaw-Curtis Lobatto nodes and positive weights on [-1, 1]."""
    nodes = [mp.cos(j * mp.pi / M) for j in range(M + 1)]
    weights = []
    half = M // 2
    for j in range(M + 1):
        cj = mp.mpf(1) if (j == 0 or j == M) else mp.mpf(2)
        s = mp.mpf(0)
        for k in range(1, half + 1):
            bk = mp.mpf(1) if (2 * k == M) else mp.mpf(2)
            s += (bk / (4 * k * k - 1)) * mp.cos(2 * k * j * mp.pi / M)
        weights.append((cj / M) * (1 - s))
    return nodes, weights


def eval_clock_R_at_tau(tau, fd_cache, E25, CS25, weil25, m_list=(1, 3)):
    """Evaluate R_ud, R_ed, and swapped R_ud^{swap} at tau for reading S (at dps=25)."""
    old_dps = mp.mp.dps
    L2_v = eval_L2_gauss_reduced(tau, fd_cache, target_dps=22, high_acc=False)
    mp.mp.dps = 25
    tau25 = mp.mpc(tau)
    L2_25 = mp.mpf(L2_v)
    ctx = prepare_tau_yukawa(tau25, L2_25, E25)
    Yw_dict = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            ac = a if a <= 2 else a - 5
            bc = b if b <= 2 else b - 5
            wL = (mp.mpf(ac) / 5, mp.mpf(bc) / 5)
            wR = (mp.mpf(2 * ac) / 5, mp.mpf(2 * bc) / 5)
            Yw, _ = Y_from_tau_ctx(ctx, wL, wR, CS25, None)
            Yw_dict[(a, b)] = Yw
    out = {}
    for m_gal in m_list:
        D3, D2, phi = weil25[m_gal]
        _, G3L, G2L, G3R, G2R = build_gramians_from_Yw(Yw_dict, D3, D2, phi)
        d3R = det_gepp(G3R)
        d32R = det_gepp(G3R + G2R)
        d32L = det_gepp(G3L + G2L)
        d332L = det_gepp(3 * G3L + G2L)
        d2R = det_gepp(G2R)
        Rud = mp.sqrt(mp.re(d32R / d3R))
        Red = mp.sqrt(mp.re((d32L * d32R) / (d332L * d2R)))
        # Swapped hypercharge metrics K_{uR}^{swap} = 2 G_{3,R} + 2 G_{2,R}, K_{dR}^{swap} = 2 G_{3,R}
        Rud_swap = mp.sqrt(mp.re(det_gepp(2 * G3R) / det_gepp(2 * G3R + 2 * G2R)))
        out[m_gal] = (Rud, Red, Rud_swap)
    mp.mp.dps = old_dps
    return out


def run_section_2(fd_cache):
    """Run W-P1c 64 length-6 words and Process Clocks A, B, C (plus PFU4-2 data)."""
    mp.mp.dps = 25
    E25, CS25, _ = build_yukawa_helpers()
    weil25 = {1: build_weil(1), 3: build_weil(3)}

    def mat_mul(A, B):
        return (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
        )

    L_mat = ((1, 1), (0, 1))
    R_mat = ((1, 0), (1, 1))
    parabolic_words = []
    hyperbolic_words = []
    pell_words = {}
    word_eval_cache = {}
    rho_conj = mp.mpc(mp.mpf(1) / 2, mp.sqrt(3) / 2)

    for w in product("LR", repeat=6):
        w_str = "".join(w)
        M = ((1, 0), (0, 1))
        for ch in w:
            M = mat_mul(M, L_mat if ch == "L" else R_mat)
        tr = M[0][0] + M[1][1]
        if tr == 2:
            parabolic_words.append(w_str)
        else:
            assert tr > 2 and M[1][0] > 0
            a, _, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
            apex = (mp.mpf(a - d) + mp.mpc(0, 1) * mp.sqrt(tr * tr - 4)) / (2 * c)
            fd, _ = gauss_reduce_sl2z(apex)
            # Identify x = -1/2 boundary with +1/2 via T
            if abs(mp.re(fd) + mp.mpf(1) / 2) < mp.mpf(1) / (10 ** 18):
                fd = fd + 1
            if w_str in ("LRRLRR", "RRLRRL"):
                assert tr == 14
                assert abs(fd - rho_conj) < mp.mpf(1) / (10 ** 20)
                pell_words[w_str] = {"tr": tr, "fd_apex_err": mp.nstr(abs(fd - rho_conj), 6)}
            key = (mp.nstr(mp.re(fd), 15), mp.nstr(mp.im(fd), 15))
            if key not in word_eval_cache:
                word_eval_cache[key] = eval_clock_R_at_tau(fd, fd_cache, E25, CS25, weil25, m_list=(1, 3))
            ell = 2 * mp.acosh(mp.mpf(tr) / 2)
            hyperbolic_words.append((w_str, tr, ell, word_eval_cache[key]))

    assert set(parabolic_words) == {"LLLLLL", "RRRRRR"}
    assert len(hyperbolic_words) == 62 and set(pell_words.keys()) == {"LRRLRR", "RRLRRL"}

    clock_AB = {}
    for m_gal in (1, 3):
        ln_ud_A = sum(mp.log(r[m_gal][0]) for _, _, _, r in hyperbolic_words) / len(hyperbolic_words)
        ln_ed_A = sum(mp.log(r[m_gal][1]) for _, _, _, r in hyperbolic_words) / len(hyperbolic_words)
        ln_ud_swap_A = sum(mp.log(r[m_gal][2]) for _, _, _, r in hyperbolic_words) / len(hyperbolic_words)
        wsum = sum(ell for _, _, ell, _ in hyperbolic_words)
        ln_ud_B = sum(ell * mp.log(r[m_gal][0]) for _, _, ell, r in hyperbolic_words) / wsum
        ln_ed_B = sum(ell * mp.log(r[m_gal][1]) for _, _, ell, r in hyperbolic_words) / wsum
        ln_ud_swap_B = sum(ell * mp.log(r[m_gal][2]) for _, _, ell, r in hyperbolic_words) / wsum
        clock_AB[m_gal] = {
            "A": {"ln_Rud": ln_ud_A, "ln_Red": ln_ed_A, "ln_Rud_swap": ln_ud_swap_A},
            "B": {"ln_Rud": ln_ud_B, "ln_Red": ln_ed_B, "ln_Rud_swap": ln_ud_swap_B},
        }

    # Clock C: 2D Clenshaw-Curtis Lobatto (N_x=12, N_y=14) over F_6
    ux, wx = clenshaw_curtis_lobatto(12)
    vy, wy = clenshaw_curtis_lobatto(14)
    area_exact = mp.pi / 3 - mp.mpf(1) / 6
    area_num = mp.mpf(0)
    int_ud = mp.mpf(0)
    int_ed = mp.mpf(0)
    int_ud_swap = mp.mpf(0)
    for ix in range(13):
        x = ux[ix] / 2
        dx_w = wx[ix] / 2
        y_min = mp.sqrt(1 - x * x)
        y_max = mp.mpf(6)
        half_y = (y_max - y_min) / 2
        mid_y = (y_max + y_min) / 2
        for iy in range(15):
            y = mid_y + half_y * vy[iy]
            w_tot = dx_w * half_y * wy[iy] / (y * y)
            area_num += w_tot
            tau_q = mp.mpc(x, y)
            r = eval_clock_R_at_tau(tau_q, fd_cache, E25, CS25, weil25, m_list=(1,))
            int_ud += w_tot * mp.log(r[1][0])
            int_ed += w_tot * mp.log(r[1][1])
            int_ud_swap += w_tot * mp.log(r[1][2])
    area_err = abs(area_num - area_exact)
    assert area_err < mp.mpf(1) / 1000, f"Clock C area_err={area_err}"
    ln_ud_C = int_ud / area_exact
    ln_ed_C = int_ed / area_exact
    ln_ud_swap_C = int_ud_swap / area_exact

    # Verify sealed clock bars for (m=1, S)
    ud_m1 = [clock_AB[1]["A"]["ln_Rud"], clock_AB[1]["B"]["ln_Rud"], ln_ud_C]
    ed_m1 = [clock_AB[1]["A"]["ln_Red"], clock_AB[1]["B"]["ln_Red"], ln_ed_C]
    spread_ud_m1 = max(ud_m1) - min(ud_m1)
    spread_ed_m1 = max(ed_m1) - min(ed_m1)
    assert all(mp.mpf(11) / 20 < v < mp.mpf(3) / 4 for v in ud_m1)
    assert spread_ud_m1 < mp.mpf(1) / 20
    assert all(mp.mpf(1) < v < mp.mpf(7) / 5 for v in ed_m1)
    assert spread_ed_m1 < mp.mpf(3) / 20

    # Verify sealed clock bars for (m=3, S)
    ud_m3 = [clock_AB[3]["A"]["ln_Rud"], clock_AB[3]["B"]["ln_Rud"]]
    ed_m3 = [clock_AB[3]["A"]["ln_Red"], clock_AB[3]["B"]["ln_Red"]]
    assert all(0 < v < mp.mpf(1) / 4 for v in ud_m3)
    assert all(v > mp.mpf(5) / 2 for v in ed_m3)

    return {
        "word_counts": {"total": 64, "parabolic": len(parabolic_words), "hyperbolic": len(hyperbolic_words), "unique_fd": len(word_eval_cache)},
        "pell_words": pell_words,
        "m1_S": {
            "Clock_A_ln_Rud": mp.nstr(clock_AB[1]["A"]["ln_Rud"], 12),
            "Clock_B_ln_Rud": mp.nstr(clock_AB[1]["B"]["ln_Rud"], 12),
            "Clock_C_ln_Rud": mp.nstr(ln_ud_C, 12),
            "spread_ln_Rud": mp.nstr(spread_ud_m1, 8),
            "Clock_A_ln_Red": mp.nstr(clock_AB[1]["A"]["ln_Red"], 12),
            "Clock_B_ln_Red": mp.nstr(clock_AB[1]["B"]["ln_Red"], 12),
            "Clock_C_ln_Red": mp.nstr(ln_ed_C, 12),
            "spread_ln_Red": mp.nstr(spread_ed_m1, 8),
        },
        "m3_S": {
            "Clock_A_ln_Rud": mp.nstr(clock_AB[3]["A"]["ln_Rud"], 12),
            "Clock_B_ln_Rud": mp.nstr(clock_AB[3]["B"]["ln_Rud"], 12),
            "Clock_A_ln_Red": mp.nstr(clock_AB[3]["A"]["ln_Red"], 12),
            "Clock_B_ln_Red": mp.nstr(clock_AB[3]["B"]["ln_Red"], 12),
        },
        "clock_C_area_err": mp.nstr(area_err, 6),
        "swapped_m1_clocks": [clock_AB[1]["A"]["ln_Rud_swap"], clock_AB[1]["B"]["ln_Rud_swap"], ln_ud_swap_C],
    }


# ---------------------------------------------------------------------------
# Section 3: 58-Node Epistemic DAG v2 (Tarjan SCC + Kahn Rank Propagation)
# ---------------------------------------------------------------------------

def build_58_node_dag():
    """Construct exact 58-node Epistemic DAG v2 specification."""
    nodes = {}

    def add(name, cat, irk, parents, stab):
        assert name not in nodes
        nodes[name] = {
            "category": cat,
            "intrinsic_rank": irk,
            "parents": list(parents),
            "stabilized": stab,
        }

    # ROOT (9, irk=0, stab=True)
    for r in [
        "G:m004_Mostow_Rigidity",
        "G:m000_Amphichiral_Collar",
        "G:Adams_Maximal_Horotorus",
        "G:Wang_Stokes_Homology",
        "G:Spin10_2D_Anomaly_Plane",
        "G:Weil5_CAR_Cl10_PostulateD",
        "G:E8_Prime3_Prime5_Orthogonality",
        "G:Culler_Spin_Bordism_Bar_Gap",
        "G:D5_Irregular_Cover_8_3_4",
    ]:
        add(r, "ROOT", 0, [], True)

    # OPERATOR (9)
    add("OP:BPV_MV_2Loop_RGE", "OPERATOR", 0, ["G:Spin10_2D_Anomaly_Plane", "G:Weil5_CAR_Cl10_PostulateD"], True)
    add("OP:PatiSalam_Z2D_Breaking", "OPERATOR", 1, ["G:m000_Amphichiral_Collar", "G:Spin10_2D_Anomaly_Plane", "G:E8_Prime3_Prime5_Orthogonality"], True)
    add("OP:Kaplan_4D_Amphicheiral_Kink", "OPERATOR", 1, ["G:m000_Amphichiral_Collar", "G:Culler_Spin_Bordism_Bar_Gap", "G:E8_Prime3_Prime5_Orthogonality"], True)
    add("OP:CIM_33m6_Triple_Overlap", "OPERATOR", 1, ["G:Adams_Maximal_Horotorus", "G:Wang_Stokes_Homology", "G:E8_Prime3_Prime5_Orthogonality"], True)
    add("OP:Level6_Higgs_v_plus_minus_pi6_Pair", "OPERATOR", 2, ["OP:CIM_33m6_Triple_Overlap", "G:m004_Mostow_Rigidity"], False)
    add("OP:Covariant_Majorana_Jets", "OPERATOR", 1, ["OP:CIM_33m6_Triple_Overlap"], True)
    add("OP:SchwingerDyson_Singlet_Resolvent", "OPERATOR", 1, ["OP:Covariant_Majorana_Jets"], True)
    add("OP:Fock_Exterior_Weil_Yukawa_Om", "OPERATOR", 0, ["G:D5_Irregular_Cover_8_3_4", "G:Weil5_CAR_Cl10_PostulateD", "OP:CIM_33m6_Triple_Overlap"], True)
    add("OP:Level6_Box_Quartic_vs_CW_Dichotomy", "OPERATOR", 1, ["OP:CIM_33m6_Triple_Overlap", "G:Spin10_2D_Anomaly_Plane"], True)

    # SEAM (8, stab=False)
    add("S:Parity_Det_Sign_Bit", "SEAM", 2, ["OP:Kaplan_4D_Amphicheiral_Kink"], False)
    add("S:Residual_Z2_TM1_Bit", "SEAM", 2, ["OP:SchwingerDyson_Singlet_Resolvent"], False)
    add("S:Collar_Modulus_Delta_PS", "SEAM", 3, ["OP:PatiSalam_Z2D_Breaking", "OP:Kaplan_4D_Amphicheiral_Kink"], False)
    add("S:Unified_Coupling_Alpha_U", "SEAM", 3, ["OP:PatiSalam_Z2D_Breaking"], False)
    add("S:Bidoublet_Angle_Beta", "SEAM", 3, ["OP:PatiSalam_Z2D_Breaking"], False)
    add("S:Torsion_Tau_SU2R_Break", "SEAM", 3, ["OP:CIM_33m6_Triple_Overlap"], False)
    add("S:Resolvent_Loop_Coupling_Kappa", "SEAM", 3, ["OP:SchwingerDyson_Singlet_Resolvent"], False)
    add("S:EWSB_Scale_Anchor_vEW", "SEAM", 3, ["OP:BPV_MV_2Loop_RGE"], False)

    # RELATION (13, stab=True)
    add("PR-1:Global_Z6_Hypercharge", "RELATION", 0, ["G:Weil5_CAR_Cl10_PostulateD", "G:Spin10_2D_Anomaly_Plane"], True)
    add("PR-2:3Fam_Strong_CP_Zero", "RELATION", 2, ["OP:PatiSalam_Z2D_Breaking", "OP:Kaplan_4D_Amphicheiral_Kink", "OP:BPV_MV_2Loop_RGE", "S:Parity_Det_Sign_Bit"], True)
    add("PR-3:PatiSalam_2Loop_Corridor", "RELATION", 1, ["OP:PatiSalam_Z2D_Breaking", "OP:BPV_MV_2Loop_RGE"], True)
    add("PR-4:Dterm_Higgs_IR_Envelope", "RELATION", 1, ["OP:PatiSalam_Z2D_Breaking", "OP:BPV_MV_2Loop_RGE"], True)
    add("PR-5:Level6_Higgs_1Bit_Pair", "RELATION", 2, ["OP:Level6_Higgs_v_plus_minus_pi6_Pair"], True)
    add("PR-6:PS_3BL_288_CKM_Alignment", "RELATION", 1, ["OP:CIM_33m6_Triple_Overlap", "OP:PatiSalam_Z2D_Breaking"], True)
    add("PR-7:PS_Lepton_Down_Split", "RELATION", 1, ["OP:CIM_33m6_Triple_Overlap", "OP:PatiSalam_Z2D_Breaking"], True)
    add("PR-8:Even_Delta_SL2Z_Gramian", "RELATION", 1, ["OP:CIM_33m6_Triple_Overlap", "OP:PatiSalam_Z2D_Breaking"], True)
    add("PR-9:TM1_Solar_Reactor_SumRule", "RELATION", 2, ["OP:SchwingerDyson_Singlet_Resolvent", "OP:BPV_MV_2Loop_RGE", "S:Residual_Z2_TM1_Bit"], True)
    add("PR-10:Picard_Casimir_Scale_Law", "RELATION", 0, ["OP:BPV_MV_2Loop_RGE", "G:m004_Mostow_Rigidity", "G:Culler_Spin_Bordism_Bar_Gap"], True)
    add("PR-11:P874_Weil_Class_Separation", "RELATION", 1, ["OP:Fock_Exterior_Weil_Yukawa_Om", "G:D5_Irregular_Cover_8_3_4"], True)
    add("PR-12:B1962_B1963_Cusp_Alignment_And_Lepton_Split", "RELATION", 1, ["OP:Fock_Exterior_Weil_Yukawa_Om", "OP:Level6_Box_Quartic_vs_CW_Dichotomy"], True)
    add("PR-13:P862_WP1c_Universal_Yu_Over_Yd_Law", "RELATION", 1, ["OP:Fock_Exterior_Weil_Yukawa_Om", "G:Culler_Spin_Bordism_Bar_Gap"], True)

    # SM_TARGET (19, irk=0, stab=True)
    sm_yuk_parents = [
        "OP:Fock_Exterior_Weil_Yukawa_Om",
        "OP:Level6_Box_Quartic_vs_CW_Dichotomy",
        "OP:Kaplan_4D_Amphicheiral_Kink",
        "OP:BPV_MV_2Loop_RGE",
        "S:Torsion_Tau_SU2R_Break",
        "S:Bidoublet_Angle_Beta",
    ]
    for sm in [
        "SM01:y_u", "SM02:y_c", "SM03:y_t",
        "SM04:y_d", "SM05:y_s", "SM06:y_b",
        "SM07:y_e", "SM08:y_mu", "SM09:y_tau",
        "SM10:V_us", "SM11:V_cb", "SM12:V_ub", "SM13:delta_CKM",
    ]:
        add(sm, "SM_TARGET", 0, sm_yuk_parents, True)

    sm_gauge_parents = [
        "PR-3:PatiSalam_2Loop_Corridor",
        "S:Unified_Coupling_Alpha_U",
        "S:Collar_Modulus_Delta_PS",
        "S:EWSB_Scale_Anchor_vEW",
    ]
    for sm in ["SM14:g_1", "SM15:g_2", "SM16:g_3"]:
        add(sm, "SM_TARGET", 0, sm_gauge_parents, True)

    add("SM17:m_H_over_vEW", "SM_TARGET", 0, ["PR-4:Dterm_Higgs_IR_Envelope", "S:Bidoublet_Angle_Beta", "SM03:y_t", "SM16:g_3"], True)
    add("SM18:v_EW", "SM_TARGET", 0, ["PR-10:Picard_Casimir_Scale_Law", "S:EWSB_Scale_Anchor_vEW"], True)
    add("SM19:bar_theta_QCD", "SM_TARGET", 0, ["PR-2:3Fam_Strong_CP_Zero"], True)

    return nodes


def tarjan_scc(nodes):
    """Run Tarjan strongly connected components algorithm to detect all cycles and self-loops."""
    adj = {u: [] for u in nodes}
    for v, info in nodes.items():
        for u in info["parents"]:
            assert u in nodes, f"Missing parent {u} of {v}"
            adj[u].append(v)

    index_counter = 0
    indices = {}
    lowlink = {}
    stack = []
    on_stack = set()
    sccs = []

    def strongconnect(v):
        nonlocal index_counter
        indices[v] = index_counter
        lowlink[v] = index_counter
        index_counter += 1
        stack.append(v)
        on_stack.add(v)
        for w in adj[v]:
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])
        if lowlink[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            sccs.append(comp)

    for v in nodes:
        if v not in indices:
            strongconnect(v)

    self_loops = [u for u in nodes if u in adj[u]]
    cyclic_sccs = [c for c in sccs if len(c) > 1]
    return adj, sccs, cyclic_sccs, self_loops


def analyze_dag(nodes):
    """Run Tarjan SCC, Kahn topological rank propagation, and Guardrail 1 & 5 checks."""
    adj, sccs, cyclic_sccs, self_loops = tarjan_scc(nodes)
    is_acyclic = (len(cyclic_sccs) == 0 and len(self_loops) == 0)

    seam_honesty_violations = [
        name for name, info in nodes.items()
        if (not info["stabilized"]) and info["intrinsic_rank"] <= 0
    ]

    if not is_acyclic:
        return {
            "is_acyclic": False,
            "cyclic_sccs": cyclic_sccs,
            "self_loops": self_loops,
            "seam_honesty_violations": seam_honesty_violations,
            "prop_ranks": None,
        }

    indeg = {v: len(info["parents"]) for v, info in nodes.items()}
    queue = [v for v, d in indeg.items() if d == 0]
    topo = []
    idx = 0
    while idx < len(queue):
        u = queue[idx]
        idx += 1
        topo.append(u)
        for w in adj[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                queue.append(w)
    assert len(topo) == len(nodes)

    prop = {}
    for v in topo:
        p_ranks = [nodes[p]["intrinsic_rank"] if p not in prop else prop[p] for p in nodes[v]["parents"]]
        prop[v] = max([nodes[v]["intrinsic_rank"]] + p_ranks)

    monotone_ok = all(prop[p] <= prop[v] for v, info in nodes.items() for p in info["parents"])
    assert monotone_ok
    return {
        "is_acyclic": True,
        "cyclic_sccs": [],
        "self_loops": [],
        "seam_honesty_violations": seam_honesty_violations,
        "prop_ranks": prop,
    }


def run_section_3():
    """Verify 58-node Epistemic DAG v2 invariants."""
    nodes = build_58_node_dag()
    res = analyze_dag(nodes)
    assert res["is_acyclic"] and len(res["seam_honesty_violations"]) == 0
    prop = res["prop_ranks"]

    cats = ["ROOT", "OPERATOR", "SEAM", "RELATION", "SM_TARGET"]
    cat_counts = [sum(1 for info in nodes.values() if info["category"] == c) for c in cats]
    assert cat_counts == [9, 9, 8, 13, 19], f"Bad category counts: {cat_counts}"
    assert len(nodes) == 58

    assert prop["S:EWSB_Scale_Anchor_vEW"] == 3 and prop["SM18:v_EW"] == 3
    rel_hist = [
        sum(1 for n, info in nodes.items() if info["category"] == "RELATION" and prop[n] == r)
        for r in range(4)
    ]
    sm_hist = [
        sum(1 for n, info in nodes.items() if info["category"] == "SM_TARGET" and prop[n] == r)
        for r in range(4)
    ]
    assert rel_hist == [2, 8, 3, 0], f"rel_hist={rel_hist}"
    assert sm_hist == [0, 0, 1, 18], f"sm_hist={sm_hist}"
    rank2_sm = [n for n, info in nodes.items() if info["category"] == "SM_TARGET" and prop[n] == 2]
    assert rank2_sm == ["SM19:bar_theta_QCD"], f"rank2_sm={rank2_sm}"

    return {
        "node_count": len(nodes),
        "category_counts": cat_counts,
        "acyclic": True,
        "guardrail_1_seam_honest": True,
        "guardrail_5_vEW_rank": prop["SM18:v_EW"],
        "relation_rank_histogram_0_1_2_3": rel_hist,
        "sm_target_rank_histogram_0_1_2_3": sm_hist,
        "unique_rank2_sm_target": rank2_sm[0],
    }


# ---------------------------------------------------------------------------
# Section 4: Five Planted Fault Controls PFU4-1..PFU4-5
# ---------------------------------------------------------------------------

def run_section_4(sec1_res, sec2_res):
    """Verify all 5 Planted Fault Controls PFU4-1..PFU4-5 fail as specified."""
    mp.mp.dps = 50
    _, _, res0 = sec1_res["tau0_state"]
    st_1S = res0[(1, "S")]
    G3L, G2L, G3R, G2R = st_1S["G"]
    Sph = st_1S["Sph"]
    Ybase = st_1S["Ybase"]

    # PFU4-1: Linear Casimir scalar trace collapse
    T3L = mp.re(G3L[0, 0] + G3L[1, 1] + G3L[2, 2]) / 3
    T2L = mp.re(G2L[0, 0] + G2L[1, 1] + G2L[2, 2]) / 3
    T3R = mp.re(G3R[0, 0] + G3R[1, 1] + G3R[2, 2]) / 3
    T2R = mp.re(G2R[0, 0] + G2R[1, 1] + G2R[2, 2]) / 3
    I3 = mp.eye(3)
    K_QL_lin = (T3L + T2L) * I3
    K_LL_lin = (3 * T3L + T2L) * I3
    K_dR_lin = (2 * T3R + 2 * T2R) * I3
    K_eR_lin = 2 * T2R * I3

    inv_QL_lin = jacobi_hermitian_inv_sqrt(K_QL_lin)
    inv_LL_lin = jacobi_hermitian_inv_sqrt(K_LL_lin)
    inv_dR_lin = jacobi_hermitian_inv_sqrt(K_dR_lin)
    inv_eR_lin = jacobi_hermitian_inv_sqrt(K_eR_lin)

    max_sv_split_lin = mp.mpf(0)
    for Yhol in (Ybase, Sph):
        Yd_lin = inv_QL_lin * Yhol * inv_dR_lin
        Ye_lin = inv_LL_lin * Yhol * inv_eR_lin
        _, svd, _ = mp.svd_c(Yd_lin)
        _, sve, _ = mp.svd_c(Ye_lin)
        rd = [s / svd[0] for s in svd]
        re_ = [s / sve[0] for s in sve]
        split = max(abs(re_[i] - rd[i]) for i in range(3))
        if split > max_sv_split_lin:
            max_sv_split_lin = split
    assert max_sv_split_lin < mp.mpf(1) / (10 ** 35)

    # Equalized scalar trace determinant check
    Ye_eq = I3 * Sph * I3
    Yd_eq = I3 * Sph * I3
    ln_Red_eq = abs(mp.log(abs(det_gepp(Ye_eq) / det_gepp(Yd_eq))))
    assert ln_Red_eq < mp.mpf(1) / (10 ** 35)

    # PFU4-2: Swapped u_R^c <-> d_R^c flips <ln R_ud> < -1/2 < 0 on all 3 W-P1c clocks
    swapped_clocks = sec2_res["swapped_m1_clocks"]
    assert all(v < -mp.mpf(1) / 2 and v < 0 for v in swapped_clocks)

    # PFU4-3: Guardrail 1 0-bit seam smuggling
    nodes_f3 = build_58_node_dag()
    nodes_f3["S:Torsion_Tau_SU2R_Break"]["intrinsic_rank"] = 0
    nodes_f3["S:Torsion_Tau_SU2R_Break"]["stabilized"] = False
    res_f3 = analyze_dag(nodes_f3)
    assert "S:Torsion_Tau_SU2R_Break" in res_f3["seam_honesty_violations"]

    # PFU4-4: Circular feedback edge & missing v_EW anchor
    nodes_f4a = build_58_node_dag()
    nodes_f4a["G:m004_Mostow_Rigidity"]["parents"].append("SM18:v_EW")
    res_f4a = analyze_dag(nodes_f4a)
    assert not res_f4a["is_acyclic"] and len(res_f4a["cyclic_sccs"]) >= 1

    nodes_f4b = build_58_node_dag()
    nodes_f4b["SM18:v_EW"]["parents"] = [
        p for p in nodes_f4b["SM18:v_EW"]["parents"] if p != "S:EWSB_Scale_Anchor_vEW"
    ]
    res_f4b = analyze_dag(nodes_f4b)
    assert res_f4b["is_acyclic"] and res_f4b["prop_ranks"]["SM18:v_EW"] < 3

    # PFU4-5: Guardrail 3 Haar SU(3)^5 vs raw |det(Re Y_u) / det(Re Y_d)|
    K_QL, K_LL, K_uR, K_dR, K_eR = st_1S["K"]
    Yu_0, Yd_0, Ye_0 = st_1S["phys_mats"]["phased_sum"]
    ref_ud = abs(det_gepp(Yu_0) / det_gepp(Yd_0))
    ref_ed = abs(det_gepp(Ye_0) / det_gepp(Yd_0))
    ref_re_ud = abs(det_gepp(Yu_0.apply(mp.re)) / det_gepp(Yd_0.apply(mp.re)))
    rng = random.Random(4045)
    max_phys_drift = mp.mpf(0)
    max_re_shift = mp.mpf(0)
    for _ in range(10):
        U_QL = haar_su3(rng)
        U_LL = haar_su3(rng)
        U_uR = haar_su3(rng)
        U_dR = haar_su3(rng)
        U_eR = haar_su3(rng)
        inv_QL = jacobi_hermitian_inv_sqrt(U_QL * K_QL * U_QL.H)
        inv_LL = jacobi_hermitian_inv_sqrt(U_LL * K_LL * U_LL.H)
        inv_uR = jacobi_hermitian_inv_sqrt(U_uR * K_uR * U_uR.H)
        inv_dR = jacobi_hermitian_inv_sqrt(U_dR * K_dR * U_dR.H)
        inv_eR = jacobi_hermitian_inv_sqrt(U_eR * K_eR * U_eR.H)
        Yu_p = inv_QL * (U_QL * Sph * U_uR.H) * inv_uR
        Yd_p = inv_QL * (U_QL * Sph * U_dR.H) * inv_dR
        Ye_p = inv_LL * (U_LL * Sph * U_eR.H) * inv_eR
        ud_p = abs(det_gepp(Yu_p) / det_gepp(Yd_p))
        ed_p = abs(det_gepp(Ye_p) / det_gepp(Yd_p))
        re_ud_p = abs(det_gepp(Yu_p.apply(mp.re)) / det_gepp(Yd_p.apply(mp.re)))
        max_phys_drift = max(max_phys_drift, abs(ud_p - ref_ud), abs(ed_p - ref_ed))
        max_re_shift = max(max_re_shift, abs(re_ud_p - ref_re_ud))
    assert max_phys_drift < mp.mpf(1) / (10 ** 30)
    assert max_re_shift > mp.mpf(1) / 5

    return {
        "PFU4-1": {
            "max_sv_split_lin": mp.nstr(max_sv_split_lin, 6),
            "ln_Red_equal": mp.nstr(ln_Red_eq, 6),
            "caught": True,
        },
        "PFU4-2": {
            "swapped_clocks_ln_Rud": [mp.nstr(v, 10) for v in swapped_clocks],
            "caught": True,
        },
        "PFU4-3": {
            "seam_honesty_violations": res_f3["seam_honesty_violations"],
            "caught": True,
        },
        "PFU4-4": {
            "cycle_detected": not res_f4a["is_acyclic"],
            "detached_vEW_rank": res_f4b["prop_ranks"]["SM18:v_EW"],
            "caught": True,
        },
        "PFU4-5": {
            "phys_haar_drift": mp.nstr(max_phys_drift, 6),
            "raw_Re_shift": mp.nstr(max_re_shift, 8),
            "caught": True,
        },
    }


def main():
    t_start = time.time()
    script_path = Path(__file__).resolve()
    out_dir = script_path.parent
    repo_root = script_path.parents[2]
    out_json_path = out_dir / "referee_found_v2_u4_out.json"
    self_output_sha_path = out_dir / "OUTPUT_SHA256.txt"

    # Section 0: AST, 20/20 Manifests, Unreduced RK4 L_2 T & S
    ast_res = audit_ast_and_imports(script_path)
    manifest_res = verify_sha256_manifests(repo_root, self_output_sha_path)

    mp.mp.dps = 50
    tau0 = mp.mpc(mp.mpf(13) / 100, mp.mpf(17) / 10)
    L2_0_unred, rn0, det0 = solve_L2_rk4_direct(tau0, target_dps=50, high_acc=True)
    L2_T_unred, rnT, detT = solve_L2_rk4_direct(tau0 + 1, target_dps=50, high_acc=True)
    L2_S_unred, rnS, detS = solve_L2_rk4_direct(-1 / tau0, target_dps=50, high_acc=True)
    T_cov_err = abs(L2_T_unred - L2_0_unred)
    S_cov_err = abs(L2_S_unred - (L2_0_unred + mp.log(abs(tau0))))
    tol_unred = mp.mpf(1) / (10 ** 11)
    assert T_cov_err < tol_unred, f"Unreduced T_cov_err={T_cov_err}"
    assert S_cov_err < tol_unred, f"Unreduced S_cov_err={S_cov_err}"
    assert max(rn0, rnT, rnS, det0, detT, detS) < tol_unred

    sec0_res = {
        "ast": ast_res,
        "manifests": manifest_res,
        "unreduced_rk4_L2": {
            "L2_tau0": mp.nstr(L2_0_unred, 20),
            "T_cov_err": mp.nstr(T_cov_err, 6),
            "S_cov_err": mp.nstr(S_cov_err, 6),
            "max_monodromy_res": mp.nstr(max(rn0, rnT, rnS), 6),
        },
    }

    # Build Gauss-reduced FD cache seeded with tau0
    fd_cache = {}
    fd_cache[(mp.nstr(mp.re(tau0), 45), mp.nstr(mp.im(tau0), 45), 50, True)] = L2_0_unred

    E, C_S, C_tS = build_yukawa_helpers()
    weil_data = {1: build_weil(1), 3: build_weil(3)}

    sec1_full = run_section_1(fd_cache, E, C_S, C_tS, weil_data)
    sec2_res = run_section_2(fd_cache)
    sec3_res = run_section_3()
    sec4_res = run_section_4(sec1_full, sec2_res)

    # Strip large in-memory matrix objects from sec1_full and swapped list before JSON dump
    sec1_json = {k: v for k, v in sec1_full.items() if k != "tau0_state"}
    sec2_json = {k: v for k, v in sec2_res.items() if k != "swapped_m1_clocks"}

    elapsed = time.time() - t_start
    payload = {
        "gate": "AGY-002_FOUND-V2-U4_REFEREE",
        "runtime_seconds": round(elapsed, 3),
        "section_0": sec0_res,
        "section_1": sec1_json,
        "section_2": sec2_json,
        "section_3": sec3_res,
        "section_4": sec4_res,
        "all_passed": True,
    }
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        f"REFEREE_PASS manifests={manifest_res['manifest_count']}/{manifest_res['manifest_count']} "
        f"ast_float_literals={ast_res['float_complex_literal_count']} "
        f"runtime={elapsed:.2f}s"
    )


if __name__ == "__main__":
    main()
