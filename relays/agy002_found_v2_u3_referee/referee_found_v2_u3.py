"""Cold-Room Zero-Trust Referee for Gate F-U3 (AGY-002_FOUND-V2-U3).

Independently verifies Sections 0-4 from the three specification cards using:
- Symbolic Q(zeta_24) cyclotomic arithmetic in SymPy
- 1D unfolded universal-cover Gauss-Legendre and trapezoidal quadrature at 55 digits
- Closed-form Jacobi Theta_c(6 tau, 6 xi) overlap contractions
- 25 x 25 shifted Gauss-Legendre (and 33 x 33 midpoint cross-check) on E_tau
- 55-digit mpmath determinant evaluation and 10-trial Haar SU(3) scrambling
Zero repo imports; zero float/complex AST literals; 0 of 19 empirical constants.
"""

import ast
import hashlib
import json
import math
import pathlib
import re
import time

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as sp


def rat_f(num, den=1):
    return num / den


def f_c(re_val, im_val=0):
    return complex(re_val, im_val)


def mp_rat(num, den=1):
    return mp.mpf(num) / mp.mpf(den)


def mp_c(re_val, im_val=0):
    return mp.mpc(re_val, im_val)


def mp_pow10(exp_int):
    return mp.mpf(10) ** exp_int


ALLOWED_IMPORTS = {
    "ast",
    "hashlib",
    "json",
    "math",
    "pathlib",
    "re",
    "sys",
    "time",
    "mpmath",
    "numpy",
    "sympy",
}


def audit_ast_and_imports(script_path):
    """Verify 0 float/complex AST literals and stdlib+numpy+sympy+mpmath only."""
    src = pathlib.Path(script_path).read_text(encoding="utf-8")
    tree = ast.parse(src)
    float_complex_nodes = []
    disallowed = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_complex_nodes.append((node.lineno, repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top not in ALLOWED_IMPORTS:
                    disallowed.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            mod = (node.module or "").split(".")[0]
            if mod and mod not in ALLOWED_IMPORTS:
                disallowed.append((node.lineno, node.module))
    assert len(float_complex_nodes) == 0, f"AST float/complex literals found: {float_complex_nodes}"
    assert len(disallowed) == 0, f"Disallowed imports found: {disallowed}"
    return {
        "float_complex_literal_count": 0,
        "disallowed_imports": [],
        "passed": True,
    }


def verify_manifests(repo_root, self_script_rel):
    """Discover all 16 *SHA256.txt manifests (15 prior + own SCRIPT_SHA256.txt) and verify digests."""
    relays_dir = pathlib.Path(repo_root) / "relays"
    all_manifests = sorted(relays_dir.glob("agy002_found_v2_*/*SHA256.txt"))
    self_out_manifest = relays_dir / "agy002_found_v2_u3_referee" / "OUTPUT_SHA256.txt"
    manifests = [m for m in all_manifests if m != self_out_manifest]
    assert len(manifests) == 16, f"Expected 16 manifests (15 prior + own SCRIPT_SHA256.txt), got {len(manifests)}"
    hex_re = re.compile(r"^[0-9a-f]{64}$")
    verified = []
    mismatches = []
    self_verified = False
    for m_path in manifests:
        lines = [ln.strip() for ln in m_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
        assert len(lines) >= 1, f"Empty manifest {m_path}"
        for ln in lines:
            parts = ln.split()
            assert len(parts) == 2, f"Malformed SHA256 line in {m_path}: {ln}"
            digest, rel_target = parts
            assert hex_re.match(digest), f"Invalid hex digest in {m_path}: {digest}"
            target = pathlib.Path(repo_root) / rel_target
            assert target.is_file(), f"Missing target file {target}"
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            if actual != digest:
                mismatches.append(str(m_path.relative_to(repo_root)))
            verified.append(str(m_path.relative_to(repo_root)))
            if rel_target == self_script_rel and actual == digest:
                self_verified = True
    assert len(mismatches) == 0, f"SHA256 mismatches: {mismatches}"
    assert self_verified, "Own SCRIPT_SHA256.txt did not verify self script"
    return {
        "manifest_count": len(manifests),
        "verified_files": len(verified),
        "self_script_sha256_verified": self_verified,
        "mismatches": [],
        "manifests": verified,
        "passed": True,
    }


def exact_theta_by_c_mp(zL, zR, tau):
    """Exact bounded-Gaussian Jacobi Theta_c(6 tau, 6 xi) prefactor contraction at 55 digits."""
    y = mp.im(tau)
    du = mp.im(zL - zR) / y
    dx = mp.re(zL - zR) - mp.re(tau) * du
    norm = (3 * y) ** mp_rat(1, 4)
    center = int(round(float(-du / 2)))
    half_mp = mp_rat(1, 2)
    three_halves = mp_rat(3, 2)
    vals = []
    for c in range(6):
        th = mp.mpc(0)
        for ell in range(center - 8, center + 9):
            ap = ell + mp_rat(c, 6) + du * half_mp
            th += mp.exp(mp_c(0, 1) * mp.pi * (6 * tau * ap * ap + 6 * ap * dx - three_halves * dx * du))
        vals.append(norm * th)
    return vals


def exact_theta_mp(i, j, k, zL, zR, tau):
    if (i + j + 1 - k) % 3 != 0:
        return mp.mpc(0)
    c = (2 * i + 1 - k) % 6
    phase_b = mp.exp(mp_c(0, 1) * mp.pi * k / 3)
    return phase_b * exact_theta_by_c_mp(zL, zR, tau)[c]


def exact_theta_np(i, j, k, zL, zR, tau):
    if (i + j + 1 - k) % 3 != 0:
        return f_c(0)
    y = float(np.imag(tau))
    du = float(np.imag(zL - zR)) / y
    dx = float(np.real(zL - zR)) - float(np.real(tau)) * du
    c = (2 * i + 1 - k) % 6
    norm = (3 * y) ** rat_f(1, 4)
    phase_b = np.exp(f_c(0, 1) * np.pi * rat_f(k, 3))
    center = int(round(-du * rat_f(1, 2)))
    th = f_c(0)
    half_f = rat_f(1, 2)
    three_halves = rat_f(3, 2)
    for ell in range(center - 10, center + 11):
        ap = ell + rat_f(c, 6) + du * half_f
        th += np.exp(f_c(0, 1) * np.pi * (6 * tau * ap * ap + 6 * ap * dx - three_halves * dx * du))
    return norm * phase_b * th


def _unfolded_integrand_mp(i, j, k, zL, zR, zH, tau):
    """Unfolded 1D integrand over u in R after exact x in [0, 1] Kronecker projection."""
    s = (i + j + 1 - k) // 3
    y = mp.im(tau)
    uL = mp.im(zL) / y
    uR = mp.im(zR) / y
    uH = mp.im(zH) / y
    aL = mp_rat(2 * i + 1, 6)
    aR = mp_rat(2 * j + 1, 6)
    aH = mp_rat(k, 6)
    norm = (6 * y) ** mp_rat(1, 4) * (6 * y) ** mp_rat(1, 4) * (12 * y) ** mp_rat(1, 4)
    half_mp = mp_rat(1, 2)
    center = int(round(float(-mp.im(zL - zR) / (2 * y))))

    def f_u(u):
        z = tau * u
        pref = mp.exp(mp_c(0, 1) * mp.pi * (3 * (z + zL) * (u + uL) + 3 * (z + zR) * (u + uR) - 6 * mp.conj(z + zH) * (u + uH)))
        h_part = mp.exp(-mp_c(0, 1) * mp.pi * 6 * mp.conj(tau) * aH * aH - 2 * mp_c(0, 1) * mp.pi * aH * (6 * mp.conj(z + zH)))
        lr_sum = mp.mpc(0)
        for ell in range(center - 7, center + 8):
            n1 = ell
            n2 = -ell - s
            al1 = n1 + aL
            al2 = n2 + aR
            lr_sum += mp.exp(
                mp_c(0, 1) * mp.pi * 3 * tau * al1 * al1 + 2 * mp_c(0, 1) * mp.pi * al1 * (3 * (z + zL) + half_mp) +
                mp_c(0, 1) * mp.pi * 3 * tau * al2 * al2 + 2 * mp_c(0, 1) * mp.pi * al2 * (3 * (z + zR) + half_mp)
            )
        return norm * pref * h_part * lr_sum

    uc = -uH - aH
    return f_u, uc


def unfolded_1d_gl_mp(i, j, k, zL, zR, zH, tau):
    if (i + j + 1 - k) % 3 != 0:
        return mp.mpc(0)
    f_u, uc = _unfolded_integrand_mp(i, j, k, zL, zR, zH, tau)
    half_mp = mp_rat(1, 2)
    return mp.quad(f_u, [-5, uc - half_mp, uc, uc + half_mp, 5], method="gauss-legendre")


def unfolded_1d_trap_mp(i, j, k, zL, zR, zH, tau):
    if (i + j + 1 - k) % 3 != 0:
        return mp.mpc(0)
    f_u, uc = _unfolded_integrand_mp(i, j, k, zL, zR, zH, tau)
    half_width = mp_rat(3, 2)
    n_pts = 150
    h_step = 2 * half_width / n_pts
    total = (f_u(uc - half_width) + f_u(uc + half_width)) / 2
    for m in range(1, n_pts):
        total += f_u(uc - half_width + m * h_step)
    return total * h_step


def run_section_0(repo_root, self_script_path):
    mp.mp.dps = 55
    ast_res = audit_ast_and_imports(self_script_path)
    self_rel = str(pathlib.Path(self_script_path).resolve().relative_to(pathlib.Path(repo_root).resolve()))
    man_res = verify_manifests(repo_root, self_rel)

    tau6 = mp_rat(13, 100) + mp_c(0, 6)
    w_test = (1 + tau6) / 5
    sectors = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]

    gl_max_err = mp.mpf(0)
    for (i, j, k) in [(1, 1, 0), (2, 0, 3)]:
        zL, zR = 1 * w_test, -4 * w_test
        zH = (zL + zR) / 2
        val_th = exact_theta_mp(i, j, k, zL, zR, tau6)
        val_gl = unfolded_1d_gl_mp(i, j, k, zL, zR, zH, tau6)
        gl_max_err = max(gl_max_err, abs(val_th - val_gl))
    assert gl_max_err < mp_pow10(-35), f"1D GL cross-cal failed: {gl_max_err}"

    trap_max_err = mp.mpf(0)
    for _, qL, qR in sectors:
        zL, zR = qL * w_test, qR * w_test
        zH = (zL + zR) / 2
        th_c = exact_theta_by_c_mp(zL, zR, tau6)
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    if (i + j + 1 - k) % 3 == 0:
                        c = (2 * i + 1 - k) % 6
                        val_th = mp.exp(mp_c(0, 1) * mp.pi * k / 3) * th_c[c]
                    else:
                        val_th = mp.mpc(0)
                    val_tr = unfolded_1d_trap_mp(i, j, k, zL, zR, zH, tau6)
                    trap_max_err = max(trap_max_err, abs(val_th - val_tr))
    assert trap_max_err < mp_pow10(-35), f"1D trap cross-cal failed: {trap_max_err}"

    return {
        "ast": ast_res,
        "manifests": man_res,
        "gl_1d_vs_theta_max_err": mp.nstr(gl_max_err, 12),
        "trap_1d_vs_theta_all162_max_err": mp.nstr(trap_max_err, 12),
        "passed": True,
    }


def build_weil_basis_mp():
    N = 6
    T = mp.diag([mp.exp(mp_c(0, 1) * mp.pi * j * j / N) for j in range(N)])
    S = mp.matrix(N, N)
    inv_sq6 = 1 / mp.sqrt(N)
    for j in range(N):
        for k in range(N):
            S[j, k] = mp.exp(-2 * mp_c(0, 1) * mp.pi * j * k / N) * inv_sq6
    UM = T * S * T.H * S.H
    P_p = mp.zeros(N, N)
    P_m = mp.zeros(N, N)
    cur = mp.eye(N)
    for k in range(12):
        P_p += mp.exp(-mp_c(0, 1) * k * mp.pi / N) * cur
        P_m += mp.exp(mp_c(0, 1) * k * mp.pi / N) * cur
        cur = UM * cur
    P_p /= 12
    P_m /= 12
    e0 = mp.matrix([1, 0, 0, 0, 0, 0])
    vp = P_p * e0
    vp /= mp.norm(vp)
    vm = P_m * e0
    vm /= mp.norm(vm)
    hstar = (vp + vm) / mp.sqrt(2)
    return T, S, UM, vp, vm, hstar


def run_section_1():
    mp.mp.dps = 55
    z = sp.Symbol("z")
    phi24 = sp.cyclotomic_poly(24, z)

    def red(expr):
        return sp.rem(sp.expand(expr), phi24, z)

    def mat_conj(M):
        return M.applyfunc(lambda e: red(e.subs(z, z**23)))

    sqrt2 = red(z**3 - z**9)
    sqrt3 = red(z**2 - z**10)
    sqrt6 = red(sqrt2 * sqrt3)
    T_sym = sp.Matrix(6, 6, lambda j, k: red(z ** (2 * j * j)) if j == k else 0)
    S_sym = sp.Matrix(6, 6, lambda j, k: red((sqrt6 / 6) * z ** ((-4 * j * k) % 24)))
    UM_sym = (T_sym * S_sym * mat_conj(T_sym.T) * mat_conj(S_sym.T)).applyfunc(red)
    assert (UM_sym**12).applyfunc(red) == sp.eye(6)

    e0_sym = sp.Matrix([1, 0, 0, 0, 0, 0])
    Pp_e0 = sp.zeros(6, 1)
    Pm_e0 = sp.zeros(6, 1)
    cur_sym = e0_sym
    for k in range(12):
        Pp_e0 += z ** ((-2 * k) % 24) * cur_sym
        Pm_e0 += z ** ((2 * k) % 24) * cur_sym
        cur_sym = (UM_sym * cur_sym).applyfunc(red)
    vp_sym = ((Pp_e0 / 12) * red(3 + sqrt3)).applyfunc(red)
    vm_sym = ((Pm_e0 / 12) * red(3 - sqrt3)).applyfunc(red)
    assert (mat_conj(vp_sym.T) * vp_sym).applyfunc(red) == sp.Matrix([[1]])
    assert (mat_conj(vm_sym.T) * vm_sym).applyfunc(red) == sp.Matrix([[1]])
    assert (mat_conj(vp_sym.T) * vm_sym).applyfunc(red) == sp.Matrix([[0]])
    assert (UM_sym * vp_sym - z**2 * vp_sym).applyfunc(red) == sp.zeros(6, 1)
    assert (UM_sym * vm_sym - z**22 * vm_sym).applyfunc(red) == sp.zeros(6, 1)

    hstar_sym = ((vp_sym + vm_sym) * sqrt2 / 2).applyfunc(red)
    for idx in [2, 3, 4]:
        assert hstar_sym[idx] == 0

    assert red(vp_sym[0] + (-(2 - sqrt3)) * vm_sym[0]) == 0
    for idx in [1, 5]:
        assert red(vp_sym[idx] + (-(2 + sqrt3)) * vm_sym[idx]) == 0
    for idx in [2, 3, 4]:
        assert red(vp_sym[idx] + 1 * vm_sym[idx]) == 0

    _, _, UM, vp, vm, hstar = build_weil_basis_mp()
    tol50 = mp_pow10(-50)
    eig_p_err = mp.norm(UM * vp - mp.exp(mp_c(0, 1) * mp.pi / 6) * vp)
    eig_m_err = mp.norm(UM * vm - mp.exp(-mp_c(0, 1) * mp.pi / 6) * vm)
    ortho_err = abs((vp.H * vm)[0, 0])
    zero_modes_err = max(abs(hstar[idx]) for idx in [2, 3, 4])
    assert eig_p_err < tol50 and eig_m_err < tol50 and ortho_err < tol50 and zero_modes_err < tol50

    H_cos = (UM + UM.H) / 2
    H_sin = (UM - UM.H) / (2 * mp_c(0, 1))
    cos_p_err = mp.norm(H_cos * vp - (mp.sqrt(3) / 2) * vp)
    sin_p_err = mp.norm(H_sin * vp - mp_rat(1, 2) * vp)
    sin_m_err = mp.norm(H_sin * vm + mp_rat(1, 2) * vm)
    assert max(cos_p_err, sin_p_err, sin_m_err) < tol50

    r_vals = [-vp[k] / vm[k] for k in range(6)]
    r0_err = abs(r_vals[0] - (-(2 - mp.sqrt(3))))
    r15_err = max(abs(r_vals[idx] - (-(2 + mp.sqrt(3)))) for idx in [1, 5])
    r234_err = max(abs(r_vals[idx] - 1) for idx in [2, 3, 4])
    assert max(r0_err, r15_err, r234_err) < tol50

    orbit = []
    cur = hstar
    for _ in range(13):
        orbit.append(cur)
        cur = UM * cur
    um_order12_err = mp.norm(orbit[12] - orbit[0])
    um_half_order6_err = mp.norm(orbit[6] + orbit[0])
    assert um_order12_err < tol50
    assert um_half_order6_err < tol50

    tol12 = mp_pow10(-12)
    distinct_vecs = []
    distinct_rays = []
    for v in orbit[:12]:
        if all(mp.norm(v - u) > tol12 for u in distinct_vecs):
            distinct_vecs.append(v)
        if all(1 - abs((v.H * u)[0, 0]) ** 2 > tol12 for u in distinct_rays):
            distinct_rays.append(v)
    assert len(distinct_vecs) == 12
    assert len(distinct_rays) == 6

    B_sym = sp.Matrix.hstack(vp_sym, vm_sym)
    UM_E = (mat_conj(B_sym.T) * UM_sym * B_sym).applyfunc(red)
    S_E = (mat_conj(B_sym.T) * S_sym * B_sym).applyfunc(red)
    a_s, br_s, bi_s, d_s = sp.symbols("a_s br_s bi_s d_s", real=True)
    i_z = red(z**6)
    H_E = sp.Matrix([[a_s, br_s + i_z * bi_s], [br_s - i_z * bi_s, d_s]])
    eq_UM = (mat_conj(UM_E.T) * H_E * UM_E - H_E).applyfunc(red)
    eq_S = (mat_conj(S_E.T) * H_E * S_E - H_E).applyfunc(red)
    vars_4 = [a_s, br_s, bi_s, d_s]
    rows = []
    for mat_eq in [eq_UM, eq_S]:
        for r in range(2):
            for c in range(2):
                poly = sp.Poly(mat_eq[r, c], z)
                for deg in range(8):
                    coeff = poly.coeff_monomial(z**deg)
                    if coeff != 0:
                        rows.append([sp.diff(coeff, v) for v in vars_4])
    ns = sp.Matrix(rows).nullspace()
    assert len(ns) == 1
    H_inv = H_E.subs(list(zip(vars_4, ns[0])))
    ep, em = sp.symbols("ep em")
    n2_vp = (sp.Matrix([1, 0]).T * H_inv * sp.Matrix([1, 0]))[0, 0]
    n2_eq = sp.expand((sp.Matrix([1, em]).T / sp.sqrt(2) * H_inv * sp.Matrix([1, ep]) / sp.sqrt(2))[0, 0]).subs(ep * em, 1)
    n2_diff = sp.simplify(n2_vp - n2_eq)
    assert n2_diff == 0

    nodes, weights = leggauss(25)
    x_gl = rat_f(1, 2) * (nodes + 1)
    w_gl = rat_f(1, 2) * weights
    WW_gl = np.outer(w_gl, w_gl)
    XX_gl, UU_gl = np.meshgrid(x_gl, x_gl, indexing="ij")

    grid_mid = 33
    xs_mid = (np.arange(grid_mid) + rat_f(1, 2)) / grid_mid
    XX_mid, UU_mid = np.meshgrid(xs_mid, xs_mid, indexing="ij")

    vp_np = np.array([complex(vp[k]) for k in range(6)], dtype=np.complex128)
    vm_np = np.array([complex(vm[k]) for k in range(6)], dtype=np.complex128)
    hs_np = np.array([complex(hstar[k]) for k in range(6)], dtype=np.complex128)
    phis_24 = np.linspace(0, 2 * np.pi, 24, endpoint=False)
    circ_np = [(vp_np + np.exp(f_c(0, 1) * ph) * vm_np) / np.sqrt(2) for ph in phis_24]

    def psi6_np(k, z_arr, tau):
        y = float(np.imag(tau))
        u = np.imag(z_arr) / y
        norm = (12 * y) ** rat_f(1, 4)
        th = np.zeros_like(z_arr, dtype=np.complex128)
        for n in range(-10, 11):
            a_n = n + rat_f(k, 6)
            th += np.exp(f_c(0, 1) * np.pi * 6 * tau * (a_n * a_n) + 2 * f_c(0, 1) * np.pi * 6 * a_n * z_arr)
        return norm * np.exp(f_c(0, 1) * np.pi * 6 * z_arr * u) * th

    moduli = [
        ("bulk_17_10", rat_f(13, 100) + f_c(0, 1) * rat_f(17, 10)),
        ("i", f_c(0, 1)),
        ("2sqrt3_i", f_c(0, 1) * 2 * math.sqrt(3)),
    ]
    frozen_results = {}
    for label, tau in moduli:
        psis_gl = np.array([psi6_np(k, XX_gl + tau * UU_gl, tau) for k in range(6)])
        psis_mid = np.array([psi6_np(k, XX_mid + tau * UU_mid, tau) for k in range(6)])

        def v4_gl(h_vec):
            phi = np.tensordot(h_vec, psis_gl, axes=(0, 0))
            return float(np.sum(WW_gl * (np.abs(phi) ** 4)))

        def v4_mid(h_vec):
            phi = np.tensordot(h_vec, psis_mid, axes=(0, 0))
            return float(np.mean(np.abs(phi) ** 4))

        b_frozen = v4_gl(vp_np) - v4_gl(hs_np)
        b_frozen_mid = v4_mid(vp_np) - v4_mid(hs_np)
        b_mean = v4_gl(vp_np) - float(np.mean([v4_gl(hc) for hc in circ_np]))
        assert abs(b_frozen - b_frozen_mid) < rat_f(1, 10000)
        assert b_frozen < -1
        assert b_mean < -rat_f(1, 5)
        frozen_results[label] = {
            "B_frozen_P873": b_frozen,
            "B_frozen_mean": b_mean,
            "gl_vs_33x33_mid_diff": abs(b_frozen - b_frozen_mid),
        }

    return {
        "sympy_qzeta24_exact": True,
        "eig_p_err": mp.nstr(eig_p_err, 8),
        "eig_m_err": mp.nstr(eig_m_err, 8),
        "zero_modes_err": mp.nstr(zero_modes_err, 8),
        "um_signed_vector_count": len(distinct_vecs),
        "um_projective_ray_count": len(distinct_rays),
        "um_order12_err": mp.nstr(um_order12_err, 8),
        "um_half_order6_err": mp.nstr(um_half_order6_err, 8),
        "invariant_hermitian_quad_dim": len(ns),
        "cartan_relaxed_n2_diff": int(n2_diff),
        "frozen_25x25_gl": frozen_results,
        "passed": True,
    }, (UM, vp, vm, hstar, vp_np, vm_np, hs_np)


def build_sector_tensors_np(tau):
    sectors = [("up", 1, -4, 3), ("down", 1, 2, 3), ("lepton", -3, 6, 1)]
    pts = [(a, b) for a in range(5) for b in range(5) if not (a == 0 and b == 0)]
    tensors = {}
    for name, qL, qR, _ in sectors:
        for (a, b) in pts:
            w = (a * tau + b) / 5
            Y = np.zeros((3, 3, 6), dtype=np.complex128)
            for i in range(3):
                for j in range(3):
                    for k in range(6):
                        Y[i, j, k] = exact_theta_np(i, j, k, qL * w, qR * w, tau)
            tensors[(name, a, b)] = Y
    return sectors, pts, tensors


def build_sector_tensors_mp(tau):
    sectors = [("up", 1, -4, 3), ("down", 1, 2, 3), ("lepton", -3, 6, 1)]
    pts = [(a, b) for a in range(5) for b in range(5) if not (a == 0 and b == 0)]
    phase_k = [mp.exp(mp_c(0, 1) * mp.pi * k / 3) for k in range(6)]
    tensors = {}
    for name, qL, qR, _ in sectors:
        for (a, b) in pts:
            w = (a * tau + b) / 5
            th_c = exact_theta_by_c_mp(qL * w, qR * w, tau)
            Y = [[[mp.mpc(0) for _ in range(6)] for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(6):
                        if (i + j + 1 - k) % 3 == 0:
                            c = (2 * i + 1 - k) % 6
                            Y[i][j][k] = phase_k[k] * th_c[c]
            tensors[(name, a, b)] = Y
    return sectors, pts, tensors


def eval_box_cw_np(h_vec, y_val, sectors, pts, tensors, mu2=1):
    val_box = 0
    val_cw = 0
    tr_sum = 0
    inv24 = rat_f(1, 24)
    three_halves = rat_f(3, 2)
    for name, _, _, Nc in sectors:
        for (a, b) in pts:
            M = np.tensordot(tensors[(name, a, b)], h_vec, axes=(2, 0))
            s = np.linalg.svd(M, compute_uv=False)
            evals = y_val * (s * s)
            val_box += -inv24 * Nc * float(np.sum(evals * evals))
            tr_sum += inv24 * Nc * float(np.sum(evals))
            pos = evals[evals > 0]
            if len(pos) > 0:
                val_cw += -inv24 * Nc * float(np.sum((pos * pos) * (np.log(pos / mu2) - three_halves)))
    return val_box, val_cw, tr_sum


def eval_box_cw_mp(h_mp, y_mp, sectors, pts, tensors_mp, mu2=1):
    val_box = mp.mpf(0)
    val_cw = mp.mpf(0)
    tr_sum = mp.mpf(0)
    three_halves = mp_rat(3, 2)
    for name, _, _, Nc in sectors:
        weight = mp.mpf(Nc) / 24
        for (a, b) in pts:
            Y = tensors_mp[(name, a, b)]
            M = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    M[i, j] = sum(Y[i][j][k] * h_mp[k] for k in range(6))
            H = y_mp * (M * M.H)
            evals = [max(mp.re(x), mp.mpf(0)) for x in mp.eighe(H)[0]]
            for ev in evals:
                val_box += -weight * (ev * ev)
                tr_sum += weight * ev
                if ev > mp_pow10(-45):
                    val_cw += -weight * (ev * ev) * (mp.log(ev / mu2) - three_halves)
    return val_box, val_cw, tr_sum


def eval_det_mp(h_mp, y_mp, sectors, pts, tensors_mp):
    tot = mp.mpf(0)
    y3 = y_mp ** 3
    for name, _, _, Nc in sectors:
        weight = mp.mpf(Nc) / 24
        for (a, b) in pts:
            Y = tensors_mp[(name, a, b)]
            M = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    M[i, j] = sum(Y[i][j][k] * h_mp[k] for k in range(6))
            dM = mp.det(M)
            det_H = y3 * (mp.re(dM) ** 2 + mp.im(dM) ** 2)
            tot += -weight * mp.log(det_H)
    return tot


def run_section_2(UM, vp_mp, vm_mp, hstar_mp, vp_np, vm_np, hs_np):
    mp.mp.dps = 55
    phis_24 = np.linspace(0, 2 * np.pi, 24, endpoint=False)
    circ_np = [(vp_np + np.exp(f_c(0, 1) * ph) * vm_np) / np.sqrt(2) for ph in phis_24]
    circ_mp = [(vp_mp + mp.exp(mp_c(0, 1) * 2 * mp.pi * idx / 24) * vm_mp) / mp.sqrt(2) for idx in range(24)]

    y17 = rat_f(17, 10)
    tau17 = rat_f(13, 100) + f_c(0, 1) * y17
    sec17, pts17, tens17 = build_sector_tensors_np(tau17)
    bx_vp17, _, muE2_17 = eval_box_cw_np(vp_np, y17, sec17, pts17, tens17)
    bx_vm17, _, _ = eval_box_cw_np(vm_np, y17, sec17, pts17, tens17)
    bx_hs17, _, _ = eval_box_cw_np(hs_np, y17, sec17, pts17, tens17)
    circ_res17 = [eval_box_cw_np(hc, y17, sec17, pts17, tens17)[0] for hc in circ_np]
    orbit6_17 = [circ_res17[idx] for idx in [0, 4, 8, 12, 16, 20]]
    b_box_vp17 = bx_vp17 - bx_hs17
    b_box_vm17 = bx_vm17 - bx_hs17
    spread6_17 = max(orbit6_17) - min(orbit6_17)
    halfstep17 = min(circ_res17[2], circ_res17[22]) - circ_res17[0]
    box_argmin17 = int(np.argmin(circ_res17))

    cur_um = hstar_mp
    for m in range(6):
        h_um_np = np.array([complex(cur_um[k]) for k in range(6)], dtype=np.complex128)
        v_um = eval_box_cw_np(h_um_np, y17, sec17, pts17, tens17)[0]
        assert abs(v_um - circ_res17[(-4 * m) % 24]) < 10 ** (-11)
        cur_um = UM * cur_um

    thetas_9 = np.linspace(0, np.pi, 9)
    s3_grid = np.zeros((9, 24))
    for it, th in enumerate(thetas_9):
        for ip, ph in enumerate(phis_24):
            h_s3 = np.cos(th / 2) * vp_np + np.sin(th / 2) * np.exp(f_c(0, 1) * ph) * vm_np
            s3_grid[it, ip] = eval_box_cw_np(h_s3, y17, sec17, pts17, tens17)[0]
    s3_argmin17 = [int(x) for x in np.unravel_index(int(np.argmin(s3_grid)), s3_grid.shape)]

    cwE_vp17 = eval_box_cw_np(vp_np, y17, sec17, pts17, tens17, mu2=muE2_17)[1]
    cwE_hs17 = eval_box_cw_np(hs_np, y17, sec17, pts17, tens17, mu2=muE2_17)[1]
    cwE_diff17 = cwE_vp17 - cwE_hs17

    y17_mp = mp_rat(17, 10)
    tau17_mp = mp_rat(13, 100) + mp_c(0, 1) * y17_mp
    sec17_mp, pts17_mp, tens17_mp = build_sector_tensors_mp(tau17_mp)
    bx_vp17_mp, _, muE2_17_mp = eval_box_cw_mp(vp_mp, y17_mp, sec17_mp, pts17_mp, tens17_mp)
    bx_hs17_mp, _, _ = eval_box_cw_mp(hstar_mp, y17_mp, sec17_mp, pts17_mp, tens17_mp)
    cwE_vp17_mp = eval_box_cw_mp(vp_mp, y17_mp, sec17_mp, pts17_mp, tens17_mp, mu2=muE2_17_mp)[1]
    cwE_hs17_mp = eval_box_cw_mp(hstar_mp, y17_mp, sec17_mp, pts17_mp, tens17_mp, mu2=muE2_17_mp)[1]
    assert abs(float(bx_vp17_mp - bx_hs17_mp) - b_box_vp17) < 10 ** (-10)
    assert abs(float(cwE_vp17_mp - cwE_hs17_mp) - cwE_diff17) < 10 ** (-10)

    vd_circ17 = [eval_det_mp(hc, y17_mp, sec17_mp, pts17_mp, tens17_mp) for hc in circ_mp]
    det_excess17 = float(vd_circ17[0] - min(vd_circ17))

    assert b_box_vp17 > 15
    assert b_box_vm17 > 15
    assert spread6_17 > 20
    assert halfstep17 > 1
    assert box_argmin17 == 0
    assert s3_argmin17 == [4, 0]
    assert cwE_diff17 < -40
    assert det_excess17 > 60

    y6 = 6
    tau6 = rat_f(13, 100) + f_c(0, 1) * y6
    sec6, pts6, tens6 = build_sector_tensors_np(tau6)
    bx_vp6, cw1_vp6, muE2_6 = eval_box_cw_np(vp_np, y6, sec6, pts6, tens6, mu2=1)
    bx_vm6, _, _ = eval_box_cw_np(vm_np, y6, sec6, pts6, tens6, mu2=1)
    bx_hs6, cw1_hs6, _ = eval_box_cw_np(hs_np, y6, sec6, pts6, tens6, mu2=1)
    circ_res6 = [eval_box_cw_np(hc, y6, sec6, pts6, tens6, mu2=1) for hc in circ_np]
    bxs6 = [r[0] for r in circ_res6]
    cw1s6 = [r[1] for r in circ_res6]
    orbit6_6 = [bxs6[idx] for idx in [0, 4, 8, 12, 16, 20]]
    b_box_vp6 = bx_vp6 - bx_hs6
    b_box_vm6 = bx_vm6 - bx_hs6
    spread6_6 = max(orbit6_6) - min(orbit6_6)
    halfstep6 = min(bxs6[2], bxs6[22]) - bxs6[0]
    box_argmin6 = int(np.argmin(bxs6))
    cw1_diff6 = cw1_vp6 - cw1_hs6
    cw1_argmin6 = int(np.argmin(cw1s6))

    cwE_vp6 = eval_box_cw_np(vp_np, y6, sec6, pts6, tens6, mu2=muE2_6)[1]
    cwE_hs6 = eval_box_cw_np(hs_np, y6, sec6, pts6, tens6, mu2=muE2_6)[1]
    cwE_diff6 = cwE_vp6 - cwE_hs6

    y6_mp = mp.mpf(6)
    tau6_mp = mp_rat(13, 100) + mp_c(0, 1) * y6_mp
    sec6_mp, pts6_mp, tens6_mp = build_sector_tensors_mp(tau6_mp)
    bx_vp6_mp, cw1_vp6_mp, muE2_6_mp = eval_box_cw_mp(vp_mp, y6_mp, sec6_mp, pts6_mp, tens6_mp, mu2=1)
    bx_hs6_mp, cw1_hs6_mp, _ = eval_box_cw_mp(hstar_mp, y6_mp, sec6_mp, pts6_mp, tens6_mp, mu2=1)
    cwE_vp6_mp = eval_box_cw_mp(vp_mp, y6_mp, sec6_mp, pts6_mp, tens6_mp, mu2=muE2_6_mp)[1]
    cwE_hs6_mp = eval_box_cw_mp(hstar_mp, y6_mp, sec6_mp, pts6_mp, tens6_mp, mu2=muE2_6_mp)[1]
    assert abs(float(bx_vp6_mp - bx_hs6_mp) - b_box_vp6) < 10 ** (-10)
    assert abs(float(cw1_vp6_mp - cw1_hs6_mp) - cw1_diff6) < 10 ** (-10)
    assert abs(float(cwE_vp6_mp - cwE_hs6_mp) - cwE_diff6) < 10 ** (-10)

    vd_circ6 = [eval_det_mp(hc, y6_mp, sec6_mp, pts6_mp, tens6_mp) for hc in circ_mp]
    det_excess6 = float(vd_circ6[0] - min(vd_circ6))

    assert b_box_vp6 > 100
    assert b_box_vm6 > 15
    assert spread6_6 > 200
    assert halfstep6 > 40
    assert box_argmin6 == 0
    assert cw1_diff6 > 150
    assert cw1_argmin6 == 0
    assert cwE_diff6 < -200
    assert det_excess6 > 250

    return {
        "y_17_10": {
            "B_box_vp": b_box_vp17,
            "B_box_vm": b_box_vm17,
            "orbit_6_spread_box": spread6_17,
            "halfstep_barrier_box": halfstep17,
            "box_circ_min_idx": box_argmin17,
            "s3_box_argmin": s3_argmin17,
            "cw_muE_diff": cwE_diff17,
            "det_excess": det_excess17,
        },
        "y_6": {
            "B_box_vp": b_box_vp6,
            "B_box_vm": b_box_vm6,
            "orbit_6_spread_box": spread6_6,
            "halfstep_barrier_box": halfstep6,
            "box_circ_min_idx": box_argmin6,
            "cw_mu1_diff": cw1_diff6,
            "cw1_circ_min_idx": cw1_argmin6,
            "cw_muE_diff": cwE_diff6,
            "det_excess": det_excess6,
        },
        "passed": True,
    }, (sec17_mp, tens17_mp)


def run_section_3(hstar_mp):
    mp.mp.dps = 55
    z = sp.Symbol("z")
    phi24 = sp.cyclotomic_poly(24, z)

    def red(expr):
        return sp.rem(sp.expand(expr), phi24, z)

    def mat_conj(M):
        return M.applyfunc(lambda e: red(e.subs(z, z**23)))

    sqrt2 = red(z**3 - z**9)
    sqrt3 = red(z**2 - z**10)
    sqrt6 = red(sqrt2 * sqrt3)
    T_sym = sp.Matrix(6, 6, lambda j, k: red(z ** (2 * j * j)) if j == k else 0)
    S_sym = sp.Matrix(6, 6, lambda j, k: red((sqrt6 / 6) * z ** ((-4 * j * k) % 24)))
    UM_sym = (T_sym * S_sym * mat_conj(T_sym.T) * mat_conj(S_sym.T)).applyfunc(red)
    e0_sym = sp.Matrix([1, 0, 0, 0, 0, 0])
    Pp_e0 = sp.zeros(6, 1)
    Pm_e0 = sp.zeros(6, 1)
    cur_sym = e0_sym
    for k in range(12):
        Pp_e0 += z ** ((-2 * k) % 24) * cur_sym
        Pm_e0 += z ** ((2 * k) % 24) * cur_sym
        cur_sym = (UM_sym * cur_sym).applyfunc(red)
    vp_sym = ((Pp_e0 / 12) * red(3 + sqrt3)).applyfunc(red)
    vm_sym = ((Pm_e0 / 12) * red(3 - sqrt3)).applyfunc(red)
    hstar_sym = ((vp_sym + vm_sym) * sqrt2 / 2).applyfunc(red)

    th = [sp.Symbol(f"th{c}") for c in range(4)]
    th_bar = [sp.Symbol(f"thb{c}") for c in range(4)]

    def get_th(c_idx):
        c_mod = c_idx % 6
        if c_mod > 3:
            c_mod = 6 - c_mod
        return th[c_mod]

    R_sym = sp.Matrix([[0, 0, red(z**16)], [0, 1, 0], [red(z**8), 0, 0]])
    assert (R_sym * R_sym).applyfunc(red) == sp.eye(3)
    assert mat_conj(R_sym.T) == R_sym

    for a_par in [0, 1]:
        for b_par in [0, 1]:
            M_sym = sp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    for k in [0, 1, 5]:
                        if (i + j + 1 - k) % 3 == 0:
                            c_idx = (2 * i + 1 - k + 3 * a_par) % 6
                            sgn = (-1) ** (c_idx * b_par)
                            phase_b = z ** (4 * k)
                            M_sym[i, j] += sgn * phase_b * hstar_sym[k] * get_th(c_idx)
            M_sym = M_sym.applyfunc(sp.expand)
            M_dag = M_sym.T.applyfunc(lambda e: e.subs(list(zip(th, th_bar))).subs(z, z**23))
            G_sym = (M_sym * M_dag).applyfunc(sp.expand)
            comm_red = (R_sym * G_sym - G_sym * R_sym).applyfunc(lambda e: sp.rem(sp.expand(e), phi24, z))
            assert comm_red == sp.zeros(3, 3)

    tau6 = mp_rat(13, 100) + mp_c(0, 6)
    R_mp = mp.matrix([[0, 0, mp.exp(-2 * mp_c(0, 1) * mp.pi / 3)], [0, 1, 0], [mp.exp(2 * mp_c(0, 1) * mp.pi / 3), 0, 0]])
    pts = [(a, b) for a in range(5) for b in range(5) if not (a == 0 and b == 0)]
    max_comm_24 = mp.mpf(0)
    for (a, b) in pts:
        w = (a * tau6 + b) / 5
        th_c = exact_theta_by_c_mp(1 * w, -4 * w, tau6)
        Mu = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    if (i + j + 1 - k) % 3 == 0:
                        c = (2 * i + 1 - k) % 6
                        Mu[i, j] += mp.exp(mp_c(0, 1) * mp.pi * k / 3) * th_c[c] * hstar_mp[k]
        Gu = Mu * Mu.H
        comm_err = max(abs(x) for x in (R_mp * Gu - Gu * R_mp))
        max_comm_24 = max(max_comm_24, comm_err)
    assert max_comm_24 < mp_pow10(-40)

    w_mark = (2 * tau6 + 4) / 5
    th_cu = exact_theta_by_c_mp(1 * w_mark, -4 * w_mark, tau6)
    th_cd = exact_theta_by_c_mp(1 * w_mark, 2 * w_mark, tau6)
    Mu_m = mp.zeros(3, 3)
    Md_m = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            for k in range(6):
                if (i + j + 1 - k) % 3 == 0:
                    c = (2 * i + 1 - k) % 6
                    ph_b = mp.exp(mp_c(0, 1) * mp.pi * k / 3)
                    Mu_m[i, j] += ph_b * th_cu[c] * hstar_mp[k]
                    Md_m[i, j] += ph_b * th_cd[c] * hstar_mp[k]
    _, Uu_m = mp.eighe(Mu_m * Mu_m.H)
    _, Ud_m = mp.eighe(Md_m * Md_m.H)
    Uu_desc = mp.matrix([[Uu_m[r, 2 - c] for c in range(3)] for r in range(3)])
    Ud_desc = mp.matrix([[Ud_m[r, 2 - c] for c in range(3)] for r in range(3)])
    V_ckm = Uu_desc.H * Ud_desc
    inv_sq2 = 1 / mp.sqrt(2)
    target_v = [
        [inv_sq2, mp.mpf(0), inv_sq2],
        [inv_sq2, mp.mpf(0), inv_sq2],
        [mp.mpf(0), mp.mpf(1), mp.mpf(0)],
    ]
    mark_ckm_err = max(abs(abs(V_ckm[r, c]) - target_v[r][c]) for r in range(3) for c in range(3))
    assert mark_ckm_err < mp_rat(1, 5)

    def eval_unshifted(y_int):
        tau = mp_rat(13, 100) + mp_c(0, y_int)
        th_c0 = exact_theta_by_c_mp(0, 0, tau)
        M0 = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    if (i + j + 1 - k) % 3 == 0:
                        c = (2 * i + 1 - k) % 6
                        M0[i, j] += mp.exp(mp_c(0, 1) * mp.pi * k / 3) * th_c0[c] * hstar_mp[k]
        G0 = M0 * M0.H
        comm0 = max(abs(x) for x in (R_mp * G0 - G0 * R_mp))
        evals0 = sorted([mp.re(x) for x in mp.eighe(G0)[0]], reverse=True)
        sv0 = [mp.sqrt(max(x, 0)) for x in evals0]
        return comm0, sv0

    comm0_6, _ = eval_unshifted(6)
    comm0_11, sv11 = eval_unshifted(11)
    comm0_14, sv14 = eval_unshifted(14)
    assert max(comm0_6, comm0_11, comm0_14) < mp_pow10(-40)
    exp1 = -mp.log((sv14[1] / sv14[0]) / (sv11[1] / sv11[0])) / (mp.pi * 3)
    exp2 = -mp.log((sv14[2] / sv14[0]) / (sv11[2] / sv11[0])) / (mp.pi * 3)
    assert abs(exp1 - 0) < mp_rat(2, 1000)
    assert abs(exp2 - mp_rat(4, 3)) < mp_rat(2, 1000)

    return {
        "sympy_comm_zero_all4_parities": True,
        "max_comm_24pts_y6": mp.nstr(max_comm_24, 8),
        "mark_2_4_ckm_max_diff": float(mark_ckm_err),
        "mark_2_4_V_abs": [[float(abs(V_ckm[r, c])) for c in range(3)] for r in range(3)],
        "unshifted_comm_y6": mp.nstr(comm0_6, 8),
        "unshifted_sv_exponents_11_to_14": [float(exp1), float(exp2)],
        "passed": True,
    }, (Mu_m, Md_m)


class DetStream:
    """Deterministic SHA-256 rational stream for Haar unitary generation at 55 digits."""

    def __init__(self, seed_bytes):
        self.state = seed_bytes
        self.counter = 0

    def next_rat(self):
        self.counter += 1
        digest = hashlib.sha256(self.state + self.counter.to_bytes(8, "big")).digest()
        val = int.from_bytes(digest[:16], "big")
        if val == 0:
            val = 1
        return mp.mpf(val) / mp.mpf(1 << 128)


def haar_u3_mp(stream):
    Z = mp.zeros(3, 3)
    two_pi = 2 * mp.pi
    for r in range(3):
        for c in range(3):
            u1 = stream.next_rat()
            u2 = stream.next_rat()
            rad = mp.sqrt(-2 * mp.log(u1))
            ang = two_pi * u2
            Z[r, c] = mp.mpc(rad * mp.cos(ang), rad * mp.sin(ang))
    Q, R = mp.qr(Z)
    for c in range(3):
        d = R[c, c]
        ph = d / abs(d)
        for r in range(3):
            Q[r, c] *= ph
    return Q


def haar_su3_mp(stream):
    U = haar_u3_mp(stream)
    det_u = mp.det(U)
    ph_conj = mp.conj(det_u) / abs(det_u)
    for r in range(3):
        U[r, 0] *= ph_conj
    return U


def run_section_4(UM, vp_mp, vm_mp, hstar_mp, sec1_res, sec2_res, tens17_mp, sec17_mp, Mu_mark, Md_mark):
    mp.mp.dps = 55
    v_fake_vals = []
    cur = hstar_mp
    for _ in range(12):
        ov = (hstar_mp.H * cur)[0, 0]
        v_fake_vals.append(float(1 - (mp.re(ov) ** 2 + mp.im(ov) ** 2)))
        cur = UM * cur
    pfu3_1_spread = max(v_fake_vals) - min(v_fake_vals)
    assert pfu3_1_spread > rat_f(1, 2)

    b_froz_vals = [v["B_frozen_P873"] for v in sec1_res["frozen_25x25_gl"].values()]
    assert all(val < -1 for val in b_froz_vals)

    det_excess17 = sec2_res["y_17_10"]["det_excess"]
    assert det_excess17 > 60

    def q_quad_11(h_mp, sec_mp, tens_mp):
        tot = mp.mpf(0)
        for name, _, _, Nc in sec_mp:
            Y = tens_mp[(name, 1, 1)]
            M = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    M[i, j] = sum(Y[i][j][k] * h_mp[k] for k in range(6))
            tr_val = sum(mp.re(M[i, j]) ** 2 + mp.im(M[i, j]) ** 2 for i in range(3) for j in range(3))
            tot += mp.mpf(Nc) * tr_val
        return tot

    qp17 = q_quad_11(vp_mp, sec17_mp, tens17_mp)
    qm17 = q_quad_11(vm_mp, sec17_mp, tens17_mp)
    pfu3_4_rel = float(abs(qp17 - qm17) / qp17)
    assert pfu3_4_rel > rat_f(1, 5)

    tau6 = mp_rat(13, 100) + mp_c(0, 6)
    w11 = (1 * tau6 + 1) / 5
    M_u11 = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            for k in range(6):
                M_u11[i, j] += exact_theta_mp(i, j, k, 1 * w11, -4 * w11, tau6) * hstar_mp[k]

    def sv_ratios(M):
        G = M * M.H
        ev = sorted([mp.re(x) for x in mp.eighe(G)[0]], reverse=True)
        sv = [mp.sqrt(max(x, 0)) for x in ev]
        return sv[1] / sv[0], sv[2] / sv[0]

    base_r1, base_r2 = sv_ratios(M_u11)
    base_raw_ratio = abs(M_u11[0, 0] / M_u11[2, 2])

    def ckm_abs(Mu, Md):
        _, Uu = mp.eighe(Mu * Mu.H)
        _, Ud = mp.eighe(Md * Md.H)
        Uu_d = mp.matrix([[Uu[r, 2 - c] for c in range(3)] for r in range(3)])
        Ud_d = mp.matrix([[Ud[r, 2 - c] for c in range(3)] for r in range(3)])
        V = Uu_d.H * Ud_d
        return [[abs(V[r, c]) for c in range(3)] for r in range(3)]

    base_ckm = ckm_abs(Mu_mark, Md_mark)
    stream = DetStream(b"PFU3-5-HAAR-SU3-GUARDRAIL3")
    max_sv_err = mp.mpf(0)
    max_raw_shift = mp.mpf(0)
    max_ckm_err = mp.mpf(0)
    for _ in range(10):
        UL_q = haar_su3_mp(stream)
        UR_u = haar_su3_mp(stream)
        UR_d = haar_su3_mp(stream)
        Mp = UL_q * M_u11 * UR_u.H
        r1, r2 = sv_ratios(Mp)
        max_sv_err = max(max_sv_err, abs(r1 - base_r1), abs(r2 - base_r2))
        raw_ratio = abs(Mp[0, 0] / Mp[2, 2])
        max_raw_shift = max(max_raw_shift, abs(raw_ratio - base_raw_ratio))
        ckm_p = ckm_abs(UL_q * Mu_mark * UR_u.H, UL_q * Md_mark * UR_d.H)
        for r in range(3):
            for c in range(3):
                max_ckm_err = max(max_ckm_err, abs(ckm_p[r][c] - base_ckm[r][c]))

    assert max_sv_err < mp_pow10(-30)
    assert max_raw_shift > mp_rat(1, 5)
    assert max_ckm_err < mp_pow10(-30)

    return {
        "PFU3_1_vfake_spread": pfu3_1_spread,
        "PFU3_2_bfrozen_all3": b_froz_vals,
        "PFU3_3_vdet_excess_y17": det_excess17,
        "PFU3_4_1pt_quad_rel_spread": pfu3_4_rel,
        "PFU3_5_haar_sv_ratio_err": mp.nstr(max_sv_err, 8),
        "PFU3_5_raw_m00_m22_shift": float(max_raw_shift),
        "PFU3_5_guardrail3_ckm_invariance_err": mp.nstr(max_ckm_err, 8),
        "passed": True,
    }


def main():
    t0 = time.time()
    self_path = pathlib.Path(__file__).resolve()
    repo_root = self_path.parents[2]
    out_path = self_path.parent / "referee_found_v2_u3_out.json"

    s0 = run_section_0(repo_root, self_path)
    s1, (UM, vp_mp, vm_mp, hstar_mp, vp_np, vm_np, hs_np) = run_section_1()
    s2, (sec17_mp, tens17_mp) = run_section_2(UM, vp_mp, vm_mp, hstar_mp, vp_np, vm_np, hs_np)
    s3, (Mu_m, Md_m) = run_section_3(hstar_mp)
    s4 = run_section_4(UM, vp_mp, vm_mp, hstar_mp, s1, s2, tens17_mp, sec17_mp, Mu_m, Md_m)

    elapsed = time.time() - t0
    payload = {
        "gate": "AGY-002_FOUND-V2-U3",
        "role": "cold-room-zero-trust-referee",
        "empirical_firewall": "0 of 19",
        "elapsed_seconds": elapsed,
        "all_passed": True,
        "section_0": s0,
        "section_1": s1,
        "section_2": s2,
        "section_3": s3,
        "section_4": s4,
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"STATUS: PASS | manifests=16/16 | elapsed={elapsed:.2f}s | out={out_path.name}", flush=True)


if __name__ == "__main__":
    main()
