"""B253 locks -- adjudication of the Chat-2 chirality reduction. Part A: E6 complex-rep-capable, E7/E8 not, axis
coincides with the B248 transition. Part B: CS=0 discriminator inconclusive; not object-decidable. FIREWALLED;
nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B253_chirality_capability" / "chirality_capability.py"
_spec = importlib.util.spec_from_file_location("b253", _PATH)
b253 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b253)


def test_part_a_complex_rep_capability():
    # E6 has a complex rep; E7, E8 do not (Sage-verified backbone)
    assert b253.COMPLEX_REP_CAPABLE == {"E6": True, "E7": False, "E8": False}
    assert b253.OUT_GROUP_ORDER == {"E6": 2, "E7": 1, "E8": 1}
    assert b253.MIN_REP["E8"] == (248, "real")          # E8's min rep is the real adjoint


def test_chirality_axis_matches_transition_axis():
    # B248: hyperbolic E6 (capable) -> spherical E8 (not)
    assert b253.chirality_axis_matches_transition_axis()


def test_cs_discriminator_inconclusive_at_zero():
    # tau: CS -> -CS; CS(4_1)=0 -> tau fixed -> gaugeable, but NOT decisive (both branches open)
    assert b253.cs_under_tau(0) == 0
    assert b253.tau_is_gaugeable()
    assert not b253.cs_discriminator_is_decisive()


def test_part_b_not_object_decidable():
    # 3d-not-4d, McKay-label-not-gauge-group, gauging/SSB external -> Part B is firewalled, not decidable
    assert not b253.part_b_decidable_from_object()
