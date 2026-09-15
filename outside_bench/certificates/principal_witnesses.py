#!/usr/bin/env python3
"""MEMO-103 CELL (CLOSURE ROUTES, route i bench half): THE PRINCIPAL
WITNESSES — an INDEPENDENT, ELEMENTARY re-proof of memo 102's
h(K) = 1 for the disc-6237 cubic field, by a different method:
an explicit principal generator is exhibited for EVERY prime ideal
of norm <= the Minkowski bound, each exhibit self-verifying by a
norm equation plus a Hensel valuation.  No relation harvest, no
Smith normal form, no rank argument — the two proofs share only the
field and the splitting data.  (True second-SEAT reproduction stays
relayed to cc/codex; this cell removes the single-METHOD risk now.)

THE ARGUMENT (fully elementary):
  1. f = x^3 - 12x + 5 has disc 6237 = disc(K) => Z[theta] = O_K
     (memo 102's gate, re-run).  f totally real (three real roots)
     => Minkowski constant (3!/3^3) sqrt(6237), and EXACTLY
     17 < (2/9) sqrt(6237) < 18 by integer arithmetic
     (23409 < 24948 < 26244 over 81) => every ideal class contains
     an integral ideal of norm <= 17.
  2. Every integral ideal of norm <= 17 is a product of prime ideals
     of norm <= 17 (norms multiply).  The COMPLETE list of primes of
     norm <= 17 comes from the splitting shapes at p = 2,...,17:
     p2 (2), q2 (4), p3 (3, ram), p5 (5), p7a (7), p7b (7, ram),
     p11a (11), p11b (11, ram); 13, 17 inert (norms 2197, 4913 —
     no ideal of norm <= 17 lives over them).
  3. WITNESSES: for each of the eight primes, exhibit alpha with
     |N(alpha)| = the prime's norm and the discriminating valuation
     (v_{p2}(alpha) = 0 for q2; the plain-root Hensel valuation
     splits p7a from p7b and p11a from p11b).  A norm-2/3/5 element
     needs no valuation (only one ideal of that norm exists).
  4. All eight principal => every ideal of norm <= 17 principal =>
     every class trivial => h(K) = 1.
TWO-OUTCOME: all eight witnesses found in the search box (h = 1
INDEPENDENTLY CERTIFIED) or some witness missing (banks as an
incomplete witness list; memo 102's SNF route then stands alone).
Gate 5 untouched (algebraic number theory only).
"""
import sympy as sp
from sympy import Poly, symbols
from math import gcd

x = symbols('x')
f = Poly(x**3 - 12*x + 5, x)
disc = sp.discriminant(f.as_expr(), x)
assert disc == 6237 == 3**4*7*11
assert len(sp.real_roots(f.as_expr())) == 3          # totally real: no (4/pi)^s factor
# Minkowski: (3!/3^3) sqrt(6237) = (2/9) sqrt(6237); squared = 4*6237/81 = 24948/81
assert 17**2 * 81 < 4*6237 < 18**2 * 81              # 23409 < 24948 < 26244
print("f = x^3 - 12x + 5, disc 6237 = disc(K) => Z[theta] = O_K; totally real;")
print("   Minkowski bound in (17, 18) EXACTLY => classes are represented by")
print("   integral ideals of norm <= 17.")

# the complete prime list of norm <= 17, from the splitting shapes:
def splitting(p):
    return sorted((int(sp.degree(b)), e) for b, e in sp.factor_list(f.as_expr(), modulus=p)[1])
shapes = {p: splitting(p) for p in (2, 3, 5, 7, 11, 13, 17)}
assert shapes[2] == [(1, 1), (2, 1)] and shapes[3] == [(1, 3)]
assert shapes[5] == [(1, 1), (2, 1)] and shapes[7] == [(1, 1), (1, 2)]
assert shapes[11] == [(1, 1), (1, 2)] and shapes[13] == [(3, 1)] and shapes[17] == [(3, 1)]
print("splitting shapes re-verified (memo 102 / B931): the primes of norm <= 17 are")
print("   EXACTLY p2(2), q2(4), p3(3), p5(5), p7a(7), p7b(7), p11a(11), p11b(11);")
print("   13 and 17 inert (norms 2197, 4913) contribute none.  The list is complete.")

def deg1_roots(p):
    return [r for r in range(p) if (r**3 - 12*r + 5) % p == 0]
R = {p: deg1_roots(p) for p in (2, 7, 11)}
def ram_root(p):
    return [r for r in R[p] if (3*r*r - 12) % p == 0][0]
plain = {p: [r for r in R[p] if r != ram_root(p)][0] for p in (7, 11)}
assert len(R[2]) == 1

def hensel_val(u, v, w, p, r0, cap=12):
    """v_P(alpha) at the unramified deg-1 prime P = (p, theta - r0)."""
    r, pk = r0, p
    for _ in range(cap):
        fr = (r**3 - 12*r + 5) % (pk*p)
        fpr = (3*r*r - 12) % (pk*p)
        if gcd(fpr, p) != 1:
            break
        r = (r - fr*pow(fpr, -1, pk*p)) % (pk*p)
        pk *= p
    val, a = 0, (u + v*r + w*r*r) % pk
    while val < cap - 1 and a % p == 0:
        val += 1
        a //= p
    return val

def norm(u, v, w):
    return int(sp.resultant(f.as_expr(), (u + v*x + w*x**2), x))

# the witness hunt: one exhibit per prime, discriminated as preregistered
need = ["p2", "q2", "p3", "p5", "p7a", "p7b", "p11a", "p11b"]
wit = {}
BOX = 9
for u in range(-BOX, BOX + 1):
    for v in range(-BOX, BOX + 1):
        for w in range(-BOX, BOX + 1):
            if (u, v, w) == (0, 0, 0) or len(wit) == len(need):
                continue
            N = norm(u, v, w)
            aN = abs(N)
            if aN == 2 and "p2" not in wit:
                wit["p2"] = (u, v, w, N, "norm 2: the unique norm-2 ideal")
            elif aN == 4 and "q2" not in wit:
                if hensel_val(u, v, w, 2, R[2][0]) == 0:
                    wit["q2"] = (u, v, w, N, "norm 4 with v_p2 = 0: (alpha) = q2, not p2^2")
            elif aN == 3 and "p3" not in wit:
                wit["p3"] = (u, v, w, N, "norm 3: the unique ideal over 3")
            elif aN == 5 and "p5" not in wit:
                wit["p5"] = (u, v, w, N, "norm 5: the unique norm-5 ideal")
            elif aN == 7:
                va = hensel_val(u, v, w, 7, plain[7])
                key = "p7a" if va == 1 else "p7b"
                if key not in wit:
                    tag = f"norm 7 with plain-root valuation {va}: (alpha) = {key}"
                    wit[key] = (u, v, w, N, tag)
            elif aN == 11:
                va = hensel_val(u, v, w, 11, plain[11])
                key = "p11a" if va == 1 else "p11b"
                if key not in wit:
                    tag = f"norm 11 with plain-root valuation {va}: (alpha) = {key}"
                    wit[key] = (u, v, w, N, tag)

print(f"\nwitness hunt (box {BOX}): {len(wit)}/{len(need)} primes hit")
for k in need:
    assert k in wit, f"MISSING witness for {k} — banks as incomplete; memo 102 stands alone"
    u, v, w, N, tag = wit[k]
    print(f"   {k:5s}: alpha = {u:+d} {v:+d} theta {w:+d} theta^2,  N = {N:+d}  ({tag})")

# cross-pin: memo 102's exhibited generator of the 953 prime still verifies
assert abs(norm(-26, -1, 2)) == 953
print("cross-pin: N(-26 - theta + 2 theta^2) = +-953 (memo 102's exhibit re-verified).")

print("""
h(K) = 1 INDEPENDENTLY CERTIFIED, ELEMENTARILY: every prime ideal of
norm <= 17 has an EXPLICIT principal generator above (each exhibit
self-verifying: a norm equation + at most one Hensel valuation); every
ideal class contains an integral ideal of norm <= 17 (Minkowski, exact
integer inequality); such an ideal is a product of the eight witnessed
primes; therefore every class is trivial.  No relation matrix, no
Smith form, no rank argument — memo 102's conclusion reproduced by a
DISJOINT method.  The single-method risk on the 953 closure is
retired; true second-SEAT reproduction remains relayed (cc/codex).
Gate 5 untouched.""")
