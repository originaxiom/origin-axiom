"""Cold-Room Zero-Trust Referee for Card A2-WG96 (E:J5 / W:G96 / W:T / X:HAND).

Independent first-principles verification built strictly from the four
Card A2-WG96 specification files (main card + Errata 2, 3, 4), with zero
repo imports, zero float/complex AST literals, Guardrail 2 & 3 enforcement,
0-of-19 empirical firewall, and independent Gauss-Legendre + RK4 punctured-torus
ODE integrators for L_2(tau).
"""

import ast
import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np


def pow10_neg(k):
    """Return 10^(-k) as a Python float without using float AST literals."""
    return 1 / (10 ** k)


def mp_pow10_neg(k):
    """Return 10^(-k) as an mpmath mpf without using float AST literals."""
    return mp.mpf(10) ** (-k)


def c_i():
    """Return imaginary unit as Python complex without using complex literals."""
    return complex(0, 1)


def mp_i():
    """Return imaginary unit as mpmath mpc without using complex literals."""
    return mp.mpc(0, 1)


def to_py_complex(val):
    """Convert mpmath scalar to Python complex."""
    return complex(float(mp.re(val)), float(mp.im(val)))


def to_py_float(val):
    """Convert mpmath real scalar to Python float."""
    return float(mp.re(val))


def mp_mat_to_np(M):
    """Convert an mpmath matrix to a NumPy complex128 array."""
    out = np.zeros((M.rows, M.cols), dtype=complex)
    for r in range(M.rows):
        for c in range(M.cols):
            out[r, c] = to_py_complex(M[r, c])
    return out


# =============================================================================
# Section 0: AST Hygiene & SHA-256 Chain of Custody
# =============================================================================

def run_section_0_custody(script_path):
    """Verify 0 float/complex AST literals, 0 disallowed imports, and SHA-256."""
    script_bytes = script_path.read_bytes()
    source = script_bytes.decode("utf-8")
    tree = ast.parse(source, filename=str(script_path))

    float_literals = []
    complex_literals = []
    imported_roots = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append((getattr(node, "lineno", 0), repr(node.value)))
            elif isinstance(node.value, complex):
                complex_literals.append((getattr(node, "lineno", 0), repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_roots.add(node.module.split(".")[0])

    allowed_roots = set(sys.stdlib_module_names) | {"numpy", "mpmath"}
    disallowed_imports = sorted(imported_roots - allowed_roots)

    actual_sha256 = hashlib.sha256(script_bytes).hexdigest().lower()
    sha_file = script_path.parent / "SCRIPT_SHA256.txt"
    expected_sha256 = ""
    if sha_file.exists():
        tokens = sha_file.read_text(encoding="utf-8").strip().split()
        if tokens:
            expected_sha256 = tokens[0].lower()

    sha256_match = bool(expected_sha256) and (actual_sha256 == expected_sha256)
    passed = (
        len(float_literals) == 0
        and len(complex_literals) == 0
        and len(disallowed_imports) == 0
        and sha256_match
    )
    return {
        "script_path": str(script_path),
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "float_literals": float_literals,
        "complex_literals": complex_literals,
        "imported_modules": sorted(imported_roots),
        "disallowed_imports": disallowed_imports,
        "actual_sha256": actual_sha256,
        "expected_sha256": expected_sha256,
        "sha256_match": sha256_match,
        "passed": passed,
    }


# =============================================================================
# Linear Algebra & Finite Matrix Group Helpers
# =============================================================================

def gen_group_fast(gens, max_ord=1500, tol=None):
    """Generate finite matrix group <gens> via BFS with preallocated buffer."""
    if tol is None:
        tol = pow10_neg(9)
    d = gens[0].shape[0]
    all_gens = list(gens) + [np.linalg.inv(g) for g in gens]
    buf = np.empty((max_ord, d, d), dtype=complex)
    buf[0] = np.eye(d, dtype=complex)
    cnt = 1
    qi = 0
    while qi < cnt:
        cur = buf[qi]
        qi += 1
        for g in all_gens:
            cand = cur @ g
            diffs = np.max(np.abs(buf[:cnt] - cand), axis=(1, 2))
            if float(diffs.min()) >= tol:
                if cnt >= max_ord:
                    raise RuntimeError("Group order exceeded max_ord")
                buf[cnt] = cand
                cnt += 1
    return buf[:cnt]


def commutant_dim(gens, tol=None):
    """Compute dimension of {X : G X = X G for all G in gens}."""
    if tol is None:
        tol = pow10_neg(9)
    d = gens[0].shape[0]
    rows = []
    for G in gens:
        for i in range(d):
            for k in range(d):
                row = np.zeros(d * d, dtype=complex)
                for j in range(d):
                    row[j * d + k] += G[i, j]
                    row[i * d + j] -= G[j, k]
                rows.append(row)
    sv = np.linalg.svd(np.array(rows, dtype=complex), compute_uv=False)
    return int(np.sum(sv < tol))


def intertwiner_space(As, Bs, tol=None):
    """Find nullspace of U A_r - B_r U = 0; conjugates Vh rows per SVD convention."""
    if tol is None:
        tol = pow10_neg(9)
    d1 = As[0].shape[0]
    d2 = Bs[0].shape[0]
    rows = []
    for A, B in zip(As, Bs):
        for i in range(d2):
            for k in range(d1):
                row = np.zeros(d2 * d1, dtype=complex)
                for j in range(d1):
                    row[i * d1 + j] += A[j, k]
                for l_idx in range(d2):
                    row[l_idx * d1 + k] -= B[i, l_idx]
                rows.append(row)
    _, sv, Vh = np.linalg.svd(np.array(rows, dtype=complex), full_matrices=True)
    # Standard NumPy SVD returns Vh = V^H, so null vectors are conjugated rows.
    null_vecs = Vh[sv < tol].conj()
    mats = [v.reshape(d2, d1) for v in null_vecs]
    return len(mats), mats


def make_unitary_intertwiner(U_raw, As, Bs):
    """Scale a 1D intertwiner matrix to unitary and compute all error metrics."""
    d = U_raw.shape[0]
    fro = float(np.linalg.norm(U_raw, "fro"))
    U = U_raw * (math.sqrt(d) / fro)
    unitary_err = float(np.max(np.abs(U.conj().T @ U - np.eye(d, dtype=complex))))
    intertwine_err = max(
        float(np.max(np.abs(U @ A - B @ U))) for A, B in zip(As, Bs)
    )
    return U, unitary_err, intertwine_err


def char_overlap(As, Bs, max_ord=2500):
    """Compute finite-group character inner product on joint image in B_3."""
    d1 = As[0].shape[0]
    d2 = Bs[0].shape[0]
    Jgens = [
        np.block([
            [A, np.zeros((d1, d2), dtype=complex)],
            [np.zeros((d2, d1), dtype=complex), B],
        ])
        for A, B in zip(As, Bs)
    ]
    G = gen_group_fast(Jgens, max_ord=max_ord)
    trA = np.trace(G[:, :d1, :d1], axis1=1, axis2=2)
    trB = np.trace(G[:, d1:, d1:], axis1=1, axis2=2)
    ip = np.mean(np.conj(trA) * trB)
    return complex(ip), len(G)


def braid_err(ML, MR):
    """Compute ||M_L M_R^{-1} M_L - M_R^{-1} M_L M_R^{-1}||_max."""
    MR_inv = np.linalg.inv(MR)
    lhs = ML @ MR_inv @ ML
    rhs = MR_inv @ ML @ MR_inv
    return float(np.max(np.abs(lhs - rhs)))


def normalized_turns(M):
    """Return sorted normalized phase turns arg(lambda)/(2*pi) in [0, 1)."""
    ev = np.linalg.eigvals(M)
    tol = pow10_neg(10)
    turns = []
    for z in ev:
        ang = math.atan2(z.imag, z.real) / (2 * math.pi)
        ang = ang % 1
        if abs(ang - 1) < tol or abs(ang) < tol:
            ang = 0 / 1
        turns.append(ang)
    turns.sort()
    return turns


# =============================================================================
# Section 1 (W1): Cohomological Reconstruction of W:G96, H_Q, W:T, W:\overline{T}, B1610
# =============================================================================

PAR = [(1, 0), (0, 1), (1, 1)]


def quat_matrices():
    """Return I2, qi, qj, qk in SU(2)."""
    I2 = np.eye(2, dtype=complex)
    I = c_i()
    qi = np.array([[I, 0], [0, -I]], dtype=complex)
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    qk = qi @ qj
    return I2, qi, qj, qk


def rho_p_mat(p, word, I2, qi, qj):
    """Evaluate representation chi_p x rho_Q on a word in {a, A, b, B}."""
    sa = (-1) ** p[0]
    sb = (-1) ** p[1]
    M = I2.copy()
    for ch in word:
        if ch == "a":
            M = M @ (sa * qi)
        elif ch == "A":
            M = M @ (sa * (-qi))
        elif ch == "b":
            M = M @ (sb * qj)
        elif ch == "B":
            M = M @ (sb * (-qj))
        else:
            raise ValueError(f"Unknown generator letter: {ch}")
    return M


def eval_cocycle(z_ab, p, word, I2, qi, qj):
    """Evaluate left-module 1-cocycle z on word using z(uv) = z(u) + rho_p(u)z(v)."""
    za = z_ab[:2]
    zb = z_ab[2:]
    sa = (-1) ** p[0]
    sb = (-1) ** p[1]
    total = np.zeros(2, dtype=complex)
    prefix = I2.copy()
    for ch in word:
        if ch == "a":
            step = za
            mat = sa * qi
        elif ch == "b":
            step = zb
            mat = sb * qj
        elif ch == "A":
            mat = sa * (-qi)
            step = -mat @ za
        elif ch == "B":
            mat = sb * (-qj)
            step = -mat @ zb
        else:
            raise ValueError(f"Unknown generator letter: {ch}")
        total = total + prefix @ step
        prefix = prefix @ mat
    return total


def cup_product_p(z1, z2, p, I2, qi, qj):
    """Bar-resolution cup product on relator w_rel = abABabAB with B(x,y) = y^H x."""
    w_rel = "abABabAB"
    acc = complex(0, 0)
    pk = ""
    for k in range(len(w_rel) - 1):
        pk += w_rel[k]
        g_next = w_rel[k + 1]
        x = eval_cocycle(z1, p, pk, I2, qi, qj)
        y = rho_p_mat(p, pk, I2, qi, qj) @ eval_cocycle(z2, p, g_next, I2, qi, qj)
        acc += np.vdot(y, x)
    # Subtract the two [a | a^{-1}] and [b | b^{-1}] boundary pairs
    xa = eval_cocycle(z1, p, "a", I2, qi, qj)
    ya = rho_p_mat(p, "a", I2, qi, qj) @ eval_cocycle(z2, p, "A", I2, qi, qj)
    xb = eval_cocycle(z1, p, "b", I2, qi, qj)
    yb = rho_p_mat(p, "b", I2, qi, qj) @ eval_cocycle(z2, p, "B", I2, qi, qj)
    acc -= 2 * np.vdot(ya, xa)
    acc -= 2 * np.vdot(yb, xb)
    return acc


def cup_triv(za, zb):
    """Bar-resolution cup product on trivial 1D module for SIGN calibration."""
    w_rel = "abABabAB"
    val_map = {"a": za, "A": -za, "b": zb, "B": -zb}
    acc = complex(0, 0)
    z_pk = complex(0, 0)
    for k in range(len(w_rel) - 1):
        z_pk += val_map[w_rel[k]]
        z_next = val_map[w_rel[k + 1]]
        acc += np.conj(z_next) * z_pk
    acc -= 2 * np.conj(-za) * za
    acc -= 2 * np.conj(-zb) * zb
    return acc


def build_cohomology_space(par_list, I2, qi, qj):
    """Construct orthonormal H^1 bases (coboundary complements) per parity."""
    bases = {}
    cob_mats = {}
    for p in par_list:
        C = np.vstack([
            rho_p_mat(p, "a", I2, qi, qj) - I2,
            rho_p_mat(p, "b", I2, qi, qj) - I2,
        ])
        U, s, _ = np.linalg.svd(C, full_matrices=True)
        rank = int(np.sum(s > pow10_neg(9)))
        cob_mats[p] = U[:, :rank]
        bases[p] = U[:, rank:]
    return bases, cob_mats


def parity_pullback(p, wa, wb):
    """Compute target parity q = p o m mod 2 for automorphism m: (a->wa, b->wb)."""
    q0 = sum(p[0] if ch in "aA" else p[1] for ch in wa) % 2
    q1 = sum(p[0] if ch in "aA" else p[1] for ch in wb) % 2
    return (q0, q1)


def build_automorphism_operator(wa, wb, g, par_list, bases, I2, qi, qj):
    """Build matrix of (M_{m,g} z)(u) = g^{-1} z(m(u)) on V = oplus H^1."""
    dim = 2 * len(par_list)
    M = np.zeros((dim, dim), dtype=complex)
    g_inv = np.linalg.inv(g)
    for ip, p in enumerate(par_list):
        q = parity_pullback(p, wa, wb)
        iq = par_list.index(q)
        Bp = bases[p]
        Bq = bases[q]
        for r in range(Bp.shape[1]):
            z = Bp[:, r]
            za_new = g_inv @ eval_cocycle(z, p, wa, I2, qi, qj)
            zb_new = g_inv @ eval_cocycle(z, p, wb, I2, qi, qj)
            z_new = np.concatenate([za_new, zb_new])
            M[2 * iq:2 * iq + 2, 2 * ip + r] = Bq.conj().T @ z_new
    return M


def invert_word(w):
    """Invert a word in {a, A, b, B}."""
    inv_map = {"a": "A", "A": "a", "b": "B", "B": "b"}
    return "".join(inv_map[ch] for ch in reversed(w))


def compose_words(w, wa, wb):
    """Apply substitution (a->wa, b->wb) to word w."""
    mp_w = {"a": wa, "A": invert_word(wa), "b": wb, "B": invert_word(wb)}
    return "".join(mp_w[ch] for ch in w)


def solve_su2_lift_order3(wa, wb, I2, qi, qj):
    """Solve g rho_Q(u) g^{-1} = rho_Q(m(u)) for g in SU(2) with g^3 = +I_2."""
    A = rho_p_mat((0, 0), wa, I2, qi, qj)
    B = rho_p_mat((0, 0), wb, I2, qi, qj)
    eqs = []
    for L_mat, R_mat in [(qi, A), (qj, B)]:
        for i in range(2):
            for j in range(2):
                row = np.zeros(4, dtype=complex)
                for k in range(2):
                    row[2 * i + k] += L_mat[k, j]
                    row[2 * k + j] -= R_mat[i, k]
                eqs.append(row)
    _, _, Vh = np.linalg.svd(np.array(eqs, dtype=complex), full_matrices=True)
    v = Vh[-1].conj().reshape(2, 2)
    g = v / np.sqrt(np.linalg.det(v))
    g3 = g @ g @ g
    if np.max(np.abs(g3 + I2)) < np.max(np.abs(g3 - I2)):
        g = -g
    return g


def analyze_finite_group_structure(G_arr, ML, MR):
    """Compute mult table, conjugacy classes, true centralizer Z, and quotient G/Z."""
    n = len(G_arr)
    tol = pow10_neg(8)
    I_d = np.eye(G_arr.shape[1], dtype=complex)

    def find_idx(mat):
        diffs = np.max(np.abs(G_arr - mat), axis=(1, 2))
        idx = int(np.argmin(diffs))
        if float(diffs[idx]) >= tol:
            raise RuntimeError("Matrix not found in finite group")
        return idx

    idx_I = find_idx(I_d)
    idx_L = find_idx(ML)
    idx_R = find_idx(MR)

    mul = np.zeros((n, n), dtype=int)
    for i in range(n):
        prods = G_arr[i] @ G_arr
        for j in range(n):
            diffs = np.max(np.abs(G_arr - prods[j]), axis=(1, 2))
            mul[i, j] = int(np.argmin(diffs))

    inv_idx = [int(np.where(mul[i] == idx_I)[0][0]) for i in range(n)]

    # Conjugacy classes
    seen = set()
    conj_classes = []
    for x in range(n):
        if x in seen:
            continue
        cls = {int(mul[mul[g, x], inv_idx[g]]) for g in range(n)}
        seen |= cls
        conj_classes.append(sorted(cls))

    # True centralizer Z = {g in G : [g, M_L] = [g, M_R] = 0}
    center_indices = [
        g for g in range(n)
        if mul[g, idx_L] == mul[idx_L, g] and mul[g, idx_R] == mul[idx_R, g]
    ]
    center_set = set(center_indices)

    def elt_order(idx):
        cur = idx
        ord_val = 1
        while cur != idx_I:
            cur = mul[cur, idx]
            ord_val += 1
        return ord_val

    center_orders = sorted(elt_order(g) for g in center_indices)

    # Coset quotient G / Z
    cosets = []
    used = set()
    elt_to_coset = {}
    for g in range(n):
        if g in used:
            continue
        c_members = sorted(int(mul[g, z]) for z in center_indices)
        cid = len(cosets)
        cosets.append(c_members)
        for m_idx in c_members:
            used.add(m_idx)
            elt_to_coset[m_idx] = cid

    q_ord = len(cosets)
    q_id = elt_to_coset[idx_I]
    q_mul = np.zeros((q_ord, q_ord), dtype=int)
    q_well_defined = True
    for ci in range(q_ord):
        for cj in range(q_ord):
            targets = {elt_to_coset[mul[a, b]] for a in cosets[ci] for b in cosets[cj]}
            if len(targets) != 1:
                q_well_defined = False
            q_mul[ci, cj] = next(iter(targets))

    q_order_hist = {}
    for ci in range(q_ord):
        cur = ci
        k_ord = 1
        while cur != q_id:
            cur = q_mul[cur, ci]
            k_ord += 1
        q_order_hist[k_ord] = q_order_hist.get(k_ord, 0) + 1

    return {
        "order": n,
        "num_conjugacy_classes": len(conj_classes),
        "center_order": len(center_indices),
        "center_orders": center_orders,
        "center_indices": center_indices,
        "quotient_order": q_ord,
        "quotient_well_defined": q_well_defined,
        "quotient_order_histogram": {str(k): v for k, v in sorted(q_order_hist.items())},
        "center_is_C4": (len(center_indices) == 4 and max(center_orders) == 4),
        "quotient_is_S4": (q_well_defined and q_ord == 24 and q_order_hist == {1: 1, 2: 9, 3: 8, 4: 6}),
        "center_matrices": G_arr[list(center_indices)],
    }


def run_w1_cohomology():
    """Execute Section W1 verification and return data + matrices for later sections."""
    tol = pow10_neg(12)
    tol_cob = pow10_neg(10)
    I = c_i()
    I2, qi, qj, qk = quat_matrices()
    bases, cob_mats = build_cohomology_space(PAR, I2, qi, qj)

    # SIGN calibration on trivial module {a: 1, b: tau}
    tau_cal = Fraction(1, 3) + I * Fraction(7, 5)
    triv_cup = cup_triv(complex(1, 0), complex(tau_cal))
    sign_candidates = [1, -1]
    cal_vals = {s: (s * I * triv_cup).real for s in sign_candidates}
    SIGN = 1 if cal_vals[1] > 0 else -1
    cal_expected = 4 * tau_cal.imag
    cal_err = abs(cal_vals[SIGN] - cal_expected)

    # Coboundary annihilation check across all parities
    max_cob_err = 0 / 1
    for p in PAR:
        Bp = bases[p]
        Cp = cob_mats[p]
        for r in range(Cp.shape[1]):
            for s in range(Bp.shape[1]):
                err1 = abs(cup_product_p(Cp[:, r], Bp[:, s], p, I2, qi, qj))
                err2 = abs(cup_product_p(Bp[:, s], Cp[:, r], p, I2, qi, qj))
                max_cob_err = max(max_cob_err, float(err1), float(err2))
            for s in range(Cp.shape[1]):
                err3 = abs(cup_product_p(Cp[:, r], Cp[:, s], p, I2, qi, qj))
                max_cob_err = max(max_cob_err, float(err3))

    # Build Q and H_Q = conj(Q)
    Q = np.zeros((6, 6), dtype=complex)
    for ip, p in enumerate(PAR):
        Bp = bases[p]
        for r in range(2):
            for s in range(2):
                Q[2 * ip + r, 2 * ip + s] = SIGN * I * cup_product_p(Bp[:, r], Bp[:, s], p, I2, qi, qj)
    H_Q = Q.conj()
    herm_err = float(np.max(np.abs(H_Q - H_Q.conj().T)))
    hq_evals, hq_evecs = np.linalg.eigh(H_Q)
    expected_evals = np.array([-4, -4, -4, 4, 4, 4])
    hq_spec_err = float(np.max(np.abs(np.sort(hq_evals) - expected_evals)))
    n_neg = int(np.sum(hq_evals < 0))
    n_pos = int(np.sum(hq_evals > 0))

    # Nielsen automorphisms & SU(2) lifts
    s2 = math.sqrt(2)
    gL = (I2 + qi) / s2
    gR = (I2 - qj) / s2
    giota = qk
    gP = (qi + qj) / s2

    ML = build_automorphism_operator("a", "ab", gL, PAR, bases, I2, qi, qj)
    MR = build_automorphism_operator("ab", "b", gR, PAR, bases, I2, qi, qj)
    Miota = build_automorphism_operator("A", "B", giota, PAR, bases, I2, qi, qj)
    MP = build_automorphism_operator("b", "a", gP, PAR, bases, I2, qi, qj)

    pres_L_err = float(np.max(np.abs(ML.conj().T @ H_Q @ ML - H_Q)))
    pres_R_err = float(np.max(np.abs(MR.conj().T @ H_Q @ MR - H_Q)))
    pres_iota_err = float(np.max(np.abs(Miota.conj().T @ H_Q @ Miota - H_Q)))
    rev_P_err = float(np.max(np.abs(MP.conj().T @ H_Q @ MP + H_Q)))
    w1_braid_err = braid_err(ML, MR)

    G_LR = gen_group_fast([ML, MR])
    cdim_V = commutant_dim([ML, MR])
    grp_info = analyze_finite_group_structure(G_LR, ML, MR)

    # Chiral subspaces W:T (H_Q > 0) and W:\overline{T} (H_Q < 0)
    Vp = hq_evecs[:, 3:]
    Vm = hq_evecs[:, :3]
    swap_Pm_err = float(np.max(np.abs(Vp.conj().T @ MP @ Vp)))
    swap_Pp_err = float(np.max(np.abs(Vm.conj().T @ MP @ Vm)))

    TL = Vp.conj().T @ ML @ Vp
    TR = Vp.conj().T @ MR @ Vp
    TbL = Vm.conj().T @ ML @ Vm
    TbR = Vm.conj().T @ MR @ Vm

    # Verify block decoupling of ML, MR
    decouple_err = max(
        float(np.max(np.abs(Vm.conj().T @ ML @ Vp))),
        float(np.max(np.abs(Vp.conj().T @ ML @ Vm))),
        float(np.max(np.abs(Vm.conj().T @ MR @ Vp))),
        float(np.max(np.abs(Vp.conj().T @ MR @ Vm))),
    )

    G_T = gen_group_fast([TL, TR])
    G_Tb = gen_group_fast([TbL, TbR])
    cdim_T = commutant_dim([TL, TR])
    cdim_Tb = commutant_dim([TbL, TbR])

    # Verify split-chirality center action on W:T vs W:\overline{T}
    center_acts_scalar_chiral = True
    for Cmat in grp_info["center_matrices"]:
        CT = Vp.conj().T @ Cmat @ Vp
        CTb = Vm.conj().T @ Cmat @ Vm
        zT = CT[0, 0]
        zTb = CTb[0, 0]
        if (
            float(np.max(np.abs(CT - zT * np.eye(3, dtype=complex)))) >= tol
            or float(np.max(np.abs(CTb - zTb * np.eye(3, dtype=complex)))) >= tol
        ):
            center_acts_scalar_chiral = False

    exp_tr_T = complex(math.cos(-math.pi / 4), math.sin(-math.pi / 4))
    exp_tr_Tb = complex(math.cos(math.pi / 4), math.sin(math.pi / 4))
    exp_det_T = complex(math.cos(-3 * math.pi / 4), math.sin(-3 * math.pi / 4))
    exp_det_Tb = complex(math.cos(3 * math.pi / 4), math.sin(3 * math.pi / 4))

    tr_T_err = abs(complex(np.trace(TL)) - exp_tr_T)
    tr_Tb_err = abs(complex(np.trace(TbL)) - exp_tr_Tb)
    det_T_err = abs(complex(np.linalg.det(TL)) - exp_det_T)
    det_Tb_err = abs(complex(np.linalg.det(TbL)) - exp_det_Tb)

    # B1610 Founding Torsor Verification (all 4 rules, both order-3 and order-6 lifts)
    b1610_rules = [
        ("sigma", ("ab", "a")),
        ("C(sigma)", ("b", "ba")),
        ("rev(sigma)", ("ba", "a")),
        ("C(rev(sigma))", ("b", "ab")),
    ]
    exp_turns_ord3 = [1 / 6, 1 / 2, 5 / 6]
    exp_turns_ord6 = [0 / 1, 1 / 3, 2 / 3]
    b1610_results = {}
    I6 = np.eye(6, dtype=complex)

    for rname, (wa, wb) in b1610_rules:
        g1 = solve_su2_lift_order3(wa, wb, I2, qi, qj)
        g1_lift_err = max(
            float(np.max(np.abs(g1 @ qi @ np.linalg.inv(g1) - rho_p_mat((0, 0), wa, I2, qi, qj)))),
            float(np.max(np.abs(g1 @ qj @ np.linalg.inv(g1) - rho_p_mat((0, 0), wb, I2, qi, qj)))),
            float(np.max(np.abs(g1 @ g1 @ g1 - I2))),
        )
        M1 = build_automorphism_operator(wa, wb, g1, PAR, bases, I2, qi, qj)
        single_tick_rev_err = float(np.max(np.abs(M1.conj().T @ H_Q @ M1 + H_Q)))

        wa2 = compose_words(wa, wa, wb)
        wb2 = compose_words(wb, wa, wb)
        g2_ord3 = g1 @ g1
        g2_ord6 = -g2_ord3

        lift_records = {}
        for lift_name, g2, expected_M2_cube, exp_turns in [
            ("order3_lift", g2_ord3, -I6, exp_turns_ord3),
            ("order6_lift", g2_ord6, I6, exp_turns_ord6),
        ]:
            g2_cube = g2 @ g2 @ g2
            g2_target = I2 if lift_name == "order3_lift" else -I2
            g2_cube_err = float(np.max(np.abs(g2_cube - g2_target)))
            M2 = build_automorphism_operator(wa2, wb2, g2, PAR, bases, I2, qi, qj)
            M2_cube_err = float(np.max(np.abs(M2 @ M2 @ M2 - expected_M2_cube)))
            double_tick_keep_err = float(np.max(np.abs(M2.conj().T @ H_Q @ M2 - H_Q)))
            subspace_inv_err = max(
                float(np.max(np.abs(Vm.conj().T @ M2 @ Vp))),
                float(np.max(np.abs(Vp.conj().T @ M2 @ Vm))),
            )
            turns_T = normalized_turns(Vp.conj().T @ M2 @ Vp)
            turns_Tb = normalized_turns(Vm.conj().T @ M2 @ Vm)
            turns_T_err = max(abs(a - b) for a, b in zip(turns_T, exp_turns))
            turns_Tb_err = max(abs(a - b) for a, b in zip(turns_Tb, exp_turns))
            lift_passed = (
                g2_cube_err < tol
                and M2_cube_err < tol
                and double_tick_keep_err < tol
                and subspace_inv_err < tol
                and turns_T_err < tol
                and turns_Tb_err < tol
            )
            lift_records[lift_name] = {
                "g2_cube_err": g2_cube_err,
                "M2_cube_err": M2_cube_err,
                "double_tick_keep_err": double_tick_keep_err,
                "subspace_inv_err": subspace_inv_err,
                "turns_T": turns_T,
                "turns_Tb": turns_Tb,
                "turns_T_err": turns_T_err,
                "turns_Tb_err": turns_Tb_err,
                "passed": lift_passed,
            }

        rule_passed = (
            g1_lift_err < tol
            and single_tick_rev_err < tol
            and lift_records["order3_lift"]["passed"]
            and lift_records["order6_lift"]["passed"]
        )
        b1610_results[rname] = {
            "words_single": [wa, wb],
            "words_double": [wa2, wb2],
            "g1_lift_err": g1_lift_err,
            "single_tick_rev_err": single_tick_rev_err,
            "order3_lift": lift_records["order3_lift"],
            "order6_lift": lift_records["order6_lift"],
            "passed": rule_passed,
        }

    w1_passed = (
        SIGN == 1
        and cal_err < tol
        and max_cob_err < tol_cob
        and herm_err < tol
        and hq_spec_err < tol
        and (n_pos, n_neg) == (3, 3)
        and pres_L_err < tol
        and pres_R_err < tol
        and pres_iota_err < tol
        and rev_P_err < tol
        and swap_Pm_err < tol
        and swap_Pp_err < tol
        and decouple_err < tol
        and w1_braid_err < tol
        and grp_info["order"] == 96
        and grp_info["num_conjugacy_classes"] == 20
        and cdim_V == 2
        and grp_info["center_is_C4"]
        and grp_info["quotient_is_S4"]
        and center_acts_scalar_chiral
        and len(G_T) == 96
        and len(G_Tb) == 96
        and cdim_T == 1
        and cdim_Tb == 1
        and tr_T_err < tol
        and tr_Tb_err < tol
        and det_T_err < tol
        and det_Tb_err < tol
        and all(b1610_results[k]["passed"] for k in b1610_results)
    )

    summary = {
        "SIGN": SIGN,
        "cal_4Im_tau_err": cal_err,
        "coboundary_annihilation_max_err": max_cob_err,
        "H_Q_hermitian_err": herm_err,
        "H_Q_spectrum": [float(x) for x in np.sort(hq_evals)],
        "H_Q_spectrum_err": hq_spec_err,
        "H_Q_signature": [n_pos, n_neg],
        "L_preserves_H_Q_err": pres_L_err,
        "R_preserves_H_Q_err": pres_R_err,
        "S_iota_preserves_H_Q_err": pres_iota_err,
        "P_reverses_H_Q_err": rev_P_err,
        "P_swaps_chiral_err": max(swap_Pm_err, swap_Pp_err),
        "chiral_decouple_err": decouple_err,
        "braid_err": w1_braid_err,
        "W_G96_order": grp_info["order"],
        "W_G96_conjugacy_classes": grp_info["num_conjugacy_classes"],
        "W_G96_commutant_dim": cdim_V,
        "Z_order": grp_info["center_order"],
        "Z_element_orders": grp_info["center_orders"],
        "Z_acts_scalar_chiral": center_acts_scalar_chiral,
        "quotient_order": grp_info["quotient_order"],
        "quotient_well_defined": grp_info["quotient_well_defined"],
        "quotient_order_histogram": grp_info["quotient_order_histogram"],
        "W_T_order": len(G_T),
        "W_T_commutant_dim": cdim_T,
        "tr_T_L_err": tr_T_err,
        "det_T_L_err": det_T_err,
        "W_Tbar_order": len(G_Tb),
        "W_Tbar_commutant_dim": cdim_Tb,
        "tr_Tbar_L_err": tr_Tb_err,
        "det_Tbar_L_err": det_Tb_err,
        "B1610_rules": b1610_results,
        "passed": w1_passed,
    }

    artifacts = {
        "H_Q": H_Q,
        "ML": ML,
        "MR": MR,
        "Vp": Vp,
        "Vm": Vm,
        "TL": TL,
        "TR": TR,
        "TbL": TbL,
        "TbR": TbR,
        "bases": bases,
        "I2": I2,
        "qi": qi,
        "qj": qj,
    }
    return summary, artifacts


# =============================================================================
# Section 2 (W2): Candidate I — Torsion Wilson Line w_0 != 0 -> Outcome [3]
# =============================================================================

def run_w2_wilson_line():
    """Verify <L, R> mod N orbit sizes and 0 common fixed points for N in {3, 5}."""
    L = ((1, 1), (0, 1))
    R = ((1, 0), (1, 1))

    def step_row(v, M, N):
        return ((v[0] * M[0][0] + v[1] * M[1][0]) % N, (v[0] * M[0][1] + v[1] * M[1][1]) % N)

    def step_col(v, M, N):
        return ((M[0][0] * v[0] + M[0][1] * v[1]) % N, (M[1][0] * v[0] + M[1][1] * v[1]) % N)

    results = {}
    all_ok = True
    for N in (3, 5):
        nonzero = [(a, b) for a in range(N) for b in range(N) if (a, b) != (0, 0)]
        sub = {}
        for mode, fn in [("row_action", step_row), ("col_action", step_col)]:
            seed = (1, 0)
            visited = {seed}
            queue = [seed]
            idx = 0
            while idx < len(queue):
                cur = queue[idx]
                idx += 1
                for M in (L, R):
                    nxt = fn(cur, M, N)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            fixed = [v for v in nonzero if fn(v, L, N) == v and fn(v, R, N) == v]
            ok = (len(visited) == N * N - 1) and (len(fixed) == 0)
            all_ok = all_ok and ok
            sub[mode] = {
                "orbit_size": len(visited),
                "nonzero_count": len(nonzero),
                "common_fixed_points": len(fixed),
                "L_image_of_1_0": list(fn(seed, L, N)),
                "R_image_of_1_0": list(fn(seed, R, N)),
                "passed": ok,
            }
        results[f"N_{N}"] = sub

    results["outcome"] = "Outcome [3]"
    results["passed"] = all_ok
    return results


# =============================================================================
# Section 3 (W3): Candidate II — Level-3 Odd-Spin (1/2, 1/2) CIM Basis -> Outcome [2]
# =============================================================================

def cim_psi_vec(z, tau, n_max=30):
    """Evaluate Level-3 odd-spin (1/2, 1/2) theta basis (psi_0, psi_1, psi_2)."""
    I = mp_i()
    out = []
    for j in range(3):
        shift = (mp.mpf(j) + mp.mpf(1) / 2) / 3
        s = mp.mpc(0)
        for n in range(-n_max, n_max + 1):
            na = n + shift
            arg = 3 * mp.pi * I * tau * (na ** 2) + 6 * mp.pi * I * na * (z + mp.mpf(1) / 6)
            s += mp.exp(arg)
        out.append(s)
    return out


def cim_eval_matrix(zs, tau):
    """Build 3x3 matrix with columns psi(z_c | tau)."""
    M = mp.zeros(3, 3)
    for c, z in enumerate(zs):
        vec = cim_psi_vec(z, tau)
        for r in range(3):
            M[r, c] = vec[r]
    return M


def cim_extract_generators(zs, tau):
    """Solve for 3x3 M_T^{CIM} and M_S^{CIM} at (zs, tau)."""
    I = mp_i()
    Psi = cim_eval_matrix(zs, tau)
    Psi_T = cim_eval_matrix(zs, tau + 1)
    MT = Psi_T * (Psi ** (-1))

    Psi_S = cim_eval_matrix([z / tau for z in zs], -1 / tau)
    for c, z in enumerate(zs):
        fac = mp.sqrt(-I * tau) * mp.exp(3 * mp.pi * I * (z ** 2) / tau)
        for r in range(3):
            Psi_S[r, c] /= fac
    MS = Psi_S * (Psi ** (-1))
    return mp_mat_to_np(MT), mp_mat_to_np(MS)


def run_w3_cim_level3(TL, TR, TbL, TbR):
    """Verify W3 Level-3 CIM basis, charge conjugation [-1,-1,1], 24 twists -> Outcome [2]."""
    tol = pow10_neg(12)
    with mp.workdps(45):
        tau1 = mp.mpf(13) / 100 + mp_i() * mp.mpf(3) / 2
        zs1 = [
            mp.mpf(1) / 7 + mp_i() / 11,
            mp.mpf(-2) / 9 + mp_i() * 3 / 13,
            mp.mpf(4) / 15 - mp_i() * 2 / 17,
        ]
        tau2 = mp.mpf(-1) / 4 + mp_i() * mp.mpf(11) / 5
        zs2 = [
            mp.mpf(3) / 19 - mp_i() / 13,
            mp.mpf(5) / 23 + mp_i() * 2 / 17,
            mp.mpf(-1) / 8 + mp_i() * 4 / 29,
        ]

        MT, MS = cim_extract_generators(zs1, tau1)
        MT_chk, MS_chk = cim_extract_generators(zs2, tau2)
    cross_MT_diff = float(np.max(np.abs(MT - MT_chk)))
    cross_MS_diff = float(np.max(np.abs(MS - MS_chk)))

    I3 = np.eye(3, dtype=complex)
    MT_unit_err = float(np.max(np.abs(MT.conj().T @ MT - I3)))
    MS_unit_err = float(np.max(np.abs(MS.conj().T @ MS - I3)))

    MR = MS @ np.linalg.inv(MT) @ np.linalg.inv(MS)
    cim_braid_err = braid_err(MT, MR)

    MS2 = MS @ MS
    comm_MS2_MT_err = float(np.max(np.abs(MS2 @ MT - MT @ MS2)))
    comm_MS2_MR_err = float(np.max(np.abs(MS2 @ MR - MR @ MS2)))

    ms2_evals = np.linalg.eigvals(MS2)
    ms2_real = sorted(float(z.real) for z in ms2_evals)
    ms2_imag_err = max(abs(float(z.imag)) for z in ms2_evals)
    ms2_spec_err = max(abs(a - b) for a, b in zip(ms2_real, [-1, -1, 1]))

    mt_turns = normalized_turns(MT)
    exp_mt_turns = [1 / 24, 1 / 24, 3 / 8]
    mt_turns_err = max(abs(a - b) for a, b in zip(mt_turns, exp_mt_turns))

    # Scan all 24 Dedekind twists k = 0..23
    cT = complex(math.cos(2 * math.pi / 24), math.sin(2 * math.pi / 24))
    twist_records = []
    all_cdim2 = True
    max_ov_T = 0 / 1
    max_ov_Tb = 0 / 1
    for k in range(24):
        Lk = (cT ** k) * MT
        Rk = (cT ** (-k)) * MR
        cd = commutant_dim([Lk, Rk])
        ovT, j_ord_T = char_overlap([Lk, Rk], [TL, TR])
        ovTb, j_ord_Tb = char_overlap([Lk, Rk], [TbL, TbR])
        if cd != 2:
            all_cdim2 = False
        max_ov_T = max(max_ov_T, abs(ovT))
        max_ov_Tb = max(max_ov_Tb, abs(ovTb))
        twist_records.append({
            "k": k,
            "commutant_dim": cd,
            "overlap_WT": abs(ovT),
            "overlap_WTbar": abs(ovTb),
            "joint_order_WT": j_ord_T,
            "joint_order_WTbar": j_ord_Tb,
        })

    passed = (
        cross_MT_diff < tol
        and cross_MS_diff < tol
        and MT_unit_err < tol
        and MS_unit_err < tol
        and cim_braid_err < tol
        and comm_MS2_MT_err < tol
        and comm_MS2_MR_err < tol
        and ms2_imag_err < tol
        and ms2_spec_err < tol
        and mt_turns_err < tol
        and all_cdim2
        and max_ov_T < tol
        and max_ov_Tb < tol
    )

    summary = {
        "cross_check_MT_diff": cross_MT_diff,
        "cross_check_MS_diff": cross_MS_diff,
        "MT_unitary_err": MT_unit_err,
        "MS_unitary_err": MS_unit_err,
        "braid_err": cim_braid_err,
        "MS2_comm_MT_err": comm_MS2_MT_err,
        "MS2_comm_MR_err": comm_MS2_MR_err,
        "MS2_eigenvalues": ms2_real,
        "MS2_spectrum_err": max(ms2_spec_err, ms2_imag_err),
        "MT_turns": mt_turns,
        "MT_turns_err": mt_turns_err,
        "all_24_twists_commutant_dim_2": all_cdim2,
        "max_overlap_WT_across_24": max_ov_T,
        "max_overlap_WTbar_across_24": max_ov_Tb,
        "twists": twist_records,
        "outcome": "Outcome [2]",
        "passed": passed,
    }
    return summary, {"MT": MT, "MS": MS, "MR": MR}


# =============================================================================
# Section 4 (W4): Half-Period Modes, Punctured-Torus L_2 ODEs, & Gate F-U2 -> Outcome [1]
# =============================================================================

def theta_and_dot_mp(alpha, beta, tau, N=28):
    """Evaluate theta(alpha, beta | tau) and d_theta = (1/2) sum (n+a)^2 q^{(n+a)^2/2}."""
    I = mp_i()
    th = mp.mpc(0)
    dth = mp.mpc(0)
    for n in range(-N, N + 1):
        na = n + alpha
        term = mp.exp(mp.pi * I * (na ** 2) * tau + 2 * mp.pi * I * na * beta)
        th += term
        dth += (mp.mpf(1) / 2) * (na ** 2) * term
    return th, dth


def eval_Rh_c3_mp(tau, q_terms=80):
    """Evaluate R_h(tau) and Ramanujan-Serre c_3(tau) directly on E_tau."""
    I = mp_i()
    q = mp.exp(2 * mp.pi * I * tau)
    eta = mp.exp(mp.pi * I * tau / 12)
    E2 = mp.mpf(1)
    qk = q
    for m in range(1, q_terms + 1):
        eta *= (1 - qk)
        E2 -= 24 * m * qk / (1 - qk)
        qk *= q
    denom_hat = 2 * mp.pi * (eta ** 3)
    th2, dth2 = theta_and_dot_mp(mp.mpf(1) / 2, mp.mpf(0), tau)
    th4, dth4 = theta_and_dot_mp(mp.mpf(0), mp.mpf(1) / 2, tau)
    th3, dth3 = theta_and_dot_mp(mp.mpf(0), mp.mpf(0), tau)

    Rh = mp.matrix([-(th2 ** 2) / denom_hat, -(th4 ** 2) / denom_hat, I * (th3 ** 2) / denom_hat])
    dNh = mp.matrix([
        -2 * th2 * dth2 / denom_hat,
        -2 * th4 * dth4 / denom_hat,
        2 * I * th3 * dth3 / denom_hat,
    ])
    c3 = dNh - (E2 / 12) * Rh
    return Rh, c3, denom_hat


def solve_L2_punctured_torus_gl6(tau, N=250):
    """Independent 3-stage 6th-order Gauss-Legendre shooting on punctured-torus Liouville BVP.

    Solves u''(t) = exp(2 u(t)) on t in [t_R, T_end] where t = -ln(r),
    R = sqrt(Im(tau)/pi) is the flat-area torus cell radius, t_R = -ln(R),
    with outer Neumann BC u'(t_R) = -1 and asymptotic cusp manifold BC
    u'(T_end) + exp(u(T_end)) = 0. Extracts the universal Keen horocycle
    collar radius r_0 = exp(-t_0) where 2*pi*exp(u(t_0)) = 2, returning L_2 = t_0.
    """
    with mp.workdps(30):
        y = mp.im(tau)
        tR = -mp.log(y / mp.pi) / 2
        T_end = mp.mpf(4)

        s15 = mp.sqrt(15)
        A = [
            [mp.mpf(5) / 36, mp.mpf(2) / 9 - s15 / 15, mp.mpf(5) / 36 - s15 / 30],
            [mp.mpf(5) / 36 + s15 / 24, mp.mpf(2) / 9, mp.mpf(5) / 36 - s15 / 24],
            [mp.mpf(5) / 36 + s15 / 30, mp.mpf(2) / 9 + s15 / 15, mp.mpf(5) / 36],
        ]
        b = [mp.mpf(5) / 18, mp.mpf(4) / 9, mp.mpf(5) / 18]
        h = (tR - T_end) / N
        stage_tol = mp.mpf(10) ** (-26)

        def gl6_step(u, v, hs):
            k_u = [v, v, v]
            e0 = mp.exp(2 * u)
            k_v = [e0, e0, e0]
            for _ in range(15):
                n_ku = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
                n_kv = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
                err = mp.mpf(0)
                for i in range(3):
                    ui = u + hs * (A[i][0] * k_u[0] + A[i][1] * k_u[1] + A[i][2] * k_u[2])
                    vi = v + hs * (A[i][0] * k_v[0] + A[i][1] * k_v[1] + A[i][2] * k_v[2])
                    n_ku[i] = vi
                    n_kv[i] = mp.exp(2 * ui)
                    d1 = abs(n_ku[i] - k_u[i])
                    d2 = abs(n_kv[i] - k_v[i])
                    if d1 > err:
                        err = d1
                    if d2 > err:
                        err = d2
                k_u, k_v = n_ku, n_kv
                if err < stage_tol:
                    break
            u_new = u + hs * (b[0] * k_u[0] + b[1] * k_u[1] + b[2] * k_u[2])
            v_new = v + hs * (b[0] * k_v[0] + b[1] * k_v[1] + b[2] * k_v[2])
            return u_new, v_new

        def shoot_residual(uT):
            u, v = uT, -mp.exp(uT)
            for _ in range(N):
                u, v = gl6_step(u, v, h)
            return v + 1

        # Non-trivial starting guess away from any hardcoded closed form
        u0 = -mp.log(T_end) - mp.mpf(1) / 5
        u1 = u0 + mp.mpf(1) / 50
        r0 = shoot_residual(u0)
        shoot_tol = mp.mpf(10) ** (-24)
        for _ in range(12):
            r1 = shoot_residual(u1)
            if abs(r1) < shoot_tol:
                u0 = u1
                break
            du = -r1 * (u1 - u0) / (r1 - r0)
            u0, r0 = u1, r1
            u1 = u1 + du
            if abs(du) < shoot_tol:
                u0 = u1
                break

        # Locate horocycle 2*pi*exp(u(t_0)) = 2 => u(t_0) = -ln(pi)
        u_target = -mp.log(mp.pi)
        u, v = u0, -mp.exp(u0)
        t = T_end
        for _ in range(N):
            un, vn = gl6_step(u, v, h)
            if u <= u_target <= un:
                dt = (u_target - u) / v
                for _ in range(8):
                    ue, ve = gl6_step(u, v, dt)
                    err = ue - u_target
                    if abs(err) < shoot_tol:
                        break
                    dt -= err / ve
                return t + dt
            u, v = un, vn
            t += h
        raise RuntimeError("GL6 failed to bracket horocycle target")


def solve_L2_punctured_torus_rk4(y_float, N=3000):
    """Independent fine explicit RK4 shooting cross-check on punctured-torus ODE."""
    tR = -math.log(y_float / math.pi) / 2
    T_end = 4 / 1
    h = (tR - T_end) / N
    half = 1 / 2

    def rk4_step(u, v, hs):
        k1u, k1v = v, math.exp(2 * u)
        u2, v2 = u + half * hs * k1u, v + half * hs * k1v
        k2u, k2v = v2, math.exp(2 * u2)
        u3, v3 = u + half * hs * k2u, v + half * hs * k2v
        k3u, k3v = v3, math.exp(2 * u3)
        u4, v4 = u + hs * k3u, v + hs * k3v
        k4u, k4v = v4, math.exp(2 * u4)
        return (
            u + (hs / 6) * (k1u + 2 * k2u + 2 * k3u + k4u),
            v + (hs / 6) * (k1v + 2 * k2v + 2 * k3v + k4v),
        )

    def shoot_residual(uT):
        u, v = uT, -math.exp(uT)
        for _ in range(N):
            u, v = rk4_step(u, v, h)
        return v + 1

    u0 = -math.log(T_end) - 1 / 5
    u1 = u0 + 1 / 50
    r0 = shoot_residual(u0)
    tol = pow10_neg(14)
    for _ in range(15):
        r1 = shoot_residual(u1)
        if abs(r1) < tol:
            u0 = u1
            break
        du = -r1 * (u1 - u0) / (r1 - r0)
        u0, r0 = u1, r1
        u1 = u1 + du
        if abs(du) < tol:
            u0 = u1
            break

    u_target = -math.log(math.pi)
    u, v = u0, -math.exp(u0)
    t = T_end
    for _ in range(N):
        un, vn = rk4_step(u, v, h)
        if u <= u_target <= un:
            dt = (u_target - u) / v
            for _ in range(8):
                ue, ve = rk4_step(u, v, dt)
                err = ue - u_target
                if abs(err) < tol:
                    break
                dt -= err / ve
            return t + dt
        u, v = un, vn
        t += h
    raise RuntimeError("RK4 failed to bracket horocycle target")


def build_fu2_constants():
    """Construct Clifford dual basis, coupling tensor C[qi,si,a,b], D1, B3, B2."""
    I = mp_i()
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = mp.matrix([[0, I], [I, 0]])
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]
    q_S = [QI, QJ, QK]

    def frob(A, B):
        s = mp.mpc(0)
        for r in range(2):
            for c in range(2):
                s += A[r, c] * B[r, c]
        return s

    ec_list = [EPS * U for U in units]
    Gmat = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            Gmat[t, s] = frob(ec_list[t], units[s])
    Ginv = Gmat ** (-1)
    edual = []
    for a in range(4):
        M = mp.zeros(2, 2)
        for b in range(4):
            M += Ginv[b, a] * units[b]
        edual.append(M)

    Cten = {}
    for qi in range(3):
        for si in range(4):
            for a in range(3):
                for b in range(3):
                    Cten[(qi, si, a, b)] = frob(blocks[a].T * EPS * q_S[qi] * blocks[b], edual[si])

    zeta5 = mp.exp(2 * mp.pi * I / 5)
    X5 = mp.zeros(5, 5)
    Z5 = mp.zeros(5, 5)
    for j in range(5):
        X5[(j + 1) % 5, j] = 1
        Z5[j, j] = zeta5 ** j

    s2inv = 1 / mp.sqrt(2)
    B3 = mp.zeros(5, 3)
    B3[0, 0] = 1
    B3[1, 1] = s2inv
    B3[4, 1] = s2inv
    B3[2, 2] = s2inv
    B3[3, 2] = s2inv
    B2 = mp.zeros(5, 2)
    B2[1, 0] = s2inv
    B2[4, 0] = -s2inv
    B2[2, 1] = s2inv
    B2[3, 1] = -s2inv

    D_proj3 = {}
    D_proj2 = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            D = (zeta5 ** ((3 * a * b) % 5)) * (X5 ** a) * (Z5 ** b)
            D_proj3[(a, b)] = B3.H * D * B3
            D_proj2[(a, b)] = B2.H * D * B2

    return {
        "ec_list": ec_list,
        "frob": frob,
        "Cten": Cten,
        "zeta5": zeta5,
        "D_proj3": D_proj3,
        "D_proj2": D_proj2,
    }


def X01_mp(alpha, beta, tau, N=26):
    """Evaluate X_0(alpha, beta) and X_1(alpha, beta)."""
    I = mp_i()
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    half = mp.mpf(1) / 2
    for k in range(-N, N + 1):
        n = k + alpha
        s0 += mp.exp(2 * mp.pi * I * tau * (n ** 2) + 2 * mp.pi * I * n * beta)
        s1 += mp.exp(2 * mp.pi * I * tau * ((n + half) ** 2) + 2 * mp.pi * I * n * beta)
    return s0, s1


def compute_fu_a0_mp(ua, ub, tau, M_lim=80):
    """Evaluate f_u and a_0 from Erratum 2."""
    I = mp_i()
    x = mp.re(tau)
    y = mp.im(tau)
    q = mp.exp(2 * mp.pi * I * tau)
    if ua == 0:
        fu = (
            mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
            + (mp.pi ** 2) * y / (mp.sin(mp.pi * ub) ** 2)
        )
        for m in range(1, M_lim + 1):
            for s in (m, -m):
                ws = mp.exp(2 * mp.pi * I * (s * x + ub) - 2 * mp.pi * abs(s) * y)
                fu += (2 * mp.pi / abs(s)) * mp.re(ws / (1 - ws))
    else:
        fu = -mp.pi * (mp.digamma(ua) + mp.digamma(1 - ua) + 2 * mp.log(2) + mp.log(y))
        for k in range(-M_lim, M_lim + 1):
            s = k + ua
            ws = mp.exp(2 * mp.pi * I * (s * x + ub) - 2 * mp.pi * abs(s) * y)
            fu += (2 * mp.pi / abs(s)) * mp.re(ws / (1 - ws))

    nu = ua if ua <= mp.mpf(1) / 2 else ua - 1
    Bm = (-ub) % 1
    wz = nu * tau - Bm
    a0 = mp.pi * mp.cot(mp.pi * wz) + 2 * mp.pi * I * nu
    qm = q
    for m in range(1, M_lim + 1):
        num = mp.exp(2 * mp.pi * I * m * (tau + wz)) - mp.exp(2 * mp.pi * I * m * (tau - wz))
        a0 += 4 * mp.pi * num / (2 * I * (1 - qm))
        qm *= q
    return fu, abs(a0) ** 2


def prepare_fu2_tau_cache(tau, consts):
    """Precompute tau-dependent theta/Eisenstein/f_u/|a_0|^2 data independent of L_2."""
    I = mp_i()
    frob = consts["frob"]
    ec_list = consts["ec_list"]
    _, c3, denom = eval_Rh_c3_mp(tau, q_terms=80)
    CHAR_SHIFTS = [
        (mp.mpf(0), mp.mpf(0)),
        (mp.mpf(0), mp.mpf(-1) / 2),
        (mp.mpf(-1) / 2, mp.mpf(0)),
        (mp.mpf(-1) / 2, mp.mpf(-1) / 2),
    ]

    def point_data(wL, wR):
        ax, bx = wL[0], 2 * wL[1]
        ay, by = wR[0], 2 * wR[1]
        X0x, X1x = X01_mp(ax, bx, tau)
        X0y, X1y = X01_mp(ay, by, tau)
        Mm = mp.matrix([
            [X0x * X0y, -I * mp.exp(mp.pi * I * by) * X0x * X1y],
            [-I * mp.exp(mp.pi * I * bx) * X1x * X0y, -mp.exp(mp.pi * I * (bx + by)) * X1x * X1y],
        ]) / denom
        Rch = [frob(ec_list[si], Mm) for si in range(4)]
        shifts = []
        for ds1, ds2 in CHAR_SHIFTS:
            ua = (wL[0] + wR[0] + ds1) % 1
            ub = (wL[1] + wR[1] + ds2) % 1
            if ua == 0 and ub == 0:
                shifts.append(None)
            else:
                shifts.append(compute_fu_a0_mp(ua, ub, tau))
        return Rch, shifts

    base_data = point_data((mp.mpf(0), mp.mpf(0)), (mp.mpf(0), mp.mpf(0)))
    orbit_data = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            ac = a if a <= 2 else a - 5
            bc = b if b <= 2 else b - 5
            wL = (mp.mpf(ac) / 5, mp.mpf(bc) / 5)
            wR = (mp.mpf(2 * ac) / 5, mp.mpf(2 * bc) / 5)
            orbit_data[(a, b)] = point_data(wL, wR)

    return {
        "y": mp.im(tau),
        "c3": c3,
        "base_data": base_data,
        "orbit_data": orbit_data,
    }


def eval_fu2_observables(tau_cache, L2, consts):
    """Evaluate (r_u, r_d, r_e) and |V_CKM| for both phased_sum and base_w0 at L2."""
    y = tau_cache["y"]
    c3 = tau_cache["c3"]
    Cten = consts["Cten"]
    zeta5 = consts["zeta5"]
    D_proj3 = consts["D_proj3"]
    D_proj2 = consts["D_proj2"]

    def eval_Y_from_data(pdata):
        Rch, shifts = pdata
        uch = []
        for si in range(4):
            item = shifts[si]
            if item is None:
                uch.append(mp.mpc(0))
            else:
                fu, a0_sq = item
                arg = (
                    2 * mp.pi * (L2 + mp.mpf(1) / 2 * mp.log(y) - mp.euler - mp.log(mp.pi))
                    + fu
                    - mp.pi * a0_sq * mp.exp(-2 * L2)
                )
                uch.append(mp.sqrt(arg) * Rch[si])
        Y = mp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                s = mp.mpc(0)
                for qi in range(3):
                    for si in range(4):
                        s += c3[qi] * uch[si] * Cten[(qi, si, a, b)]
                Y[a, b] = s
        return Y

    Ybase = eval_Y_from_data(tau_cache["base_data"])
    Sph = mp.zeros(3, 3)
    O3 = {}
    O2 = {}
    for (a, b), pdata in tau_cache["orbit_data"].items():
        Yw = eval_Y_from_data(pdata)
        phi_ab = zeta5 ** ((-a * b) % 5)
        Sph += phi_ab * Yw
        M3 = D_proj3[(a, b)]
        M2 = D_proj2[(a, b)]
        for i in range(3):
            for j in range(3):
                yij = phi_ab * Yw[i, j]
                for ca in range(3):
                    for cb in range(3):
                        key3 = (i, ca, j, cb)
                        O3[key3] = O3.get(key3, mp.mpc(0)) + yij * M3[ca, cb]
                for wa in range(2):
                    for wb in range(2):
                        key2 = (i, wa, j, wb)
                        O2[key2] = O2.get(key2, mp.mpc(0)) + yij * M2[wa, wb]

    def gram_L(O, dm):
        G = mp.zeros(3, 3)
        for i in range(3):
            for k in range(3):
                s = mp.mpc(0)
                for ca in range(dm):
                    for j in range(3):
                        for cb in range(dm):
                            s += O[(i, ca, j, cb)] * mp.conj(O[(k, ca, j, cb)])
                G[i, k] = s / dm
        return G

    def gram_R(O, dm):
        G = mp.zeros(3, 3)
        for i in range(3):
            for k in range(3):
                s = mp.mpc(0)
                for j in range(3):
                    for ca in range(dm):
                        for cb in range(dm):
                            s += mp.conj(O[(j, ca, i, cb)]) * O[(j, ca, k, cb)]
                G[i, k] = s / dm
        return G

    def inv_sqrt_herm(M):
        ev, U = mp.eigh(M)
        D = mp.zeros(3, 3)
        for idx in range(3):
            D[idx, idx] = 1 / mp.sqrt(ev[idx])
        return U * D * U.H

    G3L, G2L = gram_L(O3, 3), gram_L(O2, 2)
    G3R, G2R = gram_R(O3, 3), gram_R(O2, 2)
    KQL_ih = inv_sqrt_herm(G3L + G2L)
    KLL_ih = inv_sqrt_herm(3 * G3L + G2L)
    KuR_ih = inv_sqrt_herm(2 * G3R)
    KdR_ih = inv_sqrt_herm(2 * G3R + 2 * G2R)
    KeR_ih = inv_sqrt_herm(2 * G2R)

    out = {}
    for label, Yh in [("phased_sum", Sph), ("base_w0", Ybase)]:
        Yu = KQL_ih * Yh * KuR_ih
        Yd = KQL_ih * Yh * KdR_ih
        Ye = KLL_ih * Yh * KeR_ih
        ratios = {}
        Us = {}
        for f, Yf in [("u", Yu), ("d", Yd), ("e", Ye)]:
            ev, Uf = mp.eigh(Yf * Yf.H)
            sig = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in reversed(ev)]
            ratios[f] = [sig[1] / sig[0], sig[2] / sig[0]]
            Udesc = mp.matrix(3, 3)
            for col in range(3):
                for row in range(3):
                    Udesc[row, col] = Uf[row, 2 - col]
            Us[f] = Udesc
        Vckm = Us["u"].H * Us["d"]
        absV = [[abs(Vckm[r, c]) for c in range(3)] for r in range(3)]
        out[label] = (ratios, absV)
    return out


def run_w4_half_period_and_fu2(TL, TR, TbL, TbR):
    """Verify R_h & c_3 modular covariance, independent ODE L_2, Gate F-U2, and 24 twists."""
    tol = pow10_neg(12)
    mp.mp.dps = 45
    I = mp_i()

    rT_mp = mp.exp(I * mp.pi / 4) * mp.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    P01_mp = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    R0_mp = P01_mp * (rT_mp ** (-1)) * (P01_mp ** (-1))

    # 1. Direct E_tau evaluation of R_h and c_3 at two generic moduli
    tau_tests = [
        ("tau1", mp.mpf(17) / 100 + I * mp.mpf(13) / 10),
        ("tau2", mp.mpf(-2) / 7 + I * mp.mpf(19) / 10),
    ]
    automorphy_checks = {}
    all_auto_ok = True
    for name, tau in tau_tests:
        Rh, c3, _ = eval_Rh_c3_mp(tau)
        Rh_T, c3_T, _ = eval_Rh_c3_mp(tau + 1)
        Rh_S, c3_S, _ = eval_Rh_c3_mp(-1 / tau)
        Rh_R, c3_R, _ = eval_Rh_c3_mp(tau / (tau + 1))

        err_Rh_T = float(max(abs((Rh_T - rT_mp * Rh)[i]) for i in range(3)))
        err_c3_T = float(max(abs((c3_T - rT_mp * c3)[i]) for i in range(3)))

        w_mhalf = (-I * tau) ** (mp.mpf(-1) / 2)
        w_3half = (-I * tau) ** (mp.mpf(3) / 2)
        err_Rh_S = float(max(abs((Rh_S - w_mhalf * P01_mp * Rh)[i]) for i in range(3)))
        err_c3_S = float(max(abs((c3_S + w_3half * P01_mp * c3)[i]) for i in range(3)))

        r_fac_Rh = (tau + 1) ** (mp.mpf(-1) / 2)
        r_fac_c3 = (tau + 1) ** (mp.mpf(3) / 2)
        err_Rh_R = float(max(abs((Rh_R - r_fac_Rh * R0_mp * Rh)[i]) for i in range(3)))
        err_c3_R = float(max(abs((c3_R - r_fac_c3 * R0_mp * c3)[i]) for i in range(3)))

        ok = max(err_Rh_T, err_c3_T, err_Rh_S, err_c3_S, err_Rh_R, err_c3_R) < tol
        all_auto_ok = all_auto_ok and ok
        automorphy_checks[name] = {
            "Rh_T_err": err_Rh_T,
            "c3_T_err": err_c3_T,
            "Rh_S_err": err_Rh_S,
            "c3_S_err": err_c3_S,
            "Rh_R_proj_err": err_Rh_R,
            "c3_R_proj_err": err_c3_R,
            "passed": ok,
        }

    # 2. Independent punctured-torus L_2 ODE integrators (GL6 + RK4 cross-check)
    tau0 = mp.mpf(13) / 100 + I * mp.mpf(17) / 10
    tauL = tau0 + 1
    tauR = tau0 / (tau0 + 1)

    L2_gl6_0 = solve_L2_punctured_torus_gl6(tau0)
    L2_gl6_L = solve_L2_punctured_torus_gl6(tauL)
    L2_gl6_R = solve_L2_punctured_torus_gl6(tauR)

    mp.mp.dps = 40
    cov_gl6_L = to_py_float(abs(L2_gl6_L - L2_gl6_0))
    cov_gl6_R = to_py_float(abs(L2_gl6_R - (L2_gl6_0 + mp.log(abs(tau0 + 1)))))

    L2_rk4_0 = solve_L2_punctured_torus_rk4(to_py_float(mp.im(tau0)))
    L2_rk4_L = solve_L2_punctured_torus_rk4(to_py_float(mp.im(tauL)))
    L2_rk4_R = solve_L2_punctured_torus_rk4(to_py_float(mp.im(tauR)))
    cov_rk4_L = abs(L2_rk4_L - L2_rk4_0)
    cov_rk4_R = abs(L2_rk4_R - (L2_rk4_0 + math.log(abs(to_py_complex(tau0 + 1)))))
    gl6_vs_rk4_diff = abs(to_py_float(L2_gl6_0) - L2_rk4_0)

    ode_ok = (
        cov_gl6_L < tol
        and cov_gl6_R < tol
        and cov_rk4_L < tol
        and cov_rk4_R < tol
        and gl6_vs_rk4_diff < tol
    )

    # 3. Gate F-U2 24-pt O_1(tau) at tau_0 for BOTH ODE L_2 and seed 5/2
    consts = build_fu2_constants()
    cache0 = prepare_fu2_tau_cache(tau0, consts)
    cacheL = prepare_fu2_tau_cache(tauL, consts)
    cacheR = prepare_fu2_tau_cache(tauR, consts)

    seed_0 = mp.mpf(5) / 2
    seed_L = seed_0
    seed_R = seed_0 + mp.log(abs(tau0 + 1))

    fu2_modes = {}
    all_fu2_ok = True
    for mode_name, (l0, lL, lR) in [
        ("ode_gl6", (L2_gl6_0, L2_gl6_L, L2_gl6_R)),
        ("seed_5_2", (seed_0, seed_L, seed_R)),
    ]:
        res0 = eval_fu2_observables(cache0, l0, consts)
        resL = eval_fu2_observables(cacheL, lL, consts)
        resR = eval_fu2_observables(cacheR, lR, consts)
        sub = {}
        for lbl in ("phased_sum", "base_w0"):
            rat0, V0 = res0[lbl]
            ratL, VL = resL[lbl]
            ratR, VR = resR[lbl]
            dL_rat = to_py_float(max(abs(rat0[f][k] - ratL[f][k]) for f in ("u", "d", "e") for k in range(2)))
            dR_rat = to_py_float(max(abs(rat0[f][k] - ratR[f][k]) for f in ("u", "d", "e") for k in range(2)))
            dL_V = to_py_float(max(abs(V0[i][j] - VL[i][j]) for i in range(3) for j in range(3)))
            dR_V = to_py_float(max(abs(V0[i][j] - VR[i][j]) for i in range(3) for j in range(3)))
            ok = max(dL_rat, dR_rat, dL_V, dR_V) < tol
            all_fu2_ok = all_fu2_ok and ok
            sub[lbl] = {
                "ratios_tau0": {f: [to_py_float(x) for x in rat0[f]] for f in ("u", "d", "e")},
                "V_CKM_tau0": [[to_py_float(V0[i][j]) for j in range(3)] for i in range(3)],
                "drift_L_ratios": dL_rat,
                "drift_R_ratios": dR_rat,
                "drift_L_Vckm": dL_V,
                "drift_R_Vckm": dR_V,
                "passed": ok,
            }
        fu2_modes[mode_name] = sub

    # 4. Full 24-twist scan k = 0..23 and B1736 det=1 diagnosis
    rT = mp_mat_to_np(rT_mp)
    R0 = mp_mat_to_np(R0_mp)
    cT = complex(math.cos(2 * math.pi / 24), math.sin(2 * math.pi / 24))

    twist_rows = []
    rho_by_k = {}
    det1_orders = {}
    U0_mat = None
    U18_mat = None
    ov0_Tb_complex = complex(0, 0)
    ov18_T_complex = complex(0, 0)

    for k in range(24):
        rkL = (cT ** k) * rT
        rkR = (cT ** (-k)) * R0
        rho_by_k[k] = (rkL, rkR)
        Gk = gen_group_fast([rkL, rkR])
        cd = commutant_dim([rkL, rkR])
        ovT, jT = char_overlap([rkL, rkR], [TL, TR])
        ovTb, jTb = char_overlap([rkL, rkR], [TbL, TbR])
        if k == 0:
            ov0_Tb_complex = ovTb
        if k == 18:
            ov18_T_complex = ovT
        detL = complex(np.linalg.det(rkL))
        det_is_1 = abs(detL - 1) < tol
        if det_is_1:
            det1_orders[k] = len(Gk)
        twist_rows.append({
            "k": k,
            "order": len(Gk),
            "commutant_dim": cd,
            "overlap_WT": abs(ovT),
            "overlap_WTbar": abs(ovTb),
            "joint_order_WT": jT,
            "joint_order_WTbar": jTb,
            "det_L_real": detL.real,
            "det_L_imag": detL.imag,
            "det_is_1": det_is_1,
        })

    # k = 0 intertwiner onto W:\overline{T}
    n0, mats0 = intertwiner_space([TbL, TbR], list(rho_by_k[0]))
    U0_mat, U0_unit_err, U0_int_err = make_unitary_intertwiner(mats0[0], [TbL, TbR], list(rho_by_k[0]))
    n0_wrong, _ = intertwiner_space([TL, TR], list(rho_by_k[0]))

    # k = 18 intertwiner onto W:T and conjugate check (conj(r_T), conj(R_0)) == rho_18
    conj_18_err = max(
        float(np.max(np.abs(rT.conj() - rho_by_k[18][0]))),
        float(np.max(np.abs(R0.conj() - rho_by_k[18][1]))),
    )
    n18, mats18 = intertwiner_space([TL, TR], list(rho_by_k[18]))
    U18_mat, U18_unit_err, U18_int_err = make_unitary_intertwiner(mats18[0], [TL, TR], list(rho_by_k[18]))
    n18_wrong, _ = intertwiner_space([TbL, TbR], list(rho_by_k[18]))

    other_twists_zero = all(
        row["overlap_WT"] < tol and row["overlap_WTbar"] < tol
        for row in twist_rows
        if row["k"] not in (0, 18)
    )
    k0_ok = (
        twist_rows[0]["order"] == 96
        and twist_rows[0]["commutant_dim"] == 1
        and abs(ov0_Tb_complex - 1) < tol
        and twist_rows[0]["overlap_WT"] < tol
        and n0 == 1
        and n0_wrong == 0
        and U0_unit_err < tol
        and U0_int_err < tol
    )
    k18_ok = (
        conj_18_err < tol
        and twist_rows[18]["order"] == 96
        and twist_rows[18]["commutant_dim"] == 1
        and abs(ov18_T_complex - 1) < tol
        and twist_rows[18]["overlap_WTbar"] < tol
        and n18 == 1
        and n18_wrong == 0
        and U18_unit_err < tol
        and U18_int_err < tol
    )
    b1736_ok = det1_orders == {5: 72, 13: 72, 21: 24}

    passed = (
        all_auto_ok
        and ode_ok
        and all_fu2_ok
        and k0_ok
        and k18_ok
        and other_twists_zero
        and b1736_ok
    )

    summary = {
        "automorphy_checks": automorphy_checks,
        "L2_ode": {
            "tau0": [to_py_float(mp.re(tau0)), to_py_float(mp.im(tau0))],
            "gl6_L2_tau0": to_py_float(L2_gl6_0),
            "gl6_L2_tau0_str": mp.nstr(L2_gl6_0, 26),
            "gl6_cov_L": cov_gl6_L,
            "gl6_cov_R": cov_gl6_R,
            "rk4_L2_tau0": L2_rk4_0,
            "rk4_cov_L": cov_rk4_L,
            "rk4_cov_R": cov_rk4_R,
            "gl6_vs_rk4_diff": gl6_vs_rk4_diff,
            "passed": ode_ok,
        },
        "gate_fu2_24pt": {
            "modes": fu2_modes,
            "passed": all_fu2_ok,
        },
        "k0_match_WTbar": {
            "order": twist_rows[0]["order"],
            "commutant_dim": twist_rows[0]["commutant_dim"],
            "overlap_WTbar": twist_rows[0]["overlap_WTbar"],
            "overlap_WT": twist_rows[0]["overlap_WT"],
            "intertwiner_nullspace_dim": n0,
            "wrong_chirality_nullspace_dim": n0_wrong,
            "U0_unitary_err": U0_unit_err,
            "U0_intertwine_err": U0_int_err,
            "passed": k0_ok,
        },
        "k18_match_WT": {
            "conj_rT_R0_equals_rho18_err": conj_18_err,
            "order": twist_rows[18]["order"],
            "commutant_dim": twist_rows[18]["commutant_dim"],
            "overlap_WT": twist_rows[18]["overlap_WT"],
            "overlap_WTbar": twist_rows[18]["overlap_WTbar"],
            "intertwiner_nullspace_dim": n18,
            "wrong_chirality_nullspace_dim": n18_wrong,
            "U18_unitary_err": U18_unit_err,
            "U18_intertwine_err": U18_int_err,
            "passed": k18_ok,
        },
        "other_22_twists_zero_overlap": other_twists_zero,
        "B1736_det1_orders": {str(k): v for k, v in sorted(det1_orders.items())},
        "B1736_diagnosis_passed": b1736_ok,
        "twists": twist_rows,
        "outcome": "Outcome [1]",
        "passed": passed,
    }
    return summary, {"rho0": rho_by_k[0], "rho18": rho_by_k[18], "rho21": rho_by_k[21], "U0": U0_mat, "U18": U18_mat}


# =============================================================================
# Section 5: Guardrail 3 (10-Trial Haar Scrambling) & 5 Planted Faults (PF1..PF5)
# =============================================================================

def random_haar_unitary(d, rng):
    """Sample random Haar U(d) via QR of complex Ginibre matrix."""
    Z = rng.standard_normal((d, d)) + c_i() * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    diag_R = np.diag(R)
    phases = diag_R / np.abs(diag_R)
    return Q @ np.diag(phases)


def run_section_5_haar_and_planted_faults(w1_art, cim_art, w4_art):
    """Run 10-trial Haar U(6)xU(3) scrambling and adversarial PF1..PF5 checks."""
    tol = pow10_neg(12)
    rng = np.random.default_rng(20261120)

    H_Q = w1_art["H_Q"]
    ML = w1_art["ML"]
    MR = w1_art["MR"]
    TL = w1_art["TL"]
    TR = w1_art["TR"]
    TbL = w1_art["TbL"]
    TbR = w1_art["TbR"]
    r0L, r0R = w4_art["rho0"]
    r18L, r18R = w4_art["rho18"]
    cimL, cimR = cim_art["MT"], cim_art["MR"]

    haar_trials = []
    max_haar_err = 0 / 1
    all_haar_ok = True
    expected_evals = np.array([-4, -4, -4, 4, 4, 4])

    for trial in range(10):
        U = random_haar_unitary(6, rng)
        W = random_haar_unitary(3, rng)
        U_haar_err = float(np.max(np.abs(U.conj().T @ U - np.eye(6, dtype=complex))))
        W_haar_err = float(np.max(np.abs(W.conj().T @ W - np.eye(3, dtype=complex))))

        H_Qp = U @ H_Q @ U.conj().T
        MLp = U @ ML @ U.conj().T
        MRp = U @ MR @ U.conj().T

        evals_p, evecs_p = np.linalg.eigh(H_Qp)
        hq_err = float(np.max(np.abs(np.sort(evals_p) - expected_evals)))
        sig_p = [int(np.sum(evals_p > 0)), int(np.sum(evals_p < 0))]

        Vpp = evecs_p[:, 3:]
        Vmp = evecs_p[:, :3]
        TLp = Vpp.conj().T @ MLp @ Vpp
        TRp = Vpp.conj().T @ MRp @ Vpp
        TbLp = Vmp.conj().T @ MLp @ Vmp
        TbRp = Vmp.conj().T @ MRp @ Vmp

        r0Lp = W @ r0L @ W.conj().T
        r0Rp = W @ r0R @ W.conj().T
        r18Lp = W @ r18L @ W.conj().T
        r18Rp = W @ r18R @ W.conj().T
        cimLp = W @ cimL @ W.conj().T
        cimRp = W @ cimR @ W.conj().T

        ord_LR = len(gen_group_fast([MLp, MRp]))
        cdim_LR = commutant_dim([MLp, MRp])
        b_LR = braid_err(MLp, MRp)
        b_0 = braid_err(r0Lp, r0Rp)
        b_18 = braid_err(r18Lp, r18Rp)

        ov_0_Tb, _ = char_overlap([r0Lp, r0Rp], [TbLp, TbRp])
        ov_0_T, _ = char_overlap([r0Lp, r0Rp], [TLp, TRp])
        ov_18_T, _ = char_overlap([r18Lp, r18Rp], [TLp, TRp])
        ov_18_Tb, _ = char_overlap([r18Lp, r18Rp], [TbLp, TbRp])
        ov_cim_T, _ = char_overlap([cimLp, cimRp], [TLp, TRp])
        ov_cim_Tb, _ = char_overlap([cimLp, cimRp], [TbLp, TbRp])

        n0, m0 = intertwiner_space([TbLp, TbRp], [r0Lp, r0Rp])
        n18, m18 = intertwiner_space([TLp, TRp], [r18Lp, r18Rp])
        U0p, U0_uerr, U0_ierr = make_unitary_intertwiner(m0[0], [TbLp, TbRp], [r0Lp, r0Rp])
        U18p, U18_uerr, U18_ierr = make_unitary_intertwiner(m18[0], [TLp, TRp], [r18Lp, r18Rp])
        cd_0 = commutant_dim([r0Lp, r0Rp])
        cd_18 = commutant_dim([r18Lp, r18Rp])
        cd_cim = commutant_dim([cimLp, cimRp])

        trial_err = max(
            U_haar_err,
            W_haar_err,
            hq_err,
            b_LR,
            b_0,
            b_18,
            abs(ov_0_Tb - 1),
            abs(ov_0_T),
            abs(ov_18_T - 1),
            abs(ov_18_Tb),
            abs(ov_cim_T),
            abs(ov_cim_Tb),
            U0_uerr,
            U0_ierr,
            U18_uerr,
            U18_ierr,
        )
        max_haar_err = max(max_haar_err, trial_err)
        ok = (
            trial_err < tol
            and sig_p == [3, 3]
            and ord_LR == 96
            and cdim_LR == 2
            and cd_0 == 1
            and cd_18 == 1
            and cd_cim == 2
            and n0 == 1
            and n18 == 1
        )
        all_haar_ok = all_haar_ok and ok
        haar_trials.append({
            "trial": trial,
            "max_residual": trial_err,
            "order_G_LR": ord_LR,
            "commutant_dims": {"G_LR": cdim_LR, "rho0": cd_0, "rho18": cd_18, "cim": cd_cim},
            "passed": ok,
        })

    # Planted Faults PF1..PF5
    # PF1: det=1 at k=21 falsely claimed to give order 96 & unit overlap with W:T
    r21L, r21R = w4_art["rho21"]
    G21 = gen_group_fast([r21L, r21R])
    ov21_T, _ = char_overlap([r21L, r21R], [TL, TR])
    n21, _ = intertwiner_space([TL, TR], [r21L, r21R])
    pf1_caught = (
        abs(complex(np.linalg.det(r21L)) - 1) < tol
        and len(G21) == 24
        and len(G21) != 96
        and abs(ov21_T) < tol
        and n21 == 0
    )

    # PF2: Swap (0, 1) chirality labels (claim k=0 intertwines H_Q>0 = W:T instead of W:\overline{T})
    ov0_T_wrong, _ = char_overlap([r0L, r0R], [TL, TR])
    n0_wrong, _ = intertwiner_space([TL, TR], [r0L, r0R])
    pf2_caught = (abs(ov0_T_wrong) < tol) and (n0_wrong == 0)

    # PF3: Claim CIM Level-3 is irreducible (commutant dim 1)
    cim_cd = commutant_dim([cimL, cimR])
    cim_S2 = cim_art["MS"] @ cim_art["MS"]
    cim_comm_err = max(
        float(np.max(np.abs(cim_S2 @ cimL - cimL @ cim_S2))),
        float(np.max(np.abs(cim_S2 @ cimR - cimR @ cim_S2))),
    )
    ov_cim_T0, _ = char_overlap([cimL, cimR], [TL, TR])
    ov_cim_Tb0, _ = char_overlap([cimL, cimR], [TbL, TbR])
    pf3_caught = (
        cim_cd == 2
        and cim_cd != 1
        and cim_comm_err < tol
        and abs(ov_cim_T0) < tol
        and abs(ov_cim_Tb0) < tol
    )

    # PF4: Break spin lift / parity:
    # (a) single trivial parity p = (0, 0) -> dim = 2 != 6
    I2, qi, qj, _ = w1_art["I2"], w1_art["qi"], w1_art["qj"], None
    s2 = math.sqrt(2)
    gL = (I2 + qi) / s2
    gR_good = (I2 - qj) / s2
    gR_bad = (I2 + qj) / s2
    triv_bases, _ = build_cohomology_space([(0, 0)], I2, qi, qj)
    ML_triv = build_automorphism_operator("a", "ab", gL, [(0, 0)], triv_bases, I2, qi, qj)
    MR_triv = build_automorphism_operator("ab", "b", gR_good, [(0, 0)], triv_bases, I2, qi, qj)
    ord_triv = len(gen_group_fast([ML_triv, MR_triv]))
    # (b) flip gR sign -> breaks 3-strand braid relation
    MR_bad = build_automorphism_operator("ab", "b", gR_bad, PAR, w1_art["bases"], I2, qi, qj)
    bad_braid = braid_err(ML, MR_bad)
    pf4_caught = (ML_triv.shape[0] == 2) and (ord_triv != 96) and (bad_braid > 1 / 2)

    # PF5: Claim unaveraged N=5 Wilson line w0 = (1/5, 0) is fixed by <L, R>
    L_mod = ((1, 1), (0, 1))
    R_mod = ((1, 0), (1, 1))
    w0 = (1, 0)
    w0_row_L = ((w0[0] * L_mod[0][0] + w0[1] * L_mod[1][0]) % 5, (w0[0] * L_mod[0][1] + w0[1] * L_mod[1][1]) % 5)
    w0_col_R = ((R_mod[0][0] * w0[0] + R_mod[0][1] * w0[1]) % 5, (R_mod[1][0] * w0[0] + R_mod[1][1] * w0[1]) % 5)
    pf5_caught = (w0_row_L != w0) and (w0_col_R != w0)

    planted_faults = {
        "PF1_det1_k21": {"order_k21": len(G21), "overlap_WT": abs(ov21_T), "nullspace_dim": n21, "caught": pf1_caught},
        "PF2_swap_chirality_k0": {"overlap_WT": abs(ov0_T_wrong), "nullspace_dim": n0_wrong, "caught": pf2_caught},
        "PF3_cim_irreducible": {"commutant_dim": cim_cd, "MS2_comm_err": cim_comm_err, "caught": pf3_caught},
        "PF4_broken_parity_or_gR": {
            "trivial_parity_dim": ML_triv.shape[0],
            "trivial_parity_order": ord_triv,
            "flipped_gR_braid_err": bad_braid,
            "caught": pf4_caught,
        },
        "PF5_unaveraged_N5_fixed": {"row_L_1_0": list(w0_row_L), "col_R_1_0": list(w0_col_R), "caught": pf5_caught},
    }
    all_pf_caught = all(v["caught"] for v in planted_faults.values())

    return {
        "haar_10_trials": {
            "trials": haar_trials,
            "max_residual_across_trials": max_haar_err,
            "passed": all_haar_ok,
        },
        "planted_faults": planted_faults,
        "all_5_planted_faults_caught": all_pf_caught,
        "passed": all_haar_ok and all_pf_caught,
    }


def main():
    t_start = time.time()
    script_path = Path(__file__).resolve()

    sec0 = run_section_0_custody(script_path)
    w1_sum, w1_art = run_w1_cohomology()
    w2_sum = run_w2_wilson_line()
    w3_sum, cim_art = run_w3_cim_level3(w1_art["TL"], w1_art["TR"], w1_art["TbL"], w1_art["TbR"])
    w4_sum, w4_art = run_w4_half_period_and_fu2(w1_art["TL"], w1_art["TR"], w1_art["TbL"], w1_art["TbR"])
    sec5 = run_section_5_haar_and_planted_faults(w1_art, cim_art, w4_art)

    all_gates_passed = (
        sec0["passed"]
        and w1_sum["passed"]
        and w2_sum["passed"]
        and w3_sum["passed"]
        and w4_sum["passed"]
        and sec5["passed"]
    )

    report = {
        "card": "AGY-002 / A2-WG96 Cold-Room Zero-Trust Referee",
        "empirical_firewall": "0 of 19",
        "elapsed_seconds": time.time() - t_start,
        "section_0_ast_and_custody": sec0,
        "W1_cohomology_W_G96_and_B1610": w1_sum,
        "W2_candidate_I_wilson_line": w2_sum,
        "W3_candidate_II_cim_level3": w3_sum,
        "W4_candidate_III_half_period_and_fu2": w4_sum,
        "section_5_haar_and_planted_faults": sec5,
        "all_gates_passed": all_gates_passed,
    }

    out_path = script_path.parent / "referee_a2_wg96_out.json"
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
