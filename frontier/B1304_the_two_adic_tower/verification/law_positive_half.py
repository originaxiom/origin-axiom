#!/usr/bin/env python3
"""THE POSITIVE HALF OF THE TOWER'S LAW, PROVED (B1304 addendum, 2026-09-08).

Setting (B1303/B1304): pi_1(Y_n) = <a, b | alpha^n(x) = x> for the monodromy automorphism alpha of the punctured-torus fibre;
for a character psi of H_1(Y_n) = Z[phi]/(phi^{2n} - 1) (a <-> phi, b <-> 1), h^1(Y_n; psi) = 1 iff the Fox matrix P_n of
alpha^n at psi is the identity.  A Psi-eigencharacter has psi(x) = zeta^{lam(x)} with lam: Z[phi] -> Z/m a ring map, lam(phi) = u,
u^2 = u + 1 mod m, and psi is a character of Y_n iff u^{2n} = 1 mod m.

THEOREM (the positive half).  Let e = ord_m(u) and e' = ord_m(-u) = ord_m(ubar), ubar = 1 - u = -1/u the conjugate root.
If e is odd, or e' is odd, then h^1(Y_n; psi) = 1 at every level n at which psi lives.

Proof.  (1) Three presentations of pi_1(Y_n) coincide exactly: with phi: a -> a^2 b, b -> a b (B1303's), phi' = c_{a^-1} phi
(fixes the boundary commutator c = [a, b], so <a, b | phi'^n(x) = x> IS pi_1 of the branched cover), and h: a -> ab, b -> a
(the half-deck: Psi on H_1, h^2 = c_{ab} phi = c_{aba} phi'), the groups <a,b | phi^n = id>, <a,b | phi'^n = id>,
<a,b | h^{2n} = id> are all Gamma/<< g_n t^n >> for the mapping-torus group Gamma = <a,b,t | t x t^-1 = phi'(x)> with
g_n t^n = (g t)^n, g = a resp. aba; and a = z phi'(z)^-1 with z = b^-1, aba = z phi'(z)^-1 with z = a^-1 b^-1 (Reidemeister
coboundaries), so g t = z t z^-1 and << (gt)^n >> = << t^n >>.  All three are pi_1(Y_n).  [checked below in the free group]
(2) With the half-deck presentation the Fox matrix of h^{2n} at psi is the ordered product of B(zeta^{u^j}) = [[1, zeta^{u^j}],
[1, 0]] over j = 1 .. 2n (the chain rule), which is periodic in j with period e; so P_n = N_0^{2n/e}, N_0 the product over one
period (the Fox matrix of h^e at psi; psi is h^e-invariant).  (3) N_0 fixes the coboundary vector v = (psi(a)-1, psi(b)-1) and
acts on the quotient Z^1/B^1 = H^1(F_2; psi) (one-dimensional) by the scalar (-1)^e psi(g_e), where h^e(c) = g_e c^{(-1)^e}
g_e^-1 and g_e abelianises to phi^2 (phi^e - 1), so psi(g_e) = zeta^{u^2 (u^e - 1)} = 1: the scalar is (-1)^e.  (4) If e is odd
the eigenvalues 1, -1 are distinct, N_0 is diagonalisable, N_0^2 = I; and e | 2n with e odd forces e | n, so 2n/e is even and
P_n = I: h^1 = 1.  (5) If e' = ord(-u) is odd: Y_n is amphichiral (the orientation-reversing symmetry of the figure-eight lifts
to every cyclic branched cover), the lift inverts the deck and acts on H_1 by J = Psi o (Galois conjugation) (B1303), so
psi o J is a Psi-eigencharacter of the same order with eigenvalue ubar = -1/u, and h^1(psi) = h^1(psi o J) = 1 by (4).  QED.

COROLLARY.  In the conductor form (B1304 addendum): 'd odd and u^d = +-1 globally, m prime to 5' is EQUIVALENT to
'ord(u) odd or ord(-u) odd' [checked below over all m <= 4000], so the theorem is exactly the law's 'if' direction; the
'only if' (both orders even => h^1 = 0, which contains 'new characters at even conductor never carry' and the ramified prime)
stays a verified conjecture (exact at every level <= 30), now reduced to: for ord(u), ord(-u) both even, the unipotent
one-period product N_0 is not the identity.

This script checks: (A) the free-group identities of step (1); (B) the conductor form <=> the odd-order form for all m <= 4000;
(C) on every eigencharacter of every level n <= NMAX (exact, two large primes): P_n = N_0^{2n/e}, the eigenvalue of N_0 on
the quotient is (-1)^e, e odd => N_0^2 = I and P_n = I; and the theorem's prediction h^1 = 1 whenever e or e' is odd."""
import sys, itertools
from sympy import isprime, primitive_root, factorint, divisors
from sympy.ntheory import n_order

def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]: out.pop()
        else: out.append(x)
    return out
def inv(w): return [(g, -e) for (g, e) in reversed(w)]
def apply(auto, w):
    out = []
    for (g, e) in w:
        out += auto[g] if e == 1 else inv(auto[g])
    return reduce_word(out)
A, B = [('a', 1)], [('b', 1)]
phi = {'a': A + A + B, 'b': A + B}
phip = {x: reduce_word(inv(A) + phi[x] + A) for x in 'ab'}          # c_{a^-1} phi
h = {'a': A + B, 'b': A}
c = reduce_word(A + B + inv(A) + inv(B))

def check_A():
    assert apply(phip, c) == c, "phi' must fix [a,b]"
    hh = {x: apply(h, h[x]) for x in 'ab'}
    aba = A + B + A
    assert all(hh[x] == reduce_word(aba + phip[x] + inv(aba)) for x in 'ab'), "h^2 = c_{aba} phi'"
    assert all(phi[x] == reduce_word(A + phip[x] + inv(A)) for x in 'ab'), "phi = c_a phi'"
    # Reidemeister coboundaries: g = z phi'(z)^-1
    for g, z in ((A, inv(B)), (aba, reduce_word(inv(A) + inv(B)))):
        assert reduce_word(z + inv(apply(phip, z))) == g, (g, z)
    print("(A) free-group identities: phi' fixes c; phi = c_a phi'; h^2 = c_{aba} phi'; a = b^-1 phi'(b^-1)^-1; aba = (a^-1 b^-1) phi'(a^-1 b^-1)^-1 -- all hold")

def roots(m):
    return [u for u in range(m) if (u * u - u - 1) % m == 0]

def check_B(MMAX=4000):
    bad = 0; total = 0
    for m in range(2, MMAX + 1):
        for u in roots(m):
            if u % m == 0: continue
            total += 1
            e = n_order(u, m); ep = n_order((-u) % m, m)
            odd_form = (e % 2 == 1) or (ep % 2 == 1)
            # conductor form: d = min{d : u^{2d} = 1}; class iff d odd, u^d = +-1 mod m, gcd(m, 5) = 1
            d = e if e % 2 else e // 2
            cond_form = (d % 2 == 1) and (pow(u, d, m) in (1, m - 1)) and (m % 5 != 0)
            if odd_form != cond_form:
                bad += 1
                if bad <= 5: print("   mismatch", m, u, e, ep, d, pow(u, d, m))
    print(f"(B) conductor form <=> odd-order form on all {total} pairs (m, u) with m <= {MMAX}: {'EQUIVALENT' if bad == 0 else str(bad) + ' MISMATCHES'}")
    return bad == 0

def matmul(X, Y, q):
    return [[(X[0][0]*Y[0][0] + X[0][1]*Y[1][0]) % q, (X[0][0]*Y[0][1] + X[0][1]*Y[1][1]) % q],
            [(X[1][0]*Y[0][0] + X[1][1]*Y[1][0]) % q, (X[1][0]*Y[0][1] + X[1][1]*Y[1][1]) % q]]
def matpow(X, k, q):
    R = [[1, 0], [0, 1]]
    while k:
        if k & 1: R = matmul(R, X, q)
        X = matmul(X, X, q); k >>= 1
    return R
def two_primes(m):
    qs = []; qq = m * (10 ** 9 // m) + 1
    while len(qs) < 2:
        if isprime(qq) and (qq - 1) % m == 0: qs.append(qq)
        qq += m
    return qs

def check_C(NMAX=13):
    from sympy import Matrix, fibonacci, lucas
    print(f"(C) every eigencharacter of every level n <= {NMAX}: structure of N_0 and the theorem's prediction")
    allok = True
    for n in range(2, NMAX + 1):
        c_ = lucas(n) if n % 2 else 5 * fibonacci(n)     # |H_1| = c^2 ... the exponent of H_1 as Z[phi]/(c) or (sqrt5 F_n)
        # eigencharacters: lam: Z[phi]/(phi^{2n}-1) -> Z/m, m | exponent; take every m dividing the group exponent, every root u with u^{2n} = 1
        expo = int(lucas(n)) if n % 2 else int(5 * fibonacci(n)) // (1 if n % 2 else 1)
        # the exponent of Z[phi]/(phi^{2n} - 1): for n odd Z[phi]/(L_n) has exponent L_n; for n even Z[phi]/(sqrt5 F_n) has exponent 5 F_n
        stats = dict(chars=0, pred_pos=0, pos=0, mism=0, e_odd=0, ep_odd=0, both_even=0, pos_both_even=0)
        for m in divisors(expo):
            if m == 1: continue
            for u in roots(m):
                if pow(u, 2 * n, m) != 1: continue
                if any(pow(u, 2 * n, mm) == 1 and (u * u - u - 1) % mm == 0 for mm in divisors(m) if 1 < mm < m and m % mm == 0 and False):
                    pass
                # the eigencharacter psi_u of exact order m: zeta of order m, psi(a) = zeta^u, psi(b) = zeta; count each (m, u) once (its Galois orbit has phi(m) members with the same h^1)
                e = n_order(u, m); ep = n_order((-u) % m, m)
                qs = two_primes(m); vals = []
                for q in qs:
                    z = pow(primitive_root(q), (q - 1) // m, q)
                    Bs = [[[1, pow(z, pow(u, j, m), q)], [1, 0]] for j in range(1, 2 * n + 1)]
                    P = [[1, 0], [0, 1]]
                    for Bj in Bs: P = matmul(Bj, P, q)       # J_{h^{2n}} = J_h^{psi h^{2n-1}} ... J_h^{psi}: later factors on the left
                    N0 = [[1, 0], [0, 1]]
                    for Bj in Bs[:e]: N0 = matmul(Bj, N0, q)
                    I2 = [[1, 0], [0, 1]]
                    vals.append((P == I2, matpow(N0, 2 * n // e, q) == P, (matmul(N0, N0, q) == I2) if e % 2 else None,
                                 # trace of N0 = 1 + (-1)^e (eigenvalues 1 and (-1)^e)
                                 (N0[0][0] + N0[1][1]) % q == (1 + (-1) ** e) % q))
                assert vals[0] == vals[1], (n, m, u, vals)
                isI, powok, sq, trok = vals[0]
                assert powok and trok, (n, m, u, vals)
                if e % 2: assert sq and isI, (n, m, u)
                stats['chars'] += 1; stats['pos'] += isI
                pred = (e % 2 == 1) or (ep % 2 == 1)
                stats['pred_pos'] += pred; stats['e_odd'] += e % 2; stats['ep_odd'] += ep % 2
                if pred and not isI: stats['mism'] += 1; allok = False
                if not pred:
                    stats['both_even'] += 1; stats['pos_both_even'] += isI
        print(f"    n = {n:2d}: {stats['chars']} eigencharacter classes (one per (m, u)); theorem predicts h1 = 1 for {stats['pred_pos']} (ord u odd: {stats['e_odd']}, ord -u odd: {stats['ep_odd']}), "
              f"all of them carry: {stats['mism'] == 0}; both orders even: {stats['both_even']}, of which carry: {stats['pos_both_even']} (the converse's content)")
    return allok

if __name__ == "__main__":
    check_A()
    okB = check_B()
    okC = check_C(int(sys.argv[1]) if len(sys.argv) > 1 else 13)
    print("SELFTEST:", "PASS" if okB and okC else "FAIL")
