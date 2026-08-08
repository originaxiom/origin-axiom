#!/usr/bin/env python
"""
B971 / L132 -- SECOND, INDEPENDENT ROUTE.

The first script (su5_anomaly_verdict.py) built the 27 out of SU(5) multiplets and
took the E6 -> SO(10) -> SU(5) branching pattern as CITED group theory.

This script does not.  It generates the 27 as a Weyl orbit from the E6 Cartan
matrix alone, and then:

  (A) checks  sum_lambda lambda(H) == 0  and  sum_lambda lambda(H)^3 == 0
      IDENTICALLY in all six Cartan coordinates -- i.e. for EVERY abelian
      direction in e6, not merely the three the SM picture supplies;
  (B) recovers the branchings by grading the orbit with fundamental coweights:
        - grading by alpha_1  -> the SO(10) x U(1)_psi split      (expect 16/10/1)
        - grading by (alpha_1, alpha_2) -> the SU(5) x U(1)^2 split
          with the A4 Dynkin labels read off, giving the six SU(5) pieces;
  (C) runs the same machinery on A4 (SU(5)) and A2 (SU(3)) as LIVE CONTROLS,
      where the cubic must NOT vanish.

Exact throughout (sympy).  Convention: for lambda = sum_i lambda_i omega_i and
H = sum_i h_i alpha_i^vee, lambda(H) = sum_i lambda_i h_i.  The grading by the
alpha_j-coefficient of lambda in the ROOT basis equals lambda(omega_j^vee).
"""

import json
from collections import Counter
import sympy as sp

# --------------------------------------------------------------- Cartan data
# E6, Bourbaki labelling: chain 1-3-4-5-6 with node 2 attached to node 4.
E6_EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
A4_EDGES = [(1, 2), (2, 3), (3, 4)]
A2_EDGES = [(1, 2)]


def cartan(n, edges):
    A = sp.zeros(n, n)
    for i in range(n):
        A[i, i] = 2
    for (i, j) in edges:
        A[i-1, j-1] = -1
        A[j-1, i-1] = -1
    return A


def weight_orbit(A, hw):
    """Weyl orbit of a MINUSCULE highest weight, in Dynkin-label coordinates.
    s_i(lambda)_j = lambda_j - lambda_i * A[i,j]   (simply-laced)."""
    n = A.shape[0]
    seen = {tuple(hw)}
    frontier = [tuple(hw)]
    while frontier:
        new = []
        for lam in frontier:
            for i in range(n):
                if lam[i] == 0:
                    continue
                s = tuple(lam[j] - lam[i]*A[i, j] for j in range(n))
                if s not in seen:
                    seen.add(s)
                    new.append(s)
        frontier = new
    return sorted(seen, reverse=True)


RESULT = {}
lines = []


def say(s=''):
    lines.append(s)
    print(s)


# --------------------------------------------------------------- (A) the identity
A6 = cartan(6, E6_EDGES)
W27 = weight_orbit(A6, [1, 0, 0, 0, 0, 0])       # omega_1 -> the 27
say("=" * 78)
say("(A) THE 27 AS AN E6 WEYL ORBIT -- generated from the Cartan matrix alone")
say("=" * 78)
say(f"  |orbit of omega_1| = {len(W27)}   (expect 27)")
assert len(W27) == 27

h = sp.symbols('h1:7', rational=True)
lin = sp.expand(sum(sum(sp.Integer(l)*hi for l, hi in zip(lam, h)) for lam in W27))
cub = sp.expand(sum((sum(sp.Integer(l)*hi for l, hi in zip(lam, h)))**3 for lam in W27))
say(f"  sum_lambda  lambda(H)    = {sp.simplify(lin)}")
say(f"  sum_lambda  lambda(H)^3  = {sp.simplify(cub)}")
say("  => vanishes IDENTICALLY in h1..h6: every abelian direction in e6 is")
say("     gravity- and cubic-anomaly-free on the complete 27.")
RESULT['E6_27'] = dict(orbit_size=len(W27), linear=str(sp.simplify(lin)),
                       cubic=str(sp.simplify(cub)))

# quadratic index for completeness (must be nonzero -- shows the orbit is not trivial)
quad = sp.expand(sum((sum(sp.Integer(l)*hi for l, hi in zip(lam, h)))**2 for lam in W27))
say(f"  (sanity: sum lambda(H)^2 = {sp.factor(quad)}  -- nonzero, so the orbit is live)")
RESULT['E6_27']['quadratic'] = str(sp.expand(quad))

# also the conjugate 27bar: orbit of omega_6
W27b = weight_orbit(A6, [0, 0, 0, 0, 0, 1])
say(f"  27bar (orbit of omega_6): size {len(W27b)}, weight set differs from 27? "
    f"{set(W27b) != set(W27)}  -> the 27 is COMPLEX (computed)")
RESULT['E6_27bar'] = dict(size=len(W27b), differs=bool(set(W27b) != set(W27)))

# --------------------------------------------------------------- (B) branchings
Ainv = A6.inv()


def coweight_grade(lam, j):
    """lambda(omega_j^vee) = alpha_j-coefficient of lambda in the root basis."""
    return sum(Ainv[j-1, i]*sp.Integer(lam[i]) for i in range(6))


say()
say("=" * 78)
say("(B) BRANCHINGS RECOVERED BY GRADING -- the cited pattern, now COMPUTED")
say("=" * 78)

g1 = Counter(coweight_grade(lam, 1) for lam in W27)
say("  grading by alpha_1 (removing node 1 leaves D5 = so(10)):")
for v, n in sorted(g1.items(), key=lambda kv: -kv[0]):
    say(f"     psi-grade {str(v):>6}   multiplicity {n}")
say(f"  => 27 = {sorted(g1.values(), reverse=True)} under SO(10)xU(1): "
    f"the 16 + 10 + 1 split is COMPUTED, not cited.")
# normalise the grades to the standard psi = (1, -2, 4) convention
grades = sorted(g1.items(), key=lambda kv: -kv[1])          # 16 first, then 10, then 1
scale = sp.Rational(1, 1) / (grades[0][0]) if grades[0][0] != 0 else None
say(f"  grade ratios (16 : 10 : 1) = "
    f"{[sp.nsimplify(v/grades[0][0]) for v, _ in grades]}  "
    f"-> matches psi = (1, -2, 4) up to overall scale: "
    f"{[sp.nsimplify(v/grades[0][0]) for v, _ in grades] == [sp.Integer(1), sp.Integer(-2), sp.Integer(4)]}")
RESULT['so10_grading'] = {str(v): n for v, n in g1.items()}
RESULT['so10_grade_ratios'] = [str(sp.nsimplify(v/grades[0][0])) for v, _ in grades]

# double grading -> SU(5) pieces.  Removing nodes 1 and 2 leaves A4 on nodes 3,4,5,6.
say()
say("  double grading by (alpha_1, alpha_2) -- removing nodes 1,2 leaves A4 = su(5):")
buckets = {}
for lam in W27:
    key = (coweight_grade(lam, 1), coweight_grade(lam, 2))
    buckets.setdefault(key, []).append(lam)


def a4_label(lam):
    """A4 Dynkin labels on nodes 3,4,5,6 (E6 numbering)."""
    return (lam[2], lam[3], lam[4], lam[5])


A4_NAME = {(1, 0, 0, 0): '5', (0, 0, 0, 1): '5bar', (0, 1, 0, 0): '10',
           (0, 0, 1, 0): '10bar', (0, 0, 0, 0): '1'}
say(f"     {'(psi-grade, chi-grade)':<28} {'size':>5}  highest A4 label -> irrep")
pieces = []
for key, lams in sorted(buckets.items(), key=lambda kv: (-kv[0][0], -kv[0][1])):
    # the highest weight of the A4 sub-multiplet is the unique A4-DOMINANT one
    dom = [a4_label(l) for l in lams if all(x >= 0 for x in a4_label(l))]
    assert len(dom) == 1, (key, dom)
    hi = dom[0]
    nm = A4_NAME.get(hi, f'?{hi}')
    say(f"     {str((str(key[0]), str(key[1]))):<28} {len(lams):>5}  {str(hi):<12} -> {nm}")
    pieces.append(dict(grade=[str(key[0]), str(key[1])], size=len(lams),
                       highest_a4_label=str(hi), irrep=nm))
say(f"  => SU(5) content of the omega_1 orbit: "
    f"{dict(Counter(p['irrep'] for p in pieces))}")
RESULT['su5_pieces'] = pieces
RESULT['su5_content_omega1'] = dict(Counter(p['irrep'] for p in pieces))

# The SAME grading on the omega_6 orbit -- the other member of the conjugate pair.
b2 = {}
for lam in W27b:
    b2.setdefault((coweight_grade(lam, 1), coweight_grade(lam, 2)), []).append(lam)
c2 = Counter()
for key, lams in b2.items():
    dom = [a4_label(l) for l in lams if all(x >= 0 for x in a4_label(l))]
    assert len(dom) == 1
    c2[A4_NAME.get(dom[0], f'?{dom[0]}')] += 1
say(f"  => SU(5) content of the omega_6 orbit: {dict(c2)}")
say("     The two orbits are conjugate labellings of the same 27; script 1's")
say("     convention (10 + 5 + 5bar + 5bar + 1 + 1) is one of them, and every")
say("     anomaly coefficient simply flips sign between them -- 0 either way.")
RESULT['su5_content_omega6'] = dict(c2)

# --------------------------------------------------------------- (C) controls
say()
say("=" * 78)
say("(C) MB12 CONTROLS -- the same machinery where the cubic MUST NOT vanish")
say("=" * 78)
ctrl = {}
for label, n, edges, hw in (
    ('SU(5) 5   (A4, omega_1)', 4, A4_EDGES, [1, 0, 0, 0]),
    ('SU(5) 10  (A4, omega_2)', 4, A4_EDGES, [0, 1, 0, 0]),
    ('SU(3) 3   (A2, omega_1)', 2, A2_EDGES, [1, 0]),
):
    Ac = cartan(n, edges)
    orb = weight_orbit(Ac, hw)
    hh = sp.symbols(f'k1:{n+1}', rational=True)
    L = sp.expand(sum(sum(sp.Integer(l)*x for l, x in zip(lam, hh)) for lam in orb))
    C = sp.expand(sum((sum(sp.Integer(l)*x for l, x in zip(lam, hh)))**3 for lam in orb))
    ctrl[label] = dict(size=len(orb), linear=str(sp.simplify(L)),
                       cubic_is_zero=bool(sp.simplify(C) == 0), cubic=str(sp.simplify(C)))
    say(f"  {label:<26} size {len(orb):>3}  sum lambda(H) = {sp.simplify(L)}   "
        f"cubic identically zero? {sp.simplify(C) == 0}")
say("  => the instrument can fail.  The vanishing on the 27 is a property of the")
say("     INPUT (a complete E6 multiplet), not of the test.")
RESULT['controls'] = ctrl

# --------------------------------------------------------------- (D) incompleteness
say()
say("=" * 78)
say("(D) WHAT IT TAKES TO MAKE IT NONZERO -- delete states from the 27")
say("=" * 78)
say("  Removing each SO(10)-graded block in turn, and each single weight:")
blocks = {}
for lam in W27:
    blocks.setdefault(coweight_grade(lam, 1), []).append(lam)
blk = {}
for g, lams in sorted(blocks.items(), key=lambda kv: -kv[0]):
    rest = [l for l in W27 if l not in lams]
    c = sp.expand(sum((sum(sp.Integer(x)*hi for x, hi in zip(lam, h)))**3 for lam in rest))
    ln = sp.expand(sum(sum(sp.Integer(x)*hi for x, hi in zip(lam, h)) for lam in rest))
    blk[str(g)] = dict(kept=len(rest), linear_zero=bool(sp.simplify(ln) == 0),
                       cubic_zero=bool(sp.simplify(c) == 0))
    say(f"     drop the psi-grade {str(g):>6} block ({len(lams):>2} states): "
        f"linear==0? {sp.simplify(ln) == 0}   cubic==0? {sp.simplify(c) == 0}")
nsingle = 0
for lam in W27:
    rest = [l for l in W27 if l != lam]
    ln = sp.expand(sum(sum(sp.Integer(x)*hi for x, hi in zip(l2, h)) for l2 in rest))
    if sp.simplify(ln) != 0:
        nsingle += 1
say(f"     dropping a single weight: linear condition nonzero in {nsingle}/27 cases")
RESULT['deletions'] = dict(by_so10_block=blk, single_weight_nonzero=nsingle)

with open('e6_weight_route_out.json', 'w') as f:
    json.dump(RESULT, f, indent=2)
with open('e6_weight_route_out.txt', 'w') as f:
    f.write("\n".join(lines) + "\n")
print("\n[wrote e6_weight_route_out.json + .txt]")
