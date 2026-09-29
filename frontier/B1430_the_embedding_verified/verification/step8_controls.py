"""Step 5 of the brief: VACUITY CONTROLS.

The same A2-subsystem counter and the same orbit routine, run on other root
systems.  If the machinery said "one orbit" everywhere it would be worthless.
"""
from fractions import Fraction as F
from rootsys import *
from collections import Counter

CASES = [
    ("A3", A3_simple(), 12, 24),
    ("D4", D4_simple(), 24, 192),
    ("B3", B3_simple(), 18, 48),
    ("F4", F4_simple(), 48, 1152),
    ("G2", [vec(1, -1, 0), vec(-2, 1, 1)], 12, 12),
    ("A2+A2 (reducible)", [vec(1, -1, 0, 0, 0, 0), vec(0, 1, -1, 0, 0, 0),
                           vec(0, 0, 0, 1, -1, 0), vec(0, 0, 0, 0, 1, -1)],
     12, 36),
]

for name, sim, _, _ in CASES:
    roots = generate_roots(sim)
    gens = simple_reflection_perms(roots, sim)
    order, group = weyl_group_order(roots, sim)
    A = cartan_matrix(sim)
    lens = sorted({ip(r, r) for r in roots})
    print("=" * 62)
    print(name)
    print("  roots:", len(roots), " rank:", rank_of(roots),
          " |W|:", order)
    print("  Cartan:", [[str(x) for x in row] for row in A])
    print("  distinct squared root lengths:", [str(x) for x in lens])
    A2 = a2_subsystems(roots)
    print("  A2 subsystems (sets of 6 roots):", len(A2))
    if A2:
        orbs = orbits_of_subsets(A2, gens)
        print("  W-orbits on them:", len(orbs),
              " sizes:", sorted(len(o) for o in orbs))
        # length of each orbit's roots, to show what separates them
        for o in sorted(orbs, key=len):
            r0 = next(iter(o))
            L = {str(ip(roots[k], roots[k])) for k in r0}
            print("     orbit size %d : root length^2 in the subsystem %s"
                  % (len(o), L))
        # stabiliser cross-check on one representative
        s0 = sorted(A2, key=lambda s: sorted(s))[0]
        st = setwise_stabilizer_order(s0, group)
        print("     orbit-stabiliser check: |W|/|stab| = %d/%d = %d"
              % (order, st, order // st))
    A2A1 = a2_a1_subsystems(roots, A2)
    print("  A2+A1 subsystems (8 roots, A1 orthogonal to the A2):", len(A2A1))
    if A2A1:
        o2 = orbits_of_subsets(A2A1, gens)
        print("  W-orbits on them:", len(o2), " sizes:",
              sorted(len(o) for o in o2))
        for o in sorted(o2, key=len):
            r0 = next(iter(o))
            L = Counter(str(ip(roots[k], roots[k])) for k in r0)
            print("     orbit size %d : length^2 multiset %s" % (len(o), dict(L)))
print("=" * 62)
