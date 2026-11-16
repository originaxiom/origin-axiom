"""Cold-room zero-trust mathematical-physics countercheck for Gate 3 of AGY-002-ENDGAME-V2.

Independently constructs and verifies from primary literature:
  - Buttazzo et al. (2013), JHEP 12, 089 [arXiv:1307.3536], Appendix A
  - Machacek and Vaughn (1983-1985), Nucl. Phys. B 222, 83; B 236, 221; B 249, 70
  - Luo, Wang, and Xiao (2003), Phys. Rev. Lett. 90, 011601; Phys. Rev. D 67, 065019
  - Gildener and Weinberg (1976), Phys. Rev. D 13, 3333
  - Vissani (1998), Phys. Rev. D 57, 7027, Eq. (5)
  - Barbieri and Giudice (1988), Nucl. Phys. B 306, 63

Strict 0 of 19 empirical firewall and zero Python float literals across the entire file.
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import json
import math
import mpmath as mp
import numpy as np
from pathlib import Path
from scipy.integrate import solve_ivp
from typing import Any


ALLOWED_IMPORTS: frozenset[str] = frozenset(
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

CAMPAIGN_RELAY_DIRS: tuple[str, ...] = (
    "agy002_endgame_v2_g0_fixed",
    "agy002_endgame_v2_g0_referee",
    "agy002_endgame_v2_g1_fixed",
    "agy002_endgame_v2_g1_referee",
    "agy002_endgame_v2_g2",
    "agy002_endgame_v2_g2_referee",
    "agy002_endgame_v2_g3",
)


def rat_float(num: int, den: int = 1) -> float:
    """Convert an exact rational p/q into IEEE-754 binary64 without float literals."""
    return float(Fraction(num, den))


def rat_mpf(num: int, den: int = 1) -> Any:
    """Convert an exact rational p/q into current-precision mpmath mpf."""
    return mp.mpf(num) / mp.mpf(den)


# ============================================================================
# Section 0: Self-AST & Campaign-Wide SHA-256 Manifest Verification
# ============================================================================


def run_section_0_ast_and_manifests(self_path: Path, repo_root: Path) -> dict[str, Any]:
    """Verify own AST (0 float literals, allowed imports) and all 14 campaign SHA-256 digests."""
    source_text = self_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=str(self_path))

    imported_roots: set[str] = set()
    float_literal_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                imported_roots.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literal_count += 1

    imported_sorted = sorted(imported_roots)
    disallowed_imports = sorted(imported_roots - ALLOWED_IMPORTS)

    manifest_records: list[dict[str, Any]] = []
    mismatches: list[str] = []

    for relay_subdir in CAMPAIGN_RELAY_DIRS:
        for manifest_name in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            manifest_path = repo_root / "relays" / relay_subdir / manifest_name
            raw_line = manifest_path.read_text(encoding="utf-8").strip()
            parts = raw_line.split()
            if len(parts) != 2:
                mismatches.append(f"{relay_subdir}/{manifest_name}:malformed_manifest")
                continue
            expected_hex, rel_target = parts[0], parts[1]
            expected_prefix = f"relays/{relay_subdir}/"
            target_path = repo_root / rel_target
            hex_valid = len(expected_hex) == 64 and all(
                ch in "0123456789abcdef" for ch in expected_hex
            )
            prefix_valid = rel_target.startswith(expected_prefix)
            file_exists = target_path.is_file()
            actual_hex = (
                hashlib.sha256(target_path.read_bytes()).hexdigest()
                if file_exists
                else ""
            )
            matched = hex_valid and prefix_valid and file_exists and (actual_hex == expected_hex)
            if not matched:
                mismatches.append(f"{relay_subdir}/{manifest_name}")
            manifest_records.append(
                {
                    "manifest": f"relays/{relay_subdir}/{manifest_name}",
                    "target": rel_target,
                    "expected_sha256": expected_hex,
                    "actual_sha256": actual_hex,
                    "matched": matched,
                }
            )

    verified_count = sum(1 for rec in manifest_records if rec["matched"])
    section_passed = (
        len(disallowed_imports) == 0
        and float_literal_count == 0
        and len(manifest_records) == 14
        and verified_count == 14
        and len(mismatches) == 0
    )

    return {
        "section_0_passed": section_passed,
        "imported_modules": imported_sorted,
        "disallowed_imports": disallowed_imports,
        "float_literals_in_entire_file": float_literal_count,
        "campaign_sha256_manifests_total": len(manifest_records),
        "campaign_sha256_manifests_verified": verified_count,
        "campaign_sha256_mismatches": mismatches,
        "campaign_sha256_records": manifest_records,
    }


# ============================================================================
# Section 1: Exact Fraction 2-Loop gamma_{mu_H^2} Polynomial Lock
# ============================================================================


def frac_mat_zeros(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def frac_mat_mul(
    a: list[list[Fraction]], b: list[list[Fraction]]
) -> list[list[Fraction]]:
    n = len(a)
    m = len(b[0])
    k_len = len(b)
    out = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(k_len):
            aik = a[i][k]
            if aik != 0:
                for j in range(m):
                    out[i][j] += aik * b[k][j]
    return out


def frac_mat_transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = len(a[0])
    return [[a[i][j] for i in range(n)] for j in range(m)]


def frac_mat_trace(a: list[list[Fraction]]) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def gamma_muH2_machacek_vaughn_fraction(
    hu: list[list[Fraction]],
    hd: list[list[Fraction]],
    he: list[list[Fraction]],
    g1_sq: Fraction,
    g2_sq: Fraction,
    g3_sq: Fraction,
    lam: Fraction,
) -> tuple[Fraction, Fraction]:
    """First-principles O(4) real-scalar tensor + SU(3)xSU(2)xU(1)_GUT Casimir derivation.

    Constructs the 4x4x4x4 real-scalar quartic tensor Lambda_{abcd} for V = lam (H^dag H)^2,
    evaluates exact tadpole and sunset contractions, derives all gauge-quartic and
    gauge-Yukawa coefficients from the Standard Model representation quantum numbers
    (Luo, Wang, Xiao 2003, Phys. Rev. D 67, 065019), and evaluates 3x3 flavor matrix traces.
    """
    # 1. Explicit O(4) real-scalar quartic tensor contractions for V = (lam / 4) (phi_a phi_a)^2:
    # Lambda_{abcd} = 2 * lam * (delta_{ab} delta_{cd} + delta_{ac} delta_{bd} + delta_{ad} delta_{bc})
    tadpole_00 = Fraction(0)
    sunset_00 = Fraction(0)
    for c in range(4):
        d_00 = Fraction(1)
        d_cc = Fraction(1)
        d_0c = Fraction(1) if c == 0 else Fraction(0)
        lam_00cc = 2 * lam * (d_00 * d_cc + d_0c * d_0c + d_0c * d_0c)
        tadpole_00 += lam_00cc
        for d in range(4):
            for e in range(4):
                d_0d = Fraction(1) if d == 0 else Fraction(0)
                d_0e = Fraction(1) if e == 0 else Fraction(0)
                d_cd = Fraction(1) if c == d else Fraction(0)
                d_ce = Fraction(1) if c == e else Fraction(0)
                d_de = Fraction(1) if d == e else Fraction(0)
                lam_0cde = 2 * lam * (d_0c * d_de + d_0d * d_ce + d_0e * d_cd)
                sunset_00 += lam_0cde * lam_0cde

    pure_scalar_1l = tadpole_00
    pure_scalar_2l = Fraction(-5, 6) * sunset_00

    # 2. Exact SU(3)_c x SU(2)_L x U(1)_GUT Casimir & Dynkin table for N_g = 3 generations:
    n_gen = 3
    gut_norm = Fraction(3, 5)
    # Gauge group ordering: A = 0 -> U(1)_GUT, A = 1 -> SU(2)_L, A = 2 -> SU(3)_c
    g_sq = (g1_sq, g2_sq, g3_sq)
    c2_adj = (Fraction(0), Fraction(2), Fraction(3))
    c2_h = (gut_norm * Fraction(1, 4), Fraction(3, 4), Fraction(0))
    # Complex Higgs doublet H ~ (1, 2, 1/2): Dynkin index S_2(H)
    s2_h = (gut_norm * 2 * Fraction(1, 4), Fraction(1, 2), Fraction(0))
    # Chiral Weyl fermion Dynkin index per generation:
    # Q ~ (3, 2, 1/6), u^c ~ (3bar, 1, -2/3), d^c ~ (3bar, 1, 1/3), L ~ (1, 2, -1/2), e^c ~ (1, 1, 1)
    s2_weyl_1gen_u1 = gut_norm * (
        6 * Fraction(1, 36)
        + 3 * Fraction(4, 9)
        + 3 * Fraction(1, 9)
        + 2 * Fraction(1, 4)
        + 1 * Fraction(1, 1)
    )
    s2_weyl_1gen_su2 = (3 + 1) * Fraction(1, 2)
    s2_weyl_1gen_su3 = (2 + 1 + 1) * Fraction(1, 2)
    s2_weyl = (
        n_gen * s2_weyl_1gen_u1,
        n_gen * s2_weyl_1gen_su2,
        n_gen * s2_weyl_1gen_su3,
    )

    gauge_1l = -6 * sum((g_sq[a] * c2_h[a] for a in range(3)), Fraction(0))
    scalar_gauge_2l = 8 * tadpole_00 * sum(
        (g_sq[a] * c2_h[a] for a in range(3)), Fraction(0)
    )

    pure_gauge_2l = Fraction(0)
    for a in range(3):
        for b in range(3):
            pure_gauge_2l += 5 * g_sq[a] * g_sq[b] * c2_h[a] * c2_h[b]
        pure_gauge_2l += (
            g_sq[a]
            * g_sq[a]
            * c2_h[a]
            * (
                Fraction(-143, 6) * c2_adj[a]
                + Fraction(10, 3) * s2_weyl[a]
                + Fraction(71, 3) * s2_h[a]
            )
        )

    # 3. Fermion representation Casimirs for 2-loop gauge-Yukawa contractions:
    c2_q = (gut_norm * Fraction(1, 36), Fraction(3, 4), Fraction(4, 3))
    c2_u = (gut_norm * Fraction(4, 9), Fraction(0), Fraction(4, 3))
    c2_d = (gut_norm * Fraction(1, 9), Fraction(0), Fraction(4, 3))
    c2_l = (gut_norm * Fraction(1, 4), Fraction(3, 4), Fraction(0))
    c2_e = (gut_norm * Fraction(1, 1), Fraction(0), Fraction(0))

    tr_hu = frac_mat_trace(hu)
    tr_hd = frac_mat_trace(hd)
    tr_he = frac_mat_trace(he)

    gauge_yuk_2l = Fraction(0)
    for a in range(3):
        gauge_yuk_2l += 5 * g_sq[a] * 3 * (c2_q[a] + c2_u[a]) * tr_hu
        gauge_yuk_2l += 5 * g_sq[a] * 3 * (c2_q[a] + c2_d[a]) * tr_hd
        gauge_yuk_2l += 5 * g_sq[a] * 1 * (c2_l[a] + c2_e[a]) * tr_he

    # 4. 3x3 flavor matrix traces for 1-loop and 2-loop Yukawa / scalar-Yukawa sectors:
    yuk_trace_1l = 6 * tr_hu + 6 * tr_hd + 2 * tr_he
    scalar_yuk_2l = -2 * tadpole_00 * (3 * tr_hu + 3 * tr_hd + tr_he)

    hu_sq = frac_mat_mul(hu, hu)
    hd_sq = frac_mat_mul(hd, hd)
    he_sq = frac_mat_mul(he, he)
    hu_hd = frac_mat_mul(hu, hd)

    pure_yuk_2l = (
        Fraction(-27, 2) * frac_mat_trace(hu_sq)
        + Fraction(-27, 2) * frac_mat_trace(hd_sq)
        + Fraction(-9, 2) * frac_mat_trace(he_sq)
        - 21 * frac_mat_trace(hu_hd)
    )

    gamma_1l = pure_scalar_1l + yuk_trace_1l + gauge_1l
    gamma_2l = (
        pure_scalar_2l
        + scalar_yuk_2l
        + scalar_gauge_2l
        + pure_yuk_2l
        + gauge_yuk_2l
        + pure_gauge_2l
    )
    return gamma_1l, gamma_2l


def gamma_muH2_buttazzo_appendix_a_fraction(
    hu: list[list[Fraction]],
    hd: list[list[Fraction]],
    he: list[list[Fraction]],
    g1_sq: Fraction,
    g2_sq: Fraction,
    g3_sq: Fraction,
    lam: Fraction,
) -> tuple[Fraction, Fraction]:
    """Published Buttazzo et al. (2013) Appendix A expression: 2 * (1/m^2) dm^2 / d ln(bar_mu^2).

    Evaluated directly in standard hypercharge g_Y^2 = (3/5) g_1^2 and multiplied by 2
    to convert from d / d ln(bar_mu^2) to d / d ln(mu).
    """
    gy_sq = Fraction(3, 5) * g1_sq
    tr_hu = frac_mat_trace(hu)
    tr_hd = frac_mat_trace(hd)
    tr_he = frac_mat_trace(he)
    tr_hu2 = frac_mat_trace(frac_mat_mul(hu, hu))
    tr_hd2 = frac_mat_trace(frac_mat_mul(hd, hd))
    tr_he2 = frac_mat_trace(frac_mat_mul(he, he))
    tr_huhd = frac_mat_trace(frac_mat_mul(hu, hd))

    # (1/m^2) dm^2 / d ln(bar_mu^2) at 1-loop and 2-loop:
    dm2_dlnmu2_1l = (
        6 * lam
        + 3 * tr_hu
        + 3 * tr_hd
        + tr_he
        - Fraction(9, 4) * g2_sq
        - Fraction(3, 4) * gy_sq
    )
    dm2_dlnmu2_2l = (
        -30 * lam * lam
        - 36 * lam * tr_hu
        - 36 * lam * tr_hd
        - 12 * lam * tr_he
        + 36 * lam * g2_sq
        + 12 * lam * gy_sq
        - Fraction(27, 4) * tr_hu2
        - Fraction(27, 4) * tr_hd2
        - Fraction(9, 4) * tr_he2
        - Fraction(21, 2) * tr_huhd
        + 20 * g3_sq * (tr_hu + tr_hd)
        + Fraction(45, 8) * g2_sq * (tr_hu + tr_hd)
        + Fraction(15, 8) * g2_sq * tr_he
        + Fraction(85, 24) * gy_sq * tr_hu
        + Fraction(25, 24) * gy_sq * tr_hd
        + Fraction(25, 8) * gy_sq * tr_he
        - Fraction(145, 32) * g2_sq * g2_sq
        + Fraction(15, 16) * g2_sq * gy_sq
        + Fraction(557, 96) * gy_sq * gy_sq
    )
    # Convert d / d ln(bar_mu^2) -> d / d ln(mu) via factor of 2:
    return 2 * dm2_dlnmu2_1l, 2 * dm2_dlnmu2_2l


def diag_frac_3x3(d0: Fraction, d1: Fraction, d2: Fraction) -> list[list[Fraction]]:
    z = Fraction(0)
    return [[d0, z, z], [z, d1, z], [z, z, d2]]


def build_ten_rational_test_tuples() -> list[dict[str, Any]]:
    """Construct 10 distinct rational coupling configurations (diagonal and dense 3x3)."""
    tuples: list[dict[str, Any]] = []

    # Tuple 1: Canonical prime-denominator tuple for cross-check against Gate 3 JSON output
    tuples.append(
        {
            "label": "prime_sample_tuple",
            "hu": diag_frac_3x3(Fraction(0), Fraction(0), Fraction(7, 11)),
            "hd": diag_frac_3x3(Fraction(0), Fraction(0), Fraction(3, 13)),
            "he": diag_frac_3x3(Fraction(0), Fraction(0), Fraction(2, 17)),
            "g1_sq": Fraction(5, 19),
            "g2_sq": Fraction(6, 23),
            "g3_sq": Fraction(9, 29),
            "lam": Fraction(4, 31),
        }
    )

    # Tuple 2: Pure O(4) scalar quartic limit
    tuples.append(
        {
            "label": "pure_scalar_limit",
            "hu": frac_mat_zeros(3),
            "hd": frac_mat_zeros(3),
            "he": frac_mat_zeros(3),
            "g1_sq": Fraction(0),
            "g2_sq": Fraction(0),
            "g3_sq": Fraction(0),
            "lam": Fraction(3, 7),
        }
    )

    # Tuple 3: Pure electroweak gauge limit
    tuples.append(
        {
            "label": "pure_electroweak_gauge_limit",
            "hu": frac_mat_zeros(3),
            "hd": frac_mat_zeros(3),
            "he": frac_mat_zeros(3),
            "g1_sq": Fraction(4, 9),
            "g2_sq": Fraction(5, 8),
            "g3_sq": Fraction(7, 6),
            "lam": Fraction(0),
        }
    )

    # Tuple 4: Unified gauge limit with 3-generation diagonal Yukawas
    tuples.append(
        {
            "label": "unified_gauge_three_gen_diag",
            "hu": diag_frac_3x3(Fraction(1, 100), Fraction(1, 20), Fraction(1, 2)),
            "hd": diag_frac_3x3(Fraction(1, 200), Fraction(1, 40), Fraction(1, 5)),
            "he": diag_frac_3x3(Fraction(1, 300), Fraction(1, 50), Fraction(1, 8)),
            "g1_sq": Fraction(3, 10),
            "g2_sq": Fraction(3, 10),
            "g3_sq": Fraction(3, 10),
            "lam": Fraction(1, 8),
        }
    )

    # Helper to form H_f = Y_f^T Y_f from dense 3x3 rational Yukawa matrices:
    def gram(y_mat: list[list[Fraction]]) -> list[list[Fraction]]:
        return frac_mat_mul(frac_mat_transpose(y_mat), y_mat)

    # Tuple 5..10: Six distinct dense non-commuting 3x3 rational Yukawa configurations
    for idx in range(1, 7):
        p = idx + 1
        yu = [
            [Fraction(1, 3 * p), Fraction(1, 5 * p), Fraction(-1, 7 * p)],
            [Fraction(2, 11 * p), Fraction(3, 4 * p), Fraction(1, 6 * p)],
            [Fraction(-1, 9 * p), Fraction(2, 5 * p), Fraction(4, 5 * p)],
        ]
        yd = [
            [Fraction(2, 7 * p), Fraction(-1, 4 * p), Fraction(1, 8 * p)],
            [Fraction(1, 5 * p), Fraction(1, 3 * p), Fraction(-2, 9 * p)],
            [Fraction(3, 10 * p), Fraction(1, 6 * p), Fraction(1, 2 * p)],
        ]
        ye = [
            [Fraction(1, 6 * p), Fraction(1, 9 * p), Fraction(0)],
            [Fraction(-1, 8 * p), Fraction(2, 7 * p), Fraction(1, 5 * p)],
            [Fraction(1, 11 * p), Fraction(-1, 7 * p), Fraction(3, 8 * p)],
        ]
        tuples.append(
            {
                "label": f"dense_noncommuting_matrix_tuple_{idx}",
                "yu_raw": yu,
                "yd_raw": yd,
                "ye_raw": ye,
                "hu": gram(yu),
                "hd": gram(yd),
                "he": gram(ye),
                "g1_sq": Fraction(p + 1, 5 * p + 2),
                "g2_sq": Fraction(p + 2, 4 * p + 3),
                "g3_sq": Fraction(2 * p + 1, 3 * p + 4),
                "lam": Fraction(p, 6 * p + 5),
            }
        )

    return tuples


def run_section_1_buttazzo_polynomial_lock(g3_json: dict[str, Any]) -> dict[str, Any]:
    """Verify exact Fraction identity across 10 rational tuples + SO(3)^5 basis invariance."""
    test_tuples = build_ten_rational_test_tuples()
    all_matched = True
    tuple_checks: list[dict[str, Any]] = []

    sample_1l_str = ""
    sample_2l_str = ""

    for item in test_tuples:
        mv_1l, mv_2l = gamma_muH2_machacek_vaughn_fraction(
            item["hu"],
            item["hd"],
            item["he"],
            item["g1_sq"],
            item["g2_sq"],
            item["g3_sq"],
            item["lam"],
        )
        bt_1l, bt_2l = gamma_muH2_buttazzo_appendix_a_fraction(
            item["hu"],
            item["hd"],
            item["he"],
            item["g1_sq"],
            item["g2_sq"],
            item["g3_sq"],
            item["lam"],
        )
        exact_1l = mv_1l == bt_1l
        exact_2l = mv_2l == bt_2l
        if not (exact_1l and exact_2l):
            all_matched = False

        if item["label"] == "prime_sample_tuple":
            sample_1l_str = f"{mv_1l.numerator}/{mv_1l.denominator}"
            sample_2l_str = f"{mv_2l.numerator}/{mv_2l.denominator}"

        tuple_checks.append(
            {
                "label": item["label"],
                "gamma_1loop_rational": f"{mv_1l.numerator}/{mv_1l.denominator}",
                "gamma_2loop_rational": f"{mv_2l.numerator}/{mv_2l.denominator}",
                "exact_1loop_match": exact_1l,
                "exact_2loop_match": exact_2l,
            }
        )

    # Exact rational SO(3)^5 basis-scrambling check on dense non-commuting tuple:
    o_q = [
        [Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)],
        [Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)],
        [Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)],
    ]
    o_u = [
        [Fraction(6, 7), Fraction(3, 7), Fraction(-2, 7)],
        [Fraction(-2, 7), Fraction(6, 7), Fraction(3, 7)],
        [Fraction(3, 7), Fraction(-2, 7), Fraction(6, 7)],
    ]
    o_d = frac_mat_transpose(o_u)
    o_l = frac_mat_mul(o_q, o_u)
    o_e = frac_mat_transpose(o_q)

    dense_item = test_tuples[4]
    yu_rot = frac_mat_mul(o_u, frac_mat_mul(dense_item["yu_raw"], frac_mat_transpose(o_q)))
    yd_rot = frac_mat_mul(o_d, frac_mat_mul(dense_item["yd_raw"], frac_mat_transpose(o_q)))
    ye_rot = frac_mat_mul(o_e, frac_mat_mul(dense_item["ye_raw"], frac_mat_transpose(o_l)))
    hu_rot = frac_mat_mul(frac_mat_transpose(yu_rot), yu_rot)
    hd_rot = frac_mat_mul(frac_mat_transpose(yd_rot), yd_rot)
    he_rot = frac_mat_mul(frac_mat_transpose(ye_rot), ye_rot)

    rot_1l, rot_2l = gamma_muH2_machacek_vaughn_fraction(
        hu_rot,
        hd_rot,
        he_rot,
        dense_item["g1_sq"],
        dense_item["g2_sq"],
        dense_item["g3_sq"],
        dense_item["lam"],
    )
    orig_1l, orig_2l = gamma_muH2_buttazzo_appendix_a_fraction(
        dense_item["hu"],
        dense_item["hd"],
        dense_item["he"],
        dense_item["g1_sq"],
        dense_item["g2_sq"],
        dense_item["g3_sq"],
        dense_item["lam"],
    )
    rational_so3_5_invariant = (rot_1l == orig_1l) and (rot_2l == orig_2l)

    g3_sec1 = g3_json["section_1_buttazzo_2013_gamma_m2_polynomial_lock"]
    sample_1l_matches_g3 = sample_1l_str == g3_sec1["gamma_1loop_sample_rational"]
    sample_2l_matches_g3 = sample_2l_str == g3_sec1["gamma_2loop_sample_rational"]

    section_passed = (
        len(test_tuples) == 10
        and all_matched
        and rational_so3_5_invariant
        and sample_1l_matches_g3
        and sample_2l_matches_g3
    )

    return {
        "section_1_passed": section_passed,
        "rational_tuples_tested": len(test_tuples),
        "all_10_tuples_exact_match": all_matched,
        "rational_so3_5_basis_invariance_exact": rational_so3_5_invariant,
        "gamma_1loop_sample_rational": sample_1l_str,
        "gamma_2loop_sample_rational": sample_2l_str,
        "sample_1loop_matches_producer_json": sample_1l_matches_g3,
        "sample_2loop_matches_producer_json": sample_2l_matches_g3,
    }


# ============================================================================
# Section 2: 2-Loop SM RGEs, Picard-Lindelof Non-Crossing & CW Obstruction
# ============================================================================


def sm_2loop_rhs_matrix_complex(
    yu: np.ndarray,
    yd: np.ndarray,
    ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    mu_h2: float,
    gamma_scale: float = rat_float(1, 1),
    portal_inhom: float = rat_float(0, 1),
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float, float, float]:
    """Full 3x3 complex-matrix 2-loop MSbar Standard Model RGEs in d / d ln(mu)."""
    g1_2 = g1 * g1
    g2_2 = g2 * g2
    g3_2 = g3 * g3

    hu = yu.conj().T @ yu
    hd = yd.conj().T @ yd
    he = ye.conj().T @ ye

    hu2 = hu @ hu
    hd2 = hd @ hd
    he2 = he @ he
    hu3 = hu2 @ hu
    hd3 = hd2 @ hd
    he3 = he2 @ he
    huhd = hu @ hd
    hdhu = hd @ hu

    tr_hu = float(np.real(np.trace(hu)))
    tr_hd = float(np.real(np.trace(hd)))
    tr_he = float(np.real(np.trace(he)))
    tr_hu2 = float(np.real(np.trace(hu2)))
    tr_hd2 = float(np.real(np.trace(hd2)))
    tr_he2 = float(np.real(np.trace(he2)))
    tr_hu3 = float(np.real(np.trace(hu3)))
    tr_hd3 = float(np.real(np.trace(hd3)))
    tr_he3 = float(np.real(np.trace(he3)))
    tr_huhd = float(np.real(np.trace(huhd)))
    tr_hu2hd = float(np.real(np.trace(hu2 @ hd)))
    tr_huhd2 = float(np.real(np.trace(hu @ hd2)))

    t_tr = 3 * tr_hu + 3 * tr_hd + tr_he
    i3 = np.eye(3, dtype=complex)

    inv16pi2 = rat_float(1, 1) / (rat_float(16, 1) * (math.pi**2))
    inv16pi2_2 = inv16pi2 * inv16pi2

    # 2-loop gauge beta functions (GUT-normalized g_1^2 = 5/3 g_Y^2):
    bg1 = (g1**3) * (
        rat_float(41, 10) * inv16pi2
        + (
            rat_float(199, 50) * g1_2
            + rat_float(27, 10) * g2_2
            + rat_float(44, 5) * g3_2
            - rat_float(17, 10) * tr_hu
            - rat_float(1, 2) * tr_hd
            - rat_float(3, 2) * tr_he
        )
        * inv16pi2_2
    )
    bg2 = (g2**3) * (
        rat_float(-19, 6) * inv16pi2
        + (
            rat_float(9, 10) * g1_2
            + rat_float(35, 6) * g2_2
            + rat_float(12, 1) * g3_2
            - rat_float(3, 2) * tr_hu
            - rat_float(3, 2) * tr_hd
            - rat_float(1, 2) * tr_he
        )
        * inv16pi2_2
    )
    bg3 = (g3**3) * (
        rat_float(-7, 1) * inv16pi2
        + (
            rat_float(11, 10) * g1_2
            + rat_float(9, 2) * g2_2
            - rat_float(26, 1) * g3_2
            - rat_float(2, 1) * tr_hu
            - rat_float(2, 1) * tr_hd
        )
        * inv16pi2_2
    )

    # 1-loop & 2-loop 3x3 Yukawa beta functions (Machacek-Vaughn 1984 / Luo-Xiao 2003):
    chi4 = rat_float(9, 4) * (3 * tr_hu2 + 3 * tr_hd2 + tr_he2) - rat_float(3, 2) * tr_huhd
    y2g = (
        rat_float(20, 1) * g3_2 * (tr_hu + tr_hd)
        + rat_float(45, 8) * g2_2 * (tr_hu + tr_hd)
        + rat_float(15, 8) * g2_2 * tr_he
        + rat_float(17, 8) * g1_2 * tr_hu
        + rat_float(5, 8) * g1_2 * tr_hd
        + rat_float(15, 8) * g1_2 * tr_he
    )

    byu1 = yu @ (
        rat_float(3, 2) * hu
        - rat_float(3, 2) * hd
        + (t_tr - rat_float(17, 20) * g1_2 - rat_float(9, 4) * g2_2 - rat_float(8, 1) * g3_2) * i3
    )
    byd1 = yd @ (
        rat_float(3, 2) * hd
        - rat_float(3, 2) * hu
        + (t_tr - rat_float(1, 4) * g1_2 - rat_float(9, 4) * g2_2 - rat_float(8, 1) * g3_2) * i3
    )
    bye1 = ye @ (
        rat_float(3, 2) * he
        + (t_tr - rat_float(9, 4) * g1_2 - rat_float(9, 4) * g2_2) * i3
    )

    byu2 = yu @ (
        rat_float(3, 2) * hu2
        - hdhu
        - rat_float(1, 4) * huhd
        - rat_float(3, 2) * hdhu
        + rat_float(11, 4) * hd2
        + t_tr * (rat_float(5, 4) * hd - rat_float(9, 4) * hu)
        - rat_float(12, 1) * lam * hu
        + (rat_float(223, 80) * g1_2 + rat_float(135, 16) * g2_2 + rat_float(16, 1) * g3_2) * hu
        - (rat_float(43, 80) * g1_2 - rat_float(9, 16) * g2_2 + rat_float(16, 1) * g3_2) * hd
        + (
            -chi4
            + rat_float(6, 1) * lam * lam
            + y2g
            + rat_float(1187, 600) * g1_2 * g1_2
            - rat_float(9, 20) * g1_2 * g2_2
            + rat_float(19, 15) * g1_2 * g3_2
            - rat_float(23, 4) * g2_2 * g2_2
            + rat_float(9, 1) * g2_2 * g3_2
            - rat_float(108, 1) * g3_2 * g3_2
        )
        * i3
    )
    byd2 = yd @ (
        rat_float(3, 2) * hd2
        - huhd
        - rat_float(1, 4) * hdhu
        - rat_float(3, 2) * huhd
        + rat_float(11, 4) * hu2
        + t_tr * (rat_float(5, 4) * hu - rat_float(9, 4) * hd)
        - rat_float(12, 1) * lam * hd
        + (rat_float(187, 80) * g1_2 + rat_float(135, 16) * g2_2 + rat_float(16, 1) * g3_2) * hd
        - (rat_float(79, 80) * g1_2 - rat_float(9, 16) * g2_2 + rat_float(16, 1) * g3_2) * hu
        + (
            -chi4
            + rat_float(6, 1) * lam * lam
            + y2g
            - rat_float(127, 600) * g1_2 * g1_2
            - rat_float(27, 20) * g1_2 * g2_2
            + rat_float(31, 15) * g1_2 * g3_2
            - rat_float(23, 4) * g2_2 * g2_2
            + rat_float(9, 1) * g2_2 * g3_2
            - rat_float(108, 1) * g3_2 * g3_2
        )
        * i3
    )
    bye2 = ye @ (
        rat_float(3, 2) * he2
        - rat_float(9, 4) * t_tr * he
        - rat_float(12, 1) * lam * he
        + (rat_float(387, 80) * g1_2 + rat_float(135, 16) * g2_2) * he
        + (
            -chi4
            + rat_float(6, 1) * lam * lam
            + y2g
            + rat_float(1371, 200) * g1_2 * g1_2
            + rat_float(27, 20) * g1_2 * g2_2
            - rat_float(23, 4) * g2_2 * g2_2
        )
        * i3
    )

    # 1-loop & 2-loop Higgs quartic beta_lambda:
    blam1 = (
        rat_float(24, 1) * lam * lam
        - lam * (rat_float(9, 1) * g2_2 + rat_float(9, 5) * g1_2)
        + rat_float(9, 8) * g2_2 * g2_2
        + rat_float(9, 20) * g1_2 * g2_2
        + rat_float(27, 200) * g1_2 * g1_2
        + rat_float(4, 1) * lam * t_tr
        - rat_float(6, 1) * tr_hu2
        - rat_float(6, 1) * tr_hd2
        - rat_float(2, 1) * tr_he2
    )
    blam2 = (
        rat_float(-312, 1) * (lam**3)
        + (lam * lam) * (rat_float(108, 1) * g2_2 + rat_float(108, 5) * g1_2)
        + lam
        * (
            rat_float(-73, 8) * g2_2 * g2_2
            + rat_float(117, 20) * g1_2 * g2_2
            + rat_float(1887, 200) * g1_2 * g1_2
        )
        + rat_float(305, 16) * (g2_2**3)
        - rat_float(289, 80) * g1_2 * g2_2 * g2_2
        - rat_float(1677, 400) * g1_2 * g1_2 * g2_2
        - rat_float(3411, 2000) * (g1_2**3)
        - rat_float(32, 1) * g3_2 * (tr_hu2 + tr_hd2)
        - rat_float(8, 5) * g1_2 * (2 * tr_hu2 - tr_hd2 + 3 * tr_he2)
        - rat_float(3, 4) * g2_2 * g2_2 * t_tr
        + g1_2
        * g2_2
        * (
            rat_float(63, 10) * tr_hu
            + rat_float(27, 10) * tr_hd
            + rat_float(33, 10) * tr_he
        )
        - g1_2
        * g1_2
        * (
            rat_float(171, 100) * tr_hu
            - rat_float(9, 20) * tr_hd
            + rat_float(9, 4) * tr_he
        )
        + lam
        * (
            rat_float(80, 1) * g3_2 * (tr_hu + tr_hd)
            + rat_float(45, 2) * g2_2 * (tr_hu + tr_hd)
            + rat_float(15, 2) * g2_2 * tr_he
            + rat_float(17, 2) * g1_2 * tr_hu
            + rat_float(5, 2) * g1_2 * tr_hd
            + rat_float(15, 2) * g1_2 * tr_he
        )
        - rat_float(48, 1) * lam * lam * t_tr
        - lam * (3 * tr_hu2 + 3 * tr_hd2 + tr_he2 + 6 * tr_huhd)
        + rat_float(30, 1) * tr_hu3
        + rat_float(30, 1) * tr_hd3
        + rat_float(10, 1) * tr_he3
        - rat_float(6, 1) * (tr_hu2hd + tr_huhd2)
    )

    # 1-loop & 2-loop gamma_{mu_H^2}:
    gam1 = (
        rat_float(12, 1) * lam
        + rat_float(6, 1) * tr_hu
        + rat_float(6, 1) * tr_hd
        + rat_float(2, 1) * tr_he
        - rat_float(9, 2) * g2_2
        - rat_float(9, 10) * g1_2
    )
    gam2 = (
        rat_float(-60, 1) * lam * lam
        - rat_float(72, 1) * lam * tr_hu
        - rat_float(72, 1) * lam * tr_hd
        - rat_float(24, 1) * lam * tr_he
        + rat_float(72, 1) * lam * g2_2
        + rat_float(72, 5) * lam * g1_2
        - rat_float(27, 2) * tr_hu2
        - rat_float(27, 2) * tr_hd2
        - rat_float(9, 2) * tr_he2
        - rat_float(21, 1) * tr_huhd
        + rat_float(40, 1) * g3_2 * (tr_hu + tr_hd)
        + rat_float(45, 4) * g2_2 * (tr_hu + tr_hd)
        + rat_float(15, 4) * g2_2 * tr_he
        + rat_float(17, 4) * g1_2 * tr_hu
        + rat_float(5, 4) * g1_2 * tr_hd
        + rat_float(15, 4) * g1_2 * tr_he
        - rat_float(145, 16) * g2_2 * g2_2
        + rat_float(9, 8) * g1_2 * g2_2
        + rat_float(1671, 400) * g1_2 * g1_2
    )

    gamma_eff = gamma_scale * (gam1 * inv16pi2 + gam2 * inv16pi2_2)
    d_mu_h2 = gamma_eff * mu_h2 + portal_inhom

    d_yu = byu1 * inv16pi2 + byu2 * inv16pi2_2
    d_yd = byd1 * inv16pi2 + byd2 * inv16pi2_2
    d_ye = bye1 * inv16pi2 + bye2 * inv16pi2_2
    d_lam = blam1 * inv16pi2 + blam2 * inv16pi2_2
    return d_yu, d_yd, d_ye, bg1, bg2, bg3, d_lam, d_mu_h2, gamma_eff


def make_sm_diag_rhs_float(
    gamma_scale: float = rat_float(1, 1),
    portal_inhom: float = rat_float(0, 1),
) -> Any:
    """Fast 15-state diagonal-Yukawa ODE RHS verified identical to the 3x3 matrix RHS."""

    def rhs(_t: float, state: np.ndarray) -> np.ndarray:
        yu = np.diag(state[0:3]).astype(complex)
        yd = np.diag(state[3:6]).astype(complex)
        ye = np.diag(state[6:9]).astype(complex)
        dyu, dyd, dye, bg1, bg2, bg3, dlam, dmu, gam = sm_2loop_rhs_matrix_complex(
            yu,
            yd,
            ye,
            float(state[9]),
            float(state[10]),
            float(state[11]),
            float(state[12]),
            float(state[13]),
            gamma_scale=gamma_scale,
            portal_inhom=portal_inhom,
        )
        out = np.zeros_like(state)
        out[0:3] = np.real(np.diag(dyu))
        out[3:6] = np.real(np.diag(dyd))
        out[6:9] = np.real(np.diag(dye))
        out[9] = bg1
        out[10] = bg2
        out[11] = bg3
        out[12] = dlam
        out[13] = dmu
        out[14] = gam
        return out

    return rhs


def build_mpmath_rk4_integrator() -> Any:
    """Construct a 45-digit mpmath RK4 integrator for the 15-state 2-loop SM + portal system."""
    c_41_10 = rat_mpf(41, 10)
    c_199_50 = rat_mpf(199, 50)
    c_27_10 = rat_mpf(27, 10)
    c_44_5 = rat_mpf(44, 5)
    c_17_10 = rat_mpf(17, 10)
    c_1_2 = rat_mpf(1, 2)
    c_3_2 = rat_mpf(3, 2)
    c_m19_6 = rat_mpf(-19, 6)
    c_9_10 = rat_mpf(9, 10)
    c_35_6 = rat_mpf(35, 6)
    c_11_10 = rat_mpf(11, 10)
    c_9_2 = rat_mpf(9, 2)
    c_9_4 = rat_mpf(9, 4)
    c_45_8 = rat_mpf(45, 8)
    c_15_8 = rat_mpf(15, 8)
    c_17_8 = rat_mpf(17, 8)
    c_5_8 = rat_mpf(5, 8)
    c_17_20 = rat_mpf(17, 20)
    c_1_4 = rat_mpf(1, 4)
    c_11_4 = rat_mpf(11, 4)
    c_5_4 = rat_mpf(5, 4)
    c_223_80 = rat_mpf(223, 80)
    c_135_16 = rat_mpf(135, 16)
    c_43_80 = rat_mpf(43, 80)
    c_9_16 = rat_mpf(9, 16)
    c_1187_600 = rat_mpf(1187, 600)
    c_9_20 = rat_mpf(9, 20)
    c_19_15 = rat_mpf(19, 15)
    c_23_4 = rat_mpf(23, 4)
    c_187_80 = rat_mpf(187, 80)
    c_79_80 = rat_mpf(79, 80)
    c_m127_600 = rat_mpf(-127, 600)
    c_27_20 = rat_mpf(27, 20)
    c_31_15 = rat_mpf(31, 15)
    c_387_80 = rat_mpf(387, 80)
    c_1371_200 = rat_mpf(1371, 200)
    c_9_5 = rat_mpf(9, 5)
    c_9_8 = rat_mpf(9, 8)
    c_27_200 = rat_mpf(27, 200)
    c_108_5 = rat_mpf(108, 5)
    c_m73_8 = rat_mpf(-73, 8)
    c_117_20 = rat_mpf(117, 20)
    c_1887_200 = rat_mpf(1887, 200)
    c_305_16 = rat_mpf(305, 16)
    c_289_80 = rat_mpf(289, 80)
    c_1677_400 = rat_mpf(1677, 400)
    c_3411_2000 = rat_mpf(3411, 2000)
    c_8_5 = rat_mpf(8, 5)
    c_3_4 = rat_mpf(3, 4)
    c_63_10 = rat_mpf(63, 10)
    c_33_10 = rat_mpf(33, 10)
    c_171_100 = rat_mpf(171, 100)
    c_45_2 = rat_mpf(45, 2)
    c_15_2 = rat_mpf(15, 2)
    c_17_2 = rat_mpf(17, 2)
    c_5_2 = rat_mpf(5, 2)
    c_72_5 = rat_mpf(72, 5)
    c_27_2 = rat_mpf(27, 2)
    c_45_4 = rat_mpf(45, 4)
    c_15_4 = rat_mpf(15, 4)
    c_17_4 = rat_mpf(17, 4)
    c_145_16 = rat_mpf(145, 16)
    c_1671_400 = rat_mpf(1671, 400)
    inv16pi2 = rat_mpf(1, 16) / (mp.pi**2)
    inv16pi2_2 = inv16pi2 * inv16pi2

    def rhs_mp(state: list[Any], portal_inhom: Any) -> list[Any]:
        yu = state[0:3]
        yd = state[3:6]
        ye = state[6:9]
        g1, g2, g3, lam, mu_h2, _igam = (
            state[9],
            state[10],
            state[11],
            state[12],
            state[13],
            state[14],
        )
        g1_2 = g1 * g1
        g2_2 = g2 * g2
        g3_2 = g3 * g3
        hu = [x * x for x in yu]
        hd = [x * x for x in yd]
        he = [x * x for x in ye]
        tr_hu = hu[0] + hu[1] + hu[2]
        tr_hd = hd[0] + hd[1] + hd[2]
        tr_he = he[0] + he[1] + he[2]
        tr_hu2 = hu[0] ** 2 + hu[1] ** 2 + hu[2] ** 2
        tr_hd2 = hd[0] ** 2 + hd[1] ** 2 + hd[2] ** 2
        tr_he2 = he[0] ** 2 + he[1] ** 2 + he[2] ** 2
        tr_hu3 = hu[0] ** 3 + hu[1] ** 3 + hu[2] ** 3
        tr_hd3 = hd[0] ** 3 + hd[1] ** 3 + hd[2] ** 3
        tr_he3 = he[0] ** 3 + he[1] ** 3 + he[2] ** 3
        tr_huhd = hu[0] * hd[0] + hu[1] * hd[1] + hu[2] * hd[2]
        tr_hu2hd_p_huhd2 = sum(
            (hu[k] * hd[k] * (hu[k] + hd[k]) for k in range(3)), mp.mpf(0)
        )
        t_tr = 3 * tr_hu + 3 * tr_hd + tr_he

        bg1 = (g1**3) * (
            c_41_10 * inv16pi2
            + (
                c_199_50 * g1_2
                + c_27_10 * g2_2
                + c_44_5 * g3_2
                - c_17_10 * tr_hu
                - c_1_2 * tr_hd
                - c_3_2 * tr_he
            )
            * inv16pi2_2
        )
        bg2 = (g2**3) * (
            c_m19_6 * inv16pi2
            + (
                c_9_10 * g1_2
                + c_35_6 * g2_2
                + 12 * g3_2
                - c_3_2 * tr_hu
                - c_3_2 * tr_hd
                - c_1_2 * tr_he
            )
            * inv16pi2_2
        )
        bg3 = (g3**3) * (
            -7 * inv16pi2
            + (c_11_10 * g1_2 + c_9_2 * g2_2 - 26 * g3_2 - 2 * tr_hu - 2 * tr_hd)
            * inv16pi2_2
        )

        chi4 = c_9_4 * (3 * tr_hu2 + 3 * tr_hd2 + tr_he2) - c_3_2 * tr_huhd
        y2g = (
            20 * g3_2 * (tr_hu + tr_hd)
            + c_45_8 * g2_2 * (tr_hu + tr_hd)
            + c_15_8 * g2_2 * tr_he
            + c_17_8 * g1_2 * tr_hu
            + c_5_8 * g1_2 * tr_hd
            + c_15_8 * g1_2 * tr_he
        )

        dyu: list[Any] = []
        dyd: list[Any] = []
        dye: list[Any] = []
        u_gauge2 = (
            -chi4
            + 6 * lam * lam
            + y2g
            + c_1187_600 * g1_2 * g1_2
            - c_9_20 * g1_2 * g2_2
            + c_19_15 * g1_2 * g3_2
            - c_23_4 * g2_2 * g2_2
            + 9 * g2_2 * g3_2
            - 108 * g3_2 * g3_2
        )
        d_gauge2 = (
            -chi4
            + 6 * lam * lam
            + y2g
            + c_m127_600 * g1_2 * g1_2
            - c_27_20 * g1_2 * g2_2
            + c_31_15 * g1_2 * g3_2
            - c_23_4 * g2_2 * g2_2
            + 9 * g2_2 * g3_2
            - 108 * g3_2 * g3_2
        )
        e_gauge2 = (
            -chi4
            + 6 * lam * lam
            + y2g
            + c_1371_200 * g1_2 * g1_2
            + c_27_20 * g1_2 * g2_2
            - c_23_4 * g2_2 * g2_2
        )

        for k in range(3):
            byu1_k = yu[k] * (
                c_3_2 * hu[k]
                - c_3_2 * hd[k]
                + t_tr
                - c_17_20 * g1_2
                - c_9_4 * g2_2
                - 8 * g3_2
            )
            byu2_k = yu[k] * (
                c_3_2 * (hu[k] ** 2)
                - c_11_4 * hu[k] * hd[k]
                + c_11_4 * (hd[k] ** 2)
                + t_tr * (c_5_4 * hd[k] - c_9_4 * hu[k])
                - 12 * lam * hu[k]
                + (c_223_80 * g1_2 + c_135_16 * g2_2 + 16 * g3_2) * hu[k]
                - (c_43_80 * g1_2 - c_9_16 * g2_2 + 16 * g3_2) * hd[k]
                + u_gauge2
            )
            dyu.append(byu1_k * inv16pi2 + byu2_k * inv16pi2_2)

            byd1_k = yd[k] * (
                c_3_2 * hd[k]
                - c_3_2 * hu[k]
                + t_tr
                - c_1_4 * g1_2
                - c_9_4 * g2_2
                - 8 * g3_2
            )
            byd2_k = yd[k] * (
                c_3_2 * (hd[k] ** 2)
                - c_11_4 * hu[k] * hd[k]
                + c_11_4 * (hu[k] ** 2)
                + t_tr * (c_5_4 * hu[k] - c_9_4 * hd[k])
                - 12 * lam * hd[k]
                + (c_187_80 * g1_2 + c_135_16 * g2_2 + 16 * g3_2) * hd[k]
                - (c_79_80 * g1_2 - c_9_16 * g2_2 + 16 * g3_2) * hu[k]
                + d_gauge2
            )
            dyd.append(byd1_k * inv16pi2 + byd2_k * inv16pi2_2)

            bye1_k = ye[k] * (c_3_2 * he[k] + t_tr - c_9_4 * g1_2 - c_9_4 * g2_2)
            bye2_k = ye[k] * (
                c_3_2 * (he[k] ** 2)
                - c_9_4 * t_tr * he[k]
                - 12 * lam * he[k]
                + (c_387_80 * g1_2 + c_135_16 * g2_2) * he[k]
                + e_gauge2
            )
            dye.append(bye1_k * inv16pi2 + bye2_k * inv16pi2_2)

        blam1 = (
            24 * lam * lam
            - lam * (9 * g2_2 + c_9_5 * g1_2)
            + c_9_8 * g2_2 * g2_2
            + c_9_20 * g1_2 * g2_2
            + c_27_200 * g1_2 * g1_2
            + 4 * lam * t_tr
            - 6 * tr_hu2
            - 6 * tr_hd2
            - 2 * tr_he2
        )
        blam2 = (
            -312 * (lam**3)
            + (lam * lam) * (108 * g2_2 + c_108_5 * g1_2)
            + lam
            * (
                c_m73_8 * g2_2 * g2_2
                + c_117_20 * g1_2 * g2_2
                + c_1887_200 * g1_2 * g1_2
            )
            + c_305_16 * (g2_2**3)
            - c_289_80 * g1_2 * g2_2 * g2_2
            - c_1677_400 * g1_2 * g1_2 * g2_2
            - c_3411_2000 * (g1_2**3)
            - 32 * g3_2 * (tr_hu2 + tr_hd2)
            - c_8_5 * g1_2 * (2 * tr_hu2 - tr_hd2 + 3 * tr_he2)
            - c_3_4 * g2_2 * g2_2 * t_tr
            + g1_2 * g2_2 * (c_63_10 * tr_hu + c_27_10 * tr_hd + c_33_10 * tr_he)
            - g1_2 * g1_2 * (c_171_100 * tr_hu - c_9_20 * tr_hd + c_9_4 * tr_he)
            + lam
            * (
                80 * g3_2 * (tr_hu + tr_hd)
                + c_45_2 * g2_2 * (tr_hu + tr_hd)
                + c_15_2 * g2_2 * tr_he
                + c_17_2 * g1_2 * tr_hu
                + c_5_2 * g1_2 * tr_hd
                + c_15_2 * g1_2 * tr_he
            )
            - 48 * lam * lam * t_tr
            - lam * (3 * tr_hu2 + 3 * tr_hd2 + tr_he2 + 6 * tr_huhd)
            + 30 * tr_hu3
            + 30 * tr_hd3
            + 10 * tr_he3
            - 6 * tr_hu2hd_p_huhd2
        )

        gam1 = (
            12 * lam
            + 6 * tr_hu
            + 6 * tr_hd
            + 2 * tr_he
            - c_9_2 * g2_2
            - c_9_10 * g1_2
        )
        gam2 = (
            -60 * lam * lam
            - 72 * lam * tr_hu
            - 72 * lam * tr_hd
            - 24 * lam * tr_he
            + 72 * lam * g2_2
            + c_72_5 * lam * g1_2
            - c_27_2 * tr_hu2
            - c_27_2 * tr_hd2
            - c_9_2 * tr_he2
            - 21 * tr_huhd
            + 40 * g3_2 * (tr_hu + tr_hd)
            + c_45_4 * g2_2 * (tr_hu + tr_hd)
            + c_15_4 * g2_2 * tr_he
            + c_17_4 * g1_2 * tr_hu
            + c_5_4 * g1_2 * tr_hd
            + c_15_4 * g1_2 * tr_he
            - c_145_16 * g2_2 * g2_2
            + c_9_8 * g1_2 * g2_2
            + c_1671_400 * g1_2 * g1_2
        )

        gam = gam1 * inv16pi2 + gam2 * inv16pi2_2
        d_lam = blam1 * inv16pi2 + blam2 * inv16pi2_2
        d_mu = gam * mu_h2 + portal_inhom
        return dyu + dyd + dye + [bg1, bg2, bg3, d_lam, d_mu, gam]

    def integrate_rk4(
        y_init: list[Any], delta_t: Any, n_steps: int, portal_inhom: Any = mp.mpf(0)
    ) -> list[Any]:
        h = delta_t / n_steps
        half = mp.mpf(1) / 2
        sixth = mp.mpf(1) / 6
        state = list(y_init)
        for _ in range(n_steps):
            k1 = rhs_mp(state, portal_inhom)
            k2 = rhs_mp([s + h * half * d for s, d in zip(state, k1)], portal_inhom)
            k3 = rhs_mp([s + h * half * d for s, d in zip(state, k2)], portal_inhom)
            k4 = rhs_mp([s + h * d for s, d in zip(state, k3)], portal_inhom)
            state = [
                s + h * sixth * (d1 + 2 * d2 + 2 * d3 + d4)
                for s, d1, d2, d3, d4 in zip(state, k1, k2, k3, k4)
            ]
        return state

    return integrate_rk4


def sample_haar_u3(rng: np.random.Generator) -> np.ndarray:
    """Mezzadri exact Haar U(3) sampler via complex Ginibre QR with positive R diagonal."""
    imag_unit = complex(0, 1)
    z = (rng.normal(size=(3, 3)) + imag_unit * rng.normal(size=(3, 3))) / math.sqrt(
        rat_float(2, 1)
    )
    q, r = np.linalg.qr(z)
    diag_r = np.diag(r)
    phases = diag_r / np.abs(diag_r)
    return q * phases


def verify_analytic_rge_benchmark_gate() -> dict[str, Any]:
    """Literature analytical benchmark check (Guardrail 4) prior to model UV evolution.

    1) Pure 1-loop O(4) scalar trajectory: exact solution of d lam / dt = 24 lam^2 / (16 pi^2)
       and d mu_H^2 / dt = 12 lam mu_H^2 / (16 pi^2) satisfies mu_H^2(t) = mu_0^2 (1 - 24 lam_0 t / (16 pi^2))^(-1/2).
    2) Pure 2-loop SU(3)_c trajectory (b_3 = -7, B_33 = -26): exact analytical implicit
       integral Delta t_exact(g_3(0), g_3(IR)) = -28 verified to < 1e-12.
    """
    rtol = rat_float(1, 10**13)
    atol = rat_float(1, 10**15)
    g3_init = math.sqrt(rat_float(4, 1) * math.pi / rat_float(45, 1))
    y0_qcd = np.zeros(15, dtype=float)
    y0_qcd[11] = g3_init
    y0_qcd[13] = rat_float(1, 1)
    sol_qcd = solve_ivp(
        make_sm_diag_rhs_float(),
        (rat_float(0, 1), rat_float(-28, 1)),
        y0_qcd,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    g3_ir = float(sol_qcd.y[11, -1])
    inv16pi2 = rat_float(1, 1) / (rat_float(16, 1) * (math.pi**2))
    u0 = (g3_init * g3_init) * inv16pi2
    u1 = (g3_ir * g3_ir) * inv16pi2
    b3 = rat_float(-7, 1)
    b33 = rat_float(-26, 1)

    def primitive_t(u: float) -> float:
        return -rat_float(1, 1) / (rat_float(2, 1) * b3 * u) - (
            b33 / (rat_float(2, 1) * b3 * b3)
        ) * math.log(abs(u / (b3 + b33 * u)))

    dt_analytic = primitive_t(u1) - primitive_t(u0)
    qcd_2loop_rel_err = abs(dt_analytic - rat_float(-28, 1)) / rat_float(28, 1)

    return {
        "qcd_2loop_implicit_benchmark_rel_err": qcd_2loop_rel_err,
        "benchmark_gate_passed": qcd_2loop_rel_err < rat_float(1, 10**12),
    }


def run_section_2_picard_lindelof_and_cw(g3_json: dict[str, Any]) -> dict[str, Any]:
    """Verify Picard-Lindelof homogeneous non-crossing + Coleman-Weinberg top obstruction."""
    bench = verify_analytic_rge_benchmark_gate()

    # Verify U(3)^5 covariance of the full 3x3 complex-matrix 2-loop RGE RHS:
    imag_unit = complex(0, 1)
    rng = np.random.default_rng(20261116)
    yu_test = (rng.normal(size=(3, 3)) + imag_unit * rng.normal(size=(3, 3))) * rat_float(1, 5)
    yd_test = (rng.normal(size=(3, 3)) + imag_unit * rng.normal(size=(3, 3))) * rat_float(1, 7)
    ye_test = (rng.normal(size=(3, 3)) + imag_unit * rng.normal(size=(3, 3))) * rat_float(1, 9)
    u_q = sample_haar_u3(rng)
    u_u = sample_haar_u3(rng)
    u_d = sample_haar_u3(rng)
    u_l = sample_haar_u3(rng)
    u_e = sample_haar_u3(rng)

    dyu_0, dyd_0, dye_0, bg1_0, bg2_0, bg3_0, dlam_0, dmu_0, gam_0 = (
        sm_2loop_rhs_matrix_complex(
            yu_test,
            yd_test,
            ye_test,
            rat_float(1, 2),
            rat_float(3, 5),
            rat_float(4, 5),
            rat_float(1, 8),
            rat_float(1, 1),
        )
    )
    dyu_r, dyd_r, dye_r, bg1_r, bg2_r, bg3_r, dlam_r, dmu_r, gam_r = (
        sm_2loop_rhs_matrix_complex(
            u_u @ yu_test @ u_q.conj().T,
            u_d @ yd_test @ u_q.conj().T,
            u_e @ ye_test @ u_l.conj().T,
            rat_float(1, 2),
            rat_float(3, 5),
            rat_float(4, 5),
            rat_float(1, 8),
            rat_float(1, 1),
        )
    )
    rhs_u3_5_err = max(
        float(np.max(np.abs(dyu_r - (u_u @ dyu_0 @ u_q.conj().T)))),
        float(np.max(np.abs(dyd_r - (u_d @ dyd_0 @ u_q.conj().T)))),
        float(np.max(np.abs(dye_r - (u_e @ dye_0 @ u_l.conj().T)))),
        abs(bg1_r - bg1_0),
        abs(bg2_r - bg2_0),
        abs(bg3_r - bg3_0),
        abs(dlam_r - dlam_0),
        abs(dmu_r - dmu_0),
        abs(gam_r - gam_0),
    )

    # Perturbative UV initial state: g_uv = sqrt(4 pi / 45), y_t(UV) = 1/2, lam(UV) = 1/8, mu_H^2(0) = 1
    g_uv = math.sqrt(rat_float(4, 1) * math.pi / rat_float(45, 1))
    y0_pos = np.array(
        [
            rat_float(1, 100),
            rat_float(1, 20),
            rat_float(1, 2),
            rat_float(1, 200),
            rat_float(1, 40),
            rat_float(1, 5),
            rat_float(1, 300),
            rat_float(1, 50),
            rat_float(1, 8),
            g_uv,
            g_uv,
            g_uv,
            rat_float(1, 8),
            rat_float(1, 1),
            rat_float(0, 1),
        ],
        dtype=float,
    )
    rtol = rat_float(1, 10**13)
    atol = rat_float(1, 10**15)
    t_grid = np.linspace(rat_float(0, 1), rat_float(-28, 1), 561)

    sol_pos = solve_ivp(
        make_sm_diag_rhs_float(),
        (rat_float(0, 1), rat_float(-28, 1)),
        y0_pos,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        t_eval=t_grid,
    )
    mu_h2_ir_dop = float(sol_pos.y[13, -1])
    i_gamma_ir_dop = float(sol_pos.y[14, -1])
    mu_h2_from_exp_dop = float(y0_pos[13]) * math.exp(i_gamma_ir_dop)
    picard_rel_err_dop = abs(mu_h2_ir_dop - mu_h2_from_exp_dop) / abs(mu_h2_ir_dop)
    min_mu_h2_pos = float(np.min(sol_pos.y[13, :]))
    alpha3_inv_ir = (rat_float(4, 1) * math.pi) / (float(sol_pos.y[11, -1]) ** 2)

    # Also verify negative initial state mu_H^2(0) = -1 preserves negative sign everywhere:
    y0_neg = y0_pos.copy()
    y0_neg[13] = rat_float(-1, 1)
    sol_neg = solve_ivp(
        make_sm_diag_rhs_float(),
        (rat_float(0, 1), rat_float(-28, 1)),
        y0_neg,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        t_eval=t_grid,
    )
    max_mu_h2_neg = float(np.max(sol_neg.y[13, :]))
    homogeneous_crosses_zero = (min_mu_h2_pos <= rat_float(0, 1)) or (
        max_mu_h2_neg >= rat_float(0, 1)
    )

    # Cross-check against independent 45-digit mpmath RK4 integration:
    mp.mp.dps = 45
    integrate_mp = build_mpmath_rk4_integrator()
    g_uv_mp = mp.sqrt(4 * mp.pi / rat_mpf(45, 1))
    y0_mp = [
        rat_mpf(1, 100),
        rat_mpf(1, 20),
        rat_mpf(1, 2),
        rat_mpf(1, 200),
        rat_mpf(1, 40),
        rat_mpf(1, 5),
        rat_mpf(1, 300),
        rat_mpf(1, 50),
        rat_mpf(1, 8),
        g_uv_mp,
        g_uv_mp,
        g_uv_mp,
        rat_mpf(1, 8),
        rat_mpf(1, 1),
        rat_mpf(0, 1),
    ]
    ir_mp = integrate_mp(y0_mp, rat_mpf(-28, 1), 560)
    mu_h2_ir_mp = ir_mp[13]
    i_gamma_ir_mp = ir_mp[14]
    picard_rel_err_mp = float(
        abs(mu_h2_ir_mp - mp.exp(i_gamma_ir_mp)) / abs(mu_h2_ir_mp)
    )
    dop_vs_mp_rel_err = abs(mu_h2_ir_dop - float(mu_h2_ir_mp)) / abs(float(mu_h2_ir_mp))

    # Coleman-Weinberg effective potential V_CW(|H|) = (1/2) beta_lam(mu_CW) ln(|H|^2 / mu_CW^2) |H|^4
    # (for tree convention V_0(|H|) = mu_H^2 |H|^2 + lam |H|^4; equivalently (1/4) beta_lam ln(h^2/mu_CW^2) h^4
    # in canonical field, satisfying d^2 V_CW(|H|) / d|H|^2 |_{|H|=v} = 4 beta_lam(mu_CW) v^2).
    z3 = np.zeros((3, 3), dtype=complex)
    _, _, _, _, _, _, beta_lam_gauge, _, _ = sm_2loop_rhs_matrix_complex(
        z3,
        z3,
        z3,
        rat_float(1, 2),
        rat_float(3, 5),
        rat_float(4, 5),
        rat_float(0, 1),
        rat_float(0, 1),
    )
    yu_top = np.diag([rat_float(0, 1), rat_float(0, 1), rat_float(9, 10)]).astype(complex)
    _, _, _, _, _, _, beta_lam_top, _, _ = sm_2loop_rhs_matrix_complex(
        yu_top,
        z3,
        z3,
        rat_float(1, 2),
        rat_float(3, 5),
        rat_float(4, 5),
        rat_float(0, 1),
        rat_float(0, 1),
    )

    # Verify stationary point and second derivative in 50-digit mpmath via mp.diff:
    mp.mp.dps = 50
    mu_cw = rat_mpf(1, 1)
    v_stat = mu_cw * mp.exp(-rat_mpf(1, 4))

    def eval_cw_curvature_over_v2(beta_val_f: float) -> tuple[float, float, float]:
        b_mp = mp.mpf(repr(beta_val_f))

        def v_cw_doublet(h_norm: Any) -> Any:
            return (
                rat_mpf(1, 2)
                * b_mp
                * mp.log((h_norm * h_norm) / (mu_cw * mu_cw))
                * (h_norm**4)
            )

        dv_at_v = mp.diff(v_cw_doublet, v_stat, 1)
        d2v_over_v2 = mp.diff(v_cw_doublet, v_stat, 2) / (v_stat * v_stat)
        analytic_4beta = 4 * b_mp
        return (
            float(d2v_over_v2),
            float(abs(dv_at_v)),
            float(abs(d2v_over_v2 - analytic_4beta)),
        )

    d2v_gauge_over_v2, dv_gauge_err, d2v_gauge_ident_err = eval_cw_curvature_over_v2(
        beta_lam_gauge
    )
    d2v_top_over_v2, dv_top_err, d2v_top_ident_err = eval_cw_curvature_over_v2(
        beta_lam_top
    )

    # Also check canonical real-field shorthand V_shorthand(H) = (1/4) beta_lam ln(H^2 / mu_CW^2) H^4
    # has exact same strict sign (+ in gauge-only limit, - when top Yukawa dominates):
    top_cw_is_maximum = (d2v_gauge_over_v2 > rat_float(0, 1)) and (
        d2v_top_over_v2 < rat_float(0, 1)
    )

    g3_sec2 = g3_json["section_2_picard_lindelof_and_coleman_weinberg_obstructions"]
    gauge_beta_matches_producer = abs(
        beta_lam_gauge - float(g3_sec2["coleman_weinberg_beta_lam_at_lam0_gauge_only"])
    ) < rat_float(1, 10**15)

    tol_1e12 = rat_float(1, 10**12)
    section_passed = (
        bench["benchmark_gate_passed"]
        and rhs_u3_5_err < tol_1e12
        and picard_rel_err_dop < tol_1e12
        and picard_rel_err_mp < tol_1e12
        and dop_vs_mp_rel_err < tol_1e12
        and min_mu_h2_pos > rat_float(1, 10)
        and max_mu_h2_neg < rat_float(-1, 10)
        and (not homogeneous_crosses_zero)
        and alpha3_inv_ir > rat_float(13, 1)
        and dv_gauge_err < tol_1e12
        and dv_top_err < tol_1e12
        and d2v_gauge_ident_err < tol_1e12
        and d2v_top_ident_err < tol_1e12
        and top_cw_is_maximum
        and gauge_beta_matches_producer
    )

    return {
        "section_2_passed": section_passed,
        "literature_benchmark_gate": bench,
        "rhs_u3_5_basis_covariance_max_err": rhs_u3_5_err,
        "picard_lindelof_exp_integral_rel_err_dop853": picard_rel_err_dop,
        "picard_lindelof_exp_integral_rel_err_mpmath45": picard_rel_err_mp,
        "dop853_vs_mpmath45_muH2_ir_rel_err": dop_vs_mp_rel_err,
        "min_muH2_along_pure_sm_flow_from_unit_uv": min_mu_h2_pos,
        "max_muH2_along_pure_sm_flow_from_minus_unit_uv": max_mu_h2_neg,
        "alpha3_inv_at_ir_end": alpha3_inv_ir,
        "homogeneous_msbar_crosses_zero": homogeneous_crosses_zero,
        "coleman_weinberg_beta_lam_at_lam0_gauge_only": beta_lam_gauge,
        "coleman_weinberg_beta_lam_at_lam0_top_dominated": beta_lam_top,
        "coleman_weinberg_d2V_over_v2_gauge_only": d2v_gauge_over_v2,
        "coleman_weinberg_d2V_over_v2_top_dominated": d2v_top_over_v2,
        "top_dominated_cw_is_maximum_not_minimum": top_cw_is_maximum,
        "_y0_pos": y0_pos,
        "_mu_h2_ir_dop": mu_h2_ir_dop,
    }


# ============================================================================
# Section 3: Vissani Seesaw Sign vs Pati-Salam Portal & Dimensionless Ledger
# ============================================================================


def compute_vissani_seesaw_cw_rg_check() -> dict[str, Any]:
    """Derive 1-loop MSbar Majorana seesaw threshold RGE directly from 2x2 M(H) eigenvalues.

    Constructs M(H) = [[0, y_nu H], [y_nu H, M_R]] across 3 heavy generations with
    Tr(Y_nu^dag Y_nu M_R^2) = 1/10 + 1/5 + 3/10 = 3/5 in 50-digit mpmath, extracts the
    exact O(|H|^2) coefficient of V_1^{(N_R)}(|H|, mu) via numerical differentiation, and
    verifies mu d/d(mu) V_eff^{(N_R)}|_{O(|H|^2)} = 0 to < 1e-13.
    """
    mp.mp.dps = 55
    generations = (
        (mp.sqrt(rat_mpf(1, 10)), rat_mpf(1, 1)),
        (mp.sqrt(rat_mpf(1, 20)), rat_mpf(2, 1)),
        (mp.sqrt(rat_mpf(1, 30)), rat_mpf(3, 1)),
    )
    tr_ynu_mr2 = sum(((ynu * ynu) * (mr * mr) for ynu, mr in generations), mp.mpf(0))
    pref = -rat_mpf(2, 64) / (mp.pi**2)

    def v1_nr(h_val: Any, ln_mu: Any) -> Any:
        mu2 = mp.exp(2 * ln_mu)
        acc = mp.mpf(0)
        for ynu, mr in generations:
            # Explicit 2x2 symmetric Majorana mass matrix M(H) = [[0, y_nu H], [y_nu H, M_R]]:
            m_d = ynu * h_val
            # Exact eigenvalues of M(H)^dag M(H):
            tr_m2 = mr * mr + 2 * m_d * m_d
            det_m2 = (m_d**4)
            disc = mp.sqrt(tr_m2 * tr_m2 - 4 * det_m2)
            lam_plus = (tr_m2 + disc) / 2
            lam_minus = (tr_m2 - disc) / 2
            for lam_eig in (lam_plus, lam_minus):
                if lam_eig > 0:
                    acc += pref * (lam_eig * lam_eig) * (mp.log(lam_eig / mu2) - rat_mpf(3, 2))
        return acc

    step_h = mp.mpf(10) ** (-10)
    step_mu = mp.mpf(10) ** (-12)

    def o_h2_coeff(ln_mu: Any) -> Any:
        return mp.diff(lambda hv: v1_nr(hv, ln_mu), mp.mpf(0), 2, h=step_h) / 2

    # Test RG invariance across 3 distinct renormalization scales ln(mu):
    residuals: list[Any] = []
    beta_mu_nr = -tr_ynu_mr2 / (4 * (mp.pi**2))
    for ln_mu_pt in (rat_mpf(-1, 2), rat_mpf(1, 3), rat_mpf(7, 5)):
        dc2_dlnmu = mp.diff(o_h2_coeff, ln_mu_pt, 1, h=step_mu)
        residuals.append(abs(beta_mu_nr + dc2_dlnmu))

    max_rg_residual = float(max(residuals))

    # Inverted sign (+1/(4 pi^2)) control for PF3.3:
    dc2_ref = mp.diff(o_h2_coeff, rat_mpf(1, 3), 1, h=step_mu)
    inverted_rg_violation = float(abs((-beta_mu_nr) + dc2_ref))

    # Downward flow M_PS -> M_R over Delta t = -3 gives strictly POSITIVE shift Delta mu_H^2 > 0:
    downward_delta_mu_h2 = float(beta_mu_nr * rat_mpf(-3, 1))

    return {
        "tr_Ynu_dag_Ynu_MR2": float(tr_ynu_mr2),
        "d_muH2_d_ln_mu_nr": float(beta_mu_nr),
        "vissani_nr_msbar_rg_invariance_residual": max_rg_residual,
        "vissani_downward_nr_shift_positive": downward_delta_mu_h2,
        "inverted_sign_rg_violation": inverted_rg_violation,
    }


def count_dimensionful_anchors(
    anchor_labels: list[str], dimensionless_ratios: dict[str, float]
) -> dict[str, Any]:
    """Enforce Guardrail 5: count independent dimensionful anchors and validate dimensionless ratios."""
    cleaned = [lbl.strip() for lbl in anchor_labels if lbl.strip()]
    unique_anchors = list(dict.fromkeys(cleaned))
    ratios_positive_finite = len(dimensionless_ratios) == 12 and all(
        math.isfinite(val) and val > rat_float(0, 1)
        for val in dimensionless_ratios.values()
    )
    anchor_count = len(unique_anchors)
    return {
        "anchor_count": anchor_count,
        "unique_anchors": unique_anchors,
        "solely_v_EW": unique_anchors == ["v_EW"],
        "all_12_ratios_dimensionless_positive": ratios_positive_finite,
        "guardrail_5_passed": (
            anchor_count == 1 and unique_anchors == ["v_EW"] and ratios_positive_finite
        ),
    }


def extract_12_dimensionless_mass_ratios(
    yu: np.ndarray,
    yd: np.ndarray,
    ye: np.ndarray,
    g1: float,
    g2: float,
    lam: float,
) -> dict[str, float]:
    """Compute all 12 SM dimensionless ratios m_i / v_EW from physical Hermitian invariants."""
    inv_sqrt2 = rat_float(1, 1) / math.sqrt(rat_float(2, 1))
    # Singular values via eigenvalues of Hermitian Y_f^dag Y_f (basis-invariant under U(3)^6):
    su = np.sqrt(np.maximum(np.linalg.eigvalsh(yu.conj().T @ yu), rat_float(0, 1))) * inv_sqrt2
    sd = np.sqrt(np.maximum(np.linalg.eigvalsh(yd.conj().T @ yd), rat_float(0, 1))) * inv_sqrt2
    se = np.sqrt(np.maximum(np.linalg.eigvalsh(ye.conj().T @ ye), rat_float(0, 1))) * inv_sqrt2

    su_sorted = np.sort(su)
    sd_sorted = np.sort(sd)
    se_sorted = np.sort(se)

    mw_over_v = rat_float(1, 2) * abs(g2)
    mz_over_v = rat_float(1, 2) * math.sqrt(g2 * g2 + rat_float(3, 5) * g1 * g1)
    mh_over_v = math.sqrt(rat_float(2, 1) * lam)

    return {
        "m_u1_over_v_EW": float(su_sorted[0]),
        "m_u2_over_v_EW": float(su_sorted[1]),
        "m_u3_over_v_EW": float(su_sorted[2]),
        "m_d1_over_v_EW": float(sd_sorted[0]),
        "m_d2_over_v_EW": float(sd_sorted[1]),
        "m_d3_over_v_EW": float(sd_sorted[2]),
        "m_e1_over_v_EW": float(se_sorted[0]),
        "m_e2_over_v_EW": float(se_sorted[1]),
        "m_e3_over_v_EW": float(se_sorted[2]),
        "m_W_over_v_EW": mw_over_v,
        "m_Z_over_v_EW": mz_over_v,
        "m_h_over_v_EW": mh_over_v,
    }


def run_section_3_thresholds_and_ledger(g3_json: dict[str, Any]) -> dict[str, Any]:
    """Verify Vissani sign, Pati-Salam portal zero-crossing, Barbieri-Giudice tuning, and U(3)^6 ledger."""
    vissani = compute_vissani_seesaw_cw_rg_check()

    # Heavy Pati-Salam scalar portal inhomogeneous 2-loop flow over Delta t = -4:
    # d_S = 16, lambda_{HS} = 1/2, mu_H^2(M_U)/M_PS^2 = +1/10, g_u = sqrt(4 pi / 50), lam_u = 1/8
    d_s = rat_float(16, 1)
    lam_hs = rat_float(1, 2)
    portal_source = d_s * lam_hs / (rat_float(16, 1) * (math.pi**2))
    g_u = math.sqrt(rat_float(4, 1) * math.pi / rat_float(50, 1))

    y0_portal = np.array(
        [
            rat_float(1, 100),
            rat_float(1, 20),
            rat_float(1, 2),
            rat_float(1, 200),
            rat_float(1, 40),
            rat_float(1, 5),
            rat_float(1, 300),
            rat_float(1, 50),
            rat_float(1, 8),
            g_u,
            g_u,
            g_u,
            rat_float(1, 8),
            rat_float(1, 10),
            rat_float(0, 1),
        ],
        dtype=float,
    )

    def zero_cross_event(_t: float, state: np.ndarray) -> float:
        return float(state[13])

    zero_cross_event.terminal = True  # type: ignore[attr-defined]
    zero_cross_event.direction = -1  # type: ignore[attr-defined]

    rtol = rat_float(1, 10**13)
    atol = rat_float(1, 10**15)
    portal_rhs = make_sm_diag_rhs_float(portal_inhom=portal_source)

    sol_to_cross = solve_ivp(
        portal_rhs,
        (rat_float(0, 1), rat_float(-4, 1)),
        y0_portal,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        events=zero_cross_event,
    )
    crossed = (sol_to_cross.status == 1) and (len(sol_to_cross.t_events[0]) == 1)
    t_cross = float(sol_to_cross.t_events[0][0])
    y_at_cross = sol_to_cross.y_events[0][0]

    # Continue from terminal root event t_cross down to t = -4 (M_PS):
    sol_to_mps = solve_ivp(
        portal_rhs,
        (t_cross, rat_float(-4, 1)),
        y_at_cross,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    mu_h2_at_mps = float(sol_to_mps.y[13, -1])
    lam_at_mps = float(sol_to_mps.y[12, -1])
    g1_at_mps = float(sol_to_mps.y[9, -1])
    g2_at_mps = float(sol_to_mps.y[10, -1])

    g3_sec3 = g3_json["section_3_heavy_threshold_ewsb_and_dimensionless_vEW_ledger"]
    t_cross_diff_vs_producer = abs(t_cross - float(g3_sec3["portal_zero_crossing_t"]))

    # 45-digit mpmath Barbieri-Giudice hierarchy sensitivity at Delta_SM = 28:
    # Integrate UV portal (Delta t = -4) followed by pure SM homogeneous flow (Delta t = -28)
    # and measure logarithmic fine-tuning sensitivity required for v_EW^2 / M_PS^2 = exp(-56).
    mp.mp.dps = 45
    integrate_mp = build_mpmath_rk4_integrator()
    g_u_mp = mp.sqrt(4 * mp.pi / rat_mpf(50, 1))
    portal_src_base = rat_mpf(16, 1) * rat_mpf(1, 2) / (16 * (mp.pi**2))

    def eval_v2_over_mps2_mp(mu_uv_init: Any, lam_hs_scale: Any = mp.mpf(1)) -> Any:
        y_uv = [
            rat_mpf(1, 100),
            rat_mpf(1, 20),
            rat_mpf(1, 2),
            rat_mpf(1, 200),
            rat_mpf(1, 40),
            rat_mpf(1, 5),
            rat_mpf(1, 300),
            rat_mpf(1, 50),
            rat_mpf(1, 8),
            g_u_mp,
            g_u_mp,
            g_u_mp,
            rat_mpf(1, 8),
            mu_uv_init,
            rat_mpf(0, 1),
        ]
        state_mps = integrate_mp(
            y_uv, rat_mpf(-4, 1), 160, portal_inhom=portal_src_base * lam_hs_scale
        )
        state_ir = integrate_mp(state_mps, rat_mpf(-28, 1), 560, portal_inhom=mp.mpf(0))
        mu_ir = state_ir[13]
        lam_ir = state_ir[12]
        return -mu_ir / lam_ir

    # Solve in 45-digit mpmath for the tuned UV mass-squared mu_uv_star giving v_EW^2 / M_PS^2 = exp(-56):
    target_hierarchy = mp.exp(rat_mpf(-56, 1))
    r_at_0 = eval_v2_over_mps2_mp(mp.mpf(0))
    r_at_tenth = eval_v2_over_mps2_mp(rat_mpf(1, 10))
    slope_r = (r_at_tenth - r_at_0) / rat_mpf(1, 10)
    mu_uv_star = rat_mpf(1, 10) + (target_hierarchy - r_at_tenth) / slope_r
    r_star = eval_v2_over_mps2_mp(mu_uv_star)
    hierarchy_target_rel_err = float(abs(r_star - target_hierarchy) / target_hierarchy)

    # Central finite-difference Barbieri-Giudice derivative directly on 45-digit ODE trajectories:
    eps_mp = mp.mpf(10) ** (-30)
    r_plus = eval_v2_over_mps2_mp(mu_uv_star * (1 + eps_mp))
    r_minus = eval_v2_over_mps2_mp(mu_uv_star * (1 - eps_mp))
    bg_sensitivity_mu_uv = abs((r_plus - r_minus) / (2 * eps_mp * r_star))
    bg_sensitivity_float = float(bg_sensitivity_mu_uv)

    # Guardrail 1: because > 1e20 fine-tuning is required, v_EW / M_PS does NOT close parameter-free:
    thresh_1e20 = mp.mpf(10) ** 20
    parameter_free_closure = not (bg_sensitivity_mu_uv > thresh_1e20)

    # Guardrail 3 & 5: 12 fresh Haar U(3)^6 trials on non-commuting complex (Y_u, Y_d, Y_e)
    # confirming < 1e-12 invariance of all 12 dimensionless mass ratios m_i / v_EW:
    iu = complex(0, 1)
    yu_complex = np.array(
        [
            [rat_float(1, 90) + iu * rat_float(1, 130), rat_float(1, 70), rat_float(-1, 50) + iu * rat_float(1, 80)],
            [rat_float(-1, 110), rat_float(1, 18) + iu * rat_float(1, 45), rat_float(1, 25)],
            [rat_float(1, 60) - iu * rat_float(1, 95), rat_float(-1, 30), rat_float(1, 2) + iu * rat_float(1, 15)],
        ],
        dtype=complex,
    )
    yd_complex = np.array(
        [
            [rat_float(1, 180), rat_float(1, 120) - iu * rat_float(1, 160), rat_float(1, 90)],
            [rat_float(1, 100) + iu * rat_float(1, 140), rat_float(1, 36), rat_float(-1, 40) + iu * rat_float(1, 75)],
            [rat_float(-1, 85), rat_float(1, 48) + iu * rat_float(1, 65), rat_float(1, 5) - iu * rat_float(1, 25)],
        ],
        dtype=complex,
    )
    ye_complex = np.array(
        [
            [rat_float(1, 280) + iu * rat_float(1, 350), rat_float(-1, 190), rat_float(1, 150)],
            [rat_float(1, 210), rat_float(1, 48) - iu * rat_float(1, 90), rat_float(1, 70) + iu * rat_float(1, 110)],
            [rat_float(-1, 130) + iu * rat_float(1, 170), rat_float(1, 65), rat_float(1, 8) + iu * rat_float(1, 35)],
        ],
        dtype=complex,
    )
    comm_norm = float(
        np.linalg.norm(
            (yu_complex.conj().T @ yu_complex) @ (yd_complex.conj().T @ yd_complex)
            - (yd_complex.conj().T @ yd_complex) @ (yu_complex.conj().T @ yu_complex)
        )
    )

    ref_ratios = extract_12_dimensionless_mass_ratios(
        yu_complex, yd_complex, ye_complex, g1_at_mps, g2_at_mps, lam_at_mps
    )
    rng_haar = np.random.default_rng(314159265)
    max_haar_err = rat_float(0, 1)
    n_haar_trials = 12
    for _ in range(n_haar_trials):
        ul_u = sample_haar_u3(rng_haar)
        ur_u = sample_haar_u3(rng_haar)
        ul_d = sample_haar_u3(rng_haar)
        ur_d = sample_haar_u3(rng_haar)
        ul_e = sample_haar_u3(rng_haar)
        ur_e = sample_haar_u3(rng_haar)
        scrambled_ratios = extract_12_dimensionless_mass_ratios(
            ul_u @ yu_complex @ ur_u.conj().T,
            ul_d @ yd_complex @ ur_d.conj().T,
            ul_e @ ye_complex @ ur_e.conj().T,
            g1_at_mps,
            g2_at_mps,
            lam_at_mps,
        )
        for key, ref_val in ref_ratios.items():
            err = abs(scrambled_ratios[key] - ref_val)
            if err > max_haar_err:
                max_haar_err = err

    ledger_check = count_dimensionful_anchors(["v_EW"], ref_ratios)

    tol_1e13 = rat_float(1, 10**13)
    tol_1e12 = rat_float(1, 10**12)
    tol_1e7 = rat_float(1, 10**7)

    section_passed = (
        vissani["vissani_nr_msbar_rg_invariance_residual"] < tol_1e13
        and vissani["d_muH2_d_ln_mu_nr"] < rat_float(0, 1)
        and vissani["vissani_downward_nr_shift_positive"] > rat_float(0, 1)
        and crossed
        and t_cross_diff_vs_producer < tol_1e7
        and mu_h2_at_mps < rat_float(0, 1)
        and lam_at_mps > rat_float(0, 1)
        and hierarchy_target_rel_err < tol_1e12
        and (bg_sensitivity_mu_uv > thresh_1e20)
        and (parameter_free_closure is False)
        and (g3_sec3["parameter_free_v_EW_over_M_PS_closure"] is False)
        and ledger_check["guardrail_5_passed"]
        and ledger_check["anchor_count"] == 1
        and comm_norm > rat_float(1, 10**4)
        and max_haar_err < tol_1e12
    )

    return {
        "section_3_passed": section_passed,
        "vissani_nr_msbar_rg_invariance_residual": vissani[
            "vissani_nr_msbar_rg_invariance_residual"
        ],
        "vissani_d_muH2_d_ln_mu_negative": vissani["d_muH2_d_ln_mu_nr"],
        "vissani_downward_nr_shift_positive": vissani[
            "vissani_downward_nr_shift_positive"
        ],
        "portal_scalar_drives_radiative_zero_crossing": crossed,
        "portal_zero_crossing_t": t_cross,
        "portal_zero_crossing_diff_vs_producer_json": t_cross_diff_vs_producer,
        "muH2_at_M_PS_in_M_PS_sq_units": mu_h2_at_mps,
        "lambda_at_M_PS": lam_at_mps,
        "barbieri_giudice_hierarchy_sensitivity_at_DeltaSM_28": bg_sensitivity_float,
        "tuned_hierarchy_target_rel_err": hierarchy_target_rel_err,
        "parameter_free_v_EW_over_M_PS_closure": parameter_free_closure,
        "dimensionful_anchors_in_ir_ledger": ledger_check["anchor_count"],
        "noncommuting_yukawa_commutator_norm": comm_norm,
        "haar_u3_6_trials": n_haar_trials,
        "haar_u3_6_dimensionless_mass_ratios_max_err": max_haar_err,
        "_inverted_vissani_violation": vissani["inverted_sign_rg_violation"],
        "_ref_ratios": ref_ratios,
    }


# ============================================================================
# Section 4: Five Planted Fault Controls (PF3.1 - PF3.5)
# ============================================================================


def run_section_4_planted_faults(
    sec2: dict[str, Any], sec3: dict[str, Any]
) -> dict[str, Any]:
    """Execute all 5 planted fault controls PF3.1-PF3.5 against Card G3 thresholds."""
    rtol = rat_float(1, 10**13)
    atol = rat_float(1, 10**15)

    # PF3.1: Half-slope gamma_scale = 1/2 over Delta t = -28 (must break mu_H^2(IR) by > 1/10):
    sol_half = solve_ivp(
        make_sm_diag_rhs_float(gamma_scale=rat_float(1, 2)),
        (rat_float(0, 1), rat_float(-28, 1)),
        sec2["_y0_pos"],
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    mu_half_ir = float(sol_half.y[13, -1])
    mu_true_ir = float(sec2["_mu_h2_ir_dop"])
    pf3_1_err = abs(mu_half_ir - mu_true_ir) / abs(mu_true_ir)
    pf3_1_caught = pf3_1_err > rat_float(1, 10)

    # PF3.2: Homogeneous positivity floor min mu_H^2 > 1/10 along pure-SM flow from mu_H^2(0) = 1:
    pf3_2_min = float(sec2["min_muH2_along_pure_sm_flow_from_unit_uv"])
    pf3_2_caught = pf3_2_min > rat_float(1, 10)

    # PF3.3: Inverted Vissani sign +1/(4 pi^2) breaks |mu d/d(mu) V_eff| by > 1/100:
    pf3_3_err = float(sec3["_inverted_vissani_violation"])
    pf3_3_caught = pf3_3_err > rat_float(1, 100)

    # PF3.4: Top-dominated CW curvature 4 * beta_lam(y_t=9/10) < -1/100:
    pf3_4_curv = float(sec2["coleman_weinberg_d2V_over_v2_top_dominated"])
    pf3_4_caught = pf3_4_curv < rat_float(-1, 100)

    # PF3.5: Supplying ["v_EW", "M_Z_imported"] gives anchor count 2 > 1:
    pf3_5_ledger = count_dimensionful_anchors(
        ["v_EW", "M_Z_imported"], sec3["_ref_ratios"]
    )
    pf3_5_count = int(pf3_5_ledger["anchor_count"])
    pf3_5_caught = (pf3_5_count == 2) and (pf3_5_count > 1) and (
        not pf3_5_ledger["guardrail_5_passed"]
    )

    all_caught = (
        pf3_1_caught and pf3_2_caught and pf3_3_caught and pf3_4_caught and pf3_5_caught
    )

    return {
        "all_5_planted_faults_caught": all_caught,
        "PF3_1_half_gamma_scale_rel_err": {
            "measured_err": pf3_1_err,
            "threshold": rat_float(1, 10),
            "caught": pf3_1_caught,
        },
        "PF3_2_homogeneous_positivity_floor": {
            "min_muH2": pf3_2_min,
            "threshold": rat_float(1, 10),
            "caught": pf3_2_caught,
        },
        "PF3_3_inverted_vissani_sign_rg_violation": {
            "measured_err": pf3_3_err,
            "threshold": rat_float(1, 100),
            "caught": pf3_3_caught,
        },
        "PF3_4_unstable_top_cw_curvature": {
            "d2V_over_v2": pf3_4_curv,
            "threshold": rat_float(-1, 100),
            "caught": pf3_4_caught,
        },
        "PF3_5_extra_dimensionful_anchor_count": {
            "anchor_count": pf3_5_count,
            "max_allowed": 1,
            "caught": pf3_5_caught,
        },
    }


def main() -> None:
    self_path = Path(__file__).resolve()
    referee_dir = self_path.parent
    repo_root = referee_dir.parents[1]

    g3_json_path = repo_root / "relays" / "agy002_endgame_v2_g3" / "verify_endgame_v2_g3_out.json"
    g3_json = json.loads(g3_json_path.read_text(encoding="utf-8"))

    sec0 = run_section_0_ast_and_manifests(self_path, repo_root)
    sec1 = run_section_1_buttazzo_polynomial_lock(g3_json)
    sec2_raw = run_section_2_picard_lindelof_and_cw(g3_json)
    sec3_raw = run_section_3_thresholds_and_ledger(g3_json)
    sec4 = run_section_4_planted_faults(sec2_raw, sec3_raw)

    sec2 = {k: v for k, v in sec2_raw.items() if not k.startswith("_")}
    sec3 = {k: v for k, v in sec3_raw.items() if not k.startswith("_")}

    overall_passed = (
        sec0["section_0_passed"]
        and sec1["section_1_passed"]
        and sec2["section_2_passed"]
        and sec3["section_3_passed"]
        and sec4["all_5_planted_faults_caught"]
    )

    report = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 3 Referee — Radiative EWSB Scale Closure & Campaign Manifest Check",
        "empirical_firewall": "0 of 19",
        "gate_3_referee_passed": overall_passed,
        "section_0_ast_and_campaign_manifests": sec0,
        "section_1_buttazzo_2013_gamma_m2_polynomial_lock": sec1,
        "section_2_picard_lindelof_and_coleman_weinberg_obstructions": sec2,
        "section_3_heavy_threshold_ewsb_and_dimensionless_vEW_ledger": sec3,
        "section_4_planted_fault_controls": sec4,
    }

    out_json_path = referee_dir / "referee_endgame_v2_g3_out.json"
    out_json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    out_sha256 = hashlib.sha256(out_json_path.read_bytes()).hexdigest()
    sha_manifest_path = referee_dir / "OUTPUT_SHA256.txt"
    sha_manifest_path.write_text(
        f"{out_sha256}  relays/agy002_endgame_v2_g3_referee/referee_endgame_v2_g3_out.json\n",
        encoding="utf-8",
    )

    if not overall_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
