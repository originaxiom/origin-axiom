#!/usr/bin/env python3
"""W-P1, step 3 (W-P1c): the clock and the heights. Data-free; no frame is read.

    python3 -I wp1c_heights.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, step 3 (committed before this script).

A word is a positive word in L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]] with both letters. Its thread is the closed
geodesic of its matrix on the modular surface; height is Im tau after reduction to SL(2, Z)'s standard fundamental
domain; time is hyperbolic arc length.

One period is cut into one piece per letter. For the word A_0 ... A_{n-1} and its rotations M_k = A_k ... A_{k-1}, each
axis has its endpoints on either side of 0 (positive words), so it crosses the imaginary axis at q_k. On M_k's axis the
points q_k, A_k q_{k+1}, ..., M_k q_k follow in order and span one period; the piece of letter k is the arc from q_k
to A_k q_{k+1}. Each piece is sampled uniformly in arc length (at least DENS points per unit length, and 8 per piece),
and each sample is reduced to the fundamental domain. Endpoints are computed with 60-digit arithmetic.

  H0  controls: LR's top is sqrt(5)/2 and no time lies above it; L^n R's top is sqrt((n + 2)^2 - 4)/2; the pieces of
      every word sum to its translation length 2 arccosh(tr/2); no thread rises above a/2 + 1, where a is its longest
      cyclic run of one letter;
  H1  (a), the move count: N_WORDS uniform random words of n letters (n = 20, 40, 80; seeds 1, 2, 3), each thread
      weighted by its length (W-F24's measure); the pooled share of time above heights 1.118, 2, 4 and 6;
  H2  (b), the length: every primitive cyclic word (a Lyndon word in L < R) with both letters and trace at most X, for
      X = 100, 200 and 400, each counted once; the pooled share above the same heights, beside 3/(pi y);
  H3  which words carry it: under (a) at n = 40 and under (b) at X = 400, the time above each height, by the word's
      longest cyclic run a (bins 1, 2, 3, 4-5, 6-9, 10 and more), as shares of all time above that height.
"""
import math

import mpmath as mp
import numpy as np

mp.mp.dps = 60
HEIGHTS = (math.sqrt(5) / 2 + 1e-9, 2.0, 4.0, 6.0)
HNAMES = ("1.118", "2", "4", "6")
DENS = 120
N_WORDS = 2000
L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def mat(word):
    M = ((1, 0), (0, 1))
    for ch in word:
        M = mul(M, L if ch == "L" else R)
    return M


def ends(M):
    """the repelling and attracting fixed points (y < 0 < x) of a positive hyperbolic matrix, to 60 digits"""
    (a, b), (c, d) = M
    t = a + d
    s = mp.sqrt(mp.mpf(t) ** 2 - 4)
    r1, r2 = (mp.mpf(a - d) + s) / (2 * c), (mp.mpf(a - d) - s) / (2 * c)
    return min(r1, r2), max(r1, r2)


def apply(A, z):
    (a, b), (c, d) = A
    return (a * z + b) / (c * z + d)


def s_of(z, y, x):
    """arc-length coordinate of a point z on the geodesic with endpoints y < x: s = log tan(theta/2)"""
    c0, r = (x + y) / 2, (x - y) / 2
    th = mp.atan2(mp.im(z), mp.re(z) - c0)
    return mp.log(mp.tan(th / 2)), c0, r


def reduce_heights(zr, zi):
    """Im tau after reduction to the standard fundamental domain (vectorised)"""
    x, y = zr.copy(), zi.copy()
    for _ in range(200):
        x = x - np.round(x)
        m = x * x + y * y < 1 - 1e-13
        if not m.any():
            break
        d = x[m] * x[m] + y[m] * y[m]
        x[m], y[m] = -x[m] / d, y[m] / d
    return y


def inv(A):
    (a, b), (c, d) = A
    return ((d, -b), (-c, a))


def thread(word):
    """samples (heights, weights) along one period of the word's closed geodesic, and the checks"""
    n = len(word)
    Ms = [mat(word)]
    for k in range(n - 1):                      # M_{k+1} = A_k^-1 M_k A_k
        A = L if word[k] == "L" else R
        Ms.append(mul(mul(inv(A), Ms[-1]), A))
    E = [ends(M) for M in Ms]
    q = [mp.mpc(0, mp.sqrt(-y * x)) for (y, x) in E]
    hs, ws, total = [], [], mp.mpf(0)
    for k in range(n):
        y, x = E[k]
        A = L if word[k] == "L" else R
        p1, p2 = q[k], apply(A, q[(k + 1) % n])
        s1, c0, r = s_of(p1, y, x)
        s2, _, _ = s_of(p2, y, x)
        ln = s1 - s2                            # towards the attracting end x, s decreases
        assert ln > -mp.mpf(10) ** -40, ("piece order", word, k)
        total += ln
        m = max(8, int(float(ln) * DENS) + 1)
        s = float(s2) + (np.arange(m) + 0.5) / m * float(ln)
        th = 2 * np.arctan(np.exp(s))
        zr, zi = float(c0) + float(r) * np.cos(th), float(r) * np.sin(th)
        hs.append(reduce_heights(zr, zi))
        ws.append(np.full(m, float(ln) / m))
    t = Ms[0][0][0] + Ms[0][1][1]
    ell = 2 * mp.acosh(mp.mpf(t) / 2)
    return np.concatenate(hs), np.concatenate(ws), float(total), float(ell)


def longest_run(word):
    w = word + word
    best = run = 1
    for i in range(1, len(w)):
        run = run + 1 if w[i] == w[i - 1] else 1
        best = max(best, min(run, len(word)))
    return best


def bin_of(a):
    return "1" if a == 1 else "2" if a == 2 else "3" if a == 3 else "4-5" if a <= 5 else "6-9" if a <= 9 else "10+"


BINS = ("1", "2", "3", "4-5", "6-9", "10+")


def pooled(words, carry=False):
    tot = 0.0
    above = np.zeros(len(HEIGHTS))
    by = {b: np.zeros(len(HEIGHTS)) for b in BINS}
    worst_len, worst_top = 0.0, 0.0
    for w in words:
        h, wt, total, ell = thread(w)
        worst_len = max(worst_len, abs(total - ell))
        a = longest_run(w)
        worst_top = max(worst_top, float(h.max()) - (a / 2 + 1))
        tot += wt.sum()
        for j, H in enumerate(HEIGHTS):
            v = wt[h > H].sum()
            above[j] += v
            if carry:
                by[bin_of(a)][j] += v
    return above / tot, by, above, worst_len, worst_top


def lyndon_words(X):
    """primitive cyclic words (Lyndon words, L < R) with both letters and trace at most X"""
    out = []

    def dfs(w, M):
        if len(set(w)) == 2:
            t = M[0][0] + M[1][1]
            if t > X:
                return
            if is_lyndon(w):
                out.append(w)
        elif len(w) + 2 > X:
            return
        for ch in "LR":
            dfs(w + ch, mul(M, L if ch == "L" else R))

    dfs("", ((1, 0), (0, 1)))
    return out


def is_lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w)))


# H0: controls
h, wt, total, ell = thread("LR")
print("H0: LR: top %.12f (sqrt 5/2 = %.12f); time above 1.118: %.3g; pieces %.12f, translation length %.12f" %
      (h.max(), math.sqrt(5) / 2, wt[h > HEIGHTS[0]].sum(), total, ell))
for n in (2, 3, 5, 8):
    h, wt, total, ell = thread("L" * n + "R")
    print("H0: L^%d R: top %.6f (expected %.6f); pieces %.9f against %.9f" %
          (n, h.max(), math.sqrt((n + 2) ** 2 - 4) / 2, total, ell))

# H1: the move count
rows1 = {}
for n, seed in ((20, 1), (40, 2), (80, 3)):
    rng = np.random.default_rng(seed)
    words = []
    while len(words) < N_WORDS:
        w = "".join(rng.choice(["L", "R"], size=n))
        if len(set(w)) == 2:
            words.append(w)
    share, by, above, wl, wtop = pooled(words, carry=(n == 40))
    rows1[n] = (share, by, above)
    print("H1 (a) n = %d, %d words: share above %s: %s; worst |pieces - length| %.2g; worst top - (a/2 + 1) %.3g" %
          (n, N_WORDS, "/".join(HNAMES), ["%.5f" % v for v in share], wl, wtop))

# H2: the length
for X in (100, 200, 400):
    words = lyndon_words(X)
    share, by, above, wl, wtop = pooled(words, carry=(X == 400))
    if X == 400:
        rows2 = (share, by, above)
    print("H2 (b) X = %d, %d primitive classes: share above %s: %s; 3/(pi y): %s; worst |pieces - length| %.2g; "
          "worst top - (a/2 + 1) %.3g" % (X, len(words), "/".join(HNAMES), ["%.5f" % v for v in share],
                                          ["%.5f" % (3 / (math.pi * H)) for H in HEIGHTS], wl, wtop))

# H3: which words carry it
for lab, (share, by, above) in (("(a) n = 40", rows1[40]), ("(b) X = 400", rows2)):
    for j, H in enumerate(HNAMES):
        tot = above[j]
        parts = ["%s: %.3f" % (b, by[b][j] / tot) for b in BINS] if tot > 0 else ["no time above"]
        print("H3 %s, above %s, by the longest run a: %s" % (lab, H, ", ".join(parts)))
