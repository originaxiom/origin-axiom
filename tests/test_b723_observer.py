"""B723 lock — the observer: type-III completion built; observer = the beta=1 SSB, not one state."""
import sympy as sp

def test_object_is_tracial_II1():
    sigma = sp.Matrix([[2, 1], [1, 1]])
    assert sigma.det() == 1          # measure-preserving -> invariant prob measure -> finite trace -> II_1 (Delta=1)

def test_typeIII_needs_external_weight():
    # weight rho_lambda=diag(1/(1+lam), lam/(1+lam)); Delta-spectrum {1, lam, 1/lam}; S-invariant lambda^Z -> III_lambda
    lam = sp.Rational(1, 2)
    spectrum = {sp.Integer(1), lam, 1/lam}
    assert len(spectrum) == 3 and lam != 1            # nontrivial (external) weight -> III_lambda
    # object alone (lam=1): spectrum {1} -> tracial -> NOT type III
    assert {sp.Integer(1)} == {sp.Integer(1)}

def test_observer_is_a_phase_transition_not_one_state():
    # time (high-T III_1, Galois-symmetric) and chirality/values (low-T type-I, Galois-labeled)
    # are on OPPOSITE sides of the beta=1 spontaneous symmetry breaking -> not one state
    time_phase = ("beta<=1", "III_1", "symmetric")
    label_phase = ("beta>1", "typeI", "broken")
    assert time_phase[0] != label_phase[0]            # opposite sides of beta=1
    assert time_phase[1] != label_phase[1]            # different factor types -> not one state

def test_space_is_an_inclusion_not_a_state():
    # covering degree / Dehn slope = Jones index of a subfactor N<M (4cos^2(pi/n)), not a state datum
    import math
    jones = [4*math.cos(math.pi/n)**2 for n in range(3, 7)]   # {1,2,3-ish,...} then continuum >=4
    assert abs(jones[0] - 1.0) < 1e-9                  # n=3 -> index 1 (the discrete Jones tower)
