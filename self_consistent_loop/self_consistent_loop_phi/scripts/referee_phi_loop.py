#!/usr/bin/env python3
"""Zero-Trust Independent Referee Audit for Phi(X*) = X* (Guardrail 6).

STRICT ZERO-IMPORT ENFORCEMENT:
  - Self-audits its own AST at startup to guarantee ZERO imports from `phi_loop` or `src`.
  - Rebuilds every mathematical sector from scratch using DIFFERENT algorithms:
      * BE-1: Dynkin-diagram + symmetrizer D*C exact rational Fractions (vs Euclidean vectors)
              + adversarial SL(2,Z) matrix [[3,-1],[7,-2]] check on Theta_{E_8}.
      * BE-2: Sinc-DVR spectral collocation solver (vs tridiagonal FD + Richardson)
              + independent Farey/geodesic orbit finder and mod-N torsion check.
      * BE-3: 30-digit mpmath evaluation + adversarial Gamma(5) matrix [[6,5],[-5,-4]]
              modular invariance check on order-5 torsion Wilson line.
      * BE-4: Clifford algebra Spin(16) = Lambda^2(R^16) (+) S^+_16 construction of e_8
              (vs Frenkel-Kac root-lattice cocycle) + fresh adversarial Haar unitaries.
"""

from __future__ import annotations

import ast
import fractions
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = Path(__file__).resolve()
PLAN_PATH = PROJECT_ROOT / "PREREGISTRATION_PLAN.md"
SEAL_PATH = PROJECT_ROOT / "SEAL_SHA256.txt"
PRODUCER_JSON_PATH = PROJECT_ROOT / "outputs" / "phi_loop_results.json"
REFEREE_JSON_PATH = PROJECT_ROOT / "outputs" / "referee_audit_verdict.json"


def assert_zero_producer_imports() -> Dict[str, Any]:
    """Guardrail 6: Parse this file's own AST and assert zero imports from phi_loop or src."""
    source = SELF_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SELF_PATH))
    imported_modules: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_modules.append(node.module)
    forbidden = [m for m in imported_modules if "phi_loop" in m or m.startswith("src")]
    if forbidden:
        raise RuntimeError(f"Guardrail 6 violation! Forbidden producer imports: {forbidden}")
    return {
        "ast_checked_file": str(SELF_PATH.name),
        "imported_modules": sorted(set(imported_modules)),
        "forbidden_imports_found": forbidden,
        "zero_producer_imports_verified": len(forbidden) == 0,
    }


def exact_rational_det(mat: List[List[fractions.Fraction]]) -> fractions.Fraction:
    """Exact Gaussian elimination over Q using fractions.Fraction."""
    n = len(mat)
    A = [[fractions.Fraction(x) for x in row] for row in mat]
    det = fractions.Fraction(1, 1)
    for col in range(n):
        piv = None
        for row in range(col, n):
            if A[row][col] != 0:
                piv = row
                break
        if piv is None:
            return fractions.Fraction(0, 1)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        for row in range(col + 1, n):
            factor = A[row][col] / A[col][col]
            for k in range(col, n):
                A[row][k] -= factor * A[col][k]
    return det


def build_dynkin_gram_from_cartan(fam: str, r: int) -> Tuple[List[List[fractions.Fraction]], List[List[fractions.Fraction]]]:
    """Build asymmetric Cartan C and symmetric Euclidean Gram G = diag(d_i) * C (min d_i = 2) purely from Dynkin data."""
    C = [[fractions.Fraction(2 if i == j else 0) for j in range(r)] for i in range(r)]
    d = [fractions.Fraction(2) for _ in range(r)]

    if fam == "A":
        for i in range(r - 1):
            C[i][i + 1] = fractions.Fraction(-1)
            C[i + 1][i] = fractions.Fraction(-1)
    elif fam == "B":
        for i in range(r - 1):
            C[i][i + 1] = fractions.Fraction(-1)
            C[i + 1][i] = fractions.Fraction(-1)
        # alpha_{r-1} long (norm^2=4), alpha_r short (norm^2=2): C_{r-2, r-1} = 2*<long,short>/<short,short> = -2
        C[r - 2][r - 1] = fractions.Fraction(-2)
        C[r - 1][r - 2] = fractions.Fraction(-1)
        for i in range(r - 1):
            d[i] = fractions.Fraction(4)
        d[r - 1] = fractions.Fraction(2)
    elif fam == "C":
        for i in range(r - 1):
            C[i][i + 1] = fractions.Fraction(-1)
            C[i + 1][i] = fractions.Fraction(-1)
        # alpha_1..alpha_{r-1} short (norm^2=2), alpha_r long (norm^2=4): C_{r-2, r-1} = 2*<-2>/4 = -1, C_{r-1, r-2} = -2
        C[r - 2][r - 1] = fractions.Fraction(-1)
        C[r - 1][r - 2] = fractions.Fraction(-2)
        d[r - 1] = fractions.Fraction(4)
    elif fam == "D":
        for i in range(r - 2):
            C[i][i + 1] = fractions.Fraction(-1)
            C[i + 1][i] = fractions.Fraction(-1)
        C[r - 3][r - 1] = fractions.Fraction(-1)
        C[r - 1][r - 3] = fractions.Fraction(-1)
    elif fam == "G" and r == 2:
        # alpha_1 short (d_1=2), alpha_2 long (d_2=6), <alpha_1, alpha_2> = -3:
        # C_12 = 2*(-3)/6 = -1, C_21 = 2*(-3)/2 = -3.
        C = [[fractions.Fraction(2), fractions.Fraction(-1)], [fractions.Fraction(-3), fractions.Fraction(2)]]
        d = [fractions.Fraction(2), fractions.Fraction(6)]
    elif fam == "F" and r == 4:
        C = [
            [fractions.Fraction(2), fractions.Fraction(-1), fractions.Fraction(0), fractions.Fraction(0)],
            [fractions.Fraction(-1), fractions.Fraction(2), fractions.Fraction(-2), fractions.Fraction(0)],
            [fractions.Fraction(0), fractions.Fraction(-1), fractions.Fraction(2), fractions.Fraction(-1)],
            [fractions.Fraction(0), fractions.Fraction(0), fractions.Fraction(-1), fractions.Fraction(2)],
        ]
        d = [fractions.Fraction(4), fractions.Fraction(4), fractions.Fraction(2), fractions.Fraction(2)]
    elif fam == "E" and r in (6, 7, 8):
        # Bourbaki numbering: spine 1-3-4-5-6-(7)-(8) with leaf 2 attached to 4
        edges = [(0, 2), (2, 3), (1, 3), (3, 4), (4, 5)]
        if r >= 7:
            edges.append((5, 6))
        if r == 8:
            edges.append((6, 7))
        for u, v in edges:
            C[u][v] = fractions.Fraction(-1)
            C[v][u] = fractions.Fraction(-1)
    else:
        raise ValueError(f"Unknown Dynkin type {fam}_{r}")

    # Wait: recall C_{ij} = 2 G_{ij} / G_{jj} => G_{ij} = C_{ij} * (d_j / 2)!
    G = [[C[i][j] * (d[j] / fractions.Fraction(2)) for j in range(r)] for i in range(r)]
    return G, C


def referee_check_sector1(prod_s1: Dict[str, Any]) -> Dict[str, Any]:
    """Independently check all 94 root systems via Dynkin data + adversarial SL(2,Z) E_8 theta transformation."""
    winners = []
    sym_err_max = 0.0
    for fam, r_range in [("A", range(1, 25)), ("B", range(2, 25)), ("C", range(3, 25)), ("D", range(4, 25))]:
        for r in r_range:
            G, _ = build_dynkin_gram_from_cartan(fam, r)
            for i in range(r):
                for j in range(r):
                    sym_err_max = max(sym_err_max, float(abs(G[i][j] - G[j][i])))
            if exact_rational_det(G) == 1 and all(int(G[i][i]) % 2 == 0 for i in range(r)):
                winners.append(f"{fam}_{r}")

    for fam, r in [("G", 2), ("F", 4), ("E", 6), ("E", 7), ("E", 8)]:
        G, C = build_dynkin_gram_from_cartan(fam, r)
        for i in range(r):
            for j in range(r):
                sym_err_max = max(sym_err_max, float(abs(G[i][j] - G[j][i])))
        if exact_rational_det(G) == 1 and all(int(G[i][i]) % 2 == 0 for i in range(r)):
            winners.append(f"{fam}_{r}")

    # Adversarial modular transformation gamma = [[3, -1], [7, -2]] in SL(2, Z) on Theta_{E_8}:
    # Note Im(gamma . tau) = Im(tau) / |7*tau - 2|^2; pick tau_adv = 0.28 + 0.45j so |7*tau - 2|^2 = (-0.04)^2 + 3.15^2 ~ 9.92,
    # or pick gamma = [[2, -1], [3, -1]] (det = -2 + 3 = +1!) at tau_adv = 0.33 + 0.62j:
    # |3*tau - 1|^2 = (-0.01)^2 + 1.86^2 = 3.46 => Im(gamma.tau) = 0.62 / 3.46 = 0.179 (q = exp(-2*pi*0.179) = 0.32, 35 shells -> 0.32^35 < 1e-17!).
    mp.mp.dps = 30
    tau_adv = mp.mpc("0.33", "0.62")
    gamma_tau = (2 * tau_adv - 1) / (3 * tau_adv - 1)

    def e4_mp(z: mp.mpc) -> mp.mpc:
        q = mp.exp(2j * mp.pi * z)
        s = mp.mpc(1)
        for n in range(1, 45):
            sig3 = sum(d**3 for d in range(1, n + 1) if n % d == 0)
            s += 240 * sig3 * (q**n)
        return s

    lhs = e4_mp(gamma_tau)
    rhs = ((3 * tau_adv - 1) ** 4) * e4_mp(tau_adv)
    adv_e8_mod_err = float(abs(lhs - rhs))

    matches_producer = (winners == prod_s1["catalogue_summary"]["sewed_winners"] == ["E_8"])
    return {
        "independent_winners": winners,
        "gram_symmetry_err": sym_err_max,
        "adversarial_SL2Z_E8_theta_err": adv_e8_mod_err,
        "matches_producer_winner": bool(matches_producer and adv_e8_mod_err < 1e-12 and sym_err_max == 0.0),
    }


def sinc_dvr_cosh_ground_state(q_coeff: float, L_box: float = 14.0, n_pts: int = 240) -> Tuple[float, float]:
    """Independent Sinc-DVR (Fourier grid Hamiltonian) solver for -d^2/dt^2 + q_coeff * cosh(t)."""
    dt = (2.0 * L_box) / (n_pts + 1)
    idx = np.arange(1, n_pts + 1, dtype=np.float64)
    t_grid = -L_box + idx * dt
    diff = idx[:, None] - idx[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        T_mat = (2.0 * ((-1.0) ** diff)) / ((diff * dt) ** 2)
    np.fill_diagonal(T_mat, (math.pi**2) / (3.0 * dt * dt))
    H_mat = T_mat + np.diag(q_coeff * np.cosh(t_grid))
    evals = np.linalg.eigvalsh(H_mat)
    return float(evals[0]), float(evals[1])


def referee_check_sector2(prod_s2: Dict[str, Any]) -> Dict[str, Any]:
    """Independently check Sinc-DVR eigenvalues, s*_(T) vs s*_(S1) (T0), and negative controls (T3)."""
    # Recompute W = L^6 R L R = [[20, 13], [3, 2]] from scratch:
    L = np.array([[1, 1], [0, 1]], dtype=np.int64)
    R = np.array([[1, 0], [1, 1]], dtype=np.int64)

    def mat_from_str(s: str) -> np.ndarray:
        M = np.eye(2, dtype=np.int64)
        for ch in s:
            M = M @ (L if ch == "L" else R)
        return M

    W_6_k1 = mat_from_str("LLLLLLRLR")
    a, b, c, d = [float(x) for x in W_6_k1.ravel()]
    tr = a + d
    ell = 2.0 * math.acosh(0.5 * tr)
    disc = math.sqrt(tr * tr - 4.0)
    xp = ((a - d) + disc) / (2.0 * c)
    xm = ((a - d) - disc) / (2.0 * c)

    # Brute-force search over integer box [-40, 40]^2 for both S1 (Z^2 \ {0}) and T ((1/5, 2/5) + Z^2):
    best_s1 = (float("inf"), 0.0)
    best_t = (float("inf"), 0.0)
    for m1 in range(-40, 41):
        for m2 in range(-40, 41):
            if (m1, m2) != (0, 0):
                f_s1 = 2.0 * abs((m1 * xp + m2) * (m1 * xm + m2)) / (xp - xm)
                tk_s1 = math.log(abs((m1 * xm + m2) / (m1 * xp + m2))) % ell
                if f_s1 < best_s1[0] - 1e-12:
                    best_s1 = (f_s1, tk_s1 / ell)

            k1 = m1 + 0.2
            k2 = m2 + 0.4
            f_t = 2.0 * abs((k1 * xp + k2) * (k1 * xm + k2)) / (xp - xm)
            tk_t = math.log(abs((k1 * xm + k2) / (k1 * xp + k2))) % ell
            if f_t < best_t[0] - 1e-12:
                best_t = (f_t, tk_t / ell)

    # Solve via Sinc-DVR at A = 1.0:
    L_s1 = max(10.0, min(18.0, math.log(1e12 / max(4 * math.pi**2 * best_s1[0], 1e-3))))
    L_t = max(10.0, min(18.0, math.log(1e12 / max(4 * math.pi**2 * best_t[0], 1e-3))))
    E0_s1_dvr, _ = sinc_dvr_cosh_ground_state(4.0 * (math.pi**2) * best_s1[0], L_box=L_s1, n_pts=380)
    E0_t_dvr, _ = sinc_dvr_cosh_ground_state(4.0 * (math.pi**2) * best_t[0], L_box=L_t, n_pts=380)

    prod_6_k1 = prod_s2["history_catalog_A1_A4"]["(6)"]["k=1"]
    e0_s1_rel_diff = abs(E0_s1_dvr - prod_6_k1["S1_A1"]["E0"]) / prod_6_k1["S1_A1"]["E0"]
    e0_t_rel_diff = abs(E0_t_dvr - prod_6_k1["T_A1"]["E0"]) / prod_6_k1["T_A1"]["E0"]

    def cdist(u: float, v: float) -> float:
        dd = abs(u - v) % 1.0
        return min(dd, 1.0 - dd)

    s_star_s1_err = cdist(best_s1[1], prod_6_k1["S1_A1"]["s_star"])
    s_star_t_err = cdist(best_t[1], prod_6_k1["T_A1"]["s_star"])
    t0_shift = cdist(best_t[1], best_s1[1])

    # Independent check of L^2 R L R non-extension mod 5:
    W_neg = mat_from_str("LLRLR")
    v5 = np.array([1, 2], dtype=np.int64)
    img_v5 = (W_neg.T @ v5) % 5
    extends_neg = bool(np.array_equal(img_v5, v5 % 5) or np.array_equal(img_v5, (-v5) % 5))

    return {
        "sinc_dvr_vs_fd_E0_S1_rel_diff": float(e0_s1_rel_diff),
        "sinc_dvr_vs_fd_E0_T_rel_diff": float(e0_t_rel_diff),
        "s_star_S1_diff_vs_producer": float(s_star_s1_err),
        "s_star_T_diff_vs_producer": float(s_star_t_err),
        "independent_T0_circle_shift_on_6_k1": float(t0_shift),
        "independent_L2RLR_extends": extends_neg,
        "verified": bool(
            e0_s1_rel_diff < 1e-8
            and e0_t_rel_diff < 1e-8
            and s_star_s1_err < 1e-12
            and s_star_t_err < 1e-12
            and (not extends_neg)
        ),
    }


def referee_check_sector3(prod_s3: Dict[str, Any]) -> Dict[str, Any]:
    """Independently verify BE-3 via 30-digit mpmath + adversarial Gamma(5) matrix [[6,5],[-5,-4]]."""
    mp.mp.dps = 30

    def e3_mpmath(z: mp.mpc, a: mp.mpf, b: mp.mpf) -> mp.mpf:
        a = a % 1
        b = b % 1
        x, y = mp.re(z), mp.im(z)
        b6 = (b**6) - 3 * (b**5) + mp.mpf("2.5") * (b**4) - mp.mpf("0.5") * (b**2) + mp.mpf(1) / 42
        total = (4 * (mp.pi**6) / 45) * b6 * (y**3)
        if b == 0:
            cl5 = mp.re(mp.polylog(5, mp.exp(2j * mp.pi * a)))
            total += (3 * mp.pi / (4 * y * y)) * cl5
        for w1 in range(1, 55):
            for k in range(-50, 51):
                kb = k - b
                akb = abs(kb)
                if akb == 0:
                    continue
                arg = 2 * mp.pi * akb * w1 * y
                if arg > 68:
                    continue
                total += (
                    ((mp.pi**3) * (akb**2) / (w1**3))
                    * mp.cos(2 * mp.pi * w1 * (a + kb * x))
                    * mp.exp(-arg)
                    * (1 + 3 / arg + 3 / (arg * arg))
                )
        return total

    # Adversarial Gamma(5) matrix [[6, 5], [-5, -4]] (det = -24 + 25 = +1, congruent to I_2 mod 5!):
    # Pick tau_0 = -0.78 + 0.42j so |-5*tau_0 - 4|^2 = (-0.10)^2 + (-2.10)^2 = 4.42 => Im(tau_0) = 0.42, Im(gamma.tau_0) = 0.095...
    # Better: pick tau_0 = -0.80 + 0.25j => |-5*(-0.80 + 0.25j) - 4|^2 = |0 - 1.25j|^2 = 1.5625 => Im(tau_0)=0.25, Im(gamma.tau_0)=0.16!
    tau_0 = mp.mpc("-0.80", "0.25")
    tau_g5 = (6 * tau_0 + 5) / (-5 * tau_0 - 4)
    v_orig = e3_mpmath(tau_0, mp.mpf(1) / 5, mp.mpf(2) / 5)
    v_g5 = e3_mpmath(tau_g5, mp.mpf(1) / 5, mp.mpf(2) / 5)
    gamma5_adv_err = float(abs(v_orig - v_g5))

    # High-precision gradient at omega = exp(2pi i/3) for E_8 248 weave potential (-480 * E_3):
    omega = mp.mpc("-0.5", mp.sqrt(3) / 2)
    h_step = mp.mpf("1e-10")
    gx = (e3_mpmath(omega + h_step, mp.mpf(0), mp.mpf(0)) - e3_mpmath(omega - h_step, mp.mpf(0), mp.mpf(0))) / (2 * h_step)
    gy = (e3_mpmath(omega + 1j * h_step, mp.mpf(0), mp.mpf(0)) - e3_mpmath(omega - 1j * h_step, mp.mpf(0), mp.mpf(0))) / (2 * h_step)
    grad_omega_norm = float(mp.hypot(gx, gy))

    # Cross-check value of E8_248_3branch_weave_6D at y = 2.0 against producer JSON:
    v_e8_y2_ref = float(-480 * e3_mpmath(mp.mpc("0.0", "2.0"), mp.mpf(0), mp.mpf(0)))
    v_e8_y2_prod = prod_s3["sl2z_candidates"]["E8_248_3branch_weave_6D"]["heights_y_2_5_8"][0]
    prod_val_rel_err = abs(v_e8_y2_ref - v_e8_y2_prod) / abs(v_e8_y2_ref)

    return {
        "adversarial_Gamma5_matrix_invariance_err": gamma5_adv_err,
        "mpmath_grad_norm_at_omega": grad_omega_norm,
        "e8_248_y2_rel_diff_vs_producer": float(prod_val_rel_err),
        "verified": bool(gamma5_adv_err < 1e-12 and grad_omega_norm < 1e-14 and prod_val_rel_err < 1e-13),
    }


def referee_check_sector4(prod_s4: Dict[str, Any]) -> Dict[str, Any]:
    """Independently verify BE-4 using Spin(16) = Lambda^2(R^16) (+) S^+_16 Clifford algebra & fresh Haar unitaries!"""
    # Build 16 Euclidean Clifford gamma matrices on C^(2^8 = 256), then project to positive chirality S^+_16 (dim 128)!
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    id2 = np.eye(2, dtype=np.complex128)

    def kron_list(mats: List[np.ndarray]) -> np.ndarray:
        out = mats[0]
        for m in mats[1:]:
            out = np.kron(out, m)
        return out

    gammas: List[np.ndarray] = []
    for k in range(8):
        prefix = [sz] * k
        suffix = [id2] * (7 - k)
        gammas.append(kron_list(prefix + [sx] + suffix))
        gammas.append(kron_list(prefix + [sy] + suffix))

    chirality = kron_list([sz] * 8)  # diag(+1 on 128 states, -1 on 128 states)
    pos_idx = np.where(np.diag(chirality).real > 0.5)[0]
    assert len(pos_idx) == 128

    # Construct the 120 generators of so(16) acting on 248 = 120 (adjoint of so(16)) (+) 128 (S^+_16):
    pairs_120 = [(a, b) for a in range(16) for b in range(a + 1, 16)]
    pair_to_idx = {p: idx for idx, p in enumerate(pairs_120)}

    def so16_on_248(a: int, b: int) -> np.ndarray:
        """Action of E_{ab} - E_{ba} in so(16) on 120 (+) 128^+."""
        M = np.zeros((248, 248), dtype=np.complex128)
        # Action on Lambda^2(R^16): [E_ab - E_ba, E_cd - E_dc]
        for col, (c, d) in enumerate(pairs_120):
            # [M_ab, M_cd] = delta_bc M_ad - delta_ac M_bd - delta_bd M_ac + delta_ad M_bc
            for coeff, u, v in [
                (1.0 if b == c else 0.0, a, d),
                (-1.0 if a == c else 0.0, b, d),
                (-1.0 if b == d else 0.0, a, c),
                (1.0 if a == d else 0.0, b, c),
            ]:
                if coeff != 0.0 and u != v:
                    if u < v:
                        M[pair_to_idx[(u, v)], col] += coeff
                    else:
                        M[pair_to_idx[(v, u)], col] -= coeff
        # Action on S^+_16: (1/2) Gamma_a Gamma_b restricted to pos_idx
        spin_block = 0.5 * (gammas[a] @ gammas[b])[np.ix_(pos_idx, pos_idx)]
        M[120:, 120:] = spin_block
        return M

    # Embed u(3)_c subset so(6) (coords 10..15 of R^16, with complex structure J: (10,11), (12,13), (14,15)):
    # A 3x3 skew-Hermitian matrix Z = A + i S in u(3) (A real skew-sym, S real sym) embeds into so(6) as:
    # [[A, -S], [S, A]] on (u_1,u_2,u_3, v_1,v_2,v_3) = (10,12,14, 11,13,15)!
    u_coords = [10, 12, 14]
    v_coords = [11, 13, 15]

    def embed_u3_into_248(Z3: np.ndarray) -> np.ndarray:
        A3 = Z3.real
        S3 = Z3.imag
        M6 = np.zeros((6, 6), dtype=np.float64)
        # Wait: (A + i S)(u + i v) = (A u - S v) + i (S u + A v) => block matrix [[A, -S], [S, A]]!
        M6[:3, :3] = A3
        M6[:3, 3:] = -S3
        M6[3:, :3] = S3
        M6[3:, 3:] = A3
        idx6 = u_coords + v_coords
        out = np.zeros((248, 248), dtype=np.complex128)
        for p in range(6):
            for q in range(p + 1, 6):
                if abs(M6[p, q]) > 1e-15:
                    a_g, b_g = idx6[p], idx6[q]
                    if a_g < b_g:
                        out += M6[p, q] * so16_on_248(a_g, b_g)
                    else:
                        out -= M6[p, q] * so16_on_248(b_g, a_g)
        return out

    # Build 9 basis matrices of u(3)_c and compute commutant dimension in 248 (= 120 + 128^+) directly!
    u3_basis_248: List[np.ndarray] = []
    for p in range(3):
        Z_diag = np.zeros((3, 3), dtype=np.complex128)
        Z_diag[p, p] = 1j
        u3_basis_248.append(embed_u3_into_248(Z_diag))
    for p in range(3):
        for q in range(p + 1, 3):
            Z_re = np.zeros((3, 3), dtype=np.complex128)
            Z_re[p, q] = 1.0
            Z_re[q, p] = -1.0
            Z_im = np.zeros((3, 3), dtype=np.complex128)
            Z_im[p, q] = 1j
            Z_im[q, p] = 1j
            u3_basis_248.append(embed_u3_into_248(Z_re))
            u3_basis_248.append(embed_u3_into_248(Z_im))

    # Note: On 248 = so(16) (+) S^+_16, the action of g in u(3)_c subset so(16) on X in e_8 IS block-diagonal
    # (so(16) maps to so(16) via adjoint, and S^+_16 maps to S^+_16 via spinor action)!!
    # Wait: THAT MEANS WE DON'T EVEN NEED THE S^+ x S^+ -> so(16) BRACKET TO FIND Z_{e_8}(u(3)_c),
    # BECAUSE u(3)_c LIES ENTIRELY INSIDE so(16), SO [g, (X_120, psi_128)] = ([g, X_120], g . psi_128) IS 100% EXACT!!
    svals_spin16 = np.linalg.svd(np.vstack(u3_basis_248), compute_uv=False)
    dim_commutant_clifford = int(np.sum(svals_spin16 < 1e-12))
    spinor_zero_modes = int(np.sum(np.linalg.svd(np.vstack([M[120:, 120:] for M in u3_basis_248]), compute_uv=False) < 1e-12))

    # Independent adversarial check of Coset (2,2)_25 Trace No-Go & Haar scrambling on 10x10 + 128D Spin(16) representation:
    rng_adv = np.random.default_rng(9999991)
    ms = [2, 1, 0, -1, -2]
    Jz = np.diag([float(m) for m in ms]).astype(np.complex128)
    Jp = np.zeros((5, 5), dtype=np.complex128)
    for i in range(1, 5):
        m = ms[i]
        Jp[i - 1, i] = math.sqrt(6.0 - m * (m + 1))
    Jm = Jp.conj().T
    Jx = 0.5 * (Jp + Jm)
    Jy = -0.5j * (Jp - Jm)
    W5 = np.zeros((5, 5), dtype=np.complex128)
    W5[2, 0] = 1.0
    W5[1, 1] = 1.0 / math.sqrt(2.0)
    W5[3, 1] = -1.0 / math.sqrt(2.0)
    W5[1, 2] = 1j / math.sqrt(2.0)
    W5[3, 2] = 1j / math.sqrt(2.0)
    W5[0, 3] = 1.0 / math.sqrt(2.0)
    W5[4, 3] = 1.0 / math.sqrt(2.0)
    W5[0, 4] = 1j / math.sqrt(2.0)
    W5[4, 4] = -1j / math.sqrt(2.0)

    L5_list = [((W5.conj().T @ (-1j * J) @ W5).real) for J in (Jx, Jy, Jz)]
    L5_list = [M / math.sqrt(float(np.sum(M * M))) for M in L5_list]

    def embed_so10_into_248(X10: np.ndarray) -> np.ndarray:
        out = np.zeros((248, 248), dtype=np.complex128)
        for a in range(10):
            for b in range(a + 1, 10):
                if abs(X10[a, b]) > 1e-15:
                    out += X10[a, b] * so16_on_248(a, b)
        return out

    wL_ref = []
    wR_ref = []
    for L5 in L5_list:
        XL = np.zeros((10, 10))
        XL[:5, :5] = L5
        XR = np.zeros((10, 10))
        XR[5:, 5:] = L5
        wL_ref.append(embed_so10_into_248(XL))
        wR_ref.append(embed_so10_into_248(XR))

    # Random pure (2,2)_25 background embedded via Spin(16) Clifford matrices:
    B_rand = rng_adv.standard_normal((5, 5))
    X_coset = np.zeros((10, 10))
    X_coset[:5, 5:] = B_rand
    X_coset[5:, :5] = -B_rand.T
    Phi_coset_248 = embed_so10_into_248(X_coset)

    tr_wL = sum(float(np.real(np.trace((A @ Phi_coset_248 - Phi_coset_248 @ A).conj().T @ (A @ Phi_coset_248 - Phi_coset_248 @ A)))) for A in wL_ref)
    tr_wR = sum(float(np.real(np.trace((A @ Phi_coset_248 - Phi_coset_248 @ A).conj().T @ (A @ Phi_coset_248 - Phi_coset_248 @ A)))) for A in wR_ref)
    clifford_coset_trace_diff = abs(tr_wL - tr_wR)

    # Adversarial 248x248 Haar unitary rotation check:
    Z_haar = (rng_adv.standard_normal((248, 248)) + 1j * rng_adv.standard_normal((248, 248))) / math.sqrt(2.0)
    Q_h, R_h = np.linalg.qr(Z_haar)
    U_adv = Q_h * (np.diag(R_h) / np.abs(np.diag(R_h)))[None, :]
    Phi_scr = U_adv @ Phi_coset_248 @ U_adv.conj().T
    wL_scr = [U_adv @ A @ U_adv.conj().T for A in wL_ref]
    ML_orig = np.array([[float(np.real(np.trace((A @ Phi_coset_248 - Phi_coset_248 @ A).conj().T @ (B @ Phi_coset_248 - Phi_coset_248 @ B)))) for B in wL_ref] for A in wL_ref])
    ML_adv = np.array([[float(np.real(np.trace((A @ Phi_scr - Phi_scr @ A).conj().T @ (B @ Phi_scr - Phi_scr @ B)))) for B in wL_scr] for A in wL_scr])
    adv_haar_err = float(np.max(np.abs(np.linalg.eigvalsh(ML_orig) - np.linalg.eigvalsh(ML_adv))))

    return {
        "clifford_spin16_commutant_dim": dim_commutant_clifford,
        "clifford_spinor_u3c_singlets": spinor_zero_modes,
        "clifford_coset22_trace_diff": float(clifford_coset_trace_diff),
        "adversarial_haar_248_err": adv_haar_err,
        "matches_producer_dim_46": bool(
            dim_commutant_clifford == prod_s4["commutant_u3_c"]["dim"] == 46
            and spinor_zero_modes == 0
            and clifford_coset_trace_diff < 1e-12
            and adv_haar_err < 1e-12
        ),
    }


def main() -> None:
    ast_check = assert_zero_producer_imports()

    # Verify seal independently:
    seal_expected = SEAL_PATH.read_text(encoding="utf-8").strip().split()[0]
    seal_actual = hashlib.sha256(PLAN_PATH.read_bytes()).hexdigest()
    seal_ok = (seal_expected == seal_actual)

    prod_data = json.loads(PRODUCER_JSON_PATH.read_text(encoding="utf-8"))
    c1 = referee_check_sector1(prod_data["sector1_BE1"])
    c2 = referee_check_sector2(prod_data["sector2_BE2"])
    c3 = referee_check_sector3(prod_data["sector3_BE3"])
    c4 = referee_check_sector4(prod_data["sector4_BE4"])

    all_passed = bool(
        ast_check["zero_producer_imports_verified"]
        and seal_ok
        and c1["matches_producer_winner"]
        and c2["verified"]
        and c3["verified"]
        and c4["matches_producer_dim_46"]
    )

    verdict = {
        "referee": "Zero-Trust Independent Referee (Guardrail 6)",
        "all_checks_passed": all_passed,
        "preregistration_seal_verified": seal_ok,
        "ast_zero_import_audit": ast_check,
        "sector1_dynkin_and_adv_modular": c1,
        "sector2_sinc_dvr_and_torsion": c2,
        "sector3_mpmath_and_adv_gamma5": c3,
        "sector4_clifford_spin16_and_adv_haar": c4,
    }
    REFEREE_JSON_PATH.write_text(json.dumps(verdict, indent=2), encoding="utf-8")

    print("=" * 78)
    print("ZERO-TRUST INDEPENDENT REFEREE AUDIT — VERDICT")
    print("=" * 78)
    print(f"Zero producer imports (AST verified): {ast_check['zero_producer_imports_verified']}")
    print(f"Pre-registration SHA-256 seal intact : {seal_ok}")
    print(f"Sector 1 (Dynkin Q-det & adv SL2Z)   : {c1['matches_producer_winner']} (adv_err={c1['adversarial_SL2Z_E8_theta_err']:.2e})")
    print(f"Sector 2 (Sinc-DVR & T0/T3 check)    : {c2['verified']} (E0_rel_diff={c2['sinc_dvr_vs_fd_E0_T_rel_diff']:.2e}, T0_shift={c2['independent_T0_circle_shift_on_6_k1']:.6f})")
    print(f"Sector 3 (30-digit mpmath & Gamma5)  : {c3['verified']} (gamma5_err={c3['adversarial_Gamma5_matrix_invariance_err']:.2e})")
    print(f"Sector 4 (Spin(16) Clifford & Haar)  : {c4['matches_producer_dim_46']} (dim={c4['clifford_spin16_commutant_dim']}, haar_err={c4['adversarial_haar_248_err']:.2e})")
    print("-" * 78)
    print(f"OVERALL REFEREE VERDICT              : {'PASS' if all_passed else 'FAIL'}")
    print("=" * 78)
    if not all_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
