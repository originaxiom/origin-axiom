"""B1856, corrected (B1862; the advisor seat's audit, finding E3, reproduced on main; data-free, exact).

The arc equated "invisible to every state" with the charge premise E = +-I mod 5. In the level-5 Weil representation
rho(-I) is the parity operator: it sends the basis vector e_x to e_{-x}, so it is +1 on the even sector (dimension 3)
and -1 on the odd sector (dimension 2). It is a scalar on each sector and not on C^5. So:
  E = +I   is invisible to every state;
  E = -I   is invisible on a state of definite parity only, i.e. under a parity superselection rule.
This script checks the parity operator exactly (integers and roots of unity as exponents mod 5) and splits B1853's
rung-invisible defects by the sign. Definitions as in B1853's explore_facts.py. Prints integers only."""
import itertools

P = 5


def mul(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))


def inv(A):
    return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))


def pw(A, n):
    X = ((1, 0), (0, 1))
    for _ in range(n):
        X = mul(X, A)
    return X


def mod(A, n):
    return tuple(tuple(x % n for x in r) for r in A)


L, R, I = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
MINUS = ((-1, 0), (0, -1))


def D(runs):
    M = I
    for i, r in enumerate(runs):
        M = mul(M, pw(L if i % 2 == 0 else R, r))
    return M


def E(runs):
    return mul(D(runs), inv(D([1] * len(runs))))


def R1():
    for m in range(1, 9):
        top = 6 if m <= 6 else 3
        for r in itertools.product(range(1, top + 1), repeat=m):
            if r[0] >= 2 and r[-1] >= 2:
                yield r


def parity_operator():
    """rho(S)^2 for the DFT rho(S)[x][y] = w^(s x y)/sqrt(5): (rho(S)^2)[x][z] = (1/5) sum_y w^(s y (x + z)), which is 1
    when x + z = 0 mod 5 and 0 otherwise, for either sign s. Returned as an exact 0/1 matrix, computed by the sum over
    exponents: the sum of w^(k y) over y is 5 when k = 0 mod 5 and 0 otherwise."""
    return [[1 if (x + z) % P == 0 else 0 for z in range(P)] for x in range(P)]


def split():
    plus, minus, total = [], [], 0
    for r in R1():
        total += 1
        e = mod(E(r), P)
        if e == mod(I, P):
            plus.append(r)
        elif e == mod(MINUS, P):
            minus.append(r)
    return total, plus, minus


def check_against_the_representation():
    """rho(S)^2, computed numerically from the DFT of either sign, is the 0/1 matrix above (S^2 = -I in SL(2, F5))."""
    import cmath
    import math
    worst = 0.0
    for sign in (-1, 1):
        RS = [[cmath.exp(2j * math.pi * sign * x * y / P) / math.sqrt(P) for y in range(P)] for x in range(P)]
        sq = [[sum(RS[x][y] * RS[y][z] for y in range(P)) for z in range(P)] for x in range(P)]
        Par = parity_operator()
        worst = max(worst, max(abs(sq[x][z] - Par[x][z]) for x in range(P) for z in range(P)))
    return worst


if __name__ == "__main__":
    Par = parity_operator()
    assert check_against_the_representation() < 1e-12
    # S^2 = -I in SL(2, F5), so rho(-I) is rho(S)^2 up to a phase: the map e_x -> e_{-x}
    fixed = sum(1 for x in range(P) if (-x) % P == x)
    dim_even = (P + fixed) // 2
    dim_odd = (P - fixed) // 2
    is_identity = all(Par[x][z] == (1 if x == z else 0) for x in range(P) for z in range(P))
    print("the parity operator rho(-I): e_x -> e_(-x); +1 on the even sector (dimension %d), -1 on the odd sector (dimension %d)" % (dim_even, dim_odd))
    print("rho(-I) is a scalar on C^5: %s" % is_identity)
    total, plus, minus = split()
    print("R1: %d defects; rung-invisible (E = +-I mod 5): %d = %d with E = +I and %d with E = -I" % (total, len(plus) + len(minus), len(plus), len(minus)))
    print("the run of 6 has E = +I mod 5: %s" % ((6,) in plus))
    print("the shortest defects with E = -I mod 5: %s" % sorted(minus, key=lambda r: (len(r), sum(r)))[:4])
