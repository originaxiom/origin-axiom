"""B589 — the E6_2 pair amplitudes identified exactly (locks).

p_j = (2/sqrt7) sin(2pi j'/7) * zeta_14^{k_j} with (j', k) = (1,+3), (3,-2), (2,-1)
— the moduli are the theta-odd sine kernel (B572); verified against the banked
B586 values. See frontier/B589_pair_amplitudes/FINDINGS.md.
"""
import cmath
import math


BANKED = {
    "27": 0.13151189 + 0.57619122j,
    "351p": 0.20449548 - 0.25642922j,
    "351": 0.66399264 - 0.31976200j,
}
CLOSED = {
    "27": (2 / math.sqrt(7)) * math.sin(2 * math.pi / 7)
          * cmath.exp(2j * math.pi * 3 / 14),
    "351p": (2 / math.sqrt(7)) * math.sin(6 * math.pi / 7)
            * cmath.exp(-2j * math.pi * 2 / 14),
    "351": (2 / math.sqrt(7)) * math.sin(4 * math.pi / 7)
           * cmath.exp(-2j * math.pi * 1 / 14),
}


def test_closed_forms_match_banked():
    for nm in BANKED:
        assert abs(CLOSED[nm] - BANKED[nm]) < 1e-7


def test_sum_is_one():
    assert abs(sum(CLOSED.values()) - 1) < 1e-12


def test_moduli_are_the_sine_kernel():
    # the s=1 row of B572's S_odd = -i (2/sqrt7) sin(2 pi s t / 7), t = 1,2,3
    kernel = sorted(2 / math.sqrt(7) * abs(math.sin(2 * math.pi * t / 7))
                    for t in (1, 2, 3))
    ours = sorted(abs(v) for v in CLOSED.values())
    for a, b in zip(kernel, ours):
        assert abs(a - b) < 1e-12


def test_r2_cubic():
    r2 = abs(CLOSED["351p"])
    assert abs(7 * r2 ** 3 + 7 * r2 ** 2 - 1) < 1e-12
