"""B802 — locks the independently verified part of cc3's B783 harvest."""
import importlib.util
from pathlib import Path

import sympy as sp

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B802_cc3_b783_harvest"


def _m():
    spec = importlib.util.spec_from_file_location("b802", ARC / "verify.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_reversal_preserves_frequencies_but_complement_swaps():
    m = _m()
    w = m.fib_word(18)
    fa, fb = m.freqs(w)
    assert m.freqs(w[::-1]) == (fa, fb)                                  # reversal: preserved
    assert m.freqs(w.translate(str.maketrans("ab", "ba"))) == (fb, fa)   # complement: swapped
    assert fa + fb == 1
    assert fa != fb                                                      # so the swap is real


def test_frequencies_converge_to_golden():
    m = _m()
    fa, fb = m.freqs(m.fib_word(22))
    phi = (1 + sp.sqrt(5)) / 2
    assert abs(float(fa) - float(1 / phi)) < 1e-8
    assert abs(float(fb) - float(1 / phi**2)) < 1e-8


def test_gamma5_is_not_reading_direction():
    """The load-bearing negative: gamma5 moves phi-built quantities; reversal does not."""
    m = _m()
    phi = (1 + sp.sqrt(5)) / 2
    phibar = 1 - phi
    assert sp.simplify(phibar - (1 - phi)) == 0
    assert sp.simplify(1 / phibar - 1 / phi) != 0          # gamma5 MOVES it
    w = m.fib_word(16)
    assert m.freqs(w[::-1]) == m.freqs(w)                  # reversal does NOT
