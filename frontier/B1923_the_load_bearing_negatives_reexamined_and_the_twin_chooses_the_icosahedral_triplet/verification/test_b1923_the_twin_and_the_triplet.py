"""B1923's lock: the Weil representation's triplet under T for psi and for psi scaled by 2 (the twin), recomputed; a
planted square scaling (4 = 2^2, a square mod 5) must NOT exchange them. It writes nothing."""
import sys, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import weil_twin as W
S5 = 5 ** 0.5


def tr3(a):
    T, F = W.weil(a)
    E3, O2 = W.parity_parts(T)
    return complex(np.trace(E3))


def test_the_twin_exchanges_the_triplets():
    assert abs(tr3(1) - (1 - S5) / 2) < 1e-9 and abs(tr3(2) - (1 + S5) / 2) < 1e-9


def test_a_square_scaling_does_not():
    assert abs(tr3(4) - tr3(1)) < 1e-9                         # 4 is a square mod 5: the same triplet


def test_the_image_is_sl2_f5():
    T, F = W.weil(1)
    assert len(W.closure([T, F])) == 120
