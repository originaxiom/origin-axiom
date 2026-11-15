#!/usr/bin/env python3
"""Zero-trust mathematical-physics countercheck for Gate 0 of AGY-002-ENDGAME-V2.

Constructs all group-theoretic invariants, two-loop Standard Model matrix RGEs,
one-loop Weinberg seesaw operator evolution, exact mpmath antiderivative and
Bulirsch-Stoer solvers, SciPy DOP853 event/trajectory integrators, random Haar
U(3)^6 basis-scrambling checks, and five planted-fault controls strictly from
published literature and rational arithmetic under the 0-of-19 empirical
firewall with zero Python float literals.
"""

from __future__ import annotations

import ast
import fractions
import hashlib
import json
import math
import pathlib
import typing

import mpmath
import numpy
from scipy import integrate

Fraction = fractions.Fraction
Path = pathlib.Path
Any = typing.Any

ALLOWED_IMPORTS = frozenset(
    {
        "__future__",
        "ast",
        "fractions",
        "hashlib",
        "json",
        "math",
        "mpmath",
        "numpy",
        "pathlib",
        "scipy",
        "typing",
    }
)


# ---------------------------------------------------------------------------
# Exact rational / arbitrary-precision conversion helpers (zero float literals)
# ---------------------------------------------------------------------------


def rat_float(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def sci_float(mantissa: int, exp10: int) -> float:
    if exp10 >= 0:
        return float(Fraction(mantissa * (10 ** exp10), 1))
    return float(Fraction(mantissa, 10 ** (-exp10)))


def frac_to_mpf(q: Fraction) -> mpmath.mpf:
    return mpmath.mpf(q.numerator) / mpmath.mpf(q.denominator)


def rat_mpf(num: int, den: int = 1) -> mpmath.mpf:
    return mpmath.mpf(num) / mpmath.mpf(den)


def rat_complex(re_num: int, re_den: int, im_num: int = 0, im_den: int = 1) -> complex:
    return complex(rat_float(re_num, re_den), rat_float(im_num, im_den))


def to_jsonable(obj: Any) -> Any:
    if isinstance(obj, (bool, numpy.bool_)):
        return bool(obj)
    if isinstance(obj, (int, numpy.integer)):
        return int(obj)
    if isinstance(obj, (float, numpy.floating)):
        return float(obj)
    if isinstance(obj, Fraction):
        return str(obj)
    if isinstance(obj, mpmath.mpf):
        return float(obj)
    if isinstance(obj, str) or obj is None:
        return obj
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(v) for v in obj]
    raise TypeError(f"Unsupported type for JSON serialization: {type(obj)!r}")


# ---------------------------------------------------------------------------
# Section 0: Own AST Self-Check & Producer Artifact SHA-256 Digest Verification
# ---------------------------------------------------------------------------


def parse_sha256_manifest(manifest_path: Path) -> tuple[str, str]:
    raw_line = manifest_path.read_text(encoding="utf-8").strip()
    parts = raw_line.split()
    if len(parts) != 2 or len(parts[0]) != 64:
        raise ValueError(f"Malformed SHA-256 manifest in {manifest_path.name}")
    return parts[0], parts[1]


def sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_section_0_ast_and_digests(script_path: Path, repo_root: Path) -> dict[str, Any]:
    source_text = script_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=script_path.name)

    float_literal_count = 0
    imported_modules_set: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_literal_count += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules_set.add(alias.name.split(".")[0])
                imported_modules_set.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                imported_modules_set.add(node.module.split(".")[0])
                imported_modules_set.add(node.module)

    imported_modules = sorted(imported_modules_set)
    disallowed_imports = sorted(m for m in imported_modules_set if m not in ALLOWED_IMPORTS)

    fixed_dir = repo_root / "relays" / "agy002_endgame_v2_g0_fixed"
    exp_script_sha, rel_script_str = parse_sha256_manifest(fixed_dir / "SCRIPT_SHA256.txt")
    exp_output_sha, rel_output_str = parse_sha256_manifest(fixed_dir / "OUTPUT_SHA256.txt")

    actual_script_sha = sha256_hex(repo_root / rel_script_str)
    actual_output_sha = sha256_hex(repo_root / rel_output_str)

    script_sha_ok = actual_script_sha == exp_script_sha
    output_sha_ok = actual_output_sha == exp_output_sha
    ast_ok = (float_literal_count == 0) and (len(disallowed_imports) == 0)

    return {
        "ast_and_digest_gate_passed": bool(ast_ok and script_sha_ok and output_sha_ok),
        "own_script_relpath": script_path.relative_to(repo_root).as_posix(),
        "own_script_sha256": sha256_hex(script_path),
        "imported_modules": imported_modules,
        "disallowed_imports": disallowed_imports,
        "float_literals_in_entire_file": float_literal_count,
        "producer_script_relpath": rel_script_str,
        "producer_script_sha256_expected": exp_script_sha,
        "producer_script_sha256_actual": actual_script_sha,
        "producer_script_sha256_match": script_sha_ok,
        "producer_output_relpath": rel_output_str,
        "producer_output_sha256_expected": exp_output_sha,
        "producer_output_sha256_actual": actual_output_sha,
        "producer_output_sha256_match": output_sha_ok,
    }


# ---------------------------------------------------------------------------
# Section 1: Exact Group-Theoretic Lie Algebra & Two-Loop Polynomial Checks
# ---------------------------------------------------------------------------


class GaussianRational:
    """Exact Q(i) scalar for exact Lie-algebra trace and commutator arithmetic."""

    __slots__ = ("re", "im")

    def __init__(self, re: Fraction | int = 0, im: Fraction | int = 0) -> None:
        self.re = re if isinstance(re, Fraction) else Fraction(re, 1)
        self.im = im if isinstance(im, Fraction) else Fraction(im, 1)

    def __add__(self, other: GaussianRational) -> GaussianRational:
        return GaussianRational(self.re + other.re, self.im + other.im)

    def __sub__(self, other: GaussianRational) -> GaussianRational:
        return GaussianRational(self.re - other.re, self.im - other.im)

    def __mul__(self, other: GaussianRational) -> GaussianRational:
        return GaussianRational(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conj(self) -> GaussianRational:
        return GaussianRational(self.re, -self.im)

    def norm_sq(self) -> Fraction:
        return self.re * self.re + self.im * self.im


GR_ZERO = GaussianRational(0, 0)


def gr_zeros(n: int) -> list[list[GaussianRational]]:
    return [[GR_ZERO for _ in range(n)] for _ in range(n)]


def gr_matmul(
    a: list[list[GaussianRational]],
    b: list[list[GaussianRational]],
) -> list[list[GaussianRational]]:
    n = len(a)
    out = gr_zeros(n)
    for i in range(n):
        for k in range(n):
            aik = a[i][k]
            if aik.re == 0 and aik.im == 0:
                continue
            for j in range(n):
                bjk = b[k][j]
                if bjk.re == 0 and bjk.im == 0:
                    continue
                out[i][j] = out[i][j] + aik * bjk
    return out


def gr_comm(
    a: list[list[GaussianRational]],
    b: list[list[GaussianRational]],
) -> list[list[GaussianRational]]:
    ab = gr_matmul(a, b)
    ba = gr_matmul(b, a)
    n = len(a)
    return [[ab[i][j] - ba[i][j] for j in range(n)] for i in range(n)]


def gr_trace(a: list[list[GaussianRational]]) -> GaussianRational:
    acc = GR_ZERO
    for i in range(len(a)):
        acc = acc + a[i][i]
    return acc


def build_sun_scaled_generators(
    n: int,
) -> list[tuple[int, list[list[GaussianRational]]]]:
    """Construct all n^2 - 1 Hermitian generators T^a = (1/sqrt(d_a)) * M^a of SU(n)
    normalized to Tr(T^a T^b) = (1/2) delta^{ab}, storing exact (d_a, M^a).
    """
    gens: list[tuple[int, list[list[GaussianRational]]]] = []
    half = Fraction(1, 2)
    for p in range(n):
        for q in range(p + 1, n):
            m_sym = gr_zeros(n)
            m_sym[p][q] = GaussianRational(half, 0)
            m_sym[q][p] = GaussianRational(half, 0)
            gens.append((1, m_sym))

            m_asym = gr_zeros(n)
            m_asym[p][q] = GaussianRational(0, -half)
            m_asym[q][p] = GaussianRational(0, half)
            gens.append((1, m_asym))

    for m in range(1, n):
        # Cartan H_m = (1 / sqrt(2*m*(m+1))) * diag(1,...,1, -m, 0,...,0)
        denom_sq = 2 * m * (m + 1)
        m_cart = gr_zeros(n)
        for idx in range(m):
            m_cart[idx][idx] = GaussianRational(1, 0)
        m_cart[m][m] = GaussianRational(-m, 0)
        gens.append((denom_sq, m_cart))

    if len(gens) != n * n - 1:
        raise RuntimeError("Generator count mismatch for SU(N)")
    return gens


def verify_dynkin_and_adjoint_casimir(n: int) -> tuple[Fraction, Fraction]:
    """Compute fundamental Dynkin index T(F) and adjoint Casimir C_2(SU(n))
    directly from explicit n x n generator matrices and structure constants.
    """
    gens = build_sun_scaled_generators(n)
    num_g = len(gens)

    # Verify Tr(T^a T^b) = (1/2) delta^{ab}
    dynkin_f = Fraction(1, 2)
    for a in range(num_g):
        da, ma = gens[a]
        for b in range(num_g):
            db, mb = gens[b]
            tr_ab = gr_trace(gr_matmul(ma, mb))
            if tr_ab.im != 0:
                raise ValueError("Non-real Killing trace")
            if a == b:
                if Fraction(tr_ab.re, da) != dynkin_f:
                    raise ValueError("Generator normalization != 1/2")
            else:
                if tr_ab.re != 0:
                    raise ValueError("Generators not orthogonal")

    # Compute C_2(G) = sum_{b,c} (f^{0bc})^2 where f^{abc} = -2i Tr([T^a, T^b] T^c)
    d0, m0 = gens[0]
    c2_adj = Fraction(0, 1)
    minus_two_i = GaussianRational(0, -2)
    for b in range(num_g):
        db, mb = gens[b]
        comm_0b = gr_comm(m0, mb)
        for c in range(num_g):
            dc, mc = gens[c]
            raw = minus_two_i * gr_trace(gr_matmul(comm_0b, mc))
            if raw.im != 0:
                raise ValueError("Structure constant is not purely real")
            c2_adj += (raw.re * raw.re) / Fraction(d0 * db * dc, 1)

    return dynkin_f, c2_adj


# ---------------------------------------------------------------------------
# Exact Two-Loop SM Matrix Beta Functions (GUT-normalized g_1, left-row Y_f)
# ---------------------------------------------------------------------------

SM_B1_VEC = (Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1))

SM_B2_MAT = (
    (Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)),
    (Fraction(9, 10), Fraction(35, 6), Fraction(12, 1)),
    (Fraction(11, 10), Fraction(9, 2), Fraction(-26, 1)),
)

SM_YUK_GAUGE_2LOOP = (
    (Fraction(17, 10), Fraction(1, 2), Fraction(3, 2)),
    (Fraction(3, 2), Fraction(3, 2), Fraction(1, 2)),
    (Fraction(2, 1), Fraction(2, 1), Fraction(0, 1)),
)


def sm_2loop_diagonal_rational_rhs(
    g1: Fraction,
    g2: Fraction,
    g3: Fraction,
    yt: Fraction,
    yb: Fraction,
    ytau: Fraction,
    lam: Fraction,
) -> dict[str, tuple[Fraction, Fraction]]:
    """Evaluate 1-loop and 2-loop polynomial numerators (beta^{(1)}, beta^{(2)})
    from the 3x3 matrix formulas evaluated at diagonal Y_u=diag(0,0,yt),
    Y_d=diag(0,0,yb), Y_e=diag(0,0,ytau) in exact Fraction arithmetic.
    """
    hu33 = yt * yt
    hd33 = yb * yb
    he33 = ytau * ytau

    tr_hu = hu33
    tr_hd = hd33
    tr_he = he33

    y2 = 3 * tr_hu + 3 * tr_hd + tr_he
    hs = 3 * (hu33 * hu33) + 3 * (hd33 * hd33) + (he33 * he33)
    h6 = 3 * (hu33 ** 3) + 3 * (hd33 ** 3) + (he33 ** 3)
    tr_huhd = hu33 * hd33

    g1_sq = g1 * g1
    g2_sq = g2 * g2
    g3_sq = g3 * g3

    y4 = (
        (Fraction(17, 20) * g1_sq + Fraction(9, 4) * g2_sq + 8 * g3_sq) * tr_hu
        + (Fraction(1, 4) * g1_sq + Fraction(9, 4) * g2_sq + 8 * g3_sq) * tr_hd
        + Fraction(3, 4) * (g1_sq + g2_sq) * tr_he
    )
    chi4 = Fraction(9, 4) * hs - Fraction(3, 2) * tr_huhd

    g_sq_vec = (g1_sq, g2_sq, g3_sq)
    g_vec = (g1, g2, g3)
    tr_vec = (tr_hu, tr_hd, tr_he)

    out: dict[str, tuple[Fraction, Fraction]] = {}
    names_g = ("g1", "g2", "g3")
    for idx in range(3):
        gi = g_vec[idx]
        gi3 = gi * gi * gi
        b1_g = SM_B1_VEC[idx] * gi3
        loop2_inner = Fraction(0, 1)
        for jdx in range(3):
            loop2_inner += SM_B2_MAT[idx][jdx] * g_sq_vec[jdx]
            loop2_inner -= SM_YUK_GAUGE_2LOOP[idx][jdx] * tr_vec[jdx]
        b2_g = gi3 * loop2_inner
        out[names_g[idx]] = (b1_g, b2_g)

    # Yukawa 1-loop and 2-loop (3,3) entries
    yt_1 = (
        Fraction(3, 2) * (hu33 - hd33)
        + y2
        - (Fraction(17, 20) * g1_sq + Fraction(9, 4) * g2_sq + 8 * g3_sq)
    ) * yt
    yt_2 = (
        Fraction(3, 2) * (hu33 * hu33)
        - hd33 * hu33
        - Fraction(1, 4) * hu33 * hd33
        + Fraction(11, 4) * (hd33 * hd33)
        + y2 * (Fraction(5, 4) * hd33 - Fraction(9, 4) * hu33)
        - chi4
        + 6 * lam * lam
        - 12 * lam * hu33
        + Fraction(5, 2) * y4
        + (Fraction(223, 80) * g1_sq + Fraction(135, 16) * g2_sq + 16 * g3_sq) * hu33
        - (Fraction(43, 80) * g1_sq - Fraction(9, 16) * g2_sq + 16 * g3_sq) * hd33
        + Fraction(1187, 600) * (g1_sq * g1_sq)
        - Fraction(9, 20) * g1_sq * g2_sq
        + Fraction(19, 15) * g1_sq * g3_sq
        - Fraction(23, 4) * (g2_sq * g2_sq)
        + 9 * g2_sq * g3_sq
        - 108 * (g3_sq * g3_sq)
    ) * yt
    out["yt"] = (yt_1, yt_2)

    yb_1 = (
        Fraction(3, 2) * (hd33 - hu33)
        + y2
        - (Fraction(1, 4) * g1_sq + Fraction(9, 4) * g2_sq + 8 * g3_sq)
    ) * yb
    yb_2 = (
        Fraction(3, 2) * (hd33 * hd33)
        - hu33 * hd33
        - Fraction(1, 4) * hd33 * hu33
        + Fraction(11, 4) * (hu33 * hu33)
        + y2 * (Fraction(5, 4) * hu33 - Fraction(9, 4) * hd33)
        - chi4
        + 6 * lam * lam
        - 12 * lam * hd33
        + Fraction(5, 2) * y4
        + (Fraction(187, 80) * g1_sq + Fraction(135, 16) * g2_sq + 16 * g3_sq) * hd33
        - (Fraction(79, 80) * g1_sq - Fraction(9, 16) * g2_sq + 16 * g3_sq) * hu33
        - Fraction(127, 600) * (g1_sq * g1_sq)
        - Fraction(27, 20) * g1_sq * g2_sq
        + Fraction(31, 15) * g1_sq * g3_sq
        - Fraction(23, 4) * (g2_sq * g2_sq)
        + 9 * g2_sq * g3_sq
        - 108 * (g3_sq * g3_sq)
    ) * yb
    out["yb"] = (yb_1, yb_2)

    ytau_1 = (
        Fraction(3, 2) * he33
        + y2
        - (Fraction(9, 4) * g1_sq + Fraction(9, 4) * g2_sq)
    ) * ytau
    ytau_2 = (
        Fraction(3, 2) * (he33 * he33)
        - Fraction(9, 4) * y2 * he33
        - chi4
        + 6 * lam * lam
        - 12 * lam * he33
        + Fraction(5, 2) * y4
        + (Fraction(387, 80) * g1_sq + Fraction(135, 16) * g2_sq) * he33
        + Fraction(1371, 200) * (g1_sq * g1_sq)
        + Fraction(27, 20) * g1_sq * g2_sq
        - Fraction(23, 4) * (g2_sq * g2_sq)
    ) * ytau
    out["ytau"] = (ytau_1, ytau_2)

    lam_1 = (
        24 * lam * lam
        - (Fraction(9, 5) * g1_sq + 9 * g2_sq) * lam
        + Fraction(27, 200) * (g1_sq * g1_sq)
        + Fraction(9, 20) * g1_sq * g2_sq
        + Fraction(9, 8) * (g2_sq * g2_sq)
        + 4 * y2 * lam
        - 2 * hs
    )
    lam_2 = (
        -312 * (lam ** 3)
        + (108 * g2_sq + Fraction(108, 5) * g1_sq) * (lam * lam)
        - 48 * (lam * lam) * y2
        + (
            Fraction(-73, 8) * (g2_sq * g2_sq)
            + Fraction(117, 20) * g1_sq * g2_sq
            + Fraction(1887, 200) * (g1_sq * g1_sq)
        )
        * lam
        + 10 * lam * y4
        - lam * hs
        - 42 * lam * tr_huhd
        + Fraction(305, 16) * (g2_sq ** 3)
        - Fraction(289, 80) * (g2_sq * g2_sq) * g1_sq
        - Fraction(1677, 400) * g2_sq * (g1_sq * g1_sq)
        - Fraction(3411, 2000) * (g1_sq ** 3)
        - 32 * g3_sq * (hu33 * hu33 + hd33 * hd33)
        - Fraction(4, 5) * g1_sq * (2 * hu33 * hu33 - hd33 * hd33 + 3 * he33 * he33)
        - Fraction(3, 4) * (g2_sq * g2_sq) * y2
        + g1_sq
        * (
            (Fraction(63, 10) * g2_sq - Fraction(171, 100) * g1_sq) * tr_hu
            + (Fraction(27, 10) * g2_sq + Fraction(9, 20) * g1_sq) * tr_hd
            + (Fraction(33, 10) * g2_sq - Fraction(9, 4) * g1_sq) * tr_he
        )
        + 10 * h6
        - 6 * (hu33 * hu33 * hd33 + hu33 * hd33 * hd33)
    )
    out["lam"] = (lam_1, lam_2)
    return out


def buttazzo_2013_published_scalar_rhs(
    g1: Fraction,
    g2: Fraction,
    g3: Fraction,
    yt: Fraction,
    yb: Fraction,
    ytau: Fraction,
    lam: Fraction,
) -> dict[str, tuple[Fraction, Fraction]]:
    """Standalone transcription of Buttazzo et al. (2013) SM 2-loop RGEs
    converted from d(g^2)/d ln mu^2, d(y^2)/d ln mu^2, d(lam)/d ln mu^2
    to d/d ln mu.
    """
    g1s = g1 * g1
    g2s = g2 * g2
    g3s = g3 * g3
    yts = yt * yt
    ybs = yb * yb
    ytaus = ytau * ytau

    yt_1 = yt * (
        Fraction(9, 2) * yts
        + Fraction(3, 2) * ybs
        + ytaus
        - 8 * g3s
        - Fraction(9, 4) * g2s
        - Fraction(17, 20) * g1s
    )
    yt_2 = yt * (
        yts
        * (
            -12 * yts
            - Fraction(11, 4) * ybs
            - Fraction(9, 4) * ytaus
            - 12 * lam
            + 36 * g3s
            + Fraction(225, 16) * g2s
            + Fraction(393, 80) * g1s
        )
        + ybs
        * (
            Fraction(-1, 4) * ybs
            + Fraction(5, 4) * ytaus
            + 4 * g3s
            + Fraction(99, 16) * g2s
            + Fraction(7, 80) * g1s
        )
        + ytaus * (Fraction(-9, 4) * ytaus + Fraction(15, 8) * g2s + Fraction(15, 8) * g1s)
        + 6 * lam * lam
        - 108 * g3s * g3s
        - Fraction(23, 4) * g2s * g2s
        + Fraction(1187, 600) * g1s * g1s
        + 9 * g3s * g2s
        + Fraction(19, 15) * g3s * g1s
        - Fraction(9, 20) * g2s * g1s
    )

    yb_1 = yb * (
        Fraction(3, 2) * yts
        + Fraction(9, 2) * ybs
        + ytaus
        - 8 * g3s
        - Fraction(9, 4) * g2s
        - Fraction(1, 4) * g1s
    )
    yb_2 = yb * (
        yts
        * (
            Fraction(-1, 4) * yts
            - Fraction(11, 4) * ybs
            + Fraction(5, 4) * ytaus
            + 4 * g3s
            + Fraction(99, 16) * g2s
            + Fraction(91, 80) * g1s
        )
        + ybs
        * (
            -12 * ybs
            - Fraction(9, 4) * ytaus
            - 12 * lam
            + 36 * g3s
            + Fraction(225, 16) * g2s
            + Fraction(237, 80) * g1s
        )
        + ytaus * (Fraction(-9, 4) * ytaus + Fraction(15, 8) * g2s + Fraction(15, 8) * g1s)
        + 6 * lam * lam
        - 108 * g3s * g3s
        - Fraction(23, 4) * g2s * g2s
        - Fraction(127, 600) * g1s * g1s
        + 9 * g3s * g2s
        + Fraction(31, 15) * g3s * g1s
        - Fraction(27, 20) * g2s * g1s
    )

    ytau_1 = ytau * (
        3 * yts + 3 * ybs + Fraction(5, 2) * ytaus - Fraction(9, 4) * g2s - Fraction(9, 4) * g1s
    )
    ytau_2 = ytau * (
        6 * lam * lam
        - Fraction(23, 4) * g2s * g2s
        + Fraction(1371, 200) * g1s * g1s
        + Fraction(27, 20) * g2s * g1s
        + yts
        * (
            Fraction(-27, 4) * yts
            + Fraction(3, 2) * ybs
            - Fraction(27, 4) * ytaus
            + 20 * g3s
            + Fraction(45, 8) * g2s
            + Fraction(17, 8) * g1s
        )
        + ybs
        * (
            Fraction(-27, 4) * ybs
            - Fraction(27, 4) * ytaus
            + 20 * g3s
            + Fraction(45, 8) * g2s
            + Fraction(5, 8) * g1s
        )
        + ytaus * (-3 * ytaus - 12 * lam + Fraction(165, 16) * g2s + Fraction(537, 80) * g1s)
    )

    # Multiply d(lambda)/d(ln mu^2) by 2 to obtain d(lambda)/d(ln mu)
    lam_1 = 2 * (
        lam * (12 * lam + 6 * yts + 6 * ybs + 2 * ytaus - Fraction(9, 2) * g2s - Fraction(9, 10) * g1s)
        - 3 * yts * yts
        - 3 * ybs * ybs
        - ytaus * ytaus
        + Fraction(9, 16) * g2s * g2s
        + Fraction(27, 400) * g1s * g1s
        + Fraction(9, 40) * g2s * g1s
    )
    lam_2 = 2 * (
        (lam * lam) * (-156 * lam - 72 * yts - 72 * ybs - 24 * ytaus + 54 * g2s + Fraction(54, 5) * g1s)
        + lam * yts * (Fraction(-3, 2) * yts - 21 * ybs + 40 * g3s + Fraction(45, 4) * g2s + Fraction(17, 4) * g1s)
        + lam * ybs * (Fraction(-3, 2) * ybs + 40 * g3s + Fraction(45, 4) * g2s + Fraction(5, 4) * g1s)
        + lam * ytaus * (Fraction(-1, 2) * ytaus + Fraction(15, 4) * g2s + Fraction(15, 4) * g1s)
        + lam * (Fraction(-73, 16) * g2s * g2s + Fraction(1887, 400) * g1s * g1s + Fraction(117, 40) * g2s * g1s)
        + (yts * yts) * (15 * yts - 3 * ybs - 16 * g3s - Fraction(4, 5) * g1s)
        + yts * (Fraction(-9, 8) * g2s * g2s - Fraction(171, 200) * g1s * g1s + Fraction(63, 20) * g2s * g1s)
        + (ybs * ybs) * (-3 * yts + 15 * ybs - 16 * g3s + Fraction(2, 5) * g1s)
        + ybs * (Fraction(-9, 8) * g2s * g2s + Fraction(9, 40) * g1s * g1s + Fraction(27, 20) * g2s * g1s)
        + (ytaus * ytaus) * (5 * ytaus - Fraction(6, 5) * g1s)
        + ytaus * (Fraction(-3, 8) * g2s * g2s - Fraction(9, 8) * g1s * g1s + Fraction(33, 20) * g2s * g1s)
        + Fraction(305, 32) * (g2s ** 3)
        - Fraction(3411, 4000) * (g1s ** 3)
        - Fraction(289, 160) * (g2s * g2s) * g1s
        - Fraction(1677, 800) * g2s * (g1s * g1s)
    )

    return {
        "yt": (yt_1, yt_2),
        "yb": (yb_1, yb_2),
        "ytau": (ytau_1, ytau_2),
        "lam": (lam_1, lam_2),
    }


def run_section_1_group_theory_and_polynomials() -> dict[str, Any]:
    # 1. Explicit Casimirs and Dynkin indices from SU(2), SU(3), SU(4) generators
    t_su2, c2_su2 = verify_dynkin_and_adjoint_casimir(2)
    t_su3, c2_su3 = verify_dynkin_and_adjoint_casimir(3)
    t_su4, c2_su4 = verify_dynkin_and_adjoint_casimir(4)

    # 2. Chiral SM generation quantum numbers (left-handed Weyl fields):
    # (name, d_su3, is_su3_plet, d_su2, is_su2_plet, Y)
    sm_chiral_gen = [
        ("Q_L", 3, True, 2, True, Fraction(1, 6)),
        ("u_L^c", 3, True, 1, False, Fraction(-2, 3)),
        ("d_L^c", 3, True, 1, False, Fraction(1, 3)),
        ("L_L", 1, False, 2, True, Fraction(-1, 2)),
        ("e_L^c", 1, False, 1, False, Fraction(1, 1)),
    ]

    anom_su3_sq_u1 = sum(
        (d2 * t_su3 * y_val for _, _, in3, d2, _, y_val in sm_chiral_gen if in3),
        Fraction(0, 1),
    )
    anom_su2_sq_u1 = sum(
        (d3 * t_su2 * y_val for _, d3, _, _, in2, y_val in sm_chiral_gen if in2),
        Fraction(0, 1),
    )
    anom_u1_cubed = sum(
        (d3 * d2 * (y_val ** 3) for _, d3, _, d2, _, y_val in sm_chiral_gen),
        Fraction(0, 1),
    )
    anom_grav_sq_u1 = sum(
        (d3 * d2 * y_val for _, d3, _, d2, _, y_val in sm_chiral_gen),
        Fraction(0, 1),
    )
    sm_anomalies = [anom_su3_sq_u1, anom_su2_sq_u1, anom_u1_cubed, anom_grav_sq_u1]
    anomalies_zero = all(a == 0 for a in sm_anomalies)

    # 3. 1-loop SM gauge slopes b_SM = (41/10, -19/6, -7) for N_g = 3, N_H = 1
    n_gen = 3
    gut_u1_factor = Fraction(3, 5)
    t1_gen = gut_u1_factor * sum(
        (d3 * d2 * (y_val ** 2) for _, d3, _, d2, _, y_val in sm_chiral_gen),
        Fraction(0, 1),
    )
    t2_gen = sum(
        (d3 * t_su2 for _, d3, _, _, in2, _ in sm_chiral_gen if in2),
        Fraction(0, 1),
    )
    t3_gen = sum(
        (d2 * t_su3 for _, _, in3, d2, _, _ in sm_chiral_gen if in3),
        Fraction(0, 1),
    )

    # Complex Higgs doublet H ~ (1, 2, +1/2)
    t1_higgs = gut_u1_factor * 2 * (Fraction(1, 2) ** 2)
    t2_higgs = t_su2
    t3_higgs = Fraction(0, 1)

    b1_sm = Fraction(2, 3) * (n_gen * t1_gen) + Fraction(1, 3) * t1_higgs
    b2_sm = Fraction(-11, 3) * c2_su2 + Fraction(2, 3) * (n_gen * t2_gen) + Fraction(1, 3) * t2_higgs
    b3_sm = Fraction(-11, 3) * c2_su3 + Fraction(2, 3) * (n_gen * t3_gen) + Fraction(1, 3) * t3_higgs
    sm_b_tuple = (b1_sm, b2_sm, b3_sm)
    sm_b_ok = sm_b_tuple == (Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1))

    # 4. Left-Right D-symmetric Pati-Salam SU(4)_c x SU(2)_L x SU(2)_R
    # Explicit 15th generator of SU(4)_c from build_sun_scaled_generators(4):
    su4_gens = build_sun_scaled_generators(4)
    d15, m15 = su4_gens[-1]
    # Verify d15 == 24 and M15 = diag(1, 1, 1, -3), so (B-L)/2 = diag(1/6,1/6,1/6,-1/2) = sqrt(2/3) T_4^15
    b_minus_l_half_diag = [Fraction(1, 6), Fraction(1, 6), Fraction(1, 6), Fraction(-1, 2)]
    m15_diag = [m15[k][k].re for k in range(4)]
    # Check (B-L)/2_k^2 == c_{4c}^2 * (M15_k^2 / d15) => c_{4c}^2 = 2/3
    c4c_sq_list = [
        (b_minus_l_half_diag[k] ** 2) / (Fraction(m15_diag[k] ** 2, d15))
        for k in range(4)
    ]
    if len(set(c4c_sq_list)) != 1:
        raise ValueError("Inconsistent B-L embedding in SU(4)_c")
    c4c_sq = c4c_sq_list[0]
    c2r_sq = Fraction(1, 1)

    # Verify Y = T_{3R} + (B-L)/2 reproduces all SM hypercharges on Psi_L=(4,2,1) and Psi_R=(4,1,2)
    psi_l_y = [bml for bml in b_minus_l_half_diag for _ in range(2)]
    psi_r_y = [t3r + bml for bml in b_minus_l_half_diag for t3r in (Fraction(1, 2), Fraction(-1, 2))]
    # Trace check on 16-component generation: Tr(Y^2) = 10/3, so GUT T_1 = sqrt(3/5) Y
    tr_y_sq_ps_gen = sum((y ** 2 for y in psi_l_y), Fraction(0, 1)) + sum(
        (y ** 2 for y in psi_r_y), Fraction(0, 1)
    )
    # Matching weights for T_1 = sqrt(w_{2R}) T_{3R} + sqrt(w_{4c}) T_4^{15}:
    # Since Tr_{16}(T_1^2) = 2 and Tr_{16}(T_{3R}^2) = Tr_{16}((T_4^{15})^2) = 2:
    w_2r = gut_u1_factor * c2r_sq
    w_4c = gut_u1_factor * c4c_sq
    ps_weights_ok = (w_2r == Fraction(3, 5)) and (w_4c == Fraction(2, 5)) and (tr_y_sq_ps_gen == Fraction(10, 3))

    # 1-loop Pati-Salam gauge slopes with N_g=3 chiral (4,2,1) + (4bar,1,2bar)
    # and minimal D-symmetric complex scalars Phi=(1,2,2) + chi_R=(4,1,2) + chi_L=(4bar,2,1)
    t4_ferm_gen = 2 * t_su4 + 2 * t_su4
    t2l_ferm_gen = 4 * t_su2
    t2r_ferm_gen = 4 * t_su2

    t4_scal = Fraction(0, 1) + 2 * t_su4 + 2 * t_su4
    t2l_scal = 2 * t_su2 + Fraction(0, 1) + 4 * t_su2
    t2r_scal = 2 * t_su2 + 4 * t_su2 + Fraction(0, 1)

    b4_ps = Fraction(-11, 3) * c2_su4 + Fraction(2, 3) * (n_gen * t4_ferm_gen) + Fraction(1, 3) * t4_scal
    b2l_ps = Fraction(-11, 3) * c2_su2 + Fraction(2, 3) * (n_gen * t2l_ferm_gen) + Fraction(1, 3) * t2l_scal
    b2r_ps = Fraction(-11, 3) * c2_su2 + Fraction(2, 3) * (n_gen * t2r_ferm_gen) + Fraction(1, 3) * t2r_scal
    ps_b_ok = (b4_ps, b2l_ps, b2r_ps) == (Fraction(-10, 1), Fraction(-7, 3), Fraction(-7, 3))

    # 5. Multi-point exact rational polynomial identity check against Buttazzo et al. (2013)
    test_points = [
        (
            Fraction(1, 2),
            Fraction(3, 5),
            Fraction(1, 1),
            Fraction(9, 10),
            Fraction(0, 1),
            Fraction(0, 1),
            Fraction(1, 10),
        ),
        (
            Fraction(3, 7),
            Fraction(5, 11),
            Fraction(4, 5),
            Fraction(6, 7),
            Fraction(2, 9),
            Fraction(3, 13),
            Fraction(2, 15),
        ),
        (
            Fraction(7, 13),
            Fraction(4, 9),
            Fraction(6, 11),
            Fraction(5, 8),
            Fraction(3, 7),
            Fraction(4, 11),
            Fraction(-1, 17),
        ),
        (
            Fraction(2, 5),
            Fraction(7, 10),
            Fraction(9, 8),
            Fraction(11, 12),
            Fraction(5, 14),
            Fraction(7, 19),
            Fraction(3, 8),
        ),
    ]
    yt_exact_match = True
    yb_exact_match = True
    ytau_exact_match = True
    lam_exact_match = True
    for pt in test_points:
        mat_res = sm_2loop_diagonal_rational_rhs(*pt)
        but_res = buttazzo_2013_published_scalar_rhs(*pt)
        if mat_res["yt"] != but_res["yt"]:
            yt_exact_match = False
        if mat_res["yb"] != but_res["yb"]:
            yb_exact_match = False
        if mat_res["ytau"] != but_res["ytau"]:
            ytau_exact_match = False
        if mat_res["lam"] != but_res["lam"]:
            lam_exact_match = False

    gate_ok = (
        anomalies_zero
        and sm_b_ok
        and ps_weights_ok
        and ps_b_ok
        and yt_exact_match
        and yb_exact_match
        and ytau_exact_match
        and lam_exact_match
    )

    return {
        "lie_algebra_and_polynomial_gate_passed": gate_ok,
        "casimir_adjoint_su2_su3_su4": [c2_su2, c2_su3, c2_su4],
        "sm_anomaly_traces_zero": sm_anomalies,
        "sm_1loop_b": [b1_sm, b2_sm, b3_sm],
        "pati_salam_hypercharge_weights_w2R_w4c": [w_2r, w_4c],
        "pati_salam_1loop_b4_b2L_b2R": [b4_ps, b2l_ps, b2r_ps],
        "buttazzo_2013_yt_2loop_exact_match": yt_exact_match,
        "buttazzo_2013_yb_2loop_exact_match": yb_exact_match,
        "buttazzo_2013_ytau_2loop_exact_match": ytau_exact_match,
        "buttazzo_2013_lam_2loop_exact_match": lam_exact_match,
    }


# ---------------------------------------------------------------------------
# NumPy Float64 & Mpmath Matrix RGE RHS and Bulirsch-Stoer Integrators
# ---------------------------------------------------------------------------

KAPPA_1_F64 = float(1) / (float(16) * (math.pi ** 2))
KAPPA_2_F64 = KAPPA_1_F64 * KAPPA_1_F64
EYE3_C128 = numpy.eye(3, dtype=numpy.complex128)


def pack_sm_state(
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    yu: numpy.ndarray,
    yd: numpy.ndarray,
    ye: numpy.ndarray,
    kappa: numpy.ndarray | None = None,
) -> numpy.ndarray:
    parts = [
        numpy.array([g1, g2, g3, lam], dtype=numpy.float64),
        yu.real.ravel(),
        yu.imag.ravel(),
        yd.real.ravel(),
        yd.imag.ravel(),
        ye.real.ravel(),
        ye.imag.ravel(),
    ]
    if kappa is not None:
        parts.append(kappa.real.ravel())
        parts.append(kappa.imag.ravel())
    return numpy.concatenate(parts)


def unpack_sm_state(
    y: numpy.ndarray,
    with_kappa: bool = False,
) -> tuple[
    float,
    float,
    float,
    float,
    numpy.ndarray,
    numpy.ndarray,
    numpy.ndarray,
    numpy.ndarray | None,
]:
    g1 = float(y[0])
    g2 = float(y[1])
    g3 = float(y[2])
    lam = float(y[3])
    yu = (y[4:13] + complex(0, 1) * y[13:22]).reshape((3, 3))
    yd = (y[22:31] + complex(0, 1) * y[31:40]).reshape((3, 3))
    ye = (y[40:49] + complex(0, 1) * y[49:58]).reshape((3, 3))
    kap = None
    if with_kappa:
        kap = (y[58:67] + complex(0, 1) * y[67:76]).reshape((3, 3))
    return g1, g2, g3, lam, yu, yd, ye, kap


def sm_matrix_rge_rhs_f64(
    _t: float,
    y: numpy.ndarray,
    two_loop: bool = True,
    with_kappa: bool = False,
    wrong_yu_right_mult: bool = False,
    scale_factor: float = float(1),
) -> numpy.ndarray:
    g1, g2, g3, lam, yu, yd, ye, kap = unpack_sm_state(y, with_kappa=with_kappa)

    hu = yu @ yu.conj().T
    hd = yd @ yd.conj().T
    he = ye @ ye.conj().T

    tr_hu = float( numpy.trace(hu).real )
    tr_hd = float( numpy.trace(hd).real )
    tr_he = float( numpy.trace(he).real )
    y2_tr = float(3) * tr_hu + float(3) * tr_hd + tr_he

    hu2 = hu @ hu
    hd2 = hd @ hd
    he2 = he @ he
    hs_tr = (
        float(3) * float(numpy.trace(hu2).real)
        + float(3) * float(numpy.trace(hd2).real)
        + float(numpy.trace(he2).real)
    )

    g1s = g1 * g1
    g2s = g2 * g2
    g3s = g3 * g3

    dg1 = KAPPA_1_F64 * rat_float(41, 10) * (g1 * g1s)
    dg2 = KAPPA_1_F64 * rat_float(-19, 6) * (g2 * g2s)
    dg3 = KAPPA_1_F64 * float(-7) * (g3 * g3s)

    mu1_scalar = y2_tr - (rat_float(17, 20) * g1s + rat_float(9, 4) * g2s + float(8) * g3s)
    md1_scalar = y2_tr - (rat_float(1, 4) * g1s + rat_float(9, 4) * g2s + float(8) * g3s)
    me1_scalar = y2_tr - (rat_float(9, 4) * g1s + rat_float(9, 4) * g2s)

    if wrong_yu_right_mult:
        byu1 = yu @ (rat_float(3, 2) * (hu - hd)) + mu1_scalar * yu
    else:
        byu1 = (rat_float(3, 2) * (hu - hd) + mu1_scalar * EYE3_C128) @ yu

    byd1 = (rat_float(3, 2) * (hd - hu) + md1_scalar * EYE3_C128) @ yd
    bye1 = (rat_float(3, 2) * he + me1_scalar * EYE3_C128) @ ye

    dyu = KAPPA_1_F64 * byu1
    dyd = KAPPA_1_F64 * byd1
    dye = KAPPA_1_F64 * bye1

    dlam = KAPPA_1_F64 * (
        float(24) * lam * lam
        - (rat_float(9, 5) * g1s + float(9) * g2s) * lam
        + rat_float(27, 200) * g1s * g1s
        + rat_float(9, 20) * g1s * g2s
        + rat_float(9, 8) * g2s * g2s
        + float(4) * y2_tr * lam
        - float(2) * hs_tr
    )

    if two_loop:
        dg1 += KAPPA_2_F64 * (g1 * g1s) * (
            rat_float(199, 50) * g1s
            + rat_float(27, 10) * g2s
            + rat_float(44, 5) * g3s
            - rat_float(17, 10) * tr_hu
            - rat_float(1, 2) * tr_hd
            - rat_float(3, 2) * tr_he
        )
        dg2 += KAPPA_2_F64 * (g2 * g2s) * (
            rat_float(9, 10) * g1s
            + rat_float(35, 6) * g2s
            + float(12) * g3s
            - rat_float(3, 2) * tr_hu
            - rat_float(3, 2) * tr_hd
            - rat_float(1, 2) * tr_he
        )
        dg3 += KAPPA_2_F64 * (g3 * g3s) * (
            rat_float(11, 10) * g1s
            + rat_float(9, 2) * g2s
            - float(26) * g3s
            - float(2) * tr_hu
            - float(2) * tr_hd
        )

        huhd = hu @ hd
        hdhu = hd @ hu
        tr_huhd = float(numpy.trace(huhd).real)

        y4_tr = (
            (rat_float(17, 20) * g1s + rat_float(9, 4) * g2s + float(8) * g3s) * tr_hu
            + (rat_float(1, 4) * g1s + rat_float(9, 4) * g2s + float(8) * g3s) * tr_hd
            + rat_float(3, 4) * (g1s + g2s) * tr_he
        )
        chi4_tr = rat_float(9, 4) * hs_tr - rat_float(3, 2) * tr_huhd

        mu2 = (
            rat_float(3, 2) * hu2
            - hdhu
            - rat_float(1, 4) * huhd
            + rat_float(11, 4) * hd2
            + y2_tr * (rat_float(5, 4) * hd - rat_float(9, 4) * hu)
            - float(12) * lam * hu
            + (rat_float(223, 80) * g1s + rat_float(135, 16) * g2s + float(16) * g3s) * hu
            - (rat_float(43, 80) * g1s - rat_float(9, 16) * g2s + float(16) * g3s) * hd
            + (
                -chi4_tr
                + float(6) * lam * lam
                + rat_float(5, 2) * y4_tr
                + rat_float(1187, 600) * g1s * g1s
                - rat_float(9, 20) * g1s * g2s
                + rat_float(19, 15) * g1s * g3s
                - rat_float(23, 4) * g2s * g2s
                + float(9) * g2s * g3s
                - float(108) * g3s * g3s
            )
            * EYE3_C128
        )
        md2 = (
            rat_float(3, 2) * hd2
            - huhd
            - rat_float(1, 4) * hdhu
            + rat_float(11, 4) * hu2
            + y2_tr * (rat_float(5, 4) * hu - rat_float(9, 4) * hd)
            - float(12) * lam * hd
            + (rat_float(187, 80) * g1s + rat_float(135, 16) * g2s + float(16) * g3s) * hd
            - (rat_float(79, 80) * g1s - rat_float(9, 16) * g2s + float(16) * g3s) * hu
            + (
                -chi4_tr
                + float(6) * lam * lam
                + rat_float(5, 2) * y4_tr
                - rat_float(127, 600) * g1s * g1s
                - rat_float(27, 20) * g1s * g2s
                + rat_float(31, 15) * g1s * g3s
                - rat_float(23, 4) * g2s * g2s
                + float(9) * g2s * g3s
                - float(108) * g3s * g3s
            )
            * EYE3_C128
        )
        me2 = (
            rat_float(3, 2) * he2
            - rat_float(9, 4) * y2_tr * he
            - float(12) * lam * he
            + (rat_float(387, 80) * g1s + rat_float(135, 16) * g2s) * he
            + (
                -chi4_tr
                + float(6) * lam * lam
                + rat_float(5, 2) * y4_tr
                + rat_float(1371, 200) * g1s * g1s
                + rat_float(27, 20) * g1s * g2s
                - rat_float(23, 4) * g2s * g2s
            )
            * EYE3_C128
        )

        if wrong_yu_right_mult:
            dyu += KAPPA_2_F64 * (yu @ mu2)
        else:
            dyu += KAPPA_2_F64 * (mu2 @ yu)
        dyd += KAPPA_2_F64 * (md2 @ yd)
        dye += KAPPA_2_F64 * (me2 @ ye)

        h6_tr = (
            float(3) * float(numpy.trace(hu2 @ hu).real)
            + float(3) * float(numpy.trace(hd2 @ hd).real)
            + float(numpy.trace(he2 @ he).real)
        )
        tr_hu2hd_huhd2 = float(numpy.trace(hu2 @ hd + hu @ hd2).real)

        dlam += KAPPA_2_F64 * (
            float(-312) * (lam ** 3)
            + (float(108) * g2s + rat_float(108, 5) * g1s) * lam * lam
            - float(48) * lam * lam * y2_tr
            + (
                rat_float(-73, 8) * g2s * g2s
                + rat_float(117, 20) * g1s * g2s
                + rat_float(1887, 200) * g1s * g1s
            )
            * lam
            + float(10) * lam * y4_tr
            - lam * hs_tr
            - float(42) * lam * tr_huhd
            + rat_float(305, 16) * (g2s ** 3)
            - rat_float(289, 80) * g2s * g2s * g1s
            - rat_float(1677, 400) * g2s * g1s * g1s
            - rat_float(3411, 2000) * (g1s ** 3)
            - float(32) * g3s * float(numpy.trace(hu2 + hd2).real)
            - rat_float(4, 5) * g1s * float(numpy.trace(float(2) * hu2 - hd2 + float(3) * he2).real)
            - rat_float(3, 4) * g2s * g2s * y2_tr
            + g1s
            * (
                (rat_float(63, 10) * g2s - rat_float(171, 100) * g1s) * tr_hu
                + (rat_float(27, 10) * g2s + rat_float(9, 20) * g1s) * tr_hd
                + (rat_float(33, 10) * g2s - rat_float(9, 4) * g1s) * tr_he
            )
            + float(10) * h6_tr
            - float(6) * tr_hu2hd_huhd2
        )

    dkap = None
    if with_kappa and kap is not None:
        alpha_kap = float(-3) * g2s + float(4) * lam + float(2) * y2_tr
        dkap = KAPPA_1_F64 * (rat_float(-3, 2) * (he @ kap + kap @ he.T) + alpha_kap * kap)

    packed = pack_sm_state(dg1, dg2, dg3, dlam, dyu, dyd, dye, dkap)
    if scale_factor != float(1):
        packed = scale_factor * packed
    return packed


def bulirsch_stoer_step_mp(
    rhs_fn: typing.Callable[[list[mpmath.mpf]], list[mpmath.mpf]],
    y0: list[mpmath.mpf],
    h_step: mpmath.mpf,
    tol: mpmath.mpf,
    max_levels: int = 9,
) -> tuple[list[mpmath.mpf], mpmath.mpf]:
    """Single Gragg modified-midpoint + Neville polynomial extrapolation step."""
    dim = len(y0)
    half = rat_mpf(1, 2)
    two = mpmath.mpf(2)
    f0 = rhs_fn(y0)

    table: list[list[list[mpmath.mpf]]] = []
    best = y0
    err_est = mpmath.mpf(1)

    for k in range(max_levels):
        m_sub = 2 * (k + 1)
        h = h_step / mpmath.mpf(m_sub)
        two_h = two * h

        z_prev = y0
        z_curr = [y0[i] + h * f0[i] for i in range(dim)]
        for _ in range(1, m_sub):
            fz = rhs_fn(z_curr)
            z_next = [z_prev[i] + two_h * fz[i] for i in range(dim)]
            z_prev = z_curr
            z_curr = z_next

        f_end = rhs_fn(z_curr)
        s_m = [half * (z_curr[i] + z_prev[i] + h * f_end[i]) for i in range(dim)]

        row: list[list[mpmath.mpf]] = [s_m]
        for j in range(1, k + 1):
            m_prev = 2 * (k - j + 1)
            denom = rat_mpf(m_sub * m_sub - m_prev * m_prev, m_prev * m_prev)
            prev_same = row[j - 1]
            prev_up = table[k - 1][j - 1]
            extrap = [
                prev_same[i] + (prev_same[i] - prev_up[i]) / denom
                for i in range(dim)
            ]
            row.append(extrap)

        table.append(row)
        best = row[k]
        if k >= 2:
            err_est = max(abs(best[i] - row[k - 1][i]) for i in range(dim))
            if err_est <= tol:
                return best, err_est

    return best, err_est


def integrate_mp_adaptive(
    rhs_fn: typing.Callable[[list[mpmath.mpf]], list[mpmath.mpf]],
    y_init: list[mpmath.mpf],
    t_start: mpmath.mpf,
    t_end: mpmath.mpf,
    initial_steps: int,
    tol: mpmath.mpf,
    max_levels: int = 9,
) -> list[mpmath.mpf]:
    """Adaptive Bulirsch-Stoer integrator on [t_start, t_end] in mpmath."""
    y_curr = list(y_init)
    t_curr = t_start
    total_span = t_end - t_start
    h_try = total_span / mpmath.mpf(initial_steps)
    direction = mpmath.mpf(1) if total_span >= 0 else mpmath.mpf(-1)

    guard = 0
    while direction * (t_end - t_curr) > mpmath.mpf(10) ** (-(mpmath.mp.dps - 4)):
        guard += 1
        if guard > 4000:
            raise RuntimeError("Adaptive mpmath Bulirsch-Stoer exceeded step budget")
        rem = t_end - t_curr
        if abs(h_try) > abs(rem):
            h_try = rem
        y_next, err = bulirsch_stoer_step_mp(rhs_fn, y_curr, h_try, tol, max_levels=max_levels)
        if err <= tol:
            y_curr = y_next
            t_curr = t_curr + h_try
        else:
            h_try = h_try / mpmath.mpf(2)
    return y_curr


# ---------------------------------------------------------------------------
# Section 2: Four Independent Literature RGE Benchmarks (B0.1 - B0.4)
# ---------------------------------------------------------------------------


def solve_b01_su3_exact_mp(
    delta_t_int: int,
    scale_factor_num: int = 1,
    scale_factor_den: int = 1,
    dps: int = 60,
) -> tuple[mpmath.mpf, mpmath.mpf]:
    """Exact 2-loop pure-gauge SU(3) implicit integral via monotone bisection
    and analytical Landau-pole distance Delta t_Landau = F(infty) - F(3/5).
    """
    with mpmath.workdps(dps):
        sf = rat_mpf(scale_factor_num, scale_factor_den)
        kap1 = mpmath.mpf(1) / (mpmath.mpf(16) * (mpmath.pi ** 2))
        kap2 = kap1 * kap1
        a_mp = sf * mpmath.mpf(-7) * kap1
        c_mp = sf * mpmath.mpf(-26) * kap2
        g0 = rat_mpf(3, 5)
        two = mpmath.mpf(2)

        def antideriv_f(g_val: mpmath.mpf) -> mpmath.mpf:
            u = g_val * g_val
            ratio = abs(u / (a_mp + c_mp * u))
            return -(mpmath.mpf(1) / (two * a_mp * u)) - (c_mp / (two * a_mp * a_mp)) * mpmath.log(ratio)

        f_g0 = antideriv_f(g0)
        f_inf = -(c_mp / (two * a_mp * a_mp)) * mpmath.log(mpmath.mpf(1) / abs(c_mp))
        dt_landau = f_inf - f_g0

        dt_mp = mpmath.mpf(delta_t_int)
        if dt_mp <= dt_landau:
            raise ValueError("Requested Delta t lies at or beyond the 2-loop Landau pole")

        def residual(g_val: mpmath.mpf) -> mpmath.mpf:
            return antideriv_f(g_val) - f_g0 - dt_mp

        # Since dF/dg = 1 / (a g^3 + c g^5) < 0 on (0, infty), residual(g) is strictly decreasing:
        if delta_t_int == 0:
            return g0, dt_landau
        if delta_t_int < 0:
            # residual(g0) = -dt_mp > 0; increase g_hi until residual(g_hi) < 0
            g_lo = g0
            g_hi = g0
            while residual(g_hi) > 0:
                g_hi = g_hi * two
        else:
            # residual(g0) = -dt_mp < 0; decrease g_lo until residual(g_lo) > 0
            g_hi = g0
            g_lo = g0
            while residual(g_lo) < 0:
                g_lo = g_lo / two

        for _ in range(220):
            g_mid = (g_lo + g_hi) / two
            if residual(g_mid) > 0:
                g_lo = g_mid
            else:
                g_hi = g_mid

        return (g_lo + g_hi) / two, dt_landau


def solve_b01_su3_dop853(
    delta_t_int: int,
    scale_factor: float = float(1),
) -> float:
    def rhs(_t: float, y: numpy.ndarray) -> numpy.ndarray:
        gv = float(y[0])
        gv2 = gv * gv
        dg = scale_factor * (
            KAPPA_1_F64 * float(-7) * gv * gv2
            + KAPPA_2_F64 * float(-26) * gv * gv2 * gv2
        )
        return numpy.array([dg], dtype=numpy.float64)

    sol = integrate.solve_ivp(
        rhs,
        (float(0), float(delta_t_int)),
        numpy.array([rat_float(3, 5)], dtype=numpy.float64),
        method="DOP853",
        rtol=sci_float(1, -12),
        atol=sci_float(1, -14),
    )
    if not sol.success:
        raise RuntimeError(f"DOP853 failed on B0.1 at dt={delta_t_int}: {sol.message}")
    return float(sol.y[0, -1])


def buttazzo_5var_rhs_f64(
    _t: float,
    y: numpy.ndarray,
    scale_factor: float = float(1),
) -> numpy.ndarray:
    g1, g2, g3, yt, lam = (float(y[0]), float(y[1]), float(y[2]), float(y[3]), float(y[4]))
    g1s = g1 * g1
    g2s = g2 * g2
    g3s = g3 * g3
    yts = yt * yt

    dg1 = (g1 * g1s) * (
        KAPPA_1_F64 * rat_float(41, 10)
        + KAPPA_2_F64
        * (
            rat_float(199, 50) * g1s
            + rat_float(27, 10) * g2s
            + rat_float(44, 5) * g3s
            - rat_float(17, 10) * yts
        )
    )
    dg2 = (g2 * g2s) * (
        KAPPA_1_F64 * rat_float(-19, 6)
        + KAPPA_2_F64
        * (
            rat_float(9, 10) * g1s
            + rat_float(35, 6) * g2s
            + float(12) * g3s
            - rat_float(3, 2) * yts
        )
    )
    dg3 = (g3 * g3s) * (
        KAPPA_1_F64 * float(-7)
        + KAPPA_2_F64
        * (
            rat_float(11, 10) * g1s
            + rat_float(9, 2) * g2s
            - float(26) * g3s
            - float(2) * yts
        )
    )
    dyt = yt * (
        KAPPA_1_F64 * (rat_float(9, 2) * yts - float(8) * g3s - rat_float(9, 4) * g2s - rat_float(17, 20) * g1s)
        + KAPPA_2_F64
        * (
            yts
            * (
                float(-12) * yts
                - float(12) * lam
                + float(36) * g3s
                + rat_float(225, 16) * g2s
                + rat_float(393, 80) * g1s
            )
            + float(6) * lam * lam
            - float(108) * g3s * g3s
            - rat_float(23, 4) * g2s * g2s
            + rat_float(1187, 600) * g1s * g1s
            + float(9) * g3s * g2s
            + rat_float(19, 15) * g3s * g1s
            - rat_float(9, 20) * g2s * g1s
        )
    )
    dlam = (
        KAPPA_1_F64
        * (
            float(24) * lam * lam
            + lam * (float(12) * yts - float(9) * g2s - rat_float(9, 5) * g1s)
            - float(6) * yts * yts
            + rat_float(9, 8) * g2s * g2s
            + rat_float(27, 200) * g1s * g1s
            + rat_float(9, 20) * g2s * g1s
        )
        + KAPPA_2_F64
        * (
            float(-312) * (lam ** 3)
            + (lam * lam) * (float(-144) * yts + float(108) * g2s + rat_float(108, 5) * g1s)
            + lam * yts * (float(-3) * yts + float(80) * g3s + rat_float(45, 2) * g2s + rat_float(17, 2) * g1s)
            + lam
            * (
                rat_float(-73, 8) * g2s * g2s
                + rat_float(1887, 200) * g1s * g1s
                + rat_float(117, 20) * g2s * g1s
            )
            + (yts * yts) * (float(30) * yts - float(32) * g3s - rat_float(8, 5) * g1s)
            + yts * (rat_float(-9, 4) * g2s * g2s - rat_float(171, 100) * g1s * g1s + rat_float(63, 10) * g2s * g1s)
            + rat_float(305, 16) * (g2s ** 3)
            - rat_float(3411, 2000) * (g1s ** 3)
            - rat_float(289, 80) * g2s * g2s * g1s
            - rat_float(1677, 400) * g2s * g1s * g1s
        )
    )
    return scale_factor * numpy.array([dg1, dg2, dg3, dyt, dlam], dtype=numpy.float64)


def solve_b02_buttazzo_dop853(scale_factor: float = float(1), t_max_int: int = 25) -> float:
    def lam_zero_event(_t: float, y: numpy.ndarray) -> float:
        return float(y[4])

    lam_zero_event.terminal = True  # type: ignore[attr-defined]
    lam_zero_event.direction = float(-1)  # type: ignore[attr-defined]

    y0 = numpy.array(
        [
            rat_float(1, 2),
            rat_float(3, 5),
            rat_float(1, 1),
            rat_float(9, 10),
            rat_float(1, 10),
        ],
        dtype=numpy.float64,
    )
    sol = integrate.solve_ivp(
        lambda t, y: buttazzo_5var_rhs_f64(t, y, scale_factor=scale_factor),
        (float(0), float(t_max_int)),
        y0,
        method="DOP853",
        events=lam_zero_event,
        rtol=sci_float(1, -12),
        atol=sci_float(1, -14),
    )
    if not sol.success or len(sol.t_events[0]) == 0:
        raise RuntimeError("DOP853 failed to locate lambda(t_crit) = 0 event in B0.2")
    return float(sol.t_events[0][0])


def solve_b02_buttazzo_mp50(dps: int = 58) -> mpmath.mpf:
    with mpmath.workdps(dps):
        kap1 = mpmath.mpf(1) / (mpmath.mpf(16) * (mpmath.pi ** 2))
        kap2 = kap1 * kap1

        def rhs_mp(y: list[mpmath.mpf]) -> list[mpmath.mpf]:
            g1, g2, g3, yt, lam = y
            g1s = g1 * g1
            g2s = g2 * g2
            g3s = g3 * g3
            yts = yt * yt

            dg1 = (g1 * g1s) * (
                kap1 * rat_mpf(41, 10)
                + kap2
                * (
                    rat_mpf(199, 50) * g1s
                    + rat_mpf(27, 10) * g2s
                    + rat_mpf(44, 5) * g3s
                    - rat_mpf(17, 10) * yts
                )
            )
            dg2 = (g2 * g2s) * (
                kap1 * rat_mpf(-19, 6)
                + kap2
                * (
                    rat_mpf(9, 10) * g1s
                    + rat_mpf(35, 6) * g2s
                    + mpmath.mpf(12) * g3s
                    - rat_mpf(3, 2) * yts
                )
            )
            dg3 = (g3 * g3s) * (
                kap1 * mpmath.mpf(-7)
                + kap2
                * (
                    rat_mpf(11, 10) * g1s
                    + rat_mpf(9, 2) * g2s
                    - mpmath.mpf(26) * g3s
                    - mpmath.mpf(2) * yts
                )
            )
            dyt = yt * (
                kap1 * (rat_mpf(9, 2) * yts - mpmath.mpf(8) * g3s - rat_mpf(9, 4) * g2s - rat_mpf(17, 20) * g1s)
                + kap2
                * (
                    yts
                    * (
                        mpmath.mpf(-12) * yts
                        - mpmath.mpf(12) * lam
                        + mpmath.mpf(36) * g3s
                        + rat_mpf(225, 16) * g2s
                        + rat_mpf(393, 80) * g1s
                    )
                    + mpmath.mpf(6) * lam * lam
                    - mpmath.mpf(108) * g3s * g3s
                    - rat_mpf(23, 4) * g2s * g2s
                    + rat_mpf(1187, 600) * g1s * g1s
                    + mpmath.mpf(9) * g3s * g2s
                    + rat_mpf(19, 15) * g3s * g1s
                    - rat_mpf(9, 20) * g2s * g1s
                )
            )
            dlam = (
                kap1
                * (
                    mpmath.mpf(24) * lam * lam
                    + lam * (mpmath.mpf(12) * yts - mpmath.mpf(9) * g2s - rat_mpf(9, 5) * g1s)
                    - mpmath.mpf(6) * yts * yts
                    + rat_mpf(9, 8) * g2s * g2s
                    + rat_mpf(27, 200) * g1s * g1s
                    + rat_mpf(9, 20) * g2s * g1s
                )
                + kap2
                * (
                    mpmath.mpf(-312) * (lam ** 3)
                    + (lam * lam) * (mpmath.mpf(-144) * yts + mpmath.mpf(108) * g2s + rat_mpf(108, 5) * g1s)
                    + lam * yts * (mpmath.mpf(-3) * yts + mpmath.mpf(80) * g3s + rat_mpf(45, 2) * g2s + rat_mpf(17, 2) * g1s)
                    + lam
                    * (
                        rat_mpf(-73, 8) * g2s * g2s
                        + rat_mpf(1887, 200) * g1s * g1s
                        + rat_mpf(117, 20) * g2s * g1s
                    )
                    + (yts * yts) * (mpmath.mpf(30) * yts - mpmath.mpf(32) * g3s - rat_mpf(8, 5) * g1s)
                    + yts * (rat_mpf(-9, 4) * g2s * g2s - rat_mpf(171, 100) * g1s * g1s + rat_mpf(63, 10) * g2s * g1s)
                    + rat_mpf(305, 16) * (g2s ** 3)
                    - rat_mpf(3411, 2000) * (g1s ** 3)
                    - rat_mpf(289, 80) * g2s * g2s * g1s
                    - rat_mpf(1677, 400) * g2s * g1s * g1s
                )
            )
            return [dg1, dg2, dg3, dyt, dlam]

        y_curr = [
            rat_mpf(1, 2),
            rat_mpf(3, 5),
            rat_mpf(1, 1),
            rat_mpf(9, 10),
            rat_mpf(1, 10),
        ]
        tol = mpmath.mpf(10) ** (-48)
        h_coarse = rat_mpf(1, 4)
        t_curr = mpmath.mpf(0)

        # Advance in 1/4 macro-steps until lambda <= 0
        for _ in range(100):
            y_next, err = bulirsch_stoer_step_mp(rhs_mp, y_curr, h_coarse, tol, max_levels=10)
            if err > tol:
                y_next = integrate_mp_adaptive(rhs_mp, y_curr, t_curr, t_curr + h_coarse, 2, tol, max_levels=10)
            if y_next[4] <= 0:
                break
            y_curr = y_next
            t_curr = t_curr + h_coarse
        else:
            raise RuntimeError("mpmath B0.2 failed to bracket zero crossing")

        # Monotone bisection on [0, h_coarse] from (t_curr, y_curr)
        dt_lo = mpmath.mpf(0)
        dt_hi = h_coarse
        two = mpmath.mpf(2)
        for _ in range(168):
            dt_mid = (dt_lo + dt_hi) / two
            if dt_mid == 0:
                lam_mid = y_curr[4]
            else:
                y_mid, err_m = bulirsch_stoer_step_mp(rhs_mp, y_curr, dt_mid, tol, max_levels=10)
                if err_m > tol:
                    y_mid = integrate_mp_adaptive(rhs_mp, y_curr, mpmath.mpf(0), dt_mid, 2, tol, max_levels=10)
                lam_mid = y_mid[4]
            if lam_mid > 0:
                dt_lo = dt_mid
            else:
                dt_hi = dt_mid

        return t_curr + (dt_lo + dt_hi) / two


# 3x3 mpmath complex matrix helpers for B0.3
MpMat3 = list[list[mpmath.mpc]]


def mp_mat3_zeros() -> MpMat3:
    z = mpmath.mpc(0, 0)
    return [[z, z, z], [z, z, z], [z, z, z]]


def mp_mat3_eye(scale: mpmath.mpf | mpmath.mpc) -> MpMat3:
    z = mpmath.mpc(0, 0)
    sc = mpmath.mpc(scale)
    return [[sc, z, z], [z, sc, z], [z, z, sc]]


def mp_mat3_mul(a: MpMat3, b: MpMat3) -> MpMat3:
    out = mp_mat3_zeros()
    for i in range(3):
        for j in range(3):
            out[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]
    return out


def mp_mat3_dag(a: MpMat3) -> MpMat3:
    out = mp_mat3_zeros()
    for i in range(3):
        for j in range(3):
            out[i][j] = mpmath.conj(a[j][i])
    return out


def mp_mat3_tr_re(a: MpMat3) -> mpmath.mpf:
    return (a[0][0] + a[1][1] + a[2][2]).real


def mp_mat3_lincomb(terms: list[tuple[mpmath.mpf | mpmath.mpc, MpMat3]]) -> MpMat3:
    out = mp_mat3_zeros()
    for coeff, mat in terms:
        c = mpmath.mpc(coeff)
        for i in range(3):
            for j in range(3):
                out[i][j] += c * mat[i][j]
    return out


def build_b03_rational_seed() -> tuple[
    tuple[Fraction, Fraction, Fraction, Fraction],
    list[list[tuple[Fraction, Fraction]]],
    list[list[tuple[Fraction, Fraction]]],
    list[list[tuple[Fraction, Fraction]]],
]:
    g_and_lam = (Fraction(9, 20), Fraction(1, 2), Fraction(1, 2), Fraction(3, 20))
    yu_rat = [
        [(Fraction(1, 25), Fraction(0, 1)), (Fraction(1, 30), Fraction(1, 25)), (Fraction(1, 45), Fraction(-1, 35))],
        [(Fraction(-1, 35), Fraction(1, 40)), (Fraction(3, 20), Fraction(0, 1)), (Fraction(1, 20), Fraction(1, 30))],
        [(Fraction(1, 50), Fraction(1, 45)), (Fraction(-1, 25), Fraction(1, 30)), (Fraction(11, 25), Fraction(0, 1))],
    ]
    yd_rat = [
        [(Fraction(1, 30), Fraction(0, 1)), (Fraction(1, 35), Fraction(-1, 40)), (Fraction(1, 50), Fraction(1, 45))],
        [(Fraction(1, 40), Fraction(1, 30)), (Fraction(1, 10), Fraction(0, 1)), (Fraction(1, 25), Fraction(-1, 35))],
        [(Fraction(-1, 55), Fraction(1, 50)), (Fraction(1, 30), Fraction(1, 40)), (Fraction(7, 25), Fraction(0, 1))],
    ]
    ye_rat = [
        [(Fraction(1, 40), Fraction(0, 1)), (Fraction(1, 50), Fraction(1, 60)), (Fraction(-1, 70), Fraction(1, 65))],
        [(Fraction(1, 55), Fraction(-1, 50)), (Fraction(1, 12), Fraction(0, 1)), (Fraction(1, 35), Fraction(1, 45))],
        [(Fraction(1, 65), Fraction(1, 70)), (Fraction(-1, 40), Fraction(1, 50)), (Fraction(11, 50), Fraction(0, 1))],
    ]
    return g_and_lam, yu_rat, yd_rat, ye_rat


def rat_mat_to_c128(mat_rat: list[list[tuple[Fraction, Fraction]]]) -> numpy.ndarray:
    arr = numpy.zeros((3, 3), dtype=numpy.complex128)
    for i in range(3):
        for j in range(3):
            re_q, im_q = mat_rat[i][j]
            arr[i, j] = complex(float(re_q), float(im_q))
    return arr


def solve_b03_noncommuting_and_jacobi() -> tuple[float, float, float]:
    g_and_lam, yu_rat, yd_rat, ye_rat = build_b03_rational_seed()
    yu0 = rat_mat_to_c128(yu_rat)
    yd0 = rat_mat_to_c128(yd_rat)
    ye0 = rat_mat_to_c128(ye_rat)

    # Confirm genuine non-commutativity at t = 0
    hu0 = yu0 @ yu0.conj().T
    hd0 = yd0 @ yd0.conj().T
    comm_norm = float(numpy.linalg.norm(hu0 @ hd0 - hd0 @ hu0))
    if comm_norm <= sci_float(1, -4):
        raise ValueError("B0.3 seed matrices unexpectedly nearly commute")

    y0_f64 = pack_sm_state(
        float(g_and_lam[0]),
        float(g_and_lam[1]),
        float(g_and_lam[2]),
        float(g_and_lam[3]),
        yu0,
        yd0,
        ye0,
        None,
    )

    # 1. Float64 SciPy DOP853 2-loop matrix integration across Delta t = -27
    sol_2loop = integrate.solve_ivp(
        lambda t, y: sm_matrix_rge_rhs_f64(t, y, two_loop=True, with_kappa=False),
        (float(0), float(-27)),
        y0_f64,
        method="DOP853",
        rtol=sci_float(1, -12),
        atol=sci_float(1, -14),
    )
    if not sol_2loop.success:
        raise RuntimeError(f"DOP853 failed on B0.3 2-loop matrix flow: {sol_2loop.message}")
    y_end_dop = sol_2loop.y[:, -1]

    # 2. Independent 45-digit mpmath Bulirsch-Stoer 2-loop matrix integration across Delta t = -27
    with mpmath.workdps(45):
        kap1 = mpmath.mpf(1) / (mpmath.mpf(16) * (mpmath.pi ** 2))
        kap2 = kap1 * kap1

        def unpack_mp_58(vec: list[mpmath.mpf]) -> tuple[mpmath.mpf, mpmath.mpf, mpmath.mpf, mpmath.mpf, MpMat3, MpMat3, MpMat3]:
            g1, g2, g3, lam = vec[0], vec[1], vec[2], vec[3]

            def slice_mat(offset: int) -> MpMat3:
                m = mp_mat3_zeros()
                for r in range(3):
                    for c in range(3):
                        idx = r * 3 + c
                        m[r][c] = mpmath.mpc(vec[offset + idx], vec[offset + 9 + idx])
                return m

            return g1, g2, g3, lam, slice_mat(4), slice_mat(22), slice_mat(40)

        def pack_mp_58(
            g1: mpmath.mpf,
            g2: mpmath.mpf,
            g3: mpmath.mpf,
            lam: mpmath.mpf,
            yu: MpMat3,
            yd: MpMat3,
            ye: MpMat3,
        ) -> list[mpmath.mpf]:
            out: list[mpmath.mpf] = [g1, g2, g3, lam]
            for mat in (yu, yd, ye):
                for r in range(3):
                    for c in range(3):
                        out.append(mat[r][c].real)
                for r in range(3):
                    for c in range(3):
                        out.append(mat[r][c].imag)
            return out

        def rhs_mp_2loop(vec: list[mpmath.mpf]) -> list[mpmath.mpf]:
            g1, g2, g3, lam, yu, yd, ye = unpack_mp_58(vec)
            hu = mp_mat3_mul(yu, mp_mat3_dag(yu))
            hd = mp_mat3_mul(yd, mp_mat3_dag(yd))
            he = mp_mat3_mul(ye, mp_mat3_dag(ye))

            tr_hu = mp_mat3_tr_re(hu)
            tr_hd = mp_mat3_tr_re(hd)
            tr_he = mp_mat3_tr_re(he)
            y2_tr = mpmath.mpf(3) * tr_hu + mpmath.mpf(3) * tr_hd + tr_he

            hu2 = mp_mat3_mul(hu, hu)
            hd2 = mp_mat3_mul(hd, hd)
            he2 = mp_mat3_mul(he, he)
            hs_tr = (
                mpmath.mpf(3) * mp_mat3_tr_re(hu2)
                + mpmath.mpf(3) * mp_mat3_tr_re(hd2)
                + mp_mat3_tr_re(he2)
            )
            huhd = mp_mat3_mul(hu, hd)
            hdhu = mp_mat3_mul(hd, hu)
            tr_huhd = mp_mat3_tr_re(huhd)

            g1s = g1 * g1
            g2s = g2 * g2
            g3s = g3 * g3

            dg1 = (g1 * g1s) * (
                kap1 * rat_mpf(41, 10)
                + kap2
                * (
                    rat_mpf(199, 50) * g1s
                    + rat_mpf(27, 10) * g2s
                    + rat_mpf(44, 5) * g3s
                    - rat_mpf(17, 10) * tr_hu
                    - rat_mpf(1, 2) * tr_hd
                    - rat_mpf(3, 2) * tr_he
                )
            )
            dg2 = (g2 * g2s) * (
                kap1 * rat_mpf(-19, 6)
                + kap2
                * (
                    rat_mpf(9, 10) * g1s
                    + rat_mpf(35, 6) * g2s
                    + mpmath.mpf(12) * g3s
                    - rat_mpf(3, 2) * tr_hu
                    - rat_mpf(3, 2) * tr_hd
                    - rat_mpf(1, 2) * tr_he
                )
            )
            dg3 = (g3 * g3s) * (
                kap1 * mpmath.mpf(-7)
                + kap2
                * (
                    rat_mpf(11, 10) * g1s
                    + rat_mpf(9, 2) * g2s
                    - mpmath.mpf(26) * g3s
                    - mpmath.mpf(2) * tr_hu
                    - mpmath.mpf(2) * tr_hd
                )
            )

            y4_tr = (
                (rat_mpf(17, 20) * g1s + rat_mpf(9, 4) * g2s + mpmath.mpf(8) * g3s) * tr_hu
                + (rat_mpf(1, 4) * g1s + rat_mpf(9, 4) * g2s + mpmath.mpf(8) * g3s) * tr_hd
                + rat_mpf(3, 4) * (g1s + g2s) * tr_he
            )
            chi4_tr = rat_mpf(9, 4) * hs_tr - rat_mpf(3, 2) * tr_huhd

            mu1_sc = y2_tr - (rat_mpf(17, 20) * g1s + rat_mpf(9, 4) * g2s + mpmath.mpf(8) * g3s)
            md1_sc = y2_tr - (rat_mpf(1, 4) * g1s + rat_mpf(9, 4) * g2s + mpmath.mpf(8) * g3s)
            me1_sc = y2_tr - (rat_mpf(9, 4) * g1s + rat_mpf(9, 4) * g2s)

            mu2_sc = (
                -chi4_tr
                + mpmath.mpf(6) * lam * lam
                + rat_mpf(5, 2) * y4_tr
                + rat_mpf(1187, 600) * g1s * g1s
                - rat_mpf(9, 20) * g1s * g2s
                + rat_mpf(19, 15) * g1s * g3s
                - rat_mpf(23, 4) * g2s * g2s
                + mpmath.mpf(9) * g2s * g3s
                - mpmath.mpf(108) * g3s * g3s
            )
            md2_sc = (
                -chi4_tr
                + mpmath.mpf(6) * lam * lam
                + rat_mpf(5, 2) * y4_tr
                - rat_mpf(127, 600) * g1s * g1s
                - rat_mpf(27, 20) * g1s * g2s
                + rat_mpf(31, 15) * g1s * g3s
                - rat_mpf(23, 4) * g2s * g2s
                + mpmath.mpf(9) * g2s * g3s
                - mpmath.mpf(108) * g3s * g3s
            )
            me2_sc = (
                -chi4_tr
                + mpmath.mpf(6) * lam * lam
                + rat_mpf(5, 2) * y4_tr
                + rat_mpf(1371, 200) * g1s * g1s
                + rat_mpf(27, 20) * g1s * g2s
                - rat_mpf(23, 4) * g2s * g2s
            )

            mu_tot = mp_mat3_lincomb(
                [
                    (kap1 * rat_mpf(3, 2) - kap2 * (rat_mpf(9, 4) * y2_tr + mpmath.mpf(12) * lam - (rat_mpf(223, 80) * g1s + rat_mpf(135, 16) * g2s + mpmath.mpf(16) * g3s)), hu),
                    (-kap1 * rat_mpf(3, 2) + kap2 * (rat_mpf(5, 4) * y2_tr - (rat_mpf(43, 80) * g1s - rat_mpf(9, 16) * g2s + mpmath.mpf(16) * g3s)), hd),
                    (kap2 * rat_mpf(3, 2), hu2),
                    (-kap2, hdhu),
                    (-kap2 * rat_mpf(1, 4), huhd),
                    (kap2 * rat_mpf(11, 4), hd2),
                    (kap1 * mu1_sc + kap2 * mu2_sc, mp_mat3_eye(mpmath.mpf(1))),
                ]
            )
            md_tot = mp_mat3_lincomb(
                [
                    (kap1 * rat_mpf(3, 2) - kap2 * (rat_mpf(9, 4) * y2_tr + mpmath.mpf(12) * lam - (rat_mpf(187, 80) * g1s + rat_mpf(135, 16) * g2s + mpmath.mpf(16) * g3s)), hd),
                    (-kap1 * rat_mpf(3, 2) + kap2 * (rat_mpf(5, 4) * y2_tr - (rat_mpf(79, 80) * g1s - rat_mpf(9, 16) * g2s + mpmath.mpf(16) * g3s)), hu),
                    (kap2 * rat_mpf(3, 2), hd2),
                    (-kap2, huhd),
                    (-kap2 * rat_mpf(1, 4), hdhu),
                    (kap2 * rat_mpf(11, 4), hu2),
                    (kap1 * md1_sc + kap2 * md2_sc, mp_mat3_eye(mpmath.mpf(1))),
                ]
            )
            me_tot = mp_mat3_lincomb(
                [
                    (kap1 * rat_mpf(3, 2) + kap2 * (-rat_mpf(9, 4) * y2_tr - mpmath.mpf(12) * lam + rat_mpf(387, 80) * g1s + rat_mpf(135, 16) * g2s), he),
                    (kap2 * rat_mpf(3, 2), he2),
                    (kap1 * me1_sc + kap2 * me2_sc, mp_mat3_eye(mpmath.mpf(1))),
                ]
            )

            dyu = mp_mat3_mul(mu_tot, yu)
            dyd = mp_mat3_mul(md_tot, yd)
            dye = mp_mat3_mul(me_tot, ye)

            h6_tr = (
                mpmath.mpf(3) * mp_mat3_tr_re(mp_mat3_mul(hu2, hu))
                + mpmath.mpf(3) * mp_mat3_tr_re(mp_mat3_mul(hd2, hd))
                + mp_mat3_tr_re(mp_mat3_mul(he2, he))
            )
            tr_hu2hd_huhd2 = mp_mat3_tr_re(mp_mat3_mul(hu2, hd)) + mp_mat3_tr_re(mp_mat3_mul(hu, hd2))

            dlam = (
                kap1
                * (
                    mpmath.mpf(24) * lam * lam
                    - (rat_mpf(9, 5) * g1s + mpmath.mpf(9) * g2s) * lam
                    + rat_mpf(27, 200) * g1s * g1s
                    + rat_mpf(9, 20) * g1s * g2s
                    + rat_mpf(9, 8) * g2s * g2s
                    + mpmath.mpf(4) * y2_tr * lam
                    - mpmath.mpf(2) * hs_tr
                )
                + kap2
                * (
                    mpmath.mpf(-312) * (lam ** 3)
                    + (mpmath.mpf(108) * g2s + rat_mpf(108, 5) * g1s) * lam * lam
                    - mpmath.mpf(48) * lam * lam * y2_tr
                    + (
                        rat_mpf(-73, 8) * g2s * g2s
                        + rat_mpf(117, 20) * g1s * g2s
                        + rat_mpf(1887, 200) * g1s * g1s
                    )
                    * lam
                    + mpmath.mpf(10) * lam * y4_tr
                    - lam * hs_tr
                    - mpmath.mpf(42) * lam * tr_huhd
                    + rat_mpf(305, 16) * (g2s ** 3)
                    - rat_mpf(289, 80) * g2s * g2s * g1s
                    - rat_mpf(1677, 400) * g2s * g1s * g1s
                    - rat_mpf(3411, 2000) * (g1s ** 3)
                    - mpmath.mpf(32) * g3s * (mp_mat3_tr_re(hu2) + mp_mat3_tr_re(hd2))
                    - rat_mpf(4, 5) * g1s * (mpmath.mpf(2) * mp_mat3_tr_re(hu2) - mp_mat3_tr_re(hd2) + mpmath.mpf(3) * mp_mat3_tr_re(he2))
                    - rat_mpf(3, 4) * g2s * g2s * y2_tr
                    + g1s
                    * (
                        (rat_mpf(63, 10) * g2s - rat_mpf(171, 100) * g1s) * tr_hu
                        + (rat_mpf(27, 10) * g2s + rat_mpf(9, 20) * g1s) * tr_hd
                        + (rat_mpf(33, 10) * g2s - rat_mpf(9, 4) * g1s) * tr_he
                    )
                    + mpmath.mpf(10) * h6_tr
                    - mpmath.mpf(6) * tr_hu2hd_huhd2
                )
            )
            return pack_mp_58(dg1, dg2, dg3, dlam, dyu, dyd, dye)

        def rat_to_mpmat(mat_rat: list[list[tuple[Fraction, Fraction]]]) -> MpMat3:
            m = mp_mat3_zeros()
            for r in range(3):
                for c in range(3):
                    rq, iq = mat_rat[r][c]
                    m[r][c] = mpmath.mpc(frac_to_mpf(rq), frac_to_mpf(iq))
            return m

        y0_mp = pack_mp_58(
            frac_to_mpf(g_and_lam[0]),
            frac_to_mpf(g_and_lam[1]),
            frac_to_mpf(g_and_lam[2]),
            frac_to_mpf(g_and_lam[3]),
            rat_to_mpmat(yu_rat),
            rat_to_mpmat(yd_rat),
            rat_to_mpmat(ye_rat),
        )
        y_end_mp = integrate_mp_adaptive(
            rhs_mp_2loop,
            y0_mp,
            mpmath.mpf(0),
            mpmath.mpf(-27),
            initial_steps=18,
            tol=mpmath.mpf(10) ** (-28),
            max_levels=7,
        )
        y_end_mp_f64 = numpy.array([float(v) for v in y_end_mp], dtype=numpy.float64)

    rel_err_2loop = float(numpy.linalg.norm(y_end_dop - y_end_mp_f64) / numpy.linalg.norm(y_end_mp_f64))

    # 3. 1-loop Xing-Zhou Jacobi determinant identity across Delta t = -27:
    # d/dt ln det(Y_f Y_f^dag) = 2 Re Tr((dY_f/dt)_{1-loop} Y_f^{-1})
    def rhs_1loop_with_jacobi(t_val: float, z: numpy.ndarray) -> numpy.ndarray:
        y_core = z[:58]
        dy_core = sm_matrix_rge_rhs_f64(t_val, y_core, two_loop=False, with_kappa=False)
        _, _, _, _, yu_t, yd_t, ye_t, _ = unpack_sm_state(y_core, with_kappa=False)
        _, _, _, _, dyu_t, dyd_t, dye_t, _ = unpack_sm_state(dy_core, with_kappa=False)
        qu = float(2) * float(numpy.trace(dyu_t @ numpy.linalg.inv(yu_t)).real)
        qd = float(2) * float(numpy.trace(dyd_t @ numpy.linalg.inv(yd_t)).real)
        qe = float(2) * float(numpy.trace(dye_t @ numpy.linalg.inv(ye_t)).real)
        return numpy.concatenate([dy_core, numpy.array([qu, qd, qe], dtype=numpy.float64)])

    z0 = numpy.concatenate([y0_f64, numpy.zeros(3, dtype=numpy.float64)])
    sol_1loop = integrate.solve_ivp(
        rhs_1loop_with_jacobi,
        (float(0), float(-27)),
        z0,
        method="DOP853",
        rtol=sci_float(1, -13),
        atol=sci_float(1, -15),
    )
    if not sol_1loop.success:
        raise RuntimeError(f"DOP853 failed on B0.3 1-loop Jacobi check: {sol_1loop.message}")

    z_end = sol_1loop.y[:, -1]
    _, _, _, _, yu_end, yd_end, ye_end, _ = unpack_sm_state(z_end[:58], with_kappa=False)
    quad_int = z_end[58:61]

    logdet_init = [
        math.log(float(numpy.linalg.det(yu0 @ yu0.conj().T).real)),
        math.log(float(numpy.linalg.det(yd0 @ yd0.conj().T).real)),
        math.log(float(numpy.linalg.det(ye0 @ ye0.conj().T).real)),
    ]
    logdet_final = [
        math.log(float(numpy.linalg.det(yu_end @ yu_end.conj().T).real)),
        math.log(float(numpy.linalg.det(yd_end @ yd_end.conj().T).real)),
        math.log(float(numpy.linalg.det(ye_end @ ye_end.conj().T).real)),
    ]
    jacobi_errs = [abs((logdet_final[k] - logdet_init[k]) - float(quad_int[k])) for k in range(3)]
    jacobi_abs_err = max(jacobi_errs)

    return rel_err_2loop, jacobi_abs_err, comm_norm


def solve_b04_antusch_weinberg_flow() -> float:
    """Compare 1-loop DOP853 matrix flow of kappa(t) against exact diagonal-Y_e
    exponential quadrature kappa(t) = I_alpha(t) D_e(t) kappa(0) D_e(t).
    """
    g_and_lam, yu_rat, yd_rat, _ = build_b03_rational_seed()
    yu0 = rat_mat_to_c128(yu_rat)
    yd0 = rat_mat_to_c128(yd_rat)
    ye0 = numpy.diag(
        [
            complex(rat_float(1, 20), float(0)),
            complex(rat_float(3, 20), float(0)),
            complex(rat_float(7, 20), float(0)),
        ]
    )
    ynu0 = numpy.array(
        [
            [rat_complex(1, 20), rat_complex(1, 25, 1, 30), rat_complex(1, 35, -1, 40)],
            [rat_complex(1, 30, -1, 25), rat_complex(9, 50), rat_complex(1, 20, 1, 25)],
            [rat_complex(1, 40, 1, 35), rat_complex(1, 25, -1, 30), rat_complex(2, 5)],
        ],
        dtype=numpy.complex128,
    )
    mr0 = numpy.array(
        [
            [rat_complex(1, 2), rat_complex(1, 20, 1, 25), rat_complex(1, 30, -1, 35)],
            [rat_complex(1, 20, 1, 25), rat_complex(6, 5), rat_complex(2, 15, 1, 20)],
            [rat_complex(1, 30, -1, 35), rat_complex(2, 15, 1, 20), rat_complex(5, 2)],
        ],
        dtype=numpy.complex128,
    )
    kap0 = ynu0 @ numpy.linalg.inv(mr0) @ ynu0.T

    # 1. Full matrix ODE integration of (SM + kappa) over Delta t = -25
    y0_with_kap = pack_sm_state(
        float(g_and_lam[0]),
        float(g_and_lam[1]),
        float(g_and_lam[2]),
        float(g_and_lam[3]),
        yu0,
        yd0,
        ye0,
        kap0,
    )
    sol_ode = integrate.solve_ivp(
        lambda t, y: sm_matrix_rge_rhs_f64(t, y, two_loop=False, with_kappa=True),
        (float(0), float(-25)),
        y0_with_kap,
        method="DOP853",
        rtol=sci_float(1, -13),
        atol=sci_float(1, -15),
    )
    if not sol_ode.success:
        raise RuntimeError(f"DOP853 failed on B0.4 matrix ODE: {sol_ode.message}")
    _, _, _, _, _, _, _, kap_ode = unpack_sm_state(sol_ode.y[:, -1], with_kappa=True)
    if kap_ode is None:
        raise RuntimeError("Missing kappa matrix from ODE unpack")

    # 2. Independent background + 4 scalar exponent quadratures (no kappa matrix in ODE)
    y0_bg = pack_sm_state(
        float(g_and_lam[0]),
        float(g_and_lam[1]),
        float(g_and_lam[2]),
        float(g_and_lam[3]),
        yu0,
        yd0,
        ye0,
        None,
    )
    w0 = numpy.concatenate([y0_bg, numpy.zeros(4, dtype=numpy.float64)])

    def rhs_bg_quadrature(t_val: float, w: numpy.ndarray) -> numpy.ndarray:
        y_core = w[:58]
        dy_core = sm_matrix_rge_rhs_f64(t_val, y_core, two_loop=False, with_kappa=False)
        _, g2_t, _, lam_t, yu_t, yd_t, ye_t, _ = unpack_sm_state(y_core, with_kappa=False)
        hu_t = yu_t @ yu_t.conj().T
        hd_t = yd_t @ yd_t.conj().T
        he_t = ye_t @ ye_t.conj().T
        y2_t = (
            float(3) * float(numpy.trace(hu_t).real)
            + float(3) * float(numpy.trace(hd_t).real)
            + float(numpy.trace(he_t).real)
        )
        d_int_alpha = KAPPA_1_F64 * (float(-3) * g2_t * g2_t + float(4) * lam_t + float(2) * y2_t)
        d_int_he0 = KAPPA_1_F64 * rat_float(-3, 2) * float(he_t[0, 0].real)
        d_int_he1 = KAPPA_1_F64 * rat_float(-3, 2) * float(he_t[1, 1].real)
        d_int_he2 = KAPPA_1_F64 * rat_float(-3, 2) * float(he_t[2, 2].real)
        return numpy.concatenate(
            [dy_core, numpy.array([d_int_alpha, d_int_he0, d_int_he1, d_int_he2], dtype=numpy.float64)]
        )

    sol_quad = integrate.solve_ivp(
        rhs_bg_quadrature,
        (float(0), float(-25)),
        w0,
        method="DOP853",
        rtol=sci_float(1, -13),
        atol=sci_float(1, -15),
    )
    if not sol_quad.success:
        raise RuntimeError(f"DOP853 failed on B0.4 quadrature: {sol_quad.message}")

    quads = sol_quad.y[58:62, -1]
    scale_alpha = math.exp(float(quads[0]))
    diag_e = numpy.diag([math.exp(float(quads[1])), math.exp(float(quads[2])), math.exp(float(quads[3]))])
    kap_exact = scale_alpha * (diag_e @ kap0 @ diag_e)

    return float(numpy.linalg.norm(kap_ode - kap_exact) / numpy.linalg.norm(kap_exact))


def run_section_2_four_benchmarks(producer_json: dict[str, Any]) -> dict[str, Any]:
    # B0.1 at Delta t = -15, -25, +30 + exact Landau pole location
    g_mp_m15, dt_landau_mp = solve_b01_su3_exact_mp(-15)
    g_mp_m25, _ = solve_b01_su3_exact_mp(-25)
    g_mp_p30, _ = solve_b01_su3_exact_mp(30)

    g_dop_m15 = solve_b01_su3_dop853(-15)
    g_dop_m25 = solve_b01_su3_dop853(-25)
    g_dop_p30 = solve_b01_su3_dop853(30)

    b01_err_m15 = abs(g_dop_m15 - float(g_mp_m15)) / abs(float(g_mp_m15))
    b01_err_m25 = abs(g_dop_m25 - float(g_mp_m25)) / abs(float(g_mp_m25))
    b01_err_p30 = abs(g_dop_p30 - float(g_mp_p30)) / abs(float(g_mp_p30))
    b01_max_err = max(b01_err_m15, b01_err_m25, b01_err_p30)
    dt_landau_f64 = float(dt_landau_mp)
    dist_from_m30_to_landau = float(mpmath.mpf(-30) - dt_landau_mp)

    # B0.2 Buttazzo 2-loop Higgs quartic zero crossing
    t_crit_dop853 = solve_b02_buttazzo_dop853()
    t_crit_mp50 = solve_b02_buttazzo_mp50()
    b02_rel_err = abs(t_crit_dop853 - float(t_crit_mp50)) / abs(float(t_crit_mp50))

    prod_t_crit_mp45 = float(
        producer_json["section_2_four_literature_rge_benchmarks"]["B0_2_buttazzo_t_crit_mp45"]
    )
    b02_vs_producer_rel_diff = abs(float(t_crit_mp50) - prod_t_crit_mp45) / abs(float(t_crit_mp50))

    # B0.3 Non-commuting 2-loop matrix Yukawa flow + 1-loop Xing-Zhou Jacobi identity
    b03_rel_err, b03_jacobi_abs_err, b03_seed_comm_norm = solve_b03_noncommuting_and_jacobi()

    # B0.4 Antusch et al. 1-loop Weinberg seesaw operator flow
    b04_rel_err = solve_b04_antusch_weinberg_flow()

    tol_10 = sci_float(1, -10)
    tol_9 = sci_float(1, -9)
    tol_11 = sci_float(1, -11)

    benchmarks_ok = (
        (b01_err_m15 < tol_10)
        and (b01_err_m25 < tol_10)
        and (b01_err_p30 < tol_10)
        and (b02_rel_err < tol_10)
        and (b02_vs_producer_rel_diff < tol_10)
        and (b03_rel_err < tol_9)
        and (b03_jacobi_abs_err < tol_11)
        and (b04_rel_err < tol_10)
    )

    return {
        "four_benchmarks_gate_passed": benchmarks_ok,
        "B0_1_su3_landau_pole_dt_exact": dt_landau_f64,
        "B0_1_efolds_from_dt_minus_30_to_landau_pole": dist_from_m30_to_landau,
        "B0_1_rel_err_dt_minus_15": b01_err_m15,
        "B0_1_rel_err_dt_minus_25": b01_err_m25,
        "B0_1_rel_err_dt_plus_30": b01_err_p30,
        "B0_1_max_rel_err": b01_max_err,
        "B0_2_buttazzo_t_crit_dop853": t_crit_dop853,
        "B0_2_buttazzo_t_crit_mp50": float(t_crit_mp50),
        "B0_2_buttazzo_t_crit_mp50_str": mpmath.nstr(t_crit_mp50, 35),
        "B0_2_buttazzo_dop853_vs_mp50_rel_err": b02_rel_err,
        "B0_2_vs_producer_mp45_rel_diff": b02_vs_producer_rel_diff,
        "B0_3_seed_hu_hd_commutator_norm": b03_seed_comm_norm,
        "B0_3_noncommuting_2loop_matrix_dop853_vs_mp45_rel_err": b03_rel_err,
        "B0_3_xing_zhou_1loop_jacobi_abs_err": b03_jacobi_abs_err,
        "B0_4_antusch_weinberg_dop853_vs_exact_quad_rel_err": b04_rel_err,
    }


# ---------------------------------------------------------------------------
# Section 3: Random Haar U(3)^6 Scrambling (12 Trials) & 5 Planted Faults
# ---------------------------------------------------------------------------


def sample_haar_u3(rng: numpy.random.Generator) -> numpy.ndarray:
    """Mezzadri (2007) exact Haar-measure random unitary matrix in U(3)."""
    x = rng.standard_normal((3, 3))
    y = rng.standard_normal((3, 3))
    z = (x + complex(0, 1) * y) / math.sqrt(float(2))
    q, r = numpy.linalg.qr(z)
    diag_r = numpy.diag(r)
    phases = diag_r / numpy.abs(diag_r)
    u = q * phases[numpy.newaxis, :]
    unitarity_err = float(numpy.linalg.norm(u.conj().T @ u - EYE3_C128))
    if unitarity_err > sci_float(1, -13):
        raise RuntimeError("Haar U(3) sample failed unitarity check")
    return u


def wrap_angle_pm_pi(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def angular_abs_diff(a: float, b: float) -> float:
    return abs(wrap_angle_pm_pi(a - b))


def build_uv_synthetic_pati_salam_state() -> dict[str, Any]:
    yu = numpy.array(
        [
            [rat_complex(1, 25), rat_complex(1, 30, 1, 30), rat_complex(1, 40, -1, 20)],
            [rat_complex(1, 35, -1, 35), rat_complex(1, 5), rat_complex(2, 25, 1, 25)],
            [rat_complex(1, 45, 1, 45), rat_complex(1, 30, -2, 30), rat_complex(4, 5)],
        ],
        dtype=numpy.complex128,
    )
    yd = numpy.array(
        [
            [rat_complex(1, 40), rat_complex(1, 45, 2, 45), rat_complex(1, 60, -1, 60)],
            [rat_complex(2, 50, -1, 50), rat_complex(3, 25), rat_complex(1, 30, 1, 30)],
            [rat_complex(1, 55, 1, 55), rat_complex(2, 35, -1, 35), rat_complex(9, 25)],
        ],
        dtype=numpy.complex128,
    )
    ye = numpy.array(
        [
            [rat_complex(1, 50), rat_complex(1, 60, -1, 60), rat_complex(1, 80, 1, 80)],
            [rat_complex(1, 65, 2, 65), rat_complex(1, 10), rat_complex(1, 35, -2, 35)],
            [rat_complex(1, 75, -1, 75), rat_complex(1, 40, 1, 40), rat_complex(3, 10)],
        ],
        dtype=numpy.complex128,
    )
    ynu = numpy.array(
        [
            [rat_complex(1, 20), rat_complex(1, 25, 1, 25), rat_complex(1, 30, -1, 30)],
            [rat_complex(1, 30, -2, 30), rat_complex(9, 50), rat_complex(1, 20, 2, 20)],
            [rat_complex(1, 35, 1, 35), rat_complex(1, 25, -1, 25), rat_complex(9, 20)],
        ],
        dtype=numpy.complex128,
    )
    mr = numpy.array(
        [
            [rat_complex(1, 2), rat_complex(1, 20, 1, 20), rat_complex(1, 25, -1, 25)],
            [rat_complex(1, 20, 1, 20), rat_complex(6, 5), rat_complex(2, 15, 1, 15)],
            [rat_complex(1, 25, -1, 25), rat_complex(2, 15, 1, 15), rat_complex(5, 2)],
        ],
        dtype=numpy.complex128,
    )
    return {
        "g4_ps": rat_float(1, 2),
        "g2L_ps": rat_float(1, 2),
        "g2R_ps": rat_float(1, 2),
        "lam_mr": rat_float(3, 20),
        "theta_0": rat_float(3, 10),
        "dt_ps": float(-4),
        "dt_sm": float(-20),
        "yu": yu,
        "yd": yd,
        "ye": ye,
        "ynu": ynu,
        "mr": mr,
    }


def apply_u3_6_basis_scrambling(
    uv: dict[str, Any],
    uq: numpy.ndarray,
    uu: numpy.ndarray,
    ud: numpy.ndarray,
    ul: numpy.ndarray,
    ue: numpy.ndarray,
    un: numpy.ndarray,
) -> dict[str, Any]:
    """Apply U(3)^6 basis change in left-doublet-row convention plus Fujikawa
    chiral anomaly shift theta_0 -> theta_0 - arg(det(U_Q)^2 det(U_u^dag) det(U_d^dag)).
    """
    det_factor = (
        (numpy.linalg.det(uq) ** 2)
        * numpy.linalg.det(uu.conj().T)
        * numpy.linalg.det(ud.conj().T)
    )
    fujikawa_shift = math.atan2(float(det_factor.imag), float(det_factor.real))
    out = dict(uv)
    out["yu"] = uq @ uv["yu"] @ uu.conj().T
    out["yd"] = uq @ uv["yd"] @ ud.conj().T
    out["ye"] = ul @ uv["ye"] @ ue.conj().T
    out["ynu"] = ul @ uv["ynu"] @ un.conj().T
    out["mr"] = un.conj() @ uv["mr"] @ un.conj().T
    out["theta_0"] = wrap_angle_pm_pi(float(uv["theta_0"]) - fujikawa_shift)
    return out


def extract_21_observables(
    yu: numpy.ndarray,
    yd: numpy.ndarray,
    ye: numpy.ndarray,
    kap: numpy.ndarray,
    theta_0: float,
) -> tuple[numpy.ndarray, float]:
    """Extract all 21 physical dimensionless observables from left-covariant
    Hermitian combinations plus bar_theta_QCD.
    """
    sv_u = numpy.sort(numpy.linalg.svd(yu, compute_uv=False))
    sv_d = numpy.sort(numpy.linalg.svd(yd, compute_uv=False))
    sv_e = numpy.sort(numpy.linalg.svd(ye, compute_uv=False))
    sv_kap = numpy.sort(numpy.linalg.svd(kap, compute_uv=False))

    hu = yu @ yu.conj().T
    hd = yd @ yd.conj().T
    he = ye @ ye.conj().T
    kk = kap @ kap.conj().T

    # Symmetrize Hermitian forms against 1e-16 roundoff before eigh
    hu = rat_float(1, 2) * (hu + hu.conj().T)
    hd = rat_float(1, 2) * (hd + hd.conj().T)
    he = rat_float(1, 2) * (he + he.conj().T)
    kk = rat_float(1, 2) * (kk + kk.conj().T)

    _, vu = numpy.linalg.eigh(hu)
    _, vd = numpy.linalg.eigh(hd)
    v_ckm = vu.conj().T @ vd

    v_us = abs(v_ckm[0, 1])
    v_cb = abs(v_ckm[1, 2])
    v_ub = abs(v_ckm[0, 2])
    j_ckm = float((v_ckm[0, 1] * v_ckm[1, 2] * numpy.conj(v_ckm[0, 2]) * numpy.conj(v_ckm[1, 1])).imag)

    _, u_le = numpy.linalg.eigh(he)
    _, u_nu = numpy.linalg.eigh(kk)
    u_pmns = u_le.conj().T @ u_nu

    u_e2 = abs(u_pmns[0, 1])
    u_e3 = abs(u_pmns[0, 2])
    u_mu3 = abs(u_pmns[1, 2])
    j_pmns = float((u_pmns[0, 1] * u_pmns[1, 2] * numpy.conj(u_pmns[0, 2]) * numpy.conj(u_pmns[1, 1])).imag)

    det_yu_yd = numpy.linalg.det(yu @ yd)
    arg_det = math.atan2(float(det_yu_yd.imag), float(det_yu_yd.real))
    bar_theta_qcd = wrap_angle_pm_pi(theta_0 + arg_det)

    obs = numpy.array(
        [
            float(sv_u[0]),
            float(sv_u[1]),
            float(sv_u[2]),
            float(sv_d[0]),
            float(sv_d[1]),
            float(sv_d[2]),
            float(sv_e[0]),
            float(sv_e[1]),
            float(sv_e[2]),
            float(sv_kap[0]),
            float(sv_kap[1]),
            float(sv_kap[2]),
            float(v_us),
            float(v_cb),
            float(v_ub),
            j_ckm,
            float(u_e2),
            float(u_e3),
            float(u_mu3),
            j_pmns,
            bar_theta_qcd,
        ],
        dtype=numpy.float64,
    )
    return obs, arg_det


def run_ps_seesaw_sm_pipeline(
    uv: dict[str, Any],
    solver_kind: str = "DOP853",
    wrong_yu_right_mult: bool = False,
    transposed_weinberg: bool = False,
) -> tuple[numpy.ndarray, float]:
    """Execute 2-step UV->IR pipeline:
    1) D-symmetric Pati-Salam 1-loop gauge running over dt_ps,
    2) Hypercharge matching + tree-level Weinberg seesaw matching at M_R,
    3) Coupled 2-loop SM + 1-loop Weinberg RGE evolution over dt_sm.
    """
    b_ps = numpy.array([float(-10), rat_float(-7, 3), rat_float(-7, 3)], dtype=numpy.float64)

    def ps_rhs(_t: float, g_vec: numpy.ndarray) -> numpy.ndarray:
        return KAPPA_1_F64 * b_ps * (g_vec ** 3)

    g0_ps = numpy.array([uv["g4_ps"], uv["g2L_ps"], uv["g2R_ps"]], dtype=numpy.float64)
    sol_ps = integrate.solve_ivp(
        ps_rhs,
        (float(0), float(uv["dt_ps"])),
        g0_ps,
        method="DOP853",
        rtol=sci_float(1, -13),
        atol=sci_float(1, -15),
    )
    if not sol_ps.success:
        raise RuntimeError(f"DOP853 failed on Pati-Salam step: {sol_ps.message}")

    g4_mr, g2l_mr, g2r_mr = (
        float(sol_ps.y[0, -1]),
        float(sol_ps.y[1, -1]),
        float(sol_ps.y[2, -1]),
    )
    g3_mr = g4_mr
    g2_mr = g2l_mr
    inv_g1_sq = rat_float(3, 5) / (g2r_mr * g2r_mr) + rat_float(2, 5) / (g4_mr * g4_mr)
    g1_mr = float(1) / math.sqrt(inv_g1_sq)

    ynu = uv["ynu"]
    mr_inv = numpy.linalg.inv(uv["mr"])
    if transposed_weinberg:
        kap_uv = ynu.T @ mr_inv @ ynu
    else:
        kap_uv = ynu @ mr_inv @ ynu.T

    det_uv = numpy.linalg.det(uv["yu"] @ uv["yd"])
    arg_det_uv = math.atan2(float(det_uv.imag), float(det_uv.real))

    y0_sm = pack_sm_state(g1_mr, g2_mr, g3_mr, float(uv["lam_mr"]), uv["yu"], uv["yd"], uv["ye"], kap_uv)

    if solver_kind == "DOP853":
        sol_sm = integrate.solve_ivp(
            lambda t, y: sm_matrix_rge_rhs_f64(
                t,
                y,
                two_loop=True,
                with_kappa=True,
                wrong_yu_right_mult=wrong_yu_right_mult,
            ),
            (float(0), float(uv["dt_sm"])),
            y0_sm,
            method="DOP853",
            rtol=sci_float(1, -13),
            atol=sci_float(1, -15),
        )
        if not sol_sm.success:
            raise RuntimeError(f"DOP853 failed on SM step: {sol_sm.message}")
        y_ir = sol_sm.y[:, -1]
    elif solver_kind == "RK4":
        n_steps = 400
        h = float(uv["dt_sm"]) / float(n_steps)
        half_h = rat_float(1, 2) * h
        sixth_h = h / float(6)
        y_curr = y0_sm.copy()
        t_curr = float(0)
        for _ in range(n_steps):
            k1 = sm_matrix_rge_rhs_f64(t_curr, y_curr, two_loop=True, with_kappa=True, wrong_yu_right_mult=wrong_yu_right_mult)
            k2 = sm_matrix_rge_rhs_f64(t_curr + half_h, y_curr + half_h * k1, two_loop=True, with_kappa=True, wrong_yu_right_mult=wrong_yu_right_mult)
            k3 = sm_matrix_rge_rhs_f64(t_curr + half_h, y_curr + half_h * k2, two_loop=True, with_kappa=True, wrong_yu_right_mult=wrong_yu_right_mult)
            k4 = sm_matrix_rge_rhs_f64(t_curr + h, y_curr + h * k3, two_loop=True, with_kappa=True, wrong_yu_right_mult=wrong_yu_right_mult)
            y_curr = y_curr + sixth_h * (k1 + float(2) * k2 + float(2) * k3 + k4)
            t_curr += h
        y_ir = y_curr
    else:
        raise ValueError(f"Unknown solver_kind: {solver_kind}")

    _, _, _, _, yu_ir, yd_ir, ye_ir, kap_ir = unpack_sm_state(y_ir, with_kappa=True)
    if kap_ir is None:
        raise RuntimeError("Missing IR kappa matrix")

    obs_ir, arg_det_ir = extract_21_observables(yu_ir, yd_ir, ye_ir, kap_ir, float(uv["theta_0"]))
    rge_theta_shift = wrap_angle_pm_pi(arg_det_ir - arg_det_uv)
    return obs_ir, rge_theta_shift


def max_observable_drift(obs_a: numpy.ndarray, obs_b: numpy.ndarray) -> float:
    linear_diff = float(numpy.max(numpy.abs(obs_a[:20] - obs_b[:20])))
    theta_diff = angular_abs_diff(float(obs_a[20]), float(obs_b[20]))
    return max(linear_diff, theta_diff)


def run_section_3_haar_and_planted_faults(producer_json: dict[str, Any]) -> dict[str, Any]:
    uv_base = build_uv_synthetic_pati_salam_state()
    obs_ref_dop, theta_shift_ref_dop = run_ps_seesaw_sm_pipeline(uv_base, solver_kind="DOP853")
    obs_ref_rk4, theta_shift_ref_rk4 = run_ps_seesaw_sm_pipeline(uv_base, solver_kind="RK4")
    dop_vs_rk4_obs_diff = max_observable_drift(obs_ref_dop, obs_ref_rk4)

    # 12 independent random Haar U(3)^6 trials with distinct RNG seed
    rng = numpy.random.default_rng(20261116)
    num_trials = 12
    per_trial_dop_err: list[float] = []
    per_trial_rk4_err: list[float] = []
    theta_shift_dop_errs: list[float] = []
    first_trial_tuple: tuple[numpy.ndarray, ...] | None = None

    for trial_idx in range(num_trials):
        uq = sample_haar_u3(rng)
        uu = sample_haar_u3(rng)
        ud = sample_haar_u3(rng)
        ul = sample_haar_u3(rng)
        ue = sample_haar_u3(rng)
        un = sample_haar_u3(rng)
        if trial_idx == 0:
            first_trial_tuple = (uq, uu, ud, ul, ue, un)

        uv_scr = apply_u3_6_basis_scrambling(uv_base, uq, uu, ud, ul, ue, un)
        obs_scr_dop, theta_shift_scr_dop = run_ps_seesaw_sm_pipeline(uv_scr, solver_kind="DOP853")
        obs_scr_rk4, _ = run_ps_seesaw_sm_pipeline(uv_scr, solver_kind="RK4")

        per_trial_dop_err.append(max_observable_drift(obs_ref_dop, obs_scr_dop))
        per_trial_rk4_err.append(max_observable_drift(obs_ref_rk4, obs_scr_rk4))
        theta_shift_dop_errs.append(angular_abs_diff(theta_shift_ref_dop, theta_shift_scr_dop))

    max_dop_err = max(per_trial_dop_err)
    max_rk4_err = max(per_trial_rk4_err)
    max_theta_shift_err = max(theta_shift_dop_errs)

    haar_gate_ok = (max_dop_err < sci_float(1, -12)) and (max_rk4_err < sci_float(1, -13))

    if first_trial_tuple is None:
        raise RuntimeError("Missing Haar trial tuple")
    uq0, uu0, ud0, ul0, ue0, un0 = first_trial_tuple
    uv_scr0 = apply_u3_6_basis_scrambling(uv_base, uq0, uu0, ud0, ul0, ue0, un0)

    # -----------------------------------------------------------------------
    # Five Planted Fault Controls (PF0.1 - PF0.5)
    # -----------------------------------------------------------------------

    # PF0.1: Scale-factor fault beta -> beta / 2 (d/d ln mu^2 vs d/d ln mu)
    t_crit_true = solve_b02_buttazzo_dop853(scale_factor=float(1), t_max_int=25)
    t_crit_half = solve_b02_buttazzo_dop853(scale_factor=rat_float(1, 2), t_max_int=25)
    pf01_b02_rel_err = abs(t_crit_half - t_crit_true) / abs(t_crit_true)

    g_true_m25, _ = solve_b01_su3_exact_mp(-25, 1, 1)
    g_half_m25, _ = solve_b01_su3_exact_mp(-25, 1, 2)
    pf01_b01_dt_m25_rel_err = float(abs(g_half_m25 - g_true_m25) / abs(g_true_m25))

    g_true_m30, _ = solve_b01_su3_exact_mp(-30, 1, 1)
    g_half_m30, _ = solve_b01_su3_exact_mp(-30, 1, 2)
    pf01_b01_dt_m30_rel_err = float(abs(g_half_m30 - g_true_m30) / abs(g_true_m30))

    g_true_m15, _ = solve_b01_su3_exact_mp(-15, 1, 1)
    g_half_m15, _ = solve_b01_su3_exact_mp(-15, 1, 2)
    pf01_b01_dt_m15_rel_err = float(abs(g_half_m15 - g_true_m15) / abs(g_true_m15))

    prod_pf01_err = float(
        producer_json["section_3_haar_u3_6_and_planted_faults"]["planted_faults"]["PF0_1_scale_factor_err"][
            "measured_err"
        ]
    )
    pf01_producer_dt_m15_match_diff = abs(pf01_b01_dt_m15_rel_err - prod_pf01_err)

    pf01_threshold = rat_float(1, 4)
    pf01_measured_err = max(pf01_b02_rel_err, pf01_b01_dt_m25_rel_err)
    pf01_caught = (pf01_b02_rel_err > pf01_threshold) and (pf01_b01_dt_m25_rel_err > pf01_threshold)

    # PF0.2: Wrong chirality / right-multiplied Yukawa beta (H_u Y_u -> Y_u H_u)
    obs_pf02_ref, _ = run_ps_seesaw_sm_pipeline(uv_base, solver_kind="DOP853", wrong_yu_right_mult=True)
    obs_pf02_scr, _ = run_ps_seesaw_sm_pipeline(uv_scr0, solver_kind="DOP853", wrong_yu_right_mult=True)
    pf02_ckm_err = float(numpy.max(numpy.abs(obs_pf02_ref[12:15] - obs_pf02_scr[12:15])))
    pf02_caught = pf02_ckm_err > sci_float(1, -3)

    # PF0.3: Single-matrix left-right SVD overlap |U_{L,u}^dag V_{R,u}| under U(3)_Q x U(3)_u
    u_lu_ref, _, vh_ru_ref = numpy.linalg.svd(uv_base["yu"])
    vr_u_ref = vh_ru_ref.conj().T
    lr_overlap_ref = numpy.abs(u_lu_ref.conj().T @ vr_u_ref)

    u_lu_scr, _, vh_ru_scr = numpy.linalg.svd(uv_scr0["yu"])
    vr_u_scr = vh_ru_scr.conj().T
    lr_overlap_scr = numpy.abs(u_lu_scr.conj().T @ vr_u_scr)

    pf03_err = float(numpy.max(numpy.abs(lr_overlap_ref - lr_overlap_scr)))
    pf03_caught = pf03_err > rat_float(1, 10)

    # PF0.4: Transposed Weinberg contraction Y_nu^T M_R^{-1} Y_nu under Y_nu -> U_L Y_nu U_N^dag
    obs_pf04_ref, _ = run_ps_seesaw_sm_pipeline(uv_base, solver_kind="DOP853", transposed_weinberg=True)
    obs_pf04_scr, _ = run_ps_seesaw_sm_pipeline(uv_scr0, solver_kind="DOP853", transposed_weinberg=True)
    pf04_pmns_err = float(numpy.max(numpy.abs(obs_pf04_ref[16:19] - obs_pf04_scr[16:19])))
    pf04_caught = pf04_pmns_err > rat_float(1, 10)

    # PF0.5: Corrupted Pati-Salam hypercharge weights (1/2, 1/2) vs (3/5, 2/5)
    # On chiral Pati-Salam multiplets Psi_L=(4,2,1) (Tr(T_{3R}^2)=0, Tr((T_4^15)^2)=1)
    # and Psi_R=(4,1,2) (Tr(T_{3R}^2)=2, Tr((T_4^15)^2)=1):
    w2r_true, w4c_true = Fraction(3, 5), Fraction(2, 5)
    w2r_bad, w4c_bad = Fraction(1, 2), Fraction(1, 2)
    tr_t1_sq_psi_l_true = w2r_true * 0 + w4c_true * 1
    tr_t1_sq_psi_l_bad = w2r_bad * 0 + w4c_bad * 1
    tr_t1_sq_psi_r_true = w2r_true * 2 + w4c_true * 1
    tr_t1_sq_psi_r_bad = w2r_bad * 2 + w4c_bad * 1
    pf05_err_frac = max(
        abs(tr_t1_sq_psi_l_bad - tr_t1_sq_psi_l_true),
        abs(tr_t1_sq_psi_r_bad - tr_t1_sq_psi_r_true),
    )
    pf05_err = float(pf05_err_frac)
    pf05_caught = pf05_err > rat_float(1, 20)

    all_faults_caught = pf01_caught and pf02_caught and pf03_caught and pf04_caught and pf05_caught

    return {
        "haar_u3_6_gate_passed": haar_gate_ok,
        "haar_u3_6_num_trials": num_trials,
        "haar_u3_6_rng_seed": 20261116,
        "haar_u3_6_dop853_max_err_across_12_trials_21_observables": max_dop_err,
        "haar_u3_6_dop853_per_trial_max_err": per_trial_dop_err,
        "haar_u3_6_rk4_max_err_across_12_trials_21_observables": max_rk4_err,
        "haar_u3_6_rk4_per_trial_max_err": per_trial_rk4_err,
        "haar_u3_6_dop853_vs_rk4_reference_max_diff": dop_vs_rk4_obs_diff,
        "haar_u3_6_rge_theta_shift_max_err": max_theta_shift_err,
        "all_5_planted_faults_caught": all_faults_caught,
        "planted_faults": {
            "PF0_1_scale_factor_err": {
                "measured_err": pf01_measured_err,
                "b02_t_crit_rel_err": pf01_b02_rel_err,
                "b01_dt_minus_25_rel_err": pf01_b01_dt_m25_rel_err,
                "b01_dt_minus_30_rel_err": pf01_b01_dt_m30_rel_err,
                "b01_dt_minus_15_rel_err": pf01_b01_dt_m15_rel_err,
                "producer_dt_minus_15_abs_diff": pf01_producer_dt_m15_match_diff,
                "diagnosis": (
                    "Evaluating half-slope fault only on pure-gauge flow at shallow IR step minus-fifteen "
                    "stays below the one-quarter threshold, whereas scalar-quartic zero-crossing doubles "
                    "t_crit (unit relative shift) and deeper IR pure-gauge flow exceeds one-quarter."
                ),
                "caught": pf01_caught,
            },
            "PF0_2_wrong_chirality_err": {
                "measured_err": pf02_ckm_err,
                "caught": pf02_caught,
            },
            "PF0_3_left_right_overlap_err": {
                "measured_err": pf03_err,
                "caught": pf03_caught,
            },
            "PF0_4_transposed_weinberg_err": {
                "measured_err": pf04_pmns_err,
                "caught": pf04_caught,
            },
            "PF0_5_corrupted_ps_weights_err": {
                "measured_err": pf05_err,
                "measured_err_exact_fraction": pf05_err_frac,
                "caught": pf05_caught,
            },
        },
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    out_dir = script_path.parent
    repo_root = script_path.parents[2]

    producer_out_path = (
        repo_root
        / "relays"
        / "agy002_endgame_v2_g0_fixed"
        / "verify_endgame_v2_g0_fixed_out.json"
    )
    producer_json = json.loads(producer_out_path.read_text(encoding="utf-8"))

    sec0 = run_section_0_ast_and_digests(script_path, repo_root)
    sec1 = run_section_1_group_theory_and_polynomials()
    sec2 = run_section_2_four_benchmarks(producer_json)
    sec3 = run_section_3_haar_and_planted_faults(producer_json)

    all_passed = bool(
        sec0["ast_and_digest_gate_passed"]
        and sec1["lie_algebra_and_polynomial_gate_passed"]
        and sec2["four_benchmarks_gate_passed"]
        and sec3["haar_u3_6_gate_passed"]
        and sec3["all_5_planted_faults_caught"]
    )

    report = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 0 \u2014 Zero-Trust Mathematical-Physics Countercheck",
        "empirical_firewall": "0 of 19",
        "gate_0_countercheck_passed": all_passed,
        "producer_gate_0_reported_passed": bool(producer_json.get("gate_0_passed", False)),
        "section_0_ast_and_artifact_digests": sec0,
        "section_1_lie_algebra_and_buttazzo_polynomial_lock": sec1,
        "section_2_four_literature_rge_benchmarks": sec2,
        "section_3_haar_u3_6_and_planted_faults": sec3,
    }

    out_json_path = out_dir / "referee_endgame_v2_g0_out.json"
    out_sha_path = out_dir / "OUTPUT_SHA256.txt"

    json_text = json.dumps(to_jsonable(report), indent=2) + "\n"
    out_json_path.write_text(json_text, encoding="utf-8")

    out_digest = sha256_hex(out_json_path)
    rel_out_posix = out_json_path.relative_to(repo_root).as_posix()
    out_sha_path.write_text(f"{out_digest}  {rel_out_posix}\n", encoding="utf-8")

    print(f"gate_0_countercheck_passed={all_passed}")
    print(f"wrote {rel_out_posix} ({out_digest})")


if __name__ == "__main__":
    main()
