"""B198 -- the B157 metallic-exponent wall breached by computation (V190). Fast pyenv locks.

Headline: SL(5) o=5 m=1 has [A,B]=+mu^2 (k=2) -- verified on the shipped certified rep to high
precision (deterministic, no Sage / no slow SL5 search). Plus quick gauge-Newton reproductions of
the known SL(3) cells (k=4 at o=3, k=3 at o=4; m=2 o=4 -> k=2). Full runs in gauge_newton.py /
sage_groebner.py / mp_certificate.py.  Standalone character-variety math; nothing to CLAIMS.md.
"""
import os
import sys
import json
import numpy as np
import mpmath as mp

HERE = os.path.dirname(__file__)
FRONT = os.path.join(HERE, "..", "frontier", "B198_metallic_exponent_CAS")
sys.path.insert(0, FRONT)
from gauge_newton import confirm  # noqa: E402


def _dominant(counter):
    return max(counter.items(), key=lambda kv: kv[1])[0]


def test_sl5_o5_certified_k2():
    """[A,B] = +mu^2 exactly on the shipped SL(5) o=5 rep; k=1,3 excluded."""
    mp.mp.dps = 45
    d = json.load(open(os.path.join(FRONT, "cert_sl5o5_rep.json")))
    o, n, exps = d["o"], d["n"], d["exps"]
    t = mp.matrix([[mp.mpc(mp.mpf(d["t"][i][j][0]), mp.mpf(d["t"][i][j][1]))
                    for j in range(n)] for i in range(n)])
    z = mp.exp(2j * mp.pi / o); dg = [z**e for e in exps]
    A = mp.diag(dg); Ai = mp.diag([1 / x for x in dg]); Ai2 = mp.diag([1 / x**2 for x in dg])
    # on-variety + nondegenerate
    R = t * Ai2 * t * A - Ai * t * A * t
    assert mp.norm(R, mp.inf) < mp.mpf(10)**(-20)
    mu = Ai * t
    assert mp.norm(mu - t, mp.inf) > 1            # A^m != I (genuine meridian)
    B = Ai2 * t * A * (t**-1)
    comm = A * B * Ai * (B**-1)
    e2 = mp.norm(comm - mu**2, mp.inf)
    e1 = mp.norm(comm - mu**1, mp.inf)
    e3 = mp.norm(comm - mu**3, mp.inf)
    # 40-digit rep; the exponent identity amplifies relresid ~1e24, so e2 ~ 1e-19 here (the dps=60
    # certificate in mp_certificate.py reaches 1e-23). 1e-12 vs O(1) neighbours is a 19-order lock.
    assert e2 < mp.mpf(10)**(-12)                 # k=2 holds
    assert e1 > mp.mpf(1) and e3 > mp.mpf(1)      # neighbours excluded
    # scalar c = +1
    c = comm * (mu**-2)
    assert abs(c[0, 0] - 1) < mp.mpf(10)**(-12)
    assert max(abs(c[i, j]) for i in range(n) for j in range(n) if i != j) < mp.mpf(10)**(-12)
    # the rep is on the GEOMETRIC/cusped component: mu loxodromic + infinite order (NOT a
    # finite-order-mu Dehn-filling point, where k would be ambiguous mod order(mu)). See meridian_order.py.
    ev = [complex(e) for e in mp.eig(mu, left=False, right=False)]
    assert max(abs(abs(e) - 1) for e in ev) > 0.1                       # loxodromic (off unit circle)
    assert all(max(abs(e**dd - 1) for e in ev) > 1e-6 for dd in range(1, 41))  # mu infinite order


def test_validation_cells_reproduce_known_k():
    """gauge-Newton reproduces the known exact cells (B71/B89/B157)."""
    assert _dominant(confirm(1, 3, 3, [0, 1, 2], "SL3 o3", seeds=60, rng_seeds=(0,))) == (1, 4)
    assert _dominant(confirm(1, 4, 3, [0, 1, 3], "SL3 o4", seeds=60, rng_seeds=(0,))) == (1, 3)
    assert _dominant(confirm(2, 4, 3, [0, 1, 3], "SL3 o4 m2", seeds=80, rng_seeds=(0,))) == (1, 2)


# NOTE: the live SL(5) o=5 gauge-Newton breach is exercised by gauge_newton.py's __main__
# (slow: irreducible reps are ~1/130 of seeds). The fast lock above uses the shipped certified rep.


if __name__ == "__main__":
    test_sl5_o5_certified_k2()
    test_validation_cells_reproduce_known_k()
    print("ALL CHECKS PASS")
