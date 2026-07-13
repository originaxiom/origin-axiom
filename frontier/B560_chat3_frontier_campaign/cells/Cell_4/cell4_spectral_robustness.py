#!/usr/bin/env python3
"""Cell 4 — degree-4 spectral robustness and measurement audit."""

from __future__ import annotations

from pathlib import Path
import csv
import itertools
import json
import math

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parent

SUB = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
PHI = (1 + np.sqrt(5.0)) / 2
TAU = np.sqrt(PHI)

COUPLINGS = {
    "C1": {"a": 1.0, "b": 0.8, "A": 0.6, "B": 0.4},
    "C2": {"a": 1.0, "b": 0.55, "A": 0.75, "B": 0.35},
}

LABELS = {
    "f_b": TAU**3 - TAU**2 - TAU + 1,
    "f_B": -TAU**3 + TAU + 1,
    "f_a": TAU - 1,
    "f_A": TAU**2 - TAU,
}
LABELS["f_a+f_b"] = LABELS["f_a"] + LABELS["f_b"]


def substitution_word(length: int) -> str:
    word = "a"
    while len(word) < length:
        word = "".join(SUB[letter] for letter in word)
    return word[:length]


def target_gap_from_eigenvalues(
    eigenvalues: np.ndarray,
    target_label: float,
    window: int = 5,
) -> dict:
    size = len(eigenvalues)
    gaps = np.diff(eigenvalues)
    central = int(round(target_label * size))
    candidates = range(
        max(1, central - window),
        min(size, central + window + 1),
    )
    gap_index = max(candidates, key=lambda index: gaps[index - 1])
    width = float(gaps[gap_index - 1])
    rank = int(np.sum(gaps > width) + 1)
    measured_label = gap_index / size
    return {
        "gap_index": gap_index,
        "measured_label": measured_label,
        "label_error": abs(measured_label - target_label),
        "gap_width": width,
        "gap_rank": rank,
    }


def target_gap_local(
    coupling: dict[str, float],
    target_label: float,
    size: int,
    window: int = 6,
) -> dict:
    word = substitution_word(size)
    hopping = np.fromiter(
        (coupling[letter] for letter in word[:-1]),
        dtype=float,
        count=size - 1,
    )
    central = int(round(target_label * size))
    lower = max(0, central - window - 1)
    upper = min(size - 1, central + window)

    eigenvalues = eigh_tridiagonal(
        np.zeros(size),
        hopping,
        select="i",
        select_range=(lower, upper),
        eigvals_only=True,
    )

    best = None
    for offset in range(len(eigenvalues) - 1):
        gap_index = lower + offset + 1
        if abs(gap_index - central) > window:
            continue
        width = float(eigenvalues[offset + 1] - eigenvalues[offset])
        candidate = {
            "gap_index": gap_index,
            "measured_label": gap_index / size,
            "label_error": abs(gap_index / size - target_label),
            "gap_width": width,
        }
        if best is None or candidate["gap_width"] > best["gap_width"]:
            best = candidate

    assert best is not None
    return best


def exact_module_certificate() -> dict:
    t, y = sp.symbols("t y")
    minimal = t**4 - t**2 - 1

    expressions = {
        "f_b": t**3 - t**2 - t + 1,
        "f_B": -t**3 + t + 1,
        "f_a": t - 1,
        "f_A": t**2 - t,
    }
    expressions["f_a+f_b"] = sp.rem(
        expressions["f_a"] + expressions["f_b"],
        minimal,
        t,
    )

    four_frequencies = [
        expressions["f_a"],
        expressions["f_b"],
        expressions["f_A"],
        expressions["f_B"],
    ]
    coefficient_matrix = sp.Matrix([
        [
            sp.Poly(expression, t).coeff_monomial(t**power)
            for expression in four_frequencies
        ]
        for power in range(4)
    ])
    determinant = int(coefficient_matrix.det())
    assert abs(determinant) == 1

    minpolys = {}
    for name, expression in expressions.items():
        resultant = sp.factor(
            sp.resultant(minimal, y - expression, t)
        )
        polynomial = sp.Poly(resultant, y)
        assert polynomial.degree() == 4
        minpolys[name] = str(polynomial.as_expr())

    assert sp.rem(sum(four_frequencies) - 1, minimal, t) == 0

    return {
        "tau_minimal_polynomial": "t^4 - t^2 - 1",
        "frequency_expressions_in_Z_tau": {
            name: str(expression)
            for name, expression in expressions.items()
        },
        "basis_coefficient_matrix_columns_fa_fb_fA_fB":
            [[int(value) for value in row] for row in coefficient_matrix.tolist()],
        "basis_change_determinant": determinant,
        "frequency_module": "Z[f_a,f_b,f_A,f_B] = Z[tau]",
        "all_five_target_labels_have_degree": 4,
        "target_minimal_polynomials": minpolys,
        "sum_of_letter_frequencies": "1 exactly",
    }


def run_chamber(
    chamber_name: str,
    b_values: np.ndarray,
    A_values: np.ndarray,
    B_values: np.ndarray,
    size: int = 3000,
) -> list[dict]:
    word = substitution_word(size)
    records = []

    for b_value, A_value, B_value in itertools.product(
        b_values,
        A_values,
        B_values,
    ):
        coupling = {
            "a": 1.0,
            "b": float(b_value),
            "A": float(A_value),
            "B": float(B_value),
        }
        hopping = np.fromiter(
            (coupling[letter] for letter in word[:-1]),
            dtype=float,
            count=size - 1,
        )
        eigenvalues = eigh_tridiagonal(
            np.zeros(size),
            hopping,
            eigvals_only=True,
        )

        for label_name, target in LABELS.items():
            tracked = target_gap_from_eigenvalues(
                eigenvalues,
                target,
            )
            records.append({
                "chamber": chamber_name,
                "N": size,
                "a": 1.0,
                "b": float(b_value),
                "A": float(A_value),
                "B": float(B_value),
                "label_name": label_name,
                "target_label": float(target),
                **tracked,
            })

    return records


def chamber_summary(records: list[dict]) -> dict:
    summary = {}
    label_names = sorted({record["label_name"] for record in records})
    point_count = len(records) // len(label_names)

    for label_name in label_names:
        subset = [
            record for record in records
            if record["label_name"] == label_name
        ]
        summary[label_name] = {
            "sampled_points": point_count,
            "minimum_gap_width": min(
                record["gap_width"] for record in subset
            ),
            "maximum_gap_rank": max(
                record["gap_rank"] for record in subset
            ),
            "top_30_fraction": sum(
                record["gap_rank"] <= 30 for record in subset
            ) / len(subset),
            "maximum_label_error": max(
                record["label_error"] for record in subset
            ),
        }

    return summary


def finite_size_records() -> list[dict]:
    sizes = [893, 3283, 12069, 44368]
    records = []

    for coupling_name, coupling in COUPLINGS.items():
        for size in sizes:
            for label_name, target in LABELS.items():
                tracked = target_gap_local(
                    coupling,
                    target,
                    size,
                )
                records.append({
                    "coupling": coupling_name,
                    "N": size,
                    "label_name": label_name,
                    "target_label": float(target),
                    **tracked,
                    "N_times_label_error":
                        size * tracked["label_error"],
                })

    return records


def golden_folded_label(index: np.ndarray) -> np.ndarray:
    values = np.mod(index / PHI, 1.0)
    return np.minimum(values, 1 - values)


def nearest_golden_with_cutoff(
    target: float,
    maximum_index: int,
) -> dict:
    indices = np.arange(0, maximum_index + 1, dtype=np.int64)
    values = golden_folded_label(indices)
    distances = np.abs(values - target)
    position = int(np.argmin(distances))
    return {
        "maximum_index": maximum_index,
        "best_index": int(indices[position]),
        "best_label": float(values[position]),
        "distance": float(distances[position]),
    }


def first_golden_index_within(
    target: float,
    tolerance: float,
    maximum_index: int = 250000,
) -> dict:
    indices = np.arange(0, maximum_index + 1, dtype=np.int64)
    values = golden_folded_label(indices)
    distances = np.abs(values - target)
    hits = np.flatnonzero(distances < tolerance)
    if not len(hits):
        return {
            "tolerance": tolerance,
            "first_index": None,
            "label": None,
            "distance": None,
        }

    position = int(hits[0])
    return {
        "tolerance": tolerance,
        "first_index": int(indices[position]),
        "label": float(values[position]),
        "distance": float(distances[position]),
    }


def golden_control_table() -> tuple[list[dict], dict]:
    records = []
    for label_name, target in LABELS.items():
        low_order = nearest_golden_with_cutoff(target, 30)
        for tolerance in (1e-4, 1e-5, 1e-6):
            hit = first_golden_index_within(target, tolerance)
            records.append({
                "label_name": label_name,
                "target_label": float(target),
                "golden_index_cutoff": 30,
                "distance_to_best_index_le_30":
                    low_order["distance"],
                "best_index_le_30": low_order["best_index"],
                **hit,
            })

    minimum_low_order_distance = min(
        record["distance_to_best_index_le_30"]
        for record in records
    )
    required_ids_uncertainty = minimum_low_order_distance / 2
    minimum_counting_size = math.floor(
        1 / required_ids_uncertainty
    ) + 1

    summary = {
        "full_golden_module_mod_1_is_dense": True,
        "single_label_absolute_field_separation": False,
        "corrected_control": (
            "Exclude low-index Fibonacci labels, not the entire dense "
            "golden module."
        ),
        "golden_index_cutoff": 30,
        "minimum_distance_to_index_le_30":
            minimum_low_order_distance,
        "required_total_IDS_uncertainty_below":
            required_ids_uncertainty,
        "counting_only_minimum_N":
            minimum_counting_size,
        "conservative_recommended_N": 5000,
    }
    return records, summary


def center_margin(coupling_name: str, size: int = 3000) -> dict:
    coupling = COUPLINGS[coupling_name]
    word = substitution_word(size)
    hopping = np.fromiter(
        (coupling[letter] for letter in word[:-1]),
        dtype=float,
        count=size - 1,
    )
    eigenvalues = eigh_tridiagonal(
        np.zeros(size),
        hopping,
        eigvals_only=True,
    )

    gaps = {}
    for label_name, target in LABELS.items():
        gaps[label_name] = target_gap_from_eigenvalues(
            eigenvalues,
            target,
        )

    minimum_gap = min(
        record["gap_width"] for record in gaps.values()
    )

    return {
        "coupling": coupling,
        "N": size,
        "target_gaps": gaps,
        "minimum_target_gap_width": minimum_gap,
        "finite_N_Weyl_open_ball_radius_linf": minimum_gap / 4,
        "half_margin_disorder_radius": minimum_gap / 8,
        "combined_budget_inequality":
            "4*delta_hopping + 2*linewidth < minimum_gap_width",
    }


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    exact = exact_module_certificate()

    chamber_1 = run_chamber(
        "C1_BOX",
        np.linspace(0.72, 0.88, 4),
        np.linspace(0.52, 0.68, 4),
        np.linspace(0.32, 0.48, 4),
    )
    chamber_2 = run_chamber(
        "C2_BOX",
        np.linspace(0.52, 0.58, 5),
        np.linspace(0.72, 0.78, 5),
        np.linspace(0.32, 0.38, 5),
    )
    chamber_records = chamber_1 + chamber_2

    finite_size = finite_size_records()
    golden_records, golden_summary = golden_control_table()
    margins = {
        name: center_margin(name)
        for name in COUPLINGS
    }

    chamber_summaries = {
        "C1_BOX": chamber_summary(chamber_1),
        "C2_BOX": chamber_summary(chamber_2),
    }

    certificate = {
        "exact_frequency_module": exact,
        "sampled_coupling_chambers": {
            "C1_BOX": {
                "bounds": {
                    "a": [1.0, 1.0],
                    "b": [0.72, 0.88],
                    "A": [0.52, 0.68],
                    "B": [0.32, 0.48],
                },
                "grid_shape": [4, 4, 4],
                "point_count": 64,
                "summary": chamber_summaries["C1_BOX"],
            },
            "C2_BOX": {
                "bounds": {
                    "a": [1.0, 1.0],
                    "b": [0.52, 0.58],
                    "A": [0.72, 0.78],
                    "B": [0.32, 0.38],
                },
                "grid_shape": [5, 5, 5],
                "point_count": 125,
                "summary": chamber_summaries["C2_BOX"],
            },
            "classification":
                "COMPUTED_FINITE_N_GRID_NOT_CONTINUUM_THEOREM",
        },
        "finite_size": {
            "substitution_prefix_lengths": [893, 3283, 12069, 44368],
            "record_count": len(finite_size),
            "maximum_N_times_label_error": max(
                record["N_times_label_error"]
                for record in finite_size
            ),
            "minimum_gap_width_by_coupling": {
                coupling_name: min(
                    record["gap_width"]
                    for record in finite_size
                    if record["coupling"] == coupling_name
                )
                for coupling_name in COUPLINGS
            },
        },
        "golden_control_correction": golden_summary,
        "finite_N_local_robustness": margins,
        "gap_opening_status": {
            "allowed_label_group": "PROVED_EXACTLY",
            "five_open_target_gaps_at_two_centers":
                "COMPUTED_AND_FINITE_N_PERTURBATION_MARGINS_GIVEN",
            "top_30_on_two_sampled_boxes":
                "COMPUTED_AT_ALL_189_GRID_POINTS",
            "infinite_volume_open_chamber":
                "NOT_PROVED",
            "all_module_labels_open":
                "OPEN_DRY_TEN_MARTINI_TYPE_PROBLEM",
        },
        "classification": {
            "degree_4_module": "PROVED_EXACTLY",
            "five_target_labels_are_degree_4": "PROVED_EXACTLY",
            "coupling_invariance_when_gap_remains_open":
                "CLASSICAL_GAP_LABEL_THEOREM_CONDITION",
            "finite_N_robustness":
                "COMPUTED_WITH_WEYL_LOCAL_BALLS",
            "distance_from_full_golden_module":
                "REFUTED_AS_AN_ABSOLUTE_DISCRIMINATOR",
            "bounded_index_golden_control":
                "QUANTIFIED",
            "experiment_status":
                "DIMENSIONLESS_SPECIFICATION_READY",
            "cell_status":
                "EXPERIMENT_READY_WITH_INFINITE_VOLUME_GAP_OPENING_OPEN",
        },
    }

    (ROOT / "CELL4_SPECTRAL_ROBUSTNESS_CERTIFICATE.json").write_text(
        json.dumps(certificate, indent=2),
        encoding="utf-8",
    )

    write_csv(
        ROOT / "cell4_coupling_chamber.csv",
        chamber_records,
        [
            "chamber", "N", "a", "b", "A", "B", "label_name",
            "target_label", "gap_index", "measured_label",
            "label_error", "gap_width", "gap_rank",
        ],
    )
    write_csv(
        ROOT / "cell4_finite_size.csv",
        finite_size,
        [
            "coupling", "N", "label_name", "target_label",
            "gap_index", "measured_label", "label_error",
            "gap_width", "N_times_label_error",
        ],
    )
    write_csv(
        ROOT / "cell4_golden_control.csv",
        golden_records,
        [
            "label_name", "target_label", "golden_index_cutoff",
            "distance_to_best_index_le_30", "best_index_le_30",
            "tolerance", "first_index", "label", "distance",
        ],
    )
    write_csv(
        ROOT / "cell4_center_gap_margins.csv",
        [
            {
                "coupling_name": name,
                "minimum_gap_width":
                    record["minimum_target_gap_width"],
                "finite_N_Weyl_open_ball_radius_linf":
                    record["finite_N_Weyl_open_ball_radius_linf"],
                "half_margin_disorder_radius":
                    record["half_margin_disorder_radius"],
            }
            for name, record in margins.items()
        ],
        [
            "coupling_name",
            "minimum_gap_width",
            "finite_N_Weyl_open_ball_radius_linf",
            "half_margin_disorder_radius",
        ],
    )

    print(json.dumps({
        "C1_points": 64,
        "C2_points": 125,
        "all_C1_top30": all(
            record["gap_rank"] <= 30 for record in chamber_1
        ),
        "all_C2_top30": all(
            record["gap_rank"] <= 30 for record in chamber_2
        ),
        "minimum_low_order_golden_distance":
            golden_summary["minimum_distance_to_index_le_30"],
        "recommended_N":
            golden_summary["conservative_recommended_N"],
        "C1_Weyl_radius":
            margins["C1"]["finite_N_Weyl_open_ball_radius_linf"],
        "C2_Weyl_radius":
            margins["C2"]["finite_N_Weyl_open_ball_radius_linf"],
    }, indent=2))


if __name__ == "__main__":
    main()
