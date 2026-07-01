"""B323 lock -- adjudication of Chat-1's four-levels meditation + the omega-circulant Yukawa. Part 1 (the four levels)
VERIFIED + helpful: L1 object Sym=D4 order 8 (no Z/3), L2 seam Z/2xZ/2 (no Z/3, B321), L3 E6 center Z/3 (det Cartan
E6=3), L4 commensurator Eisenstein Z/3 (B302) -- two DISTINCT Z/3's (gauge vs commensurator), both from prime 3; the
session's overclaims were level-confusions. Part 3 (M=alpha J + omega P, 'perturbation exactly omega') REFUTED as a
crossing: tautological (omega-conjugates related by omega by construction) + eigenvalue ratio ~0.15 doesn't match any SM
mass ratio + firewalled/CRUX-gated. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B323_four_levels_adjudication" / "four_levels_adjudication.py"
_spec = importlib.util.spec_from_file_location("b323", _PATH)
b323 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b323)


def test_four_levels_z3_attribution():
    assert b323.object_has_no_z3()                                 # L1 D4 order 8, 3 does not divide 8
    assert b323.e6_cartan_det() == 3                               # L3 E6 center Z/3
    assert b323.FOUR_LEVELS_FRAMING_VERIFIED and b323.TWO_Z3_ARE_DISTINCT


def test_framing_is_helpful():
    assert b323.FRAMING_IS_A_HELPFUL_CONSOLIDATION                # explains overclaims as level-confusions


def test_omega_yukawa_is_tautological_and_nonmatching():
    assert b323.OMEGA_PERTURBATION_IS_TAUTOLOGICAL               # omega-conjugates related by omega
    assert abs(b323.omega_circulant_ratio() - 0.145) < 0.03      # ~0.14, no SM ratio
    assert b323.YUKAWA_RATIO_DOES_NOT_MATCH_SM
    assert b323.PART3_IS_NOT_A_CROSSING


def test_no_claims():
    assert b323.DERIVES_SM_VALUES is False
    assert b323.verdict()
