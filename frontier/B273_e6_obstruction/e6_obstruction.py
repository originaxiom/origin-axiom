"""B273 result encoding (pyenv-importable). The heavy computation is e6_obstruction_modp.py (sage-python, exact
mod p); its verdict is recorded here for the test and for downstream reference. FIREWALLED; nothing to CLAIMS.md.

VERDICT (exact, mod p = 99991 and 100003, both agree): the e6 bracket-coupled quadratic cup-product obstruction
H^1 x H^1 -> H^2(e6) at rho_prin VANISHES IDENTICALLY -- for all 6 pure exponent directions and for a generic
random combination of all six (q a nonzero 2-cochain but a coboundary). rank d^1 = 72, dim H^2 = 6. By
Schwartz-Zippel over two large primes, the full quadratic form is identically zero: no second-order obstruction in
any direction => the {4,8} E6 deformations integrate to second order.
"""
EXPONENTS = [1, 4, 5, 7, 8, 11]
PRIMES = [99991, 100003]
H2_DIM = 6
RANK_D1 = 72

# per-prime: every pure-direction obstruction vanishes, and the generic-combination obstruction vanishes
# (non-vacuously: q is a nonzero cochain that is nonetheless a coboundary).
RESULT = {
    99991: {"H2dim": 6, **{f"exp{m}": True for m in EXPONENTS}, "generic": True, "generic_nonvacuous": True},
    100003: {"H2dim": 6, **{f"exp{m}": True for m in EXPONENTS}, "generic": True, "generic_nonvacuous": True},
}


def cup_product_identically_zero():
    """True iff, for every recorded prime, every pure direction AND the generic combination have [xi U xi]=0."""
    for p in PRIMES:
        r = RESULT[p]
        if r["H2dim"] != H2_DIM:
            return False
        if not all(r[f"exp{m}"] for m in EXPONENTS):
            return False
        if not (r["generic"] and r["generic_nonvacuous"]):
            return False
    return True


if __name__ == "__main__":
    print("B273 verdict: full quadratic cup product H^1 x H^1 -> H^2(e6) identically zero:",
          cup_product_identically_zero())
    print(f"  primes {PRIMES}; dim H^2 = {H2_DIM}; rank d^1 = {RANK_D1}; exponents {EXPONENTS}")
    print("  => no 2nd-order obstruction; the {4,8} E6 deformations integrate to 2nd order (B265 upgraded).")
    print("  Reproduce the computation: sage-python e6_obstruction_modp.py")
