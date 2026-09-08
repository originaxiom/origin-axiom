#!/usr/bin/env python3
"""TWO LEMMAS FROM THE CRITERION (B1304 addendum), with their numerical confirmation on the banked supports.

Lemma 1 (pullback exactness).  If d | n and psi is a character of H_1(Y_d) pulled back to Y_n (the same functional on
Z^2, Phi^d-invariant), the sequence x_k = psi(Phi^k a) is d-periodic, so P_n(psi) = P_d(psi)^{n/d}; P_d is unipotent
(B1304), and a unipotent matrix U = I + N with U^k = I has N = 0; hence h^1(Y_n; pi^* psi) = h^1(Y_d; psi) -- the
pullback of Y_d's support is exactly the pulled-back part of Y_n's support (transfer's injectivity is an equality here),
and in particular Y_2's characters (a lens space, h^1 = 0) stay at 0 on every even level: the ramified clause.

Lemma 2 (Galois closure).  For k prime to the order of psi, x_k(psi^k) = x_k(psi)^k, so P(psi^k) = sigma_k(P(psi)) for the
Galois automorphism sigma_k: zeta -> zeta^k, and h^1(Y_n; psi^k) = h^1(Y_n; psi): the support is a union of the sets of
generators of cyclic subgroups (a character is in the support iff every generator of the cyclic group it generates is).

Checked: (1) on every pair d | n with 2 <= d < n <= 21, the characters of Y_n whose functional is Phi^d-invariant have
h^1 equal to their h^1 on Y_d (both from the criterion's support files); (2) on every level, the support is closed under
psi -> psi^k for k prime to the order."""
import sys, math, json, pathlib, itertools, collections
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
B1303 = HERE.parents[1] / 'B1303_the_two_by_two_criterion' / 'verification'
sys.path.insert(0, str(B1303))
import criterion_at_scale as S

def load(n):
    d = json.loads((B1303 / f"support_mt_Y{n}.json").read_text())
    return d['m'], {tuple(w) for w in d['positives']}, d['d1'], d['d2'], d['U']

def phi_pow(k):
    M = sp.Matrix([[2, 1], [1, 1]]) ** k
    return [[int(M[0, 0]), int(M[0, 1])], [int(M[1, 0]), int(M[1, 1])]]

def invariant_under(w, m, k):
    """psi (exponents w mod m on a, b) is Phi^k-invariant: (Phi^k)^T w = w mod m."""
    M = phi_pow(k)
    return ((M[0][0] * w[0] + M[1][0] * w[1] - w[0]) % m == 0) and ((M[0][1] * w[0] + M[1][1] * w[1] - w[1]) % m == 0)

def main():
    levels = [n for n in range(2, 22) if (B1303 / f"support_mt_Y{n}.json").exists()]
    data = {n: load(n) for n in levels}
    ok = True
    print("=== Lemma 1: pullback exactness on the banked supports ===")
    for n in levels:
        m_n, pos_n, d1, d2, U = data[n]
        for d in levels:
            if d >= n or n % d:
                continue
            m_d, pos_d, *_ = data[d]
            assert m_n % m_d == 0
            # pull back every character of Y_d (as exponents mod m_d -> mod m_n) and compare h^1
            # characters of Y_d: enumerate through its Smith parametrisation
            dd1, dd2, mm, UU = S.smith(d)
            mism = 0; count = 0; pulled_pos = 0
            for c1 in range(dd1):
                for c2 in range(dd2):
                    e1 = (c1 * (mm // dd1)) % mm; e2 = (c2 * (mm // dd2)) % mm
                    w = ((UU[0][0] * e1 + UU[1][0] * e2) % mm, (UU[0][1] * e1 + UU[1][1] * e2) % mm)
                    if w == (0, 0):
                        continue
                    wn = ((w[0] * (m_n // mm)) % m_n, (w[1] * (m_n // mm)) % m_n)
                    assert invariant_under(wn, m_n, n)
                    h_d = int(w in pos_d); h_n = int(wn in pos_n)
                    mism += (h_d != h_n); count += 1; pulled_pos += h_d
            # and every Phi^d-invariant character of Y_n is such a pullback: count them
            inv_n = sum(1 for w in pos_n if invariant_under(w, m_n, d))
            print(f"  Y_{d} -> Y_{n}: {count} characters pulled back, {pulled_pos} in Y_{d}'s support, mismatches of h^1: {mism}; Phi^{d}-invariant characters in Y_{n}'s support: {inv_n} (= {pulled_pos}: {inv_n == pulled_pos})", flush=True)
            ok &= (mism == 0 and inv_n == pulled_pos)
    print("=== Lemma 2: Galois closure of every support ===")
    for n in levels:
        m, pos, *_ = data[n]
        order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
        closed = all(((k * w[0]) % m, (k * w[1]) % m) in pos for w in pos for k in range(1, order(w)) if math.gcd(k, order(w)) == 1)
        print(f"  Y_{n}: support closed under psi -> psi^k, k prime to the order: {closed}", flush=True)
        ok &= closed
    return ok

if __name__ == "__main__":
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
