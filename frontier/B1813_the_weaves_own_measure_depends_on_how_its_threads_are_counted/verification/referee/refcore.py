"""Referee core (B1813 draft; independent of the draft's code).  Two samplers of the length measure of a closed
geodesic on SL(2,Z)\\H:
  (1) axis method: fixed points of A, arclength z = m + r(tanh s + i sech s), s in [0, ell), reduce to F;
  (2) run-segment method (Series' cross-section): for the cyclic run sequence a_1..a_{2m} of the positive word, the piece
      of the geodesic (-y_i, x_i), x_i = [a_i; a_{i+1}, ...], y_i = [0; a_{i-1}, a_{i-2}, ...], between Re z = 0 and
      Re z = a_i; the pieces partition the closed geodesic (z -> 1/(conj z - a_i) carries piece i to piece i+1).
      Numerically stable for arbitrarily long words (all quantities O(1)).
Convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]] (B1720's)."""
import itertools, math
import numpy as np

L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1))


def mul(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))


def mat(w):
    M = ((1, 0), (0, 1))
    for ch in w: M = mul(M, L if ch == "L" else R)
    return M


def lyndon(nmax):
    """Duval's algorithm: all Lyndon words over L < R of length <= nmax (primitive necklaces, canonical = least rotation)"""
    out = []; w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        if m <= nmax: out.append("".join("LR"[c] for c in w))
        while len(w) < nmax: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()
    return [x for x in out if "L" in x and "R" in x]


def runs(w):
    """cyclic run lengths, starting at the start of an L-run (even count, alternating L, R)"""
    k = next(i for i in range(len(w)) if w[i] == "L" and w[i - 1] == "R")
    s = w[k:] + w[:k]
    return [len(list(g)) for _, g in itertools.groupby(s)]


def reduce_vec(z):
    z = np.array(z, dtype=complex)
    for _ in range(5000):
        z = z - np.floor(z.real + 0.5)
        m = np.abs(z) < 1 - 1e-13
        if not m.any(): return z
        z[m] = -1 / z[m]
    raise RuntimeError("reduction did not terminate")


def cf_forward(seq, i, K=64):
    n = len(seq); v = float(seq[(i + K) % n])
    for k in range(K - 1, -1, -1): v = seq[(i + k) % n] + 1.0 / v
    return v


def segments_from_runs(a, dens=40.0, K=64, cyclic=True):
    """midpoint samples (z, ds) of the run-segment partition; returns z (unreduced), weights, total length"""
    n = len(a); Z = []; W = []; tot = 0.0
    for i in range(n):
        x = cf_forward(a, i, K)
        yinv = cf_forward([a[(i - 1 - k) % n] for k in range(n)], 0, K)      # [a_{i-1}; a_{i-2}, ...]
        y = 1.0 / yinv
        c, rho = (x - y) / 2, (x + y) / 2
        s0, s1 = math.atanh(-c / rho), math.atanh((a[i] - c) / rho)
        L_ = s1 - s0; tot += L_
        k = max(4, int(math.ceil(dens * L_)))
        s = s0 + (np.arange(k) + 0.5) * (L_ / k)
        Z.append(c + rho * (np.tanh(s) + 1j / np.cosh(s))); W.append(np.full(k, L_ / k))
    return np.concatenate(Z), np.concatenate(W), tot


def axis_samples(M, dens=40.0):
    """the draft's method, re-implemented independently: axis of M from its fixed points"""
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; t = a + d
    assert c != 0 and abs(t) > 2
    sq = math.sqrt(t * t - 4)
    f1, f2 = ((a - d) + sq) / (2 * c), ((a - d) - sq) / (2 * c)
    m, r = (f1 + f2) / 2, abs(f1 - f2) / 2
    ell = 2 * math.acosh(abs(t) / 2)
    k = max(8, int(dens * ell)); s = (np.arange(k) + 0.5) * (ell / k)
    return m + r * (np.tanh(s) + 1j / np.cosh(s)), np.full(k, ell / k), ell


def hyp_tail(Y):
    """P(Im tau > Y) under hyperbolic area on F, Y >= 1"""
    return 3 / (math.pi * Y)
