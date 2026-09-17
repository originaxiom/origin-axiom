"""B14 lock -- the half-step square root: the arithmetic under the orientation axiom.

B14 was banked PROVED in the repository's first week and carried no script and no lock. It was the one
record of the paper's ninety-five without a primary lock, and it underpins the axiom the paper prices
highest: the squaring that buys orientation and, by the paper's own account, costs the chirality bit.
Found by an outside referee auditing the manifest, closed 2026-09-17 (B1424).

Every assertion here is exact integer arithmetic and runs in well under a second.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B14_half_step_square_root_selector" / "verification"))

import square_root as sr  # noqa: E402


A = sr.mul(sr.L, sr.R)
F = sr.mul(sr.L, sr.P)


def test_F_is_a_square_root_of_A_and_reverses_orientation():
    assert sr.mul(F, F) == A
    assert sr.det(F) == -1          # the squaring is exactly what buys orientability
    assert sr.det(A) == 1


def test_the_square_root_is_unique_up_to_sign():
    roots = sr.square_roots_by_search(A, 6)
    assert roots == sorted([F, sr.neg(F)])


def test_A_has_no_orientation_preserving_square_root():
    """the Cayley-Hamilton half: det X = +1 would need tr(X)^2 = det(A + I) = 5"""
    assert not any(sr.det(X) == 1 for X in sr.square_roots_by_search(A, 6))
    assert sr.det(((3, 1), (1, 2))) == 5     # A + I, whose determinant is the obstruction


def test_L_a_R_b_has_an_orientation_reversing_root_iff_a_equals_b():
    for k in range(1, 5):
        assert sr.has_orientation_reversing_root(k, k)
        Lk = ((1, k), (0, 1))
        assert sr.mul(sr.mul(Lk, sr.P), sr.mul(Lk, sr.P)) == sr.B(k, k)


def test_the_control_fires_for_a_not_equal_b():
    """the criterion can fail -- otherwise the iff would be vacuous"""
    off = [(a, b) for a in range(1, 5) for b in range(1, 5) if a != b]
    assert off and all(not sr.has_orientation_reversing_root(a, b) for a, b in off)


def test_the_recorded_run_agrees():
    out = (ROOT / "frontier" / "B14_half_step_square_root_selector" / "verification" / "square_root.out.txt").read_text()
    assert "B14 VERIFIED: True" in out
