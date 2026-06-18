"""B170 -- the relational/Machian scale leap, ASSESSED (V164, closes S035's last [LEAP]). Fast locks.

L2 [num, null-test]: the program's dimensionless numbers do NOT match observed constants beyond
fine-tuned numerology -- the exponents needed are non-integer (no structure), and a RANDOM base does
just as poorly => the dead value-matching lane (S014). The leap reinterprets the firewall, no teeth.
The full L1/L2 narrative lives in relational_scale.py.
"""
import numpy as np


def _phi():
    return (1 + 5 ** 0.5) / 2


def test_program_exponents_are_not_near_integers():
    # to hit constant C from base b you need N = ln C / ln b; a NATURAL match is a small integer.
    phi = _phi()
    bases = [phi ** 2, 1 + 2 ** 0.5, (3 + 13 ** 0.5) / 2]      # fig-8 / silver / bronze (>1)
    constants = [137.035999, 1836.15267, 0.23122, 0.1179, 206.7683]
    dists = [abs((d := np.log(C) / np.log(b)) - round(d)) for C in constants for b in bases]
    # median distance-to-integer ~ 0.25 (uniform) => no structure, matching needs S014 fine-tuning
    assert float(np.median(dists)) > 0.15


def test_random_base_is_indistinguishable_from_program():
    # null control: a random "metallic-like" base needs exponents just as non-integer => not special
    phi = _phi()
    prog = [phi ** 2, 1 + 2 ** 0.5, (3 + 13 ** 0.5) / 2]
    constants = [137.035999, 1836.15267, 0.23122, 0.1179, 206.7683]
    prog_med = float(np.median([abs((d := np.log(C) / np.log(b)) - round(d))
                                for C in constants for b in prog]))
    rng = np.random.default_rng(0)
    rand = [abs((d := np.log(C) / np.log(b)) - round(d))
            for _ in range(2000) for b in [rng.uniform(1.5, 3.5)] for C in constants]
    assert abs(float(np.median(rand)) - prog_med) < 0.12        # indistinguishable => value-matching dead
