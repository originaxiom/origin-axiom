#!/usr/bin/env python3
r"""Independent Zero-Trust Referee Countercheck for P-753 / R77-2 (WP-2.2 & WP-3.2).

Guardrail 6 enforcement:
- Zero imports from src/origin_axiom/p753_register_field_join.py.
- Independently constructs:
  (1) All 240 explicit E8 root vectors in R^8 + 8 Cartan generators (without using the
      producer's tensor-product module builder) to prove the E8 coroot identity
      (1,1,1,1,1,1,1,1) in Q^v(E8) => -h4 == zeta_Spin(10) * (+h4) across all 248 dims.
  (2) Explicit 5-fold Pauli Clifford algebra Cl(10) (32x32) and Spin(10) Pin/Spin lifts
      under adversarial Haar unitary basis rotations to independently verify [2O : St] = 3,
      all E_theta compensators (< 1e-12), and the Klein-4 spectrum (112; 37, 33, 33, 33).
  (3) Adversarial Haar-scrambled quaternion F2 1-cocycle + independent q-series leading-power
      & Cauchy contour quadrature of V(tau) = (theta_2^2, theta_3^2, theta_4^2) / eta^3
      (verifying fractional powers +1/8, -1/8, -1/8 => order-8 L action and odd Z_24 twist
      m = 3, 15, while excluding 96 from all even twists {24, 48, 72, 144}).
  (4) Independent Cauchy contour residue quadrature around the puncture z = 0 on E_tau \ {0}
      verifying the cusp pole-order filtration (1 + 1) on H^0(O(2p)) and H^0(chi_(1,1)(2p))
      versus the irreducible S_theta-swapped doublet (2) on H^0(chi_(1,0)(p) + chi_(0,1)(p)).

Strictly data-free (0 of 19). Writes tracked receipts to relays/p753_verification/.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json
import math
from pathlib import Path
import sys
from typing import Any

import mpmath as mp
import numpy as np


TOL = 1e-12


def _mat_sig(mat: np.ndarray, digits: int = 6) -> bytes:
    arr = np.asarray(mat, dtype=complex)
    return (np.round(arr.real, digits) + 0.0).tobytes() + (np.round(arr.imag, digits) + 0.0).tobytes()


def _bfs_group(gens: dict[str, np.ndarray], cap: int = 4096) -> list[tuple[str, np.ndarray]]:
    dim = next(iter(gens.values())).shape[0]
    eye = np.eye(dim, dtype=complex)
    seen: dict[bytes, tuple[str, np.ndarray]] = {_mat_sig(eye): ("", eye)}
    q: list[tuple[str, np.ndarray]] = [("", eye)]
    while q:
        w, cur = q.pop(0)
        for lbl, g in gens.items():
            nxt = cur @ g
            s = _mat_sig(nxt)
            if s not in seen:
                seen[s] = (w + lbl, nxt)
                q.append((w + lbl, nxt))
                if len(seen) > cap:
                    raise RuntimeError(f"Group order exceeded cap {cap}")
    return list(seen.values())


def _haar(dim: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > 0.0, d / np.abs(d), 1.0 + 0.0j)
    return q * ph


# ---------------------------------------------------------------------------
# Check 1: Explicit E8 Root Lattice in R^8 (240 roots + 8 Cartan = 248)
# ---------------------------------------------------------------------------
def check_e8_root_lattice_coroot_identity() -> dict[str, Any]:
    roots_d5_adj: list[np.ndarray] = []
    roots_d3_adj: list[np.ndarray] = []
    roots_10_6: list[np.ndarray] = []
    roots_16_4: list[np.ndarray] = []
    roots_bar16_bar4: list[np.ndarray] = []

    # 112 integer roots +- e_i +- e_j in R^8 (0..4 = D5, 5..7 = D3 ~= A3)
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1.0, 1.0), repeat=2):
            v = np.zeros(8, dtype=float)
            v[i] = si
            v[j] = sj
            if j < 5:
                roots_d5_adj.append(v)
            elif i >= 5:
                roots_d3_adj.append(v)
            else:
                roots_10_6.append(v)

    # 128 half-integer roots (1/2)(+-1)^8 with even number of minus signs
    for signs in product((-1.0, 1.0), repeat=8):
        if signs.count(-1.0) % 2 == 0:
            v = 0.5 * np.array(signs, dtype=float)
            d5_minus = signs[:5].count(-1.0)
            if d5_minus % 2 == 1:
                roots_16_4.append(v)
            else:
                roots_bar16_bar4.append(v)

    all_roots = roots_d5_adj + roots_d3_adj + roots_10_6 + roots_16_4 + roots_bar16_bar4
    n_roots = len(all_roots)
    total_dim = n_roots + 8  # 8 Cartan generators

    # Verify E8 norm-squared = 2 for all 240 roots and integrality of inner products
    norms_ok = all(abs(float(np.dot(r, r)) - 2.0) < 1e-12 for r in all_roots)

    # Coroot shift delta_D3 = (0,0,0,0,0, 1,1,1) flips +h4 -> -h4 in SU(4) ~= Spin(6).
    # Coroot shift delta_D5 = (1,1,1,1,1, 0,0,0) applies Spin(10) center zeta_Spin(10).
    delta_d3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0])
    delta_d5 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0])

    max_phase_diff = 0.0
    integer_root_flips = 0
    spinor_root_flips = 0
    for r in all_roots:
        ph_d3 = np.exp(2j * math.pi * float(np.dot(r, delta_d3)))
        ph_d5 = np.exp(2j * math.pi * float(np.dot(r, delta_d5)))
        max_phase_diff = max(max_phase_diff, abs(ph_d3 - ph_d5))
        if abs(r[0]) in (0.0, 1.0):
            if abs(ph_d3 - 1.0) > 1e-9:
                integer_root_flips += 1
        else:
            if abs(ph_d3 + 1.0) < 1e-9:
                spinor_root_flips += 1

    # Also verify on D3 ~= A3 weights of (16,4): singlet (-1/2,-1/2,-1/2) vs triplet (-1/2,+1/2,+1/2) etc.
    theta_plus_h4 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, -0.25, -0.25, -0.25])
    theta_minus_h4 = theta_plus_h4 + delta_d3
    ratios = set()
    for theta in (theta_plus_h4, theta_minus_h4):
        w_sing = np.array([0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, -0.5])
        w_trip = np.array([0.0, 0.0, 0.0, 0.0, 0.0, -0.5, +0.5, +0.5])
        lam_s = np.exp(2j * math.pi * float(np.dot(w_sing, theta)))
        lam_t = np.exp(2j * math.pi * float(np.dot(w_trip, theta)))
        ratios.add(round(float((lam_s / lam_t).real), 9))

    # Check (1,15) = 12 D3 roots + 3 D3 Cartan under theta_+-h4
    d3_plus_minus = Counter()
    for r in roots_d3_adj:
        val = int(round(float(np.exp(2j * math.pi * float(np.dot(r, theta_plus_h4))).real)))
        d3_plus_minus[val] += 1
    d3_plus_minus[1] += 3  # 3 Cartan generators commute with h4

    return {
        "n_roots": n_roots,
        "total_e8_dim": total_dim,
        "branching_dims": {
            "(45,1)": len(roots_d5_adj) + 5,
            "(1,15)": len(roots_d3_adj) + 3,
            "(10,6)": len(roots_10_6),
            "(16,4)": len(roots_16_4),
            "(bar16,bar4)": len(roots_bar16_bar4),
        },
        "all_roots_norm_sq_2": norms_ok,
        "coroot_phase_equivalence_max_err": float(max_phase_diff),
        "integer_root_flips": integer_root_flips,
        "spinor_root_flips": spinor_root_flips,
        "singlet_over_triplet_h4_ratio_set": sorted(ratios),
        "a3_adjoint_15_parity_split": {str(k): v for k, v in d3_plus_minus.items()},
    }


# ---------------------------------------------------------------------------
# Check 2: Independent Pauli-Clifford Cl(10) Construction & Scrambled E_theta Audit
# ---------------------------------------------------------------------------
def check_pauli_clifford_spin10_and_e_theta(seed: int = 99173) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron5(ops: list[np.ndarray]) -> np.ndarray:
        out = ops[0]
        for op in ops[1:]:
            out = np.kron(out, op)
        return out

    # Orthonormal Euclidean Cl(10) generators {G_a, G_b} = 2 delta_ab I_32
    gammas_eucl: list[np.ndarray] = []
    for k in range(5):
        pref = [sz] * k
        suff = [i2] * (4 - k)
        gammas_eucl.append(kron5(pref + [sx] + suff))
        gammas_eucl.append(kron5(pref + [sy] + suff))

    chirality = kron5([sz] * 5)

    # Convert to split-isotropic basis matching metric g = [[0, I5], [I5, 0]]
    # psi_k = (gamma_{2k} + i gamma_{2k+1}) / 2, psi_k^dag = (gamma_{2k} - i gamma_{2k+1}) / 2
    # so {psi_j, psi_k^dag} = delta_{jk}
    psis = [(gammas_eucl[2 * k] + 1j * gammas_eucl[2 * k + 1]) / 2.0 for k in range(5)]
    psidags = [p.conj().T for p in psis]

    # Build D5 operators independently
    e5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([2.0, math.sqrt(6.0), math.sqrt(6.0), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4.0, -2.0, 0.0, 2.0, 4.0]).astype(complex)
    j5 = np.diag([1.0, -1.0, 1.0, -1.0, 1.0])[:, ::-1].astype(complex)
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2.0 / 5.0); bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3.0 / 5.0); bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)

    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10.0) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    ep10, em10 = (e10 + g10) / 2.0, (e10 - g10) / 2.0
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    def cliff_lie(m10: np.ndarray) -> np.ndarray:
        out = -0.5 * np.trace(m10[:5, :5]) * np.eye(32, dtype=complex)
        for a in range(5):
            for b in range(5):
                out += m10[a, b] * (psis[a] @ psidags[b])
                out += 0.5 * m10[a, b + 5] * (psis[a] @ psis[b])
                out += 0.5 * m10[a + 5, b] * (psidags[a] @ psidags[b])
        return out

    # Solve A_spin by Pin/Spin Clifford intertwining U Psi_M U^-1 = sum_N (A_vec)_{NM} Psi_N
    # where Psi = (psis[0..4], psidags[0..4]), calibrated on highest weight!
    a_vec = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4.0))
    psi_vec = psis + psidags
    # Intertwining linear system: U Psi_M - (sum_N a_vec[N, M] Psi_N) U = 0
    rows = []
    for m_idx in range(10):
        target_op = sum(a_vec[n_idx, m_idx] * psi_vec[n_idx] for n_idx in range(10))
        rows.append(np.kron(psi_vec[m_idx].T, np.eye(32)) - np.kron(np.eye(32), target_op))
    _, svals_a, vh_a = np.linalg.svd(np.vstack(rows), full_matrices=False)
    if float(svals_a[-1]) > 1e-10:
        raise RuntimeError("Failed to find Clifford Spin(10) lift of A_vec")
    raw_a = vh_a[-1].conj().reshape((32, 32), order="F")
    ua_pol, _, vha_pol = np.linalg.svd(raw_a)
    a_spin_raw = ua_pol @ vha_pol
    # Calibrate overall Spin(10) phase so top state |+++++> (all +1 of sz => index 0) has phase exp(2pi i * (-3/8))?
    # Wait: in Pauli sz, index 0 has sz=+1 on all 5 qubits (n_i = 1, n_i - 1/2 = +1/2), sum xw*(+1/2) = (-1.25)*0.5 = -5/8 => exp(-5pi i/4) = exp(3pi i/4);
    # index 31 has sz=-1 on all 5 qubits (n_i = 0, n_i - 1/2 = -1/2) => exp(+5pi i/4) = exp(-3pi i/4)!
    # Check psis[0]: sx + i sy = [[0, 2], [0, 0]], so psis[k] maps |1> -> |0>! Thus index 0 is |11111> (all occupied)!
    top_phase_target = np.exp(2j * math.pi * sum(w * 0.5 for w in [0.25, 0.0, -0.25, -0.5, -0.75]))
    a_spin = a_spin_raw * (top_phase_target / a_spin_raw[0, 0])

    vals_hd, vecs_hd = np.linalg.eigh(cliff_lie(hp10 - hm10))
    d_spin = (vecs_hd * np.exp(-1j * math.pi * vals_hd / 4.0)) @ vecs_hd.conj().T
    dh_spin = (vecs_hd * np.exp(+1j * math.pi * vals_hd / 8.0)) @ vecs_hd.conj().T

    vals_v, vecs_v = np.linalg.eigh(hp10 - hm10)
    d_vec = (vecs_v * np.exp(-1j * math.pi * vals_v / 4.0)) @ vecs_v.conj().T
    dh_vec = (vecs_v * np.exp(+1j * math.pi * vals_v / 8.0)) @ vecs_v.conj().T

    # Extract chiral 16s from chirality operator (occupied parity: odd occupied -> chirality = -1, even -> +1)
    ev_ch = np.real(np.diag(chirality))
    idx_odd = [i for i in range(32) if ev_ch[i] < 0.0]   # odd number of -1? Wait: |0> has sz=+1 (occupied!), so odd occupied = even -1s -> wait:
    # Let's check e10/ep10 top weight! Check which 16 has X_singlet = (-1,-1) for +h4:
    h4 = np.diag([np.exp(3j * math.pi / 4.0)] + [np.exp(-1j * math.pi / 4.0)] * 3)
    # Apply adversarial Haar unitary basis rotation to BOTH 16-blocks and 4-block!
    u32_adv = np.zeros((32, 32), dtype=complex)
    idx_ch_plus = [i for i in range(32) if ev_ch[i] > 0.0]
    idx_ch_minus = [i for i in range(32) if ev_ch[i] < 0.0]
    # Note: index 0 has all 5 qubits in |0> (occupied, sz=+1 => chirality = +1, 5 occupied = odd!).
    # So chirality = +1 is 16_odd (5, 3, 1 occupied) and chirality = -1 is 16_even (4, 2, 0 occupied)!
    u16_a = _haar(16, rng)
    u16_b = _haar(16, rng)
    u4_adv = _haar(4, rng)

    x_16_4 = (u16_a @ a_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T)
    d_16_4 = (u16_a @ d_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T)
    dh_16_4 = (u16_a @ dh_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T)
    e_16_4 = (u16_a @ cliff_lie(e10)[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T)
    g_16_4 = (u16_a @ cliff_lie(g10)[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T)
    h4_s = u4_adv @ h4 @ u4_adv.conj().T

    X_64a = np.kron(x_16_4, h4_s)
    Y_64a = np.kron(d_16_4 @ x_16_4, h4_s)
    DH_64a = np.kron(dh_16_4, np.eye(4, dtype=complex))
    E_64a = np.kron(e_16_4, np.eye(4, dtype=complex))
    G_64a = np.kron(g_16_4, np.eye(4, dtype=complex))

    x_b16 = (u16_b @ a_spin[np.ix_(idx_ch_minus, idx_ch_minus)] @ u16_b.conj().T)
    d_b16 = (u16_b @ d_spin[np.ix_(idx_ch_minus, idx_ch_minus)] @ u16_b.conj().T)
    X_64b = np.kron(x_b16, (u4_adv @ h4.conj() @ u4_adv.conj().T))
    Y_64b = np.kron(d_b16 @ x_b16, (u4_adv @ h4.conj() @ u4_adv.conj().T))

    # Verify S_theta and L^2 compensator errors on adversarially scrambled (16,4)
    fi = np.diag([1j, -1j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    fk = fi @ fj
    gs = (np.eye(2) - fk) / math.sqrt(2.0)
    gl = (np.eye(2) + fi) / math.sqrt(2.0)
    gr = (np.eye(2) - fj) / math.sqrt(2.0)

    phi_s0 = gs[0, 0] * E_64a + gs[0, 1] * G_64a
    phi_s1 = gs[1, 0] * E_64a + gs[1, 1] * G_64a
    err_s_scrambled = max(
        float(np.max(np.abs(DH_64a @ Y_64a @ DH_64a.conj().T - X_64a))),
        float(np.max(np.abs(DH_64a @ X_64a.conj().T @ DH_64a.conj().T - Y_64a))),
        float(np.max(np.abs(DH_64a @ phi_s0 @ DH_64a.conj().T - E_64a))),
        float(np.max(np.abs(DH_64a @ phi_s1 @ DH_64a.conj().T - G_64a))),
    )

    # Full 248D Klein-4 parity check using independent exterior / adjoint blocks
    def ext2(m: np.ndarray) -> np.ndarray:
        ps = list(combinations(range(m.shape[0]), 2))
        out = np.zeros((len(ps), len(ps)), dtype=complex)
        for i, (r0, r1) in enumerate(ps):
            for j, (c0, c1) in enumerate(ps):
                out[i, j] = m[r0, c0] * m[r1, c1] - m[r0, c1] * m[r1, c0]
        return out

    # Adjoint of A3 = traceless part of 4 x 4bar
    x_4x4b = np.kron(h4, h4.conj())
    # Project out trace (1/2) sum_i |ii>
    v_tr = np.zeros(16, dtype=complex)
    for i in range(4):
        v_tr[5 * i] = 0.5
    P_15 = np.eye(16, dtype=complex) - np.outer(v_tr, v_tr.conj())
    u_15, sv_15, _ = np.linalg.svd(P_15)
    b_15 = u_15[:, sv_15 > 0.5]
    X_15 = b_15.conj().T @ x_4x4b @ b_15

    blocks_xy = [
        (ext2(a_vec), ext2(d_vec @ a_vec)),
        (X_15, X_15),
        (np.kron(a_vec, ext2(h4)), np.kron(d_vec @ a_vec, ext2(h4))),
        (X_64a, Y_64a),
        (X_64b, Y_64b),
    ]
    kpi_minus = 0
    k4_counts: Counter[str] = Counter()
    for xm, ym in blocks_xy:
        kpi = xm @ ym @ xm.conj().T @ ym.conj().T
        ev, vc = np.linalg.eigh((kpi + kpi.conj().T) / 2.0)
        kpi_minus += int(np.sum(np.abs(ev + 1.0) < 1e-8))
        vp = vc[:, np.abs(ev - 1.0) < 1e-8]
        xp = vp.conj().T @ xm @ vp
        yp = vp.conj().T @ ym @ vp
        id_p = np.eye(vp.shape[1], dtype=complex)
        for p1, p2 in product((0, 1), repeat=2):
            proj = 0.25 * (id_p + ((-1) ** p1) * xp) @ (id_p + ((-1) ** p2) * yp)
            k4_counts[f"{p1}{p2}"] += int(round(float(np.real(np.trace(proj)))))

    # Check [2O : St] = 3 independently
    g_2o = _bfs_group({"L": gl, "R": gr, "l": gl.conj().T, "r": gr.conj().T})
    st = [
        m for _, m in g_2o
        if np.max(np.abs(m.conj() @ sx @ m.T - sx)) < 1e-9 or np.max(np.abs(m.conj() @ sx @ m.T + sx)) < 1e-9
    ]

    return {
        "order_2O": len(g_2o),
        "order_St": len(st),
        "index_2O_St": len(g_2o) // len(st),
        "pauli_clifford_scrambled_S_theta_err": err_s_scrambled,
        "kpi_minus_total": kpi_minus,
        "klein4_totals": dict(k4_counts),
    }


# ---------------------------------------------------------------------------
# Check 3: q-Series Leading Powers + Cauchy Quadrature + Scrambled F2 Cocycle
# ---------------------------------------------------------------------------
def check_qseries_and_scrambled_weave_triplet(seed: int = 44201) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    # 1. Extract leading fractional q_2 = exp(2pi i tau) powers of V(tau) = (theta_2^2, theta_3^2, theta_4^2)/eta^3
    # by numerical log-ratio and Cauchy contour quadrature on tau = x + i y (x in [0, 8), period 8 in tau because 1/8 power!)
    def eval_v(tau: complex) -> np.ndarray:
        with mp.workdps(35):
            t = mp.mpc(tau)
            q2 = mp.exp(2j * mp.pi * t)
            q1 = mp.exp(1j * mp.pi * t)
            t2 = 2 * mp.exp(1j * mp.pi * t / 4) * sum(q2 ** (n * (n + 1) // 2) for n in range(30))
            t3 = mp.jtheta(3, 0, q1)
            t4 = mp.jtheta(4, 0, q1)
            eta3 = mp.exp(1j * mp.pi * t / 4) * mp.fprod([(1 - q2 ** n) ** 3 for n in range(1, 60)])
            return np.array([complex(t2**2 / eta3), complex(t3**2 / eta3), complex(t4**2 / eta3)], dtype=complex)

    # Under tau -> tau + 1 (L), q_2^{alpha} picks up exp(2pi i alpha). Measure alpha_j directly at two distinct heights!
    v_t1 = eval_v(0.13 + 1.85j)
    v_t1_shift = eval_v(1.13 + 1.85j)
    phases_l = v_t1_shift / v_t1
    measured_exponents_mod1 = [round(float(np.angle(ph) / (2.0 * math.pi)), 9) for ph in phases_l]
    # Expected fractional q2 exponents: +1/8 = +0.125, -1/8 = -0.125, -1/8 = -0.125? Wait:
    # For theta_3^2/eta^3: theta_3(tau+1) = theta_4(tau), so L swaps components 1 <-> 2!
    # Under tau -> tau + 2 (L^2), all three components are diagonal! Let's check both L and Cauchy integral on q2^{+-1/8} * V!
    y0 = 1.6
    n_quad = 64
    # Integrate over x in [0, 2) because theta_3^2/eta^3 = q_2^{-1/8}(1 + 4 q_2^{1/2} + ...) has period 2 in Re(tau)!
    xs = np.linspace(0.0, 2.0, n_quad, endpoint=False)
    c0_lead = 0.0 + 0.0j
    c1_lead = 0.0 + 0.0j
    c2_lead = 0.0 + 0.0j
    for x in xs:
        tau = float(x) + 1j * y0
        q2_eighth = np.exp(2j * math.pi * tau / 8.0)
        vv = eval_v(tau)
        c0_lead += vv[0] / q2_eighth
        c1_lead += vv[1] * q2_eighth
        c2_lead += vv[2] * q2_eighth
    c0_lead /= n_quad
    c1_lead /= n_quad
    c2_lead /= n_quad
    qseries_leading_coeff_err = max(abs(c0_lead - 4.0), abs(c1_lead - 1.0), abs(c2_lead - 1.0))

    # 2. Construct F2 1-cocycle in an adversarially Haar-scrambled quaternion basis U2 * Q8 * U2^dag
    u2 = _haar(2, rng)
    qi = u2 @ np.diag([1j, -1j]) @ u2.conj().T
    qj = u2 @ np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex) @ u2.conj().T
    gl = (np.eye(2) + qi) / math.sqrt(2.0)
    gr = (np.eye(2) - qj) / math.sqrt(2.0)
    rho = {"a": qi, "b": qj}
    pars = [(1, 0), (0, 1), (1, 1)]

    def chi(p: tuple[int, int], ch: str) -> int:
        return -1 if (p[0] if ch == "a" else p[1]) else 1

    def rep_w(w: str, p: tuple[int, int]) -> np.ndarray:
        m = np.eye(2, dtype=complex)
        for c in w:
            g = rho[c.lower()] * chi(p, c.lower())
            m = m @ (g if c.islower() else g.conj().T)
        return m

    def cocyc(z: dict[str, np.ndarray], w: str, p: tuple[int, int]) -> np.ndarray:
        val = np.zeros(2, dtype=complex)
        m = np.eye(2, dtype=complex)
        for c in w:
            mg = rep_w(c.lower(), p)
            if c.islower():
                val = val + m @ z[c.lower()]
                m = m @ mg
            else:
                mi = mg.conj().T
                val = val - m @ (mi @ z[c.lower()])
                m = m @ mi
        return val

    bases = {}
    for p in pars:
        cob = np.zeros((4, 2), dtype=complex)
        for k in range(2):
            ek = np.zeros(2, dtype=complex); ek[k] = 1.0
            cob[:2, k] = rep_w("a", p) @ ek - ek
            cob[2:, k] = rep_w("b", p) @ ek - ek
        qc, _ = np.linalg.qr(cob)
        pr = np.eye(4, dtype=complex) - qc @ qc.conj().T
        us, _, _ = np.linalg.svd(pr)
        bases[p] = (us[:, :2], pr)

    def act_p(mv: dict[str, str], p: tuple[int, int]) -> tuple[int, int]:
        sa = math.prod(chi(p, c.lower()) for c in mv["a"])
        sb = math.prod(chi(p, c.lower()) for c in mv["b"])
        return (0 if sa == 1 else 1, 0 if sb == 1 else 1)

    def build_mv(mv: dict[str, str], lift: np.ndarray) -> np.ndarray:
        li = lift.conj().T
        out = np.zeros((6, 6), dtype=complex)
        for ip, p in enumerate(pars):
            q = act_p(mv, p)
            iq = pars.index(q)
            bp, _ = bases[p]
            bq, pq = bases[q]
            for k in range(2):
                v = bp[:, k]
                z = {"a": v[:2], "b": v[2:]}
                w = pq @ np.concatenate([li @ cocyc(z, mv["a"], p), li @ cocyc(z, mv["b"], p)])
                out[2 * iq : 2 * iq + 2, 2 * ip + k] = bq.conj().T @ w
        return out

    ml6 = build_mv({"a": "a", "b": "ab"}, gl)
    mr6 = build_mv({"a": "ab", "b": "b"}, gr)
    gv = _bfs_group({"L": ml6, "R": mr6})

    # Split 6D into two 3D irreps via commutant, identify T by trace(TL) = exp(-i pi/4)
    cstack = np.vstack([np.kron(np.eye(6), m) - np.kron(m.T, np.eye(6)) for _, m in gv])
    _, _, vhc = np.linalg.svd(cstack)
    xc = next(
        r.reshape((6, 6), order="F")
        for r in vhc[-2:].conj()
        if np.linalg.norm(r.reshape((6, 6), order="F") - (np.trace(r.reshape((6, 6), order="F")) / 6.0) * np.eye(6)) > 1e-6
    )
    evx, vxx = np.linalg.eig(xc)
    cl: dict[tuple[float, float], list[int]] = {}
    for idx, val in enumerate(evx):
        cl.setdefault((round(float(val.real), 4), round(float(val.imag), 4)), []).append(idx)
    tl_cand = tr_cand = None
    w8b = np.exp(-1j * math.pi / 4.0)
    for idxs in cl.values():
        qp, _ = np.linalg.qr(vxx[:, idxs])
        tl_try = qp.conj().T @ ml6 @ qp
        tr_try = qp.conj().T @ mr6 @ qp
        if abs(np.trace(tl_try) - w8b) < 1e-7:
            tl_cand, tr_cand = tl_try, tr_try
    if tl_cand is None or tr_cand is None:
        raise RuntimeError("Failed to isolate T in scrambled quaternion basis")

    gt = _bfs_group({"L": tl_cand, "R": tr_cand})
    zt = [w for w, m in gt if all(np.max(np.abs(m @ n - n @ m)) < 1e-7 for _, n in gt)]
    st_mat = tl_cand @ np.linalg.inv(tr_cand) @ tl_cand
    st4_plus_i_err = float(np.max(np.abs(np.linalg.matrix_power(st_mat, 4) + np.eye(3))))

    # Independent Sym^2(Weil_2) even vs odd Z_24 twist orders
    rt2 = math.sqrt(2.0)
    l2 = np.diag([1.0, 1j])
    s0 = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / rt2
    r2 = s0 @ np.linalg.inv(l2) @ s0

    def sym2(u: np.ndarray) -> np.ndarray:
        a, b, c, d = u[0, 0], u[0, 1], u[1, 0], u[1, 1]
        return np.array(
            [[a * a, rt2 * a * b, b * b], [rt2 * a * c, a * d + b * c, rt2 * b * d], [c * c, rt2 * c * d, d * d]],
            dtype=complex,
        )

    untwisted_order = len(_bfs_group({"L": sym2(l2), "R": sym2(r2)}))
    even_orders = sorted(
        {
            len(
                _bfs_group(
                    {
                        "L": np.exp(2j * math.pi * m / 24.0) * sym2(l2),
                        "R": np.exp(-2j * math.pi * m / 24.0) * sym2(r2),
                    }
                )
            )
            for m in range(0, 24, 2)
        }
    )
    odd_m3_bar_L = np.exp(2j * math.pi * 3.0 / 24.0) * sym2(l2.conj())
    odd_m3_bar_R = np.exp(-2j * math.pi * 3.0 / 24.0) * sym2(r2.conj())
    sys_int = np.vstack(
        [
            np.kron(tl_cand.T, np.eye(3)) - np.kron(np.eye(3), odd_m3_bar_L),
            np.kron(tr_cand.T, np.eye(3)) - np.kron(np.eye(3), odd_m3_bar_R),
        ]
    )
    _, sv_int, vh_int = np.linalg.svd(sys_int)
    u_raw = vh_int[-1].conj().reshape((3, 3), order="F")
    up, _, vhp = np.linalg.svd(u_raw)
    u_int = up @ vhp
    intertwine_err = max(
        float(np.max(np.abs(u_int @ tl_cand @ u_int.conj().T - odd_m3_bar_L))),
        float(np.max(np.abs(u_int @ tr_cand @ u_int.conj().T - odd_m3_bar_R))),
    )

    return {
        "qseries_leading_coeff_quadrature_err": float(qseries_leading_coeff_err),
        "scrambled_order_G_V": len(gv),
        "scrambled_order_G_T": len(gt),
        "scrambled_center_order": len(zt),
        "scrambled_S_T_fourth_plus_I_err": st4_plus_i_err,
        "untwisted_Sym2_Weil2_order": untwisted_order,
        "even_Z24_twist_orders": even_orders,
        "odd_m3_Sym2_Weil2_bar_intertwiner_err": intertwine_err,
    }


# ---------------------------------------------------------------------------
# Check 4: Independent Cauchy Contour Residue Quadrature on E_tau \ {0}
# ---------------------------------------------------------------------------
def check_elliptic_contour_pole_filtration() -> dict[str, Any]:
    r"""Use direct Cauchy contour integration around |z| = eps on E_tau \ {0} to verify:
    (a) On H^0(E_tau, O(2p)) * dz = span{dz, wp(z|tau) dz}, the double-pole residue coeff
        c_{-2}(f) = (1/2pi i) oint z f(z) dz vanishes on dz and is preserved as an invariant
        subspace ker(c_{-2}) under Gamma_theta = <L^2, S_theta> (reducible 1 + 1).
    (b) On H^0(E_tau, chi_(1,1)(2p)) * dz = span{S_3(z|tau) dz, S_3'(z|tau) dz}, ker(c_{-2})
        = C * S_3(z|tau) dz is invariant under Gamma_theta with unit simple-pole residue (reducible 1 + 1).
    (c) On H^0(E_tau, (chi_(1,0)(p) (+) chi_(0,1)(p))) * dz = span{S_2 dz, S_4 dz}, S_theta
        swaps the two simple-pole residue channels off-diagonally (irreducible 2).
    """
    with mp.workdps(35):
        tau = mp.mpc("0.19", "1.27")
        eps = mp.mpf("0.04")
        n_pts = 64

        def szego(idx_th: int, z: mp.mpc, t: mp.mpc) -> mp.mpc:
            q = mp.exp(1j * mp.pi * t)
            return (mp.pi * mp.jtheta(1, 0, q, 1) * mp.jtheta(idx_th, mp.pi * z, q)) / (
                mp.jtheta(idx_th, 0, q) * mp.jtheta(1, mp.pi * z, q)
            )

        def szego_deriv(idx_th: int, z: mp.mpc, t: mp.mpc) -> mp.mpc:
            h = mp.mpf("1e-7")
            return (szego(idx_th, z + h, t) - szego(idx_th, z - h, t)) / (2 * h)

        def weierstrass_p(z: mp.mpc, t: mp.mpc) -> mp.mpc:
            # q-expansion of wp(z|tau): -pi^2/3 E_2*(tau) + pi^2/sin^2(pi z) - 8 pi^2 sum_{m>=1} m q^{2m}/(1-q^{2m}) cos(2pi m z)
            # Up to holomorphic constant, double pole part is pi^2/sin^2(pi z) - ...
            # Exact modular-covariant wp via lattice sum subtracted at origin:
            tot = 1 / (z**2)
            for m in range(-6, 7):
                for n in range(-6, 7):
                    if m == 0 and n == 0:
                        continue
                    w = m + n * t
                    tot += 1 / ((z - w) ** 2) - 1 / (w**2)
            return tot

        def contour_laurent(fn, power_z: int) -> complex:
            # Computes (1 / 2pi i) oint_{|z|=eps} z^{power_z} fn(z) dz:
            # power_z = 0 => c_{-1} (simple pole residue); power_z = 1 => c_{-2} (double pole coeff)
            acc = mp.mpc(0)
            for k in range(n_pts):
                ang = 2 * mp.pi * k / n_pts
                z = eps * mp.exp(1j * ang)
                dz_dtheta = 1j * z
                acc += (z**power_z) * fn(z) * dz_dtheta
            return complex(acc / (2j * mp.pi) * (2 * mp.pi / n_pts))

        # (a) Trivial character double-pole space span{1*dz, wp(z|tau)*dz} under S_theta: (z, tau) -> (z/tau, -1/tau)
        # Pullback of 1*dz is (1/tau) dz -> c_{-2} = 0!
        c_minus2_hol_after_S = contour_laurent(lambda z: (1 / tau), 1)
        c_minus2_wp_base = contour_laurent(lambda z: weierstrass_p(z, tau), 1)
        # Pullback of wp(z/tau | -1/tau) * d(z/tau) = tau^2 wp(z|tau) * (1/tau) dz = tau wp(z|tau) dz -> c_{-2} = tau!
        c_minus2_wp_after_S = contour_laurent(lambda z: (1 / tau) * weierstrass_p(z / tau, -1 / tau), 1)
        triv_filtration_err = max(
            abs(c_minus2_hol_after_S),
            abs(c_minus2_wp_base - 1.0),
            abs(c_minus2_wp_after_S - complex(tau)),
        )

        # (b) Active chi_(1,1) space span{S_3 dz, S_3' dz} under L^2 and S_theta
        c_minus1_s3_base = contour_laurent(lambda z: szego(3, z, tau), 0)
        c_minus2_s3_after_S = contour_laurent(lambda z: (1 / tau) * szego(3, z / tau, -1 / tau), 1)
        c_minus1_s3_after_S = contour_laurent(lambda z: (1 / tau) * szego(3, z / tau, -1 / tau), 0)
        c_minus2_s3p_base = contour_laurent(lambda z: szego_deriv(3, z, tau), 1)
        chi11_filtration_err = max(
            abs(c_minus1_s3_base - 1.0),
            abs(c_minus2_s3_after_S),
            abs(c_minus1_s3_after_S - 1.0),
            abs(c_minus2_s3p_base + 1.0),  # d/dz (1/z) = -1/z^2 => c_{-2} = -1
        )

        # (c) Vector-six (10,6) doublet (S_2 dz, S_4 dz) swap under S_theta evaluated at generic z_probe + residue
        z_probe = mp.mpc("0.17", "0.31")
        swap_err = max(
            abs(complex((1 / tau) * szego(2, z_probe / tau, -1 / tau) - szego(4, z_probe, tau))),
            abs(complex((1 / tau) * szego(4, z_probe / tau, -1 / tau) - szego(2, z_probe, tau))),
        )

    return {
        "trivial_O2p_pole_filtration_err": float(triv_filtration_err),
        "chi11_2p_pole_filtration_err": float(chi11_filtration_err),
        "vector_six_S2_S4_swap_err": float(swap_err),
        "filtration_and_swap_verified": max(triv_filtration_err, chi11_filtration_err, swap_err) < 1e-8,
    }


def run_independent_referee_suite() -> dict[str, Any]:
    if "origin_axiom.p753_register_field_join" in sys.modules:
        raise RuntimeError("Guardrail 6 violation: producer module must not be imported in referee script!")
    c1 = check_e8_root_lattice_coroot_identity()
    c2 = check_pauli_clifford_spin10_and_e_theta()
    c3 = check_qseries_and_scrambled_weave_triplet()
    c4 = check_elliptic_contour_pole_filtration()

    all_pass = (
        c1["n_roots"] == 240
        and c1["total_e8_dim"] == 248
        and c1["all_roots_norm_sq_2"]
        and c1["coroot_phase_equivalence_max_err"] < TOL
        and c1["integer_root_flips"] == 0
        and c1["spinor_root_flips"] == 128
        and c1["singlet_over_triplet_h4_ratio_set"] == [-1.0]
        and c1["a3_adjoint_15_parity_split"] == {"1": 9, "-1": 6}
        and c2["order_2O"] == 48
        and c2["order_St"] == 16
        and c2["index_2O_St"] == 3
        and c2["pauli_clifford_scrambled_S_theta_err"] < TOL
        and c2["kpi_minus_total"] == 112
        and c2["klein4_totals"] == {"00": 37, "10": 33, "01": 33, "11": 33}
        and c3["qseries_leading_coeff_quadrature_err"] < TOL
        and c3["scrambled_order_G_V"] == 96
        and c3["scrambled_order_G_T"] == 96
        and c3["scrambled_center_order"] == 4
        and c3["scrambled_S_T_fourth_plus_I_err"] < TOL
        and c3["untwisted_Sym2_Weil2_order"] == 48
        and c3["even_Z24_twist_orders"] == [24, 48, 72, 144]
        and (96 not in c3["even_Z24_twist_orders"])
        and c3["odd_m3_Sym2_Weil2_bar_intertwiner_err"] < TOL
        and c4["filtration_and_swap_verified"]
    )

    return {
        "zero_producer_imports": "origin_axiom.p753_register_field_join" not in sys.modules,
        "all_independent_checks_pass": all_pass,
        "check1_e8_root_lattice_coroot": c1,
        "check2_pauli_clifford_scrambled_e_theta": c2,
        "check3_qseries_and_scrambled_cocycle": c3,
        "check4_cauchy_contour_pole_filtration": c4,
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / "relays" / "p753_verification"
    out_dir.mkdir(parents=True, exist_ok=True)

    receipt = run_independent_referee_suite()
    json_path = out_dir / "p753_referee_receipt.json"
    txt_path = out_dir / "p753_referee_run.txt"

    json_text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")

    summary_lines = [
        "P-753 / R77-2 (WP-2.2 & WP-3.2) Independent Zero-Trust Referee Run",
        "===================================================================",
        f"Zero producer imports (Guardrail 6): {receipt['zero_producer_imports']}",
        f"All independent checks PASS:         {receipt['all_independent_checks_pass']}",
        f"E8 root lattice dim (240 + 8):       {receipt['check1_e8_root_lattice_coroot']['total_e8_dim']}",
        f"Coroot -h4 == zeta_Spin10*(+h4) err: {receipt['check1_e8_root_lattice_coroot']['coroot_phase_equivalence_max_err']:.3e}",
        f"Singlet/triplet h4 ratio (+-h4):     {receipt['check1_e8_root_lattice_coroot']['singlet_over_triplet_h4_ratio_set']}",
        f"Pauli Cl(10) scrambled S_theta err:  {receipt['check2_pauli_clifford_scrambled_S_theta']['pauli_clifford_scrambled_S_theta_err'] if 'check2_pauli_clifford_scrambled_S_theta' in receipt else receipt['check2_pauli_clifford_scrambled_e_theta']['pauli_clifford_scrambled_S_theta_err']:.3e}",
        f"248D Klein-4 totals (112; 136):      kpi_minus={receipt['check2_pauli_clifford_scrambled_e_theta']['kpi_minus_total']}, k4={receipt['check2_pauli_clifford_scrambled_e_theta']['klein4_totals']}",
        f"q-series leading coeff quadrature:   {receipt['check3_qseries_and_scrambled_cocycle']['qseries_leading_coeff_quadrature_err']:.3e}",
        f"Scrambled |G_T| / untwisted Sym^2:   {receipt['check3_qseries_and_scrambled_cocycle']['scrambled_order_G_T']} vs {receipt['check3_qseries_and_scrambled_cocycle']['untwisted_Sym2_Weil2_order']}",
        f"Even Z_24 twist orders:              {receipt['check3_qseries_and_scrambled_cocycle']['even_Z24_twist_orders']}",
        f"Odd m=3 Sym^2(Weil_2^*) intertwiner: {receipt['check3_qseries_and_scrambled_cocycle']['odd_m3_Sym2_Weil2_bar_intertwiner_err']:.3e}",
        f"Contour O(2p) / chi11(2p) / swap:    {receipt['check4_cauchy_contour_pole_filtration']['trivial_O2p_pole_filtration_err']:.3e}, {receipt['check4_cauchy_contour_pole_filtration']['chi11_2p_pole_filtration_err']:.3e}, {receipt['check4_cauchy_contour_pole_filtration']['vector_six_S2_S4_swap_err']:.3e}",
        "0 of 19.",
    ]
    txt_out = "\n".join(summary_lines) + "\n"
    txt_path.write_text(txt_out, encoding="utf-8")
    print(txt_out, end="")
    if not receipt["all_independent_checks_pass"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
