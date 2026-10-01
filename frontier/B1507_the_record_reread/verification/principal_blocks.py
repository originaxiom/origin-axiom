"""B1507 -- the record's other three: h^1(m004; 27) = 3 under the principal sl2, one class per block 27 = V17 + V9 + V1 (B632, B656,
B657, B662), the three that B714/B715's item 6' says no symmetry or Hecke correspondence can cycle (the blocks have different
dimensions).  Own code: h^1(m004; Sym^k) for k = 16, 8, 0 over F_p, p = 1 mod 3 (omega in F_p), three primes, exact linear algebra.
m004 = <a, b | w a = b w>, w = a^-1 b a b^-1, holonomy a -> [[1,1],[0,1]], b -> [[1,0],[-omega,1]] (Riley)."""
from math import comb


def _mul(A, B, p):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) % p for j in range(len(B[0]))] for i in range(len(A))]


def _inv2(M, p):
    (a, b), (c, d) = M
    di = pow((a * d - b * c) % p, p - 2, p)
    return [[d * di % p, -b * di % p], [-c * di % p, a * di % p]]


def _sym(M, n, p):
    (a, b), (c, d) = M

    def pw(u, v, e):
        return [comb(e, j) * pow(u, e - j, p) * pow(v, j, p) % p for j in range(e + 1)]
    R = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        px, py = pw(a, c, n - i), pw(b, d, i)
        prod = [0] * (n + 1)
        for s, cs in enumerate(px):
            for t, ct in enumerate(py):
                prod[s + t] = (prod[s + t] + cs * ct) % p
        for j in range(n + 1):
            R[j][i] = prod[j]
    return R


def _rank(M, p):
    M = [r[:] for r in M]; r = 0
    for c in range(len(M[0]) if M else 0):
        piv = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r


def h1(p, n):
    omega = next(x for x in range(2, p) if (x * x + x + 1) % p == 0)
    A = [[1, 1], [0, 1]]; B = [[1, 0], [(-omega) % p, 1]]
    Ai, Bi = _inv2(A, p), _inv2(B, p)
    W = _mul(_mul(Ai, B, p), _mul(A, Bi, p), p)
    assert _mul(W, A, p) == _mul(B, W, p), "not a representation"
    d = n + 1
    rho = {'a': _sym(A, n, p), 'b': _sym(B, n, p), 'A': _sym(Ai, n, p), 'B': _sym(Bi, n, p)}
    I = [[int(i == j) for j in range(d)] for i in range(d)]
    word = list("AbaB") + ["a"] + list("bABa") + ["B"]          # w a w^-1 b^-1
    P = I
    for L in word:
        P = _mul(P, rho[L], p)
    assert P == I, "relator not trivial"
    Da = [[0] * d for _ in range(d)]; Db = [[0] * d for _ in range(d)]
    prefix = I
    for L in word:
        if L in "aA":
            T = prefix if L == 'a' else _mul(prefix, rho['A'], p)
            s = 1 if L == 'a' else -1
            Da = [[(x + s * y) % p for x, y in zip(r1, r2)] for r1, r2 in zip(Da, T)]
        else:
            T = prefix if L == 'b' else _mul(prefix, rho['B'], p)
            s = 1 if L == 'b' else -1
            Db = [[(x + s * y) % p for x, y in zip(r1, r2)] for r1, r2 in zip(Db, T)]
        prefix = _mul(prefix, rho[L], p)
    dimZ = 2 * d - _rank([ra + rb for ra, rb in zip(Da, Db)], p)
    Bm = [[(rho['a'][i][j] - I[i][j]) % p for j in range(d)] for i in range(d)] + \
         [[(rho['b'][i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    return dimZ - _rank(Bm, p)


PRIMES = (601, 1201, 1801)
BLOCKS = (16, 8, 0)


def main():
    return {p: {f"V{n + 1}": h1(p, n) for n in BLOCKS} for p in PRIMES}


if __name__ == "__main__":
    for p, row in main().items():
        print(f"p = {p}: h^1(m004; V) = {row}  (sum {sum(row.values())})")
