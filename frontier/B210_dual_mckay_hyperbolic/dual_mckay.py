"""B210 -- golden's DUAL McKay structure: E8 (monodromy) and E6 (hyperbolic); and the WRT face is
NOT the congruence shadow as a group (resolved negative).

Two genuinely-uncomputed paths, run:
 (1) The metallic bundles have a COMPLEX hyperbolic invariant trace field (the cusped manifold's
     arithmetic) DISTINCT from the REAL monodromy field Q(sqrt(m^2+4)). Computed (SnapPy/sage-python,
     recorded below): golden (figure-eight, m004) = Q(sqrt-3); silver (m136) = Q(i); bronze (s464)
     degree 8 (non-arithmetic); m=4 (t03910) degree 4. So GOLDEN carries BOTH McKay-exceptional
     congruence groups:
        monodromy field Q(sqrt5)  ram. prime 5 -> SL(2,F5)=2I=E8   [B206]
        hyperbolic field Q(sqrt-3) ram. prime 3 -> SL(2,F3)=2T=E6   [NEW]
     The two McKay-exceptional congruence primes are exactly {3,5}; E7=2O is not a congruence quotient
     (B207), so neither arithmetic reaches it. Silver = degenerate prime 2 on both sides (Q(sqrt2),Q(i));
     bronze+ non-arithmetic. => golden is the unique metallic mean hitting exceptional McKay primes on
     BOTH arithmetics.
 (2) Is the WRT modular-rep image at the golden level (SU(2)_3) = 2I? NO: |<S,T>| = 2880 (SL(2,Z/20)-
     related; ord(T) gives level 20, not 5). So the quantum face is NOT the congruence shadow as a
     group -- the WRT<->shadow link is purely arithmetic (det(gamma+I)=m^2+4, B208), not a group iso.
FIREWALL: McKay/representation-theoretic E6/E8, NOT physics; nothing to CLAIMS.md."""
import numpy as np

# (1) recorded hyperbolic invariant trace fields (sage-python: M.invariant_trace_field_gens().find_field):
HYP_TRACE_FIELDS = {
    1: ("m004", "x^2-x+1", 2, "Q(sqrt-3)"),     # golden -- ramified at 3
    2: ("m136", "x^2+1", 2, "Q(i)"),            # silver -- ramified at 2
    3: ("s464", "deg 8", 8, "non-arithmetic"),
    4: ("t03910", "deg 4", 4, "non-arithmetic"),
}
MONODROMY_FIELDS = {1: ("Q(sqrt5)", 5), 2: ("Q(sqrt2)", 2), 3: ("Q(sqrt13)", 13)}


def sl2_order(p):
    return p * (p * p - 1)


def mckay_at_prime(p):
    return {2: "S3 (degenerate)", 3: "2T=E6", 5: "2I=E8"}.get(p, f"PSL(2,{p}) generic")


def wrt_image_order_su2_3():
    """|<S,T>| for the SU(2)_3 modular representation (the golden level, q=e^{2pi i/5})."""
    k = 3; n = k + 2
    a = np.arange(4)
    S = np.sqrt(2 / n) * np.sin(np.pi * np.outer(a + 1, a + 1) / n)
    h = a * (a + 2) / (4 * n)
    T = np.diag(np.exp(2j * np.pi * (h - (3 * k / (k + 2)) / 24)))
    I = np.eye(4)
    def key(M):
        return tuple(np.round(M.flatten(), 5))
    seen = {key(I): I}; frontier = [I]
    while frontier:
        nf = []
        for M in frontier:
            for g in (S, T):
                P = M @ g; kk = key(P)
                if kk not in seen:
                    seen[kk] = P; nf.append(P)
                    if len(seen) > 100000:
                        return None
        frontier = nf
    return len(seen)


if __name__ == "__main__":
    print("(1) golden's DUAL arithmetic and its two McKay-exceptional congruence shadows:")
    print(f"    monodromy  field {MONODROMY_FIELDS[1][0]:>9} ramified at {MONODROMY_FIELDS[1][1]} -> SL(2,F{MONODROMY_FIELDS[1][1]}) = {mckay_at_prime(MONODROMY_FIELDS[1][1])}")
    print(f"    hyperbolic field {'Q(sqrt-3)':>9} ramified at 3 -> SL(2,F3) = {mckay_at_prime(3)}")
    print(f"    => golden hits BOTH McKay-exceptional primes (3,5 -> E6,E8). |2T|={sl2_order(3)}, |2I|={sl2_order(5)}.")
    print(f"    E7=2O (48) not an SL(2,Fp) order: {48 not in [sl2_order(p) for p in range(2,200)]} -> excluded from both.")
    print("    silver: monodromy Q(sqrt2)(ram 2) + hyperbolic Q(i)(ram 2) -> both S3 (degenerate); bronze+ non-arith.")
    print()
    o = wrt_image_order_su2_3()
    print(f"(2) WRT modular-rep image at golden level (SU(2)_3): |<S,T>| = {o}  (2I would be 120)")
    print(f"    => {o} != 120, NOT 2I -- the quantum face is a bigger (SL(2,Z/20)-related) object;")
    print(f"       the WRT<->shadow link is arithmetic (m^2+4, B208), not a group iso.")
    assert sl2_order(3) == 24 and sl2_order(5) == 120 and 48 not in [sl2_order(p) for p in range(2, 200)]
    assert o == 2880 and o != 120
    print("ALL CHECKS PASS")
