#!/usr/bin/env python3
"""B839 — is B685's non-3 denominator an artifact of expanding in h? Prereg 0bbdc9f5fcf96cb2.

Searches the SEALED family of factorial normalisations N(n) for one making N(n)*c_n have a
pure-power-of-3 denominator at EVERY computed n. Gate 5: arithmetic only.
"""
import importlib.util, math, os
from sympy import Integer, Rational, factorint

HERE = os.path.dirname(os.path.abspath(__file__))
B800 = os.path.join(os.path.dirname(HERE), "B800_habiro_integrality", "fast_expansion.py")


def coefficients(order=14):
    """Rebuild the symmetrised series from B800's OWN verified components.

    B800 computes these inline in its main() and prints them; it exposes no accessor. Rather than
    edit a banked artifact, this imports its `phihat` and `K` and repeats the symmetrisation
    Phat(h)*Phat(-h) exactly as B800's main() does -- same code path, same arithmetic.
    """
    spec = importlib.util.spec_from_file_location("b800", B800)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    from fractions import Fraction as F
    c = m.phihat(order)
    S = [m.K(0, 0)] * (order + 1)
    for i in range(order + 1):
        for j in range(order + 1 - i):
            S[i + j] = S[i + j] + c[i] * c[j].scal(F((-1) ** j))
    out = {}
    for n in range(order + 1):
        z = S[n]
        if z.a == 0 and z.b == 0:
            continue
        assert z.is_rat(), f"n={n} not rational -- the symmetrised series must land in Q"
        if z.a != 0:
            out[n] = Rational(z.a.numerator, z.a.denominator)
    return out


def dfact(k):
    r = 1
    while k > 1:
        r *= k
        k -= 2
    return r


# The SEALED family, not adjustable here.
FAMILY = {
    "n!":            lambda n: math.factorial(n),
    "(n+1)!":        lambda n: math.factorial(n + 1),
    "(2n)!":         lambda n: math.factorial(2 * n),
    "n!!":           lambda n: dfact(n),
    "(n+1)!!":       lambda n: dfact(n + 1),
    "(2n-1)!!":      lambda n: dfact(2 * n - 1) if n >= 1 else 1,
    "(n/2)!":        lambda n: math.factorial(n // 2),
    "2^n (n/2)!":    lambda n: 2 ** n * math.factorial(n // 2),
    "4^n (n/2)!":    lambda n: 4 ** n * math.factorial(n // 2),
}


def non3_denominator(x):
    """The part of the denominator coprime to 3 -- what must vanish."""
    d = Rational(x).q
    for p, e in factorint(d).items():
        if p == 3:
            d //= p ** e
    return d


def main():
    print("=" * 78)
    print("B839 — expansion artifact or object arithmetic?  Prereg 0bbdc9f5fcf96cb2")
    print("=" * 78)
    C = coefficients()
    ns = sorted(C)
    print(f"\n  coefficients from B800's exact expansion: n = {ns}")
    print(f"\n  {'n':>3}  {'non-3 denominator':>22}  factorisation")
    base = {}
    for n in ns:
        d = non3_denominator(C[n])
        base[n] = d
        print(f"  {n:>3}  {str(d):>22}  {dict(factorint(d)) if d != 1 else '-'}")

    print(f"\n  {'normalisation':16} {'clears all n?':14} first failure")
    winners = []
    for name, f in FAMILY.items():
        bad = None
        for n in ns:
            if base[n] == 1:
                continue
            N = Integer(f(n))
            if N % base[n] != 0:                  # N must ABSORB the non-3 denominator
                bad = n
                break
        ok = bad is None
        if ok:
            winners.append(name)
        print(f"  {name:16} {'YES' if ok else 'no':14} {'-' if ok else f'n={bad}'}")

    print(f"\n  VERDICT: ", end="")
    if winners:
        print(f"ARTIFACT CONFIRMED — cleared by {winners}")
        print(f"  => the non-3 content is the EXPANSION's, not the object's.")
        print(f"  => B685's 'integral away from 3' is discharged for the ARITHMETIC,")
        print(f"     CONDITIONAL on GSWZ using such a normalisation — a convention still CITED.")
    else:
        print("ARTIFACT REFUTED — no sealed-family normalisation clears the non-3 primes")
        print("  => B800's diagnosis is WRONG and B685's claim is CONTRADICTED by the only")
        print("     in-repo computation of it.")
    return winners, base


if __name__ == "__main__":
    main()
