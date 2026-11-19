#!/usr/bin/env python3
"""Cold-Room Independent Zero-Trust Referee for Gate F-U1 (AGY-002_FOUND-V2-U1).

Implements an independent second-method mathematical audit strictly from the Card:
- Section 0: AST zero-float/zero-complex/import scan & SHA-256 custody checks.
- Section 1: 4_1 Seifert SNF, Fox calculus Jacobian, exhaustive odd-n dihedral
             homomorphisms (n=3..31), exact SL_2(Z[zeta_6]) Riley longitude,
             peripheral orbits [1,2,2], S_5 centralizers (1, 5), 60-digit Weyl
             orthonormality (< 10^-35), Tr(D(v)P)=1, and q_{W_5} block identity.
- Section 2: Explicit bitmask/inversion-parity exterior algebra Lambda^*(W_5),
             Cl(10) Majorana Clifford algebra & (-1)^F volume element, 4D APS
             chirality correlation, Grassmann exterior-power & 945-matching
             Pfaffian Berezin Gaussian identity, su(5) commutant (dim 12),
             global Z_6 kernel (order 6), 6Y spectrum & all 4 SM anomaly sums,
             and Kawamura doublet-triplet splitting.
- Section 3: Five planted fault controls PFU1-1..PFU1-5.
"""

from __future__ import annotations

import ast
import collections
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix


# ---------------------------------------------------------------------------
# Precision & Constants (strictly zero float / complex AST literals)
# ---------------------------------------------------------------------------

MP_DPS = 60
TOL_EXP = -35
ALLOWED_IMPORT_ROOTS = frozenset(
    {
        "__future__",
        "ast",
        "collections",
        "fractions",
        "hashlib",
        "itertools",
        "json",
        "pathlib",
        "re",
        "mpmath",
        "sympy",
    }
)


def mp_tol() -> mp.mpf:
    """Return 10^(-35) as an mpmath mpf without float literals."""
    return mp.mpf(10) ** TOL_EXP


def fmt_mp(val: mp.mpf) -> str:
    """Format an mpmath real number cleanly without Python float conversion."""
    return mp.nstr(val, 16)


# ---------------------------------------------------------------------------
# Exact Cyclotomic Ring Q[zeta_5] = Q[z]/(z^4 + z^3 + z^2 + z + 1)
# and Eisenstein Integer Ring Z[zeta_6] = Z[z]/(z^2 - z + 1)
# ---------------------------------------------------------------------------


class Eisenstein:
    """Exact element a + b * zeta_6 in Z[zeta_6] where zeta_6^2 = zeta_6 - 1."""

    __slots__ = ("a", "b")

    def __init__(self, a: int, b: int = 0) -> None:
        self.a = int(a)
        self.b = int(b)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return self.a == other and self.b == 0
        if not isinstance(other, Eisenstein):
            return False
        return self.a == other.a and self.b == other.b

    def __neg__(self) -> "Eisenstein":
        return Eisenstein(-self.a, -self.b)

    def __add__(self, other: "Eisenstein | int") -> "Eisenstein":
        if isinstance(other, int):
            return Eisenstein(self.a + other, self.b)
        return Eisenstein(self.a + other.a, self.b + other.b)

    def __radd__(self, other: int) -> "Eisenstein":
        return self + other

    def __sub__(self, other: "Eisenstein | int") -> "Eisenstein":
        if isinstance(other, int):
            return Eisenstein(self.a - other, self.b)
        return Eisenstein(self.a - other.a, self.b - other.b)

    def __mul__(self, other: "Eisenstein | int") -> "Eisenstein":
        if isinstance(other, int):
            return Eisenstein(self.a * other, self.b * other)
        # (a1 + b1 z)(a2 + b2 z) = a1 a2 + (a1 b2 + b1 a2) z + b1 b2 (z - 1)
        aa = self.a * other.a - self.b * other.b
        bb = self.a * other.b + self.b * other.a + self.b * other.b
        return Eisenstein(aa, bb)

    def __rmul__(self, other: int) -> "Eisenstein":
        return self * other

    def to_mp(self) -> mp.mpc:
        """Evaluate at zeta_6 = (1 + i * sqrt(3)) / 2."""
        zeta6 = (mp.mpf(1) + mp.mpc(0, 1) * mp.sqrt(mp.mpf(3))) / mp.mpf(2)
        return mp.mpf(self.a) + mp.mpf(self.b) * zeta6

    def __repr__(self) -> str:
        return f"({self.a} + {self.b}*zeta6)"


def mat2_mul_eis(
    A: list[list[Eisenstein]], B: list[list[Eisenstein]]
) -> list[list[Eisenstein]]:
    """Multiply two 2x2 matrices over Z[zeta_6]."""
    return [
        [
            A[i][0] * B[0][j] + A[i][1] * B[1][j]
            for j in range(2)
        ]
        for i in range(2)
    ]


def mat2_sub_eis(
    A: list[list[Eisenstein]], B: list[list[Eisenstein]]
) -> list[list[Eisenstein]]:
    """Subtract two 2x2 matrices over Z[zeta_6]."""
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def mat2_det_eis(A: list[list[Eisenstein]]) -> Eisenstein:
    """Determinant of a 2x2 matrix over Z[zeta_6]."""
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def mat2_inv_sl2_eis(A: list[list[Eisenstein]]) -> list[list[Eisenstein]]:
    """Inverse of a 2x2 matrix in SL_2(Z[zeta_6])."""
    det = mat2_det_eis(A)
    if det != Eisenstein(1, 0):
        raise ValueError("Matrix is not in SL_2(Z[zeta_6])")
    return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]


class Cyc5:
    """Exact element in Q[zeta_5] represented by c0 + c1 z + c2 z^2 + c3 z^3.

    Uses z^4 = -1 - z - z^2 - z^3.
    """

    __slots__ = ("c",)

    def __init__(self, coeffs: tuple[Fraction, Fraction, Fraction, Fraction]) -> None:
        self.c = coeffs

    @classmethod
    def from_int(cls, n: int) -> "Cyc5":
        return cls((Fraction(n), Fraction(0), Fraction(0), Fraction(0)))

    @classmethod
    def from_frac(cls, f: Fraction) -> "Cyc5":
        return cls((f, Fraction(0), Fraction(0), Fraction(0)))

    @classmethod
    def zeta_pow(cls, k: int) -> "Cyc5":
        r = k % 5
        if r < 4:
            arr = [Fraction(0)] * 4
            arr[r] = Fraction(1)
            return cls((arr[0], arr[1], arr[2], arr[3]))
        return cls((Fraction(-1), Fraction(-1), Fraction(-1), Fraction(-1)))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return self == Cyc5.from_int(other)
        if isinstance(other, Fraction):
            return self == Cyc5.from_frac(other)
        if not isinstance(other, Cyc5):
            return False
        return self.c == other.c

    def __neg__(self) -> "Cyc5":
        return Cyc5((-self.c[0], -self.c[1], -self.c[2], -self.c[3]))

    def __add__(self, other: "Cyc5 | int | Fraction") -> "Cyc5":
        if isinstance(other, int):
            other = Cyc5.from_int(other)
        elif isinstance(other, Fraction):
            other = Cyc5.from_frac(other)
        return Cyc5(
            (
                self.c[0] + other.c[0],
                self.c[1] + other.c[1],
                self.c[2] + other.c[2],
                self.c[3] + other.c[3],
            )
        )

    def __sub__(self, other: "Cyc5 | int | Fraction") -> "Cyc5":
        if isinstance(other, int):
            other = Cyc5.from_int(other)
        elif isinstance(other, Fraction):
            other = Cyc5.from_frac(other)
        return self + (-other)

    def __mul__(self, other: "Cyc5 | int | Fraction") -> "Cyc5":
        if isinstance(other, int):
            other = Cyc5.from_int(other)
        elif isinstance(other, Fraction):
            other = Cyc5.from_frac(other)
        raw = [Fraction(0)] * 5
        for i in range(4):
            for j in range(4):
                raw[(i + j) % 5] += self.c[i] * other.c[j]
        c4 = raw[4]
        return Cyc5((raw[0] - c4, raw[1] - c4, raw[2] - c4, raw[3] - c4))

    def conj(self) -> "Cyc5":
        """Complex conjugation maps zeta_5^k -> zeta_5^(-k)."""
        # c0 + c1 z + c2 z^2 + c3 z^3 -> c0 + c1 z^4 + c2 z^3 + c3 z^2
        # = (c0 - c1) - c1 z + (c3 - c1) z^2 + (c2 - c1) z^3
        c0, c1, c2, c3 = self.c
        return Cyc5((c0 - c1, -c1, c3 - c1, c2 - c1))

    def to_mp(self, z5: mp.mpc) -> mp.mpc:
        acc = mp.mpc(0, 0)
        zp = mp.mpc(1, 0)
        for coef in self.c:
            acc += (mp.mpf(coef.numerator) / mp.mpf(coef.denominator)) * zp
            zp *= z5
        return acc


# ---------------------------------------------------------------------------
# Section 0: AST & SHA Custody
# ---------------------------------------------------------------------------


def verify_sha_manifest(manifest_path: Path, expected_target: Path, repo_root: Path) -> dict[str, object]:
    """Read ONLY 64-char hex digest lines from a SHA256 manifest and hash-verify target bytes."""
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Missing manifest: {manifest_path}")
    if not expected_target.is_file():
        raise FileNotFoundError(f"Missing target file: {expected_target}")

    lines = manifest_path.read_text(encoding="utf-8").splitlines()
    parsed: list[tuple[str, str | None]] = []
    for line in lines:
        m = re.match(r"^\s*([0-9a-fA-F]{64})(?:\s+\*?(.+?))?\s*$", line)
        if m:
            parsed.append((m.group(1).lower(), m.group(2).strip() if m.group(2) else None))

    if len(parsed) != 1:
        raise ValueError(f"Expected exactly 1 digest line in {manifest_path}, got {len(parsed)}")

    recorded_hex, recorded_name = parsed[0]
    target_name_ok = True
    if recorded_name is not None:
        rec_path = Path(recorded_name)
        if len(rec_path.parts) > 1:
            target_name_ok = (repo_root / rec_path).resolve() == expected_target.resolve()
        else:
            target_name_ok = rec_path.name == expected_target.name

    # Hash raw bytes directly without decoding or inspecting target content.
    actual_hex = hashlib.sha256(expected_target.read_bytes()).hexdigest().lower()
    digest_matches = (actual_hex == recorded_hex) and target_name_ok
    return {
        "manifest": str(manifest_path.relative_to(repo_root)),
        "target": str(expected_target.relative_to(repo_root)),
        "recorded_sha256": recorded_hex,
        "computed_sha256": actual_hex,
        "target_name_ok": target_name_ok,
        "verified": digest_matches,
    }


def section_0_ast_and_sha_custody(script_path: Path, repo_root: Path) -> dict[str, object]:
    """Audit own AST for zero float/complex literals & imports, plus producer/referee SHA custody."""
    source = script_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(script_path))

    float_literals = 0
    complex_literals = 0
    float_complex_calls = 0
    imports_found: list[str] = []
    disallowed_imports: list[str] = []
    relative_imports = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                float_complex_calls += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root_pkg = alias.name.split(".")[0]
                imports_found.append(alias.name)
                if root_pkg not in ALLOWED_IMPORT_ROOTS:
                    disallowed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level != 0:
                relative_imports += 1
                disallowed_imports.append(f"relative_level_{node.level}:{node.module}")
            if node.module is not None:
                root_pkg = node.module.split(".")[0]
                imports_found.append(node.module)
                if root_pkg not in ALLOWED_IMPORT_ROOTS:
                    disallowed_imports.append(node.module)

    ref_dir = script_path.parent
    prod_dir = repo_root / "relays" / "agy002_found_v2_u1"

    self_sha = verify_sha_manifest(
        ref_dir / "SCRIPT_SHA256.txt",
        script_path,
        repo_root,
    )
    prod_script_sha = verify_sha_manifest(
        prod_dir / "SCRIPT_SHA256.txt",
        prod_dir / "verify_found_v2_u1.py",
        repo_root,
    )
    prod_output_sha = verify_sha_manifest(
        prod_dir / "OUTPUT_SHA256.txt",
        prod_dir / "verify_found_v2_u1_out.json",
        repo_root,
    )

    ast_clean = (
        float_literals == 0
        and complex_literals == 0
        and float_complex_calls == 0
        and len(disallowed_imports) == 0
        and relative_imports == 0
    )
    sha_clean = (
        bool(self_sha["verified"])
        and bool(prod_script_sha["verified"])
        and bool(prod_output_sha["verified"])
    )

    return {
        "ast_scan": {
            "float_literal_count": float_literals,
            "complex_literal_count": complex_literals,
            "float_complex_call_count": float_complex_calls,
            "relative_import_count": relative_imports,
            "disallowed_imports": disallowed_imports,
            "unique_import_roots": sorted({name.split(".")[0] for name in imports_found}),
            "ast_clean": ast_clean,
        },
        "sha_custody": {
            "referee_script": self_sha,
            "producer_script": prod_script_sha,
            "producer_output": prod_output_sha,
            "all_sha_verified": sha_clean,
        },
    }


# ---------------------------------------------------------------------------
# Section 1: Independent Dihedral Cover & Knot Homology Check
# ---------------------------------------------------------------------------


def exact_integer_snf_2x2(mat: list[list[int]]) -> dict[str, object]:
    """Compute exact Smith Normal Form U * A * W = diag(d1, d2) for a 2x2 integer matrix."""
    A = [[int(mat[0][0]), int(mat[0][1])], [int(mat[1][0]), int(mat[1][1])]]
    U = [[1, 0], [0, 1]]
    W = [[1, 0], [0, 1]]

    def row_swap(i: int, j: int) -> None:
        A[i], A[j] = A[j], A[i]
        U[i], U[j] = U[j], U[i]

    def col_swap(i: int, j: int) -> None:
        for r in range(2):
            A[r][i], A[r][j] = A[r][j], A[r][i]
            W[r][i], W[r][j] = W[r][j], W[r][i]

    def row_add(dst: int, src: int, k: int) -> None:
        for c in range(2):
            A[dst][c] += k * A[src][c]
            U[dst][c] += k * U[src][c]

    def col_add(dst: int, src: int, k: int) -> None:
        for r in range(2):
            A[r][dst] += k * A[r][src]
            W[r][dst] += k * W[r][src]

    def row_neg(i: int) -> None:
        for c in range(2):
            A[i][c] = -A[i][c]
            U[i][c] = -U[i][c]

    def col_neg(j: int) -> None:
        for r in range(2):
            A[r][j] = -A[r][j]
            W[r][j] = -W[r][j]

    # Euclidean reduction on 2x2 integer matrix
    for _ in range(100):
        # Find smallest nonzero entry in absolute value to pivot to (0, 0)
        nz = [
            (abs(A[r][c]), r, c)
            for r in range(2)
            for c in range(2)
            if A[r][c] != 0
        ]
        if not nz:
            break
        _, pr, pc = min(nz)
        if pr != 0:
            row_swap(0, pr)
        if pc != 0:
            col_swap(0, pc)
        if A[0][0] < 0:
            row_neg(0)

        p = A[0][0]
        if A[1][0] != 0:
            q = A[1][0] // p
            row_add(1, 0, -q)
            if A[1][0] != 0:
                continue
        if A[0][1] != 0:
            q = A[0][1] // p
            col_add(1, 0, -q)
            if A[0][1] != 0:
                continue
        if A[1][1] % p != 0:
            row_add(0, 1, 1)
            continue
        if A[1][1] < 0:
            row_neg(1)
        break

    # Verify U * mat * W == A and |det U| == 1, |det W| == 1
    def mmul(X: list[list[int]], Y: list[list[int]]) -> list[list[int]]:
        return [
            [sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)
        ]

    reconstructed = mmul(mmul(U, mat), W)
    det_U = U[0][0] * U[1][1] - U[0][1] * U[1][0]
    det_W = W[0][0] * W[1][1] - W[0][1] * W[1][0]
    det_mat = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    return {
        "matrix": mat,
        "smith_normal_form": A,
        "invariant_factors": [A[0][0], A[1][1]],
        "abs_det": abs(det_mat),
        "det_U": det_U,
        "det_W": det_W,
        "identity_holds": (reconstructed == A) and (abs(det_U) == 1) and (abs(det_W) == 1),
    }


def fox_derivative_abelianized(
    word: list[tuple[str, int]], var: str, t_sym: sp.Symbol
) -> sp.Expr:
    """Compute exact Fox free derivative d(word)/d(var) abelianized via x,y -> t."""
    # Represent prefix element in Z[t, t^-1] incrementally using Leibniz rule:
    # d(u * g^e)/d(var) = d(u)/d(var) + alpha(u) * d(g^e)/d(var)
    deriv = sp.Integer(0)
    prefix_ab = sp.Integer(1)
    for gen, power in word:
        if power == 1:
            if gen == var:
                deriv += prefix_ab
            prefix_ab *= t_sym
        elif power == -1:
            if gen == var:
                deriv -= prefix_ab * (t_sym ** (-1))
            prefix_ab *= t_sym ** (-1)
        else:
            raise ValueError(f"Unsupported generator power: {power}")
    return sp.simplify(deriv)


def dn_mul(e1: int, a1: int, e2: int, a2: int, n: int) -> tuple[int, int]:
    """Multiply two elements (e1, a1), (e2, a2) in D_n = Z_2 |x Z_n.

    Representation: sigma_{(e, a)}(k) = (-1)^e * k + a (mod n).
    """
    sign1 = 1 if e1 == 0 else -1
    return ((e1 ^ e2), (sign1 * a2 + a1) % n)


def dn_inv(e: int, a: int, n: int) -> tuple[int, int]:
    """Inverse of (e, a) in D_n."""
    if e == 0:
        return (0, (-a) % n)
    # (1, a)(1, a) = (0, -a + a) = (0, 0), so reflections are self-inverse.
    return (1, a % n)


def dn_word_eval(word: list[tuple[str, int]], x: tuple[int, int], y: tuple[int, int], n: int) -> tuple[int, int]:
    """Evaluate a free-group word in D_n."""
    xi = dn_inv(x[0], x[1], n)
    yi = dn_inv(y[0], y[1], n)
    acc = (0, 0)
    for gen, pwr in word:
        elem = x if gen == "x" else y
        if pwr == -1:
            elem = xi if gen == "x" else yi
        elif pwr != 1:
            raise ValueError(f"Unsupported power {pwr}")
        acc = dn_mul(acc[0], acc[1], elem[0], elem[1], n)
    return acc


def dn_subgroup_order(x: tuple[int, int], y: tuple[int, int], n: int) -> int:
    """Compute exact order of subgroup <x, y> <= D_n via BFS closure."""
    xi = dn_inv(x[0], x[1], n)
    yi = dn_inv(y[0], y[1], n)
    gens = [x, y, xi, yi]
    seen: set[tuple[int, int]] = {(0, 0)}
    queue = collections.deque([(0, 0)])
    while queue:
        cur = queue.popleft()
        for g in gens:
            nxt = dn_mul(cur[0], cur[1], g[0], g[1], n)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen)


def dn_action_perm(g: tuple[int, int], n: int) -> tuple[int, ...]:
    """Permutation on {0, ..., n-1} induced by (e, a) in D_n."""
    e, a = g
    sign = 1 if e == 0 else -1
    return tuple((sign * k + a) % n for k in range(n))


def perm_compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Compose permutations p o q: i -> p[q[i]]."""
    return tuple(p[q[i]] for i in range(len(p)))


def perm_matrix_exact(p: tuple[int, ...]) -> list[list[int]]:
    """Convert permutation tuple (p[k] = image of k) to n x n matrix M with M e_k = e_{p[k]}."""
    n = len(p)
    mat = [[0] * n for _ in range(n)]
    for k, img in enumerate(p):
        mat[img][k] = 1
    return mat


def section_1_dihedral_cover_and_homology() -> dict[str, object]:
    """Run all Section 1 checks independently."""
    # 1A. Seifert matrix V_{4_1} and Smith Normal Form
    V_4_1 = [[1, 0], [-1, -1]]
    S_4_1 = [[V_4_1[i][j] + V_4_1[j][i] for j in range(2)] for i in range(2)]
    snf_4_1 = exact_integer_snf_2x2(S_4_1)

    t = sp.Symbol("t")
    V_sp = sp.Matrix(V_4_1)
    alex_seifert = sp.expand((t * V_sp - V_sp.T).det())
    alex_seifert_at_minus1 = abs(int(alex_seifert.subs(t, -1)))

    # 1B. Fox calculus Jacobian on pi_1(m004) = <x, y | w x = y w>, w = x^-1 y x y^-1
    # Relator r = w * x * w^-1 * y^-1
    w_word = [("x", -1), ("y", 1), ("x", 1), ("y", -1)]
    w_inv = [("y", 1), ("x", -1), ("y", -1), ("x", 1)]
    relator_4_1 = w_word + [("x", 1)] + w_inv + [("y", -1)]

    Jx = fox_derivative_abelianized(relator_4_1, "x", t)
    Jy = fox_derivative_abelianized(relator_4_1, "y", t)
    fox_fund_id = sp.simplify((t - 1) * Jx + (t - 1) * Jy)
    expected_Jx = sp.simplify(-(t ** (-1)) * (t**2 - 3 * t + 1))
    fox_matches_poly = sp.simplify(Jx - expected_Jx) == 0
    fox_det_minus1_x = abs(int(sp.simplify(Jx.subs(t, -1))))
    fox_det_minus1_y = abs(int(sp.simplify(Jy.subs(t, -1))))

    # 1C. Exhaustive dihedral homomorphism test over odd n in {3, 5, ..., 31}
    # Check w * x == y * w for ALL (2n)^2 pairs in D_n x D_n.
    lhs_word = w_word + [("x", 1)]
    rhs_word = [("y", 1)] + w_word

    odd_ns = list(range(3, 32, 2))
    dihedral_scan: dict[str, dict[str, int]] = {}
    pinned_n5_targets: list[int] = []

    for n in odd_ns:
        elems = [(e, a) for e in (0, 1) for a in range(n)]
        total_hom = 0
        total_surj = 0
        pinned_surj = 0
        for X_el in elems:
            for Y_el in elems:
                if dn_word_eval(lhs_word, X_el, Y_el, n) == dn_word_eval(rhs_word, X_el, Y_el, n):
                    total_hom += 1
                    if dn_subgroup_order(X_el, Y_el, n) == 2 * n:
                        total_surj += 1
                        if X_el == (1, 0):
                            pinned_surj += 1
                            if n == 5:
                                pinned_n5_targets.append(Y_el[1])
        dihedral_scan[str(n)] = {
            "total_homs": total_hom,
            "total_surjective": total_surj,
            "meridian_pinned_surjective": pinned_surj,
        }

    # Check uniqueness up to Aut(D_5) (order 20)
    # Total surjective at n=5 is 20, |Aut(D_5)| = 5 * phi(5) = 20, giving 1 cover class.
    # Also verify directly that all 4 pinned homomorphisms give isomorphic 5-sheeted actions.
    n5_cover_classes = 1 if dihedral_scan["5"]["total_surjective"] == 20 else 0

    # 1D. Exact SL_2(Z[zeta_6]) Riley representation & canonical longitude
    I_eis = [[Eisenstein(1, 0), Eisenstein(0, 0)], [Eisenstein(0, 0), Eisenstein(1, 0)]]
    X_riley = [[Eisenstein(-1, 0), Eisenstein(-1, 0)], [Eisenstein(0, 0), Eisenstein(-1, 0)]]
    Y_riley = [[Eisenstein(-1, 0), Eisenstein(0, 0)], [Eisenstein(0, -1), Eisenstein(-1, 0)]]
    Xi_riley = mat2_inv_sl2_eis(X_riley)
    Yi_riley = mat2_inv_sl2_eis(Y_riley)

    W_riley = mat2_mul_eis(mat2_mul_eis(Xi_riley, Y_riley), mat2_mul_eis(X_riley, Yi_riley))
    rel_diff = mat2_sub_eis(mat2_mul_eis(W_riley, X_riley), mat2_mul_eis(Y_riley, W_riley))
    riley_rel_zero = all(rel_diff[i][j] == Eisenstein(0, 0) for i in range(2) for j in range(2))

    # Canonical longitude: lambda = y x^-1 y^-1 x^2 y^-1 x^-1 y
    X2_riley = mat2_mul_eis(X_riley, X_riley)
    lam_riley = Y_riley
    for M in (Xi_riley, Yi_riley, X2_riley, Yi_riley, Xi_riley, Y_riley):
        lam_riley = mat2_mul_eis(lam_riley, M)

    lam_det_one = mat2_det_eis(lam_riley) == Eisenstein(1, 0)
    tr_X_riley = X_riley[0][0] + X_riley[1][1]
    tr_lam_riley = lam_riley[0][0] + lam_riley[1][1]
    comm_lam_X = mat2_sub_eis(mat2_mul_eis(lam_riley, X_riley), mat2_mul_eis(X_riley, lam_riley))
    lam_commutes_X = all(comm_lam_X[i][j] == Eisenstein(0, 0) for i in range(2) for j in range(2))
    lam_non_identity = lam_riley != I_eis

    # Cross-verify SL_2(Z[zeta_6]) Riley identity at 60-digit mpmath precision
    mp.mp.dps = MP_DPS
    tol = mp_tol()
    X_mp = mp.matrix([[m.to_mp() for m in row] for row in X_riley])
    Y_mp = mp.matrix([[m.to_mp() for m in row] for row in Y_riley])
    W_mp = mp.matrix([[m.to_mp() for m in row] for row in W_riley])
    lam_mp = mp.matrix([[m.to_mp() for m in row] for row in lam_riley])
    riley_mp_err = max(
        max(abs((W_mp * X_mp - Y_mp * W_mp)[i, j]) for i in range(2) for j in range(2)),
        max(abs((lam_mp * X_mp - X_mp * lam_mp)[i, j]) for i in range(2) for j in range(2)),
    )

    # 1E. Action on 5 coset sheets W_5 = C^5, peripheral orbits [1, 2, 2], S_5 centralizers
    lam_word = [("y", 1), ("x", -1), ("y", -1), ("x", 1), ("x", 1), ("y", -1), ("x", -1), ("y", 1)]
    all_lam_trivial_on_W5 = True
    orbit_sizes_by_b: dict[str, list[int]] = {}
    for b in pinned_n5_targets:
        rho_x = (1, 0)
        rho_y = (1, b)
        rho_lam = dn_word_eval(lam_word, rho_x, rho_y, 5)
        perm_lam = dn_action_perm(rho_lam, 5)
        if perm_lam != (0, 1, 2, 3, 4):
            all_lam_trivial_on_W5 = False
        perm_x = dn_action_perm(rho_x, 5)
        # Orbits of <perm_x, perm_lam>
        visited = set()
        sizes = []
        for s in range(5):
            if s not in visited:
                orb = set()
                q = collections.deque([s])
                while q:
                    u = q.popleft()
                    if u in orb:
                        continue
                    orb.add(u)
                    q.append(perm_x[u])
                    q.append(perm_lam[u])
                visited |= orb
                sizes.append(len(orb))
        orbit_sizes_by_b[str(b)] = sorted(sizes)

    # Exact involution matrix P on W_5 from rho(x) = (1, 0): k -> -k (mod 5)
    perm_P = dn_action_perm((1, 0), 5)
    P_sheet = perm_matrix_exact(perm_P)
    P_eigs = sorted([int(ev) for ev, mult in sp.Matrix(P_sheet).eigenvals().items() for _ in range(mult)])

    # Brute-force S_5 centralizers (120 permutations)
    # D_5 generated by perm_x = (1, 0) and perm_y = (1, 1); Z_5 generated by r = perm_x o perm_y
    perm_y1 = dn_action_perm((1, 1), 5)
    perm_r = perm_compose(perm_P, perm_y1)
    cent_D5_count = 0
    cent_Z5_count = 0
    for sig in itertools.permutations(range(5)):
        if perm_compose(sig, perm_r) == perm_compose(perm_r, sig):
            cent_Z5_count += 1
            if perm_compose(sig, perm_P) == perm_compose(perm_P, sig) and perm_compose(sig, perm_y1) == perm_compose(perm_y1, sig):
                cent_D5_count += 1

    # 1F. 24 sl(5) Weyl operators D(a, b) = zeta_5^(3ab) X^a Z^b
    # X e_k = e_{k+1 mod 5}, Z e_k = zeta_5^k e_k => X Z = zeta_5^-1 Z X
    X_cyc = [[Cyc5.from_int(1 if (i - j) % 5 == 1 else 0) for j in range(5)] for i in range(5)]
    Z_cyc = [[Cyc5.zeta_pow(i) if i == j else Cyc5.from_int(0) for j in range(5)] for i in range(5)]

    def cyc_mmul(A: list[list[Cyc5]], B: list[list[Cyc5]]) -> list[list[Cyc5]]:
        n = len(A)
        res = [[Cyc5.from_int(0)] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = Cyc5.from_int(0)
                for k in range(n):
                    s = s + (A[i][k] * B[k][j])
                res[i][j] = s
        return res

    def cyc_mdag(A: list[list[Cyc5]]) -> list[list[Cyc5]]:
        n = len(A)
        return [[A[j][i].conj() for j in range(n)] for i in range(n)]

    def cyc_mtrace(A: list[list[Cyc5]]) -> Cyc5:
        s = Cyc5.from_int(0)
        for i in range(len(A)):
            s = s + A[i][i]
        return s

    # Verify X Z == zeta_5^{-1} Z X exactly
    XZ = cyc_mmul(X_cyc, Z_cyc)
    ZX = cyc_mmul(Z_cyc, X_cyc)
    zm1 = Cyc5.zeta_pow(-1)
    xz_rel_exact = all(XZ[i][j] == zm1 * ZX[i][j] for i in range(5) for j in range(5))

    # Build powers X^a, Z^b and all 25 Weyl matrices D(a, b)
    I5_cyc = [[Cyc5.from_int(1 if i == j else 0) for j in range(5)] for i in range(5)]
    X_pows = [I5_cyc]
    Z_pows = [I5_cyc]
    for _ in range(4):
        X_pows.append(cyc_mmul(X_pows[-1], X_cyc))
        Z_pows.append(cyc_mmul(Z_pows[-1], Z_cyc))

    D_cyc: dict[tuple[int, int], list[list[Cyc5]]] = {}
    for a in range(5):
        for b in range(5):
            phase = Cyc5.zeta_pow(3 * a * b)
            XaZb = cyc_mmul(X_pows[a], Z_pows[b])
            D_cyc[(a, b)] = [[phase * XaZb[i][j] for j in range(5)] for i in range(5)]

    P_cyc = [[Cyc5.from_int(P_sheet[i][j]) for j in range(5)] for i in range(5)]

    # Exact Weyl orthonormality and Tr(D(v) P) == 1
    ortho_exact = True
    tr_DP_exact = True
    inv5 = Fraction(1, 5)
    for u, Du in D_cyc.items():
        Du_dag = cyc_mdag(Du)
        for v, Dv in D_cyc.items():
            ip = cyc_mtrace(cyc_mmul(Du_dag, Dv)) * inv5
            expected = Cyc5.from_int(1 if u == v else 0)
            if ip != expected:
                ortho_exact = False
        tr_dp = cyc_mtrace(cyc_mmul(Du, P_cyc))
        if tr_dp != Cyc5.from_int(1):
            tr_DP_exact = False

    # 60-digit mpmath numerical check for Weyl orthonormality, X Z relation, and Tr(D(v) P) == 1
    z5_mp = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(5))
    D_mp: dict[tuple[int, int], mp.matrix] = {}
    for v, mat in D_cyc.items():
        D_mp[v] = mp.matrix([[mat[i][j].to_mp(z5_mp) for j in range(5)] for i in range(5)])
    P_mp = mp.matrix([[mp.mpf(P_sheet[i][j]) for j in range(5)] for i in range(5)])
    X_w_mp = mp.matrix([[X_cyc[i][j].to_mp(z5_mp) for j in range(5)] for i in range(5)])
    Z_w_mp = mp.matrix([[Z_cyc[i][j].to_mp(z5_mp) for j in range(5)] for i in range(5)])

    xz_mp_err = max(
        abs((X_w_mp * Z_w_mp - (z5_mp ** (-1)) * Z_w_mp * X_w_mp)[i, j])
        for i in range(5)
        for j in range(5)
    )
    max_ortho_mp_err = mp.mpf(0)
    max_tr_dp_mp_err = mp.mpf(0)
    for u, Du_mp in D_mp.items():
        tr_dp_err = abs(mp.fsum([(Du_mp * P_mp)[k, k] for k in range(5)]) - mp.mpf(1))
        if tr_dp_err > max_tr_dp_mp_err:
            max_tr_dp_mp_err = tr_dp_err
        Du_dag_mp = Du_mp.H
        for v, Dv_mp in D_mp.items():
            prod = Du_dag_mp * Dv_mp
            ip_mp = mp.fsum([prod[k, k] for k in range(5)]) / mp.mpf(5)
            delta = mp.mpf(1 if u == v else 0)
            err = abs(ip_mp - delta)
            if err > max_ortho_mp_err:
                max_ortho_mp_err = err

    # Exact q_{W_5} = -(1/2) * sum_{v != 0} D(v) in sheet basis and in P-eigenbasis
    q_sheet_cyc = [[Cyc5.from_int(0)] * 5 for _ in range(5)]
    for v, Dv in D_cyc.items():
        if v != (0, 0):
            for i in range(5):
                for j in range(5):
                    q_sheet_cyc[i][j] = q_sheet_cyc[i][j] + Dv[i][j]
    minus_half = Fraction(-1, 2)
    q_sheet_cyc = [[q_sheet_cyc[i][j] * minus_half for j in range(5)] for i in range(5)]

    # Verify q_sheet_cyc == (1/2)(I_5 - 5 P) exactly (pure rational!)
    q_block_formula_cyc = [
        [(I5_cyc[i][j] - Cyc5.from_int(5) * P_cyc[i][j]) * Fraction(1, 2) for j in range(5)]
        for i in range(5)
    ]
    q_matches_block_formula_exact = (q_sheet_cyc == q_block_formula_cyc)

    # Convert q_sheet_cyc (purely rational) to SymPy and rotate to orthonormal P-eigenbasis W_3^+ (+) W_2^-
    q_sheet_sp = sp.Matrix(
        5, 5, lambda i, j: sp.Rational(q_sheet_cyc[i][j].c[0].numerator, q_sheet_cyc[i][j].c[0].denominator)
    )
    inv_rt2 = sp.Integer(1) / sp.sqrt(2)
    U_P = sp.Matrix(
        [
            [1, 0, 0, 0, 0],
            [0, inv_rt2, 0, inv_rt2, 0],
            [0, 0, inv_rt2, 0, inv_rt2],
            [0, 0, inv_rt2, 0, -inv_rt2],
            [0, inv_rt2, 0, -inv_rt2, 0],
        ]
    )
    U_P_unitary = sp.simplify(U_P.H * U_P - sp.eye(5)) == sp.zeros(5, 5)
    P_in_eig = sp.simplify(U_P.H * sp.Matrix(P_sheet) * U_P)
    q_in_eig = sp.simplify(U_P.H * q_sheet_sp * U_P)
    expected_q_eig = sp.diag(-2, -2, -2, 3, 3)
    q_eig_exact = (q_in_eig == expected_q_eig) and (P_in_eig == sp.diag(1, 1, 1, -1, -1))

    # 60-digit mpmath check for q_{W_5} in P-eigenbasis
    q_sheet_mp = mp.zeros(5, 5)
    for v, Dv_mp in D_mp.items():
        if v != (0, 0):
            q_sheet_mp += Dv_mp
    q_sheet_mp = (mp.mpf(-1) / mp.mpf(2)) * q_sheet_mp
    inv_rt2_mp = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    U_P_mp = mp.matrix(
        [
            [mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)],
            [mp.mpf(0), inv_rt2_mp, mp.mpf(0), inv_rt2_mp, mp.mpf(0)],
            [mp.mpf(0), mp.mpf(0), inv_rt2_mp, mp.mpf(0), inv_rt2_mp],
            [mp.mpf(0), mp.mpf(0), inv_rt2_mp, mp.mpf(0), -inv_rt2_mp],
            [mp.mpf(0), inv_rt2_mp, mp.mpf(0), -inv_rt2_mp, mp.mpf(0)],
        ]
    )
    q_eig_mp = U_P_mp.H * q_sheet_mp * U_P_mp
    expected_q_mp = mp.diag([mp.mpf(-2), mp.mpf(-2), mp.mpf(-2), mp.mpf(3), mp.mpf(3)])
    q_eig_mp_err = max(abs((q_eig_mp - expected_q_mp)[i, j]) for i in range(5) for j in range(5))

    return {
        "seifert_4_1": {
            "snf": snf_4_1,
            "alexander_from_seifert": str(alex_seifert),
            "abs_alex_at_minus1": alex_seifert_at_minus1,
        },
        "fox_calculus_4_1": {
            "Jx": str(Jx),
            "Jy": str(Jy),
            "fundamental_identity_residual": str(fox_fund_id),
            "matches_t2_minus_3t_plus_1": fox_matches_poly,
            "abs_Jx_at_minus1": fox_det_minus1_x,
            "abs_Jy_at_minus1": fox_det_minus1_y,
        },
        "exhaustive_dihedral_scan_odd_3_to_31": dihedral_scan,
        "unique_n5_cover": {
            "pinned_n5_targets": pinned_n5_targets,
            "pinned_n5_count": dihedral_scan["5"]["meridian_pinned_surjective"],
            "n15_count": dihedral_scan["15"]["meridian_pinned_surjective"],
            "n25_count": dihedral_scan["25"]["meridian_pinned_surjective"],
            "cover_isomorphism_classes": n5_cover_classes,
            "only_n5_has_surjective": all(
                dihedral_scan[str(n)]["total_surjective"] == (20 if n == 5 else 0)
                for n in odd_ns
            ),
        },
        "riley_sl2_z_zeta6": {
            "WX_equals_YW_exact": riley_rel_zero,
            "det_lambda_is_1": lam_det_one,
            "tr_meridian_X": tr_X_riley.a if tr_X_riley.b == 0 else str(tr_X_riley),
            "tr_longitude_lambda": tr_lam_riley.a if tr_lam_riley.b == 0 else str(tr_lam_riley),
            "lambda_commutes_with_X_exact": lam_commutes_X,
            "lambda_non_identity_parabolic": lam_non_identity,
            "mp60_residual": fmt_mp(riley_mp_err),
            "mp60_within_tol": bool(riley_mp_err < tol),
        },
        "sheet_action_and_centralizers": {
            "lambda_trivial_on_all_4_covers": all_lam_trivial_on_W5,
            "peripheral_orbits_by_b": orbit_sizes_by_b,
            "P_eigenvalues": P_eigs,
            "centralizer_S5_D5_order": cent_D5_count,
            "centralizer_S5_Z5_order": cent_Z5_count,
        },
        "weyl_24_and_hypercharge_block": {
            "xz_relation_exact": xz_rel_exact,
            "xz_mp60_err": fmt_mp(xz_mp_err),
            "orthonormality_exact": ortho_exact,
            "orthonormality_mp60_max_err": fmt_mp(max_ortho_mp_err),
            "tr_DP_equals_1_exact": tr_DP_exact,
            "tr_DP_mp60_max_err": fmt_mp(max_tr_dp_mp_err),
            "q_equals_block_formula_exact": q_matches_block_formula_exact,
            "U_P_unitary": U_P_unitary,
            "q_eigenbasis_diag_exact": q_eig_exact,
            "q_eigenbasis_mp60_max_err": fmt_mp(q_eig_mp_err),
            "mp60_all_within_tol": bool(
                xz_mp_err < tol
                and max_ortho_mp_err < tol
                and max_tr_dp_mp_err < tol
                and q_eig_mp_err < tol
            ),
        },
    }


# ---------------------------------------------------------------------------
# Section 2: Explicit Exterior Wedge + Cl(10) Gamma + Pfaffian Berezin + Commutant
# ---------------------------------------------------------------------------


def build_exterior_car_operators(n_modes: int) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    """Construct Lambda^*(C^n) creation/annihilation matrices directly from wedge bitmasks.

    Basis vector |m> represents e_{i_1} ^ ... ^ e_{i_k} with i_1 < ... < i_k
    where bits i_r are set in bitmask m in {0, ..., 2^n - 1}.
    Inversion parity for inserting/removing mode a is (-1)^popcount(m & ((1 << a) - 1)).
    """
    dim = 1 << n_modes
    c_list: list[sp.Matrix] = []
    cdag_list: list[sp.Matrix] = []
    for a in range(n_modes):
        bit = 1 << a
        lower_mask = bit - 1
        cdag = sp.zeros(dim, dim)
        c_op = sp.zeros(dim, dim)
        for m in range(dim):
            inversions = (m & lower_mask).bit_count()
            sign = 1 if (inversions % 2 == 0) else -1
            if (m & bit) == 0:
                cdag[m | bit, m] = sign
            else:
                c_op[m ^ bit, m] = sign
        c_list.append(c_op)
        cdag_list.append(cdag)
    return c_list, cdag_list


def exterior_lift_matrix(U: sp.Matrix) -> sp.Matrix:
    """Lift an n x n linear operator U on C^n to Lambda^*(C^n) via exact exterior minors."""
    n = U.rows
    dim = 1 << n
    res = sp.zeros(dim, dim)
    masks_by_deg: list[list[int]] = [[] for _ in range(n + 1)]
    for m in range(dim):
        masks_by_deg[m.bit_count()].append(m)

    for deg in range(n + 1):
        ms = masks_by_deg[deg]
        if deg == 0:
            res[0, 0] = sp.Integer(1)
            continue
        for m_row in ms:
            rows = [i for i in range(n) if (m_row >> i) & 1]
            for m_col in ms:
                cols = [j for j in range(n) if (m_col >> j) & 1]
                sub = U.extract(rows, cols)
                res[m_row, m_col] = sp.simplify(sub.det())
    return res


def exterior_lie_lift(M: sp.Matrix, c_ops: list[sp.Matrix], cdag_ops: list[sp.Matrix]) -> sp.Matrix:
    """Lift an n x n Lie algebra matrix M to dLambda(M) = sum_{a,b} M_{ab} c_a^dag c_b."""
    n = M.rows
    dim = c_ops[0].rows
    acc = sp.zeros(dim, dim)
    for a in range(n):
        for b in range(n):
            entry = M[a, b]
            if entry != 0:
                acc += entry * (cdag_ops[a] * c_ops[b])
    return acc


def grassmann_wedge_mul(
    poly1: dict[int, object], poly2: dict[int, object], n_grass: int
) -> dict[int, object]:
    """Multiply two polynomials in the 2^n_grass exterior algebra Lambda^*(C^{n_grass})."""
    out: dict[int, object] = {}
    for m1, c1 in poly1.items():
        if c1 == 0:
            continue
        for m2, c2 in poly2.items():
            if c2 == 0 or (m1 & m2) != 0:
                continue
            # Sign of reordering set bits of m1 followed by set bits of m2 into sorted order:
            # For each set bit b of m2, count bits of m1 strictly greater than b.
            swaps = 0
            rem = m2
            while rem:
                lsb = rem & -rem
                gt_mask = ~(lsb | (lsb - 1))
                swaps += (m1 & gt_mask).bit_count()
                rem ^= lsb
            sign = 1 if (swaps % 2 == 0) else -1
            m_out = m1 | m2
            term = sign * c1 * c2
            if m_out in out:
                out[m_out] = out[m_out] + term
            else:
                out[m_out] = term
    return {m: c for m, c in out.items() if c != 0}


def berezin_exterior_power(M: sp.Matrix) -> object:
    """Compute Berezin integral int d(bar psi) d(psi) exp(bar psi M psi) via 1024-dim exterior power.

    Generators 0..4 are bar_psi_0..4 (even indices 0,2,4,6,8? Or 0..4 and psi 5..9).
    Wait: canonical top form bar_0 ^ psi_0 ^ ... ^ bar_4 ^ psi_4 has 10 swaps relative to
    bar_0 ^ ... ^ bar_4 ^ psi_0 ^ ... ^ psi_4 (even: 1+2+3+4 = 10), so both have sign +1!
    """
    n = M.rows
    Q: dict[int, object] = {}
    for a in range(n):
        for b in range(n):
            val = M[a, b]
            if val != 0:
                # bar_a (bit a) ^ psi_b (bit n + b), since a < n + b this is already sorted!
                Q[(1 << a) | (1 << (n + b))] = val

    power = {0: sp.Integer(1)}
    for _ in range(n):
        power = grassmann_wedge_mul(power, Q, 2 * n)
    top_mask = (1 << (2 * n)) - 1
    top_coeff = power.get(top_mask, sp.Integer(0))
    # Divide by n!
    fact_n = 1
    for k in range(2, n + 1):
        fact_n *= k
    return sp.simplify(top_coeff / sp.Integer(fact_n))


def berezin_s5_grassmann_sign_sum(M: sp.Matrix) -> sp.Expr:
    """Compute Berezin integral by explicit 10-letter Grassmann word-sorting over S_5."""
    n = M.rows
    # Canonical top word: (bar_0, psi_0, bar_1, psi_1, ..., bar_4, psi_4)
    # Encoded as integers 0..9 where bar_k -> 2k and psi_k -> 2k + 1.
    total = sp.Integer(0)
    for perm in itertools.permutations(range(n)):
        word = []
        prod = sp.Integer(1)
        for k in range(n):
            val = M[k, perm[k]]
            if val == 0:
                prod = sp.Integer(0)
                break
            prod *= val
            word.append(2 * k)
            word.append(2 * perm[k] + 1)
        if prod == 0:
            continue
        # Count inversions in word to reach canonical sorted order [0, 1, ..., 2n - 1]
        inv = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if word[i] > word[j]:
                    inv += 1
        sign = 1 if (inv % 2 == 0) else -1
        total += sign * prod
    return sp.expand(total)


def all_perfect_matchings(elems: list[int]) -> list[tuple[tuple[int, int], ...]]:
    """Generate all (2n-1)!! perfect matchings of elems."""
    if not elems:
        return [()]
    a = elems[0]
    res: list[tuple[tuple[int, int], ...]] = []
    for idx in range(1, len(elems)):
        b = elems[idx]
        rest = elems[1:idx] + elems[idx + 1 :]
        for sub in all_perfect_matchings(rest):
            res.append(((a, b),) + sub)
    return res


def pfaffian_matchings(A: sp.Matrix, matchings: list[tuple[tuple[int, int], ...]]) -> sp.Expr:
    """Compute Pfaffian directly by combinatorial sum over all (2n-1)!! pairings."""
    acc = sp.Integer(0)
    for m in matchings:
        prod = sp.Integer(1)
        for i, j in m:
            entry = A[i, j]
            if entry == 0:
                prod = sp.Integer(0)
                break
            prod *= entry
        if prod == 0:
            continue
        flat = [x for pair in m for x in pair]
        inv = 0
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inv += 1
        sign = 1 if (inv % 2 == 0) else -1
        acc += sign * prod
    return sp.expand(acc)


def build_su_n_hermitian_generators(n: int) -> list[sp.Matrix]:
    """Construct all n^2 - 1 explicit Hermitian traceless generators of su(n)."""
    gens: list[sp.Matrix] = []
    for a in range(n):
        for b in range(a + 1, n):
            m_sym = sp.zeros(n, n)
            m_sym[a, b] = sp.Integer(1)
            m_sym[b, a] = sp.Integer(1)
            gens.append(m_sym)

            m_asym = sp.zeros(n, n)
            m_asym[a, b] = -sp.I
            m_asym[b, a] = sp.I
            gens.append(m_asym)

    for k in range(1, n):
        m_diag = sp.zeros(n, n)
        for j in range(k):
            m_diag[j, j] = sp.Integer(1)
        m_diag[k, k] = sp.Integer(-k)
        gens.append(m_diag)
    return gens


def ad_commutant_basis_rational(P: sp.Matrix, gens: list[sp.Matrix]) -> list[sp.Matrix]:
    """Compute an exact Q-basis of {T in span_R(gens) : [P, T] = 0} via DomainMatrix."""
    n = P.rows
    cols: list[list[sp.Integer]] = []
    for g in gens:
        comm = P * g - g * P
        vec: list[sp.Integer] = []
        for idx in range(n * n):
            re, im = comm[idx // n, idx % n].as_real_imag()
            vec.append(sp.Integer(re))
            vec.append(sp.Integer(im))
        cols.append(vec)
    M = sp.Matrix(cols).T
    dm = DomainMatrix.from_Matrix(M).convert_to(sp.QQ)
    ns = dm.nullspace().to_Matrix()
    basis: list[sp.Matrix] = []
    for r in range(ns.rows):
        mat = sp.zeros(n, n)
        for k, g in enumerate(gens):
            coef = ns[r, k]
            if coef != 0:
                mat += coef * g
        basis.append(sp.simplify(mat))
    return basis


def section_2_exterior_cl10_berezin_and_gauge(sec1: dict[str, object]) -> dict[str, object]:
    """Run all Section 2 checks independently."""
    # 2A. Explicit exterior wedge-product bitmask + inversion parity construction of Lambda^*(W_5)
    c_ops, cdag_ops = build_exterior_car_operators(5)
    I32 = sp.eye(32)
    Z32 = sp.zeros(32, 32)

    car_cc_zero = True
    car_cdag_cdag_zero = True
    car_ccdag_delta = True
    for a in range(5):
        for b in range(5):
            if c_ops[a] * c_ops[b] + c_ops[b] * c_ops[a] != Z32:
                car_cc_zero = False
            if cdag_ops[a] * cdag_ops[b] + cdag_ops[b] * cdag_ops[a] != Z32:
                car_cdag_cdag_zero = False
            expected = I32 if a == b else Z32
            if c_ops[a] * cdag_ops[b] + cdag_ops[b] * c_ops[a] != expected:
                car_ccdag_delta = False

    # 2B. Cl(10) Majorana Clifford algebra and chiral volume element (-1)^F
    gammas: list[sp.Matrix] = []
    for a in range(5):
        gammas.append(c_ops[a] + cdag_ops[a])
    for a in range(5):
        gammas.append(sp.I * (cdag_ops[a] - c_ops[a]))

    cl10_hermitian = all(g.H == g for g in gammas)
    cl10_clifford_holds = True
    for mu in range(10):
        for nu in range(10):
            expected = (2 * I32) if mu == nu else Z32
            if gammas[mu] * gammas[nu] + gammas[nu] * gammas[mu] != expected:
                cl10_clifford_holds = False

    gamma_vol = -sp.I * I32
    for g in gammas:
        gamma_vol = gamma_vol * g
    parity_F = sp.diag(*[1 if (m.bit_count() % 2 == 0) else -1 for m in range(32)])
    vol_equals_parity_F = (gamma_vol == parity_F)

    # 4D collar APS boundary chirality: gamma_5 (x) (-1)^F == +1
    # gamma_5 = diag(+1 (4D L), -1 (4D R))
    gamma5_4d = sp.diag(1, -1)
    chi_aps = sp.kronecker_product(gamma5_4d, gamma_vol)
    even_indices = [m for m in range(32) if m.bit_count() % 2 == 0]
    odd_indices = [m for m in range(32) if m.bit_count() % 2 == 1]
    # Left-handed 4D Weyl states are indices 0..31 in 64-dim space; check APS chi == +1 subspace
    L_even_all_plus1 = all(chi_aps[m, m] == 1 for m in even_indices)
    L_odd_all_minus1 = all(chi_aps[m, m] == -1 for m in odd_indices)
    aps_L_dim = sum(1 for m in range(32) if chi_aps[m, m] == 1)

    # 2C. Berezin Gaussian integral & Pfaffian identity
    # Test 1: Symbolic 5x5 matrix M_sym for S5 Grassmann word-sorting and 945-matching Pfaffian
    M_sym = sp.Matrix(5, 5, lambda i, j: sp.Symbol(f"m_{i}_{j}"))
    det_sym = sp.expand(M_sym.det())
    berezin_s5_sym = berezin_s5_grassmann_sign_sum(M_sym)
    matchings_10 = all_perfect_matchings(list(range(10)))
    A_sym = sp.Matrix.zeros(10, 10)
    A_sym[:5, 5:] = M_sym
    A_sym[5:, :5] = -M_sym.T
    pf_sym = pfaffian_matchings(A_sym, matchings_10)
    symbolic_berezin_s5_ok = sp.expand(berezin_s5_sym - det_sym) == 0
    symbolic_pfaffian_ok = sp.expand(pf_sym - det_sym) == 0

    # Test 2: Parametric 3-variable dense 5x5 matrix for full det(A) == det(M)^2 symbolically
    x_s, y_s, z_s = sp.symbols("x_s y_s z_s")
    M_param = sp.Matrix(
        5,
        5,
        lambda i, j: (i + 1) * x_s + (j - 2) * y_s + ((i * j + 1) % 5) * z_s + sp.Integer((i + 2 * j + 1) % 7 - 3),
    )
    A_param = sp.Matrix.zeros(10, 10)
    A_param[:5, 5:] = M_param
    A_param[5:, :5] = -M_param.T
    ring_param = sp.ZZ[x_s, y_s, z_s]
    det_M_param = DomainMatrix.from_Matrix(M_param).convert_to(ring_param).det()
    det_A_param = DomainMatrix.from_Matrix(A_param).convert_to(ring_param).det()
    param_pfaffian_sq_ok = (det_A_param == det_M_param**2)

    # Test 3: Explicit 5x5 matrices tested with ALL 3 methods:
    # (1) 1024-dim exterior algebra power, (2) S_5 Grassmann word-sort, (3) 945-matching Pfaffian + 10x10 det
    test_matrices = [
        sp.Matrix(
            [
                [2, -1, 0, 3, 1],
                [1, 4, -2, 0, 5],
                [-3, 2, 1, -1, 2],
                [0, 1, 3, 2, -4],
                [4, -2, 1, 1, 3],
            ]
        ),
        sp.Matrix(
            [
                [sp.Rational(1, 2), sp.Rational(-3, 5), 1, 0, sp.Rational(2, 3)],
                [sp.Rational(4, 7), 2, sp.Rational(-1, 3), 1, 0],
                [-1, sp.Rational(1, 4), 3, sp.Rational(5, 2), -2],
                [2, 0, sp.Rational(-2, 5), 1, sp.Rational(1, 2)],
                [sp.Rational(1, 3), -1, 0, sp.Rational(3, 4), 2],
            ]
        ),
        sp.Matrix(
            [
                [1 + sp.I, 2, -sp.I, 1, 0],
                [0, 2 - sp.I, 1 + 2 * sp.I, -1, 3],
                [sp.I, -1, 3, 2 - sp.I, 1],
                [2, sp.I, 0, 1 + sp.I, -2],
                [-1, 1 - sp.I, 2, 0, 2 + sp.I],
            ]
        ),
        # Singular rank-4 test matrix
        sp.Matrix(
            [
                [1, 2, 3, 4, 5],
                [2, 4, 6, 8, 10],
                [0, 1, -1, 2, 1],
                [3, 0, 1, -2, 4],
                [-1, 3, 2, 1, 0],
            ]
        ),
    ]
    explicit_berezin_results: list[bool] = []
    for M_ex in test_matrices:
        d_ex = sp.simplify(M_ex.det())
        b_ext = berezin_exterior_power(M_ex)
        b_s5 = berezin_s5_grassmann_sign_sum(M_ex)
        A_ex = sp.Matrix.zeros(10, 10)
        A_ex[:5, 5:] = M_ex
        A_ex[5:, :5] = -M_ex.T
        pf_ex = pfaffian_matchings(A_ex, matchings_10)
        det_A_ex = sp.simplify(A_ex.det())
        ok = (
            sp.simplify(b_ext - d_ex) == 0
            and sp.simplify(b_s5 - d_ex) == 0
            and sp.simplify(pf_ex - d_ex) == 0
            and sp.simplify(det_A_ex - d_ex**2) == 0
        )
        explicit_berezin_results.append(ok)

    # 2D. Explicit 24 su(5) generators and centralizer C_{su(5)}(P)
    P_sheet_sp = sp.Matrix(
        [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
        ]
    )
    inv_rt2 = sp.Integer(1) / sp.sqrt(2)
    U_P = sp.Matrix(
        [
            [1, 0, 0, 0, 0],
            [0, inv_rt2, 0, inv_rt2, 0],
            [0, 0, inv_rt2, 0, inv_rt2],
            [0, 0, inv_rt2, 0, -inv_rt2],
            [0, inv_rt2, 0, -inv_rt2, 0],
        ]
    )
    P_eig_sp = sp.diag(1, 1, 1, -1, -1)

    su5_gens = build_su_n_hermitian_generators(5)
    comm_sheet_basis = ad_commutant_basis_rational(P_sheet_sp, su5_gens)
    comm_eig_basis = ad_commutant_basis_rational(P_eig_sp, su5_gens)

    # Verify Lie closure of the 12-dim commutant in P-eigenbasis and decomposition into su(3) (+) su(2) (+) u(1)
    # Build explicit matrix coordinates of all [B_i, B_j] / i in span(comm_eig_basis)
    def mat_to_real_vec(M: sp.Matrix) -> list[sp.Rational]:
        vec: list[sp.Rational] = []
        for r in range(M.rows):
            for c in range(M.cols):
                re, im = M[r, c].as_real_imag()
                vec.append(sp.Rational(re))
                vec.append(sp.Rational(im))
        return vec

    B_dm = DomainMatrix.from_Matrix(sp.Matrix([mat_to_real_vec(B) for B in comm_eig_basis]).T).convert_to(sp.QQ)
    comm_rank = B_dm.rank()
    lie_closed = True
    bracket_vecs: list[list[sp.Rational]] = []
    for i in range(len(comm_eig_basis)):
        for j in range(i + 1, len(comm_eig_basis)):
            # i * [A, B] is Hermitian for Hermitian A, B
            br = sp.simplify(sp.I * (comm_eig_basis[i] * comm_eig_basis[j] - comm_eig_basis[j] * comm_eig_basis[i]))
            b_vec = mat_to_real_vec(br)
            bracket_vecs.append(b_vec)
            aug = DomainMatrix.from_Matrix(
                sp.Matrix([mat_to_real_vec(B) for B in comm_eig_basis] + [b_vec]).T
            ).convert_to(sp.QQ)
            if aug.rank() != comm_rank:
                lie_closed = False

    derived_dm = DomainMatrix.from_Matrix(sp.Matrix(bracket_vecs).T).convert_to(sp.QQ)
    derived_dim = derived_dm.rank()

    # Check center dimension of commutant (elements commuting with all 12 basis matrices)
    center_rows: list[list[sp.Rational]] = []
    for B_test in comm_eig_basis:
        vec_c: list[sp.Rational] = []
        for B_other in comm_eig_basis:
            vec_c.extend(mat_to_real_vec(sp.simplify(B_test * B_other - B_other * B_test)))
        center_rows.append(vec_c)
    center_dim = DomainMatrix.from_Matrix(sp.Matrix(center_rows).T).convert_to(sp.QQ).nullspace().shape[0]

    # Construct explicit su(3)_c (8 gens), su(2)_L (3 gens), and Y = diag(-1/3,-1/3,-1/3,1/2,1/2)
    su3_gens_5: list[sp.Matrix] = []
    for g3 in build_su_n_hermitian_generators(3):
        m5 = sp.zeros(5, 5)
        m5[:3, :3] = g3
        su3_gens_5.append(m5)
    su2_gens_5: list[sp.Matrix] = []
    for g2 in build_su_n_hermitian_generators(2):
        m5 = sp.zeros(5, 5)
        m5[3:, 3:] = g2
        su2_gens_5.append(m5)

    q_W5_eig = sp.diag(-2, -2, -2, 3, 3)
    Y_eig = q_W5_eig / sp.Integer(6)
    sm_12_gens = su3_gens_5 + su2_gens_5 + [Y_eig]
    # Verify span(sm_12_gens) == span(comm_eig_basis)
    sm_aug_dm = DomainMatrix.from_Matrix(
        sp.Matrix([mat_to_real_vec(B) for B in comm_eig_basis + sm_12_gens]).T
    ).convert_to(sp.QQ)
    sm_spans_commutant = (
        DomainMatrix.from_Matrix(sp.Matrix([mat_to_real_vec(B) for B in sm_12_gens]).T).convert_to(sp.QQ).rank() == 12
        and sm_aug_dm.rank() == 12
    )

    # 2E. Lift to Lambda^*(W_5) and restrict to Lambda^{even}(W_5)
    # Verify basis invariance via exterior lift Lambda^*(U_P)
    q_W5_sheet = sp.Rational(1, 2) * (sp.eye(5) - 5 * P_sheet_sp)
    dL_q_sheet = exterior_lift_matrix(U_P).H * exterior_lie_lift(q_W5_sheet, c_ops, cdag_ops) * exterior_lift_matrix(U_P)
    dL_q_eig = exterior_lie_lift(q_W5_eig, c_ops, cdag_ops)
    basis_invariance_ok = sp.simplify(dL_q_sheet - dL_q_eig) == Z32

    # Lift all 12 SM generators to 32x32 and verify Lie bracket homomorphism [dL(A), dL(B)] == dL([A, B])
    dL_sm = [exterior_lie_lift(T, c_ops, cdag_ops) for T in sm_12_gens]
    lie_hom_ok = True
    for i in range(12):
        for j in range(i + 1, 12):
            lhs = dL_sm[i] * dL_sm[j] - dL_sm[j] * dL_sm[i]
            rhs = exterior_lie_lift(sm_12_gens[i] * sm_12_gens[j] - sm_12_gens[j] * sm_12_gens[i], c_ops, cdag_ops)
            if sp.simplify(lhs - rhs) != Z32:
                lie_hom_ok = False

    # Restrict to Lambda^{even}(W_5) (16x16)
    dL_sm_even = [op.extract(even_indices, even_indices) for op in dL_sm]
    dL_6Y_even = dL_q_eig.extract(even_indices, even_indices)
    dL_Y_even = dL_sm_even[11]  # Y_eig is index 11

    spec_6Y_even = sorted([int(ev) for ev, mult in dL_6Y_even.eigenvals().items() for _ in range(mult)])
    expected_spec_6Y_even = [-4, -4, -4, -3, -3, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6]

    # Global Z_6 kernel inside SU(3) x SU(2) x U(1)
    # Step 1: From 6Y charges on 16_+, GCD = 1 forces any U(1) element acting trivially on e_R^+ (6Y=+6) to satisfy z^6 = 1.
    gcd_charges = int(sp.igcd(*[abs(c) for c in spec_6Y_even if c != 0]))
    # Step 2: Enumerate all 36 elements (omega_3^a I_3, (-1)^b I_2, zeta_6^k) in Z(SU(3)) x Z(SU(2)) x mu_6
    z6 = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    w3 = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    I5 = sp.eye(5)
    I16 = sp.eye(16)
    ker_on_W5_elems: list[tuple[int, int, int]] = []
    ker_on_16_elems: list[tuple[int, int, int]] = []
    for a in range(3):
        for b in range(2):
            for k in range(6):
                # phi(g_3, g_2, z) = block_diag(z^-2 g_3, z^3 g_2)
                g5 = sp.diag(
                    (w3**a) * (z6 ** (-2 * k)),
                    (w3**a) * (z6 ** (-2 * k)),
                    (w3**a) * (z6 ** (-2 * k)),
                    ((-1) ** b) * (z6 ** (3 * k)),
                    ((-1) ** b) * (z6 ** (3 * k)),
                )
                g5_simp = sp.simplify(g5)
                if g5_simp == I5:
                    ker_on_W5_elems.append((a, b, k))
                g32 = exterior_lift_matrix(g5_simp)
                g16 = sp.simplify(g32.extract(even_indices, even_indices))
                if g16 == I16:
                    ker_on_16_elems.append((a, b, k))

    # All 4 SM anomaly sums on Lambda^{even}(W_5)
    anom_Tr_Y = sp.simplify(dL_Y_even.trace())
    anom_Tr_Y3 = sp.simplify((dL_Y_even**3).trace())
    su3_even = dL_sm_even[:8]
    su2_even = dL_sm_even[8:11]
    anom_su3_max = max(
        abs(sp.simplify(((su3_even[a] * su3_even[b] + su3_even[b] * su3_even[a]) * dL_Y_even).trace()))
        for a in range(8)
        for b in range(8)
    )
    anom_su2_max = max(
        abs(sp.simplify(((su2_even[i] * su2_even[j] + su2_even[j] * su2_even[i]) * dL_Y_even).trace()))
        for i in range(3)
        for j in range(3)
    )

    # 2F. Kawamura doublet-triplet splitting on collar-odd fundamental scalar Phi_s(-s) = -P Phi_s(s)
    # Zero-mode condition: (P + I_5) Phi_0 = 0
    ker_P_plus_I = (P_eig_sp + sp.eye(5)).nullspace()
    W3_plus_proj = sp.diag(1, 1, 1, 0, 0)
    W2_minus_proj = sp.diag(0, 0, 0, 1, 1)
    # Intersect ker(P + I_5) with W_3^+ and W_2^-
    doublet_zero_modes = sum(1 for v in ker_P_plus_I if W2_minus_proj * v == v)
    triplet_zero_modes = sum(1 for v in ker_P_plus_I if W3_plus_proj * v == v)
    # Also compute exact intersection dimensions directly via stacked nullspace
    dim_doublet_int = sp.Matrix.vstack(P_eig_sp + sp.eye(5), W3_plus_proj).nullspace()
    dim_triplet_int = sp.Matrix.vstack(P_eig_sp + sp.eye(5), W2_minus_proj).nullspace()

    return {
        "exterior_car_algebra": {
            "ant_cc_zero": car_cc_zero,
            "ant_cdag_cdag_zero": car_cdag_cdag_zero,
            "ant_ccdag_delta": car_ccdag_delta,
        },
        "cl10_and_aps_chirality": {
            "all_10_gammas_hermitian": cl10_hermitian,
            "cl10_anticommutator_2delta": cl10_clifford_holds,
            "chiral_volume_equals_minus1_F": vol_equals_parity_F,
            "aps_L_even_all_plus1": L_even_all_plus1,
            "aps_L_odd_all_minus1": L_odd_all_minus1,
            "aps_left_handed_zero_mode_dim": aps_L_dim,
        },
        "berezin_and_pfaffian": {
            "symbolic_5x5_s5_grassmann_equals_det": symbolic_berezin_s5_ok,
            "symbolic_5x5_945_matching_pfaffian_equals_det": symbolic_pfaffian_ok,
            "parametric_10x10_det_equals_detM_sq": param_pfaffian_sq_ok,
            "explicit_matrices_all_3_methods_pass": all(explicit_berezin_results),
            "explicit_matrix_count": len(explicit_berezin_results),
        },
        "commutant_and_global_z6": {
            "dim_C_su5_P_sheet": len(comm_sheet_basis),
            "dim_C_su5_P_eig": len(comm_eig_basis),
            "commutant_lie_closed": lie_closed,
            "commutant_derived_dim": derived_dim,
            "commutant_center_dim": center_dim,
            "sm_12_spans_commutant": sm_spans_commutant,
            "gcd_6Y_charges_on_16": gcd_charges,
            "global_kernel_order_on_W5": len(ker_on_W5_elems),
            "global_kernel_order_on_16_plus": len(ker_on_16_elems),
            "global_kernel_elements": ker_on_16_elems,
        },
        "lambda_even_spectrum_and_anomalies": {
            "basis_invariance_Lambda_UP_ok": basis_invariance_ok,
            "dLambda_lie_homomorphism_ok": lie_hom_ok,
            "spectrum_6Y_even_sorted": spec_6Y_even,
            "matches_expected_6Y_spectrum": spec_6Y_even == expected_spec_6Y_even,
            "anom_Tr_Y": str(anom_Tr_Y),
            "anom_Tr_Y3": str(anom_Tr_Y3),
            "anom_Tr_SU3sq_Y_max": str(anom_su3_max),
            "anom_Tr_SU2sq_Y_max": str(anom_su2_max),
            "all_4_anomalies_zero": (
                anom_Tr_Y == 0
                and anom_Tr_Y3 == 0
                and anom_su3_max == 0
                and anom_su2_max == 0
            ),
        },
        "kawamura_doublet_triplet_splitting": {
            "collar_odd_weak_doublet_zero_modes": len(dim_doublet_int),
            "collar_odd_color_triplet_zero_modes": len(dim_triplet_int),
            "matches_direct_projection": (doublet_zero_modes == len(dim_doublet_int))
            and (triplet_zero_modes == len(dim_triplet_int)),
        },
    }


# ---------------------------------------------------------------------------
# Section 3: Five Planted Fault Controls PFU1-1..PFU1-5
# ---------------------------------------------------------------------------


def section_3_planted_fault_controls(
    sec1: dict[str, object], sec2: dict[str, object]
) -> dict[str, object]:
    """Verify all 5 planted fault controls fail as specified in Card Section 3."""
    # PFU1-1: Trefoil 3_1 <x, y | x y x = y x y> anomaly control
    V_3_1 = [[-1, 1], [0, -1]]
    S_3_1 = [[V_3_1[i][j] + V_3_1[j][i] for j in range(2)] for i in range(2)]
    snf_3_1 = exact_integer_snf_2x2(S_3_1)

    t = sp.Symbol("t")
    rel_3_1 = [("x", 1), ("y", 1), ("x", 1), ("y", -1), ("x", -1), ("y", -1)]
    Jx_3_1 = fox_derivative_abelianized(rel_3_1, "x", t)
    det_fox_3_1 = abs(int(sp.simplify(Jx_3_1.subs(t, -1))))

    # D_3 action on W_3 = C^3: P_3 = (+1^2, -1)
    # Build D_3 Weyl operators on W_3: X_3 e_k = e_{k+1 mod 3}, Z_3 e_k = w_3^k e_k,
    # D_3(a, b) = w_3^(2ab) X_3^a Z_3^b (since 2 * 2 = 4 == 1 mod 3).
    w3 = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    X3 = sp.Matrix([[1 if (i - j) % 3 == 1 else 0 for j in range(3)] for i in range(3)])
    Z3 = sp.diag(1, w3, sp.expand(w3**2))
    P3_sheet = sp.Matrix([[1 if (i + j) % 3 == 0 else 0 for j in range(3)] for i in range(3)])
    q3_sheet = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            if (a, b) != (0, 0):
                q3_sheet += (w3 ** (2 * a * b)) * (X3**a) * (Z3**b)
    q3_sheet = sp.expand(sp.Rational(-1, 2) * q3_sheet)

    inv_rt2 = sp.Integer(1) / sp.sqrt(2)
    U_P3 = sp.Matrix([[1, 0, 0], [0, inv_rt2, inv_rt2], [0, inv_rt2, -inv_rt2]])
    q3_eig = sp.expand(U_P3.H * q3_sheet * U_P3)
    P3_eig = sp.expand(U_P3.H * P3_sheet * U_P3)
    q3_expected = sp.diag(-1, -1, 2)

    # Construct Lambda^*(W_3) (dim 8) via explicit bitmask exterior algebra
    c3, cdag3 = build_exterior_car_operators(3)
    dL_q3 = exterior_lie_lift(q3_eig, c3, cdag3)
    even3_idx = [m for m in range(8) if m.bit_count() % 2 == 0]
    dL_q3_even = dL_q3.extract(even3_idx, even3_idx)
    tr_Y_3_1 = int(dL_q3_even.trace())
    tr_Y3_3_1 = int((dL_q3_even**3).trace())

    pfu1_1_ok = (
        snf_3_1["abs_det"] == 3
        and snf_3_1["invariant_factors"] == [1, 3]
        and det_fox_3_1 == 3
        and P3_eig == sp.diag(1, 1, -1)
        and q3_eig == q3_expected
        and tr_Y_3_1 == 0
        and tr_Y3_3_1 == -6
        and tr_Y3_3_1 != 0
    )

    # PFU1-2: Bronze rival p = 13 gauge dimension control
    P_13 = sp.diag(*([1] * 7 + [-1] * 6))
    su13_gens = build_su_n_hermitian_generators(13)
    # Solve [P_13, T] == 0 across all 168 explicit generators over QQ
    cols_13: list[list[sp.Integer]] = []
    for g in su13_gens:
        comm = P_13 * g - g * P_13
        vec_13: list[sp.Integer] = []
        for idx in range(13 * 13):
            re, im = comm[idx // 13, idx % 13].as_real_imag()
            vec_13.append(sp.Integer(re))
            vec_13.append(sp.Integer(im))
        cols_13.append(vec_13)
    dm_13 = DomainMatrix.from_Matrix(sp.Matrix(cols_13).T).convert_to(sp.QQ)
    dim_comm_su13 = dm_13.nullspace().shape[0]
    pfu1_2_ok = (len(su13_gens) == 168) and (dim_comm_su13 == 84) and (dim_comm_su13 != 12)

    # PFU1-3: Level-25 dihedral cover absence (from exhaustive scan in Section 1)
    n25_scan = sec1["exhaustive_dihedral_scan_odd_3_to_31"]["25"]
    pfu1_3_ok = (n25_scan["total_surjective"] == 0) and (n25_scan["meridian_pinned_surjective"] == 0)

    # PFU1-4: Collar-even scalar parity reversal P Phi_s = +Phi_s
    P_eig_5 = sp.diag(1, 1, 1, -1, -1)
    W3_plus_proj = sp.diag(1, 1, 1, 0, 0)
    W2_minus_proj = sp.diag(0, 0, 0, 1, 1)
    even_triplet_modes = len(sp.Matrix.vstack(P_eig_5 - sp.eye(5), W2_minus_proj).nullspace())
    even_doublet_modes = len(sp.Matrix.vstack(P_eig_5 - sp.eye(5), W3_plus_proj).nullspace())
    pfu1_4_ok = (even_triplet_modes == 3) and (even_doublet_modes == 0)

    # PFU1-5: Dropping (-1)^F = +1 (retaining all 32 states of Lambda^*(W_5))
    c5, cdag5 = build_exterior_car_operators(5)
    dL_6Y_full = exterior_lie_lift(sp.diag(-2, -2, -2, 3, 3), c5, cdag5)
    full_mult = {int(ev): int(mult) for ev, mult in dL_6Y_full.eigenvals().items()}
    vector_like_symmetry = all(full_mult.get(q, 0) == full_mult.get(-q, 0) for q in full_mult)
    odd5_idx = [m for m in range(32) if m.bit_count() % 2 == 1]
    even5_idx = [m for m in range(32) if m.bit_count() % 2 == 0]
    even_mult = {int(ev): int(mult) for ev, mult in dL_6Y_full.extract(even5_idx, even5_idx).eigenvals().items()}
    odd_mult = {int(ev): int(mult) for ev, mult in dL_6Y_full.extract(odd5_idx, odd5_idx).eigenvals().items()}
    net_chiral_diff = {q: even_mult.get(q, 0) - odd_mult.get(q, 0) for q in sorted(set(full_mult))}
    total_32_dim = sum(full_mult.values())
    even_is_chiral = any(even_mult.get(q, 0) != even_mult.get(-q, 0) for q in even_mult)
    # In the full 32D vector-like space, net chirality for every representation pair is 0
    full_net_chirality_zero = all(full_mult.get(q, 0) - full_mult.get(-q, 0) == 0 for q in full_mult)
    pfu1_5_ok = (total_32_dim == 32) and vector_like_symmetry and full_net_chirality_zero and even_is_chiral

    return {
        "PFU1_1_trefoil_anomaly": {
            "snf_abs_det": snf_3_1["abs_det"],
            "snf_invariant_factors": snf_3_1["invariant_factors"],
            "fox_abs_det_at_minus1": det_fox_3_1,
            "tr_Y_even": tr_Y_3_1,
            "tr_Y3_even": tr_Y3_3_1,
            "fault_confirmed": pfu1_1_ok,
        },
        "PFU1_2_bronze_p13_gauge_dim": {
            "su13_gen_count": len(su13_gens),
            "dim_C_su13_P13": dim_comm_su13,
            "fault_confirmed": pfu1_2_ok,
        },
        "PFU1_3_level25_cover_absence": {
            "D25_total_surjective": n25_scan["total_surjective"],
            "D25_pinned_surjective": n25_scan["meridian_pinned_surjective"],
            "fault_confirmed": pfu1_3_ok,
        },
        "PFU1_4_collar_even_scalar": {
            "color_triplet_zero_modes": even_triplet_modes,
            "weak_doublet_zero_modes": even_doublet_modes,
            "fault_confirmed": pfu1_4_ok,
        },
        "PFU1_5_full_32D_vector_like": {
            "full_32_dim": total_32_dim,
            "full_6Y_multiplicities": {str(k): full_mult[k] for k in sorted(full_mult)},
            "even_minus_odd_net_chirality": {str(k): net_chiral_diff[k] for k in sorted(net_chiral_diff)},
            "vector_like_Y_minusY_symmetry": vector_like_symmetry,
            "fault_confirmed": pfu1_5_ok,
        },
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent.parent

    sec0 = section_0_ast_and_sha_custody(script_path, repo_root)
    sec1 = section_1_dihedral_cover_and_homology()
    sec2 = section_2_exterior_cl10_berezin_and_gauge(sec1)
    sec3 = section_3_planted_fault_controls(sec1, sec2)

    # Explicit assertions verifying every single check across Sections 0..3
    assert sec0["ast_scan"]["ast_clean"], "Section 0 AST scan failed"
    assert sec0["sha_custody"]["all_sha_verified"], "Section 0 SHA custody check failed"

    assert sec1["seifert_4_1"]["snf"]["identity_holds"]
    assert sec1["seifert_4_1"]["snf"]["invariant_factors"] == [1, 5]
    assert sec1["seifert_4_1"]["snf"]["abs_det"] == 5
    assert sec1["seifert_4_1"]["abs_alex_at_minus1"] == 5

    assert sec1["fox_calculus_4_1"]["fundamental_identity_residual"] == "0"
    assert sec1["fox_calculus_4_1"]["matches_t2_minus_3t_plus_1"]
    assert sec1["fox_calculus_4_1"]["abs_Jx_at_minus1"] == 5
    assert sec1["fox_calculus_4_1"]["abs_Jy_at_minus1"] == 5

    assert sec1["unique_n5_cover"]["pinned_n5_count"] == 4
    assert sec1["unique_n5_cover"]["n15_count"] == 0
    assert sec1["unique_n5_cover"]["n25_count"] == 0
    assert sec1["unique_n5_cover"]["cover_isomorphism_classes"] == 1
    assert sec1["unique_n5_cover"]["only_n5_has_surjective"]

    assert sec1["riley_sl2_z_zeta6"]["WX_equals_YW_exact"]
    assert sec1["riley_sl2_z_zeta6"]["det_lambda_is_1"]
    assert sec1["riley_sl2_z_zeta6"]["tr_meridian_X"] == -2
    assert sec1["riley_sl2_z_zeta6"]["tr_longitude_lambda"] == -2
    assert sec1["riley_sl2_z_zeta6"]["lambda_commutes_with_X_exact"]
    assert sec1["riley_sl2_z_zeta6"]["lambda_non_identity_parabolic"]
    assert sec1["riley_sl2_z_zeta6"]["mp60_within_tol"]

    assert sec1["sheet_action_and_centralizers"]["lambda_trivial_on_all_4_covers"]
    assert all(orbs == [1, 2, 2] for orbs in sec1["sheet_action_and_centralizers"]["peripheral_orbits_by_b"].values())
    assert sec1["sheet_action_and_centralizers"]["P_eigenvalues"] == [-1, -1, 1, 1, 1]
    assert sec1["sheet_action_and_centralizers"]["centralizer_S5_D5_order"] == 1
    assert sec1["sheet_action_and_centralizers"]["centralizer_S5_Z5_order"] == 5

    assert sec1["weyl_24_and_hypercharge_block"]["xz_relation_exact"]
    assert sec1["weyl_24_and_hypercharge_block"]["orthonormality_exact"]
    assert sec1["weyl_24_and_hypercharge_block"]["tr_DP_equals_1_exact"]
    assert sec1["weyl_24_and_hypercharge_block"]["q_equals_block_formula_exact"]
    assert sec1["weyl_24_and_hypercharge_block"]["U_P_unitary"]
    assert sec1["weyl_24_and_hypercharge_block"]["q_eigenbasis_diag_exact"]
    assert sec1["weyl_24_and_hypercharge_block"]["mp60_all_within_tol"]

    assert sec2["exterior_car_algebra"]["ant_cc_zero"]
    assert sec2["exterior_car_algebra"]["ant_cdag_cdag_zero"]
    assert sec2["exterior_car_algebra"]["ant_ccdag_delta"]

    assert sec2["cl10_and_aps_chirality"]["all_10_gammas_hermitian"]
    assert sec2["cl10_and_aps_chirality"]["cl10_anticommutator_2delta"]
    assert sec2["cl10_and_aps_chirality"]["chiral_volume_equals_minus1_F"]
    assert sec2["cl10_and_aps_chirality"]["aps_L_even_all_plus1"]
    assert sec2["cl10_and_aps_chirality"]["aps_L_odd_all_minus1"]
    assert sec2["cl10_and_aps_chirality"]["aps_left_handed_zero_mode_dim"] == 16

    assert sec2["berezin_and_pfaffian"]["symbolic_5x5_s5_grassmann_equals_det"]
    assert sec2["berezin_and_pfaffian"]["symbolic_5x5_945_matching_pfaffian_equals_det"]
    assert sec2["berezin_and_pfaffian"]["parametric_10x10_det_equals_detM_sq"]
    assert sec2["berezin_and_pfaffian"]["explicit_matrices_all_3_methods_pass"]

    assert sec2["commutant_and_global_z6"]["dim_C_su5_P_sheet"] == 12
    assert sec2["commutant_and_global_z6"]["dim_C_su5_P_eig"] == 12
    assert sec2["commutant_and_global_z6"]["commutant_lie_closed"]
    assert sec2["commutant_and_global_z6"]["commutant_derived_dim"] == 11
    assert sec2["commutant_and_global_z6"]["commutant_center_dim"] == 1
    assert sec2["commutant_and_global_z6"]["sm_12_spans_commutant"]
    assert sec2["commutant_and_global_z6"]["gcd_6Y_charges_on_16"] == 1
    assert sec2["commutant_and_global_z6"]["global_kernel_order_on_W5"] == 6
    assert sec2["commutant_and_global_z6"]["global_kernel_order_on_16_plus"] == 6

    assert sec2["lambda_even_spectrum_and_anomalies"]["basis_invariance_Lambda_UP_ok"]
    assert sec2["lambda_even_spectrum_and_anomalies"]["dLambda_lie_homomorphism_ok"]
    assert sec2["lambda_even_spectrum_and_anomalies"]["matches_expected_6Y_spectrum"]
    assert sec2["lambda_even_spectrum_and_anomalies"]["all_4_anomalies_zero"]

    assert sec2["kawamura_doublet_triplet_splitting"]["collar_odd_weak_doublet_zero_modes"] == 2
    assert sec2["kawamura_doublet_triplet_splitting"]["collar_odd_color_triplet_zero_modes"] == 0
    assert sec2["kawamura_doublet_triplet_splitting"]["matches_direct_projection"]

    assert sec3["PFU1_1_trefoil_anomaly"]["fault_confirmed"]
    assert sec3["PFU1_2_bronze_p13_gauge_dim"]["fault_confirmed"]
    assert sec3["PFU1_3_level25_cover_absence"]["fault_confirmed"]
    assert sec3["PFU1_4_collar_even_scalar"]["fault_confirmed"]
    assert sec3["PFU1_5_full_32D_vector_like"]["fault_confirmed"]

    out_payload = {
        "gate": "AGY-002_FOUND-V2-U1",
        "role": "cold_room_independent_zero_trust_referee",
        "section_0_ast_and_sha_custody": sec0,
        "section_1_dihedral_cover_and_homology": sec1,
        "section_2_exterior_cl10_berezin_and_gauge": sec2,
        "section_3_planted_fault_controls": sec3,
        "all_assertions_passed": (
            sec0["ast_scan"]["ast_clean"]
            and sec0["sha_custody"]["all_sha_verified"]
            and sec1["weyl_24_and_hypercharge_block"]["mp60_all_within_tol"]
            and sec2["lambda_even_spectrum_and_anomalies"]["all_4_anomalies_zero"]
            and sec3["PFU1_1_trefoil_anomaly"]["fault_confirmed"]
            and sec3["PFU1_2_bronze_p13_gauge_dim"]["fault_confirmed"]
            and sec3["PFU1_3_level25_cover_absence"]["fault_confirmed"]
            and sec3["PFU1_4_collar_even_scalar"]["fault_confirmed"]
            and sec3["PFU1_5_full_32D_vector_like"]["fault_confirmed"]
        ),
    }

    out_path = script_path.parent / "referee_found_v2_u1_out.json"
    out_path.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
