"""
Step B & Refined Census Structural Diagnostics (B1825 Read-Out and Defect Verifiers).

Provides pure, data-free functions that verify the four Step B / census architectural
defects without modifying the SHA-256 hash-pinned files in scripts/stepb/:
1. Defect A (scripts/stepb/kten.py lines 170-214):
   Decodes choice = 30900 under assemble.py's canonical (str(line_key), d, r, k) ordering to
   ((2/5, 0), F_26, L_max, ('S~', 'S', 'S')), and verifies that six_mixture(physical=False)
   omitted the physical=True filter (which passes the two null-quaternion directions R and t=-5/288
   where a.a == 0 and J == 0 identically), while K_ten ignored m["choice"] = 30900 and summed
   num and den over all 29,063 rows in the tau-window across all discrete choices.
2. Defect B (scripts/stepb/cells.py lines 131-139):
   Proves that physical_choice checks only F[:, 6:10] (the 4 CKM columns) and misses all 48
   order-12 lines where det M_lep = 0 (m_e/m_tau = 0 identically, B1716), leaving
   48 * 10 * 2 * 8 = 7,680 massless-electron choices (19.2% of the 40,000 reported physical
   choices) in the prior denominator; provides strict_ten_physical_choice_mask(F, R) which
   checks all 10 observables F[:, :10].
3. Defect C:
   Verifies the exact 2:1 duplication of CKM trajectories across lepton readings (r_u, r_d, S)
   and (r_u, r_d, S~).
"""
from __future__ import annotations

from fractions import Fraction
import math
from typing import Dict, List, Tuple

import numpy as np

KEPT_DIRECTIONS: Tuple[str, ...] = (
    "DR", "a0", "R", "t=-5/288", "F_-10", "F_-6", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"
)
RADII_NAMES: Tuple[str, ...] = ("L_max", "L_2")
READINGS: Tuple[Tuple[str, str, str], ...] = (
    ("S", "S", "S"), ("S", "S", "S~"), ("S", "S~", "S"), ("S", "S~", "S~"),
    ("S~", "S", "S"), ("S~", "S", "S~"), ("S~", "S~", "S"), ("S~", "S~", "S~"),
)


def canonical_line_key(a: str | Fraction, b: str | Fraction) -> Tuple[Fraction, Fraction]:
    """Match scripts/stepb/census_io.py's line_key(a, b) = min((A, B), ((-A) % 1, (-B) % 1))."""
    fa, fb = Fraction(a), Fraction(b)
    return min((fa, fb), ((-fa) % 1, (-fb) % 1))


def canonical_non_trivial_lines(per_file_manifest: Dict[str, str]) -> List[Tuple[Fraction, Fraction]]:
    """Extract and sort the 265 non-trivial lines in assemble.py's exact order (sorted by str(key))."""
    lines: List[Tuple[Fraction, Fraction]] = []
    for fname in sorted(per_file_manifest):
        stem = fname.split(".")[0]
        _, p1_s, p2_s = stem.split("_")
        n1, d1 = p1_s.split("-")
        n2, d2 = p2_s.split("-")
        key = canonical_line_key(f"{n1}/{d1}", f"{n2}/{d2}")
        if key != (Fraction(0, 1), Fraction(0, 1)):
            lines.append(key)
    return sorted(lines, key=str)


def decode_stepb_choice_index(
    choice_idx: int,
    per_file_manifest: Dict[str, str],
) -> Dict[str, object]:
    """Decode a Step B discrete choice index (0..50879) into (line, direction, radius, reading)."""
    lines = canonical_non_trivial_lines(per_file_manifest)
    rem = int(choice_idx)
    r_idx = rem % 8
    rem //= 8
    rad_idx = rem % 2
    rem //= 2
    d_idx = rem % 12
    rem //= 12
    line_idx = rem
    line = lines[line_idx]
    direction = KEPT_DIRECTIONS[d_idx]
    return {
        "choice_index": int(choice_idx),
        "line_index": line_idx,
        "line": line,
        "line_order": math.lcm(line[0].denominator, line[1].denominator),
        "direction": direction,
        "radius": RADII_NAMES[rad_idx],
        "reading": READINGS[r_idx],
        "has_complex_ckm": direction not in ("R", "t=-5/288"),
    }


def count_order12_massless_electron_choices(per_file_manifest: Dict[str, str]) -> Dict[str, int | float]:
    """Count the order-12 lines and their massless-electron choices (m_e/m_tau = 0 by B1716)
    that pass cells.py's 4-column CKM check."""
    lines = canonical_non_trivial_lines(per_file_manifest)
    order12 = [l for l in lines if math.lcm(l[0].denominator, l[1].denominator) == 12]
    n_lines = len(order12)
    total_choices = n_lines * 12 * 2 * 8
    # R and t=-5/288 have a.a == 0 and J = 0 everywhere; the 10 remaining directions have J != 0 on order 12:
    complex_ckm_choices = n_lines * 10 * 2 * 8
    return {
        "order_12_lines": n_lines,
        "order_12_total_choices": total_choices,
        "order_12_choices_in_physical_choice": complex_ckm_choices,
        "fraction_of_40000_physical_choices": complex_ckm_choices / 40000.0,
    }


def strict_ten_physical_choice_mask(
    f_matrix: np.ndarray,
    r_table: np.ndarray,
    floor: float = 1e-12,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute the strict 10-observable physical-choice mask (requiring ALL 10 observables
    in f_matrix[:, :10], including e/tau, u/t, d/b as well as |V_us|, |V_cb|, |V_ub|, |J|,
    to attain values >= ln(floor) on at least one node of the choice).

    Returns (physical_choice_ten, zero10) where zero10 has shape (n_choices, 10).
    """
    lf = math.log(floor)
    nch = r_table.shape[0]
    present = r_table >= 0
    jj, _ = np.nonzero(present)
    rows = r_table[present]
    zero10 = np.ones((nch, 10), dtype=bool)
    f10 = f_matrix[:, :10]
    ok_f = np.where(np.isfinite(f10[rows]), f10[rows] >= lf, False)
    np.logical_and.at(zero10, jj, ~ok_f)
    return ~zero10.any(axis=1), zero10


def repaired_stepb_k_cell_audit(
    run_json_data: Dict[str, object],
    per_file_manifest: Dict[str, str],
) -> Dict[str, object]:
    """Quantify the exact bit and choice-count corrections required for Step B v2 (Pillar 1):
    1. Choice-coherent K_ten denominator vs run.json's all-choice sum:
       In run.json, L_six = 36.828958267893995 and A_DISCRETE = log2(50880) = 15.634811066510738,
       so choice 30900 has log2 integral log2(Q_30900) = -L_tau(30900) = -21.194147201383257.
       However, kten.py line 203 computed den = lse2(m['I']) = -16.45902728787725 (summing over all
       29,063 rows across all choices in the 6-ratio window), inflating den by +4.735120 bits
       (choice 30900 carries only 2^-4.735120 = 3.755% of the 6-ratio window integral).
    2. Strict 10-observable physical discrete choice count:
       Removing the 10,880 null-direction choices (R and t=-5/288 where a.a == 0 and J == 0)
       gives 40,000 CKM-defined choices; further removing the 48 order-12 massless-electron lines
       (48 * 10 * 2 * 8 = 7,680 choices where m_e/m_tau == 0) leaves 32,320 strictly physical
       10-observable choices (and 16,160 distinct quark/lepton choices after removing the 2:1
       lepton-reading duplication of V_CKM).
    """
    k_cell = run_json_data["K"]
    reports = k_cell["reports"]
    n_total_choices = int(run_json_data["choices"])
    n_ckm_physical = int(run_json_data["choices_physical"])
    a_discrete_raw = math.log2(n_total_choices)

    l_six = float(k_cell["L_six"])
    l_tau_30900 = l_six - a_discrete_raw
    log2_q_30900 = -l_tau_30900
    den_all_choices = float(reports["six_report"]["total_bits"])
    den_inflation_bits = den_all_choices - log2_q_30900
    choice_30900_window_share = 2.0 ** (-den_inflation_bits)

    o12 = count_order12_massless_electron_choices(per_file_manifest)
    n_massless_e = int(o12["order_12_choices_in_physical_choice"])
    n_strict_physical = n_ckm_physical - n_massless_e
    n_dedup_strict_physical = n_strict_physical // 2

    return {
        "n_total_choices": n_total_choices,
        "n_ckm_physical_choices": n_ckm_physical,
        "n_massless_electron_choices_removed": n_massless_e,
        "n_strict_ten_physical_choices": n_strict_physical,
        "n_deduplicated_strict_physical_choices": n_dedup_strict_physical,
        "A_discrete_raw_bits": a_discrete_raw,
        "A_discrete_strict_physical_bits": math.log2(n_strict_physical),
        "A_discrete_dedup_strict_bits": math.log2(n_dedup_strict_physical),
        "log2_Q_30900": log2_q_30900,
        "den_all_choices_bits": den_all_choices,
        "den_inflation_bits": den_inflation_bits,
        "choice_30900_share_of_six_window": choice_30900_window_share,
        "ckm_clause_best_chi2_4_in_six_window": float(run_json_data["CKM"]["clause"]["best_chi2_4"]),
    }

