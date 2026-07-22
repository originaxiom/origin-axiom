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


def test_addendum2_twist_invariance_of_the_mixing_entry():
    # the sign-flip negates the block: eigenvectors coincide, eigenvalues negate
    # (72deg <-> 108deg supplementary); p = (1 +- Im/sin)/2 is invariant because
    # both Im(B00) and sin(theta) flip sign together under negation.
    th_tw, th_un = 2 * sp.pi / 5, 3 * sp.pi / 5
    B00_tw = 1 / (2 * phi) + sp.I * sp.sin(th_tw) / sp.sqrt(5)
    B00_un = -B00_tw
    p_tw = sp.simplify((1 + sp.im(B00_tw) / sp.sin(th_tw)) / 2)
    p_un = sp.simplify((1 + sp.im(B00_un) / sp.sin(th_un) * (-1)) / 2)
    # untwisted eigenphase 108deg: lambda = e^{+-i*108}; B00_un = e^{i108}p + e^{-i108}(1-p)
    p_un_direct = sp.simplify((1 + sp.im(B00_un) / sp.sin(th_un)) / 2)
    assert sp.simplify(sp.re(B00_un) - sp.cos(th_un)) == 0          # -1/(2phi) = cos108
    # negation keeps the eigenLINES but swaps the phase labels: p_un = 1 - p_tw,
    # so the overlap SET per row {p, 1-p} = {phi/sqrt5, 1/(phi*sqrt5)} is invariant
    assert sp.simplify(p_un_direct - (1 - p_tw)) == 0
    assert sp.simplify((1 - p_tw) - 1 / (phi * sp.sqrt(5))) == 0
    assert sp.simplify(p_tw - phi / sp.sqrt(5)) == 0
