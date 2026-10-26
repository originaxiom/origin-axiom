"""Lock for B1760 — Class-Choosing & Joint-Law Null Calibration (P-381, P-384) and P210 / Oct 26 Reductions Audit (P-386)."""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1760_class_choosing_null_and_p210_review"
VER = ARC / "verification"


def test_b1760_class_choosing_and_cross_census():
    data = json.loads((VER / "class_choosing_and_p210_audit.json").read_text())
    assert data["arc"] == "B1760"
    assert data["num_random_targets"] == 80000

    b49 = data["b1749_class_choosing_nulls"]
    assert b49["prime_divisibility"]["num_classes"] == 5
    assert b49["exact_order"]["num_classes"] == 11
    assert b49["slope_alpha"]["num_classes"] == 24
    assert abs(b49["prime_divisibility"]["inflation_factor_at_named"] - 4.25) < 1e-12
    assert abs(b49["exact_order"]["inflation_factor_at_named"] - 11.0) < 1e-12
    assert abs(b49["slope_alpha"]["inflation_factor_at_named"] - 24.0) < 1e-12

    b55 = data["b1755_class_choosing_nulls"]
    assert b55["prime_divisibility"]["num_classes"] == 5
    assert b55["exact_order"]["num_classes"] == 4
    assert b55["slope_alpha"]["num_classes"] == 28
    # Every class-choosing null on B1755 exceeds 0.001 (0.1%)
    assert b55["prime_divisibility"]["class_choosing_min_p_at_named"] > 0.003
    assert b55["prime_divisibility"]["class_choosing_min_p_at_best"] > 0.001
    assert b55["exact_order"]["class_choosing_min_p_at_named"] > 0.001
    assert b55["slope_alpha"]["class_choosing_min_p_at_named"] > 0.004

    cc = data["cross_census_and_two_stage"]
    assert cc["pearson_corr_b1749_p5_vs_b1755_15plus20"] > 0.70
    assert cc["pearson_corr_b1749_alpha25_vs_b1755_alpha25"] > 0.89
    assert cc["conditional_enhancement_factor_at_16p75"] > 30.0
    ts = cc["two_stage_train_b1749_to_test_b1755_prime_menu"]
    assert ts["two_stage_min_p_null"] > 0.0015
    assert ts["two_stage_min_p_hits"] == 125


def test_b1760_p386_p210_and_oct26_audit():
    data = json.loads((VER / "class_choosing_and_p210_audit.json").read_text())
    p386 = data["p386_p210_and_oct26_audit"]
    assert p386["sealed_commit"] == "39ce620a82e5373d5f07eee91a6a7cbfd4cdd4f7"
    assert p386["artifacts_verified"] == 39
    assert p386["source_manifest_entries_verified"] == 14
    assert len(p386["symmetric_response_test_methods"]) == 10
    assert p386["prospective_non_execution_preserved"] is True
    assert p386["weyl_norm_derivative_identity_verified"] is True
    assert p386["unitary_slot_chart_grading_transport_verified"] is True
    assert p386["schur_mode_elimination_induced_metric_verified"] is True
    assert p386["end_amplitude_sewing_discriminator_verified"] is True
    assert p386["quaternion_orbifold_local_bps_core_and_custody_verified"] is True
    assert len(p386["reviewed_note_sha256"]) == 8


def test_b1760_clean_run_log():
    txt = (VER / "class_choosing_and_p210_audit_run.txt").read_text()
    assert "Traceback" not in txt
    assert "/Users/" not in txt
    assert "Wrote verification/class_choosing_and_p210_audit.json successfully." in txt
