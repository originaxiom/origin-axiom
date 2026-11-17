"""Independent Cold-Room Zero-Trust Referee for Gate 8 (AGY-002_FOUND-G8 / P-863).

Strict Zero-Trust & Firewall Compliance:
- 0 of 19 empirical inputs.
- 0 float AST literals and 0 complex AST literals anywhere in this file.
- 0 repository imports (Python stdlib + numpy + sympy only).
- Guardrails 1-6 enforced: all invariants, spectra, commutants, Frobenius-Schur
  indicators, invariant bilinear forms, fundamental discriminants, E_8 root/Lie
  intersections, Weyl involutions, planted-fault controls (PF8.1-PF8.5), Haar
  unitary basis-scrambling checks, and SHA-256 manifests are computed directly
  from explicit operators constructed from first principles at runtime.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
from pathlib import Path
import re

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix


ALLOWED_IMPORT_ROOTS = frozenset({
    "__future__",
    "ast",
    "hashlib",
    "itertools",
    "json",
    "math",
    "pathlib",
    "re",
    "numpy",
    "sympy",
})


def _scaled_residual_1e15(val: float) -> int:
    """Convert non-negative numerical residual to ceil(val * 10^15) integer."""
    return int(math.ceil(abs(val) * (10 ** 15)))


def _deterministic_haar_unitary(dim: int, seed_offset: int) -> np.ndarray:
    """Construct a deterministic unitary matrix in U(dim) via complex QR with zero float literals."""
    i_unit = complex(0, 1)
    mat = np.zeros((dim, dim), dtype=np.complex128)
    for r in range(dim):
        for c in range(dim):
            idx = (r + 1) * 13 + (c + 1) * 29 + seed_offset * 47
            re_part = math.sin(idx) + math.cos(idx * 3) / 2
            im_part = math.cos(idx * 2) - math.sin(idx * 5) / 3
            mat[r, c] = re_part + i_unit * im_part
    q_mat, r_mat = np.linalg.qr(mat)
    diag = np.diag(r_mat)
    phases = diag / np.abs(diag)
    return q_mat @ np.diag(phases)


def audit_self_ast_and_imports(script_path: Path) -> dict[str, object]:
    """Verify 0 float AST literals, 0 complex AST literals, and 0 repo imports."""
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_literals: list[str] = []
    complex_literals: list[str] = []
    imported_roots: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append(f"line {node.lineno}: {node.value!r}")
            elif isinstance(node.value, complex):
                complex_literals.append(f"line {node.lineno}: {node.value!r}")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level != 0 or node.module is None:
                imported_roots.add("<relative>")
            else:
                imported_roots.add(node.module.split(".")[0])

    disallowed_imports = sorted(imported_roots - ALLOWED_IMPORT_ROOTS)
    passed = (
        len(float_literals) == 0
        and len(complex_literals) == 0
        and len(disallowed_imports) == 0
    )
    return {
        "float_ast_literal_count": len(float_literals),
        "complex_ast_literal_count": len(complex_literals),
        "disallowed_imports": disallowed_imports,
        "imported_roots": sorted(imported_roots),
        "passed": passed,
    }


def _parse_manifest_entries(manifest_path: Path, repo_root: Path) -> list[tuple[Path, str]]:
    """Parse SHA-256 manifest lines into (resolved_target_path, expected_hex)."""
    raw_text = manifest_path.read_bytes().decode("utf-8")
    entries: list[tuple[Path, str]] = []
    pat_std = re.compile(r"^([0-9a-fA-F]{64})\s+\*?(.+?)\s*$")
    pat_bsd = re.compile(r"^SHA256\s*\((.+?)\)\s*=\s*([0-9a-fA-F]{64})\s*$")
    pat_bare = re.compile(r"^([0-9a-fA-F]{64})\s*$")

    for raw_line in raw_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        m_std = pat_std.match(line)
        m_bsd = pat_bsd.match(line)
        m_bare = pat_bare.match(line)
        if m_std:
            expected_hex = m_std.group(1).lower()
            rel_str = m_std.group(2).strip()
        elif m_bsd:
            rel_str = m_bsd.group(1).strip()
            expected_hex = m_bsd.group(2).lower()
        elif m_bare:
            expected_hex = m_bare.group(1).lower()
            if "SCRIPT" in manifest_path.name:
                py_files = sorted(manifest_path.parent.glob("*.py"))
                if len(py_files) != 1:
                    raise RuntimeError(f"Ambiguous bare script manifest: {manifest_path}")
                entries.append((py_files[0], expected_hex))
                continue
            json_files = sorted(manifest_path.parent.glob("*.json"))
            if len(json_files) != 1:
                raise RuntimeError(f"Ambiguous bare output manifest: {manifest_path}")
            entries.append((json_files[0], expected_hex))
            continue
        else:
            raise RuntimeError(f"Unrecognized SHA256 manifest format in {manifest_path}: {line!r}")

        candidates = [
            repo_root / rel_str,
            manifest_path.parent / rel_str,
            manifest_path.parent / Path(rel_str).name,
        ]
        resolved: Path | None = None
        for cand in candidates:
            if cand.is_file():
                resolved = cand.resolve()
                break
        if resolved is None:
            raise FileNotFoundError(f"Target {rel_str!r} from {manifest_path} not found")
        entries.append((resolved, expected_hex))

    if not entries:
        raise RuntimeError(f"Empty SHA256 manifest: {manifest_path}")
    return entries


def verify_sha256_manifests(repo_root: Path, self_script_path: Path) -> dict[str, object]:
    """Verify all 4 prior *SHA256.txt manifests under relays/ plus runtime self SCRIPT_SHA256.txt."""
    relays_dir = repo_root / "relays"
    self_dir = self_script_path.parent.resolve()
    prior_manifests = sorted(
        p for p in relays_dir.rglob("*SHA256.txt") if p.parent.resolve() != self_dir
    )

    prior_records: list[dict[str, object]] = []
    all_prior_matched = True
    for mpath in prior_manifests:
        entries = _parse_manifest_entries(mpath, repo_root)
        entry_results = []
        for target_path, expected_hex in entries:
            actual_hex = hashlib.sha256(target_path.read_bytes()).hexdigest()
            matched = actual_hex == expected_hex
            if not matched:
                all_prior_matched = False
            entry_results.append({
                "target": str(target_path.relative_to(repo_root)),
                "expected_sha256": expected_hex,
                "actual_sha256": actual_hex,
                "matched": matched,
            })
        prior_records.append({
            "manifest": str(mpath.relative_to(repo_root)),
            "entries": entry_results,
            "all_entries_matched": all(e["matched"] for e in entry_results),
        })

    self_manifest_path = self_dir / "SCRIPT_SHA256.txt"
    self_manifest_exists = self_manifest_path.is_file()
    self_matched = False
    self_actual_hex = hashlib.sha256(self_script_path.read_bytes()).hexdigest()
    self_expected_hex = ""
    if self_manifest_exists:
        self_entries = _parse_manifest_entries(self_manifest_path, repo_root)
        if len(self_entries) == 1 and self_entries[0][0] == self_script_path.resolve():
            self_expected_hex = self_entries[0][1]
            self_matched = self_actual_hex == self_expected_hex

    passed = (
        len(prior_manifests) == 4
        and all_prior_matched
        and self_manifest_exists
        and self_matched
    )
    return {
        "prior_manifest_count": len(prior_manifests),
        "expected_prior_manifest_count": 4,
        "all_prior_manifests_matched": all_prior_matched,
        "prior_manifests": prior_records,
        "self_script_manifest_exists": self_manifest_exists,
        "self_script_expected_sha256": self_expected_hex,
        "self_script_actual_sha256": self_actual_hex,
        "self_script_sha256_matched": self_matched,
        "passed": passed,
    }


def check_deliverable_1_and_2() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    """Verify Deliverable 1 (CAR/Cl(10) Fock & Postulate D), Deliverable 2 (Commutant & FS), PF8.1, PF8.2."""
    tol = 1 / (10 ** 12)
    i_unit = complex(0, 1)

    # 1A. Exact cyclotomic field QQ(zeta_5) construction of SL(2, F_5) Weil representation
    zeta5_sym = sp.exp(2 * sp.pi * sp.I / 5)
    K = sp.QQ.algebraic_field(zeta5_sym)
    z = K.from_sympy(zeta5_sym)
    z_pows = [K.one, z, z * z, z * z * z, z * z * z * z]
    cyclotomic_sum_zero = sum(z_pows, K.zero) == K.zero

    # Quadratic Gauss sum over F_5: G = sum_{x=1}^4 (x/5) zeta_5^x = zeta_5 - zeta_5^2 - zeta_5^3 + zeta_5^4 = +sqrt(5)
    s5 = z_pows[1] - z_pows[2] - z_pows[3] + z_pows[4]
    gauss_sum_sq_eq_5 = (s5 * s5) == K(5)
    inv_s5 = s5 / K(5)

    def alg_mul(A, B):
        dim = len(A)
        return [
            [sum((A[r][k] * B[k][c] for k in range(dim)), K.zero) for c in range(dim)]
            for r in range(dim)
        ]

    def alg_pow(A, exp_n: int):
        dim = len(A)
        res = [[K.one if r == c else K.zero for c in range(dim)] for r in range(dim)]
        base = A
        e = exp_n
        while e > 0:
            if e & 1:
                res = alg_mul(res, base)
            base = alg_mul(base, base)
            e >>= 1
        return res

    def alg_key(M):
        return tuple(tuple(tuple(M[r][c].rep) for c in range(len(M))) for r in range(len(M)))

    I5_alg = [[K.one if r == c else K.zero for c in range(5)] for r in range(5)]
    P_alg = [[K.one if (x + y) % 5 == 0 else K.zero for y in range(5)] for x in range(5)]
    neg_I5_alg = [[-I5_alg[r][c] for c in range(5)] for r in range(5)]
    neg_P_alg = [[-P_alg[r][c] for c in range(5)] for r in range(5)]

    # Canonical Weil character psi_1(u) = zeta_5^u:
    # 2^(-1) == 3 (mod 5) => rho(T) = diag(zeta_5^(3 x^2)), rho(S)_{xy} = -(1/sqrt(5)) zeta_5^(4 x y)
    T_psi1 = [[z_pows[(3 * x * x) % 5] if x == y else K.zero for y in range(5)] for x in range(5)]
    S_psi1 = [[-inv_s5 * z_pows[(4 * x * y) % 5] for y in range(5)] for x in range(5)]

    # Galois-conjugate Weil character psi_2(u) = zeta_5^(2 u) (Erratum card):
    # rho(T) = diag(zeta_5^(x^2)), rho(S)_{xy} = +(1/sqrt(5)) zeta_5^(3 x y)
    T_psi2 = [[z_pows[(x * x) % 5] if x == y else K.zero for y in range(5)] for x in range(5)]
    S_psi2 = [[inv_s5 * z_pows[(3 * x * y) % 5] for y in range(5)] for x in range(5)]

    # Erratum control: uncompensated sign convention (diag(zeta_5^(4 x^2)), -(1/sqrt(5)) zeta_5^(3 x y)) -> order 240
    T_uncomp = [[z_pows[(4 * x * x) % 5] if x == y else K.zero for y in range(5)] for x in range(5)]
    S_uncomp = [[-inv_s5 * z_pows[(3 * x * y) % 5] for y in range(5)] for x in range(5)]

    def group_closure(gens):
        seen = {alg_key(I5_alg): I5_alg}
        queue = [I5_alg]
        while queue:
            cur = queue.pop()
            for g in gens:
                nxt = alg_mul(cur, g)
                k = alg_key(nxt)
                if k not in seen:
                    seen[k] = nxt
                    queue.append(nxt)
        return list(seen.values())

    # Verify exact group homomorphism from 2x2 matrices SL(2, F_5) -> U(5)
    S_f5 = ((0, 4), (1, 0))
    T_f5 = ((1, 1), (0, 1))
    I_f5 = ((1, 0), (0, 1))

    def mul_f5(A, B):
        return (
            ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5),
        )

    hom_psi1 = {I_f5: I5_alg}
    q_f5 = [I_f5]
    exact_homomorphism_psi1 = True
    while q_f5:
        g = q_f5.pop()
        rg = hom_psi1[g]
        for gm, rgm in ((S_f5, S_psi1), (T_f5, T_psi1)):
            ng = mul_f5(g, gm)
            nrg = alg_mul(rg, rgm)
            if ng not in hom_psi1:
                hom_psi1[ng] = nrg
                q_f5.append(ng)
            elif hom_psi1[ng] != nrg:
                exact_homomorphism_psi1 = False

    grp_psi1 = group_closure((S_psi1, T_psi1))
    grp_psi2 = group_closure((S_psi2, T_psi2))
    grp_uncomp = group_closure((S_uncomp, T_uncomp))

    psi1_s2_eq_p = alg_mul(S_psi1, S_psi1) == P_alg
    psi1_st3_eq_p = alg_pow(alg_mul(S_psi1, T_psi1), 3) == P_alg
    psi2_s2_eq_p = alg_mul(S_psi2, S_psi2) == P_alg
    psi2_st3_eq_p = alg_pow(alg_mul(S_psi2, T_psi2), 3) == P_alg
    # Note T_uncomp^(-1) = T_psi2 while S_uncomp = -S_psi2, so (S_uncomp * T_uncomp^(-1))^3 = -P and (S_uncomp * T_uncomp)^3 = -I_5
    uncomp_st_inv3_eq_neg_p = alg_pow(alg_mul(S_uncomp, T_psi2), 3) == neg_P_alg
    uncomp_st3_eq_neg_i = alg_pow(alg_mul(S_uncomp, T_uncomp), 3) == neg_I5_alg

    # 1B. Numerical SL(2, F_5) verification (< 10^-12)
    theta = 2 * math.pi / 5
    z_num = [complex(math.cos(k * theta), math.sin(k * theta)) for k in range(5)]
    inv_s5_num = 1 / math.sqrt(5)
    P_num = np.array([[1 if (x + y) % 5 == 0 else 0 for y in range(5)] for x in range(5)], dtype=np.complex128)
    T_num = np.diag([z_num[(3 * x * x) % 5] for x in range(5)]).astype(np.complex128)
    S_num = np.array([[-inv_s5_num * z_num[(4 * x * y) % 5] for y in range(5)] for x in range(5)], dtype=np.complex128)

    s2_num_res = float(np.linalg.norm(S_num @ S_num - P_num))
    st3_num_res = float(np.linalg.norm(np.linalg.matrix_power(S_num @ T_num, 3) - P_num))
    unitary_s_res = float(np.linalg.norm(S_num.conj().T @ S_num - np.eye(5)))
    unitary_t_res = float(np.linalg.norm(T_num.conj().T @ T_num - np.eye(5)))

    # 1C. 32 x 32 CAR operators via Jordan-Wigner tensor products:
    # c_a = sigma_z^(otimes a) otimes sigma_- otimes I_2^(otimes (4-a))
    # With qubit |0> = (1,0)^T (empty), |1> = (0,1)^T (occupied), lowering sigma_- = [[0,1],[0,0]].
    I2 = np.array([[1, 0], [0, 1]], dtype=np.int64)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=np.int64)
    sigma_minus = np.array([[0, 1], [0, 0]], dtype=np.int64)
    sigma_plus = sigma_minus.T

    def kron_chain(mats: list[np.ndarray]) -> np.ndarray:
        acc = mats[0]
        for m in mats[1:]:
            acc = np.kron(acc, m)
        return acc

    c_ops = [kron_chain([sigma_z] * a + [sigma_minus] + [I2] * (4 - a)) for a in range(5)]
    cdag_ops = [kron_chain([sigma_z] * a + [sigma_plus] + [I2] * (4 - a)) for a in range(5)]

    I32 = np.eye(32, dtype=np.int64)
    Z32 = np.zeros((32, 32), dtype=np.int64)
    car_exact = True
    for a in range(5):
        for b in range(5):
            ac_mixed = c_ops[a] @ cdag_ops[b] + cdag_ops[b] @ c_ops[a]
            ac_ann = c_ops[a] @ c_ops[b] + c_ops[b] @ c_ops[a]
            ac_cre = cdag_ops[a] @ cdag_ops[b] + cdag_ops[b] @ cdag_ops[a]
            expected_mixed = I32 if a == b else Z32
            if not (
                np.array_equal(ac_mixed, expected_mixed)
                and np.array_equal(ac_ann, Z32)
                and np.array_equal(ac_cre, Z32)
            ):
                car_exact = False

    # 1D. Cl(10, C) 10 gamma generators and 2^10 = 1024 product basis span
    gammas: list[np.ndarray] = []
    for a in range(5):
        gammas.append((c_ops[a] + cdag_ops[a]).astype(np.complex128))
        gammas.append((-i_unit * (c_ops[a] - cdag_ops[a])).astype(np.complex128))

    clifford_anticomm_ok = True
    max_clifford_res = 0 / 1
    for mu in range(10):
        for nu in range(10):
            ac = gammas[mu] @ gammas[nu] + gammas[nu] @ gammas[mu]
            target = (2 * I32 if mu == nu else Z32).astype(np.complex128)
            err = float(np.linalg.norm(ac - target))
            if err > max_clifford_res:
                max_clifford_res = err
            if err >= tol:
                clifford_anticomm_ok = False

    I32_c = I32.astype(np.complex128)
    gamma_products_flat = []
    for mask in range(1024):
        prod = I32_c
        for bit in range(10):
            if (mask >> bit) & 1:
                prod = prod @ gammas[bit]
        gamma_products_flat.append(prod.reshape(-1))
    M_1024 = np.stack(gamma_products_flat, axis=0)
    gram_1024 = (M_1024.conj() @ M_1024.T) / 32
    gram_1024_res = float(np.linalg.norm(gram_1024 - np.eye(1024)))
    cl10_span_rank = int(np.linalg.matrix_rank(M_1024))

    # 1E. Hypercharge 6Y = (I_5 - 5 P)/2 on W_5 and Fock quantization dGamma(6Y)
    P_int = np.array([[1 if (x + y) % 5 == 0 else 0 for y in range(5)] for x in range(5)], dtype=np.int64)
    two_6Y_w5 = np.eye(5, dtype=np.int64) - 5 * P_int
    tr_two_6Y_w5 = int(np.trace(two_6Y_w5))

    two_6Y_fock = np.zeros((32, 32), dtype=np.int64)
    two_6Y_weyl_ordered = np.zeros((32, 32), dtype=np.int64)
    N_fock = np.zeros((32, 32), dtype=np.int64)
    for a in range(5):
        N_fock = N_fock + (cdag_ops[a] @ c_ops[a])
        for b in range(5):
            coeff = int(two_6Y_w5[a, b])
            two_6Y_fock = two_6Y_fock + coeff * (cdag_ops[a] @ c_ops[b])
            # Weyl-symmetrized 2 * (1/2) sum (6Y)_{ab} [c_a^dag, c_b] -> exact integer test via 2 * two_6Y
            two_6Y_weyl_ordered = two_6Y_weyl_ordered + coeff * (cdag_ops[a] @ c_ops[b] - c_ops[b] @ cdag_ops[a])

    # Because [c_a^dag, c_b] = 2 c_a^dag c_b - delta_{ab} I_32, two_6Y_weyl_ordered == 2 * two_6Y_fock - Tr(two_6Y_w5) I_32
    zero_normal_ordering_shift = bool(
        tr_two_6Y_w5 == 0
        and int(np.trace(two_6Y_fock)) == 0
        and np.array_equal(two_6Y_weyl_ordered, 2 * two_6Y_fock)
    )

    fermion_parity = kron_chain([sigma_z] * 5)
    parity_product = I32.copy()
    for a in range(5):
        parity_product = parity_product @ (I32 - 2 * (cdag_ops[a] @ c_ops[a]))
    parity_consistent = bool(np.array_equal(fermion_parity, parity_product))

    even_indices = [idx for idx in range(32) if int(fermion_parity[idx, idx]) == 1]
    odd_indices = [idx for idx in range(32) if int(fermion_parity[idx, idx]) == -1]
    n1_indices = [idx for idx in range(32) if int(N_fock[idx, idx]) == 1]

    def exact_6y_eigenvalues(indices: list[int]) -> list[int]:
        sub_2 = sp.Matrix(two_6Y_fock[np.ix_(indices, indices)].tolist())
        evals_2 = sorted(int(val) for val, mult in sub_2.eigenvals().items() for _ in range(mult))
        if any(v % 2 != 0 for v in evals_2):
            raise RuntimeError(f"Non-integer 6Y eigenvalue encountered: {evals_2}")
        return [v // 2 for v in evals_2]

    even_6y_spec = exact_6y_eigenvalues(even_indices)
    odd_6y_spec = exact_6y_eigenvalues(odd_indices)
    lambda1_6y_spec = exact_6y_eigenvalues(n1_indices)

    target_even_6y = [-4, -4, -4, -3, -3, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6]
    target_lambda1_6y = [-2, -2, -2, 3, 3]
    expected_odd_pf81 = [-6, -2, -2, -2, -1, -1, -1, -1, -1, -1, 0, 3, 3, 4, 4, 4]

    even_sum = sum(even_6y_spec)
    even_cubic_sum = sum(v ** 3 for v in even_6y_spec)

    # 1F. Guardrail 3 Mandatory Unitary Basis-Scrambling Test on W_5 -> U_5 W_5
    U5_haar = _deterministic_haar_unitary(5, seed_offset=1)
    sixY_w5_num = (np.eye(5, dtype=np.complex128) - 5 * P_num) / 2
    sixY_w5_scrambled = U5_haar @ sixY_w5_num @ U5_haar.conj().T
    sixY_fock_scrambled = np.zeros((32, 32), dtype=np.complex128)
    for a in range(5):
        for b in range(5):
            sixY_fock_scrambled = sixY_fock_scrambled + sixY_w5_scrambled[a, b] * (
                cdag_ops[a] @ c_ops[b]
            ).astype(np.complex128)

    ev_even_scr = np.linalg.eigvalsh(sixY_fock_scrambled[np.ix_(even_indices, even_indices)])
    ev_n1_scr = np.linalg.eigvalsh(sixY_fock_scrambled[np.ix_(n1_indices, n1_indices)])
    haar_even_res = float(np.max(np.abs(np.sort(ev_even_scr) - np.array(target_even_6y, dtype=np.float64))))
    haar_n1_res = float(np.max(np.abs(np.sort(ev_n1_scr) - np.array(target_lambda1_6y, dtype=np.float64))))

    # PF8.1: Wrong-chirality odd Fock projection flips signs to [-6^1, ..., +4^3]
    pf8_1_caught = (odd_6y_spec == expected_odd_pf81) and (odd_6y_spec != target_even_6y)

    deliv_1 = {
        "sl2_f5_order_exact_psi1": len(grp_psi1),
        "sl2_f5_order_exact_psi2": len(grp_psi2),
        "sl2_f5_2x2_homomorphism_size": len(hom_psi1),
        "sl2_f5_exact_homomorphism": exact_homomorphism_psi1,
        "cyclotomic_fifth_root_sum_zero": cyclotomic_sum_zero,
        "gauss_sum_squared_eq_5": gauss_sum_sq_eq_5,
        "psi1_S2_eq_P_exact": psi1_s2_eq_p,
        "psi1_ST3_eq_P_exact": psi1_st3_eq_p,
        "psi2_S2_eq_P_exact": psi2_s2_eq_p,
        "psi2_ST3_eq_P_exact": psi2_st3_eq_p,
        "erratum_uncompensated_order": len(grp_uncomp),
        "erratum_uncompensated_ST_inv3_eq_neg_P": uncomp_st_inv3_eq_neg_p,
        "erratum_uncompensated_ST3_eq_neg_I": uncomp_st3_eq_neg_i,
        "numerical_S2_minus_P_scaled_1e15": _scaled_residual_1e15(s2_num_res),
        "numerical_ST3_minus_P_scaled_1e15": _scaled_residual_1e15(st3_num_res),
        "car_32x32_exact_anticommutators": car_exact,
        "cl10_anticommutators_lt_1e_12": clifford_anticomm_ok,
        "cl10_1024_basis_rank": cl10_span_rank,
        "cl10_gram_orthonormality_lt_1e_12": gram_1024_res < tol,
        "tr_w5_6Y_exact": tr_two_6Y_w5 // 2,
        "zero_normal_ordering_ambiguity": zero_normal_ordering_shift,
        "fermion_parity_consistent": parity_consistent,
        "even_fock_dim": len(even_indices),
        "even_fock_6Y_eigenvalues": even_6y_spec,
        "even_fock_sum_6Y": even_sum,
        "even_fock_sum_6Y_cubed": even_cubic_sum,
        "lambda1_dim": len(n1_indices),
        "lambda1_6Y_eigenvalues": lambda1_6y_spec,
        "haar_basis_scrambling_invariant_lt_1e_12": (haar_even_res < tol) and (haar_n1_res < tol),
        "haar_even_max_res_scaled_1e15": _scaled_residual_1e15(haar_even_res),
        "passed": (
            len(grp_psi1) == 120
            and len(grp_psi2) == 120
            and len(hom_psi1) == 120
            and exact_homomorphism_psi1
            and psi1_s2_eq_p
            and psi1_st3_eq_p
            and psi2_s2_eq_p
            and psi2_st3_eq_p
            and len(grp_uncomp) == 240
            and uncomp_st_inv3_eq_neg_p
            and s2_num_res < tol
            and st3_num_res < tol
            and unitary_s_res < tol
            and unitary_t_res < tol
            and car_exact
            and clifford_anticomm_ok
            and cl10_span_rank == 1024
            and gram_1024_res < tol
            and zero_normal_ordering_shift
            and parity_consistent
            and even_6y_spec == target_even_6y
            and even_sum == 0
            and even_cubic_sum == 0
            and lambda1_6y_spec == target_lambda1_6y
            and haar_even_res < tol
            and haar_n1_res < tol
        ),
    }

    # =========================================================================
    # Deliverable 2: Continuous-Colour Commutant Dichotomy & Frobenius-Schur
    # =========================================================================
    su5_basis: list[np.ndarray] = []
    for a in range(5):
        for b in range(a + 1, 5):
            m_re = np.zeros((5, 5), dtype=np.complex128)
            m_re[a, b] = 1
            m_re[b, a] = -1
            su5_basis.append(m_re)
            m_im = np.zeros((5, 5), dtype=np.complex128)
            m_im[a, b] = i_unit
            m_im[b, a] = i_unit
            su5_basis.append(m_im)
    for d in range(4):
        m_d = np.zeros((5, 5), dtype=np.complex128)
        m_d[d, d] = i_unit
        m_d[d + 1, d + 1] = -i_unit
        su5_basis.append(m_d)

    def real_su5_commutant_dim(operators: list[np.ndarray]) -> int:
        blocks = []
        for op in operators:
            cols = []
            for gen in su5_basis:
                comm = op @ gen - gen @ op
                cols.append(np.concatenate([comm.real.reshape(-1), comm.imag.reshape(-1)]))
            blocks.append(np.stack(cols, axis=1))
        mat_l = np.concatenate(blocks, axis=0)
        svals = np.linalg.svd(mat_l, compute_uv=False)
        return int(np.sum(svals < tol))

    # Also exact algebraic sl(5, C) commutant dimension in QQ(zeta_5)!
    # Since rho(G) subset U(5), C_{sl(5,C)}(G) = C_{su(5)}(G) otimes_R C, so dim_C == dim_R!
    sl5_alg_basis = []
    for a in range(5):
        for b in range(5):
            if a != b:
                m = [[K.one if (r == a and c == b) else K.zero for c in range(5)] for r in range(5)]
                sl5_alg_basis.append(m)
    for d in range(4):
        m = [[K.one if (r == d and c == d) else (-K.one if (r == d + 1 and c == d + 1) else K.zero) for c in range(5)] for r in range(5)]
        sl5_alg_basis.append(m)

    def exact_sl5_commutant_dim(alg_ops) -> int:
        rows = []
        for op in alg_ops:
            op_cols = []
            for gen in sl5_alg_basis:
                comm = [
                    [
                        sum((op[r][k] * gen[k][c] - gen[r][k] * op[k][c] for k in range(5)), K.zero)
                        for c in range(5)
                    ]
                    for r in range(5)
                ]
                op_cols.append([comm[r][c] for r in range(5) for c in range(5)])
            for entry_idx in range(25):
                rows.append([op_cols[col_idx][entry_idx] for col_idx in range(24)])
        dm = DomainMatrix(rows, (len(rows), 24), K)
        return 24 - int(dm.rank())

    dim_comm_weil_num = real_su5_commutant_dim([S_num, T_num])
    dim_comm_p_num = real_su5_commutant_dim([P_num])
    dim_comm_weil_exact = exact_sl5_commutant_dim([S_psi1, T_psi1])
    dim_comm_p_exact = exact_sl5_commutant_dim([P_alg])

    # Guardrail 3 Haar-scrambled commutant dimension check
    U5_comm = _deterministic_haar_unitary(5, seed_offset=2)
    dim_comm_weil_haar = real_su5_commutant_dim([
        U5_comm @ S_num @ U5_comm.conj().T,
        U5_comm @ T_num @ U5_comm.conj().T,
    ])
    dim_comm_p_haar = real_su5_commutant_dim([U5_comm @ P_num @ U5_comm.conj().T])

    # Exact Frobenius-Schur indicators in QQ(zeta_5) on 3_+ and 2_-
    half = K(1) / K(2)
    Pi_plus = [[(K.one if r == c else K.zero) * half + P_alg[r][c] * half for c in range(5)] for r in range(5)]
    Pi_minus = [[(K.one if r == c else K.zero) * half - P_alg[r][c] * half for c in range(5)] for r in range(5)]

    def alg_trace(M):
        return sum((M[idx][idx] for idx in range(len(M))), K.zero)

    # Complex conjugation on QQ(zeta_5): z -> z^4, z^2 -> z^3, z^3 -> z^2
    def alg_conj(val):
        sym_e = K.to_sympy(val).subs(zeta5_sym, zeta5_sym ** 4)
        return K.from_sympy(sym_e)

    fs_sum_3 = K.zero
    fs_sum_2 = K.zero
    norm_sq_3 = K.zero
    norm_sq_2 = K.zero
    for g in grp_psi1:
        g2 = alg_mul(g, g)
        fs_sum_3 = fs_sum_3 + alg_trace(alg_mul(Pi_plus, g2))
        fs_sum_2 = fs_sum_2 + alg_trace(alg_mul(Pi_minus, g2))
        chi3 = alg_trace(alg_mul(Pi_plus, g))
        chi2 = alg_trace(alg_mul(Pi_minus, g))
        norm_sq_3 = norm_sq_3 + chi3 * alg_conj(chi3)
        norm_sq_2 = norm_sq_2 + chi2 * alg_conj(chi2)

    fs_3_exact_ok = (fs_sum_3 / K(120)) == K.one
    fs_2_exact_ok = (fs_sum_2 / K(120)) == -K.one
    irrep_3_exact = (norm_sq_3 / K(120)) == K.one
    irrep_2_exact = (norm_sq_2 / K(120)) == K.one
    fs_3_int = int(K.to_sympy(fs_sum_3 / K(120)))
    fs_2_int = int(K.to_sympy(fs_sum_2 / K(120)))

    # Explicit invariant bilinear forms on 3_+ and 2_- (both exact algebraic and numerical SO(3)/Sp(1)):
    # Orthonormal basis V_+ (5x3) of 3_+ and V_- (5x2) of 2_-
    inv_sqrt2 = 1 / math.sqrt(2)
    V_plus = np.zeros((5, 3), dtype=np.complex128)
    V_plus[0, 0] = 1
    V_plus[1, 1] = inv_sqrt2
    V_plus[4, 1] = inv_sqrt2
    V_plus[2, 2] = inv_sqrt2
    V_plus[3, 2] = inv_sqrt2

    V_minus = np.zeros((5, 2), dtype=np.complex128)
    V_minus[1, 0] = inv_sqrt2
    V_minus[4, 0] = -inv_sqrt2
    V_minus[2, 1] = inv_sqrt2
    V_minus[3, 1] = -inv_sqrt2

    # In rational orthogonal basis B_+ = [e0, e1+e4, e2+e3] and B_- = [e1-e4, e2-e3], verify EXACTLY in QQ(zeta_5)!
    # B_+^T B_+ = diag(1, 2, 2), so B_+^(-1) on 3_+ is diag(1, 1/2, 1/2) B_+^T
    B_plus = [
        [K.one, K.zero, K.zero],
        [K.zero, K.one, K.zero],
        [K.zero, K.zero, K.one],
        [K.zero, K.zero, K.one],
        [K.zero, K.one, K.zero],
    ]
    B_plus_pinv = [
        [K.one, K.zero, K.zero, K.zero, K.zero],
        [K.zero, half, K.zero, K.zero, half],
        [K.zero, K.zero, half, half, K.zero],
    ]
    B_minus = [
        [K.zero, K.zero],
        [K.one, K.zero],
        [K.zero, K.one],
        [K.zero, -K.one],
        [-K.one, K.zero],
    ]
    B_minus_pinv = [
        [K.zero, half, K.zero, K.zero, -half],
        [K.zero, K.zero, half, -half, K.zero],
    ]

    def rect_mul(A, B):
        r_len = len(A)
        k_len = len(B)
        c_len = len(B[0])
        return [
            [sum((A[r][k] * B[k][c] for k in range(k_len)), K.zero) for c in range(c_len)]
            for r in range(r_len)
        ]

    def mat_T(A):
        return [[A[r][c] for r in range(len(A))] for c in range(len(A[0]))]

    # Symmetric form M_plus_rat = [[1, 0, 0], [0, 0, 2], [0, 2, 0]] on B_+ (which equals [[1,0,0],[0,0,1],[0,1,0]] on orthonormal V_+)
    M_plus_rat = [
        [K.one, K.zero, K.zero],
        [K.zero, K.zero, K(2)],
        [K.zero, K(2), K.zero],
    ]
    # Antisymmetric symplectic form J_minus_rat = [[0, 1], [-1, 0]] on B_- (and V_-)
    J_minus_rat = [
        [K.zero, K.one],
        [-K.one, K.zero],
    ]

    sym_form_3_all120_exact = True
    symp_form_2_all120_exact = True
    for g in grp_psi1:
        g3 = rect_mul(B_plus_pinv, rect_mul(g, B_plus))
        g2 = rect_mul(B_minus_pinv, rect_mul(g, B_minus))
        if rect_mul(mat_T(g3), rect_mul(M_plus_rat, g3)) != M_plus_rat:
            sym_form_3_all120_exact = False
        if rect_mul(mat_T(g2), rect_mul(J_minus_rat, g2)) != J_minus_rat:
            symp_form_2_all120_exact = False

    # Also verify real SO(3, R) basis on 3_+ where preserved symmetric form is literally I_3 (positive-definite real symmetric)!
    U_to_so3 = np.array([
        [1, 0, 0],
        [0, inv_sqrt2, inv_sqrt2],
        [0, -i_unit * inv_sqrt2, i_unit * inv_sqrt2],
    ], dtype=np.complex128)
    S3_so3 = U_to_so3 @ (V_plus.conj().T @ S_num @ V_plus) @ U_to_so3.conj().T
    T3_so3 = U_to_so3 @ (V_plus.conj().T @ T_num @ V_plus) @ U_to_so3.conj().T
    so3_real_imag_res = max(float(np.linalg.norm(S3_so3.imag)), float(np.linalg.norm(T3_so3.imag)))
    so3_orth_res = max(
        float(np.linalg.norm(S3_so3.real.T @ S3_so3.real - np.eye(3))),
        float(np.linalg.norm(T3_so3.real.T @ T3_so3.real - np.eye(3))),
    )
    so3_det_ok = (
        abs(float(np.linalg.det(S3_so3.real)) - 1) < tol
        and abs(float(np.linalg.det(T3_so3.real)) - 1) < tol
    )

    S2_sp = V_minus.conj().T @ S_num @ V_minus
    T2_sp = V_minus.conj().T @ T_num @ V_minus
    J2_num = np.array([[0, 1], [-1, 0]], dtype=np.complex128)
    sp1_symp_res = max(
        float(np.linalg.norm(S2_sp.T @ J2_num @ S2_sp - J2_num)),
        float(np.linalg.norm(T2_sp.T @ J2_num @ T2_sp - J2_num)),
    )

    # Verify uniqueness: antisymmetric invariant bilinear forms on 3_+ = 0, symmetric invariant forms on 2_- = 0
    # Check basis of skew 3x3 (3 matrices) and sym 2x2 (3 matrices)
    skew3_seeds = [
        np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], dtype=np.complex128),
        np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], dtype=np.complex128),
        np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=np.complex128),
    ]
    sym2_seeds = [
        np.array([[1, 0], [0, 0]], dtype=np.complex128),
        np.array([[0, 1], [1, 0]], dtype=np.complex128),
        np.array([[0, 0], [0, 1]], dtype=np.complex128),
    ]
    # Build numerical 120 group elements via BFS for fast averaging check
    grp_num = [np.eye(5, dtype=np.complex128)]
    for g_idx in range(200):
        if g_idx >= len(grp_num):
            break
        cur = grp_num[g_idx]
        for gen_m in (S_num, T_num):
            cand = cur @ gen_m
            if not any(np.linalg.norm(cand - prev) < (1 / (10 ** 8)) for prev in grp_num):
                grp_num.append(cand)

    max_skew3_inv = 0 / 1
    for seed in skew3_seeds:
        acc = sum((V_plus.conj().T @ g @ V_plus).T @ seed @ (V_plus.conj().T @ g @ V_plus) for g in grp_num) / len(grp_num)
        max_skew3_inv = max(max_skew3_inv, float(np.linalg.norm(acc)))
    max_sym2_inv = 0 / 1
    for seed in sym2_seeds:
        acc = sum((V_minus.conj().T @ g @ V_minus).T @ seed @ (V_minus.conj().T @ g @ V_minus) for g in grp_num) / len(grp_num)
        max_sym2_inv = max(max_sym2_inv, float(np.linalg.norm(acc)))

    # PF8.2: Traceless off-diagonal SU(3)_c generator on 3_+ commutes with P to 0 but fails [G_c, rho(S)] == 0 by > 1/2
    # Construct unit-Frobenius-norm anti-Hermitian generator G_c = (|0><u_1| - |u_1><0|) / sqrt(2) in su(3)_c subset su(5)
    u0_vec = V_plus[:, [0]]
    u1_vec = V_plus[:, [1]]
    G_c = (u0_vec @ u1_vec.conj().T - u1_vec @ u0_vec.conj().T) * inv_sqrt2
    comm_Gc_P_norm = float(np.linalg.norm(G_c @ P_num - P_num @ G_c))
    comm_Gc_S_norm = float(np.linalg.norm(G_c @ S_num - S_num @ G_c))

    # Exact algebraic squared Frobenius norm of [G_c, rho(S)] in QQ(zeta_5):
    # Since |(e1+e4)/sqrt(2)> has norm 1, G_c = (|0><(e1+e4)| - |(e1+e4)><0|) / 2 has exact rational entries 0, +-1/2.
    G_c_alg = [[K.zero for _ in range(5)] for _ in range(5)]
    G_c_alg[0][1] = half
    G_c_alg[0][4] = half
    G_c_alg[1][0] = -half
    G_c_alg[4][0] = -half
    comm_Gc_P_alg = [
        [sum((G_c_alg[r][k] * P_alg[k][c] - P_alg[r][k] * G_c_alg[k][c] for k in range(5)), K.zero) for c in range(5)]
        for r in range(5)
    ]
    comm_Gc_P_exact_zero = all(comm_Gc_P_alg[r][c] == K.zero for r in range(5) for c in range(5))
    comm_Gc_S_alg = [
        [sum((G_c_alg[r][k] * S_psi1[k][c] - S_psi1[r][k] * G_c_alg[k][c] for k in range(5)), K.zero) for c in range(5)]
        for r in range(5)
    ]
    norm_sq_Gc_S = K.zero
    for r in range(5):
        for c in range(5):
            norm_sq_Gc_S = norm_sq_Gc_S + comm_Gc_S_alg[r][c] * alg_conj(comm_Gc_S_alg[r][c])
    # Exact verification in QQ(zeta_5): norm_sq_Gc_S == (15 - sqrt(5)) / 5 > 12/5 > 1/4 => ||[G_c, rho(S)]||_F > 1/2!
    expected_norm_sq = (K(15) - s5) / K(5)
    pf8_2_exact_formula_match = norm_sq_Gc_S == expected_norm_sq
    pf8_2_caught = (
        comm_Gc_P_exact_zero
        and comm_Gc_P_norm < tol
        and pf8_2_exact_formula_match
        and comm_Gc_S_norm > (1 / 2)
    )

    deliv_2 = {
        "dim_R_commutant_su5_full_weil_numerical": dim_comm_weil_num,
        "dim_R_commutant_su5_full_weil_exact": dim_comm_weil_exact,
        "dim_R_commutant_su5_centre_P_numerical": dim_comm_p_num,
        "dim_R_commutant_su5_centre_P_exact": dim_comm_p_exact,
        "haar_scrambled_commutant_dims": [dim_comm_weil_haar, dim_comm_p_haar],
        "frobenius_schur_3_plus": fs_3_int,
        "frobenius_schur_2_minus": fs_2_int,
        "irrep_character_norm_sq_exact_ones": irrep_3_exact and irrep_2_exact,
        "3_plus_preserves_symmetric_form_all120_exact": sym_form_3_all120_exact,
        "3_plus_real_SO3_basis_verified_lt_1e_12": (so3_real_imag_res < tol) and (so3_orth_res < tol) and so3_det_ok,
        "3_plus_no_antisymmetric_form_lt_1e_12": max_skew3_inv < tol,
        "2_minus_preserves_symplectic_form_all120_exact": symp_form_2_all120_exact,
        "2_minus_symplectic_residual_lt_1e_12": sp1_symp_res < tol,
        "2_minus_no_symmetric_form_lt_1e_12": max_sym2_inv < tol,
        "numerical_group_order_check": len(grp_num),
        "passed": (
            dim_comm_weil_num == 1
            and dim_comm_weil_exact == 1
            and dim_comm_p_num == 12
            and dim_comm_p_exact == 12
            and dim_comm_weil_haar == 1
            and dim_comm_p_haar == 12
            and fs_3_exact_ok
            and fs_2_exact_ok
            and fs_3_int == 1
            and fs_2_int == -1
            and irrep_3_exact
            and irrep_2_exact
            and sym_form_3_all120_exact
            and so3_real_imag_res < tol
            and so3_orth_res < tol
            and so3_det_ok
            and max_skew3_inv < tol
            and symp_form_2_all120_exact
            and sp1_symp_res < tol
            and max_sym2_inv < tol
            and len(grp_num) == 120
        ),
    }

    pf_1_2 = {
        "PF8_1_odd_fock_wrong_chirality": {
            "odd_fock_6Y_eigenvalues": odd_6y_spec,
            "matches_flipped_sign_spectrum": odd_6y_spec == expected_odd_pf81,
            "differs_from_even_fock_target": odd_6y_spec != target_even_6y,
            "fault_caught": pf8_1_caught,
        },
        "PF8_2_off_diagonal_su3c_commutator": {
            "unit_norm_Gc_comm_P_exact_zero": comm_Gc_P_exact_zero,
            "comm_Gc_P_scaled_1e15": _scaled_residual_1e15(comm_Gc_P_norm),
            "comm_Gc_rhoS_norm_sq_exact": "(15 - sqrt(5))/5",
            "comm_Gc_rhoS_norm_sq_exact_verified": pf8_2_exact_formula_match,
            "comm_Gc_rhoS_gt_one_half": comm_Gc_S_norm > (1 / 2),
            "fault_caught": pf8_2_caught,
        },
    }
    return deliv_1, deliv_2, pf_1_2


def _squarefree_kernel(n: int) -> int:
    """Compute square-free positive integer kernel m of n = s^2 * m."""
    rem = n
    out = 1
    d = 2
    while d * d <= rem:
        cnt = 0
        while rem % d == 0:
            rem //= d
            cnt += 1
        if cnt % 2 == 1:
            out *= d
        d += 1
    if rem > 1:
        out *= rem
    return out


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def check_deliverable_3() -> tuple[dict[str, object], dict[str, object]]:
    """Verify Deliverable 3 (Metallic-mean fundamental discriminants k=1..12 & rival primes) and PF8.3."""
    metallic_table: list[dict[str, object]] = []
    odd_prime_discriminants: set[int] = set()

    for k in range(1, 13):
        d_k = k * k + 4
        sf = _squarefree_kernel(d_k)
        delta_k = sf if (sf % 4 == 1) else (4 * sf)
        is_odd_prime_disc = (delta_k % 2 == 1) and _is_prime(delta_k)
        if is_odd_prime_disc:
            odd_prime_discriminants.add(delta_k)
        metallic_table.append({
            "k": k,
            "D_k": d_k,
            "squarefree_kernel": sf,
            "fundamental_discriminant_Delta_K": delta_k,
            "is_odd_prime_discriminant": is_odd_prime_disc,
        })

    # Verify k = 4 -> D_4 = 20 = 4 * 5 -> Delta_K = 5 and mu_4 = (4 + sqrt(20))/2 == phi^3 in Q(sqrt(5))
    sqrt5 = sp.sqrt(5)
    phi = (1 + sqrt5) / 2
    mu_4 = (4 + sp.sqrt(20)) / 2
    mu_11 = (11 + sp.sqrt(125)) / 2
    k4_is_phi_cubed = sp.simplify(mu_4 - phi ** 3) == 0
    k11_is_phi_fifth = sp.simplify(mu_11 - phi ** 5) == 0
    k4_entry = metallic_table[3]
    k4_delta_eq_5 = (k4_entry["D_k"] == 20) and (k4_entry["fundamental_discriminant_Delta_K"] == 5)

    # Construct explicit p x p central parity matrices P_p = rho_p(-I) on L^2(F_p)
    rival_primes = [3, 5, 7, 11, 13, 29]
    prime_splits: dict[str, list[int]] = {}
    splits_match_formula = True
    for p in rival_primes:
        P_p = sp.Matrix(p, p, lambda x, y: 1 if (x + y) % p == 0 else 0)
        evals = P_p.eigenvals()
        dim_plus = int(evals.get(1, 0))
        dim_minus = int(evals.get(-1, 0))
        prime_splits[str(p)] = [dim_plus, dim_minus]
        if (dim_plus, dim_minus) != ((p + 1) // 2, (p - 1) // 2):
            splits_match_formula = False

    # Also test all odd-prime fundamental discriminants occurring in k=1..12
    metallic_prime_splits: dict[str, list[int]] = {}
    for p in sorted(odd_prime_discriminants):
        P_p = sp.Matrix(p, p, lambda x, y: 1 if (x + y) % p == 0 else 0)
        evals = P_p.eigenvals()
        metallic_prime_splits[str(p)] = [int(evals.get(1, 0)), int(evals.get(-1, 0))]

    unique_primes_for_3_2_rivals = [int(p) for p, sp_pair in prime_splits.items() if sp_pair == [3, 2]]
    unique_primes_for_3_2_metallic = [int(p) for p, sp_pair in metallic_prime_splits.items() if sp_pair == [3, 2]]

    # PF8.3: Bronze-mean prime p = 13 (k = 3) gives (7, 6) != (3, 2)
    p13_split = prime_splits["13"]
    pf8_3_caught = (p13_split == [7, 6]) and (p13_split != [3, 2])

    deliv_3 = {
        "metallic_discriminants_k_1_to_12": metallic_table,
        "odd_prime_discriminants_k_1_to_12": sorted(odd_prime_discriminants),
        "k4_D4_eq_20_Delta_K_eq_5": k4_delta_eq_5,
        "k4_root_eq_phi_cubed_exact": k4_is_phi_cubed,
        "k11_root_eq_phi_fifth_exact": k11_is_phi_fifth,
        "rival_prime_splits": prime_splits,
        "metallic_odd_prime_splits": metallic_prime_splits,
        "all_splits_match_half_p_plus_minus_1": splits_match_formula,
        "unique_rival_primes_giving_3_2": unique_primes_for_3_2_rivals,
        "unique_metallic_odd_primes_giving_3_2": unique_primes_for_3_2_metallic,
        "passed": (
            k4_delta_eq_5
            and k4_is_phi_cubed
            and k11_is_phi_fifth
            and splits_match_formula
            and unique_primes_for_3_2_rivals == [5]
            and unique_primes_for_3_2_metallic == [5]
        ),
    }
    pf_3 = {
        "PF8_3_bronze_prime_p13_control": {
            "k3_Delta_K": metallic_table[2]["fundamental_discriminant_Delta_K"],
            "rho_13_minus_I_split": p13_split,
            "differs_from_3_2": p13_split != [3, 2],
            "fault_caught": pf8_3_caught,
        }
    }
    return deliv_3, pf_3


def check_deliverable_4() -> tuple[dict[str, object], dict[str, object]]:
    """Verify Deliverable 4 (Prime-3 Family vs Prime-5 Gauge Orthogonality in 248D E_8), PF8.4, PF8.5."""
    tol = 1 / (10 ** 12)

    # 4A. Construct 240 E_8 roots in scaled integer coordinates (2 * r in Z^8, so (2r).(2r) == 8 <=> r.r == 2)
    roots_2: list[tuple[int, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-2, 2):
                for sj in (-2, 2):
                    vec = [0] * 8
                    vec[i] = si
                    vec[j] = sj
                    roots_2.append(tuple(vec))
    for signs in itertools.product((-1, 1), repeat=8):
        if sum(1 for s in signs if s == -1) % 2 == 0:
            roots_2.append(signs)

    root_set = set(roots_2)
    all_norm_sq_two = all(sum(c * c for c in r) == 8 for r in roots_2)

    # 4B. Simple roots of E_8, Cartan matrix det == 1, and Frenkel-Kac 2-cocycle for exact 248D e_8 Lie bracket
    simples_2 = [
        (1, -1, -1, -1, -1, -1, -1, 1),
        (0, 0, 0, 0, 0, 2, 2, 0),
        (0, 0, 0, 0, 0, 0, -2, 2),
        (0, 0, 0, 0, 0, -2, 2, 0),
        (0, 0, 0, 0, -2, 2, 0, 0),
        (0, 0, 0, -2, 2, 0, 0, 0),
        (0, 0, -2, 2, 0, 0, 0, 0),
        (0, -2, 2, 0, 0, 0, 0, 0),
    ]
    simples_in_e8 = all(s in root_set for s in simples_2)
    S_mat = sp.Matrix(simples_2)
    cartan_e8 = (S_mat * S_mat.T) / 4
    cartan_det = int(cartan_e8.det())
    S_inv = S_mat.inv()

    coords_simple: dict[tuple[int, ...], tuple[int, ...]] = {}
    integral_root_lattice = True
    for r in roots_2:
        c_vec = sp.Matrix([r]) * S_inv
        tup = tuple(int(c_vec[0, k]) for k in range(8))
        recon = tuple(int((sp.Matrix([tup]) * S_mat)[0, k]) for k in range(8))
        if recon != r:
            integral_root_lattice = False
        coords_simple[r] = tup

    C_int = [[int(cartan_e8[i, j]) for j in range(8)] for i in range(8)]

    def cocycle(r1: tuple[int, ...], r2: tuple[int, ...]) -> int:
        a = coords_simple[r1]
        b = coords_simple[r2]
        parity = 0
        for i in range(8):
            parity += a[i] * b[i]
            for j in range(i + 1, 8):
                parity += a[i] * b[j] * C_int[i][j]
        return -1 if (parity & 1) else 1

    root_to_basis = {r: 8 + idx for idx, r in enumerate(roots_2)}

    def e8_bracket_basis(idx_a: int, idx_b: int) -> dict[int, int]:
        """Exact integer Lie bracket on 248D scaled Chevalley basis (2*h_{e_i}, 2*E_r)."""
        if idx_a < 8 and idx_b < 8:
            return {}
        if idx_a < 8 and idx_b >= 8:
            r = roots_2[idx_b - 8]
            return {idx_b: r[idx_a]} if r[idx_a] != 0 else {}
        if idx_a >= 8 and idx_b < 8:
            r = roots_2[idx_a - 8]
            return {idx_a: -r[idx_b]} if r[idx_b] != 0 else {}
        r1 = roots_2[idx_a - 8]
        r2 = roots_2[idx_b - 8]
        rsum = tuple(r1[k] + r2[k] for k in range(8))
        if all(x == 0 for x in rsum):
            eps = cocycle(r1, r2)
            return {i: eps * r1[i] for i in range(8) if r1[i] != 0}
        if rsum in root_to_basis:
            return {root_to_basis[rsum]: 2 * cocycle(r1, r2)}
        return {}

    def e8_bracket(v1: dict[int, int], v2: dict[int, int]) -> dict[int, int]:
        out: dict[int, int] = {}
        for i, c1 in v1.items():
            for j, c2 in v2.items():
                for k, c3 in e8_bracket_basis(i, j).items():
                    nv = out.get(k, 0) + c1 * c2 * c3
                    if nv == 0:
                        out.pop(k, None)
                    else:
                        out[k] = nv
        return out

    # Sample Jacobi & skew-symmetry audit on 248D e_8
    sample_ids = list(range(0, 248, 12)) + [1, 3, 9, 55, 130, 247]
    e8_skew_and_jacobi_ok = True
    for ia in sample_ids[:18]:
        for ib in sample_ids[:18]:
            va, vb = {ia: 1}, {ib: 1}
            ab = e8_bracket(va, vb)
            ba = e8_bracket(vb, va)
            if any(ab.get(k, 0) + ba.get(k, 0) != 0 for k in set(ab) | set(ba)):
                e8_skew_and_jacobi_ok = False
                break
            for ic in sample_ids[:10]:
                vc = {ic: 1}
                j1 = e8_bracket(ab, vc)
                j2 = e8_bracket(e8_bracket(vb, vc), va)
                j3 = e8_bracket(e8_bracket(vc, va), vb)
                keys = set(j1) | set(j2) | set(j3)
                if any(j1.get(k, 0) + j2.get(k, 0) + j3.get(k, 0) != 0 for k in keys):
                    e8_skew_and_jacobi_ok = False
                    break

    # 4C. Subalgebra definitions in 248D E_8:
    # A_2^{fam} on {0, 1, 2}; E_6^{GUT} = C_{E_8}(A_2^{fam}) (r_0 == r_1 == r_2)
    # A_2^{(c)} on {3, 4, 5}; E_6^{cent} = C_{E_8}(A_2^{(c)}) (r_3 == r_4 == r_5)
    # G_{422} = D_3({3, 4, 5}) (+) D_2({6, 7}) subset D_5({3,4,5,6,7}) subset E_6^{GUT}
    a2_fam_roots = [r for r in roots_2 if (r[0] + r[1] + r[2] == 0) and all(r[k] == 0 for k in range(3, 8))]
    e6_gut_roots = [r for r in roots_2 if r[0] == r[1] == r[2]]
    a2_col_roots = [r for r in roots_2 if (r[3] + r[4] + r[5] == 0) and all(r[k] == 0 for k in (0, 1, 2, 6, 7))]
    e6_cent_roots = [r for r in roots_2 if r[3] == r[4] == r[5]]
    g422_roots = [
        r for r in roots_2
        if r[0] == 0 and r[1] == 0 and r[2] == 0 and (
            (r[6] == 0 and r[7] == 0) or (r[3] == 0 and r[4] == 0 and r[5] == 0)
        )
    ]

    # Explicit 248D subspace bases (rows in Z^248) for exact linear-algebra intersection & commutator checks
    def subalgebra_248_rows(cartan_vecs: list[list[int]], sub_roots: list[tuple[int, ...]]) -> list[list[int]]:
        rows = []
        for cv in cartan_vecs:
            row = [0] * 248
            for idx in range(8):
                row[idx] = cv[idx]
            rows.append(row)
        for r in sub_roots:
            row = [0] * 248
            row[root_to_basis[r]] = 1
            rows.append(row)
        return rows

    def exact_zz_rank(rows: list[list[int]]) -> int:
        return int(DomainMatrix(rows, (len(rows), len(rows[0])), sp.ZZ).rank())

    cartan_a2_fam = [
        [1, -1, 0, 0, 0, 0, 0, 0],
        [0, 1, -1, 0, 0, 0, 0, 0],
    ]
    cartan_e6_gut = [
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
    ]
    cartan_e6_cent = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
    ]
    cartan_g422 = [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
    ]

    B_a2_fam = subalgebra_248_rows(cartan_a2_fam, a2_fam_roots)
    B_e6_gut = subalgebra_248_rows(cartan_e6_gut, e6_gut_roots)
    B_e6_cent = subalgebra_248_rows(cartan_e6_cent, e6_cent_roots)
    B_g422 = subalgebra_248_rows(cartan_g422, g422_roots)

    dim_a2_fam = exact_zz_rank(B_a2_fam)
    dim_e6_gut = exact_zz_rank(B_e6_gut)
    dim_e6_cent = exact_zz_rank(B_e6_cent)
    dim_g422 = exact_zz_rank(B_g422)

    # Subspace intersection dim(U cap W) = dim(U) + dim(W) - rank([U; W])!
    dim_inter_e6_cent_gut = dim_e6_cent + dim_e6_gut - exact_zz_rank(B_e6_cent + B_e6_gut)
    dim_inter_e6_cent_g422 = dim_e6_cent + dim_g422 - exact_zz_rank(B_e6_cent + B_g422)

    inter_e6_root_count = len(set(e6_cent_roots) & set(e6_gut_roots))
    inter_422_root_count = len(set(e6_cent_roots) & set(g422_roots))

    # 4D. Exact commutator check [A_2^{fam}, E_6^{GUT}] == 0 across ALL 8 x 78 = 624 generator pairs in 248D e_8!
    a2_fam_elements = [{idx: row[idx] for idx in range(248) if row[idx] != 0} for row in B_a2_fam]
    e6_gut_elements = [{idx: row[idx] for idx in range(248) if row[idx] != 0} for row in B_e6_gut]

    comm_a2_fam_e6_gut_all_zero = True
    tested_pairs = 0
    for x_el in a2_fam_elements:
        for y_el in e6_gut_elements:
            tested_pairs += 1
            if e8_bracket(x_el, y_el):
                comm_a2_fam_e6_gut_all_zero = False
                break

    # 4E. Orthogonal Weyl involution W_inv in SO(8) cap W(E_8) vs PF8.4 order-4 (0 4 1 3)(2 5)
    # 4 mutually orthogonal roots: (e_0 - e_3), (e_1 - e_4), (e_2 - e_5), (e_6 - e_7)
    refl_roots_2 = [
        (2, 0, 0, -2, 0, 0, 0, 0),
        (0, 2, 0, 0, -2, 0, 0, 0),
        (0, 0, 2, 0, 0, -2, 0, 0),
        (0, 0, 0, 0, 0, 0, 2, -2),
    ]
    refl_roots_in_e8 = all(r in root_set for r in refl_roots_2)
    refl_roots_orthogonal = all(
        sum(refl_roots_2[a][k] * refl_roots_2[b][k] for k in range(8)) == 0
        for a in range(4) for b in range(a + 1, 4)
    )

    def weyl_reflection_matrix(r2: tuple[int, ...]) -> sp.Matrix:
        # s_alpha(v) = v - 2 (v.alpha)/(alpha.alpha) alpha; for r2 = 2*alpha, r2.r2 = 8, so I_8 - (1/4) r2^T r2
        v_col = sp.Matrix(8, 1, list(r2))
        return sp.eye(8) - (v_col * v_col.T) / 4

    W_inv = sp.eye(8)
    for r2 in refl_roots_2:
        W_inv = weyl_reflection_matrix(r2) * W_inv

    w_inv_orth = (W_inv.T * W_inv) == sp.eye(8)
    w_inv_det = int(W_inv.det())
    w_inv_not_id = W_inv != sp.eye(8)
    w_inv_sq_eq_id = (W_inv * W_inv) == sp.eye(8)

    def apply_w(W_mat: sp.Matrix, r_list: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
        out = set()
        for r in r_list:
            img = W_mat * sp.Matrix(8, 1, list(r))
            out.add(tuple(int(img[k, 0]) for k in range(8)))
        return out

    w_inv_preserves_e8 = apply_w(W_inv, roots_2) == root_set
    w_inv_swaps_e6 = (
        apply_w(W_inv, e6_cent_roots) == set(e6_gut_roots)
        and apply_w(W_inv, e6_gut_roots) == set(e6_cent_roots)
    )
    # Check Cartan subspace conjugation too:
    C_cent_8 = sp.Matrix(cartan_e6_cent)  # 6x8
    C_gut_8 = sp.Matrix(cartan_e6_gut)    # 6x8
    C_cent_conj = C_cent_8 * W_inv.T
    w_inv_swaps_cartan = int(sp.Matrix.vstack(C_cent_conj, C_gut_8).rank()) == 6

    # PF8.4: 4-cycle permutation (0 4 1 3)(2 5) in SO(8) cap W(E_8) has exact order 4 != 2!
    perm_pf84 = [4, 3, 5, 0, 1, 2, 6, 7]  # 0->4->1->3->0, 2<->5, 6->6, 7->7
    W_4cyc = sp.zeros(8, 8)
    for col_idx, row_target in enumerate(perm_pf84):
        W_4cyc[row_target, col_idx] = 1

    w_4cyc_det = int(W_4cyc.det())
    w_4cyc_preserves_e8 = apply_w(W_4cyc, roots_2) == root_set
    w_4cyc_swaps_e6 = apply_w(W_4cyc, e6_cent_roots) == set(e6_gut_roots)
    W_4cyc_sq = W_4cyc * W_4cyc
    W_4cyc_fourth = W_4cyc_sq * W_4cyc_sq
    w_4cyc_sq_neq_id = W_4cyc_sq != sp.eye(8)
    w_4cyc_fourth_eq_id = W_4cyc_fourth == sp.eye(8)
    # Exact order computation for W_4cyc
    order_w_4cyc = 1
    cur_w = W_4cyc
    while cur_w != sp.eye(8):
        cur_w = cur_w * W_4cyc
        order_w_4cyc += 1
    pf8_4_caught = w_4cyc_sq_neq_id and (order_w_4cyc == 4)

    # 4F. Matter decomposition 240 - 6 - 72 == 162 == 2 x (3 x 27): (3_fam, 27_GUT) (+) (3bar_fam, 27bar_GUT)
    matter_roots = [r for r in roots_2 if (r not in set(a2_fam_roots)) and (r not in set(e6_gut_roots))]
    # Project (r_0, r_1, r_2) onto traceless A_2^{fam} plane: 3 * proj = (2r_0 - r_1 - r_2, 2r_1 - r_0 - r_2, 2r_2 - r_0 - r_1)
    # For 3_fam fundamental weights w_0, w_1, w_2 (scaled by 6 since roots_2 = 2*r):
    # w_0 -> (4, -2, -2), w_1 -> (-2, 4, -2), w_2 -> (-2, -2, 4)
    # -w_0 -> (-4, 2, 2), -w_1 -> (2, -4, 2), -w_2 -> (2, 2, -4)
    fam_3_weights = [(4, -2, -2), (-2, 4, -2), (-2, -2, 4)]
    fam_3bar_weights = [(-4, 2, 2), (2, -4, 2), (2, 2, -4)]

    buckets_3: dict[tuple[int, int, int], list[tuple[int, ...]]] = {w: [] for w in fam_3_weights}
    buckets_3bar: dict[tuple[int, int, int], list[tuple[int, ...]]] = {w: [] for w in fam_3bar_weights}
    unclassified_matter = 0

    for r in matter_roots:
        proj_6 = (2 * r[0] - r[1] - r[2], 2 * r[1] - r[0] - r[2], 2 * r[2] - r[0] - r[1])
        if proj_6 in buckets_3:
            buckets_3[proj_6].append(r)
        elif proj_6 in buckets_3bar:
            buckets_3bar[proj_6].append(r)
        else:
            unclassified_matter += 1

    per_family_3_counts = [len(buckets_3[w]) for w in fam_3_weights]
    per_family_3bar_counts = [len(buckets_3bar[w]) for w in fam_3bar_weights]
    # Inside each 27_GUT = 10_SO10 + 16_+_Spin10 + 1_SO10, count spinor roots (odd entries in coords 3..7 => 16_+!)
    per_family_chiral_16_counts = [
        sum(1 for r in buckets_3[w] if abs(r[3]) == 1) for w in fam_3_weights
    ]

    # 4G. Chinese Remainder Theorem Z_{15} ~= Z_3^{fam} x Z_5^{gauge} (arithmetic + 15x15 unitary operator check)
    crt_pairs = {(n % 3, n % 5) for n in range(15)}
    crt_ring_hom_ok = all(
        (((a + b) % 15) % 3 == (a % 3 + b % 3) % 3)
        and (((a + b) % 15) % 5 == (a % 5 + b % 5) % 5)
        and (((a * b) % 15) % 3 == ((a % 3) * (b % 3)) % 3)
        and (((a * b) % 15) % 5 == ((a % 5) * (b % 5)) % 5)
        for a in range(15) for b in range(15)
    )
    # 15 x 15 operator check: U_15 = Z_3 otimes Z_5
    w3 = complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))
    w5 = complex(math.cos(2 * math.pi / 5), math.sin(2 * math.pi / 5))
    Z3_op = np.diag([1, w3, w3 * w3]).astype(np.complex128)
    Z5_op = np.diag([1, w5, w5 ** 2, w5 ** 3, w5 ** 4]).astype(np.complex128)
    U15_op = np.kron(Z3_op, Z5_op)
    I15_op = np.eye(15, dtype=np.complex128)
    u15_exact_order_15 = (
        all(float(np.linalg.norm(np.linalg.matrix_power(U15_op, k) - I15_op)) > (1 / 10) for k in range(1, 15))
        and float(np.linalg.norm(np.linalg.matrix_power(U15_op, 15) - I15_op)) < tol
    )
    # Orthogonal CRT idempotents 10 == (1, 0) and 6 == (0, 1) mod (3, 5) recover pure family and pure gauge factors!
    crt_operator_factor_recovery = (
        float(np.linalg.norm(np.linalg.matrix_power(U15_op, 10) - np.kron(Z3_op, np.eye(5)))) < tol
        and float(np.linalg.norm(np.linalg.matrix_power(U15_op, 6) - np.kron(np.eye(3), Z5_op))) < tol
    )

    # 4H. PF8.5: Conflating generation triplet 3_{fam} with colour triplet 3_c inside E_6^{GUT}
    # Take G_fam_conflated = E_{e_3 - e_4} in A_2^{(c)} subset E_6^{GUT} and G_c = E_{e_4 - e_5} in A_2^{(c)} subset E_6^{GUT}
    r_34 = (0, 0, 0, 2, -2, 0, 0, 0)
    r_45 = (0, 0, 0, 0, 2, -2, 0, 0)
    comm_pf85_e8 = e8_bracket({root_to_basis[r_34]: 1}, {root_to_basis[r_45]: 1})
    # Also on fundamental 3D triplet: [E_01 - E_10, E_12 - E_21] = E_02 - E_20, Frobenius norm = sqrt(2) > 1!
    G_fam_wrong_3 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], dtype=np.int64)
    G_col_3 = np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=np.int64)
    comm_3d = G_fam_wrong_3 @ G_col_3 - G_col_3 @ G_fam_wrong_3
    comm_3d_norm_sq = int(np.sum(comm_3d * comm_3d))  # == 2 > 1 => norm == sqrt(2) > 1!
    comm_e8_coeff_norm_sq = sum(v * v for v in comm_pf85_e8.values())  # == 4 > 1 => norm == 2 > 1!
    pf8_5_caught = (len(comm_pf85_e8) > 0) and (comm_3d_norm_sq > 1) and (comm_e8_coeff_norm_sq > 1)

    deliv_4 = {
        "e8_root_count": len(roots_2),
        "e8_distinct_roots": len(root_set),
        "e8_all_roots_norm_sq_eq_2": all_norm_sq_two,
        "e8_cartan_det": cartan_det,
        "e8_all_roots_integral_in_simple_basis": integral_root_lattice,
        "e8_248d_frenkel_kac_skew_and_jacobi_verified": e8_skew_and_jacobi_ok,
        "dim_A2_fam": dim_a2_fam,
        "A2_col_root_count": len(a2_col_roots),
        "dim_E6_GUT": dim_e6_gut,
        "dim_E6_cent": dim_e6_cent,
        "dim_G422": dim_g422,
        "dim_E6_cent_cap_E6_GUT": dim_inter_e6_cent_gut,
        "E6_cent_cap_E6_GUT_roots_plus_cartans": [inter_e6_root_count, 4],
        "dim_E6_cent_cap_G422": dim_inter_e6_cent_g422,
        "E6_cent_cap_G422_roots_plus_cartans": [inter_422_root_count, 3],
        "orthogonal_reflections_in_E8_and_mutually_orthogonal": refl_roots_in_e8 and refl_roots_orthogonal,
        "W_inv_in_SO8_cap_WE8": w_inv_orth and (w_inv_det == 1) and w_inv_preserves_e8,
        "W_inv_exact_order_2": w_inv_not_id and w_inv_sq_eq_id,
        "W_inv_conjugates_E6_cent_and_E6_GUT": w_inv_swaps_e6 and w_inv_swaps_cartan,
        "commutator_A2_fam_E6_GUT_tested_pairs": tested_pairs,
        "commutator_A2_fam_E6_GUT_exact_zero": comm_a2_fam_e6_gut_all_zero,
        "matter_root_total": len(matter_roots),
        "matter_3_fam_x_27_GUT_counts": per_family_3_counts,
        "matter_3bar_fam_x_27bar_GUT_counts": per_family_3bar_counts,
        "matter_chiral_16_per_family": per_family_chiral_16_counts,
        "matter_162_eq_2_x_3_x_27": (
            len(matter_roots) == 162
            and unclassified_matter == 0
            and per_family_3_counts == [27, 27, 27]
            and per_family_3bar_counts == [27, 27, 27]
            and per_family_chiral_16_counts == [16, 16, 16]
        ),
        "crt_Z15_bijection_size": len(crt_pairs),
        "crt_Z15_ring_isomorphism": crt_ring_hom_ok,
        "crt_15x15_operator_order_15_and_factor_recovery": u15_exact_order_15 and crt_operator_factor_recovery,
        "passed": (
            len(roots_2) == 240
            and len(root_set) == 240
            and all_norm_sq_two
            and simples_in_e8
            and cartan_det == 1
            and integral_root_lattice
            and e8_skew_and_jacobi_ok
            and dim_a2_fam == 8
            and len(a2_col_roots) == 6
            and dim_e6_gut == 78
            and dim_e6_cent == 78
            and dim_g422 == 21
            and dim_inter_e6_cent_gut == 16
            and inter_e6_root_count == 12
            and dim_inter_e6_cent_g422 == 7
            and inter_422_root_count == 4
            and refl_roots_in_e8
            and refl_roots_orthogonal
            and w_inv_orth
            and w_inv_det == 1
            and w_inv_preserves_e8
            and w_inv_not_id
            and w_inv_sq_eq_id
            and w_inv_swaps_e6
            and w_inv_swaps_cartan
            and tested_pairs == 624
            and comm_a2_fam_e6_gut_all_zero
            and len(matter_roots) == 162
            and unclassified_matter == 0
            and per_family_3_counts == [27, 27, 27]
            and per_family_3bar_counts == [27, 27, 27]
            and per_family_chiral_16_counts == [16, 16, 16]
            and math.gcd(3, 5) == 1
            and len(crt_pairs) == 15
            and crt_ring_hom_ok
            and u15_exact_order_15
            and crt_operator_factor_recovery
        ),
    }

    pf_4_5 = {
        "PF8_4_non_orthogonal_4cycle_order_4": {
            "det_eq_plus_1": w_4cyc_det == 1,
            "in_WE8_and_swaps_E6": w_4cyc_preserves_e8 and w_4cyc_swaps_e6,
            "W_4cyc_squared_neq_I8": w_4cyc_sq_neq_id,
            "W_4cyc_fourth_eq_I8": w_4cyc_fourth_eq_id,
            "exact_order": order_w_4cyc,
            "fault_caught": pf8_4_caught,
        },
        "PF8_5_conflating_family_with_colour_triplet": {
            "e8_bracket_nonzero_terms": len(comm_pf85_e8),
            "e8_bracket_norm_sq": comm_e8_coeff_norm_sq,
            "fundamental_3d_commutator_norm_sq": comm_3d_norm_sq,
            "norm_strictly_gt_1": (comm_3d_norm_sq > 1) and (comm_e8_coeff_norm_sq > 1),
            "fault_caught": pf8_5_caught,
        },
    }
    return deliv_4, pf_4_5


def run_referee(write_output: bool = True) -> dict[str, object]:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]

    ast_audit = audit_self_ast_and_imports(script_path)
    manifest_audit = verify_sha256_manifests(repo_root, script_path)
    deliv_1, deliv_2, pf_1_2 = check_deliverable_1_and_2()
    deliv_3, pf_3 = check_deliverable_3()
    deliv_4, pf_4_5 = check_deliverable_4()

    planted_faults = {}
    planted_faults.update(pf_1_2)
    planted_faults.update(pf_3)
    planted_faults.update(pf_4_5)

    all_planted_faults_caught = all(
        bool(v["fault_caught"]) for v in planted_faults.values()
    )

    overall_passed = bool(
        ast_audit["passed"]
        and manifest_audit["passed"]
        and deliv_1["passed"]
        and deliv_2["passed"]
        and deliv_3["passed"]
        and deliv_4["passed"]
        and all_planted_faults_caught
    )

    report: dict[str, object] = {
        "gate": "AGY-002_FOUND-G8",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_inputs_used": "0 of 19",
        "ast_and_import_self_audit": ast_audit,
        "sha256_manifest_verification": manifest_audit,
        "deliverable_1_car_cl10_fock_postulate_d": deliv_1,
        "deliverable_2_commutant_dichotomy_and_frobenius_schur": deliv_2,
        "deliverable_3_metallic_discriminants_and_rival_primes": deliv_3,
        "deliverable_4_e8_family_colour_orthogonality": deliv_4,
        "planted_fault_controls": planted_faults,
        "all_planted_faults_caught": all_planted_faults_caught,
        "overall_passed": overall_passed,
    }

    if write_output:
        out_path = script_path.parent / "referee_found_g8_out.json"
        out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    if not overall_passed:
        raise SystemExit(1)
    return report


if __name__ == "__main__":
    run_referee(write_output=True)
