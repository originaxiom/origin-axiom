#!/usr/bin/env python3
"""Independent zero-shared-code verification and analytic extension of Q0016 (P-879 two-sector floor scope)."""
import math
import sys
import numpy as np

SIGMA = (
    np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex),
    np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex),
    np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
)


def yukawa_from_doublet(h_mat, chan):
    out = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        sa_h = SIGMA[a] @ h_mat
        for b in range(3):
            out[a, b] = 0.5 * np.trace(sa_h @ SIGMA[b] @ chan)
    return out


def three_regime_floor(t_val, s_left, align_a):
    arg0 = min(1.0, max(-1.0, (1.0 + s_left) / (3.0 - s_left)))
    arg_a = min(1.0, max(-1.0, align_a))
    gap = math.acos(arg0) - math.acos(arg_a)
    s_req = math.sin(0.5 * gap) if gap > 0.0 else 0.0
    thresh1 = s_req / (2.0 * (1.0 + s_req)) if s_req > 0.0 else 0.0
    if t_val <= thresh1:
        return (s_req * s_req) / (2.0 * (1.0 + 2.0 * s_req))
    if t_val <= s_req:
        return (s_req * t_val) / (1.0 + 2.0 * t_val)
    return (t_val * t_val) / (1.0 + 2.0 * t_val)


def eval_pair(h_vec, mu_mat, md_mat, alike_reading):
    hd_mat = h_vec[0] * SIGMA[0] + h_vec[1] * SIGMA[1] + h_vec[2] * SIGMA[2]
    if alike_reading:
        hu_mat = hd_mat
    else:
        hu_mat = np.conj(h_vec[0]) * SIGMA[0] + np.conj(h_vec[1]) * SIGMA[1] + np.conj(h_vec[2]) * SIGMA[2]
    uu, su, _ = np.linalg.svd(yukawa_from_doublet(hu_mat, mu_mat))
    ud, sd, _ = np.linalg.svd(yukawa_from_doublet(hd_mat, md_mat))
    rho = max(float(su[1] / su[0]), float(sd[1] / sd[0]))
    align_a = float(abs(np.vdot(uu[:, 0], ud[:, 0])))
    r_val = float(abs(h_vec @ h_vec) / np.vdot(h_vec, h_vec).real)
    t_val = r_val / (1.0 + math.sqrt(max(0.0, 1.0 - r_val * r_val)))
    _, _, vhu = np.linalg.svd(mu_mat)
    _, _, vhd = np.linalg.svd(md_mat)
    ru = np.conj(vhu[0])
    rd = np.conj(vhd[0])
    s_left = float(abs(ru[0] * rd[1] - ru[1] * rd[0]))
    f_val = three_regime_floor(t_val, s_left, align_a)
    return rho, f_val, t_val, s_left, align_a


def analytic_alike_limit_check():
    """Exact rank-one null-Higgs witness proving reading (ii) violates M3 down to rho -> 0 against F -> (2*sqrt(3)-3)/6."""
    eps = 1e-7
    h_near_null = np.array([1.0, 1.0j, eps], dtype=complex)
    psi_u = np.array([1.0, 0.0], dtype=complex)
    psi_d = np.array([0.0, 1.0], dtype=complex)
    phi_shared = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    phi_orth = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2.0)
    mu_mat = np.outer(psi_u, np.conj(phi_shared)) + eps * np.outer(psi_d, np.conj(phi_orth))
    md_mat = np.outer(psi_d, np.conj(phi_shared)) + eps * np.outer(psi_u, np.conj(phi_orth))
    rho_ii, f_ii, _, _, a_ii = eval_pair(h_near_null, mu_mat, md_mat, True)
    rho_i, f_i, _, _, a_i = eval_pair(h_near_null, mu_mat, md_mat, False)
    exact_target_f = (2.0 * math.sqrt(3.0) - 3.0) / 6.0
    return rho_i, f_i, a_i, rho_ii, f_ii, a_ii, exact_target_f


def independent_campaign(n_trials=24000):
    rng = np.random.default_rng(31415926)
    viol_conj = 0
    viol_alike = 0
    for k in range(n_trials):
        kind = k % 6
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        mu_mat = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        md_mat = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        if kind == 1:
            u1 = rng.normal(size=3)
            u1 /= np.linalg.norm(u1)
            u2 = rng.normal(size=3)
            u2 -= (u2 @ u1) * u1
            u2 /= np.linalg.norm(u2)
            h_vec = u1 + 1j * u2 + (10.0 ** rng.uniform(-6.0, -1.0)) * (rng.normal(size=3) + 1j * rng.normal(size=3))
        elif kind == 2:
            h_vec = rng.normal(size=3) + 1j * (10.0 ** rng.uniform(-6.0, -1.0)) * rng.normal(size=3)
        elif kind == 3:
            for mat in (mu_mat, md_mat):
                u, _, vh = np.linalg.svd(mat)
                mat[:] = u @ np.diag([1.0, 10.0 ** rng.uniform(-6.0, -1.0)]) @ vh
        elif kind == 4:
            u1, _, vh = np.linalg.svd(mu_mat)
            u2, _, _ = np.linalg.svd(md_mat)
            mu_mat = u1 @ np.diag([1.0, rng.uniform(0.0, 0.3)]) @ vh
            md_mat = u2 @ np.diag([1.0, rng.uniform(0.0, 0.3)]) @ vh
        elif kind == 5:
            u1, _, vh = np.linalg.svd(mu_mat)
            u2, _, _ = np.linalg.svd(md_mat)
            mu_mat = u1 @ np.diag([1.0, rng.uniform(0.0, 0.3)]) @ vh
            md_mat = u2 @ np.diag([1.0, rng.uniform(0.0, 0.3)]) @ vh[::-1]
        rho_c, f_c, _, _, _ = eval_pair(h_vec, mu_mat, md_mat, False)
        rho_a, f_a, _, _, _ = eval_pair(h_vec, mu_mat, md_mat, True)
        if rho_c < f_c - 1e-9:
            viol_conj += 1
        if rho_a < f_a - 1e-9:
            viol_alike += 1
    return viol_conj, viol_alike


def main():
    rho_i, f_i, a_i, rho_ii, f_ii, a_ii, exact_f = analytic_alike_limit_check()
    viol_conj, viol_alike = independent_campaign(24000)
    analytic_ok = (
        abs(a_i - (1.0 / 3.0)) < 1e-6
        and abs(f_i) < 1e-12
        and abs(a_ii - 1.0) < 1e-12
        and rho_ii < 1e-6
        and abs(f_ii - exact_f) < 1e-6
    )
    holds = (viol_conj == 0) and (viol_alike >= 5) and analytic_ok
    print("DECISIVE: independent_24000_conjugate_violations = %d" % viol_conj)
    print("DECISIVE: independent_24000_alike_violations = %d" % viol_alike)
    print("DECISIVE: analytic_null_limit_conjugate_alignment = %.8f" % a_i)
    print("DECISIVE: analytic_null_limit_alike_floor_gap = %.8f" % (f_ii - rho_ii))
    print("DECISIVE: q0016_scope_and_analytic_extension_hold = %s" % holds)
    return 0 if holds else 1


if __name__ == "__main__":
    sys.exit(main())
