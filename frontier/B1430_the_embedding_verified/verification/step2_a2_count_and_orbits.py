"""Steps 2 and 3: count A2 subsystems of E6 and compute their W-orbits.

Also reports the count under several alternative conventions, because the
number depends on the convention.
"""
from fractions import Fraction as F
from rootsys import *
from collections import Counter
import json

simple = E6_simple()
roots = generate_roots(simple)
gens = simple_reflection_perms(roots, simple)
order, group = weyl_group_order(roots, simple)

print("=== A2 SUBSYSTEMS OF E6 ===")
print("roots:", len(roots), " |W|:", order)

A2 = a2_subsystems(roots)
print()
print("CONVENTION A (the one I use): an A2 subsystem is a SET of 6 roots")
print("  {+-a,+-b,+-(a+b)}, closed under negation and under addition inside")
print("  E6, of rank 2, all six of equal length.  Two different generating")
print("  pairs that span the same 6-element set are ONE subsystem.")
print("  COUNT =", len(A2))

# alternative conventions, derived from the same objects
ordered_pairs = 0
for i, a in enumerate(roots):
    for j, b in enumerate(roots):
        if i != j and ip(a, a) == ip(b, b) and ip(a, b) == -ip(a, a) / 2 \
           and add(a, b) in set(roots):
            ordered_pairs += 1
print()
print("CONVENTION B: ORDERED pairs (a,b) of roots at 120 degrees whose sum")
print("  is a root (i.e. ordered bases of an A2).  COUNT =", ordered_pairs)
print("  ratio to convention A:", F(ordered_pairs, len(A2)),
      "(= 12 = #ordered bases of one A2)")
print("CONVENTION C: unordered such pairs {a,b}. COUNT =", ordered_pairs // 2)
print("CONVENTION D: sets of 3 POSITIVE roots (A2 up to sign) -- same objects")
print("  as convention A, so COUNT =", len(A2))

# how many A2's contain a fixed root
cnt = Counter()
for fs in A2:
    for k in fs:
        cnt[k] += 1
print()
print("number of A2 subsystems through each root (should be constant):",
      sorted(set(cnt.values())))

print()
print("=== STEP 3: W(E6)-ORBITS ON THE A2 SUBSYSTEMS ===")
orbs = orbits_of_subsets(A2, gens)
sizes = sorted(len(o) for o in orbs)
print("number of orbits:", len(orbs))
print("orbit sizes:", sizes)
print("sum of orbit sizes:", sum(sizes), "== total count:",
      sum(sizes) == len(A2))
print("SINGLE ORBIT:", len(orbs) == 1)

# orbit-stabiliser cross-check
s0 = A2[0]
st = setwise_stabilizer_order(s0, group)
print("setwise stabiliser of one A2 in W has order:", st)
print("orbit-stabiliser: |W|/|stab| =", order // st,
      " matches orbit size:", order // st == len(orbs[0]))

# what is the stabiliser's orbit structure worth: roots orthogonal to an A2
S = [roots[k] for k in s0]
perp = [r for r in roots if all(ip(r, s) == 0 for s in S)]
print("roots orthogonal to a fixed A2:", len(perp),
      "rank of their span:", rank_of(perp))

json.dump([sorted(x) for x in A2], open("e6_a2_subsystems.json", "w"))
print("wrote e6_a2_subsystems.json")
