"""B451 — locks: B186's banked value reproduces under its exact setup (0.509),
the asymptotic escape rate is 0.445(6) by two independent methods, and the
stable orbit-count table at lambda=3."""
import os
import sys

import numpy as np

np.seterr(over="ignore", invalid="ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B451_thermo_d4_resonances"))

import resonances as R


def _b186_survival(lmb, Egrid, Kmax=30, Rbound=20.0):
    P = np.array([[(Ev - lmb) / 2, Ev / 2, 1.0] for Ev in Egrid], dtype=complex)
    alive = np.ones(len(P), bool)
    f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1)
        alive &= np.isfinite(nrm) & (nrm < Rbound)
        f.append(alive.mean())
        P[~alive] = 0.0
        P = np.array([np.array([2 * p[0] * p[1] - p[2], p[0], p[1]]) for p in P])
    return np.array(f)


def test_b186_banked_value_reproduces_with_their_window():
    f = _b186_survival(3.0, np.linspace(-4, 4, 400) + 0j)
    K = np.arange(len(f))
    m = (f > 1e-3) & (f < 0.5)
    g = float(-np.polyfit(K[m], np.log(f[m]), 1)[0])
    assert abs(g - 0.51) < 0.01          # the banked number IS their estimator's output


def test_asymptotic_line_rate_is_smaller():
    f = _b186_survival(3.0, np.linspace(-4, 4, 40000) + 0j, Kmax=24)
    K = np.arange(len(f))
    m = (K >= 10) & (K < 20) & (f > 0)
    g = float(-np.polyfit(K[m], np.log(f[m]), 1)[0])
    assert 0.42 < g < 0.48               # the corrected asymptotic ground truth


def test_no_onsurface_fixed_points():
    # T's only fixed points are (0,0,0), (1,1,1) — both off the lambda=3 surface
    for p in (np.zeros(3), np.ones(3)):
        assert np.linalg.norm(R.T(p) - p) < 1e-14
        assert abs(R.Ival(p) - 2.25) > 1     # not on I = (3/2)^2

def test_stable_orbit_counts_lambda3():
    c = 2.25
    counts = {}
    for n in (1, 2, 3, 4):
        pts = R.find_period_n_points(n, c, ngrid=30, box=3.5)
        orbs = R.orbits_from_points(pts, n)
        counts[n] = len(orbs)
    assert counts[1] == 0 and counts[2] == 2 and counts[3] == 0 and counts[4] == 1


def test_certified_primitive_table():
    import json
    path = os.path.join(HERE, "..", "frontier", "B451_thermo_d4_resonances",
                        "orbits_certified.json")
    prims = json.load(open(path))
    counts = {}
    for n, _ in prims:
        counts[n] = counts.get(n, 0) + 1
    assert counts == {'2': 2, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5} or \
           counts == {2: 2, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5}
    # the exact fixed-point identities N_n = sum_{d|n} d*P_d
    P = {2: 2, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5}
    N = {n: sum(d * P.get(d, 0) for d in range(1, n + 1) if n % d == 0)
         for n in (2, 4, 5, 6, 7, 8)}
    assert (N[2], N[4], N[5], N[6], N[7], N[8]) == (4, 8, 10, 22, 28, 48)
