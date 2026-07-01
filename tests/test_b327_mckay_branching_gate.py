"""B327 — the 27|_2T self-duality gate (Chat-1 handoff, verified + sharpened). sympy/pure-python only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..',
                                'frontier', 'B327_mckay_branching_gate'))
import sympy as sp
from mckay_branching_gate import principal_decomposition, characters, two_T_classes


def test_principal_27_is_V16_V8_V0():
    # resolves the cross-chat contradiction: Chat-2 (spins 8,4,0) right; Chat-1 (9V0+6V1) wrong.
    size, grades, spins = principal_decomposition()
    assert size == 27
    assert spins == {sp.Integer(8): 1, sp.Integer(4): 1, sp.Integer(0): 1}
    assert max(grades) == 16 and min(grades) == -16      # not +-2


def test_character_real_so_n1_equals_n2():
    _, _, spins = principal_decomposition()
    chi_g, chi_m1 = characters(spins)
    assert chi_g == 0            # real on order-3 elt => n1 = n2 (principal / any self-dual SU(2))
    assert chi_m1 == 27          # -I acts trivially (all integer spins)


def test_2T_order3_classes_share_su2_trace():
    # the two order-3 classes have the SAME SU(2) trace (-1); an SU(2)-restricted (self-dual)
    # character is equal on both => omega and omega^2 multiplicities equal => n1 = n2.
    classes = two_T_classes()
    order3 = [c for c in classes if c[2] == 3]
    assert len(order3) == 2
    assert {c[1] for c in order3} == {-1}                # identical trace -> real character forced
    order6 = [c for c in classes if c[2] == 6]
    assert len(order6) == 2 and {c[1] for c in order6} == {1}
