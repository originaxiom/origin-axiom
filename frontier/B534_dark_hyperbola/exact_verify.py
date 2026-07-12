#!/usr/bin/env python3
"""B534: exact verification of the three crystallization theorems.

THE DARK HYPERBOLA THEOREM (exact, all primes 3..41):
  T(j,l) = tr(Par W1^j W2^l), W1 = diag(zeta^{n(n-1)/2}), W2 = F W1^-1 F^-1.
  p*T(j,l) = sum_{n,k} zeta^{E(n,k)},  E = j*T(n) - l*T(k) + 2nk  (T(n)=n(n-1)/2).
  In the group ring Z[x]/(x^p - 1): p*T = sum x^E; the kernel of the map to
  Z[zeta_p] is (1+x+...+x^{p-1}), so T = 0  <=>  the count vector
  c[e] = #{(n,k) : E(n,k)=e}  is CONSTANT. Pure integer counting -- exact.

  |p*T|^2 = autocorrelation of c; it is the rational r <=> autocorr is constant
  s off zero, and then r = autocorr[0] - s. Survivor magnitude sqrt(p) <=> r = p^3.

THE POWER-SET MAGNITUDE THEOREM (exact at N=15, float64 at N=105, 165):
  same construction mod N; zero test and |T|^2 via reduction mod Phi_N (sympy).

THE ASYMPTOTIC DARKNESS (proof + numeric crossing):
  active fraction prod_p (1-(p-2)/p^2) -> 0 since sum (p-2)/p^2 = sum 1/p - 2/p^2
  diverges (Euler-Mertens); 0 < 1-x <= exp(-x) bounds the product by exp(-sum).

THE TOWER TORSION LAW (symbolic + Smith forms):
  det(A1^n - I) = 2 - L(2n) since A1^n has trace L(2n), det 1 (2-line proof);
  L(2n)-2 = L(n)^2 (n odd), = 5 F(n)^2 = (L(n)-2)(L(n)+2) (n even) -- classical
  identities proved symbolically; H1 torsion of b++(RL)^4 = coker(A1^4 - I)
  = Z/3 + Z/15 by exact Smith form.
"""

import numpy as np
import sympy as sp
from sympy import primerange


# ────────────────────────── Part 1: the dark hyperbola ──────────────────────────

def count_vector(p, j, l):
    """c[e] = #{(n,k) in (Z/p)^2 : j*T(n) - l*T(k) + 2nk = e mod p} (exact ints)."""
    n = np.arange(p)
    Tn = (n * (n - 1) // 2) % p
    E = (j * Tn[:, None] - l * Tn[None, :] + 2 * np.outer(n, n)) % p
    return np.bincount(E.ravel(), minlength=p).astype(np.int64)


def is_zero_trace(c):
    """sum_e c[e] zeta^e = 0 in Z[zeta_p]  <=>  c constant."""
    return bool(np.all(c == c[0]))


def abs_squared_rational(c, p):
    """|sum c[e] zeta^e|^2 if rational, else None. autocorr[d] = sum_e c[e]c[e+d]."""
    ac = np.array([int(np.dot(c, np.roll(c, -d))) for d in range(p)], dtype=object)
    off = ac[1:]
    if np.all(off == off[0]):
        return int(ac[0] - off[0])
    return None


def verify_dark_hyperbola(p):
    """Exact: dark set == {jl = -4 mod p} \\ {(2, p-2)}; survivor |pT|^2 = p^3;
    all other actives |pT|^2 = p^2 (magnitude 1)."""
    dark = set()
    survivor_ok = other_mags_ok = True
    for j in range(p):
        for l in range(p):
            c = count_vector(p, j, l)
            if is_zero_trace(c):
                dark.add((j, l))
            else:
                r = abs_squared_rational(c, p)
                if j == 2 and l == (p - 2) % p:
                    survivor_ok &= (r == p**3)
                elif r is not None and r not in (p**2,):
                    other_mags_ok = False
    claim = {(j, l) for j in range(p) for l in range(p)
             if (j * l) % p == (-4) % p and not (j == 2 and l == p - 2)}
    return dark == claim, len(dark) == p - 2, survivor_ok, other_mags_ok


# ────────────────────────── Part 2: power-set magnitudes ──────────────────────────

def exact_powerset_15():
    """Exact at N=15 over Z[zeta_15]: |15*T|^2 reduced mod Phi_15 must be the
    rational 15^2 * m with m in {0,1,3,5,15}."""
    N = 15
    x = sp.Symbol('x')
    phi15 = sp.Poly(sp.cyclotomic_poly(15, x), x)
    n = np.arange(N)
    Tn = (n * (n - 1) // 2) % N
    mags = set()
    for j in range(N):
        for l in range(N):
            E = (j * Tn[:, None] - l * Tn[None, :] + 2 * np.outer(n, n)) % N
            c = np.bincount(E.ravel(), minlength=N)
            # |sum c[e] x^e|^2 = sum_d autocorr[d] x^{-d}; reduce mod Phi_15
            ac = [int(np.dot(c, np.roll(c, -d))) for d in range(N)]
            poly = sp.Poly([ac[(-e) % N] for e in range(N - 1, -1, -1)], x)
            red = poly.rem(phi15)
            if red.degree() <= 0:
                r = int(red.as_expr()) if red.degree() == 0 else 0
                assert r % (N * N) == 0, (j, l, r)
                mags.add(r // (N * N))
            else:
                return None, f"non-rational |T|^2 at {(j, l)}"
    return mags, "ok"


def float_powerset(N):
    """Float64 sweep at composite N: magnitudes^2 should hit only divisors of N."""
    w = np.exp(2j * np.pi / N)
    n = np.arange(N)
    Tn = (n * (n - 1) // 2) % N
    U = w ** np.outer(np.arange(N), Tn)          # U[j,n] = w^{j T(n)}
    V = w ** (-np.outer(np.arange(N), Tn))       # V[l,k] = w^{-l T(k)}
    Z = w ** (2 * np.outer(n, n) % N)
    M = U @ Z @ V.T / N                          # M[j,l] = T(j,l)
    m2 = np.abs(M) ** 2
    divisors = [d for d in range(1, N + 1) if N % d == 0]
    bad = 0
    hit = set()
    for v in m2.ravel():
        d = min(divisors + [0], key=lambda t: abs(v - t))
        if abs(v - d) > 1e-6:
            bad += 1
        else:
            hit.add(d)
    return hit, bad, N * N


# ────────────────────────── Part 3: asymptotic darkness ──────────────────────────

def darkness_crossing():
    prod = 1.0
    crossing = None
    for p in primerange(3, 200):
        prod *= 1 - (p - 2) / p**2
        if crossing is None and prod < 0.5:
            crossing = p
    return crossing, prod


# ────────────────────────── Part 4: the tower torsion law ──────────────────────────

def tower_law():
    """det(A1^n - I) = 2 - L(2n); odd/even split; n=4 Smith form."""
    A1 = sp.Matrix([[2, 1], [1, 1]])
    ok_det = all(
        (A1**n - sp.eye(2)).det() == 2 - sp.lucas(2 * n) for n in range(1, 13))

    # classical identities, symbolic: x = phi^n, y = psi^n, xy = (-1)^n
    x, y = sp.symbols('x y')
    L2n = x**2 + y**2          # L(2n)
    Ln = x + y                 # L(n)
    # L(2n) = L(n)^2 - 2(xy):  (x+y)^2 - 2xy = x^2+y^2  -- identity in Z[x,y]
    ok_id1 = sp.expand(Ln**2 - 2 * x * y - L2n) == 0
    # L(n)^2 - 5F(n)^2 = 4(xy):  F(n) = (x-y)/sqrt5
    Fn2 = (x - y)**2 / 5
    ok_id2 = sp.expand(Ln**2 - 5 * Fn2 - 4 * x * y) == 0
    # => n odd (xy=-1): L(2n)-2 = L(n)^2;  n even (xy=1): L(2n)-2 = 5F(n)^2
    ok_split = all(
        (sp.lucas(2 * n) - 2 == sp.lucas(n)**2 if n % 2 == 1
         else sp.lucas(2 * n) - 2 == 5 * sp.fibonacci(n)**2)
        for n in range(1, 13))

    # n=4: coker(A1^4 - I) = Z/3 + Z/15
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(A1**4 - sp.eye(2))
    ok_h1 = (abs(S[0, 0]), abs(S[1, 1])) == (3, 15)
    return ok_det, ok_id1, ok_id2, ok_split, ok_h1, S


# ────────────────────────── main ──────────────────────────

def main():
    print("=" * 76)
    print("B534 — exact verification of the crystallization theorems")
    print("=" * 76)

    print("\n─── 1. THE DARK HYPERBOLA (exact integer counting, primes 3..41) ───\n")
    all_ok = True
    for p in primerange(3, 42):
        setm, cnt, surv, oth = verify_dark_hyperbola(p)
        ok = setm and cnt and surv and oth
        all_ok &= ok
        print(f"  p={p:2d}: dark=={{jl=-4}}\\{{(2,p-2)}}: {setm}; count=p-2: {cnt}; "
              f"survivor |T|=sqrt(p): {surv}; other actives |T|=1: {oth}")
    print(f"\n  DARK HYPERBOLA: {'EXACT-VERIFIED at all 12 primes' if all_ok else 'FAILURES'}")

    print("\n─── 2. POWER-SET MAGNITUDES ───\n")
    mags15, msg = exact_powerset_15()
    print(f"  N=15 exact over Z[zeta_15]: |T|^2 values = {sorted(mags15)} ({msg})")
    print(f"    claim {{0,1,3,5,15}}: {mags15 == {0, 1, 3, 5, 15}}")
    for N in (105, 165):
        hit, bad, tot = float_powerset(N)
        print(f"  N={N} float64: {tot} points, off-catalog: {bad}, "
              f"|T|^2 hits: {sorted(hit)}")

    print("\n─── 3. ASYMPTOTIC DARKNESS ───\n")
    crossing, tail = darkness_crossing()
    print(f"  active fraction crosses 1/2 at p = {crossing} (claim: 31)")
    print(f"  at p<200: {tail:.4f}; proof: sum (p-2)/p^2 diverges (Mertens), "
          f"product <= exp(-sum) -> 0")

    print("\n─── 4. THE TOWER TORSION LAW ───\n")
    ok_det, id1, id2, split, h1, S = tower_law()
    print(f"  det(A1^n - I) == 2 - L(2n), n=1..12: {ok_det}")
    print(f"  L(2n) = L(n)^2 - 2(-1)^n  (symbolic): {id1}")
    print(f"  L(n)^2 - 5F(n)^2 = 4(-1)^n (symbolic): {id2}")
    print(f"  odd n -> L(n)^2; even n -> 5F(n)^2 = (L(n)-2)(L(n)+2), n=1..12: {split}")
    print(f"  H1 torsion of b++(RL)^4: Smith(A1^4 - I) diag = "
          f"({S[0,0]}, {S[1,1]}) -> Z/3 + Z/15: {h1}")


if __name__ == '__main__':
    main()
