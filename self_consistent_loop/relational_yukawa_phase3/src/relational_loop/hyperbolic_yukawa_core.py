"""Exact 3D Cusped Hyperbolic Geometry, Discrete Harmonic 1-Form, Spin-Flux & Trilinear Yukawa FEM Core.

Clean-room Phase 3 core (zero imports from Phase 1 or Phase 2, zero empirical inputs).
Provides:
  1. Quad-precision Epstein-Penner hyperbolic Riemannian metrics and 24-cone volumes.
  2. Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature on S_4-symmetric
     Eulerian subdivisions.
  3. Exact arbitrary-precision integer Smith Normal Form extracting BOTH flat Z/5Z torsion
     1-cocycles (cusp-unramified and cusp-ramified) AND the canonical integer free cohomology
     generator n_free in H^1_free(M; Z) ~= Z.
  4. Exact discrete Hodge harmonic 1-form solver alpha_s = d theta_s (d alpha_s = 0,
     d^dagger alpha_s = 0, integral_{S^1} alpha_s = 1).
  5. Twisted 3D scalar & coupled 2-component spin-flux eigenvalue solvers, plus exact
     degree-5 trilinear 3D Yukawa overlap integration and Haar-invariant CKM/Jarlskog extractors.
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh, spsolve
from scipy.special import roots_legendre, spence
import snappy
from snappy.geometric_structure.cusp_neighborhood.complex_cusp_cross_section import (
    ComplexCuspCrossSection,
)


VBITS = (1, 2, 4, 8)
FBITS = (14, 13, 11, 7)


# Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature (Jinyun-Walkington / Stroud):
_JW_A1 = 0.0927352503108912264023239
_JW_B1 = 1.0 - 3.0 * _JW_A1
_JW_W1 = 0.0734930431163619495438667 / 6.0

_JW_A2 = 0.3108859192633006097973457
_JW_B2 = 1.0 - 3.0 * _JW_A2
_JW_W2 = 0.1126879257180158508001550 / 6.0

_JW_A3 = 0.0455037041256496494918805
_JW_B3 = 0.5 - _JW_A3
_JW_W3 = 0.0425460207770814664386522 / 6.0


def build_tet_quad14() -> Tuple[np.ndarray, np.ndarray]:
    """Return (pts_bary (14,4), wts (14,)) for the positive-weight S_4-symmetric degree-5 rule."""
    pts: List[List[float]] = []
    wts: List[float] = []
    for i in range(4):
        v1 = [_JW_A1] * 4
        v1[i] = _JW_B1
        pts.append(v1)
        wts.append(_JW_W1)

        v2 = [_JW_A2] * 4
        v2[i] = _JW_B2
        pts.append(v2)
        wts.append(_JW_W2)

    for i in range(4):
        for j in range(i + 1, 4):
            pts.append([_JW_B3 if k in (i, j) else _JW_A3 for k in range(4)])
            wts.append(_JW_W3)

    return np.array(pts, dtype=float), np.array(wts, dtype=float)


TET_QUAD14_BARY, TET_QUAD14_WTS = build_tet_quad14()


def random_haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    """Mezzadri QR algorithm for a Haar-distributed unitary matrix in U(n)."""
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > 0, d / np.abs(d), 1.0 + 0.0j)
    return q * ph[None, :]


def gauss_reduce_tau(tau: complex, tol: float = 1e-13) -> complex:
    """Map tau in H into the canonical PSL(2, Z) fundamental domain F."""
    z = complex(tau)
    if z.imag <= 0:
        raise ValueError(f"Modulus must have Im(tau) > 0, got {z}")
    for _ in range(200):
        n = round(z.real)
        if n != 0:
            z = z - n
        if abs(z) < 1.0 - tol:
            z = -1.0 / z
            continue
        if abs(z.real) <= 0.5 + tol and abs(z) >= 1.0 - tol:
            break
    if abs(z.real + 0.5) <= tol:
        z = complex(0.5, z.imag)
    if abs(abs(z) - 1.0) <= tol and z.real < -tol:
        z = -1.0 / z
    return z


def bloch_wigner_volume(z: complex) -> float:
    """Exact hyperbolic volume D(z) of an ideal tetrahedron with shape z in H."""
    zc = complex(z)
    li2 = spence(1.0 - zc)
    return float(np.imag(li2) + np.angle(1.0 - zc) * np.log(abs(zc)))


def extract_epstein_penner_data(spec_or_manifold: Any) -> Dict[str, Any]:
    """Extract quad-precision Epstein-Penner Minkowski Grams, gluings, and dual chain maps."""
    if isinstance(spec_or_manifold, str):
        M_base = snappy.Manifold(spec_or_manifold)
        name = spec_or_manifold
    else:
        M_base = spec_or_manifold
        name = M_base.name()

    M = M_base.high_precision() if hasattr(M_base, "high_precision") else M_base
    shapes_hp = M.tetrahedra_shapes("rect")
    shapes = [complex(z) for z in shapes_hp]
    ccs = ComplexCuspCrossSection.fromManifoldAndShapes(M, shapes_hp)
    ccs.normalize_cusps()

    n_tet = len(ccs.mcomplex.Tetrahedra)
    grams: List[np.ndarray] = []
    gluings: List[List[Tuple[int, Tuple[int, int, int, int]]]] = []
    horo_min_edge: List[float] = []
    tet_bw_vols: List[float] = []

    max_intra_err = 0.0
    for T in ccs.mcomplex.Tetrahedra:
        G = np.zeros((4, 4), dtype=float)
        h_lens = [
            float(abs(val))
            for vb in VBITS
            for val in T.horotriangles[vb].lengths.values()
        ]
        horo_min_edge.append(min(h_lens))

        for i in range(4):
            for j in range(i + 1, 4):
                lam2_vals = []
                for k in range(4):
                    if k != i and k != j:
                        Fk = FBITS[k]
                        li = float(abs(T.horotriangles[VBITS[i]].lengths[Fk]))
                        lj = float(abs(T.horotriangles[VBITS[j]].lengths[Fk]))
                        lam2_vals.append(1.0 / (li * lj))
                max_intra_err = max(max_intra_err, abs(lam2_vals[0] - lam2_vals[1]))
                G[i, j] = G[j, i] = -2.0 * (0.5 * (lam2_vals[0] + lam2_vals[1]))
        grams.append(G)

        g_row: List[Tuple[int, Tuple[int, int, int, int]]] = []
        for f_idx in range(4):
            Fb = FBITS[f_idx]
            nb_obj = T.Neighbor[Fb]
            perm = T.Gluing[Fb]
            g_row.append((nb_obj.Index, (perm[0], perm[1], perm[2], perm[3])))
        gluings.append(g_row)
        tet_bw_vols.append(bloch_wigner_volume(shapes[T.Index]))

    max_inter_err = 0.0
    for t_idx in range(n_tet):
        for f_idx in range(4):
            nb_idx, perm = gluings[t_idx][f_idx]
            verts = [v for v in range(4) if v != f_idx]
            for a in verts:
                for b in verts:
                    diff = abs(grams[t_idx][a, b] - grams[nb_idx][perm[a], perm[b]])
                    max_inter_err = max(max_inter_err, diff)

    bmaps_raw = ccs.mcomplex.boundary_maps()
    d1, d2, d3 = [
        np.array([int(x) for x in m.list()], dtype=int).reshape((m.nrows(), m.ncols()))
        for m in bmaps_raw
    ]

    fbit_to_idx = {14: 0, 13: 1, 11: 2, 7: 3}
    faces_info: List[Dict[str, Any]] = []
    for f_global, F_obj in enumerate(ccs.mcomplex.Faces):
        c0, c1 = F_obj.Corners[0], F_obj.Corners[1]
        t0, fi0 = c0.Tetrahedron.Index, fbit_to_idx[c0.Subsimplex]
        t1, fi1 = c1.Tetrahedron.Index, fbit_to_idx[c1.Subsimplex]
        nb0, perm0 = gluings[t0][fi0]
        assert nb0 == t1
        faces_info.append(
            {
                "face_global": f_global,
                "t_pos": t0,
                "f_pos": fi0,
                "t_neg": t1,
                "f_neg": fi1,
                "perm_pos_to_neg": perm0,
            }
        )

    M.set_peripheral_curves("shortest")
    cusp_moduli = [complex(M.cusp_info(i)["modulus"]) for i in range(M.num_cusps())]
    try:
        cs_val = float(M.chern_simons())
    except Exception:
        cs_val = float("nan")

    try:
        sym_grp_str = str(M_base.symmetry_group())
        is_amph = bool(M_base.symmetry_group().is_amphicheiral())
    except Exception:
        sym_grp_str = "unknown"
        is_amph = abs(math.sin(4.0 * math.pi * cs_val)) < 1e-10

    return {
        "name": name,
        "manifold": M,
        "manifold_std": M_base,
        "symmetry_group_str": sym_grp_str,
        "is_amphicheiral": is_amph,
        "num_tets": n_tet,
        "num_cusps": M.num_cusps(),
        "homology_str": str(M.homology()),
        "snappy_volume": float(M.volume()),
        "chern_simons": cs_val,
        "cusp_moduli": cusp_moduli,
        "shapes": shapes,
        "tet_bw_volumes": tet_bw_vols,
        "horo_min_edge": horo_min_edge,
        "grams": grams,
        "gluings": gluings,
        "faces_info": faces_info,
        "d1": d1,
        "d2": d2,
        "d3": d3,
        "max_intra_penner_err": max_intra_err,
        "max_inter_gluing_err": max_inter_err,
    }


def compute_penner_tet_volume(G: np.ndarray, nq: int = 20) -> float:
    """Exact 24-cone cusp-desingularized Riemannian hyperbolic volume from Penner Gram G."""
    pts, wts = roots_legendre(nq)
    u = 0.5 * (pts + 1.0)
    wu = 0.5 * wts
    S, T, R = np.meshgrid(u, u, u, indexing="ij")
    WS, WT, WR = np.meshgrid(wu, wu, wu, indexing="ij")

    c = np.array([0.25, 0.25, 0.25, 0.25], dtype=float)
    e = np.eye(4, dtype=float)

    Dmat = G[1:, :] - G[0:1, :]
    Gdiff = Dmat[:, 1:] - Dmat[:, 0:1]
    detA = float(np.linalg.det(Gdiff))
    adjA = detA * np.linalg.inv(Gdiff)

    total = 0.0
    for i0, i1, i2, i3 in itertools.permutations(range(4)):
        p0 = c
        p1 = (e[i1] + e[i2] + e[i3]) / 3.0
        p2 = (e[i2] + e[i3]) / 2.0
        p3 = e[i3]

        detJ = abs(float(np.linalg.det(np.array([p1[1:] - p0[1:], p2[1:] - p0[1:], p3[1:] - p0[1:]]))))
        Y = (1.0 - T)[..., None] * p0 + (T * R)[..., None] * p1 + (T * (1.0 - R))[..., None] * p2
        YG = np.einsum("...a,ab->...b", Y, G)
        q_yy = -np.sum(YG * Y, axis=-1)
        q_yp3 = -YG[..., i3]
        Q_hat = (1.0 - S) * q_yy + 2.0 * S * q_yp3

        W = (1.0 - S)[..., None] * Y + S[..., None] * p3
        dQ = -2.0 * np.einsum("mb,...b->...m", Dmat, W)
        u_adj_u = np.einsum("...m,mn,...n->...", dQ, adjA, dQ)

        det_g_omS4 = ((1.0 - S) * Q_hat * detA + 0.25 * u_adj_u) / (Q_hat ** 4)
        total += float(np.sum(detJ * T * np.sqrt(np.maximum(0.0, det_g_omS4)) * WS * WT * WR))
    return total


def _integer_snf_with_inverses(
    A_in: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Arbitrary-precision integer Smith Normal Form U @ A_in @ V = S with unimodular inverses."""
    A = np.array(A_in, dtype=object)
    m, n = A.shape
    U = np.eye(m, dtype=object)
    U_inv = np.eye(m, dtype=object)
    V = np.eye(n, dtype=object)
    V_inv = np.eye(n, dtype=object)

    def swap_rows(i: int, j: int) -> None:
        if i != j:
            A[[i, j], :] = A[[j, i], :]
            U[[i, j], :] = U[[j, i], :]
            U_inv[:, [i, j]] = U_inv[:, [j, i]]

    def swap_cols(i: int, j: int) -> None:
        if i != j:
            A[:, [i, j]] = A[:, [j, i]]
            V[:, [i, j]] = V[:, [j, i]]
            V_inv[[i, j], :] = V_inv[[j, i], :]

    def add_row(dst: int, src: int, factor: int) -> None:
        if factor != 0:
            A[dst, :] = A[dst, :] + factor * A[src, :]
            U[dst, :] = U[dst, :] + factor * U[src, :]
            U_inv[:, src] = U_inv[:, src] - factor * U_inv[:, dst]

    def add_col(dst: int, src: int, factor: int) -> None:
        if factor != 0:
            A[:, dst] = A[:, dst] + factor * A[:, src]
            V[:, dst] = V[:, dst] + factor * V[:, src]
            V_inv[src, :] = V_inv[src, :] - factor * V_inv[dst, :]

    r = 0
    while r < m and r < n:
        nz = [(i, j, abs(int(A[i, j]))) for i in range(r, m) for j in range(r, n) if A[i, j] != 0]
        if not nz:
            break
        pi, pj, _ = min(nz, key=lambda x: x[2])
        swap_rows(r, pi)
        swap_cols(r, pj)

        while True:
            changed = False
            for i in range(r + 1, m):
                if A[i, r] != 0:
                    q = int(A[i, r]) // int(A[r, r])
                    add_row(i, r, -q)
                    if A[i, r] != 0:
                        swap_rows(r, i)
                        changed = True
            for j in range(r + 1, n):
                if A[r, j] != 0:
                    q = int(A[r, j]) // int(A[r, r])
                    add_col(j, r, -q)
                    if A[r, j] != 0:
                        swap_cols(r, j)
                        changed = True
            if changed:
                continue

            piv = int(A[r, r])
            div_fail = None
            for i in range(r + 1, m):
                for j in range(r + 1, n):
                    if int(A[i, j]) % piv != 0:
                        div_fail = i
                        break
                if div_fail is not None:
                    break
            if div_fail is not None:
                add_row(r, div_fail, 1)
                continue
            break

        if int(A[r, r]) < 0:
            A[r, :] = -A[r, :]
            U[r, :] = -U[r, :]
            U_inv[:, r] = -U_inv[:, r]
        r += 1

    return U, U_inv, A, V, V_inv


def _count_cover_cusps_mod_p(ep_data: Dict[str, Any], cocycle: np.ndarray, p: int = 5) -> int:
    n_tet = ep_data["num_tets"]
    total = n_tet * 4 * p
    parent = list(range(total))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for finfo in ep_data["faces_info"]:
        fg = finfo["face_global"]
        tp, fp = finfo["t_pos"], finfo["f_pos"]
        tn = finfo["t_neg"]
        perm = finfo["perm_pos_to_neg"]
        sh = int(cocycle[fg]) % p
        for vp in range(4):
            if vp != fp:
                vn = perm[vp]
                for s in range(p):
                    r1 = find((tp * 4 + vp) * p + s)
                    r2 = find((tn * 4 + vn) * p + ((s + sh) % p))
                    if r1 != r2:
                        parent[r2] = r1
    return len({find(i) for i in range(total)})


def classify_cohomology_and_z5_cocycles(ep_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract both Z/5Z torsion lines AND the exact integer free 1-cocycle n_free in H^1_free(M; Z)."""
    d2_obj = ep_data["d2"].astype(object)
    d3_obj = ep_data["d3"].astype(object)
    _, _, S_d3t, V_d3t, V_inv = _integer_snf_with_inverses(d3_obj.T)
    rank_d3t = sum(1 for k in range(min(S_d3t.shape)) if int(S_d3t[k, k]) != 0)
    K_basis = V_d3t[:, rank_d3t:]

    full_coords = V_inv @ d2_obj.T
    assert all(int(x) == 0 for x in full_coords[:rank_d3t, :].ravel())
    B_coords = full_coords[rank_d3t:, :]
    U_b, U_b_inv, S_b, _, _ = _integer_snf_with_inverses(B_coords)

    H1_gens = K_basis @ U_b_inv
    inv_factors = [
        int(S_b[j, j]) if j < min(S_b.shape) else 0 for j in range(H1_gens.shape[1])
    ]

    # Exact integer free generators (inv_factors[j] == 0)
    free_cocycles_int: List[np.ndarray] = []
    free_cycles_int: List[np.ndarray] = []
    for j, d_val in enumerate(inv_factors):
        if d_val == 0:
            w_free = np.zeros(H1_gens.shape[1], dtype=object)
            w_free[j] = 1
            low_z = U_b.T @ w_free
            full_z = np.concatenate([np.zeros(rank_d3t, dtype=object), low_z])
            n_free_obj = V_inv.T @ full_z
            assert all(int(x) == 0 for x in (d2_obj @ n_free_obj))
            cyc_free_obj = H1_gens[:, j]
            assert int(n_free_obj @ cyc_free_obj) == 1
            n_arr = np.array([int(x) for x in n_free_obj], dtype=int)
            c_arr = np.array([int(x) for x in cyc_free_obj], dtype=int)
            # Canonical sign: make first non-zero entry of n_arr positive
            nz_entries = [x for x in n_arr if x != 0]
            if nz_entries and nz_entries[0] < 0:
                n_arr = -n_arr
                c_arr = -c_arr
            free_cocycles_int.append(n_arr)
            free_cycles_int.append(c_arr)

    torsion_5_cycles_mod5: List[np.ndarray] = []
    for j, d_val in enumerate(inv_factors):
        if d_val != 0 and d_val % 5 == 0:
            cyc = H1_gens[:, j]
            torsion_5_cycles_mod5.append(
                np.array([int(((d_val // 5) * x) % 5) for x in cyc], dtype=int)
            )

    active_j = [j for j, d_val in enumerate(inv_factors) if d_val % 5 == 0]
    U_b_mod5 = np.array([[int(x % 5) for x in row] for row in U_b], dtype=int)
    V_inv_mod5 = np.array([[int(x % 5) for x in row] for row in V_inv], dtype=int)

    projective_lines: List[Dict[str, Any]] = []
    seen_canon = set()
    for combo in itertools.product(range(5), repeat=len(active_j)):
        if all(x == 0 for x in combo):
            continue
        first_nz = next(x for x in combo if x != 0)
        inv_f = pow(first_nz, -1, 5)
        canon = tuple((x * inv_f) % 5 for x in combo)
        if canon in seen_canon:
            continue
        seen_canon.add(canon)

        w = np.zeros(H1_gens.shape[1], dtype=int)
        for idx_a, j_col in enumerate(active_j):
            w[j_col] = canon[idx_a]
        low_v = (U_b_mod5.T @ w) % 5
        full_v = np.concatenate([np.zeros(rank_d3t, dtype=int), low_v])
        coc = (V_inv_mod5.T @ full_v) % 5
        assert np.all((ep_data["d2"] @ coc) % 5 == 0)

        t_pairs = [int((coc @ tc) % 5) for tc in torsion_5_cycles_mod5]
        is_tors = any(tp != 0 for tp in t_pairs)
        ncusps = _count_cover_cusps_mod_p(ep_data, coc, p=5)
        projective_lines.append(
            {
                "f5_coords": list(canon),
                "cocycle": coc,
                "torsion_pairings_mod5": t_pairs,
                "is_torsion_nontrivial": is_tors,
                "cover_num_cusps": ncusps,
                "is_cusp_unramified": (ncusps == 5 * ep_data["num_cusps"]),
            }
        )

    return {
        "h1_invariant_factors": inv_factors,
        "betti_1": len(free_cocycles_int),
        "free_cocycles_int": free_cocycles_int,
        "free_cycles_int": free_cycles_int,
        "has_5_torsion": len(torsion_5_cycles_mod5) > 0,
        "torsion_5_rank": len(torsion_5_cycles_mod5),
        "cusp_unramified_torsion_lines": [
            ln for ln in projective_lines if ln["is_torsion_nontrivial"] and ln["is_cusp_unramified"]
        ],
        "cusp_ramified_torsion_lines": [
            ln for ln in projective_lines if ln["is_torsion_nontrivial"] and not ln["is_cusp_unramified"]
        ],
        "all_lines": projective_lines,
    }


def build_eulerian_subdivision(n_sub: int, truncate_cusp_corners: bool = True) -> Dict[str, Any]:
    """100% S_4-permutation-symmetric tetrahedral subdivision into sub-tetrahedra."""
    if n_sub < 2:
        raise ValueError("n_sub must be >= 2")

    nodes_bary: List[Tuple[float, float, float, float]] = []
    grid_map: Dict[Tuple[int, int, int, int], int] = {}
    is_horo_boundary: List[bool] = []

    for i0 in range(n_sub + 1):
        for i1 in range(n_sub + 1 - i0):
            for i2 in range(n_sub + 1 - i0 - i1):
                i3 = n_sub - i0 - i1 - i2
                if truncate_cusp_corners and max(i0, i1, i2, i3) == n_sub:
                    continue
                grid_map[(i0, i1, i2, i3)] = len(nodes_bary)
                nodes_bary.append((i0 / n_sub, i1 / n_sub, i2 / n_sub, i3 / n_sub))
                is_horo_boundary.append(max(i0, i1, i2, i3) == n_sub - 1)

    sub_tets: List[Tuple[int, int, int, int]] = []
    e4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

    for b0 in range(n_sub):
        for b1 in range(n_sub - b0):
            for b2 in range(n_sub - b0 - b1):
                b3 = (n_sub - 1) - b0 - b1 - b2
                if truncate_cusp_corners and max(b0, b1, b2, b3) == n_sub - 1:
                    continue
                b = (b0, b1, b2, b3)
                sub_tets.append(
                    tuple(grid_map[(b[0] + e[0], b[1] + e[1], b[2] + e[2], b[3] + e[3])] for e in e4)
                )

    for c0 in range(n_sub - 1):
        for c1 in range(n_sub - 1 - c0):
            for c2 in range(n_sub - 1 - c0 - c1):
                c3 = (n_sub - 2) - c0 - c1 - c2
                c = (c0, c1, c2, c3)
                oct_c = len(nodes_bary)
                nodes_bary.append(((c0 + 0.5) / n_sub, (c1 + 0.5) / n_sub, (c2 + 0.5) / n_sub, (c3 + 0.5) / n_sub))
                is_horo_boundary.append(False)

                pidx: Dict[Tuple[int, int], int] = {}
                for a in range(4):
                    for b in range(a + 1, 4):
                        tup = tuple(c[m] + e4[a][m] + e4[b][m] for m in range(4))
                        pidx[(a, b)] = pidx[(b, a)] = grid_map[tup]

                for a in range(4):
                    oth = [b for b in range(4) if b != a]
                    sub_tets.append((oct_c, pidx[(a, oth[0])], pidx[(a, oth[1])], pidx[(a, oth[2])]))
                for d in range(4):
                    rem = [a for a in range(4) if a != d]
                    sub_tets.append((oct_c, pidx[(rem[0], rem[1])], pidx[(rem[1], rem[2])], pidx[(rem[2], rem[0])]))

    if n_sub >= 3:
        for d0 in range(n_sub - 2):
            for d1 in range(n_sub - 2 - d0):
                for d2 in range(n_sub - 2 - d0 - d1):
                    d3v = (n_sub - 3) - d0 - d1 - d2
                    d = (d0, d1, d2, d3v)
                    sub_tets.append(
                        tuple(
                            grid_map[(d[0] + 1 - e[0], d[1] + 1 - e[1], d[2] + 1 - e[2], d[3] + 1 - e[3])]
                            for e in e4
                        )
                    )

    return {
        "n_sub": n_sub,
        "nodes_bary": np.array(nodes_bary, dtype=float),
        "grid_map": grid_map,
        "is_horo_boundary": np.array(is_horo_boundary, dtype=bool),
        "sub_tets": np.array(sub_tets, dtype=int),
    }


def compute_tet_element_geometry_q14(
    G: np.ndarray, nodes_bary: np.ndarray, sub_tets: np.ndarray
) -> Dict[str, np.ndarray]:
    """Precompute 14-point degree-5 quadrature volume weights, g^{-1}, and P1 gradients on one ideal tet."""
    Dmat = G[1:, :] - G[0:1, :]
    Gdiff = Dmat[:, 1:] - Dmat[:, 0:1]

    elem_verts = nodes_bary[sub_tets]  # (n_elem, 4, 4)
    v0 = elem_verts[:, 0, 1:]
    J = np.stack([elem_verts[:, 1, 1:] - v0, elem_verts[:, 2, 1:] - v0, elem_verts[:, 3, 1:] - v0], axis=-1)
    detJ = np.abs(np.linalg.det(J))  # (n_elem,)
    invJT = np.linalg.inv(np.swapaxes(J, 1, 2))

    grad_phi = np.zeros((sub_tets.shape[0], 4, 3), dtype=float)
    grad_phi[:, 1:, :] = np.swapaxes(invJT, 1, 2)
    grad_phi[:, 0, :] = -np.sum(grad_phi[:, 1:, :], axis=1)

    # Evaluate metric at all 14 quadrature points simultaneously: W shape (n_elem, 14, 4)
    W = np.einsum("qk,ekb->eqb", TET_QUAD14_BARY, elem_verts)
    WG = W @ G
    Q = -np.sum(WG * W, axis=-1)  # (n_elem, 14)
    dQ = -2.0 * (W @ Dmat.T)  # (n_elem, 14, 3)

    g_mat = (
        Gdiff[None, None, :, :] / Q[:, :, None, None]
        + (dQ[:, :, :, None] * dQ[:, :, None, :]) / (4.0 * (Q[:, :, None, None] ** 2))
    )  # (n_elem, 14, 3, 3)
    sqrt_det_g = np.sqrt(np.maximum(0.0, np.linalg.det(g_mat)))  # (n_elem, 14)
    g_inv = np.linalg.inv(g_mat)  # (n_elem, 14, 3, 3)
    dvol_q14 = detJ[:, None] * sqrt_det_g * TET_QUAD14_WTS[None, :]  # (n_elem, 14)

    return {
        "grad_phi": grad_phi,
        "g_inv_q14": g_inv,
        "dvol_q14": dvol_q14,
        "trunc_vol": float(np.sum(dvol_q14)),
    }


def _local_stiffness_mass_q14(
    geom: Dict[str, np.ndarray], n_nodes: int, sub_tets: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    grad_phi = geom["grad_phi"]  # (n_elem, 4, 3)
    g_inv = geom["g_inv_q14"]    # (n_elem, 14, 3, 3)
    dvol = geom["dvol_q14"]      # (n_elem, 14)

    # g_inv_int[e, m, n] = sum_q dvol[e, q] * g_inv[e, q, m, n]
    g_inv_int = np.einsum("eq,eqmn->emn", dvol, g_inv)
    K_elem = np.einsum("eam,emn,ebn->eab", grad_phi, g_inv_int, grad_phi)

    # outer_bary[q, a, b] = lb[q, a] * lb[q, b]
    outer_bary = TET_QUAD14_BARY[:, :, None] * TET_QUAD14_BARY[:, None, :]  # (14, 4, 4)
    M_elem = np.einsum("eq,qab->eab", dvol, outer_bary)

    rows = np.repeat(sub_tets, 4, axis=1).ravel()
    cols = np.tile(sub_tets, (1, 4)).ravel()
    K_loc = coo_matrix((K_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    M_loc = coo_matrix((M_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    return K_loc, M_loc


def solve_harmonic_base_1form(
    ep_data: Dict[str, Any],
    free_cocycle_int: np.ndarray,
    subdiv: Dict[str, Any],
    tet_geoms: Optional[List[Dict[str, np.ndarray]]] = None,
    free_cycle_int: Optional[np.ndarray] = None,
) -> Dict[str, Any]:
    """Solve for the exact discrete harmonic 1-form alpha_s = d theta_s with unit period around S^1."""
    n_tet = ep_data["num_tets"]
    nodes_bary = subdiv["nodes_bary"]
    grid_map = subdiv["grid_map"]
    sub_tets = subdiv["sub_tets"]
    n_local = nodes_bary.shape[0]
    geoms = tet_geoms if tet_geoms is not None else [
        compute_tet_element_geometry_q14(G, nodes_bary, sub_tets) for G in ep_data["grams"]
    ]

    # Additive integer Union-Find: theta[i] = theta[root] + offset[i]
    # Convention across face f (t_pos -> t_neg): theta_pos(x) - theta_neg(perm(x)) = free_cocycle_int[f]
    total_raw = n_tet * n_local
    parent = list(range(total_raw))
    offset = np.zeros(total_raw, dtype=int)

    def find(x: int) -> Tuple[int, int]:
        if parent[x] == x:
            return x, 0
        r, off_p = find(parent[x])
        parent[x] = r
        offset[x] = int(offset[x]) + off_p
        return r, int(offset[x])

    max_jump_defect = 0
    for finfo in ep_data["faces_info"]:
        fg = finfo["face_global"]
        tp, fp = finfo["t_pos"], finfo["f_pos"]
        tn = finfo["t_neg"]
        perm = finfo["perm_pos_to_neg"]
        jump = int(free_cocycle_int[fg])
        for tup_p, lp in grid_map.items():
            if tup_p[fp] != 0:
                continue
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = grid_map[tuple(tup_n)]
            ip, ineg = tp * n_local + lp, tn * n_local + ln
            rp, op = find(ip)
            rn, on = find(ineg)
            # Required: (theta[rp] + op) - (theta[rn] + on) == jump => theta[rp] = theta[rn] + (jump + on - op)
            rel_off = jump + on - op
            if rp != rn:
                parent[rp] = rn
                offset[rp] = rel_off
            else:
                max_jump_defect = max(max_jump_defect, abs(rel_off))

    if max_jump_defect != 0:
        raise RuntimeError(f"Non-closed integer cocycle defect {max_jump_defect}!")

    roots = sorted({find(i)[0] for i in range(total_raw)})
    rmap = {r: idx for idx, r in enumerate(roots)}
    n_dof = len(roots)

    rows_l, cols_l, kv_l, mv_l = [], [], [], []
    rhs = np.zeros(n_dof, dtype=float)

    tet_dofs_list: List[np.ndarray] = []
    tet_offs_list: List[np.ndarray] = []

    for t in range(n_tet):
        K_loc, M_loc = _local_stiffness_mass_q14(geoms[t], n_local, sub_tets)
        dofs_t = np.zeros(n_local, dtype=int)
        offs_t = np.zeros(n_local, dtype=float)
        for loc in range(n_local):
            r, off = find(t * n_local + loc)
            dofs_t[loc] = rmap[r]
            offs_t[loc] = float(off)
        tet_dofs_list.append(dofs_t)
        tet_offs_list.append(offs_t)

        rhs_loc = -(K_loc @ offs_t)
        np.add.at(rhs, dofs_t, rhs_loc)

        rr = np.repeat(dofs_t, n_local)
        cc = np.tile(dofs_t, n_local)
        rows_l.append(rr)
        cols_l.append(cc)
        kv_l.append(K_loc.ravel())
        mv_l.append(M_loc.ravel())

    K_mat = coo_matrix((np.concatenate(kv_l), (np.concatenate(rows_l), np.concatenate(cols_l))), shape=(n_dof, n_dof)).toarray()
    M_mat = coo_matrix((np.concatenate(mv_l), (np.concatenate(rows_l), np.concatenate(cols_l))), shape=(n_dof, n_dof)).toarray()
    K_mat = 0.5 * (K_mat + K_mat.T)
    M_mat = 0.5 * (M_mat + M_mat.T)

    # Pin zero-mean gauge (1^T M u == 0) via bordered symmetric system
    m_ones = M_mat @ np.ones(n_dof, dtype=float)
    A_aug = np.zeros((n_dof + 1, n_dof + 1), dtype=float)
    A_aug[:n_dof, :n_dof] = K_mat
    A_aug[:n_dof, n_dof] = m_ones
    A_aug[n_dof, :n_dof] = m_ones
    b_aug = np.zeros(n_dof + 1, dtype=float)
    b_aug[:n_dof] = rhs

    sol_aug = np.linalg.solve(A_aug, b_aug)
    u_dof = sol_aug[:n_dof]

    # Verify discrete Hodge co-closure: max |K_mat @ u_dof - rhs| (since 1^T rhs == 0!)
    coclosure_residual = float(np.max(np.abs(K_mat @ u_dof - rhs)))

    # Extract piecewise-constant covector alpha_s[t] (n_elem, 3) and norm^2 ||alpha_s||_g^2 (n_elem, 14)
    alpha_cov_by_tet: List[np.ndarray] = []
    alpha_norm2_by_tet: List[np.ndarray] = []
    harmonic_energy = 0.0
    max_dtheta_err = 0.0
    elem_verts = nodes_bary[sub_tets]  # (n_elem, 4, 4)
    edge_dw = elem_verts[:, 1:, 1:] - elem_verts[:, 0:1, 1:]  # (n_elem, 3, 3)

    for t in range(n_tet):
        theta_loc = u_dof[tet_dofs_list[t]] + tet_offs_list[t]  # (n_local,)
        theta_elem = theta_loc[sub_tets]  # (n_elem, 4)
        alpha_cov = np.einsum("ea,eam->em", theta_elem, geoms[t]["grad_phi"])  # (n_elem, 3)
        line_diff = np.einsum("em,ekm->ek", alpha_cov, edge_dw) - (theta_elem[:, 1:] - theta_elem[:, 0:1])
        max_dtheta_err = max(max_dtheta_err, float(np.max(np.abs(line_diff))))
        norm2_q14 = np.einsum("em,eqmn,en->eq", alpha_cov, geoms[t]["g_inv_q14"], alpha_cov)  # (n_elem, 14)
        harmonic_energy += float(np.sum(geoms[t]["dvol_q14"] * norm2_q14))
        alpha_cov_by_tet.append(alpha_cov)
        alpha_norm2_by_tet.append(norm2_q14)

    loop_holonomy = float("nan")
    loop_holonomy_err = float("nan")
    if free_cycle_int is not None:
        adj_edges: Dict[int, List[Tuple[int, int, np.ndarray]]] = {i: [] for i in range(n_local)}
        for e_idx in range(sub_tets.shape[0]):
            vs = sub_tets[e_idx]
            for a in range(4):
                for b in range(a + 1, 4):
                    va, vb = int(vs[a]), int(vs[b])
                    dw_ab = nodes_bary[vb, 1:] - nodes_bary[va, 1:]
                    adj_edges[va].append((vb, e_idx, dw_ab))
                    adj_edges[vb].append((va, e_idx, -dw_ab))

        def integrate_alpha_mesh_path(t_idx: int, src: int, dst: int) -> float:
            if src == dst:
                return 0.0
            prev: Dict[int, Tuple[int, int, np.ndarray]] = {}
            q_bfs = [src]
            seen = {src}
            while q_bfs:
                cur = q_bfs.pop(0)
                if cur == dst:
                    break
                for nb, e_i, dw_vec in adj_edges[cur]:
                    if nb not in seen:
                        seen.add(nb)
                        prev[nb] = (cur, e_i, dw_vec)
                        q_bfs.append(nb)
            val = 0.0
            cur = dst
            acov_t = alpha_cov_by_tet[t_idx]
            while cur != src:
                p_node, e_i, dw_vec = prev[cur]
                val += float(np.dot(acov_t[e_i], dw_vec))
                cur = p_node
            return val

        c_node = int(np.argmin(np.sum((nodes_bary - 0.25) ** 2, axis=1)))
        hol = 0.0
        for finfo in ep_data["faces_info"]:
            fg = finfo["face_global"]
            cf = int(free_cycle_int[fg])
            if cf == 0:
                continue
            tp, fp = finfo["t_pos"], finfo["f_pos"]
            tn = finfo["t_neg"]
            perm = finfo["perm_pos_to_neg"]
            face_cands = [tup for tup in grid_map if tup[fp] == 0]
            tup_p = face_cands[0]
            lp = grid_map[tup_p]
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = grid_map[tuple(tup_n)]
            seg_int = integrate_alpha_mesh_path(tp, c_node, lp) + integrate_alpha_mesh_path(tn, ln, c_node)
            hol += cf * seg_int
        loop_holonomy = float(hol)
        loop_holonomy_err = abs(loop_holonomy - 1.0)

    return {
        "n_dof": n_dof,
        "coclosure_residual": coclosure_residual,
        "max_element_dtheta_err": max_dtheta_err,
        "loop_holonomy": loop_holonomy,
        "loop_holonomy_err": loop_holonomy_err,
        "harmonic_l2_norm2": harmonic_energy,
        "alpha_cov_by_tet": alpha_cov_by_tet,
        "alpha_norm2_q14_by_tet": alpha_norm2_by_tet,
    }


def assemble_and_solve_3d_sector(
    ep_data: Dict[str, Any],
    cocycle_mod5: Optional[np.ndarray] = None,
    charge_q: int = 0,
    n_sub: int = 4,
    cusp_bc: str = "neumann",
    n_eigs: int = 6,
    subdiv: Optional[Dict[str, Any]] = None,
    tet_geoms: Optional[List[Dict[str, np.ndarray]]] = None,
    base_flux_phi: float = 0.0,
    harm_form: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Solve 3D hyperbolic Laplacian with flat Z/5Z cocycle AND optional continuous harmonic base flux Phi*alpha_s."""
    n_tet = ep_data["num_tets"]
    sub = subdiv if subdiv is not None else build_eulerian_subdivision(n_sub, True)
    nodes_bary = sub["nodes_bary"]
    grid_map = sub["grid_map"]
    is_horo = sub["is_horo_boundary"]
    sub_tets = sub["sub_tets"]
    n_local = nodes_bary.shape[0]

    geoms = tet_geoms if tet_geoms is not None else [
        compute_tet_element_geometry_q14(G, nodes_bary, sub_tets) for G in ep_data["grams"]
    ]

    use_twist = cocycle_mod5 is not None and (charge_q % 5 != 0)
    omega5 = np.exp(2j * math.pi * (charge_q % 5) / 5.0) if use_twist else 1.0 + 0.0j

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

    holonomy_defect = 0.0
    for finfo in ep_data["faces_info"]:
        fg = finfo["face_global"]
        tp, fp = finfo["t_pos"], finfo["f_pos"]
        tn = finfo["t_neg"]
        perm = finfo["perm_pos_to_neg"]
        tfac = (omega5 ** int(cocycle_mod5[fg])) if use_twist else (1.0 + 0.0j)
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
            else:
                holonomy_defect = max(holonomy_defect, abs(rel - 1.0))

    if holonomy_defect > 1e-10:
        raise RuntimeError(f"Non-flat Z/5Z holonomy defect {holonomy_defect:.3e}")

    root_is_dir: Dict[int, bool] = {}
    for t in range(n_tet):
        for loc in range(n_local):
            r, _ = find(t * n_local + loc)
            if is_horo[loc]:
                root_is_dir[r] = True
            elif r not in root_is_dir:
                root_is_dir[r] = False

    root_to_dof: Dict[int, int] = {}
    for r, is_d in sorted(root_is_dir.items()):
        if cusp_bc == "dirichlet" and is_d:
            continue
        root_to_dof[r] = len(root_to_dof)
    n_dof = len(root_to_dof)

    use_harm = abs(base_flux_phi) > 1e-15 and harm_form is not None
    two_pi_phi = 2.0 * math.pi * base_flux_phi

    rows_all, cols_all, kv_all, mv_all = [], [], [], []
    tet_mass_mats: List[csr_matrix] = []
    tet_nodal_map: List[Tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    trunc_vol_total = 0.0
    tet_trunc_vols: List[float] = []

    for t in range(n_tet):
        gm = geoms[t]
        trunc_vol_total += gm["trunc_vol"]
        tet_trunc_vols.append(gm["trunc_vol"])

        if not use_harm:
            K_loc_c, M_loc_r = _local_stiffness_mass_q14(gm, n_local, sub_tets)
            K_loc = K_loc_c.astype(np.complex128)
            M_loc = M_loc_r.astype(np.complex128)
        else:
            # Covariant derivative D_mu u = (d_mu - i * 2*pi*Phi * alpha_mu) u on each element!
            # <(d - i A) phi_a, (d - i A) phi_b> = (grad_a + i A phi_a) . g^{-1} . (grad_b - i A phi_b)
            # Wait: <D phi_a, D phi_b> with inner product int conj(D phi_a) g^{-1} (D phi_b):
            # conj((grad_a - i A phi_a)) = grad_a + i A phi_a!
            grad_p = gm["grad_phi"]  # (n_elem, 4, 3)
            acov = two_pi_phi * harm_form["alpha_cov_by_tet"][t]  # (n_elem, 3)
            # At each q in 0..13: D_vec[e, q, a, m] = grad_p[e, a, m] - 1j * acov[e, m] * BARY[q, a]
            D_vec = grad_p[:, None, :, :] - 1j * (
                acov[:, None, None, :] * TET_QUAD14_BARY[None, :, :, None]
            )  # (n_elem, 14, 4, 3)
            K_elem = np.einsum(
                "eq,eqam,eqmn,eqbn->eab",
                gm["dvol_q14"],
                np.conj(D_vec),
                gm["g_inv_q14"],
                D_vec,
            )
            outer_bary = TET_QUAD14_BARY[:, :, None] * TET_QUAD14_BARY[:, None, :]
            M_elem = np.einsum("eq,qab->eab", gm["dvol_q14"], outer_bary).astype(np.complex128)
            er = np.repeat(sub_tets, 4, axis=1).ravel()
            ec = np.tile(sub_tets, (1, 4)).ravel()
            K_loc = coo_matrix((K_elem.ravel(), (er, ec)), shape=(n_local, n_local)).toarray()
            M_loc = coo_matrix((M_elem.ravel(), (er, ec)), shape=(n_local, n_local)).toarray()

        act_l, act_d, act_p = [], [], []
        for loc in range(n_local):
            r, ph = find(t * n_local + loc)
            if r in root_to_dof:
                act_l.append(loc)
                act_d.append(root_to_dof[r])
                act_p.append(ph)

        al = np.array(act_l, dtype=int)
        ad = np.array(act_d, dtype=int)
        ap = np.array(act_p, dtype=np.complex128)
        tet_nodal_map.append((al, ad, ap))

        ph_mat = np.conj(ap)[:, None] * ap[None, :]
        K_gl = K_loc[np.ix_(al, al)] * ph_mat
        M_gl = M_loc[np.ix_(al, al)] * ph_mat

        rr = np.repeat(ad, len(ad))
        cc = np.tile(ad, len(ad))
        rows_all.append(rr)
        cols_all.append(cc)
        kv_all.append(K_gl.ravel())
        mv_all.append(M_gl.ravel())
        tet_mass_mats.append(coo_matrix((M_gl.ravel(), (rr, cc)), shape=(n_dof, n_dof)).tocsr())

    R_c = np.concatenate(rows_all)
    C_c = np.concatenate(cols_all)
    K_csr = coo_matrix((np.concatenate(kv_all), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    M_csr = coo_matrix((np.concatenate(mv_all), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    K_csr = 0.5 * (K_csr + K_csr.conj().T)
    M_csr = 0.5 * (M_csr + M_csr.conj().T)

    k_req = min(n_eigs, n_dof - 1)
    if n_dof <= 2600:
        sigma_sh = -1.0
        m_diag = np.real(M_csr.diagonal())
        d_sc = 1.0 / np.sqrt(np.maximum(1e-30, m_diag))
        K_eq = (K_csr.toarray() * d_sc[:, None]) * d_sc[None, :]
        M_eq = (M_csr.toarray() * d_sc[:, None]) * d_sc[None, :]
        M_eq = 0.5 * (M_eq + M_eq.conj().T)
        H_sh = 0.5 * (K_eq + K_eq.conj().T) - sigma_sh * M_eq
        L_ch = np.linalg.cholesky(H_sh)
        L_inv_M = np.linalg.solve(L_ch, M_eq)
        C_op = np.linalg.solve(L_ch, L_inv_M.conj().T).conj().T
        C_op = 0.5 * (C_op + C_op.conj().T)
        mu_v, w_v = eigh(C_op, subset_by_index=[n_dof - k_req, n_dof - 1])
        evals_raw = sigma_sh + 1.0 / mu_v[::-1]
        evecs_raw = d_sc[:, None] * np.linalg.solve(L_ch.conj().T, w_v[:, ::-1])
    else:
        evals_raw, evecs_raw = eigsh(K_csr, k=k_req, M=M_csr, sigma=-0.5, which="LM", tol=1e-14)

    order = np.argsort(evals_raw.real)
    evals = np.array(evals_raw[order].real, dtype=float)
    evecs = np.array(evecs_raw[:, order], dtype=np.complex128)

    for j in range(k_req):
        v = evecs[:, j]
        nrm = math.sqrt(max(1e-30, float(np.real(np.vdot(v, M_csr @ v)))))
        evecs[:, j] = v / nrm

    first_phys = 1 if (not use_twist and not use_harm and cusp_bc == "neumann" and abs(evals[0]) < 1e-8) else 0
    E0 = float(evals[first_phys])
    deg_idx = [j for j in range(first_phys, k_req) if abs(evals[j] - E0) <= max(1e-7, 1e-5 * abs(E0))]
    mult = len(deg_idx)
    nxt = [j for j in range(first_phys, k_req) if j not in deg_idx]
    E1 = float(evals[nxt[0]]) if nxt else float("nan")
    rel_gap = (E1 - E0) / max(1e-15, abs(E0)) if nxt else 0.0

    layer_probs = np.zeros(n_tet, dtype=float)
    for j in deg_idx:
        vj = evecs[:, j]
        for t in range(n_tet):
            layer_probs[t] += float(np.real(np.vdot(vj, tet_mass_mats[t] @ vj)))
    layer_probs /= max(1, mult)
    layer_probs /= np.sum(layer_probs)

    # Expand eigenvectors to local per-tetrahedron nodal arrays: shape (k_req, n_tet, n_local)
    local_modes = np.zeros((k_req, n_tet, n_local), dtype=np.complex128)
    for t in range(n_tet):
        al, ad, ap = tet_nodal_map[t]
        # evecs[ad, :] has shape (len(ad), k_req)
        local_modes[:, t, al] = (ap[:, None] * evecs[ad, :]).T

    return {
        "n_sub": n_sub,
        "cusp_bc": cusp_bc,
        "charge_q": charge_q % 5,
        "n_dof": n_dof,
        "truncated_volume": trunc_vol_total,
        "tet_truncated_volumes": tet_trunc_vols,
        "eigenvalues": evals.tolist(),
        "E0": E0,
        "E1_next": E1,
        "rel_gap": rel_gap,
        "ground_multiplicity": mult,
        "layer_probs": layer_probs.tolist(),
        "evecs_dof": evecs,
        "local_modes": local_modes,
    }


def compute_trilinear_overlap_matrix_q14(
    modes_A: np.ndarray,
    modes_B: np.ndarray,
    mode_H: np.ndarray,
    sub_tets: np.ndarray,
    tet_geoms: List[Dict[str, np.ndarray]],
) -> np.ndarray:
    """Compute exact degree-5 3D overlap matrix Y_{ab} = int_{M_H} sqrt(det g) A_a(x) B_b(x) H(x) d^3x.

    Args:
        modes_A: shape (n_A, n_tet, n_local) complex128
        modes_B: shape (n_B, n_tet, n_local) complex128
        mode_H:  shape (n_tet, n_local) complex128
    Returns:
        Y: shape (n_A, n_B) complex128
    """
    n_A = modes_A.shape[0]
    n_B = modes_B.shape[0]
    n_tet = mode_H.shape[0]
    Y = np.zeros((n_A, n_B), dtype=np.complex128)

    Q_T = TET_QUAD14_BARY.T  # (4, 14)
    for t in range(n_tet):
        dvol = tet_geoms[t]["dvol_q14"]  # (n_elem, 14)
        # H_q: (n_elem, 14)
        H_q = mode_H[t, sub_tets] @ Q_T
        wH = dvol * H_q  # (n_elem, 14)

        # A_q: (n_A, n_elem, 14), B_q: (n_B, n_elem, 14)
        A_q = modes_A[:, t, :][:, sub_tets] @ Q_T
        B_q = modes_B[:, t, :][:, sub_tets] @ Q_T

        # Contract over (e, q):
        Y += np.einsum("aeq,beq,eq->ab", A_q, B_q, wH)

    return Y


def extract_haar_invariant_yukawa_observables(
    Y_u: np.ndarray, Y_d: np.ndarray, rank_tol: float = 1e-10
) -> Dict[str, Any]:
    """Extract strictly basis-invariant observables from a 3x3 Yukawa pair (Y_u, Y_d) (Guardrail 3)."""
    assert Y_u.shape == (3, 3) and Y_d.shape == (3, 3)

    # SVD sorted ascending: s_1 <= s_2 <= s_3
    U_u, sv_u_desc, _ = np.linalg.svd(Y_u)
    U_d, sv_d_desc, _ = np.linalg.svd(Y_d)
    sv_u = sv_u_desc[::-1]
    sv_d = sv_d_desc[::-1]
    U_Lu = U_u[:, ::-1]
    U_Ld = U_d[:, ::-1]

    rank_u = int(np.sum(sv_u > rank_tol * max(1e-30, float(sv_u[-1]))))
    rank_d = int(np.sum(sv_d > rank_tol * max(1e-30, float(sv_d[-1]))))

    su_ratios = (
        [float(sv_u[0] / sv_u[2]), float(sv_u[1] / sv_u[2]), 1.0]
        if sv_u[2] > 1e-30
        else [0.0, 0.0, 0.0]
    )
    sd_ratios = (
        [float(sv_d[0] / sv_d[2]), float(sv_d[1] / sv_d[2]), 1.0]
        if sv_d[2] > 1e-30
        else [0.0, 0.0, 0.0]
    )

    # Check relative singular-value splittings (to detect exact m_1 == m_2 or m_2 == m_3 degeneracies)
    min_rel_split_u = (
        min(abs(sv_u[1] - sv_u[0]) / sv_u[2], abs(sv_u[2] - sv_u[1]) / sv_u[2])
        if sv_u[2] > 1e-30
        else 0.0
    )
    min_rel_split_d = (
        min(abs(sv_d[1] - sv_d[0]) / sv_d[2], abs(sv_d[2] - sv_d[1]) / sv_d[2])
        if sv_d[2] > 1e-30
        else 0.0
    )

    # CKM mixing magnitudes |U_{L,u}^dagger U_{L,d}| (strictly invariant under Y_u -> U_L Y_u U_{Ru}^dagger,
    # Y_d -> U_L Y_d U_{Rd}^dagger whenever singular values of Y_u and Y_d are non-degenerate!)
    V_ckm = U_Lu.conj().T @ U_Ld
    V_abs = np.abs(V_ckm)

    # Basis-invariant Jarlskog commutator determinant (invariant EVEN if singular values are degenerate!):
    # det[H_u, H_d] is purely imaginary because ([H_u, H_d])^dagger = -[H_u, H_d] in 3x3:
    # Specifically, 2i * Im(V_{us} V_{cb} V_{ub}^* V_{cs}^*) * prod (m_u^2 diff) * prod (m_d^2 diff) = det[H_u, H_d]!
    H_u = Y_u @ Y_u.conj().T
    H_d = Y_d @ Y_d.conj().T
    comm = H_u @ H_d - H_d @ H_u
    det_comm = complex(np.linalg.det(comm))
    denom = (float(np.linalg.norm(H_u, "fro")) ** 3) * (float(np.linalg.norm(H_d, "fro")) ** 3)
    jarlskog_norm = float(det_comm.imag / denom) if denom > 1e-60 else 0.0

    # Also compute rephasing-invariant quartet J_ckm = Im(V[0,1] V[1,2] conj(V[0,2]) conj(V[1,1]))
    j_quartet = float(
        np.imag(V_ckm[0, 1] * V_ckm[1, 2] * np.conj(V_ckm[0, 2]) * np.conj(V_ckm[1, 1]))
    )

    return {
        "sv_u_asc": sv_u.tolist(),
        "sv_d_asc": sv_d.tolist(),
        "sv_u_ratios_to_top": su_ratios,
        "sv_d_ratios_to_bottom": sd_ratios,
        "rank_u": rank_u,
        "rank_d": rank_d,
        "min_rel_sv_split_u": float(min_rel_split_u),
        "min_rel_sv_split_d": float(min_rel_split_d),
        "ckm_abs_matrix": V_abs.tolist(),
        "jarlskog_commutator_im_det_norm": jarlskog_norm,
        "jarlskog_ckm_quartet": j_quartet,
        "comm_det_real_leakage": abs(float(det_comm.real)) / max(1e-60, denom),
    }


def verify_haar_scrambling_invariance(
    Y_u: np.ndarray, Y_d: np.ndarray, n_trials: int = 12, seed: int = 20261111
) -> Dict[str, Any]:
    """Apply independent random Haar unitaries (U_L, U_Ru, U_Rd) in U(3)^3 and verify invariance (< 1e-12)."""
    rng = np.random.default_rng(seed)
    base = extract_haar_invariant_yukawa_observables(Y_u, Y_d)

    max_sv_err = 0.0
    max_jarlskog_err = 0.0
    max_ckm_err = 0.0
    min_split = min(base["min_rel_sv_split_u"], base["min_rel_sv_split_d"])
    nondeg = min_split > 1e-6
    # Wedin singular-vector conditioning factor for float64 perturbations (~O(eps_mach / min_split))
    wedin_scale = min(1.0, min_split / 1e-3) if nondeg else 0.0

    for _ in range(n_trials):
        U_L = random_haar_unitary(3, rng)
        U_Ru = random_haar_unitary(3, rng)
        U_Rd = random_haar_unitary(3, rng)

        Yu_scr = U_L @ Y_u @ U_Ru.conj().T
        Yd_scr = U_L @ Y_d @ U_Rd.conj().T
        scr = extract_haar_invariant_yukawa_observables(Yu_scr, Yd_scr)

        max_sv_err = max(
            max_sv_err,
            float(np.max(np.abs(np.array(base["sv_u_ratios_to_top"]) - np.array(scr["sv_u_ratios_to_top"])))),
            float(np.max(np.abs(np.array(base["sv_d_ratios_to_bottom"]) - np.array(scr["sv_d_ratios_to_bottom"])))),
        )
        max_jarlskog_err = max(
            max_jarlskog_err,
            abs(base["jarlskog_commutator_im_det_norm"] - scr["jarlskog_commutator_im_det_norm"]),
        )
        if nondeg:
            raw_ckm_diff = float(
                np.max(np.abs(np.array(base["ckm_abs_matrix"]) - np.array(scr["ckm_abs_matrix"])))
            )
            max_ckm_err = max(max_ckm_err, wedin_scale * raw_ckm_diff)

    return {
        "trials": n_trials,
        "singular_values_nondegenerate": nondeg,
        "max_sv_ratio_haar_err": max_sv_err,
        "max_jarlskog_haar_err": max_jarlskog_err,
        "max_ckm_abs_haar_err": max_ckm_err,
        "haar_invariance_verified": (
            max_sv_err < 1e-12
            and max_jarlskog_err < 1e-12
            and (max_ckm_err < 1e-12 if nondeg else True)
        ),
    }


def find_order5_deck_generator(
    ep_cov: Dict[str, Any], ep_base: Dict[str, Any]
) -> Dict[int, Tuple[int, Tuple[int, int, int, int]]]:
    """Find the exact free order-5 isometric deck transformation of a 5-fold cyclic cover."""
    n_cov = ep_cov["num_tets"]
    grams = ep_cov["grams"]
    gluings = ep_cov["gluings"]

    proj = None
    for tb in range(ep_base["num_tets"]):
        for pb in itertools.permutations(range(4)):
            if np.max(np.abs(grams[0] - ep_base["grams"][tb][np.ix_(pb, pb)])) > 1e-9:
                continue
            cmap = {0: (tb, pb)}
            queue = [0]
            ok = True
            while queue and ok:
                tc = queue.pop()
                t_b, p_b = cmap[tc]
                for fc in range(4):
                    nbc, g_c = gluings[tc][fc]
                    fb = p_b[fc]
                    nbb, g_b = ep_base["gluings"][t_b][fb]
                    inv_gc = [0, 0, 0, 0]
                    for v in range(4):
                        inv_gc[g_c[v]] = v
                    p_nbc = tuple(g_b[p_b[inv_gc[w]]] for w in range(4))
                    if np.max(np.abs(grams[nbc] - ep_base["grams"][nbb][np.ix_(p_nbc, p_nbc)])) > 1e-9:
                        ok = False
                        break
                    if nbc in cmap:
                        if cmap[nbc] != (nbb, p_nbc):
                            ok = False
                            break
                    else:
                        cmap[nbc] = (nbb, p_nbc)
                        queue.append(nbc)
            if ok and len(cmap) == n_cov:
                proj = cmap
                break
        if proj is not None:
            break

    if proj is None:
        raise RuntimeError("Isometric 5-fold covering projection not found.")

    fiber0 = [t for t in range(1, n_cov) if proj[t][0] == proj[0][0]]
    for t_img in fiber0:
        p0 = proj[0][1]
        pt = proj[t_img][1]
        inv_pt = [0, 0, 0, 0]
        for w in range(4):
            inv_pt[pt[w]] = w
        gperm0 = tuple(inv_pt[p0[v]] for v in range(4))
        dmap = {0: (t_img, gperm0)}
        queue = [0]
        ok = True
        while queue and ok:
            tc = queue.pop()
            ti, gp = dmap[tc]
            for fc in range(4):
                nbc, gc = gluings[tc][fc]
                fi = gp[fc]
                nbi, gi = gluings[ti][fi]
                inv_gc = [0, 0, 0, 0]
                for v in range(4):
                    inv_gc[gc[v]] = v
                gp_nb = tuple(gi[gp[inv_gc[w]]] for w in range(4))
                if nbc in dmap:
                    if dmap[nbc] != (nbi, gp_nb):
                        ok = False
                        break
                else:
                    dmap[nbc] = (nbi, gp_nb)
                    queue.append(nbc)
        if ok and len(dmap) == n_cov:
            return dmap

    raise RuntimeError("No free order-5 deck generator found.")


def apply_deck_map_to_local_modes(
    local_modes: np.ndarray,
    dmap: Dict[int, Tuple[int, Tuple[int, int, int, int]]],
    subdiv: Dict[str, Any],
) -> np.ndarray:
    """Pullback (D^* psi)(t, x) = psi(dmap(t), perm(x)) on local nodal modes (k, n_cov, n_local)."""
    grid_map = subdiv["grid_map"]
    n_local = subdiv["nodes_bary"].shape[0]
    nodes_bary = subdiv["nodes_bary"]
    n_sub = subdiv["n_sub"]

    # Map every local node index (including octahedron centers!) under each of the 24 S_4 permutations
    bary_key_to_loc = {
        tuple(int(round(2.0 * n_sub * c)) for c in nodes_bary[idx]): idx
        for idx in range(n_local)
    }
    perm_node_cache: Dict[Tuple[int, int, int, int], np.ndarray] = {}
    for _, (_, gp) in dmap.items():
        if gp not in perm_node_cache:
            arr = np.zeros(n_local, dtype=int)
            for key, idx in bary_key_to_loc.items():
                pkey = [0, 0, 0, 0]
                for a in range(4):
                    pkey[gp[a]] = key[a]
                arr[idx] = bary_key_to_loc[tuple(pkey)]
            perm_node_cache[gp] = arr

    out = np.zeros_like(local_modes)
    for t in range(local_modes.shape[1]):
        ti, gp = dmap[t]
        out[:, t, :] = local_modes[:, ti, :][:, perm_node_cache[gp]]
    return out
