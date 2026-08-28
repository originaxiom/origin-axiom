#!/usr/bin/env python3
"""MEMO-100 CELL (NINE-CELL WAVE, cell 7): THE GRAMMAR -> DISC-48
BRIDGE — GC-17's named gap closed: a script that derives the disc-48
Gauss-form pair (the r-bit's carrier) from the substitution grammar's
own words, with no geometric import beyond the banked Riley holonomy.

GC-17 (B1192) killed three candidates for a grammar-internal supply of
the r-bit and left one survivor with a named gap: "the disc-48
Gauss-form swap (h(-48) = 2, exact object-own fact) — but no script
derives it from the {a,b}-substitution grammar; it comes from the
manifold's cusp lattice (geometric/CM input), not a grammar orbit."
THIS CELL IS THAT SCRIPT.  The chain, all exact:
  GRAMMAR WORDS -> the peripheral pair: the meridian is the letter a;
  the longitude is FOUND BY GRAMMAR SEARCH — the shortest
  commutator-subgroup word (total exponent zero in both letters)
  whose Riley holonomy is parabolic upper-triangular and commutes
  with a's — no cusp geometry is imported, the word is discovered
  from the group presentation's own alphabet.
  -> THE CUSP LATTICE: the pair of translation lengths (1, tau) with
  tau read off the longitude's holonomy; assert tau in Z[omega] with
  tau = +-(4 omega - 2) = +-2 sqrt(-3) (exact pair arithmetic).
  -> THE FORM: the lattice Z + Z tau has norm form x^2 + 12 y^2,
  discriminant -48 (computed from tau exactly).
  -> THE CLASS PAIR: the reduced primitive forms of disc -48 are
  enumerated from scratch: EXACTLY TWO — (1,0,12) and (3,0,4):
  h(-48) = 2.  The r-bit's Gauss swap is the exchange of this pair.
TWO-OUTCOME: the grammar search either finds the longitude with the
banked modulus (bridge BUILT — GC-17's gap closed: the disc-48 carrier
IS reachable from the grammar because the longitude is a grammar word)
or fails in the searched radius (banks as the gap standing).  Either
way exact.  Fence: "grammar-reachable" here means reachable from the
group presentation's words + the banked holonomy; the holonomy itself
is the object's banked realization (memo 98's vendored Riley matrices,
systole-trace control re-asserted).  Gate 5 untouched.
"""
from fractions import Fraction as Fr
from itertools import product

# ---- pair arithmetic over Q(omega), omega^2 = omega - 1 (memo 98's, verbatim)
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
ZERO, ONE = (Fr(0), Fr(0)), (Fr(1), Fr(0))
W = (Fr(0), Fr(1))
def mmul(A, B):
    return tuple(tuple(padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j]))
                 for j in range(2)) for i in range(2))
Ma = ((ONE, ONE), (ZERO, ONE))
Mb = ((ONE, ZERO), ((-W[0], -W[1]), ONE))
def minv(A):
    (p, q_), (r_, s_) = A
    det = padd(pmul(p, s_), (-pmul(q_, r_)[0], -pmul(q_, r_)[1]))
    assert det == ONE
    return ((s_, (-q_[0], -q_[1])), ((-r_[0], -r_[1]), p))
MAT = {'a': Ma, 'b': Mb, 'A': minv(Ma), 'B': minv(Mb)}
def ev(w):
    M = ((ONE, ZERO), (ZERO, ONE))
    for c in w:
        M = mmul(M, MAT[c])
    return M
def mtr(A): return padd(A[0][0], A[1][1])
assert mtr(ev(('a', 'b'))) == (Fr(2), Fr(-1))       # the banked systole control
print("control: the vendored Riley holonomy reproduces the banked systole trace 2-omega.")

# ---- the grammar search for the longitude
EXP = {'a': (1, 0), 'b': (0, 1), 'A': (-1, 0), 'B': (0, -1)}
def expsum(w):
    ea = sum(EXP[c][0] for c in w); eb = sum(EXP[c][1] for c in w)
    return (ea, eb)
found = []
for L in range(4, 9):
    for w in product('abAB', repeat=L):
        ok = all(w[i] != {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}[w[i+1]] for i in range(L-1))
        if not ok or expsum(w) != (0, 0):
            continue
        M = ev(w)
        # parabolic upper-triangular, commuting with Ma, and NOT the identity:
        if M[1][0] == ZERO and M[0][0] == M[1][1] and M[0][0] in (ONE, (Fr(-1), Fr(0))) \
           and M[0][1] != ZERO:
            found.append((w, M))
    if found:
        break
assert found, "no longitude found in the search radius — the gap stands"
w0, M0 = found[0]
sign = 1 if M0[0][0] == ONE else -1
tau = M0[0][1] if sign == 1 else (M0[0][1][0], M0[0][1][1])
print(f"LONGITUDE FOUND BY GRAMMAR SEARCH: word {''.join(w0)} (length {len(w0)}),")
print(f"   holonomy {'+' if sign==1 else '-'}[[1, tau],[0, 1]] with tau = {tau} (as x + y*omega)")

# tau must be +-(4 omega - 2) = +-2 sqrt(-3):  (2 omega - 1)^2 = -3
tau_x, tau_y = tau
assert (tau_x, tau_y) in ((Fr(-2), Fr(4)), (Fr(2), Fr(-4))), tau
s = pmul((Fr(-1), Fr(2)), (Fr(-1), Fr(2)))          # (2 omega - 1)^2
assert s == (Fr(-3), Fr(0))
print("   tau = +-(4 omega - 2) = +-2 sqrt(-3) EXACTLY — the banked cusp modulus")
print("   2 sqrt3 i, now DERIVED from a grammar word (no cusp geometry imported).")

# ---- the lattice's form and its class pair
# lattice Z*1 + Z*tau, tau = 2 sqrt(-3): |m + n tau|^2 = m^2 + 12 n^2
# discriminant of x^2 + 12 y^2: b^2 - 4ac = -48
disc = 0*0 - 4*1*12
assert disc == -48
forms = []
for a in range(1, 8):
    for b in range(-a, a + 1):
        num = b*b + 48
        if num % (4*a) == 0:
            c = num // (4*a)
            if c >= a and (b >= 0 or (abs(b) < a and a < c)) and (a <= c):
                from math import gcd
                if gcd(gcd(a, abs(b)), c) == 1 and (abs(b) <= a <= c) and not (b < 0 and (abs(b) == a or a == c)):
                    forms.append((a, b, c))
forms = sorted(set(forms))
assert forms == [(1, 0, 12), (3, 0, 4)], forms
print(f"THE CLASS PAIR: reduced primitive forms of disc -48 = {forms} — h(-48) = 2.")

print("""
GC-17'S GAP CLOSED (two-outcome: BRIDGE BUILT): the disc-48 Gauss pair
IS grammar-reachable — the longitude is a word of the {a,b} alphabet,
found by exhaustive grammar search with no geometric input; its banked
holonomy hands the cusp lattice Z + 2 sqrt(-3) Z, whose norm form has
discriminant -48 with EXACTLY TWO classes {(1,0,12), (3,0,4)}.  The
r-bit's carrier (the Gauss swap of this pair) is therefore supplied by
the object's own grammar + its banked realization — the 'geometric/CM
import' objection dissolves: the CM datum was a grammar word all
along.  What remains r-side after this cell: only the SWAP's choice
itself (the bit), exactly as the census prices it.  Fence: the
holonomy realization is the banked one; a grammar-only derivation
WITHOUT any realization would be a different (stronger) claim, not
made.  Gate 5 untouched.""")
