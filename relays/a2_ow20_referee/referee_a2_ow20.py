#!/usr/bin/env python3
"""
Cold-Room Zero-Shared-Code Independent Referee for agy-002 Card A2-OW20 & Card A2-OW16 v6.

Disjoint numerical methods:
  - OW20-A: Implicit 2-stage Gauss-Legendre 4th-order (GL4) Runge-Kutta integrator
    on full non-commuting 3x3 Type-II 2HDM 2-loop Yukawa + 2-loop gauge + 1-loop quartic ODEs,
    disjoint SplitMix64 Box-Muller Mezzadri Haar U(3)^3 x U(3)^2 covariance test,
    and independent 2-flavor vs 3-flavor leptogenesis with Autonne-Takagi verification.
  - OW20-B: Analytical 1D elimination g(lam) = -2/(b1(lam) - 2 b2(lam)) + Ridder/bisection 1D
    root finder for G_SM 2HDM FRG under DP Type-I (f_W = -1/2) & DEP Type-II (f_W = +1),
    F-OW18-03 sealed JSON vs prose audit, and E_6 N_W = 81 & Z_4 M_R == 0 algebra.
  - OW20-C: Direct enumeration of (Z/5Z)^2 & (Z/6Z)^2 primitive torsion, explicit SL(2, Z)
    conjugacy covariance, Synergy S-1 antipodal p_3 -> -p_3 weave, and direct 2^{d-1}
    weight-lattice half-spinor cubic trace sums for SO(2d) SU(d)^3 anomalies (d = 3..15).
  - A2-OW16 v6: Independent recount of 1/10/9/4 partition, Guardrail 5 ledger, & full
    historical false-flag JSON scan across relays/.
  - Custody: Producer AST hygiene audit + full live SHA-256 verification of all manifests
    across relays/ + 6/6 referee planted fault controls.

Firewall: strictly 0 of 19 (zero empirical numbers; 0 Python float/complex AST literals).
"""

import ast
import hashlib
import json
import math
import pathlib
from fractions import Fraction
import mpmath as mp


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
OUT_DIR = pathlib.Path(__file__).resolve().parent
FORBIDDEN_IMPORT_TOKENS = ("frontier", "relays", "self_consistent", "phase10", "c29", "c30")


# ============================================================================
# Pure-mpmath & Fraction arithmetic helpers (ZERO float/complex literals)
# ============================================================================

def Q(num, den=1):
    return mp.mpf(num) / mp.mpf(den)


def frac_to_mp(f):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def pow10(exp_int):
    return mp.mpf(10) ** exp_int


def m2_mul(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def m2_T(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def m2_add(A, B, scale=1):
    return [[A[r][c] + scale * B[r][c] for c in range(2)] for r in range(2)]


def m2_scale(A, scale):
    return [[A[r][c] * scale for c in range(2)] for r in range(2)]


def m3_zero():
    return [[mp.mpc(0, 0) for _ in range(3)] for _ in range(3)]


def m3_eye(val=1):
    z = mp.mpc(0, 0)
    return [[val if i == j else z for j in range(3)] for i in range(3)]


def m3_mul(A, B):
    return [
        [sum((A[i][k] * B[k][j] for k in range(3)), mp.mpc(0, 0)) for j in range(3)]
        for i in range(3)
    ]


def m3_H(A):
    return [[mp.conj(A[j][i]) for j in range(3)] for i in range(3)]


def m3_T(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def m3_add(A, B, scale=1):
    return [[A[i][j] + scale * B[i][j] for j in range(3)] for i in range(3)]


def m3_scale(A, scale):
    return [[A[i][j] * scale for j in range(3)] for i in range(3)]


def m3_tr(A):
    return A[0][0] + A[1][1] + A[2][2]


def m3_frob(A, B=None):
    acc = mp.mpf(0)
    for i in range(3):
        for j in range(3):
            diff = A[i][j] if B is None else (A[i][j] - B[i][j])
            acc += mp.re(diff * mp.conj(diff))
    return mp.sqrt(acc)


def parse_json_mat3(raw_mat):
    return [[mp.mpc(mp.mpf(cell[0]), mp.mpf(cell[1])) for cell in row] for row in raw_mat]


def mat3_to_mpmatrix(A):
    return mp.matrix([[A[i][j] for j in range(3)] for i in range(3)])


def mpmatrix_to_mat3(M):
    return [[M[i, j] for j in range(3)] for i in range(3)]


def hermitian_eigh_sorted(H):
    """Ascending eigendecomposition of 3x3 Hermitian matrix H with explicit residual checks."""
    evals, evecs = mp.eigh(mat3_to_mpmatrix(H))
    order = sorted(range(3), key=lambda k: mp.re(evals[k]))
    vals_s = [mp.re(evals[k]) for k in order]
    U = [[evecs[i, order[j]] for j in range(3)] for i in range(3)]
    D = [[vals_s[i] if i == j else mp.mpc(0, 0) for j in range(3)] for i in range(3)]
    eig_err = m3_frob(m3_mul(H, U), m3_mul(U, D))
    unit_err = m3_frob(m3_mul(m3_H(U), U), m3_eye(mp.mpf(1)))
    return vals_s, U, eig_err, unit_err


def ckm_abs_ascending(Yu, Yd):
    """Compute ascending-mass CKM |V_12|, |V_23|, |V_13| from Yu, Yd."""
    _, Uu, eu_err, uu_err = hermitian_eigh_sorted(m3_mul(Yu, m3_H(Yu)))
    _, Ud, ed_err, ud_err = hermitian_eigh_sorted(m3_mul(Yd, m3_H(Yd)))
    V = m3_mul(m3_H(Uu), Ud)
    return (
        [abs(V[0][1]), abs(V[1][2]), abs(V[0][2])],
        max(eu_err, uu_err, ed_err, ud_err),
    )


def takagi_3x3(M_sym):
    """Autonne-Takagi factorization U_R^T M_sym U_R = diag(M_1, M_2, M_3), ascending M_k >= 0."""
    sym_err = m3_frob(M_sym, m3_T(M_sym))
    H_R = m3_mul(m3_H(M_sym), M_sym)
    evals, V, eig_err, unit_err = hermitian_eigh_sorted(H_R)
    D_ph = m3_mul(m3_mul(m3_T(V), M_sym), V)
    # Extract phases on diagonal; verify off-diagonals vanish
    U_R = m3_zero()
    masses = []
    for k in range(3):
        dkk = D_ph[k][k]
        mk = abs(dkk)
        masses.append(mk)
        if mk > pow10(-45):
            phase = mp.exp(mp.mpc(0, -1) * mp.arg(dkk) / mp.mpf(2))
        else:
            phase = mp.mpc(1, 0)
        for i in range(3):
            U_R[i][k] = V[i][k] * phase
    # Enforce ascending mass order
    order = sorted(range(3), key=lambda k: masses[k])
    masses_s = [masses[k] for k in order]
    U_s = [[U_R[i][order[j]] for j in range(3)] for i in range(3)]
    D_m = [[masses_s[i] if i == j else mp.mpc(0, 0) for j in range(3)] for i in range(3)]
    tak_err = m3_frob(m3_mul(m3_mul(m3_T(U_s), M_sym), U_s), D_m)
    u_err = m3_frob(m3_mul(m3_H(U_s), U_s), m3_eye(mp.mpf(1)))
    return masses_s, U_s, max(sym_err, eig_err, unit_err, tak_err, u_err)


# ============================================================================
# Disjoint SplitMix64 Haar U(3) generator (Mezzadri 2007 QR normalization)
# ============================================================================

class SplitMix64:
    def __init__(self, seed):
        self.state = seed & ((1 << 64) - 1)

    def next_u64(self):
        self.state = (self.state + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
        return (z ^ (z >> 31)) & ((1 << 64) - 1)

    def next_unit_open(self):
        # Strictly in (0, 1) using exact rational construction
        denom = mp.mpf((1 << 64) + 1)
        return mp.mpf(self.next_u64() + 1) / denom

    def next_complex_normal(self):
        u1 = self.next_unit_open()
        u2 = self.next_unit_open()
        rad = mp.sqrt(mp.mpf(-2) * mp.log(u1))
        ang = mp.mpf(2) * mp.pi * u2
        return mp.mpc(rad * mp.cos(ang), rad * mp.sin(ang))


def haar_u3(rng):
    Z = [[rng.next_complex_normal() for _ in range(3)] for _ in range(3)]
    # Modified Gram-Schmidt QR with Mezzadri positive-real diagonal phase fix
    cols = [[Z[i][j] for i in range(3)] for j in range(3)]
    q_cols = []
    for j in range(3):
        v = list(cols[j])
        for q in q_cols:
            dot = sum((mp.conj(q[i]) * v[i] for i in range(3)), mp.mpc(0, 0))
            v = [v[i] - dot * q[i] for i in range(3)]
        nrm = mp.sqrt(sum((mp.re(x * mp.conj(x)) for x in v), mp.mpf(0)))
        q_new = [x / nrm for x in v]
        # Diagonal phase r_jj = q_new^H * cols[j] is already positive real; fix via Z[j][j] projection
        # For exact Mezzadri invariance under column phase, pick first nonzero phase of r_jj
        r_jj = sum((mp.conj(q_new[i]) * cols[j][i] for i in range(3)), mp.mpc(0, 0))
        ph = r_jj / abs(r_jj)
        q_cols.append([x * ph for x in q_new])
    U = [[q_cols[j][i] for j in range(3)] for i in range(3)]
    unit_err = m3_frob(m3_mul(m3_H(U), U), m3_eye(mp.mpf(1)))
    return U, unit_err


# ============================================================================
# MODULE 1: Producer AST & Full Branch Manifest Audit
# ============================================================================

def ast_audit_file(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    fc_count = 0
    forb_count = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            fc_count += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                nm = alias.name.lower()
                if any(tok in nm for tok in FORBIDDEN_IMPORT_TOKENS):
                    forb_count += 1
        elif isinstance(node, ast.ImportFrom):
            mod = (node.module or "").lower()
            if any(tok in mod for tok in FORBIDDEN_IMPORT_TOKENS):
                forb_count += 1
            for alias in node.names:
                nm = alias.name.lower()
                if any(tok in nm for tok in FORBIDDEN_IMPORT_TOKENS):
                    forb_count += 1
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "file": str(path.relative_to(REPO_ROOT)),
        "ast_float_complex_count": fc_count,
        "ast_forbidden_import_count": forb_count,
        "sha256": sha,
    }


def verify_all_manifests(exclude_relpaths):
    relays_dir = REPO_ROOT / "relays"
    manifest_files = sorted(
        list(relays_dir.glob("**/SCRIPT_SHA256.txt"))
        + list(relays_dir.glob("**/OUTPUT_SHA256.txt"))
    )
    entries_verified = 0
    files_checked = 0
    mismatches = []
    sample_manifest_for_pf = None

    for mf in manifest_files:
        rel_mf = str(mf.relative_to(REPO_ROOT))
        if rel_mf in exclude_relpaths:
            continue
        files_checked += 1
        lines = [ln.strip() for ln in mf.read_text(encoding="utf-8").splitlines() if ln.strip()]
        if not lines:
            mismatches.append({"manifest": rel_mf, "reason": "empty_manifest"})
            continue
        for ln in lines:
            parts = ln.split(None, 1)
            if len(parts) != 2:
                mismatches.append({"manifest": rel_mf, "line": ln, "reason": "malformed_line"})
                continue
            exp_hash, rel_target = parts[0].lower(), parts[1].strip().lstrip("*")
            cand1 = mf.parent / rel_target
            cand2 = REPO_ROOT / rel_target
            target = cand1 if cand1.exists() else (cand2 if cand2.exists() else None)
            if target is None:
                mismatches.append({"manifest": rel_mf, "target": rel_target, "reason": "missing_file"})
                continue
            actual_hash = hashlib.sha256(target.read_bytes()).hexdigest().lower()
            if actual_hash != exp_hash:
                mismatches.append({
                    "manifest": rel_mf,
                    "target": str(target.relative_to(REPO_ROOT)),
                    "expected": exp_hash,
                    "actual": actual_hash,
                    "reason": "sha256_mismatch",
                })
            else:
                entries_verified += 1
                if sample_manifest_for_pf is None:
                    sample_manifest_for_pf = (rel_mf, target, exp_hash)

    return {
        "manifest_files_checked": files_checked,
        "manifests_verified": entries_verified,
        "mismatches": mismatches,
        "zero_mismatches": (len(mismatches) == 0 and entries_verified > 0),
        "_sample_for_pf1": sample_manifest_for_pf,
    }


def audit_1_ast_and_manifests(d20, d16, discrepancies):
    p_ow20 = REPO_ROOT / "relays" / "a2_ow20" / "verify_a2_ow20.py"
    p_ow16 = REPO_ROOT / "relays" / "a2_ow16_v6" / "verify_a2_ow16_v6.py"
    p_self = pathlib.Path(__file__).resolve()

    ast_ow20 = ast_audit_file(p_ow20)
    ast_ow16 = ast_audit_file(p_ow16)
    ast_self = ast_audit_file(p_self)

    for rec in (ast_ow20, ast_ow16, ast_self):
        if rec["ast_float_complex_count"] != 0:
            discrepancies.append("AST float/complex count nonzero in " + rec["file"])
        if rec["ast_forbidden_import_count"] != 0:
            discrepancies.append("AST forbidden import nonzero in " + rec["file"])

    ow20_sha_ok = (ast_ow20["sha256"] == d20["hygiene"]["script_sha256"])
    ow16_sha_ok = (ast_ow16["sha256"] == d16["hygiene"]["script_sha256"])
    if not ow20_sha_ok:
        discrepancies.append("verify_a2_ow20.py SHA-256 mismatch vs JSON")
    if not ow16_sha_ok:
        discrepancies.append("verify_a2_ow16_v6.py SHA-256 mismatch vs JSON")

    exclude = {str((OUT_DIR / "OUTPUT_SHA256.txt").relative_to(REPO_ROOT))}
    mf_res = verify_all_manifests(exclude)
    if not mf_res["zero_mismatches"]:
        discrepancies.append("Branch SHA-256 manifest mismatches detected")

    sample_pf1 = mf_res.pop("_sample_for_pf1")
    return {
        "producer_ast_ow20": ast_ow20,
        "producer_ast_ow16_v6": ast_ow16,
        "referee_ast_self": ast_self,
        "ow20_script_sha_matches_json": ow20_sha_ok,
        "ow16_script_sha_matches_json": ow16_sha_ok,
        "manifests": mf_res,
    }, sample_pf1


# ============================================================================
# MODULE 2: OW20-A — Disjoint GL4 Type-II 2HDM 2-Loop RGEs & 2-Flavor Lepto
# ============================================================================

def beta_yukawa_2loop_type2_parts(g, lam, Yu, Yd, Ye):
    """Return 1-loop and 2-loop beta matrices (without 1/(16pi^2) factors) for Type-II 2HDM."""
    g1, g2, g3 = g
    l1, l2, l3, l4 = lam
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3

    Hu = m3_mul(Yu, m3_H(Yu))
    Hd = m3_mul(Yd, m3_H(Yd))
    He = m3_mul(Ye, m3_H(Ye))
    Hu2 = m3_mul(Hu, Hu)
    Hd2 = m3_mul(Hd, Hd)
    He2 = m3_mul(He, He)
    HuHd = m3_mul(Hu, Hd)
    HdHu = m3_mul(Hd, Hu)

    Tu = mp.re(m3_tr(Hu))
    Td = mp.re(m3_tr(Hd))
    Te = mp.re(m3_tr(He))
    T1 = mp.mpf(3) * Td + Te
    T2 = mp.mpf(3) * Tu
    trHu2 = mp.re(m3_tr(Hu2))
    trHd2 = mp.re(m3_tr(Hd2))
    trHe2 = mp.re(m3_tr(He2))
    trHuHd = mp.re(m3_tr(HuHd))

    # 1-loop Yukawa (Type-II 2HDM)
    Mu1 = m3_add(m3_scale(Hu, Q(3, 2)), m3_scale(Hd, Q(1, 2)))
    Mu1 = m3_add(Mu1, m3_eye(T2 - (Q(17, 20) * g1s + Q(9, 4) * g2s + mp.mpf(8) * g3s)))
    bYu1 = m3_mul(Mu1, Yu)

    Md1 = m3_add(m3_scale(Hd, Q(3, 2)), m3_scale(Hu, Q(1, 2)))
    Md1 = m3_add(Md1, m3_eye(T1 - (Q(1, 4) * g1s + Q(9, 4) * g2s + mp.mpf(8) * g3s)))
    bYd1 = m3_mul(Md1, Yd)

    Me1 = m3_add(m3_scale(He, Q(3, 2)), m3_eye(T1 - (Q(9, 4) * g1s + Q(9, 4) * g2s)))
    bYe1 = m3_mul(Me1, Ye)

    # 2-loop Yukawa (Type-II 2HDM, Machacek-Vaughn NPB 236 & Chowdhury-Eberhardt 1503.08216)
    su2 = (
        -Q(27, 4) * trHu2 - Q(9, 4) * trHuHd
        + Q(3, 2) * l2 * l2 + l3 * l3 + l3 * l4 + l4 * l4
        + (Q(17, 8) * g1s + Q(45, 8) * g2s + mp.mpf(20) * g3s) * Tu
        + Q(1267, 600) * g1s * g1s - Q(9, 20) * g1s * g2s + Q(19, 15) * g1s * g3s
        - Q(21, 4) * g2s * g2s + mp.mpf(9) * g2s * g3s - mp.mpf(108) * g3s * g3s
    )
    Mu2 = m3_eye(su2)
    Mu2 = m3_add(Mu2, m3_scale(Hu2, Q(3, 2)))
    Mu2 = m3_add(Mu2, m3_scale(HuHd, Q(-1, 4)))
    Mu2 = m3_add(Mu2, m3_scale(Hd2, Q(-1, 4)))
    Mu2 = m3_add(Mu2, m3_scale(Hu, -Q(9, 4) * T2 - mp.mpf(6) * l2 + Q(223, 80) * g1s + Q(135, 16) * g2s + mp.mpf(16) * g3s))
    Mu2 = m3_add(Mu2, m3_scale(Hd, -Q(3, 4) * T1 - mp.mpf(2) * l3 + mp.mpf(2) * l4 + Q(-41, 240) * g1s + Q(33, 16) * g2s + Q(16, 3) * g3s))
    bYu2 = m3_mul(Mu2, Yu)

    sd2 = (
        -Q(27, 4) * trHd2 - Q(9, 4) * trHe2 - Q(9, 4) * trHuHd
        + Q(3, 2) * l1 * l1 + l3 * l3 + l3 * l4 + l4 * l4
        + (Q(5, 8) * g1s + Q(45, 8) * g2s + mp.mpf(20) * g3s) * Td
        + (Q(15, 8) * g1s + Q(15, 8) * g2s) * Te
        + Q(-113, 600) * g1s * g1s - Q(27, 20) * g1s * g2s + Q(31, 15) * g1s * g3s
        - Q(21, 4) * g2s * g2s + mp.mpf(9) * g2s * g3s - mp.mpf(108) * g3s * g3s
    )
    Md2 = m3_eye(sd2)
    Md2 = m3_add(Md2, m3_scale(Hd2, Q(3, 2)))
    Md2 = m3_add(Md2, m3_scale(HdHu, Q(-1, 4)))
    Md2 = m3_add(Md2, m3_scale(Hu2, Q(-1, 4)))
    Md2 = m3_add(Md2, m3_scale(Hd, -Q(9, 4) * T1 - mp.mpf(6) * l1 + Q(187, 80) * g1s + Q(135, 16) * g2s + mp.mpf(16) * g3s))
    Md2 = m3_add(Md2, m3_scale(Hu, -Q(3, 4) * T2 - mp.mpf(2) * l3 + mp.mpf(2) * l4 + Q(-53, 240) * g1s + Q(33, 16) * g2s + Q(16, 3) * g3s))
    bYd2 = m3_mul(Md2, Yd)

    se2 = (
        -Q(27, 4) * trHd2 - Q(9, 4) * trHe2 - Q(9, 4) * trHuHd
        + Q(3, 2) * l1 * l1 + l3 * l3 + l3 * l4 + l4 * l4
        + (Q(5, 8) * g1s + Q(45, 8) * g2s + mp.mpf(20) * g3s) * Td
        + (Q(15, 8) * g1s + Q(15, 8) * g2s) * Te
        + Q(1449, 200) * g1s * g1s + Q(27, 20) * g1s * g2s - Q(21, 4) * g2s * g2s
    )
    Me2 = m3_eye(se2)
    Me2 = m3_add(Me2, m3_scale(He2, Q(3, 2)))
    Me2 = m3_add(Me2, m3_scale(He, -Q(9, 4) * T1 - mp.mpf(6) * l1 + Q(387, 80) * g1s + Q(135, 16) * g2s))
    bYe2 = m3_mul(Me2, Ye)

    return (bYu1, bYd1, bYe1), (bYu2, bYd2, bYe2), (Tu, Td, Te, T1, T2, trHu2, trHd2, trHe2, trHuHd)


def rhs_type2_2hdm(state, c_hd_in_yu_1loop=None):
    """Full coupled Type-II 2HDM ODE RHS (2-loop gauge, 1-loop quartic lam5=0, 2-loop Yukawa)."""
    g, lam, Yu, Yd, Ye = state
    g1, g2, g3 = g
    l1, l2, l3, l4 = lam
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    inv16 = mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi)
    inv16_2 = inv16 * inv16

    (bYu1, bYd1, bYe1), (bYu2, bYd2, bYe2), traces = beta_yukawa_2loop_type2_parts(g, lam, Yu, Yd, Ye)
    Tu, Td, Te, T1, T2, trHu2, trHd2, trHe2, trHuHd = traces

    if c_hd_in_yu_1loop is not None:
        # Perturbation hook for PF-REF-2 (replaces +(1/2) Hd Yu with c_hd_in_yu_1loop Hd Yu)
        delta_c = c_hd_in_yu_1loop - Q(1, 2)
        Hd = m3_mul(Yd, m3_H(Yd))
        bYu1 = m3_add(bYu1, m3_mul(Hd, Yu), delta_c)

    b1 = [Q(21, 5), mp.mpf(-3), mp.mpf(-7)]
    B_mat = [
        [Q(104, 25), Q(18, 5), Q(44, 5)],
        [Q(6, 5), mp.mpf(8), mp.mpf(12)],
        [Q(11, 10), Q(9, 2), mp.mpf(-26)],
    ]
    c_yuk = [
        [Q(17, 10), Q(1, 2), Q(3, 2)],
        [Q(3, 2), Q(3, 2), Q(1, 2)],
        [mp.mpf(2), mp.mpf(2), mp.mpf(0)],
    ]
    gs = [g1s, g2s, g3s]
    dg = []
    for i in range(3):
        g3i = g[i] * g[i] * g[i]
        b2i = sum(B_mat[i][j] * gs[j] for j in range(3)) - c_yuk[i][0] * Tu - c_yuk[i][1] * Td - c_yuk[i][2] * Te
        dg.append(inv16 * b1[i] * g3i + inv16_2 * g3i * b2i)

    gbox_p = Q(27, 100) * g1s * g1s + Q(9, 10) * g1s * g2s + Q(9, 4) * g2s * g2s
    gbox_m = Q(27, 100) * g1s * g1s - Q(9, 10) * g1s * g2s + Q(9, 4) * g2s * g2s
    g_anom = Q(9, 5) * g1s + mp.mpf(9) * g2s
    dl1 = inv16 * (
        mp.mpf(12) * l1 * l1 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + gbox_p - l1 * g_anom + mp.mpf(4) * l1 * T1 - mp.mpf(12) * trHd2 - mp.mpf(4) * trHe2
    )
    dl2 = inv16 * (
        mp.mpf(12) * l2 * l2 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + gbox_p - l2 * g_anom + mp.mpf(4) * l2 * T2 - mp.mpf(12) * trHu2
    )
    dl3 = inv16 * (
        (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4) + mp.mpf(4) * l3 * l3 + mp.mpf(2) * l4 * l4
        + gbox_m - l3 * g_anom + mp.mpf(2) * l3 * (T1 + T2) - mp.mpf(12) * trHuHd
    )
    dl4 = inv16 * (
        mp.mpf(2) * (l1 + l2) * l4 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4 * l4
        + Q(9, 5) * g1s * g2s - l4 * g_anom + mp.mpf(2) * l4 * (T1 + T2) + mp.mpf(12) * trHuHd
    )
    dYu = m3_add(m3_scale(bYu1, inv16), m3_scale(bYu2, inv16_2))
    dYd = m3_add(m3_scale(bYd1, inv16), m3_scale(bYd2, inv16_2))
    dYe = m3_add(m3_scale(bYe1, inv16), m3_scale(bYe2, inv16_2))
    return (dg, [dl1, dl2, dl3, dl4], dYu, dYd, dYe)


def beta_yu_1hdm_pure_yukawa(Yu, Yd, Ye, buggy_ordering=False):
    """Exact 1HDM Luo-Xiao Eq. (14) pure-Yukawa 2-loop beta_Yu (and OW18-A buggy ordering)."""
    Hu = m3_mul(Yu, m3_H(Yu))
    Hd = m3_mul(Yd, m3_H(Yd))
    He = m3_mul(Ye, m3_H(Ye))
    Hu2 = m3_mul(Hu, Hu)
    Hd2 = m3_mul(Hd, Hd)
    He2 = m3_mul(He, He)
    HuHd = m3_mul(Hu, Hd)
    HdHu = m3_mul(Hd, Hu)
    T_all = mp.mpf(3) * mp.re(m3_tr(Hu)) + mp.mpf(3) * mp.re(m3_tr(Hd)) + mp.re(m3_tr(He))
    scalar_part = (
        -Q(27, 4) * mp.re(m3_tr(Hu2))
        - Q(27, 4) * mp.re(m3_tr(Hd2))
        - Q(9, 4) * mp.re(m3_tr(He2))
        + Q(3, 2) * mp.re(m3_tr(HuHd))
    )
    M = m3_eye(scalar_part)
    M = m3_add(M, m3_scale(Hu2, Q(3, 2)))
    if not buggy_ordering:
        M = m3_add(M, m3_scale(HdHu, mp.mpf(-1)))
        M = m3_add(M, m3_scale(HuHd, Q(-1, 4)))
    else:
        M = m3_add(M, m3_scale(HuHd, mp.mpf(-1)))
        M = m3_add(M, m3_scale(HdHu, Q(-1, 4)))
    M = m3_add(M, m3_scale(Hd2, Q(11, 4)))
    M = m3_add(M, m3_scale(Hu, -Q(9, 4) * T_all))
    M = m3_add(M, m3_scale(Hd, Q(5, 4) * T_all))
    return m3_mul(M, Yu)


def rhs_1hdm_1loop_ckm_compare(state):
    """1-loop SM (1HDM) Yukawa + gauge ODE for clean CKM sign-reversal countercheck."""
    g, lam, Yu, Yd, Ye = state
    g1, g2, g3 = g
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    inv16 = mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi)
    Hu = m3_mul(Yu, m3_H(Yu))
    Hd = m3_mul(Yd, m3_H(Yd))
    He = m3_mul(Ye, m3_H(Ye))
    T_all = mp.mpf(3) * mp.re(m3_tr(Hu)) + mp.mpf(3) * mp.re(m3_tr(Hd)) + mp.re(m3_tr(He))
    b1 = [Q(41, 10), Q(-19, 6), mp.mpf(-7)]
    dg = [inv16 * b1[i] * g[i] ** 3 for i in range(3)]
    dlam = [mp.mpf(0) for _ in range(4)]
    Mu1 = m3_add(m3_scale(Hu, Q(3, 2)), m3_scale(Hd, Q(-3, 2)))
    Mu1 = m3_add(Mu1, m3_eye(T_all - (Q(17, 20) * g1s + Q(9, 4) * g2s + mp.mpf(8) * g3s)))
    Md1 = m3_add(m3_scale(Hd, Q(3, 2)), m3_scale(Hu, Q(-3, 2)))
    Md1 = m3_add(Md1, m3_eye(T_all - (Q(1, 4) * g1s + Q(9, 4) * g2s + mp.mpf(8) * g3s)))
    Me1 = m3_add(m3_scale(He, Q(3, 2)), m3_eye(T_all - (Q(9, 4) * g1s + Q(9, 4) * g2s)))
    return (
        dg,
        dlam,
        m3_scale(m3_mul(Mu1, Yu), inv16),
        m3_scale(m3_mul(Md1, Yd), inv16),
        m3_scale(m3_mul(Me1, Ye), inv16),
    )


def state_add(s, ds, h):
    g, l, u, d, e = s
    dg, dl, du, dd, de = ds
    return (
        [g[i] + h * dg[i] for i in range(3)],
        [l[i] + h * dl[i] for i in range(4)],
        m3_add(u, du, h),
        m3_add(d, dd, h),
        m3_add(e, de, h),
    )


def state_dist(s1, s2):
    g1, l1, u1, d1, e1 = s1
    g2, l2, u2, d2, e2 = s2
    return max(
        max(abs(g1[i] - g2[i]) for i in range(3)),
        max(abs(l1[i] - l2[i]) for i in range(4)),
        m3_frob(u1, u2),
        m3_frob(d1, d2),
        m3_frob(e1, e2),
    )


def gl4_integrate(rhs_fn, state0, dt_total, n_steps):
    """Implicit 2-stage Gauss-Legendre 4th-order Runge-Kutta integrator."""
    sq3 = mp.sqrt(mp.mpf(3))
    a11 = Q(1, 4)
    a12 = Q(1, 4) - sq3 / mp.mpf(6)
    a21 = Q(1, 4) + sq3 / mp.mpf(6)
    a22 = Q(1, 4)
    b1 = Q(1, 2)
    b2 = Q(1, 2)
    h = dt_total / mp.mpf(n_steps)
    tol = pow10(-38)
    st = state0
    max_fp_resid = mp.mpf(0)
    for _ in range(n_steps):
        k1 = rhs_fn(st)
        k2 = k1
        err = mp.mpf(1)
        for _it in range(45):
            y1 = state_add(state_add(st, k1, h * a11), k2, h * a12)
            y2 = state_add(state_add(st, k1, h * a21), k2, h * a22)
            nk1 = rhs_fn(y1)
            nk2 = rhs_fn(y2)
            err = max(state_dist(nk1, k1), state_dist(nk2, k2))
            k1, k2 = nk1, nk2
            if err < tol:
                break
        if err > max_fp_resid:
            max_fp_resid = err
        st = state_add(state_add(st, k1, h * b1), k2, h * b2)
    return st, max_fp_resid


# ----------------------------------------------------------------------------
# Synergy S-1 Szego Yukawa Engine (from exact specification, zero shared code)
# ----------------------------------------------------------------------------

def make_quat_basis():
    I = mp.mpc(0, 1)
    z = mp.mpc(0, 0)
    one = mp.mpc(1, 0)
    qi = [[I, z], [z, -I]]
    qj = [[z, one], [-one, z]]
    qk = m2_mul(qi, qj)
    I2 = [[one, z], [z, one]]
    B_blocks = [qj, qi, qk]
    e_basis = {
        "1": m2_scale(qj, Q(1, 2)),
        "i": m2_scale(qk, Q(1, 2)),
        "j": m2_scale(I2, Q(-1, 2)),
        "k": m2_scale(qi, Q(-1, 2)),
    }
    return qi, qj, qk, B_blocks, e_basis


def tau_precompute(tau, L2_val):
    I = mp.mpc(0, 1)
    qi, qj, qk, B_blocks, e_basis = make_quat_basis()
    x = mp.re(tau)
    y = mp.im(tau)
    q = mp.exp(mp.mpf(2) * mp.pi * I * tau)

    th2 = mp.mpc(0, 0)
    dth2 = mp.mpc(0, 0)
    for n in range(0, 22):
        ex = Q((2 * n + 1) ** 2, 8)
        term = mp.mpf(2) * mp.exp(mp.mpf(2) * mp.pi * I * tau * ex)
        th2 += term
        dth2 += ex * term

    th3 = mp.mpc(1, 0)
    dth3 = mp.mpc(0, 0)
    th4 = mp.mpc(1, 0)
    dth4 = mp.mpc(0, 0)
    for n in range(1, 22):
        ex = Q(n * n, 2)
        term = mp.mpf(2) * mp.exp(mp.mpf(2) * mp.pi * I * tau * ex)
        th3 += term
        dth3 += ex * term
        sgn = mp.mpf(-1) if (n % 2 == 1) else mp.mpf(1)
        th4 += sgn * term
        dth4 += sgn * ex * term

    l2 = dth2 / th2
    l3 = dth3 / th3
    l4 = dth4 / th4

    E2 = mp.mpc(1, 0)
    qn = q
    for n in range(1, 48):
        E2 -= mp.mpf(24 * n) * qn / (mp.mpc(1, 0) - qn)
        qn *= q

    e24 = E2 / mp.mpf(24)
    c_i = (-th2 / (th3 * th4)) * (l2 - l3 - l4 + e24)
    c_j = (-th4 / (th2 * th3)) * (l4 - l2 - l3 + e24)
    c_k = (I * th3 / (th2 * th4)) * (l3 - l2 - l4 + e24)

    Sh = m2_add(m2_add(m2_scale(qi, c_i), m2_scale(qj, c_j)), m2_scale(qk, c_k))
    C = [
        [m2_mul(m2_mul(m2_T(B_blocks[a]), qj), m2_mul(Sh, B_blocks[b])) for b in range(3)]
        for a in range(3)
    ]

    prod_eta = mp.mpc(1, 0)
    qn = q
    for _n in range(1, 48):
        prod_eta *= (mp.mpc(1, 0) - qn)
        qn *= q
    th1p = mp.mpf(2) * mp.pi * (mp.exp(I * mp.pi * tau / mp.mpf(12)) * prod_eta) ** 3
    C_sh = (
        mp.mpf(2) * mp.pi * L2_val
        + mp.pi * mp.log(y)
        - mp.mpf(2) * mp.pi * (mp.euler + mp.log(mp.pi))
    )
    return {
        "tau": tau,
        "x": x,
        "y": y,
        "C": C,
        "th1p": th1p,
        "C_sh": C_sh,
        "L2": L2_val,
        "e_basis": e_basis,
    }


def theta_char(ca, cb, tau):
    I = mp.mpc(0, 1)
    na = math.floor(ca)
    ta_f = ca - na
    nb = math.floor(cb)
    tb_f = cb - nb
    ta = frac_to_mp(ta_f)
    tb = frac_to_mp(tb_f)
    if nb == 0 or ta_f == 0:
        lead = mp.mpc(1, 0)
    else:
        lead = mp.exp(mp.mpf(2) * mp.pi * I * ta * mp.mpf(nb))
    z = ta * tau + tb
    acc = mp.mpc(0, 0)
    for k in range(-22, 23):
        acc += mp.exp(I * mp.pi * mp.mpf(k * k) * tau + mp.mpf(2) * mp.pi * I * mp.mpf(k) * z)
    return lead * mp.exp(I * mp.pi * ta * ta * tau + mp.mpf(2) * mp.pi * I * ta * tb) * acc


def green_A2_and_F(alpha_f, beta_f, pc):
    I = mp.mpc(0, 1)
    tau, x, y = pc["tau"], pc["x"], pc["y"]
    alpha = frac_to_mp(alpha_f)
    beta = frac_to_mp(beta_f)
    z = alpha * tau + beta
    th1 = mp.mpc(0, 0)
    dth1 = mp.mpc(0, 0)
    half = Q(1, 2)
    for k in range(-22, 22):
        m = mp.mpf(2 * k + 1) / mp.mpf(2)
        term = mp.exp(I * mp.pi * m * m * tau + mp.mpf(2) * mp.pi * I * m * (z + half))
        th1 -= term
        dth1 -= (mp.mpf(2) * mp.pi * I * m) * term
    val = mp.mpf(2) * mp.pi * I * alpha + dth1 / th1
    A2 = mp.re(val * mp.conj(val))

    if alpha_f != 0:
        f0 = -mp.pi * (
            mp.mpf(2) * mp.log(mp.mpf(2))
            + mp.log(y)
            + mp.psi(0, alpha)
            + mp.psi(0, mp.mpf(1) - alpha)
        )
    else:
        f0 = (
            mp.pi * (mp.mpf(2) * mp.euler - mp.mpf(2) * mp.log(mp.mpf(2)) - mp.log(y))
            + y * mp.pi * mp.pi / (mp.sin(mp.pi * beta) ** 2)
        )

    F_val = f0
    for k in range(-22, 23):
        mf = alpha_f + k
        if mf == 0:
            continue
        m = frac_to_mp(mf)
        absm = abs(m)
        w = mp.exp(mp.mpf(-2) * mp.pi * absm * y + mp.mpf(2) * mp.pi * I * (m * x + beta))
        F_val += (mp.mpf(2) * mp.pi / absm) * mp.re(w / (mp.mpc(1, 0) - w))
    return A2, F_val


def szego_Y(pc, p, qL, qR):
    I = mp.mpc(0, 1)
    pa, pb = p
    x0, x1 = qL * pa, 2 * qL * pb
    y0, y1 = qR * pa, 2 * qR * pb
    ap, am = x0 + y0, x0 - y0
    bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    half = Fraction(1, 2)
    e_ph = mp.exp(mp.mpf(-2) * mp.pi * I * frac_to_mp(x0))
    kappa = {"1": -I * e_ph, "i": mp.mpc(-1, 0), "j": -e_ph, "k": I}
    cs = {"1": (ap + half, bp + half), "i": (ap + half, bp), "j": (ap, bp + half), "k": (ap, bp)}
    ds = {"1": (am + half, bm + half), "i": (am + half, bm), "j": (am, bm + half), "k": (am, bm)}

    MW = [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]]
    e_basis = pc["e_basis"]
    exp_m2L2 = mp.exp(mp.mpf(-2) * pc["L2"])
    for s in ("1", "i", "j", "k"):
        c0, c1 = cs[s]
        d0, d1 = ds[s]
        al = (c0 - half) - math.floor(c0 - half)
        be = (c1 - half) - math.floor(c1 - half)
        dal = (d0 - half) - math.floor(d0 - half)
        dbe = (d1 - half) - math.floor(d1 - half)
        if (al == 0 and be == 0) or (dal == 0 and dbe == 0):
            us = mp.mpc(0, 0)
        else:
            rs = kappa[s] * theta_char(c0, c1, pc["tau"]) * theta_char(d0, d1, pc["tau"]) / pc["th1p"]
            A2, F_val = green_A2_and_F(al, be, pc)
            arg_s = pc["C_sh"] + F_val - mp.pi * A2 * exp_m2L2
            us = mp.sqrt(arg_s) * rs if arg_s > mp.mpf(0) else mp.mpc(0, 0)
        MW = m2_add(MW, m2_scale(e_basis[s], us))

    C = pc["C"]
    return [
        [
            sum((C[a][b][r][c] * MW[r][c] for r in range(2) for c in range(2)), mp.mpc(0, 0))
            for b in range(3)
        ]
        for a in range(3)
    ]


def synergy_weights():
    w3 = ((mp.mpf(3) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)) ** (-4)
    w4 = mp.mpf(2) * ((mp.mpf(4) + mp.sqrt(mp.mpf(12))) / mp.mpf(2)) ** (-4)
    return w3 / (w3 + w4), w4 / (w3 + w4)


def weave_Y0(pc, p3, p4, om3, om4, qL, qR):
    return m3_add(m3_scale(szego_Y(pc, p3, qL, qR), om3), m3_scale(szego_Y(pc, p4, qL, qR), om4))


def dress_Yeff(Y0):
    H0 = m3_mul(m3_H(Y0), Y0)
    H02 = m3_mul(H0, H0)
    tr = mp.re(m3_tr(H0))
    return m3_scale(m3_mul(Y0, H02), mp.mpf(1) / (tr * tr))


def canonicalize_K(M, Ke2):
    Kinv2 = [[mp.mpf(1) / mp.sqrt(Ke2[i]) if i == j else mp.mpc(0, 0) for j in range(3)] for i in range(3)]
    return m3_mul(m3_mul(Kinv2, M), Kinv2)


def compute_leptogenesis_observables(Ye, Ynu, MR):
    """Compute exact 2-flavor (|tau> vs |e+mu>) and 3-flavor leptogenesis observables."""
    _, Ue, ue_err, uu_err = hermitian_eigh_sorted(m3_mul(Ye, m3_H(Ye)))
    masses, UR, tak_err = takagi_3x3(MR)
    Y_tilde = m3_mul(m3_mul(m3_H(Ue), Ynu), UR)
    H_tilde = m3_mul(m3_H(Y_tilde), Y_tilde)
    h00 = mp.re(H_tilde[0][0])

    eps = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for j in (1, 2):
        xj = (masses[j] / masses[0]) ** 2
        gamj = mp.re(H_tilde[j][j]) / (mp.mpf(8) * mp.pi)
        Dj = (xj - mp.mpf(1)) ** 2 + xj * gamj * gamj
        f_SV = mp.sqrt(xj) * ((mp.mpf(1) - xj) / Dj + mp.mpf(1) - (mp.mpf(1) + xj) * mp.log(mp.mpf(1) + mp.mpf(1) / xj))
        g_osc = (mp.mpf(1) - xj) / Dj
        for a in range(3):
            c_sv = mp.conj(Y_tilde[a][0]) * Y_tilde[a][j] * H_tilde[0][j]
            c_osc = mp.conj(Y_tilde[a][0]) * Y_tilde[a][j] * H_tilde[j][0]
            eps[a] += (mp.im(c_sv) * f_SV + mp.im(c_osc) * g_osc) / (mp.mpf(8) * mp.pi * h00)

    p_br = [mp.re(Y_tilde[a][0] * mp.conj(Y_tilde[a][0])) / h00 for a in range(3)]
    K1 = mp.mpf(200)
    pw = Q(29, 25)
    gstar = Q(443, 4)
    n_eq = Q(3, 4) / (mp.zeta(mp.mpf(3)) * gstar)
    a_sph = Q(-8, 23)

    def eta_w(K):
        return mp.mpf(1) / (mp.mpf(1) + K ** pw)

    yb_3f = a_sph * n_eq * sum(eps[a] * eta_w(p_br[a] * K1) for a in range(3))
    eps_emu = eps[0] + eps[1]
    p_emu = p_br[0] + p_br[1]
    yb_2f = a_sph * n_eq * (eps_emu * eta_w(p_emu * K1) + eps[2] * eta_w(p_br[2] * K1))
    return {
        "eps": eps,
        "eps_emu": eps_emu,
        "p_br": p_br,
        "yb_3f": yb_3f,
        "yb_2f": yb_2f,
        "max_decomp_err": max(ue_err, uu_err, tak_err),
    }


def extract_1x1_benchmarks():
    """Extract Arason/Buttazzo 1HDM and all 15 Chowdhury-Eberhardt Type-II 2HDM coefficients directly from 3x3 RHS."""
    def diag3(v):
        z = mp.mpc(0, 0)
        return [[z, z, z], [z, z, z], [z, z, mp.mpc(v, 0)]]

    g0 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    l0 = [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]

    # 1HDM Arason/Buttazzo 1x1: beta_yt^(2) = c_yt5 yt^5 + c_yt3yb2 yt^3 yb^2 + c_ytyb4 yt yb^4
    v10 = mp.re(beta_yu_1hdm_pure_yukawa(diag3(1), diag3(0), diag3(0))[2][2])
    v11 = mp.re(beta_yu_1hdm_pure_yukawa(diag3(1), diag3(1), diag3(0))[2][2])
    v12 = mp.re(beta_yu_1hdm_pure_yukawa(diag3(1), diag3(2), diag3(0))[2][2])
    # v11 - v10 = b + c; v12 - v10 = 4b + 16c => 12c = (v12-v10) - 4(v11-v10)
    c_1hdm_yt5 = v10
    c_1hdm_ytyb4 = ((v12 - v10) - mp.mpf(4) * (v11 - v10)) / mp.mpf(12)
    c_1hdm_yt3yb2 = (v11 - v10) - c_1hdm_ytyb4
    arason_targets = [
        ("yt5", c_1hdm_yt5, mp.mpf(-12)),
        ("yt3_yb2", c_1hdm_yt3yb2, Q(-11, 4)),
        ("yt_yb4", c_1hdm_ytyb4, Q(-1, 4)),
    ]
    arason_max_err = max(abs(got - exp) for _, got, exp in arason_targets)

    # Type-II 2HDM Chowdhury-Eberhardt 15 exact 1x1 coefficients from beta_yukawa_2loop_type2_parts
    def b2_t2(g_vec, yt, yb, ytau):
        _, (bu2, bd2, be2), _ = beta_yukawa_2loop_type2_parts(g_vec, l0, diag3(yt), diag3(yb), diag3(ytau))
        return mp.re(bu2[2][2]), mp.re(bd2[2][2]), mp.re(be2[2][2])

    u100, _, _ = b2_t2(g0, 1, 0, 0)
    u110, _, _ = b2_t2(g0, 1, 1, 0)
    u120, _, _ = b2_t2(g0, 1, 2, 0)
    u111, _, _ = b2_t2(g0, 1, 1, 1)
    c_yt5 = u100
    c_ytyb4 = ((u120 - u100) - mp.mpf(4) * (u110 - u100)) / mp.mpf(12)
    c_yt3yb2 = (u110 - u100) - c_ytyb4
    c_ytyb2ytau2 = u111 - u110

    _, _, e001 = b2_t2(g0, 0, 0, 1)
    _, _, e011 = b2_t2(g0, 0, 1, 1)
    _, _, e021 = b2_t2(g0, 0, 2, 1)
    _, _, e111 = b2_t2(g0, 1, 1, 1)
    c_ytau5 = e001
    c_ytauyb4 = ((e021 - e001) - mp.mpf(4) * (e011 - e001)) / mp.mpf(12)
    c_ytau3yb2 = (e011 - e001) - c_ytauyb4
    c_ytauyt2yb2 = e111 - e011

    # Pure gauge g1^4, g2^4 (set Yukawas = 1 with tiny scaling or subtract Y^5 at g=0; better: scale g=1 and Yukawa=eps?
    # Even cleaner: with Yu=diag(1), Yd=0, Ye=0, g=(1,0,0), bYu2(g1) - bYu2(0) = c_g1_4 * 1 + c_g1_2_yt3 * 1;
    # evaluate at g=(1,0,0) and g=(2,0,0)!)
    u_g1_1, _, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 1, 0, 0)
    u_g1_2, _, _ = b2_t2([mp.mpf(2), mp.mpf(0), mp.mpf(0)], 1, 0, 0)
    # du(1) = c2 + c4; du(2) = 4 c2 + 16 c4 => 12 c4 = du(2) - 4 du(1)
    c_g1_4_u = ((u_g1_2 - u100) - mp.mpf(4) * (u_g1_1 - u100)) / mp.mpf(12)

    _, d010, _ = b2_t2(g0, 0, 1, 0)
    _, d_g1_1, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 0, 1, 0)
    _, d_g1_2, _ = b2_t2([mp.mpf(2), mp.mpf(0), mp.mpf(0)], 0, 1, 0)
    c_g1_4_d = ((d_g1_2 - d010) - mp.mpf(4) * (d_g1_1 - d010)) / mp.mpf(12)

    _, _, e_g1_1 = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 0, 0, 1)
    _, _, e_g1_2 = b2_t2([mp.mpf(2), mp.mpf(0), mp.mpf(0)], 0, 0, 1)
    c_g1_4_e = ((e_g1_2 - e001) - mp.mpf(4) * (e_g1_1 - e001)) / mp.mpf(12)

    u_g2_1, _, _ = b2_t2([mp.mpf(0), mp.mpf(1), mp.mpf(0)], 1, 0, 0)
    u_g2_2, _, _ = b2_t2([mp.mpf(0), mp.mpf(2), mp.mpf(0)], 1, 0, 0)
    c_g2_4_u = ((u_g2_2 - u100) - mp.mpf(4) * (u_g2_1 - u100)) / mp.mpf(12)

    # Off-diagonal gauge * H_d on Y_u and gauge * H_u on Y_d:
    # bYu2(g, yt=1, yb=1) - bYu2(g, yt=1, yb=0) - (bYu2(0, yt=1, yb=1) - bYu2(0, yt=1, yb=0)) = coeff(g^2 Hd Yu) * g^2
    u_g3_11, _, _ = b2_t2([mp.mpf(0), mp.mpf(0), mp.mpf(1)], 1, 1, 0)
    u_g3_10, _, _ = b2_t2([mp.mpf(0), mp.mpf(0), mp.mpf(1)], 1, 0, 0)
    c_g3_hd_yu = (u_g3_11 - u_g3_10) - (u110 - u100)

    u_g2_11, _, _ = b2_t2([mp.mpf(0), mp.mpf(1), mp.mpf(0)], 1, 1, 0)
    u_g2_10, _, _ = b2_t2([mp.mpf(0), mp.mpf(1), mp.mpf(0)], 1, 0, 0)
    c_g2_hd_yu = (u_g2_11 - u_g2_10) - (u110 - u100)

    u_g1_11, _, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 1, 1, 0)
    u_g1_10, _, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 1, 0, 0)
    c_g1_hd_yu = (u_g1_11 - u_g1_10) - (u110 - u100)

    _, d110, _ = b2_t2(g0, 1, 1, 0)
    _, d_g1_11, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 1, 1, 0)
    _, d_g1_01, _ = b2_t2([mp.mpf(1), mp.mpf(0), mp.mpf(0)], 0, 1, 0)
    c_g1_hu_yd = (d_g1_11 - d_g1_01) - (d110 - d010)

    ce15 = [
        ("yt5", c_yt5, mp.mpf(-12)),
        ("yt3_yb2", c_yt3yb2, Q(-5, 2)),
        ("yt_yb4", c_ytyb4, Q(-5, 2)),
        ("yt_yb2_ytau2", c_ytyb2ytau2, Q(-3, 4)),
        ("ytau3_yb2", c_ytau3yb2, Q(-27, 4)),
        ("ytau_yt2_yb2", c_ytauyt2yb2, Q(-9, 4)),
        ("ytau5", c_ytau5, mp.mpf(-3)),
        ("g1_4_yu", c_g1_4_u, Q(1267, 600)),
        ("g1_4_yd", c_g1_4_d, Q(-113, 600)),
        ("g1_4_ye", c_g1_4_e, Q(1449, 200)),
        ("g2_4_yu", c_g2_4_u, Q(-21, 4)),
        ("g3_2_hd_yu", c_g3_hd_yu, Q(16, 3)),
        ("g2_2_hd_yu", c_g2_hd_yu, Q(33, 16)),
        ("g1_2_hd_yu", c_g1_hd_yu, Q(-41, 240)),
        ("g1_2_hu_yd", c_g1_hu_yd, Q(-53, 240)),
    ]
    ce_max_err = max(abs(got - exp) for _, got, exp in ce15)
    return arason_max_err, ce_max_err


def audit_2_ow20_a(d20, d19, discrepancies):
    ow20_a = d20["OW20_A_type2_2hdm_rge_and_2flav_lepto"]
    blk_int = ow20_a["type2_2hdm_noncommuting_3x3_integration"]
    blk_1hdm = ow20_a["f_ow18_01_1hdm_bug_and_benchmark"]
    blk_lep = ow20_a["f_c30_08_two_flavor_leptogenesis"]

    # UV Benchmark 1 (Concrete Non-Commuting Rational 3x3)
    g0 = [Q(13, 25), Q(13, 25), Q(13, 25)]
    l0 = [Q(1, 5), Q(1, 4), Q(1, 10), Q(-1, 20)]
    z = mp.mpc(0, 0)
    Yu0 = [
        [Q(1, 10), Q(1, 20), z],
        [Q(1, 15), Q(1, 5), Q(1, 12)],
        [z, Q(1, 25), Q(3, 5)],
    ]
    Yd0 = [
        [Q(1, 12), Q(-1, 15), Q(1, 30)],
        [Q(1, 10), Q(1, 4), z],
        [Q(1, 20), Q(1, 16), Q(2, 5)],
    ]
    Ye0 = [
        [Q(1, 20), z, z],
        [z, Q(1, 10), z],
        [z, z, Q(3, 10)],
    ]

    # 1HDM commutator bug residual & Arason/Chowdhury-Eberhardt 1x1 benchmarks
    b_lx = beta_yu_1hdm_pure_yukawa(Yu0, Yd0, Ye0, buggy_ordering=False)
    b_bug = beta_yu_1hdm_pure_yukawa(Yu0, Yd0, Ye0, buggy_ordering=True)
    diff_bug = m3_add(b_bug, b_lx, mp.mpf(-1))
    Hu0 = m3_mul(Yu0, m3_H(Yu0))
    Hd0 = m3_mul(Yd0, m3_H(Yd0))
    comm_expected = m3_scale(m3_mul(m3_add(m3_mul(Hd0, Hu0), m3_mul(Hu0, Hd0), mp.mpf(-1)), Yu0), Q(3, 4))
    comm_resid = m3_frob(diff_bug, comm_expected)
    bug_frob = m3_frob(diff_bug)
    bug_frob_diff = abs(bug_frob - mp.mpf(blk_1hdm["buggy_minus_lx_frob"]))

    arason_err, ce15_err = extract_1x1_benchmarks()
    if comm_resid >= pow10(-35):
        discrepancies.append("1HDM commutator residual >= 1e-35")
    if bug_frob_diff >= pow10(-11):
        discrepancies.append("1HDM buggy_minus_lx_frob mismatch vs JSON")
    if arason_err >= pow10(-38):
        discrepancies.append("Arason/Buttazzo 1x1 benchmark err >= 1e-38")
    if ce15_err >= pow10(-38):
        discrepancies.append("Chowdhury-Eberhardt 15-coeff benchmark err >= 1e-38")

    # Benchmark 1 GL4 (N = 40, dt = -10)
    st_b1_ir, b1_fp_resid = gl4_integrate(rhs_type2_2hdm, (g0, l0, Yu0, Yd0, Ye0), mp.mpf(-10), 40)
    g_ir, l_ir, Yu_ir, Yd_ir, Ye_ir = st_b1_ir
    Yu_ref = parse_json_mat3(blk_int["Yu_ir_N120"])
    Yd_ref = parse_json_mat3(blk_int["Yd_ir_N120"])
    Ye_ref = parse_json_mat3(blk_int["Ye_ir_N120"])
    g_ref = [mp.mpf(x) for x in blk_int["g_ir_N120"]]
    l_ref = [mp.mpf(x) for x in blk_int["lam_ir_N120"]]

    b1_Yu_err = m3_frob(Yu_ir, Yu_ref)
    b1_Yd_err = m3_frob(Yd_ir, Yd_ref)
    b1_Ye_err = m3_frob(Ye_ir, Ye_ref)
    b1_g_err = max(abs(g_ir[i] - g_ref[i]) for i in range(3))
    b1_l_err = max(abs(l_ir[i] - l_ref[i]) for i in range(4))

    ckm_b1_uv, _ = ckm_abs_ascending(Yu0, Yd0)
    ckm_b1_ir, _ = ckm_abs_ascending(Yu_ir, Yd_ir)
    vcb_uv = ckm_b1_uv[1]
    vcb_ir = ckm_b1_ir[1]
    vcb_uv_err = abs(vcb_uv - mp.mpf(blk_int["vcb_uv"]))
    vcb_ir_err = abs(vcb_ir - mp.mpf(blk_int["vcb_ir_2hdm"]))

    if b1_fp_resid >= pow10(-35):
        discrepancies.append("GL4 Benchmark 1 fixed-point residual >= 1e-35")
    if max(b1_Yu_err, b1_Yd_err, b1_Ye_err, b1_g_err, b1_l_err) >= pow10(-11):
        discrepancies.append("GL4 Benchmark 1 countercheck err >= 1e-11")
    if vcb_uv_err >= pow10(-12) or vcb_ir_err >= pow10(-11):
        discrepancies.append("Benchmark 1 vcb_uv or vcb_ir_2hdm mismatch")

    # 1HDM vs Type-II 2HDM CKM running sign reversal on GL4 step (dt = -1)
    st_1hdm_step, _ = gl4_integrate(rhs_1hdm_1loop_ckm_compare, (g0, l0, Yu0, Yd0, Ye0), mp.mpf(-1), 8)
    st_2hdm_step, _ = gl4_integrate(rhs_type2_2hdm, (g0, l0, Yu0, Yd0, Ye0), mp.mpf(-1), 8)
    dvcb_1hdm = ckm_abs_ascending(st_1hdm_step[2], st_1hdm_step[3])[0][1] - vcb_uv
    dvcb_2hdm = ckm_abs_ascending(st_2hdm_step[2], st_2hdm_step[3])[0][1] - vcb_uv
    ckm_sign_reverses = (dvcb_1hdm < mp.mpf(0)) and (dvcb_2hdm > mp.mpf(0))
    if not ckm_sign_reverses:
        discrepancies.append("1HDM vs Type-II 2HDM CKM running sign did not reverse")

    # Benchmark 2: Synergy S-1 Complex Non-Commuting 3x3 UV -> IR (GL4 N = 30, dt = -10)
    L2 = mp.mpf(d19["OW19_A_2d_hyperbolic_kahler_and_lepto"]["fuchsian_tau8_plus"]["L2_from_bc_rich"])
    Ke2 = [mp.mpf(x) for x in d19["OW19_A_2d_hyperbolic_kahler_and_lepto"]["kahler_2d_hyperbolic"]["K_e2_hyp_theta4_theta2_theta3"]]
    tau_p = mp.mpc(Q(16, 5), Q(8, 5))
    tau_m = mp.mpc(Q(-16, 5), Q(8, 5))
    pc_p = tau_precompute(tau_p, L2)
    pc_m = tau_precompute(tau_m, L2)
    om3, om4 = synergy_weights()
    p3_p = (Fraction(1, 5), Fraction(2, 5))
    p4_p = (Fraction(1, 6), Fraction(1, 6))
    p3_m = (Fraction(1, 5), Fraction(-2, 5))
    p4_m = (Fraction(1, 6), Fraction(-1, 6))

    s1_Yu_uv = dress_Yeff(weave_Y0(pc_p, p3_p, p4_p, om3, om4, 1, -4))
    s1_Yd_uv = dress_Yeff(weave_Y0(pc_p, p3_p, p4_p, om3, om4, 1, 2))
    s1_Ye_uv = dress_Yeff(weave_Y0(pc_p, p3_p, p4_p, om3, om4, -3, 6))

    st_s1_ir, s1_fp_resid = gl4_integrate(rhs_type2_2hdm, (g0, l0, s1_Yu_uv, s1_Yd_uv, s1_Ye_uv), mp.mpf(-10), 30)
    _, _, s1_Yu_ir, s1_Yd_ir, s1_Ye_ir = st_s1_ir

    s1_Yu_ref = parse_json_mat3(blk_int["synergy_s1_Yu_ir_N80"])
    s1_Yd_ref = parse_json_mat3(blk_int["synergy_s1_Yd_ir_N80"])
    s1_Ye_ref = parse_json_mat3(blk_int["synergy_s1_Ye_ir_N80"])
    s1_Yu_err = m3_frob(s1_Yu_ir, s1_Yu_ref)
    s1_Yd_err = m3_frob(s1_Yd_ir, s1_Yd_ref)
    s1_Ye_err = m3_frob(s1_Ye_ir, s1_Ye_ref)

    s1_ckm_uv, _ = ckm_abs_ascending(s1_Yu_uv, s1_Yd_uv)
    s1_ckm_ir, _ = ckm_abs_ascending(s1_Yu_ir, s1_Yd_ir)
    s1_ckm_uv_ref = [mp.mpf(x) for x in blk_int["synergy_s1_ckm_uv_12_23_13"]]
    s1_ckm_ir_ref = [mp.mpf(x) for x in blk_int["synergy_s1_ckm_ir_12_23_13"]]
    s1_ckm_uv_err = max(abs(s1_ckm_uv[i] - s1_ckm_uv_ref[i]) for i in range(3))
    s1_ckm_ir_err = max(abs(s1_ckm_ir[i] - s1_ckm_ir_ref[i]) for i in range(3))

    if s1_fp_resid >= pow10(-35):
        discrepancies.append("GL4 Synergy S-1 fixed-point residual >= 1e-35")
    if max(s1_Yu_err, s1_Yd_err, s1_Ye_err) >= pow10(-10):
        discrepancies.append("GL4 Synergy S-1 3x3 IR matrix err >= 1e-10")
    if s1_ckm_uv_err >= pow10(-12) or s1_ckm_ir_err >= pow10(-10):
        discrepancies.append("Synergy S-1 CKM UV/IR mismatch vs JSON")

    # 10-trial disjoint SplitMix64 Haar U(3)^3 (+ U(3)^2 lepton) covariance on GL4 flow
    rng = SplitMix64(0xA202020261122001)
    base_st, _ = gl4_integrate(rhs_type2_2hdm, (g0, l0, s1_Yu_uv, s1_Yd_uv, s1_Ye_uv), mp.mpf(-4), 8)
    base_ckm, _ = ckm_abs_ascending(base_st[2], base_st[3])
    haar_max_frob = mp.mpf(0)
    haar_max_ckm = mp.mpf(0)
    haar_max_unit_err = mp.mpf(0)
    for _trial in range(10):
        UQ, eQ = haar_u3(rng)
        Uu, eu = haar_u3(rng)
        Ud, ed = haar_u3(rng)
        UL, eL = haar_u3(rng)
        Ue, ee = haar_u3(rng)
        haar_max_unit_err = max(haar_max_unit_err, eQ, eu, ed, eL, ee)
        Yu_rot = m3_mul(m3_mul(UQ, s1_Yu_uv), m3_H(Uu))
        Yd_rot = m3_mul(m3_mul(UQ, s1_Yd_uv), m3_H(Ud))
        Ye_rot = m3_mul(m3_mul(UL, s1_Ye_uv), m3_H(Ue))
        rot_st, _ = gl4_integrate(rhs_type2_2hdm, (g0, l0, Yu_rot, Yd_rot, Ye_rot), mp.mpf(-4), 8)
        exp_Yu = m3_mul(m3_mul(UQ, base_st[2]), m3_H(Uu))
        exp_Yd = m3_mul(m3_mul(UQ, base_st[3]), m3_H(Ud))
        exp_Ye = m3_mul(m3_mul(UL, base_st[4]), m3_H(Ue))
        frob_err = max(
            m3_frob(rot_st[2], exp_Yu),
            m3_frob(rot_st[3], exp_Yd),
            m3_frob(rot_st[4], exp_Ye),
        )
        rot_ckm, _ = ckm_abs_ascending(rot_st[2], rot_st[3])
        ckm_err = max(abs(rot_ckm[i] - base_ckm[i]) for i in range(3))
        if frob_err > haar_max_frob:
            haar_max_frob = frob_err
        if ckm_err > haar_max_ckm:
            haar_max_ckm = ckm_err
    if haar_max_frob >= pow10(-30) or haar_max_ckm >= pow10(-30):
        discrepancies.append("10-trial Haar U(3)^3 GL4 covariance drift >= 1e-30")

    # 2-flavor vs 3-flavor leptogenesis (+ and - mirrors, flat and 2D E[2], rad and tree)
    c_rad = Q(1, 50)
    lep_runs = {}
    for sign_tag, pc, p3, p4 in (("plus", pc_p, p3_p, p4_p), ("minus", pc_m, p3_m, p4_m)):
        Ye_flat = dress_Yeff(weave_Y0(pc, p3, p4, om3, om4, -3, 6))
        Ynu_flat = szego_Y(pc, p3, -3, 0)
        MR_tree_flat = szego_Y(pc, (Fraction(0, 1), Fraction(0, 1)), 0, 0)
        Hnu_flat = m3_mul(m3_H(Ynu_flat), Ynu_flat)
        MR_rad_flat = m3_add(m3_eye(mp.mpf(1)), m3_add(Hnu_flat, m3_T(Hnu_flat)), -c_rad)

        Ye_2d = canonicalize_K(Ye_flat, Ke2)
        Ynu_2d = canonicalize_K(Ynu_flat, Ke2)
        MR_tree_2d = canonicalize_K(MR_tree_flat, Ke2)
        Hnu_2d = m3_mul(m3_H(Ynu_2d), Ynu_2d)
        MR_rad_2d = m3_add(m3_eye(mp.mpf(1)), m3_add(Hnu_2d, m3_T(Hnu_2d)), -c_rad)

        lep_runs[("rad_flat", sign_tag)] = compute_leptogenesis_observables(Ye_flat, Ynu_flat, MR_rad_flat)
        lep_runs[("rad_2d_e2", sign_tag)] = compute_leptogenesis_observables(Ye_2d, Ynu_2d, MR_rad_2d)
        lep_runs[("tree_flat", sign_tag)] = compute_leptogenesis_observables(Ye_flat, Ynu_flat, MR_tree_flat)
        lep_runs[("tree_2d_e2", sign_tag)] = compute_leptogenesis_observables(Ye_2d, Ynu_2d, MR_tree_2d)

    max_lep_decomp_err = max(v["max_decomp_err"] for v in lep_runs.values())
    if max_lep_decomp_err >= pow10(-32):
        discrepancies.append("Leptogenesis SVD/Takagi residual >= 1e-32")

    rad_flat_p = lep_runs[("rad_flat", "plus")]
    rad_2d_p = lep_runs[("rad_2d_e2", "plus")]
    tree_flat_p = lep_runs[("tree_flat", "plus")]
    tree_2d_p = lep_runs[("tree_2d_e2", "plus")]

    lep_checks = {
        "rad_flat_yb_2f_plus": (rad_flat_p["yb_2f"], mp.mpf(blk_lep["rad_flat_yb_2f_plus"])),
        "rad_flat_yb_3f_plus": (rad_flat_p["yb_3f"], mp.mpf(blk_lep["rad_flat_yb_3f_plus"])),
        "rad_flat_ratio_2f_over_3f": (rad_flat_p["yb_2f"] / rad_flat_p["yb_3f"], mp.mpf(blk_lep["rad_flat_ratio_2f_over_3f"])),
        "rad_2d_e2_yb_2f_plus": (rad_2d_p["yb_2f"], mp.mpf(blk_lep["rad_2d_e2_yb_2f_plus"])),
        "rad_2d_e2_yb_3f_plus": (rad_2d_p["yb_3f"], mp.mpf(blk_lep["rad_2d_e2_yb_3f_plus"])),
        "tree_flat_eps_emu_plus": (tree_flat_p["eps_emu"], mp.mpf(blk_lep["tree_flat_eps_emu_plus"])),
        "tree_flat_yb_2f_plus": (tree_flat_p["yb_2f"], mp.mpf(blk_lep["tree_flat_yb_2f_plus"])),
        "tree_flat_yb_3f_plus": (tree_flat_p["yb_3f"], mp.mpf(blk_lep["tree_flat_yb_3f_plus"])),
        "tree_2d_e2_yb_2f_plus": (tree_2d_p["yb_2f"], mp.mpf(blk_lep["tree_2d_e2_yb_2f_plus"])),
        "tree_2d_e2_yb_3f_plus": (tree_2d_p["yb_3f"], mp.mpf(blk_lep["tree_2d_e2_yb_3f_plus"])),
    }
    lep_rel_errs = {}
    for key, (got, exp) in lep_checks.items():
        rerr = abs(got - exp) / abs(exp)
        lep_rel_errs[key] = mp.nstr(rerr, 6)
        if rerr >= pow10(-9):
            discrepancies.append("Leptogenesis rel err >= 1e-9 on " + key)

    mirror_errs = {}
    for mode in ("rad_flat", "rad_2d_e2", "tree_flat", "tree_2d_e2"):
        s_err = abs(lep_runs[(mode, "plus")]["yb_2f"] + lep_runs[(mode, "minus")]["yb_2f"])
        mirror_errs[mode] = mp.nstr(s_err, 6)
        if s_err >= pow10(-35):
            discrepancies.append("Leptogenesis mirror antisymmetry failed on " + mode)

    # Confirm sign flips: rad 2f > 0, tree 2f < 0 on both flat and 2D E[2]
    lep_signs_ok = (
        rad_flat_p["yb_2f"] > mp.mpf(0)
        and rad_2d_p["yb_2f"] > mp.mpf(0)
        and tree_flat_p["yb_2f"] < mp.mpf(0)
        and tree_2d_p["yb_2f"] < mp.mpf(0)
        and tree_flat_p["eps_emu"] > mp.mpf(0)
    )
    if not lep_signs_ok:
        discrepancies.append("Leptogenesis qualitative sign pattern failed")

    return {
        "benchmark1_gl4_N40": {
            "Yu_ir_frob_err": mp.nstr(b1_Yu_err, 6),
            "Yd_ir_frob_err": mp.nstr(b1_Yd_err, 6),
            "Ye_ir_frob_err": mp.nstr(b1_Ye_err, 6),
            "g_ir_max_err": mp.nstr(b1_g_err, 6),
            "lam_ir_max_err": mp.nstr(b1_l_err, 6),
            "vcb_uv_err": mp.nstr(vcb_uv_err, 6),
            "vcb_ir_2hdm_err": mp.nstr(vcb_ir_err, 6),
            "max_gl4_fp_resid": mp.nstr(b1_fp_resid, 6),
        },
        "benchmark2_synergy_s1_gl4_N30": {
            "Yu_ir_frob_err": mp.nstr(s1_Yu_err, 6),
            "Yd_ir_frob_err": mp.nstr(s1_Yd_err, 6),
            "Ye_ir_frob_err": mp.nstr(s1_Ye_err, 6),
            "ckm_uv_max_err": mp.nstr(s1_ckm_uv_err, 6),
            "ckm_ir_max_err": mp.nstr(s1_ckm_ir_err, 6),
            "max_gl4_fp_resid": mp.nstr(s1_fp_resid, 6),
        },
        "1hdm_and_literature_benchmarks": {
            "three_quarters_commutator_resid": mp.nstr(comm_resid, 6),
            "buggy_minus_lx_frob_diff": mp.nstr(bug_frob_diff, 6),
            "arason_buttazzo_1x1_max_err": mp.nstr(arason_err, 6),
            "chowdhury_eberhardt_15coeff_max_err": mp.nstr(ce15_err, 6),
            "dvcb_1hdm_gl4_step": mp.nstr(dvcb_1hdm, 8),
            "dvcb_2hdm_gl4_step": mp.nstr(dvcb_2hdm, 8),
            "ckm_running_sign_reverses": ckm_sign_reverses,
        },
        "haar_10trial_gl4_covariance": {
            "max_frob_err": mp.nstr(haar_max_frob, 6),
            "max_ckm_err": mp.nstr(haar_max_ckm, 6),
            "max_unitarity_err": mp.nstr(haar_max_unit_err, 6),
        },
        "two_flavor_leptogenesis": {
            "rel_errors_vs_ow20": lep_rel_errs,
            "mirror_antisymmetry_abs_errors": mirror_errs,
            "max_svd_takagi_err": mp.nstr(max_lep_decomp_err, 6),
            "signs_rad_pos_tree_neg_ok": lep_signs_ok,
        },
    }, {
        "g0": g0,
        "l0": l0,
        "Yu0": Yu0,
        "Yd0": Yd0,
        "Ye0": Ye0,
        "Yu_ref": Yu_ref,
        "pc_p": pc_p,
        "om3": om3,
        "om4": om4,
        "p3_p": p3_p,
        "p4_p": p4_p,
    }


# ============================================================================
# MODULE 3: OW20-B — 1D Eliminated Ridder/Bisection FRG & E_6 Algebra
# ============================================================================

def frg_1d_ridder_solve(Ns, Nw, Nv, fW, lam_lo, lam_hi):
    """Eliminate g(lam) = -2/(b1(lam) - 2 b2(lam)) and solve beta_lam(g(lam), lam) = 0 via Ridder's method."""
    Mg = mp.mpf(Ns) + fW * mp.mpf(Nw) - mp.mpf(4 * Nv)

    def b1(lam):
        d = mp.mpf(1) - mp.mpf(2) * lam
        return (mp.mpf(1) / (mp.mpf(3) * mp.pi)) * (mp.mpf(5) / d - mp.mpf(9) / (d * d) - mp.mpf(7)) + Mg / (mp.mpf(6) * mp.pi)

    def b2(lam):
        d = mp.mpf(1) - mp.mpf(2) * lam
        return -(mp.mpf(1) / (mp.mpf(12) * mp.pi)) * (mp.mpf(5) / d - mp.mpf(6) / (d * d))

    def g_of_lam(lam):
        return mp.mpf(-2) / (b1(lam) - mp.mpf(2) * b2(lam))

    def beta_lam_eq(g, lam):
        d = mp.mpf(1) - mp.mpf(2) * lam
        eta = g * b1(lam) / (mp.mpf(1) - g * b2(lam))
        grav = (mp.mpf(5) / d) * (mp.mpf(1) - eta / mp.mpf(6)) - mp.mpf(4)
        mat = mp.mpf(Ns - 2 * Nw + 2 * Nv) / mp.mpf(2)
        return (eta - mp.mpf(2)) * lam + (g / (mp.mpf(2) * mp.pi)) * (grav + mat)

    def F(lam):
        return beta_lam_eq(g_of_lam(lam), lam)

    a, b = lam_lo, lam_hi
    fa, fb = F(a), F(b)
    if fa * fb > mp.mpf(0):
        raise ValueError("FRG 1D bracket does not straddle a root")

    tol = pow10(-42)
    root = (a + b) / mp.mpf(2)
    for _ in range(120):
        m = (a + b) / mp.mpf(2)
        fm = F(m)
        if abs(fm) < tol or abs(b - a) < tol:
            root = m
            break
        # Ridder exponential interpolation step
        s_arg = fm * fm - fa * fb
        if s_arg <= mp.mpf(0):
            # Bisection fallback
            if fa * fm <= mp.mpf(0):
                b, fb = m, fm
            else:
                a, fa = m, fm
            root = (a + b) / mp.mpf(2)
            continue
        s = mp.sqrt(s_arg)
        sgn = mp.mpf(1) if fa >= fb else mp.mpf(-1)
        x = m + (m - a) * sgn * fm / s
        fx = F(x)
        root = x
        if abs(fx) < tol:
            break
        if fm * fx < mp.mpf(0):
            a, fa, b, fb = m, fm, x, fx
        elif fa * fx < mp.mpf(0):
            b, fb = x, fx
        else:
            a, fa = x, fx
        if a > b:
            a, fa, b, fb = b, fb, a, fa
        if abs(b - a) < tol:
            break

    lam_star = root
    g_star = g_of_lam(lam_star)
    eta_star = g_star * b1(lam_star) / (mp.mpf(1) - g_star * b2(lam_star))
    eta_resid = abs(eta_star + mp.mpf(2))
    blam_resid = abs(beta_lam_eq(g_star, lam_star))
    d_star = mp.mpf(1) - mp.mpf(2) * lam_star
    f_lam_dD = (mp.mpf(20) * g_star) / (mp.mpf(3) * mp.pi * d_star * d_star)
    return g_star, lam_star, f_lam_dD, eta_resid, blam_resid


def quad_2hdm_pure_gauge(f_lam, g_val):
    """Pure-gauge 2HDM 1-loop quartic quadratic: 12 lam^2 + (16 pi^2 f_lam - 54/5 g^2) lam + 171/50 g^4 = 0."""
    A = mp.mpf(12)
    b0 = -Q(54, 5) * g_val * g_val
    B = mp.mpf(16) * mp.pi * mp.pi * f_lam + b0
    C = Q(171, 50) * (g_val ** 4)
    disc = B * B - mp.mpf(4) * A * C
    f_crit = (mp.mpf(2) * mp.sqrt(A * C) - b0) / (mp.mpf(16) * mp.pi * mp.pi)
    roots = []
    if disc >= mp.mpf(0):
        sq = mp.sqrt(disc)
        roots = [(-B + sq) / (mp.mpf(2) * A), (-B - sq) / (mp.mpf(2) * A)]
    return f_crit, disc, roots


def audit_3_ow20_b(d20, d18, discrepancies):
    ow20_b = d20["OW20_B_consistent_frg_higgs_audit_and_e6"]
    frg_ref = ow20_b["f_ow18_02_consistent_frg_gsm_2hdm"]
    higgs_ref = ow20_b["f_ow18_03_prose_vs_json_higgs_audit"]
    e6_ref = ow20_b["f_ow18_05_and_f_c30_01_e6_nw81_and_z4"]

    g_uv = Q(13, 25)
    g1, l1, fl1, eta_r1, bl_r1 = frg_1d_ridder_solve(8, 48, 12, Q(-1, 2), mp.mpf(-2), mp.mpf(0))
    g2, l2, fl2, eta_r2, bl_r2 = frg_1d_ridder_solve(8, 48, 12, mp.mpf(1), mp.mpf(-15), mp.mpf(-5))

    f_crit, disc_t1, roots_t1 = quad_2hdm_pure_gauge(fl1, g_uv)
    _, disc_t2, roots_t2 = quad_2hdm_pure_gauge(fl2, g_uv)

    Mg_t1 = Fraction(8, 1) + Fraction(-1, 2) * 48 - 4 * 12
    Mg_t2 = Fraction(8, 1) + Fraction(1, 1) * 48 - 4 * 12

    fc_err = abs(f_crit - mp.mpf(frg_ref["f_crit_2hdm_g052"]))
    fl1_err = abs(fl1 - mp.mpf(frg_ref["type1_f_lam_dD"]))
    fl2_err = abs(fl2 - mp.mpf(frg_ref["type2_f_lam_dD"]))
    d1_err = abs(disc_t1 - mp.mpf(frg_ref["type1_disc"]))
    d2_err = abs(disc_t2 - mp.mpf(frg_ref["type2_disc"]))
    r_ref = [mp.mpf(x) for x in frg_ref["type1_roots_both_negative"]]
    roots_err = max(abs(roots_t1[0] - r_ref[0]), abs(roots_t1[1] - r_ref[1])) if len(roots_t1) == 2 else mp.mpf(1)

    no_pos_fp = (
        len(roots_t1) == 2
        and roots_t1[0] < mp.mpf(0)
        and roots_t1[1] < mp.mpf(0)
        and disc_t2 < mp.mpf(0)
        and len(roots_t2) == 0
    )

    if max(eta_r1, bl_r1, eta_r2, bl_r2) >= pow10(-38):
        discrepancies.append("FRG 1D Ridder root residuals >= 1e-38")
    if max(fc_err, fl1_err, fl2_err, d1_err, d2_err, roots_err) >= pow10(-10):
        discrepancies.append("FRG Type-I/Type-II observables mismatch vs JSON")
    if str(Mg_t1) != frg_ref["type1_fW_neg_half_Mg"] or str(Mg_t2) != frg_ref["type2_fW_pos1_Mg"]:
        discrepancies.append("FRG M_g exact rational mismatch")
    if not no_pos_fp:
        discrepancies.append("FRG no-positive-FP verification failed")

    # F-OW18-03: direct read from sealed a2_ow18_v3_results.json vs prose numbers
    ewsb18 = d18["ow18_b"]["bridge_b3s02_conformal_instanton_ewsb_on_yb_high"]
    mh0_18 = mp.mpf(ewsb18["mh0_over_v"])
    mH0_18 = mp.mpf(ewsb18["mH0_over_v"])
    mHpm_18 = mp.mpf(ewsb18["mHpm_over_v"])
    prose_mH0 = Q(95547910, 10 ** 8)
    prose_mHpm = Q(94624861, 10 ** 8)
    rel_err_mH0 = (prose_mH0 - mH0_18) / mH0_18
    rel_err_mHpm = (prose_mHpm - mHpm_18) / mHpm_18

    higgs_mH0_diff = abs(rel_err_mH0 - mp.mpf(higgs_ref["prose_mH0_rel_err"]))
    higgs_mHpm_diff = abs(rel_err_mHpm - mp.mpf(higgs_ref["prose_mHpm_rel_err"]))
    sealed_list_diff = max(
        abs(mh0_18 - mp.mpf(higgs_ref["sealed_json_mh0_mH0_mHpm"][0])),
        abs(mH0_18 - mp.mpf(higgs_ref["sealed_json_mh0_mH0_mHpm"][1])),
        abs(mHpm_18 - mp.mpf(higgs_ref["sealed_json_mh0_mH0_mHpm"][2])),
    )
    if max(higgs_mH0_diff, higgs_mHpm_diff, sealed_list_diff) >= pow10(-8):
        discrepancies.append("F-OW18-03 prose vs sealed JSON Higgs audit mismatch")

    # E_6 N_W = 81 & Z_4 M_R == 0 selection rule
    tr_3x16 = 3 * (16 * 1)
    tr_3x27 = 3 * (16 * 1 + 10 * (-2) + 1 * 4)
    Mg_e6_dep = Fraction(8, 1) + Fraction(1, 1) * 81 - 4 * 12
    Mg_e6_dp = Fraction(8, 1) + Fraction(-1, 2) * 81 - 4 * 12
    breaks_dep = Mg_e6_dep > 31
    z4_forbids_mr = all(((2 + 4 * n) % 4) != 0 for n in range(-25, 26))
    pm_16H = (-1) ** (3 * 1 + 0)
    pm_126bar = (-1) ** (3 * (-2) + 0)
    qpsi_16_16_126bar = 1 + 1 + (-2)

    if (
        tr_3x16 != e6_ref["Tr_Qpsi_3x16"]
        or tr_3x27 != e6_ref["Tr_Qpsi_3x27"]
        or str(Mg_e6_dep) != e6_ref["Mg_GSM_2H_NW81_DEP_Type2"]
        or str(Mg_e6_dp) != e6_ref["Mg_GSM_2H_NW81_DP_Type1"]
        or (not breaks_dep)
        or (not z4_forbids_mr)
        or pm_16H != -1
        or pm_126bar != 1
        or qpsi_16_16_126bar != 0
    ):
        discrepancies.append("E_6 N_W=81 / Z_4 M_R==0 / P_M verification failed")

    return {
        "frg_1d_ridder": {
            "f_crit_err": mp.nstr(fc_err, 6),
            "type1_g_star": mp.nstr(g1, 12),
            "type1_lam_star": mp.nstr(l1, 12),
            "type1_f_lam_err": mp.nstr(fl1_err, 6),
            "type1_disc": mp.nstr(disc_t1, 12),
            "type1_disc_err": mp.nstr(d1_err, 6),
            "type1_roots_err": mp.nstr(roots_err, 6),
            "type1_max_eq_resid": mp.nstr(max(eta_r1, bl_r1), 6),
            "type2_g_star": mp.nstr(g2, 12),
            "type2_lam_star": mp.nstr(l2, 12),
            "type2_f_lam_err": mp.nstr(fl2_err, 6),
            "type2_disc": mp.nstr(disc_t2, 12),
            "type2_disc_err": mp.nstr(d2_err, 6),
            "type2_max_eq_resid": mp.nstr(max(eta_r2, bl_r2), 6),
            "no_positive_pure_gauge_uv_fp_either_scheme": no_pos_fp,
        },
        "f_ow18_03_higgs_prose_audit": {
            "prose_mH0_rel_err": mp.nstr(rel_err_mH0, 10),
            "prose_mHpm_rel_err": mp.nstr(rel_err_mHpm, 10),
            "max_diff_vs_ow20": mp.nstr(max(higgs_mH0_diff, higgs_mHpm_diff, sealed_list_diff), 6),
        },
        "e6_nw81_and_z4": {
            "Tr_Qpsi_3x16": tr_3x16,
            "Tr_Qpsi_3x27": tr_3x27,
            "Mg_DEP_Type2": str(Mg_e6_dep),
            "Mg_DP_Type1": str(Mg_e6_dp),
            "breaks_DEP_lt_31": breaks_dep,
            "Z4_forbids_MR_identically": z4_forbids_mr,
            "PM_16H": pm_16H,
            "PM_126bar": pm_126bar,
            "Qpsi_16_16_126bar": qpsi_16_16_126bar,
        },
    }, {"disc_t1": disc_t1, "disc_t2": disc_t2}


# ============================================================================
# MODULE 4: OW20-C — Synergy 144->2, SL(2,Z) Conjugacy, Direct Weight-Lattice SO(2d)
# ============================================================================

def count_primitive_antipodal_pairs(N):
    prim = []
    for a in range(N):
        for b in range(N):
            g = math.gcd(N, math.gcd(a, b))
            if g == 1:
                prim.append((a, b))
    pairs = set()
    for a, b in prim:
        neg = ((-a) % N, (-b) % N)
        pairs.add(min((a, b), neg))
    return len(prim), len(pairs)


def mat2_int_mul(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat2_int_inv_sl2(g):
    det = g[0][0] * g[1][1] - g[0][1] * g[1][0]
    if det != 1:
        raise ValueError("Not in SL(2, Z)")
    return [[g[1][1], -g[0][1]], [-g[1][0], g[0][0]]]


def ker_M_plus_I_mod(M, N):
    pts = set()
    for a in range(N):
        for b in range(N):
            r0 = ((M[0][0] + 1) * a + M[0][1] * b) % N
            r1 = (M[1][0] * a + (M[1][1] + 1) * b) % N
            if r0 == 0 and r1 == 0:
                pts.add((a, b))
    return pts


def apply_mat2_mod(g, pts, N):
    return {((g[0][0] * a + g[0][1] * b) % N, (g[1][0] * a + g[1][1] * b) % N) for (a, b) in pts}


def so2d_cubic_anomaly_weight_lattice(d):
    """
    Direct 2^{d-1} half-spinor weight-lattice cubic trace for SO(2d) -> SU(d)^3.
    Uses fundamental SU(d) diagonal generator H = (1, ..., 1, -(d-1)) with Tr_fund(H^3) = -d(d-1)(d-2).
    Half-spinor S_+ = bigoplus_{k even} Lambda^k(C^d) corresponds to weight vectors s in {+1/2, -1/2}^d
    with even number k of +1/2 entries (so H(s) = sum_{j: s_j=+1/2} H_j since sum H_j = 0).
    Also computes the conjugate chirality (even number of -1/2 entries) as a cross-check.
    """
    H = [1] * (d - 1) + [-(d - 1)]
    tr_fund_H3 = sum(h ** 3 for h in H)
    # Direct enumeration of all 2^d sign vectors s in {+1/2, -1/2}^d
    tr_even_plus = 0
    tr_even_minus = 0
    count_even_plus = 0
    count_even_minus = 0
    for mask in range(1 << d):
        k_plus = mask.bit_count()
        k_minus = d - k_plus
        # Exact weight inner product 2 * (s . H) = sum_{bit j=1} H_j - sum_{bit j=0} H_j = 2 * sum_{bit j=1} H_j
        hs = 0
        for j in range(d):
            if (mask >> j) & 1:
                hs += H[j]
        hs3 = hs * hs * hs
        if k_plus % 2 == 0:
            tr_even_plus += hs3
            count_even_plus += 1
        if k_minus % 2 == 0:
            tr_even_minus += hs3
            count_even_minus += 1
    expected_dim = 1 << (d - 1)
    if count_even_plus != expected_dim or count_even_minus != expected_dim:
        raise RuntimeError("Weight count mismatch")
    return Fraction(tr_even_plus, tr_fund_H3), Fraction(tr_even_minus, tr_fund_H3)


def audit_4_ow20_c(d20, ctx_a, discrepancies):
    ow20_c = d20["OW20_C_synergy144_and_so2d_anomalies"]
    s1_ref = ow20_c["f_ow18_06_synergy_s1_144_and_antipodal"]
    b_ref = ow20_c["f_ow18_07_spin10_brane2h_beta"]
    an_ref = ow20_c["f_ow18_08_explicit_so2d_cubic_anomalies"]

    # 1. Primitive torsion enumeration (Z/5Z)^2 & (Z/6Z)^2
    prim5, P5 = count_primitive_antipodal_pairs(5)
    prim6, P6 = count_primitive_antipodal_pairs(6)
    P5xP6 = P5 * P6
    bits_144_to_2 = mp.log(mp.mpf(P5xP6) / mp.mpf(2), mp.mpf(2))
    bits_err = abs(bits_144_to_2 - mp.mpf(s1_ref["bits_144_to_2"]))

    if P5 != 12 or P6 != 12 or P5xP6 != 144 or bits_err >= pow10(-12):
        discrepancies.append("Synergy S-1 144 -> 2 cardinality or log2(72) bits mismatch")

    # 2. Explicit SL(2, Z) conjugacy covariance ker(g M g^-1 + I) == g ker(M + I)
    L = [[1, 1], [0, 1]]
    R = [[1, 0], [1, 1]]
    T = [[1, 1], [0, 1]]
    S = [[0, -1], [1, 0]]
    LR = mat2_int_mul(L, R)  # [[2, 1], [1, 1]]
    L2R = mat2_int_mul(L, LR)  # [[3, 2], [1, 1]]
    LR2 = mat2_int_mul(LR, R)  # [[3, 1], [2, 1]]
    T3S = mat2_int_mul([[1, 3], [0, 1]], S)  # [[3, -1], [1, 0]]
    T4S = mat2_int_mul([[1, 4], [0, 1]], S)  # [[4, -1], [1, 0]]
    T4S_inv = mat2_int_inv_sl2(T4S)  # [[0, 1], [-1, 4]]

    g_t3 = T  # T (LR) T^-1 == T3S
    g_t4a = T  # T (L2R) T^-1 == T4S
    g_t4b = [[1, 0], [3, 1]]  # g_t4b (LR2) g_t4b^-1 == (T4S)^-1

    conj_t3_ok = (mat2_int_mul(mat2_int_mul(g_t3, LR), mat2_int_inv_sl2(g_t3)) == T3S)
    conj_t4a_ok = (mat2_int_mul(mat2_int_mul(g_t4a, L2R), mat2_int_inv_sl2(g_t4a)) == T4S)
    conj_t4b_ok = (mat2_int_mul(mat2_int_mul(g_t4b, LR2), mat2_int_inv_sl2(g_t4b)) == T4S_inv)

    cov_t3_ok = (ker_M_plus_I_mod(T3S, 5) == apply_mat2_mod(g_t3, ker_M_plus_I_mod(LR, 5), 5))
    cov_t4a_ok = (ker_M_plus_I_mod(T4S, 6) == apply_mat2_mod(g_t4a, ker_M_plus_I_mod(L2R, 6), 6))
    cov_t4b_ok = (ker_M_plus_I_mod(T4S_inv, 6) == apply_mat2_mod(g_t4b, ker_M_plus_I_mod(LR2, 6), 6))
    t4_inv_same_ker = (ker_M_plus_I_mod(T4S, 6) == ker_M_plus_I_mod(T4S_inv, 6))

    # Also verify exact Lefschetz joint antipodal pair count: 2 (mod 5) x 1 (mod 6) = 2
    ker_LR_5_prim_pairs = len({min(v, ((-v[0]) % 5, (-v[1]) % 5)) for v in ker_M_plus_I_mod(LR, 5) if math.gcd(5, math.gcd(v[0], v[1])) == 1})
    ker_T4S_6_prim_pairs = len({min(v, ((-v[0]) % 6, (-v[1]) % 6)) for v in ker_M_plus_I_mod(T4S, 6) if math.gcd(6, math.gcd(v[0], v[1])) == 1})
    joint_pairs = ker_LR_5_prim_pairs * ker_T4S_6_prim_pairs

    sl2z_ok = conj_t3_ok and conj_t4a_ok and conj_t4b_ok and cov_t3_ok and cov_t4a_ok and cov_t4b_ok and t4_inv_same_ker and (joint_pairs == 2)
    if not sl2z_ok:
        discrepancies.append("SL(2, Z) conjugacy covariance or Lefschetz pair count failed")

    # 3. Broken antipodal w ~ -w on coherent weave: p_3 = (1/5, 2/5) vs -p_3 = (4/5, 3/5)
    pc_p, om3, om4 = ctx_a["pc_p"], ctx_a["om3"], ctx_a["om4"]
    p3_p, p4_p = ctx_a["p3_p"], ctx_a["p4_p"]
    p3_neg = (Fraction(4, 5), Fraction(3, 5))

    Yu_p = dress_Yeff(weave_Y0(pc_p, p3_p, p4_p, om3, om4, 1, -4))
    Yd_p = dress_Yeff(weave_Y0(pc_p, p3_p, p4_p, om3, om4, 1, 2))
    Yu_m = dress_Yeff(weave_Y0(pc_p, p3_neg, p4_p, om3, om4, 1, -4))
    Yd_m = dress_Yeff(weave_Y0(pc_p, p3_neg, p4_p, om3, om4, 1, 2))

    vcb_p = ckm_abs_ascending(Yu_p, Yd_p)[0][1]
    vcb_m = ckm_abs_ascending(Yu_m, Yd_m)[0][1]
    dvcb_anti = abs(vcb_p - vcb_m)
    bth_p = mp.arg(mp.det(mat3_to_mpmatrix(Yu_p)) * mp.det(mat3_to_mpmatrix(Yd_p)))
    bth_m = mp.arg(mp.det(mat3_to_mpmatrix(Yu_m)) * mp.det(mat3_to_mpmatrix(Yd_m)))

    anti_max_err = max(
        abs(vcb_p - mp.mpf(s1_ref["vcb_p3_plus"])),
        abs(vcb_m - mp.mpf(s1_ref["vcb_p3_minus"])),
        abs(dvcb_anti - mp.mpf(s1_ref["delta_vcb_antipodal"])),
        abs(bth_p - mp.mpf(s1_ref["bar_theta_p3_plus_rad"])),
        abs(bth_m - mp.mpf(s1_ref["bar_theta_p3_minus_rad"])),
    )
    if anti_max_err >= pow10(-10):
        discrepancies.append("Synergy S-1 antipodal p_3 -> -p_3 observables mismatch vs JSON")

    # 4. Direct 2^{d-1} weight-lattice SO(2d) SU(d)^3 cubic anomalies (d = 3..15)
    anoms_even_plus = {}
    anoms_even_minus = {}
    anoms_match_ow20 = True
    for d in range(3, 16):
        ap, am = so2d_cubic_anomaly_weight_lattice(d)
        key = str(2 * d)
        if ap.denominator != 1 or am.denominator != 1:
            anoms_match_ow20 = False
        anoms_even_plus[key] = int(ap.numerator)
        anoms_even_minus[key] = int(am.numerator)
        if an_ref["so2d_SUd3_anomalies"][key] != int(ap.numerator):
            anoms_match_ow20 = False
    so6_anom_m1 = (anoms_even_plus["6"] == -1)
    so8_to_30_zero = all(anoms_even_plus[str(2 * d)] == 0 for d in range(4, 16))
    if not (anoms_match_ow20 and so6_anom_m1 and so8_to_30_zero):
        discrepancies.append("Direct weight-lattice SO(2d) cubic anomaly check failed")

    # 5. Pure-fermion Spin(10) brane-2H beta vs bulk 10_R
    b_brane2h = -Fraction(11, 3) * 8 + Fraction(2, 3) * 3 * 2
    b_bulk10r = b_brane2h + Fraction(1, 6) * 1
    b_diff = b_bulk10r - b_brane2h
    beta_ok = (
        b_brane2h == Fraction(-76, 3)
        and b_bulk10r == Fraction(-151, 6)
        and str(b_brane2h) == b_ref["b_Spin10_pure_fermion_brane2H"]
        and str(b_bulk10r) == b_ref["b_Spin10_with_bulk_10R"]
        and str(b_diff) == b_ref["diff_bulk_10R_minus_brane2H"]
    )
    if not beta_ok:
        discrepancies.append("Spin(10) brane-2H vs bulk 10_R beta mismatch")

    return {
        "synergy_144_to_2": {
            "prim5": prim5,
            "P5": P5,
            "prim6": prim6,
            "P6": P6,
            "P5_x_P6": P5xP6,
            "joint_lefschetz_pairs": joint_pairs,
            "bits_144_to_2": mp.nstr(bits_144_to_2, 14),
            "bits_err_vs_ow20": mp.nstr(bits_err, 6),
            "sl2z_conjugacy_covariance_ok": sl2z_ok,
        },
        "antipodal_p3_swap": {
            "vcb_p3_plus": mp.nstr(vcb_p, 12),
            "vcb_p3_minus": mp.nstr(vcb_m, 12),
            "delta_vcb": mp.nstr(dvcb_anti, 12),
            "bar_theta_p3_plus_rad": mp.nstr(bth_p, 12),
            "bar_theta_p3_minus_rad": mp.nstr(bth_m, 12),
            "max_err_vs_ow20": mp.nstr(anti_max_err, 6),
        },
        "so2d_weight_lattice_cubic_anomalies": {
            "even_plus_S_plus": anoms_even_plus,
            "even_minus_conjugate": anoms_even_minus,
            "SO6_is_minus1": so6_anom_m1,
            "SO8_to_SO30_all_zero": so8_to_30_zero,
            "matches_ow20_exact": anoms_match_ow20,
        },
        "spin10_beta": {
            "b_pure_fermion_brane2H": str(b_brane2h),
            "b_with_bulk_10R": str(b_bulk10r),
            "diff": str(b_diff),
            "matches_ow20_exact": beta_ok,
        },
    }, {
        "so6_anom": anoms_even_plus["6"],
        "dvcb_anti": dvcb_anti,
        "bth_p": bth_p,
        "bth_m": bth_m,
    }


# ============================================================================
# MODULE 5: A2-OW16 v6 Independent Master Ledger & Historical False-Flag Audit
# ============================================================================

def validate_v6_partition(obs_list):
    counts = {
        "DERIVED_EXACT": 0,
        "CONDITIONAL_OR_QUALITATIVE": 0,
        "INTERNAL_WALL_OR_TENSION": 0,
        "OPEN_EXTERNAL_BOUNDARY": 0,
    }
    by_id = {}
    for row in obs_list:
        b = row["bucket"]
        if b in counts:
            counts[b] += 1
        by_id[row["id"]] = row
    expected_ids = {"OBS-" + str(i).zfill(2) for i in range(1, 25)}
    ids_ok = (len(obs_list) == 24 and set(by_id.keys()) == expected_ids)
    expected_counts = {
        "DERIVED_EXACT": 1,
        "CONDITIONAL_OR_QUALITATIVE": 10,
        "INTERNAL_WALL_OR_TENSION": 9,
        "OPEN_EXTERNAL_BOUNDARY": 4,
    }
    counts_ok = (counts == expected_counts)
    derived_ids = [r["id"] for r in obs_list if r["bucket"] == "DERIVED_EXACT"]
    obs07_sole = (derived_ids == ["OBS-07"])
    obs01_open = (by_id.get("OBS-01", {}).get("bucket") == "OPEN_EXTERNAL_BOUNDARY")
    obs02_cond = (by_id.get("OBS-02", {}).get("bucket") == "CONDITIONAL_OR_QUALITATIVE")
    return {
        "counts": counts,
        "ids_unique_24": ids_ok,
        "partition_1_10_9_4": counts_ok,
        "obs07_sole_derived_exact": obs07_sole,
        "obs01_in_open_external_boundary": obs01_open,
        "obs02_in_conditional": obs02_cond,
        "all_ok": (ids_ok and counts_ok and obs07_sole and obs01_open and obs02_cond),
    }


def scan_historical_false_flag_jsons():
    found = {}
    for jp in sorted((REPO_ROOT / "relays").glob("**/*.json")):
        rel = str(jp.relative_to(REPO_ROOT))
        try:
            data = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        fk = []
        for k in ("all_gates_passed", "overall_pass"):
            if k in data and data[k] is False:
                fk.append(k)
        if "summary" in data and isinstance(data["summary"], dict):
            for k in ("all_gates_passed", "overall_pass"):
                if k in data["summary"] and data["summary"][k] is False:
                    fk.append("summary." + k)
        if fk:
            found[rel] = fk
    return found


def audit_5_a2_ow16_v6(d16, discrepancies):
    ledger = d16["blind_prediction_ledger_24_v6"]
    obs_list = ledger["observables"]
    part_res = validate_v6_partition(obs_list)
    if not part_res["all_ok"]:
        discrepancies.append("A2-OW16 v6 partition/ID/bucket check failed")

    by_id = {r["id"]: r for r in obs_list}
    obs22_val = by_id["OBS-22"]["value"]
    obs22_beta_ok = ("-76/3" in obs22_val) and ("-151/6" not in obs22_val)
    if not obs22_beta_ok:
        discrepancies.append("OBS-22 value does not exclusively record -76/3 (or contains -151/6)")

    g5 = d16["guardrail5_input_ledger_v6"]
    ratio_lists = (
        g5["uv_continuous_ratios_core"]
        + g5["uv_continuous_ratios_threshold"]
        + g5["flavor_bulk_mass_ratios"]
        + g5["unfixed_2hdm_uv_quartics_priced"]
        + g5["unfixed_soft_and_modulus_priced"]
    )
    n_ratios = len(ratio_lists)
    n_unique_ratios = len(set(ratio_lists))
    anchors = g5["dimensionful_anchors"]
    anchor_ok = (len(anchors) == 1 and g5["dimensionful_anchor_count"] == 1 and g5["guardrail5_anchor_limit_ok"] is True)
    s1_bits_err = abs(mp.mpf(g5["discrete_synergy_s1_144_to_2_bits"]) - mp.log(mp.mpf(72), mp.mpf(2)))

    if n_ratios != 15 or n_unique_ratios != 15 or g5["total_priced_continuous_ratios"] != 15:
        discrepancies.append("Guardrail 5 priced continuous UV ratio count != 15")
    if not anchor_ok:
        discrepancies.append("Guardrail 5 single dimensionful anchor limit failed")
    if s1_bits_err >= pow10(-12):
        discrepancies.append("Guardrail 5 Synergy S-1 bits != log2(72)")

    disk_false = scan_historical_false_flag_jsons()
    v6_disc = {x["file"]: x["false_keys"] for x in d16["historical_false_json_disclosure"]["files"]}
    undisclosed = sorted(set(disk_false.keys()) - set(v6_disc.keys()))
    extra_disclosed = sorted(set(v6_disc.keys()) - set(disk_false.keys()))
    false_json_exact = (disk_false == v6_disc and len(disk_false) == d16["historical_false_json_disclosure"]["total_historical_false_flag_jsons"])
    if not false_json_exact:
        discrepancies.append("Historical false-flag JSON disclosure mismatch vs disk scan")

    return {
        "partition_audit": part_res,
        "obs22_neg76_3_no_neg151_6": obs22_beta_ok,
        "priced_continuous_uv_ratios": n_ratios,
        "priced_continuous_uv_ratios_unique": n_unique_ratios,
        "guardrail5_anchor_limit_ok": anchor_ok,
        "synergy_s1_bits_err_vs_log2_72": mp.nstr(s1_bits_err, 6),
        "historical_false_flag_jsons_on_disk": len(disk_false),
        "historical_false_flag_jsons_disclosed_v6": len(v6_disc),
        "undisclosed_false_flag_jsons": undisclosed,
        "extra_disclosed_false_flag_jsons": extra_disclosed,
        "historical_false_flag_exact_match": false_json_exact,
    }, obs_list


# ============================================================================
# MODULE 6: 6 / 6 Referee Planted Fault Controls
# ============================================================================

def audit_6_planted_faults(sample_pf1, ctx_a, ctx_b, ctx_c, obs_list, discrepancies):
    # PF-REF-1: 1-byte tamper on a prior SHA-256 manifest caught in memory
    rel_mf, target_path, exp_hash = sample_pf1
    raw = bytearray(target_path.read_bytes())
    raw[0] ^= 1
    tampered_hash = hashlib.sha256(bytes(raw)).hexdigest().lower()
    pf1 = (tampered_hash != exp_hash)

    # PF-REF-2: Perturbing Type-II 2HDM +(1/2) Hd back to 1HDM -(3/2) Hd fails GL4 Yu_ir_N120 countercheck
    st_bad, _ = gl4_integrate(
        lambda st: rhs_type2_2hdm(st, c_hd_in_yu_1loop=Q(-3, 2)),
        (ctx_a["g0"], ctx_a["l0"], ctx_a["Yu0"], ctx_a["Yd0"], ctx_a["Ye0"]),
        mp.mpf(-10),
        40,
    )
    pf2_err = m3_frob(st_bad[2], ctx_a["Yu_ref"])
    pf2 = (pf2_err > pow10(-4))

    # PF-REF-3: Perturbing DP Type-I f_W = -1/2 to +1 flips +789.61 discriminant to negative
    pf3 = (ctx_b["disc_t1"] > mp.mpf(700)) and (ctx_b["disc_t2"] < mp.mpf(-5))

    # PF-REF-4: Evaluating SO(6) (d = 3) half-spinor weight trace yields -1 != 0
    pf4 = (ctx_c["so6_anom"] == -1)

    # PF-REF-5: Swapping p_3 -> -p_3 shifts |V_cb| by > 0.1 and flips bar_theta sign
    pf5 = (ctx_c["dvcb_anti"] > Q(1, 10)) and (ctx_c["bth_p"] * ctx_c["bth_m"] < mp.mpf(0))

    # PF-REF-6: Restoring v5's 3/9/9/3 (OBS-01 & OBS-02 as DERIVED_EXACT) fails 1/10/9/4 countercheck
    v5_mutated = []
    for row in obs_list:
        rc = dict(row)
        if rc["id"] in ("OBS-01", "OBS-02"):
            rc["bucket"] = "DERIVED_EXACT"
        v5_mutated.append(rc)
    v5_check = validate_v6_partition(v5_mutated)
    pf6 = (not v5_check["all_ok"]) and (v5_check["counts"]["DERIVED_EXACT"] == 3)

    controls = {
        "PF_REF_1_1byte_manifest_tamper": pf1,
        "PF_REF_2_1hdm_minus3half_Hd_fails_gl4": pf2,
        "PF_REF_3_fW_pos1_flips_disc_negative": pf3,
        "PF_REF_4_SO6_half_spinor_minus1": pf4,
        "PF_REF_5_p3_swap_vcb_and_bartheta_flip": pf5,
        "PF_REF_6_v5_3_9_9_3_fails_1_10_9_4": pf6,
    }
    caught = sum(1 for v in controls.values() if v)
    if caught != 6:
        discrepancies.append("Planted fault controls caught != 6")
    return {
        "controls": controls,
        "pf1_manifest_tested": rel_mf,
        "pf2_perturbed_Yu_frob_err": mp.nstr(pf2_err, 6),
        "planted_faults_caught": caught,
        "planted_faults_total": 6,
    }


def main():
    mp.mp.dps = 50
    discrepancies = []

    d20 = json.loads((REPO_ROOT / "relays" / "a2_ow20" / "a2_ow20_results.json").read_text(encoding="utf-8"))
    d16 = json.loads((REPO_ROOT / "relays" / "a2_ow16_v6" / "a2_ow16_v6_results.json").read_text(encoding="utf-8"))
    d19 = json.loads((REPO_ROOT / "relays" / "a2_ow19_v3" / "a2_ow19_v3_results.json").read_text(encoding="utf-8"))
    d18 = json.loads((REPO_ROOT / "relays" / "a2_ow18_v3" / "a2_ow18_v3_results.json").read_text(encoding="utf-8"))

    res_1, sample_pf1 = audit_1_ast_and_manifests(d20, d16, discrepancies)
    res_2, ctx_a = audit_2_ow20_a(d20, d19, discrepancies)
    res_3, ctx_b = audit_3_ow20_b(d20, d18, discrepancies)
    res_4, ctx_c = audit_4_ow20_c(d20, ctx_a, discrepancies)
    res_5, obs_list = audit_5_a2_ow16_v6(d16, discrepancies)
    res_6 = audit_6_planted_faults(sample_pf1, ctx_a, ctx_b, ctx_c, obs_list, discrepancies)

    total_discrepancies = len(discrepancies)
    all_gates_passed = (total_discrepancies == 0 and res_6["planted_faults_caught"] == 6)

    out = {
        "card": "A2-OW20-and-A2-OW16-v6-REFEREE",
        "seat": "agy-002-cold-room-referee",
        "firewall": "0 of 19",
        "audit_1_ast_and_manifests": res_1,
        "audit_2_ow20_a_gl4_and_2flav_lepto": res_2,
        "audit_3_ow20_b_1d_frg_and_e6": res_3,
        "audit_4_ow20_c_synergy144_and_so2d_weights": res_4,
        "audit_5_a2_ow16_v6_ledger_and_false_jsons": res_5,
        "audit_6_referee_planted_faults": res_6,
        "discrepancies": discrepancies,
        "total_discrepancies": total_discrepancies,
        "planted_faults_caught": res_6["planted_faults_caught"],
        "manifests_verified": res_1["manifests"]["manifests_verified"],
        "all_gates_passed": all_gates_passed,
    }

    out_path = OUT_DIR / "a2_ow20_referee_results.json"
    out_bytes = (json.dumps(out, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    out_sha = hashlib.sha256(out_bytes).hexdigest()
    (OUT_DIR / "OUTPUT_SHA256.txt").write_text(
        out_sha + "  a2_ow20_referee_results.json\n",
        encoding="utf-8",
    )
    print("SEALED_REFEREE_OUTPUT_SHA256:", out_sha)


if __name__ == "__main__":
    main()
