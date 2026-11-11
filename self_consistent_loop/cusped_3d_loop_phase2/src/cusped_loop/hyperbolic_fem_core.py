"""Exact 3D Cusped Hyperbolic Geometry & Simplicial P1 Finite-Element Core.

Constructs intrinsic Riemannian hyperbolic metrics directly from SnapPyHP
quad-precision ideal triangulations via Epstein-Penner horotriangle lambda-lengths,
computes exact 24-cone cusp-desingularized hyperbolic volumes, classifies flat
Z/5Z cohomology cocycles via Poincaré-Lefschetz dual chain complexes, and solves
the 3D twisted Laplace-Beltrami eigenvalue problem on S_4-symmetric Eulerian meshes.
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.linalg import eigh, null_space
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh
from scipy.special import roots_legendre, spence
import snappy
from snappy.geometric_structure.cusp_neighborhood.complex_cusp_cross_section import (
    ComplexCuspCrossSection,
)


VBITS = (1, 2, 4, 8)
FBITS = (14, 13, 11, 7)


def gauss_reduce_tau(tau: complex, tol: float = 1e-13) -> complex:
    """Map tau in H into the standard PSL(2, Z) fundamental domain F."""
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
    # Canonical boundary tie-breaking: Re(z) in (-0.5, +0.5], and if |z|==1, Re(z) >= 0
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
    sol_type = M.solution_type()

    shapes_hp = M.tetrahedra_shapes("rect")
    shapes = [complex(z) for z in shapes_hp]
    ccs = ComplexCuspCrossSection.fromManifoldAndShapes(M, shapes_hp)
    ccs.normalize_cusps()

    n_tet = len(ccs.mcomplex.Tetrahedra)
    grams: List[np.ndarray] = []
    gluings: List[List[Tuple[int, Tuple[int, int, int, int]]]] = []
    horo_min_edge: List[float] = []
    horo_mean_edge: List[float] = []
    tet_bw_vols: List[float] = []
    tet_canonical_taus: List[complex] = []

    max_intra_err = 0.0
    for T in ccs.mcomplex.Tetrahedra:
        G = np.zeros((4, 4), dtype=float)
        all_h_lens: List[float] = []
        for v_b in VBITS:
            for val in T.horotriangles[v_b].lengths.values():
                all_h_lens.append(float(abs(val)))
        horo_min_edge.append(min(all_h_lens))
        horo_mean_edge.append(float(np.mean(all_h_lens)))

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
            N_tet_obj = T.Neighbor[Fb]
            perm = T.Gluing[Fb]
            g_row.append((N_tet_obj.Index, (perm[0], perm[1], perm[2], perm[3])))
        gluings.append(g_row)

        zt = shapes[T.Index]
        tet_bw_vols.append(bloch_wigner_volume(zt))
        tet_canonical_taus.append(gauss_reduce_tau(zt) if zt.imag > 1e-14 else complex(0.0, 1.0))

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

    # Map each oriented Face k in mcomplex.Faces (0..2*n_tet-1) to its two incident (tet, face_idx) corners
    fbit_to_idx = {14: 0, 13: 1, 11: 2, 7: 3}
    faces_info: List[Dict[str, Any]] = []
    for f_global, F_obj in enumerate(ccs.mcomplex.Faces):
        c0, c1 = F_obj.Corners[0], F_obj.Corners[1]
        t0, fi0 = c0.Tetrahedron.Index, fbit_to_idx[c0.Subsimplex]
        t1, fi1 = c1.Tetrahedron.Index, fbit_to_idx[c1.Subsimplex]
        nb0, perm0 = gluings[t0][fi0]
        assert nb0 == t1, f"Face corner neighbor mismatch: {nb0} != {t1}"
        # Verify sign in d3[f_global]: d3[f_global, t0] - d3[f_global, t1] when t0 != t1
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

    return {
        "name": name,
        "manifold": M,
        "solution_type": sol_type,
        "num_tets": n_tet,
        "num_cusps": M.num_cusps(),
        "homology_str": str(M.homology()),
        "homology_divisors": [int(d) for d in M.homology().elementary_divisors()],
        "snappy_volume": float(M.volume()),
        "chern_simons": cs_val,
        "complex_volume": complex(M.complex_volume()),
        "cusp_moduli": cusp_moduli,
        "shapes": shapes,
        "tet_bw_volumes": tet_bw_vols,
        "tet_canonical_taus": tet_canonical_taus,
        "horo_min_edge": horo_min_edge,
        "horo_mean_edge": horo_mean_edge,
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
    invA = np.linalg.inv(Gdiff)
    adjA = detA * invA

    total = 0.0
    for i0, i1, i2, i3 in itertools.permutations(range(4)):
        p0 = c
        p1 = (e[i1] + e[i2] + e[i3]) / 3.0
        p2 = (e[i2] + e[i3]) / 2.0
        p3 = e[i3]

        Jmat = np.array([p1[1:] - p0[1:], p2[1:] - p0[1:], p3[1:] - p0[1:]])
        detJ = abs(float(np.linalg.det(Jmat)))

        Y = (
            (1.0 - T)[..., None] * p0
            + (T * R)[..., None] * p1
            + (T * (1.0 - R))[..., None] * p2
        )
        YG = np.einsum("...a,ab->...b", Y, G)
        q_yy = -np.sum(YG * Y, axis=-1)
        q_yp3 = -YG[..., i3]
        Q_hat = (1.0 - S) * q_yy + 2.0 * S * q_yp3

        W = (1.0 - S)[..., None] * Y + S[..., None] * p3
        dQ = -2.0 * np.einsum("mb,...b->...m", Dmat, W)
        u_adj_u = np.einsum("...m,mn,...n->...", dQ, adjA, dQ)

        det_g_times_omS4 = ((1.0 - S) * Q_hat * detA + 0.25 * u_adj_u) / (Q_hat ** 4)
        sqrt_det_g_times_omS2 = np.sqrt(np.maximum(0.0, det_g_times_omS4))
        total += float(np.sum(detJ * T * sqrt_det_g_times_omS2 * WS * WT * WR))
    return total


def _integer_snf_with_inverses(
    A_in: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Exact arbitrary-precision integer Smith Normal Form U @ A_in @ V = S,
    returning (U, U_inv, S, V, V_inv) in dtype=object with zero float overflow.
    """
    A = np.array(A_in, dtype=object)
    m, n = A.shape
    U = np.eye(m, dtype=object)
    U_inv = np.eye(m, dtype=object)
    V = np.eye(n, dtype=object)
    V_inv = np.eye(n, dtype=object)

    def swap_rows(i: int, j: int) -> None:
        if i == j:
            return
        A[[i, j], :] = A[[j, i], :]
        U[[i, j], :] = U[[j, i], :]
        U_inv[:, [i, j]] = U_inv[:, [j, i]]

    def swap_cols(i: int, j: int) -> None:
        if i == j:
            return
        A[:, [i, j]] = A[:, [j, i]]
        V[:, [i, j]] = V[:, [j, i]]
        V_inv[[i, j], :] = V_inv[[j, i], :]

    def add_row(dst: int, src: int, factor: int) -> None:
        if factor == 0:
            return
        A[dst, :] = A[dst, :] + factor * A[src, :]
        U[dst, :] = U[dst, :] + factor * U[src, :]
        U_inv[:, src] = U_inv[:, src] - factor * U_inv[:, dst]

    def add_col(dst: int, src: int, factor: int) -> None:
        if factor == 0:
            return
        A[:, dst] = A[:, dst] + factor * A[:, src]
        V[:, dst] = V[:, dst] + factor * V[:, src]
        V_inv[src, :] = V_inv[src, :] - factor * V_inv[dst, :]

    r = 0
    while r < m and r < n:
        nz = [
            (i, j, abs(int(A[i, j])))
            for i in range(r, m)
            for j in range(r, n)
            if A[i, j] != 0
        ]
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
    """Count ideal vertices (cusps) of the p-fold cyclic cover defined by dual 1-cocycle `cocycle`."""
    n_tet = ep_data["num_tets"]
    total_states = n_tet * 4 * p
    parent = list(range(total_states))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    def idx(t: int, v: int, s: int) -> int:
        return (t * 4 + v) * p + (s % p)

    for finfo in ep_data["faces_info"]:
        f_glob = finfo["face_global"]
        t_pos, f_pos = finfo["t_pos"], finfo["f_pos"]
        t_neg, _ = finfo["t_neg"], finfo["f_neg"]
        perm = finfo["perm_pos_to_neg"]
        shift = int(cocycle[f_glob]) % p
        for v_pos in range(4):
            if v_pos == f_pos:
                continue
            v_neg = perm[v_pos]
            for s in range(p):
                union(idx(t_pos, v_pos, s), idx(t_neg, v_neg, (s + shift) % p))

    roots = {find(i) for i in range(total_states)}
    return len(roots)


def classify_z5_torsion_cocycles(ep_data: Dict[str, Any]) -> Dict[str, Any]:
    """Classify all projective Z/5Z cohomology lines in H^1(M; Z/5Z) via exact integer SNF."""
    d2 = ep_data["d2"]  # (n_edges, n_faces)
    d3 = ep_data["d3"]  # (n_faces, n_tets)
    n_faces = d3.shape[0]

    # Dual homology H_1(M; Z) = ker(d3^T) / im(d2^T)
    d2_obj = d2.astype(object)
    d3_obj = d3.astype(object)
    _, _, S_d3t, V_d3t, V_inv = _integer_snf_with_inverses(d3_obj.T)
    rank_d3t = sum(
        1 for k in range(min(S_d3t.shape)) if int(S_d3t[k, k]) != 0
    )
    K_basis = V_d3t[:, rank_d3t:]  # (n_faces, dim_ker) object ints

    full_coords = V_inv @ d2_obj.T
    assert all(int(x) == 0 for x in full_coords[:rank_d3t, :].ravel())
    B_coords = full_coords[rank_d3t:, :]

    U_b, U_b_inv, S_b, _, _ = _integer_snf_with_inverses(B_coords)

    # Generators of H_1(M; Z) are columns j of K_basis @ U_b_inv with invariant factors diag(S_b)[j]
    H1_gens = K_basis @ U_b_inv
    inv_factors = [
        int(S_b[j, j]) if j < min(S_b.shape) else 0 for j in range(H1_gens.shape[1])
    ]

    torsion_5_cycles_mod5: List[np.ndarray] = []
    for j, d_val in enumerate(inv_factors):
        cyc = H1_gens[:, j]
        if d_val != 0 and d_val % 5 == 0:
            cyc_5 = np.array([int(((d_val // 5) * x) % 5) for x in cyc], dtype=int)
            torsion_5_cycles_mod5.append(cyc_5)

    active_j = [j for j, d_val in enumerate(inv_factors) if d_val % 5 == 0]
    U_b_mod5 = np.array([[int(x % 5) for x in row] for row in U_b], dtype=int)
    V_inv_mod5 = np.array([[int(x % 5) for x in row] for row in V_inv], dtype=int)

    projective_lines: List[Dict[str, Any]] = []
    seen_canonical = set()
    dim_h1_mod5 = len(active_j)

    for combo in itertools.product(range(5), repeat=dim_h1_mod5):
        if all(x == 0 for x in combo):
            continue
        first_nz = next(x for x in combo if x != 0)
        inv_first = pow(first_nz, -1, 5)
        canon = tuple((x * inv_first) % 5 for x in combo)
        if canon in seen_canonical:
            continue
        seen_canonical.add(canon)

        w = np.zeros(H1_gens.shape[1], dtype=int)
        for idx_a, j_col in enumerate(active_j):
            w[j_col] = canon[idx_a]
        low_vec = (U_b_mod5.T @ w) % 5
        full_vec = np.concatenate([np.zeros(rank_d3t, dtype=int), low_vec])
        cocycle = (V_inv_mod5.T @ full_vec) % 5
        assert np.all((d2 @ cocycle) % 5 == 0), "Cocycle failed d2 @ c == 0 mod 5!"

        tors_pairings = [int((cocycle @ tc) % 5) for tc in torsion_5_cycles_mod5]
        is_torsion_nontrivial = any(tp != 0 for tp in tors_pairings)
        n_cover_cusps = _count_cover_cusps_mod_p(ep_data, cocycle, p=5)

        projective_lines.append(
            {
                "f5_coords": list(canon),
                "cocycle": cocycle,
                "torsion_pairings_mod5": tors_pairings,
                "is_torsion_nontrivial": is_torsion_nontrivial,
                "cover_num_cusps": n_cover_cusps,
                "is_cusp_unramified": (n_cover_cusps == 5 * ep_data["num_cusps"]),
            }
        )

    cusp_unramified_torsion = [
        ln for ln in projective_lines if ln["is_torsion_nontrivial"] and ln["is_cusp_unramified"]
    ]
    cusp_ramified_torsion = [
        ln for ln in projective_lines if ln["is_torsion_nontrivial"] and not ln["is_cusp_unramified"]
    ]
    base_only_lines = [ln for ln in projective_lines if not ln["is_torsion_nontrivial"]]

    return {
        "h1_invariant_factors": inv_factors,
        "has_5_torsion": len(torsion_5_cycles_mod5) > 0,
        "torsion_5_rank": len(torsion_5_cycles_mod5),
        "total_f5_lines": len(projective_lines),
        "cusp_unramified_torsion_lines": cusp_unramified_torsion,
        "cusp_ramified_torsion_lines": cusp_ramified_torsion,
        "base_only_lines": base_only_lines,
        "all_lines": projective_lines,
    }


def build_eulerian_subdivision(
    n_sub: int, truncate_cusp_corners: bool = True
) -> Dict[str, Any]:
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
                idx = len(nodes_bary)
                grid_map[(i0, i1, i2, i3)] = idx
                nodes_bary.append((i0 / n_sub, i1 / n_sub, i2 / n_sub, i3 / n_sub))
                is_horo_boundary.append(max(i0, i1, i2, i3) == n_sub - 1)

    n_grid_nodes = len(nodes_bary)
    sub_tets: List[Tuple[int, int, int, int]] = []
    e4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

    # 1. Upward simplices: base b with sum(b) == n_sub - 1
    for b0 in range(n_sub):
        for b1 in range(n_sub - b0):
            for b2 in range(n_sub - b0 - b1):
                b3 = (n_sub - 1) - b0 - b1 - b2
                if truncate_cusp_corners and max(b0, b1, b2, b3) == n_sub - 1:
                    continue
                b = (b0, b1, b2, b3)
                verts = tuple(
                    grid_map[(b[0] + e[0], b[1] + e[1], b[2] + e[2], b[3] + e[3])]
                    for e in e4
                )
                sub_tets.append(verts)

    # 2. Octahedra: base c with sum(c) == n_sub - 2, split symmetrically into 8 sub-tets around centroid
    for c0 in range(n_sub - 1):
        for c1 in range(n_sub - 1 - c0):
            for c2 in range(n_sub - 1 - c0 - c1):
                c3 = (n_sub - 2) - c0 - c1 - c2
                c = (c0, c1, c2, c3)
                oct_center_idx = len(nodes_bary)
                nodes_bary.append(
                    (
                        (c0 + 0.5) / n_sub,
                        (c1 + 0.5) / n_sub,
                        (c2 + 0.5) / n_sub,
                        (c3 + 0.5) / n_sub,
                    )
                )
                is_horo_boundary.append(False)

                pair_idx: Dict[Tuple[int, int], int] = {}
                for a in range(4):
                    for b in range(a + 1, 4):
                        tup = tuple(c[m] + e4[a][m] + e4[b][m] for m in range(4))
                        pair_idx[(a, b)] = grid_map[tup]
                        pair_idx[(b, a)] = grid_map[tup]

                # 4 type-A faces (fixed a, three b != a)
                for a in range(4):
                    others = [b for b in range(4) if b != a]
                    sub_tets.append(
                        (
                            oct_center_idx,
                            pair_idx[(a, others[0])],
                            pair_idx[(a, others[1])],
                            pair_idx[(a, others[2])],
                        )
                    )
                # 4 type-B faces (three pairs among {0,1,2,3}\{d})
                for d in range(4):
                    rem = [a for a in range(4) if a != d]
                    sub_tets.append(
                        (
                            oct_center_idx,
                            pair_idx[(rem[0], rem[1])],
                            pair_idx[(rem[1], rem[2])],
                            pair_idx[(rem[2], rem[0])],
                        )
                    )

    # 3. Downward simplices: base d with sum(d) == n_sub - 3 (for n_sub >= 3)
    if n_sub >= 3:
        for d0 in range(n_sub - 2):
            for d1 in range(n_sub - 2 - d0):
                for d2 in range(n_sub - 2 - d0 - d1):
                    d3_val = (n_sub - 3) - d0 - d1 - d2
                    d = (d0, d1, d2, d3_val)
                    verts = tuple(
                        grid_map[
                            (
                                d[0] + 1 - e[0],
                                d[1] + 1 - e[1],
                                d[2] + 1 - e[2],
                                d[3] + 1 - e[3],
                            )
                        ]
                        for e in e4
                    )
                    sub_tets.append(verts)

    return {
        "n_sub": n_sub,
        "truncate_cusp_corners": truncate_cusp_corners,
        "nodes_bary": np.array(nodes_bary, dtype=float),
        "grid_map": grid_map,
        "n_grid_nodes": n_grid_nodes,
        "is_horo_boundary": np.array(is_horo_boundary, dtype=bool),
        "sub_tets": np.array(sub_tets, dtype=int),
    }


# Exact 4-point degree-2 symmetric quadrature on reference 3-simplex (l0, l1, l2, l3)
_KEAST_A = (5.0 - math.sqrt(5.0)) / 20.0
_KEAST_B = (5.0 + 3.0 * math.sqrt(5.0)) / 20.0
_TET_QUAD_BARY = np.array(
    [
        [_KEAST_B, _KEAST_A, _KEAST_A, _KEAST_A],
        [_KEAST_A, _KEAST_B, _KEAST_A, _KEAST_A],
        [_KEAST_A, _KEAST_A, _KEAST_B, _KEAST_A],
        [_KEAST_A, _KEAST_A, _KEAST_A, _KEAST_B],
    ],
    dtype=float,
)
_TET_QUAD_WTS = np.full(4, 1.0 / 24.0, dtype=float)  # sum = 1/6 = vol(unit 3-simplex)


def _local_tet_fem_matrices(
    G: np.ndarray, nodes_bary: np.ndarray, sub_tets: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, float]:
    """Compute local P1 stiffness K_loc (n_nodes, n_nodes) and mass M_loc on one ideal tetrahedron."""
    n_nodes = nodes_bary.shape[0]
    n_elem = sub_tets.shape[0]

    # Reference coordinates xi = (w1, w2, w3)
    Dmat = G[1:, :] - G[0:1, :]  # (3, 4)
    Gdiff = Dmat[:, 1:] - Dmat[:, 0:1]  # (3, 3)

    elem_verts = nodes_bary[sub_tets]  # (n_elem, 4, 4)
    v0 = elem_verts[:, 0, 1:]
    J = np.stack(
        [
            elem_verts[:, 1, 1:] - v0,
            elem_verts[:, 2, 1:] - v0,
            elem_verts[:, 3, 1:] - v0,
        ],
        axis=-1,
    )  # (n_elem, 3, 3): d xi / d l_{1,2,3}
    detJ = np.abs(np.linalg.det(J))  # (n_elem,)
    invJT = np.linalg.inv(np.swapaxes(J, 1, 2))  # (n_elem, 3, 3): grad_xi l_{1,2,3}

    # Gradients of the 4 barycentric shape functions phi_0..3 in xi=(w1,w2,w3) space:
    # grad_xi phi_k = invJT[:, :, k-1] for k=1,2,3 and -sum_{k=1}^3 grad_xi phi_k for k=0
    grad_phi = np.zeros((n_elem, 4, 3), dtype=float)
    grad_phi[:, 1:, :] = np.swapaxes(invJT, 1, 2)
    grad_phi[:, 0, :] = -np.sum(grad_phi[:, 1:, :], axis=1)

    K_elem = np.zeros((n_elem, 4, 4), dtype=float)
    M_elem = np.zeros((n_elem, 4, 4), dtype=float)
    vol_sum = 0.0

    for q_idx in range(4):
        lb = _TET_QUAD_BARY[q_idx]  # (4,)
        wq = _TET_QUAD_WTS[q_idx]
        W = np.einsum("k,ekb->eb", lb, elem_verts)  # (n_elem, 4)
        WG = W @ G
        Q = -np.sum(WG * W, axis=-1)  # (n_elem,)
        dQ = -2.0 * (W @ Dmat.T)  # (n_elem, 3)

        g_mat = (
            Gdiff[None, :, :] / Q[:, None, None]
            + (dQ[:, :, None] * dQ[:, None, :]) / (4.0 * (Q[:, None, None] ** 2))
        )  # (n_elem, 3, 3)
        sqrt_det_g = np.sqrt(np.maximum(0.0, np.linalg.det(g_mat)))  # (n_elem,)
        g_inv = np.linalg.inv(g_mat)  # (n_elem, 3, 3)

        dvol = detJ * sqrt_det_g * wq  # (n_elem,)
        vol_sum += float(np.sum(dvol))

        # Stiffness: dvol * grad_phi_a^T g_inv grad_phi_b
        K_elem += dvol[:, None, None] * np.einsum(
            "eam,emn,ebn->eab", grad_phi, g_inv, grad_phi
        )
        # Consistent P1 mass: dvol * lb_a * lb_b? Wait: 4-point Keast degree-2 quadrature is EXACT for quadratic phi_a * phi_b!
        outer_lb = np.outer(lb, lb)
        M_elem += dvol[:, None, None] * outer_lb[None, :, :]

    rows = np.repeat(sub_tets, 4, axis=1).ravel()
    cols = np.tile(sub_tets, (1, 4)).ravel()
    K_loc = coo_matrix((K_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    M_loc = coo_matrix((M_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    return K_loc, M_loc, vol_sum


def assemble_and_solve_3d_laplacian(
    ep_data: Dict[str, Any],
    cocycle_mod5: Optional[np.ndarray] = None,
    charge_q: int = 0,
    n_sub: int = 4,
    cusp_bc: str = "neumann",
    n_eigs: int = 6,
    subdiv_cache: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Assemble and solve the global twisted 3D hyperbolic P1 Laplacian K u = E M u."""
    n_tet = ep_data["num_tets"]
    subdiv = subdiv_cache if subdiv_cache is not None else build_eulerian_subdivision(n_sub, True)
    nodes_bary = subdiv["nodes_bary"]
    grid_map = subdiv["grid_map"]
    n_local = nodes_bary.shape[0]
    is_horo = subdiv["is_horo_boundary"]
    sub_tets = subdiv["sub_tets"]

    use_twist = cocycle_mod5 is not None and (charge_q % 5 != 0)
    omega5 = np.exp(2j * math.pi * (charge_q % 5) / 5.0) if use_twist else 1.0 + 0.0j

    # Union-Find with unitary phase tracking across glued face grid nodes:
    # State i = t * n_local + loc_idx. Maintain parent[i] and phase_to_parent[i] s.t. u[i] = phase[i] * u[root].
    total_raw = n_tet * n_local
    parent = list(range(total_raw))
    phase = np.ones(total_raw, dtype=np.complex128)

    def find(x: int) -> Tuple[int, complex]:
        if parent[x] == x:
            return x, 1.0 + 0.0j
        r, p_up = find(parent[x])
        parent[x] = r
        phase[x] = phase[x] * p_up
        return r, phase[x]

    holonomy_defect_err = 0.0
    for finfo in ep_data["faces_info"]:
        f_glob = finfo["face_global"]
        t_pos, f_pos = finfo["t_pos"], finfo["f_pos"]
        t_neg = finfo["t_neg"]
        perm = finfo["perm_pos_to_neg"]
        twist_factor = (omega5 ** int(cocycle_mod5[f_glob])) if use_twist else (1.0 + 0.0j)
        # Convention: u_pos(x) = twist_factor * u_neg(perm(x))
        for tup_pos, loc_pos in grid_map.items():
            if tup_pos[f_pos] != 0:
                continue
            tup_neg = [0, 0, 0, 0]
            for a in range(4):
                tup_neg[perm[a]] = tup_pos[a]
            loc_neg = grid_map[tuple(tup_neg)]
            idx_pos = t_pos * n_local + loc_pos
            idx_neg = t_neg * n_local + loc_neg

            r_pos, ph_pos = find(idx_pos)
            r_neg, ph_neg = find(idx_neg)
            # Required: ph_pos * u[r_pos] = twist_factor * ph_neg * u[r_neg]
            # => u[r_pos] = (twist_factor * ph_neg / ph_pos) * u[r_neg]
            rel = twist_factor * ph_neg / ph_pos
            if r_pos != r_neg:
                parent[r_pos] = r_neg
                phase[r_pos] = rel
            else:
                holonomy_defect_err = max(holonomy_defect_err, abs(rel - 1.0))

    if holonomy_defect_err > 1e-10:
        raise RuntimeError(
            f"Non-flat cocycle holonomy defect {holonomy_defect_err:.3e} during global DOF assembly!"
        )

    # Assign active global DOF indices (excluding horosphere boundary if cusp_bc == 'dirichlet')
    root_is_dirichlet: Dict[int, bool] = {}
    for t in range(n_tet):
        for loc in range(n_local):
            r, _ = find(t * n_local + loc)
            if is_horo[loc]:
                root_is_dirichlet[r] = True
            elif r not in root_is_dirichlet:
                root_is_dirichlet[r] = False

    root_to_dof: Dict[int, int] = {}
    for r, is_dir in sorted(root_is_dirichlet.items()):
        if cusp_bc == "dirichlet" and is_dir:
            continue
        root_to_dof[r] = len(root_to_dof)
    n_dof = len(root_to_dof)

    # Assemble global Hermitian K and M, plus per-tetrahedron mass matrices for layer probabilities
    rows_all: List[np.ndarray] = []
    cols_all: List[np.ndarray] = []
    k_vals_all: List[np.ndarray] = []
    m_vals_all: List[np.ndarray] = []
    tet_mass_mats: List[csr_matrix] = []
    trunc_vol_total = 0.0
    tet_trunc_vols: List[float] = []

    for t in range(n_tet):
        K_loc, M_loc, v_t = _local_tet_fem_matrices(ep_data["grams"][t], nodes_bary, sub_tets)
        trunc_vol_total += v_t
        tet_trunc_vols.append(v_t)

        active_locs = []
        active_dofs = []
        active_phases = []
        for loc in range(n_local):
            r, ph = find(t * n_local + loc)
            if r in root_to_dof:
                active_locs.append(loc)
                active_dofs.append(root_to_dof[r])
                active_phases.append(ph)

        act_l = np.array(active_locs, dtype=int)
        act_d = np.array(active_dofs, dtype=int)
        act_p = np.array(active_phases, dtype=np.complex128)

        K_sub = K_loc[np.ix_(act_l, act_l)]
        M_sub = M_loc[np.ix_(act_l, act_l)]
        ph_mat = np.conj(act_p)[:, None] * act_p[None, :]

        K_gl = K_sub * ph_mat
        M_gl = M_sub * ph_mat

        rr = np.repeat(act_d, len(act_d))
        cc = np.tile(act_d, len(act_d))
        rows_all.append(rr)
        cols_all.append(cc)
        k_vals_all.append(K_gl.ravel())
        m_vals_all.append(M_gl.ravel())

        tet_mass_mats.append(
            coo_matrix((M_gl.ravel(), (rr, cc)), shape=(n_dof, n_dof)).tocsr()
        )

    R_cat = np.concatenate(rows_all)
    C_cat = np.concatenate(cols_all)
    K_csr = coo_matrix((np.concatenate(k_vals_all), (R_cat, C_cat)), shape=(n_dof, n_dof)).tocsr()
    M_csr = coo_matrix((np.concatenate(m_vals_all), (R_cat, C_cat)), shape=(n_dof, n_dof)).tocsr()

    # Symmetrize strictly to machine precision
    K_csr = 0.5 * (K_csr + K_csr.conj().T)
    M_csr = 0.5 * (M_csr + M_csr.conj().T)

    k_req = min(n_eigs, n_dof - 1)
    if n_dof <= 2500:
        evals_raw, evecs_raw = eigh(
            K_csr.toarray(), M_csr.toarray(), subset_by_index=[0, k_req - 1]
        )
    else:
        evals_raw, evecs_raw = eigsh(
            K_csr, k=k_req, M=M_csr, sigma=-0.1, which="LM", tol=1e-14
        )
    order = np.argsort(evals_raw.real)
    evals = np.array(evals_raw[order].real, dtype=float)
    evecs = evecs_raw[:, order]

    # Normalize eigenvectors w.r.t. M_csr
    for j in range(k_req):
        v = evecs[:, j]
        nrm = math.sqrt(max(1e-30, float(np.real(np.vdot(v, M_csr @ v)))))
        evecs[:, j] = v / nrm

    # For untwisted Neumann, the lowest mode is constant E_0 ~ 0; physical non-constant mode is index 1
    first_phys_idx = 1 if (not use_twist and cusp_bc == "neumann" and abs(evals[0]) < 1e-8) else 0
    E0 = float(evals[first_phys_idx])

    # Determine multiplicity of E0 (within relative tolerance 1e-5)
    deg_indices = [
        j for j in range(first_phys_idx, k_req)
        if abs(evals[j] - E0) <= max(1e-7, 1e-5 * abs(E0))
    ]
    mult = len(deg_indices)
    next_indices = [j for j in range(first_phys_idx, k_req) if j not in deg_indices]
    E1_next = float(evals[next_indices[0]]) if next_indices else float("nan")
    rel_gap = (E1_next - E0) / max(1e-15, abs(E0)) if next_indices else 0.0

    # Gauge-invariant layer probability P_t averaged across the ground eigenspace
    layer_probs = np.zeros(n_tet, dtype=float)
    for j in deg_indices:
        vj = evecs[:, j]
        for t in range(n_tet):
            layer_probs[t] += float(np.real(np.vdot(vj, tet_mass_mats[t] @ vj)))
    layer_probs /= max(1, mult)
    layer_probs /= np.sum(layer_probs)

    # Also compute probability density per unit hyperbolic volume in each tetrahedron layer:
    # rho_t = P_t / (tet_trunc_vols[t] / trunc_vol_total)
    vol_fracs = np.array(tet_trunc_vols, dtype=float) / trunc_vol_total
    layer_density_ratio = layer_probs / vol_fracs

    # Count strict local maxima around the circular layer sequence t = 0..n_tet-1
    def _circular_peaks(arr: np.ndarray, tol_tie: float = 1e-5) -> List[int]:
        n = len(arr)
        if n == 1:
            return [0]
        if n == 2:
            if abs(arr[0] - arr[1]) <= tol_tie:
                return [0, 1]
            return [int(np.argmax(arr))]
        # Group plateau-tied adjacent maxima or identify strict peaks above neighbors
        peaks = []
        for i in range(n):
            prev_v = arr[(i - 1) % n]
            next_v = arr[(i + 1) % n]
            if arr[i] >= prev_v - tol_tie and arr[i] >= next_v - tol_tie:
                if arr[i] > prev_v + tol_tie or arr[i] > next_v + tol_tie:
                    peaks.append(i)
        # Merge adjacent plateau endpoints if two neighboring cells tie to tol_tie
        merged: List[int] = []
        for p in peaks:
            if merged and (p - merged[-1] == 1) and abs(arr[p] - arr[merged[-1]]) <= tol_tie:
                continue
            merged.append(p)
        if len(merged) >= 2 and merged[0] == 0 and merged[-1] == n - 1 and abs(arr[0] - arr[n - 1]) <= tol_tie:
            merged.pop()
        return merged if merged else [int(np.argmax(arr))]

    prob_peaks = _circular_peaks(layer_probs)
    dens_peaks = _circular_peaks(layer_density_ratio)

    # Dominant peaks within 2% of global max
    p_max = float(np.max(layer_probs))
    dominant_prob_layers = [i for i in prob_peaks if layer_probs[i] >= 0.98 * p_max]
    d_max = float(np.max(layer_density_ratio))
    dominant_dens_layers = [i for i in dens_peaks if layer_density_ratio[i] >= 0.98 * d_max]

    tet_taus = np.array(ep_data["tet_canonical_taus"], dtype=np.complex128)
    tau_expectation = complex(np.sum(layer_probs * tet_taus))

    return {
        "n_sub": n_sub,
        "cusp_bc": cusp_bc,
        "n_dof": n_dof,
        "holonomy_defect_err": holonomy_defect_err,
        "truncated_volume": trunc_vol_total,
        "tet_truncated_volumes": tet_trunc_vols,
        "eigenvalues": evals.tolist(),
        "E0": E0,
        "E1_next_distinct": E1_next,
        "rel_gap": rel_gap,
        "ground_multiplicity": mult,
        "layer_probs": layer_probs.tolist(),
        "layer_density_ratio": layer_density_ratio.tolist(),
        "dominant_prob_peak_layers": dominant_prob_layers,
        "dominant_density_peak_layers": dominant_dens_layers,
        "is_unique_single_layer_prob_peak": (mult == 1 and len(dominant_prob_layers) == 1),
        "is_unique_single_layer_density_peak": (mult == 1 and len(dominant_dens_layers) == 1),
        "tau_pleated_expectation": [float(tau_expectation.real), float(tau_expectation.imag)],
    }
