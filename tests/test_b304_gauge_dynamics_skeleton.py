"""B304 lock -- the gauge-dynamics skeleton + the two peer handoffs assessed. VERIFIED (generic-GUT): sin^2(theta_W)
=3/8, the beta AF unification pattern. VERIFIED (object-relevant): 24=|2T| E6 principal-grading weights with
j==0 mod 3. REFUTED: Chat-1's "E6->SU(3) at the saddle" (height-6 roots orthogonal = SU(2)^3, A2 impossible).
FIREWALLED [LEAP]: the filling = N=2->N=1 datum (DGG). Nothing to CLAIMS.md.
(E6-root facts Sage-verified; recorded as constants.)"""
import importlib.util
import pathlib
from fractions import Fraction as F

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B304_gauge_dynamics_skeleton" / "gauge_dynamics_skeleton.py"
_spec = importlib.util.spec_from_file_location("b304", _PATH)
b304 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b304)


def test_sin2_theta_w_is_three_eighths():
    assert b304.sin2_theta_w() == F(3, 8)                 # Georgi-Glashow; generation-independent (bypasses B298)


def test_beta_af_unification_pattern():
    assert b304.beta_signs_unify()                        # SU(3),SU(2) AF; U(1) grows -- the unification direction


def test_principal_grading_24_equals_2T():
    assert b304.principal_grading_mod3_count() == 24      # = |2T|, object-relevant (B266)


def test_saddle_su3_refuted_and_firewall():
    assert b304.E6_HEIGHT6_POSITIVE_ROOTS == 3
    assert b304.E6_HEIGHT6_ROOTS_MUTUALLY_ORTHOGONAL     # (A1)^3 = SU(2)^3, not A2=SU(3)
    assert b304.SADDLE_SU3_CLAIM_REFUTED
    assert b304.GAUGE_DYNAMICS_IS_GENERIC_GUT            # forced via E6, not object-specific
    assert b304.DERIVES_SM_VALUES is False
    assert b304.verdict()
