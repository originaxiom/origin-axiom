"""B291 lock -- is any closing SCALE-DISTINGUISHED? A min-volume closing exists and is stable (m004(+-5,1)=m003(-2,3),
vol 0.98137, NOT Weeks), but it is non-arithmetic (B288) and not the fiber/Sol closing (B287); the systole gives no
finite distinguished closing. Selection is AXIS-STRATIFIED (scale axis picks yet another closing). FIREWALLED; nothing
to CLAIMS.md. (SnapPy+Regina reproducer: sage-python frontier/B291_scale_extremal/scale_extremal.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B291_scale_extremal" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b291", _PATH)
b291 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b291)


def test_min_volume_closing_exists_and_stable():
    assert b291.MIN_VOLUME > b291.WEEKS_VOLUME                    # not the Weeks manifold
    assert b291.TWO_METHODS_AGREE and b291.TRIANGULATION_STABLE


def test_min_volume_closing_is_not_arithmetic():
    assert b291.min_volume_is_arithmetic() is False              # x^4-x-1 non-arithmetic (re-checked in pyenv)


def test_selection_is_axis_stratified():
    assert b291.SCALE_AXIS_COINCIDES_WITH_FIBER is False         # B287 (0,1) non-hyperbolic
    assert b291.SCALE_AXIS_COINCIDES_WITH_ARITHMETIC is False    # B288 none arithmetic
    assert b291.AXIS_STRATIFIED


def test_systole_no_finite_extremum_firewall():
    assert b291.SYSTOLE_INF == 0                                 # shortest geodesic -> 0; no finite extremum
    assert b291.DERIVES_SM_VALUES is False
    assert b291.verdict()
