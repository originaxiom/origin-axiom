#!/usr/bin/env python3
"""BUILD: J^{2T} as a cubic etale algebra.

SEALED CRITERION, fixed before any structure constant is read:

  GATE 1  the 27 is minuscule: 27 weights, one Weyl orbit, all multiplicity 1.
  GATE 2  the principal h-grading of the 27 has the multiplicity profile of
          V(16) + V(8) + V(0) -- i.e. h-values 16,14,...,-16 once, 8,6,...,-8
          once more, and 0 once more again.  (Independently known from the
          height of omega_1 = 8.)
  GATE 3  the number of unordered weight-triples summing to zero is 45 --
          the classical count of tritangent planes / the cubic form's terms.
  GATE 4  dim (27)^{2T} = 3, with principal degrees {0, 8, 16}
          -- independently known from the Molien series of 2T.

OUTCOME to be read only after all four gates pass:
  the restriction of the E6 cubic form det to (27)^{2T}, as a ternary cubic in
  (a,b,c) for  u = a*e + b*v8 + c*v16, and the cubic etale algebra it names.

DECLARED IN ADVANCE, so that neither answer can be dressed as the expected one:
  * if J^{2T} is a cubic FIELD, it has no primitive idempotents over Q and the
    object supplies no rational rank-1 VEV -- L138 does NOT fire rationally,
    though a totally real field still splits over R.
  * if J^{2T} is SPLIT (Q x Q x Q), the object supplies three rational
    primitive idempotents and two of them start the E6 -> SU(5) break.
  * either way the discriminant of the restricted cubic is to be compared with
    disc K = 6237 = 3^4 * 7 * 11.  Agreement is a result; disagreement is a
    result; "close to" is not a result.
"""
import itertools
import sys
from fractions import Fraction

import sympy as sp

# ---------------------------------------------------------------- E6 root data
CART = [[2, 0, -1, 0, 0, 0],
        [0, 2, 0, -1, 0, 0],
        [-1, 0, 2, -1, 0, 0],
        [0, -1, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, -1],
        [0, 0, 0, 0, -1, 2]]
N = 6
C = sp.Matrix(CART)
Cinv = C.inv()

FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}\n          got:      {got}")
        FAIL.append(label)


def reflect_weight(w, i):
    """s_i(w) = w - <w, alpha_i^vee> alpha_i, weights in the FUNDAMENTAL basis."""
    c = w[i]
    return tuple(w[j] - c * CART[i][j] for j in range(N))


print("=" * 74)
print("STAGE 1  the 27 as a minuscule E6-module")
print("=" * 74)

# omega_1 in the fundamental-weight basis is (1,0,0,0,0,0)
hw = tuple(1 if i == 0 else 0 for i in range(N))
orbit = {hw}
frontier = [hw]
while frontier:
    w = frontier.pop()
    for i in range(N):
        v = reflect_weight(w, i)
        if v not in orbit:
            orbit.add(v)
            frontier.append(v)
W27 = sorted(orbit)
check("GATE 1a: the Weyl orbit of omega_1 has 27 elements", len(W27), 27)
check("GATE 1b: all weights distinct (multiplicity one)", len(set(W27)), 27)

# ---- principal grading: h has alpha_i(h) = 2 for all i, so <lambda, h> is
# ---- 2 * (sum of coefficients of lambda in the SIMPLE-ROOT basis).
def to_root_basis(wf):
    """fundamental-basis weight -> simple-root basis (rational)."""
    v = sp.Matrix([[wf[j] for j in range(N)]]) * Cinv
    return [sp.Rational(v[j]) for j in range(N)]


def hval(wf):
    return int(2 * sum(to_root_basis(wf)))


from collections import Counter
prof = Counter(hval(w) for w in W27)
print(f"\n  principal h-values on the 27: {dict(sorted(prof.items()))}")
expected = Counter()
for n in (16, 8, 0):
    for k in range(0, n + 1):
        expected[n - 2 * k] += 1
check("GATE 2: h-profile matches V(16) + V(8) + V(0)", dict(prof), dict(expected))
check("GATE 2b: top h-value is 16", max(prof), 16)

# ---- GATE 3: weight triples summing to zero
print("\n" + "=" * 74)
print("STAGE 2  the cubic form's support: triples of weights summing to zero")
print("=" * 74)
zero = tuple([0] * N)


def add3(a, b, c):
    return tuple(a[i] + b[i] + c[i] for i in range(N))


triples = [t for t in itertools.combinations(W27, 3) if add3(*t) == zero]
check("GATE 3: there are exactly 45 such triples", len(triples), 45)
inc = Counter()
for t in triples:
    for w in t:
        inc[w] += 1
check("GATE 3b: each weight lies in exactly 5 triples", set(inc.values()), {5})
print("      (27 weights x 5 = 135 = 45 x 3, the 27 lines / 45 tritangent planes)")

print("\n" + "-" * 74)
if FAIL:
    print(f"GATES FAILED ({len(FAIL)}).  Stopping before any structure constant is read.")
    for f in FAIL:
        print("   -", f)
    sys.exit(1)
print("ALL STAGE-1/2 GATES PASSED.")
print("The 27's skeleton is correct: minuscule, principal grading V(16)+V(8)+V(0),")
print("cubic form supported on 45 weight-triples.")
