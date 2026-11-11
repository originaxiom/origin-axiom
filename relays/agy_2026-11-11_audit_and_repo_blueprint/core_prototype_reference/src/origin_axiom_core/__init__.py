"""Origin Axiom Core — Distilled Zero-Trust Mathematical Verification Package.

Contains strictly proven, data-free (`0 of 19`) mathematical theorems and the
executable Guardrail 1-6 static/dynamic verification compiler (`guardrail_dsl`).
"""

from .analytic_theta import (
    analytic_jtheta,
    dedekind_eta_holomorphic,
    theta_triplet_weight_minus_half,
)
from .guardrail_dsl import (
    ComplexChainError,
    EquivariantCochainComplex,
    FramedMatrix,
    GatedRGEIntegrator,
    Guardrail1PostInspectionError,
    Guardrail1UnpricedScanError,
    Guardrail2LiteralClaimError,
    Guardrail3BasisDependenceError,
    Guardrail3IllegalLeftRightOverlapError,
    Guardrail4BenchmarkGateError,
    Guardrail5UnpricedScaleError,
    Guardrail6ProducerEchoError,
    GuardrailCompilerError,
    IntertwinerError,
    IntertwinerSpec,
    LedgerContext,
    TrackedValue,
    haar_random_unitary,
    observable,
    producer,
    referee,
    stabilization_potential,
    theorem,
    zero_bit_prediction,
)
from .maass_p776 import (
    twin_odd_maass_golden_and_kramers,
    two_tick_bijection_census,
)
from .subweave_r10 import (
    act_marked_line,
    build_marked_lines,
    mayer_selberg_subweave_spectrum,
    ray_singer_x1_sheet_potential_mp,
    schreier_closure_pm_gamma1_5,
)
from .tick_and_settling import (
    adjoint_settling_spectrum,
    apply_fricke_word,
    nonorientable_pin_pullback_census,
    projective_modular_tick_orders,
    stern_brocot_axis_correlation,
    weave_6d_commutant_fusion,
)

__all__ = [
    "analytic_jtheta",
    "dedekind_eta_holomorphic",
    "theta_triplet_weight_minus_half",
    "ComplexChainError",
    "EquivariantCochainComplex",
    "FramedMatrix",
    "GatedRGEIntegrator",
    "Guardrail1PostInspectionError",
    "Guardrail1UnpricedScanError",
    "Guardrail2LiteralClaimError",
    "Guardrail3BasisDependenceError",
    "Guardrail3IllegalLeftRightOverlapError",
    "Guardrail4BenchmarkGateError",
    "Guardrail5UnpricedScaleError",
    "Guardrail6ProducerEchoError",
    "GuardrailCompilerError",
    "IntertwinerError",
    "IntertwinerSpec",
    "LedgerContext",
    "TrackedValue",
    "haar_random_unitary",
    "observable",
    "producer",
    "referee",
    "stabilization_potential",
    "theorem",
    "zero_bit_prediction",
    "act_marked_line",
    "build_marked_lines",
    "mayer_selberg_subweave_spectrum",
    "ray_singer_x1_sheet_potential_mp",
    "schreier_closure_pm_gamma1_5",
    "adjoint_settling_spectrum",
    "apply_fricke_word",
    "nonorientable_pin_pullback_census",
    "projective_modular_tick_orders",
    "stern_brocot_axis_correlation",
    "twin_odd_maass_golden_and_kramers",
    "two_tick_bijection_census",
    "weave_6d_commutant_fusion",
]
