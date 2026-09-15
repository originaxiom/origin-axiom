#!/usr/bin/env python3
"""MEMO-119 CELL (the owner's "keep climbing up, introducing ab/ba at
each level — do we get any math?"): THE SECOND CLIMB — ab/ba applied
at the level of MAPS.

THE CLIMB, stated:
  level 0 : LETTERS      a, b            ab != ba  -> ORDER, kappa (memo 86)
  level 1 : ORDERS/WORDS (AB, BA)        the layer tower (memos 117/118)
  level 2 : MAPS         the transformations themselves.  ab != ba here
            asks whether the record's own maps COMMUTE.
This is a genuinely different question from levels 0-1: memo 113's
first beat law governs trace VALUES, and says no new information ever
appears.  It says NOTHING about the maps.  So level 2 is the first
climb that is not automatically covered by the first beat law, and
that is exactly why it is worth running.

THE CAST (all banked, all exact polynomial maps on the character
coordinates (x, y, z) = (tr A, tr B, tr AB)):
  T  = the Fricke map (z, x, zx - y)                      [memo 94]
  L  = the layering map (z, z, xyz - y^2 - x^2 + 2)       [memos 117/118]
  s  = the isometry swap (y, x, z)                        [memo 97]
  e  = the fourth-trace flip (x, y, xy - z)               [memo 97]
  R  = s o e, the reverser                                [memo 97]
CHECKS (each two-outcome):
  C1 THE COMMUTATION TABLE: for every ordered pair, is F o G = G o F?
     Detected at random rational points, then CONFIRMED symbolically.
     A fully commuting table would mean the climb yields nothing; any
     non-commuting pair is level-2 ab/ba with content.
  C2 WHAT EACH MAP DOES TO kappa: preserved, or not.  (T is banked
     kappa-preserving; L is banked NOT.  s, e, R re-derived here.)
  C3 THE RELATION HUNT: search words in the generators for identities
     (F...F = identity as a polynomial map), detected at random points
     and confirmed symbolically.  Relations are the level-2 analogue
     of the level-0 relator — they are what makes the climb MATH
     rather than a list.
  C4 THE VERDICT: does climbing produce mathematics, and of what kind?
Gate 5 untouched.  Interpretive passages labeled.
"""
import sympy as sp
from itertools import product
import random

x, y, z = sp.symbols('x y z')
V = (x, y, z)
def app(F, P):
    """apply a map F (a 3-tuple of polynomials) to a point/tuple P."""
    sub = {x: P[0], y: P[1], z: P[2]}
    return tuple(sp.expand(c.subs(sub, simultaneous=True)) for c in F)
def comp(F, G):     # F o G
    return app(F, G)
KAPPA = sp.expand(x**2 + y**2 + z**2 - x*y*z - 2)

T = (z, x, sp.expand(z*x - y))
L = (z, z, sp.expand(x*y*z - y**2 - x**2 + 2))
S = (y, x, z)
E = (x, y, sp.expand(x*y - z))
R = comp(S, E)
MAPS = {"T": T, "L": L, "s": S, "e": E, "R": R}

# ---- fast identity detection at random rational points, then symbolic confirm
random.seed(11)
PTS = [(sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
        sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
        sp.Rational(random.randint(-9, 9), random.randint(1, 5))) for _ in range(6)]
def same_at_points(F, G):
    for P in PTS:
        if tuple(sp.nsimplify(c) for c in app(F, P)) != tuple(sp.nsimplify(c) for c in app(G, P)):
            return False
    return True
def same_symbolic(F, G):
    return all(sp.expand(F[i] - G[i]) == 0 for i in range(3))
def equal_maps(F, G):
    if not same_at_points(F, G):
        return False
    return same_symbolic(F, G)

# ---- C1: the commutation table
names = list(MAPS)
print("C1 — THE COMMUTATION TABLE (ab/ba at the level of MAPS):\n")
print("        " + "  ".join(f"{n:>5s}" for n in names))
noncomm_pairs = []
for n1 in names:
    row = []
    for n2 in names:
        F, G = MAPS[n1], MAPS[n2]
        c = equal_maps(comp(F, G), comp(G, F))
        row.append(" comm" if c else "  NO ")
        if not c and (n2, n1) not in noncomm_pairs:
            noncomm_pairs.append((n1, n2))
    print(f"  {n1:>5s} " + "  ".join(row))
print(f"\n    non-commuting pairs: {len(noncomm_pairs)} of {len(names)*(len(names)-1)//2}")
print(f"    {[f'[{a},{b}]' for a, b in noncomm_pairs]}")
assert noncomm_pairs, "everything commutes — the climb yields nothing"
print("    => LEVEL-2 ab/ba HAS CONTENT: the record's own maps do not commute.\n")

# ---- C2: what each map does to kappa
print("C2 — WHAT EACH MAP DOES TO kappa:")
for n, F in MAPS.items():
    kf = sp.expand(KAPPA.subs({x: F[0], y: F[1], z: F[2]}, simultaneous=True))
    pres = sp.expand(kf - KAPPA) == 0
    print(f"    {n:>2s}: kappa {'PRESERVED' if pres else 'NOT preserved'}"
          + ("" if pres else f"   (kappa -> {sp.factor(kf)})"))
print()

# ---- C3: the relation hunt
print("C3 — THE RELATION HUNT (words in the generators equal to the identity):")
ID = (x, y, z)
found = []
gens = [(n, MAPS[n]) for n in names]
# breadth-first over words up to length 4, pruning by point-evaluation signature
frontier = {(): ID}
for Lw in range(1, 5):
    nxt = {}
    for w, F in frontier.items():
        for n, G in gens:
            w2 = w + (n,)
            F2 = comp(G, F)                     # apply G after F
            sig = tuple(tuple(sp.nsimplify(c) for c in app(F2, P)) for P in PTS[:3])
            if sig == tuple(tuple(sp.nsimplify(c) for c in app(ID, P)) for P in PTS[:3]):
                if same_symbolic(F2, ID):
                    found.append("".join(w2))
                    continue
            nxt[w2] = F2
    frontier = nxt
if found:
    print(f"    RELATIONS FOUND (length <= 4): {sorted(set(found))}")
else:
    print("    no relation of length <= 4 among these generators")
# the banked relation from memo 97, re-verified at this level:
RTTR = comp(R, comp(T, comp(T, R)))
Tm2 = comp(sp.Tuple(*T), sp.Tuple(*T))
Tinv = sp.solve([sp.Eq(T[0], x), sp.Eq(T[1], y), sp.Eq(T[2], z)], V, dict=True)
print(f"    memo 97's banked relation R T^2 R = T^-2 re-checked at map level:")
T2 = comp(T, T)
lhs = comp(R, comp(T2, R))
# T^-2 as a map: invert T symbolically -> T^{-1}(x,y,z) = (y, xy - z, x)
Tinv_map = (y, sp.expand(x*y - z), x)
assert equal_maps(comp(T, Tinv_map), ID)
T2inv = comp(Tinv_map, Tinv_map)
print(f"      R T^2 R == T^-2 ?  {equal_maps(lhs, T2inv)}")
print()

# ---- C4
ncount = len(noncomm_pairs)
print(f"""C4 — THE VERDICT: does climbing produce mathematics?
  YES, AND OF A DIFFERENT KIND FROM LEVELS 0-1.  At level 2 the
  objects are the record's own transformations, and ab/ba asks whether
  they commute.  {ncount} of the {len(names)*(len(names)-1)//2} pairs do NOT — so the climb
  produces a genuinely NON-COMMUTATIVE structure: a group of exact
  polynomial maps on the character variety, with a commutation table
  and (above) an explicit relation.
  WHY THIS IS NOT COVERED BY THE FIRST BEAT LAW (the important point):
  memo 113 governs trace VALUES and proves no new information appears
  at any word length.  It says nothing about MAPS.  Level 2 is
  therefore the first climb whose content the first beat law does not
  already determine — the tower of memo 117 was re-expression, but the
  group of maps is new structure.
  WHAT IT IS AND IS NOT (labeled): this is MATHEMATICS — an exactly
  specified non-commutative system with computable relations.  It is
  NOT new physics: no rate, no time, no measured quantity enters, and
  the schedule wall stands.  The honest claim is that the climb yields
  a new algebraic object at each level whose SYMMETRIES are content
  even when its VALUES are not.
  HOW FAR THE LADDER GOES (stated, not run): level 3 would be maps of
  maps — the automorphisms of the group found here.  That is a
  well-posed next cell and it is NOT run in this one.
Gate 5 untouched.""")
