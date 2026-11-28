#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0018: an own recomputation of the one part of the card that its own definitions
fix, P1, sharing nothing with the producer's code. On Re tau = 0, tau = iy, q = exp(-2 pi y):
eta = q^(1/24) prod (1 - q^n), E_2 = 1 - 24 sum sigma_1(n) q^n, E2_hat = E_2 - 3/(pi y), and
V_FILQ,n = (2y)^(-3n) |eta|^(-12n) ((n pi^2 y^2 / 3) E2_hat^2 - 3); the minima in y for n = 1, 2, 3.
    python3 relays/claims/banking/q0018_own.py                the decisive run
    python3 relays/claims/banking/q0018_own.py --plant-sign   the failing control: E2_hat = E_2 + 3/(pi y), which must
                                                              move the minima off the recorded values
Exit 0 when the recomputed P1 values agree with the recorded ones; 1 otherwise. P2 to P4 are not recomputed (the
verdict says why)."""
import sys
import mpmath as mp

ARGS = sys.argv[1:]
if ARGS not in ([], ["--plant-sign"]):
    print("usage: no argument, or --plant-sign"); sys.exit(2)
SIGN = 1 if ARGS == ["--plant-sign"] else -1
mp.mp.dps = 40


def V(n, y):
    q = mp.exp(-2 * mp.pi * y)
    eta = mp.exp(-2 * mp.pi * y / 24)
    e2 = mp.mpf(1)
    k = 1
    while True:
        t = q ** k
        if t < mp.mpf(10) ** -45:
            break
        eta *= 1 - t
        e2 -= 24 * mp.fsum(d for d in range(1, k + 1) if k % d == 0) * t
        k += 1
    e2h = e2 + SIGN * 3 / (mp.pi * y)
    return (2 * y) ** (-3 * n) * eta ** (-12 * n) * ((n * mp.pi ** 2 * y ** 2 / 3) * e2h ** 2 - 3)


ok = True
def show(label, got, good):
    global ok
    print("DECISIVE: %s %s" % (label, got))
    if not good:
        ok = False

rec = {1: (mp.mpf("1.234579947"), mp.mpf("-8.92881487")), 2: (mp.mpf("1.18338966"), None),
       3: (mp.mpf("1.155439018"), mp.mpf("-78.340509"))}
for n in (1, 2, 3):
    ys = [mp.mpf(1) + mp.mpf(k) / 200 for k in range(0, 401)]
    vals = [V(n, y) for y in ys]
    i = min(range(len(vals)), key=lambda j: vals[j])
    interior = 0 < i < len(vals) - 1
    ystar = mp.findroot(lambda y: mp.diff(lambda u: V(n, u), y), ys[i]) if interior else ys[i]
    vstar = V(n, ystar)
    curv = mp.diff(lambda u: V(n, u), ystar, 2)
    ry, rv = rec[n]
    agree = interior and abs(ystar - ry) < 2e-9 and (rv is None or abs(vstar - rv) < 1e-6 * abs(rv)) and curv > 0
    show("P1 V_FILQ,%d on Re tau = 0, y in [1, 3]: the minimum at y = %s, V = %s, V'' = %s; as recorded"
         % (n, mp.nstr(ystar, 12), mp.nstr(vstar, 12), mp.nstr(curv, 6)), agree, agree)
sys.exit(0 if ok else 1)
