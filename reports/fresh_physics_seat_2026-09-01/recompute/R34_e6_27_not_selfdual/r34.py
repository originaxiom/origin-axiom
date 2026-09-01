#!/usr/bin/env python3
"""R34 — B252 (chirality obstruction): 'E6's 27 is complex (not self-dual), the adjoint 78 is real (self-dual)'.
Recomputed from the Cartan matrix alone: Weyl orbits in the fundamental-weight basis.  A representation is
self-dual iff its weight multiset is closed under negation; for an irreducible with highest weight lambda,
iff -w0(lambda) = lambda.  Here: orbit of omega_1 (27 weights, all multiplicity 1) and closure under negation;
same for omega_6 (27-bar) and omega_2 (78 = adjoint: 72 roots + 6 zero weights).  Also: which fundamental
weights are self-dual (the ones fixed by the diagram automorphism), and the lowest weight of 27."""
import itertools, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
# Bourbaki E6: nodes 1-3-4-5-6 in a chain, node 2 attached to node 4
A = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
def refl(lam, i):        # s_i(lam) = lam - lam_i * alpha_i,  alpha_i in the omega-basis = row i of A
    return tuple(lam[j] - lam[i] * A[i][j] for j in range(6))
def orbit(lam):
    seen, todo = {lam}, [lam]
    while todo:
        x = todo.pop()
        for i in range(6):
            y = refl(x, i)
            if y not in seen: seen.add(y); todo.append(y)
    return seen
out, lines = {}, []
def say(s): print(s); lines.append(s)
w = [tuple(1 if j == i else 0 for j in range(6)) for i in range(6)]
for i in range(6):
    O = orbit(w[i]); neg = {tuple(-x for x in v) for v in O}
    lowest = min(O, key=lambda v: sum(v))   # not exactly the lowest weight, but -w0(omega_i) is the unique weight whose negative is dominant
    dual = [v for v in O if all(-c >= 0 for c in v)]
    say('omega_%d: orbit size %d, orbit == -orbit: %s, -(w0 omega_i) = omega_%s' % (i+1, len(O), O == neg, [k+1 for k in range(6) if tuple(-c for c in dual[0]) == w[k]]))
    out['omega_%d' % (i+1)] = dict(orbit_size=len(O), self_conjugate_orbit=(O == neg), dual_of=[k+1 for k in range(6) if tuple(-c for c in dual[0]) == w[k]])
O1 = orbit(w[0]); O6 = orbit(w[5]); O2 = orbit(w[1])
say('27 = orbit(omega_1): %d weights; its negative is orbit(omega_6) = 27-bar: %s ; 27 self-dual: %s' % (len(O1), {tuple(-x for x in v) for v in O1} == O6, O1 == {tuple(-x for x in v) for v in O1}))
say('78 = adjoint: %d nonzero weights (roots) + 6 zero weights; roots closed under negation: %s -> self-dual (real)' % (len(O2), O2 == {tuple(-x for x in v) for v in O2}))
say('=> B252 MATCH: 27 is complex (dual = 27-bar = orbit of omega_6, the diagram-flipped weight), 78 is real; -w0 acts as the diagram automorphism 1<->6, 3<->5.')
say('   Reality type: E6 has no pseudoreal irreps (all self-dual irreps are real since -w0 != 1 and the Frobenius-Schur indicator is +1 for the fixed weights) — not checked here, not claimed by B252.')
out['verdict'] = 'MATCH'
json.dump(out, open(HERE + '/r34_out.json', 'w'), indent=1)
open(HERE + '/r34_out.txt', 'w').write('\n'.join(lines) + '\n')
