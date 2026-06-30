"""B305 lock -- the Eisenstein trinification grading. VERIFIED: E6 -> SU(3)^3 trinification at the Eisenstein point
u=2pi i/3 (height==0 mod 3 -> 9 roots = A2^3); grading eigenvalue omega in Q(sqrt-3) (B266/B285); (theta,phi)=the
triality (B299). REFUTED (2nd time): the saddle u=i pi/3 (height==0 mod 6) gives 3 orthogonal roots = SU(2)^3, NOT
SU(3). Cascade E6 -> SU(3)^3 -> SU(2)^3 x U(1)^3. FIREWALLED; nothing to CLAIMS.md.
(E6-root component structure Sage-verified; sage-python frontier/B305_eisenstein_trinification_grading/eisenstein_trinification_grading.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B305_eisenstein_trinification_grading" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b305", _PATH)
b305 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b305)


def test_trinification_at_eisenstein():
    m3, m6 = b305.mod_counts()
    assert m3 == 9 and b305.EISENSTEIN_MOD3_COMPONENTS == [3, 3, 3]    # A2^3 = SU(3)^3
    assert b305.TRINIFICATION_AT_EISENSTEIN
    assert b305.GRADING_EIGENVALUE_IS_EISENSTEIN_OMEGA               # omega in Q(sqrt-3) = the atom


def test_theta_phi_is_the_triality():
    assert b305.THETA_PHI_IS_THE_TRINIFICATION_TRIALITY             # = B299


def test_saddle_is_su2cubed_not_su3():
    m3, m6 = b305.mod_counts()
    assert m6 == 3 and b305.SADDLE_MOD6_COMPONENTS == [1, 1, 1]      # orthogonal -> SU(2)^3
    assert b305.SADDLE_IS_SU2_CUBED_NOT_SU3                          # Chat-1 refuted, 2nd time


def test_firewall():
    assert b305.WHICH_SU3_IS_COLOR_IS_EXTERNAL
    assert b305.DEFORMATION_AS_RG_IS_LEAP
    assert b305.DERIVES_SM_VALUES is False
    assert b305.verdict()
