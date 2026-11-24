#!/usr/bin/env python3
r"""
Standalone Disjoint Cold-Room Zero-Trust Referee (run3; supersedes frozen v1
referee_a2_peer_audit_v2.py @ 2458d7736 and frozen run2 referee_a2_peer_audit_v2_run2.py
@ 78b4c14ed -> 6ee08d020 whose strict 1e-16 Kutta-3/8 alpha_3 RG-invariance self-gate hit
1.70e-16 at n_base=64; run3 refines n_base=64 -> 128 without loosening any threshold) for
Card A2-PEER-AUDIT-V2 (strictly 0 of 19; auditing Authoritative Producer v2 at
relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py -> a2_peer_audit_v2_run2_results.json,
commits 9e3e5b118 -> 18a5c79c9, with frozen v1 at relays/a2_peer_audit_v2/ untouched).

Disjoint Algorithms & Zero Shared Helpers with Producer:
  - R_PA2_A: Independent SHA-256 manifest verification for Producer v2, frozen v1,
    12/12 agy-exp (57ad12a6a), AND BOTH Producer v2's 7-dir agy subset (23/23) and the
    complete 8-dir AGY-C31..C38 set (27/27 including agy_2026-11-22_c35), AST hygiene,
    JSON float scan, and Catch FL8-F2b audit on referee_x_floor_link8.py.
  - R_PA2_B: Explicit 32x32 Cl(10) Clifford Gamma-matrix traces (disjoint from Cartan
    weight sums!) + explicit 15x15 / 24x24 ad(X) traces for pure 6D SU(4)/SU(5) +
    8x8 Bourbaki E_8 Cartan-matrix Weyl-orbit BFS (disjoint from R^8 root coordinates!)
    confirming FL8-F1, FL8-F7, and L8_3.
  - R_PA2_C: Gieseking 2-gen 1-relator m000 + Wirtinger 2-gen knot presentation of m004
    (disjoint from mapping-torus presentation!) + Wirtinger Reidemeister-Schreier 8^3_4 +
    32x32 Cl(10) spinor-commutator centralizers (21,25,13,12) & 16x16 spinor SM anomalies
    (disjoint from 45x45 adjoint!) + CRT E[6] ~= E[2] x E[3] FL8-F3 audit + mp.jtheta
    Delta Z(2i) < 0 < Delta Z(tau_8^+) (disjoint from Jacobi triple product!).
  - R_PA2_D: Pure mp.jtheta W_hol (via heat equation & E_2 = 8 sum(dt/t), disjoint from
    manual q-series!) + non-squaring 6x6 real symmetric eigsy Takagi (disjoint from
    eighe(M M^H)!) + explicit classical Kutta-3/8 RK4 (1/8, 3/8, 3/8, 1/8 weights,
    2-level Richardson, disjoint from GL4/GBS8/GL6!) for Fuchsian Dirac Gramian,
    Jack-Jones/FMM benchmarks, 24-ODE MSSM, 11-ODE Giudice-Romanino Split-SUSY + exact
    Coleman-Weinberg & matching-scale-invariance audit of 1-loop stop threshold, FL8-F2,
    FL8-F4, FL8-F5, FL8-F6.
  - R_PA2_E: Lobachevsky Gauss-Legendre quadrature for Vol(m004) (disjoint from polylog!),
    M_11-free Friedmann-Witten M_Pl^SD & M_Pl^ISO, Kutta-3/8 2-loop Caswell-Jones
    Lambda_QCD^(5f), Seam AGY-C37-S1, Cl(10) 16_+ spinor 6/6 U(1)_chi anomalies +
    explicit STr M_{Z'_chi}^2 == 0 + 6D I_8 gravity check, SymPy 2HDM B4 quartics,
    symbolic+numeric C37 E3 seesaw eps_1-cancellation, and OW22-F1..F3.
  - R_PA2_F: Independent LOCK_V3 canonical SHA-256 verification and full cross-seat
    table cross-check directly against a2_ow27_v8_results.json, agy v7.json, and
    agy-exp verify_x_floor_link8_out.json.
  - RPF1..RPF6: Six dynamically scored Referee planted controls.

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 binary64 float()/complex() casts, 0 JSON floats.
  - 0 imports from frontier/, relays/, snappy, or Producer scripts.
  - 0 empirical PDG/NuFIT/Planck/DESI/CODATA constants (strictly 0 of 19).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import random
import subprocess
from collections import deque
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

SELF_PATH = Path(__file__).resolve()
REPO_ROOT = SELF_PATH.parents[2]
OUT_PATH = SELF_PATH.parent / "referee_a2_peer_audit_v2_run3_results.json"

PROD_V2_DIR = REPO_ROOT / "relays/a2_peer_audit_v2_run2"
PROD_V1_DIR = REPO_ROOT / "relays/a2_peer_audit_v2"
PROD_V2_SCRIPT = PROD_V2_DIR / "verify_a2_peer_audit_v2_run2.py"
PROD_V2_JSON = PROD_V2_DIR / "a2_peer_audit_v2_run2_results.json"

AGY_EXP_REF = "origin/agy/self-consistent-loop-2026-11-11"
AGY_REF = "origin/agy/cusp-action-2026-11-20"
MAIN_REF = "origin/main"
PHYS_REF = "origin/audit/physical-bridge-2026-09-05"
CHAT1_REF = "origin/chat1/web-seat"
SM_REF = "origin/claude/standard-model-derivation-0qt6ao"
CLD_REF = "origin/cld/cool-hamilton-k9eqvo"

EXPECTED_LOCK_V3 = "ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a"

J_MP = mp.mpc(0, 1)


def rat_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def fr_mp(val: Fr) -> mp.mpf:
    return mp.mpf(val.numerator) / mp.mpf(val.denominator)


def p10_mp(exp_i: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp_i)


def fr_str(val: Fr) -> str:
    return f"{val.numerator}/{val.denominator}" if val.denominator != 1 else str(val.numerator)


def git_bytes(ref: str, rel_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{ref}:{rel_path}"])


def git_tree_files(ref: str, prefix: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "ls-tree", "-r", "--name-only", ref, prefix]
    ).decode("utf-8")
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def git_rev9(ref: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=9", ref]
    ).decode("utf-8").strip()


def count_json_float_tokens(node: Any) -> int:
    if isinstance(node, float):
        return 1
    if isinstance(node, dict):
        return sum(count_json_float_tokens(v) for v in node.values())
    if isinstance(node, list):
        return sum(count_json_float_tokens(v) for v in node)
    return 0


def assert_zero_json_floats(node: Any, path: str = "$") -> None:
    if isinstance(node, float):
        raise AssertionError(f"Forbidden JSON float token at {path}: {node!r}")
    if isinstance(node, dict):
        for k, v in node.items():
            assert_zero_json_floats(v, f"{path}.{k}")
    elif isinstance(node, list):
        for idx, v in enumerate(node):
            assert_zero_json_floats(v, f"{path}[{idx}]")


def check_ast_hygiene(src: str, filename: str) -> dict[str, Any]:
    tree = ast.parse(src, filename=filename)
    lit_lines = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))
    ]
    cast_lines = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id in ("float", "complex")
    ]
    bad_imports: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = getattr(n, "module", "") or ""
            names = " ".join(a.name for a in n.names)
            joined = f"{mod} {names}"
            if any(tok in joined for tok in ("frontier", "relays", "self_consistent", "snappy", "verify_a2_peer_audit")):
                bad_imports.append(joined)
    return {
        "float_complex_literals": len(lit_lines),
        "binary64_casts": len(cast_lines),
        "forbidden_imports": len(bad_imports),
        "clean": bool(len(lit_lines) == 0 and len(cast_lines) == 0 and len(bad_imports) == 0),
    }


# ==============================================================================
# Disjoint Numerical Primitives: Classical Kutta-3/8 RK4 + 2-Level Richardson,
# Non-Squaring 6x6 Real Symmetric Takagi, and Mezzadri-QR Haar U(3)
# ==============================================================================

def kutta38_integrate(rhs_fn, y0: list[mp.mpf], t0: mp.mpf, t1: mp.mpf, n_steps: int) -> list[mp.mpf]:
    """Explicit classical 4th-order Kutta-3/8 Runge-Kutta (weights 1/8, 3/8, 3/8, 1/8)."""
    h = (t1 - t0) / mp.mpf(n_steps)
    c13 = rat_mp(1, 3)
    c23 = rat_mp(2, 3)
    c18 = rat_mp(1, 8)
    dim = len(y0)
    y = list(y0)
    t = t0
    for _ in range(n_steps):
        k1 = rhs_fn(t, y)
        y2 = [y[i] + c13 * h * k1[i] for i in range(dim)]
        k2 = rhs_fn(t + c13 * h, y2)
        y3 = [y[i] + h * (-c13 * k1[i] + k2[i]) for i in range(dim)]
        k3 = rhs_fn(t + c23 * h, y3)
        y4 = [y[i] + h * (k1[i] - k2[i] + k3[i]) for i in range(dim)]
        k4 = rhs_fn(t + h, y4)
        y = [y[i] + c18 * h * (k1[i] + mp.mpf(3) * k2[i] + mp.mpf(3) * k3[i] + k4[i]) for i in range(dim)]
        t += h
    return y


def kutta38_rich2(rhs_fn, y0: list[mp.mpf], t0: mp.mpf, t1: mp.mpf, n_base: int) -> list[mp.mpf]:
    """2-level Richardson extrapolation (order 6) on Kutta-3/8: (N, 2N, 4N)."""
    y1 = kutta38_integrate(rhs_fn, y0, t0, t1, n_base)
    y2 = kutta38_integrate(rhs_fn, y0, t0, t1, 2 * n_base)
    y4 = kutta38_integrate(rhs_fn, y0, t0, t1, 4 * n_base)
    dim = len(y0)
    r1a = [(mp.mpf(16) * y2[i] - y1[i]) / mp.mpf(15) for i in range(dim)]
    r1b = [(mp.mpf(16) * y4[i] - y2[i]) / mp.mpf(15) for i in range(dim)]
    return [(mp.mpf(32) * r1b[i] - r1a[i]) / mp.mpf(31) for i in range(dim)]


def takagi_real6_eigsy(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """
    Non-squaring Takagi factorization M_sym = U_T * diag(s) * U_T^T via 6x6 real
    symmetric block matrix H_6 = [[Re M, Im M], [Im M, -Re M]] using mp.eigsy
    (strictly disjoint from eighe(M M^H) and svd_c).
    """
    m_s = (m_sym + m_sym.T) / mp.mpf(2)
    h6 = mp.zeros(6, 6)
    for r in range(3):
        for c in range(3):
            ar = mp.re(m_s[r, c])
            bi = mp.im(m_s[r, c])
            h6[r, c] = ar
            h6[r, c + 3] = bi
            h6[r + 3, c] = bi
            h6[r + 3, c + 3] = -ar
    evals, evecs = mp.eigsy(h6)
    # Sort eigenvalues ascending; the top 3 eigenvalues are +s_0 <= +s_1 <= +s_2:
    idx_sorted = sorted(range(6), key=lambda k: evals[k])
    pos_idx = idx_sorted[3:]
    ut = mp.zeros(3, 3)
    svs: list[mp.mpf] = []
    for col_new, k in enumerate(pos_idx):
        svs.append(evals[k])
        for r in range(3):
            ut[r, col_new] = mp.mpc(evecs[r, k], evecs[r + 3, k])
    return ut, svs


def svd_left_asc(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """Left singular vectors and singular values in ascending order via Hermitian eighe(M M^H)."""
    hh = mat * mat.H
    evs, vecs = mp.eighe((hh + hh.H) / mp.mpf(2))
    idx = sorted(range(3), key=lambda k: mp.re(evs[k]))
    u_out = mp.matrix([[vecs[r, idx[c]] for c in range(3)] for r in range(3)])
    s_out = [mp.sqrt(max(mp.mpf(0), mp.re(evs[k]))) for k in idx]
    return u_out, s_out


def haar_u3_householder(rng: random.Random) -> mp.matrix:
    """Disjoint Haar-random U(3) via complex Householder QR with Mezzadri phase normalization."""
    z = mp.zeros(3, 3)
    denom = mp.mpf(1 << 53)
    twopi = mp.mpf(2) * mp.pi
    for r in range(3):
        for c in range(3):
            u1 = mp.mpf(max(1, rng.getrandbits(53))) / denom
            u2 = mp.mpf(rng.getrandbits(53)) / denom
            rad = mp.sqrt(-mp.mpf(2) * mp.log(u1))
            z[r, c] = mp.mpc(rad * mp.cos(twopi * u2), rad * mp.sin(twopi * u2))
    r_mat = z.copy()
    q_mat = mp.eye(3)
    for k in range(3):
        x = mp.matrix([[r_mat[i, k]] for i in range(k, 3)])
        nrm = mp.sqrt(mp.re((x.H * x)[0, 0]))
        ph = mp.exp(J_MP * mp.arg(x[0, 0])) if abs(x[0, 0]) > mp.mpf(0) else mp.mpc(1)
        v = x.copy()
        v[0, 0] += ph * nrm
        vn2 = mp.re((v.H * v)[0, 0])
        h_sub = mp.eye(3 - k) - (mp.mpf(2) / vn2) * (v * v.H)
        h_full = mp.eye(3)
        for i in range(3 - k):
            for j in range(3 - k):
                h_full[k + i, k + j] = h_sub[i, j]
        r_mat = h_full * r_mat
        q_mat = q_mat * h_full.H
    d_fix = mp.diag([r_mat[k, k] / abs(r_mat[k, k]) for k in range(3)])
    return q_mat * d_fix


def gl_nodes_weights(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    jm = mp.zeros(n, n)
    for k in range(1, n):
        bk = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
        jm[k - 1, k] = bk
        jm[k, k - 1] = bk
    evs, vecs = mp.eigsy(jm)
    return [evs[k] for k in range(n)], [mp.mpf(2) * (vecs[0, k] ** 2) for k in range(n)]


# ==============================================================================
# Shared Exact Cl(10) 32x32 Clifford Algebra Builder (for R_PA2_B, R_PA2_C, R_PA2_E)
# ==============================================================================

def build_cl10_gammas() -> tuple[list[sp.SparseMatrix], sp.SparseMatrix, list[int]]:
    """Explicit 32x32 Cl(10) Gamma matrices via 5-fold Pauli Kronecker products."""
    i2 = sp.SparseMatrix([[1, 0], [0, 1]])
    s1 = sp.SparseMatrix([[0, 1], [1, 0]])
    s2 = sp.SparseMatrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.SparseMatrix([[1, 0], [0, -1]])

    def kron5(mats: list[sp.SparseMatrix]) -> sp.SparseMatrix:
        acc = mats[0]
        for m in mats[1:]:
            acc = sp.SparseMatrix(sp.kronecker_product(acc, m))
        return acc

    gammas: list[sp.SparseMatrix] = []
    for k in range(5):
        gammas.append(kron5([s3] * k + [s1] + [i2] * (4 - k)))
        gammas.append(kron5([s3] * k + [s2] + [i2] * (4 - k)))
    g11 = (-sp.I) ** 5 * gammas[0]
    for g in gammas[1:]:
        g11 = g11 * g
    plus16_idx = [r for r in range(32) if g11[r, r] == 1]
    return gammas, g11, plus16_idx


# ==============================================================================
# R_PA2_A: Custody, AST/JSON Hygiene, & Guardrail-6 Referee Audit
# ==============================================================================

def run_r_pa2_a(prod_v2: dict[str, Any], discrepancies: list[dict[str, Any]]) -> dict[str, Any]:
    def verify_local_dir_manifests(dir_path: Path) -> dict[str, Any]:
        total = 0
        matched = 0
        details: dict[str, bool] = {}
        sample_bytes = b""
        sample_hash = ""
        for mf_name in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            mf = dir_path / mf_name
            for ln in mf.read_text(encoding="utf-8").splitlines():
                ln = ln.strip()
                if not ln:
                    continue
                parts = ln.split()
                h, target = parts[0], parts[1].lstrip("*")
                tpath = REPO_ROOT / target if "/" in target else dir_path / target
                data = tpath.read_bytes()
                ok = hashlib.sha256(data).hexdigest() == h
                total += 1
                if ok:
                    matched += 1
                details[mf_name] = ok
                if not sample_bytes:
                    sample_bytes, sample_hash = data, h
        return {
            "matched": matched,
            "total": total,
            "details": details,
            "_sample_bytes": sample_bytes,
            "_sample_hash": sample_hash,
        }

    v2_loc = verify_local_dir_manifests(PROD_V2_DIR)
    v1_loc = verify_local_dir_manifests(PROD_V1_DIR)
    v2_sample_bytes = v2_loc.pop("_sample_bytes")
    v2_sample_hash = v2_loc.pop("_sample_hash")
    v1_loc.pop("_sample_bytes")
    v1_loc.pop("_sample_hash")

    v2_ast = check_ast_hygiene(PROD_V2_SCRIPT.read_text(encoding="utf-8"), PROD_V2_SCRIPT.name)
    v2_json_floats = count_json_float_tokens(prod_v2)

    def audit_git_dirs(ref: str, dirs: list[str]) -> dict[str, Any]:
        total_m = 0
        matched_m = 0
        mismatches: list[str] = []
        missing_dirs: list[str] = []
        py_cnt = 0
        py_bad = 0
        json_cnt = 0
        json_floats = 0
        samp_b = b""
        samp_h = ""
        for d in dirs:
            files = git_tree_files(ref, d)
            if not files:
                missing_dirs.append(d)
                continue
            for f in files:
                if f.endswith("SHA256.txt"):
                    txt = git_bytes(ref, f).decode("utf-8")
                    for ln in txt.splitlines():
                        ln = ln.strip()
                        if not ln:
                            continue
                        parts = ln.split()
                        if len(parts) < 2:
                            continue
                        h, target = parts[0], parts[1].lstrip("*")
                        tpath = target if "/" in target else (f.rsplit("/", 1)[0] + "/" + target)
                        data = git_bytes(ref, tpath)
                        total_m += 1
                        if not samp_b:
                            samp_b, samp_h = data, h
                        if hashlib.sha256(data).hexdigest() == h:
                            matched_m += 1
                        else:
                            mismatches.append(f"{f} -> {tpath}")
                elif f.endswith(".py"):
                    py_cnt += 1
                    res = check_ast_hygiene(git_bytes(ref, f).decode("utf-8"), f)
                    if res["float_complex_literals"] > 0 or res["binary64_casts"] > 0:
                        py_bad += 1
                elif f.endswith(".json"):
                    json_cnt += 1
                    json_floats += count_json_float_tokens(json.loads(git_bytes(ref, f).decode("utf-8")))
        return {
            "head": git_rev9(ref),
            "manifests_matched": matched_m,
            "manifests_total": total_m,
            "mismatches": mismatches,
            "missing_dirs": missing_dirs,
            "py_files": py_cnt,
            "py_ast_bad": py_bad,
            "json_files": json_cnt,
            "json_float_tokens": json_floats,
            "_samp_b": samp_b,
            "_samp_h": samp_h,
        }

    exp_dirs = [
        "relays/x_hierarchy_link6_verify",
        "relays/x_hierarchy_link6_referee",
        "relays/x_foundations_link7_verify",
        "relays/x_foundations_link7_referee",
        "relays/x_floor_link8_verify",
        "relays/x_floor_link8_referee",
    ]
    agy_dirs_prod_v2 = [
        "relays/agy_2026-11-22_c31",
        "relays/agy_2026-11-22_c32",
        "relays/agy_2026-11-22_c33",
        "relays/agy_2026-11-22_c34",
        "relays/agy_2026-11-23_c35",  # Producer v2's typo path
        "relays/agy_2026-11-23_c36",
        "relays/agy_2026-11-23_c37",
        "relays/agy_2026-11-24_c38",
    ]
    agy_dirs_true = [
        "relays/agy_2026-11-22_c31",
        "relays/agy_2026-11-22_c32",
        "relays/agy_2026-11-22_c33",
        "relays/agy_2026-11-22_c34",
        "relays/agy_2026-11-22_c35",  # Actual C35 directory on b06c8fc1e!
        "relays/agy_2026-11-23_c36",
        "relays/agy_2026-11-23_c37",
        "relays/agy_2026-11-24_c38",
    ]

    exp_res = audit_git_dirs(AGY_EXP_REF, exp_dirs)
    agy_prod_subset = audit_git_dirs(AGY_REF, agy_dirs_prod_v2)
    agy_true_full = audit_git_dirs(AGY_REF, agy_dirs_true)
    agy_c35_only = audit_git_dirs(AGY_REF, ["relays/agy_2026-11-22_c35"])

    c35_samp_b = agy_c35_only.pop("_samp_b")
    c35_samp_h = agy_c35_only.pop("_samp_h")
    for d_clean in (exp_res, agy_prod_subset, agy_true_full):
        d_clean.pop("_samp_b")
        d_clean.pop("_samp_h")

    # Check DISC-PA2-1: Producer v2 skipped agy_2026-11-22_c35 due to 2026-11-23_c35 typo:
    prod_agy_reported = prod_v2["PA2_A_custody_hygiene_and_referee_audit"]["agy_custody"]["manifests_total"]
    if agy_prod_subset["missing_dirs"] or prod_agy_reported != agy_true_full["manifests_total"]:
        discrepancies.append({
            "id": "DISC-PA2-1",
            "block": "PA2-A",
            "severity": "REAL_DISCREPANCY",
            "location": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py:302",
            "producer_claim": (
                f"Claimed full AGY-C31..C38 custody audit with {prod_agy_reported}/{prod_agy_reported} "
                f"manifests, {prod_v2['PA2_A_custody_hygiene_and_referee_audit']['agy_custody']['py_files_audited']} .py files, "
                f"{prod_v2['PA2_A_custody_hygiene_and_referee_audit']['agy_custody']['json_files_audited']} .json files."
            ),
            "referee_finding": (
                f"Typo 'relays/agy_2026-11-23_c35' silently returned empty git ls-tree, omitting the entire "
                f"relays/agy_2026-11-22_c35/ directory ({agy_c35_only['manifests_total']} manifest entries, "
                f"{agy_c35_only['py_files']} .py files, {agy_c35_only['json_files']} .json files: c35_out.json & "
                f"blind_predictions_full_toe_v6.json). True AGY-C31..C38 totals on b06c8fc1e are "
                f"{agy_true_full['manifests_matched']}/{agy_true_full['manifests_total']} manifests, "
                f"{agy_true_full['py_files']} .py files, {agy_true_full['json_files']} .json files (all 4/4 C35 manifests pass with 0 floats)."
            ),
        })

    # Independent Catch FL8-F2b AST call/name/attribute audit of referee_x_floor_link8.py:
    ref_l8_src = git_bytes(AGY_EXP_REF, "relays/x_floor_link8_referee/referee_x_floor_link8.py").decode("utf-8")
    ref_l8_lines = ref_l8_src.splitlines()
    ref_l8_tree = ast.parse(ref_l8_src, filename="referee_x_floor_link8.py")
    code_names: set[str] = set()
    call_names: set[str] = set()
    for node in ast.walk(ref_l8_tree):
        if isinstance(node, ast.FunctionDef):
            code_names.add(node.name.lower())
        elif isinstance(node, ast.Name):
            code_names.add(node.id.lower())
        elif isinstance(node, ast.Attribute):
            code_names.add(node.attr.lower())
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                call_names.add(node.func.id.lower())
            elif isinstance(node.func, ast.Attribute):
                call_names.add(node.func.attr.lower())
    forbidden_kws = ("liouville", "fuchs", "weierstrass", "jtheta", "takagi", "svd", "pmns", "ckm", "w_hol", "gramian")
    code_hits = sorted([nm for nm in code_names if any(kw in nm for kw in forbidden_kws)])
    call_hits = sorted([nm for nm in call_names if any(kw in nm for kw in forbidden_kws)])
    doc_claims_fuchs = any("Fuchsian Liouville" in ln for ln in ref_l8_lines[:30])
    # Direct AST check for subscript/string literal "uv_yb0_ytau0_over_yt0":
    uv_echo_ast_lines = sorted({
        getattr(n, "lineno", 0)
        for n in ast.walk(ref_l8_tree)
        if isinstance(n, ast.Constant) and n.value == "uv_yb0_ytau0_over_yt0"
    })
    fl8_f2b_confirmed = bool(doc_claims_fuchs and len(code_hits) == 0 and len(call_hits) == 0 and uv_echo_ast_lines == [510, 511])

    unchanged = {
        "main": git_rev9(MAIN_REF),
        "physical": git_rev9(PHYS_REF),
        "chat1": git_rev9(CHAT1_REF),
        "sm": git_rev9(SM_REF),
        "cld_advisor": git_rev9(CLD_REF),
    }
    unchanged_match = bool(unchanged == prod_v2["PA2_A_custody_hygiene_and_referee_audit"]["unchanged_peer_heads"])
    if not unchanged_match:
        discrepancies.append({
            "id": "DISC-PA2-A-HEADS",
            "block": "PA2-A",
            "severity": "REAL_DISCREPANCY",
            "producer_claim": str(prod_v2["PA2_A_custody_hygiene_and_referee_audit"]["unchanged_peer_heads"]),
            "referee_finding": str(unchanged),
        })

    # RPF1: 1-byte tamper on Producer v2 script AND on agy C35 manifest target:
    t_v2 = bytes([v2_sample_bytes[0] ^ 1]) + v2_sample_bytes[1:]
    t_c35 = bytes([c35_samp_b[0] ^ 1]) + c35_samp_b[1:]
    rpf1_caught = bool(
        hashlib.sha256(v2_sample_bytes).hexdigest() == v2_sample_hash
        and hashlib.sha256(t_v2).hexdigest() != v2_sample_hash
        and hashlib.sha256(c35_samp_b).hexdigest() == c35_samp_h
        and hashlib.sha256(t_c35).hexdigest() != c35_samp_h
    )

    internal_ok = bool(
        v2_loc["matched"] == v2_loc["total"] == 2
        and v1_loc["matched"] == v1_loc["total"] == 2
        and v2_ast["clean"]
        and v2_json_floats == 0
        and exp_res["manifests_matched"] == exp_res["manifests_total"] == 12
        and exp_res["py_ast_bad"] == 0 and exp_res["json_float_tokens"] == 0
        and agy_prod_subset["manifests_matched"] == agy_prod_subset["manifests_total"] == 23
        and agy_true_full["manifests_matched"] == agy_true_full["manifests_total"] == 27
        and agy_true_full["py_ast_bad"] == 0 and agy_true_full["json_float_tokens"] == 0
        and fl8_f2b_confirmed
        and unchanged_match
        and rpf1_caught
    )
    return {
        "producer_v2_manifests": v2_loc,
        "frozen_v1_manifests": v1_loc,
        "producer_v2_ast_hygiene": v2_ast,
        "producer_v2_json_float_tokens": v2_json_floats,
        "agy_exp_57ad12a6a_custody": exp_res,
        "agy_b06c8fc1e_prod_v2_7dir_subset": agy_prod_subset,
        "agy_b06c8fc1e_true_complete_8dir_c31_c38": agy_true_full,
        "agy_b06c8fc1e_missed_c35_dir": agy_c35_only,
        "catch_FL8_F2b_independent_ast_audit": {
            "docstring_claims_fuchsian_liouville": doc_claims_fuchs,
            "code_identifier_hits": code_hits,
            "call_hits": call_hits,
            "uv_yb0_ytau0_over_yt0_ast_lines": uv_echo_ast_lines,
            "confirmed": fl8_f2b_confirmed,
        },
        "unchanged_peer_heads": unchanged,
        "rpf1_tamper_caught": rpf1_caught,
        "internal_gate_passed": internal_ok,
    }


# ==============================================================================
# R_PA2_B: 32x32 Cl(10) Traces, Sadov/KMT, 6D SU(4)/SU(5), & Bourbaki E_8 BFS
# ==============================================================================

def run_r_pa2_b(
    gammas: list[sp.SparseMatrix],
    plus16_idx: list[int],
    prod_v2: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    # 1. Verify full 55-pair Cl(10) anticommutator algebra:
    i32 = sp.SparseMatrix.eye(32)
    z32 = sp.SparseMatrix(32, 32, {})
    cliff_ok = True
    for a in range(10):
        for b in range(a, 10):
            ac = gammas[a] * gammas[b] + gammas[b] * gammas[a]
            tgt = (2 * i32) if a == b else z32
            if ac != tgt:
                cliff_ok = False

    # Build all 45 Spin(10) Hermitian generators Sigma_{ab} = (1/(2i)) Gamma_a Gamma_b (a < b):
    pairs45 = [(a, b) for a in range(10) for b in range(a + 1, 10)]
    sigmas45 = [sp.Rational(1, 2) * (-sp.I) * (gammas[a] * gammas[b]) for a, b in pairs45]

    # Symbolic Cartan F = sum_{k=0..4} h_k Sigma_{2k, 2k+1} on 16_+ (explicit 16x16 matrix):
    h_syms = sp.symbols("h1 h2 h3 h4 h5")
    cartan_pos = [pairs45.index((2 * k, 2 * k + 1)) for k in range(5)]
    f16_mat = sp.SparseMatrix(16, 16, {})
    f10_mat = sp.SparseMatrix(10, 10, {})
    for k in range(5):
        sk = sigmas45[cartan_pos[k]]
        for r_i, r_g in enumerate(plus16_idx):
            for c_i, c_g in enumerate(plus16_idx):
                if sk[r_g, c_g] != 0:
                    f16_mat[r_i, c_i] += h_syms[k] * sk[r_g, c_g]
        f10_mat[2 * k, 2 * k + 1] = -sp.I * h_syms[k]
        f10_mat[2 * k + 1, 2 * k] = sp.I * h_syms[k]

    tr16_2 = sp.expand((f16_mat * f16_mat).trace())
    tr16_4 = sp.expand((f16_mat ** 4).trace())
    tr10_2 = sp.expand((f10_mat * f10_mat).trace())
    tr10_4 = sp.expand((f10_mat ** 4).trace())

    # Explicit 45x45 adjoint action of f10_mat on so(10) basis T_{ab} = -i(E_{ab} - E_{ba}):
    t10_basis = []
    for a, b in pairs45:
        m = sp.SparseMatrix(10, 10, {(a, b): -sp.I, (b, a): sp.I})
        t10_basis.append(m)
    ad45_f = sp.SparseMatrix(45, 45, {})
    for col, tb in enumerate(t10_basis):
        comm = f10_mat * tb - tb * f10_mat
        for row, (a, b) in enumerate(pairs45):
            if comm[a, b] != 0:
                ad45_f[row, col] = sp.I * comm[a, b]
    tr45_2 = sp.expand((ad45_f * ad45_f).trace())
    tr45_4 = sp.expand((ad45_f ** 4).trace())

    id_16_2 = bool(sp.simplify(tr16_2 - 2 * tr10_2) == 0)
    id_16_4 = bool(sp.simplify(tr16_4 - (-tr10_4 + sp.Rational(3, 4) * (tr10_2 ** 2))) == 0)
    id_45_2 = bool(sp.simplify(tr45_2 - 8 * tr10_2) == 0)
    id_45_4 = bool(sp.simplify(tr45_4 - (2 * tr10_4 + 3 * (tr10_2 ** 2))) == 0)

    # Also verify non-diagonal generic integer element F_gen in 32x32 Cl(10), 10x10, 45x45!
    gen_coeffs = [(0, 1, 2), (1, 2, -1), (2, 3, 3), (3, 4, 1), (4, 5, -2), (5, 6, 1), (6, 7, 2), (7, 8, -1), (8, 9, 1), (0, 9, -1)]
    f32_gen = sp.SparseMatrix(32, 32, {})
    f10_gen = sp.SparseMatrix(10, 10, {})
    for a, b, coeff in gen_coeffs:
        idx = pairs45.index((a, b))
        f32_gen += coeff * sigmas45[idx]
        f10_gen += coeff * t10_basis[idx]
    f16_gen = sp.Matrix([[f32_gen[r, c] for c in plus16_idx] for r in plus16_idx])
    ad45_gen = sp.SparseMatrix(45, 45, {})
    for col, tb in enumerate(t10_basis):
        comm = f10_gen * tb - tb * f10_gen
        for row, (a, b) in enumerate(pairs45):
            if comm[a, b] != 0:
                ad45_gen[row, col] = sp.I * comm[a, b]
    g_t10_2 = sp.simplify((f10_gen ** 2).trace())
    g_t10_4 = sp.simplify((f10_gen ** 4).trace())
    g_t16_2 = sp.simplify((f16_gen ** 2).trace())
    g_t16_4 = sp.simplify((f16_gen ** 4).trace())
    g_t45_2 = sp.simplify((ad45_gen ** 2).trace())
    g_t45_4 = sp.simplify((ad45_gen ** 4).trace())
    nondiag_cl10_ok = bool(
        g_t16_2 == 2 * g_t10_2
        and g_t16_4 == -g_t10_4 + sp.Rational(3, 4) * (g_t10_2 ** 2)
        and g_t45_2 == 8 * g_t10_2
        and g_t45_4 == 2 * g_t10_4 + 3 * (g_t10_2 ** 2)
    )

    # 2. Sadov / KMT 6D N=(1,0) anomaly cancellation (lambda_{SO(10)} = 2):
    n16_s, n10_s = sp.symbols("n16 n10")
    coeff_f4 = sp.simplify((2 + n16_s - n10_s))
    n10_sol = sp.solve(sp.Eq(coeff_f4, 0), n10_s)[0]  # n16 + 2
    # Check exact cancellation in Cl(10) polynomial:
    c_f2sq = sp.Rational(3, 4) * (4 - n16_s)
    a_f2 = 8 - 2 * n16_s - n10_sol  # 6 - 3 n16
    poly_quart_ok = bool(sp.simplify((tr45_4 - n16_s * tr16_4 - n10_sol * tr10_4) - c_f2sq * (tr10_2 ** 2)) == 0)
    poly_quad_ok = bool(sp.simplify((tr45_2 - n16_s * tr16_2 - n10_sol * tr10_2) - a_f2 * tr10_2) == 0)

    lam_so10 = 2
    a_dot_b = sp.simplify(sp.Rational(lam_so10, 6) * a_f2)  # 2 - n16
    b_dot_b = sp.simplify(-sp.Rational(lam_so10 ** 2, 3) * c_f2sq)  # n16 - 4
    adj_2gm2 = sp.simplify(a_dot_b + b_dot_b)  # -2
    k_of_n16_0 = int(-b_dot_b.subs(n16_s, 0))  # 4
    k_of_n16_2 = int(-b_dot_b.subs(n16_s, 2))  # 2
    n16_on_f6 = int(sp.solve(sp.Eq(b_dot_b, -6), n16_s)[0])  # -2
    # Single-base k1 + k2 = 24 with k_i = 12 - 2 v_i => v_1 + v_2 = 0 (at n_5 = 0);
    # for (v_1, v_2) = (2, 1): k_1 = 8, k_2 = 10 => n_5 = 6 => n_T = 7:
    n5_req = 24 - ((12 - 2 * 2) + (12 - 2 * 1))
    nT_req = 1 + n5_req

    # 3. Pure 6D SU(4) and SU(5) irreducible tr_N F^4 via explicit 15x15 and 24x24 ad(X) traces:
    su_pure_f4: dict[str, int] = {}
    su_nondiag_ok = True
    for n_su in (4, 5):
        # Build explicit traceless basis of su(N) (dim N^2 - 1):
        basis: list[sp.Matrix] = []
        for i in range(n_su):
            for j in range(n_su):
                if i != j:
                    m = sp.zeros(n_su, n_su)
                    m[i, j] = 1
                    basis.append(m)
        for k in range(n_su - 1):
            m = sp.zeros(n_su, n_su)
            m[k, k] = 1
            m[k + 1, k + 1] = -1
            basis.append(m)
        dim_su = len(basis)
        # Dual extraction matrix: express any traceless M in `basis`:
        # Off-diagonal (i,j) coeff is M[i,j]; diagonal M[k,k] = c_k - c_{k-1} => c_k = sum_{r=0..k} M[r,r].
        off_idx = {(i, j): idx for idx, (i, j) in enumerate((i, j) for i in range(n_su) for j in range(n_su) if i != j)}
        diag_start = n_su * (n_su - 1)

        def to_coords(mat: sp.Matrix) -> list[sp.Expr]:
            vec = [sp.Integer(0)] * dim_su
            for (i, j), idx in off_idx.items():
                vec[idx] = mat[i, j]
            acc = sp.Integer(0)
            for k in range(n_su - 1):
                acc += mat[k, k]
                vec[diag_start + k] = acc
            return vec

        xs = sp.symbols(f"u0:{n_su - 1}")
        x_mat = sp.diag(*(list(xs) + [-sum(xs)]))
        ad_x = sp.SparseMatrix(dim_su, dim_su, {})
        for col, bm in enumerate(basis):
            cm = x_mat * bm - bm * x_mat
            vc = to_coords(cm)
            for row in range(dim_su):
                if vc[row] != 0:
                    ad_x[row, col] = vc[row]
        tr_ad4 = sp.expand((ad_x ** 4).trace())
        tr_f2 = sp.expand((x_mat ** 2).trace())
        tr_f4 = sp.expand((x_mat ** 4).trace())
        assert sp.simplify(tr_ad4 - (2 * n_su * tr_f4 + 6 * (tr_f2 ** 2))) == 0
        su_pure_f4[f"SU({n_su})_pure_SYM_trF4_coeff"] = 2 * n_su

        # Also check on a non-diagonal integer traceless matrix:
        x_nd = sp.zeros(n_su, n_su)
        for k in range(n_su - 1):
            x_nd[k, k] = k + 1
            x_nd[k, k + 1] = 1
            x_nd[k + 1, k] = -2
        x_nd[n_su - 1, n_su - 1] = -sum(k + 1 for k in range(n_su - 1))
        ad_nd = sp.SparseMatrix(dim_su, dim_su, {})
        for col, bm in enumerate(basis):
            vc = to_coords(x_nd * bm - bm * x_nd)
            for row in range(dim_su):
                if vc[row] != 0:
                    ad_nd[row, col] = vc[row]
        if (ad_nd ** 4).trace() != 2 * n_su * (x_nd ** 4).trace() + 6 * (((x_nd ** 2).trace()) ** 2):
            su_nondiag_ok = False

    # 4. 8x8 Bourbaki E_8 Cartan-matrix Weyl-orbit BFS (ZERO R^8 coordinates!):
    # Bourbaki numbering (0-indexed): 0-2-3-4-5-6-7 with 1 attached to 3.
    cartan_e8 = sp.eye(8) * 2
    for u, v in ((0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)):
        cartan_e8[u, v] = -1
        cartan_e8[v, u] = -1
    assert int(cartan_e8.det()) == 1
    c_rows = [[int(cartan_e8[i, j]) for j in range(8)] for i in range(8)]

    def weyl_reflect(root: tuple[int, ...], node_i: int) -> tuple[int, ...]:
        inner = sum(root[k] * c_rows[k][node_i] for k in range(8))
        out = list(root)
        out[node_i] -= inner
        return tuple(out)

    start_r = (1, 0, 0, 0, 0, 0, 0, 0)
    roots_set: set[tuple[int, ...]] = {start_r}
    dq = deque([start_r])
    while dq:
        cur = dq.popleft()
        for i in range(8):
            nxt = weyl_reflect(cur, i)
            if nxt not in roots_set:
                roots_set.add(nxt)
                dq.append(nxt)
    roots_240 = sorted(roots_set)
    # Highest root theta = (2, 3, 4, 6, 5, 4, 3, 2); extended affine node alpha_0 = -theta:
    theta_e8 = max(roots_240, key=lambda r: sum(r))
    alpha0 = tuple(-x for x in theta_e8)

    def reflect_by_root(v: tuple[int, ...], r_ref: tuple[int, ...]) -> tuple[int, ...]:
        # <v, r_ref> = v^T C r_ref (since all E_8 roots have norm^2 = 2):
        ip = sum(v[a] * c_rows[a][b] * r_ref[b] for a in range(8) for b in range(8))
        return tuple(v[a] - ip * r_ref[a] for a in range(8))

    # Branching 1: E_8 -> SU(5)_GUT x SU(5)_perp (delete node 4 [Bourbaki 5], Kac mark 5):
    # SU(5)_GUT simple roots: {0, 1, 2, 3}; SU(5)_perp simple roots: {5, 6, 7, alpha0}:
    gut5_gens = [tuple(1 if j == i else 0 for j in range(8)) for i in (0, 1, 2, 3)]
    perp5_gens = [tuple(1 if j == i else 0 for j in range(8)) for i in (5, 6, 7)] + [alpha0]

    def orbit_under(seed: tuple[int, ...], gens: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
        seen = {seed}
        q = deque([seed])
        while q:
            cur = q.popleft()
            for g in gens:
                nxt = reflect_by_root(cur, g)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return seen

    rem = set(roots_240)
    su5xsu5_orbits: list[tuple[int, int, int]] = []
    while rem:
        seed = next(iter(rem))
        joint = orbit_under(seed, gut5_gens + perp5_gens)
        d_gut = len(orbit_under(seed, gut5_gens))
        d_perp = len(orbit_under(seed, perp5_gens))
        rem -= joint
        su5xsu5_orbits.append((len(joint), d_gut, d_perp))
    # Add 4 Cartans to (20, 1) -> (24, 1) and 4 Cartans to (1, 20) -> (1, 24):
    su5_dims_final = sorted([d + 4 if d == 20 else d for d, _, _ in su5xsu5_orbits])
    # Extract the two (5, 10) / (5bar, 10bar) Higgs orbits (d_gut == 5):
    higgs_5_orbits = [(tot, dg, dp) for tot, dg, dp in su5xsu5_orbits if dg == 5]
    hu_perp_dim = higgs_5_orbits[0][2] if len(higgs_5_orbits) == 2 else -1
    hd_perp_dim = higgs_5_orbits[1][2] if len(higgs_5_orbits) == 2 else -1

    # Branching 2: E_8 -> Spin(10) x SU(4)_perp (delete node 5 [Bourbaki 6], Kac mark 4):
    # Spin(10) = D_5 simple roots {0, 1, 2, 3, 4}; SU(4)_perp = A_3 simple roots {6, 7, alpha0}:
    so10_gens = [tuple(1 if j == i else 0 for j in range(8)) for i in (0, 1, 2, 3, 4)]
    su4_gens = [tuple(1 if j == i else 0 for j in range(8)) for i in (6, 7)] + [alpha0]
    rem2 = set(roots_240)
    so10xsu4_orbits: list[tuple[int, int, int, set[tuple[int, ...]]]] = []
    while rem2:
        seed = next(iter(rem2))
        joint = orbit_under(seed, so10_gens + su4_gens)
        d10 = len(orbit_under(seed, so10_gens))
        d4 = len(orbit_under(seed, su4_gens))
        rem2 -= joint
        so10xsu4_orbits.append((len(joint), d10, d4, joint))
    # Cartan dims: 5 for Spin(10) (40+5=45), 3 for SU(4)_perp (12+3=15):
    so10_dims_map: dict[str, int] = {}
    orb_10_6: set[tuple[int, ...]] = set()
    orbs_16: list[set[tuple[int, ...]]] = []
    for tot, d10, d4, orb in so10xsu4_orbits:
        if d10 == 40 and d4 == 1:
            so10_dims_map["45"] = 45
        elif d10 == 1 and d4 == 12:
            so10_dims_map["15"] = 15
        elif d10 == 10 and d4 == 6:
            so10_dims_map["60"] = 60
            orb_10_6 = orb
        elif d10 == 16 and d4 == 4:
            so10_dims_map["64_a" if "64_a" not in so10_dims_map else "64_b"] = 64
            orbs_16.append(orb)
    orb_16_a, orb_16_b = orbs_16[0], orbs_16[1]
    # Compute exact Q_X on D_5 = {0,1,2,3,4} via the fundamental weight omega_4 (dual to deleted SU(5) node 4):
    # On D_5 Cartan C_D5, omega_4 has Dynkin labels [0,0,0,0,1]; Q_X = 4 * <alpha, omega_4> (gives {-3, 1, 5} on 16_+!):
    c_d5 = cartan_e8.extract([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
    c_d5_inv = c_d5.inv()
    # In simple-root basis, <alpha, omega_4> = sum_{i=0..4} c_d5_inv[4, i] * <alpha, alpha_i>:
    def qx_of_root(r: tuple[int, ...]) -> int:
        d_labels = [sum(r[k] * c_rows[k][i] for k in range(8)) for i in range(5)]
        val = sum(c_d5_inv[4, i] * d_labels[i] for i in range(5))
        return int(4 * val)

    qx_16_a = sorted({qx_of_root(r) for r in orb_16_a})
    qx_16_b = sorted({qx_of_root(r) for r in orb_16_b})
    qx_16_pos = qx_16_a if qx_16_a == [-3, 1, 5] else qx_16_b
    qx_10_set = sorted({qx_of_root(r) for r in orb_10_6})

    pm_16 = sorted({-1 if (q % 2 != 0) else 1 for q in qx_16_pos})
    pm_10 = sorted({-1 if (q % 2 != 0) else 1 for q in qx_10_set})
    dim4_pdecay = (-1) ** 3
    bilin_rpv = (-1) * (+1)

    # D_5 reflection even dimensions on 5_perp and Lambda^2(5_perp) via Adams character psi^2:
    # Reflection r: k -> -k mod 5 on 5_perp has trace chi(r) = 1 (fixes 0, swaps (1,4),(2,3)) and chi(r^2) = chi(e) = 5.
    chi_r_5 = 1
    chi_e_5 = 5
    chi_r_10 = (chi_r_5 ** 2 - chi_e_5) // 2  # Adams formula: (1 - 5)/2 = -2
    d5_even_5 = (5 + chi_r_5) // 2  # 3
    d5_even_10 = (10 + chi_r_10) // 2  # 4

    # RPF2: Plant n_10 = n_16 + 3 (tr_10 F^4 != 0) AND F_6 (n_16 = -2 < 0):
    rpf2_bad_f4 = sp.simplify((tr45_4 - n16_s * tr16_4 - (n16_s + 3) * tr10_4) - c_f2sq * (tr10_2 ** 2))
    rpf2_caught = bool(sp.simplify(rpf2_bad_f4 + tr10_4) == 0 and k_of_n16_0 == 4 and n16_on_f6 == -2)

    # Cross-check against Producer v2 PA2_B:
    pb_v2 = prod_v2["PA2_B_agy_exp_block_B1_hirzebruch_and_E8"]
    b_match_v2 = bool(
        pb_v2["L8_3_verified_the_same"]["e8_spin10_su4_dims"] == [45, 15, 60, 64, 64]
        and pb_v2["L8_3_verified_the_same"]["qx_16_and_10"] == [qx_16_pos, qx_10_set]
        and pb_v2["L8_3_verified_the_same"]["d5_reflection_even_5perp_10perp"] == [d5_even_5, d5_even_10]
        and pb_v2["catch_FL8_F1_hirzebruch_refutation"]["true_hirzebruch_k_for_n16_0_and_2"] == [k_of_n16_0, k_of_n16_2]
        and pb_v2["catch_FL8_F1_hirzebruch_refutation"]["spin10_n16_required_on_F6_impossible"] == n16_on_f6
        and pb_v2["catch_FL8_F1_hirzebruch_refutation"]["single_base_v1_plus_v2_24_instanton_rule_n5_and_nT_needed_for_2_and_1"] == [n5_req, nT_req]
        and pb_v2["catch_FL8_F1_hirzebruch_refutation"]["pure_6d_su4_su5_irreducible_trF4_anomalies"] == su_pure_f4
        and pb_v2["catch_FL8_F7_hu_hd_su5_perp_symmetry"]["e8_su5_gut_x_su5_perp_dims"] == su5_dims_final
        and pb_v2["catch_FL8_F7_hu_hd_su5_perp_symmetry"]["hu_in_5_GUT_su5_perp_rep_dim"] == hu_perp_dim
        and pb_v2["catch_FL8_F7_hu_hd_su5_perp_symmetry"]["hd_in_5bar_GUT_su5_perp_rep_dim"] == hd_perp_dim
    )
    if not b_match_v2:
        discrepancies.append({
            "id": "DISC-PA2-B",
            "block": "PA2-B",
            "severity": "REAL_DISCREPANCY",
            "producer_claim": str(pb_v2),
            "referee_finding": "Mismatch in Cl(10) / Sadov-KMT / Bourbaki E_8 branching.",
        })

    internal_ok = bool(
        cliff_ok and id_16_2 and id_16_4 and id_45_2 and id_45_4 and nondiag_cl10_ok
        and poly_quart_ok and poly_quad_ok and adj_2gm2 == -2
        and k_of_n16_0 == 4 and k_of_n16_2 == 2 and n16_on_f6 == -2
        and n5_req == 6 and nT_req == 7 and su_nondiag_ok
        and su_pure_f4 == {"SU(4)_pure_SYM_trF4_coeff": 8, "SU(5)_pure_SYM_trF4_coeff": 10}
        and len(roots_240) == 240 and theta_e8 == (2, 3, 4, 6, 5, 4, 3, 2)
        and su5_dims_final == [24, 24, 50, 50, 50, 50]
        and hu_perp_dim == 10 and hd_perp_dim == 10
        and sorted(so10_dims_map.values()) == [15, 45, 60, 64, 64]
        and qx_16_pos == [-3, 1, 5] and qx_10_set == [-2, 2]
        and pm_16 == [-1] and pm_10 == [1] and dim4_pdecay == -1 and bilin_rpv == -1
        and (d5_even_5, d5_even_10) == (3, 4)
        and rpf2_caught and b_match_v2
    )
    return {
        "cl10_32x32_identities_and_nondiag_verified": bool(cliff_ok and id_16_2 and id_16_4 and id_45_2 and id_45_4 and nondiag_cl10_ok),
        "sadov_kmt_FL8_F1": {
            "a_dot_b": str(a_dot_b),
            "b_dot_b": str(b_dot_b),
            "adjunction_2g_minus_2": int(adj_2gm2),
            "true_k_n16_0_2": [k_of_n16_0, k_of_n16_2],
            "F6_forces_n16": n16_on_f6,
            "single_base_n5_nT": [n5_req, nT_req],
            "pure_6d_su4_su5_adX4_coeffs": su_pure_f4,
            "pure_6d_su4_su5_nondiag_ok": su_nondiag_ok,
        },
        "bourbaki_e8_weyl_bfs": {
            "root_count": len(roots_240),
            "highest_root": list(theta_e8),
            "su5_gut_x_su5_perp_dims": su5_dims_final,
            "hu_hd_perp_dims_FL8_F7": [hu_perp_dim, hd_perp_dim],
            "spin10_x_su4_dims": sorted(so10_dims_map.values()),
            "qx_16_and_10": [qx_16_pos, qx_10_set],
            "z2_matter_parity_16_10_dim4_rpv": [pm_16[0], pm_10[0], dim4_pdecay, bilin_rpv],
            "d5_adams_reflection_even_5_10": [d5_even_5, d5_even_10],
        },
        "matches_producer_v2": b_match_v2,
        "rpf2_bad_n10_and_F6_caught": rpf2_caught,
        "internal_gate_passed": internal_ok,
    }


# ==============================================================================
# R_PA2_C: Wirtinger m004/8^3_4, 32x32 Cl(10) Centralizers, CRT E[2]xE[3], jtheta
# ==============================================================================

def run_r_pa2_c(
    gammas: list[sp.SparseMatrix],
    plus16_idx: list[int],
    prod_v2: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 50
    # 1. m000 Gieseking 2-generator 1-relator abelianization a^2 b^2 = b a => a + b = 0:
    snf_gies = smith_normal_form(sp.Matrix([[1, 1]]), domain=sp.ZZ)
    nz_gies = [abs(int(snf_gies[i, i])) for i in range(1) if snf_gies[i, i] != 0]
    rk_gies = 2 - len(nz_gies)
    m000_dbl = (2 ** rk_gies) - 1
    m_gies_mon = sp.Matrix([[1, 1], [1, 0]])
    m_rl_sq_ok = bool(m_gies_mon ** 2 == sp.Matrix([[2, 1], [1, 1]]) and int(m_gies_mon.det()) == -1)

    # 2. Disjoint 2-generator Wirtinger knot presentation of m004 = 4_1:
    # pi_1(4_1) = <x, y | (x y^{-1} x^{-1} y) x = y (x y^{-1} x^{-1} y)>
    # Build all 7 non-abelian groups of order <= 12 via explicit Cayley tables:
    def make_cayley(order: int, mul_fn) -> tuple[list[list[int]], list[int]]:
        tbl = [[mul_fn(a, b) for b in range(order)] for a in range(order)]
        inv = [0] * order
        for a in range(order):
            for b in range(order):
                if tbl[a][b] == 0:
                    inv[a] = b
                    break
        return tbl, inv

    def dihedral_mul(n: int):
        # Element = s * n + r (s in {0,1}, r in {0..n-1}); (s1,r1)(s2,r2) = (s1^s2, (r1 + (-1)^s1 r2) mod n)
        # Convention: r^r1 s^s1 * r^r2 s^s2 = r^(r1 + (-1)^s1 r2) s^(s1+s2)
        def _m(a: int, b: int) -> int:
            s1, r1 = divmod(a, n)
            s2, r2 = divmod(b, n)
            r = (r1 + (r2 if s1 == 0 else -r2)) % n
            return (s1 ^ s2) * n + r
        return _m

    # Q_8 elements: 0:1, 1:-1, 2:i, 3:-i, 4:j, 5:-j, 6:k, 7:-k
    q8_signs = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [1, 0, 3, 2, 5, 4, 7, 6],
        [2, 3, 1, 0, 6, 7, 5, 4],
        [3, 2, 0, 1, 7, 6, 4, 5],
        [4, 5, 7, 6, 1, 0, 2, 3],
        [5, 4, 6, 7, 0, 1, 3, 2],
        [6, 7, 4, 5, 3, 2, 1, 0],
        [7, 6, 5, 4, 2, 3, 0, 1],
    ]
    # A_4 via even permutations of (0,1,2,3):
    a4_perms = [
        p for p in itertools.permutations(range(4))
        if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0
    ]
    a4_idx = {p: i for i, p in enumerate(a4_perms)}
    # Dic_3 = <a, b | a^6 = 1, b^2 = a^3, b a b^{-1} = a^{-1}>, elem = s*6 + r:
    def dic3_mul(u: int, v: int) -> int:
        s1, r1 = divmod(u, 6)
        s2, r2 = divmod(v, 6)
        if s1 == 0 and s2 == 0:
            return (r1 + r2) % 6
        if s1 == 0 and s2 == 1:
            return 6 + ((r1 + r2) % 6)
        if s1 == 1 and s2 == 0:
            return 6 + ((r1 - r2) % 6)
        return (r1 - r2 + 3) % 6

    cayleys = {
        "S_3": make_cayley(6, dihedral_mul(3)),
        "D_4": make_cayley(8, dihedral_mul(4)),
        "Q_8": make_cayley(8, lambda a, b: q8_signs[a][b]),
        "D_5": make_cayley(10, dihedral_mul(5)),
        "D_6": make_cayley(12, dihedral_mul(6)),
        "A_4": make_cayley(12, lambda a, b: a4_idx[tuple(a4_perms[a][a4_perms[b][k]] for k in range(4))]),
        "Dic_3": make_cayley(12, dic3_mul),
    }

    def gen_size(tbl: list[list[int]], gens: list[int]) -> int:
        seen = {0}
        q = deque([0])
        while q:
            cur = q.popleft()
            for g in gens:
                nxt = tbl[cur][g]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return len(seen)

    surj_wirt: dict[str, int] = {}
    for gname, (tbl, inv) in cayleys.items():
        og = len(tbl)
        cnt = 0
        for x in range(og):
            xi = inv[x]
            for y in range(og):
                yi = inv[y]
                # w = x y^{-1} x^{-1} y
                w = tbl[tbl[tbl[x][yi]][xi]][y]
                if tbl[w][x] == tbl[y][w]:
                    if gen_size(tbl, [x, y]) == og:
                        cnt += 1
        surj_wirt[gname] = cnt

    # 3. Wirtinger Reidemeister-Schreier for 5-sheeted irregular D_5 cover 8^3_4:
    # p_x(k) = (-k) mod 5, p_y(k) = (1 - k) mod 5 (both involutions!)
    px = tuple((-k) % 5 for k in range(5))
    py = tuple((1 - k) % 5 for k in range(5))
    pmap = {"x": px, "y": py}
    eidx = {(k, g): 2 * k + gi for k in range(5) for gi, g in enumerate(("x", "y"))}
    # Spanning tree: 0 -y- 1 -x- 4 -y- 2 -x- 3 => edges (0,y), (1,x), (4,y), (2,x):
    rs_rows: list[list[int]] = []
    for k_t, g_t in ((0, "y"), (1, "x"), (4, "y"), (2, "x")):
        rw = [0] * 10
        rw[eidx[(k_t, g_t)]] = 1
        rs_rows.append(rw)
    # Single Wirtinger relator: x y^{-1} x^{-1} y x y^{-1} x y x^{-1} y^{-1} = 1:
    wirt_rel = [("x", 1), ("y", -1), ("x", -1), ("y", 1), ("x", 1), ("y", -1), ("x", 1), ("y", 1), ("x", -1), ("y", -1)]
    for k0 in range(5):
        rw = [0] * 10
        cur = k0
        for g, sgn in wirt_rel:
            if sgn == 1:
                rw[eidx[(cur, g)]] += 1
                cur = pmap[g][cur]
            else:
                prv = pmap[g][cur]  # involution!
                rw[eidx[(prv, g)]] -= 1
                cur = prv
        assert cur == k0
        rs_rows.append(rw)
    snf_834 = smith_normal_form(sp.Matrix(rs_rows), domain=sp.ZZ)
    nz_834 = [abs(int(snf_834[i, i])) for i in range(min(snf_834.rows, snf_834.cols)) if snf_834[i, i] != 0]
    rk_834 = 10 - len(nz_834)
    tors_834 = [d for d in nz_834 if d > 1]

    # Canonical longitude lambda = (y x^{-1} y^{-1} x)(x y^{-1} x^{-1} y) acts trivially on all 5 sheets:
    def act_word(word: list[tuple[str, int]], k0: int) -> int:
        cur = k0
        for g, _ in word:
            cur = pmap[g][cur]  # both x, y are involutions
        return cur

    lam_word = [("y", 1), ("x", -1), ("y", -1), ("x", 1), ("x", 1), ("y", -1), ("x", -1), ("y", 1)]
    lam_perm = tuple(act_word(lam_word, k) for k in range(5))
    assert lam_perm == (0, 1, 2, 3, 4)
    seen_s: set[int] = set()
    cusps_834: list[int] = []
    for k in range(5):
        if k not in seen_s:
            orb = {k, px[k], lam_perm[k]}
            seen_s |= orb
            cusps_834.append(len(orb))
    cusps_834.sort()

    # 4. Affine E_8 order-8 Kac pairs:
    aff_e8 = sp.eye(9) * 2
    for u, v in ((1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 0)):
        aff_e8[u, v] = -1
        aff_e8[v, u] = -1
    kv = aff_e8.nullspace()[0]
    marks = [int(x / min(kv)) for x in kv]
    ord8_pairs = sorted([
        (int(aff_e8.extract([r for r in range(9) if r not in (i, j)], [r for r in range(9) if r not in (i, j)]).det()), [i, j], [marks[i], marks[j]])
        for i, j in itertools.combinations(range(9), 2)
        if marks[i] + marks[j] == 8
    ])

    # 5. Spin(10) centralizers (21, 25, 13, 12) via 32x32 Cl(10) spinor commutators!
    pairs45 = [(a, b) for a in range(10) for b in range(a + 1, 10)]
    sigmas45 = [sp.Rational(1, 2) * (-sp.I) * (gammas[a] * gammas[b]) for a, b in pairs45]
    p_spin = gammas[6] * gammas[7] * gammas[8] * gammas[9]
    j_spin = sp.SparseMatrix(32, 32, {})
    for k in range(5):
        j_spin += sigmas45[pairs45.index((2 * k, 2 * k + 1))]

    # Exact QQ Gaussian elimination on real & imaginary parts of 32x32 Cl(10) spinor commutators:
    def flat_spinor_qq_rows(mats: list[sp.SparseMatrix]) -> list[list[Fr]]:
        keys = sorted({k for m in mats for k in m.todok().keys()})
        re_rows = [[Fr(0)] * len(mats) for _ in keys]
        im_rows = [[Fr(0)] * len(mats) for _ in keys]
        kidx = {k: i for i, k in enumerate(keys)}
        for col, m in enumerate(mats):
            for k, val in m.todok().items():
                rv, iv = val.as_real_imag()
                if rv != 0:
                    re_rows[kidx[k]][col] = Fr(int(rv.p), int(rv.q))
                if iv != 0:
                    im_rows[kidx[k]][col] = Fr(int(iv.p), int(iv.q))
        return [r for r in re_rows + im_rows if any(x != 0 for x in r)]

    def rank_qq(rows: list[list[Fr]]) -> int:
        mat = [list(r) for r in rows]
        ncols = len(mat[0]) if mat else 0
        rk = 0
        for col in range(ncols):
            piv = -1
            for r in range(rk, len(mat)):
                if mat[r][col] != 0:
                    piv = r
                    break
            if piv == -1:
                continue
            mat[rk], mat[piv] = mat[piv], mat[rk]
            pv = mat[rk][col]
            for r in range(rk + 1, len(mat)):
                if mat[r][col] != 0:
                    fac = mat[r][col] / pv
                    for c in range(col, ncols):
                        mat[r][c] -= fac * mat[rk][c]
            rk += 1
        return rk

    comm_p_list = [p_spin * s * p_spin - s for s in sigmas45]  # p_spin^2 == +I_32
    comm_j_list = [j_spin * s - s * j_spin for s in sigmas45]
    rows_p = flat_spinor_qq_rows(comm_p_list)
    rows_j = flat_spinor_qq_rows(comm_j_list)
    tr_j_qq = [[Fr(int(v.p), int(v.q)) for v in (sp.simplify((j_spin * s).trace()) for s in sigmas45)]]
    cent_dims_cl10 = [
        45 - rank_qq(rows_p),
        45 - rank_qq(rows_j),
        45 - rank_qq(rows_p + rows_j),
        45 - rank_qq(rows_p + rows_j + tr_j_qq),
    ]

    # 16_+ spinor 8+8 split and 4/4 SM anomalies via literal 16x16 Cl(10) matrix traces!
    h_op = [sigmas45[pairs45.index((2 * k, 2 * k + 1))] for k in range(5)]
    y_op32 = sp.Rational(1, 6) * (-2 * (h_op[0] + h_op[1] + h_op[2]) + 3 * (h_op[3] + h_op[4]))
    t3c_op32 = sp.Rational(1, 2) * (h_op[0] - h_op[1])
    t3w_op32 = sp.Rational(1, 2) * (h_op[3] - h_op[4])

    def restr16(m32: sp.SparseMatrix) -> sp.Matrix:
        return sp.Matrix([[m32[r, c] for c in plus16_idx] for r in plus16_idx])

    y16 = restr16(y_op32)
    p16 = restr16(p_spin)
    t3c16 = restr16(t3c_op32)
    t3w16 = restr16(t3w_op32)
    ps_l_cnt = sum(1 for k in range(16) if p16[k, k] == -1)
    ps_r_cnt = sum(1 for k in range(16) if p16[k, k] == 1)
    an_sm_cl10 = [
        sp.simplify(y16.trace()),
        sp.simplify((y16 ** 3).trace()),
        sp.simplify((t3c16 * t3c16 * y16).trace()),
        sp.simplify((t3w16 * t3w16 * y16).trace()),
    ]
    # Vector 10 Higgs doublet-triplet projection (-P_5 = +1):
    # On C^5 + C^5bar with 6Y = (-2,-2,-2,3,3) and (+2,+2,+2,-3,-3), P_5 = (+1,+1,+1,-1,-1):
    kept_6y = sorted([y for p, y in zip([1, 1, 1, -1, -1] * 2, [-2, -2, -2, 3, 3, 2, 2, 2, -3, -3]) if -p == 1])

    # 6. K_5 over F_5 and FL8-F3 via CRT E[6] ~= E[2] x E[3]:
    m_rl = ((2, 1), (1, 1))
    m_2 = ((1, 0), (2, 1))
    k5_inv: list[list[int]] = []
    for g in ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 1)):
        sub = {((k * g[0]) % 5, (k * g[1]) % 5) for k in range(1, 5)}
        img = {((m_rl[0][0] * p[0] + m_rl[0][1] * p[1]) % 5, (m_rl[1][0] * p[0] + m_rl[1][1] * p[1]) % 5) for p in sub}
        if img == sub:
            k5_inv.append([g[0], g[1]])

    # Explicit CRT E[2] x E[3] -> E[6]: (u2, u3) -> (3*u2 + 4*u3) mod 6 (since 3==1 mod 2, 0 mod 3; 4==0 mod 2, 1 mod 3):
    lines_e2 = [((1, 0),), ((0, 1),), ((1, 1),)]  # 3 order-2 subgroups of E[2]
    lines_e3 = [((1, 0),), ((0, 1),), ((1, 1),), ((1, 2),)]  # 4 order-3 subgroups of E[3]
    crt_total_e6 = len(lines_e2) * len(lines_e3)  # 12
    crt_anchored_33_sym: list[list[list[int]]] = []
    crt_k6_sets: dict[str, set[tuple[int, int]]] = {}
    for (g2,) in lines_e2:
        # Anchoring at (3,3) mod 6 <=> g2 == (1,1) mod 2!
        if g2 != (1, 1):
            continue
        for (g3,) in lines_e3:
            # Setwise A<->B swap on E[3]: (g3[1], g3[0]) in {g3, 2*g3 mod 3}:
            h3 = {((k * g3[0]) % 3, (k * g3[1]) % 3) for k in range(3)}
            if {(p[1], p[0]) for p in h3} == h3:
                # Reconstruct full order-6 subgroup in E[6] via CRT:
                gen6 = ((3 * g2[0] + 4 * g3[0]) % 6, (3 * g2[1] + 4 * g3[1]) % 6)
                orb6 = {((k * gen6[0]) % 6, (k * gen6[1]) % 6) for k in range(6)}
                prims = sorted([list(p) for p in orb6 if all(((m * p[0]) % 6, (m * p[1]) % 6) != (0, 0) for m in (1, 2, 3))])
                crt_anchored_33_sym.append(prims)
                tag = "K6_plus" if g3 == (1, 1) else "K6_minus"
                crt_k6_sets[tag] = orb6
    crt_anchored_33_sym.sort()

    k6_plus = crt_k6_sets["K6_plus"]
    k6_minus = crt_k6_sets["K6_minus"]
    s_on_k6_plus = {((-p[1]) % 6, p[0] % 6) for p in k6_plus}
    s_on_k6_minus = {((-p[1]) % 6, p[0] % 6) for p in k6_minus}
    mrl_k6p_ok = bool({((2 * p[0] + p[1]) % 6, (p[0] + p[1]) % 6) for p in k6_plus} == k6_plus)
    m2_k6p_ok = bool({(p[0] % 6, (2 * p[0] + p[1]) % 6) for p in k6_plus} == k6_plus)
    mrl_k6m_ok = bool({((2 * p[0] + p[1]) % 6, (p[0] + p[1]) % 6) for p in k6_minus} == k6_minus)
    m2_k6m_ok = bool({(p[0] % 6, (2 * p[0] + p[1]) % 6) for p in k6_minus} == k6_minus)

    # 7. |Aut(D_5)|, |Inn(D_5)|, |Out(D_5)| from Cayley table:
    d5_tbl, d5_inv = cayleys["D_5"]
    ord5_els = [g for g in range(1, 10) if d5_tbl[d5_tbl[d5_tbl[d5_tbl[g][g]][g]][g]][g] == 0]
    ord2_els = [g for g in range(1, 10) if d5_tbl[g][g] == 0]
    aut_d5 = sum(1 for r in ord5_els for s in ord2_els if d5_tbl[d5_tbl[s][r]][s] == d5_inv[r])
    inn_d5 = len({tuple(d5_tbl[d5_tbl[h][x]][d5_inv[h]] for x in range(10)) for h in range(10)})
    out_d5 = aut_d5 // inn_d5

    # 8. Delta Z(2i) < 0 < Delta Z(tau_8^+) via mp.jtheta (disjoint from Jacobi triple product!):
    def dz_jtheta(tv: mp.mpc) -> mp.mpf:
        q = mp.exp(J_MP * mp.pi * tv)
        t3 = mp.jtheta(3, 0, q)
        t4 = mp.jtheta(4, 0, q)
        al = mp.mpf(2) * mp.pi * mp.im(tv) / mp.mpf(5)
        return (mp.exp(-mp.mpf(2) * al) - mp.exp(-mp.mpf(3) * al)) * ((abs(t4) ** 4) - (abs(t3) ** 4))

    dz_2i = dz_jtheta(mp.mpf(2) * J_MP)
    dz_t8 = dz_jtheta(rat_mp(16, 5) + J_MP * rat_mp(8, 5))

    # RPF3: S swaps K6^+ <-> K6^- AND trace-4 perturbed monodromy admits 12 S_3 surjections:
    s3_tbl, s3_inv = cayleys["S_3"]
    s3_tr4 = 0
    for a in range(6):
        a2 = s3_tbl[a][a]
        a3 = s3_tbl[a2][a]
        for b in range(6):
            r1, r2 = s3_tbl[a3][b], s3_tbl[a2][b]
            for t in range(6):
                ti = s3_inv[t]
                if s3_tbl[s3_tbl[t][a]][ti] == r1 and s3_tbl[s3_tbl[t][b]][ti] == r2:
                    if gen_size(s3_tbl, [a, b, t]) == 6:
                        s3_tr4 += 1
    rpf3_caught = bool(s_on_k6_plus == k6_minus and s_on_k6_minus == k6_plus and s3_tr4 == 12)

    # Cross-check against Producer v2 PA2_C:
    pc_v2 = prod_v2["PA2_C_agy_exp_block_A_genesis_spin10_K6_outD5"]
    dz_v2 = [mp.mpf(x) for x in pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["jacobi_triple_deltaZ_2i_and_tau8"]]
    dz_diff = max(abs(dz_2i - dz_v2[0]), abs(dz_t8 - dz_v2[1]))
    c_match_v2 = bool(
        pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["m000_double_covers"] == m000_dbl
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["m004_nonabelian_surjections_le12"] == surj_wirt
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["8_3_4_H1_and_cusps"] == [rk_834, tors_834, cusps_834]
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["affine_e8_order8_min_det_and_nodes"] == [ord8_pairs[0][0], ord8_pairs[0][1], ord8_pairs[0][2]]
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["spin10_centralizer_dims"] == cent_dims_cl10
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["K5_unique_m004_RL_invariant"] == k5_inv[0]
        and pc_v2["F7_1_F7_2_L8_4_verified_the_same"]["D5_aut_inn_out"] == [aut_d5, inn_d5, out_d5]
        and pc_v2["catch_FL8_F3_K6_not_unique"]["total_order6_subgroups_of_E6"] == crt_total_e6
        and pc_v2["catch_FL8_F3_K6_not_unique"]["true_AB_setwise_symmetric_anchored_at_33_count"] == len(crt_anchored_33_sym)
        and pc_v2["catch_FL8_F3_K6_not_unique"]["true_AB_setwise_symmetric_subgroups_primitives"] == crt_anchored_33_sym
        and dz_diff < p10_mp(-10)
    )
    if not c_match_v2:
        discrepancies.append({
            "id": "DISC-PA2-C",
            "block": "PA2-C",
            "severity": "REAL_DISCREPANCY",
            "producer_claim": str(pc_v2),
            "referee_finding": f"Mismatch in PA2-C (dz_diff={mp.nstr(dz_diff, 6)}).",
        })

    internal_ok = bool(
        m000_dbl == 1 and m_rl_sq_ok
        and surj_wirt == {"S_3": 0, "D_4": 0, "Q_8": 0, "D_5": 20, "D_6": 0, "A_4": 24, "Dic_3": 0}
        and rk_834 == 3 and tors_834 == [] and cusps_834 == [1, 2, 2]
        and len(ord8_pairs) == 5 and ord8_pairs[0] == (20, [2, 5], [3, 5])
        and cent_dims_cl10 == [21, 25, 13, 12]
        and (ps_l_cnt, ps_r_cnt) == (8, 8) and all(v == 0 for v in an_sm_cl10)
        and kept_6y == [-3, -3, 3, 3]
        and k5_inv == [[1, 2]]
        and crt_total_e6 == 12 and len(crt_anchored_33_sym) == 2
        and (not mrl_k6p_ok) and (not m2_k6p_ok) and (not mrl_k6m_ok) and (not m2_k6m_ok)
        and (aut_d5, inn_d5, out_d5) == (20, 10, 2)
        and dz_2i < mp.mpf(0) and dz_t8 > mp.mpf(0)
        and rpf3_caught and c_match_v2
    )
    return {
        "m000_double_covers_and_monodromy_sq": [m000_dbl, m_rl_sq_ok],
        "m004_wirtinger_surjections_le12": surj_wirt,
        "8_3_4_wirtinger_rs_H1_cusps": [rk_834, tors_834, cusps_834],
        "affine_e8_order8_min_det": [ord8_pairs[0][0], ord8_pairs[0][1], ord8_pairs[0][2]],
        "cl10_32x32_spinor_centralizers": cent_dims_cl10,
        "cl10_16plus_ps_split_and_4_sm_anomalies_zero": [[ps_l_cnt, ps_r_cnt], all(v == 0 for v in an_sm_cl10), kept_6y],
        "K5_unique_RL_invariant": k5_inv[0],
        "crt_E2xE3_FL8_F3": {
            "total_order6_subgroups": crt_total_e6,
            "AB_setwise_sym_anchored_33_count": len(crt_anchored_33_sym),
            "primitives": crt_anchored_33_sym,
            "S_exchanges_K6p_K6m": bool(s_on_k6_plus == k6_minus and s_on_k6_minus == k6_plus),
            "K6_plus_preserved_MRL_M2": [mrl_k6p_ok, m2_k6p_ok],
            "K6_minus_preserved_MRL_M2": [mrl_k6m_ok, m2_k6m_ok],
        },
        "D5_aut_inn_out": [aut_d5, inn_d5, out_d5],
        "jtheta_deltaZ_2i_tau8": [mp.nstr(dz_2i, 12), mp.nstr(dz_t8, 12)],
        "jtheta_vs_triple_max_diff": mp.nstr(dz_diff, 6),
        "matches_producer_v2": c_match_v2,
        "rpf3_S_swap_and_tr4_S3_caught": rpf3_caught,
        "internal_gate_passed": internal_ok,
    }


# ==============================================================================
# R_PA2_D: mp.jtheta W_hol, 6x6 Real eigsy Takagi, & Classical Kutta-3/8 ODEs
# ==============================================================================

def eval_w_hol_jtheta(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    """Disjoint W_hol computed purely via mp.jtheta (heat equation + E_2 = 8 sum dtk/tk)."""
    qi = mp.matrix([[J_MP, 0], [0, -J_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = rat_mp(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    q = mp.exp(J_MP * mp.pi * tau)
    ph2 = mp.exp(J_MP * mp.pi * tau / mp.mpf(4)) / (q ** rat_mp(1, 4))
    t2 = ph2 * mp.jtheta(2, 0, q)
    t3 = mp.jtheta(3, 0, q)
    t4 = mp.jtheta(4, 0, q)
    # Heat equation: (1 / (2 pi i)) d/dtau jtheta(k, 0, q) = -(1/8) d^2/dz^2 jtheta(k, 0, q):
    dt2 = ph2 * (-mp.jtheta(2, 0, q, 2) / mp.mpf(8))
    dt3 = -mp.jtheta(3, 0, q, 2) / mp.mpf(8)
    dt4 = -mp.jtheta(4, 0, q, 2) / mp.mpf(8)
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    e2s = mp.mpf(8) * (l2d + l3d + l4d)

    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / mp.mpf(24)) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / mp.mpf(24)) * qj
        + (J_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / mp.mpf(24)) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    t1p = mp.pi * t2 * t3 * t4

    def th_char(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        am, bm, cbm = fr_mp(ta), fr_mp(tb), fr_mp(cb)
        zv = mp.pi * (am * tau + bm)
        return mp.exp(J_MP * mp.pi * am * am * tau + mp.mpf(2) * J_MP * mp.pi * am * cbm) * mp.jtheta(3, zv, q)

    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-mp.mpf(2) * J_MP * mp.pi * fr_mp(xv[0]))
    kap = {"1": -J_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": J_MP}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * th_char(cs[sk][0], cs[sk][1]) * th_char(ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    return mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])


def compute_dirac_s12_kutta38(tau_in: mp.mpc, n_th: int = 12, n_t: int = 14) -> list[mp.mpf]:
    """Disjoint classical Kutta-3/8 propagator for Fuchsian Liouville ODE u'' = -(wp(z) - c)/4 * u."""
    with mp.workdps(26):
        shift = int(mp.nint(mp.re(tau_in)))
        tau = tau_in - mp.mpf(shift)
        q = mp.exp(J_MP * mp.pi * tau)
        t30, t40 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        e1 = (mp.pi ** 2) * (t30 ** 4 + t40 ** 4) / mp.mpf(3)
        yi, xr = mp.im(tau), mp.re(tau)

        def wp_val(z: mp.mpc) -> mp.mpc:
            bv = mp.im(z) / yi
            av = mp.re(z) - bv * xr
            av -= mp.nint(av)
            bv -= mp.nint(bv)
            pz = mp.pi * (av + bv * tau)
            return e1 + (mp.pi * t30 * t40 * mp.jtheta(2, pz, q) / mp.jtheta(1, pz, q)) ** 2

        c13, c23, c18 = rat_mp(1, 3), rat_mp(2, 3), rat_mp(1, 8)

        def k38_step(z: mp.mpc, dz: mp.mpc, m: mp.matrix, cv: mp.mpc) -> mp.matrix:
            def rhs(zz: mp.mpc, mm: mp.matrix) -> mp.matrix:
                q0 = -(wp_val(zz) - cv) / mp.mpf(4)
                return mp.matrix([[mm[1, 0], mm[1, 1]], [q0 * mm[0, 0], q0 * mm[0, 1]]])

            k1 = rhs(z, m)
            k2 = rhs(z + c13 * dz, m + c13 * dz * k1)
            k3 = rhs(z + c23 * dz, m + dz * (-c13 * k1 + k2))
            k4 = rhs(z + dz, m + dz * (k1 - k2 + k3))
            return m + c18 * dz * (k1 + mp.mpf(3) * k2 + mp.mpf(3) * k3 + k4)

        def prop_uni(za: mp.mpc, zb: mp.mpc, cv: mp.mpc, ns: int) -> mp.matrix:
            dz = (zb - za) / mp.mpf(ns)
            m = mp.eye(2)
            for s in range(ns):
                m = k38_step(za + mp.mpf(s) * dz, dz, m, cv)
            return m

        z0 = (mp.mpc(1) + tau) / mp.mpf(2)

        def resid(cr: mp.mpf, ci: mp.mpf) -> mp.matrix:
            cv = mp.mpc(cr, ci)
            ta = prop_uni(z0, z0 + mp.mpc(1), cv, 24)
            tb = prop_uni(z0, z0 + tau, cv, 32)
            return mp.matrix([
                mp.im(ta[0, 0] + ta[1, 1]),
                mp.im(tb[0, 0] + tb[1, 1]),
                mp.im((ta * tb)[0, 0] + (ta * tb)[1, 1]),
            ])

        c_cur = mp.mpc(0, 0)
        h_fd = p10_mp(-6)
        for _ in range(10):
            r0 = resid(mp.re(c_cur), mp.im(c_cur))
            nrm = mp.sqrt(sum(r0[k] ** 2 for k in range(3)))
            if nrm < p10_mp(-15):
                break
            dr = (resid(mp.re(c_cur) + h_fd, mp.im(c_cur)) - r0) / h_fd
            di = (resid(mp.re(c_cur), mp.im(c_cur) + h_fd) - r0) / h_fd
            jac = mp.matrix([[dr[k], di[k]] for k in range(3)])
            st = -((jac.T * jac) ** (-1)) * (jac.T * r0)
            c_cur += mp.mpc(st[0], st[1])
            if nrm < p10_mp(-7):
                h_fd = p10_mp(-9)

        ta = prop_uni(z0, z0 + mp.mpc(1), c_cur, 24)
        tb = prop_uni(z0, z0 + tau, c_cur, 32)
        tr_a = mp.re(ta[0, 0] + ta[1, 1])
        disc = mp.sqrt(tr_a ** 2 - mp.mpf(4))
        v1 = mp.matrix([ta[0, 1], (tr_a + disc) / mp.mpf(2) - ta[0, 0]])
        v2 = mp.matrix([ta[0, 1], (tr_a - disc) / mp.mpf(2) - ta[0, 0]])
        vm = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
        vm = vm / mp.sqrt(vm[0, 0] * vm[1, 1] - vm[0, 1] * vm[1, 0])
        tbp = (vm ** (-1)) * tb * vm
        ph = mp.arg(tbp[0, 1])
        pm = vm * mp.matrix([[mp.exp(J_MP * ph / mp.mpf(2)), 0], [0, mp.exp(-J_MP * ph / mp.mpf(2))]])

        def dist_lat(z: mp.mpc) -> mp.mpf:
            bv = mp.im(z) / yi
            av = mp.re(z) - bv * xr
            av -= mp.nint(av)
            bv -= mp.nint(bv)
            zc = av + bv * tau
            return min(abs(zc + mp.mpf(m) + mp.mpf(n) * tau) for m in (-1, 0, 1) for n in (-1, 0, 1))

        def prop_seg(za: mp.mpc, zb: mp.mpc, m_in: mp.matrix) -> mp.matrix:
            m = m_in.copy()
            zc = za
            for _ in range(140):
                rem = zb - zc
                dr = abs(rem)
                if dr < p10_mp(-15):
                    break
                mst = rat_mp(1, 5) * dist_lat(zc)
                st = rem if dr <= mst else rem * (mst / dr)
                while abs(st) > rat_mp(1, 4) * dist_lat(zc + st / mp.mpf(2)):
                    st /= mp.mpf(2)
                m = k38_step(zc, st, m, c_cur)
                zc += st
            return m

        def e2phi(z: mp.mpc) -> mp.mpf:
            m = prop_seg(z0, z, mp.eye(2))
            u1 = m[0, 0] * pm[0, 0] + m[0, 1] * pm[1, 0]
            u2 = m[0, 0] * pm[0, 1] + m[0, 1] * pm[1, 1]
            return mp.mpf(1) / (mp.im(u1 * mp.conj(u2)) ** 2)

        r4, r5 = p10_mp(-4), p10_mp(-5)
        bc_star = (
            mp.mpf(100) * (mp.mpf(1) / (r5 * mp.sqrt(e2phi(r5))) + mp.log(r5))
            - (mp.mpf(1) / (r4 * mp.sqrt(e2phi(r4))) + mp.log(r4))
        ) / mp.mpf(99)

        gx_th, gw_th = gl_nodes_weights(n_th)
        gx_t, gw_t = gl_nodes_weights(n_t)
        corners = [
            rat_mp(1, 2) + tau / mp.mpf(2),
            -rat_mp(1, 2) + tau / mp.mpf(2),
            -rat_mp(1, 2) - tau / mp.mpf(2),
            rat_mp(1, 2) - tau / mp.mpf(2),
        ]
        angs = sorted((mp.arg(c) % (mp.mpf(2) * mp.pi)) for c in corners)
        sectors = [(angs[k], angs[k + 1]) for k in range(3)] + [(angs[3], angs[0] + mp.mpf(2) * mp.pi)]
        g_s12 = [mp.mpf(0)] * 3
        kinds = (3, 2, 4) if (shift % 2 != 0) else (4, 2, 3)

        for tha, thb in sectors:
            hth, mth = (thb - tha) / mp.mpf(2), (tha + thb) / mp.mpf(2)
            for ix in range(n_th):
                th = mth + hth * gx_th[ix]
                wth = hth * gw_th[ix]
                dbv = mp.sin(th) / yi
                dav = mp.cos(th) - dbv * xr
                rmax = rat_mp(1, 2) / max(abs(dav), abs(dbv))
                tmax = mp.mpf(1) / (-mp.log(rmax) + bc_star)
                ht = tmax / mp.mpf(2)
                tnodes = [ht + ht * gx_t[it] for it in range(n_t)]
                rnodes = [mp.exp(bc_star - mp.mpf(1) / tv) for tv in tnodes]
                zc = z0
                mc = mp.eye(2)
                dirc = mp.exp(J_MP * th)
                for it in range(n_t - 1, -1, -1):
                    tv, rv = tnodes[it], rnodes[it]
                    wt = ht * gw_t[it]
                    zv = rv * dirc
                    jac_r = (rv * rv) / (tv * tv)
                    if rv < p10_mp(-6):
                        ws12 = rv / tv
                    else:
                        mc = prop_seg(zc, zv, mc)
                        zc = zv
                        u1 = mc[0, 0] * pm[0, 0] + mc[0, 1] * pm[1, 0]
                        u2 = mc[0, 0] * pm[0, 1] + mc[0, 1] * pm[1, 1]
                        ws12 = jac_r / abs(mp.im(u1 * mp.conj(u2)))
                    dw2 = wth * wt
                    yv = mp.im(zv)
                    fac = mp.sqrt(mp.mpf(2) * yi) * mp.exp(-mp.mpf(2) * mp.pi * yv * yv / yi)
                    pz = mp.pi * zv
                    for ai, kd in enumerate(kinds):
                        g_s12[ai] += dw2 * (ws12 / mp.sqrt(mp.mpf(2) * mp.pi * yi)) * fac * (abs(mp.jtheta(kd, pz, q)) ** 2)
        tot = sum(g_s12)
        out = [mp.mpf(3) * x / tot for x in g_s12]
    return [mp.mpf(x) for x in out]


def prove_stop_threshold_and_split_susy_sympy() -> dict[str, Any]:
    """
    Exact SymPy proof of:
      1. 1-loop Coleman-Weinberg stop threshold in V = lambda |H|^4 (m_h^2 = 2 lambda v^2):
         Delta lambda_std(mu) = 3 y_t^4 / (8 pi^2) ln(m_stop / mu) = 6 y_t^4 / (16 pi^2) ln(m_stop / mu)
         = 2 * dlam_L8 (NOT 4 * dlam_L8 as claimed by Producer v2!).
      2. Exact 1-loop matching-scale invariance d/d(ln mu) [lambda_EFT(mu) + Delta lambda(mu)] == 0.
      3. Direct charged+neutral block derivation of Split-SUSY box_ss and gamma_H^SS.
    """
    yt, mQ, mu3, mu, h2 = sp.symbols("yt mQ mu3 mu h2", positive=True)
    # 1-loop CW potential for stop_L (6 real dof) + stop_R (6 real dof) with M^2(h2) = m^2 + yt^2 * h2:
    # V_CW(h2) = (6 / (64 pi^2)) * sum_{m in {mQ, mu3}} M^4 (ln(M^2 / mu^2) - 3/2)
    def cw_block(m_sq):
        m2h = m_sq + (yt ** 2) * h2
        return sp.Rational(6, 64) / (sp.pi ** 2) * (m2h ** 2) * (sp.log(m2h / (mu ** 2)) - sp.Rational(3, 2))

    v_cw = cw_block(mQ ** 2) + cw_block(mu3 ** 2)
    # Coefficient of |H|^4 = h2^2 is (1/2) * d^2 V_CW / d(h2)^2 |_{h2=0}:
    dlam_cw = sp.simplify(sp.Rational(1, 2) * sp.diff(v_cw, h2, 2).subs(h2, 0))
    # Express in terms of m_stop = sqrt(mQ * mu3):
    mstop = sp.Symbol("mstop", positive=True)
    dlam_cw_mstop = sp.simplify(dlam_cw.subs(mu3, (mstop ** 2) / mQ))
    dlam_true_2x = sp.Rational(3, 8) * (yt ** 4) / (sp.pi ** 2) * sp.log(mstop / mu)
    dlam_l8_1x = sp.Rational(3, 16) * (yt ** 4) / (sp.pi ** 2) * sp.log(mstop / mu)
    dlam_prodv2_4x = sp.Rational(3, 4) * (yt ** 4) / (sp.pi ** 2) * sp.log(mstop / mu)

    cw_equals_2x = bool(sp.simplify(dlam_cw_mstop - dlam_true_2x) == 0)
    # Matching-scale invariance test: d(lambda_IR)/d(ln mu) = -beta_lam_EFT^top + mu * d(Delta lambda)/d(mu) == 0!
    # Wait: lambda_EFT(mu_match) = lambda_tree + Delta lambda(mu_match); running down to IR subtracts
    # integral_{mu_IR}^{mu_match} beta_lam_EFT d ln mu, so d(lambda_IR)/d(ln mu_match) = mu d(Delta lam)/d mu - beta_lam_EFT^top!
    beta_lam_top = -sp.Rational(6, 16) * (yt ** 4) / (sp.pi ** 2)
    scale_resid_true_2x = sp.simplify(mu * sp.diff(dlam_true_2x, mu) - beta_lam_top)
    scale_resid_l8_1x = sp.simplify(mu * sp.diff(dlam_l8_1x, mu) - beta_lam_top)
    scale_resid_prodv2_4x = sp.simplify(mu * sp.diff(dlam_prodv2_4x, mu) - beta_lam_top)

    # Disjoint Split-SUSY box_ss verification via direct charged + 2x2 neutralino Yukawa blocks:
    gu, gd, gup, gdp = sp.symbols("gu gd gup gdp", real=True)
    mn = sp.Rational(1, 2) * sp.Matrix([[-gu, gd], [gup, -gdp]])
    # Charged blocks (W^+ H_u^+, W^- H_d^-) each have tr(Y^H Y)^2 = 1/2 g^4 -> -4 * (1/2) = -2 g^4;
    # Neutral block has tr(Y_N^H Y_N)^2 = 2 tr((mn mn^T)^2) -> -4 * 2 = -8 tr((mn mn^T)^2):
    box_derived = sp.expand(-2 * (gu ** 4 + gd ** 4) - 8 * ((mn * mn.T) ** 2).trace())
    box_gr = sp.expand(
        -sp.Rational(5, 2) * (gu ** 4 + gd ** 4) - sp.Rational(1, 2) * (gup ** 4 + gdp ** 4)
        - (gu ** 2) * (gd ** 2) - (gu ** 2) * (gup ** 2) - (gd ** 2) * (gdp ** 2)
        - (gup ** 2) * (gdp ** 2) - 2 * gu * gd * gup * gdp
    )
    box_exact_ok = bool(sp.simplify(box_derived - box_gr) == 0)
    # Higgs anomalous dimension gamma_H^SS = 2 * tr(Y_0^H Y_0) / 2?
    # Charged: |gu|^2 + |gd|^2; Neutral: 2 * tr(mn mn^T) = 1/2 (gu^2 + gd^2 + gup^2 + gdp^2):
    gam_h_derived = sp.expand(gu ** 2 + gd ** 2 + 2 * (mn * mn.T).trace())
    gam_h_gr = sp.Rational(3, 2) * (gu ** 2 + gd ** 2) + sp.Rational(1, 2) * (gup ** 2 + gdp ** 2)
    gam_h_exact_ok = bool(sp.simplify(gam_h_derived - gam_h_gr) == 0)

    return {
        "cw_exact_equals_3_over_8pi2_ln_mstop_over_mu": cw_equals_2x,
        "matching_scale_invar_resid_true_2x_is_zero": bool(scale_resid_true_2x == 0),
        "matching_scale_invar_resid_L8_1x_nonzero": str(scale_resid_l8_1x),
        "matching_scale_invar_resid_ProdV2_4x_nonzero": str(scale_resid_prodv2_4x),
        "split_susy_box_and_gammaH_blocks_exact": bool(box_exact_ok and gam_h_exact_ok),
    }


def run_r_pa2_d(
    prod_v2: dict[str, Any],
    discrepancies: list[dict[str, Any]],
    non_blocking: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 48
    prod_l8 = json.loads(git_bytes(AGY_EXP_REF, "relays/x_floor_link8_verify/verify_x_floor_link8_out.json").decode("utf-8"))
    prod_l7 = json.loads(git_bytes(AGY_EXP_REF, "relays/x_foundations_link7_verify/verify_x_foundations_link7_out.json").decode("utf-8"))
    pd_v2 = prod_v2["PA2_D_agy_exp_block_B2_pmns_racetrack_splitsusy_bp"]

    tau8 = rat_mp(16, 5) + J_MP * rat_mp(8, 5)
    g_k38_coarse = compute_dirac_s12_kutta38(tau8, n_th=10, n_t=12)
    g_k38 = compute_dirac_s12_kutta38(tau8, n_th=12, n_t=14)
    g_k38_conv = max(abs(g_k38[i] - g_k38_coarse[i]) for i in range(3))
    g_peer = [mp.mpf(x) for x in prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["dirac_s12_gramian_tau8"]]
    g_prodv2 = [mp.mpf(x) for x in pd_v2["disjoint_rk4_dirac_gramian"]]
    g_k38_vs_peer = max(abs(g_k38[i] - g_peer[i]) for i in range(3))
    g_k38_vs_prodv2 = max(abs(g_k38[i] - g_prodv2[i]) for i in range(3))

    # Build W_hol purely via mp.jtheta:
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]

    def w_avg(tv: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
        return sum((eval_w_hol_jtheta(tv, a, b, ql, qr) for a, b in pts), mp.zeros(3, 3)) / mp.mpf(len(pts))

    wu = w_avg(tau8, k5, 1, -4)
    wd = (w_avg(tau8, k5, 1, 2) + w_avg(tau8, k6, 1, 2)) / mp.mpf(2)
    we = (w_avg(tau8, k5, -3, 6) + w_avg(tau8, k6, -3, 6)) / mp.mpf(2)
    wnu = (w_avg(tau8, k5, 3, -5) + w_avg(tau8, k6, 3, -5)) / mp.mpf(2)
    wr_raw = (w_avg(tau8, k5, 3, 3) + w_avg(tau8, k6, 3, 3)) / mp.mpf(2)
    wr_sym = (wr_raw + wr_raw.T) / mp.mpf(2)
    _, svr = svd_left_asc(wr_sym)
    mr = mp.eye(3) + wr_sym / svr[2]

    eps5 = mp.exp(mp.mpf(2) * J_MP * mp.pi * tau8 / mp.mpf(5))
    d10 = mp.diag([eps5 ** n for n in (2, 0, 3)])

    def pmns_from_u(u_mat: mp.matrix) -> list[mp.mpf]:
        s13 = abs(u_mat[0, 2]) ** 2
        s12 = (abs(u_mat[0, 1]) ** 2) / (mp.mpf(1) - s13)
        s23 = (abs(u_mat[1, 2]) ** 2) / (mp.mpf(1) - s13)
        return [s12, s23, s13]

    # Completely self-contained Referee Yukawa + Takagi using OUR Kutta-3/8 Gramian g_k38 (ZERO peer JSON input!):
    kis_ref = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_k38])
    yu_ref = kis_ref * d10 * wu * d10 * kis_ref
    yd_ref = kis_ref * d10 * wd * kis_ref
    ye_ref = kis_ref * we * d10 * kis_ref
    ynu_ref = kis_ref * wnu
    mnu_ref = -ynu_ref * (mr ** (-1)) * ynu_ref.T

    _, su_ref = svd_left_asc(yu_ref)
    _, sd_ref = svd_left_asc(yd_ref)
    ue_ref, se_ref = svd_left_asc(ye_ref)
    ut_ref, snu_ref = takagi_real6_eigsy(mnu_ref)
    takagi_resid_ref = max(
        abs((ut_ref * mp.diag(snu_ref) * ut_ref.T - mnu_ref)[i, j])
        for i in range(3) for j in range(3)
    )
    takagi_unit_err = max(
        abs((ut_ref.H * ut_ref - mp.eye(3))[i, j])
        for i in range(3) for j in range(3)
    )
    ang_true_ref = pmns_from_u(ue_ref.H * ut_ref)
    dm_ref = (snu_ref[1] ** 2 - snu_ref[0] ** 2) / (snu_ref[2] ** 2 - snu_ref[0] ** 2)

    # Reconstruct L8_5 broken formula (ue.H * conj(ut)) and V^H-only test on OUR g_k38:
    ut_ref_c = mp.matrix([[mp.conj(ut_ref[r, c]) for c in range(3)] for r in range(3)])
    ang_broken_true_tak = pmns_from_u(ue_ref.H * ut_ref_c)

    u_svd, s_svd, vh_svd = mp.svd_c(mnu_ref)
    oid = sorted(range(3), key=lambda i: s_svd[i])
    us_b = mp.matrix([[u_svd[r, oid[c]] for c in range(3)] for r in range(3)])
    vs_b = mp.matrix([[vh_svd[r, oid[c]] for c in range(3)] for r in range(3)])
    z_b = us_b.T * mp.matrix([[mp.conj(vs_b[r, c]) for c in range(3)] for r in range(3)])
    ut_l8_bug = us_b * mp.diag([mp.exp(-J_MP * mp.arg(z_b[k, k]) / mp.mpf(2)) for k in range(3)])
    ut_l8_bug_c = mp.matrix([[mp.conj(ut_l8_bug[r, c]) for c in range(3)] for r in range(3)])
    ang_l8_repro_ref = pmns_from_u(ue_ref.H * ut_l8_bug_c)
    vh_only_shift = max(abs(ang_broken_true_tak[k] - ang_l8_repro_ref[k]) for k in range(3))

    peer_l8_pmns = [mp.mpf(x) for x in prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]["pmns_s12sq_s23sq_s13sq_dmratio"][:3]]
    prodv2_true_pmns = [mp.mpf(x) for x in pd_v2["catch_FL8_F2_pmns_and_su2L_haar_bug"]["true_gauge_invariant_pmns_s12_s23_s13_dm"]]
    ref_vs_prodv2_true_pmns_diff = max(
        max(abs(ang_true_ref[k] - prodv2_true_pmns[k]) for k in range(3)),
        abs(dm_ref - prodv2_true_pmns[3]),
    )
    ref_vs_peer_l8_broken_diff = max(abs(ang_l8_repro_ref[k] - peer_l8_pmns[k]) for k in range(3))

    # 10-trial TRUE SU(2)_L-covariant Haar scrambling (Mezzadri Householder QR, disjoint seed):
    rng = random.Random(2026112499)
    haar_true_max = mp.mpf(0)
    haar_broken_max = mp.mpf(0)
    for _ in range(10):
        ul, uer, unr = haar_u3_householder(rng), haar_u3_householder(rng), haar_u3_householder(rng)
        ye_s = ul * ye_ref * uer.H
        ynu_s = ul * ynu_ref * unr
        mr_s = unr.T * mr * unr
        ue_s, _ = svd_left_asc(ye_s)
        mnu_s = -ynu_s * (mr_s ** (-1)) * ynu_s.T
        ut_s, _ = takagi_real6_eigsy(mnu_s)
        ut_sc = mp.matrix([[mp.conj(ut_s[r, c]) for c in range(3)] for r in range(3)])
        a_tr = pmns_from_u(ue_s.H * ut_s)
        a_br = pmns_from_u(ue_s.H * ut_sc)
        haar_true_max = max(haar_true_max, *(abs(a_tr[k] - ang_true_ref[k]) for k in range(3)))
        haar_broken_max = max(haar_broken_max, *(abs(a_br[k] - ang_broken_true_tak[k]) for k in range(3)))

    # FL8-F5: Mirror + CPT invariance on flat [1,1,1] and curved g_k38, plus sign of YB_proxy(tau_8^+):
    def eval_mirror_cpt(g_vec: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        ki = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_vec])

        def one_side(tv: mp.mpc, mirror_flag: bool) -> tuple[mp.mpf, mp.mpf]:
            k5u = [(-a, b) for a, b in k5] if mirror_flag else k5
            k6u = [(-a, b) for a, b in k6] if mirror_flag else k6
            wu_l = w_avg(tv, k5u, 1, -4)
            wd_l = (w_avg(tv, k5u, 1, 2) + w_avg(tv, k6u, 1, 2)) / mp.mpf(2)
            wnu_l = (w_avg(tv, k5u, 3, -5) + w_avg(tv, k6u, 3, -5)) / mp.mpf(2)
            wr_l = (w_avg(tv, k5u, 3, 3) + w_avg(tv, k6u, 3, 3)) / mp.mpf(2)
            wr_sl = (wr_l + wr_l.T) / mp.mpf(2)
            _, svr_l = svd_left_asc(wr_sl)
            mr_l = mp.eye(3) + wr_sl / svr_l[2]
            e5 = mp.exp(mp.mpf(2) * J_MP * mp.pi * tv / mp.mpf(5))
            d10_l = mp.diag([e5 ** n for n in (2, 0, 3)])
            yu_l, yd_l, ynu_l = ki * d10_l * wu_l * d10_l * ki, ki * d10_l * wd_l * ki, ki * wnu_l
            hu_l, hd_l = yu_l * yu_l.H, yd_l * yd_l.H
            cm = hu_l * hd_l - hd_l * hu_l
            cm3 = cm * cm * cm
            jdet = mp.im((cm3[0, 0] + cm3[1, 1] + cm3[2, 2]) / mp.mpf(6))
            ut_r, smr = takagi_real6_eigsy(mr_l)
            ut_rc = mp.matrix([[mp.conj(ut_r[r, c]) for c in range(3)] for r in range(3)])
            yn_m = ynu_l * ut_rc
            hn = yn_m.H * yn_m
            e1 = mp.mpf(0)
            for j in (1, 2):
                xv = (smr[j] / smr[0]) ** 2
                fl = mp.sqrt(xv) * (mp.mpf(1) - (mp.mpf(1) + xv) * mp.log((mp.mpf(1) + xv) / xv) + mp.mpf(1) / (mp.mpf(1) - xv))
                e1 += -(mp.mpf(1) / (mp.mpf(8) * mp.pi * mp.re(hn[0, 0]))) * mp.im(hn[0, j] ** 2) * fl
            return jdet, -e1

        jp, ybp = one_side(tau8, False)
        jm, ybm = one_side(-rat_mp(16, 5) + J_MP * rat_mp(8, 5), True)
        return ybp, abs(ybp + ybm), abs((jp / ybp) - (jm / ybm))

    ybp_flat, yb_sum_flat, j_yb_diff_flat = eval_mirror_cpt([mp.mpf(1), mp.mpf(1), mp.mpf(1)])
    ybp_curv, yb_sum_curv, j_yb_diff_curv = eval_mirror_cpt(g_k38)
    peer_l7_yb = mp.mpf(prod_l7["modules"]["F7_2"]["YB_proxy_tau8_pos"])

    # FL8-F4: Polonyi racetrack via bisection/secant (disjoint from anderson solver):
    with mp.workdps(60):
        p1, p2 = mp.pi / mp.mpf(2), mp.mpf(2) * mp.pi / mp.mpf(5)

        def df_rt(s: mp.mpf, c1: int, c2: int) -> mp.mpf:
            u = mp.mpf(3) * s
            e1 = mp.mpf(c1) * mp.exp(-p1 * u)
            e2 = mp.mpf(c2) * mp.exp(-p2 * u)
            w = e1 - e2
            wu = -p1 * e1 + p2 * e2
            wuu = p1 * p1 * e1 - p2 * p2 * e2
            a = mp.mpf(2) * s * wu - w
            da = mp.mpf(6) * s * wuu - wu
            return mp.mpf(2) * a * da - mp.mpf(6) * w * wu

        # Pure bisection + Newton polish:
        lo, hi = rat_mp(600, 100), rat_mp(610, 100)
        flo = df_rt(lo, 240, 1)
        for _ in range(180):
            mid = (lo + hi) / mp.mpf(2)
            fmid = df_rt(mid, 240, 1)
            if (flo > 0 and fmid > 0) or (flo < 0 and fmid < 0):
                lo, flo = mid, fmid
            else:
                hi = mid
        s_star = (lo + hi) / mp.mpf(2)
        t_star = mp.mpf(2) * s_star
        u_star = mp.mpf(3) * s_star
        w_star = mp.mpf(240) * mp.exp(-p1 * u_star) - mp.exp(-p2 * u_star)
        wu_star = -p1 * mp.mpf(240) * mp.exp(-p1 * u_star) + p2 * mp.exp(-p2 * u_star)
        z_e = rat_mp(1, 2) + J_MP * mp.sqrt(mp.mpf(3)) / mp.mpf(2)
        # Disjoint eta(z_e) via mp.jtheta identity eta(tau)^3 = (1/2) t2 * t3 * t4:
        qe_half = mp.exp(J_MP * mp.pi * z_e)
        eta3_abs = abs(mp.jtheta(2, 0, qe_half) * mp.jtheta(3, 0, qe_half) * mp.jtheta(4, 0, qe_half)) / mp.mpf(2)
        eta4_abs = eta3_abs ** rat_mp(4, 3)
        inv_eis = mp.mpf(1) / (mp.mpf(2) * mp.im(z_e) * eta4_abs)
        m32_mpl = mp.sqrt(inv_eis / (mp.mpf(8) * s_star * (t_star ** 2))) * abs(w_star)
        m0_ov = mp.mpf(2) * (mp.mpf(2) * s_star * wu_star - w_star) / w_star
        agut_inv = mp.mpf(5) * s_star
        g0 = mp.sqrt(mp.mpf(4) * mp.pi / agut_inv)
        yt0 = g0 / mp.sqrt(mp.mpf(2))
        t_susy = mp.log(m32_mpl * mp.sqrt(mp.mpf(8) * s_star * (t_star ** 2)))
        sym45_s = mp.log(rat_mp(4, 5)) / (mp.mpf(3) * (p1 - p2))
        sym54_s = mp.log(rat_mp(5, 4)) / (mp.mpf(3) * (p1 - p2))
        sym54_agut = mp.mpf(5) * sym54_s

    peer_agut = mp.mpf(prod_l7["modules"]["F7_4"]["alpha_GUT_inv_derived"])
    peer_m0 = mp.mpf(prod_l7["modules"]["F7_4"]["M0_tree_over_m32_derived"])
    rt_diffs = [abs(agut_inv - peer_agut), abs(m0_ov - peer_m0)]

    # Exact SymPy proof of stop threshold & Split-SUSY blocks:
    sympy_stop_proof = prove_stop_threshold_and_split_susy_sympy()

    # Classical Kutta-3/8 ODE systems:
    def mssm_gam(g1, g2, g3, yt, yb, yl):
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
        return [
            mp.mpf(3) * yt2 - rat_mp(3, 2) * g22 - rat_mp(3, 10) * g12,
            mp.mpf(3) * yb2 + yl2 - rat_mp(3, 2) * g22 - rat_mp(3, 10) * g12,
            yt2 + yb2 - rat_mp(8, 3) * g32 - rat_mp(3, 2) * g22 - rat_mp(1, 30) * g12,
            mp.mpf(2) * yt2 - rat_mp(8, 3) * g32 - rat_mp(8, 15) * g12,
            mp.mpf(2) * yb2 - rat_mp(8, 3) * g32 - rat_mp(2, 15) * g12,
            yl2 - rat_mp(3, 2) * g22 - rat_mp(3, 10) * g12,
            mp.mpf(2) * yl2 - rat_mp(6, 5) * g12,
            -rat_mp(8, 3) * g32 - rat_mp(3, 2) * g22 - rat_mp(1, 30) * g12,
            -rat_mp(8, 3) * g32 - rat_mp(8, 15) * g12,
            -rat_mp(8, 3) * g32 - rat_mp(2, 15) * g12,
            -rat_mp(3, 2) * g22 - rat_mp(3, 10) * g12,
            -rat_mp(6, 5) * g12,
        ]

    def mssm24_rhs(_t: mp.mpf, y: list[mp.mpf]) -> list[mp.mpf]:
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        g1, g2, g3, yt, yb, yl, m1, m2, m3, at, ab, al = y[:12]
        mhu, mhd, mq3, mu3, md3, ml3, me3, mq1, mu1, md1, ml1, me1 = y[12:]
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
        m12, m22, m32 = m1 * m1, m2 * m2, m3 * m3
        gm = mssm_gam(g1, g2, g3, yt, yb, yl)
        xt = mp.mpf(2) * yt2 * (mhu + mq3 + mu3 + at * at)
        xb = mp.mpf(2) * yb2 * (mhd + mq3 + md3 + ab * ab)
        xl = mp.mpf(2) * yl2 * (mhd + ml3 + me3 + al * al)
        sy = mhu - mhd + (mq3 - ml3 - mp.mpf(2) * mu3 + md3 + me3) + mp.mpf(2) * (mq1 - ml1 - mp.mpf(2) * mu1 + md1 + me1)
        return [
            k1 * rat_mp(33, 5) * g12 * g1, k1 * g22 * g2, -k1 * mp.mpf(3) * g32 * g3,
            k1 * yt * (gm[0] + gm[2] + gm[3]), k1 * yb * (gm[1] + gm[2] + gm[4]), k1 * yl * (gm[1] + gm[5] + gm[6]),
            k1 * rat_mp(66, 5) * g12 * m1, k1 * mp.mpf(2) * g22 * m2, -k1 * mp.mpf(6) * g32 * m3,
            k1 * (mp.mpf(12) * yt2 * at + mp.mpf(2) * yb2 * ab + rat_mp(32, 3) * g32 * m3 + mp.mpf(6) * g22 * m2 + rat_mp(26, 15) * g12 * m1),
            k1 * (mp.mpf(12) * yb2 * ab + mp.mpf(2) * yt2 * at + mp.mpf(2) * yl2 * al + rat_mp(32, 3) * g32 * m3 + mp.mpf(6) * g22 * m2 + rat_mp(14, 15) * g12 * m1),
            k1 * (mp.mpf(8) * yl2 * al + mp.mpf(6) * yb2 * ab + mp.mpf(6) * g22 * m2 + rat_mp(18, 5) * g12 * m1),
            k1 * (mp.mpf(3) * xt - mp.mpf(6) * g22 * m22 - rat_mp(6, 5) * g12 * m12 + rat_mp(3, 5) * g12 * sy),
            k1 * (mp.mpf(3) * xb + xl - mp.mpf(6) * g22 * m22 - rat_mp(6, 5) * g12 * m12 - rat_mp(3, 5) * g12 * sy),
            k1 * (xt + xb - rat_mp(32, 3) * g32 * m32 - mp.mpf(6) * g22 * m22 - rat_mp(2, 15) * g12 * m12 + rat_mp(1, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xt - rat_mp(32, 3) * g32 * m32 - rat_mp(32, 15) * g12 * m12 - rat_mp(4, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xb - rat_mp(32, 3) * g32 * m32 - rat_mp(8, 15) * g12 * m12 + rat_mp(2, 5) * g12 * sy),
            k1 * (xl - mp.mpf(6) * g22 * m22 - rat_mp(6, 5) * g12 * m12 - rat_mp(3, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xl - rat_mp(24, 5) * g12 * m12 + rat_mp(6, 5) * g12 * sy),
            k1 * (-rat_mp(32, 3) * g32 * m32 - mp.mpf(6) * g22 * m22 - rat_mp(2, 15) * g12 * m12 + rat_mp(1, 5) * g12 * sy),
            k1 * (-rat_mp(32, 3) * g32 * m32 - rat_mp(32, 15) * g12 * m12 - rat_mp(4, 5) * g12 * sy),
            k1 * (-rat_mp(32, 3) * g32 * m32 - rat_mp(8, 15) * g12 * m12 + rat_mp(2, 5) * g12 * sy),
            k1 * (-mp.mpf(6) * g22 * m22 - rat_mp(6, 5) * g12 * m12 - rat_mp(3, 5) * g12 * sy),
            k1 * (-rat_mp(24, 5) * g12 * m12 + rat_mp(6, 5) * g12 * sy),
        ]

    def am_soft_analytic(g1, g2, g3, yt, yb, yl) -> list[mp.mpf]:
        """Exact analytic chain-rule anomaly-mediated soft terms (disjoint from finite-diff)."""
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        gm = mssm_gam(g1, g2, g3, yt, yb, yl)
        dg1, dg2, dg3, dyt, dyb, dyl = mssm24_rhs(mp.mpf(0), [g1, g2, g3, yt, yb, yl] + [mp.mpf(0)] * 18)[:6]
        # d(g^2)/dt = 2 g dg, d(y^2)/dt = 2 y dy:
        dg12, dg22, dg32 = mp.mpf(2) * g1 * dg1, mp.mpf(2) * g2 * dg2, mp.mpf(2) * g3 * dg3
        dyt2, dyb2, dyl2 = mp.mpf(2) * yt * dyt, mp.mpf(2) * yb * dyb, mp.mpf(2) * yl * dyl
        dgm = [
            mp.mpf(3) * dyt2 - rat_mp(3, 2) * dg22 - rat_mp(3, 10) * dg12,
            mp.mpf(3) * dyb2 + dyl2 - rat_mp(3, 2) * dg22 - rat_mp(3, 10) * dg12,
            dyt2 + dyb2 - rat_mp(8, 3) * dg32 - rat_mp(3, 2) * dg22 - rat_mp(1, 30) * dg12,
            mp.mpf(2) * dyt2 - rat_mp(8, 3) * dg32 - rat_mp(8, 15) * dg12,
            mp.mpf(2) * dyb2 - rat_mp(8, 3) * dg32 - rat_mp(2, 15) * dg12,
            dyl2 - rat_mp(3, 2) * dg22 - rat_mp(3, 10) * dg12,
            mp.mpf(2) * dyl2 - rat_mp(6, 5) * dg12,
            -rat_mp(8, 3) * dg32 - rat_mp(3, 2) * dg22 - rat_mp(1, 30) * dg12,
            -rat_mp(8, 3) * dg32 - rat_mp(8, 15) * dg12,
            -rat_mp(8, 3) * dg32 - rat_mp(2, 15) * dg12,
            -rat_mp(3, 2) * dg22 - rat_mp(3, 10) * dg12,
            -rat_mp(6, 5) * dg12,
        ]
        return [
            k1 * rat_mp(33, 5) * g1 * g1, k1 * g2 * g2, -k1 * mp.mpf(3) * g3 * g3,
            -k1 * (gm[0] + gm[2] + gm[3]), -k1 * (gm[1] + gm[2] + gm[4]), -k1 * (gm[1] + gm[5] + gm[6]),
        ] + [rat_mp(1, 2) * k1 * dgm[i] for i in range(12)]

    # Guardrail-4 benchmarks via Kutta-3/8 2-level Richardson:
    guv_jj = [rat_mp(7, 10), rat_mp(7, 10), rat_mp(7, 10), rat_mp(1, 2), rat_mp(1, 10), rat_mp(1, 12)]
    y_jj = kutta38_rich2(mssm24_rhs, guv_jj + am_soft_analytic(*guv_jj), mp.mpf(0), mp.mpf(-25), 140)
    s_jj = am_soft_analytic(*y_jj[:6])
    jj_k38_err = max(abs(y_jj[6 + k] - s_jj[k]) for k in range(18))

    gfmm = [rat_mp(7, 10), rat_mp(7, 10), rat_mp(7, 10), rat_mp(3, 5), mp.mpf(0), mp.mpf(0)]
    y_fmm = kutta38_rich2(mssm24_rhs, gfmm + [mp.mpf(0)] * 6 + [mp.mpf(1)] * 12, mp.mpf(0), mp.mpf(-30), 80)
    fmm_k38_err = abs((y_fmm[12] - rat_mp(1, 2) * (y_fmm[12] + y_fmm[14] + y_fmm[15])) + rat_mp(1, 2))

    # Run complete MSSM -> Split-SUSY -> SM trajectory purely from OUR Kutta-3/8 Gramian g_k38!
    eps5_sq = abs(eps5) ** 2
    yb0_ref = yt0 * eps5_sq * (sd_ref[2] / su_ref[2])
    ytau0_ref = yt0 * eps5_sq * (se_ref[2] / su_ref[2])
    am0_ref = am_soft_analytic(g0, g0, g0, yt0, yb0_ref, ytau0_ref)
    y0_ref = (
        [g0, g0, g0, yt0, yb0_ref, ytau0_ref]
        + [m0_ov + am0_ref[k] for k in range(3)]
        + [-m0_ov + am0_ref[3 + k] for k in range(3)]
        + [mp.mpf(1) + am0_ref[6 + k] for k in range(12)]
    )
    ypev = kutta38_rich2(mssm24_rhs, y0_ref, mp.mpf(0), t_susy, 120)
    ch_crit_ref = mp.sqrt(ypev[12] * ypev[13])
    tanb_ref = mp.sqrt(ypev[13] / ypev[12])
    sb = tanb_ref / mp.sqrt(mp.mpf(1) + tanb_ref * tanb_ref)
    cb = mp.mpf(1) / mp.sqrt(mp.mpf(1) + tanb_ref * tanb_ref)
    c2b = cb * cb - sb * sb
    yt_sm0, yb_sm0, yl_sm0 = ypev[3] * sb, ypev[4] * cb, ypev[5] * cb
    mstop_ov = (ypev[14] * ypev[15]) ** rat_mp(1, 4)

    def sm7_rhs(b_g: tuple[mp.mpf, mp.mpf, mp.mpf]):
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))

        def _f(_t: mp.mpf, st: list[mp.mpf]) -> list[mp.mpf]:
            g1, g2, g3, yt, yb, yl, lb = st
            g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
            yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
            tr = mp.mpf(3) * yt2 + mp.mpf(3) * yb2 + yl2
            return [
                k1 * b_g[0] * g12 * g1, k1 * b_g[1] * g22 * g2, k1 * b_g[2] * g32 * g3,
                k1 * yt * (tr + rat_mp(3, 2) * (yt2 - yb2) - mp.mpf(8) * g32 - rat_mp(9, 4) * g22 - rat_mp(17, 20) * g12),
                k1 * yb * (tr + rat_mp(3, 2) * (yb2 - yt2) - mp.mpf(8) * g32 - rat_mp(9, 4) * g22 - rat_mp(1, 4) * g12),
                k1 * yl * (tr + rat_mp(3, 2) * yl2 - rat_mp(9, 4) * g22 - rat_mp(9, 4) * g12),
                k1 * (
                    mp.mpf(24) * lb * lb + mp.mpf(4) * lb * tr
                    - mp.mpf(2) * (mp.mpf(3) * yt2 * yt2 + mp.mpf(3) * yb2 * yb2 + yl2 * yl2)
                    - mp.mpf(3) * lb * (mp.mpf(3) * g22 + rat_mp(3, 5) * g12)
                    + rat_mp(3, 8) * (mp.mpf(2) * g22 * g22 + (g22 + rat_mp(3, 5) * g12) ** 2)
                ),
            ]
        return _f

    def split11_rhs(_t: mp.mpf, st: list[mp.mpf]) -> list[mp.mpf]:
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        g1, g2, g3, yt, yb, yl, lb, gu, gd, gup, gdp = st
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        gp2 = rat_mp(3, 5) * g12
        yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
        gu2, gd2, gup2, gdp2 = gu * gu, gd * gd, gup * gup, gdp * gdp
        tr_y = mp.mpf(3) * yt2 + mp.mpf(3) * yb2 + yl2
        gam_h = rat_mp(3, 2) * (gu2 + gd2) + rat_mp(1, 2) * (gup2 + gdp2)
        box_ss = (
            -rat_mp(5, 2) * (gu2 * gu2 + gd2 * gd2) - rat_mp(1, 2) * (gup2 * gup2 + gdp2 * gdp2)
            - gu2 * gd2 - gu2 * gup2 - gd2 * gdp2 - gup2 * gdp2 - mp.mpf(2) * gu * gd * gup * gdp
        )
        return [
            k1 * rat_mp(9, 2) * g12 * g1, k1 * (-rat_mp(7, 6)) * g22 * g2, k1 * (-mp.mpf(5)) * g32 * g3,
            k1 * yt * (tr_y + gam_h + rat_mp(3, 2) * (yt2 - yb2) - mp.mpf(8) * g32 - rat_mp(9, 4) * g22 - rat_mp(17, 20) * g12),
            k1 * yb * (tr_y + gam_h + rat_mp(3, 2) * (yb2 - yt2) - mp.mpf(8) * g32 - rat_mp(9, 4) * g22 - rat_mp(1, 4) * g12),
            k1 * yl * (tr_y + gam_h + rat_mp(3, 2) * yl2 - rat_mp(9, 4) * g22 - rat_mp(9, 4) * g12),
            k1 * (
                mp.mpf(24) * lb * lb + mp.mpf(4) * lb * (tr_y + gam_h) + box_ss
                - mp.mpf(2) * (mp.mpf(3) * yt2 * yt2 + mp.mpf(3) * yb2 * yb2 + yl2 * yl2)
                - mp.mpf(3) * lb * (mp.mpf(3) * g22 + gp2)
                + rat_mp(3, 8) * (mp.mpf(2) * g22 * g22 + (g22 + gp2) ** 2)
            ),
            k1 * (gu * (-rat_mp(33, 4) * g22 - rat_mp(3, 4) * gp2 + tr_y + rat_mp(11, 4) * gu2 + gd2 + rat_mp(3, 4) * gup2 + rat_mp(1, 2) * gdp2) + gd * gdp * gup),
            k1 * (gd * (-rat_mp(33, 4) * g22 - rat_mp(3, 4) * gp2 + tr_y + rat_mp(11, 4) * gd2 + gu2 + rat_mp(3, 4) * gdp2 + rat_mp(1, 2) * gup2) + gu * gup * gdp),
            k1 * (gup * (-rat_mp(9, 4) * g22 - rat_mp(3, 4) * gp2 + tr_y + rat_mp(5, 4) * gup2 + mp.mpf(2) * gdp2 + rat_mp(9, 4) * gu2 + rat_mp(3, 2) * gd2) + mp.mpf(3) * gd * gdp * gu),
            k1 * (gdp * (-rat_mp(9, 4) * g22 - rat_mp(3, 4) * gp2 + tr_y + rat_mp(5, 4) * gdp2 + mp.mpf(2) * gup2 + rat_mp(9, 4) * gd2 + rat_mp(3, 2) * gu2) + mp.mpf(3) * gu * gup * gd),
        ]

    dt_split = mp.log(abs(m0_ov))
    lam_tree = ((ypev[1] ** 2 + rat_mp(3, 5) * (ypev[0] ** 2)) / mp.mpf(8)) * (c2b ** 2)
    dlam_l8 = (mp.mpf(3) * (yt_sm0 ** 4)) / (mp.mpf(16) * (mp.pi ** 2)) * mp.log(mstop_ov)
    dlam_true_2x = mp.mpf(2) * dlam_l8  # Exact 3/(8 pi^2) ln(m_stop / m_{3/2}) = 6/(16 pi^2) ln(...)
    dlam_prodv2_4x = mp.mpf(4) * dlam_l8  # Producer v2's overcorrected 3/(4 pi^2) ln(...)

    b_ss = (rat_mp(9, 2), -rat_mp(7, 6), mp.mpf(-5))
    b_nohino = (rat_mp(41, 10), -rat_mp(11, 6), mp.mpf(-5))
    b_sm = (rat_mp(41, 10), -rat_mp(19, 6), mp.mpf(-7))
    gp0 = mp.sqrt(rat_mp(3, 5)) * ypev[0]

    st_l8_m0 = kutta38_rich2(sm7_rhs(b_ss), [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_l8], mp.mpf(0), dt_split, 60)
    st_true2x_m0 = kutta38_rich2(
        split11_rhs,
        [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_true_2x, ypev[1] * sb, ypev[1] * cb, gp0 * sb, gp0 * cb],
        mp.mpf(0), dt_split, 60,
    )[:7]
    st_diag4x_m0 = kutta38_rich2(
        split11_rhs,
        [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_prodv2_4x, ypev[1] * sb, ypev[1] * cb, gp0 * sb, gp0 * cb],
        mp.mpf(0), dt_split, 60,
    )[:7]
    st_nohino_true2x_m0 = kutta38_rich2(sm7_rhs(b_nohino), [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_true_2x], mp.mpf(0), dt_split, 60)

    mh_table: dict[str, Any] = {}
    max_diag4x_vs_prodv2 = mp.mpf(0)
    max_l8raw_vs_prodv2 = mp.mpf(0)
    max_true2x_vs_prodv2 = mp.mpf(0)
    prodv2_mh_tab = pd_v2["catch_FL8_F4_racetrack_and_split_susy_rge"]["mh_over_v_L8_vs_complete_SplitSUSY_GR"]

    for dti in (-3, -4, -5):
        ir_l8 = kutta38_rich2(sm7_rhs(b_sm), st_l8_m0, mp.mpf(0), mp.mpf(dti), 60)
        ir_true2x = kutta38_rich2(sm7_rhs(b_sm), st_true2x_m0, mp.mpf(0), mp.mpf(dti), 60)
        ir_diag4x = kutta38_rich2(sm7_rhs(b_sm), st_diag4x_m0, mp.mpf(0), mp.mpf(dti), 60)
        ir_nh2x = kutta38_rich2(sm7_rhs(b_sm), st_nohino_true2x_m0, mp.mpf(0), mp.mpf(dti), 60)
        mh_l8 = mp.sqrt(mp.mpf(2) * ir_l8[6])
        mh_t2 = mp.sqrt(mp.mpf(2) * ir_true2x[6])
        mh_d4 = mp.sqrt(mp.mpf(2) * ir_diag4x[6])
        mh_nh = mp.sqrt(mp.mpf(2) * ir_nh2x[6])

        pv_row = prodv2_mh_tab[f"dt_SM_{dti}"]
        pv_l8 = mp.mpf(pv_row["mh_over_v_L8_raw_repro"])
        pv_gr4x = mp.mpf(pv_row["mh_over_v_complete_SplitSUSY_GR"])
        max_l8raw_vs_prodv2 = max(max_l8raw_vs_prodv2, abs(mh_l8 - pv_l8))
        max_diag4x_vs_prodv2 = max(max_diag4x_vs_prodv2, abs(mh_d4 - pv_gr4x))
        max_true2x_vs_prodv2 = max(max_true2x_vs_prodv2, abs(mh_t2 - pv_gr4x))

        mh_table[f"dt_SM_{dti}"] = {
            "mh_over_v_L8_raw_kutta38": mp.nstr(mh_l8, 10),
            "mh_over_v_true_2x_SplitSUSY_GR": mp.nstr(mh_t2, 10),
            "mh_over_v_true_2x_heavy_higgsinos_decoupled": mp.nstr(mh_nh, 10),
            "mh_over_v_diag_4x_matching_ProdV2": mp.nstr(mh_d4, 10),
            "prod_v2_reported_4x_SplitSUSY_GR": pv_row["mh_over_v_complete_SplitSUSY_GR"],
            "abs_diff_diag4x_vs_ProdV2": mp.nstr(abs(mh_d4 - pv_gr4x), 6),
            "abs_diff_true2x_vs_ProdV2": mp.nstr(abs(mh_t2 - pv_gr4x), 6),
            "rel_shift_true2x_vs_L8": mp.nstr((mh_t2 - mh_l8) / mh_l8, 6),
        }

    # Record DISC-PA2-2: Producer v2's 4x vs exact 2x 1-loop stop threshold error!
    prod_v2_dlam_claimed = mp.mpf(pd_v2["catch_FL8_F4_racetrack_and_split_susy_rge"]["stop_threshold_L8_vs_exact_4x"][1])
    if abs(prod_v2_dlam_claimed - dlam_true_2x) / abs(dlam_true_2x) > rat_mp(1, 10):
        discrepancies.append({
            "id": "DISC-PA2-2",
            "block": "PA2-D (and propagated to PA2-F table)",
            "severity": "REAL_DISCREPANCY",
            "location": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py:1484 (and Scope Card line 36)",
            "producer_claim": (
                f"Claimed exact 1-loop stop threshold in V = lambda |H|^4 (m_h^2 = 2 lambda v^2) is "
                f"dlam_exact = 4 * dlam_l8 = 3 y_t^4 / (4 pi^2) ln(m_stop / m_32) = {mp.nstr(prod_v2_dlam_claimed, 8)}, "
                f"yielding mh/v(dt_SM=-4) = {prodv2_mh_tab['dt_SM_-4']['mh_over_v_complete_SplitSUSY_GR']}."
            ),
            "referee_finding": (
                f"Factor-of-2 convention mix-up: 3/(4 pi^2) ln(m_stop/mu) belongs to V = (lambda/2) |H|^4 (m_h^2 = lambda v^2). "
                f"In Producer v2's SM convention V = lambda |H|^4 (m_h^2 = 2 lambda v^2, beta_lam^top = -6 y_t^4 / (16 pi^2)), "
                f"exact 1-loop Coleman-Weinberg AND 1-loop matching-scale invariance d(lam_IR)/d(ln mu_match) == 0 uniquely require "
                f"Delta lambda_std = 3 y_t^4 / (8 pi^2) ln(m_stop / m_32) = 2 * dlam_l8 = {mp.nstr(dlam_true_2x, 8)} (NOT 4x!). "
                f"L8_5 (3/(16 pi^2)) was too small by 2x; Producer v2 (3/(4 pi^2)) overcorrected by 2x, shifting mh/v down by "
                f"~{mp.nstr(max_true2x_vs_prodv2, 5)} across dt_SM in {{-3,-4,-5}} "
                f"(true 2x mh/v at dt_SM=-3,-4,-5: {mh_table['dt_SM_-3']['mh_over_v_true_2x_SplitSUSY_GR']}, "
                f"{mh_table['dt_SM_-4']['mh_over_v_true_2x_SplitSUSY_GR']}, {mh_table['dt_SM_-5']['mh_over_v_true_2x_SplitSUSY_GR']}). "
                f"When given Producer v2's 4x formula, disjoint Kutta-3/8 matches Producer v2's GL4 to {mp.nstr(max_diag4x_vs_prodv2, 5)}, "
                f"proving the discrepancy is purely the 2x analytic formula error."
            ),
        })

    # Non-blocking diagnostic NBD-1: Producer v2 used g_peer in line 1194 kis instead of g_rk4:
    non_blocking.append({
        "id": "NBD-PA2-1",
        "block": "PA2-D",
        "location": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py:1194",
        "summary": (
            f"Producer v2 imported g_peer from peer L8 JSON into kis for ang_true/yb0/ytau0 (while separately cross-checking g_rk4 "
            f"vs g_peer to 5.71e-6). Referee ran 100% self-contained Kutta-3/8 Dirac Gramian g_k38 (n_th=12, n_t=14; internal conv "
            f"{mp.nstr(g_k38_conv, 5)}, diff vs peer {mp.nstr(g_k38_vs_peer, 5)}) through the entire W_hol -> Takagi -> RGE pipeline; "
            f"max drift on true PMNS is {mp.nstr(ref_vs_prodv2_true_pmns_diff, 5)} and on L8_5 raw mh/v is {mp.nstr(max_l8raw_vs_prodv2, 5)}."
        ),
    })

    # FL8-F6: CY_4 r=8 BP spacing and 129-decade Shannon bit cost:
    ek_star = inv_eis / (mp.mpf(8) * s_star * (t_star ** 2))
    h11_8 = 11
    chi_8 = 288 + 2160
    tau_8 = 32 + chi_8 // 3
    b4p_8 = ((chi_8 - 2 - 2 * h11_8) + tau_8) // 2
    kfth_8 = mp.mpf(b4p_8 - h11_8 - 1)
    rsq_8 = rat_mp(chi_8, 12)
    bp_log10_r8 = mp.log10(ek_star * rsq_8) - ((kfth_8 / mp.mpf(2)) * mp.log10(mp.pi * rsq_8) - mp.log10(mp.gamma(kfth_8 / mp.mpf(2) + mp.mpf(1))))
    shannon_bits_129 = mp.mpf(129) * mp.log(mp.mpf(10)) / mp.log(mp.mpf(2))
    bp_vs_prodv2 = abs(bp_log10_r8 - mp.mpf(pd_v2["catch_FL8_F6_bp_shannon_bit_floor_contradiction"]["worst_case_r8_bp_log10_spacing_verified"]))
    bits_vs_prodv2 = abs(shannon_bits_129 - mp.mpf(pd_v2["catch_FL8_F6_bp_shannon_bit_floor_contradiction"]["shannon_bits_for_10e129_flux_window"]))

    b203 = prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]
    ch_diff_peer = abs(ch_crit_ref - mp.mpf(b203["giudice_masiero_cH_crit"]))
    tb_diff_peer = abs(tanb_ref - mp.mpf(b203["derived_tan_beta"]))

    # RPF4: Haar break on broken ue^H conj(ut), true pass, matching-scale invariance catches BOTH 1x and 4x, wrong RGE dir +t_SUSY:
    y_wrong_dir = kutta38_integrate(mssm24_rhs, y0_ref, mp.mpf(0), -t_susy, 80)
    rpf4_caught = bool(
        haar_true_max < p10_mp(-35)
        and haar_broken_max > rat_mp(1, 10)
        and vh_only_shift < p10_mp(-35)
        and sympy_stop_proof["matching_scale_invar_resid_true_2x_is_zero"]
        and sympy_stop_proof["matching_scale_invar_resid_L8_1x_nonzero"] != "0"
        and sympy_stop_proof["matching_scale_invar_resid_ProdV2_4x_nonzero"] != "0"
        and y_wrong_dir[12] > mp.mpf(1)
    )

    internal_ok = bool(
        g_k38_conv < p10_mp(-4)
        and g_k38_vs_peer < p10_mp(-4)
        and takagi_resid_ref < p10_mp(-40)
        and takagi_unit_err < p10_mp(-40)
        and ref_vs_prodv2_true_pmns_diff < p10_mp(-5)
        and ref_vs_peer_l8_broken_diff < p10_mp(-5)
        and vh_only_shift < p10_mp(-35)
        and yb_sum_flat < p10_mp(-40) and j_yb_diff_flat < p10_mp(-40)
        and yb_sum_curv < p10_mp(-40) and j_yb_diff_curv < p10_mp(-40)
        and ybp_flat < mp.mpf(0) and peer_l7_yb < mp.mpf(0)
        and max(rt_diffs) < p10_mp(-16)
        and sym45_s < mp.mpf(0)
        and sympy_stop_proof["cw_exact_equals_3_over_8pi2_ln_mstop_over_mu"]
        and sympy_stop_proof["split_susy_box_and_gammaH_blocks_exact"]
        and jj_k38_err < p10_mp(-14)
        and fmm_k38_err < p10_mp(-35)
        and ch_diff_peer < p10_mp(-5)
        and tb_diff_peer < p10_mp(-5)
        and max_l8raw_vs_prodv2 < p10_mp(-5)
        and max_diag4x_vs_prodv2 < p10_mp(-5)
        and bp_vs_prodv2 < p10_mp(-5)
        and bits_vs_prodv2 < p10_mp(-5)
        and rpf4_caught
    )
    return {
        "kutta38_dirac_gramian_n12_n14": [mp.nstr(x, 10) for x in g_k38],
        "kutta38_internal_conv_n10n12_vs_n12n14": mp.nstr(g_k38_conv, 6),
        "kutta38_vs_peer_and_prodv2_gramian_diffs": [mp.nstr(g_k38_vs_peer, 6), mp.nstr(g_k38_vs_prodv2, 6)],
        "FL8_F2_real6_eigsy_takagi_and_SU2L_haar": {
            "takagi_real6_residual": mp.nstr(takagi_resid_ref, 6),
            "takagi_real6_unitarity_err": mp.nstr(takagi_unit_err, 6),
            "true_pmns_s12_s23_s13_dm_from_g_k38": [mp.nstr(x, 8) for x in ang_true_ref] + [mp.nstr(dm_ref, 8)],
            "max_diff_vs_prodv2_true_pmns": mp.nstr(ref_vs_prodv2_true_pmns_diff, 6),
            "true_SU2L_10trial_haar_err": mp.nstr(haar_true_max, 8),
            "L8_broken_ueH_conj_ut_repro": [mp.nstr(x, 8) for x in ang_l8_repro_ref],
            "L8_broken_vs_peer_json_diff": mp.nstr(ref_vs_peer_l8_broken_diff, 6),
            "L8_broken_true_SU2L_haar_violation": mp.nstr(haar_broken_max, 8),
            "fixing_only_vh_transpose_shift": mp.nstr(vh_only_shift, 8),
            "L8_relay_takagi_diagnosis_refuted": bool(vh_only_shift < p10_mp(-35)),
        },
        "FL8_F5_mirror_cpt_and_YB_sign": {
            "flat_YB_proxy_tau8_pos": mp.nstr(ybp_flat, 12),
            "curved_YB_proxy_tau8_pos": mp.nstr(ybp_curv, 12),
            "flat_J_over_YB_mirror_diff": mp.nstr(j_yb_diff_flat, 8),
            "curved_J_over_YB_mirror_diff": mp.nstr(j_yb_diff_curv, 8),
            "F7_2_docstring_positive_YB_contradicted": bool(ybp_flat < mp.mpf(0) and peer_l7_yb < mp.mpf(0)),
        },
        "FL8_F4_kutta38_racetrack_and_split_susy": {
            "racetrack_s_star_agut_M0": [mp.nstr(s_star, 12), mp.nstr(agut_inv, 12), mp.nstr(m0_ov, 12)],
            "racetrack_diffs_vs_L7": [mp.nstr(x, 8) for x in rt_diffs],
            "pure_SYM_45_s_and_54_s_agut": [mp.nstr(sym45_s, 8), mp.nstr(sym54_s, 8), mp.nstr(sym54_agut, 8)],
            "kutta38_jack_jones_and_fmm_errs": [mp.nstr(jj_k38_err, 6), mp.nstr(fmm_k38_err, 6)],
            "cH_crit_and_tanb_from_g_k38": [mp.nstr(ch_crit_ref, 12), mp.nstr(tanb_ref, 12)],
            "cH_crit_and_tanb_diffs_vs_L8": [mp.nstr(ch_diff_peer, 6), mp.nstr(tb_diff_peer, 6)],
            "sympy_stop_threshold_and_split_susy_proof": sympy_stop_proof,
            "stop_threshold_L8_1x_vs_TRUE_2x_vs_ProdV2_4x": [
                mp.nstr(dlam_l8, 8),
                mp.nstr(dlam_true_2x, 8),
                mp.nstr(dlam_prodv2_4x, 8),
            ],
            "mh_over_v_table": mh_table,
        },
        "FL8_F6_bp_and_shannon_bits": {
            "cy4_r8_bp_log10_spacing": mp.nstr(bp_log10_r8, 8),
            "shannon_bits_129_decades": mp.nstr(shannon_bits_129, 8),
            "diffs_vs_prodv2": [mp.nstr(bp_vs_prodv2, 6), mp.nstr(bits_vs_prodv2, 6)],
        },
        "rpf4_haar_stopscale_wrongdir_caught": rpf4_caught,
        "internal_gate_passed": internal_ok,
    }


# ==============================================================================
# R_PA2_E: agy b06c8fc1e (Lobachevsky + M11-Free FW + Kutta-3/8 + Cl(10) chi)
# ==============================================================================

def run_r_pa2_e(
    gammas: list[sp.SparseMatrix],
    plus16_idx: list[int],
    prod_v2: dict[str, Any],
    discrepancies: list[dict[str, Any]],
    non_blocking: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 50
    v7 = json.loads(git_bytes(AGY_REF, "relays/agy_2026-11-23_c37/blind_predictions_full_toe_v7.json").decode("utf-8"))["prediction_bundle_v7"]
    c38 = json.loads(git_bytes(AGY_REF, "relays/agy_2026-11-24_c38/c38_out.json").decode("utf-8"))
    pe_v2 = prod_v2["PA2_E_agy_C37_C38_v7_and_OW22_closure"]

    # 1. Exact 11D Dirac quantization & Vol(m004) via Lobachevsky quadrature (disjoint from polylog!):
    # Vol(4_1) = 3 Cl_2(2 pi / 3) = 6 Lambda(pi / 3) = -6 int_0^{pi/3} ln(2 sin t) dt
    # Split at log singularity: -6 int_0^{pi/3} ln(2 sin t / t) dt - 6 int_0^{pi/3} ln(t) dt:
    gx, gw = gl_nodes_weights(48)
    a_int, b_int = mp.mpf(0), mp.pi / mp.mpf(3)
    hm, mm = (b_int - a_int) / mp.mpf(2), (a_int + b_int) / mp.mpf(2)
    smooth_int = mp.fsum(
        gw[k] * mp.log(mp.mpf(2) * mp.sin(mm + hm * gx[k]) / (mm + hm * gx[k]))
        for k in range(48)
    ) * hm
    # Analytical int_0^L ln(t) dt = L (ln L - 1):
    vol_m004 = -mp.mpf(6) * (smooth_int + b_int * (mp.log(b_int) - mp.mpf(1)))
    vol_check_poly = mp.mpf(3) * mp.im(mp.polylog(2, mp.exp(mp.mpf(2) * J_MP * mp.pi / mp.mpf(3))))
    vol_disjoint_diff = abs(vol_m004 - vol_check_poly)

    m11_s = sp.Symbol("M11", positive=True)
    two_k11 = (2 * sp.pi) ** 8 * m11_s ** (-9)
    tm2 = m11_s ** 3 / (2 * sp.pi) ** 2
    dirac_ok = bool(sp.simplify(two_k11 * (tm2 ** 3) - (2 * sp.pi) ** 2) == 0)

    # M_11-free Friedmann-Witten closed forms (disjoint algebraic path!):
    vq_hat = mp.mpf(8) * vol_m004
    vp_hat = ((mp.mpf(2) * mp.pi) ** 4) / mp.mpf(48)
    agut_inv_v7 = mp.mpf(40)
    m11_mgut = (agut_inv_v7 * ((mp.mpf(2) * mp.pi) ** 3) / vq_hat) ** rat_mp(1, 3)
    mpl_mgut_iso = mp.sqrt(mp.mpf(32) * (mp.pi ** 2) * vp_hat * (agut_inv_v7 ** 3) / (vq_hat ** 2))
    mpl_mgut_sd = mp.sqrt(mp.mpf(8) * vp_hat * (agut_inv_v7 ** rat_mp(5, 3)) / (((mp.mpf(2) * mp.pi) ** 2) * (vq_hat ** rat_mp(2, 3))))

    t_ew_star = mp.mpf(v7["dynamical_rg_horizons_ln_mu_over_mgut"]["t_ew_star"])
    mgut_vew = mp.exp(-t_ew_star)
    mpl_vew_sd = mpl_mgut_sd * mgut_vew
    mpl_vew_iso = mpl_mgut_iso * mgut_vew

    v7_g = v7["gravity_11d_d4_hurwitz_sector"]
    m11_diff = abs(m11_mgut - mp.mpf(v7_g["m11_over_mgut_zero_knob"]))
    mpl_sd_rel = abs(mpl_vew_sd - mp.mpf(v7_g["mpl_over_vew_d4_hurwitz_self_dual"])) / mpl_vew_sd
    mpl_iso_rel = abs(mpl_vew_iso - mp.mpf(v7_g["mpl_over_vew_d4_hurwitz_isotropic"])) / mpl_vew_iso

    # 2. 2-loop Caswell-Jones Lambda_QCD^(5f) RG invariance via Kutta-3/8 + SymPy:
    a_s, b0_s, b1_s = sp.symbols("a_s b0 b1", positive=True)
    ex_s = b1_s / (2 * b0_s ** 2)
    ln_cj = -2 * sp.pi / (b0_s * a_s) - ex_s * sp.log(b0_s * a_s / (4 * sp.pi)) + ex_s * sp.log(1 + b1_s * a_s / (4 * sp.pi * b0_s))
    da_dt = -(b0_s / (2 * sp.pi)) * a_s ** 2 - (b1_s / (8 * sp.pi ** 2)) * a_s ** 3
    cj_rg_exact = bool(sp.simplify(1 + sp.diff(ln_cj, a_s) * da_dt) == 0)

    def lam_cj(mu_q: mp.mpf, av: mp.mpf, nf: int) -> mp.mpf:
        b0 = rat_mp(33 - 2 * nf, 3)
        b1 = rat_mp(306 - 38 * nf, 3)
        ex = b1 / (mp.mpf(2) * b0 * b0)
        return mu_q * mp.exp(-mp.mpf(2) * mp.pi / (b0 * av)) * (((b0 * av) / (mp.mpf(4) * mp.pi)) ** (-ex)) * ((mp.mpf(1) + (b1 * av) / (mp.mpf(4) * mp.pi * b0)) ** ex)

    a3_ir = mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["strong_coupling_ir"])
    lam_5f = lam_cj(mp.mpf(1), a3_ir, 5)
    lam_5f_rel = abs(lam_5f - mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_5f_over_vew"])) / lam_5f
    b0_5, b1_5 = rat_mp(23, 3), rat_mp(116, 3)
    rhs_a3 = lambda _t, y: [-(b0_5 / (mp.mpf(2) * mp.pi)) * (y[0] ** 2) - (b1_5 / (mp.mpf(8) * (mp.pi ** 2))) * (y[0] ** 3)]
    a3_down = kutta38_rich2(rhs_a3, [a3_ir], mp.mpf(0), mp.mpf(-2), 128)[0]
    a3_up = kutta38_rich2(rhs_a3, [a3_ir], mp.mpf(0), mp.mpf(2), 128)[0]
    lam_5f_k38_rg_invar = max(
        abs(lam_cj(mp.exp(mp.mpf(-2)), a3_down, 5) - lam_5f) / lam_5f,
        abs(lam_cj(mp.exp(mp.mpf(2)), a3_up, 5) - lam_5f) / lam_5f,
    )

    # 3. Seam AGY-C37-S1:
    ratio_iso_sd = mpl_mgut_iso / mpl_mgut_sd
    v7_c = v7["cosmology_crv_and_honest_bounds"]
    k1_sd = mp.mpf(v7_c["leptogenesis_washout_K1_tot"])
    gtau_sd = mp.mpf(v7_c["leptogenesis_tau_equil_over_hubble"])
    yb_sd = mp.mpf(v7_c["leptogenesis_Y_B_2flavor_analytic_fit"])
    k1_iso = k1_sd * ratio_iso_sd
    gtau_iso = gtau_sd * ratio_iso_sd
    drop_29_25 = ratio_iso_sd ** rat_mp(29, 25)
    yb_iso_est = yb_sd / drop_29_25

    # 4. 6/6 U(1)_chi anomalies directly from 32x32 Cl(10) 16_+ spinor operators (ZERO hardcoded particle table!):
    pairs45 = [(a, b) for a in range(10) for b in range(a + 1, 10)]
    h_op = [sp.Rational(1, 2) * (-sp.I) * (gammas[2 * k] * gammas[2 * k + 1]) for k in range(5)]
    # Q_chi = -2 sum_{k=0..4} H_k (gives nu^c: -5, Q/u^c/e^c: -1, d^c/L: +3):
    qchi32 = -2 * sum(h_op, sp.SparseMatrix(32, 32, {}))
    y32 = sp.Rational(1, 6) * (-2 * (h_op[0] + h_op[1] + h_op[2]) + 3 * (h_op[3] + h_op[4]))
    t3c32 = sp.Rational(1, 2) * (h_op[0] - h_op[1])
    t3w32 = sp.Rational(1, 2) * (h_op[3] - h_op[4])

    def r16(m32: sp.SparseMatrix) -> sp.Matrix:
        return sp.Matrix([[m32[r, c] for c in plus16_idx] for r in plus16_idx])

    q16, y16, t3c16, t3w16 = r16(qchi32), r16(y32), r16(t3c32), r16(t3w32)
    anoms_6_cl10 = [
        sp.simplify((t3c16 * t3c16 * q16).trace()),
        sp.simplify((t3w16 * t3w16 * q16).trace()),
        sp.simplify((y16 * y16 * q16).trace()),
        sp.simplify((y16 * q16 * q16).trace()),
        sp.simplify((q16 ** 3).trace()),
        sp.simplify(q16.trace()),
    ]
    # RPF5 part 1: drop nu^c (the unique state in 16_+ with Q_chi == -5 and Y == 0):
    nuc_idx = [k for k in range(16) if q16[k, k] == -5 and y16[k, k] == 0]
    assert len(nuc_idx) == 1
    no_nuc_chi3 = sp.simplify(sum(q16[k, k] ** 3 for k in range(16) if k != nuc_idx[0]))
    no_nuc_grav = sp.simplify(sum(q16[k, k] for k in range(16) if k != nuc_idx[0]))

    # Explicit D-flat STr M_{Z'_chi}^2 == 0 check (chiral Phi_+ (+q) + Phi_- (-q) at <Phi_+>=<Phi_->=v_chi):
    # Real scalars (4): Goldstone (0), radial Higgs (M_V^2), two D-flat massless moduli (0, 0) => Tr M_scal^2 = M_V^2;
    # Vector Z'_chi (3 polarizations): +3 M_V^2; Fermions (3 Weyl: gaugino + psi_+ + psi_-): mass eigenvalues (0, M_V, M_V) => -2 * 2 M_V^2 = -4 M_V^2;
    # STr M^2 = 1 * (M_V^2) + 3 * (M_V^2) - 2 * (2 M_V^2) == 0!
    mv_s = sp.Symbol("M_V", positive=True)
    m_ferm_chi = sp.Matrix([[0, mv_s / sp.sqrt(2), -mv_s / sp.sqrt(2)], [mv_s / sp.sqrt(2), 0, 0], [-mv_s / sp.sqrt(2), 0, 0]])
    ferm_sq_evals = (m_ferm_chi * m_ferm_chi.T).eigenvals()
    tr_ferm_sq = sum(ev * mult for ev, mult in ferm_sq_evals.items())
    # Scalar 4x4 Hessian from D-term (1/2) (g q (|Phi_+|^2 - |Phi_-|^2))^2 at Phi_+ = Phi_- = v_chi (M_V^2 = 4 g^2 q^2 v_chi^2):
    m_scal_chi = sp.Matrix([[mv_s ** 2 / 2, -mv_s ** 2 / 2, 0, 0], [-mv_s ** 2 / 2, mv_s ** 2 / 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    str_m2_zchi = sp.simplify(m_scal_chi.trace() + 3 * (mv_s ** 2) - 2 * tr_ferm_sq)
    # 6D I_8 gravitational anomaly at (n_16=0, n_10=2, n_1=269, n_V=45, n_T=1):
    grav_6d_i8_resid = (0 * 16 + 2 * 10 + 269) - 45 + 29 * 1 - 273

    non_blocking.append({
        "id": "NBD-PA2-2",
        "block": "PA2-E",
        "location": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py:1598-1754",
        "summary": (
            "Scope Card PA2-E listed 6D I_8 gravity check (n_16=0, n_10=2, n_1=269), STr M_{Z'_chi}^2 == 0, and Lambda_QCD^(4f); "
            "Producer v2 omitted explicit output for these 3 sub-checks (computing Lambda_QCD^(5f) only). Referee independently "
            "verified 6D I_8 grav resid == 0 (289 - 45 + 29 == 273) and explicit D-flat STr M_{Z'_chi}^2 == 0 alongside Lambda_QCD^(5f)."
        ),
    })

    # 5. C38 B4 2HDM quartics derived directly from SymPy SU(2)_L x U(1)_Y D-term + lambda_S S H_u H_d F-term:
    g0_s, lams_s = sp.symbols("g0 lams", positive=True)
    # Expand V_D + V_F for Phi_1 = (a1, b1), Phi_2 = (a2, b2) (both Y=+1/2, where Phi_1 = eps H_d^*):
    # V_D^{SU(2)} = (g_2^2 / 8) (|Phi_1|^4 + |Phi_2|^4 + 2 |Phi_1|^2 |Phi_2|^2 - 4 |Phi_1^H Phi_2|^2)
    # Wait: check (Phi_1^H sigma^a Phi_1 + Phi_2^H sigma^a Phi_2)^2 = |Phi_1|^4 + |Phi_2|^4 + 2(2 |Phi_1^H Phi_2|^2 - |Phi_1|^2 |Phi_2|^2)
    # For H_1 = H_d (Y=-1/2) and H_2 = H_u (Y=+1/2), V_D^{SU(2)} + V_D^{U(1)_Y} + |F_S|^2 with |H_d^T eps H_u|^2 = |H_1|^2 |H_2|^2 - |H_1^H H_2|^2:
    # Using Phi_1 = eps H_d^* (Y=+1/2) and Phi_2 = H_u (Y=+1/2): |H_d^T eps H_u|^2 = |Phi_1^H Phi_2|^2,
    # and Phi_1^H sigma^a Phi_1 = - H_d^H sigma^a H_d!
    # So V_D^{SU(2)} = (g_2^2 / 8) (-Phi_1^H sigma^a Phi_1 + Phi_2^H sigma^a Phi_2)^2
    #                = (g_2^2 / 8) (|Phi_1|^4 + |Phi_2|^4 - 2(2 |Phi_1^H Phi_2|^2 - |Phi_1|^2 |Phi_2|^2))
    #                = (g_2^2 / 8) (|Phi_1|^4 + |Phi_2|^4 + 2 |Phi_1|^2 |Phi_2|^2 - 4 |Phi_1^H Phi_2|^2)
    # And V_D^{U(1)_Y} = (g'^2 / 8) (-|Phi_1|^2 + |Phi_2|^2)^2 = (g'^2 / 8) (|Phi_1|^4 + |Phi_2|^4 - 2 |Phi_1|^2 |Phi_2|^2), g'^2 = (3/5) g0^2.
    n1, n2, c12 = sp.symbols("n1 n2 c12", real=True)  # |Phi_1|^2, |Phi_2|^2, |Phi_1^H Phi_2|^2
    gp2_s = sp.Rational(3, 5) * g0_s ** 2
    v_2hdm = sp.expand(
        (g0_s ** 2 / 8) * (n1 ** 2 + n2 ** 2 + 2 * n1 * n2 - 4 * c12)
        + (gp2_s / 8) * (n1 ** 2 + n2 ** 2 - 2 * n1 * n2)
        + (lams_s ** 2) * c12
    )
    lam1_sym = sp.simplify(2 * v_2hdm.coeff(n1, 2))
    lam2_sym = sp.simplify(2 * v_2hdm.coeff(n2, 2))
    lam3_sym = sp.simplify(sp.diff(sp.diff(v_2hdm, n1), n2))
    lam4_sym = sp.simplify(v_2hdm.coeff(c12, 1))
    b4_sym_ok = bool(
        lam1_sym == sp.Rational(2, 5) * g0_s ** 2
        and lam2_sym == sp.Rational(2, 5) * g0_s ** 2
        and lam3_sym == sp.Rational(1, 10) * g0_s ** 2
        and lam4_sym == lams_s ** 2 - sp.Rational(1, 2) * g0_s ** 2
    )
    s_bl1 = mp.mpf(c38["E2_all_6_anomalies_and_explicit_dflat_str_zchi"]["four_modulus_newton_t_s_re_im_45d"][1])
    g_bl1_sq = mp.mpf(4) * mp.pi / s_bl1
    q_b4_num = [rat_mp(2, 5) * g_bl1_sq, rat_mp(2, 5) * g_bl1_sq, rat_mp(1, 10) * g_bl1_sq, rat_mp(9, 25) - rat_mp(1, 2) * g_bl1_sq]
    peer_q_b4 = [mp.mpf(x) for x in c38["E3_b4_2hdm_quartics_and_b6_verification"]["B4_2hdm_quartics_recomputed"]["derived_2hdm_quartics_at_s_star_35d"]]
    b4_q_diff = max(abs(a - b) for a, b in zip(q_b4_num, peer_q_b4))

    # 6. C37 E3 seesaw eps_1-cancellation: BOTH exact symbolic proof AND 50-dps random numerical proof:
    e1, e2, e3 = sp.symbols("e1 e2 e3", nonzero=True)
    d1_sym = sp.diag(e1, e2, e3)
    c_sym = sp.Matrix([[sp.Symbol(f"c{i}{j}") for j in range(3)] for i in range(3)])
    r_inv_sym = sp.Matrix([[sp.Symbol(f"r{min(i,j)}{max(i,j)}") for j in range(3)] for i in range(3)])
    # (C D1) (D1 R D1)^{-1} (C D1)^T = C D1 D1^{-1} R^{-1} D1^{-1} D1 C^T = C R^{-1} C^T:
    sym_cancel_mat = sp.simplify((c_sym * d1_sym) * (d1_sym.inv() * r_inv_sym * d1_sym.inv()) * (c_sym * d1_sym).T - c_sym * r_inv_sym * c_sym.T)
    sym_eps1_cancel_ok = bool(sym_cancel_mat == sp.zeros(3, 3))

    rng = random.Random(2026112477)
    cn = mp.matrix([[mp.mpc(rng.randint(-7, 7), rng.randint(-7, 7)) for _ in range(3)] for _ in range(3)])
    cr0 = mp.matrix([[mp.mpc(rng.randint(-7, 7), rng.randint(-7, 7)) for _ in range(3)] for _ in range(3)])
    cr = cr0 + cr0.T + mp.mpf(23) * mp.eye(3)
    d5 = mp.diag([rat_mp(1, 3), rat_mp(1, 5), rat_mp(1, 7)])
    d1 = mp.diag([rat_mp(1, 11), rat_mp(1, 13), rat_mp(1, 17)])
    mnu_w = -(d5 * cn * d1) * ((d1 * cr * d1) ** (-1)) * (d5 * cn * d1).T
    mnu_wo = -(d5 * cn) * (cr ** (-1)) * (d5 * cn).T
    eps1_num_err = mp.sqrt(sum(abs(mnu_w[i, j] - mnu_wo[i, j]) ** 2 for i in range(3) for j in range(3)))

    # 7. OW22-F1..F3:
    ow22_tab = {
        "B4_UV_52_13": fr_str(Fr(52 - 13, 2)),
        "B4_IR_49_12": fr_str(Fr(49 - 12, 2)),
        "B5_IR_85_12": fr_str(Fr(85 - 12, 2)),
        "B5_13vec_85_13": fr_str(Fr(85 - 13, 2)),
        "B5_UV_E6_85_14": fr_str(Fr(85 - 14, 2)),
    }
    r_ss = mp.log(mp.mpf(2)) / mp.mpf(32)
    b1_e = r_ss * rat_mp(33, 5) + (mp.mpf(1) - r_ss) * rat_mp(21, 5)
    b2_e = r_ss * mp.mpf(1) + (mp.mpf(1) - r_ss) * mp.mpf(-3)
    b3_e = r_ss * mp.mpf(-3) + (mp.mpf(1) - r_ss) * mp.mpf(-7)
    beff_ss = (b2_e - b3_e) / (b1_e - b2_e)
    hom_z2_z2_nontriv = len([(a, b) for a in (0, 1) for b in (0, 1) if (a, b) != (0, 0)])

    # RPF5: drop nu^c from Cl(10) 16_+ AND old C35 T_M2 = M_11^3 quantization fail by (2 pi)^6:
    c35_bad_ratio = sp.simplify((two_k11 * (m11_s ** 9)) / ((2 * sp.pi) ** 2))
    rpf5_caught = bool(no_nuc_chi3 == 125 and no_nuc_grav == 5 and c35_bad_ratio == (2 * sp.pi) ** 6)

    # Cross-check against Producer v2 PA2_E:
    seam_v2 = pe_v2["seam_AGY_C37_S1_leptogenesis_sd_vs_iso_branch"]
    ratio_diff_v2 = abs(ratio_iso_sd - mp.mpf(seam_v2["mpl_iso_over_sd_ratio"]))
    drop_diff_v2 = abs(drop_29_25 - mp.mpf(seam_v2["washout_drop_factor_R_pow_29_25"]))
    beff_diff_v2 = abs(beff_ss - mp.mpf(pe_v2["OW22_F1_F3_acknowledged_and_resolved"]["OW22_F2_T2_SS_Beff_collapse"]))
    e_match_v2 = bool(
        ratio_diff_v2 < p10_mp(-7)
        and drop_diff_v2 < p10_mp(-5)
        and beff_diff_v2 < p10_mp(-8)
        and pe_v2["OW22_F1_F3_acknowledged_and_resolved"]["OW22_F1_stage_consistent_a1_table"] == ow22_tab
    )
    if not e_match_v2:
        discrepancies.append({
            "id": "DISC-PA2-E",
            "block": "PA2-E",
            "severity": "REAL_DISCREPANCY",
            "producer_claim": str(pe_v2),
            "referee_finding": f"PA2-E mismatch (ratio_diff={mp.nstr(ratio_diff_v2, 5)}, drop_diff={mp.nstr(drop_diff_v2, 5)}).",
        })

    internal_ok = bool(
        vol_disjoint_diff < p10_mp(-35)
        and dirac_ok and cj_rg_exact
        and m11_diff < p10_mp(-24)
        and mpl_sd_rel < p10_mp(-9)
        and mpl_iso_rel < p10_mp(-9)
        and lam_5f_rel < p10_mp(-9)
        and lam_5f_k38_rg_invar < p10_mp(-16)
        and all(v == 0 for v in anoms_6_cl10)
        and str_m2_zchi == 0
        and grav_6d_i8_resid == 0
        and b4_sym_ok and b4_q_diff < p10_mp(-30)
        and sym_eps1_cancel_ok and eps1_num_err < p10_mp(-42)
        and ow22_tab == {"B4_UV_52_13": "39/2", "B4_IR_49_12": "37/2", "B5_IR_85_12": "73/2", "B5_13vec_85_13": "36", "B5_UV_E6_85_14": "71/2"}
        and beff_ss < rat_mp(3, 5)
        and hom_z2_z2_nontriv == 3
        and rpf5_caught and e_match_v2
    )
    return {
        "vol_m004_lobachevsky_quad_vs_polylog_diff": mp.nstr(vol_disjoint_diff, 6),
        "dirac_11d_quantization_exact": dirac_ok,
        "m11_over_mgut_abs_diff_vs_v7": mp.nstr(m11_diff, 8),
        "m11_free_FW_mpl_sd_and_iso_rel_diffs": [mp.nstr(mpl_sd_rel, 8), mp.nstr(mpl_iso_rel, 8)],
        "lambda_qcd_5f_rel_diff_and_kutta38_rg_invar": [mp.nstr(lam_5f_rel, 8), mp.nstr(lam_5f_k38_rg_invar, 8)],
        "seam_AGY_C37_S1": {
            "mpl_iso_over_sd_ratio": mp.nstr(ratio_iso_sd, 10),
            "K1_sd_vs_iso": [mp.nstr(k1_sd, 8), mp.nstr(k1_iso, 8)],
            "Gamma_tau_over_H_sd_vs_iso": [mp.nstr(gtau_sd, 8), mp.nstr(gtau_iso, 8)],
            "washout_drop_R_29_25": mp.nstr(drop_29_25, 8),
            "Y_B_sd_vs_iso_estimate": [mp.nstr(yb_sd, 8), mp.nstr(yb_iso_est, 8)],
        },
        "cl10_16plus_6_u1chi_anomalies_zero": all(v == 0 for v in anoms_6_cl10),
        "explicit_dflat_STr_M2_Zchi_zero": bool(str_m2_zchi == 0),
        "6d_I8_grav_anomaly_n16_0_n10_2_n1_269_zero": bool(grav_6d_i8_resid == 0),
        "c38_b4_sympy_and_max_diff": [b4_sym_ok, mp.nstr(b4_q_diff, 8)],
        "c37_e3_eps1_cancel_sym_and_frob_err": [sym_eps1_cancel_ok, mp.nstr(eps1_num_err, 8)],
        "ow22_F1_F3": {
            "a1_table": ow22_tab,
            "Beff_T2_SS": mp.nstr(beff_ss, 10),
            "Beff_lt_3_over_5": bool(beff_ss < rat_mp(3, 5)),
            "Hom_Z2_Z2_nontriv": hom_z2_z2_nontriv,
        },
        "matches_producer_v2": e_match_v2,
        "rpf5_drop_nuc_and_c35_quant_caught": rpf5_caught,
        "internal_gate_passed": internal_ok,
    }


# ==============================================================================
# R_PA2_F: Cross-Seat Table Direct Audit & LOCK_V3 Canonical SHA-256 Check
# ==============================================================================

def run_r_pa2_f(
    prod_v2: dict[str, Any],
    r_pa2_d: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    ow27 = json.loads((REPO_ROOT / "relays/a2_ow27_v8/a2_ow27_v8_results.json").read_text(encoding="utf-8"))
    v7 = json.loads(git_bytes(AGY_REF, "relays/agy_2026-11-23_c37/blind_predictions_full_toe_v7.json").decode("utf-8"))["prediction_bundle_v7"]
    l8 = json.loads(git_bytes(AGY_EXP_REF, "relays/x_floor_link8_verify/verify_x_floor_link8_out.json").decode("utf-8"))
    pf_v2 = prod_v2["PA2_F_blind_cross_seat_comparison_and_lock_v3"]

    ow27_e = ow27["OW27_E_planted_faults_and_blind_lock_v3"]
    lock_payload = dict(ow27_e["blind_prediction_lock_v3_B4_UV"])
    canon_bytes = json.dumps(lock_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    recomp_lock_sha = hashlib.sha256(canon_bytes).hexdigest()
    lock_v3_intact = bool(
        recomp_lock_sha == EXPECTED_LOCK_V3
        and ow27_e["blind_prediction_lock_v3_sha256"] == EXPECTED_LOCK_V3
        and pf_v2["lock_v3_sha256"] == EXPECTED_LOCK_V3
    )

    # RPF6: mutate one character of LOCK_V3 copy in memory and confirm digest mismatch caught:
    mut_bytes = canon_bytes[:-2] + (b"X" if canon_bytes[-2:-1] != b"X" else b"Y") + canon_bytes[-1:]
    rpf6_caught = bool(hashlib.sha256(mut_bytes).hexdigest() != EXPECTED_LOCK_V3 and recomp_lock_sha == EXPECTED_LOCK_V3)

    # Direct field-by-field cross-check of ALL entries in PA2_F table against authoritative source JSONs:
    runs = ow27["OW27_A_2loop_qcd_4coupling_higgs_veltman_decoupling_and_lambda_qcd"]["mz_and_mt_2loop_pipeline_runs"]
    p3 = runs["CURV_s12_Dirac_yt_gUV_tb15_m0_3v_sgnMu_pos"]
    p10 = runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    b203 = l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]
    tab_v2 = pf_v2["cross_seat_blind_comparison_0_of_19"]

    chk_agy002 = bool(
        tab_v2["agy_002_B4_UV_LOCK_V3_m0_3v_10v"]["alpha_3_5f"] == [p3["alpha3_mz_nf5"], p10["alpha3_mz_nf5"]]
        and tab_v2["agy_002_B4_UV_LOCK_V3_m0_3v_10v"]["sin2_thetaW_MSbar"] == [p3["sin2_thetaW_msbar_mz"], p10["sin2_thetaW_msbar_mz"]]
        and tab_v2["agy_002_B4_UV_LOCK_V3_m0_3v_10v"]["mh_pole_over_MZ"] == [p3["mh_pole_4c_at_mz_over_mz"], p10["mh_pole_4c_at_mz_over_mz"]]
        and tab_v2["agy_002_B4_UV_LOCK_V3_m0_3v_10v"]["Lambda_QCD_4f_over_vEW"] == [p3["Lambda_QCD_4_exact_over_v"], p10["Lambda_QCD_4_exact_over_v"]]
    )
    chk_agy_v7 = bool(
        tab_v2["agy_v7_json_nonsusy_2HDM"]["alpha_3_ir"] == v7["sm_1loop_pole_and_2hdm_bosons"]["strong_coupling_ir"]
        and tab_v2["agy_v7_json_nonsusy_2HDM"]["sin2_thetaW_ir"] == v7["sm_msbar_at_ew_horizon"]["electroweak_mix_ratio"]
        and tab_v2["agy_v7_json_nonsusy_2HDM"]["mh0_over_vEW"] == v7["sm_1loop_pole_and_2hdm_bosons"]["higgs_h0_over_vew"]
        and tab_v2["agy_v7_json_nonsusy_2HDM"]["Lambda_QCD_4f_over_vEW"] == v7["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_4f_over_vew"]
    )
    chk_exp_raw = bool(
        tab_v2["agy_exp_LINK8_dtSM_m4_raw_vs_corrected"]["alpha_3_dt_m4"] == b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["alpha_s"]
        and tab_v2["agy_exp_LINK8_dtSM_m4_raw_vs_corrected"]["sin2_thetaW_dt_m4"] == b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["sin2_thetaW"]
        and tab_v2["agy_exp_LINK8_dtSM_m4_raw_vs_corrected"]["mh_over_v_raw_vs_complete_GR"][0] == b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["mh_over_v"]
        and tab_v2["agy_exp_LINK8_dtSM_m4_raw_vs_corrected"]["pmns_s12_s23_s13_L8_corrupted_vs_true_Takagi"][0] == b203["pmns_s12sq_s23sq_s13sq_dmratio"][:3]
    )
    # Note: mh_over_v_raw_vs_complete_GR[1] in PA2_F carries Producer v2's 4x stop-threshold value (DISC-PA2-2):
    mh4_v2_table = tab_v2["agy_exp_LINK8_dtSM_m4_raw_vs_corrected"]["mh_over_v_raw_vs_complete_GR"][1]
    mh4_ref_true2x = r_pa2_d["FL8_F4_kutta38_racetrack_and_split_susy"]["mh_over_v_table"]["dt_SM_-4"]["mh_over_v_true_2x_SplitSUSY_GR"]

    if not (lock_v3_intact and chk_agy002 and chk_agy_v7 and chk_exp_raw):
        discrepancies.append({
            "id": "DISC-PA2-F",
            "block": "PA2-F",
            "severity": "REAL_DISCREPANCY",
            "producer_claim": str(pf_v2),
            "referee_finding": f"Mismatch in LOCK_V3 or source JSON transcription ({lock_v3_intact}, {chk_agy002}, {chk_agy_v7}, {chk_exp_raw}).",
        })

    internal_ok = bool(lock_v3_intact and chk_agy002 and chk_agy_v7 and chk_exp_raw and rpf6_caught)
    return {
        "lock_v3_canonical_sha256_recomputed": recomp_lock_sha,
        "lock_v3_intact": lock_v3_intact,
        "agy002_source_fields_exact_match": chk_agy002,
        "agy_v7_source_fields_exact_match": chk_agy_v7,
        "agy_exp_raw_source_fields_exact_match": chk_exp_raw,
        "agy_exp_dtSM_m4_mh_over_v_ProdV2_4x_vs_Referee_True2x": [mh4_v2_table, mh4_ref_true2x],
        "rpf6_lock_v3_tamper_caught": rpf6_caught,
        "internal_gate_passed": internal_ok,
    }


def main() -> None:
    self_src = SELF_PATH.read_text(encoding="utf-8")
    self_ast = check_ast_hygiene(self_src, SELF_PATH.name)
    self_sha = hashlib.sha256(SELF_PATH.read_bytes()).hexdigest()

    prod_v2 = json.loads(PROD_V2_JSON.read_text(encoding="utf-8"))
    discrepancies: list[dict[str, Any]] = []
    non_blocking: list[dict[str, Any]] = []

    # Check NBD-PA2-3: Producer v2 used literal integer 6 for planted_controls_caught (even though gated by all_ok):
    prod_v2_src = PROD_V2_SCRIPT.read_text(encoding="utf-8")
    if '"planted_controls_caught": 6' in prod_v2_src:
        non_blocking.append({
            "id": "NBD-PA2-3",
            "block": "Global (Guardrail 2 style)",
            "location": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py:1862",
            "summary": "Producer v2 assigned literal integer 6 to planted_controls_caught (though gated by all_ok raising AssertionError if any pfX_caught is False); dynamic sum is preferred under Guardrail 2.",
        })

    gammas, _g11, plus16_idx = build_cl10_gammas()

    ra = run_r_pa2_a(prod_v2, discrepancies)
    rb = run_r_pa2_b(gammas, plus16_idx, prod_v2, discrepancies)
    rc = run_r_pa2_c(gammas, plus16_idx, prod_v2, discrepancies)
    rd = run_r_pa2_d(prod_v2, discrepancies, non_blocking)
    re = run_r_pa2_e(gammas, plus16_idx, prod_v2, discrepancies, non_blocking)
    rf = run_r_pa2_f(prod_v2, rd, discrepancies)

    controls = {
        "RPF1_manifest_1byte_tamper_caught": ra["rpf1_tamper_caught"],
        "RPF2_cl10_bad_n10_and_F6_caught": rb["rpf2_bad_n10_and_F6_caught"],
        "RPF3_crt_S_swap_and_tr4_S3_caught": rc["rpf3_S_swap_and_tr4_S3_caught"],
        "RPF4_haar_stopscale_wrongdir_caught": rd["rpf4_haar_stopscale_wrongdir_caught"],
        "RPF5_cl10_drop_nuc_and_c35_quant_caught": re["rpf5_drop_nuc_and_c35_quant_caught"],
        "RPF6_lock_v3_mutation_caught": rf["rpf6_lock_v3_tamper_caught"],
    }
    controls_caught = sum(1 for v in controls.values() if v)
    controls_total = len(controls)

    internal_all_ok = bool(
        self_ast["clean"]
        and ra["internal_gate_passed"]
        and rb["internal_gate_passed"]
        and rc["internal_gate_passed"]
        and rd["internal_gate_passed"]
        and re["internal_gate_passed"]
        and rf["internal_gate_passed"]
        and controls_caught == controls_total
    )
    all_referee_gates_passed = bool(internal_all_ok and len(discrepancies) == 0)

    payload = {
        "referee_id": "A2-PEER-AUDIT-V2-Disjoint-Cold-Room-Zero-Trust-Referee",
        "card": "AGY-002_A2-PEER-AUDIT-V2",
        "seat": "agy-002",
        "audited_producer": "relays/a2_peer_audit_v2_run2/verify_a2_peer_audit_v2_run2.py",
        "audited_producer_json": "relays/a2_peer_audit_v2_run2/a2_peer_audit_v2_run2_results.json",
        "firewall": "0 of 19",
        "script": SELF_PATH.name,
        "script_sha256": self_sha,
        "self_ast_hygiene": self_ast,
        "R_PA2_A_custody_ast_and_FL8_F2b": ra,
        "R_PA2_B_cl10_32x32_and_bourbaki_e8_bfs": rb,
        "R_PA2_C_wirtinger_cl10_centralizers_crt_jtheta": rc,
        "R_PA2_D_jtheta_whol_real6_takagi_kutta38": rd,
        "R_PA2_E_lobachevsky_fw_kutta38_cl10_chi": re,
        "R_PA2_F_cross_seat_table_and_lock_v3": rf,
        "R_planted_controls": {
            "controls": controls,
            "caught": controls_caught,
            "total": controls_total,
            "all_caught": bool(controls_caught == controls_total),
        },
        "referee_internal_self_gates_passed": internal_all_ok,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "non_blocking_diagnostics": non_blocking,
        "all_referee_gates_passed": all_referee_gates_passed,
    }
    assert_zero_json_floats(payload)
    OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not internal_all_ok:
        raise AssertionError("Referee internal self-gate failed!")


if __name__ == "__main__":
    main()
