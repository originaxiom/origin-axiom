"""B287 lock -- THE DISTINGUISHED CLOSING. The figure-eight is a once-punctured-torus bundle; the fiber/0-slope
filling caps the puncture to the closed Sol torus bundle with monodromy EXACTLY A=[[2,1],[1,1]] (P1, A=LR) -- the
unique torus bundle among the 10 exceptional fillings. Answers B286's open selection question: SELECTIVE for the
object's own structure. FIREWALLED; nothing to CLAIMS.md.
(SnapPy/Regina/Twister reproducer: sage-python frontier/B287_distinguished_closing/distinguished_closing.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B287_distinguished_closing" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b287", _PATH)
b287 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b287)


def test_alexander_equals_charpoly_A():
    import sympy as sp
    t = sp.symbols('t')
    assert sp.expand(b287.charpoly_A() - (t**2 - 3*t + 1)) == 0       # fibration monodromy is A (P1)


def test_distinguished_closing_is_the_A_torus_bundle():
    assert b287.REGINA_0SURGERY == "T x I / [ 2,1 | 1,1 ]"            # monodromy EXACTLY A
    assert b287.DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE
    assert [n for n in b287.REGINA if b287.REGINA[n].startswith("T x I")] == [0]


def test_p8_torsion_ladder():
    assert b287.p8_torsion_ladder()[:4] == [1, 5, 16, 45]            # |det(A^n-I)|; n=1 -> 1 -> H1(0-surgery)=Z


def test_ten_exceptional_fillings():
    assert b287.EXCEPTIONAL_COUNT == 10                              # {-4..4} + meridian(S^3), Thurston


def test_selective_but_firewalled():
    assert b287.SELECTIVE_FOR_OWN_STRUCTURE
    assert b287.DERIVES_SM_VALUES is False
    assert b287.verdict()
