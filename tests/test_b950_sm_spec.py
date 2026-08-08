"""B950 locks — the SM specification ledger and the dimension correction."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "SM_SPECIFICATION_LEDGER.md"
CELL = ROOT / "frontier" / "B950_sm_spec_ledger"


def _n(p):
    return " ".join(p.read_text(encoding="utf-8").split())


def test_the_ledger_states_the_specification_not_just_the_method():
    t = _n(LEDGER)
    for frag in ("su(3)_C ⊕ su(2)_L ⊕ u(1)_Y", "8 + 3 + 1 = 12", "ℤ₆",
                 "15 Weyl fermions per generation", "19"):
        assert frag in t, f"missing specification element: {frag}"


def test_the_hypercharges_are_flagged_as_the_only_forced_value_structure():
    t = _n(LEDGER)
    assert "anomaly cancellation" in t
    assert "only computed value-level structure" in t


def test_the_dimension_correction_is_recorded():
    """14 is not 12; the mathematics stands, the sentence did not."""
    t = _n(CELL / "FINDINGS.md")
    assert "dimension 14" in t and "dimension 12" in t
    assert "overstates by two abelian factors" in t
    assert "is not a refutation" in t.lower()
    assert "two steps from the SM, not zero" in t


def test_forced_must_be_called_reproduced_not_predicted():
    t = _n(LEDGER)
    assert '"reproduced"' in t and '"predicted"' in t
    # and sin^2 theta_W is placed in the forced column, not the achievement column
    assert "3/8" in t


def test_L132_is_registered_and_not_run():
    t = _n(CELL / "FINDINGS.md")
    assert "Registered as L132" in t and "Not run here" in t
