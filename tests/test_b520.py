"""B520 locks — the handoff verification (beta-function reproduces; ceiling corrected; BTZ formula)."""
import numpy as np
import mpmath as mp


def _g(k, seeds=2, orbits=15, steps=60000):
    """Goldman-ergodic beta-function via the golden trace map orbit average."""
    def TF(p):
        x, y, z = p; return (z, x, x*z - y)
    allv = []
    for sd in range(seeds):
        rng = np.random.default_rng(sd*5 + 1); got = 0
        while got < orbits:
            x, y = rng.uniform(-2, 2, 2); b = -x*y; c = x*x + y*y - 2 - k; disc = b*b - 4*c
            if disc < 0:
                continue
            z = (-b + np.sqrt(disc))/2
            if abs(z) > 2:
                continue
            p = (x, y, z); got += 1
            for _ in range(steps):
                p = TF(p)
                if abs(p[0]) <= 2.0001 and abs(p[1]) <= 2.0001:
                    allv.append(np.log(max(abs(p[0]**2 + p[1]**2 - p[0]*p[1]*p[2]), 1e-300)))
    return np.mean(allv)


def test_beta_zero_at_pointer_not_0764():
    # B507 reproduces: g(0)~0 (the pointer), g(0.764) solidly positive => handoff's correction rejected
    assert abs(_g(0.0)) < 0.02
    assert _g(0.7638) > 0.2


def test_selfdouble_terminates_but_not_max():
    # the 8x8 self-double has no canonical Pisot coupling (ceiling of the self-double ladder)...
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    Mp = [np.linalg.matrix_power(M, k) for k in range(4)]
    def pisot8(C, D):
        M8 = np.block([[M, C], [D, M]])
        ev = np.sort(np.abs(np.linalg.eigvals(M8)))
        return ev[-1] > 1.0001 and ev[-2] < 0.9999
    assert not any(pisot8(Mp[ci], Mp[di]) for ci, di in [(1, 2), (2, 1), (1, 1), (2, 2)])
    # ...but dim-5 golden Pisot exists (B516) => "3 is the max" is false; not re-asserted here


def test_btz_entropy_formula():
    mp.mp.dps = 20
    assert abs(mp.acosh(mp.mpf(5)/2) - mp.log((5 + mp.sqrt(21))/2)) < mp.mpf('1e-18')
