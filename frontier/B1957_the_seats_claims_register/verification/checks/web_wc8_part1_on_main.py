"""B1957: the web seat's W-C8 part 1 (the tick-parity law; the metallic ticks' marks), on main's own code.  Data-free.
J_m = [[m, 1], [1, 0]], A_m = J_m^2, K = [[0, 1], [-1, 0]], N = m^2 + 4.
 P1  the normaliser of <A_m> in GL(2, Z), searched with entries to 12 at m = 1 and to 30 at m = 1 to 5: every element
     found is +-J^n K^e times a power of A, eight classes modulo <A>; J^2 = A, K^2 = -1, K J K^-1 = -J^-1.
 P2  at the mark (the line of (m, 2) mod N, odd m): J acts by lam = m/2 mod N with lam^2 = -1, K by -lam; the hand of
     +-J^n K^e is (-1)^(n+e); the control (-1)^n fails.
 P3  the Smith form of A_m + 1 is diag(gcd(m, 2), N/gcd(m, 2)), m = 1 to 12; a line of order N sent to its opposite
     exists exactly for odd m (by enumeration of the kernel mod N)."""
import functools
from math import gcd
import numpy as np
print = functools.partial(print, flush=True)


def search(m, box):
    """elements X of GL(2, Z) with entries in [-box, box] and X A = A X or X A = A^-1 X"""
    A = np.array([[m * m + 1, m], [m, 1]], dtype=np.int64); Ai = np.array([[1, -m], [-m, m * m + 1]], dtype=np.int64)
    r = np.arange(-box, box + 1, dtype=np.int64); a, b, c, d = np.meshgrid(r, r, r, r, indexing="ij", sparse=True); det = a * d - b * c
    def commutes_to(T):
        # X A - T X = 0 entrywise
        e11 = a * A[0, 0] + b * A[1, 0] - (T[0, 0] * a + T[0, 1] * c); e12 = a * A[0, 1] + b * A[1, 1] - (T[0, 0] * b + T[0, 1] * d)
        e21 = c * A[0, 0] + d * A[1, 0] - (T[1, 0] * a + T[1, 1] * c); e22 = c * A[0, 1] + d * A[1, 1] - (T[1, 0] * b + T[1, 1] * d)
        return (e11 == 0) & (e12 == 0) & (e21 == 0) & (e22 == 0)
    ok = (np.abs(det) == 1) & (commutes_to(A) | commutes_to(Ai)); idx = np.argwhere(ok)
    return [tuple(int(r[i]) for i in row) for row in idx]


def classes(found, m):
    """each found element written as s J^n K^e (n from -40 to 40); its class modulo <A> = <J^2> is (s, n mod 2, e).
    Returns the set of classes and whether every element was of that form."""
    Jm = np.array([[m, 1], [1, 0]], dtype=object); Ji = np.array([[0, 1], [1, -m]], dtype=object); K = np.array([[0, 1], [-1, 0]], dtype=object); table = {}
    P = np.eye(2, dtype=object); Q = np.eye(2, dtype=object)
    for n in range(0, 41):
        for e in (0, 1):
            for sg in (1, -1):
                for nn, X in ((n, P), (-n, Q)):
                    Y = sg * (X.dot(K) if e else X); table.setdefault(tuple(int(v) for v in Y.ravel()), (sg, nn % 2, e))
        P = P.dot(Jm); Q = Q.dot(Ji)
    cls = set(); allform = True
    for x in found:
        if x in table: cls.add(table[x])
        else: allform = False
    return cls, allform


if __name__ == "__main__":
    J = np.array([[1, 1], [1, 0]], dtype=object); K = np.array([[0, 1], [-1, 0]], dtype=object); LR = np.array([[2, 1], [1, 1]], dtype=object)
    f12 = search(1, 12); cl, form = classes(f12, 1)
    print("P1: m = 1, entries to 12: %d elements of the normaliser; every one is +-J^n K^e: %s; classes modulo <LR>: %d; J^2 = LR: %s; K^2 = -1: %s; K J K^-1 = -J^-1: %s" % (
        len(f12), form, len(cl), (J.dot(J) == LR).all(), (K.dot(K) == -np.eye(2, dtype=object)).all(), (K.dot(J).dot(-K) == -np.array([[0, 1], [1, -1]], dtype=object)).all()))
    for m in range(1, 6):
        f = search(m, 30); cm, form = classes(f, m)
        print("P1: m = %d, entries to 30: %d elements; every one is +-J_m^n K^e: %s; classes modulo <A_m>: %d" % (m, len(f), form, len(cm)))
    rows = []
    for m in range(1, 13):
        N = m * m + 4; Ap = [[m * m + 2, m], [m, 2]]; d1 = gcd(gcd(Ap[0][0], Ap[0][1]), gcd(Ap[1][0], Ap[1][1])); smith = (d1, (Ap[0][0] * Ap[1][1] - Ap[0][1] * Ap[1][0]) // d1)
        ker = [(x, y) for x in range(N) for y in range(N) if (Ap[0][0] * x + Ap[0][1] * y) % N == 0 and (Ap[1][0] * x + Ap[1][1] * y) % N == 0]
        order = lambda v: next(k for k in range(1, N + 1) if (k * v[0]) % N == 0 and (k * v[1]) % N == 0); mark = any(order(v) == N for v in ker)
        lam = None
        if m % 2:
            lam = (m * pow(2, -1, N)) % N; v = (m % N, 2); Jv = ((m * v[0] + v[1]) % N, v[0] % N); Kv = (v[1] % N, (-v[0]) % N)
            assert Jv == ((lam * v[0]) % N, (lam * v[1]) % N) and Kv == ((-lam * v[0]) % N, (-lam * v[1]) % N) and (lam * lam + 1) % N == 0 and lam not in (1, N - 1)
        rows.append((m, N, smith, mark, lam))
    print("P3: m: (N, Smith form of A + 1, a line of order N sent to its opposite, J's scalar): %s" % {r[0]: r[1:] for r in rows})
    print("P3: the Smith form is diag(gcd(m, 2), N/gcd(m, 2)) and a mark exists exactly for odd m: %s; for odd m, J acts on (m, 2) by lam = m/2 with lam^2 = -1, K by -lam (asserted above)" % all(r[2] == (gcd(r[0], 2), r[1] // gcd(r[0], 2)) and r[3] == (r[0] % 2 == 1) for r in rows))
    N = 5; lam = 3; hand = lambda n, e: (pow(lam, n, N) * pow(-lam, e, N)) % N not in (1, N - 1)      # +-J^n K^e acts on the mark by +-lam^n (-lam)^e
    print("P2: m = 1: J acts on the line of (1, 2) mod 5 by 3 and K by 2 (= -3); the hand of +-J^n K^e is (n + e) mod 2 for n, e in {0, 1}: %s; the control (n mod 2 alone): %s" % (all(hand(n, e) == ((n + e) % 2 == 1) for n in (0, 1) for e in (0, 1)), all(hand(n, e) == (n % 2 == 1) for n in (0, 1) for e in (0, 1))))
