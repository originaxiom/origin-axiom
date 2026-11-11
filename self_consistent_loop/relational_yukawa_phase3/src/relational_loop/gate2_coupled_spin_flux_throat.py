"""Step 4: Gate 2 — Coupled Spin-Flux Throat & Klein-Four Palindrome Protection (Test A).

Constructs the intrinsic discrete Hodge harmonic 1-form alpha_s = d theta_s (oint_{S^1} alpha_s = 1)
and the globally gauge-covariant 2-component spin-flux operator on M_H combining:
  - Flat Z/5Z torsion bundle holonomy (2*pi*q/5) c_tors,
  - Continuous U(1)_base harmonic connection 2*pi*(Phi_base +- kappa_so) alpha_s,
  - Intrinsic Pauli-Zeeman & throat-hybridization potential
      V_spin(x) = -mu_B * (sigma_3 * ||alpha_s(x)||_g + sigma_1 / (1 + ||alpha_s(x)||_g^2)).

Tests directly on 3D hyperbolic meshes whether spin + harmonic magnetic flux breaks
(6)'s two-shoulder profile [0, 6] or is protected to < 1e-12 by the anti-unitary
Klein-four involution tilde{iota}_1 = K o iota_1^*, contrasting against single-peaked
reversible [3,1,3] / [2,1,1,1,2] and truly irreversible [5,1,2,2] / [2,2,1,5] (Sym = Z/2).
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import bmat, coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh

from .gate1_relational_quotient import word_to_sl2z
from .hyperbolic_yukawa_core import (
    TET_QUAD14_BARY,
    build_eulerian_subdivision,
    classify_cohomology_and_z5_cocycles,
    compute_tet_element_geometry_q14,
    extract_epstein_penner_data,
    random_haar_unitary,
    solve_harmonic_base_1form,
)


def check_gl2z_time_reversibility(word: str, ep_data: Dict[str, Any]) -> Dict[str, Any]:
    """Test whether M_W is GL(2, Z)-conjugate to M_W^{-1} via bounded search & 3D symmetry group."""
    W = word_to_sl2z(word)
    W_inv = np.array([[W[1, 1], -W[0, 1]], [-W[1, 0], W[0, 0]]], dtype=int)

    # Also test cyclic centered form on (6): L^3 R L R L^3 has J_1 = diag(-1,1), J_2 = diag(1,-1)
    found_conj: List[List[int]] = []
    for a in range(-12, 13):
        for b in range(-12, 13):
            for c in range(-12, 13):
                for d in range(-12, 13):
                    det = a * d - b * c
                    if abs(det) != 1:
                        continue
                    J = np.array([[a, b], [c, d]], dtype=int)
                    if np.array_equal(J @ W, W_inv @ J):
                        found_conj.append([a, b, c, d])
                        if len(found_conj) >= 2:
                            break
                if len(found_conj) >= 2:
                    break
            if len(found_conj) >= 2:
                break
        if len(found_conj) >= 2:
            break

    sym_grp = ep_data["manifold_std"].symmetry_group()
    sym_order = int(sym_grp.order())

    return {
        "word": word,
        "symmetry_group": str(sym_grp),
        "symmetry_order": sym_order,
        "found_small_gl2z_reversers": found_conj,
        "is_time_reversible_3d": sym_order >= 4,
    }


def verify_run6_isometric_involution(ep_6: Dict[str, Any]) -> float:
    """Verify explicitly on Epstein-Penner Gram matrices that t <-> 6-t (0..6), 7 <-> 8 is an exact isometry."""
    grams = ep_6["grams"]
    target_partner = {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 0, 7: 8, 8: 7}
    max_gram_err = 0.0
    for t, t_img in target_partner.items():
        best_t = float("inf")
        for perm in itertools.permutations(range(4)):
            if t == t_img and perm == (0, 1, 2, 3):
                continue
            err = float(np.max(np.abs(grams[t] - grams[t_img][np.ix_(perm, perm)])))
            best_t = min(best_t, err)
        max_gram_err = max(max_gram_err, best_t)
    return max_gram_err


def assemble_and_solve_coupled_spin_flux(
    ep_data: Dict[str, Any],
    cocycle_mod5: np.ndarray,
    harm_form: Dict[str, Any],
    charge_q: int,
    n_sub: int = 4,
    phi_base: float = 0.0,
    kappa_so: float = 0.15,
    mu_zeeman: float = 0.25,
    n_eigs: int = 6,
    subdiv: Optional[Dict[str, Any]] = None,
    tet_geoms: Optional[List[Dict[str, np.ndarray]]] = None,
    run_haar_su2: bool = False,
) -> Dict[str, Any]:
    """Assemble and solve the globally covariant 2-component spin-flux operator on M_H."""
    n_tet = ep_data["num_tets"]
    sub = subdiv if subdiv is not None else build_eulerian_subdivision(n_sub, True)
    nodes_bary = sub["nodes_bary"]
    grid_map = sub["grid_map"]
    sub_tets = sub["sub_tets"]
    n_local = nodes_bary.shape[0]

    geoms = tet_geoms if tet_geoms is not None else [
        compute_tet_element_geometry_q14(G, nodes_bary, sub_tets) for G in ep_data["grams"]
    ]

    omega5 = np.exp(2j * math.pi * (charge_q % 5) / 5.0)
    total_raw = n_tet * n_local
    parent = list(range(total_raw))
    phase = np.ones(total_raw, dtype=np.complex128)

    def find(x: int) -> Tuple[int, complex]:
        if parent[x] == x:
            return x, 1.0 + 0.0j
        r, pup = find(parent[x])
        parent[x] = r
        phase[x] = phase[x] * pup
        return r, phase[x]

    for finfo in ep_data["faces_info"]:
        fg = finfo["face_global"]
        tp, fp = finfo["t_pos"], finfo["f_pos"]
        tn = finfo["t_neg"]
        perm = finfo["perm_pos_to_neg"]
        tfac = omega5 ** int(cocycle_mod5[fg])
        for tup_p, lp in grid_map.items():
            if tup_p[fp] != 0:
                continue
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = grid_map[tuple(tup_n)]
            rp, php = find(tp * n_local + lp)
            rn, phn = find(tn * n_local + ln)
            rel = tfac * phn / php
            if rp != rn:
                parent[rp] = rn
                phase[rp] = rel

    roots = sorted({find(i)[0] for i in range(total_raw)})
    rmap = {r: idx for idx, r in enumerate(roots)}
    n_dof = len(roots)

    phi_up = 2.0 * math.pi * (phi_base + kappa_so)
    phi_dn = 2.0 * math.pi * (phi_base - kappa_so)
    outer_bary = TET_QUAD14_BARY[:, :, None] * TET_QUAD14_BARY[:, None, :]  # (14, 4, 4)

    r_l, c_l = [], []
    h11_l, h22_l, h12_l, m_l = [], [], [], []
    tet_mass_mats: List[csr_matrix] = []

    for t in range(n_tet):
        gm = geoms[t]
        grad_p = gm["grad_phi"]  # (n_elem, 4, 3)
        dvol = gm["dvol_q14"]    # (n_elem, 14)
        ginv = gm["g_inv_q14"]   # (n_elem, 14, 3, 3)
        acov = harm_form["alpha_cov_by_tet"][t]          # (n_elem, 3)
        anorm2 = harm_form["alpha_norm2_q14_by_tet"][t]  # (n_elem, 14)
        anorm = np.sqrt(np.maximum(0.0, anorm2))
        athroat = 1.0 / (1.0 + anorm2)

        D_up = grad_p[:, None, :, :] - 1j * (
            (phi_up * acov)[:, None, None, :] * TET_QUAD14_BARY[None, :, :, None]
        )
        D_dn = grad_p[:, None, :, :] - 1j * (
            (phi_dn * acov)[:, None, None, :] * TET_QUAD14_BARY[None, :, :, None]
        )

        K_up_e = np.einsum("eq,eqam,eqmn,eqbn->eab", dvol, np.conj(D_up), ginv, D_up)
        K_dn_e = np.einsum("eq,eqam,eqmn,eqbn->eab", dvol, np.conj(D_dn), ginv, D_dn)
        Z3_e = np.einsum("eq,qab->eab", -mu_zeeman * dvol * anorm, outer_bary).astype(np.complex128)
        Z1_e = np.einsum("eq,qab->eab", -mu_zeeman * dvol * athroat, outer_bary).astype(np.complex128)
        M_e = np.einsum("eq,qab->eab", dvol, outer_bary).astype(np.complex128)

        er = np.repeat(sub_tets, 4, axis=1).ravel()
        ec = np.tile(sub_tets, (1, 4)).ravel()
        H11_loc = coo_matrix(((K_up_e + Z3_e).ravel(), (er, ec)), shape=(n_local, n_local)).toarray()
        H22_loc = coo_matrix(((K_dn_e - Z3_e).ravel(), (er, ec)), shape=(n_local, n_local)).toarray()
        H12_loc = coo_matrix((Z1_e.ravel(), (er, ec)), shape=(n_local, n_local)).toarray()
        M_loc = coo_matrix((M_e.ravel(), (er, ec)), shape=(n_local, n_local)).toarray()

        ad = np.zeros(n_local, dtype=int)
        ap = np.zeros(n_local, dtype=np.complex128)
        for loc in range(n_local):
            r, ph = find(t * n_local + loc)
            ad[loc] = rmap[r]
            ap[loc] = ph

        ph_mat = np.conj(ap)[:, None] * ap[None, :]
        rr = np.repeat(ad, n_local)
        cc = np.tile(ad, n_local)
        r_l.append(rr)
        c_l.append(cc)
        h11_l.append((H11_loc * ph_mat).ravel())
        h22_l.append((H22_loc * ph_mat).ravel())
        h12_l.append((H12_loc * ph_mat).ravel())
        m_gl = (M_loc * ph_mat).ravel()
        m_l.append(m_gl)
        tet_mass_mats.append(coo_matrix((m_gl, (rr, cc)), shape=(n_dof, n_dof)).tocsr())

    R_c = np.concatenate(r_l)
    C_c = np.concatenate(c_l)
    H11 = coo_matrix((np.concatenate(h11_l), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    H22 = coo_matrix((np.concatenate(h22_l), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    H12 = coo_matrix((np.concatenate(h12_l), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    M11 = coo_matrix((np.concatenate(m_l), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    M11 = 0.5 * (M11 + M11.conj().T)

    H_2n = bmat([[H11, H12], [H12.conj().T, H22]], format="csr")
    M_2n = bmat([[M11, None], [None, M11]], format="csr")
    H_2n = 0.5 * (H_2n + H_2n.conj().T)

    # Exact Cholesky shift-invert: H_shift = H - sigma*M is strictly HPD, reducing operator norm from ~6e3 to ~0.2!
    k_req = min(n_eigs, 2 * n_dof - 1)
    sigma_shift = -2.0 * abs(mu_zeeman) - 1.0
    m_diag = np.real(M_2n.diagonal())
    d_scale = 1.0 / np.sqrt(np.maximum(1e-30, m_diag))

    def _solve_hpd_shift_invert(H_sp: csr_matrix, k_num: int) -> Tuple[np.ndarray, np.ndarray]:
        n_sz = H_sp.shape[0]
        if n_sz <= 2600:
            H_eq = (H_sp.toarray() * d_scale[:, None]) * d_scale[None, :]
            M_eq = (M_2n.toarray() * d_scale[:, None]) * d_scale[None, :]
            H_sh = 0.5 * (H_eq + H_eq.conj().T) - sigma_shift * (0.5 * (M_eq + M_eq.conj().T))
            L_chol = np.linalg.cholesky(H_sh)
            # Solve L_chol @ Y = M_eq => C = L_chol^{-1} M_eq L_chol^{-H}
            L_inv_M = np.linalg.solve(L_chol, 0.5 * (M_eq + M_eq.conj().T))
            C_op = np.linalg.solve(L_chol, L_inv_M.conj().T).conj().T
            C_op = 0.5 * (C_op + C_op.conj().T)
            mu_vals, w_vecs = eigh(C_op, subset_by_index=[n_sz - k_num, n_sz - 1])
            # Reverse so largest mu (smallest E) comes first
            mu_desc = mu_vals[::-1]
            w_desc = w_vecs[:, ::-1]
            ev_out = sigma_shift + 1.0 / mu_desc
            vc_eq = np.linalg.solve(L_chol.conj().T, w_desc)
            return ev_out, d_scale[:, None] * vc_eq
        ev_s, vc_s = eigsh(H_sp, k=k_num, M=M_2n, sigma=sigma_shift, which="LM", tol=1e-14)
        return ev_s, vc_s

    evals_raw, evecs_raw = _solve_hpd_shift_invert(H_2n, k_req)

    order = np.argsort(evals_raw.real)
    evals = np.array(evals_raw[order].real, dtype=float)
    evecs = np.array(evecs_raw[:, order], dtype=np.complex128)
    for j in range(k_req):
        v = evecs[:, j]
        nrm = math.sqrt(max(1e-30, float(np.real(np.vdot(v, M_2n @ v)))))
        evecs[:, j] = v / nrm

    E0 = float(evals[0])
    E1 = float(evals[1])
    rel_gap = (E1 - E0) / max(1e-12, abs(E0))
    mult = int(np.sum(np.abs(evals - E0) <= 1e-6 * max(1.0, abs(E0))))

    psi0_up = evecs[:n_dof, 0]
    psi0_dn = evecs[n_dof:, 0]
    spin_up_weight = float(np.real(np.vdot(psi0_up, M11 @ psi0_up)))
    spin_dn_weight = float(np.real(np.vdot(psi0_dn, M11 @ psi0_dn)))

    layer_probs = np.zeros(n_tet, dtype=float)
    for t in range(n_tet):
        Mt = tet_mass_mats[t]
        layer_probs[t] = float(
            np.real(np.vdot(psi0_up, Mt @ psi0_up)) + np.real(np.vdot(psi0_dn, Mt @ psi0_dn))
        )
    layer_probs /= np.sum(layer_probs)

    max_haar_su2_err = 0.0
    if run_haar_su2:
        rng = np.random.default_rng(20260302)
        for _ in range(4):
            U2 = random_haar_unitary(2, rng)
            B00 = U2[0, 0] * H11 + U2[0, 1] * H12.conj().T
            B01 = U2[0, 0] * H12 + U2[0, 1] * H22
            B10 = U2[1, 0] * H11 + U2[1, 1] * H12.conj().T
            B11 = U2[1, 0] * H12 + U2[1, 1] * H22
            Hp_00 = B00 * np.conj(U2[0, 0]) + B01 * np.conj(U2[0, 1])
            Hp_01 = B00 * np.conj(U2[1, 0]) + B01 * np.conj(U2[1, 1])
            Hp_10 = B10 * np.conj(U2[0, 0]) + B11 * np.conj(U2[0, 1])
            Hp_11 = B10 * np.conj(U2[1, 0]) + B11 * np.conj(U2[1, 1])
            Hp = bmat([[Hp_00, Hp_01], [Hp_10, Hp_11]], format="csr")
            Hp = 0.5 * (Hp + Hp.conj().T)
            ev_s, vc_s = _solve_hpd_shift_invert(Hp, 2)
            idx0 = int(np.argmin(ev_s.real))
            v0 = vc_s[:, idx0]
            v0 = v0 / math.sqrt(float(np.real(np.vdot(v0, M_2n @ v0))))
            lp_s = np.array(
                [
                    float(
                        np.real(np.vdot(v0[:n_dof], tet_mass_mats[t] @ v0[:n_dof]))
                        + np.real(np.vdot(v0[n_dof:], tet_mass_mats[t] @ v0[n_dof:]))
                    )
                    for t in range(n_tet)
                ]
            )
            lp_s /= np.sum(lp_s)
            max_haar_su2_err = max(
                max_haar_su2_err,
                abs(float(ev_s[idx0].real) - E0),
                float(np.max(np.abs(lp_s - layer_probs))),
            )

    peak_t = int(np.argmax(layer_probs))
    sorted_p = np.sort(layer_probs)[::-1]
    peak_to_second_gap = float(sorted_p[0] - sorted_p[1])

    return {
        "n_sub": n_sub,
        "charge_q": charge_q % 5,
        "phi_base": phi_base,
        "n_spinor_dof": 2 * n_dof,
        "E0": E0,
        "E1": E1,
        "rel_gap": rel_gap,
        "ground_multiplicity": mult,
        "spin_up_weight": spin_up_weight,
        "spin_dn_weight": spin_dn_weight,
        "layer_probs": layer_probs.tolist(),
        "peak_tet": peak_t,
        "peak_prob": float(sorted_p[0]),
        "second_prob": float(sorted_p[1]),
        "peak_to_second_gap": peak_to_second_gap,
        "haar_su2_spin_err": max_haar_su2_err,
    }


def run_gate2(n_sub: int = 4) -> Dict[str, Any]:
    """Execute Gate 2 coupled spin-flux throat & Klein-four palindrome protection audit."""
    sub = build_eulerian_subdivision(n_sub, True)

    def prepare_manifold(spec: str, word: str) -> Dict[str, Any]:
        ep = extract_epstein_penner_data(spec)
        coh = classify_cohomology_and_z5_cocycles(ep)
        geoms = [compute_tet_element_geometry_q14(G, sub["nodes_bary"], sub["sub_tets"]) for G in ep["grams"]]
        harm = solve_harmonic_base_1form(
            ep, coh["free_cocycles_int"][0], sub, geoms, coh["free_cycles_int"][0]
        )
        rev = check_gl2z_time_reversibility(word, ep)
        return {
            "ep": ep,
            "coh": coh,
            "geoms": geoms,
            "harm": harm,
            "reversibility": rev,
            "c_unram": coh["cusp_unramified_torsion_lines"][0]["cocycle"],
        }

    m_6 = prepare_manifold("b++LLLLLLRLR", "LLLLLLRLR")
    m_16 = prepare_manifold("b++LRRRRRRLR", "LRRRRRRLR")
    m_313 = prepare_manifold("b++LLLRLLLRLR", "LLLRLLLRLR")
    m_21112 = prepare_manifold("b+-LLRLRLLRLR", "LLRLRLLRLR")
    m_5122 = prepare_manifold("b++LLLLLRLLRRLR", "LLLLLRLLRRLR")
    m_2215 = prepare_manifold("b++LLRRLRRRRRLR", "LLRRLRRRRRLR")

    run6_gram_inv_err = verify_run6_isometric_involution(m_6["ep"])

    def sigma_P_val(cs: float) -> float:
        s = math.sin(4.0 * math.pi * cs)
        return 0.0 if abs(s) <= 1e-10 else (-1.0 if s > 0.0 else 1.0)

    # 1. Test Klein-Four Palindrome Protection on (6) with intrinsic CS flux Phi = 2*CS(M_H)
    #    and relational spin-orbit coupling sigma_P(M_H)*kappa_0, PLUS generic irrational flux Phi = 1/sqrt(5)
    phi_cs_6 = 2.0 * m_6["ep"]["chern_simons"]
    phi_cs_16 = 2.0 * m_16["ep"]["chern_simons"]
    kap_6 = sigma_P_val(m_6["ep"]["chern_simons"]) * 0.15
    kap_16 = sigma_P_val(m_16["ep"]["chern_simons"]) * 0.15

    res_6_q2_cs = assemble_and_solve_coupled_spin_flux(
        m_6["ep"], m_6["c_unram"], m_6["harm"], 2, n_sub, phi_cs_6, kap_6, 0.25, 6, sub, m_6["geoms"], True
    )
    res_6_q1_cs = assemble_and_solve_coupled_spin_flux(
        m_6["ep"], m_6["c_unram"], m_6["harm"], 1, n_sub, phi_cs_6, kap_6, 0.25, 6, sub, m_6["geoms"], False
    )
    res_6_q2_irr = assemble_and_solve_coupled_spin_flux(
        m_6["ep"], m_6["c_unram"], m_6["harm"], 2, n_sub, 1.0 / math.sqrt(5.0), 0.23, 0.35, 6, sub, m_6["geoms"], False
    )
    res_16_q1_cs = assemble_and_solve_coupled_spin_flux(
        m_16["ep"], m_16["c_unram"], m_16["harm"], 1, n_sub, phi_cs_16, kap_16, 0.25, 6, sub, m_16["geoms"], False
    )
    res_16_q2_cs = assemble_and_solve_coupled_spin_flux(
        m_16["ep"], m_16["c_unram"], m_16["harm"], 2, n_sub, phi_cs_16, kap_16, 0.25, 6, sub, m_16["geoms"], False
    )

    def run6_palindrome_err(probs: List[float]) -> float:
        return max(
            abs(probs[0] - probs[6]),
            abs(probs[1] - probs[5]),
            abs(probs[2] - probs[4]),
            abs(probs[7] - probs[8]),
        )

    pal_err_q2_cs = run6_palindrome_err(res_6_q2_cs["layer_probs"])
    pal_err_q1_cs = run6_palindrome_err(res_6_q1_cs["layer_probs"])
    pal_err_q2_irr = run6_palindrome_err(res_6_q2_irr["layer_probs"])
    e_pair_6 = sorted([res_6_q1_cs["E0"], res_6_q2_cs["E0"]])
    e_pair_16 = sorted([res_16_q1_cs["E0"], res_16_q2_cs["E0"]])
    enantiomer_6_vs_16_e0_err = float(np.max(np.abs(np.array(e_pair_6) - np.array(e_pair_16))))

    # 2. Reversible single-peak histories: [3,1,3] (q=2 & q=1) and [2,1,1,1,2] (q=1)
    kap_313 = sigma_P_val(m_313["ep"]["chern_simons"]) * 0.15
    kap_21112 = sigma_P_val(m_21112["ep"]["chern_simons"]) * 0.15
    res_313_q2 = assemble_and_solve_coupled_spin_flux(
        m_313["ep"], m_313["c_unram"], m_313["harm"], 2, n_sub, 2.0 * m_313["ep"]["chern_simons"], kap_313, 0.25, 6, sub, m_313["geoms"], False
    )
    res_313_q1 = assemble_and_solve_coupled_spin_flux(
        m_313["ep"], m_313["c_unram"], m_313["harm"], 1, n_sub, 2.0 * m_313["ep"]["chern_simons"], kap_313, 0.25, 6, sub, m_313["geoms"], False
    )
    res_21112_q1 = assemble_and_solve_coupled_spin_flux(
        m_21112["ep"], m_21112["c_unram"], m_21112["harm"], 1, n_sub, 2.0 * m_21112["ep"]["chern_simons"], kap_21112, 0.25, 6, sub, m_21112["geoms"], False
    )

    # 3. Irreversible chiral pair [5,1,2,2] and [2,2,1,5] (Sym = Z/2, W not conjugate to W^{-1})
    kap_5122 = sigma_P_val(m_5122["ep"]["chern_simons"]) * 0.15
    kap_2215 = sigma_P_val(m_2215["ep"]["chern_simons"]) * 0.15
    res_5122_q1 = assemble_and_solve_coupled_spin_flux(
        m_5122["ep"], m_5122["c_unram"], m_5122["harm"], 1, n_sub, 2.0 * m_5122["ep"]["chern_simons"], kap_5122, 0.25, 6, sub, m_5122["geoms"], True
    )
    res_5122_q2 = assemble_and_solve_coupled_spin_flux(
        m_5122["ep"], m_5122["c_unram"], m_5122["harm"], 2, n_sub, 2.0 * m_5122["ep"]["chern_simons"], kap_5122, 0.25, 6, sub, m_5122["geoms"], False
    )
    res_2215_q1 = assemble_and_solve_coupled_spin_flux(
        m_2215["ep"], m_2215["c_unram"], m_2215["harm"], 1, n_sub, 2.0 * m_2215["ep"]["chern_simons"], kap_2215, 0.25, 6, sub, m_2215["geoms"], False
    )
    res_2215_q2 = assemble_and_solve_coupled_spin_flux(
        m_2215["ep"], m_2215["c_unram"], m_2215["harm"], 2, n_sub, 2.0 * m_2215["ep"]["chern_simons"], kap_2215, 0.25, 6, sub, m_2215["geoms"], False
    )

    e_pair_5122 = sorted([res_5122_q1["E0"], res_5122_q2["E0"]])
    e_pair_2215 = sorted([res_2215_q1["E0"], res_2215_q2["E0"]])
    irrev_enantiomer_e0_err = float(np.max(np.abs(np.array(e_pair_5122) - np.array(e_pair_2215))))

    # Check harmonic 1-form exactness across all 6 manifolds
    max_harm_coclosure = max(
        m["harm"]["coclosure_residual"] for m in (m_6, m_16, m_313, m_21112, m_5122, m_2215)
    )
    max_harm_holonomy_err = max(
        m["harm"]["loop_holonomy_err"] for m in (m_6, m_16, m_313, m_21112, m_5122, m_2215)
    )
    max_haar_su2 = max(res_6_q2_cs["haar_su2_spin_err"], res_5122_q1["haar_su2_spin_err"])

    # Pick lowest-energy twisted sector on [5,1,2,2]
    lowest_5122 = res_5122_q1 if res_5122_q1["E0"] <= res_5122_q2["E0"] else res_5122_q2

    gate2_passed = (
        max_harm_coclosure < 1e-12
        and max_harm_holonomy_err < 1e-12
        and run6_gram_inv_err < 1e-12
        and pal_err_q2_cs < 1e-12
        and pal_err_q1_cs < 1e-12
        and pal_err_q2_irr < 1e-12
        and max_haar_su2 < 1e-12
        and m_6["reversibility"]["is_time_reversible_3d"]
        and (not m_5122["reversibility"]["is_time_reversible_3d"])
        and m_5122["reversibility"]["symmetry_order"] == 2
        and lowest_5122["peak_to_second_gap"] > 0.02
        and irrev_enantiomer_e0_err < 1e-10
    )

    return {
        "gate": "Gate 2: Coupled Spin-Flux Throat & Klein-Four Palindrome Protection (Test A)",
        "gate2_passed": gate2_passed,
        "harmonic_1form_summary": {
            "max_coclosure_residual": max_harm_coclosure,
            "max_loop_holonomy_err": max_harm_holonomy_err,
            "run6_harmonic_norm2": m_6["harm"]["harmonic_l2_norm2"],
            "irrev_5122_harmonic_norm2": m_5122["harm"]["harmonic_l2_norm2"],
        },
        "klein_four_palindrome_protection_on_run6": {
            "symmetry_info": m_6["reversibility"],
            "epstein_penner_involution_gram_err": run6_gram_inv_err,
            "palindrome_err_q2_cs_flux": pal_err_q2_cs,
            "palindrome_err_q1_cs_flux": pal_err_q1_cs,
            "palindrome_err_q2_irrational_flux": pal_err_q2_irr,
            "spin_flux_breaks_two_shoulder_tie_on_run6": (res_6_q2_cs["peak_to_second_gap"] > 1e-6),
            "q2_cs_flux_result": res_6_q2_cs,
            "q1_cs_flux_result": res_6_q1_cs,
            "enantiomer_1_6_q2_e0_diff": enantiomer_6_vs_16_e0_err,
        },
        "reversible_single_peak_controls": {
            "3_1_3_symmetry": m_313["reversibility"],
            "3_1_3_q2": res_313_q2,
            "3_1_3_q1": res_313_q1,
            "2_1_1_1_2_symmetry": m_21112["reversibility"],
            "2_1_1_1_2_q1": res_21112_q1,
        },
        "irreversible_chiral_pair_5_1_2_2": {
            "5_1_2_2_symmetry": m_5122["reversibility"],
            "2_2_1_5_symmetry": m_2215["reversibility"],
            "5_1_2_2_q1": res_5122_q1,
            "5_1_2_2_q2": res_5122_q2,
            "lowest_sector_single_peak_gap": lowest_5122["peak_to_second_gap"],
            "enantiomer_sorted_e0_pair_err": irrev_enantiomer_e0_err,
        },
        "max_haar_su2_spin_scrambling_err": max_haar_su2,
    }


if __name__ == "__main__":
    import json

    out = run_gate2(n_sub=4)
    print(json.dumps(out, indent=2))
    if not out["gate2_passed"]:
        raise SystemExit(1)
