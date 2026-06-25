"""B212 -- the metallic congruence/monodromy shadow, COMPUTED (chat1 flagged silver's "degenerate
S3 both sides" as assumed-by-analogy; the V210 golden pass + the V212 re-audit kept catching exactly
this). Three exact facts, all pyenv:

(1) The CONGRUENCE-GROUP shadow.  <R,L> = SL(2,Z), so its reduction mod N=m^2+4 is ALL of SL(2,Z/N)
    -- golden N=5: SL(2,F5)=2I=E8 (B206); silver N=8: SL(2,Z/8) (order 384); bronze N=13: SL(2,F13).
    This is the "shadow group" of B206.  (It is a property of the modulus, not of the individual m.)

(2) The MONODROMY ELEMENT R^mL^m mod p (p|m^2+4) is generically order 2Q(m) (B211), BUT is the
    IDENTITY exactly when m is EVEN.  So silver's R^2L^2 == I (mod 2) -- TRIVIAL, not "S3"; the "S3"
    is the <R,L> group of (1), a different object.  This corrects B210's silver line.

(3) Characterization (proved): R^mL^m == I (mod p) for a prime p|m^2+4  <=>  p|m  <=>  p=2 and m even.
    [R^mL^m = M_m^2 = [[m^2+1,m],[m,1]]; mod p with m^2 == -4 it is [[-3,m],[m,1]], which = I iff
     -3 == 1 (p|4 => p=2) and m == 0 (p|m).  p|m and p|m^2+4 => p|4 => p=2, m even.]

The HYPERBOLIC-trace-field shadow (the cusped manifold's arithmetic, the B210 analogue) is recorded in
shadow_holonomy_sage.py: golden m004 mod (sqrt-3) -> 2T=E6 (integral, full, B210); silver m136 at the
prime (1+i) is DEGENERATE in a precise COMPUTED sense -- all square-traces vanish mod (1+i) (no order-3
/ no McKay-exceptional element) -- but the holonomy is a QUATERNION ORDER over Q(i) (square-matrix
off-diagonals lie in Q(zeta_8), not Z[i]), so the literal "image group in SL(2,F2)=S3" needs the
quaternion reduction (a named residual, NOT the naive matrix reduction).

Firewall: standalone arithmetic / rep theory; McKay E6/E8 rep-theoretic, NOT physics. Nothing to CLAIMS.md.
Run: python shadow_core.py   (pyenv)
"""
import math


def Q(m):
    d = m * m + 4
    return d // math.gcd(d, 4)


def _mul(x, y, p):
    a, b, c, d = x
    e, f, g, h = y
    return ((a * e + b * g) % p, (a * f + b * h) % p, (c * e + d * g) % p, (c * f + d * h) % p)


def closure(gens, p):
    """order of <gens> in SL(2,Z/p)."""
    I = (1, 0, 0, 1)
    S, fr = {I}, [I]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                z = _mul(x, g, p)
                if z not in S:
                    S.add(z); nf.append(z)
        fr = nf
    return len(S)


def order(M, N):
    I = (1, 0, 0, 1)
    P, k = M, 1
    while P != I:
        P = _mul(P, M, N); k += 1
        if k > 20 * N * N:
            return None
    return k


R, L = (1, 1, 0, 1), (1, 0, 1, 1)


def monodromy(m):
    """R^m L^m = M_m^2 over Z (trace m^2+2)."""
    a, b, c, d = (1, m, 0, 1)
    e, f, g, h = (1, 0, m, 1)
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def congruence_group_order(m):
    return closure([R, L], m * m + 4)


def monodromy_mod(m, N):
    g = monodromy(m)
    return tuple(x % N for x in g)


def monodromy_trivial_mod2(m):
    return monodromy_mod(m, 2) == (1, 0, 0, 1)


if __name__ == "__main__":
    print("(1) congruence-group shadow <R,L> mod N=m^2+4 = SL(2,Z/N):")
    for m in range(1, 8):
        N = m * m + 4
        tag = {1: " = 2I=E8 (golden)", 2: " = SL(2,Z/8)", 3: " = SL(2,F13)"}.get(m, "")
        print(f"   m={m}: N={N:3d}  |<R,L> mod N| = {congruence_group_order(m):6d}{tag}")
    print("\n(2) monodromy element R^mL^m mod 2  +  ord mod N (=2Q):")
    for m in range(1, 9):
        N = m * m + 4
        print(f"   m={m}: R^mL^m mod2={monodromy_mod(m,2)}  triv={monodromy_trivial_mod2(m)}  "
              f"ord mod N={order(monodromy_mod(m,N),N)} (2Q={2*Q(m)})"
              f"{'   <- EVEN m: trivial' if m % 2 == 0 else ''}")
    print("\n(3) R^mL^m == I (mod p), p|m^2+4  <=>  p|m  <=>  p=2 & m even  [verify m=1..12]:")
    for m in range(1, 13):
        N = m * m + 4
        for p in range(2, N + 1):
            if N % p == 0 and all(p % i for i in range(2, p)):  # prime p | N
                assert (monodromy_mod(m, p) == (1, 0, 0, 1)) == (m % p == 0), (m, p)
    print("   verified.")
    print("ALL CHECKS PASS")
