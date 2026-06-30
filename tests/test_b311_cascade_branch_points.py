"""B311 lock -- the cascade's object-specific core is the TRINIFICATION branch point only; the full chain is not
realized on the figure-eight's curve. Verifies (and corrects) Chat-2's extension: the cascade grading points M=i (N=2)
and M=e^{i pi/3} (N=3) ARE branch points of the fig-8 A-poly discriminant Disc=(x-1)^2(x+1)^2(x^2-3x+1)(x^2+x+1),
x=M^2 -- but N=2 (M=i) is REDUCIBLE (L=1, abelian), only N=3 (trinification, L=-1) is irreducible, and N>=4 are not
branch points. So the realization is NOT closed; the object core is the trinification (B305). The two arithmetic ends
(Eisenstein x^2+x+1, golden x^2-3x+1) sit in one discriminant. Realization stays the CRUX. Nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B311_cascade_branch_points" / "cascade_branch_points.py"
_spec = importlib.util.spec_from_file_location("b311", _PATH)
b311 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b311)
_x = sp.symbols("x")


def test_apoly_sign_and_two_ends_in_one_discriminant():
    assert b311.a_poly_sign_ok()                                          # complete structure L=-1, c-sign fixed
    assert b311.discriminant_factored() == (_x - 1) ** 2 * (_x + 1) ** 2 * (_x**2 - 3 * _x + 1) * (_x**2 + _x + 1)
    assert b311.TWO_ENDS_IN_ONE_DISCRIMINANT                              # Eisenstein x^2+x+1 AND golden x^2-3x+1


def test_chat2_branchpoints_verified():
    assert b311.is_branch(sp.I)                                           # N=2 M=i  -- IS a branch point (Chat-2 right)
    assert b311.is_branch(sp.exp(sp.I * sp.pi / 3))                       # N=3 M=e^{ipi/3} -- IS a branch point
    assert b311.CHAT2_BRANCHPOINT_CLAIM_VERIFIED


def test_the_catch_n2_reducible_nge4_absent():
    assert b311.is_reducible(sp.I)                                        # N=2 is REDUCIBLE (L=1) -- Chat-2 missed this
    assert not b311.is_reducible(sp.exp(sp.I * sp.pi / 3))                # N=3 trinification is irreducible (L=-1)
    assert not b311.is_branch(sp.exp(sp.I * sp.pi / 4))                   # N=4 not on the curve
    assert b311.N2_IS_BRANCH_BUT_REDUCIBLE and b311.NGE4_NOT_BRANCH


def test_object_core_is_trinification_realization_is_crux():
    assert b311.OBJECT_CORE_IS_TRINIFICATION_ONLY                         # strengthens B305 (char-variety relevance)
    assert b311.CASCADE_REALIZATION_CLOSED is False                       # full chain NOT realized on the curve
    assert b311.REALIZATION_IS_THE_CRUX
    assert b311.DERIVES_SM_VALUES is False
    assert b311.verdict()
