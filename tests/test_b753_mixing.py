"""Locks for B753 -- the mixing-structure adjudication (exact identities)."""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
TH = 2 * sp.pi / 5                                     # 72 degrees
B00 = 1 / (2 * phi) + sp.I * sp.sin(TH) / sp.sqrt(5)   # the banked B593 element


def test_real_parts_coincide_eigenphase_equals_element():
    assert sp.simplify(sp.re(B00) - sp.cos(TH)) == 0
    assert sp.simplify(sp.cos(TH) - 1 / (2 * phi)) == 0


def test_kind_correct_mixing_entry_is_the_born_weight():
    p = sp.simplify((1 + sp.im(B00) / sp.sin(TH)) / 2)
    assert sp.simplify(p - phi / sp.sqrt(5)) == 0
    assert sp.simplify((1 - p) - 1 / (phi * sp.sqrt(5))) == 0
    assert sp.simplify(sp.Abs(B00) ** 2 - (1 - p)) == 0     # |B00|^2 == mixing entry


def test_unistochastic():
    p = phi / sp.sqrt(5)
    assert sp.simplify(p + (1 - p) - 1) == 0
    assert float(p) > 0 and float(1 - p) > 0


def test_chat1_eigenphase_claim_false():
    # trace = 2*Re(B00) = +1/phi, NOT -1/phi = 2*cos(108deg)
    assert sp.simplify(2 * sp.re(B00) - 1 / phi) == 0
    assert sp.simplify(2 * sp.cos(3 * sp.pi / 5) + 1 / phi) == 0   # cos108 = -1/(2phi)
