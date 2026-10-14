"""Audit check: chat1's float Lagrange value against an exact computation (periodic continued fractions solved as
quadratic irrationals, evaluated at 50 digits), on every thread to length 12 and 300 random threads of length 13-18."""
import json, random, sys
import mpmath as mp
mp.mp.dps = 50
thr = json.loads(open(sys.argv[1]).read())
def runs(w):
    k = 0
    while w[k] == w[k - 1]: k += 1
    u = w[k:] + w[:k]; rl, cur, n = [], u[0], 0
    for ch in u:
        if ch == cur: n += 1
        else: rl.append(n); cur, n = ch, 1
    rl.append(n); return rl
def cf(seq):
    x = 0.0
    for a in reversed(seq[1:]): x = 1.0 / (a + x)
    return seq[0] + x
def lag_float(w):
    a = runs(w); n = len(a); rep = 60 // n + 4
    return max(cf([a[(i + j) % n] for j in range(n * rep)]) + 1.0 / cf([a[(i - 1 - j) % n] for j in range(n * rep)]) for i in range(n))
def purely_periodic(period):
    # x = [p0; p1, ..., p_{k-1}, x]  ->  x = (P x + P') / (Q x + Q') ; solve Q x^2 + (Q' - P) x - P' = 0, x > 1
    h0, h1, k0, k1 = 1, 0, 0, 1   # convergent recursion
    for a in period:
        h0, h1 = a * h0 + h1, h0
        k0, k1 = a * k0 + k1, k0
    P, Pp, Q, Qp = h0, h1, k0, k1
    A, B, C = Q, Qp - P, -Pp
    return (-B + mp.sqrt(B * B - 4 * A * C)) / (2 * A)
def lag_exact(w):
    a = runs(w); n = len(a); best = mp.mpf(0)
    for i in range(n):
        fwd = [a[(i + j) % n] for j in range(n)]
        bwd = [a[(i - 1 - j) % n] for j in range(n)]
        best = max(best, purely_periodic(fwd) + 1 / purely_periodic(bwd))
    return best
ws = [w for w in thr if len(w) <= 12]
random.seed(1); ws += random.sample([w for w in thr if len(w) > 12], 300)
worst = max(abs(lag_float(w) - lag_exact(w)) for w in ws)
print(len(ws), "threads; worst |float - exact| =", mp.nstr(worst, 5))
