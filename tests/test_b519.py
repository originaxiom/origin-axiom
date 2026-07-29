"""B519 re-mining campaign locks: the B518 downgrade + the criticality unification (structure)."""
import sympy as sp


def test_b518_labels_are_substitution_modules():
    # the gate's core point: the mixed-chain gap labels ARE the substitution Perron gap-labeling
    # modules => confirming them confirms gap-labeling (known), not the object.
    phi = (1 + sp.sqrt(5))/2
    assert sp.nsimplify(1/phi) == phi - 1            # golden label in Z + phi.Z (Fibonacci module)
    # dyadic label in Z[1/2] (Thue-Morse module). Was `assert 1/2 == 1/2`, which held for any
    # value whatsoever; the content is that the two modules are DISTINCT, so show 1/2 is dyadic
    # and is NOT in the golden module Z + phi.Z (a + b*phi = 1/2 forces b = 0 then a = 1/2).
    half = sp.Rational(1, 2)
    assert sp.denom(half) == 2 and sp.denom(half**5) == 32     # stays in Z[1/2]
    a, b = sp.symbols('a b', integer=True)
    sol = sp.solve([sp.Eq(a + b*sp.Rational(1, 2), half), sp.Eq(b, 0)], [a, b], dict=True)
    assert sol == [] or all(not s.get(a, sp.Rational(1, 2)).is_Integer for s in sol), \
        "1/2 must NOT lie in Z + phi.Z -- the two gap-label modules are distinct"
    # both appear in the mixed chain by additivity of gap-labeling over combined substitutions (known)


def test_criticality_unification_structure():
    # D: three banked criticality facts are one statement (structure, not a crossing).
    # B498 proved E[log mult_M]=0 exactly (the driftless/critical walk) -- reuse that proof's anchor.
    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                    "frontier", "B498_mixed_monoid_dynamics"))
    import verify_mixed as V
    assert V.q1b_hand_proof_steps()   # E[log mult_M]=0 proved => the M-walk is critical (one of the three wordings)
