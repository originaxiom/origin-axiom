"""Locks for Cell 4 spectral robustness."""

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent


def load_certificate():
    return json.loads(
        (ROOT / "CELL4_SPECTRAL_ROBUSTNESS_CERTIFICATE.json")
        .read_text(encoding="utf-8")
    )


def test_exact_module():
    certificate = load_certificate()
    exact = certificate["exact_frequency_module"]
    assert exact["basis_change_determinant"] == 1
    assert exact["frequency_module"] == "Z[f_a,f_b,f_A,f_B] = Z[tau]"
    assert exact["all_five_target_labels_have_degree"] == 4


def test_both_sampled_boxes_are_top_30():
    certificate = load_certificate()
    chambers = certificate["sampled_coupling_chambers"]
    for name in ("C1_BOX", "C2_BOX"):
        summary = chambers[name]["summary"]
        assert all(
            record["top_30_fraction"] == 1.0
            for record in summary.values()
        )
        assert all(
            record["minimum_gap_width"] > 0
            for record in summary.values()
        )


def test_finite_size_targets_stay_open():
    with (ROOT / "cell4_finite_size.csv").open(
        encoding="utf-8"
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 40
    assert all(float(row["gap_width"]) > 1e-3 for row in rows)
    assert max(float(row["N_times_label_error"]) for row in rows) < 0.14


def test_golden_control_is_scoped():
    certificate = load_certificate()
    correction = certificate["golden_control_correction"]
    assert correction["full_golden_module_mod_1_is_dense"]
    assert not correction["single_label_absolute_field_separation"]
    assert correction["golden_index_cutoff"] == 30
    assert correction["counting_only_minimum_N"] > 2000
    assert correction["conservative_recommended_N"] == 5000


def test_cell_status_keeps_gap_opening_open():
    certificate = load_certificate()
    status = certificate["gap_opening_status"]
    assert status["infinite_volume_open_chamber"] == "NOT_PROVED"
    assert status["all_module_labels_open"].startswith("OPEN")
    assert certificate["classification"]["cell_status"] == (
        "EXPERIMENT_READY_WITH_INFINITE_VOLUME_GAP_OPENING_OPEN"
    )
