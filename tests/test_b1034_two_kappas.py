"""B1034 locks — kappa names two quantities, one of them inside the certified core.

These re-run the comparison (WORKING_RULES rule 7) rather than asserting a transcript, so a
rename under L159 moves the lock rather than leaving it stale.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1034", _ROOT / "frontier" / "B1034_two_kappas" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


def test_every_check_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_core_exports_the_moebius_kappa_not_the_bridge_one():
    """`origin_axiom.mobius.KAPPA` is 2*log(phi^2)/sqrt(5) ~ 0.8608 — the flow coupling."""
    assert abs(float(v.KAPPA) - 0.8608178819280081) < 1e-12
    assert not v.KAPPA.free_symbols


def test_the_two_kappas_differ_in_type_not_only_in_value():
    """THE DISCRIMINATOR, and it is why this is not a quibble: the core's kappa is a CONSTANT and
    can never equal 2; the bridge kappa is a COORDINATE whose value 2 is the founding sentence
    ('the cancellation completes = nothing'). A constant has no locus."""
    assert v.R["checks"]["core_kappa_can_never_equal_2"]["pass"]
    assert v.R["checks"]["the_two_kappas_differ_in_TYPE_not_only_value"]["pass"]
    assert v.R["checks"]["the_bridge_kappa_carries_the_founding_sentence"]["pass"]


def test_the_criterion_could_have_come_out_the_other_way():
    """MB12. Had the core's KAPPA been symbolic in the character-variety coordinates, the type
    test would not have fired — so 'they differ in type' is a real condition, not a tautology."""
    assert v.R["checks"]["the_criterion_is_failable__a_symbolic_kappa_would_not_trip_it"]["pass"]


def test_the_collision_spans_the_proven_register_and_the_law_register():
    """Why this E1 is worse than the pass's other three: CLAIMS.md P15/P16 against LAW_MAP."""
    assert v.R["checks"]["CLAIMS_P15_P16_use_kappa_for_the_moebius_coupling"]["pass"]
    assert v.R["checks"]["the_bridge_kappa_is_a_commutator_trace_on_a_curated_surface"]["pass"]


def test_both_surfaces_now_declare_the_other():
    """The repair actually made. Renaming is L159's decision, not a drafting seat's."""
    assert v.R["checks"]["the_core_module_now_declares_the_collision"]["pass"]
    assert v.R["checks"]["CLAIMS_now_carries_the_disambiguation"]["pass"]
    assert v.R["checks"]["a_lead_is_registered_rather_than_a_rename_performed"]["pass"]


def test_the_mathematics_of_both_is_untouched():
    """Nothing here disturbs P15/P16 or the bridge-kappa family; only the symbol was undeclared."""
    import sympy as sp
    tau = sp.symbols("tau")
    assert sp.simplify(v.vector_field(tau) + v.KAPPA * (tau**2 - tau - 1)) == 0
    assert sp.simplify(sp.diff(v.potential(tau), tau) - v.KAPPA * (tau**2 - tau - 1)) == 0
