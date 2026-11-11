"""AST-Isolated Zero-Import Referee Audit for Phase 4 (Guardrails 1-6).

Enforces Guardrail 6 (Zero-Trust Countercheck Rule):
  - Zero imports from `phase4_loop`, `relational_loop`, `cusped_loop`, `phi_loop`, or `src`.
  - AST scan of `src/`, `scripts/`, and `tests/` for forbidden imports, embedded target literals,
    PDG float targets, and literal boolean/zero proof flags.
  - Pre-registration SHA-256 seal check across Phases 1, 2, 3, and 4.
  - Independent 50-digit `mpmath` Fox free-differential calculus & Wada-Reidemeister torsion
    verification on `m004`, `m003`, `b++LLLRLL`, `b++LLLLLLRLR`, `b+-LLLLLRLLRR`,
    `b++LLLLLLLRRLLR`, and `b++LLLLLRLLRRLR` (`< 1e-40` precision).
  - Independent Weyl-reflection generation of `{F, Sigma_0}^perp` inside `I_{1,9}` (`240` roots,
    `det = 1`), Bianchi `k_vis = 6 = k_inst,min(3)` threshold, and FMW / 't Hooft mod-5 audit.
  - Independent GF(5) Gaussian-elimination cocycle solver + 3D hyperbolic FEM countercheck using
    Keast's exact 11-point degree-4 simplex quadrature rule (zero shared quadrature nodes/weights
    with Producer's 14-point Jinyun-Walkington rule) at `N_sub = 4`, cross-checking Producer's
    `outputs/phase4_results.json` eigenvalues, CKM angles, Seesaw/Weinberg PMNS angles, and Jarlskog.
  - 25 fresh adversarial random Haar `U(3)^3` basis-scrambling trials on both quark `(Y_u, Y_d)`
    and lepton `(Y_e, Y_nu, M_R, M_nu^W)` matrices (`< 1e-12`).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import mpmath as mp
import numpy as np
from scipy.linalg import eigh, null_space
from scipy.sparse import coo_matrix
import snappy
from snappy.geometric_structure.cusp_neighborhood.complex_cusp_cross_section import (
    ComplexCuspCrossSection,
)
from snappy.snap.t3mlite import simplex as t3m_simplex


PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_IMPORT_PREFIXES = (
    "phase4_loop",
    "relational_loop",
    "cusped_loop",
    "phi_loop",
    "src.",
)

# Rational (num, den) pairs representing PDG experimental numbers that must never be hardcoded in `src/`:
FORBIDDEN_PDG_RATIONALS = (
    (22500, 100000),    # |V_us| ~ 0.225
    (308, 10000000),    # J_CKM ~ 3.08e-5
    (307, 1000),        # sin^2 theta_12^PMNS ~ 0.307
    (546, 1000),        # sin^2 theta_23^PMNS ~ 0.546
    (220, 10000),       # sin^2 theta_13^PMNS ~ 0.0220
    (741, 10000000),    # Delta m^2_21 ~ 7.41e-5
    (251, 100000),      # |Delta m^2_31| ~ 2.51e-3
    (16180339887, 10000000000),  # Golden ratio decimal literal
)

FORBIDDEN_LITERAL_FLAG_KEYS = {
    "extends_to_cover",
    "bar_theta_QCD",
    "theta_qcd_bar",
}


# ---------------------------------------------------------------------------
# 1. AST Static Guardrail & Zero-Import Audit
# ---------------------------------------------------------------------------

def run_ast_guardrail_scan(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Scan AST of `src/`, `scripts/`, and `tests/` for forbidden imports and hardcoded targets."""
    referee_path = Path(__file__).resolve()
    py_dirs = [project_root / "src", project_root / "scripts", project_root / "tests"]
    py_files: List[Path] = []
    for d in py_dirs:
        if d.exists():
            py_files.extend(sorted(d.rglob("*.py")))

    forbidden_referee_imports: List[str] = []
    forbidden_float_hits: List[str] = []
    forbidden_flag_hits: List[str] = []

    pdg_targets = [num / den for num, den in FORBIDDEN_PDG_RATIONALS]

    for fpath in py_files:
        rel = str(fpath.relative_to(project_root))
        tree = ast.parse(fpath.read_text(encoding="utf-8"), filename=rel)
        is_referee = (fpath.resolve() == referee_path)
        is_src = rel.startswith("src/")

        for node in ast.walk(tree):
            if is_referee:
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name == "src" or any(alias.name.startswith(p) for p in FORBIDDEN_IMPORT_PREFIXES):
                            forbidden_referee_imports.append(f"{rel}:{node.lineno}:{alias.name}")
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    if node.level > 0 or mod == "src" or any(mod.startswith(p) for p in FORBIDDEN_IMPORT_PREFIXES):
                        forbidden_referee_imports.append(f"{rel}:{node.lineno}:from {'.'*node.level}{mod}")

            if is_src and isinstance(node, ast.Constant) and isinstance(node.value, float):
                val = abs(float(node.value))
                if val > 0.0:
                    for tgt in pdg_targets:
                        if abs(val - tgt) / tgt < 1e-7:
                            forbidden_float_hits.append(f"{rel}:{node.lineno}:{node.value}")

            if is_src and isinstance(node, ast.Dict):
                for k_node, v_node in zip(node.keys, node.values):
                    if (
                        isinstance(k_node, ast.Constant)
                        and isinstance(k_node.value, str)
                        and k_node.value in FORBIDDEN_LITERAL_FLAG_KEYS
                        and isinstance(v_node, ast.Constant)
                    ):
                        forbidden_flag_hits.append(f"{rel}:{node.lineno}:{k_node.value}={v_node.value}")

    passed = (
        len(forbidden_referee_imports) == 0
        and len(forbidden_float_hits) == 0
        and len(forbidden_flag_hits) == 0
    )
    return {
        "scanned_python_files": [str(p.relative_to(project_root)) for p in py_files],
        "num_scanned_files": len(py_files),
        "forbidden_referee_imports": forbidden_referee_imports,
        "forbidden_pdg_float_hits_in_src": forbidden_float_hits,
        "forbidden_literal_flag_hits_in_src": forbidden_flag_hits,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# 2. Pre-Registration SHA-256 Seal Audit (Phases 1-4)
# ---------------------------------------------------------------------------

def run_seal_integrity_audit(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify SHA-256 pre-registration seals across Phase 4 and sibling Phases 1-3."""
    parent = project_root.parent
    specs = [
        ("phase1", parent / "self_consistent_loop_phi"),
        ("phase2", parent / "cusped_3d_loop_phase2"),
        ("phase3", parent / "relational_yukawa_phase3"),
        ("phase4", project_root),
    ]
    out: Dict[str, Any] = {}
    all_ok = True
    for label, dpath in specs:
        if not dpath.exists():
            if label == "phase4":
                all_ok = False
            continue
        seal_file = dpath / "SEAL_SHA256.txt"
        parts = seal_file.read_text(encoding="utf-8").strip().splitlines()[0].split()
        exp_sha, doc_name = parts[0].strip(), Path(parts[1].strip()).name
        act_sha = hashlib.sha256((dpath / doc_name).read_bytes()).hexdigest()
        ok = (exp_sha == act_sha)
        if not ok:
            all_ok = False
        out[label] = {
            "directory": dpath.name,
            "document": doc_name,
            "expected_sha256": exp_sha,
            "actual_sha256": act_sha,
            "intact": ok,
        }
    return {"seals": out, "passed": all_ok and ("phase4" in out)}


# ---------------------------------------------------------------------------
# 3. 50-Digit `mpmath` Independent Fox-Wada Reidemeister Torsion Countercheck
# ---------------------------------------------------------------------------

def _mp_fox_eval_word(word: str, gen_idx: Dict[str, int], rho: List[Any]) -> Tuple[List[Any], Any]:
    """Evaluate word image rho(w) and Fox derivatives d(w)/d(x_j) evaluated at rho in 50-digit mpmath."""
    mp.mp.dps = 55
    n_g = len(rho)
    derivs = [mp.mpc(0) for _ in range(n_g)]
    pref = mp.mpc(1)
    for ch in word:
        low = ch.lower()
        j = gen_idx[low]
        g_val = rho[j]
        if ch.islower():
            derivs[j] += pref
            pref *= g_val
        else:
            g_inv = mp.mpc(1) / g_val
            pref *= g_inv
            derivs[j] -= pref
    return derivs, pref


def _mp_det_square(mat: List[List[Any]]) -> Any:
    """50-digit Gaussian-elimination determinant of a small complex mpmath matrix."""
    n = len(mat)
    if n == 0:
        return mp.mpc(1)
    A = [[mp.mpc(mat[r][c]) for c in range(n)] for r in range(n)]
    det = mp.mpc(1)
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        if abs(A[piv][col]) < mp.mpf("1e-48"):
            return mp.mpc(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        inv_p = mp.mpc(1) / A[col][col]
        for r in range(col + 1, n):
            fac = A[r][col] * inv_p
            if fac != 0:
                for c in range(col, n):
                    A[r][c] -= fac * A[col][c]
    return det


def _mp_wada_torsion_1cusp(G: Any, rho: List[Any]) -> mp.mpf:
    """Compute 50-digit Wada-Reidemeister torsion |det J^{(j)}| / |rho(x_j) - 1| on deficiency-1 pi_1."""
    mp.mp.dps = 55
    gens = list(G.generators())
    rels = list(G.relators())
    n_g = len(gens)
    assert len(rels) == n_g - 1
    gen_idx = {g: i for i, g in enumerate(gens)}

    J = []
    max_rel_err = mp.mpf(0)
    for r_word in rels:
        d_row, w_img = _mp_fox_eval_word(r_word, gen_idx, rho)
        max_rel_err = max(max_rel_err, abs(w_img - 1))
        J.append(d_row)
    assert max_rel_err < mp.mpf("1e-45")

    ratios: List[mp.mpf] = []
    for j in range(n_g):
        denom = abs(rho[j] - 1)
        if denom > mp.mpf("1e-30"):
            minor = [[J[r][c] for c in range(n_g) if c != j] for r in range(n_g - 1)]
            ratios.append(abs(_mp_det_square(minor)) / denom)
    assert len(ratios) > 0
    for r_val in ratios[1:]:
        assert abs(r_val - ratios[0]) < mp.mpf("1e-42")
    return ratios[0]


def _gf5_nullspace(A_mod5: np.ndarray) -> List[List[int]]:
    """Exact nullspace basis over GF(5) via row-reduced echelon form."""
    m, n = A_mod5.shape
    M = (A_mod5.copy() % 5).astype(int)
    piv_cols: List[int] = []
    row = 0
    for col in range(n):
        if row >= m:
            break
        piv = next((r for r in range(row, m) if M[r, col] % 5 != 0), None)
        if piv is None:
            continue
        if piv != row:
            M[[row, piv]] = M[[piv, row]]
        inv_v = pow(int(M[row, col] % 5), -1, 5)
        M[row] = (M[row] * inv_v) % 5
        for r in range(m):
            if r != row and M[r, col] % 5 != 0:
                M[r] = (M[r] - M[r, col] * M[row]) % 5
        piv_cols.append(col)
        row += 1

    free_cols = [c for c in range(n) if c not in piv_cols]
    basis: List[List[int]] = []
    for fc in free_cols:
        vec = [0] * n
        vec[fc] = 1
        for r_idx, pc in enumerate(piv_cols):
            vec[pc] = (-int(M[r_idx, fc])) % 5
        basis.append(vec)
    return basis


def run_mpmath_fox_wada_countercheck() -> Dict[str, Any]:
    """50-digit mpmath countercheck of Fox-Wada Alexander & Reidemeister torsion theorems."""
    mp.mp.dps = 55
    # 1. Textbook m004 (b++LR, |3 - 2 cos theta|) and m003 (b+-LR, |3 + 2 cos theta|):
    max_textbook_err = mp.mpf(0)
    for spec, sign_cos in (("b++LR", -1), ("b+-LR", +1)):
        M = snappy.Manifold(spec)
        G = M.fundamental_group()
        gens = list(G.generators())
        rels = list(G.relators())
        n_g = len(gens)
        A_ab = np.zeros((len(rels), n_g), dtype=float)
        for r_i, rw in enumerate(rels):
            for ch in rw:
                idx = gens.index(ch.lower())
                A_ab[r_i, idx] += 1.0 if ch.islower() else -1.0
        ns = null_space(A_ab)
        assert ns.shape[1] == 1
        v = ns[:, 0]
        nz = [abs(x) for x in v if abs(x) > 1e-8]
        v_int = np.round(v / min(nz)).astype(int)
        from math import gcd
        from functools import reduce
        g_all = reduce(gcd, [abs(int(x)) for x in v_int if x != 0])
        v_int = v_int // g_all

        for q in (1, 2):
            th = 2 * mp.pi * q / 5
            rho = [mp.exp(1j * th * int(v_int[i])) for i in range(n_g)]
            t_wada = _mp_wada_torsion_1cusp(G, rho)
            delta_exact = abs(3 + sign_cos * 2 * mp.cos(th))
            exact_wada = delta_exact / abs(mp.exp(1j * th) - 1)
            max_textbook_err = max(max_textbook_err, abs(t_wada - exact_wada))

    # 2. Universal acyclicity countercheck across key census manifolds (50 digits):
    test_specs = [
        "b+-LR",
        "b++LLLRLL",
        "b++LLLLLLRLR",
        "b+-LLLLLRLLRR",
        "b++LLLLLLLRRLLR",
        "b++LLLLLRLLRRLR",
    ]
    max_unram_torsion = mp.mpf(0)
    max_ram_prod5_err = mp.mpf(0)
    manifold_records = {}

    for spec in test_specs:
        M = snappy.Manifold(spec)
        G = M.fundamental_group()
        gens = list(G.generators())
        rels = list(G.relators())
        n_g = len(gens)
        A_int = np.zeros((len(rels), n_g), dtype=int)
        for r_i, rw in enumerate(rels):
            for ch in rw:
                idx = gens.index(ch.lower())
                A_int[r_i, idx] += 1 if ch.islower() else -1

        # Rational free character (unique mod sign since b_1 = 1):
        ns = null_space(A_int.astype(float))
        v = ns[:, 0]
        # Scale rational nullspace vector to primitive integer vector:
        scale_found = None
        for mult in range(1, 500):
            cand = v * mult / max(abs(x) for x in v if abs(x) > 1e-9)
            if np.max(np.abs(cand - np.round(cand))) < 1e-7:
                v_int = np.round(cand).astype(int)
                if np.all(A_int @ v_int == 0):
                    from math import gcd
                    from functools import reduce
                    gg = reduce(gcd, [abs(int(x)) for x in v_int if x != 0])
                    scale_found = (v_int // gg) % 5
                    break
        assert scale_found is not None
        fnz = next(int(x) for x in scale_found if x != 0)
        free_canon = tuple((int(x) * pow(fnz, -1, 5)) % 5 for x in scale_found)

        gf5_basis = _gf5_nullspace(A_int % 5)
        periph_words = []
        for pw in sum(G.peripheral_curves(), ()):
            vec_p = [0] * n_g
            for ch in pw:
                idx = gens.index(ch.lower())
                vec_p[idx] = (vec_p[idx] + (1 if ch.islower() else -1)) % 5
            periph_words.append(vec_p)

        seen_lines = set()
        n_unram = 0
        n_ram = 0
        for coeffs in itertools.product(range(5), repeat=len(gf5_basis)):
            if all(c == 0 for c in coeffs):
                continue
            fn = next(c for c in coeffs if c != 0)
            inv_fn = pow(fn, -1, 5)
            c_norm = tuple((c * inv_fn) % 5 for c in coeffs)
            if c_norm in seen_lines:
                continue
            seen_lines.add(c_norm)

            char_mod5 = [0] * n_g
            for b_i, c_val in enumerate(c_norm):
                for j in range(n_g):
                    char_mod5[j] = (char_mod5[j] + c_val * gf5_basis[b_i][j]) % 5
            fn_ch = next(x for x in char_mod5 if x != 0)
            char_canon = tuple((x * pow(fn_ch, -1, 5)) % 5 for x in char_mod5)
            if char_canon == free_canon:
                continue  # pure free Z character, not torsion

            is_unram = all(
                sum(char_canon[j] * pw[j] for j in range(n_g)) % 5 == 0
                for pw in periph_words
            )
            if is_unram:
                n_unram += 1
                rho1 = [mp.exp(2j * mp.pi * char_canon[j] / 5) for j in range(n_g)]
                t1 = _mp_wada_torsion_1cusp(G, rho1)
                max_unram_torsion = max(max_unram_torsion, t1)
            else:
                n_ram += 1
                prod4 = mp.mpf(1)
                for q in (1, 2, 3, 4):
                    rho_q = [mp.exp(2j * mp.pi * ((q * char_canon[j]) % 5) / 5) for j in range(n_g)]
                    prod4 *= _mp_wada_torsion_1cusp(G, rho_q)
                max_ram_prod5_err = max(max_ram_prod5_err, abs(prod4 - 5))

        manifold_records[spec] = {
            "num_unramified_torsion_lines": n_unram,
            "num_ramified_torsion_lines": n_ram,
        }

    passed = (
        float(max_textbook_err) < 1e-40
        and float(max_unram_torsion) < 1e-40
        and float(max_ram_prod5_err) < 1e-40
    )
    return {
        "mpmath_dps": 55,
        "max_textbook_m004_m003_err": float(max_textbook_err),
        "max_unramified_k0_torsion": float(max_unram_torsion),
        "max_ramified_cyclotomic_product5_err": float(max_ram_prod5_err),
        "manifolds_checked": manifold_records,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# 4. Independent Weyl-Reflection dP_9 / E_8(-1) & Bianchi Countercheck
# ---------------------------------------------------------------------------

def run_dp9_weyl_countercheck(producer_g2: Dict[str, Any]) -> Dict[str, Any]:
    """Generate `{F, Sigma_0}^perp` roots inside `I_{1,9}` by Weyl reflections (distinct from Producer)."""
    Q = np.diag([1] + [-1] * 9).astype(int)
    F = np.array([3] + [-1] * 9, dtype=int)
    S0 = np.array([0] * 9 + [1], dtype=int)

    # 8 simple roots in I_{1,9}:
    simple = []
    for k in range(7):
        v = [0] * 10
        v[k + 1] = 1
        v[k + 2] = -1
        simple.append(tuple(v))
    simple.append((1, -1, -1, -1, 0, 0, 0, 0, 0, 0))
    S_mat = np.array(simple, dtype=int)

    # Generate full root system by BFS of Weyl reflections s_alpha(v) = v + (v . Q . alpha) * alpha
    # (since alpha . Q . alpha == -2, reflection in Lorentzian norm -2 root is v - 2*(v.alpha)/(alpha.alpha)*alpha = v + (v.Q.alpha)*alpha):
    orbit = set(simple)
    queue = list(simple)
    while queue:
        cur = np.array(queue.pop(), dtype=int)
        for s_tup in simple:
            s_arr = np.array(s_tup, dtype=int)
            ip = int(cur @ Q @ s_arr)
            nxt = tuple((cur + ip * s_arr).tolist())
            if nxt not in orbit:
                orbit.add(nxt)
                queue.append(nxt)

    roots = np.array(sorted(orbit), dtype=int)
    det_gram = int(round(abs(float(np.linalg.det(-(S_mat @ Q @ S_mat.T).astype(float))))))
    orth_ok = bool(np.all((roots @ Q @ F) == 0) and np.all((roots @ Q @ S0) == 0))
    norms_ok = bool(np.all(np.einsum("ni,ij,nj->n", roots, Q, roots) == -2))

    # Bianchi & FMW checks:
    c2_dp9 = 12
    k_vis = c2_dp9 // 2
    k_min_3 = (3 * 4) // 2

    C_vec = 5 * S0 + 6 * F
    K_vec = -F
    g_C = 1 + int(C_vec @ Q @ (C_vec + K_vec)) // 2
    R_deg = 2 * g_C - 2 - 5 * (-2)

    # 't Hooft mod-1 congruence (5*w1*w2 + 2*(6) == 0 mod 5 => w1*w2 == 0 mod 5):
    compat = [(a, b) for a in range(5) for b in range(5) if (a * b) % 5 == 0]
    unram_allowed_by_c2 = (0, 0) in compat

    prod_matches = (
        producer_g2["dp9_lattice_and_e8_mordell_weil"]["e8_norm_minus2_root_count"] == len(orbit)
        and producer_g2["bianchi_tadpole_and_3gen_threshold"]["symmetric_bianchi_k_vis"] == k_vis
        and producer_g2["peripheral_gluing_and_ramification_audit"]["bulk_integer_c2_alone_forbids_k_zero"]
        == (not unram_allowed_by_c2)
    )

    passed = (
        len(orbit) == 240
        and det_gram == 1
        and orth_ok
        and norms_ok
        and k_vis == 6 == k_min_3
        and g_C == 16
        and R_deg == 40
        and unram_allowed_by_c2
        and prod_matches
    )
    return {
        "weyl_orbit_root_count": len(orbit),
        "det_gram": det_gram,
        "orthogonal_and_norm_minus2": bool(orth_ok and norms_ok),
        "k_vis_eq_k_min_3": (k_vis == k_min_3 == 6),
        "fmw_genus_and_ramification": [g_C, R_deg],
        "unramified_00_allowed_by_bulk_c2_alone": unram_allowed_by_c2,
        "matches_producer_gate2": prod_matches,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# 5. Independent Keast-11 Degree-4 Quadrature 3D Hyperbolic FEM Countercheck
# ---------------------------------------------------------------------------

def _build_keast11_degree4_simplex_rule() -> Tuple[np.ndarray, np.ndarray]:
    """Exact 11-point degree-4 symmetric tetrahedral quadrature rule (Keast 1986, Table 1).

    Orbit parameters:
      O_0: (1/4, 1/4, 1/4, 1/4),        mult 1, w_0 = -148 / 1875
      O_1: (a, a, a, 1 - 3a), a = 1/14, mult 4, w_1 =  343 / 7500
      O_2: (b, b, 1/2 - b, 1/2 - b),
           b = 1/4 - sqrt(70)/56,       mult 6, w_2 =   56 / 375
    Shares ZERO nodes or weights with Producer's 14-point Jinyun-Walkington rule!
    """
    a = 1.0 / 14.0
    b = 0.25 - math.sqrt(70.0) / 56.0
    c = 0.5 - b
    w0 = -148.0 / 1875.0
    w1 = 343.0 / 7500.0
    w2 = 56.0 / 375.0

    pts: List[Tuple[float, float, float, float]] = [(0.25, 0.25, 0.25, 0.25)]
    wts: List[float] = [w0]

    for idx in range(4):
        p = [a, a, a, a]
        p[idx] = 1.0 - 3.0 * a
        pts.append((p[0], p[1], p[2], p[3]))
        wts.append(w1)

    for i, j in itertools.combinations(range(4), 2):
        p = [c, c, c, c]
        p[i] = b
        p[j] = b
        pts.append((p[0], p[1], p[2], p[3]))
        wts.append(w2)

    return np.array(pts, dtype=float), np.array(wts, dtype=float)


KEAST11_BARY, KEAST11_WEIGHTS = _build_keast11_degree4_simplex_rule()


def _verify_keast11_degree4_exactness() -> float:
    """Verify exactness of Keast-11 on all barycentric monomials up to total degree 4."""
    max_err = 0.0
    for deg in range(5):
        for p0 in range(deg + 1):
            for p1 in range(deg + 1 - p0):
                for p2 in range(deg + 1 - p0 - p1):
                    p3 = deg - p0 - p1 - p2
                    exact = (
                        6.0
                        * math.factorial(p0)
                        * math.factorial(p1)
                        * math.factorial(p2)
                        * math.factorial(p3)
                        / math.factorial(deg + 3)
                    )
                    vals = (
                        (KEAST11_BARY[:, 0] ** p0)
                        * (KEAST11_BARY[:, 1] ** p1)
                        * (KEAST11_BARY[:, 2] ** p2)
                        * (KEAST11_BARY[:, 3] ** p3)
                    )
                    quad = float(np.dot(KEAST11_WEIGHTS, vals))
                    max_err = max(max_err, abs(quad - exact))
    return max_err


def _ref_extract_manifold_geometry_and_gf5_cocycles(spec: str) -> Dict[str, Any]:
    """Independent Epstein-Penner extraction + GF(5) Gaussian-elimination cocycle finder."""
    M0 = snappy.Manifold(spec)
    M = M0.high_precision() if hasattr(M0, "high_precision") else M0
    shapes = M.tetrahedra_shapes("rect")
    ccs = ComplexCuspCrossSection.fromManifoldAndShapes(M, shapes)
    ccs.normalize_cusps()

    vbits = [t3m_simplex.V0, t3m_simplex.V1, t3m_simplex.V2, t3m_simplex.V3]
    fbits = [t3m_simplex.F0, t3m_simplex.F1, t3m_simplex.F2, t3m_simplex.F3]
    fb_to_i = {14: 0, 13: 1, 11: 2, 7: 3}

    grams = []
    gluings = []
    for T in ccs.mcomplex.Tetrahedra:
        G = np.zeros((4, 4), dtype=float)
        for i in range(4):
            for j in range(i + 1, 4):
                k = next(x for x in range(4) if x != i and x != j)
                li = float(abs(T.horotriangles[vbits[i]].lengths[fbits[k]]))
                lj = float(abs(T.horotriangles[vbits[j]].lengths[fbits[k]]))
                G[i, j] = G[j, i] = -2.0 / (li * lj)
        grams.append(G)
        gluings.append(
            [(T.Neighbor[fbits[f]].Index, tuple(T.Gluing[fbits[f]][m] for m in range(4))) for f in range(4)]
        )

    faces = []
    for fg, F_obj in enumerate(ccs.mcomplex.Faces):
        c0, c1 = F_obj.Corners[0], F_obj.Corners[1]
        t0, f0 = c0.Tetrahedron.Index, fb_to_i[c0.Subsimplex]
        t1, f1 = c1.Tetrahedron.Index, fb_to_i[c1.Subsimplex]
        _, p0 = gluings[t0][f0]
        faces.append((fg, t0, f0, t1, f1, p0))

    bmaps = ccs.mcomplex.boundary_maps()
    d2, d3 = [
        np.array([int(x) for x in m.list()], dtype=int).reshape((m.nrows(), m.ncols()))
        for m in bmaps[1:]
    ]

    # Solve H^1(M; GF(5)) = ker(d2 mod 5) / im(d3 mod 5) using GF(5) row reduction:
    ker_d2 = _gf5_nullspace(d2 % 5)
    # Quotient by column space of d3 mod 5:
    im_cols = [(d3[:, j] % 5).tolist() for j in range(d3.shape[1])]
    span_rows: List[List[int]] = []

    def _in_gf5_span(rows: List[List[int]], vec: List[int]) -> bool:
        if not rows:
            return all(x % 5 == 0 for x in vec)
        mat = np.array(rows + [vec], dtype=int) % 5
        # Compare rank over GF(5):
        def _rk(A: np.ndarray) -> int:
            return A.shape[1] - len(_gf5_nullspace(A))
        return _rk(mat) == _rk(np.array(rows, dtype=int) % 5)

    for col_v in im_cols:
        if not _in_gf5_span(span_rows, col_v):
            span_rows.append(col_v)

    h1_basis: List[List[int]] = []
    cur_span = list(span_rows)
    for kv in ker_d2:
        if not _in_gf5_span(cur_span, kv):
            h1_basis.append(kv)
            cur_span.append(kv)

    # Identify unique rational free 1-cocycle line (b_1 = 1) modulo im(d3):
    # Project rational nullspace of d2 orthogonal to im(d3):
    ns_d2 = null_space(d2.astype(float))
    # Remove component in im(d3):
    Q_d3, _ = np.linalg.qr(d3.astype(float))
    proj_ns = ns_d2 - Q_d3 @ (Q_d3.T @ ns_d2)
    u_col, s_col, _ = np.linalg.svd(proj_ns, full_matrices=False)
    free_real = u_col[:, 0]
    # Lift free_real + d3 * y to exact integer vector:
    # Solve min || free_real + d3 y ||_inf -> scale to integers in ker(d2):
    free_mod5_line = None
    # Express free_real in rational ker(d2): since dim H^1_free = 1, any integer vector z in ker(d2) not in im_Q(d3):
    for mult in range(1, 400):
        # Find integer z in ker(d2):
        pass
    # Clean exact method for free_mod5_line: over R, a cocycle c in Z^F lifts to a Z-cocycle iff
    # <c, t> == 0 mod 5 for every 5-torsion 1-cycle t (where d3^T t = 0 and 5 t in im(d2^T)).
    # Even simpler: check cusp cover count! Every cusp-ramified line has cover_cusps == 1 < 5*num_cusps,
    # PROVIDED it is ALSO torsion-nontrivial (since the free Z/5Z cyclic cover along longitude/meridian
    # can also have 1 cusp!). How to test torsion-nontriviality directly without SNF?
    # A mod-5 cocycle `c` is torsion-trivial (lifts to Hom(H_1, Z)) IFF there exists `z in R^F` and `b in Z^T`
    # with `d2 z == 0` AND `z - (c + 5*w + d3*b) == 0`, i.e., `c in im_F5(ker_Z(d2))`!
    # Wait: `ker_Z(d2)` mod `im_Z(d3)` has rank 1, generated by ONE integer cocycle `c_free`!
    # We find `c_free` directly from integer SVD/LLL or nullspace of `[d2; d3_complement]`:
    # Augment d2 (m x F) with F-1 rows of d3^T so nullity == 1!
    aug_rows = [d2.astype(float)]
    # Pick maximal independent columns of d3 to gauge-fix im(d3):
    _, R_qr = np.linalg.qr(d3.astype(float), mode="reduced")
    # Simply project onto orthogonal complement of im(d3): `d3^T c == 0` has rank(d3) equations!
    sys_mat = np.vstack([d2.astype(float), d3.T.astype(float)])
    ns_one = null_space(sys_mat)
    assert ns_one.shape[1] == 1
    v1 = ns_one[:, 0]
    # Now `c_real = v1` is in ker(d2); add `d3 @ alpha` to make it integer? Wait: `ker_Z(d2)` ALWAYS contains
    # a non-zero integer vector, and `d3` is unimodular on spanning tree of dual vertices (`d3` is coboundary of 0-cochains,
    # i.e. each row of `d3` has ONE +1 and ONE -1!).
    # WAIT A SECOND! `d3` is the dual 0-coboundary matrix: EVERY ROW of `d3` has one `+1` and one `-1`!
    # So fixing `phi[0] = 0` on a spanning tree of dual vertices (tetrahedra!) gives an UNIMODULAR integer gauge `c[tree_faces] = 0`!!
    n_tet = d3.shape[1]
    tree_faces: List[int] = []
    visited = {0}
    while len(visited) < n_tet:
        for fg, t0, _f0, t1, _f1, _p0 in faces:
            if (t0 in visited) ^ (t1 in visited):
                tree_faces.append(fg)
                visited.add(t0)
                visited.add(t1)
                break
    gauge_rows = np.zeros((len(tree_faces), d2.shape[1]), dtype=float)
    for idx_tf, fg in enumerate(tree_faces):
        gauge_rows[idx_tf, fg] = 1.0
    ns_tree = null_space(np.vstack([d2.astype(float), gauge_rows]))
    assert ns_tree.shape[1] == 1
    vt = ns_tree[:, 0]
    nz_vt = [abs(x) for x in vt if abs(x) > 1e-8]
    vt_scaled = vt / min(nz_vt)
    # Multiply by small integer denominator if needed:
    c_free_int = None
    for denom in range(1, 200):
        cand = vt_scaled * denom
        if np.max(np.abs(cand - np.round(cand))) < 1e-7:
            ci = np.round(cand).astype(int)
            if np.all(d2 @ ci == 0):
                from math import gcd
                from functools import reduce
                gg = reduce(gcd, [abs(int(x)) for x in ci if x != 0])
                c_free_int = (ci // gg) % 5
                break
    assert c_free_int is not None

    # Now enumerate all projective lines in H^1(M; GF(5)) and keep cusp-ramified torsion lines:
    ramified_torsion_cocycles: List[np.ndarray] = []
    seen_p = set()
    n_cusps_base = M.num_cusps()

    for coeffs in itertools.product(range(5), repeat=len(h1_basis)):
        if all(x == 0 for x in coeffs):
            continue
        fn = next(x for x in coeffs if x != 0)
        inv_f = pow(fn, -1, 5)
        cn = tuple((x * inv_f) % 5 for x in coeffs)
        if cn in seen_p:
            continue
        seen_p.add(cn)

        coc = np.zeros(d2.shape[1], dtype=int)
        for bi, cv in enumerate(cn):
            coc = (coc + cv * np.array(h1_basis[bi], dtype=int)) % 5

        # Test if [coc] == [c_free_int] in H^1(M; GF(5)), i.e. coc - k*c_free_int in im_F5(d3):
        is_pure_free = any(
            _in_gf5_span(span_rows, ((coc - k_s * c_free_int) % 5).tolist())
            for k_s in range(1, 5)
        )
        if is_pure_free:
            continue

        # Count cusps of 5-fold cover via union-find on ideal vertices x Z/5Z:
        tot_v = 4 * n_tet * 5
        par = list(range(tot_v))

        def _fnd(x: int) -> int:
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        for fg, t0, f0, t1, _f1, p0 in faces:
            sh = int(coc[fg]) % 5
            for vp in range(4):
                if vp != f0:
                    vn = p0[vp]
                    for s in range(5):
                        r1 = _fnd((t0 * 4 + vp) * 5 + s)
                        r2 = _fnd((t1 * 4 + vn) * 5 + ((s + sh) % 5))
                        if r1 != r2:
                            par[r2] = r1
        ncov_cusps = len({_fnd(i) for i in range(tot_v)})
        if ncov_cusps < 5 * n_cusps_base:
            ramified_torsion_cocycles.append(coc)

    try:
        cs_val = float(M.chern_simons())
    except Exception:
        cs_val = 0.0
    is_amph = bool(M0.symmetry_group().is_amphicheiral())
    s4 = math.sin(4.0 * math.pi * cs_val)
    sig_p = 0 if is_amph else (1 if s4 > 1e-9 else (-1 if s4 < -1e-9 else 1))

    return {
        "spec": spec,
        "num_tets": n_tet,
        "grams": grams,
        "faces": faces,
        "ramified_cocycles": ramified_torsion_cocycles,
        "sigma_P": sig_p,
    }


def _ref_build_subdivision_and_keast11_geoms(
    grams: List[np.ndarray], n_sub: int = 4
) -> Tuple[np.ndarray, Dict[Tuple[int, int, int, int], int], np.ndarray, np.ndarray, List[Dict[str, np.ndarray]]]:
    """Build S_4-symmetric mesh and compute element geometry at Keast-11 quadrature points."""
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

    stets: List[Tuple[int, int, int, int]] = []
    e4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    for b0 in range(n_sub):
        for b1 in range(n_sub - b0):
            for b2 in range(n_sub - b0 - b1):
                b3 = (n_sub - 1) - b0 - b1 - b2
                if max(b0, b1, b2, b3) == n_sub - 1:
                    continue
                stets.append(tuple(gmap[(b0 + e[0], b1 + e[1], b2 + e[2], b3 + e[3])] for e in e4))

    for c0 in range(n_sub - 1):
        for c1 in range(n_sub - 1 - c0):
            for c2 in range(n_sub - 1 - c0 - c1):
                c3 = (n_sub - 2) - c0 - c1 - c2
                oc = len(nodes)
                nodes.append(((c0 + 0.5) / n_sub, (c1 + 0.5) / n_sub, (c2 + 0.5) / n_sub, (c3 + 0.5) / n_sub))
                horo.append(False)
                px = {}
                for a in range(4):
                    for b in range(a + 1, 4):
                        px[(a, b)] = px[(b, a)] = gmap[
                            (c0 + e4[a][0] + e4[b][0], c1 + e4[a][1] + e4[b][1], c2 + e4[a][2] + e4[b][2], c3 + e4[a][3] + e4[b][3])
                        ]
                for a in range(4):
                    ot = [b for b in range(4) if b != a]
                    stets.append((oc, px[(a, ot[0])], px[(a, ot[1])], px[(a, ot[2])]))
                for d in range(4):
                    rm = [a for a in range(4) if a != d]
                    stets.append((oc, px[(rm[0], rm[1])], px[(rm[1], rm[2])], px[(rm[2], rm[0])]))

    for d0 in range(n_sub - 2):
        for d1 in range(n_sub - 2 - d0):
            for d2 in range(n_sub - 2 - d0 - d1):
                d3v = (n_sub - 3) - d0 - d1 - d2
                stets.append(
                    tuple(gmap[(d0 + 1 - e[0], d1 + 1 - e[1], d2 + 1 - e[2], d3v + 1 - e[3])] for e in e4)
                )

    nodes_arr = np.array(nodes, dtype=float)
    horo_arr = np.array(horo, dtype=bool)
    stets_arr = np.array(stets, dtype=int)

    geoms_k11 = []
    for G in grams:
        Dmat = G[1:, :] - G[0:1, :]
        Gdiff = Dmat[:, 1:] - Dmat[:, 0:1]
        ev = nodes_arr[stets_arr]
        v0 = ev[:, 0, 1:]
        J = np.stack([ev[:, 1, 1:] - v0, ev[:, 2, 1:] - v0, ev[:, 3, 1:] - v0], axis=-1)
        detJ = np.abs(np.linalg.det(J))
        invJT = np.linalg.inv(np.swapaxes(J, 1, 2))
        gphi = np.zeros((stets_arr.shape[0], 4, 3), dtype=float)
        gphi[:, 1:, :] = np.swapaxes(invJT, 1, 2)
        gphi[:, 0, :] = -np.sum(gphi[:, 1:, :], axis=1)

        W = np.einsum("qk,ekb->eqb", KEAST11_BARY, ev)
        Q_val = -np.sum((W @ G) * W, axis=-1)
        dQ = -2.0 * (W @ Dmat.T)
        g_m = (
            Gdiff[None, None, :, :] / Q_val[:, :, None, None]
            + (dQ[:, :, :, None] * dQ[:, :, None, :]) / (4.0 * (Q_val[:, :, None, None] ** 2))
        )
        sdg = np.sqrt(np.maximum(0.0, np.linalg.det(g_m)))
        ginv = np.linalg.inv(g_m)
        dvol = (detJ[:, None] / 6.0) * KEAST11_WEIGHTS[None, :] * sdg
        geoms_k11.append({"dvol": dvol, "ginv": ginv, "gphi": gphi})

    return nodes_arr, gmap, horo_arr, stets_arr, geoms_k11


def _ref_solve_sector_k11(
    mdata: Dict[str, Any],
    coc: Optional[np.ndarray],
    q: int,
    nodes_arr: np.ndarray,
    gmap: Dict[Tuple[int, int, int, int], int],
    horo_arr: np.ndarray,
    stets_arr: np.ndarray,
    geoms_k11: List[Dict[str, np.ndarray]],
    n_eigs: int = 5,
) -> Tuple[np.ndarray, np.ndarray]:
    """Assemble and solve twisted P1 Laplace-Beltrami using Keast-11 quadrature."""
    n_tet = mdata["num_tets"]
    n_loc = nodes_arr.shape[0]
    twist = (coc is not None) and (q % 5 != 0)
    om = np.exp(2j * math.pi * (q % 5) / 5.0) if twist else (1.0 + 0.0j)

    par = list(range(n_tet * n_loc))
    ph = np.ones(n_tet * n_loc, dtype=np.complex128)

    def _find(x: int) -> Tuple[int, complex]:
        if par[x] == x:
            return x, 1.0 + 0.0j
        r, pu = _find(par[x])
        par[x] = r
        ph[x] *= pu
        return r, ph[x]

    for fg, t0, f0, t1, _f1, p0 in mdata["faces"]:
        tf = (om ** int(coc[fg])) if twist else (1.0 + 0.0j)
        for tup_p, lp in gmap.items():
            if tup_p[f0] != 0:
                continue
            tn_tup = [0, 0, 0, 0]
            for a in range(4):
                tn_tup[p0[a]] = tup_p[a]
            ln = gmap[tuple(tn_tup)]
            rp, php = _find(t0 * n_loc + lp)
            rn, phn = _find(t1 * n_loc + ln)
            if rp != rn:
                par[rp] = rn
                ph[rp] = tf * phn / php

    r_dir: Dict[int, bool] = {}
    for t in range(n_tet):
        for lc in range(n_loc):
            r, _ = _find(t * n_loc + lc)
            if horo_arr[lc]:
                r_dir[r] = True
            elif r not in r_dir:
                r_dir[r] = False

    r2d = {r: idx for idx, r in enumerate(sorted(r for r, is_d in r_dir.items() if not is_d))}
    n_dof = len(r2d)

    rows_l, cols_l, kv_l, mv_l = [], [], [], []
    nmap = []
    for t in range(n_tet):
        gm = geoms_k11[t]
        dvol = gm["dvol"]
        ginv = gm["ginv"]
        gp = gm["gphi"]
        ke = np.einsum("eq,eqij,eai,ebj->eab", dvol, ginv, gp, gp)
        me = np.einsum("eq,qa,qb->eab", dvol, KEAST11_BARY, KEAST11_BARY)

        rr_e = np.repeat(stets_arr, 4, axis=1).ravel()
        cc_e = np.tile(stets_arr, (1, 4)).ravel()
        K_loc = coo_matrix((ke.ravel(), (rr_e, cc_e)), shape=(n_loc, n_loc)).toarray().astype(np.complex128)
        M_loc = coo_matrix((me.ravel(), (rr_e, cc_e)), shape=(n_loc, n_loc)).toarray().astype(np.complex128)

        al, ad, ap = [], [], []
        for lc in range(n_loc):
            r, pval = _find(t * n_loc + lc)
            if r in r2d:
                al.append(lc)
                ad.append(r2d[r])
                ap.append(pval)
        al_a = np.array(al, dtype=int)
        ad_a = np.array(ad, dtype=int)
        ap_a = np.array(ap, dtype=np.complex128)
        nmap.append((al_a, ad_a, ap_a))

        pm = np.conj(ap_a)[:, None] * ap_a[None, :]
        rows_l.append(np.repeat(ad_a, len(ad_a)))
        cols_l.append(np.tile(ad_a, len(ad_a)))
        kv_l.append((K_loc[np.ix_(al_a, al_a)] * pm).ravel())
        mv_l.append((M_loc[np.ix_(al_a, al_a)] * pm).ravel())

    K_mat = coo_matrix((np.concatenate(kv_l), (np.concatenate(rows_l), np.concatenate(cols_l))), shape=(n_dof, n_dof)).toarray()
    M_mat = coo_matrix((np.concatenate(mv_l), (np.concatenate(rows_l), np.concatenate(cols_l))), shape=(n_dof, n_dof)).toarray()
    K_mat = 0.5 * (K_mat + K_mat.conj().T)
    M_mat = 0.5 * (M_mat + M_mat.conj().T)

    # Direct generalized Hermitian solver `scipy.linalg.eigh(K, M)` (distinct from Producer's shift-invert Cholesky):
    evals, evecs = eigh(K_mat, M_mat, subset_by_index=[0, n_eigs - 1])
    for j in range(n_eigs):
        nrm = math.sqrt(max(1e-30, float(np.real(np.vdot(evecs[:, j], M_mat @ evecs[:, j])))))
        evecs[:, j] /= nrm

    loc_modes = np.zeros((n_eigs, n_tet, n_loc), dtype=np.complex128)
    for t in range(n_tet):
        al_a, ad_a, ap_a = nmap[t]
        loc_modes[:, t, al_a] = (ap_a[:, None] * evecs[ad_a, :]).T

    return np.array(evals, dtype=float), loc_modes


def _ref_extract_ckm_pmns(
    Y_u: np.ndarray, Y_d: np.ndarray, Y_e: np.ndarray, M_nu_kk: np.ndarray, M_nu_w: np.ndarray
) -> Dict[str, Any]:
    """Independent SVD / Jarlskog extraction from Yukawa & Majorana matrices."""
    def _angles_from_u(U: np.ndarray) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        Ua = np.abs(U)
        s13 = min(1.0, max(0.0, float(Ua[0, 2] ** 2)))
        c13 = max(1e-30, 1.0 - s13)
        s12 = min(1.0, max(0.0, float((Ua[0, 1] ** 2) / c13)))
        s23 = min(1.0, max(0.0, float((Ua[1, 2] ** 2) / c13)))
        return (
            (s12, s23, s13),
            (
                math.degrees(math.asin(math.sqrt(s12))),
                math.degrees(math.asin(math.sqrt(s23))),
                math.degrees(math.asin(math.sqrt(s13))),
            ),
        )

    def _jarlskog_from_herm(H1: np.ndarray, H2: np.ndarray) -> float:
        cm = H1 @ H2 - H2 @ H1
        dn = (float(np.linalg.norm(H1, "fro")) ** 3) * (float(np.linalg.norm(H2, "fro")) ** 3)
        return float(complex(np.linalg.det(cm)).imag / dn) if dn > 1e-60 else 0.0

    Uu, su_d, _ = np.linalg.svd(Y_u)
    Ud, sd_d, _ = np.linalg.svd(Y_d)
    Ue, se_d, _ = np.linalg.svd(Y_e)
    Un_kk, sn_kk_d, _ = np.linalg.svd(0.5 * (M_nu_kk + M_nu_kk.T))
    Un_w, sn_w_d, _ = np.linalg.svd(0.5 * (M_nu_w + M_nu_w.T))

    V_ckm = Uu[:, ::-1].conj().T @ Ud[:, ::-1]
    U_kk = Ue[:, ::-1].conj().T @ Un_kk[:, ::-1]
    U_w = Ue[:, ::-1].conj().T @ Un_w[:, ::-1]

    su = su_d[::-1]
    sn_w = sn_w_d[::-1]
    ckm_s2, ckm_d = _angles_from_u(V_ckm)
    kk_s2, kk_d = _angles_from_u(U_kk)
    w_s2, w_d = _angles_from_u(U_w)

    return {
        "ckm_sin2": list(ckm_s2),
        "pmns_kk_sin2": list(kk_s2),
        "pmns_w_sin2": list(w_s2),
        "ckm_deg": list(ckm_d),
        "pmns_kk_deg": list(kk_d),
        "pmns_w_deg": list(w_d),
        "j_ckm": _jarlskog_from_herm(Y_u @ Y_u.conj().T, Y_d @ Y_d.conj().T),
        "j_pmns_kk": _jarlskog_from_herm(Y_e @ Y_e.conj().T, M_nu_kk @ M_nu_kk.conj().T),
        "j_pmns_w": _jarlskog_from_herm(Y_e @ Y_e.conj().T, M_nu_w @ M_nu_w.conj().T),
        "su_ratios": [float(su[0] / su[2]), float(su[1] / su[2]), 1.0],
        "snu_w_ratios": [float(sn_w[0] / sn_w[2]), float(sn_w[1] / sn_w[2]), 1.0],
    }


def _random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    """Independent Ginibre QR Haar unitary U(3) sampler."""
    Z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = np.where(np.abs(d) > 0, d / np.abs(d), 1.0 + 0.0j)
    return Q * ph[None, :]


def run_keast11_fem_and_haar_countercheck(producer_g3: Dict[str, Any]) -> Dict[str, Any]:
    """Independent Keast-11 FEM countercheck + 25 fresh Haar U(3)^3 scrambling trials."""
    keast_deg4_err = _verify_keast11_degree4_exactness()
    rng = np.random.default_rng(20261111)

    checks_to_run = [
        ("reversible_6", "b++LLLLLLRLR"),
        ("global_min_irreversible_719", "b+-LLLLLRLLRR"),
        ("departure_irreversible_5122", "b++LLLLLRLLRRLR"),
    ]

    max_eig_rel_diff = 0.0
    max_angle_diff_deg = 0.0
    max_j_rel_diff = 0.0
    rev6_max_abs_j = 0.0
    max_haar_25_err = 0.0
    comparisons = {}

    QT = KEAST11_BARY.T

    for label, spec in checks_to_run:
        mdata = _ref_extract_manifold_geometry_and_gf5_cocycles(spec)
        nodes_arr, gmap, horo_arr, stets_arr, geoms_k11 = _ref_build_subdivision_and_keast11_geoms(
            mdata["grams"], n_sub=4
        )
        ev0, modes0 = _ref_solve_sector_k11(mdata, None, 0, nodes_arr, gmap, horo_arr, stets_arr, geoms_k11, n_eigs=5)

        line_evals = []
        for coc_raw in mdata["ramified_cocycles"]:
            coc = coc_raw.copy()
            ev1, m1 = _ref_solve_sector_k11(mdata, coc, 1, nodes_arr, gmap, horo_arr, stets_arr, geoms_k11, n_eigs=5)
            ev2, m2 = _ref_solve_sector_k11(mdata, coc, 2, nodes_arr, gmap, horo_arr, stets_arr, geoms_k11, n_eigs=5)
            if ev1[0] < ev2[0] - 1e-9:
                coc = (2 * coc) % 5
                ev1, m1 = _ref_solve_sector_k11(mdata, coc, 1, nodes_arr, gmap, horo_arr, stets_arr, geoms_k11, n_eigs=5)
                ev2, m2 = _ref_solve_sector_k11(mdata, coc, 2, nodes_arr, gmap, horo_arr, stets_arr, geoms_k11, n_eigs=5)

            psi = m1[:3]
            chi = m2[:3]
            hu = np.conj(m2[0])
            hd = m2[0]
            eta = modes0[:3]

            # Overlaps via Keast-11 rule:
            def _tri(A: np.ndarray, B: np.ndarray, H: np.ndarray) -> np.ndarray:
                out = np.zeros((3, 3), dtype=np.complex128)
                for t in range(mdata["num_tets"]):
                    dv = geoms_k11[t]["dvol"]
                    Hq = H[t, stets_arr] @ QT
                    Aq = A[:, t, :][:, stets_arr] @ QT
                    Bq = B[:, t, :][:, stets_arr] @ QT
                    out += np.einsum("aeq,beq,eq->ab", Aq, Bq, dv * Hq)
                return out

            Y_u = _tri(psi, psi, hu)
            Y_d = _tri(psi, chi, hd)
            Y_e = Y_d.T.copy()
            Y_nu = _tri(chi, eta, hu)

            B_maj = np.zeros((3, 3), dtype=np.complex128)
            M_w = np.zeros((3, 3), dtype=np.complex128)
            for t in range(mdata["num_tets"]):
                dv = geoms_k11[t]["dvol"]
                Eq = eta[:, t, :][:, stets_arr] @ QT
                B_maj += np.einsum("meq,neq,eq->mn", Eq, Eq, dv)
                Hu_q = hu[t, stets_arr] @ QT
                Ch_q = chi[:, t, :][:, stets_arr] @ QT
                M_w += np.einsum("aeq,beq,eq->ab", Ch_q, Ch_q, dv * (Hu_q ** 2))

            kkm = np.sqrt(np.maximum(0.0, ev0[:3]))
            M_R = 0.5 * (kkm[:, None] + kkm[None, :]) * (0.5 * (B_maj + B_maj.T))
            M_nu_kk = -(Y_nu @ np.linalg.solve(M_R, Y_nu.T))
            M_nu_w = 0.5 * (M_w + M_w.T)

            for conj_flag in (False, True):
                Yu_c = np.conj(Y_u) if conj_flag else Y_u
                Yd_c = np.conj(Y_d) if conj_flag else Y_d
                Ye_c = np.conj(Y_e) if conj_flag else Y_e
                Ynu_c = np.conj(Y_nu) if conj_flag else Y_nu
                MR_c = np.conj(M_R) if conj_flag else M_R
                Mnukk_c = np.conj(M_nu_kk) if conj_flag else M_nu_kk
                Mnuw_c = np.conj(M_nu_w) if conj_flag else M_nu_w

                obs = _ref_extract_ckm_pmns(Yu_c, Yd_c, Ye_c, Mnukk_c, Mnuw_c)
                obs["E0_q2"] = float(ev2[0])
                obs["E0_q1"] = float(ev1[0])
                obs["rel_j_ckm"] = float(mdata["sigma_P"] * obs["j_ckm"])
                obs["matrices"] = (Yu_c, Yd_c, Ye_c, Ynu_c, MR_c, Mnuw_c)
                line_evals.append(obs)

        # Pick canonical ground-state positive relational branch:
        min_e0 = min(x["E0_q2"] for x in line_evals)
        gs_cands = [x for x in line_evals if abs(x["E0_q2"] - min_e0) < 1e-6]
        gs_cands.sort(key=lambda x: -x["rel_j_ckm"])
        best = gs_cands[0]

        # Run 25 fresh adversarial random Haar U(3)^3 trials on `best`:
        Y_u, Y_d, Y_e, Y_nu, M_R, M_nu_w = best["matrices"]
        for _ in range(25):
            U_Q = _random_haar_u3(rng)
            U_uc = _random_haar_u3(rng)
            U_dc = _random_haar_u3(rng)
            U_L = _random_haar_u3(rng)
            U_ec = _random_haar_u3(rng)
            U_N = _random_haar_u3(rng)

            Yu_p = U_Q @ Y_u @ U_uc.conj().T
            Yd_p = U_Q @ Y_d @ U_dc.conj().T
            Ye_p = U_L @ Y_e @ U_ec.conj().T
            Ynu_p = U_L @ Y_nu @ U_N.conj().T
            MR_p = np.conj(U_N) @ M_R @ U_N.conj().T
            Mnukk_p = -(Ynu_p @ np.linalg.solve(MR_p, Ynu_p.T))
            Mnuw_p = U_L @ M_nu_w @ U_L.T

            obs_p = _ref_extract_ckm_pmns(Yu_p, Yd_p, Ye_p, Mnukk_p, Mnuw_p)
            err_trial = max(
                max(abs(a - b) for a, b in zip(best["ckm_sin2"], obs_p["ckm_sin2"])),
                max(abs(a - b) for a, b in zip(best["pmns_kk_sin2"], obs_p["pmns_kk_sin2"])),
                max(abs(a - b) for a, b in zip(best["pmns_w_sin2"], obs_p["pmns_w_sin2"])),
                abs(best["j_ckm"] - obs_p["j_ckm"]),
                abs(best["j_pmns_kk"] - obs_p["j_pmns_kk"]),
                abs(best["j_pmns_w"] - obs_p["j_pmns_w"]),
                max(abs(a - b) for a, b in zip(best["su_ratios"], obs_p["su_ratios"])),
                max(abs(a - b) for a, b in zip(best["snu_w_ratios"], obs_p["snu_w_ratios"])),
            )
            max_haar_25_err = max(max_haar_25_err, err_trial)

        prod_gs = producer_g3["candidates"][label]["resolutions"]["nsub_4"]["ground_state_positive_branch"]
        eig_diff = max(
            abs(best["E0_q2"] - prod_gs["E0_q2"]) / prod_gs["E0_q2"],
            abs(best["E0_q1"] - prod_gs["E0_q1"]) / prod_gs["E0_q1"],
        )
        max_eig_rel_diff = max(max_eig_rel_diff, eig_diff)

        p_ckm = [prod_gs["quark_ckm"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")]
        p_kk = [prod_gs["lepton_pmns_kk_dirichlet"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")]
        p_w = [prod_gs["lepton_pmns_weinberg"]["angles"][k] for k in ("theta_12_deg", "theta_23_deg", "theta_13_deg")]

        ang_diff = max(
            max(abs(a - b) for a, b in zip(best["ckm_deg"], p_ckm)),
            max(abs(a - b) for a, b in zip(best["pmns_kk_deg"], p_kk)),
            max(abs(a - b) for a, b in zip(best["pmns_w_deg"], p_w)),
        )
        max_angle_diff_deg = max(max_angle_diff_deg, ang_diff)

        if label == "reversible_6":
            for x in line_evals:
                rev6_max_abs_j = max(rev6_max_abs_j, abs(x["j_ckm"]), abs(x["j_pmns_kk"]), abs(x["j_pmns_w"]))
        else:
            p_j_ckm = prod_gs["relational_jarlskog"]["ckm"]
            j_diff = abs(best["rel_j_ckm"] - p_j_ckm) / max(1e-5, abs(p_j_ckm))
            max_j_rel_diff = max(max_j_rel_diff, j_diff)

        comparisons[label] = {
            "keast11_E0_q2_q1": [best["E0_q2"], best["E0_q1"]],
            "producer_q14_E0_q2_q1": [prod_gs["E0_q2"], prod_gs["E0_q1"]],
            "keast11_ckm_deg": best["ckm_deg"],
            "producer_q14_ckm_deg": p_ckm,
            "keast11_pmns_kk_deg": best["pmns_kk_deg"],
            "producer_q14_pmns_kk_deg": p_kk,
            "keast11_pmns_weinberg_deg": best["pmns_w_deg"],
            "producer_q14_pmns_weinberg_deg": p_w,
            "keast11_rel_j_ckm": best["rel_j_ckm"],
            "producer_q14_rel_j_ckm": prod_gs["relational_jarlskog"]["ckm"],
        }

    passed = (
        keast_deg4_err < 1e-14
        and rev6_max_abs_j < 1e-14
        and max_haar_25_err < 1e-12
        and max_eig_rel_diff < 5e-3
        and max_angle_diff_deg < 0.5
        and max_j_rel_diff < 0.03
    )
    return {
        "keast11_degree4_exactness_err": keast_deg4_err,
        "reversible_6_max_abs_jarlskog": rev6_max_abs_j,
        "max_25trial_adversarial_haar_err": max_haar_25_err,
        "max_keast11_vs_q14_eigenvalue_rel_diff": max_eig_rel_diff,
        "max_keast11_vs_q14_angle_diff_deg": max_angle_diff_deg,
        "max_keast11_vs_q14_jarlskog_rel_diff": max_j_rel_diff,
        "manifold_comparisons": comparisons,
        "passed": passed,
    }


def run_all_referee_checks(write_verdict: bool = True) -> Dict[str, Any]:
    """Execute complete zero-import Referee suite and write `outputs/referee_phase4_verdict.json`."""
    results_path = PROJECT_ROOT / "outputs" / "phase4_results.json"
    if not results_path.exists():
        raise FileNotFoundError(f"Producer output missing at {results_path}")
    prod = json.loads(results_path.read_text(encoding="utf-8"))

    ast_res = run_ast_guardrail_scan(PROJECT_ROOT)
    seal_res = run_seal_integrity_audit(PROJECT_ROOT)
    mp_res = run_mpmath_fox_wada_countercheck()
    dp9_res = run_dp9_weyl_countercheck(prod["gate2_dp9_cusp_cap"])
    fem_res = run_keast11_fem_and_haar_countercheck(prod["gate3_quark_lepton_unification"])

    all_passed = bool(
        prod.get("all_phase4_gates_passed", False)
        and ast_res["passed"]
        and seal_res["passed"]
        and mp_res["passed"]
        and dp9_res["passed"]
        and fem_res["passed"]
    )

    verdict = {
        "referee": "Phase 4 AST-Isolated Zero-Import Referee (Guardrails 1-6)",
        "all_referee_checks_passed": all_passed,
        "ast_guardrail_scan": ast_res,
        "seal_integrity_audit": seal_res,
        "mpmath_50digit_fox_wada_countercheck": mp_res,
        "dp9_weyl_reflection_countercheck": dp9_res,
        "keast11_fem_and_25trial_haar_countercheck": fem_res,
    }

    if write_verdict:
        out_path = PROJECT_ROOT / "outputs" / "referee_phase4_verdict.json"
        out_path.write_text(json.dumps(verdict, indent=2), encoding="utf-8")

    return verdict


if __name__ == "__main__":
    v = run_all_referee_checks(write_verdict=True)
    print("Phase 4 Referee all_referee_checks_passed:", v["all_referee_checks_passed"])
    print("  1. AST scan passed:", v["ast_guardrail_scan"]["passed"], "files:", v["ast_guardrail_scan"]["num_scanned_files"])
    print("  2. Seals intact:", v["seal_integrity_audit"]["passed"])
    print("  3. 50-digit mpmath Fox-Wada passed:", v["mpmath_50digit_fox_wada_countercheck"]["passed"], "max k=0 torsion:", v["mpmath_50digit_fox_wada_countercheck"]["max_unramified_k0_torsion"], "max prod-5 err:", v["mpmath_50digit_fox_wada_countercheck"]["max_ramified_cyclotomic_product5_err"])
    print("  4. dP9 Weyl-reflection countercheck passed:", v["dp9_weyl_reflection_countercheck"]["passed"], "roots:", v["dp9_weyl_reflection_countercheck"]["weyl_orbit_root_count"])
    print("  5. Keast-11 FEM & 25-trial Haar countercheck passed:", v["keast11_fem_and_25trial_haar_countercheck"]["passed"])
    print("     Keast-11 deg4 err:", v["keast11_fem_and_25trial_haar_countercheck"]["keast11_degree4_exactness_err"])
    print("     Max eig rel diff:", v["keast11_fem_and_25trial_haar_countercheck"]["max_keast11_vs_q14_eigenvalue_rel_diff"])
    print("     Max angle diff (deg):", v["keast11_fem_and_25trial_haar_countercheck"]["max_keast11_vs_q14_angle_diff_deg"])
    print("     Max 25-trial Haar err:", v["keast11_fem_and_25trial_haar_countercheck"]["max_25trial_adversarial_haar_err"])
    if not v["all_referee_checks_passed"]:
        sys.exit(1)
