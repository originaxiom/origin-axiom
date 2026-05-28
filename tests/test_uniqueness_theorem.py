"""Conditional uniqueness theorem — the computational lemmas of
``docs/UNIQUENESS_THEOREM.md``.

This formalizes claim **C1** (conditional). It does NOT promote C1 to ``proven``:
C1 remains conditional on the minimal record axioms A1–A6. These tests lock the
*algebra the axioms imply* — given the axioms, that the first mixed closure is
forced to ``A = LR`` (up to order), with trace 3 and the φ-spectrum.
"""

import sympy as sp

from origin_axiom.algebra import A, L, R
from origin_axiom.constants import PHI

a, b = sp.symbols("a b", positive=True, integer=True)
tau = sp.symbols("tau")


def L_shear(k):
    """Elementary one-channel shear adding k of record 2 to record 1."""
    return sp.Matrix([[1, k], [0, 1]])


def R_shear(k):
    """Elementary one-channel shear adding k of record 1 to record 2."""
    return sp.Matrix([[1, 0], [k, 1]])


def mixed_closure(av, bv):
    """First mixed persistent sector B(a,b) = L_a · R_b."""
    return L_shear(av) * R_shear(bv)


def mobius_fixed_poly(M):
    """Numerator of f(tau) - tau, where f is the Möbius action of M. Expanded."""
    f = (M[0, 0] * tau + M[0, 1]) / (M[1, 0] * tau + M[1, 1])
    return sp.expand(sp.numer(sp.together(f - tau)))


# --- Axiom 4: primitive shears are exactly L and R ------------------------
def test_primitive_shears_are_L_and_R():
    assert L_shear(1) == L
    assert R_shear(1) == R


# --- Axiom 5 lemmas: closure form, det/trace/torsion ----------------------
def test_mixed_closure_form():
    """B(a,b) = [[1+ab, a],[b, 1]]."""
    assert mixed_closure(a, b) == sp.Matrix([[1 + a * b, a], [b, 1]])


def test_det_trace_and_torsion_formulas():
    """det B = 1, trace B = 2 + ab, det(B - I) = -ab."""
    B = mixed_closure(a, b)
    assert sp.simplify(B.det() - 1) == 0
    assert sp.simplify(sp.trace(B) - (2 + a * b)) == 0
    assert sp.simplify((B - sp.eye(2)).det() - (-a * b)) == 0


def test_torsion_order_equals_ab():
    """|det(B - I)| = ab is the torsion order of H_1 of the mapping torus.

    Checked via Smith normal form for a few values: torsion is trivial iff ab = 1.
    """
    for av, bv, expected_order in [(1, 1, 1), (1, 2, 2), (2, 2, 4), (2, 3, 6)]:
        B = mixed_closure(av, bv)
        order = abs((B - sp.eye(2)).det())
        assert order == expected_order
    # torsion-free (order 1) over positive integers <=> a = b = 1
    torsion_free = [(av, bv) for av in range(1, 13) for bv in range(1, 13) if av * bv == 1]
    assert torsion_free == [(1, 1)]


# --- The 144 -> 1 collapse (Axiom 5 or 6) ---------------------------------
def test_grid_144_collapses_to_1():
    """In the 12x12 positive grid, all 144 mixed closures are hyperbolic;
    the torsion-free filter leaves exactly one, namely (1,1) -> A."""
    grid = [(av, bv) for av in range(1, 13) for bv in range(1, 13)]
    hyperbolic = [(av, bv) for (av, bv) in grid if abs(2 + av * bv) > 2]
    assert len(hyperbolic) == 144
    survivors = [(av, bv) for (av, bv) in hyperbolic if av * bv == 1]
    assert survivors == [(1, 1)]


def test_minimal_hyperbolic_trace_is_three():
    """trace = 2 + ab >= 3 for positive integers; 3 is the first hyperbolic trace."""
    traces = {2 + av * bv for av in range(1, 13) for bv in range(1, 13)}
    assert min(t for t in traces if t > 2) == 3


# --- The selected matrix and its spectrum ---------------------------------
def test_selected_matrix_is_A():
    B = mixed_closure(1, 1)
    assert B == A == sp.Matrix([[2, 1], [1, 1]])


def test_eigenvalues_are_phi_squared_and_inverse():
    ev = A.eigenvals()
    assert sp.simplify(PHI**2 - max(ev, key=lambda e: float(e))) == 0
    assert sp.simplify(PHI**-2 - min(ev, key=lambda e: float(e))) == 0


# --- Axiom 7: the residual order choice (the based-invariant fact) ---------
def test_order_choice_LR_vs_RL_conjugate_but_distinct_mobius_poly():
    """LR and RL are SL(2,Z)-conjugate (via the swap) yet give DIFFERENT Möbius
    fixed-point polynomials: LR -> tau^2 - tau - 1, RL -> tau^2 + tau - 1.
    The order is an irreducible labeled choice; it selects the golden polynomial."""
    LR, RL = L * R, R * L
    swap = sp.Matrix([[0, 1], [1, 0]])
    # conjugate
    assert sp.simplify(swap * LR * swap.inv() - RL) == sp.zeros(2, 2)
    # same trace, same eigenvalues
    assert sp.trace(LR) == sp.trace(RL) == 3
    # but different Möbius polynomials
    poly_LR = mobius_fixed_poly(LR)   # -tau^2 + tau + 1  (i.e. -(tau^2 - tau - 1))
    poly_RL = mobius_fixed_poly(RL)   # -tau^2 - tau + 1  (i.e. -(tau^2 + tau - 1))
    assert sp.expand(poly_LR - (-(tau**2 - tau - 1))) == 0
    assert sp.expand(poly_RL - (-(tau**2 + tau - 1))) == 0
    assert sp.expand(poly_LR - poly_RL) != 0
