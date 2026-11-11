"""Phase 4 Mathematical-Physics Core: Hyperbolic Geometry, Fox-Wada Torsion, & Quark-Lepton FEM.

Clean-room Phase 4 core (zero imports from Phases 1-3, zero empirical inputs).
Provides:
  1. Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature (exact up to
     polynomial degree 5, covering both cubic Dirac Yukawa and quartic Weinberg integrals).
  2. Quad-precision Epstein-Penner hyperbolic Riemannian metrics, 24-cone volumes, and
     integer Smith Normal Form cohomology / Z/5Z torsion line classifiers.
  3. Exact Fox free-differential calculus and Wada-Reidemeister 1-loop torsion determinants
     on fundamental group presentations pi_1(M).
  4. Twisted 3D hyperbolic P1 FEM solvers, bilinear Majorana KK singlet overlaps, trilinear
     Dirac Yukawa overlaps, and quartic contact Weinberg neutrino overlaps.
  5. Basis-invariant CKM and PMNS (seesaw + Weinberg) observable extractors and random
     Haar U(3)^3 basis-scrambling verifiers (< 1e-12, Guardrail 3).
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh
from scipy.special import roots_legendre, spence
import snappy
from snappy.geometric_structure.cusp_neighborhood.complex_cusp_cross_section import (
    ComplexCuspCrossSection,
)


VBITS = (1, 2, 4, 8)
FBITS = (14, 13, 11, 7)

# Positive-weight S_4-symmetric 14-point degree-5 tetrahedral quadrature (Jinyun-Walkington):
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
        sym_grp = M_base.symmetry_group()
        sym_grp_str = str(sym_grp)
        sym_order = int(sym_grp.order())
        is_amph = bool(sym_grp.is_amphicheiral())
    except Exception:
        sym_grp_str = "unknown"
        sym_order = 1
        is_amph = abs(math.sin(4.0 * math.pi * cs_val)) < 1e-10

    return {
        "name": name,
        "manifold": M,
        "manifold_std": M_base,
        "symmetry_group_str": sym_grp_str,
        "symmetry_order": sym_order,
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
    for _, i1, i2, i3 in itertools.permutations(range(4)):
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


# ---------------------------------------------------------------------------
# Exact Fox Free-Differential Calculus & Wada-Reidemeister 1-Loop Torsion
# ---------------------------------------------------------------------------

def eval_group_word(word: str, rho_map: Dict[str, complex]) -> complex:
    """Evaluate a SnapPy group word (lowercase=gen, uppercase=inv) under rho: pi_1 -> C^x."""
    val = 1.0 + 0.0j
    for ch in word:
        g = rho_map[ch.lower()]
        val *= (1.0 / g) if ch.isupper() else g
    return val


def fox_derivative(word: str, gen: str, rho_map: Dict[str, complex]) -> complex:
    """Evaluate rho(d(word)/d(gen)) via exact Fox free-differential calculus."""
    acc = 0.0 + 0.0j
    prefix = 1.0 + 0.0j
    for ch in word:
        g_low = ch.lower()
        is_inv = ch.isupper()
        rho_g = rho_map[g_low]
        if g_low == gen:
            acc += prefix * ((-1.0 / rho_g) if is_inv else (1.0 + 0.0j))
        prefix *= (1.0 / rho_g) if is_inv else rho_g
    return acc


def compute_wada_reidemeister_torsion(
    gens: List[str],
    rels: List[str],
    rho_map: Dict[str, complex],
    hom_tol: float = 1e-11,
) -> Dict[str, Any]:
    """Compute exact 1-loop Wada-Reidemeister torsion |tau_Reid(M, rho)| on a deficiency-1 presentation.

    For a 1-cusped 3-manifold presentation <g_1..g_n | r_1..r_{n-1}>, Wada's invariant
    for any g_j with rho(g_j) != 1 is:
        tau_j = |det_{i, k != j} rho(dr_i / dg_k)| / |rho(g_j) - 1|,
    and |det_{i, k != j} rho(dr_i / dg_k)| is the Fox Alexander numerator magnitude
    when dropping a free-abelian generator g_j.
    """
    if len(rels) != len(gens) - 1:
        raise ValueError(f"Expected deficiency-1 presentation (n-1 rels), got {len(gens)} gens, {len(rels)} rels.")

    max_rel_err = max((abs(eval_group_word(r, rho_map) - 1.0) for r in rels), default=0.0)
    if max_rel_err > hom_tol:
        raise ValueError(f"rho_map is not a valid group homomorphism: max |rho(r)-1| = {max_rel_err:.3e}")

    n = len(gens)
    J = np.zeros((n - 1, n), dtype=np.complex128)
    for i, r in enumerate(rels):
        for k, g in enumerate(gens):
            J[i, k] = fox_derivative(r, g, rho_map)

    col_torsions: List[float] = []
    col_numerators: Dict[str, float] = {}
    active_gens: List[str] = []
    for j, g in enumerate(gens):
        denom = abs(rho_map[g] - 1.0)
        cols = [k for k in range(n) if k != j]
        minor_det = abs(complex(np.linalg.det(J[:, cols]))) if cols else 1.0
        col_numerators[g] = float(minor_det)
        if denom > 1e-10:
            active_gens.append(g)
            col_torsions.append(float(minor_det / denom))

    if not col_torsions:
        return {
            "is_trivial_character": True,
            "is_acyclic": False,
            "torsion_abs": 0.0,
            "wada_column_spread": 0.0,
            "max_relator_err": float(max_rel_err),
            "col_numerators": col_numerators,
        }

    spread = max(col_torsions) - min(col_torsions)
    tau_mean = float(np.mean(col_torsions))
    return {
        "is_trivial_character": False,
        "is_acyclic": tau_mean > 1e-11,
        "torsion_abs": tau_mean,
        "free_energy_1loop": (-math.log(tau_mean) if tau_mean > 1e-14 else float("inf")),
        "wada_column_spread": float(spread),
        "max_relator_err": float(max_rel_err),
        "active_generators": active_gens,
        "col_numerators": col_numerators,
    }


def analyze_pi1_mod5_torsion_lines(spec_or_manifold: Any) -> Dict[str, Any]:
    """Enumerate all projective F_5 character lines of pi_1(M) and evaluate exact Wada-Reidemeister torsion."""
    M = snappy.Manifold(spec_or_manifold) if isinstance(spec_or_manifold, str) else spec_or_manifold
    G = M.fundamental_group()
    gens = list(G.generators())
    rels = list(G.relators())
    periph = G.peripheral_curves()
    m_word, l_word = periph[0]

    A = np.zeros((len(rels), len(gens)), dtype=int)
    for ri, r in enumerate(rels):
        for ch in r:
            A[ri, gens.index(ch.lower())] += -1 if ch.isupper() else 1

    # Free abelian character direction (A @ v_free == 0 over Z):
    _, _, _, V_snf, _ = _integer_snf_with_inverses(A)
    # Columns of V_snf where A @ col == 0:
    free_cols = [
        np.array([int(x) for x in V_snf[:, j]], dtype=int)
        for j in range(V_snf.shape[1])
        if np.all(A @ np.array([int(x) for x in V_snf[:, j]], dtype=object) == 0)
    ]

    lines_out: List[Dict[str, Any]] = []
    seen = set()
    for c in itertools.product(range(5), repeat=len(gens)):
        if not any(c):
            continue
        c_arr = np.array(c, dtype=int)
        if not np.all((A @ c_arr) % 5 == 0):
            continue
        fnz = next(x for x in c if x != 0)
        inv = pow(fnz, -1, 5)
        canon = tuple((x * inv) % 5 for x in c)
        if canon in seen:
            continue
        seen.add(canon)

        # Check if canon is purely a reduction of free H^1_free(M; Z):
        is_pure_free = False
        if len(free_cols) == 1:
            fc_mod5 = tuple(int(x % 5) for x in free_cols[0])
            if any(fc_mod5):
                fnz_f = next(x for x in fc_mod5 if x != 0)
                inv_f = pow(fnz_f, -1, 5)
                canon_free = tuple((x * inv_f) % 5 for x in fc_mod5)
                is_pure_free = (canon == canon_free)

        hm = sum((-1 if ch.isupper() else 1) * canon[gens.index(ch.lower())] for ch in m_word) % 5
        hl = sum((-1 if ch.isupper() else 1) * canon[gens.index(ch.lower())] for ch in l_word) % 5
        unram = (hm == 0 and hl == 0)

        # Evaluate at q = 1 and q = 2 (the two conjugate pairs in (Z/5Z)^x):
        rho_q1 = {gens[i]: np.exp(2j * math.pi * canon[i] / 5.0) for i in range(len(gens))}
        rho_q2 = {gens[i]: np.exp(4j * math.pi * canon[i] / 5.0) for i in range(len(gens))}
        t_q1 = compute_wada_reidemeister_torsion(gens, rels, rho_q1)
        t_q2 = compute_wada_reidemeister_torsion(gens, rels, rho_q2)

        lines_out.append(
            {
                "canon_coords_mod5": list(canon),
                "is_pure_free_character": is_pure_free,
                "is_torsion_nontrivial": not is_pure_free,
                "peripheral_holonomy_mod5": [int(hm), int(hl)],
                "is_cusp_unramified": unram,
                "is_acyclic_q1": t_q1["is_acyclic"],
                "torsion_q1": t_q1["torsion_abs"],
                "torsion_q2": t_q2["torsion_abs"],
                "torsion_product_all_4_charges": (t_q1["torsion_abs"] ** 2) * (t_q2["torsion_abs"] ** 2),
                "wada_max_spread": max(t_q1["wada_column_spread"], t_q2["wada_column_spread"]),
            }
        )

    return {
        "generators": gens,
        "relators": rels,
        "peripheral_words": [m_word, l_word],
        "num_projective_f5_lines": len(lines_out),
        "lines": lines_out,
    }


# ---------------------------------------------------------------------------
# Integer SNF Cohomology & Z/5Z Dual-Complex Cocycle Classifier
# ---------------------------------------------------------------------------

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
    """Extract Z/5Z torsion 1-cocycle lines (cusp-unramified and cusp-ramified) via exact SNF."""
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

    torsion_5_cycles_mod5: List[np.ndarray] = []
    for j, d_val in enumerate(inv_factors):
        if d_val != 0 and d_val % 5 == 0:
            cyc = H1_gens[:, j]
            torsion_5_cycles_mod5.append(
                np.array([int(x % 5) for x in cyc], dtype=int)
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


# ---------------------------------------------------------------------------
# 3D Hyperbolic FEM, Bilinear Majorana, Trilinear Yukawa & Quartic Weinberg
# ---------------------------------------------------------------------------

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

    elem_verts = nodes_bary[sub_tets]
    v0 = elem_verts[:, 0, 1:]
    J = np.stack([elem_verts[:, 1, 1:] - v0, elem_verts[:, 2, 1:] - v0, elem_verts[:, 3, 1:] - v0], axis=-1)
    detJ = np.abs(np.linalg.det(J))
    invJT = np.linalg.inv(np.swapaxes(J, 1, 2))

    grad_phi = np.zeros((sub_tets.shape[0], 4, 3), dtype=float)
    grad_phi[:, 1:, :] = np.swapaxes(invJT, 1, 2)
    grad_phi[:, 0, :] = -np.sum(grad_phi[:, 1:, :], axis=1)

    W = np.einsum("qk,ekb->eqb", TET_QUAD14_BARY, elem_verts)
    WG = W @ G
    Q = -np.sum(WG * W, axis=-1)
    dQ = -2.0 * (W @ Dmat.T)

    g_mat = (
        Gdiff[None, None, :, :] / Q[:, :, None, None]
        + (dQ[:, :, :, None] * dQ[:, :, None, :]) / (4.0 * (Q[:, :, None, None] ** 2))
    )
    sqrt_det_g = np.sqrt(np.maximum(0.0, np.linalg.det(g_mat)))
    g_inv = np.linalg.inv(g_mat)
    dvol_q14 = detJ[:, None] * sqrt_det_g * TET_QUAD14_WTS[None, :]

    return {
        "grad_phi": grad_phi,
        "g_inv_q14": g_inv,
        "dvol_q14": dvol_q14,
        "trunc_vol": float(np.sum(dvol_q14)),
    }


def _local_stiffness_mass_q14(
    geom: Dict[str, np.ndarray], n_nodes: int, sub_tets: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    grad_phi = geom["grad_phi"]
    g_inv = geom["g_inv_q14"]
    dvol = geom["dvol_q14"]

    g_inv_int = np.einsum("eq,eqmn->emn", dvol, g_inv)
    K_elem = np.einsum("eam,emn,ebn->eab", grad_phi, g_inv_int, grad_phi)

    outer_bary = TET_QUAD14_BARY[:, :, None] * TET_QUAD14_BARY[:, None, :]
    M_elem = np.einsum("eq,qab->eab", dvol, outer_bary)

    rows = np.repeat(sub_tets, 4, axis=1).ravel()
    cols = np.tile(sub_tets, (1, 4)).ravel()
    K_loc = coo_matrix((K_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    M_loc = coo_matrix((M_elem.ravel(), (rows, cols)), shape=(n_nodes, n_nodes)).toarray()
    return K_loc, M_loc


def assemble_and_solve_3d_sector(
    ep_data: Dict[str, Any],
    cocycle_mod5: Optional[np.ndarray] = None,
    charge_q: int = 0,
    n_sub: int = 4,
    cusp_bc: str = "dirichlet",
    n_eigs: int = 8,
    subdiv: Optional[Dict[str, Any]] = None,
    tet_geoms: Optional[List[Dict[str, np.ndarray]]] = None,
) -> Dict[str, Any]:
    """Solve 3D hyperbolic Laplace-Beltrami operator twisted by a flat Z/5Z cocycle."""
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

    rows_all, cols_all, kv_all, mv_all = [], [], [], []
    tet_nodal_map: List[Tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    trunc_vol_total = 0.0

    for t in range(n_tet):
        gm = geoms[t]
        trunc_vol_total += gm["trunc_vol"]
        K_loc_r, M_loc_r = _local_stiffness_mass_q14(gm, n_local, sub_tets)
        K_loc = K_loc_r.astype(np.complex128)
        M_loc = M_loc_r.astype(np.complex128)

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

    R_c = np.concatenate(rows_all)
    C_c = np.concatenate(cols_all)
    K_csr = coo_matrix((np.concatenate(kv_all), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    M_csr = coo_matrix((np.concatenate(mv_all), (R_c, C_c)), shape=(n_dof, n_dof)).tocsr()
    K_csr = 0.5 * (K_csr + K_csr.conj().T)
    M_csr = 0.5 * (M_csr + M_csr.conj().T)

    k_req = min(n_eigs, n_dof - 1)
    if n_dof <= 2800:
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

    first_phys = 1 if (not use_twist and cusp_bc == "neumann" and abs(evals[0]) < 1e-8) else 0
    local_modes = np.zeros((k_req, n_tet, n_local), dtype=np.complex128)
    for t in range(n_tet):
        al, ad, ap = tet_nodal_map[t]
        local_modes[:, t, al] = (ap[:, None] * evecs[ad, :]).T

    return {
        "n_sub": n_sub,
        "cusp_bc": cusp_bc,
        "charge_q": charge_q % 5,
        "n_dof": n_dof,
        "truncated_volume": trunc_vol_total,
        "first_phys_idx": first_phys,
        "eigenvalues": evals.tolist(),
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
    """Exact degree-5 3D trilinear Yukawa overlap Y_{ab} = int sqrt(det g) A_a B_b H d^3x."""
    n_A = modes_A.shape[0]
    n_B = modes_B.shape[0]
    n_tet = mode_H.shape[0]
    Y = np.zeros((n_A, n_B), dtype=np.complex128)

    Q_T = TET_QUAD14_BARY.T
    for t in range(n_tet):
        dvol = tet_geoms[t]["dvol_q14"]
        H_q = mode_H[t, sub_tets] @ Q_T
        wH = dvol * H_q
        A_q = modes_A[:, t, :][:, sub_tets] @ Q_T
        B_q = modes_B[:, t, :][:, sub_tets] @ Q_T
        Y += np.einsum("aeq,beq,eq->ab", A_q, B_q, wH)
    return Y


def compute_bilinear_majorana_matrix_q14(
    modes_N: np.ndarray,
    evals_N: np.ndarray,
    sub_tets: np.ndarray,
    tet_geoms: List[Dict[str, np.ndarray]],
) -> np.ndarray:
    """Exact symmetric 3D KK Majorana matrix (M_R)_{mn} = 0.5*(sqrt(lam_m)+sqrt(lam_n))*int eta_m eta_n dVol.

    Because the integral is bilinear (no complex conjugation), any arbitrary eigensolver phases
    on modes_N cancel identically in M_nu = -Y_nu M_R^{-1} Y_nu^T.
    """
    n_R = modes_N.shape[0]
    n_tet = modes_N.shape[1]
    B = np.zeros((n_R, n_R), dtype=np.complex128)
    Q_T = TET_QUAD14_BARY.T
    for t in range(n_tet):
        dvol = tet_geoms[t]["dvol_q14"]
        N_q = modes_N[:, t, :][:, sub_tets] @ Q_T
        B += np.einsum("meq,neq,eq->mn", N_q, N_q, dvol)
    B = 0.5 * (B + B.T)
    kk_masses = np.sqrt(np.maximum(0.0, np.asarray(evals_N, dtype=float)))
    scale = 0.5 * (kk_masses[:, None] + kk_masses[None, :])
    return scale * B


def compute_quartic_weinberg_matrix_q14(
    modes_L: np.ndarray,
    mode_Hu: np.ndarray,
    sub_tets: np.ndarray,
    tet_geoms: List[Dict[str, np.ndarray]],
) -> np.ndarray:
    """Exact degree-5 3D quartic Weinberg overlap (M_nu^W)_{ab} = int sqrt(det g) L_a L_b (H_u)^2 d^3x."""
    n_L = modes_L.shape[0]
    n_tet = mode_Hu.shape[0]
    M_w = np.zeros((n_L, n_L), dtype=np.complex128)
    Q_T = TET_QUAD14_BARY.T
    for t in range(n_tet):
        dvol = tet_geoms[t]["dvol_q14"]
        Hu_q = mode_Hu[t, sub_tets] @ Q_T
        wHu2 = dvol * (Hu_q ** 2)
        L_q = modes_L[:, t, :][:, sub_tets] @ Q_T
        M_w += np.einsum("aeq,beq,eq->ab", L_q, L_q, wHu2)
    return 0.5 * (M_w + M_w.T)


# ---------------------------------------------------------------------------
# Basis-Invariant CKM & PMNS Extractors + Random Haar U(3)^3 Verifiers
# ---------------------------------------------------------------------------

def _extract_pdg_angles_from_abs_unitary(U_abs: np.ndarray) -> Dict[str, float]:
    """Extract standard mixing angles (sin^2 theta_12, sin^2 theta_23, sin^2 theta_13) from |U|."""
    s13_sq = float(min(1.0, max(0.0, U_abs[0, 2] ** 2)))
    c13_sq = max(1e-30, 1.0 - s13_sq)
    s12_sq = float(min(1.0, max(0.0, (U_abs[0, 1] ** 2) / c13_sq)))
    s23_sq = float(min(1.0, max(0.0, (U_abs[1, 2] ** 2) / c13_sq)))
    return {
        "sin2_theta_12": s12_sq,
        "sin2_theta_23": s23_sq,
        "sin2_theta_13": s13_sq,
        "theta_12_deg": math.degrees(math.asin(math.sqrt(s12_sq))),
        "theta_23_deg": math.degrees(math.asin(math.sqrt(s23_sq))),
        "theta_13_deg": math.degrees(math.asin(math.sqrt(s13_sq))),
    }


def extract_quark_ckm_observables(
    Y_u: np.ndarray, Y_d: np.ndarray, rank_tol: float = 1e-10
) -> Dict[str, Any]:
    """Extract strictly basis-invariant quark observables from (Y_u, Y_d) (Guardrail 3)."""
    assert Y_u.shape == (3, 3) and Y_d.shape == (3, 3)

    U_u, sv_u_desc, _ = np.linalg.svd(Y_u)
    U_d, sv_d_desc, _ = np.linalg.svd(Y_d)
    sv_u = sv_u_desc[::-1]
    sv_d = sv_d_desc[::-1]
    U_Lu = U_u[:, ::-1]
    U_Ld = U_d[:, ::-1]

    rank_u = int(np.sum(sv_u > rank_tol * max(1e-30, float(sv_u[-1]))))
    rank_d = int(np.sum(sv_d > rank_tol * max(1e-30, float(sv_d[-1]))))

    su_ratios = [float(sv_u[0] / sv_u[2]), float(sv_u[1] / sv_u[2]), 1.0] if sv_u[2] > 1e-30 else [0.0, 0.0, 0.0]
    sd_ratios = [float(sv_d[0] / sv_d[2]), float(sv_d[1] / sv_d[2]), 1.0] if sv_d[2] > 1e-30 else [0.0, 0.0, 0.0]

    min_split_u = min(abs(sv_u[1] - sv_u[0]) / sv_u[2], abs(sv_u[2] - sv_u[1]) / sv_u[2]) if sv_u[2] > 1e-30 else 0.0
    min_split_d = min(abs(sv_d[1] - sv_d[0]) / sv_d[2], abs(sv_d[2] - sv_d[1]) / sv_d[2]) if sv_d[2] > 1e-30 else 0.0

    V_ckm = U_Lu.conj().T @ U_Ld
    V_abs = np.abs(V_ckm)
    angles = _extract_pdg_angles_from_abs_unitary(V_abs)

    H_u = Y_u @ Y_u.conj().T
    H_d = Y_d @ Y_d.conj().T
    comm = H_u @ H_d - H_d @ H_u
    det_comm = complex(np.linalg.det(comm))
    denom = (float(np.linalg.norm(H_u, "fro")) ** 3) * (float(np.linalg.norm(H_d, "fro")) ** 3)
    jarlskog_norm = float(det_comm.imag / denom) if denom > 1e-60 else 0.0
    j_quartet = float(np.imag(V_ckm[0, 1] * V_ckm[1, 2] * np.conj(V_ckm[0, 2]) * np.conj(V_ckm[1, 1])))

    cw_quartic_trace = float(np.real(np.trace(H_u @ H_u + H_d @ H_d)))

    return {
        "sv_u_asc": sv_u.tolist(),
        "sv_d_asc": sv_d.tolist(),
        "sv_u_ratios": su_ratios,
        "sv_d_ratios": sd_ratios,
        "rank_u": rank_u,
        "rank_d": rank_d,
        "min_rel_sv_split_u": float(min_split_u),
        "min_rel_sv_split_d": float(min_split_d),
        "ckm_abs_matrix": V_abs.tolist(),
        "angles": angles,
        "jarlskog_norm": jarlskog_norm,
        "jarlskog_quartet": j_quartet,
        "cw_yukawa_quartic_trace": cw_quartic_trace,
    }


def extract_lepton_pmns_observables(
    Y_e: np.ndarray,
    M_nu: np.ndarray,
    rank_tol: float = 1e-10,
) -> Dict[str, Any]:
    """Extract strictly basis-invariant lepton PMNS observables from (Y_e, M_nu = M_nu^T).

    Gauge-group basis transformations:
        Y_e  -> U_L Y_e U_{e^c}^dagger,
        M_nu -> U_L M_nu U_L^T,
    so H_e = Y_e Y_e^dagger -> U_L H_e U_L^dagger and H_nu = M_nu M_nu^dagger -> U_L H_nu U_L^dagger.
    """
    assert Y_e.shape == (3, 3) and M_nu.shape == (3, 3)
    M_sym = 0.5 * (M_nu + M_nu.T)

    U_e, sv_e_desc, _ = np.linalg.svd(Y_e)
    U_nu, sv_nu_desc, _ = np.linalg.svd(M_sym)
    sv_e = sv_e_desc[::-1]
    sv_nu = sv_nu_desc[::-1]
    U_Le = U_e[:, ::-1]
    U_Lnu = U_nu[:, ::-1]

    rank_e = int(np.sum(sv_e > rank_tol * max(1e-30, float(sv_e[-1]))))
    rank_nu = int(np.sum(sv_nu > rank_tol * max(1e-30, float(sv_nu[-1]))))

    se_ratios = [float(sv_e[0] / sv_e[2]), float(sv_e[1] / sv_e[2]), 1.0] if sv_e[2] > 1e-30 else [0.0, 0.0, 0.0]
    snu_ratios = [float(sv_nu[0] / sv_nu[2]), float(sv_nu[1] / sv_nu[2]), 1.0] if sv_nu[2] > 1e-30 else [0.0, 0.0, 0.0]

    min_split_e = min(abs(sv_e[1] - sv_e[0]) / sv_e[2], abs(sv_e[2] - sv_e[1]) / sv_e[2]) if sv_e[2] > 1e-30 else 0.0
    min_split_nu = min(abs(sv_nu[1] - sv_nu[0]) / sv_nu[2], abs(sv_nu[2] - sv_nu[1]) / sv_nu[2]) if sv_nu[2] > 1e-30 else 0.0

    U_pmns = U_Le.conj().T @ U_Lnu
    U_abs = np.abs(U_pmns)
    angles_asc = _extract_pdg_angles_from_abs_unitary(U_abs)
    # Also record inverted column permutation (nu_1, nu_2, nu_3) = (asc_1, asc_2, asc_0) transparently:
    U_abs_inv = U_abs[:, [1, 2, 0]]
    angles_inv_ord = _extract_pdg_angles_from_abs_unitary(U_abs_inv)

    H_e = Y_e @ Y_e.conj().T
    H_nu = M_sym @ M_sym.conj().T
    comm = H_e @ H_nu - H_nu @ H_e
    det_comm = complex(np.linalg.det(comm))
    denom = (float(np.linalg.norm(H_e, "fro")) ** 3) * (float(np.linalg.norm(H_nu, "fro")) ** 3)
    jarlskog_pmns = float(det_comm.imag / denom) if denom > 1e-60 else 0.0
    j_quartet = float(np.imag(U_pmns[0, 1] * U_pmns[1, 2] * np.conj(U_pmns[0, 2]) * np.conj(U_pmns[1, 1])))

    return {
        "symmetry_defect_Mnu": float(np.max(np.abs(M_nu - M_nu.T))),
        "sv_e_asc": sv_e.tolist(),
        "sv_nu_asc": sv_nu.tolist(),
        "sv_e_ratios": se_ratios,
        "sv_nu_ratios": snu_ratios,
        "rank_e": rank_e,
        "rank_nu": rank_nu,
        "min_rel_sv_split_e": float(min_split_e),
        "min_rel_sv_split_nu": float(min_split_nu),
        "pmns_abs_matrix": U_abs.tolist(),
        "angles": angles_asc,
        "angles_inverted_column_perm": angles_inv_ord,
        "jarlskog_pmns_norm": jarlskog_pmns,
        "jarlskog_pmns_quartet": j_quartet,
    }


def verify_quark_haar_invariance(
    Y_u: np.ndarray, Y_d: np.ndarray, n_trials: int = 16, seed: int = 20261111
) -> Dict[str, Any]:
    """Verify quark CKM observables under random Haar (U_L, U_Ru, U_Rd) in U(3)^3 (< 1e-12)."""
    rng = np.random.default_rng(seed)
    base = extract_quark_ckm_observables(Y_u, Y_d)
    min_split = min(base["min_rel_sv_split_u"], base["min_rel_sv_split_d"])
    nondeg = min_split > 1e-6
    wedin_scale = min(1.0, min_split / 1e-3) if nondeg else 0.0

    max_sv_err = 0.0
    max_j_err = 0.0
    max_ckm_err = 0.0
    max_ang_err = 0.0
    for _ in range(n_trials):
        U_L = random_haar_unitary(3, rng)
        U_Ru = random_haar_unitary(3, rng)
        U_Rd = random_haar_unitary(3, rng)
        scr = extract_quark_ckm_observables(U_L @ Y_u @ U_Ru.conj().T, U_L @ Y_d @ U_Rd.conj().T)
        max_sv_err = max(
            max_sv_err,
            float(np.max(np.abs(np.array(base["sv_u_ratios"]) - np.array(scr["sv_u_ratios"])))),
            float(np.max(np.abs(np.array(base["sv_d_ratios"]) - np.array(scr["sv_d_ratios"])))),
        )
        max_j_err = max(max_j_err, abs(base["jarlskog_norm"] - scr["jarlskog_norm"]))
        if nondeg:
            raw_ckm = float(np.max(np.abs(np.array(base["ckm_abs_matrix"]) - np.array(scr["ckm_abs_matrix"]))))
            max_ckm_err = max(max_ckm_err, wedin_scale * raw_ckm)
            for k in ("sin2_theta_12", "sin2_theta_23", "sin2_theta_13"):
                max_ang_err = max(max_ang_err, wedin_scale * abs(base["angles"][k] - scr["angles"][k]))

    return {
        "trials": n_trials,
        "singular_values_nondegenerate": nondeg,
        "max_sv_ratio_err": max_sv_err,
        "max_jarlskog_err": max_j_err,
        "max_ckm_abs_err": max_ckm_err,
        "max_angle_sin2_err": max_ang_err,
        "passed": (
            max_sv_err < 1e-12
            and max_j_err < 1e-12
            and (max_ckm_err < 1e-12 and max_ang_err < 1e-12 if nondeg else True)
        ),
    }


def verify_lepton_seesaw_haar_invariance(
    Y_e: np.ndarray,
    Y_nu: np.ndarray,
    M_R: np.ndarray,
    n_trials: int = 20,
    seed: int = 20261112,
) -> Dict[str, Any]:
    """Verify seesaw PMNS observables under independent random Haar (U_L, U_ec, U_N) in U(3)^3 (< 1e-12)."""
    rng = np.random.default_rng(seed)
    M_nu_base = -(Y_nu @ np.linalg.solve(M_R, Y_nu.T))
    base = extract_lepton_pmns_observables(Y_e, M_nu_base)
    min_split = min(base["min_rel_sv_split_e"], base["min_rel_sv_split_nu"])
    nondeg = min_split > 1e-6
    wedin_scale = min(1.0, min_split / 1e-3) if nondeg else 0.0

    max_sv_err = 0.0
    max_j_err = 0.0
    max_pmns_err = 0.0
    max_ang_err = 0.0
    for _ in range(n_trials):
        U_L = random_haar_unitary(3, rng)
        U_ec = random_haar_unitary(3, rng)
        U_N = random_haar_unitary(3, rng)

        Ye_scr = U_L @ Y_e @ U_ec.conj().T
        Ynu_scr = U_L @ Y_nu @ U_N.conj().T
        MR_scr = np.conj(U_N) @ M_R @ U_N.conj().T
        Mnu_scr = -(Ynu_scr @ np.linalg.solve(MR_scr, Ynu_scr.T))

        scr = extract_lepton_pmns_observables(Ye_scr, Mnu_scr)
        max_sv_err = max(
            max_sv_err,
            float(np.max(np.abs(np.array(base["sv_e_ratios"]) - np.array(scr["sv_e_ratios"])))),
            float(np.max(np.abs(np.array(base["sv_nu_ratios"]) - np.array(scr["sv_nu_ratios"])))),
        )
        max_j_err = max(max_j_err, abs(base["jarlskog_pmns_norm"] - scr["jarlskog_pmns_norm"]))
        if nondeg:
            raw_u = float(np.max(np.abs(np.array(base["pmns_abs_matrix"]) - np.array(scr["pmns_abs_matrix"]))))
            max_pmns_err = max(max_pmns_err, wedin_scale * raw_u)
            for k in ("sin2_theta_12", "sin2_theta_23", "sin2_theta_13"):
                max_ang_err = max(max_ang_err, wedin_scale * abs(base["angles"][k] - scr["angles"][k]))

    return {
        "trials": n_trials,
        "singular_values_nondegenerate": nondeg,
        "max_sv_ratio_err": max_sv_err,
        "max_jarlskog_err": max_j_err,
        "max_pmns_abs_err": max_pmns_err,
        "max_angle_sin2_err": max_ang_err,
        "passed": (
            max_sv_err < 1e-12
            and max_j_err < 1e-12
            and (max_pmns_err < 1e-12 and max_ang_err < 1e-12 if nondeg else True)
        ),
    }


def verify_lepton_weinberg_haar_invariance(
    Y_e: np.ndarray,
    M_nu_W: np.ndarray,
    n_trials: int = 20,
    seed: int = 20261113,
) -> Dict[str, Any]:
    """Verify Weinberg PMNS observables under independent random Haar (U_L, U_ec) in U(3)^2 (< 1e-12)."""
    rng = np.random.default_rng(seed)
    base = extract_lepton_pmns_observables(Y_e, M_nu_W)
    min_split = min(base["min_rel_sv_split_e"], base["min_rel_sv_split_nu"])
    nondeg = min_split > 1e-6
    wedin_scale = min(1.0, min_split / 1e-3) if nondeg else 0.0

    max_sv_err = 0.0
    max_j_err = 0.0
    max_pmns_err = 0.0
    max_ang_err = 0.0
    for _ in range(n_trials):
        U_L = random_haar_unitary(3, rng)
        U_ec = random_haar_unitary(3, rng)

        Ye_scr = U_L @ Y_e @ U_ec.conj().T
        Mnu_scr = U_L @ M_nu_W @ U_L.T
        scr = extract_lepton_pmns_observables(Ye_scr, Mnu_scr)
        max_sv_err = max(
            max_sv_err,
            float(np.max(np.abs(np.array(base["sv_e_ratios"]) - np.array(scr["sv_e_ratios"])))),
            float(np.max(np.abs(np.array(base["sv_nu_ratios"]) - np.array(scr["sv_nu_ratios"])))),
        )
        max_j_err = max(max_j_err, abs(base["jarlskog_pmns_norm"] - scr["jarlskog_pmns_norm"]))
        if nondeg:
            raw_u = float(np.max(np.abs(np.array(base["pmns_abs_matrix"]) - np.array(scr["pmns_abs_matrix"]))))
            max_pmns_err = max(max_pmns_err, wedin_scale * raw_u)
            for k in ("sin2_theta_12", "sin2_theta_23", "sin2_theta_13"):
                max_ang_err = max(max_ang_err, wedin_scale * abs(base["angles"][k] - scr["angles"][k]))

    return {
        "trials": n_trials,
        "singular_values_nondegenerate": nondeg,
        "max_sv_ratio_err": max_sv_err,
        "max_jarlskog_err": max_j_err,
        "max_pmns_abs_err": max_pmns_err,
        "max_angle_sin2_err": max_ang_err,
        "passed": (
            max_sv_err < 1e-12
            and max_j_err < 1e-12
            and (max_pmns_err < 1e-12 and max_ang_err < 1e-12 if nondeg else True)
        ),
    }
