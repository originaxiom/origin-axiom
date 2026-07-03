"""B372 — the CRT/F_p Weil engine (toolbox row 6 applied to the seam pipeline).

All matrix arithmetic lives in F_p for primes p ≡ 1 (mod 4N·k_emb...); zeta_{4N} is realized
as a power of a primitive root. A readout trace t is identified EXACTLY in the declared
subfield basis B by solving t^{(k)} = sum_i x_i b_i^{(k)} across |B| Galois embeddings
(z -> z^k), CRT-ing the solution across primes, rational-reconstructing, and then VERIFYING
at held-out extra embeddings (a mismatch = "outside the declared span", reported, never
forced). The banked level-15 flagship is the hard conventions gate.
"""
import json
import os
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------- primes and roots ----------------
def _is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_1_mod(m, count, start=10**9):
    out, k = [], (start // m) + 1
    while len(out) < count:
        p = m * k + 1
        if _is_prime(p):
            out.append(p)
        k += 1
    return out


def primitive_root(p):
    fac, n = [], p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
        g += 1


# ---------------- the Weil pipeline mod p, at level N, embedding z -> z^k ----------------
class Level:
    def __init__(self, N, p, zk):
        """zk = zeta_{4N} in F_p for THIS embedding (already the k-th power)."""
        self.N, self.p = N, p
        self.z = zk                              # zeta_{4N}
        self.zN = pow(zk, 4, p)                  # zeta_N
        n = N
        self.D = [[pow(self.zN, (j * (j - 1) // 2) % N, p) if i == j else 0
                   for j in range(n)] for i in range(n)]
        self.Di = [[pow(self.zN, (-(j * (j - 1) // 2)) % N, p) if i == j else 0
                    for j in range(n)] for i in range(n)]
        F = [[pow(self.zN, (i * j) % N, p) for j in range(n)] for i in range(n)]
        inv15 = pow(N, p - 2, p)
        Fi = [[pow(self.zN, (-i * j) % N, p) * inv15 % p for j in range(n)] for i in range(n)]
        self.WR = self.mmul(self.mmul(F, self.Di), Fi)

    def mmul(self, A, B):
        n, p = self.N, self.p
        Bt = list(zip(*B))
        return [[sum(a * b for a, b in zip(row, col)) % p for col in Bt] for row in A]

    def W(self, m):
        P = self.WR
        for _ in range(m - 1):
            P = self.mmul(P, self.WR)
        Dm = [[pow(self.zN, (m * (j * (j - 1) // 2)) % self.N, self.p) if i == j else 0
               for j in range(self.N)] for i in range(self.N)]
        return self.mmul(P, Dm)

    def order_powers(self, M, cap=400):
        n = self.N
        ident = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        powers, P = [ident], M
        for k in range(1, cap + 1):
            if P == ident:
                return k, powers
            powers.append(P)
            P = self.mmul(P, M)
        raise RuntimeError("order cap")

    def par_trace(self, A, B):
        n, p = self.N, self.p
        return sum(A[(-x) % n][y] * B[y][x] for x in range(n) for y in range(n)) % p

    def pair_cell_table(self, pow1, pow2):
        """C[j][l] = tr(Par W1^j W2^l) for the DFT."""
        return [[self.par_trace(pow1[j], pow2[l]) for l in range(len(pow2))]
                for j in range(len(pow1))]

    def dft_cell(self, C, o1, o2, a, b):
        p = self.p
        z1 = pow(self.z, (4 * self.N) // o1, p)   # zeta_{o1}
        z2 = pow(self.z, (4 * self.N) // o2, p)
        t = 0
        for j in range(o1):
            w1 = pow(z1, (-j * a) % o1, p)
            for l in range(o2):
                t += w1 * pow(z2, (-l * b) % o2, p) * C[j][l]
        return t * pow(o1 * o2, p - 2, p) % p

    def single_cell(self, powers, a):
        p, o = self.p, len(powers)
        zo = pow(self.z, (4 * self.N) // o, p)
        tr = [sum(P[(-x) % self.N][x] for x in range(self.N)) % p for P in powers]
        t = sum(pow(zo, (-j * a) % o, p) * tr[j] for j in range(o)) % p
        return t * pow(o, p - 2, p) % p


# ---------------- the declared basis, per embedding ----------------
def basis_elements(N, p, zk):
    """Values in F_p of the declared basis at this embedding."""
    z4N = zk
    zN = pow(z4N, 4, p)
    if N == 15:
        z3, z5 = pow(zN, 5, p), pow(zN, 3, p)
    else:                                        # N = 45
        z3, z5 = pow(zN, 15, p), pow(zN, 9, p)
    s5 = (pow(z5, 1, p) - pow(z5, 2, p) - pow(z5, 3, p) + pow(z5, 4, p)) % p   # sqrt5
    sm3 = (z3 - pow(z3, 2, p)) % p                                             # sqrt(-3)
    sm15 = s5 * sm3 % p
    base = [1, s5, sm3, sm15]
    if N == 15:
        return base
    z9 = pow(zN, 5, p)                           # zeta_9 (N=45)
    c1 = (z9 + pow(z9, 8, p)) % p
    c2 = (pow(z9, 2, p) + pow(z9, 7, p)) % p
    out = []
    for c in (1, c1, c2):
        for b in base:
            out.append(c * b % p)
    return out


# ---------------- exact identification across embeddings + primes ----------------
def _solve_mod(A, y, p):
    """Solve square system A x = y mod p (Gaussian elimination)."""
    n = len(A)
    M = [row[:] + [y[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] % p)
        M[c], M[piv] = M[piv], M[c]
        inv = pow(M[c][c], p - 2, p)
        M[c] = [v * inv % p for v in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [(M[r][j] - f * M[c][j]) % p for j in range(n + 1)]
    return [M[i][n] for i in range(n)]


def rational_reconstruct(r, M):
    """r mod M -> Fraction with |num|, den <= sqrt(M/2), or None."""
    a, b = M, r % M
    p0, p1 = 0, 1
    bound = isqrt(M // 2)
    while b > bound:
        q = a // b
        a, b = b, a - q * b
        p0, p1 = p1, p0 - q * p1
    den = abs(p1)
    num = b if p1 > 0 else -b
    if den == 0 or den > bound or gcd(num, den) != 1 and gcd(abs(num), den) != 1:
        return None
    if (num - r * den) % M != 0:
        return None
    return Fr(num, den)


def identify(N, primes, cell_fn, embeddings, extra=2):
    """cell_fn(level_obj) -> trace in F_p. Solve in the declared basis; verify held-out."""
    nb = None
    sols = []
    for p in primes:
        g = primitive_root(p)
        z0 = pow(g, (p - 1) // (4 * N), p)
        rows, ys = [], []
        embs = [k for k in embeddings]
        for k in embs:
            zk = pow(z0, k, p)
            B = basis_elements(N, p, zk)
            nb = len(B)
            rows.append(B)
            ys.append(cell_fn(Level(N, p, zk)))
        x = _solve_mod([r[:nb] for r in rows[:nb]], ys[:nb], p)
        # held-out verification at this prime
        for k, row, y in zip(embs[nb:], rows[nb:], ys[nb:]):
            if sum(xi * bi for xi, bi in zip(x, row)) % p != y:
                return None, "outside-declared-span"
        sols.append((p, x))
    # CRT + rational reconstruction per coordinate
    M = 1
    for p, _ in sols:
        M *= p
    out = []
    for i in range(nb):
        r = 0
        for p, x in sols:
            Mi = M // p
            r = (r + x[i] * Mi * pow(Mi, p - 2, p)) % M
        f = rational_reconstruct(r, M)
        if f is None:
            return None, "reconstruction-failed"
        out.append(f)
    return out, "ok"
