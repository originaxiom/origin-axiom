"""B1250 -- the D2 decode: the twist is the SO(10) grading of E6.

Locks the positive answer to B916's registered question (M1 stage (a) on B926's menu), the
correction to B916's "11 = 8+3" guess, and the two-sided control that makes it non-vacuous.
"""
import importlib.util
import pathlib

_SRC = (pathlib.Path(__file__).resolve().parents[1]
        / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
_spec = importlib.util.spec_from_file_location("b1250_d2_decode", _SRC)
dd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dd)


def test_selftest_passes():
    assert dd.selftest(verbose=False) == []


def test_B916_kill_is_reproduced():
    """B916 searched the PLAIN character and correctly found nothing."""
    assert dd.plain_character_solutions() == []


def test_the_affine_character_is_unique():
    """One bit wider: exactly one a in F2^6 works, and exactly one weight of the 27 generates it."""
    assert dd.affine_character_solutions() == [(1, 0, 1, 0, 1, 1)]
    assert dd.generating_weights() == [13]


def test_the_generator_is_itself_flipped():
    _wts, flip = dd.flip_set()
    assert 13 in flip


def test_stabiliser_is_so10_plus_u1():
    """Earned, not dimension-matched: the subalgebra is exhibited as the character's stabiliser."""
    even, odd, blocks = dd.stabiliser_blocks()
    assert (even, odd) == (40, 32)          # dim 6+40 = 46 = so(10)+u(1); complement 32 = 16+16bar
    assert [len(b) for b in blocks] == [1, 10, 16]


def test_D2_flips_exactly_the_1_plus_10_and_fixes_the_16():
    _even, _odd, blocks = dd.stabiliser_blocks()
    _wts, flip = dd.flip_set()
    singlet, ten, sixteen = blocks
    assert singlet == [13]
    assert set(singlet) | set(ten) == flip          # the flips ARE the 1 + 10
    assert not (set(sixteen) & flip)                # the 16 is untouched


def test_B916_eight_plus_three_guess_is_corrected():
    """The invariant split is 1 + 10, not 8 + 3."""
    _even, _odd, blocks = dd.stabiliser_blocks()
    sizes = [len(b) for b in blocks]
    assert sizes == [1, 10, 16]
    assert 8 not in sizes and 3 not in sizes


def test_the_control_is_two_sided_and_the_test_almost_always_says_no():
    """MB12: if random 11-subsets also admitted affine characters, D2's YES would be worthless."""
    hits, trials = dd.control_random_subsets(trials=600, seed=5)
    assert trials == 600
    assert hits <= 3, f"control too permissive: {hits}/{trials}"
