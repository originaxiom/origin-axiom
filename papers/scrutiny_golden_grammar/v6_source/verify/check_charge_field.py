#!/usr/bin/env python3
"""
Appendix B — verification of §6.1: the charge cubic mu and its field K.

Self-contained: needs only sympy. Imports NOTHING project-internal, so it
travels with the paper. Exact arithmetic throughout -- no floating point in any
verdict-bearing comparison. (The Minkowski bound is compared via an exact
integer inequality, not via its decimal value.)

Verifies, in order:
  1. mu is irreducible over Q with three real roots and Galois group S_3.
  2. K = Q[t]/mu is isomorphic to Q[x]/(x^3 - 12x - 5), by exhibiting the root.
  3. disc = 6237 = 3^4 * 7 * 11, and the reduced model is monogenic (index 1).
  4. K is totally real; unit rank 2; quadratic resolvent Q(sqrt 77).
  5. The splitting census at the primes named in the paper.
  6. Class number h = 1, by Minkowski reduction plus an explicit generator for
     every prime ideal of norm below the bound.

Run:  python3 check_charge_field.py        (exit 0 = all PASS)
"""

import sys
import itertools
import sympy as sp

t, x = sp.symbols("t x")

# The charge cubic as it arrives from the 48x48 pencil minor (B866).
MU = 500716339200 * t**3 - 159667200 * t**2 - 28224 * t + 1

# The reduced model asserted in the paper.
F = x**3 - 12 * x - 5

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"         expected: {want}")
        print(f"         got:      {got}")
        FAILURES.append(label)
    return ok


print(__doc__.strip().splitlines()[0])
print()

# ---------------------------------------------------------------- 1. mu itself
print("1. The charge cubic")
check("mu is irreducible over Q", sp.Poly(MU, t).is_irreducible, True)
check("mu has three real roots", sp.Poly(MU, t).count_roots(), 3)
# For an irreducible cubic: Galois group is S_3 iff disc is not a square.
mu_disc = sp.discriminant(MU, t)
check(
    "Galois group is S_3 (disc not a square)",
    sp.sqrt(mu_disc).is_rational,
    False,
)
print()

# ------------------------------------------------- 2. the reduced model of K
print("2. K = Q[t]/mu is Q[x]/(x^3 - 12x - 5)")
# Exhibit the root of F inside Q[t]/mu explicitly, then verify F(root) == 0
# exactly by reducing modulo mu -- no numerical evaluation anywhere.
RHO = sp.Rational(-815, 338) - sp.Rational(4934160, 169) * t \
    + sp.Rational(13039488000, 169) * t**2
residue = sp.rem(
    sp.Poly(sp.expand(RHO**3 - 12 * RHO - 5), t),
    sp.Poly(MU, t),
)
check("the exhibited rho satisfies rho^3 - 12*rho - 5 = 0 in Q[t]/mu",
      residue.is_zero, True)
check("F is irreducible over Q (so the map is an isomorphism)",
      sp.Poly(F, x).is_irreducible, True)
print()

# ------------------------------------------------- 3. discriminant, monogenic
print("3. Discriminant and integral model")
dF = sp.discriminant(F, x)
check("disc(x^3 - 12x - 5) = 6237", dF, 6237)
check("6237 = 3^4 * 7 * 11", sp.factorint(dF), {3: 4, 7: 1, 11: 1})

# disc(f) = index^2 * disc(K). In 6237 = 3^4*7*11 only 3 occurs to a power >= 2,
# so a priori index is in {1, 3, 9} and only p = 3 can divide it. Dedekind's
# criterion at 3 settles the question.
check("only p = 3 can divide the index",
      sorted(p for p, e in sp.factorint(dF).items() if e >= 2), [3])


def dedekind_is_p_maximal(poly, p):
    """Dedekind's criterion: is Z[x]/(poly) maximal at p?

    Factor fbar = prod gi^ei mod p. Put gbar = prod gi (the radical),
    hbar = fbar / gbar, lift both to monic g, h in Z[x], and set
    T = (g*h - f)/p. Then Z[x]/(f) is p-maximal iff gcd(Tbar, gbar, hbar) = 1.
    """
    fac = sp.factor_list(poly, modulus=p)[1]
    g = sp.Poly(1, x, modulus=p)
    for gi, _ in fac:
        g = g * sp.Poly(gi, x, modulus=p)
    h = sp.div(sp.Poly(poly, x, modulus=p), g)[0]
    # lift to Z with symmetric representatives, then form T over Z
    gz = sp.Poly([int(c) % p for c in g.all_coeffs()], x)
    hz = sp.Poly([int(c) % p for c in h.all_coeffs()], x)
    T = sp.Poly(sp.expand((gz * hz - sp.Poly(poly, x)).as_expr() / p), x)
    Tbar = sp.Poly(T, x, modulus=p)
    d = sp.gcd(sp.gcd(Tbar, g), h)
    return d.degree() == 0, g, h, Tbar


maximal3, g3, h3, T3 = dedekind_is_p_maximal(F, 3)
check("f factors as (x+1)^3 mod 3",
      [(sp.Poly(g, x, modulus=3).as_expr(), e)
       for g, e in sp.factor_list(F, modulus=3)[1]],
      [(x + 1, 3)])
print(f"         Dedekind data at 3: g = {g3.as_expr()}, "
      f"h = {h3.as_expr()}, T = {T3.as_expr()}")
check("Z[x]/(f) is maximal at 3 (gcd(T,g,h) is a unit)", maximal3, True)
check("hence index = 1 and disc(K) = disc(f) = 6237",
      dF if maximal3 else None, 6237)
print()

# --------------------------------------------- 4. signature, rank, resolvent
print("4. Signature, unit rank, resolvent")
r1 = sp.Poly(F, x).count_roots()
check("totally real: r1 = 3, r2 = 0", (r1, (3 - r1) // 2), (3, 0))
check("unit rank r1 + r2 - 1 = 2", r1 + (3 - r1) // 2 - 1, 2)
check("squarefree part of 6237 is 77", sp.factorint(6237 // 81), {7: 1, 11: 1})
check("6237 = 81 * 77 (so the resolvent is Q(sqrt 77))", 81 * 77, 6237)
print()

# ------------------------------------------------------- 5. splitting census
print("5. Splitting census")


def shape(p):
    """Return (residue degrees with multiplicity, ramified?) of p in K.

    Valid at every p by Dedekind's theorem, since the index is 1.
    """
    fac = sp.factor_list(F, modulus=p)[1]
    degs = sorted(sp.Poly(g, x, modulus=p).degree() for g, e in fac for _ in range(e))
    return degs, any(e > 1 for _, e in fac)


EXPECTED = {
    2: ([1, 2], False),
    3: ([1, 1, 1], True),
    5: ([1, 2], False),
    7: ([1, 1, 1], True),
    11: ([1, 1, 1], True),
    13: ([3], False),
    17: ([3], False),
    19: ([3], False),
    953: ([1, 2], False),
    1129: ([1, 2], False),
    421493: ([1, 2], False),
}
for p, want in EXPECTED.items():
    check(f"p = {p}: shape {want[0]}, ramified={want[1]}", shape(p), want)
check("exactly 3, 7, 11 ramify among the tested primes",
      sorted(p for p in EXPECTED if shape(p)[1]), [3, 7, 11])
check("the value primes 953, 1129, 421493 are partially split, not ramified",
      [shape(p) for p in (953, 1129, 421493)], [([1, 2], False)] * 3)
print()

# --------------------------------------------------------- 6. class number 1
print("6. Class number")
# Minkowski: |C| is generated by prime ideals of norm <= (n!/n^n)*sqrt|d|.
# Exact integer form: N <= M  <=>  (n^n * N)^2 <= (n!)^2 * |d|.
n, absd = 3, 6237
bound = max(N for N in range(1, 100) if (n**n * N) ** 2 <= sp.factorial(n) ** 2 * absd)
check("Minkowski bound floor is 17", bound, 17)


def norm(c0, c1, c2):
    """N_{K/Q}(c0 + c1*rho + c2*rho^2); exact, since F is monic."""
    return int(sp.resultant(sp.Poly(F, x), sp.Poly(c2 * x**2 + c1 * x + c0, x), x))


def find_generator(p, root):
    """Search for alpha of norm +-p lying in the degree-one prime (p, rho-root)."""
    R = range(-14, 15)
    for c0, c1, c2 in itertools.product(R, R, R):
        if (c0, c1, c2) == (0, 0, 0):
            continue
        if (c0 + c1 * root + c2 * root**2) % p != 0:
            continue            # not in this prime
        if abs(norm(c0, c1, c2)) == p:
            return (c0, c1, c2)
    return None


# Every degree-one prime of norm <= 17 -- i.e. every prime above 2, 3, 5, 7, 11.
generators = {}
for p in (2, 3, 5, 7, 11):
    roots = sorted({int(r) for r in sp.ground_roots(sp.Poly(F, x, modulus=p)).keys()})
    for r in roots:
        gen = find_generator(p, r)
        generators[(p, r)] = gen
        ok = gen is not None
        txt = (f"alpha = {gen[0]} + {gen[1]}*rho + {gen[2]}*rho^2, N = "
               f"{norm(*gen)}") if ok else "NO GENERATOR FOUND"
        print(f"  [{'PASS' if ok else 'FAIL'}] prime (p={p}, rho={r}) is principal: {txt}")
        if not ok:
            FAILURES.append(f"principality of (p={p}, rho={r})")

check("every degree-one prime of norm <= 17 has an explicit generator",
      all(g is not None for g in generators.values()), True)
# The only other prime of norm <= 17 is the degree-two prime above 2 (norm 4);
# it equals (2) * P_1^{-1} and is therefore principal too. 5's degree-two prime
# has norm 25 > 17, and 13, 17, 19 are inert with norm p^3 > 17.
check("no other prime ideal has norm <= 17",
      sorted({p**d for p in EXPECTED for d in shape(p)[0] if p**d <= 17}),
      [2, 3, 4, 5, 7, 11])
print("         (the norm-4 prime above 2 is (2)*P^-1 with P principal, hence principal)")
print()

# ------------------------------------------------- 7. where the 5 actually is
print("7. The 5 and the 13 are model-borne, not ramification")
# B894/C28 records "the golden 5 entering only by ramification". That is a
# statement about supp(disc mu), and disc(mu) does contain 5^2. But 5 is
# UNRAMIFIED in K: a ramified prime must divide disc(K), and 5 does not.
# The same holds for 13. Their appearance in disc(mu) is a property of the
# integral model Z[t]/mu, which is non-maximal there -- not of the field.
d_mu = sp.discriminant(MU, t)
check("disc(mu) = 2^32 * 3^10 * 5^2 * 7^3 * 11 * 13^6",
      sp.factorint(d_mu), {2: 32, 3: 10, 5: 2, 7: 3, 11: 1, 13: 6})
check("5 divides disc(mu)", d_mu % 5, 0)
check("5 does NOT divide disc(K) = 6237", 6237 % 5 != 0, True)
check("5 is unramified in K (shape [1,2])", shape(5), ([1, 2], False))
check("13 does NOT divide disc(K)", 6237 % 13 != 0, True)
check("13 is unramified in K (inert)", shape(13), ([3], False))
# The S_3 closure ramifies only at primes dividing disc(K) or disc(Q(sqrt 77)).
check("disc(Q(sqrt 77)) = 77 (since 77 = 1 mod 4)", 77 % 4, 1)
check("5 is unramified in the whole S_3 closure",
      (6237 % 5 != 0) and (77 % 5 != 0), True)
print("         => the 77 resolvent is a genuine field fact (6237 = 81*77);")
print("            'the 5 by ramification' is not -- it is model-borne.")
print()

# ------------------------------------------------------------------- verdict
print("-" * 68)
if FAILURES:
    print(f"FAIL -- {len(FAILURES)} check(s) failed:")
    for f in FAILURES:
        print(f"   - {f}")
    sys.exit(1)
print("PASS -- every claim in section 6.1 reproduces exactly.")
print("        h = 1, disc K = 6237 = 3^4*7*11, K = Q[x]/(x^3 - 12x - 5).")
sys.exit(0)
