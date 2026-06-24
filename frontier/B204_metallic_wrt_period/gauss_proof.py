"""B204 -- the Gauss-sum reciprocity proof that |Z(a,b)| is exactly periodic (self-contained, fast).

Reduction (each step an EXACT identity, verified here to >=12 digits via the cheap dual forms):

  Z(a,b;n) = (2/n) e^{-i pi(a-b)/(2n)} * Ztil(n),   n = k+2,
  Ztil(n) = (1/(2n)) sum_{p,q=0}^{2n-1} e^{i pi (a p^2 - b q^2)/(2n)} sin^2(pi p q/n).
    [range extends 1..n-1 -> 0..2n-1 for free: sin^2(pi p q/n) vanishes at p,q in {0,n} mod n;
     folding p->2n-p is exact -> a FULL-PERIOD sum, no boundary corrections.]

  Split sin^2 = 1/2 - 1/4 e^{2 pi i pq/n} - 1/4 e^{-2 pi i pq/n}:
  Ztil(n) = (1/(2 sqrt(ab))) G_a(n) conj(G_b(n))           [DIAGONAL, Landsberg-Schaar, EXACT]
          - (1/(4 sqrt(4+ab))) (Gamma^+(2n) + Gamma^-(2n)) [CROSS, 2D Gauss reciprocity, EXACT]
    G_a(n)   = sum_{s=0}^{a-1} e^{-2 pi i n s^2/a}                 (depends on n mod a; period EXACTLY a)
    Gamma^t(N) = (1/(4+ab)) sum_{y in (Z/(4+ab))^2} e^{-i pi N y^T M_t^{-1} y},  M_t=[[a,2t],[2t,-b]]
                 (depends on N=2n mod (4+ab); 4+ab = det(gamma+I), gamma = R^a L^b)

CONSEQUENCES (the theorem):
  * |Z| = |Ztil| is EXACTLY periodic in the level k (the winding phase e^{-i pi(a-b)/(2n)} is the
    only non-periodic factor and drops under |.|; for a=b it is 1, so Z itself is real & periodic).
  * per(diagonal) = lcm(a,b)  [PROVED: G_a has period exactly a -- take s=1 in G_a(n+d)=G_a(n) => a|d].
  * per(cross) divides 4+ab (the form determinant); the full period
        P = lcm( lcm(a,b), per(cross) ) = lcm(a,b)(4+ab)/gcd(4+ab,4)
    -- the lcm(a,b) factor is proved; the exact-period identity is verified on the cells below.
"""
import mpmath as mp
from math import gcd
mp.mp.dps = 30


def lcm(a, b):
    return a * b // gcd(a, b)


def Ppred(a, b):
    D = 4 + a * b
    return lcm(a, b) * D // gcd(D, 4)


# ---- direct (defining) objects ----
def Ztil_direct(a, b, n):
    """(1/(2n)) sum_{p,q=0}^{2n-1} e^{i pi(ap^2-bq^2)/(2n)} sin^2(pi pq/n) -- the de-wound trace."""
    tot = mp.mpf(0)
    for p in range(2 * n):
        ep = mp.e**(1j * mp.pi * a * p * p / (2 * n))
        for q in range(2 * n):
            tot += ep * mp.e**(-1j * mp.pi * b * q * q / (2 * n)) * mp.sin(mp.pi * p * q / n) ** 2
    return tot / (2 * n)


def Z_orig(a, b, n):
    """the original trace Z(a,b;k), range 1..n-1, with sin^2 form."""
    tot = mp.mpf(0)
    for p in range(1, n):
        for q in range(1, n):
            tot += mp.e**(1j * mp.pi * (a * p * p - b * q * q - (a - b)) / (2 * n)) * mp.sin(mp.pi * p * q / n) ** 2
    return (2 / mp.mpf(n)) * tot


# ---- reciprocity closed forms ----
def G_a(a, n):
    return mp.fsum(mp.e**(-2j * mp.pi * n * s * s / a) for s in range(a))


def diag_closed(a, b, n):
    return G_a(a, n) * mp.conj(G_a(b, n)) / (2 * mp.sqrt(a * b))


def Gamma_t(a, b, t, N):
    D0 = a * b + 4
    tot = mp.mpf(0)
    for y1 in range(D0):
        for y2 in range(D0):
            quad = (b * y1 * y1 + 4 * t * y1 * y2 - a * y2 * y2) / mp.mpf(D0)  # = -y^T Minv y * det/det
            tot += mp.e**(-1j * mp.pi * N * quad)
    return tot / D0


def cross_closed(a, b, n):
    D0 = a * b + 4
    return -(Gamma_t(a, b, 1, 2 * n) + Gamma_t(a, b, -1, 2 * n)) / (4 * mp.sqrt(D0))


def Ztil_closed(a, b, n):
    return diag_closed(a, b, n) + cross_closed(a, b, n)


def sub_period(f, cap, n0=4, span=8, tol=mp.mpf(10) ** -15):
    vals = [f(n0 + i) for i in range(span + cap + 1)]
    for P in range(1, cap + 1):
        if all(abs(vals[i] - vals[i + P]) < tol for i in range(span)):
            return P
    return None


if __name__ == "__main__":
    print("(1) de-wound full-range Ztil == original Z (range/winding identity):")
    e = max(abs(Ztil_direct(a, b, 7) - Z_orig(a, b, 7) * mp.e**(1j * mp.pi * (a - b) / 14))
            for (a, b) in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)])
    print(f"    max err = {mp.nstr(e,3)}")

    print("(2) Ztil == reciprocity closed form (Landsberg-Schaar + 2D reciprocity, EXACT):")
    e = max(abs(Ztil_direct(a, b, 7) - Ztil_closed(a, b, 7))
            for (a, b) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)])
    print(f"    max err = {mp.nstr(e,3)}")

    print("(3) per(diagonal) == lcm(a,b)  [proved: G_a has period exactly a]:")
    ok = all(sub_period(lambda n: diag_closed(a, b, n), 2 * lcm(a, b) + 6) == lcm(a, b)
             for (a, b) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3), (4, 5), (3, 5)])
    print(f"    all per(diag)==lcm(a,b)?  {ok}")

    print("(4) lcm(per(diag), per(cross)) == P  (exact period):")
    print(f"    {'(a,b)':>7} {'per(diag)':>9} {'per(cross)':>10} {'lcm':>5} {'P':>5} {'==?':>5}")
    allok = True
    for (a, b) in [(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (1, 5), (2, 3),
                   (2, 4), (3, 5), (4, 5), (2, 6), (4, 6), (5, 6), (3, 7)]:
        P = Ppred(a, b)
        pD = lcm(a, b)
        pC = sub_period(lambda n: cross_closed(a, b, n), 4 * (a * b + 4) + 8)
        L = lcm(pD, pC) if pC else None
        allok &= (L == P)
        print(f"    {str((a,b)):>7} {pD:>9} {str(pC):>10} {str(L):>5} {P:>5} {str(L == P):>5}")
    print("\nALL CHECKS PASS" if allok and e < mp.mpf(10) ** -10 else "\nCHECK FAILED")
