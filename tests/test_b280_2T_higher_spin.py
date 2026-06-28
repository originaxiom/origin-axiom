"""B280 lock -- 2T=SL(2,3) higher-spin content: spin-1|2T=rho_3, spin-3/2|2T=2+2 (NOT 3+1) => no triplet+singlet,
killing 'three generations + Higgs from A_4/2T spin-3/2'. Plus E6 SU(6)xSU(2) branching 27=(15,1)+(6bar,2).
FIREWALLED; nothing to CLAIMS.md. (Heavy GAP reproduced by sage-python spin_content_2T_gap.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B280_2T_higher_spin" / "spin_content_verdict.py"
_spec = importlib.util.spec_from_file_location("b280", _PATH)
b280 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b280)


def test_spin1_is_triplet():
    assert b280.SPIN1_MULT[b280.TWO_T_DIMS.index(3)] == 1
    assert sum(m * d for m, d in zip(b280.SPIN1_MULT, b280.TWO_T_DIMS)) == 3


def test_spin32_is_2plus2_not_3plus1():
    two = [i for i, d in enumerate(b280.TWO_T_DIMS) if d == 2]
    assert sum(b280.SPIN32_MULT[i] for i in two) == 2          # 2+2
    assert b280.SPIN32_MULT[b280.TWO_T_DIMS.index(3)] == 0     # no triplet
    assert not b280.THREE_GENERATIONS_FROM_SPIN32
    assert b280.verdict()
