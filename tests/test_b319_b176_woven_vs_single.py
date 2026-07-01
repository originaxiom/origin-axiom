"""B319 lock -- B176 woven-vs-single resolved: "monotone or standalone?" is a false dichotomy. The WOVEN observable
(the two-body satellite combination ladder, C2/C4) is STANDALONE (reproduced: golden_privilege.py ALL CHECKS PASS);
the SINGLE-operator observable (spectral fractality, C1) is MONOTONE (the Hurwitz constant 1/sqrt(m^2+4) is exactly
monotone; Damanik-Gorodetski). Different observables; B176 contains both; no contradiction. The standalone-ness is a
genuine COLLECTIVE effect a single operator cannot show. The single-operator spectral MEASURE itself is numerically
q-sensitive (not a clean discriminator). Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B319_b176_woven_vs_single" / "b176_woven_vs_single.py"
_spec = importlib.util.spec_from_file_location("b319", _PATH)
b319 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b319)


def test_hurwitz_c1_monotone():
    assert b319.hurwitz_is_monotone()                              # 1/sqrt(m^2+4) monotone (single-op fractality)
    assert b319.SINGLE_OPERATOR_FRACTALITY_IS_MONOTONE


def test_woven_standalone_reproduced():
    assert b319.WOVEN_LADDER_IS_STANDALONE                         # C2/C4, golden_privilege.py PASS
    assert b319.STANDALONE_IS_A_COLLECTIVE_EFFECT                  # needs two woven bodies


def test_no_contradiction_two_observables():
    assert b319.TWO_DIFFERENT_OBSERVABLES
    assert b319.NO_CONTRADICTION
    assert b319.B176_FULLY_RESOLVED


def test_single_op_measure_not_a_clean_discriminator():
    assert b319.SINGLE_OP_MEASURE_IS_Q_SENSITIVE                   # overflow + approximant-depth dominance
    assert b319.DERIVES_SM_VALUES is False
    assert b319.verdict()
