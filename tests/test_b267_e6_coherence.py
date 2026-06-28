"""B267 locks -- coherence: the McKay-E6 (B266) and the character-variety-E6 (B264/B265) are ONE E6.
McKay(2T) graph reproduces B264's exponents {1,4,5,7,8,11}; h=12; dim=78; Molien(2T)=(1+q^12)/((1-q^6)(1-q^8)).
FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B267_e6_coherence" / "e6_coherence.py"
_spec = importlib.util.spec_from_file_location("b267", _PATH)
b267 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b267)


def test_mckay_graph_recovers_b264_exponents():
    # the decisive bridge: McKay(2T) (affine node removed) -> E6 Dynkin -> exponents = B264's grading
    assert b267.exponents_from_mckay() == b267.EXPONENTS == [1, 4, 5, 7, 8, 11]


def test_coxeter_root_dim_invariants():
    assert sum(b267.MARKS_2T) == b267.H == 12               # Coxeter number
    assert sum(b267.EXPONENTS) == 6 * b267.H // 2 == 36     # #positive roots
    assert 6 * (b267.H + 1) == 78                           # dim E6 = l(h+1)


def test_molien_series_carries_coxeter_number():
    q = sp.Symbol("q")
    target = sp.cancel((1 + q**12) / ((1 - q**6) * (1 - q**8)))   # numerator 1+q^h, h=12
    assert sp.simplify(b267.molien_series_2T() - target) == 0
