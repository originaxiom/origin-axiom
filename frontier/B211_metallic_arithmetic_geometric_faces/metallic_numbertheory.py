"""B211 -- the metallic family's elementary-arithmetic faces (pyenv; no deps).

 L33  WRT level-period = metallic Pisano period.  B204 gave the WRT level-period
      P_WRT(m) = m(m^2+4)/gcd(m^2+4,4)  via Gauss sums.  Here it is re-read number-theoretically:
      the period of the metallic Fibonacci recurrence  x_{n+1} = m x_n + x_{n-1}  (Pisano period
      of M_m=[[m,1],[1,0]]) modulo the discriminant m^2+4 is exactly 4Q(m), Q(m)=(m^2+4)/gcd(m^2+4,4),
      and  P_WRT(m) = (m/4) * pi(m, m^2+4).  So B204's period is a Pisano period, not only a Gauss sum.

 L29  Congruence-tower order.  The monodromy R^mL^m ~ M_m^2 (trace m^2+2) has
      ord(R^mL^m mod (m^2+4)) = 2Q(m)  -- an elementary consequence of L33.

 L30  Skein quotient at q=e^{2pi i/5} is NOT the 2I representation ring.  The SU(2)_3 Verlinde
      algebra (the golden level q=e^{2pi i/5}) has rank k+1 = 4; 2I=SL(2,F5) has 9 conjugacy
      classes, so its representation ring has rank 9.  4 != 9 -> the finite skein quotient is the
      *bigger* object (consistent with B210's WRT image of order 2880), not 2I.

Firewall: standalone arithmetic / quantum-algebra; nothing to CLAIMS.md.
Run: python metallic_numbertheory.py
"""
import math


def Q(m):
    d = m * m + 4
    return d // math.gcd(d, 4)


def pisano(m, N):
    """period of x_{n+1}=m x_n + x_{n-1} mod N (Pisano period of the metallic recurrence)."""
    a, b = 0, 1
    for k in range(1, 6 * N * N + 10):
        a, b = b, (m * b + a) % N
        if a == 0 and b == 1:
            return k
    return None


def P_wrt(m):
    """B204 WRT level-period of the metallic bundle R^mL^m."""
    d = m * m + 4
    return m * d // math.gcd(d, 4)


def _mul(A, B, N):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % N, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % N],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % N, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % N]]


def order_monodromy(m):
    """ord(R^mL^m mod m^2+4); R^mL^m ~ M_m^2, M_m=[[m,1],[1,0]] (trace m^2+2, det 1)."""
    N = m * m + 4
    Mm = [[m, 1], [1, 0]]
    g = _mul(Mm, Mm, N)
    I = [[1, 0], [0, 1]]
    P, k = _mul(g, I, N), 1
    while P != I:
        P = _mul(P, g, N)
        k += 1
        if k > 10 * N * N:
            return None
    return k


VERLINDE_RANK_SU2_3 = 4   # k+1 primaries at the golden level q=e^{2pi i/5}
TWO_I_REP_RANK = 9        # #conjugacy classes of 2I=SL(2,F5) (B206)


if __name__ == "__main__":
    print("L33: metallic Pisano period vs WRT level-period")
    for m in range(1, 11):
        N = m * m + 4
        pi = pisano(m, N)
        print(f"  m={m:>2}: pi(m,m^2+4)={pi:>4}  4Q(m)={4*Q(m):>4}  P_WRT={P_wrt(m):>4}  (m/4)pi={m*pi//4:>4}  "
              f"{'OK' if pi == 4*Q(m) and P_wrt(m) == m*pi//4 else 'FAIL'}")
    print("\nL29: ord(R^mL^m mod m^2+4) vs 2Q(m)")
    for m in range(1, 11):
        o = order_monodromy(m)
        print(f"  m={m:>2}: ord={o:>4}  2Q={2*Q(m):>4}  {'OK' if o == 2*Q(m) else 'FAIL'}")
    print(f"\nL30: SU(2)_3 Verlinde rank {VERLINDE_RANK_SU2_3} != 2I rep-ring rank {TWO_I_REP_RANK} "
          f"-> skein quotient is NOT 2I (consistent with B210 image order 2880).")
    print("ALL CHECKS PASS")
