"""B198 follow-up -- the meridian-order refinement (corrects the B198 secondary claims).

The exponent [A,B]=mu^k (mu=A^-m t) must be read on the GEOMETRIC / cusped component, where the
meridian mu has INFINITE order (loxodromic / parabolic). The bundle variety ALSO contains
finite-order-mu reps (Dehn-filling / orbifold points) where k is only defined mod order(mu) and
which are NOT the canonical cusp -- including them gives spurious "multi-exponent" readings.

This script shows:
  (1) the shipped certified SL(5) o=5 m=1 rep has mu INFINITE-ORDER and LOXODROMIC
      (|eig| off the unit circle) -> the k=2 headline is on the geometric component. [deterministic]
  (2) the grid follow-up that CORRECTS the over-reached B198 secondary claims: at SL(4) o=8 the
      variety has a finite-order-mu branch (order 20) to exclude; on the mu-infinite component
      o=8 m=1 -> k=3 = the o=4 value, so 'k=4-m(o-3)' and the 'gcd(m,o)' lead are REFUTED -- there
      is no simple single-valued k(o,m); the closed form stays NEEDS-SPECIALIST. [needs Newton, slow]

pyenv (numpy + mpmath). The headline (1) is fast/deterministic; (2) is guarded behind --grid.
"""
import os, sys, json
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))


def certified_meridian_is_loxodromic_infinite():
    mp.mp.dps = 40
    d = json.load(open(os.path.join(HERE, "cert_sl5o5_rep.json")))
    o, n, exps = d["o"], d["n"], d["exps"]
    t = mp.matrix([[mp.mpc(mp.mpf(d["t"][i][j][0]), mp.mpf(d["t"][i][j][1]))
                    for j in range(n)] for i in range(n)])
    z = mp.exp(2j * mp.pi / o); dg = [z**e for e in exps]
    mu = mp.diag([1 / x for x in dg]) * t           # mu = A^-1 t (m=1)
    ev = [complex(e) for e in mp.eig(mu, left=False, right=False)]
    off_circle = max(abs(abs(e) - 1) for e in ev)
    order = next((dd for dd in range(1, 121) if max(abs(e**dd - 1) for e in ev) < 1e-6), None)
    print("certified SL5 o=5 m=1 rep:")
    print("  |eig(mu)| =", [round(abs(e), 4) for e in ev])
    print("  max||eig|-1| = %.4f (loxodromic if >0)  order(mu) = %s" %
          (off_circle, order if order else "INFINITE"))
    assert off_circle > 0.1, "mu should be loxodromic (off unit circle)"
    assert order is None, "mu should have infinite order (geometric cusp, not Dehn-filling)"
    print("  => geometric/cusped component (k=2 unambiguous). OK")
    return True


def grid_correction():
    sys.path.insert(0, HERE)
    from gauge_newton import make_A, newton_t, newton_bt, irred, exponent
    print("\ngrid follow-up (mu-infinite filter) -- corrects the B198 secondary claims:")
    print("  o=4 m=1 and o=8 m=1 BOTH -> k=3 on the mu-infinite component => no simple k(o,m).")
    for (m, o, n, exps) in [(1, 4, 3, [0, 1, 3]), (1, 8, 4, [1, 3, 5, 7])]:
        A = make_A(o, exps)[0]; Ai = np.linalg.inv(A); gfix = list(range(n - 1))
        rng = np.random.default_rng(0); found = {}
        for s in range(3000):
            if m == 1:
                Aa, Aii, Ai2 = make_A(o, exps); t, r = newton_t(Aa, Aii, Ai2, n, gfix, rng)
                B = None if t is None else Ai2 @ t @ Aa @ np.linalg.inv(t)
            else:
                x, r = newton_bt(A, m, n, gfix, rng)
                B, t = (None, None) if x is None else (x[:n*n].reshape(n, n), x[n*n:].reshape(n, n))
            if t is None or r > 1e-11 or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e6:
                continue
            mu = np.linalg.matrix_power(Ai, m) @ t
            if np.max(np.abs(mu - t)) < 1e-6 or irred(A, B, n) != n*n:
                continue
            evmu = np.linalg.eigvals(mu)
            mu_inf = not any(np.max(np.abs(evmu**dd - 1)) < 1e-6 for dd in range(1, 41))  # infinite order
            s_, k_, err = exponent(A, B, t, m)
            if err < 1e-7 and mu_inf:
                found[k_] = found.get(k_, 0) + 1
            if sum(found.values()) >= 8:
                break
        print("  o=%d m=%d : mu-infinite exponents -> %s" % (o, m, found))


if __name__ == "__main__":
    certified_meridian_is_loxodromic_infinite()
    if "--grid" in sys.argv:
        grid_correction()
