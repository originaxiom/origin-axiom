#!/usr/bin/env python3
"""MEMO-121 CELL (the owner's "hunt the repo for it" — and the hunt
caught this bench): THE B496 REDISCOVERY, FILED — memos 117/118 and
parts of 119/120 independently re-derived a PROVED, banked arc without
citing it.  BENCH ERROR #11 (rediscovery without citation).

WHAT B496 BANKS (verbatim from frontier/B496_tm_endomorphism, verdict
PROVED, independently re-derived by the banking seat via verify_tm.py):
  T1: "the TM trace map: T(x,y,z) = (z, z, xyz - x^2 - y^2 + 2)"
  arc_verdict: "The Thue-Morse trace map (z, z, xyz - x^2 - y^2 + 2)
    and its exact kappa-factorization kappa' - 2 = (kappa-2)(x^2 + y^2
    - xyz) verified, with DEGREE GROWTH 2."
  Q1: "T_golden = (z, x, xz-y) ... verified to PRESERVE kappa exactly";
    and on kappa = -2, "one T_TM sends kappa -> 2 + 4z^2 >= 2 (over R),
    never -2 — a one-way door OFF the Markov surface (exact)."
AND WHAT THE BENCH DID: memo 117 built L : (A,B) -> (AB,BA) — which IS
the Thue-Morse substitution a->ab, b->ba — and memo 118 derived its
closed form as if new.  The overlap must be established exactly, not
asserted, and the genuinely-new residue must be separated honestly.

CHECKS:
  V1: is the bench's L IDENTICAL to B496's T1 map?  (symbolic)
  V2: is memo 118's closed form (z' = z^2 - k, k' = z^2(2-k) + k^2 - 2)
      ALGEBRAICALLY THE SAME as B496's factorization
      k' - 2 = (k-2)(x^2 + y^2 - xyz)?  (symbolic, on the kappa locus)
  V3: THE ONE GENUINELY NEW POINT — B496's ejection bound says
      kappa -> 2 + 4z^2 >= 2 "over R".  The record's OWN tower is
      COMPLEX (Eisenstein): does it obey or EVADE that bound?
  V4: the honest ledger — rediscovered vs new.
Gate 5 untouched.
"""
import sympy as sp
from fractions import Fraction as Fr

x, y, z, k = sp.symbols('x y z k')

# ---- V1: the maps
L_bench = (z, z, sp.expand(x*y*z - y**2 - x**2 + 2))      # memo 117/118
T_b496  = (z, z, sp.expand(x*y*z - x**2 - y**2 + 2))      # B496 T1, verbatim
same = all(sp.expand(L_bench[i] - T_b496[i]) == 0 for i in range(3))
print(f"V1 — bench's L vs B496's T1:  IDENTICAL = {same}")
assert same
print("     memo 117's layering map (A,B) -> (AB,BA) IS the Thue-Morse")
print("     endomorphism a->ab, b->ba, whose trace map B496 banked as PROVED.\n")

# ---- V2: the two kappa formulas
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2
k_after = sp.expand(KAPPA.subs({x: T_b496[0], y: T_b496[1], z: T_b496[2]},
                               simultaneous=True))
b496_form = sp.expand((KAPPA - 2)*(x**2 + y**2 - x*y*z) + 2)
print(f"V2a — B496's factorization reproduces the true kappa-image: "
      f"{sp.expand(k_after - b496_form) == 0}")
# the bench's (z, kappa)-only form, obtained by eliminating xyz via kappa:
bench_form = sp.expand(z**2*(2 - k) + k**2 - 2)
# substitute kappa = KAPPA and xyz = x^2+y^2+z^2-kappa-2 into B496's form
b496_in_k = sp.expand((k - 2)*(x**2 + y**2 - (x**2 + y**2 + z**2 - k - 2)) + 2)
print(f"V2b — B496's form rewritten in (z, kappa):  {sp.simplify(b496_in_k)}")
print(f"V2c — memo 118's closed form:               {sp.simplify(bench_form)}")
print(f"     ALGEBRAICALLY THE SAME: {sp.expand(b496_in_k - bench_form) == 0}")
assert sp.expand(b496_in_k - bench_form) == 0
print("     => memo 118 re-derived a banked identity in different coordinates.\n")

# ---- V3: the one genuinely new point — does the record's own tower obey
#     B496's real-case ejection bound kappa -> 2 + 4z^2 >= 2 ?
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def psub(u, v): return (u[0] - v[0], u[1] - v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
Z, O, W = (0, 0), (1, 0), (0, 1)
def mmul(P, Q):
    return ((padd(pmul(P[0][0], Q[0][0]), pmul(P[0][1], Q[1][0])),
             padd(pmul(P[0][0], Q[0][1]), pmul(P[0][1], Q[1][1]))),
            (padd(pmul(P[1][0], Q[0][0]), pmul(P[1][1], Q[1][0])),
             padd(pmul(P[1][0], Q[0][1]), pmul(P[1][1], Q[1][1]))))
def mtr(P): return padd(P[0][0], P[1][1])
def fr(a, b, c):
    t = padd(padd(pmul(a, a), pmul(b, b)), pmul(c, c))
    return psub(psub(t, pmul(pmul(a, b), c)), (2, 0))
A, B = ((O, O), (Z, O)), ((O, Z), ((0, -1), O))
tower = []
for n in range(4):
    zz = mtr(mmul(A, B)); kk = fr(mtr(A), mtr(B), zz)
    tower.append((n, zz, kk))
    A, B = mmul(A, B), mmul(B, A)
print("V3 — THE RECORD'S OWN TOWER vs B496's real-case ejection bound:")
for n, zz, kk in tower:
    print(f"     level {n}: z = {zz},  kappa = {kk}")
z1 = tower[1][1]; z1sq = pmul(z1, z1)
k2 = tower[2][2]
print(f"\n     at level 1 the tower sits EXACTLY on kappa = -2 — B496's Markov")
print(f"     surface, the very locus its Q1 studies.")
print(f"     then z_1^2 = {z1sq}  — NEGATIVE, because z_1 = {z1} is COMPLEX")
print(f"     (Eisenstein), not real.  So kappa_2 = 2 + 4 z_1^2 = {k2},")
print(f"     which is < 2: **the record's own tower EVADES B496's '>= 2 over R'**")
assert k2 == (-46, 0) and z1sq == (-12, 0)
print("     bound — not by contradicting it, but because B496's bound is stated")
print("     over the REALS while the record's arithmetic is Eisenstein.  The")
print("     'one-way door off the Markov surface' opens in a direction the real")
print("     case cannot see.\n")

print("""V4 — THE HONEST LEDGER (rediscovered vs new):
  REDISCOVERED (B496 has it, PROVED, and the bench did not cite it):
    * the map itself — memo 117's L IS B496's T1 (V1);
    * memo 118's closed form — algebraically B496's kappa-factorization
      in other coordinates (V2);
    * memo 120's "growth exponent 2" — B496's arc verdict already says
      "with DEGREE GROWTH 2";
    * memo 119's "T_golden preserves kappa, L does not" — B496's Q1
      states both, and studies the mixed semigroup <T_golden, T_TM>,
      which is memo 119's [T,L] non-commutation question.
  GENUINELY NEW (not found in B496 by this hunt):
    * THE COMPLEX EVASION (V3) — B496's ejection bound is stated over
      R; the record's own tower is Eisenstein, z_1^2 = -12 < 0, and
      lands at kappa = -46, BELOW the real floor.  B496's Q1(b) treats
      the figure-eight point under ONE TM event; this is the ITERATED
      tower from the record's own (a, b), which B496 did not run;
    * that the record's tower passes EXACTLY THROUGH kappa = -2 at
      level 1 — i.e. the object's own layering lands on B496's Markov
      surface after one step, then leaves it;
    * memo 119's involution layer (s, e, R), the full commutation
      table, and the relation (RT)^2 = id strengthening memo 97.
  THE LESSON, recorded: the owner's instruction "hunt the repo for it"
  caught a rediscovery three memos deep.  The standing rule — exhaust
  the repo before claiming — must be applied BEFORE building, not only
  before saying "we don't have".
Gate 5 untouched.""")
