"""B1422 lock -- the foundations re-read.

(1) the order label: M^2 = LR and not RL under the project's own convention, with the conjugacy control that
    explains why the mislabel was invisible to every invariant the corpus checks;
(2) the two corrected locks now assert the verified reading rather than the retracted one;
(3) the retracted phrases are registered, so the sweep can fire on them.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "frontier" / "B1422_the_foundations_reread" / "verification"


def test_the_monodromy_is_LR_not_RL():
    r = subprocess.run([sys.executable, str(D / "lr_vs_rl.py")], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stderr[-800:]
    assert "M^2 == LR : True" in r.stdout
    assert "M^2 == RL : False" in r.stdout


def test_the_two_orders_are_conjugate_which_is_why_it_hid():
    """trace and determinant cannot see the order -- the control that explains the fifteen-month mislabel"""
    r = subprocess.run([sys.executable, str(D / "lr_vs_rl.py")], capture_output=True, text=True, timeout=120)
    assert "cannot see the order: True" in r.stdout


def test_b291_asserts_the_corrected_reading():
    sys.path.insert(0, str(ROOT / "frontier" / "B291_scale_extremal"))
    import importlib
    b291 = importlib.import_module("verdict")
    importlib.reload(b291)
    assert b291.SCALE_AXIS_COINCIDES_WITH_ARITHMETIC is True      # the Meyerhoff manifold IS arithmetic
    assert b291.SCALE_AXIS_KEEPS_THE_OBJECTS_FIELD is False       # and keeps none of Q(sqrt-3)
    assert not hasattr(b291, "min_volume_is_arithmetic")          # the misnamed predicate is gone
    assert b291.min_volume_keeps_the_objects_field() is False


def test_the_retracted_phrases_are_registered():
    s = (ROOT / "docs" / "RETRACTED_PHRASES.md").read_text()
    assert "no closed hyperbolic filling of m004 is arithmetic" in s
    assert "the min-volume closing is non-arithmetic" in s
    assert "174 closings, still 0 arithmetic" in s


def test_the_chapter_closure_is_scoped_and_registered():
    assert "SCOPED AND SUPERSEDED IN PART" in (ROOT / "ROADMAP.md").read_text()
    assert "never scoped, and the repo held it against itself" in (ROOT / "docs" / "RETRACTIONS.md").read_text()
