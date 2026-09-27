#!/usr/bin/env python3
"""B1385 S7 -- the Eisenstein cusp lemma: on a hexagonal cusp torus, a leading Fourier shell that is invariant under a rotation of
order three is never annular.

Frame (B1351 (ii), B1370 section 1): at a free cusp the sign of the Higgs form's leading cusp mode F partitions the torus into
d+ = {F > 0} and d- = {F < 0}, and the cusp's contribution is N = -chi(d+).  B1370: when the lowest allowed shell is one direction
{+-k}, F = |a| cos(2 pi k.x + phi) and d+ is an annulus, N = 0.  Here: when the cusp lattice is hexagonal the first dual shell has
three directions k1 + k2 + k3 = 0, and if an isometry fixing the cusp acts on the torus by an order-3 rotation and fixes the class
(epsilon = +1 is forced: an order-3 map has no eigenvalue -1), then in coordinates centred at its fixed point
F = 2|c| sum_j cos(2 pi k_j.y + phi).  Its critical points are three extrema of values 3 cos(phi + 2 pi m/3) (m = 0, +-1) and three
saddles of value -cos(3 phi) (Morse count 3 - 3 = 0 = chi(T^2)); an extremum is a maximum iff it lies above the saddle value.  So
chi(d+) = #{m : cos(phi + 2 pi m/3) > 0} - 3 [cos 3 phi < 0], and writing u = phi mod 2 pi/3 in [-pi/3, pi/3):

    chi(d+) = +1 for |u| < pi/6 (d+ is one disc),   chi(d+) = -1 for |u| > pi/6 (d- is one disc),

never 0 away from the six transition phases phi = +-pi/6 mod 2 pi/3: N = -chi(d+) = -+1.  (Topologically: the rotation acts on H_1(T^2) without a fixed
line, so an invariant region cannot be a union of essential annuli.)  Without the rotation the three amplitudes are independent and
both kinds occur on open sets; with one direction (B1370) or two (a rhombic lattice) the partition is annular or degenerate.

The Euler characteristics are computed here on a triangulated periodic grid (the full subcomplex on the vertices where F > 0) and
compared with the Morse count.  Usage: python3 eisenstein_partition.py"""
import math
import random

SHELL3 = ((1, 0), (0, 1), (-1, -1))           # the hexagonal first dual shell in lattice coordinates (k1 + k2 + k3 = 0)


def chi_positive(F, n=180):
    """chi of {F > 0} on the torus [0,1)^2 via the triangulated grid (squares split along the (1,1) diagonal)"""
    pos = [[F(i / n, j / n) > 0 for j in range(n)] for i in range(n)]
    V = sum(sum(r) for r in pos)
    E = 0
    T = 0
    for i in range(n):
        for j in range(n):
            if not pos[i][j]:
                continue
            a, b, d = pos[(i + 1) % n][j], pos[i][(j + 1) % n], pos[(i + 1) % n][(j + 1) % n]
            E += a + b + d
            T += (a and d) + (b and d)
    return V - E + T


def symmetric_field(phi, amps=(1, 1, 1), phases=(0, 0, 0)):
    def F(s, t):
        return sum(a * math.cos(2 * math.pi * (m * s + k * t) + phi + p) for a, (m, k), p in zip(amps, SHELL3, phases))
    return F


def morse_prediction(phi):
    """#{m : cos(phi + 2 pi m / 3) > 0} - 3 [cos 3 phi < 0]: the extrema above zero minus the saddles above zero"""
    count = sum(1 for m in (0, 1, -1) if math.cos(phi + 2 * math.pi * m / 3) > 0)
    return count - (3 if math.cos(3 * phi) < 0 else 0)


def s7_symmetric(n=180):
    rows = []
    for deg in range(-180, 181, 15):
        if deg % 60 == 30:                                    # skip the transition phases +-30, +-90, +-150
            continue
        phi = math.radians(deg)
        c = chi_positive(symmetric_field(phi), n)
        c_minus = chi_positive(lambda s, t: -symmetric_field(phi)(s, t), n)
        assert c == morse_prediction(phi) and c in (1, -1) and c + c_minus == 0, (deg, c, c_minus)
        rows.append((deg, c))
    return rows


def s7_open_and_forced(trials=300, n=120, seed=7):
    """without the rotation: random amplitudes and phases on the hexagonal shell give both annular and disc-type partitions; a single
    direction and a rhombic two-direction shell with unequal amplitudes give annular ones"""
    rng = random.Random(seed)
    annular = disc = 0
    for _ in range(trials):
        amps = [rng.uniform(0.2, 1.0) for _ in range(3)]
        phases = [rng.uniform(-math.pi, math.pi) for _ in range(3)]
        c = chi_positive(symmetric_field(0.0, amps, phases), n)
        if c == 0:
            annular += 1
        else:
            disc += 1
    one = chi_positive(lambda s, t: math.cos(2 * math.pi * s + 0.4), n)
    two = chi_positive(lambda s, t: math.cos(2 * math.pi * s) + 0.6 * math.cos(2 * math.pi * t + 1.0), n)
    assert one == 0 and two == 0 and annular > 0 and disc > 0
    return {"hexagonal shell, no symmetry: annular": annular, "disc-type": disc,
            "one direction": one, "two directions, unequal": two}


if __name__ == "__main__":
    rows = s7_symmetric()
    print("S7 the Eisenstein cusp lemma -- chi(d+) of the order-3-symmetric first shell, by phase (degrees):")
    print("   ", "  ".join("%+d:%+d" % r for r in rows))
    print("    every phase away from +-30, +-90, +-150 degrees: chi(d+) = the Morse count = +-1, never 0 -> N = -chi(d+) = -+1")
    print("S7 controls:", s7_open_and_forced())
    print("DONE")
