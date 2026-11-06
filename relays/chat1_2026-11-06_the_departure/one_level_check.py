"""The web seat, 2026-11-06: ONE PROCESS, ONE LEVEL (PREREGISTRATION_ONE_LEVEL.md). Data-free: SL(2, Z/N) arithmetic
only. No scale ratio, coupling value or held-out quantity is computed (P-719, P-721, P-722's firewall).

For N in (2, 3, 4, 5, 15): the golden monodromy LR's twisted fixed points ((LR + I) v = 0 mod N, nonzero) and
untwisted ones; whether the level-5 pair embeds at N = 15; the order of LR in PSL(2, Z/N); the minimal single run
invisible to the level-N rung (L^(n-1) = +-I mod N) and its apex Im (N + sqrt5)/2; and |PSL(2, Z/N)| for N <= 5.

    python3 one_level_check.py
"""
import itertools
import math

L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))


def mul(A, B, N=None):
    C = ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
         (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
    return tuple(tuple(x % N for x in r) for r in C) if N else C


LR = mul(L, R)
I2 = ((1, 0), (0, 1))


def red(A, N):
    return tuple(tuple(x % N for x in r) for r in A)


def is_pm_identity(A, N):
    return red(A, N) == red(I2, N) or red(A, N) == red(((-1, 0), (0, -1)), N)


def fixed(N, sign):
    out = []
    for a, b in itertools.product(range(N), repeat=2):
        if (a, b) == (0, 0):
            continue
        u = ((a * LR[0][0] + b * LR[1][0]) % N, (a * LR[0][1] + b * LR[1][1]) % N)  # the row vector times LR
        if u == ((sign * a) % N, (sign * b) % N):
            out.append((a, b))
    return out


def order_psl(A, N):
    P = red(A, N)
    for k in range(1, 400):
        if is_pm_identity(P, N):
            return k
        P = mul(P, A, N)
    return None


def psl_order(N):
    sl = sum(1 for a, b, c, d in itertools.product(range(N), repeat=4) if (a * d - b * c) % N == 1)
    return sl // (2 if N > 2 else 1)


if __name__ == "__main__":
    print("ONE PROCESS, ONE LEVEL -- data-free check (the web seat, 2026-11-06)")
    pair5 = fixed(5, -1)
    for N in (2, 3, 4, 5, 15):
        tw, un = fixed(N, -1), fixed(N, +1)
        n = next(m for m in range(2, 100) if is_pm_identity(tuple(tuple(x for x in r) for r in
                                                                   [[1, 0], [(m - 1) % N, 1]]), N))
        print("  N = %2d: twisted fixed points %d %s; untwisted %d; order of LR in PSL(2, Z/N) %s; minimal invisible run "
              "n = %d (apex Im %.6f)" % (N, len(tw), tw if len(tw) <= 8 else "", len(un), order_psl(LR, N), n,
                                         (N + math.sqrt(5)) / 2))
    emb = sorted(((3 * a) % 15, (3 * b) % 15) for a, b in pair5)
    print("  the level-5 pair %s embedded at N = 15 by v -> 3v: %s; equal to the level-15 twisted fixed points: %s" % (
        pair5, emb, emb == sorted(fixed(15, -1))))
    print("  |PSL(2, Z/N)| for N = 2, 3, 4, 5: %s (the (2, 3, N) triangle groups: 6, 12, 24, 60)" % [psl_order(N) for N in (2, 3, 4, 5)])
    print("one_level_check exit 0")
