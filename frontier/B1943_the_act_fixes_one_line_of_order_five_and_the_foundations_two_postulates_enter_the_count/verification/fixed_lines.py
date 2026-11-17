"""B1943: the golden act fixes, up to sign, exactly one non-trivial line, of order 5 (exact).
For an integer matrix A acting on (Q/Z)^2, the points with A v = v (resp. -v) mod 1 are the kernel of A - I (resp. A + I)
on the torus, a group isomorphic to Z/d1 x Z/d2 for the Smith invariants of the matrix when its determinant is non-zero.
Checked here (1) by Smith forms, (2) by enumerating every point of every level N <= 60, for LR and its conjugates,
transposes and inverses; (3) a planted control: a trace-4 act fixes points the golden act does not."""
from fractions import Fraction as F
from math import gcd
L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1))
mul = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
T = lambda A: ((A[0][0], A[1][0]), (A[0][1], A[1][1]))
inv = lambda A: ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))            # det 1


def smith(A):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    d1 = gcd(gcd(a, b), gcd(c, d)); det = abs(a * d - b * c)
    return (d1, det // d1) if d1 else (0, 0)


def fixed_up_to_sign(A, Nmax):
    pts = {}
    for N in range(1, Nmax + 1):
        for i in range(N):
            for j in range(N):
                if gcd(gcd(i, j), N) != 1:
                    continue                                          # exact order N only
                v = (F(i, N), F(j, N)); w = tuple(F(A[r][0]) * v[0] + F(A[r][1]) * v[1] for r in range(2))
                red = lambda x: x - (x.numerator // x.denominator)
                for s in (1, -1):
                    if all(red(w[r] - s * v[r]) == 0 for r in range(2)):
                        pts.setdefault(N, set()).add((v, s))
    return pts


if __name__ == "__main__":
    LR = mul(L, R)
    I2 = ((1, 0), (0, 1)); sub = lambda A, s: tuple(tuple(A[i][j] - s * I2[i][j] for j in range(2)) for i in range(2))
    ok = True
    for name, A in (("LR", LR), ("RL", mul(R, L)), ("(LR)^T", T(LR)), ("(LR)^-1", inv(LR)), ("((LR)^T)^-1", inv(T(LR)))):
        sm, sp = smith(sub(A, 1)), smith(sub(A, -1)); f = fixed_up_to_sign(A, 60)
        orders = sorted(f); n_nontriv = sum(len(v) for N, v in f.items() if N > 1)
        print("%-12s Smith(A - I) = %s, Smith(A + I) = %s; fixed up to sign at levels <= 60: orders %s, %d non-zero points, signs %s"
              % (name, sm, sp, orders, n_nontriv, sorted({s for N, v in f.items() if N > 1 for _, s in v})))
        ok &= sm == (1, 1) and sp == (1, 5) and orders == [1, 5] and n_nontriv == 4 and {s for _, s in f[5]} == {-1}
        # Review 83 (agy-002's R83-20, agy-exp's F-R83-05): every act's own line is printed and held; RL fixes another
        # line than LR, {k(1, 3)/5}, which the old gate `if name == "LR"` had hidden
        pts5 = sorted(tuple(map(str, v)) for v, s in f[5])
        print("   the four points of order 5:", pts5)
        line12 = sorted([("1/5", "2/5"), ("2/5", "4/5"), ("3/5", "1/5"), ("4/5", "3/5")])
        line13 = sorted([("1/5", "3/5"), ("2/5", "1/5"), ("3/5", "4/5"), ("4/5", "2/5")])
        ok &= pts5 == (line13 if name == "RL" else line12)
    C = mul(mul(L, R), R)                                             # trace 4: the planted control
    fc = fixed_up_to_sign(C, 12)
    print("CONTROL LRR (trace 4): Smith(A - I) = %s; fixed points at orders %s -> %s" % (smith(sub(C, 1)), sorted(fc), "CAUGHT" if sorted(fc) != [1, 5] else "MISSED"))
    ok &= sorted(fc) != [1, 5]
    print("ALL HOLD:", ok)
