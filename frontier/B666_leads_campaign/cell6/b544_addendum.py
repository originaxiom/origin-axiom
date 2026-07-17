"""CELL 6 / B544 addendum: certify the two re-derived words against the two
numerical loose ends of the main run.

A1 (FK): the Newton solve stalled at residual 2.4e-5 because the phason mode is
near-zero (Hessian min eig ~2.5e-10, Peierls barrier astronomically small at
K=0.5, q=610). Certify the hop word: compute the correction dx = pinv(H) g at
the converged point (pseudo-inverse, phason projected), report ||dx||_inf vs the
min floor margin; polish x by the correction + extra damped relaxations and
re-extract the word. Also: an INDEPENDENT second equilibrium (gradient
pre-relaxation from a different phase) and a K = 0.8 run -- the word must be
610/610 mechanical in every case (>= 2 seeds / >= 2 settings rule).

A2 (circle map): the single 2583/2584 mismatch letter is the knife-edge closure
point (the critical orbit returns to an integer to within 3.4e-25 by the very
bisection that defines Omega). Recount with floors snapped to the nearest
integer when within 1e-15 (mpmath, dps 30 -- twelve orders of margin above the
5e-25-scale residual, twelve below the next-nearest orbit point distance).
"""
import numpy as np
import mpmath as mp

p, q = 987, 610
idx = np.arange(q)


def fk_g_hess(x, K):
    xp = np.roll(x, -1).copy(); xp[-1] += p
    xm = np.roll(x, 1).copy();  xm[0] -= p
    g = xp + xm - 2*x - (K/(2*np.pi))*np.sin(2*np.pi*x)
    H = np.zeros((q, q))
    H[idx, idx] = 2 + K*np.cos(2*np.pi*x)
    H[idx, (idx+1) % q] -= 1
    H[idx, (idx-1) % q] -= 1
    return g, H


def hop_word_match(x):
    fl = np.floor(x).astype(int)
    hop = np.append(fl[1:], int(np.floor(x[0]+p))) - fl
    best = -1
    for s in range(q):
        mech = ((idx+1)*p + s)//q - (idx*p + s)//q
        best = max(best, int(np.sum(hop == mech)))
    margin = float(np.min(np.abs(x - np.rint(x))))
    return best, margin


def solve_fk(beta, K, pre=4000, newton=60):
    x = idx*p/q + beta
    for _ in range(pre):                       # damped relaxation (energy descent)
        g, _ = fk_g_hess(x, K)
        x = x + 0.2*g                          # note: g = -dE/dx
    for _ in range(newton):
        g, H = fk_g_hess(x, K)
        if np.max(np.abs(g)) < 1e-12:
            break
        dx, *_ = np.linalg.lstsq(-H, -g, rcond=1e-8)   # H dx = g, phason-safe
        x = x + dx
    g, H = fk_g_hess(x, K)
    return x, g, H


print("A1 -- FK word certification")
for (beta, K) in ((1/(2*q), 0.5), (0.37, 0.5), (0.71, 0.5), (1/(2*q), 0.8)):
    x, g, H = solve_fk(beta, K)
    res = float(np.max(np.abs(g)))
    dx, *_ = np.linalg.lstsq(H, g, rcond=1e-8)
    ev = np.linalg.eigvalsh(H)
    best, margin = hop_word_match(x)
    print(f"  K={K}, init beta={beta:.6f}: residual {res:.2e}, "
          f"||pinv(H)g||_inf = {np.max(np.abs(dx)):.2e}, margin = {margin:.2e}, "
          f"Hessian eigs [{ev[0]:+.2e}, {ev[1]:+.2e}, ...] -> "
          f"hop word match = {best}/{q}")
print("  certification: word is 610/610 mechanical iff ||pinv(H)g||_inf << margin in every row")

print("\nA2 -- circle-map knife-edge letter")
mp.mp.dps = 30
P, Q = 1597, 2584


def f(x, Om):
    return x + Om - mp.sin(2*mp.pi*x)/(2*mp.pi)


lo, hi = mp.mpf(0), mp.mpf(1)


def orbit_end(Om, n):
    x = mp.mpf(0)
    for _ in range(n):
        x = f(x, Om)
    return x


flo = orbit_end(lo, Q) - P
for _ in range(110):
    mid = (lo + hi)/2
    fm = orbit_end(mid, Q) - P
    if (flo < 0) == (fm < 0):
        lo, flo = mid, fm
    else:
        hi = mid
Om = (lo + hi)/2

xs = [mp.mpf(0)]
for _ in range(Q):
    xs.append(f(xs[-1], Om))
snap = 0
floors = []
for v in xs:
    r = mp.nint(v)
    if abs(v - r) < mp.mpf('1e-15'):
        floors.append(int(r))          # snap: the knife-edge closure point
        if abs(v - r) > 0:
            snap += 1
    else:
        floors.append(int(mp.floor(v)))
itin = np.array([floors[n+1] - floors[n] for n in range(Q)], dtype=np.int64)
nn = np.arange(Q, dtype=np.int64)
best = -1
for s in range(Q):
    mech = ((nn+1)*P + s)//Q - (nn*P + s)//Q
    best = max(best, int(np.sum(itin == mech)))
print(f"  snapped {snap} knife-edge point(s); itinerary vs mechanical {P}/{Q}: "
      f"best match = {best}/{Q}")
