"""B309 lock -- the kappa-unification: ONE commutator trace kappa = tr[a,b] = u^2+2, FOUR faces (existence/P008,
geometry/seam B286, matter/CP B285+cascade B305-306, quantum/Face IV). kappa-2 = omega^2, |kappa-2| = 1 (the unit
obstruction); same kappa at u=0 (abelian wall, P008) and u=omega (CP phase, B285). E6 is the unique exceptional group
that is complex AND has center Z/3 (generic group theory). A CONSOLIDATION connecting the recent arc to the founding
principle P008 -- NOT a discovery. The kappa=TOE reading is firewalled. Nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B309_kappa_unification" / "kappa_unification.py"
_spec = importlib.util.spec_from_file_location("b309", _PATH)
b309 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b309)


def test_one_kappa_four_evaluations():
    f = b309.kappa_facts()
    assert f["abelian"] == 2                              # u=0 -> P008 abelian/cancellable wall
    assert f["kappa_minus_2_is_omega2"]                  # kappa-2 = omega^2 (the Eisenstein obstruction)
    assert f["modulus"] == 1                             # |kappa-2| = 1, the unit obstruction
    assert len(b309.FOUR_FACES) == 4


def test_e6_unique_complex_and_z3():
    assert b309.EXCEPTIONAL_CENTERS["E6"] == 3 and b309.EXCEPTIONAL_COMPLEX["E6"]
    assert [g for g in b309.EXCEPTIONAL_CENTERS if b309.EXCEPTIONAL_CENTERS[g] == 3] == ["E6"]
    assert sum(1 for g in b309.EXCEPTIONAL_COMPLEX if b309.EXCEPTIONAL_COMPLEX[g]) == 1   # only E6 complex
    assert b309.E6_UNIQUE_COMPLEX_AND_Z3


def test_is_a_consolidation_not_a_discovery():
    assert b309.IS_A_CONSOLIDATION_NOT_A_DISCOVERY       # P008 already banked the kappa-obstruction


def test_firewall():
    assert b309.KAPPA_IS_THE_TOE_READING_FIREWALLED      # emergent order, not the contents
    assert b309.DERIVES_SM_VALUES is False
    assert b309.verdict()
