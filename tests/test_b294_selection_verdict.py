"""B294 lock -- THE SELECTION VERDICT (Phase VI synthesis). Consolidates the seam arc (B287-B293, B295): the answer to
B286's 'selective vs catalogue?' is SELECTIVE for the object's own structure (B287 re-sees A=LR), CATALOGUE for
Standard-Model-value selection (E6 lost, CP sign external, scale gapped, chiral absent, trajectory gated), and
AXIS-STRATIFIED (different axes pick different closings). Strengthens the firewall. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B294_selection_verdict" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b294", _PATH)
b294 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b294)


def test_all_eight_probe_verdicts_hold():
    results = b294.all_probes_pass()
    assert set(results) == {"B287", "B288", "B289", "B290", "B291", "B292", "B293", "B295"}
    assert all(results.values())                                 # the whole arc closes coherently


def test_selective_for_own_structure_catalogue_for_values():
    assert b294.SELECTIVE_FOR_OWN_STRUCTURE                      # B287: canonical closing re-sees A=LR
    assert b294.CATALOGUE_FOR_SM_VALUES                          # no closing forced to be 'our universe'


def test_axis_stratified_cross_axis_distinct():
    assert b294.SELECTION_IS_AXIS_STRATIFIED
    assert b294.sv.cross_axis_distinct()                         # dynamical/arithmetic/scale pick different closings


def test_strengthens_firewall():
    assert b294.STRENGTHENS_FIREWALL
    assert b294.DERIVES_SM_VALUES is False
    assert b294.verdict()
