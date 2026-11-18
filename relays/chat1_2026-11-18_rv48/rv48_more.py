#!/usr/bin/env python3
"""The status page's section 9.2, after its second referee read: two more facts this seat offers main for VERIFIED
records of its that rest on nothing main computed. Data-free, exact. Computed once, post hoc.

    python3 -I -u rv48_more.py

H3  W-C8 part 2a's line 32 (web-wc8p2a-01): b1 = 1 at every level n of the golden tick J = ((1, 1), (1, 0)). By the
    Wang sequence of the mapping torus, b1 = 1 + dim ker(J^n - 1) over Q, so b1 = 1 exactly when det(J^n - 1) != 0.
    det(J^n - 1) = det J^n - tr J^n + 1 = (-1)^n - L_n + 1, L_n the Lucas numbers. Printed for n = 1 to 12, with the
    statement that it is never 0 (|L_n| >= 3 for n >= 2, and n = 1 gives -1). The cusp's rank 1 is by hand: the
    fibre's puncture loop is a commutator, so it is 0 in H1, and the loop of t-degree 1 is not.
H4  W-C1's lines 27 and 28 (web-wc1-01): the image of Riley's pair ((1, 1), (0, 1)), ((1, 0), (-w, 1)) in
    SL(2, Z[w]/N), w^2 = -1 - w, closed under multiplication WITHOUT adding -1: its order, and whether it holds -1, at
    N = 2, 4, 8. Expected (W-C1): 10, 320, 20480, each holding -1.
"""
L = [2, 1]
for n in range(2, 13):
    L.append(L[-1] + L[-2])
dets = [((-1) ** n) - L[n] + 1 for n in range(1, 13)]
print("H3: det(J^n - 1), n = 1 to 12: %s; |.| for n = 1 to 8: %s; never 0: %s"
      % (dets, [abs(d) for d in dets[:8]], all(d != 0 for d in dets)))


def mulr(x, y, N):                 # (a + b w)(c + d w), w^2 = -1 - w
    a, b = x; c, d = y
    return ((a * c - b * d) % N, (a * d + b * c - b * d) % N)


def addr(x, y, N):
    return ((x[0] + y[0]) % N, (x[1] + y[1]) % N)


def mulm(X, Y, N):
    return tuple(tuple(addr(mulr(X[i][0], Y[0][j], N), mulr(X[i][1], Y[1][j], N), N) for j in range(2)) for i in range(2))


for N in (2, 4, 8):
    one, zero = (1, 0), (0, 0)
    A = ((one, one), (zero, one))
    B = ((one, zero), (((0, -1)[0] % N, (-1) % N), one))       # -w = 0 + (-1) w
    I = ((one, zero), (zero, one)); mI = ((((-1) % N, 0), zero), (zero, ((-1) % N, 0)))
    seen = {I}; frontier = [I]
    while frontier:
        nxt = []
        for X in frontier:
            for g in (A, B):
                Y = mulm(X, g, N)
                if Y not in seen:
                    seen.add(Y); nxt.append(Y)
        frontier = nxt
    print("H4: N = %d: the closure has %d elements; it holds -1: %s" % (N, len(seen), mI in seen))
