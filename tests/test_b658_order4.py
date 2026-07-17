"""B658 locks — the order-4 flip verdict (wall 8 total)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B658 = os.path.join(HERE, "..", "frontier", "B658_order4_flips")


def test_control_reproduces_banked_singularity():
    out = open(os.path.join(B658, "b658_output.txt")).read()
    assert "control singular as banked: True" in out


def test_both_order4_families_broken_on_sym0():
    out = open(os.path.join(B658, "b658_output.txt")).read()
    # control + two families = three identical singular solutions
    assert out.count("d = ((0), (0), (1))   [blocks Sym16, Sym8, Sym0]") == 3
    assert out.count("invertible member: False") == 3
    assert "peripheral conjugator (w, s, t): ('', -1, 1)" in out
    assert "peripheral conjugator (w, s, t): ('aBAb', -1, 1)" in out
    assert "phi(a)=A: BROKEN" in out and "phi(a)=B: BROKEN" in out
    assert "WALL-8 UPGRADE" in out
