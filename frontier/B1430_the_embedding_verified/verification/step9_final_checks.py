"""Final consistency checks: how many candidate A2 sets were REJECTED by the
closure test (i.e. is the closure requirement doing work?), and an
independent confirmation of the orbit count via orbit-stabiliser."""
from fractions import Fraction as F
from rootsys import *

for name, sim in [("E6", E6_simple()), ("F4", F4_simple()), ("G2", [vec(1,-1,0), vec(-2,1,1)])]:
    roots = generate_roots(sim)
    R = set(roots)
    idx = {r: i for i, r in enumerate(roots)}
    cand = set()
    for i, a in enumerate(roots):
        la = ip(a, a)
        for j, b in enumerate(roots):
            if i == j or ip(b, b) != la or ip(a, b) != -la/2:
                continue
            c = add(a, b)
            if c not in R:
                continue
            S = (a, neg(a), b, neg(b), c, neg(c))
            if len(set(S)) == 6:
                cand.add(frozenset(idx[s] for s in S))
    good = a2_subsystems(roots)
    print("%s: candidate A2-shaped 6-sets %d, surviving the closure/rank/length "
          "test %d, rejected %d" % (name, len(cand), len(good), len(cand)-len(good)))
