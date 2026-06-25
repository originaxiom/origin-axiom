"""B208 -- the WRT period (B204) and the congruence shadow (B206) are the SAME arithmetic.

Both threads flow from one homological invariant of the bundle: det(gamma+I) = m^2+4 (gamma=R^m L^m).
  - B204 (Face IV, quantum): the WRT level-period P(m) = m*(m^2+4)/gcd(m^2+4,4) -- built from m^2+4.
  - B206 (Face I, arithmetic): the congruence shadow is SL(2, primes of the field Q(sqrt(m^2+4))); the
    field radicand is squarefree(m^2+4).
CONNECTION (verified here): squarefree(m^2+4) ALWAYS divides P(m) -- the period contains the field
radicand. At the GOLDEN point (m=1) the three collapse to a single prime:
    P(1) = 5  =  det(gamma+I) = m^2+4 = 5  =  disc(Q(sqrt5)) = 5  =  the McKay prime, SL(2,F5)=2I=E8.
So the quantum invariant and the arithmetic shadow are not two threads -- they are read from the same
m^2+4, and at golden it is the single number 5 (period = discriminant = McKay-E8 prime).
Firewall: standalone arithmetic / quantum-topology; nothing to CLAIMS.md. Cited by the synthesis."""
from math import gcd


def squarefree(n):
    o, f = 1, 2
    while f * f <= n:
        c = 0
        while n % f == 0:
            n //= f; c += 1
        if c % 2:
            o *= f
        f += 1
    return o * n


def wrt_period(m):                 # B204
    D = m * m + 4
    return m * D // gcd(D, 4)


def det_gamma_plus_I(m):           # = m^2+4 (gamma = R^m L^m = [[1+m^2,m],[m,1]])
    return m * m + 4


def radicand(m):                   # squarefree part of the discriminant = the field Q(sqrt .)
    return squarefree(m * m + 4)


def table(mmax=15):
    rows = []
    for m in range(1, mmax + 1):
        P, D, sf = wrt_period(m), det_gamma_plus_I(m), radicand(m)
        rows.append(dict(m=m, P=P, det=D, radicand=sf, divides=(P % sf == 0)))
    return rows


if __name__ == "__main__":
    print(f"{'m':>2} {'P(m)[B204]':>10} {'det(g+I)=m^2+4':>14} {'radicand':>9} {'radicand|P?':>11}")
    for r in table():
        print(f"{r['m']:>2} {r['P']:>10} {r['det']:>14} {r['radicand']:>9} {str(r['divides']):>11}")
    assert all(r["divides"] for r in table(200))    # the field radicand always divides the period
    print("\n=> squarefree(m^2+4) (the field radicand) ALWAYS divides the WRT period P(m).")
    print("GOLDEN collapse (m=1): P = det(gamma+I) = disc(Q(sqrt5)) = McKay prime = 5  [SL(2,F5)=2I=E8].")
    print("  Face IV (quantum period) and Face I (arithmetic shadow) are the same m^2+4; at golden, one prime 5.")
    print("ALL CHECKS PASS")
