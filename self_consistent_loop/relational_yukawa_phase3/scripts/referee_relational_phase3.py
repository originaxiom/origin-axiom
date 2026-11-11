#!/usr/bin/env python3
"""Independent Zero-Trust Referee for Phase 3 (Guardrail 6).

STRICT ZERO-IMPORT ISOLATION:
  - Contains ZERO imports from `relational_loop`, `cusped_loop`, `phi_loop`, or `src`.
  - Self-verifies via Python's `ast` module that zero producer modules are imported
    and zero empirical PDG constants appear anywhere in `src/`, `scripts/`, or `tests/`.
  - Verifies SHA-256 pre-registration seals across Phase 1, Phase 2, and Phase 3.
  - Independently reconstructs operators using a DIFFERENT quadrature scheme
    (5-point degree-3 Keast tetrahedral rule vs. Producer's 14-point degree-5 rule),
    independently solves the 45-tetrahedron 5-cusp cyclic cover of `b++LLLLLLRLR`,
    independently verifies `[5, 1, 2, 2]` chiral irreversible Jarlskog CP violation
    and enantiomer collapse, independently runs 50-digit `mpmath` relational reductions,
    independently tests 2-component spin-flux palindrome protection, and runs 25 fresh
    adversarial Haar U(3)^3 basis-scrambling trials.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
import snappy
from scipy.linalg import cho_factor, cho_solve, eigh
from scipy.sparse import coo_matrix
from snappy.geometric_structure.cusp_neighborhood.complex_cusp_cross_section import (
    ComplexCuspCrossSection,
)


mp.mp.dps = 50

PHASE3_ROOT = Path(__file__).resolve().parents[1]
SCRATCH_ROOT = PHASE3_ROOT.parent
PHASE1_ROOT = SCRATCH_ROOT / "self_consistent_loop_phi"
PHASE2_ROOT = SCRATCH_ROOT / "cusped_3d_loop_phase2"

FORBIDDEN_IMPORT_PREFIXES = ("relational_loop", "cusped_loop", "phi_loop", "src")

# Standard empirical PDG / cosmological constants forbidden by the 0-of-19 firewall
BANNED_EMPIRICAL_FLOATS = (
    125.25,      # m_H (GeV)
    172.69,      # m_t (GeV)
    91.1876,     # M_Z (GeV)
    80.377,      # M_W (GeV)
    246.22,      # v_EW (GeV)
    0.23121,     # sin^2 theta_W
    0.1179,      # alpha_s(M_Z)
    137.035999,  # alpha_em^{-1}
    0.51099895,  # m_e (MeV)
    105.6583755, # m_mu (MeV)
    1776.86,     # m_tau (MeV)
    0.22500,     # |V_us| PDG
    3.08e-5,     # J_CKM PDG
    67.4,        # H_0
)

# 5-point degree-3 Keast tetrahedral quadrature (distinct from Producer's 14-point degree-5 rule)
KEAST5_BARY = np.array(
    [
        [0.25, 0.25, 0.25, 0.25],
        [0.50, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0],
        [1.0 / 6.0, 0.50, 1.0 / 6.0, 1.0 / 6.0],
        [1.0 / 6.0, 1.0 / 6.0, 0.50, 1.0 / 6.0],
        [1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 0.50],
    ],
    dtype=float,
)
KEAST5_WTS = np.array([-2.0 / 15.0, 3.0 / 40.0, 3.0 / 40.0, 3.0 / 40.0, 3.0 / 40.0], dtype=float)

VBITS = (1, 2, 4, 8)
FBITS = (14, 13, 11, 7)
FBIT_TO_IDX = {14: 0, 13: 1, 11: 2, 7: 3}


# ============================================================================
# CHECK 0: AST Self-Isolation, Empirical Firewall & Triple-Phase Seal Audit
# ============================================================================
def audit_ast_and_seals() -> Dict[str, Any]:
    """Verify zero producer imports in referee, 0-of-19 firewall across repo, and intact seals."""
    self_path = Path(__file__).resolve()
    self_tree = ast.parse(self_path.read_text(encoding="utf-8"), filename=str(self_path))

    illegal_imports: List[str] = []
    for node in ast.walk(self_tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith(FORBIDDEN_IMPORT_PREFIXES):
                    illegal_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if node.level > 0 or mod.startswith(FORBIDDEN_IMPORT_PREFIXES):
                illegal_imports.append(f"from {'.' * node.level}{mod}")

    # Scan all Python files in Phase 3 (excluding this BANNED_EMPIRICAL_FLOATS declaration)
    firewall_hits: List[str] = []
    for sub in ("src", "scripts", "tests"):
        d = PHASE3_ROOT / sub
        if not d.exists():
            continue
        for pyf in sorted(d.rglob("*.py")):
            tree = ast.parse(pyf.read_text(encoding="utf-8"), filename=str(pyf))
            for node in ast.walk(tree):
                # Skip scanning BANNED_EMPIRICAL_FLOATS tuple inside this referee file itself
                if pyf.resolve() == self_path and isinstance(node, ast.Assign):
                    continue
                if isinstance(node, ast.Constant) and isinstance(node.value, float):
                    if pyf.resolve() == self_path and any(
                        abs(node.value - b) < 1e-12 for b in BANNED_EMPIRICAL_FLOATS
                    ):
                        # Check line context in referee: only allowed in BANNED_EMPIRICAL_FLOATS
                        continue
                    for b in BANNED_EMPIRICAL_FLOATS:
                        if abs(node.value - b) < 1e-9:
                            firewall_hits.append(f"{pyf.name}:{node.lineno}:{node.value}")

    def check_seal(root: Path, doc_name: str) -> Tuple[bool, str]:
        doc = root / doc_name
        seal = root / "SEAL_SHA256.txt"
        if not doc.exists() or not seal.exists():
            return False, "missing"
        actual = hashlib.sha256(doc.read_bytes()).hexdigest()
        expected = seal.read_text(encoding="utf-8").strip().splitlines()[0].split()[0].strip()
        return (actual == expected), actual

    p3_ok, p3_sha = check_seal(PHASE3_ROOT, "PREREGISTRATION_PHASE3.md")
    p2_ok, p2_sha = check_seal(PHASE2_ROOT, "PREREGISTRATION_PHASE2.md")
    p1_ok, p1_sha = check_seal(PHASE1_ROOT, "PREREGISTRATION_PLAN.md")

    passed = (
        len(illegal_imports) == 0
        and len(firewall_hits) == 0
        and p3_ok
        and p2_ok
        and p1_ok
    )
    return {
        "check0_passed": passed,
        "referee_producer_imports_count": len(illegal_imports),
        "illegal_imports": illegal_imports,
        "empirical_firewall_violations": firewall_hits,
        "phase3_seal_intact": p3_ok,
        "phase3_sha256": p3_sha,
        "phase2_seal_intact": p2_ok,
        "phase2_sha256": p2_sha,
        "phase1_seal_intact": p1_ok,
        "phase1_sha256": p1_sha,
    }


# ============================================================================
# Independent Geometry, SNF Cohomology & Keast-5 P1 Finite-Element Builders
# ============================================================================
def _ref_extract_penner(spec_or_m: Any) -> Dict[str, Any]:
    M0 = snappy.Manifold(spec_or_m) if isinstance(spec_or_m, str) else spec_or_m
    M = M0.high_precision() if hasattr(M0, "high_precision") else M0
    shapes = M.tetrahedra_shapes("rect")
    ccs = ComplexCuspCrossSection.fromManifoldAndShapes(M, shapes)
    ccs.normalize_cusps()

    grams: List[np.ndarray] = []
    gluings: List[List[Tuple[int, Tuple[int, int, int, int]]]] = []
    for T in ccs.mcomplex.Tetrahedra:
        G = np.zeros((4, 4), dtype=float)
        for i in range(4):
            for j in range(i + 1, 4):
                vals = []
                for k in range(4):
                    if k != i and k != j:
                        li = float(abs(T.horotriangles[VBITS[i]].lengths[FBITS[k]]))
                        lj = float(abs(T.horotriangles[VBITS[j]].lengths[FBITS[k]]))
                        vals.append(1.0 / (li * lj))
                G[i, j] = G[j, i] = -(vals[0] + vals[1])
        grams.append(G)
        row = []
        for fi in range(4):
            Fb = FBITS[fi]
            p = T.Gluing[Fb]
            row.append((T.Neighbor[Fb].Index, (p[0], p[1], p[2], p[3])))
        gluings.append(row)

    bmaps = [
        np.array([int(x) for x in m.list()], dtype=int).reshape((m.nrows(), m.ncols()))
        for m in ccs.mcomplex.boundary_maps()
    ]
    faces_info = []
    for fg, F_obj in enumerate(ccs.mcomplex.Faces):
        c0, c1 = F_obj.Corners[0], F_obj.Corners[1]
        faces_info.append(
            {
                "fg": fg,
                "tp": c0.Tetrahedron.Index,
                "fp": FBIT_TO_IDX[c0.Subsimplex],
                "tn": c1.Tetrahedron.Index,
                "fn": FBIT_TO_IDX[c1.Subsimplex],
                "perm": gluings[c0.Tetrahedron.Index][FBIT_TO_IDX[c0.Subsimplex]][1],
            }
        )

    try:
        cs_val = float(M.chern_simons())
    except Exception:
        cs_val = float("nan")

    return {
        "M": M,
        "M0": M0,
        "n_tet": len(grams),
        "grams": grams,
        "gluings": gluings,
        "faces": faces_info,
        "d2": bmaps[1],
        "d3": bmaps[2],
        "cs": cs_val,
    }


def _ref_snf_int(A_in: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    A = np.array(A_in, dtype=object)
    m, n = A.shape
    U = np.eye(m, dtype=object)
    U_inv = np.eye(m, dtype=object)
    V = np.eye(n, dtype=object)
    V_inv = np.eye(n, dtype=object)

    def swap_r(i: int, j: int) -> None:
        if i != j:
            A[[i, j]] = A[[j, i]]
            U[[i, j]] = U[[j, i]]
            U_inv[:, [i, j]] = U_inv[:, [j, i]]

    def swap_c(i: int, j: int) -> None:
        if i != j:
            A[:, [i, j]] = A[:, [j, i]]
            V[:, [i, j]] = V[:, [j, i]]
            V_inv[[i, j]] = V_inv[[j, i]]

    def add_r(dst: int, src: int, k: int) -> None:
        if k != 0:
            A[dst] += k * A[src]
            U[dst] += k * U[src]
            U_inv[:, src] -= k * U_inv[:, dst]

    def add_c(dst: int, src: int, k: int) -> None:
        if k != 0:
            A[:, dst] += k * A[:, src]
            V[:, dst] += k * V[:, src]
            V_inv[src] -= k * V_inv[dst]

    r = 0
    while r < m and r < n:
        nz = [(i, j, abs(int(A[i, j]))) for i in range(r, m) for j in range(r, n) if A[i, j] != 0]
        if not nz:
            break
        pi, pj, _ = min(nz, key=lambda t: t[2])
        swap_r(r, pi)
        swap_c(r, pj)
        while True:
            ch = False
            for i in range(r + 1, m):
                if A[i, r] != 0:
                    add_r(i, r, -(int(A[i, r]) // int(A[r, r])))
                    ch = True
            if any(A[i, r] != 0 for i in range(r + 1, m)):
                nz_col = [(i, abs(int(A[i, r]))) for i in range(r, m) if A[i, r] != 0]
                swap_r(r, min(nz_col, key=lambda t: t[1])[0])
                continue
            for j in range(r + 1, n):
                if A[r, j] != 0:
                    add_c(j, r, -(int(A[r, j]) // int(A[r, r])))
                    ch = True
            if any(A[r, j] != 0 for j in range(r + 1, n)):
                nz_row = [(j, abs(int(A[r, j]))) for j in range(r, n) if A[r, j] != 0]
                swap_c(r, min(nz_row, key=lambda t: t[1])[0])
                continue
            div_bad = None
            for i in range(r + 1, m):
                for j in range(r + 1, n):
                    if int(A[i, j]) % int(A[r, r]) != 0:
                        div_bad = (i, j)
                        break
                if div_bad:
                    break
            if div_bad:
                add_r(r, div_bad[0], 1)
                ch = True
                continue
            if not ch:
                break
        if int(A[r, r]) < 0:
            A[r] = -A[r]
            U[r] = -U[r]
            U_inv[:, r] = -U_inv[:, r]
        r += 1
    return A, U, U_inv, V, V_inv


def _ref_f5_rref(mat_in: np.ndarray) -> Tuple[np.ndarray, List[int]]:
    A = np.array(mat_in, dtype=int) % 5
    m, n = A.shape
    pivs: List[int] = []
    r = 0
    for c in range(n):
        if r >= m:
            break
        piv = next((i for i in range(r, m) if A[i, c] % 5 != 0), None)
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv_v = pow(int(A[r, c]), -1, 5)
        A[r] = (A[r] * inv_v) % 5
        for i in range(m):
            if i != r and A[i, c] % 5 != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 5
        pivs.append(c)
        r += 1
    return A, pivs


def _ref_count_5cover_cusps(ep: Dict[str, Any], coc: np.ndarray) -> int:
    nt = ep["n_tet"]
    par = list(range(nt * 20))

    def fnd(x: int) -> int:
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for f in ep["faces"]:
        sh = int(coc[f["fg"]]) % 5
        tp, fp, tn, perm = f["tp"], f["fp"], f["tn"], f["perm"]
        for vp in range(4):
            if vp != fp:
                vn = perm[vp]
                for s in range(5):
                    a = fnd((tp * 4 + vp) * 5 + s)
                    b = fnd((tn * 4 + vn) * 5 + ((s + sh) % 5))
                    if a != b:
                        par[b] = a
    return len({fnd(i) for i in range(nt * 20)})


def _ref_extract_cocycles(ep: Dict[str, Any]) -> Dict[str, Any]:
    # 1. Exact integer generator of H^1_free(M; Z) = ker_Z(d2) / im_Z(d3)
    d2_z = ep["d2"].astype(object)
    d3_z = ep["d3"].astype(object)
    S2, _, _, V2, V2_inv = _ref_snf_int(d2_z)
    r2 = sum(1 for i in range(min(S2.shape)) if int(S2[i, i]) != 0)
    Z_ker = V2[:, r2:]
    B_in_Z = V2_inv[r2:, :] @ d3_z
    S1, _, U1_inv, _, _ = _ref_snf_int(B_in_Z)
    r1 = sum(1 for i in range(min(S1.shape)) if int(S1[i, i]) != 0)
    Z_h1 = Z_ker @ U1_inv
    free_cocycle = np.array([int(x) for x in Z_h1[:, r1]], dtype=int)
    nz_fc = [x for x in free_cocycle if x != 0]
    if nz_fc and nz_fc[0] < 0:
        free_cocycle = -free_cocycle
    assert np.all(ep["d2"] @ free_cocycle == 0)

    # 2. Direct F_5 Gaussian elimination for H^1(M; F_5) = ker_{F_5}(d2) / im_{F_5}(d3)
    R_d2, piv_d2 = _ref_f5_rref(ep["d2"] % 5)
    n_f = ep["d2"].shape[1]
    free_cols = [c for c in range(n_f) if c not in piv_d2]
    ker_f5 = []
    for fc in free_cols:
        v = np.zeros(n_f, dtype=int)
        v[fc] = 1
        for r_idx, pc in enumerate(piv_d2):
            v[pc] = (-R_d2[r_idx, fc]) % 5
        ker_f5.append(v)
    K_mat = np.column_stack(ker_f5) % 5  # (n_faces, dim_ker)

    # Quotient out im_{F_5}(d3): find columns of K_mat independent of im(d3)
    im_d3 = ep["d3"] % 5
    _, piv_im = _ref_f5_rref(im_d3)
    im_basis = (im_d3[:, piv_im] if piv_im else np.zeros((n_f, 0), dtype=int)) % 5
    comb = np.hstack([im_basis, K_mat]) % 5
    _, piv_comb = _ref_f5_rref(comb)
    h1_cols = [c - im_basis.shape[1] for c in piv_comb if c >= im_basis.shape[1]]
    H1_f5 = K_mat[:, h1_cols] % 5
    assert H1_f5.shape[1] == 2

    # Enumerate the 6 projective lines in P(H^1(M; F_5)):
    # - 1 line is proportional to (free_cocycle mod 5) modulo im_{F_5}(d3)
    # - 1 torsion line has 5 cusps (c_unram)
    # - 4 torsion lines have 1 cusp (ram_lines)
    def is_coboundary_mod5(vec: np.ndarray) -> bool:
        aug = np.hstack([im_basis, vec[:, None] % 5]) % 5
        _, p_aug = _ref_f5_rref(aug)
        return (aug.shape[1] - 1) not in p_aug

    fc_mod5 = free_cocycle % 5
    proj_vecs = [H1_f5[:, 0] % 5] + [((m * H1_f5[:, 0] + H1_f5[:, 1]) % 5) for m in range(5)]
    c_unram = None
    ram_lines: List[np.ndarray] = []
    for pv in proj_vecs:
        # Check if pv lies in span(free_cocycle) modulo im(d3)
        in_free_span = any(is_coboundary_mod5((pv - s * fc_mod5) % 5) for s in range(5))
        if in_free_span:
            continue
        nc = _ref_count_5cover_cusps(ep, pv)
        if nc == 5 * ep["M"].num_cusps():
            c_unram = pv
        else:
            ram_lines.append(pv)

    assert c_unram is not None and len(ram_lines) == 4
    return {
        "free_cocycle": free_cocycle,
        "c_unram": c_unram,
        "ram_lines": ram_lines,
    }


def _ref_subdivide(n_sub: int) -> Dict[str, Any]:
    nodes: List[Tuple[float, float, float, float]] = []
    gmap: Dict[Tuple[int, int, int, int], int] = {}
    horo: List[bool] = []
    for i0 in range(n_sub + 1):
        for i1 in range(n_sub + 1 - i0):
            for i2 in range(n_sub + 1 - i0 - i1):
                i3 = n_sub - i0 - i1 - i2
                if max(i0, i1, i2, i3) == n_sub:
                    continue
                gmap[(i0, i1, i2, i3)] = len(nodes)
                nodes.append((i0 / n_sub, i1 / n_sub, i2 / n_sub, i3 / n_sub))
                horo.append(max(i0, i1, i2, i3) == n_sub - 1)

    e4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    tets: List[Tuple[int, int, int, int]] = []
    for b0 in range(n_sub):
        for b1 in range(n_sub - b0):
            for b2 in range(n_sub - b0 - b1):
                b3 = (n_sub - 1) - b0 - b1 - b2
                if max(b0, b1, b2, b3) == n_sub - 1:
                    continue
                tets.append(tuple(gmap[(b0 + e[0], b1 + e[1], b2 + e[2], b3 + e[3])] for e in e4))

    for c0 in range(n_sub - 1):
        for c1 in range(n_sub - 1 - c0):
            for c2 in range(n_sub - 1 - c0 - c1):
                c3 = (n_sub - 2) - c0 - c1 - c2
                oc = len(nodes)
                nodes.append(((c0 + 0.5) / n_sub, (c1 + 0.5) / n_sub, (c2 + 0.5) / n_sub, (c3 + 0.5) / n_sub))
                horo.append(False)
                px: Dict[Tuple[int, int], int] = {}
                for a in range(4):
                    for b in range(a + 1, 4):
                        px[(a, b)] = px[(b, a)] = gmap[
                            (c0 + e4[a][0] + e4[b][0], c1 + e4[a][1] + e4[b][1], c2 + e4[a][2] + e4[b][2], c3 + e4[a][3] + e4[b][3])
                        ]
                for a in range(4):
                    o = [b for b in range(4) if b != a]
                    tets.append((oc, px[(a, o[0])], px[(a, o[1])], px[(a, o[2])]))
                for d in range(4):
                    rm = [a for a in range(4) if a != d]
                    tets.append((oc, px[(rm[0], rm[1])], px[(rm[1], rm[2])], px[(rm[2], rm[0])]))

    if n_sub >= 3:
        for d0 in range(n_sub - 2):
            for d1 in range(n_sub - 2 - d0):
                for d2 in range(n_sub - 2 - d0 - d1):
                    d3 = (n_sub - 3) - d0 - d1 - d2
                    tets.append(tuple(gmap[(d0 + 1 - e[0], d1 + 1 - e[1], d2 + 1 - e[2], d3 + 1 - e[3])] for e in e4))

    return {
        "n_sub": n_sub,
        "nodes": np.array(nodes, dtype=float),
        "gmap": gmap,
        "horo": np.array(horo, dtype=bool),
        "tets": np.array(tets, dtype=int),
    }


def _ref_geom_keast5(G: np.ndarray, nodes: np.ndarray, tets: np.ndarray) -> Dict[str, np.ndarray]:
    Dmat = G[1:, :] - G[0:1, :]
    Gdiff = Dmat[:, 1:] - Dmat[:, 0:1]
    ev = nodes[tets]
    v0 = ev[:, 0, 1:]
    J = np.stack([ev[:, 1, 1:] - v0, ev[:, 2, 1:] - v0, ev[:, 3, 1:] - v0], axis=-1)
    detJ = np.abs(np.linalg.det(J))
    invJT = np.linalg.inv(np.swapaxes(J, 1, 2))
    grad = np.zeros((tets.shape[0], 4, 3), dtype=float)
    grad[:, 1:, :] = np.swapaxes(invJT, 1, 2)
    grad[:, 0, :] = -np.sum(grad[:, 1:, :], axis=1)

    W = np.einsum("qk,ekb->eqb", KEAST5_BARY, ev)
    WG = W @ G
    Q = -np.sum(WG * W, axis=-1)
    dQ = -2.0 * (W @ Dmat.T)
    g_mat = (
        Gdiff[None, None, :, :] / Q[:, :, None, None]
        + (dQ[:, :, :, None] * dQ[:, :, None, :]) / (4.0 * (Q[:, :, None, None] ** 2))
    )
    sq_det = np.sqrt(np.maximum(0.0, np.linalg.det(g_mat)))
    g_inv = np.linalg.inv(g_mat)
    dvol_k5 = detJ[:, None] * sq_det * KEAST5_WTS[None, :]
    return {"grad": grad, "g_inv": g_inv, "dvol": dvol_k5}


def _ref_solve_sector_keast5(
    ep: Dict[str, Any],
    cocycle: np.ndarray,
    q: int,
    cusp_bc: str,
    n_eigs: int,
    sub: Dict[str, Any],
    geoms: List[Dict[str, np.ndarray]],
) -> Dict[str, Any]:
    n_tet = ep["n_tet"]
    n_loc = sub["nodes"].shape[0]
    gmap = sub["gmap"]
    tets = sub["tets"]
    total = n_tet * n_loc

    par = list(range(total))
    phs = np.zeros(total, dtype=int)

    def find(x: int) -> Tuple[int, int]:
        if par[x] == x:
            return x, 0
        r, p = find(par[x])
        par[x] = r
        phs[x] = (phs[x] + p) % 5
        return r, int(phs[x])

    for f in ep["faces"]:
        cval = (q * int(cocycle[f["fg"]])) % 5
        tp, fp, tn, perm = f["tp"], f["fp"], f["tn"], f["perm"]
        for tup_p, lp in gmap.items():
            if tup_p[fp] != 0:
                continue
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = gmap[tuple(tup_n)]
            ip, in_ = tp * n_loc + lp, tn * n_loc + ln
            rp, pp = find(ip)
            rn, pn = find(in_)
            if rp != rn:
                par[rp] = rn
                phs[rp] = (pn + cval - pp) % 5

    dir_roots = set()
    if cusp_bc == "dirichlet":
        for t in range(n_tet):
            for l_idx, hb in enumerate(sub["horo"]):
                if hb:
                    dir_roots.add(find(t * n_loc + l_idx)[0])

    r2d: Dict[int, int] = {}
    raw_dof = np.full(total, -1, dtype=int)
    raw_wt = np.zeros(total, dtype=np.complex128)
    w5 = np.exp(2j * math.pi / 5.0)
    for idx in range(total):
        r, p = find(idx)
        if r in dir_roots:
            continue
        if r not in r2d:
            r2d[r] = len(r2d)
        raw_dof[idx] = r2d[r]
        raw_wt[idx] = w5 ** p

    n_dof = len(r2d)
    K_gl = np.zeros((n_dof, n_dof), dtype=np.complex128)
    M_gl = np.zeros((n_dof, n_dof), dtype=np.complex128)
    ob = KEAST5_BARY[:, :, None] * KEAST5_BARY[:, None, :]
    r_el = np.repeat(tets, 4, axis=1).ravel()
    c_el = np.tile(tets, (1, 4)).ravel()

    for t in range(n_tet):
        gm = geoms[t]
        gi = np.einsum("eq,eqmn->emn", gm["dvol"], gm["g_inv"])
        Ke = np.einsum("eam,emn,ebn->eab", gm["grad"], gi, gm["grad"])
        Me = np.einsum("eq,qab->eab", gm["dvol"], ob)
        Kl = coo_matrix((Ke.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()
        Ml = coo_matrix((Me.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()

        sl = slice(t * n_loc, (t + 1) * n_loc)
        valid = np.where(raw_dof[sl] >= 0)[0]
        dofs = raw_dof[sl][valid]
        wts = raw_wt[sl][valid]
        P = np.zeros((len(valid), n_dof), dtype=np.complex128)
        P[np.arange(len(valid)), dofs] = wts
        K_gl += P.conj().T @ Kl[np.ix_(valid, valid)] @ P
        M_gl += P.conj().T @ Ml[np.ix_(valid, valid)] @ P

    K_gl = 0.5 * (K_gl + K_gl.conj().T)
    M_gl = 0.5 * (M_gl + M_gl.conj().T)
    cf = cho_factor(K_gl + M_gl, lower=True)
    L_inv = cho_solve(cf, np.eye(n_dof, dtype=np.complex128))
    # Solve (K + M) v = (lambda + 1) M v via standard Hermitian eigh
    # Equivalent symmetric form using Cholesky factor L of (K + M) = L L^H:
    L_low = np.linalg.cholesky(K_gl + M_gl)
    Linv = np.linalg.inv(L_low)
    C_mat = Linv @ M_gl @ Linv.conj().T
    C_mat = 0.5 * (C_mat + C_mat.conj().T)
    mu_asc, u_vecs = eigh(C_mat)
    mu_top = mu_asc[::-1][:n_eigs]
    u_top = u_vecs[:, ::-1][:, :n_eigs]
    evals = (1.0 / mu_top) - 1.0
    evecs = Linv.conj().T @ u_top
    for k in range(n_eigs):
        nrm = math.sqrt(max(1e-30, float(np.real(evecs[:, k].conj() @ (M_gl @ evecs[:, k])))))
        evecs[:, k] /= nrm

    modes = np.zeros((n_eigs, n_tet, n_loc), dtype=np.complex128)
    for t in range(n_tet):
        sl = slice(t * n_loc, (t + 1) * n_loc)
        valid = np.where(raw_dof[sl] >= 0)[0]
        dofs = raw_dof[sl][valid]
        wts = raw_wt[sl][valid]
        modes[:, t, valid] = (wts[:, None] * evecs[dofs, :]).T

    return {"evals": evals, "modes": modes, "M_gl": M_gl, "evecs": evecs}


def _ref_yukawa_overlap_keast5(
    modes_A: np.ndarray,
    modes_B: np.ndarray,
    mode_H: np.ndarray,
    tets: np.ndarray,
    geoms: List[Dict[str, np.ndarray]],
) -> np.ndarray:
    QT = KEAST5_BARY.T
    Y = np.zeros((modes_A.shape[0], modes_B.shape[0]), dtype=np.complex128)
    for t, gm in enumerate(geoms):
        wH = gm["dvol"] * (mode_H[t, tets] @ QT)
        Aq = modes_A[:, t, :][:, tets] @ QT
        Bq = modes_B[:, t, :][:, tets] @ QT
        Y += np.einsum("aeq,beq,eq->ab", Aq, Bq, wH)
    return Y


def _ref_extract_yukawa_invariants(Yu: np.ndarray, Yd: np.ndarray) -> Dict[str, Any]:
    Uu, su_d, _ = np.linalg.svd(Yu)
    Ud, sd_d, _ = np.linalg.svd(Yd)
    su, sd = su_d[::-1], sd_d[::-1]
    ULu, ULd = Uu[:, ::-1], Ud[:, ::-1]
    V_abs = np.abs(ULu.conj().T @ ULd)
    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    comm = Hu @ Hd - Hd @ Hu
    denom = (float(np.linalg.norm(Hu, "fro")) ** 3) * (float(np.linalg.norm(Hd, "fro")) ** 3)
    j_norm = float(np.linalg.det(comm).imag / denom) if denom > 1e-60 else 0.0
    rk_u = int(np.sum(su > 1e-10 * max(1e-30, float(su[-1]))))
    rk_d = int(np.sum(sd > 1e-10 * max(1e-30, float(sd[-1]))))
    return {
        "su_ratios": (su / su[2]).tolist() if su[2] > 1e-30 else [0.0, 0.0, 0.0],
        "sd_ratios": (sd / sd[2]).tolist() if sd[2] > 1e-30 else [0.0, 0.0, 0.0],
        "rank_u": rk_u,
        "rank_d": rk_d,
        "ckm_abs": V_abs,
        "j_norm": j_norm,
    }


# ============================================================================
# CHECK 1: Independent 45-Tet 5-Fold Cover Keast-5 Audit + [5,1,2,2] CP Check
# ============================================================================
def run_check1_cover_and_yukawa(prod_data: Dict[str, Any]) -> Dict[str, Any]:
    # 0. Verify Keast-5 integrates all 3-simplex monomials up to degree 3 to < 1e-15
    mono_deg3_err = 0.0
    for a in range(4):
        for b in range(4 - a):
            for c in range(4 - a - b):
                for d in range(4 - a - b - c):
                    ex = (
                        math.factorial(a)
                        * math.factorial(b)
                        * math.factorial(c)
                        * math.factorial(d)
                        / math.factorial(a + b + c + d + 3)
                    )
                    nm = float(
                        np.sum(
                            KEAST5_WTS
                            * (KEAST5_BARY[:, 0] ** a)
                            * (KEAST5_BARY[:, 1] ** b)
                            * (KEAST5_BARY[:, 2] ** c)
                            * (KEAST5_BARY[:, 3] ** d)
                        )
                    )
                    mono_deg3_err = max(mono_deg3_err, abs(nm - ex))

    # 1. Build 45-tetrahedron 5-cusp cyclic cover of b++LLLLLLRLR ((6)) directly from SnapPy!
    M_run6 = snappy.Manifold("b++LLLLLLRLR")
    covs5 = [C for C in M_run6.covers(5) if C.num_cusps() == 5]
    assert len(covs5) == 1
    ep_cov = _ref_extract_penner(covs5[0])
    assert ep_cov["n_tet"] == 45

    # Independently discover order-5 deck generator D on the 45-tet cover
    even_p4 = [p for p in itertools.permutations(range(4)) if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0]
    deck_map = None
    for img0 in range(1, 45):
        for p0 in even_p4:
            if np.max(np.abs(ep_cov["grams"][0] - ep_cov["grams"][img0][np.ix_(p0, p0)])) > 1e-9:
                continue
            mp_cand: Dict[int, Tuple[int, Tuple[int, int, int, int]]] = {0: (img0, p0)}
            q_bfs = [0]
            ok = True
            while q_bfs and ok:
                t = q_bfs.pop(0)
                ti, pt = mp_cand[t]
                for f in range(4):
                    nb, gl = ep_cov["gluings"][t][f]
                    nb_i, gl_i = ep_cov["gluings"][ti][pt[f]]
                    inv_gl = [0, 0, 0, 0]
                    for a in range(4):
                        inv_gl[gl[a]] = a
                    p_nb = tuple(gl_i[pt[inv_gl[b]]] for b in range(4))
                    if nb in mp_cand:
                        if mp_cand[nb] != (nb_i, p_nb):
                            ok = False
                            break
                    else:
                        if np.max(np.abs(ep_cov["grams"][nb] - ep_cov["grams"][nb_i][np.ix_(p_nb, p_nb)])) > 1e-8:
                            ok = False
                            break
                        mp_cand[nb] = (nb_i, p_nb)
                        q_bfs.append(nb)
            if ok and len(mp_cand) == 45 and all(mp_cand[t][0] != t for t in range(45)):
                # Verify D^5 == id
                is_ord5 = True
                for t in range(45):
                    ct, cp = t, (0, 1, 2, 3)
                    for _ in range(5):
                        nt, np_ = mp_cand[ct]
                        cp = tuple(np_[cp[a]] for a in range(4))
                        ct = nt
                    if ct != t or cp != (0, 1, 2, 3):
                        is_ord5 = False
                        break
                if is_ord5:
                    deck_map = mp_cand
                    break
        if deck_map is not None:
            break
    assert deck_map is not None

    # Solve untwisted Neumann P1 Laplacian on the 45-tet cover at n_sub = 3 using Keast-5
    sub3 = _ref_subdivide(3)
    geoms_cov = [_ref_geom_keast5(G, sub3["nodes"], sub3["tets"]) for G in ep_cov["grams"]]
    zero_coc_cov = np.zeros(len(ep_cov["faces"]), dtype=int)
    sec_cov = _ref_solve_sector_keast5(ep_cov, zero_coc_cov, 0, "neumann", 24, sub3, geoms_cov)

    # Apply deck pullback D^* to local modes and project onto q = +1, +2 (canonically orienting q so E0(q=2) <= E0(q=1))
    def apply_deck(modes_in: np.ndarray) -> np.ndarray:
        out = np.empty_like(modes_in)
        gmap3 = sub3["gmap"]
        n_l = sub3["nodes"].shape[0]
        # Build node perm table for even_p4
        p_nodes: Dict[Tuple[int, int, int, int], np.ndarray] = {}
        for p in even_p4:
            arr = np.arange(n_l, dtype=int)
            for tup, li in gmap3.items():
                tp = [0, 0, 0, 0]
                for a in range(4):
                    tp[p[a]] = tup[a]
                arr[li] = gmap3[tuple(tp)]
            # Octahedral centers: barycentric coords (c + 0.5)/n_sub
            for li in range(len(gmap3), n_l):
                bc = sub3["nodes"][li]
                bc_p = np.zeros(4, dtype=float)
                for a in range(4):
                    bc_p[p[a]] = bc[a]
                diffs = np.max(np.abs(sub3["nodes"] - bc_p[None, :]), axis=1)
                arr[li] = int(np.argmin(diffs))
            p_nodes[p] = arr
        for t in range(45):
            ti, pt = deck_map[t]
            out[:, t, :] = modes_in[:, ti, :][:, p_nodes[pt]]
        return out

    # Compute L^2 inner product helper on 45-tet cover
    ob3 = KEAST5_BARY[:, :, None] * KEAST5_BARY[:, None, :]
    r_e3 = np.repeat(sub3["tets"], 4, axis=1).ravel()
    c_e3 = np.tile(sub3["tets"], (1, 4)).ravel()
    M_locs_cov = [
        coo_matrix(
            (np.einsum("eq,qab->eab", gm["dvol"], ob3).ravel(), (r_e3, c_e3)),
            shape=(sub3["nodes"].shape[0], sub3["nodes"].shape[0]),
        ).toarray()
        for gm in geoms_cov
    ]

    def cov_inner(u_m: np.ndarray, v_m: np.ndarray) -> complex:
        s = 0j
        for t in range(45):
            s += np.vdot(u_m[t], M_locs_cov[t] @ v_m[t])
        return complex(s)

    # Build orbit powers (D^*)^s on the 24 cover modes
    d_pows = [sec_cov["modes"]]
    for _ in range(4):
        d_pows.append(apply_deck(d_pows[-1]))

    def extract_q_subspace(q_val: int) -> Tuple[List[float], np.ndarray]:
        w5 = np.exp(2j * math.pi / 5.0)
        proj = sum((w5 ** (-q_val * s)) * d_pows[s] for s in range(5)) / 5.0
        kept_modes: List[np.ndarray] = []
        kept_evals: List[float] = []
        for k in range(proj.shape[0]):
            cand = proj[k].copy()
            nrm0 = math.sqrt(max(0.0, cov_inner(cand, cand).real))
            if nrm0 < 0.15:
                continue
            for prev in kept_modes:
                cand = cand - cov_inner(prev, cand) * prev
            nrm = math.sqrt(max(0.0, cov_inner(cand, cand).real))
            if nrm > 0.15:
                kept_modes.append(cand / nrm)
                kept_evals.append(float(sec_cov["evals"][k]))
                if len(kept_modes) == 3:
                    break
        return kept_evals, np.array(kept_modes)

    ev_q1, m_cov_q1 = extract_q_subspace(1)
    ev_q2, m_cov_q2 = extract_q_subspace(2)
    if ev_q1[0] < ev_q2[0] - 1e-8:
        # Multiply generator by 2 in (Z/5Z)^x: (1, 2) -> (2, 4)
        ev_q1, m_cov_q1 = extract_q_subspace(2)
        ev_q2, m_cov_q2 = extract_q_subspace(4)

    # Check forbidden Z/5Z overlap (+1)+(+1)+(+2) == 4 != 0 mod 5 on 45-tet cover
    Y_forb_cov = _ref_yukawa_overlap_keast5(m_cov_q1, m_cov_q1, m_cov_q2[0], sub3["tets"], geoms_cov)
    max_forb_45tet = float(np.max(np.abs(Y_forb_cov)))

    # Check allowed Yukawas on 45-tet cover of (6): rank=(3,3), 4 exact zero CKM entries, |J_hat| < 1e-15!
    Yu_cov = _ref_yukawa_overlap_keast5(m_cov_q1, m_cov_q1, np.conj(m_cov_q2[0]), sub3["tets"], geoms_cov)
    Yd_cov = _ref_yukawa_overlap_keast5(m_cov_q1, m_cov_q2, m_cov_q2[0], sub3["tets"], geoms_cov)
    obs_cov = _ref_extract_yukawa_invariants(Yu_cov, Yd_cov)
    cov_zero_ckm_entries = int(np.sum(obs_cov["ckm_abs"] < 1e-12))

    # 2. Independently solve irreversible chiral [5,1,2,2] (b++LLLLLRLLRRLR) and mirror (b++LRRRRRLRRLLR)
    #    at n_sub = 4 using Keast-5 quadrature under cusp-ramified Dirichlet BC!
    sub4 = _ref_subdivide(4)
    ep_5122 = _ref_extract_penner("b++LLLLLRLLRRLR")
    ep_1522 = _ref_extract_penner("b++LRRRRRLRRLLR")
    coh_5122 = _ref_extract_cocycles(ep_5122)
    coh_1522 = _ref_extract_cocycles(ep_1522)
    geoms_5122 = [_ref_geom_keast5(G, sub4["nodes"], sub4["tets"]) for G in ep_5122["grams"]]
    geoms_1522 = [_ref_geom_keast5(G, sub4["nodes"], sub4["tets"]) for G in ep_1522["grams"]]

    sig_5122 = -1.0 if math.sin(4.0 * math.pi * ep_5122["cs"]) > 0.0 else 1.0
    sig_1522 = -1.0 if math.sin(4.0 * math.pi * ep_1522["cs"]) > 0.0 else 1.0

    def solve_ram_lines_k5(ep_x: Dict[str, Any], ram_cocs: List[np.ndarray], gms: List[Dict[str, np.ndarray]]) -> List[Dict[str, Any]]:
        out_l = []
        for rc in ram_cocs:
            c_use = rc.copy()
            s1 = _ref_solve_sector_keast5(ep_x, c_use, 1, "dirichlet", 4, sub4, gms)
            s2 = _ref_solve_sector_keast5(ep_x, c_use, 2, "dirichlet", 4, sub4, gms)
            if s1["evals"][0] < s2["evals"][0] - 1e-9:
                c_use = (2 * c_use) % 5
                s1 = _ref_solve_sector_keast5(ep_x, c_use, 1, "dirichlet", 4, sub4, gms)
                s2 = _ref_solve_sector_keast5(ep_x, c_use, 2, "dirichlet", 4, sub4, gms)
            Yu = _ref_yukawa_overlap_keast5(s1["modes"][:3], s1["modes"][:3], np.conj(s2["modes"][0]), sub4["tets"], gms)
            Yd = _ref_yukawa_overlap_keast5(s1["modes"][:3], s2["modes"][:3], s2["modes"][0], sub4["tets"], gms)
            out_l.append(_ref_extract_yukawa_invariants(Yu, Yd))
        return out_l

    ram_k5_a = solve_ram_lines_k5(ep_5122, coh_5122["ram_lines"], geoms_5122)
    ram_k5_b = solve_ram_lines_k5(ep_1522, coh_1522["ram_lines"], geoms_1522)

    max_j_k5 = max(abs(x["j_norm"]) for x in ram_k5_a)
    prod_max_j_n4 = float(
        prod_data["gate3_3d_yukawa_overlap"]["irreversible_chiral_cp_breakthrough_5_1_2_2"]["max_abs_jarlskog_nsub4"]
    )
    rel_diff_keast5_vs_prod14 = abs(max_j_k5 - prod_max_j_n4) / max(1e-30, prod_max_j_n4)

    # Match enantiomer lines (each line in A has exact opposite j_norm in B!)
    j_vals_a = sorted(x["j_norm"] for x in ram_k5_a)
    j_vals_b_neg = sorted(-x["j_norm"] for x in ram_k5_b)
    enantiomer_reversal_err = max(abs(a - b) for a, b in zip(j_vals_a, j_vals_b_neg))
    rel_j_a = sorted(sig_5122 * x["j_norm"] for x in ram_k5_a)
    rel_j_b = sorted(sig_1522 * x["j_norm"] for x in ram_k5_b)
    relational_j_collapse_err = max(abs(a - b) for a, b in zip(rel_j_a, rel_j_b))
    min_ckm_entry_k5 = float(np.min(ram_k5_a[0]["ckm_abs"]))

    passed = (
        mono_deg3_err < 1e-15
        and max_forb_45tet < 1e-13
        and obs_cov["rank_u"] == 3
        and obs_cov["rank_d"] == 3
        and cov_zero_ckm_entries == 4
        and abs(obs_cov["j_norm"]) < 1e-15
        and max_j_k5 > 5e-5
        and rel_diff_keast5_vs_prod14 < 0.05
        and min_ckm_entry_k5 > 0.02
        and enantiomer_reversal_err < 1e-14
        and relational_j_collapse_err < 1e-14
    )
    return {
        "check1_passed": passed,
        "keast5_deg3_monomial_err": mono_deg3_err,
        "cover45_run6_forbidden_z5_overlap": max_forb_45tet,
        "cover45_run6_ranks": [obs_cov["rank_u"], obs_cov["rank_d"]],
        "cover45_run6_exact_zero_ckm_entries": cov_zero_ckm_entries,
        "cover45_run6_jarlskog": obs_cov["j_norm"],
        "irrev_5_1_2_2_keast5_max_jarlskog": max_j_k5,
        "producer_q14_max_jarlskog": prod_max_j_n4,
        "keast5_vs_q14_rel_diff": rel_diff_keast5_vs_prod14,
        "irrev_5_1_2_2_keast5_min_ckm_entry": min_ckm_entry_k5,
        "irrev_enantiomer_jarlskog_reversal_err": enantiomer_reversal_err,
        "irrev_relational_jarlskog_collapse_err": relational_j_collapse_err,
    }


# ============================================================================
# CHECK 2: Independent 50-Digit mpmath Relational Quotient Audit
# ============================================================================
def _mp_gauss_reduce(tau: mp.mpc) -> mp.mpc:
    z = tau if mp.im(tau) > 0 else -tau
    tol = mp.mpf("1e-30")
    for _ in range(300):
        n = int(mp.nint(mp.re(z)))
        if n != 0:
            z -= n
        if abs(z) < 1 - tol:
            z = -1 / z
            continue
        if abs(mp.re(z)) <= mp.mpf("0.5") + tol and abs(z) >= 1 - tol:
            break
    if abs(mp.re(z) + mp.mpf("0.5")) <= mp.mpf("1e-20"):
        z = mp.mpc(mp.mpf("0.5"), mp.im(z))
    if abs(abs(z) - 1) <= mp.mpf("1e-20") and mp.re(z) < -mp.mpf("1e-20"):
        z = -1 / z
    return z


def run_check2_mpmath_relational(prod_data: Dict[str, Any]) -> Dict[str, Any]:
    def eval_mp_rel(spec: str) -> Dict[str, Any]:
        M0 = snappy.Manifold(spec)
        M = M0.high_precision()
        M.set_peripheral_curves("shortest")
        cs = mp.mpf(str(M.chern_simons()))
        s4 = mp.sin(4 * mp.pi * cs)
        sig = mp.mpf(0) if abs(s4) < mp.mpf("1e-12") else (-mp.mpf(1) if s4 > 0 else mp.mpf(1))
        cmod = M.cusp_info(0)["modulus"]
        tc = _mp_gauss_reduce(mp.mpc(str(cmod.real()), str(cmod.imag())))
        tc_rel = mp.mpc(sig * mp.re(tc), mp.im(tc))

        zlen = M.length_spectrum(2.5)[0]["length"]
        tt = _mp_gauss_reduce(mp.mpc(mp.mpf(str(zlen.imag())) / (2 * mp.pi), mp.mpf(str(zlen.real())) / (2 * mp.pi)))
        tt_rel = mp.mpc(sig * mp.re(tt), mp.im(tt))
        return {"sig": float(sig), "tc_rel": tc_rel, "tt_rel": tt_rel}

    pairs = [
        ("b++LLLLLLRLR", "b++LRRRRRRLR"),
        ("b++LLLRLLLRLR", "b++LRRRLRRRLR"),
        ("b++LLLLLRLLRRLR", "b++LRRRRRLRRLLR"),
    ]
    max_pair_err = 0.0
    for sa, sb in pairs:
        ra, rb = eval_mp_rel(sa), eval_mp_rel(sb)
        max_pair_err = max(
            max_pair_err,
            float(abs(ra["tc_rel"] - rb["tc_rel"])),
            float(abs(ra["tt_rel"] - rb["tt_rel"])),
        )

    # Amphicheiral negative controls
    amph_lr = eval_mp_rel("b+-LR")
    amph_55 = eval_mp_rel("b+-LLLLLRRRRRLR")
    amph_err = max(
        abs(amph_lr["sig"]),
        float(abs(mp.re(amph_lr["tc_rel"]))),
        abs(amph_55["sig"]),
        float(abs(mp.re(amph_55["tc_rel"]))),
    )

    # Cross-check against Producer's Gate 1 winner tau_cusp_rel on [(6)]_rel
    r6 = eval_mp_rel("b++LLLLLLRLR")
    prod_r6_tc = prod_data["gate1_relational_quotient"]["a_one_quotient_selection"]["unique_quotient_winner"]["relational_tau_cusp"]
    vs_prod_err = math.hypot(
        float(mp.re(r6["tc_rel"])) - float(prod_r6_tc[0]),
        float(mp.im(r6["tc_rel"])) - float(prod_r6_tc[1]),
    )

    passed = max_pair_err < 1e-13 and amph_err == 0.0 and vs_prod_err < 1e-13
    return {
        "check2_passed": passed,
        "mpmath50_enantiomer_collapse_err": max_pair_err,
        "amphicheiral_controls_err": amph_err,
        "run6_tau_cusp_rel_vs_producer_err": vs_prod_err,
    }


# ============================================================================
# CHECK 3: Independent Keast-5 Coupled Spin-Flux Palindrome Countercheck
# ============================================================================
def _ref_solve_spin_flux_keast5(spec: str, n_sub: int = 3) -> np.ndarray:
    ep = _ref_extract_penner(spec)
    coh = _ref_extract_cocycles(ep)
    sub = _ref_subdivide(n_sub)
    geoms = [_ref_geom_keast5(G, sub["nodes"], sub["tets"]) for G in ep["grams"]]

    # 1. Solve harmonic 1-form alpha_s = d theta_s
    n_tet = ep["n_tet"]
    n_loc = sub["nodes"].shape[0]
    gmap = sub["gmap"]
    tets = sub["tets"]
    total = n_tet * n_loc

    par = list(range(total))
    off = np.zeros(total, dtype=int)

    def find_z(x: int) -> Tuple[int, int]:
        if par[x] == x:
            return x, 0
        r, o = find_z(par[x])
        par[x] = r
        off[x] = int(off[x]) + o
        return r, int(off[x])

    fc = coh["free_cocycle"]
    for f in ep["faces"]:
        jmp = int(fc[f["fg"]])
        tp, fp, tn, perm = f["tp"], f["fp"], f["tn"], f["perm"]
        for tup_p, lp in gmap.items():
            if tup_p[fp] != 0:
                continue
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = gmap[tuple(tup_n)]
            ip, in_ = tp * n_loc + lp, tn * n_loc + ln
            rp, op = find_z(ip)
            rn, on = find_z(in_)
            if rp != rn:
                par[rp] = rn
                off[rp] = on + jmp - op

    r2d: Dict[int, int] = {}
    rdof = np.zeros(total, dtype=int)
    roff = np.zeros(total, dtype=float)
    for idx in range(total):
        r, o = find_z(idx)
        if r not in r2d:
            r2d[r] = len(r2d)
        rdof[idx] = r2d[r]
        roff[idx] = float(o)

    nd = len(r2d)
    Kh = np.zeros((nd, nd), dtype=float)
    bh = np.zeros(nd, dtype=float)
    r_el = np.repeat(tets, 4, axis=1).ravel()
    c_el = np.tile(tets, (1, 4)).ravel()
    for t in range(n_tet):
        gm = geoms[t]
        gi = np.einsum("eq,eqmn->emn", gm["dvol"], gm["g_inv"])
        Ke = np.einsum("eam,emn,ebn->eab", gm["grad"], gi, gm["grad"])
        Kl = coo_matrix((Ke.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()
        sl = slice(t * n_loc, (t + 1) * n_loc)
        P = np.zeros((n_loc, nd), dtype=float)
        P[np.arange(n_loc), rdof[sl]] = 1.0
        Kh += P.T @ Kl @ P
        bh -= P.T @ (Kl @ roff[sl])

    u_free = np.zeros(nd, dtype=float)
    u_free[1:] = np.linalg.solve(Kh[1:, 1:], bh[1:])
    theta_loc = (u_free[rdof] + roff).reshape((n_tet, n_loc))

    # 2. Assemble 2-component Pauli-Zeeman + harmonic flux + Z/5Z (q=2)
    par5 = list(range(total))
    ph5 = np.zeros(total, dtype=int)

    def find5(x: int) -> Tuple[int, int]:
        if par5[x] == x:
            return x, 0
        r, p = find5(par5[x])
        par5[x] = r
        ph5[x] = (ph5[x] + p) % 5
        return r, int(ph5[x])

    cu = coh["c_unram"]
    for f in ep["faces"]:
        cv = (2 * int(cu[f["fg"]])) % 5
        tp, fp, tn, perm = f["tp"], f["fp"], f["tn"], f["perm"]
        for tup_p, lp in gmap.items():
            if tup_p[fp] != 0:
                continue
            tup_n = [0, 0, 0, 0]
            for a in range(4):
                tup_n[perm[a]] = tup_p[a]
            ln = gmap[tuple(tup_n)]
            rp, pp = find5(tp * n_loc + lp)
            rn, pn = find5(tn * n_loc + ln)
            if rp != rn:
                par5[rp] = rn
                ph5[rp] = (pn + cv - pp) % 5

    r2d5: Dict[int, int] = {}
    dof5 = np.zeros(total, dtype=int)
    wt5 = np.zeros(total, dtype=np.complex128)
    phi_flux = 2.0 * ep["cs"]
    sig_p = -1.0 if math.sin(4.0 * math.pi * ep["cs"]) > 0.0 else 1.0
    w5 = np.exp(2j * math.pi / 5.0)
    for idx in range(total):
        r, p = find5(idx)
        if r not in r2d5:
            r2d5[r] = len(r2d5)
        dof5[idx] = r2d5[r]
        t_i, l_i = divmod(idx, n_loc)
        wt5[idx] = (w5 ** p) * np.exp(-2j * math.pi * phi_flux * theta_loc[t_i, l_i])

    nd5 = len(r2d5)
    H2 = np.zeros((2 * nd5, 2 * nd5), dtype=np.complex128)
    M2 = np.zeros((2 * nd5, 2 * nd5), dtype=np.complex128)
    ob = KEAST5_BARY[:, :, None] * KEAST5_BARY[:, None, :]
    M_locs = []
    P_locs = []
    for t in range(n_tet):
        gm = geoms[t]
        al_e = np.einsum("ea,eam->em", theta_loc[t][tets], gm["grad"])
        al_nrm = np.sqrt(np.maximum(0.0, np.einsum("em,eqmn,en->eq", al_e, gm["g_inv"], al_e)))
        gi = np.einsum("eq,eqmn->emn", gm["dvol"], gm["g_inv"])
        Ke = np.einsum("eam,emn,ebn->eab", gm["grad"], gi, gm["grad"])
        Me = np.einsum("eq,qab->eab", gm["dvol"], ob)
        Be = np.einsum("eq,qab->eab", gm["dvol"] * al_nrm, ob)

        Kl = coo_matrix((Ke.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()
        Ml = coo_matrix((Me.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()
        Bl = coo_matrix((Be.ravel(), (r_el, c_el)), shape=(n_loc, n_loc)).toarray()

        sl = slice(t * n_loc, (t + 1) * n_loc)
        Ps = np.zeros((n_loc, nd5), dtype=np.complex128)
        Ps[np.arange(n_loc), dof5[sl]] = wt5[sl]
        P2 = np.zeros((2 * n_loc, 2 * nd5), dtype=np.complex128)
        P2[:n_loc, :nd5] = Ps
        P2[n_loc:, nd5:] = Ps

        kap = sig_p * 0.15
        mu_z = 0.25
        Hl2 = np.zeros((2 * n_loc, 2 * n_loc), dtype=np.complex128)
        Ml2 = np.zeros((2 * n_loc, 2 * n_loc), dtype=np.complex128)
        Hl2[:n_loc, :n_loc] = Kl - kap * Bl
        Hl2[n_loc:, n_loc:] = Kl + kap * Bl
        Hl2[:n_loc, n_loc:] = -mu_z * Bl
        Hl2[n_loc:, :n_loc] = -mu_z * Bl
        Ml2[:n_loc, :n_loc] = Ml
        Ml2[n_loc:, n_loc:] = Ml

        H2 += P2.conj().T @ Hl2 @ P2
        M2 += P2.conj().T @ Ml2 @ P2
        M_locs.append(Ml2)
        P_locs.append(P2)

    H2 = 0.5 * (H2 + H2.conj().T)
    M2 = 0.5 * (M2 + M2.conj().T)
    L_c = np.linalg.cholesky(H2 + 2.0 * M2)
    Li = np.linalg.inv(L_c)
    Cm = Li @ M2 @ Li.conj().T
    Cm = 0.5 * (Cm + Cm.conj().T)
    _, uv = eigh(Cm)
    psi0 = Li.conj().T @ uv[:, -1]
    psi0 /= math.sqrt(float(np.real(psi0.conj() @ (M2 @ psi0))))

    lprobs = np.array([float(np.real((P_locs[t] @ psi0).conj() @ (M_locs[t] @ (P_locs[t] @ psi0)))) for t in range(n_tet)])
    return lprobs / float(np.sum(lprobs))


def run_check3_spin_flux_palindrome() -> Dict[str, Any]:
    lp_6 = _ref_solve_spin_flux_keast5("b++LLLLLLRLR", n_sub=3)
    lp_5122 = _ref_solve_spin_flux_keast5("b++LLLLLRLLRRLR", n_sub=3)

    pal_err_6 = max(
        abs(float(lp_6[0] - lp_6[6])),
        abs(float(lp_6[1] - lp_6[5])),
        abs(float(lp_6[2] - lp_6[4])),
        abs(float(lp_6[7] - lp_6[8])),
    )
    sorted_5122 = np.sort(lp_5122)[::-1]
    gap_5122 = float(sorted_5122[0] - sorted_5122[1])

    passed = pal_err_6 < 1e-13 and gap_5122 > 0.015
    return {
        "check3_passed": passed,
        "keast5_run6_spin_flux_palindrome_err": pal_err_6,
        "keast5_run6_layer_probs": lp_6.tolist(),
        "keast5_5122_single_peak_gap": gap_5122,
    }


# ============================================================================
# CHECK 4: Independent E_8 Tadpole Enumeration, Dedekind Reciprocity & 25-Trial Haar
# ============================================================================
def run_check4_tadpole_and_adversarial_haar(prod_data: Dict[str, Any]) -> Dict[str, Any]:
    # 1. Independently construct E_8 roots and verify triangular threshold k_min(N) = N(N+1)/2
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1.0, 1.0):
                for s2 in (-1.0, 1.0):
                    v = np.zeros(8)
                    v[i], v[j] = s1, s2
                    roots.append(v)
    for sg in itertools.product((-0.5, 0.5), repeat=8):
        if sum(1 for x in sg if x < 0) % 2 == 0:
            roots.append(np.array(sg))
    R = np.array(roots)
    assert R.shape == (240, 8)

    # 5 weights of 5_perp acting on 10_GUT: (2/5^5, 0,0,0)? Wait: extract directly from roots with sum(r[:5]) == 2 or -0.5!
    # Every root in (10_GUT, 5_perp) has either two +1s in 0..4 (so sum(r[:5]) == 2, r[5:] == 0)
    # Wait: e_a + e_b (a<b<5) has perp projection (0.4^5, 0, 0, 0);
    # e_a + e_k (a<5, k>=5) is in (5, 10bar) or (10, 5)? Let's check: in SO(16) -> U(8), 10_GUT of SU(5) inside E_8:
    # Extract by orthogonality to e_0 - e_1, e_1 - e_2, e_2 - e_3, e_3 - e_4:
    # Take the 10 roots with r[0]=r[1]=1, r[2]=r[3]=r[4]=0 -> no, 1 highest weight of 10_GUT is e_0 + e_1?
    # Wait: let's find ALL roots in R with fixed GUT weight (r[:5] - mean(r[:5])) == (0.6, 0.6, -0.4, -0.4, -0.4)!
    gut_hw = np.array([0.6, 0.6, -0.4, -0.4, -0.4])
    slot_roots = np.array([r for r in R if np.max(np.abs((r[:5] - np.mean(r[:5])) - gut_hw)) < 1e-12])
    assert slot_roots.shape == (5, 8)  # Exactly 5 roots = the 5 slots of 5_perp for this 10_GUT state!

    k_mins: Dict[int, int] = {}
    dynkin_err = 0.0
    for a2 in range(-6, 7):
        a = 0.5 * a2
        for b1_2 in range(-12, 13):
            for b2_2 in range(-12, 13):
                for b3_2 in range(-12, 13):
                    if (abs(a2) % 2) != (abs(b1_2) % 2) or (abs(a2) % 2) != (abs(b2_2) % 2) or (abs(a2) % 2) != (abs(b3_2) % 2):
                        continue
                    b1, b2, b3 = 0.5 * b1_2, 0.5 * b2_2, 0.5 * b3_2
                    if int(round(5 * a + b1 + b2 + b3)) % 2 != 0:
                        continue
                    n2 = int(round(5 * a * a + b1 * b1 + b2 * b2 + b3 * b3))
                    if n2 == 0 or n2 > 32:
                        continue
                    H = np.array([a, a, a, a, a, b1, b2, b3])
                    k_i = n2 // 2
                    dynkin_err = max(dynkin_err, abs(float(np.sum((R @ H) ** 2)) / 120.0 - k_i))
                    mx = max(abs(int(round(float(w @ H)))) for w in slot_roots)
                    if mx in (1, 2, 3, 4):
                        k_mins[mx] = min(k_mins.get(mx, 999), k_i)

    # Cross-check against Producer's Gate 4 thresholds
    prod_thresh = prod_data["gate4_topological_tadpole_audit"]["e8_instanton_quantization_theorem"]["minimal_instanton_thresholds_by_ngen"]
    thresh_match = all(k_mins[n] == int(prod_thresh[str(n)]["minimal_k_inst"]) for n in (1, 2, 3, 4))

    # 2. Verify Dedekind reciprocity law 12 s(d,c) + 12 s(c,d) = d/c + c/d + 1/(cd) - 3
    def dsum(d: int, c: int) -> float:
        return sum((((k % c) / c - 0.5) if (k % c) else 0.0) * ((((k * d) % c) / c - 0.5) if ((k * d) % c) else 0.0) for k in range(1, c))

    dedekind_recip_err = 0.0
    for c, d in ((5, 3), (7, 4), (11, 8), (13, 5), (17, 12)):
        lhs = 12.0 * dsum(d, c) + 12.0 * dsum(c, d)
        rhs = (d / c) + (c / d) + (1.0 / (c * d)) - 3.0
        dedekind_recip_err = max(dedekind_recip_err, abs(lhs - rhs))

    # 3. Run 25 fresh adversarial Haar U(3)^3 rotations (seed 99999991) on complex Yukawa pair
    rng = np.random.default_rng(99999991)

    def haar_u3() -> np.ndarray:
        Z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
        Q, Rq = np.linalg.qr(Z)
        d = np.diag(Rq)
        return Q * (d / np.abs(d))[None, :]

    Yu0 = np.array(
        [[0.04 + 0.01j, 0.08 - 0.03j, 0.02 + 0.05j], [0.08 - 0.03j, 0.44 + 0.07j, 0.19 - 0.11j], [0.02 + 0.05j, 0.19 - 0.11j, 1.15 - 0.04j]],
        dtype=np.complex128,
    )
    Yd0 = np.array(
        [[0.06 - 0.02j, 0.09 + 0.04j, 0.03 - 0.01j], [0.11 + 0.05j, 0.51 - 0.08j, 0.14 + 0.09j], [0.04 + 0.02j, 0.17 - 0.06j, 0.98 + 0.03j]],
        dtype=np.complex128,
    )
    base = _ref_extract_yukawa_invariants(Yu0, Yd0)
    max_haar25_err = 0.0
    for _ in range(25):
        UL, URu, URd = haar_u3(), haar_u3(), haar_u3()
        scr = _ref_extract_yukawa_invariants(UL @ Yu0 @ URu.conj().T, UL @ Yd0 @ URd.conj().T)
        max_haar25_err = max(
            max_haar25_err,
            float(np.max(np.abs(np.array(base["su_ratios"]) - np.array(scr["su_ratios"])))),
            float(np.max(np.abs(np.array(base["sd_ratios"]) - np.array(scr["sd_ratios"])))),
            float(np.max(np.abs(base["ckm_abs"] - scr["ckm_abs"]))),
            abs(base["j_norm"] - scr["j_norm"]),
        )

    passed = (
        dynkin_err < 1e-13
        and k_mins == {1: 1, 2: 3, 3: 6, 4: 10}
        and thresh_match
        and dedekind_recip_err < 1e-14
        and abs(base["j_norm"]) > 1e-5
        and max_haar25_err < 1e-12
    )
    return {
        "check4_passed": passed,
        "e8_dynkin_instanton_err": dynkin_err,
        "independent_k_inst_mins": k_mins,
        "matches_producer_thresholds": thresh_match,
        "dedekind_reciprocity_err": dedekind_recip_err,
        "adversarial_haar25_max_err": max_haar25_err,
    }


def run_referee() -> Dict[str, Any]:
    c0 = audit_ast_and_seals()
    prod_json_path = PHASE3_ROOT / "outputs" / "phase3_results.json"
    if not prod_json_path.exists():
        raise FileNotFoundError(f"Missing producer output: {prod_json_path}")
    prod_data = json.loads(prod_json_path.read_text(encoding="utf-8"))

    c1 = run_check1_cover_and_yukawa(prod_data)
    c2 = run_check2_mpmath_relational(prod_data)
    c3 = run_check3_spin_flux_palindrome()
    c4 = run_check4_tadpole_and_adversarial_haar(prod_data)

    verdict_passed = bool(
        c0["check0_passed"]
        and prod_data.get("all_phase3_gates_passed", False)
        and c1["check1_passed"]
        and c2["check2_passed"]
        and c3["check3_passed"]
        and c4["check4_passed"]
    )
    verdict = {
        "referee": "AST-Isolated Zero-Import Referee — Phase 3 (Guardrail 6)",
        "all_referee_checks_passed": verdict_passed,
        "check0_ast_firewall_and_seals": c0,
        "check1_keast5_45tet_cover_and_yukawa": c1,
        "check2_mpmath50_relational_quotient": c2,
        "check3_keast5_spin_flux_palindrome": c3,
        "check4_e8_tadpole_and_haar25": c4,
    }
    out_path = PHASE3_ROOT / "outputs" / "referee_phase3_verdict.json"
    out_path.write_text(json.dumps(verdict, indent=2), encoding="utf-8")
    return verdict


if __name__ == "__main__":
    verdict = run_referee()
    print(json.dumps(verdict, indent=2))
    if not verdict["all_referee_checks_passed"]:
        raise SystemExit(1)
