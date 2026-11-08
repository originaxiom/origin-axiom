# SPDX-License-Identifier: MIT
# Validator contract and negative-control self-test architecture adapted from:
#   QuantumBFS/sci-brain (https://github.com/QuantumBFS/sci-brain)
#   skills/autoresearch/references/validator-contract.md
#   skills/autoresearch/references/negative-controls.md
#
# MIT License
# Copyright (c) 2025 QuantumBFS/sci-brain contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

"""Sealed validator and negative-control self-test suite for Origin Axiom bridges.

Enforces the validator-contract and negative-controls discipline from
``QuantumBFS/sci-brain`` combined with the 6 mathematical-physics guardrails
and the 9 rules of ``REVIEW_RULES_FOR_AGY.md``.

Every negative control (``cheater_f1_affine_floor``, ``cheater_f2_f3_tensor_kron``,
``cheater_f4_diagonal_or_basis_dependent``, ``cheater_o1_o2_scope_overclaim``)
must be strictly rejected with a rich ``errors[]`` diagnostic naming ``where``,
``what``, and ``hint``. The live bridge modules must pass with zero errors.
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

import numpy as np

from origin_axiom.p000_pure_logic_bridge import (
    verify_wall2_d4_to_e8_glue_and_cover_family_functor,
)
from origin_axiom.weave_unification_bridge import (
    verify_coupled_2d_surface_and_3sheet_cover_bvp,
    verify_frontiers_6_to_9_shape_torsion_hyperbolic_core_b1856_b1857_and_charged_weak,
    verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex,
)


def validate_bridge_candidate(
    source_code: str,
    f69_report: dict[str, Any],
    wall3_report: dict[str, Any],
    bvp_report: dict[str, Any],
    p000_wall2_report: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate a candidate bridge implementation against AST and numerical gates.

    Returns a dictionary matching the ``sci-brain`` validator JSON report contract:
    ``{"status": "scored" | "rejected", "score": int | None, "per_instance": [...], "errors": [...]}``.
    """
    errors: list[dict[str, str]] = []
    per_instance: list[dict[str, Any]] = []

    # 1. AST Structural Gate: Ban tensor-factor multipliers and affine floor hacks
    tree = ast.parse(source_code)
    forbidden_patterns: list[str] = []
    for node in ast.walk(tree):
        # Detect np.kron(np.eye(3), ...) or np.kron(..., np.eye(3))
        if isinstance(node, ast.Call):
            func_str = ast.unparse(node.func) if hasattr(ast, "unparse") else ""
            if func_str.endswith("kron") and len(node.args) >= 2:
                arg0_str = ast.unparse(node.args[0])
                arg1_str = ast.unparse(node.args[1])
                if "eye(3)" in arg0_str or "eye(3)" in arg1_str or "identity(3)" in arg0_str:
                    forbidden_patterns.append(f"line {node.lineno}: {ast.unparse(node)}")
        # Detect artificial affine floor 0.25 * (1.0 - b1) or 0.25 * (1 - B1)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            expr_str = ast.unparse(node).replace(" ", "")
            if "0.25*(1" in expr_str and ("b1" in expr_str.lower()):
                forbidden_patterns.append(f"line {node.lineno}: {ast.unparse(node)}")

    if forbidden_patterns:
        errors.append(
            {
                "where": "AST_structural_gate (F1/F2/F3)",
                "what": f"Forbidden fabrication pattern(s) detected in AST: {forbidden_patterns}",
                "hint": "Remove np.kron(np.eye(3), ...) tensor multipliers and 0.25*(1-B1) affine floors; derive eigenvalues and kernel dimensions directly from operators.",
            }
        )
        per_instance.append(
            {"instance": "ast_no_fabrication_shortcuts", "result": "fail", "detail": str(forbidden_patterns)}
        )
    else:
        per_instance.append(
            {"instance": "ast_no_fabrication_shortcuts", "result": "pass", "detail": "Clean AST"}
        )

    # 2. Instance F9 (F1 gate): Mass gap must come from genuine half-integer holonomy shift, not floor
    f9 = f69_report.get("frontier9_charged_128_threshold_and_weak_universality", {})
    min_half = float(f9.get("zero_flux_charged_128_min_eigenvalue", 0.0))
    max_int = float(f9.get("even_120_max_min_circle_eigenvalue", 1.0))
    if not (abs(min_half - (np.pi**2)) < 1e-12 and abs(max_int) < 1e-12):
        errors.append(
            {
                "where": "F9_half_root_mass_gap (F1)",
                "what": (
                    f"Expected min_half={np.pi**2:.12f}, max_int=0.0; "
                    f"got min_half={min_half}, max_int={max_int}"
                ),
                "hint": "Evaluate -((d/dx + 2*pi*i*(w_zeta . alpha))^2) on S^1 with w_zeta = (3/2)Q.",
            }
        )
        per_instance.append({"instance": "F9_f1_holonomy_gap", "result": "fail", "detail": "Mismatch"})
    else:
        per_instance.append({"instance": "F9_f1_holonomy_gap", "result": "pass", "detail": "Exact pi^2 gap"})

    # 3. Instance BVP Task 1 & Wall 3 Control 5 (F2/F3 gate): 24 = 8 * 3 from Fock spinor + h15, plus negative control
    t1 = bvp_report.get("task1_3sheet_d4_cover_vs_single_sheet_wilson", {})
    c19 = wall3_report.get("controls_1_to_9_coupled_half_root_and_centralizer", {})
    pure_h4_pair = t1.get("pure_h4_chi00_record_counts_sum_24", [[], 0])
    record_dims = pure_h4_pair[0] if len(pure_h4_pair) == 2 else []
    pure_h4_sum = pure_h4_pair[1] if len(pure_h4_pair) == 2 else 0
    z2_cancel = t1.get("z2_sheet_sign_cannot_cancel_omega3_dim", -1)
    c5_h4_sum = c19.get("control5_pure_h4_chi00_kernel_dim_24", 0)
    if not (
        record_dims == [3] * 8
        and pure_h4_sum == 24
        and z2_cancel == 0
        and c5_h4_sum == 24
    ):
        errors.append(
            {
                "where": "BVP_Task1_Wall3_cohomology_lift (F2/F3)",
                "what": (
                    f"Expected pure_h4_chi00_record_counts_sum_24=[[3]*8, 24], z2_sheet_sign_cannot_cancel_omega3_dim=0, "
                    f"and control5_pure_h4_chi00_kernel_dim_24=24; got dims={record_dims}, z2_cancel={z2_cancel}, c5_sum={c5_h4_sum}"
                ),
                "hint": "Compute _total_cohomology(rec, correction=0, chi=(0,0)) from the 32-component Fock spinor complex and verify ker(+-omega_3 sigma_x - I_2) = {0}.",
            }
        )
        per_instance.append({"instance": "Wall1_f2_f3_cohomology", "result": "fail", "detail": "Invalid lift"})
    else:
        per_instance.append({"instance": "Wall1_f2_f3_cohomology", "result": "pass", "detail": "24 = 8*3 verified"})

    # 4. Instance BVP Task 3 & Wall 3 (F4 gate): Genuine 3x3 overlap matrix with 3 distinct eigenvalues and Haar invariance
    t3 = bvp_report.get("task3_coupled_4slot_koszul_weak_vertex_and_haar_scrambling", {})
    eigs = t3.get("g_4slot_3mode_eigenvalues", [])
    haar_err = float(t3.get("haar_50_trial_su2L_u3fam_max_err", 1.0))
    broken_drift = float(t3.get("non_unitary_negative_control_drift", 0.0))
    if not (
        len(eigs) == 3
        and min(float(x) for x in eigs) > 0.05
        and len({round(float(x), 6) for x in eigs}) == 3
        and haar_err < 1e-12
        and broken_drift > 0.05
    ):
        errors.append(
            {
                "where": "BVP_Task3_weak_vertex_and_scrambling (F4)",
                "what": (
                    f"Expected 3 distinct positive eigenvalues > 0.05, Haar error < 1e-12, and non-unitary drift > 0.05; "
                    f"got eigs={eigs}, haar_err={haar_err}, broken_drift={broken_drift}"
                ),
                "hint": "Integrate actual 32-component zero-mode wavefunctions Phi_a(t)^dagger w_0(t) Phi_b(t) on [0,4] and verify SU(2)_L x U(3)_fam Haar basis-scrambling invariance.",
            }
        )
        per_instance.append({"instance": "Wall3_f4_weak_vertex", "result": "fail", "detail": "Shortcut or basis leak"})
    else:
        per_instance.append({"instance": "Wall3_f4_weak_vertex", "result": "pass", "detail": "Genuine 1+2 overlap"})

    # 5. Instance O1 & O2 Scope and Premise Disclosure Gate
    bvp_scope = str(bvp_report.get("scope", ""))
    e8_supplied = bool(p000_wall2_report.get("e8_remains_supplied_premise_not_earned_from_single_register", False))
    if not (
        "FIXED_PERIOD_2D_ABELIAN_HODGE_RELAXATION" in bvp_scope
        and e8_supplied
    ):
        errors.append(
            {
                "where": "O1_O2_scope_and_premise_gate",
                "what": (
                    f"Scope or premise disclosure violation: bvp_scope={bvp_scope!r}, "
                    f"e8_remains_supplied_premise={e8_supplied}"
                ),
                "hint": "Retain FIXED_PERIOD_2D_ABELIAN_HODGE_RELAXATION in BVP scope and e8_remains_supplied_premise_not_earned_from_single_register=True.",
            }
        )
        per_instance.append({"instance": "O1_O2_scope_gate", "result": "fail", "detail": "Overclaim detected"})
    else:
        per_instance.append({"instance": "O1_O2_scope_gate", "result": "pass", "detail": "Honest scope retained"})

    status = "scored" if not errors else "rejected"
    score = len([p for p in per_instance if p["result"] == "pass"]) if status == "scored" else None
    return {
        "status": status,
        "score": score,
        "per_instance": per_instance,
        "errors": errors,
    }


def test_sealed_validator_rejects_all_negative_controls_and_scores_live_bridge() -> None:
    """Verify that all 4 negative controls are rejected and the live bridge passes."""
    bridge_path = (
        Path(__file__).resolve().parent.parent
        / "src"
        / "origin_axiom"
        / "weave_unification_bridge.py"
    )
    live_source = bridge_path.read_text(encoding="utf-8")
    f69_live = verify_frontiers_6_to_9_shape_torsion_hyperbolic_core_b1856_b1857_and_charged_weak()
    wall3_live = verify_wall3_coupled_half_root_kernel_pv_eigenmode_and_weak_vertex()
    bvp_live = verify_coupled_2d_surface_and_3sheet_cover_bvp()
    p000_w2_live = verify_wall2_d4_to_e8_glue_and_cover_family_functor()

    # 1. Negative Control 1: F1 affine floor cheater
    cheater_f1_src = live_source + "\n# cheater hack\ngap = 0.25 * (1.0 - b1)\n"
    cheater_f1_f69 = dict(
        f69_live,
        frontier9_charged_128_threshold_and_weak_universality=dict(
            f69_live["frontier9_charged_128_threshold_and_weak_universality"],
            zero_flux_charged_128_min_eigenvalue=0.25,
        ),
    )
    rep_f1 = validate_bridge_candidate(
        cheater_f1_src, cheater_f1_f69, wall3_live, bvp_live, p000_w2_live
    )
    assert rep_f1["status"] == "rejected"
    assert len(rep_f1["errors"]) >= 2
    assert any("F1" in e["where"] for e in rep_f1["errors"])

    # 2. Negative Control 2: F2/F3 np.kron(np.eye(3), ...) cheater
    cheater_f2_src = live_source + "\n# cheater hack\nlift_op = np.kron(np.eye(3), base_op)\n"
    cheater_f2_bvp = dict(
        bvp_live,
        task1_3sheet_d4_cover_vs_single_sheet_wilson=dict(
            bvp_live["task1_3sheet_d4_cover_vs_single_sheet_wilson"],
            z2_sheet_sign_cannot_cancel_omega3_dim=3,
        ),
    )
    rep_f2 = validate_bridge_candidate(
        cheater_f2_src, f69_live, wall3_live, cheater_f2_bvp, p000_w2_live
    )
    assert rep_f2["status"] == "rejected"
    assert any("AST_structural_gate" in e["where"] for e in rep_f2["errors"])
    assert any("F2/F3" in e["where"] for e in rep_f2["errors"])

    # 3. Negative Control 3: F4 diagonal shortcut / basis-dependent weak vertex cheater
    cheater_f4_bvp = dict(
        bvp_live,
        task3_coupled_4slot_koszul_weak_vertex_and_haar_scrambling=dict(
            bvp_live["task3_coupled_4slot_koszul_weak_vertex_and_haar_scrambling"],
            g_4slot_3mode_eigenvalues=[0.5, 0.5, 0.5],
            haar_50_trial_su2L_u3fam_max_err=1e-2,
        ),
    )
    rep_f4 = validate_bridge_candidate(
        live_source, f69_live, wall3_live, cheater_f4_bvp, p000_w2_live
    )
    assert rep_f4["status"] == "rejected"
    assert any("F4" in e["where"] for e in rep_f4["errors"])

    # 4. Negative Control 4: O1/O2 overclaim cheater
    cheater_o1_bvp = dict(bvp_live, scope="GLOBAL_6D_SM3_COMPLETION")
    cheater_o2_p000 = dict(
        p000_w2_live, e8_remains_supplied_premise_not_earned_from_single_register=False
    )
    rep_o1_o2 = validate_bridge_candidate(
        live_source, f69_live, wall3_live, cheater_o1_bvp, cheater_o2_p000
    )
    assert rep_o1_o2["status"] == "rejected"
    assert any("O1_O2_scope_and_premise_gate" in e["where"] for e in rep_o1_o2["errors"])

    # 5. Live Bridge Positive Score
    rep_live = validate_bridge_candidate(
        live_source, f69_live, wall3_live, bvp_live, p000_w2_live
    )
    assert rep_live["status"] == "scored"
    assert rep_live["errors"] == []
    assert rep_live["score"] == 5
