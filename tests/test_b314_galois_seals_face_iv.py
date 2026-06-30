"""B314 lock -- Problem A (firewall theorem), the QUANTUM case sealed. The figure-eight colored Jones at the k=3 root
J_N(4_1; zeta_5) = {1, 1-sqrt5, 1-sqrt5, 1} (N=1..4), all in Q(sqrt5); J_2 at the two root-orbits = {1-sqrt5, 1+sqrt5}
= a golden Q(sqrt5) Galois orbit; SU(2)_3 quantum dims {1, phi, phi, 1} in Q(sqrt5). So the Face IV/WRT discrete values
are GALOIS-SYMMETRIZED (golden Z/2, sqrt5->-sqrt5) -> no discretely-multivalued-and-unsymmetric invariant -> no forced
choice. With B130 (trace ring continuous), both main invariant classes sealed. The value-free monad IS a Galois theorem:
two ends, two Z/2 (golden Q(sqrt5) Face IV + Eisenstein Q(sqrt-3) classical, B285). Refines Chat-1 (Q(sqrt5) not the full
Q(zeta_5)). Residual = the all-invariants S032-A. Nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B314_galois_seals_face_iv" / "galois_seals_face_iv.py"
_spec = importlib.util.spec_from_file_location("b314", _PATH)
b314 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b314)
_PHI = sp.Rational(1, 2) + sp.sqrt(5) / 2


def test_colored_jones_sanity_and_golden_field():
    assert b314.j2_is_figure_eight_jones()                                 # J_2 = the fig-8 Jones polynomial
    assert [b314.jones_at_zeta5(N) for N in (1, 2, 3, 4)] == [sp.Integer(1), 1 - sp.sqrt(5), 1 - sp.sqrt(5), sp.Integer(1)]


def test_discrete_values_are_a_golden_galois_orbit():
    assert set(b314.golden_galois_orbit_of_j2()) == {1 - sp.sqrt(5), 1 + sp.sqrt(5)}     # sqrt5 -> -sqrt5
    assert b314.su2_3_quantum_dims() == [sp.Integer(1), _PHI, _PHI, sp.Integer(1)]       # {1, phi, phi, 1} in Q(sqrt5)
    assert b314.DISCRETE_VALUES_ARE_GALOIS_ORBIT and b314.FIELD_IS_GOLDEN_NOT_FULL_CYCLOTOMIC


def test_value_free_monad_is_a_galois_theorem():
    assert b314.TWO_ENDS_TWO_GALOIS_GROUPS                                  # golden Q(sqrt5) + Eisenstein Q(sqrt-3) B285
    assert b314.VALUE_FREE_MONAD_IS_A_GALOIS_THEOREM


def test_problem_a_quantum_case_sealed():
    assert b314.PROBLEM_A_QUANTUM_CASE_SEALED                               # + B130 (trace ring) = both classes
    assert b314.RESIDUAL_IS_THE_ALL_INVARIANTS_THEOREM                      # S032-A fully general remains
    assert b314.DERIVES_SM_VALUES is False
    assert b314.verdict()
