#!/usr/bin/env python3
"""THE THETA-ODD FRAME AND THE OBJECT'S INVERSION: an isometry of m004 pairs every E_6 holonomy near the geometric point
with its dual iff six signs come out right.  This script computes the six signs exactly (over two finite fields).

The mechanism (the one that closes W1/W2 in chirality_probe_w1w2.py): if sigma is an isometry of M and rho = sigma^* rho*
(the dual pulled back by sigma), then h^1(M; V) = h^1(M; sigma^* V*) = h^1(M; V*) and N(V) = 0.  For the E_6 family
through the geometric holonomy rho_0 = principal E_6 o Riley, the dual of 27_rho is 27_{theta rho} (theta the outer
automorphism of E_6; it fixes rho_0 because the principal sl_2 of E_6 lies in F_4), so N(27_rho) = 0 for every rho on
the germ of the E_6 character variety at [rho_0] as soon as SOME isometry sigma satisfies theta rho = sigma^* rho on the
germ.  Both theta and sigma^* are involutions of the germ fixing [rho_0]; by Cartan's linearisation of finite group
actions on analytic germs, the involution theta o sigma^* is the identity on the germ iff it is the identity on the
Zariski tangent space
      T_[rho_0] = H^1(M; e_6) = H^1(M; V_2) + H^1(M; V_8) + H^1(M; V_10) + H^1(M; V_14) + H^1(M; V_16) + H^1(M; V_22)
(e_6 under the principal sl_2: exponents 1, 4, 5, 7, 8, 11; each h^1 = 1 -- computed here; theta = +1 on the f_4 part
{2, 10, 14, 22} and -1 on the 26 = V_8 + V_16, B1086/B1087's theta-odd slots).  So the whole question is SIX SIGNS: the
eigenvalue eps_n of sigma^* on H^1(M; Sym^n rho_0), n in {2, 8, 10, 14, 16, 22}, for the orientation-preserving
isometries of the object:
      the inversion  iota: a -> a^-1, b -> b^-1   (intertwiner g = diag(i, -i)),
      the period-2 swap tau: a -> b, b -> a       (intertwiner g = [[0, u], [u^2, 0]], u = e^{i pi/3}: g a g^-1 = b, g b g^-1 = a),
      and their product.
If some sigma has (eps_n) = (+, -, +, +, -, +), the theta-odd frame is vector-like on the cusped object near the
geometric point: N(27_rho) = 0 identically on the germ, and B1268's remaining computation (the cusp-fixed theta-odd
locus) is closed without finding the locus.

The action on cohomology: for a cocycle f (f(xy) = f(x) + rho(x) f(y)) and sigma with rho(sigma(x)) = G rho(x) G^-1,
(sigma^* f)(x) = G^-1 f(sigma(x)) is again a cocycle; f(x^-1) = -rho(x)^-1 f(x).  H^1 = Z^1/B^1 by Fox calculus on the
two-bridge presentation <a, b | a w b^-1 w^-1>, w = b a^-1 b^-1 a, Riley's holonomy a = [[1, 1], [0, 1]],
b = [[1, 0], [u, 1]].  Everything lives in Z[zeta_12] (u = zeta_12^2, i = zeta_12^3), so the computation is done EXACTLY
over F_p for two primes p = 1 mod 12 (zeta_12 a primitive twelfth root of unity mod p); the sign eps is decided by the
exact membership tests sigma^* z -/+ z in B^1.  Checked: the relator, the intertwiners, sigma^*(Z^1) = Z^1,
sigma^*(B^1) = B^1, and that exactly one of the two membership tests holds.
"""
from __future__ import annotations
import sys
from math import comb
import sympy


def primes_1_mod_12(start, k):
    out, p = [], sympy.nextprime(start)
    while len(out) < k:
        if p % 12 == 1:
            out.append(int(p))
        p = sympy.nextprime(p)
    return out


class Fp:
    def __init__(self, p):
        self.p = p
        # a primitive twelfth root of unity
        g = sympy.primitive_root(p)
        self.z12 = pow(int(g), (p - 1) // 12, p)
        self.u = pow(self.z12, 2, p)          # e^{i pi/3}
        self.i = pow(self.z12, 3, p)          # sqrt(-1)
        assert (self.u ** 3 + 1) % p == 0 and (self.i ** 2 + 1) % p == 0 and (self.u ** 2 - self.u + 1) % p == 0

    def inv(self, x):
        return pow(x % self.p, self.p - 2, self.p)

    def mat(self, rows):
        return [[x % self.p for x in r] for r in rows]

    def matmul(self, A, B):
        p = self.p
        n, m, k = len(A), len(B), len(B[0])
        return [[sum(A[i][t] * B[t][j] for t in range(m)) % p for j in range(k)] for i in range(n)]

    def matinv(self, A):
        n = len(A); p = self.p
        M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
        for c in range(n):
            piv = next(r for r in range(c, n) if M[r][c] % p)
            M[c], M[piv] = M[piv], M[c]
            iv = self.inv(M[c][c])
            M[c] = [x * iv % p for x in M[c]]
            for r in range(n):
                if r != c and M[r][c]:
                    f = M[r][c]
                    M[r] = [(x - f * y) % p for x, y in zip(M[r], M[c])]
        return [row[n:] for row in M]

    def rref(self, A):
        """reduced row echelon form; returns (R, pivot columns)."""
        p = self.p
        M = [row[:] for row in A]
        n, m = len(M), len(M[0]) if M else 0
        piv_cols, r = [], 0
        for c in range(m):
            if r >= n:
                break
            piv = next((i for i in range(r, n) if M[i][c] % p), None)
            if piv is None:
                continue
            M[r], M[piv] = M[piv], M[r]
            iv = self.inv(M[r][c])
            M[r] = [x * iv % p for x in M[r]]
            for i in range(n):
                if i != r and M[i][c]:
                    f = M[i][c]
                    M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
            piv_cols.append(c); r += 1
        return M[:r], piv_cols

    def rank(self, A):
        return len(self.rref(A)[0]) if A and A[0] else 0

    def kernel(self, A):
        """basis (list of vectors) of {x : A x = 0}."""
        R, piv = self.rref(A)
        m = len(A[0]); p = self.p
        free = [c for c in range(m) if c not in piv]
        basis = []
        for f in free:
            v = [0] * m; v[f] = 1
            for i, pc in enumerate(piv):
                v[pc] = (-R[i][f]) % p
            basis.append(v)
        return basis

    def in_span(self, cols, v):
        """is v in the column span of `cols` (list of column vectors)?"""
        if not cols:
            return all(x % self.p == 0 for x in v)
        A = [list(r) for r in zip(*cols)]
        return self.rank(A) == self.rank([row + [x] for row, x in zip(A, v)])


def symn(F, g, n):
    """Sym^n(g) mod p on the basis x^(n-j) y^j (the substitution x -> g11 x + g12 y, y -> g21 x + g22 y)."""
    p = F.p
    g11, g12, g21, g22 = g[0][0], g[0][1], g[1][0], g[1][1]
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(n + 1):
        for r in range(n - j + 1):
            for s in range(j + 1):
                k = (n - j - r) + (j - s)
                M[k][j] = (M[k][j] + comb(n - j, r) * pow(g11, r, p) * pow(g12, n - j - r, p) * comb(j, s) * pow(g21, s, p) * pow(g22, j - s, p)) % p
    return M


def word_matrix(F, rep, word):
    d = len(rep['a'])
    M = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for c in word:
        M = F.matmul(M, rep[c])
    return M


def fox_matrix(F, rep, word, x):
    d = len(rep['a']); p = F.p
    M = [[0] * d for _ in range(d)]
    pref = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for c in word:
        if c == x:
            M = [[(a + b) % p for a, b in zip(r1, r2)] for r1, r2 in zip(M, pref)]
        elif c == x.upper():
            Q = F.matmul(pref, rep[c])
            M = [[(a - b) % p for a, b in zip(r1, r2)] for r1, r2 in zip(M, Q)]
        pref = F.matmul(pref, rep[c])
    return M


W = ['b', 'A', 'B', 'a']
REL = ['a'] + W + ['B'] + [c.swapcase() for c in reversed(W)]


def cocycle_on_word(F, rep, f, word):
    """f(word) for the cocycle with values f['a'], f['b'] on the generators (f(x^-1) = -rho(x^-1) f(x))."""
    d = len(rep['a']); p = F.p
    val = [0] * d
    pref = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for c in word:
        if c.islower():
            v = f[c]
        else:
            Rv = F.matmul(rep[c], [[x] for x in f[c.lower()]])
            v = [(-x[0]) % p for x in Rv]
        Pv = F.matmul(pref, [[x] for x in v])
        val = [(a + b[0]) % p for a, b in zip(val, Pv)]
        pref = F.matmul(pref, rep[c])
    return val


def analyse(F, n, sigmas):
    p = F.p
    a2 = F.mat([[1, 1], [0, 1]]); b2 = F.mat([[1, 0], [F.u, 1]])
    rep = {'a': symn(F, a2, n), 'b': symn(F, b2, n)}
    rep['A'] = F.matinv(rep['a']); rep['B'] = F.matinv(rep['b'])
    d = n + 1
    Ident = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    assert word_matrix(F, rep, REL) == Ident, "relator"
    D = [ra + rb for ra, rb in zip(fox_matrix(F, rep, REL, 'a'), fox_matrix(F, rep, REL, 'b'))]     # d x 2d
    Z = F.kernel(D)                                                                                # cocycles (f(a), f(b))
    Bcols = [[(rep['a'][i][j] - (1 if i == j else 0)) % p for i in range(d)] + [(rep['b'][i][j] - (1 if i == j else 0)) % p for i in range(d)] for j in range(d)]
    rB = F.rank([list(r) for r in zip(*Bcols)])
    h1 = len(Z) - rB
    out = {'h1': h1, 'dimZ': len(Z), 'rankB': rB, 'eps': {}}
    if h1 == 0:
        return out
    # a cocycle not in B^1
    z = next(v for v in Z if not F.in_span(Bcols, v))
    for name, (sigma, g) in sigmas.items():
        G = symn(F, g, n)
        # intertwiner check: rho(sigma(x)) = G rho(x) G^-1 for x = a, b
        Gi = F.matinv(G)
        for x in ('a', 'b'):
            lhs = word_matrix(F, rep, sigma[x])
            rhs = F.matmul(F.matmul(G, rep[x]), Gi)
            assert lhs == rhs, f"intertwiner {name} {x}"

        def pull(f):
            fa, fb = f[:d], f[d:]
            fd = {'a': fa, 'b': fb}
            va = cocycle_on_word(F, rep, fd, sigma['a']); vb = cocycle_on_word(F, rep, fd, sigma['b'])
            ga = F.matmul(Gi, [[x] for x in va]); gb = F.matmul(Gi, [[x] for x in vb])
            return [x[0] for x in ga] + [x[0] for x in gb]
        # invariance of Z^1 and B^1
        Zcols = Z
        assert all(F.in_span(Zcols, pull(v)) for v in Z), f"Z^1 not invariant under {name}"
        assert all(F.in_span(Bcols, pull(v)) for v in Bcols), f"B^1 not invariant under {name}"
        w = pull(z)
        plus = F.in_span(Bcols, [(x - y) % p for x, y in zip(w, z)])
        minus = F.in_span(Bcols, [(x + y) % p for x, y in zip(w, z)])
        assert plus != minus, f"sign undecided for {name} at n = {n} (h^1 = {h1})"
        out['eps'][name] = +1 if plus else -1
    return out


def main():
    primes = primes_1_mod_12(10 ** 6, 2)
    print(f"primes (= 1 mod 12): {primes}")
    theta_sign = {2: +1, 8: -1, 10: +1, 14: +1, 16: -1, 22: +1}
    results = {}
    for p in primes:
        F = Fp(p)
        u, i = F.u, F.i
        g_iota = F.mat([[i, 0], [0, -i]])
        g_tau = F.mat([[0, u], [u * u, 0]])
        sigmas = {'iota': ({'a': ['A'], 'b': ['B']}, g_iota), 'tau': ({'a': ['b'], 'b': ['a']}, g_tau),
                  'iota.tau': ({'a': ['B'], 'b': ['A']}, F.matmul(g_iota, g_tau))}
        print(f"\n=== F_{p}: zeta_12 = {F.z12}, u = {u}, i = {i} ===")
        print("  n | dim Z^1 | rank B^1 | h^1(M; Sym^n) | eps(iota) eps(tau) eps(iota.tau) | theta")
        for n in range(0, 23):
            r = analyse(F, n, sigmas)
            results[(p, n)] = r
            e = r['eps']
            print(f" {n:2d} |   {r['dimZ']:2d}    |    {r['rankB']:2d}    |      {r['h1']}        | " + (f"{e['iota']:+d}  {e['tau']:+d}  {e['iota.tau']:+d}" if e else "  -   -   -") + f"       | {theta_sign.get(n, '.') if n in theta_sign else '.'}")
    # agreement between primes and the verdict
    agree = all(results[(primes[0], n)] == results[(primes[1], n)] for n in range(23))
    print(f"\nthe two primes agree on every row: {agree}")
    six = (2, 8, 10, 14, 16, 22)
    verdict = {}
    for name in ('iota', 'tau', 'iota.tau'):
        signs = [results[(primes[0], n)]['eps'][name] for n in six]
        verdict[name] = (signs, all(s == theta_sign[n] for s, n in zip(signs, six)))
        print(f"  {name}: signs on H^1(M; V_n), n = {six}: {signs}; equals theta = {[theta_sign[n] for n in six]}: {verdict[name][1]}")
    h1_ok = all(results[(primes[0], n)]['h1'] == (1 if n % 2 == 0 else 0) for n in range(23))
    print(f"  h^1(M; Sym^n) = 1 for even n, 0 for odd n (n <= 22): {h1_ok}")
    return verdict, agree, h1_ok


if __name__ == "__main__":
    verdict, agree, h1_ok = main()
    ok = agree and h1_ok
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    print("THETA-ODD PAIRING BY AN ISOMETRY:", "YES -- " + ", ".join(k for k, v in verdict.items() if v[1]) if any(v[1] for v in verdict.values()) else "NO isometry among iota, tau, iota.tau acts as theta on the tangent space")
    sys.exit(0 if ok else 1)
